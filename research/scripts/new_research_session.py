#!/usr/bin/env python3
"""
new_research_session.py — scaffold a new raw/ research session folder.

Lowers the friction for capturing raw notes (the step most likely to get skipped under
deadline pressure), per the Version Milestone Roadmap (v0.3).

Creates:
    research/raw/<date>-<topic-slug>/session-notes.md
    research/raw/<date>-<topic-slug>/participants.md

Both are pre-filled with the repo's frontmatter schema and TODO placeholders. Never overwrites
an existing session folder — if one already exists for that date+slug, the script exits with an
error rather than clobbering notes that may already be in progress.

Usage:
    python new_research_session.py \\
        --title "Onboarding flow usability test" \\
        --type usability-test \\
        --topic-slug onboarding-flow-usability-test \\
        --tags onboarding,usability,mobile \\
        --related-findings onboarding.md \\
        [--date 2026-09-12] \\
        [--researcher "J. Alvarez"] \\
        [--related-components onboarding-carousel,cta-primary]

Run with --check-tags-only <tag1,tag2,...> to validate a tag list against the glossary without
creating anything.
"""
import argparse
import datetime
import os
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_ROOT = SCRIPT_DIR.parent  # research/
RAW_ROOT = RESEARCH_ROOT / "raw"
TAGS_FILE = RESEARCH_ROOT / "findings" / "tags.md"

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
        if isinstance(v, list):
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


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", help="Session title")
    parser.add_argument("--type", dest="rtype", choices=VALID_TYPES, help="Research method type")
    parser.add_argument("--topic-slug", help="URL/filesystem-safe slug, e.g. onboarding-flow-usability-test")
    parser.add_argument("--date", default=datetime.date.today().isoformat(), help="YYYY-MM-DD, defaults to today")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    parser.add_argument("--related-components", default="", help="Comma-separated component slugs")
    parser.add_argument("--related-findings", default="", help="Comma-separated findings/*.md filenames this session feeds")
    parser.add_argument("--researcher", default="", help="Researcher name")
    parser.add_argument("--method-label", default="", help="Free-text method description for the Method section")
    parser.add_argument("--participants-count", type=int, default=None)
    parser.add_argument("--participants-roles", default="", help="Comma-separated participant roles")
    parser.add_argument("--check-tags-only", default=None, help="Comma-separated tags to validate against the glossary, then exit")
    args = parser.parse_args()

    glossary = load_tag_glossary()

    if args.check_tags_only is not None:
        tags = [t.strip() for t in args.check_tags_only.split(",") if t.strip()]
        unknown = check_tags(tags, glossary)
        sys.exit(1 if unknown else 0)

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
