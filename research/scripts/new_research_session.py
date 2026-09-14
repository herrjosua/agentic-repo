#!/usr/bin/env python3
"""
new_research_session.py — scaffold a new raw/ research session folder, or a single deliverable
file in one of the 20 top-level folders added by feature-002 (research-plans/, personas/,
mockups/, prototypes/, etc.).

Lowers the friction for capturing raw notes (the step most likely to get skipped under
deadline pressure), per the Version Milestone Roadmap (v0.3).

Raw session mode creates:
    research/raw/<date>-<topic-slug>/session-notes.md
    research/raw/<date>-<topic-slug>/participants.md

Both are pre-filled with the repo's frontmatter schema and TODO placeholders. Never overwrites
an existing session folder — if one already exists for that date+slug, the script exits with an
error rather than clobbering notes that may already be in progress.

Usage (raw research session):
    python new_research_session.py \\
        --title "Onboarding flow usability test" \\
        --type usability-test \\
        --topic-slug onboarding-flow-usability-test \\
        --tags onboarding,usability,mobile \\
        --related-findings onboarding.md \\
        [--date 2026-09-12] \\
        [--researcher "J. Alvarez"] \\
        [--related-components onboarding-carousel,cta-primary]

Usage (feature-002 deliverable, e.g. a persona or mockup file):
    python new_research_session.py \\
        --deliverable-folder personas \\
        --title "Frontline Nurse — Ambient Scribe" \\
        --filename frontline-nurse-ambient-scribe \\
        --tags nursing,ambient-scribe \\
        --related-findings clinician-experience-documentation-burden.md \\
        --fields '{"segment": "clinical staff", "based_on": ["research-plans/some-plan.md"]}' \\
        [--status draft] [--source-type native] [--description "One or two sentence summary."]

`--deliverable-folder` switches into deliverable mode: it writes a single file into
<repo-root>/<folder>/<filename>.md using the base frontmatter (title/date/status/tags/
related_findings/source_type) plus the type-specific fields for that folder from the feature-002
spec. `--fields` takes a JSON object overriding any of that folder's type-specific defaults.
Never overwrites an existing file.

Run with --check-tags-only <tag1,tag2,...> to validate a tag list against the glossary without
creating anything.
"""
import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_ROOT = SCRIPT_DIR.parent  # research/
REPO_ROOT = RESEARCH_ROOT.parent
RAW_ROOT = RESEARCH_ROOT / "raw"
TAGS_FILE = RESEARCH_ROOT / "findings" / "tags.md"

# feature-002: the 20 top-level deliverable folders and their type-specific frontmatter fields
# (beyond the shared base block), in the order given in the feature-002 spec. Values are
# defaults; --fields JSON overrides them per-invocation.
DELIVERABLE_SCHEMAS = {
    "research-plans": [("method", ""), ("study_dates", {"start": "", "end": ""}), ("related_guide", "")],
    "facilitation-guides": [("related_plan", "")],
    "topline-summaries": [("related_plan", ""), ("session_dates", [])],
    "research-readouts": [("related_analytics", []), ("presented_to", [])],
    "heuristic-evaluations": [("method", "heuristic-evaluation"), ("evaluator", ""), ("scope", ""), ("severity_scale", "")],
    "accessibility-screenings": [("wcag_level", ""), ("scope", ""), ("issues_found", 0)],
    "service-topology": [("scope", ""), ("version", "")],
    "personas": [("segment", ""), ("based_on", [])],
    "mental-models": [("scope", "")],
    "mindsets": [("segment", "")],
    "journey-maps": [("persona_ref", ""), ("scope", "")],
    "thumbnails": [("concept", ""), ("related_wireframes", [])],
    "wireframes": [("fidelity", "lo-fi"), ("flow_ref", ""), ("source_type", "native")],
    "user-flows": [("flow_name", ""), ("screens_count", 0)],
    "wireflows": [("flow_name", "")],
    "storyboards": [("scenario", "")],
    "mockups": [("fidelity", "hi-fi"), ("source_type", "native"), ("figma_url", "")],
    "prototypes": [("type", "clickthrough"), ("source_type", "figma-link"), ("url", ""), ("stack", "")],
    "design-system": [("version", ""), ("related_style_guide", "")],
    "style-guide": [("version", "")],
}

# Only prototypes/ is stub-only by design (no real file to duplicate into the repo for a
# click-through or coded prototype) — see feature-002 spec §5.
STUB_ONLY_FOLDERS = {"prototypes"}

# Extended beyond the draft plan's 5-value example enum (usability-test | interview | survey |
# analytics | synthesis) to cover contextual inquiry and accessibility audits, which this org
# actually runs. `synthesis` is deliberately excluded here — that type belongs to findings/, not
# raw/ sessions. See docs/README.md for the full note on this deviation from the original plan.
VALID_TYPES = [
    "usability-test",
    "interview",
    "survey",
    "contextual-inquiry",
    "accessibility-audit",
    "analytics",
]


def load_tag_glossary():
    """Return the set of canonical tags defined in findings/tags.md."""
    if not TAGS_FILE.exists():
        return set()
    text = TAGS_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"\*\*`([^`]+)`\*\*", text))


def check_tags(tags, glossary):
    """Print a warning for any tag not in the glossary. Never blocks creation — new tags are
    allowed, but the person should notice and add a glossary entry deliberately rather than by
    accident (per the plan's tag-drift concern: onboarding vs first-run vs first-time-user)."""
    unknown = [t for t in tags if t not in glossary]
    if unknown:
        print(
            f"⚠️  Tag(s) not in research/findings/tags.md yet: {', '.join(unknown)}\n"
            f"   Add a glossary entry for each, or use an existing tag instead, to avoid drift.",
            file=sys.stderr,
        )
    return unknown


def fm_block(fields):
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, dict):
            lines.append(f"{k}:")
            for sub_k, sub_v in v.items():
                lines.append(f"  {sub_k}: {sub_v}")
        elif isinstance(v, list):
            lines.append(f"{k}:")
            if v:
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines[-1] = f"{k}: []"
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def yaml_str(s):
    if any(c in s for c in [":", "#", '"']) or s != s.strip():
        return '"' + s.replace('"', '\\"') + '"'
    return s


def session_notes_template(title, date, rtype, tags, related_components, related_findings, researcher, method_label):
    fm_fields = {
        "title": yaml_str(title),
        "date": date,
        "type": rtype,
        "status": "raw",
        "tags": tags,
        "related_components": related_components,
        "related_findings": related_findings,
    }
    body = f"""# {title}

## Objective
TODO: one paragraph — why this session happened, what question it was meant to answer.

## Method
- **Method:** {method_label or "TODO: e.g. Moderated usability test, 5 task scenarios, 45 min/session"}
- **Researcher:** {researcher or "TODO"}
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[SEVERITY]** *(theme)* TODO — one finding per bullet, tag severity as CRITICAL/HIGH/MEDIUM/LOW
  and a short theme label in parens.

## Representative Quotes
> "TODO"
> — Role, participant ID

## Recommendations
1. TODO

## Follow-ups / Open Questions
- TODO

## Related
- Synthesized into: [{Path(related_findings[0]).name if related_findings else 'TODO.md'}]({related_findings[0] if related_findings else 'TODO.md'})
"""
    return fm_block(fm_fields) + "\n\n" + body


def participants_template(title, date, rtype, tags, related_findings, researcher, count, roles):
    fm_fields = {
        "title": f"Participants — {yaml_str(title)}",
        "date": date,
        "type": rtype,
        "status": "raw",
        "tags": tags,
        "related_components": [],
        "related_findings": related_findings,
    }
    roles_block = "\n".join(f"- {r}" for r in roles) if roles else "- TODO"
    body = f"""# Participants — {title}

**Count:** {count if count is not None else "TODO"}

**Roles:**
{roles_block}

**Researcher:** {researcher or "TODO"}

**Recruitment note:** TODO — how participants were recruited. No real patient or staff identities
should ever be recorded here; use session-scoped fictional/anonymized participant IDs (e.g. P01)
in session-notes.md instead of names.
"""
    return fm_block(fm_fields) + "\n\n" + body


def slugify(title):
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "untitled"


def deliverable_template(folder, title, date, status, tags, related_findings, source_type, extra_fields, description):
    fm_fields = {
        "title": yaml_str(title),
        "date": date,
        "status": status,
        "tags": tags,
        "related_findings": related_findings,
        "source_type": source_type,
    }
    fm_fields.update(extra_fields)

    is_stub = folder in STUB_ONLY_FOLDERS or source_type != "native"
    if is_stub:
        body = f"# {title}\n\n{description or 'TODO — one or two sentences: what this artifact covers, what it is for, and key states/screens.'}\n"
    else:
        label = folder.replace("-", " ")
        body = f"""# {title}

## Description
{description or f"TODO — one or two paragraphs describing this {label} artifact."}

## Details
TODO
"""
    return fm_block(fm_fields) + "\n\n" + body


def create_deliverable(folder, args, glossary):
    if folder not in DELIVERABLE_SCHEMAS:
        print(f"❌ Unknown --deliverable-folder {folder!r}. Valid values: {', '.join(sorted(DELIVERABLE_SCHEMAS))}", file=sys.stderr)
        sys.exit(1)

    if not args.title:
        print("❌ --title is required", file=sys.stderr)
        sys.exit(1)

    try:
        datetime.date.fromisoformat(args.date)
    except ValueError:
        print(f"❌ --date must be YYYY-MM-DD, got {args.date!r}", file=sys.stderr)
        sys.exit(1)

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    related_findings_raw = [f.strip() for f in args.related_findings.split(",") if f.strip()]
    check_tags(tags, glossary)
    related_findings = [f"../research/findings/{f}" if not f.startswith("../") else f for f in related_findings_raw]

    default_source_type = "native"
    for k, v in DELIVERABLE_SCHEMAS[folder]:
        if k == "source_type":
            default_source_type = v
    source_type = args.source_type or default_source_type

    extra_fields = {k: v for k, v in DELIVERABLE_SCHEMAS[folder]}
    if args.fields:
        try:
            overrides = json.loads(args.fields)
        except json.JSONDecodeError as e:
            print(f"❌ --fields must be valid JSON: {e}", file=sys.stderr)
            sys.exit(1)
        extra_fields.update(overrides)
    extra_fields.pop("source_type", None)  # source_type is handled via --source-type, not duplicated in extras

    if folder in STUB_ONLY_FOLDERS and source_type == "native":
        print(f"❌ {folder}/ is stub-only — source_type must not be 'native' (e.g. figma-link, github-link)", file=sys.stderr)
        sys.exit(1)

    filename = args.filename or slugify(args.title)
    folder_path = REPO_ROOT / folder
    file_path = folder_path / f"{filename}.md"

    if file_path.exists():
        print(f"❌ {file_path} already exists — not overwriting. Pick a different --filename.", file=sys.stderr)
        sys.exit(1)

    folder_path.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        deliverable_template(folder, args.title, args.date, args.status, tags, related_findings,
                              source_type, extra_fields, args.description),
        encoding="utf-8",
    )
    print(f"✅ Created {file_path}")
    print("Next: fill in the TODOs, then run build_index.py to refresh the folder's _index.md.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", help="Session or deliverable title")
    parser.add_argument("--type", dest="rtype", choices=VALID_TYPES, help="Research method type (raw session mode)")
    parser.add_argument("--topic-slug", help="URL/filesystem-safe slug, e.g. onboarding-flow-usability-test (raw session mode)")
    parser.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD, defaults to today")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--related-components", default="", help="Comma-separated component slugs (raw session mode)")
    parser.add_argument("--related-findings", default="", help="Comma-separated findings/*.md filenames")
    parser.add_argument("--researcher", default="", help="Researcher name (raw session mode)")
    parser.add_argument("--method-label", default="", help="Free-text method description for the Method section (raw session mode)")
    parser.add_argument("--participants-count", type=int, default=None)
    parser.add_argument("--participants-roles", default="", help="Comma-separated participant roles (raw session mode)")
    parser.add_argument("--check-tags-only", default=None, help="Comma-separated tags to validate against the glossary, then exit")

    # feature-002 deliverable mode
    parser.add_argument("--deliverable-folder", choices=sorted(DELIVERABLE_SCHEMAS), default=None,
                         help="Switch to deliverable mode: write a single file into this top-level folder instead of a raw/ session")
    parser.add_argument("--filename", default="", help="Deliverable mode: filesystem-safe filename (no .md), defaults to a slug of --title")
    parser.add_argument("--status", default="draft", choices=["draft", "in-review", "final", "superseded"], help="Deliverable mode: status field")
    parser.add_argument("--source-type", default="", help="Deliverable mode: source_type field (native | figma-link | github-link | confluence-link | docx-link | figma-export). Defaults to the folder's schema default.")
    parser.add_argument("--fields", default="", help="Deliverable mode: JSON object overriding this folder's type-specific frontmatter defaults")
    parser.add_argument("--description", default="", help="Deliverable mode: one or two sentence description for the body")
    args = parser.parse_args()

    glossary = load_tag_glossary()

    if args.check_tags_only is not None:
        tags = [t.strip() for t in args.check_tags_only.split(",") if t.strip()]
        unknown = check_tags(tags, glossary)
        sys.exit(1 if unknown else 0)

    if args.deliverable_folder:
        create_deliverable(args.deliverable_folder, args, glossary)
        return

    missing = [name for name, val in [("--title", args.title), ("--type", args.rtype), ("--topic-slug", args.topic_slug)] if not val]
    if missing:
        parser.error(f"missing required argument(s): {', '.join(missing)}")

    try:
        datetime.date.fromisoformat(args.date)
    except ValueError:
        parser.error(f"--date must be YYYY-MM-DD, got {args.date!r}")

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    related_components = [c.strip() for c in args.related_components.split(",") if c.strip()]
    related_findings_raw = [f.strip() for f in args.related_findings.split(",") if f.strip()]
    roles = [r.strip() for r in args.participants_roles.split(",") if r.strip()]

    check_tags(tags, glossary)

    # related_findings paths are relative to raw/<date>-<slug>/, so ../../findings/<name>
    related_findings = [f"../../findings/{f}" if not f.startswith("../") else f for f in related_findings_raw]
    if not related_findings:
        print("⚠️  No --related-findings given — remember to link this session into a findings/*.md file once synthesized.", file=sys.stderr)

    folder_name = f"{args.date}-{args.topic_slug}"
    folder_path = RAW_ROOT / folder_name

    if folder_path.exists():
        print(f"❌ {folder_path} already exists — not overwriting. Pick a different --topic-slug or --date, "
              f"or edit the existing session directly (raw/ files should never be rewritten by this script once real content exists).",
              file=sys.stderr)
        sys.exit(1)

    folder_path.mkdir(parents=True)

    (folder_path / "session-notes.md").write_text(
        session_notes_template(args.title, args.date, args.rtype, tags, related_components,
                                related_findings, args.researcher, args.method_label),
        encoding="utf-8",
    )
    (folder_path / "participants.md").write_text(
        participants_template(args.title, args.date, args.rtype, tags, related_findings,
                               args.researcher, args.participants_count, roles),
        encoding="utf-8",
    )

    print(f"✅ Created {folder_path}/")
    print(f"   - session-notes.md")
    print(f"   - participants.md")
    print(f"Next: fill in the TODOs, then synthesize into research/findings/<topic>.md and run build_index.py.")


if __name__ == "__main__":
    main()
