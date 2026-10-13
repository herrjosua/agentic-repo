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

RR-155: also validates research/participants.yml, the participant ID registry (see
docs/participants.md), against every quote attribution line ("> — <role>, P<nn>") in
raw/*/session-notes.md, and fails when one ID is attributed to two different people. Corrections
are honored through the registry's raw_id / raw_role / corrected_by fields; correction-*.md files
themselves are never parsed. No-op if participants.yml doesn't exist in a given checkout.

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
import datetime
import glob
import re
import sys
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

# Project tagging (see docs/projects.md): every record carries exactly one project-* tag. Findings,
# analytics summaries, and deliverables carry it in their own `tags:`; raw sessions and components
# can't (raw/ is append-only, components are generated), so theirs is assigned here instead.
PROJECTS_FILE = RESEARCH_ROOT / "projects.yml"
PROJECT_TAG_PREFIX = "project-"
CROSS_CUTTING_PROJECT = "project-cross-cutting"

# Participant registry (docs/participants.md): one global ID sequence, one entry per person.
PARTICIPANTS_FILE = RESEARCH_ROOT / "participants.yml"
PARTICIPANT_ID_RE = re.compile(r"P[0-9]{2,4}")
# A quote's attribution line in raw/*/session-notes.md: "> — <role>, P<nn>" plus an optional
# "(note)", e.g. "> — Physician, Internal Medicine, P09 (returning from v0.1)". The role may itself
# hold commas and parentheses. Only session-notes.md is scanned: correction-*.md files quote the
# wrong attribution they correct, so parsing them would bring the error back.
ATTRIBUTION_RE = re.compile(r"^>\s*—\s*(?P<role>.+?),\s*(?P<pid>P[0-9]{2,4})(?:\s*\((?P<note>[^)]*)\))?\s*$")
PARTICIPANT_TOP_KEYS = {"next_id", "sequence_baseline", "role_classes", "participants"}
PARTICIPANT_ENTRY_KEYS = {"role_class", "note", "appearances"}
PARTICIPANT_NOTES = {"unverified-sequence"}
APPEARANCE_KEYS = {"session", "role", "returning", "reserved", "raw_id", "raw_role", "corrected_by"}

EXCLUDE_FROM_FINDINGS = {"tags.md"}

# The files a raw session folder may hold: its notes and participants, plus any number of
# append-only correction files (correction-YYYY-MM-DD.md), each correcting that folder's own
# session-notes.md. Anything else is warned about so a misnamed correction isn't silently ignored.
RAW_SESSION_FILES = {"session-notes.md", "participants.md"}
CORRECTION_GLOB = "correction-*.md"

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


# SafeLoader is a runtime alias (CSafeLoader if available, else SafeLoader), so mypy can't use it as a base.
class StrictLoader(frontmatter.default_handlers.SafeLoader):  # type: ignore[valid-type,misc]
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
SKIPPED: dict[Path, str] = {}


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


class ProjectsError(Exception):
    """research/projects.yml can't be parsed or has the wrong shape."""


def load_projects():
    """Return research/projects.yml as {"projects": {id: entry}, "raw": {folder: id},
    "components": {slug: id}}, or None if the file doesn't exist in this checkout — project tagging
    is then off entirely (no tags added, nothing validated), same optional-file pattern as
    analytics/. A key listed twice in a map is an error, not a silent last-one-wins. Raises
    ProjectsError."""
    if not PROJECTS_FILE.exists():
        return None
    try:
        data = yaml.load(PROJECTS_FILE.read_text(encoding="utf-8"), Loader=StrictLoader) or {}
    except yaml.YAMLError as e:
        raise ProjectsError(f"{PROJECTS_FILE.name}: unparseable: " + " ".join(str(e).split())) from e
    if not isinstance(data, dict):
        raise ProjectsError(f"{PROJECTS_FILE.name}: expected a mapping at the top level")
    entries = data.get("projects") or []
    if not isinstance(entries, list) or not all(isinstance(p, dict) and isinstance(p.get("id"), str) for p in entries):
        raise ProjectsError(f"{PROJECTS_FILE.name}: projects must be a list of entries with a string id")
    projects = {}
    for p in entries:
        if p["id"] in projects:
            raise ProjectsError(f"{PROJECTS_FILE.name}: project {p['id']!r} is listed twice")
        projects[p["id"]] = p
    maps = {}
    for section in ("raw", "components"):
        m = data.get(section) or {}
        if not isinstance(m, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in m.items()):
            raise ProjectsError(f"{PROJECTS_FILE.name}: {section} must map names to project ids")
        maps[section] = m
    return dict(projects=projects, **maps)


def project_tags(tags):
    return [t for t in tags if t.startswith(PROJECT_TAG_PREFIX)]


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


def find_unexpected_raw_files():
    """Return every .md file in a raw session folder that isn't session-notes.md, participants.md
    or a correction-*.md file, as repo-relative paths. Nothing loads these, so they're warned
    about (never a failure) in case one is a correction with the wrong name."""
    unexpected = []
    for p in sorted(RAW_ROOT.glob("*/*.md")):
        if p.name in RAW_SESSION_FILES or p.match(CORRECTION_GLOB):
            continue
        unexpected.append(p.relative_to(REPO_ROOT))
    return unexpected


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
    for data in findings.values():
        for rel in data["meta"].get("related_analytics", []):
            stem = Path(rel).stem
            if stem not in summaries:
                problems.append(f"{data['path']}: related_analytics points at missing analytics/summaries/{stem}.md")
    for data in summaries.values():
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
    for data in findings.values():
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


def validate_projects(projects, glossary, findings, summaries, components, deliverables):
    """Check project tagging (docs/projects.md) against research/projects.yml: every project id is
    a project-* tag defined in the glossary and project-cross-cutting exists; every raw session
    folder and component is mapped to a known project, with no stale entries; and every finding,
    analytics summary, and deliverable carries exactly one known project-* tag.

    Returns (problems, unmapped). `unmapped` lists raw sessions and components that exist but
    aren't in projects.yml — the loaders already fall back to project-cross-cutting for those, so
    main() only fails on them under --check. Both are empty if projects.yml doesn't exist."""
    if projects is None:
        return [], []
    problems = []
    unmapped = []
    known = projects["projects"]
    for pid in known:
        if not pid.startswith(PROJECT_TAG_PREFIX):
            problems.append(f"{PROJECTS_FILE.name}: project id {pid!r} doesn't start with {PROJECT_TAG_PREFIX!r}")
        if pid not in glossary:
            problems.append(f"{PROJECTS_FILE.name}: project id {pid!r} isn't defined in findings/tags.md")
    if CROSS_CUTTING_PROJECT not in known:
        problems.append(f"{PROJECTS_FILE.name}: {CROSS_CUTTING_PROJECT!r} must be listed under projects")

    existing = {
        "raw": {Path(p).parent.name for p in glob.glob(str(RAW_ROOT / "*" / "session-notes.md"))},
        "components": components,
    }
    for section, names in existing.items():
        mapping = projects[section]
        for name in sorted(names - mapping.keys()):
            unmapped.append(f"{PROJECTS_FILE.name}: {section} entry {name!r} has no project")
        for name in sorted(mapping.keys() - names):
            problems.append(f"{PROJECTS_FILE.name}: {section} entry {name!r} doesn't exist")
        for name, pid in sorted(mapping.items()):
            if pid not in known:
                problems.append(f"{PROJECTS_FILE.name}: {section} entry {name!r} uses unknown project {pid!r}")

    tagged = list(findings.values()) + list(summaries.values())
    for items in deliverables.values():
        tagged += items.values()
    for data in tagged:
        tags = project_tags(data["meta"].get("tags", []) or [])
        if len(tags) != 1:
            problems.append(f"{data['path']}: needs exactly one project-* tag, has {tags or 'none'}")
        for t in tags:
            if t not in known:
                problems.append(f"{data['path']}: project tag {t!r} isn't listed in {PROJECTS_FILE.name}")
    return problems, unmapped


class ParticipantsError(Exception):
    """research/participants.yml can't be parsed or isn't a mapping."""


def load_participants():
    """Return research/participants.yml as a dict, or None if the file doesn't exist in this
    checkout — the participant check is then off entirely, same optional-file pattern as
    projects.yml. A duplicate key anywhere is an error. Raises ParticipantsError; everything
    finer-grained is reported by validate_participants()."""
    if not PARTICIPANTS_FILE.exists():
        return None
    try:
        data = yaml.load(PARTICIPANTS_FILE.read_text(encoding="utf-8"), Loader=StrictLoader) or {}
    except yaml.YAMLError as e:
        raise ParticipantsError(f"{PARTICIPANTS_FILE.name}: unparseable: " + " ".join(str(e).split())) from e
    if not isinstance(data, dict):
        raise ParticipantsError(f"{PARTICIPANTS_FILE.name}: expected a mapping at the top level")
    return data


def id_number(pid):
    return int(pid[1:])


def is_participant_id(value):
    return isinstance(value, str) and PARTICIPANT_ID_RE.fullmatch(value) is not None


def session_date(folder):
    """The YYYY-MM-DD prefix every raw session folder name starts with."""
    return folder[:10]


def load_attributions():
    """Every quote attribution line in raw/*/session-notes.md, as dicts of folder, line, role, pid
    and returning (the note starts with "returning"). correction-*.md files are never read."""
    found = []
    for p in sorted(RAW_ROOT.glob("*/session-notes.md")):
        for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            m = ATTRIBUTION_RE.match(line)
            if m:
                found.append(dict(folder=p.parent.name, line=n, role=m["role"].strip(), pid=m["pid"],
                                  returning=(m["note"] or "").strip().lower().startswith("returning")))
    return found


def _validate_participant_shape(data):
    """Shape problems in a loaded participants.yml, plus its {id: entry} map with only the
    usable entries and appearances kept, so the later checks never trip over a bad one."""
    name = PARTICIPANTS_FILE.name
    problems = []
    for key in sorted(set(data) - PARTICIPANT_TOP_KEYS):
        problems.append(f"{name}: unknown top-level key {key!r}")

    classes = data.get("role_classes")
    if not isinstance(classes, list) or not classes or not all(isinstance(c, str) for c in classes):
        problems.append(f"{name}: role_classes must be a non-empty list of strings")
        classes = []
    elif len(set(classes)) != len(classes):
        problems.append(f"{name}: role_classes lists a class twice")

    next_id = data.get("next_id")
    if not is_participant_id(next_id):
        problems.append(f"{name}: next_id must be a participant ID like P120, got {next_id!r}")
        next_id = None

    baseline = data.get("sequence_baseline")
    if baseline is not None:
        if (not isinstance(baseline, dict) or set(baseline) != {"date", "first_id"}
                or not is_participant_id(baseline.get("first_id"))
                or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", date_sort_key(baseline.get("date")))):
            problems.append(f"{name}: sequence_baseline must have exactly a YYYY-MM-DD date and a first_id")

    raw_entries = data.get("participants")
    if not isinstance(raw_entries, dict):
        problems.append(f"{name}: participants must map participant IDs to entries")
        raw_entries = {}

    entries = {}
    for pid, entry in raw_entries.items():
        where = f"{name}: {pid}"
        if not is_participant_id(pid):
            problems.append(f"{name}: {pid!r} isn't a participant ID like P09")
            continue
        if not isinstance(entry, dict):
            problems.append(f"{where}: expected a mapping")
            continue
        for key in sorted(set(entry) - PARTICIPANT_ENTRY_KEYS):
            problems.append(f"{where}: unknown key {key!r}")
        if entry.get("role_class") not in classes:
            problems.append(f"{where}: role_class {entry.get('role_class')!r} isn't in role_classes")
        if "note" in entry and entry["note"] not in PARTICIPANT_NOTES:
            problems.append(f"{where}: note must be one of {sorted(PARTICIPANT_NOTES)}, got {entry['note']!r}")
        if next_id and id_number(pid) >= id_number(next_id):
            problems.append(f"{where}: is at or above next_id {next_id}; bump next_id")
        appearances = entry.get("appearances")
        if not isinstance(appearances, list) or not appearances:
            problems.append(f"{where}: appearances must be a non-empty list")
            continue
        kept, seen = [], set()
        for i, app in enumerate(appearances):
            at = f"{where} appearance {i + 1}"
            if not isinstance(app, dict):
                problems.append(f"{at}: expected a mapping")
                continue
            bad = False
            for key in sorted(set(app) - APPEARANCE_KEYS):
                problems.append(f"{at}: unknown key {key!r}")
                bad = True
            session = app.get("session")
            if not isinstance(session, str) or not (RAW_ROOT / session / "session-notes.md").is_file():
                problems.append(f"{at}: session {session!r} isn't a raw session folder")
                continue
            at = f"{where} in {session}"
            if session in seen:
                problems.append(f"{at}: session listed twice for this ID")
                continue
            seen.add(session)
            if not isinstance(app.get("role"), str) or not app["role"].strip():
                problems.append(f"{at}: role must be a non-empty string")
                bad = True
            for flag in ("returning", "reserved"):
                if flag in app and not isinstance(app[flag], bool):
                    problems.append(f"{at}: {flag} must be true or false")
                    bad = True
            if "raw_id" in app and not is_participant_id(app["raw_id"]):
                problems.append(f"{at}: raw_id must be a participant ID, got {app['raw_id']!r}")
                bad = True
            if "raw_role" in app and (not isinstance(app["raw_role"], str) or not app["raw_role"].strip()):
                problems.append(f"{at}: raw_role must be a non-empty string")
                bad = True
            corrected_by = app.get("corrected_by")
            if ("raw_id" in app or "raw_role" in app) and corrected_by is None:
                problems.append(f"{at}: raw_id/raw_role needs corrected_by naming the correction file")
                bad = True
            if corrected_by is not None and (
                    not isinstance(corrected_by, str) or not Path(corrected_by).match(CORRECTION_GLOB)
                    or Path(corrected_by).name != corrected_by
                    or not (RAW_ROOT / session / corrected_by).is_file()):
                problems.append(f"{at}: corrected_by {corrected_by!r} isn't a correction-*.md file in that folder")
                bad = True
            if not bad:
                kept.append(app)
        entries[pid] = dict(role_class=entry.get("role_class"), note=entry.get("note"), appearances=kept)
    return problems, entries


def validate_participants(data, attributions):
    """Check research/participants.yml (docs/participants.md) against the raw attribution lines.

    Returns (errors, warnings, unregistered). errors fail build_index.py in any mode; warnings
    never fail; unregistered lists raw attributions with no registry appearance and fails only
    under --check (same split as unmapped projects). All three are empty if the file doesn't
    exist (data is None)."""
    if data is None:
        return [], [], []
    errors, entries = _validate_participant_shape(data)
    warnings, unregistered = [], []

    # (session, ID as session-notes.md writes it) -> (registry ID, appearance)
    by_raw = {}
    for pid, entry in entries.items():
        for app in entry["appearances"]:
            key = (app["session"], app.get("raw_id", pid))
            if key in by_raw:
                errors.append(f"{PARTICIPANTS_FILE.name}: {key[1]} in {key[0]} is claimed by both "
                              f"{by_raw[key][0]} and {pid}")
            by_raw[key] = (pid, app)

    # Registry <-> raw: every attribution resolves to an appearance with the same role and
    # returning marker; every appearance that isn't reserved has at least one attribution.
    quoted = set()
    label_class = {}
    for entry in entries.values():
        for app in entry["appearances"]:
            label_class.setdefault(app["role"], set()).add(entry["role_class"])
    effective = []  # one row per (ID, session): id, folder, role, returning, role_class, where
    for a in attributions:
        where = f"research/raw/{a['folder']}/session-notes.md:{a['line']}"
        hit = by_raw.get((a["folder"], a["pid"]))
        if hit is None:
            unregistered.append(f"{where}: {a['pid']} ({a['role']}) isn't in {PARTICIPANTS_FILE.name}")
            classes = label_class.get(a["role"], set())
            effective.append(dict(id=a["pid"], folder=a["folder"], role=a["role"], returning=a["returning"],
                                  role_class=next(iter(classes)) if len(classes) == 1 else None, where=where))
            continue
        pid, app = hit
        quoted.add((pid, a["folder"]))
        expected_role = app.get("raw_role", app["role"])
        if a["role"] != expected_role:
            errors.append(f"{where}: {a['pid']} is {a['role']!r} here but {expected_role!r} in "
                          f"{PARTICIPANTS_FILE.name}")
        if a["returning"] and not app.get("returning"):
            errors.append(f"{where}: {a['pid']} is marked returning here but not in {PARTICIPANTS_FILE.name}")
        if app.get("returning") and not a["returning"] and "corrected_by" not in app:
            errors.append(f"{where}: {a['pid']} is returning in {PARTICIPANTS_FILE.name} but has no "
                          "\"(returning from ...)\" marker here and no corrected_by")
    for pid, entry in entries.items():
        for app in entry["appearances"]:
            if (pid, app["session"]) not in quoted and not app.get("reserved"):
                errors.append(f"{PARTICIPANTS_FILE.name}: {pid} in {app['session']} has no attribution "
                              "line in its session-notes.md (mark it reserved: true if it's allocated "
                              "but not quoted yet)")
            effective.append(dict(id=pid, folder=app["session"], role=app["role"],
                                  returning=bool(app.get("returning")), role_class=entry["role_class"],
                                  where=f"{PARTICIPANTS_FILE.name}: {pid} in {app['session']}"))

    # Collision rules, over the registry plus any unregistered attribution.
    by_id = {}
    for row in effective:
        by_id.setdefault(row["id"], {}).setdefault(row["folder"], []).append(row)
    for pid, sessions in sorted(by_id.items(), key=lambda kv: id_number(kv[0])):
        firsts = []
        for folder, rows in sorted(sessions.items(), key=lambda kv: (session_date(kv[0]), kv[0])):
            roles = sorted({r["role"] for r in rows})
            if len(roles) > 1:
                errors.append(f"{pid} in {folder}: attributed to different roles in one session: "
                              + ", ".join(repr(r) for r in roles))
            row = dict(rows[0], returning=any(r["returning"] for r in rows),
                       role_class=next((r["role_class"] for r in rows if r["role_class"]), None))
            firsts.append(row)
        first = firsts[0]
        if first["returning"]:
            errors.append(f"{first['where']}: {pid} is marked returning, but this is its earliest session")
        for row in firsts[1:]:
            pair = f"{pid}: {first['role']!r} in {first['folder']} vs {row['role']!r} in {row['folder']}"
            if row["role"] != first["role"] and not row["returning"]:
                errors.append(f"{pair} — different role and no returning marker (two people share this ID)")
            elif (row["returning"] and row["role_class"] and first["role_class"]
                  and row["role_class"] != first["role_class"]):
                errors.append(f"{pair} — marked returning, but role class {first['role_class']} vs "
                              f"{row['role_class']}")
            elif row["returning"] and row["role"] != first["role"]:
                warnings.append(f"{pair} — returning, same role class, different role label")
            elif not row["returning"]:
                warnings.append(f"{pair} — same role in a later session with no returning marker")

    # Sequence (warn-only).
    for pid, entry in sorted(entries.items(), key=lambda kv: id_number(kv[0])):
        if entry["note"] == "unverified-sequence":
            warnings.append(f"{PARTICIPANTS_FILE.name}: {pid} is out of chronological sequence "
                            "(note: unverified-sequence); treated as new, no source in the repo to verify it")
    baseline = data.get("sequence_baseline")
    if isinstance(baseline, dict) and is_participant_id(baseline.get("first_id")):
        cutoff = date_sort_key(baseline.get("date"))
        for pid, entry in sorted(entries.items(), key=lambda kv: id_number(kv[0])):
            dates = [session_date(a["session"]) for a in entry["appearances"]]
            if dates and min(dates) > cutoff and id_number(pid) < id_number(baseline["first_id"]):
                warnings.append(f"{PARTICIPANTS_FILE.name}: {pid} first appears after {cutoff} but is "
                                f"below the baseline's first_id {baseline['first_id']}")
    return errors, warnings, unregistered


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
    for items in deliverables.values():
        for data in items.values():
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

    for items in deliverables.values():
        for data in items.values():
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
    unexpected_raw_files = find_unexpected_raw_files()
    link_problems = validate_index_links(findings, sessions)
    analytics_link_problems = validate_analytics_links(findings, summaries)
    component_link_problems = validate_component_links(findings, sessions, components)
    deliverable_findings_problems = validate_deliverable_findings_links(deliverables, findings)
    deliverable_cross_link_problems = validate_deliverable_cross_links(deliverables, findings, summaries)
    try:
        project_problems, unmapped_projects = validate_projects(
            load_projects(), glossary, findings, summaries, components, deliverables)
    except ProjectsError as e:
        project_problems, unmapped_projects = [str(e)], []
    try:
        participant_problems, participant_warnings, unregistered_participants = validate_participants(
            load_participants(), load_attributions())
    except ParticipantsError as e:
        participant_problems, participant_warnings, unregistered_participants = [str(e)], [], []

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

    # A warning only, even under --check: nothing reads these files, so they can't break anything.
    if unexpected_raw_files:
        print("⚠️  Unexpected files in raw session folders (not loaded; a correction must be named "
              "correction-YYYY-MM-DD.md):", file=sys.stderr)
        for p in unexpected_raw_files:
            print(f"   {p}", file=sys.stderr)

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

    if project_problems:
        print("⚠️  Project tagging issues (see docs/projects.md):", file=sys.stderr)
        for msg in project_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    # Unmapped raw sessions/components already export as project-cross-cutting, so a normal run
    # (what the CRUD UI reruns after every edit) only warns; --check is the strict gate.
    if unmapped_projects:
        print(f"⚠️  Not in research/projects.yml — exported as {CROSS_CUTTING_PROJECT} until mapped "
              "(see docs/projects.md):", file=sys.stderr)
        for msg in unmapped_projects:
            print(f"   {msg}", file=sys.stderr)
        if args.check:
            exit_code = 1

    if participant_problems:
        print("⚠️  Participant registry issues (see docs/participants.md):", file=sys.stderr)
        for msg in participant_problems:
            print(f"   {msg}", file=sys.stderr)
        exit_code = 1

    # Warnings only, even under --check.
    if participant_warnings:
        print("⚠️  Participant ID warnings (see docs/participants.md):", file=sys.stderr)
        for msg in participant_warnings:
            print(f"   {msg}", file=sys.stderr)

    # Like unmapped projects: a normal run (the CRUD UI reruns it after every edit) only warns,
    # so a quote can be saved before its ID is registered; --check is the strict gate.
    if unregistered_participants:
        print("⚠️  Participant IDs not in research/participants.yml (see docs/participants.md):",
              file=sys.stderr)
        for msg in unregistered_participants:
            print(f"   {msg}", file=sys.stderr)
        if args.check:
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
