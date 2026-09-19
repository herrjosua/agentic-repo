# agentic-repo — Agent Instructions

This repo is three things sharing one retrieval layer: a UX research memory (`research/`), a
design-ops mirror of Figma (`design-tokens/`), and quant/analytics evidence (`analytics/`). All
three turn a tool's proprietary format into git-tracked Markdown you can query directly.

## Where things live
- `research/raw/YYYY-MM-DD-topic-slug/` — one folder per research session (`session-notes.md` +
  `participants.md`). **Append-only. Never edit or rewrite a file here.** If a raw note was wrong,
  add a new file that references and corrects it.
- `research/findings/<topic>.md` — synthesized, living per-topic conclusions. These ARE meant to be
  revised as new raw evidence comes in. Every finding must cite the raw session(s) that back it.
- `research/findings/tags.md` — canonical tag glossary, shared across `raw/`, `findings/`, and
  `analytics/summaries/`. Before using a new tag, check it's here.
- `research/_index.md` — flat topic → tags → components → related analytics → last-updated →
  raw-sources table.
- `design-tokens/tokens.tokens.json` — canonical DTCG token source. Never hand-edit.
- `design-tokens/design.md` and `design-tokens/components/*.md` — generated views of the tokens
  file; treat as read-only output, not source.
- `analytics/raw/YYYY-MM-DD-topic-slug/` — untouched exports pulled from an analytics platform.
  Same append-only rule as `research/raw/`.
- `analytics/summaries/<topic>.md` — synthesized interpretation of quant data. Links back to the
  qualitative finding(s) it supports via `related_findings`; a finding links to it via
  `related_analytics`. Analytics is a data source, not a research method — it never appears as a
  finding `type`, only as a cross-reference.
- `analytics/_index.md` — flat summary → tool → tags → related findings → last-updated table.

## Frontmatter (every file in `raw/`, `findings/`, and `analytics/summaries/`)
```yaml
title: ...
date: YYYY-MM-DD
type: usability-test | interview | survey | contextual-inquiry | accessibility-audit | analytics | synthesis
status: raw | synthesized | superseded
researcher: ...          # findings/ and analytics/summaries/ only — see Attribution fields below
tags: [...]
related_components: [...]
related_findings: [...]
related_analytics: [...]
```

## Attribution fields
Four fields carry who-did-what across the repo. None are required to be filled in for a file to
be valid, and each has a different scope — don't add one to a file type it isn't listed for below.

- **`researcher`** — frontmatter field on `findings/*.md` (except `tags.md`) and
  `analytics/summaries/*.md`. **Not** a frontmatter field in `raw/` — a raw session's researcher
  is instead a `**Researcher:**` line in the body of `session-notes.md`/`participants.md`, under
  the Method section, populated via `new_research_session.py --researcher`. This split is
  historical, not a typo: the body-text convention in `raw/` predates this field's formalization
  in `findings/`/`analytics/summaries/`, and both stay as-is rather than being reconciled into one
  mechanism.
- **`designer`** — frontmatter field on deliverable files (the 20 `feature-002` folders listed
  under "Creating a feature-002 deliverable file" above), naming who produced that deliverable.
  Not present in `design-tokens/` — those files are generated/read-only (see above) and carry no
  attribution field.
- **`evaluator`** — pre-existing, `heuristic-evaluations/`-specific field (see
  `docs/deliverable-types.md`) naming who ran that evaluation. Now doing double duty as an
  attribution field: a heuristic evaluation is inherently a review/assessment activity, so it's
  populated with a reviewer's name rather than a `designer`'s, even though it lives in a
  deliverable folder.
- **`reviewed_by`** — sparse, deliberately not retrofitted onto the existing corpus. Used only
  where a second person's review/edit pass on a specific piece of content is real and worth
  recording — currently just the `ambient-scribe-post-ga-refinements.md` finding and its
  `ambient-scribe-session-lock-recovery.md` deliverable. Don't add it repo-wide as a default
  field; add it only when a genuine review pass happened on that specific file.

## Retrieval strategy
Search `findings/` first (grep/glob + frontmatter tags), including each finding's
`related_analytics` links. Fall back to `raw/` or `analytics/summaries/` only to verify or quote a
specific session or dataset. Do not build or suggest a vector/embeddings pipeline — out of scope
until keyword + tag search actually proves insufficient at scale.

## After adding a finding or analytics summary
Run `research/scripts/build_index.py` to refresh `research/_index.md` and `analytics/_index.md`
(use `--check` in CI to catch drift, undefined tags, and dangling `related_findings` /
`related_analytics` links without writing).

## Starting a new session
Run `research/scripts/new_research_session.py --title ... --type ... --topic-slug ... --tags ...`
to scaffold a new `raw/YYYY-MM-DD-topic-slug/` folder instead of creating one by hand.

## Creating a feature-002 deliverable file
`new_research_session.py` also creates single files in the 20 top-level deliverable folders —
`--type` doubles as the switch: pass one of the folder names below instead of a raw-session
research type and the script writes `<folder>/<slug>.md` instead of a `raw/` session:

```
research-plans, facilitation-guides, topline-summaries, research-readouts,
heuristic-evaluations, accessibility-screenings, service-topology, personas,
mental-models, mindsets, journey-maps, thumbnails, wireframes, user-flows,
wireflows, storyboards, mockups, prototypes, design-system, style-guide
```

```
research/scripts/new_research_session.py --type personas --title "Frontline Nurse — Ambient Scribe" \
    --slug frontline-nurse-ambient-scribe --tags nursing,ambient-scribe \
    --related-findings clinician-experience-documentation-burden.md
```

- `--slug` is required — it's the filename (kebab-case, no `.md`).
- Base frontmatter (`title`/`date`/`status`/`tags`/`related_findings`/`source_type`) always comes
  from CLI flags, never prompted.
- By default the script interactively prompts for that folder's type-specific extra fields (see
  `docs/deliverable-types.md`), in the order documented there and in the Decision Log. Press
  Enter to leave any field blank.
- **`--no-prompt`** skips all interactive prompting and leaves every extra field at its schema
  default instead — **a cold/scripted agent session should always pass this**, since it cannot
  answer interactive prompts.
- `--type prototypes` additionally requires **`--proto-type clickthrough|coded`**, which sets that
  file's `type` field and the `source_type` default (`figma-link` for clickthrough, `github-link`
  for coded) — see `docs/deliverable-types.md` for why `prototypes/` is stub-only.
- Never overwrites an existing file — pass `--force` to overwrite. This check runs before any
  interactive prompting.
- Same tag-glossary warn-don't-block validation as raw sessions, and the same
  `--check-tags-only` support.
- Doesn't auto-run `build_index.py` — run it yourself afterward to refresh the folder's
  `_index.md` (and to catch a dangling cross-link field, e.g. `persona_ref`, `related_plan`).

## Git discipline
Every synthesis is its own commit; say what raw evidence triggered the change. Never rewrite
`raw/` or `analytics/raw/` file history.