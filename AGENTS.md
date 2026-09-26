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
researcher: ...          # findings/, analytics/summaries/, and raw/ sessions created via
                          # --researcher — see Attribution fields below
tags: [...]
related_components: [...]
related_findings: [...]
related_analytics: [...]
```

## Attribution fields
Four fields carry who-did-what across the repo. None are required to be filled in for a file to
be valid, and each has a different scope — don't add one to a file type it isn't listed for below.

- **`researcher`** — frontmatter field on `findings/*.md` (except `tags.md`) and
  `analytics/summaries/*.md`. Also a frontmatter field in `raw/` for any session created via
  `new_research_session.py --researcher`: the flag writes a real `researcher:` frontmatter field
  *and* the pre-existing `**Researcher:**` body-text line under the Method section (kept as a
  redundant, human-readable convenience — not removed). Raw sessions created before this flag
  wrote frontmatter still carry only the body-text line and have no `researcher` frontmatter
  field; they were deliberately **not** backfilled (`raw/` is append-only — see above), so
  `export_records.py`/the CRUD UI report `researcher: null` for those until each is naturally
  revisited.
- **`designer`** — frontmatter field on deliverable files, naming who produced that deliverable.
  Written via `new_research_session.py --designer` in deliverable mode, and applies to all 19 of
  the `feature-002` folders listed under "Creating a feature-002 deliverable file" above *except*
  `heuristic-evaluations`, which uses `evaluator` for attribution instead (see below) — `--designer`
  is a no-op there. Not present in `design-tokens/` — those files are generated/read-only (see
  above) and carry no attribution field.
- **`evaluator`** — pre-existing, `heuristic-evaluations/`-specific field (see
  `docs/deliverable-types.md`) naming who ran that evaluation. Now doing double duty as an
  attribution field: a heuristic evaluation is inherently a review/assessment activity, so it's
  populated with a reviewer's name rather than a `designer`'s, even though it lives in a
  deliverable folder. Written via `new_research_session.py --evaluator` in deliverable mode — the
  inverse scope of `--designer`: it applies *only* to `--type heuristic-evaluations` and is a
  no-op (with a warning) for every other deliverable folder.
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
to scaffold a new `raw/YYYY-MM-DD-topic-slug/` folder instead of creating one by hand. Pass
`--researcher "Name"` to also populate the `researcher` frontmatter field (see Attribution
fields above) — the pre-existing `**Researcher:**` body-text line is still written too.

## Creating a feature-002 deliverable file
`new_research_session.py` also creates single files in the 20 top-level deliverable folders —
`--type` doubles as the switch: pass one of the folder names below instead of a raw-session
research type and the script writes `<folder>/<slug>.md` instead of a `raw/` session. Pass
`--designer "Name"` to populate the `designer` frontmatter field (ignored for
`heuristic-evaluations`, which uses its own `evaluator` field instead — see Attribution fields
above). Pass `--evaluator "Name"` for the inverse case: it populates the `evaluator` frontmatter
field for `--type heuristic-evaluations` only, and is ignored (with a warning) for every other
folder:

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

## Demo repo sync
The public CRUD UI demo never runs against this (real) repo — it runs against a separate,
isolated, private repo, `research-repo-demo`, kept in sync by
`.github/workflows/sync-demo.yml`. That workflow runs on a schedule (every 6 hours) and on
`workflow_dispatch`, copies `research/` (which brings `research/scripts/` along with it — no
separate script sync needed), `design-tokens/`, `analytics/`, the 20 top-level deliverable
folders (read from `DELIVERABLE_SCHEMAS` in `new_research_session.py`, not a second hand-typed
list — the workflow fails if that dict doesn't have exactly 20 entries), and `requirements.txt`
into the demo repo. Because syncing `research/scripts/` means importing one of its modules
mid-workflow, the job sets `PYTHONDONTWRITEBYTECODE=1` and the sync step also strips any stray
`__pycache__/`/`*.pyc` and writes a `.gitignore` for them into the demo repo, so a compiled
bytecode file never gets published or reappears as an untracked file when the scripts run on the
demo server. Before committing or moving the tag, it runs `build_index.py --check` against
the assembled demo content and fails the job if that check fails, so a sync that would leave
broken cross-references (e.g. a finding's `related_analytics` pointing at a summary that didn't
get synced) never gets published. On success it commits, pushes to the demo repo's `main`, and
force-moves a fixed tag, `demo-baseline`, onto that commit. It authenticates to the demo repo with
the `DEMO_REPO_PAT` repo secret, a fine-grained PAT scoped only to `research-repo-demo` with
Contents: Read and write — nothing else in this repo (docs/, .github/, tests/, README.md,
AGENTS.md, CLAUDE.md, dev-only config) is synced.

On the demo server (once it exists), `research/scripts/reset_demo.sh` resets that checkout to
`demo-baseline` (`git fetch` + `git reset --hard`) and reruns `build_index.py` (via `PYTHON_BIN`,
falling back to `python3`), so the demo can't accumulate visitor edits between resets. It isn't
scheduled anywhere yet — see `docs/demo-deploy.md` for what's still unwired before it can be.

## Git discipline
Every synthesis is its own commit; say what raw evidence triggered the change. Never rewrite
`raw/` or `analytics/raw/` file history.