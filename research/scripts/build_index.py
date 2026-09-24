#!/usr/bin/env python3
"""
build_index.py — regenerate research/_index.md from research/findings/*.md frontmatter,
cross-referenced with the raw/ sessions that back each finding, and validate every frontmatter
tag in use (across raw/, findings/, and analytics/summaries/) against the canonical glossary in
research/findings/tags.md.

Also regenerates analytics/_index.md from analytics/summaries/*.md frontmatter, and validates the
related_analytics <-> related_findings cross-references between research/findings/ and
analytics/summaries/. Per the "Still open" item resolved in the plan: analytics/quant data lives
in its own top-level analytics/ folder (raw/ + summaries/), sibling to research/ and
design-tokens/ — same rationale as design-tokens (different cadence, different source of truth).
A finding links out to a summary via related_analytics rather than analytics being a `type` value
on a finding itself, since analytics is a data source, not a research method. If analytics/
doesn't exist yet in a given checkout, everything analytics-related here is a no-op.

Also validates related_components (in raw/ and findings/) against real files in
design-tokens/components/, so a typo'd or removed component slug shows up here instead of
silently rendering as a dead reference in research/_index.md. No-op if design-tokens/components/
doesn't exist yet in a given checkout.

feature-002: also regenerates an `_index.md` inside each of the 20 top-level deliverable folders
(research-plans/, facilitation-guides/, ..., style-guide/ — see DELIVERABLE_FOLDERS) from that
folder's own *.md frontmatter, validates every deliverable's related_findings against
research/findings/, validates the type-specific cross-link fields (related_guide, related_plan,
persona_ref, flow_ref, related_wireframes, related_style_guide, based_on) against their target
folder(s), and folds every deliverable file's tags into the repo-wide tag glossary check.

Per the plan's key decisions: these files are generated, not hand-maintained. Each should be
small enough to fit entirely in an agent's context, so most "have we looked at X" queries can be
answered from the relevant index plus one or two findings/summaries files, without a full-repo
search.

Requires: pip install python-frontmatter

Usage:
    python build_index.py            # regenerate research/_index.md, analytics/_index.md, and
                                      # every deliverable folder's _index.md
    python build_index.py --check    # exit 1 if any index is out of date or any tag/link is
                                      # invalid, without writing anything (for CI / pre-commit)
"""
import argparse
import glob
import re
import sys
import datetime
from pathlib import Path

try:
    import frontmatter
    import yaml
except ImportError:
    sys.exit("This script requires python-frontmatter: pip install python-frontmatter --break-system-packages")

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_ROOT = SCRIPT_DIR.parent  # research/
REPO_ROOT = RESEARCH_ROOT.parent
RAW_ROOT = RESEARCH_ROOT / "raw"
FINDINGS_ROOT = RESEARCH_ROOT / "findings"
TAGS_FILE = FINDINGS_ROOT / "tags.md"
INDEX_FILE = RESEARCH_ROOT / "_index.md"

ANALYTICS_ROOT = REPO_ROOT / "analytics"
ANALYTICS_SUMMARIES_ROOT = ANALYTICS_ROOT / "summaries"
ANALYTICS_INDEX_FILE = ANALYTICS_ROOT / "_index.md"

COMPONENTS_ROOT = REPO_ROOT / "design-tokens" / "components"

EXCLUDE_FROM_FINDINGS = {"tags.md"}

# feature-002: the 20 top-level deliverable folders, each holding real (source_type: native) or
# stub (frontmatter + short description) files per the feature-002 spec. Indexed and validated
# the same way as research/findings/ and analytics/summaries/ — see AGENTS.md.
DELIVERABLE_FOLDERS = [
    "research-plans", "facilitation-guides", "topline-summaries", "research-readouts",
    "heuristic-evaluations", "accessibility-screenings", "service-topology", "personas",
    "mental-models", "mindsets", "journey-maps", "thumbnails", "wireframes", "user-flows",
    "wireflows", "storyboards", "mockups", "prototypes", "design-system", "style-guide",
]

# Cross-link frontmatter fields (beyond related_findings, validated separately via
# validate_deliverable_findings_links) that point at a file in another deliverable or research
# folder, and which folder(s) to resolve them against. A field's value may be a single string or
# a list of strings; each is matched by filename stem, same convention as related_findings.
DELIVERABLE_CROSS_LINK_TARGETS = {
    "related_guide": ["facilitation-guides"],
    "related_plan": ["research-plans"],
    "related_analytics": ["analytics/summaries"],
    "persona_ref": ["personas"],
    "flow_ref": ["user-flows", "wireflows"],
    "related_wireframes": ["wireframes"],
    "related_style_guide": ["style-guide"],
    "based_on": ["research-plans", "research/findings"],
}

# Frontmatter fields every script treats as a list of strings (joined, sorted, iterated as paths).
LIST_FIELDS = ("tags", "related_components", "related_findings", "related_analytics")


class StrictLoader(frontmatter.default_handlers.SafeLoader):
    """The same YAML loader python-frontmatter uses by default (CSafeLoader when available),
    plus one check: a duplicate mapping key is an error instead of silently keeping the last
    value. Everything else parses exactly as before."""

    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            if key_node.tag == "tag:yaml.org,2002:merge":
                continue
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in seen:
                    raise yaml.constructor.ConstructorError(
                        "while constructing a mapping", node.start_mark,
                        f"found duplicate key {key!r}", key_node.start_mark)
                seen.add(key)
            except TypeError:
                pass  # unhashable key — let the base constructor report it
        return super().construct_mapping(node, deep=deep)


class StrictYAMLHandler(frontmatter.YAMLHandler):
    """frontmatter.load() treats extra kwargs as metadata defaults, not loader options, so the
    loader has to be swapped in via the handler."""

    def load(self, fm, **kwargs):
        kwargs.setdefault("Loader", StrictLoader)
        return super().load(fm, **kwargs)


class RecordError(Exception):
    """A single record's frontmatter can't be parsed or has a wrong-typed field."""


# path -> reason for every record skipped this run (so --check can fail on it).
SKIPPED = {}


def load_record(path):
    """frontmatter.load() one record, rejecting duplicate keys and any LIST_FIELDS value that
    isn't a list of strings (null is normalized to []). Raises RecordError."""
    try:
        post = frontmatter.load(path, handler=StrictYAMLHandler())
    except Exception as e:
        raise RecordError("unparseable frontmatter: " + " ".join(str(e).split())) from e
    meta = post.metadata
    for field in LIST_FIELDS:
        if field not in meta:
            continue
        if meta[field] is None:
            meta[field] = []
        elif not isinstance(meta[field], list) or not all(isinstance(v, str) for v in meta[field]):
            raise RecordError(f"{field} must be a list of strings, got {meta[field]!r}")
    return post


def skip_record(path, reason):
    """Warn once on stderr that `path` is being skipped, and remember it."""
    path = Path(path)
    try:
        shown = path.resolve().relative_to(REPO_ROOT)
    except ValueError:
        shown = path
    if path.resolve() not in SKIPPED:
        SKIPPED[path.resolve()] = str(reason)
        print(f"⚠️  Skipping {shown}: {reason}", file=sys.stderr)
    return shown


def try_load_record(path):
    """load_record(), or None (with a one-line stderr warning) if the record is bad."""
    try:
        return load_record(path)
    except RecordError as e:
        skip_record(path, e)
        return None


def load_tag_glossary():
    if not TAGS_FILE.exists():
        return set()
    text = TAGS_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"\*\*`([^`]+)`\*\*", text))


def load_findings():
    """Return {topic_stem: {meta, path}} for every findings/*.md except tags.md."""
    findings = {}
    for p in sorted(glob.glob(str(FINDINGS_ROOT / "*.md"))):
        if Path(p).name in EXCLUDE_FROM_FINDINGS:
            continue
        post = try_load_record(p)
        if post is None:
            continue
        findings[Path(p).stem] = dict(meta=post.metadata, path=Path(p))
    return findings


def load_raw_sessions():
    """Return a list of {meta, folder, path} for every raw/*/session-notes.md."""
    sessions = []
    for p in sorted(glob.glob(str(RAW_ROOT / "*" / "session-notes.md"))):
        post = try_load_record(p)
        if post is None:
            continue
        sessions.append(dict(meta=post.metadata, folder=Path(p).parent.name, path=Path(p)))
    return sessions


def load_analytics_summaries():
    """Return {topic_stem: {meta, path}} for every analytics/summaries/*.md.
    Returns {} if analytics/ doesn't exist yet in this checkout — analytics is optional."""
    summaries = {}
    for p in sorted(glob.glob(str(ANALYTICS_SUMMARIES_ROOT / "*.md"))):
        post = try_load_record(p)
        if post is None:
            continue
        summaries[Path(p).stem] = dict(meta=post.metadata, path=Path(p))
    return summaries


def load_components():
    """Return the set of component stems (filename without .md) under design-tokens/components/.
    Returns an empty set if design-tokens/components/ doesn't exist yet in this checkout —
    component-reference validation is then skipped entirely (see validate_component_links)."""
    if not COMPONENTS_ROOT.exists():
        return set()
    return {Path(p).stem for p in glob.glob(str(COMPONENTS_ROOT / "*.md"))}


def load_deliverables():
    """Return {folder: {stem: {meta, path}}} for every *.md (excluding _index.md) in each of the
    20 feature-002 top-level folders. A folder missing from this checkout contributes {} for
    itself — same optional-folder pattern as analytics/ and design-tokens/components/."""
    deliverables = {}
    for folder in DELIVERABLE_FOLDERS:
        root = REPO_ROOT / folder
        items = {}
        if root.exists():
            for p in sorted(glob.glob(str(root / "*.md"))):
                if Path(p).name == "_index.md":
                    continue
                post = try_load_record(p)
                if post is None:
                    continue
                items[Path(p).stem] = dict(meta=post.metadata, path=Path(p))
        deliverables[folder] = items
    return deliverables


def validate_tags(glossary):
    """Check every tag used in raw/, findings/, analytics/summaries/, and the feature-002
    deliverable folders' frontmatter against the glossary. Returns a list of (file, tag)
    problems."""
    problems = []
    all_files = (
            glob.glob(str(RAW_ROOT / "*" / "*.md"))
            + [str(p) for p in FINDINGS_ROOT.glob("*.md") if p.name not in EXCLUDE_FROM_FINDINGS]
            + glob.glob(str(ANALYTICS_SUMMARIES_ROOT / "*.md"))
    )
    for folder in DELIVERABLE_FOLDERS:
        all_files += [str(p) for p in (REPO_ROOT / folder).glob("*.md") if p.name != "_index.md"] if (REPO_ROOT / folder).exists() else []
    for p in all_files:
        post = try_load_record(p)
        if post is None:
            continue
        for t in post.metadata.get("tags", []):
            if t not in glossary:
                problems.append((p, t))
    return problems


def date_sort_key(value):
    """Sort key for a raw frontmatter date: PyYAML gives datetime.date for unquoted dates but str
    for quoted ones (and ""/None when missing), which can't be compared directly."""
    if isinstance(value, datetime.date):  # also covers datetime.datetime
        return value.isoformat()
    return "" if value is None else str(value)


def build_index_content(findings, sessions):
    # map findings topic file -> list of backing raw session folders
    backing = {topic: [] for topic in findings}
    for s in sessions:
        for rel in s["meta"].get("related_findings", []):
            topic = Path(rel).stem
            if topic in backing:
                backing[topic].append(s)
            # silently ignore dangling references — validate_index_links() surfaces those

    rows = []
    for topic, data in findings.items():
        meta = data["meta"]

        def normalize_date(value):
            """Coerce a frontmatter date value to a plain datetime.date for sorting.
            Frontmatter dates are usually loaded as datetime.date, but gray-matter
            (used by the CRUD UI's PUT endpoint) can write a full ISO timestamp
            string or datetime.datetime instead — normalize everything to date so
            sorting never compares incompatible types again."""
            if isinstance(value, datetime.datetime):
                return value.date()
            if isinstance(value, datetime.date):
                return value
            if isinstance(value, str) and value:
                try:
                    return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).date()
                except ValueError:
                    return datetime.date.min
            return datetime.date.min

        backing_sessions = sorted(backing[topic], key=lambda s: normalize_date(s["meta"].get("date", "")))


        rows.append(dict(
            topic=meta.get("title", topic),
            file=f"findings/{topic}.md",
            tags=", ".join(sorted(meta.get("tags", []))),
            components=", ".join(sorted(meta.get("related_components", []))) or "—",
            analytics=", ".join(sorted(meta.get("related_analytics", []))) or "—",
            updated=meta.get("date", ""),
            raw=", ".join(f"raw/{s['folder']}/" for s in backing_sessions) or "—",
        ))

    rows.sort(key=lambda r: date_sort_key(r["updated"]))

    lines = [
        "# Research Index\n",
        "Maintained by `scripts/build_index.py`. Flat table: topic → tags → related components → "
        "related analytics → last updated → backing raw sessions. Small enough to fit in an "
        "agent's context in full, so most \"have we looked at X\" queries should be answerable "
        "from this file plus one or two `findings/` files, without a full-repo search.\n",
        "| Topic | Tags | Related Components | Related Analytics | Last Updated | Backing Raw Sessions |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| [{r['topic']}]({r['file']}) | {r['tags']} | {r['components']} | {r['analytics']} | {r['updated']} | {r['raw']} |")
    return "\n".join(lines) + "\n"


def build_analytics_index_content(summaries):
    rows = []
    for stem, data in summaries.items():
        meta = data["meta"]
        rows.append(dict(
            title=meta.get("title", stem),
            file=f"summaries/{stem}.md",
            tool=meta.get("tool", "—"),
            tags=", ".join(sorted(meta.get("tags", []))),
            findings=", ".join(f"../research/findings/{Path(f).name}" for f in meta.get("related_findings", [])) or "—",
            updated=meta.get("date", ""),
        ))

    rows.sort(key=lambda r: date_sort_key(r["updated"]))

    lines = [
        "# Analytics Index\n",
        "Maintained by `research/scripts/build_index.py`. Flat table of synthesized analytics "
        "summaries — quant evidence kept separate from `research/` (different cadence, different "
        "source of truth than moderated/observed research), cross-referenced with the "
        "qualitative findings each summary supports.\n",
        "| Summary | Tool | Tags | Related Findings | Last Updated |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| [{r['title']}]({r['file']}) | {r['tool']} | {r['tags']} | {r['findings']} | {r['updated']} |")
    return "\n".join(lines) + "\n"


def validate_index_links(findings, sessions):
    """Warn about raw sessions whose related_findings points at a topic file that doesn't exist,
    and findings files with zero backing raw sessions."""
    problems = []
    for s in sessions:
        for rel in s["meta"].get("related_findings", []):
            topic = Path(rel).stem
            if topic not in findings:
                problems.append(f"{s['path']}: related_findings points at missing findings/{topic}.md")
    backed = set()
    for s in sessions:
        for rel in s["meta"].get("related_findings", []):
            backed.add(Path(rel).stem)
    for topic in findings:
        if topic not in backed:
            problems.append(f"findings/{topic}.md: no raw session lists this in related_findings")
    return problems


def validate_analytics_links(findings, summaries):
    """Cross-check related_analytics (in findings/) and related_findings (in
    analytics/summaries/) both resolve to real files. Unlike raw/ sessions, a finding with zero
    related_analytics is NOT flagged — analytics is optional per finding, not every finding has
    quant data behind it."""
    problems = []
    for topic, data in findings.items():
        for rel in data["meta"].get("related_analytics", []):
            stem = Path(rel).stem
            if stem not in summaries:
                problems.append(f"{data['path']}: related_analytics points at missing analytics/summaries/{stem}.md")
    for stem, data in summaries.items():
        for rel in data["meta"].get("related_findings", []):
            topic = Path(rel).stem
            if topic not in findings:
                problems.append(f"{data['path']}: related_findings points at missing findings/{topic}.md")
    return problems


def validate_component_links(findings, sessions, components):
    """Check related_components (in raw/ sessions and findings/) resolves to a real file in
    design-tokens/components/. No-op (returns no problems) if design-tokens/components/ doesn't
    exist yet in this checkout — same optional-folder pattern as analytics."""
    problems = []
    if not COMPONENTS_ROOT.exists():
        return problems
    for topic, data in findings.items():
        for c in data["meta"].get("related_components", []) or []:
            stem = Path(c).stem
            if stem not in components:
                problems.append(f"{data['path']}: related_components references missing design-tokens/components/{stem}.md")
    for s in sessions:
        for c in s["meta"].get("related_components", []) or []:
            stem = Path(c).stem
            if stem not in components:
                problems.append(f"{s['path']}: related_components references missing design-tokens/components/{stem}.md")
    return problems


def build_deliverable_index_content(folder, items):
    rows = []
    for stem, data in items.items():
        meta = data["meta"]
        rows.append(dict(
            title=meta.get("title") or stem,
            file=f"{stem}.md",
            status=meta.get("status", "—"),
            tags=", ".join(sorted(meta.get("tags", []))) or "—",
            source_type=meta.get("source_type", "—"),
            updated=meta.get("date", ""),
            related_findings=", ".join(f"../research/findings/{Path(f).name}" for f in meta.get("related_findings", [])) or "—",
        ))

    rows.sort(key=lambda r: date_sort_key(r["updated"]))

    label = folder.replace("-", " ").title()
    lines = [
        f"# {label} Index\n",
        f"Maintained by `research/scripts/build_index.py`. Flat table of files in `{folder}/` — "
        "title, status, tags, source type, last updated, and any linked research findings.\n",
        "| Title | Status | Tags | Source Type | Last Updated | Related Findings |",
        "|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| [{r['title']}]({r['file']}) | {r['status']} | {r['tags']} | {r['source_type']} | {r['updated']} | {r['related_findings']} |")
    return "\n".join(lines) + "\n"


def validate_deliverable_findings_links(deliverables, findings):
    """Check related_findings in every deliverable folder resolves to a real findings/*.md."""
    problems = []
    for folder, items in deliverables.items():
        for stem, data in items.items():
            for rel in data["meta"].get("related_findings", []) or []:
                topic = Path(rel).stem
                if topic not in findings:
                    problems.append(f"{data['path']}: related_findings points at missing findings/{topic}.md")
    return problems


def validate_deliverable_cross_links(deliverables, findings, summaries):
    """Check the feature-002 type-specific cross-link fields (related_guide, related_plan,
    related_analytics, persona_ref, flow_ref, related_wireframes, related_style_guide, based_on)
    each resolve to a real file in their target folder(s)."""
    problems = []
    stem_sets = {folder: set(items.keys()) for folder, items in deliverables.items()}
    stem_sets["research/findings"] = set(findings.keys())
    stem_sets["analytics/summaries"] = set(summaries.keys())

    for folder, items in deliverables.items():
        for stem, data in items.items():
            meta = data["meta"]
            for field, targets in DELIVERABLE_CROSS_LINK_TARGETS.items():
                if field not in meta:
                    continue
                val = meta[field]
                vals = val if isinstance(val, list) else ([val] if val else [])
                for v in vals:
                    if not v:
                        continue
                    ref_stem = Path(v).stem
                    if not any(ref_stem in stem_sets.get(t, set()) for t in targets):
                        problems.append(f"{data['path']}: {field} references missing {v!r} (expected in {'/'.join(targets)}/)")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Exit 1 if either index is stale or tags/links are invalid; don't write")
    args = parser.parse_args()

    glossary = load_tag_glossary()
    findings = load_findings()
    sessions = load_raw_sessions()
    summaries = load_analytics_summaries()
    components = load_components()
    deliverables = load_deliverables()
    analytics_exists = ANALYTICS_ROOT.exists()

    tag_problems = validate_tags(glossary)
    link_problems = validate_index_links(findings, sessions)
    analytics_link_problems = validate_analytics_links(findings, summaries)
    component_link_problems = validate_component_links(findings, sessions, components)
    deliverable_findings_problems = validate_deliverable_findings_links(deliverables, findings)
    deliverable_cross_link_problems = validate_deliverable_cross_links(deliverables, findings, summaries)

    new_research_content = build_index_content(findings, sessions)
    old_research_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else None

    new_analytics_content = build_analytics_index_content(summaries) if analytics_exists else None
    old_analytics_content = ANALYTICS_INDEX_FILE.read_text(encoding="utf-8") if ANALYTICS_INDEX_FILE.exists() else None

    new_deliverable_contents = {}
    old_deliverable_contents = {}
    for folder in DELIVERABLE_FOLDERS:
        folder_root = REPO_ROOT / folder
        if not folder_root.exists():
            continue
        index_path = folder_root / "_index.md"
        new_deliverable_contents[folder] = build_deliverable_index_content(folder, deliverables[folder])
        old_deliverable_contents[folder] = index_path.read_text(encoding="utf-8") if index_path.exists() else None

    exit_code = 0

    if tag_problems:
        print("⚠️  Tags not in research/findings/tags.md glossary:", file=sys.stderr)
        for f, t in tag_problems:
            print(f"   {f}: {t}", file=sys.stderr)
        exit_code = 1

    if link_problems:
        print("⚠️  Cross-reference issues (research):", file=sys.stderr)
        for msg in link_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    if analytics_link_problems:
        print("⚠️  Cross-reference issues (analytics):", file=sys.stderr)
        for msg in analytics_link_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    if component_link_problems:
        print("⚠️  Cross-reference issues (components):", file=sys.stderr)
        for msg in component_link_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    if deliverable_findings_problems:
        print("⚠️  Cross-reference issues (deliverables → research/findings):", file=sys.stderr)
        for msg in deliverable_findings_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    if deliverable_cross_link_problems:
        print("⚠️  Cross-reference issues (deliverables):", file=sys.stderr)
        for msg in deliverable_cross_link_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    if args.check:
        if SKIPPED:
            exit_code = 1
        if new_research_content != old_research_content:
            print("❌ research/_index.md is out of date. Run without --check to regenerate.", file=sys.stderr)
            exit_code = 1
        if analytics_exists and new_analytics_content != old_analytics_content:
            print("❌ analytics/_index.md is out of date. Run without --check to regenerate.", file=sys.stderr)
            exit_code = 1
        for folder in new_deliverable_contents:
            if new_deliverable_contents[folder] != old_deliverable_contents[folder]:
                print(f"❌ {folder}/_index.md is out of date. Run without --check to regenerate.", file=sys.stderr)
                exit_code = 1
        sys.exit(exit_code)

    if new_research_content != old_research_content:
        INDEX_FILE.write_text(new_research_content, encoding="utf-8")
        print(f"✅ Wrote {INDEX_FILE} ({len(findings)} topics, {len(sessions)} raw sessions)")
    else:
        print(f"✅ {INDEX_FILE} already up to date ({len(findings)} topics, {len(sessions)} raw sessions)")

    if analytics_exists:
        if new_analytics_content != old_analytics_content:
            ANALYTICS_INDEX_FILE.write_text(new_analytics_content, encoding="utf-8")
            print(f"✅ Wrote {ANALYTICS_INDEX_FILE} ({len(summaries)} summaries)")
        else:
            print(f"✅ {ANALYTICS_INDEX_FILE} already up to date ({len(summaries)} summaries)")
    else:
        print("ℹ️  analytics/ doesn't exist in this checkout — skipping analytics/_index.md")

    for folder, new_content in new_deliverable_contents.items():
        index_path = REPO_ROOT / folder / "_index.md"
        if new_content != old_deliverable_contents[folder]:
            index_path.write_text(new_content, encoding="utf-8")
            print(f"✅ Wrote {index_path} ({len(deliverables[folder])} files)")
        else:
            print(f"✅ {index_path} already up to date ({len(deliverables[folder])} files)")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()