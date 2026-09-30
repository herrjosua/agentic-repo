# Research Repo — Fictional Sample Dataset (Meridian Health Network / "Compass AI")

**This entire dataset is synthetic/fictional.** No real patients, staff, organizations, or PHI are
represented. Generated as sample content for the agentic UX research repo, matching the structure
and frontmatter schema in [`agentic-ux-research-repo-plan.md`](agentic-ux-research-repo-plan.md).
Decisions behind that structure are in [`decisions.md`](decisions.md); setup is in
[`SETUP.md`](SETUP.md).

## Docs in this folder

"Checked against repo" means the doc was re-read against the scripts and folders on that date.
Docs not re-checked show their last-commit date instead.

| Path | Purpose | Status |
|---|---|---|
| [`../README.md`](../README.md) | Repo overview and development commands | checked against repo 2026-09-30 |
| [`../AGENTS.md`](../AGENTS.md) | Instructions for any agent working in the repo (`CLAUDE.md` imports it) | checked against repo 2026-09-30 |
| [`README.md`](README.md) | This file: the sample dataset, its structure, frontmatter schema, and a docs inventory | checked against repo 2026-09-30 |
| [`SETUP.md`](SETUP.md) | Step-by-step setup: clone, venv, dependencies, tests, first session, index, search UI, Figma access, Windows notes | checked against repo 2026-09-30 |
| [`agentic-ux-research-repo-plan.md`](agentic-ux-research-repo-plan.md) | The design plan and its current status | checked against repo 2026-09-30 |
| [`decisions.md`](decisions.md) | Decision log: one numbered entry per decision, with date, status and rationale | checked against repo 2026-09-30 |
| [`deliverable-types.md`](deliverable-types.md) | The 20 deliverable folders, their frontmatter fields and the stub pattern | checked against repo 2026-09-30 |
| [`how-to-query-the-repo.md`](how-to-query-the-repo.md) | Ways to query the corpus: an agent, `research/search.html`, and Ask the Repo | checked against repo 2026-09-30 |
| [`projects.md`](projects.md) | `project-*` tags and `research/projects.yml` rules | not re-verified (last commit 2026-09-28) |
| [`demo-deploy.md`](demo-deploy.md) | How the public demo is synced and reset | checked against repo 2026-09-30 |
| [`ask-audit-2026-09-27.md`](ask-audit-2026-09-27.md) | Corpus consistency audit (point-in-time record) | not re-verified (last commit 2026-09-27) |
| [`synthesis-audit-2026-09-29.md`](synthesis-audit-2026-09-29.md) | Synthesis overreach audit (point-in-time record) | not re-verified (last commit 2026-09-29) |

## What's in the corpus

| Kind | Count | Where |
|---|---|---|
| Raw research sessions | 30 (60 `session-notes.md` / `participants.md` files, plus 1 correction file) | `research/raw/` |
| Findings | 12 (plus the `tags.md` glossary) | `research/findings/` |
| Analytics summaries | 1 | `analytics/summaries/` |
| Components | 18 | `design-tokens/components/` |
| Deliverables | 36, across 20 folders | the top-level deliverable folders (see [`deliverable-types.md`](deliverable-types.md)) |

## Structure

```
research/
  raw/
    YYYY-MM-DD-topic-slug/
      session-notes.md      <- objective, method, findings, quotes, recs, follow-ups
      participants.md       <- participant roster/detail, kept separate from session-notes.md
  findings/
    <topic>.md               <- synthesized, living doc per topic, cross-referenced
    tags.md                  <- canonical tag glossary, shared with analytics/summaries/
  _index.md                  <- topic -> tags -> related components -> related analytics -> last-updated -> raw sources
analytics/
  raw/
    YYYY-MM-DD-topic-slug/
      snapshot.csv            <- untouched export from whatever analytics tool is in use
  summaries/
    <topic>.md                <- synthesized interpretation, cross-referenced back to findings/
  _index.md                   <- summary -> tool -> tags -> related findings -> last-updated
```

`raw/` (in both `research/` and `analytics/`) is treated as append-only per the plan: nothing here
should be rewritten. `findings/` is the compiled, freely-revised layer an agent should search first
(frontmatter tags + grep/glob), falling back to `raw/` only to verify or quote a specific session.
`analytics/summaries/` follows the same pattern as `findings/` — synthesized, freely revised — but
for quant evidence instead of qualitative sessions, per [decision 5](decisions.md#5-analytics-gets-its-own-top-level-folder):
analytics gets its own sibling folder rather than being a `type: analytics` finding.

## Frontmatter schema

Every file in `raw/`, `findings/`, and `analytics/summaries/` carries:

```yaml
---
title: ...
date: YYYY-MM-DD
type: usability-test | interview | survey | contextual-inquiry | accessibility-audit | analytics | synthesis
status: raw | synthesized | superseded
researcher: ...           # optional — see below
tags: [...]
related_components: [...]
related_findings: [...]   # paths to findings/*.md files
related_analytics: [...]  # paths to analytics/summaries/*.md files
---
```

**`researcher` is optional.** `new_research_session.py` always writes a `researcher:` key into a
new raw session, filled from `--researcher` or left empty. None of the 61 raw files that exist
today has the key: they predate it and are append-only, so they carry the researcher only as a
`**Researcher:**` line in the body. See `AGENTS.md` → "Attribution fields".

**Note on `type`:** the plan's original example enum listed `usability-test | interview | survey |
analytics | synthesis` (the plan's §6 example now shows all seven values). This dataset includes two research methods the org actually uses
(contextual inquiry, accessibility audits) that don't fit those five cleanly, so `contextual-inquiry`
and `accessibility-audit` were added as additional values. **Confirmed with the schema owner:** both
stay as their own `type` values rather than folding into `interview`.

**`analytics` as a raw-session `type`:** the plan's resolved decision drops `analytics` as a
finding-level `type` — analytics is a data source (its own `analytics/summaries/*.md`), not a
research method a finding was synthesized from. `new_research_session.py`'s `VALID_TYPES`, however,
also lists `analytics` as a valid type for a *raw research session* — e.g. a session where someone
manually reviewed a dashboard as a discovery activity, distinct from an automated export landing in
`analytics/raw/`. **Confirmed with the schema owner:** this stays. See
`research/raw/2026-01-27-dashboard-review-ambient-scribe-ga-adoption/` for a sample `type: analytics`
session.

## Topics in `findings/`

- `ambient-scribe.md` — v0.1 → v0.2 → GA release candidate, longitudinal
- `ambient-scribe-post-ga-refinements.md` — post-GA follow-on, reviewed by a second researcher
- `prior-authorization.md` — v1 → v2
- `governance-and-phi.md` — the year-long executive/privacy/CMIO thread
- `accessibility-cross-cutting.md` — a pattern found independently in 3 separate audits
- `care-coordination-triage.md`
- `clinician-experience-documentation-burden.md`
- `patient-scheduling-chatbot.md`
- `him-coding-and-billing.md`
- `scope-boundaries-and-workflow-fit.md` — deliberate "don't build this yet" findings
- `rollout-and-change-management.md`
- `onboarding.md` — setup-step confusion, backed by `analytics/summaries/onboarding-funnel-dropoff.md`

Each `findings/*.md` has an **Evidence Trail** section linking back to every `raw/` session that
backs it, and a **Related Findings** section cross-linking to thematically connected topics — e.g.
the color-only status accessibility bug is findable both from `accessibility-cross-cutting.md` and
from the December executive retro entry in `governance-and-phi.md`, which cites it as an example of
a cross-cutting pattern.

## What's NOT included here

`research/scripts/new_research_session.py` and `research/scripts/build_index.py` are now built
(see those files directly, and note `build_index.py` also regenerates `analytics/_index.md` and
validates `related_analytics` cross-references). `_index.md` in this sample was regenerated by
running `build_index.py` for real, not written by hand. `design-tokens/scripts/sync_figma_tokens.py`
is also built, but its live Figma-fetch path has not been run against a real Figma file in this
sandbox — only its offline transform/write functions were tested (see the script's own docstring
for what was and wasn't verified). Its Variables endpoint also requires a Figma Enterprise org
plan, which this account doesn't have, so this repo is in the manual fallback: `tokens.tokens.json`
is normally generated by the sync, but here it remains a hand-maintained placeholder until either
that changes or an alternate token source (Style Dictionary, Tokens Studio) is wired in via
`--regenerate-design-only`. Component files in `design-tokens/components/` are written by the
sync; their hand-written `## Notes` sections survive a re-sync and are fine to edit, and only the
generated parts are overwritten.

`analytics/summaries/` now has one fictional sample (`onboarding-funnel-dropoff.md`, cross-linked
from `research/findings/onboarding.md`), but `analytics/raw/` still has no content — no
analytics-platform export has been written for this dataset yet. There's also no
`analytics/scripts/pull_analytics.py` — that's expected until a real analytics platform is
actually in the picture; there's nothing to pull from yet. (A `type: analytics` sample *does*
exist under `research/raw/` — see the note above — but that's a manually-reviewed dashboard
session, distinct from an automated `analytics/raw/` export.)