#!/usr/bin/env python3
"""
new_research_session.py — scaffold a new raw/ research session folder, or a single deliverable
file in one of the 20 top-level folders added by feature-002 (research-plans/, personas/,
mockups/, prototypes/, etc.).

Lowers the friction for capturing raw notes (the step most likely to get skipped under
deadline pressure), per the Version Milestone Roadmap (v0.3).

Raw session mode (default — no new flags) creates:
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

--researcher writes a real researcher frontmatter field (as well as the existing
**Researcher:** line in the Method section / participants.md body, kept as a redundant
display convenience). This only applies going forward — existing raw sessions created before
this flag wrote frontmatter are not backfilled; see AGENTS.md's Attribution fields section.

Usage (feature-002 deliverable, e.g. a persona or mockup file) — `--type` doubles as the
deliverable-folder switch: pass one of the 20 folder names instead of a raw-session research
type and the script switches into deliverable mode, writing a single file to
<repo-root>/<type>/<slug>.md:
    python new_research_session.py \\
        --type personas \\
        --title "Frontline Nurse — Ambient Scribe" \\
        --slug frontline-nurse-ambient-scribe \\
        --tags nursing,ambient-scribe \\
        --related-findings clinician-experience-documentation-burden.md \\
        [--date 2026-09-12] [--status draft] [--source-type native] [--force] \\
        [--designer "Sam Okafor"] [--evaluator "Jordan Lee"]

--designer writes the designer frontmatter field and applies to all deliverable folders except
--type heuristic-evaluations, which uses its own evaluator field for attribution instead.

--evaluator writes the evaluator frontmatter field and applies ONLY to --type
heuristic-evaluations — the inverse of --designer's scope. Passing --evaluator for any other
deliverable folder is a no-op with a warning printed, the same way --designer is a no-op with a
warning for heuristic-evaluations.

By default (no --no-prompt), deliverable mode interactively prompts for that folder's
type-specific extra frontmatter fields (e.g. personas prompts for segment, based_on), in the
order given in docs/deliverable-types.md / the Decision Log. Press Enter on any prompt to leave
that field empty — nothing is required. Pass --no-prompt for scripted/non-interactive use (a
cold agent session should always pass this — it cannot answer interactive prompts); every extra
field is then left at its schema default (empty for most fields) with no prompting at all.

`prototypes/` additionally requires `--proto-type clickthrough|coded`, which sets that file's
`type` field and the `source_type` default (figma-link for clickthrough, github-link for coded)
— see docs/deliverable-types.md for why prototypes/ is stub-only.

Base frontmatter (title/date/status/tags/related_findings/source_type) always comes from CLI
flags (--title/--date/--status/--tags/--related-findings/--source-type), never from a prompt.
Never overwrites an existing deliverable file — pass --force to overwrite. The overwrite check
runs before any interactive prompting, so a rejected run never asks you ten questions first.

Run with --check-tags-only <tag1,tag2,...> to validate a tag list against the glossary without
creating anything (works the same in both modes).
"""
import argparse
import copy
import datetime
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RESEARCH_ROOT = SCRIPT_DIR.parent  # research/
REPO_ROOT = RESEARCH_ROOT.parent
RAW_ROOT = RESEARCH_ROOT / "raw"
TAGS_FILE = RESEARCH_ROOT / "findings" / "tags.md"

# feature-002: the 20 top-level deliverable folders and their type-specific frontmatter fields
# (beyond the shared base block), in the order given in docs/deliverable-types.md and the
# Decision Log. Values are the schema defaults used verbatim in --no-prompt mode; interactive
# mode (the default) prompts for each of these instead — see prompt_for_value().
#
# "source_type" and (prototypes-only) "type" are deliberately NOT here: source_type is a base
# field (never prompted, driven by --source-type / the per-folder default below), and
# prototypes' `type` is driven by the required --proto-type flag instead. See
# resolve_source_type() and create_deliverable().
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
    "wireframes": [("fidelity", "lo-fi"), ("flow_ref", "")],
    "user-flows": [("flow_name", ""), ("screens_count", 0)],
    "wireflows": [("flow_name", "")],
    "storyboards": [("scenario", "")],
    "mockups": [("fidelity", "hi-fi"), ("figma_url", "")],
    "prototypes": [("url", ""), ("stack", "")],
    "design-system": [("version", ""), ("related_style_guide", "")],
    "style-guide": [("version", "")],
}

# One-line hints shown during interactive prompting, keyed by (folder, field) since the same
# field name means different things in different folders (e.g. "scope", "version", "method").
# Reused verbatim as the prompt text per feature-002 spec §5.
DELIVERABLE_FIELD_HINTS = {
    ("research-plans", "method"): "e.g. moderated-usability, survey, diary-study",
    ("research-plans", "related_guide"): "path to a facilitation-guides/*.md, blank if none yet",
    ("facilitation-guides", "related_plan"): "path to a research-plans/*.md, blank if none yet",
    ("topline-summaries", "related_plan"): "path to a research-plans/*.md, blank if none yet",
    ("topline-summaries", "session_dates"): "comma-separated YYYY-MM-DD dates, blank for none",
    ("research-readouts", "related_analytics"): "comma-separated analytics/summaries/*.md filenames, blank for none",
    ("research-readouts", "presented_to"): "comma-separated audience/stakeholder names, blank for none",
    ("heuristic-evaluations", "method"): "e.g. heuristic-evaluation, cognitive-walkthrough",
    ("heuristic-evaluations", "evaluator"): "name of the person who ran the evaluation",
    ("heuristic-evaluations", "scope"): "what surface or flow was evaluated",
    ("heuristic-evaluations", "severity_scale"): "e.g. Nielsen 0-4, custom 1-5",
    ("accessibility-screenings", "wcag_level"): "e.g. A, AA, AAA",
    ("accessibility-screenings", "scope"): "what surface or flow was screened",
    ("accessibility-screenings", "issues_found"): "integer count, blank defaults to 0",
    ("service-topology", "scope"): "what service or journey this topology covers",
    ("service-topology", "version"): "e.g. v1, v2",
    ("personas", "segment"): "e.g. clinical staff, admin staff, patient",
    ("personas", "based_on"): "comma-separated research-plans/*.md or findings/*.md filenames, blank for none",
    ("mental-models", "scope"): "what concept or system this mental model covers",
    ("mindsets", "segment"): "attitude/motivation-based segment name, not identity",
    ("journey-maps", "persona_ref"): "path to a personas/*.md file, blank if none yet",
    ("journey-maps", "scope"): "what journey this map covers",
    ("thumbnails", "concept"): "short label for the layout idea explored",
    ("thumbnails", "related_wireframes"): "comma-separated wireframes/*.md filenames, blank for none",
    ("wireframes", "fidelity"): "e.g. lo-fi, mid-fi, hi-fi",
    ("wireframes", "flow_ref"): "path to a user-flows/*.md or wireflows/*.md file, blank if none yet",
    ("user-flows", "flow_name"): "short name for this flow",
    ("user-flows", "screens_count"): "integer, blank defaults to 0",
    ("wireflows", "flow_name"): "short name for this flow",
    ("storyboards", "scenario"): "short description of the situational context depicted",
    ("mockups", "fidelity"): "e.g. lo-fi, mid-fi, hi-fi",
    ("mockups", "figma_url"): "link to the source Figma file, blank if none yet",
    ("prototypes", "url"): "link to the Figma click-through or the GitHub repo",
    ("prototypes", "stack"): "e.g. React + Storybook, blank if click-through",
    ("design-system", "version"): "e.g. v1, v2",
    ("design-system", "related_style_guide"): "path to a style-guide/*.md file, blank if none yet",
    ("style-guide", "version"): "e.g. v1, v2",
}

# Sub-field hints for the one dict-valued extra field (research-plans/study_dates).
DELIVERABLE_DICT_SUBFIELD_HINTS = {
    ("research-plans", "study_dates", "start"): "YYYY-MM-DD",
    ("research-plans", "study_dates", "end"): "YYYY-MM-DD",
}

# Only prototypes/ is stub-only by design (no real file to duplicate into the repo for a
# click-through or coded prototype) — see docs/deliverable-types.md.
STUB_ONLY_FOLDERS = {"prototypes"}

PROTO_TYPE_SOURCE_TYPE = {"clickthrough": "figma-link", "coded": "github-link"}

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
        "researcher": yaml_str(researcher) if researcher else "",
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
        "researcher": yaml_str(researcher) if researcher else "",
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


def deliverable_template(folder, title, date, status, tags, related_findings, source_type, designer, extra_fields, description):
    fm_fields = {
        "title": yaml_str(title),
        "date": date,
        "status": status,
    }
    # heuristic-evaluations/ uses its own evaluator field for attribution instead (see AGENTS.md
    # Attribution fields) — designer is never written there, even if --designer is passed.
    if folder != "heuristic-evaluations":
        fm_fields["designer"] = yaml_str(designer) if designer else ""
    fm_fields["tags"] = tags
    fm_fields["related_findings"] = related_findings
    fm_fields["source_type"] = source_type
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


def prompt_for_value(folder, field, default):
    """Interactively prompt for one type-specific extra field, showing its hint from
    DELIVERABLE_FIELD_HINTS. Enter (blank input) always leaves the field empty — it never falls
    back to `default`; `default` only shapes *how* we parse the input (dict/list/int/str), since
    --no-prompt mode is what actually uses the schema defaults verbatim."""
    hint = DELIVERABLE_FIELD_HINTS.get((folder, field), "")
    suffix = f" ({hint})" if hint else ""

    if isinstance(default, dict):
        result = {}
        for sub_k in default:
            sub_hint = DELIVERABLE_DICT_SUBFIELD_HINTS.get((folder, field, sub_k), "")
            sub_suffix = f" ({sub_hint})" if sub_hint else ""
            result[sub_k] = input(f"  {field}.{sub_k}{sub_suffix}: ").strip()
        return result
    if isinstance(default, list):
        raw = input(f"{field}{suffix}, comma-separated: ").strip()
        return [v.strip() for v in raw.split(",") if v.strip()]
    if isinstance(default, int) and not isinstance(default, bool):
        raw = input(f"{field}{suffix}: ").strip()
        if not raw:
            return 0
        try:
            return int(raw)
        except ValueError:
            print(f"⚠️  {field} must be an integer — leaving it at 0", file=sys.stderr)
            return 0
    raw = input(f"{field}{suffix}: ")
    return raw.strip()


def resolve_source_type(folder, args):
    """The base source_type default for this folder, before any --source-type override.
    Every folder defaults to 'native' except prototypes/, which is stub-only and derives its
    default from --proto-type (figma-link for clickthrough, github-link for coded)."""
    if folder == "prototypes":
        return PROTO_TYPE_SOURCE_TYPE[args.proto_type]
    return "native"


def create_deliverable(folder, args, glossary):
    if not args.title:
        print("❌ --title is required", file=sys.stderr)
        sys.exit(1)

    if not args.slug:
        print(f"❌ --slug is required for --type {folder} (deliverable mode) — the file is written to {folder}/<slug>.md", file=sys.stderr)
        sys.exit(1)

    if folder == "prototypes" and not args.proto_type:
        print("❌ --proto-type clickthrough|coded is required when --type prototypes", file=sys.stderr)
        sys.exit(1)

    try:
        datetime.date.fromisoformat(args.date)
    except ValueError:
        print(f"❌ --date must be YYYY-MM-DD, got {args.date!r}", file=sys.stderr)
        sys.exit(1)

    # Overwrite guard runs before anything interactive — reject a clobber before asking ten
    # prompts nobody needed to answer.
    folder_path = REPO_ROOT / folder
    file_path = folder_path / f"{args.slug}.md"
    if file_path.exists() and not args.force:
        print(f"❌ {file_path} already exists — not overwriting. Pass --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    related_findings_raw = [f.strip() for f in args.related_findings.split(",") if f.strip()]
    check_tags(tags, glossary)  # validated at input time, right after tags are parsed
    related_findings = [f"../research/findings/{f}" if not f.startswith("../") else f for f in related_findings_raw]

    source_type = args.source_type or resolve_source_type(folder, args)
    if folder in STUB_ONLY_FOLDERS and source_type == "native":
        print(f"❌ {folder}/ is stub-only — source_type must not be 'native' (e.g. figma-link, github-link)", file=sys.stderr)
        sys.exit(1)

    schema = DELIVERABLE_SCHEMAS[folder]
    extra_fields = {}
    if folder == "prototypes":
        extra_fields["type"] = args.proto_type  # driven by --proto-type, never prompted
    if args.no_prompt:
        extra_fields.update({k: copy.deepcopy(v) for k, v in schema})
    else:
        print(f"Extra fields for {folder}/ (Enter to leave any of these blank):")
        extra_fields.update({k: prompt_for_value(folder, k, default) for k, default in schema})

    if folder == "heuristic-evaluations" and args.designer:
        print(
            "⚠️  --designer is ignored for heuristic-evaluations/ — that folder uses the "
            "evaluator field for attribution instead (set it via the interactive prompt or "
            "--no-prompt default).",
            file=sys.stderr,
        )

    # --evaluator is the inverse of --designer above: it's the heuristic-evaluations/-only
    # attribution flag (see AGENTS.md's Attribution fields section). `evaluator` lives in
    # DELIVERABLE_SCHEMAS as a per-folder extra field (already filled from the schema default or
    # an interactive prompt above), not a base fm_fields entry like designer — so it's applied by
    # overriding extra_fields here rather than by passing it into deliverable_template().
    if folder == "heuristic-evaluations" and args.evaluator:
        extra_fields["evaluator"] = yaml_str(args.evaluator)
    elif folder != "heuristic-evaluations" and args.evaluator:
        print(
            "⚠️  --evaluator is ignored outside heuristic-evaluations/ — that field only applies "
            "to heuristic evaluations; use --designer for other deliverable folders instead.",
            file=sys.stderr,
        )

    folder_path.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        deliverable_template(folder, args.title, args.date, args.status, tags, related_findings,
                              source_type, args.designer, extra_fields, args.description),
        encoding="utf-8",
    )
    print(f"✅ Created {file_path}")
    print("Next: fill in the TODOs, then run build_index.py to refresh the folder's _index.md.")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", help="Session or deliverable title")
    parser.add_argument(
        "--type", dest="rtype", choices=VALID_TYPES + sorted(DELIVERABLE_SCHEMAS),
        help="Raw-session research method (usability-test, interview, ...) for the default mode, OR one of "
             "the 20 feature-002 deliverable folder names (research-plans, personas, mockups, ...) to switch "
             "into deliverable mode instead",
    )
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

    # feature-002 deliverable mode (triggered by --type <folder-name>, see above)
    parser.add_argument("--slug", default="", help="Deliverable mode: kebab-case filename (no .md); file is written to <type>/<slug>.md. Required in deliverable mode.")
    parser.add_argument("--status", default="draft", choices=["draft", "in-review", "final", "superseded"], help="Deliverable mode: status field")
    parser.add_argument("--source-type", default="", help="Deliverable mode: source_type field (native | figma-link | github-link | confluence-link | docx-link | figma-export). Defaults to the folder's schema default.")
    parser.add_argument("--proto-type", choices=sorted(PROTO_TYPE_SOURCE_TYPE), default=None, help="Deliverable mode, required when --type prototypes: clickthrough or coded")
    parser.add_argument("--no-prompt", action="store_true", help="Deliverable mode: skip interactive prompting for type-specific extra fields; leave them at their schema defaults. Use for scripted/non-interactive runs (e.g. a cold agent session).")
    parser.add_argument("--force", action="store_true", help="Deliverable mode: overwrite an existing deliverable file")
    parser.add_argument("--description", default="", help="Deliverable mode: one or two sentence description for the body")
    parser.add_argument("--designer", default="", help="Deliverable mode: designer name, written to the designer frontmatter field. Ignored for --type heuristic-evaluations, which uses its own evaluator field instead.")
    parser.add_argument("--evaluator", default="", help="Deliverable mode: evaluator name, written to the evaluator frontmatter field. Applies ONLY to --type heuristic-evaluations; ignored (with a warning) for every other deliverable folder.")
    args = parser.parse_args()

    glossary = load_tag_glossary()

    if args.check_tags_only is not None:
        tags = [t.strip() for t in args.check_tags_only.split(",") if t.strip()]
        unknown = check_tags(tags, glossary)
        sys.exit(1 if unknown else 0)

    if args.rtype in DELIVERABLE_SCHEMAS:
        create_deliverable(args.rtype, args, glossary)
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
