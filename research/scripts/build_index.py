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

Per the plan's key decisions: these files are generated, not hand-maintained. Each should be
small enough to fit entirely in an agent's context, so most "have we looked at X" queries can be
answered from the relevant index plus one or two findings/summaries files, without a full-repo
search.

Requires: pip install python-frontmatter

Usage:
    python build_index.py            # regenerate research/_index.md and analytics/_index.md
    python build_index.py --check    # exit 1 if either index is out of date or any tag/link is
                                      # invalid, without writing anything (for CI / pre-commit)
"""
import argparse
import glob
import re
import sys
from pathlib import Path

try:
    import frontmatter
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

EXCLUDE_FROM_FINDINGS = {"tags.md"}


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
        post = frontmatter.load(p)
        findings[Path(p).stem] = dict(meta=post.metadata, path=Path(p))
    return findings


def load_raw_sessions():
    """Return a list of {meta, folder, path} for every raw/*/session-notes.md."""
    sessions = []
    for p in sorted(glob.glob(str(RAW_ROOT / "*" / "session-notes.md"))):
        post = frontmatter.load(p)
        sessions.append(dict(meta=post.metadata, folder=Path(p).parent.name, path=Path(p)))
    return sessions


def load_analytics_summaries():
    """Return {topic_stem: {meta, path}} for every analytics/summaries/*.md.
    Returns {} if analytics/ doesn't exist yet in this checkout — analytics is optional."""
    summaries = {}
    for p in sorted(glob.glob(str(ANALYTICS_SUMMARIES_ROOT / "*.md"))):
        post = frontmatter.load(p)
        summaries[Path(p).stem] = dict(meta=post.metadata, path=Path(p))
    return summaries


def validate_tags(glossary):
    """Check every tag used in raw/, findings/, and analytics/summaries/ frontmatter against the
    glossary. Returns a list of (file, tag) problems."""
    problems = []
    all_files = (
        glob.glob(str(RAW_ROOT / "*" / "*.md"))
        + [str(p) for p in FINDINGS_ROOT.glob("*.md") if p.name not in EXCLUDE_FROM_FINDINGS]
        + glob.glob(str(ANALYTICS_SUMMARIES_ROOT / "*.md"))
    )
    for p in all_files:
        post = frontmatter.load(p)
        for t in post.metadata.get("tags", []):
            if t not in glossary:
                problems.append((p, t))
    return problems


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
        backing_sessions = sorted(backing[topic], key=lambda s: s["meta"].get("date", ""))
        rows.append(dict(
            topic=meta.get("title", topic),
            file=f"findings/{topic}.md",
            tags=", ".join(sorted(meta.get("tags", []))),
            components=", ".join(sorted(meta.get("related_components", []))) or "—",
            analytics=", ".join(sorted(meta.get("related_analytics", []))) or "—",
            updated=meta.get("date", ""),
            raw=", ".join(f"raw/{s['folder']}/" for s in backing_sessions) or "—",
        ))

    rows.sort(key=lambda r: r["updated"])

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

    rows.sort(key=lambda r: r["updated"])

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


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Exit 1 if either index is stale or tags/links are invalid; don't write")
    args = parser.parse_args()

    glossary = load_tag_glossary()
    findings = load_findings()
    sessions = load_raw_sessions()
    summaries = load_analytics_summaries()
    analytics_exists = ANALYTICS_ROOT.exists()

    tag_problems = validate_tags(glossary)
    link_problems = validate_index_links(findings, sessions)
    analytics_link_problems = validate_analytics_links(findings, summaries)

    new_research_content = build_index_content(findings, sessions)
    old_research_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else None

    new_analytics_content = build_analytics_index_content(summaries) if analytics_exists else None
    old_analytics_content = ANALYTICS_INDEX_FILE.read_text(encoding="utf-8") if ANALYTICS_INDEX_FILE.exists() else None

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

    if args.check:
        if new_research_content != old_research_content:
            print("❌ research/_index.md is out of date. Run without --check to regenerate.", file=sys.stderr)
            exit_code = 1
        if analytics_exists and new_analytics_content != old_analytics_content:
            print("❌ analytics/_index.md is out of date. Run without --check to regenerate.", file=sys.stderr)
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

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
