# Agentic UX Research Repo — Plan

**Status:** Living document, last updated 2026-09-30

**Scope:** Applies to both the work version (Figma MCP not yet available) and the side-project version (Figma MCP available)

# Where this plan stands (2026-09-30)

Sections 1–8 are the original design, kept as the reasoning record and updated where reality moved. Decisions are logged in [`docs/decisions.md`](decisions.md); setup and day-to-day commands are in the [README](../README.md) and [`docs/SETUP.md`](SETUP.md).

**Where it was.** The plan's build order was carried out: repo skeleton, frontmatter schema and `AGENTS.md`; `new_research_session.py`; Figma token sync; `build_index.py`. Along the way the repo grew pieces this plan didn't anticipate: `export_records.py` (a JSON export of every record), a Search UI (`research/search.html`, built by `build_search_ui.py`), and CI (Ruff, mypy, pytest, pip-audit). The deliverable folders (§3) were added and populated, and a separate demo repo was set up (§9).

**Where it is.** As of 2026-09-30 the corpus is 97 records (30 raw, 12 findings, 18 components, 1 analytics summary, 36 deliverables). A synthesis audit ([`docs/synthesis-audit-2026-09-29.md`](synthesis-audit-2026-09-29.md)) checked synthesized records against the raw sessions behind them. A CRUD UI (separate repo) and its Ask the Repo feature sit on top of this repo.

**Where it is going.** Make raw correction files visible to retrieval; add the raw sessions the demo questions depend on; then the Figma MCP swap for the side project. Details are in §8 and §10.

# 1. What this is actually solving

Two related problems, one repo:

1. **Research memory.** Findings get captured in the moment, then forgotten. Six months later nobody can answer "did we already test this?" without digging through old decks. You want an agent that can be pinged and pull up the actual finding, with sourcing.
2. **Design ops / tokens.** Figma holds the canonical visual language, but it's opaque to anything outside Figma. You want that translated into a form an agent (and a human skimming git) can read directly — without hand-copying token values every time the file changes.

Both are the same underlying pattern: **turn something that lives in a tool's proprietary format into git-tracked Markdown that an agent can query later.** So one repo, two content types (research notes, design tokens), one retrieval layer.

# 2. Architecture: three layers, not one pile of files

The failure mode with "just dump everything into markdown files" is that six months in, the agent either drowns in raw notes or hallucinates a synthesis it never actually did. The pattern that's held up in practice (this mirrors Andrej Karpathy's "LLM Wiki" approach, and how Claude Code's own `CLAUDE.md` system is structured) is three layers:

| Layer | Contents | Who/what writes it | Mutability |
| --- | --- | --- | --- |
| **Raw** | Interview transcripts, usability test notes, session recordings' text, raw Figma exports | You, during/right after a session | Append-only, never edited |
| **Synthesized** | Per-topic or per-feature findings, written in your own words, cross-referenced | Agent, on your instruction, reviewed by you | Living — gets revised as new raw evidence comes in |
| **Schema/index** | Frontmatter tags, a top-level index file, a glossary of recurring terms/personas | Script (Python) + agent | Regenerated, not hand-maintained |

The reason this matters for your "ping it in 6 months" use case: if you only have raw notes, the agent has to re-derive the finding every time and may derive it differently each time. If you only have synthesized notes with no raw layer, you can't audit *why* the agent concluded something, and corrections don't have anywhere to attach. Keep both, and keep them visibly separate.

# 3. Proposed repo structure

Matches the shape you're already using on the work repo (`agentic-repo/` root, `docs/`, `research/`), with design tokens added as a sibling folder rather than a separate repo:

```
agentic-repo/
├── docs/                        # AGENTS.md-adjacent guidance, frontmatter schema, this plan
├── research/
│   ├── raw/
│   │   └── 2026-09-11-onboarding-flow-usability-test/
│   │       ├── session-notes.md
│   │       └── participants.md
│   ├── findings/
│   │   ├── onboarding.md        # synthesized, living doc per topic
│   │   ├── search-and-filter.md
│   │   └── tags.md              # tag glossary — canonical list + what each tag means
│   ├── _index.md                # Research index: topic -> finding -> raw sources -> tags
│   └── scripts/                 # python files that operate on research/ live here
│       ├── build_index.py
│       └── new_research_session.py
├── design-tokens/
│   ├── tokens.tokens.json       # canonical DTCG-format tokens (source of truth)
│   ├── design.md                # agent-readable layer generated FROM tokens.json
│   ├── components/
│   │   └── <component>.md       # one file per component: variants, states, Figma node ref, code mapping
│   └── scripts/
│       └── sync_figma_tokens.py # pulls via the Figma REST API, writes tokens.tokens.json + design.md
├── analytics/
│   ├── raw/
│   │   └── 2026-09-11-onboarding-funnel-export/
│   │       └── snapshot.csv     # untouched export from whatever analytics tool is in use
│   ├── summaries/
│   │   └── onboarding-funnel-dropoff.md  # synthesized interpretation, human-written
│   ├── _index.md
│   └── scripts/
│       └── pull_analytics.py    # pulls from the analytics platform's API, once one exists
├── AGENTS.md                    # instructions for any agent working in this repo
└── README.md
```

A few deliberate choices here worth flagging:

- **`research/raw/` folders are named by date + topic**, not by participant, so an agent doing a "have we tested X" query can pattern-match on folder names before even opening files.
- **Tagging lives in two places on purpose**: per-file frontmatter (`tags: [...]`) for machine filtering, and `research/findings/tags.md` as the canonical glossary so tags don't drift into near-duplicates (`onboarding` vs `first-run` vs `first-time-user`) over six months of use. `build_index.py` should validate that every tag used in frontmatter exists in the glossary and flag ones that don't.
- **`design-tokens/` sits alongside `research/`, not inside it** — different update cadence and different source of truth (Figma vs. your own notes), but same repo so a finding can reference a component file by relative path without crossing repo boundaries.
- **`analytics/` is a third sibling folder, same logic as `design-tokens/`** — quant data has its own cadence (pulled from a platform, not written after a session) and its own source of truth (the platform, not your notes). It gets the same raw/summaries split as `research/`: `raw/` holds untouched exports, `summaries/` holds your written interpretation of them. A research finding can reference an analytics summary by relative path, and vice versa, without either folder needing to absorb the other's content.
- **`tokens.tokens.json` is the canonical source**, and `design.md` is a *generated* view of it — never hand-edited. This is the same split Google's `DESIGN.md` project and the community `designtoken.md` spec use: DTCG JSON for deterministic, tool-interoperable values; a markdown layer on top for the rationale and context an agent needs but a token file can't express (why this shade of blue, when not to use it, what it maps to in code).
- **Each notional deliverable type gets its own top-level folder**, alongside `research/`, `design-tokens/`, and `analytics/` (the tree above shows only those three). Research types: research plans, facilitation guides, topline summaries, research readouts, heuristic/usability evaluations, accessibility screenings. Design types: service topology, personas, mental models, mindsets, journey maps, thumbnails, wireframes, user flows, wireflows, storyboards, mockups, prototypes, design system, style guide. Same reasoning as the other sibling folders: each type stays independently queryable/filterable. For a client environment the folder list may need pruning or renaming to match their deliverable taxonomy.
- **Artifacts whose real content lives in an external tool are stubs, not copies.** Figma click-through prototypes, GitHub-hosted coded prototypes, and eventually Confluence/Word content get a lightweight Markdown stub (frontmatter with `source_type` + link, plus a short description) rather than a duplicate of the artifact. This keeps folders small and filterable instead of turning into a huge design-file dump. `source_type` values will need to expand to Confluence and Word in a client environment.
- **Click-through and coded prototypes share one `prototypes/` folder**, with a `type` frontmatter field telling them apart. Both are stub-only, so metadata does the filtering and a second folder wasn't adding anything.
- **`AGENTS.md`** is what makes the "ping it in 6 months" step actually work — it tells any agent session, cold, how the repo is organized, what the frontmatter/tag schema means, and where to look first. See §5 for how this plays with Claude Code specifically, and with Copilot on the work side.

# 4. Design tokens pipeline (the Figma Make / design ops piece)

Current state of Figma's MCP server as of this year, since it's moved fast:

- Figma ships an **official MCP server** — originally a local server requiring Figma desktop, now also available as a **remote hosted server** (no desktop app needed). It exposes variables, component structure, styles, and — if you've set up Code Connect — the mapping from a Figma component to your actual code component.
- As of the most recent update, Figma Make integrates with the MCP server too, so an agent can read the underlying code of a Make file, not just the design.
- Token export increasingly lands in **DTCG format** (`$value`/`$type`, stable spec as of late 2025), which is what Figma, Style Dictionary, Tokens Studio, and Penpot all now read/write — so it's the right canonical format to standardize on rather than inventing your own JSON shape.

Pipeline:

1. `sync_figma_tokens.py` calls the Figma REST API to pull variables and the file's component tree. **The script currently supports the REST path only.** Calling the Figma MCP server instead is planned (§8, step 5) but not implemented; the script's docstring and its closing "MCP swap" comment describe what that change would touch.
2. Writes them straight to `tokens.tokens.json` in DTCG format.
3. Runs a generator step that produces `design.md` from that JSON — token values plus whatever rationale/aliasing notes you've added in frontmatter. This is the file the agent actually reads when a research finding references "the primary CTA color" or when you're asking it to check a proposed change against the existing system.
4. The same script walks components and writes/updates one `.md` per component in `design-tokens/components/`, pulling variant/state data from Figma. A Figma-to-code mapping from Code Connect would come with the MCP swap; it isn't implemented today.

**Update:** the component `.md` files are not purely generated. `sync_figma_tokens.py` preserves a hand-written Notes section on re-sync, so edits there are legitimate synthesis edits, and only the generated parts are overwritten. Generated components carry `status: generated`, and the CRUD UI treats them as read-only.

Because the REST API is the only path the script supports today, both the work version and the side-project version use it: the variables endpoint plus the file's node tree. That gets you 80% of the way — you lose the live component/code-mapping context Code Connect would give you, but token sync still works.

# 5. Making the agent instructions portable (Claude Code + Copilot)

Since the side project runs on Claude Code and the work repo will likely need Claude Code and/or Copilot: write the actual instructions once, in the tool-agnostic format, and point the tool-specific files at it rather than maintaining two versions.

- **`AGENTS.md` at the repo root is the canonical file.** It's now the broadest-compatibility format — Copilot, Cursor, Codex, Gemini CLI, and others read it natively, and it's stewarded by the Agentic AI Foundation at the Linux Foundation rather than any single vendor. The original target was lean (roughly 20–30 lines): repo purpose, where raw vs. synthesized content lives, the frontmatter/tag schema, and the one command to run (`build_index.py`) after adding a finding. It has grown well past that as scripts, attribution fields and the demo sync were added; the rule now is to keep what an agent needs to act in `AGENTS.md` and move reference detail to `docs/` where possible. Don't duplicate the README into it — that's been shown to measurably hurt agent performance rather than help it.
- **Claude Code is the one holdout that doesn't read `AGENTS.md` natively.** It looks for `CLAUDE.md`. The fix is a one-line `CLAUDE.md` at the root that just imports the real file:

  ```
  @AGENTS.md
  ```

  That's the whole file. Claude Code follows the import and treats `AGENTS.md`'s contents as its own instructions. Add anything *Claude Code–specific* (subagents, hooks, custom skills for this repo) below that import line in `CLAUDE.md` — that content stays out of `AGENTS.md` since Copilot and other tools wouldn't know what to do with it.

- **GitHub Copilot is a separate product from Microsoft 365 Copilot** — worth flagging since it's an easy mix-up. An Office 365 subscription includes M365 Copilot (Word/Excel/Outlook/Teams), which has no concept of a git repo and won't read `AGENTS.md`. GitHub Copilot — the one that reads repo instruction files and would actually work in `agentic-repo` — needs its own seat (GitHub Copilot Business/Enterprise or individual), separate from Office 365. Until/unless that's provisioned, Claude Code is the only agent reading instructions in this repo, on both the work and side-project versions.
- Net effect for now: **`AGENTS.md` + the one-line `CLAUDE.md` import is the whole setup.** No need for `.github/copilot-instructions.md` unless a GitHub Copilot seat gets added later — revisit at that point, not before.

# 6. Research capture and retrieval

**Frontmatter schema** for every file in `raw/` and `findings/` — keep it small and consistent, since this is what the index script and the agent both rely on:

```yaml
---
title: Onboarding flow usability test
date: 2026-09-11
type: usability-test        # usability-test | interview | survey | contextual-inquiry | accessibility-audit | analytics | synthesis
status: raw                 # raw | synthesized | superseded
tags: [onboarding, first-run, mobile]
related_components: [onboarding-carousel, cta-primary]
related_findings: [onboarding.md]
related_analytics: [onboarding-funnel-dropoff.md]
---
```

These are the seven `type` values in `AGENTS.md`. `analytics` is valid for a raw session (for example, a manual dashboard review run as a discovery activity) but not for a finding: analytics is a data source with its own `analytics/summaries/` folder, not a method a finding is synthesized from (§9). `synthesis` belongs to findings, not raw sessions.

**Stub frontmatter** for external-tool artifacts (e.g. `prototypes/`): `type` (distinguishes click-through from coded), `source_type`, and a link to the real artifact, with a short description in the body. Nothing from the source artifact is duplicated.

**Retrieval strategy — two paths, one source of truth.** *(Rewritten 2026-09-30. The original position was that a vector database and embeddings pipeline was very likely overkill for a corpus this size, and that embeddings/RAG should wait for a real scaling problem.)*

**Path 1: an agent working in the repo (unchanged).** Structured search over the compiled `findings/` layer first (grep/glob + frontmatter tags), falling back to `raw/` only to verify or quote something. This is how a Claude Code session answers "did we already test this?"

**Path 2: Ask the Repo (CRUD UI, v1.3.6).** A researcher asks a question in the app; the backend fetches passages from the corpus and a local model (gemma2:9b via Ollama, with nomic-embed-text embeddings) writes a cited answer. It reads the corpus through `export_records.py`, and the repo stays the only source of truth. This path carries the maintenance and quality cost the original plan warned about, which is why it has an evaluation harness.

**What measuring Path 2 taught us.** On a 17-question gold set (10 regression, 7 scenario), the baseline passed 5 of 10 and 0 of 7. Larger local models did worse and ran 4 to 7 times slower. In most failures the evidence the answer needed never reached the prompt: retrieval picked the passage that sounded most like the question, not the one that held the answer. What that means for this repo:

- Raw sessions have to be retrievable, and their corrections have to be visible.
- Findings, toplines and deliverables can't say more than their raw evidence supports, because answers inherit their errors (the v0.5.31 synthesis audit, [`docs/synthesis-audit-2026-09-29.md`](synthesis-audit-2026-09-29.md)).
- Verifying a claim means reading a raw session's whole notes, not one matching passage.

**Still true from the original position:** don't over-build. Path 1 needs nothing beyond the repo's own files, and the repo's content stays Markdown + frontmatter whatever sits on top of it.

`build_index.py` maintains `research/_index.md` (the location shown in the §3 tree): a flat table of topic → tags → related components → last-updated date → which raw sessions back it. That index file is small enough to fit entirely in an agent's context, which means the "ping it in 6 months" query can usually be answered from the index plus one or two finding files, not a full-repo search. The same script also writes `analytics/_index.md` (summary → tool → tags → related findings → last-updated) and an `_index.md` in each deliverable folder.

# 7. Git as the audit trail

This is the part that makes the research side trustworthy rather than just "a chatbot's opinion of what we found":

- Every synthesis is a commit. Commit messages should say what raw evidence triggered the update.
- Never rewrite `raw/` files — if a note was wrong, add a `correction-*.md` file in the session folder that references it, don't edit history.
- `findings/` files can be freely revised, but git log is the record of *how the conclusion evolved*, which matters when someone asks "didn't we think X six months ago?"

# 8. Suggested build order

**Status (2026-09-30):** steps 1–4 are done. Step 5 (Figma MCP swap for the side project) is still future work. Step 6 was overtaken by events: retrieval is now two paths (§6).

1. **Repo skeleton + frontmatter/tag schema + `AGENTS.md`/`CLAUDE.md` pointer** — get the shape right before generating content, since restructuring later means rewriting file paths in every cross-reference.
2. **`new_research_session.py`** — lowers the friction for capturing raw notes, which is the step most likely to get skipped under deadline pressure.
3. **Token sync (`sync_figma_tokens.py`) against the REST API first**, DTCG output only — get the design ops half producing something real before layering MCP on.
4. **`build_index.py`** — once you have a handful of real findings files, not before (no point indexing an empty repo), including the tag-glossary validation.
5. **Swap in Figma MCP** for the side project once available, add Code Connect component mapping.
6. **Retrieval** — originally "re-evaluate only if/when keyword + index search starts missing things." In practice Ask the Repo added embeddings-based retrieval on top of the repo (§6).

# 9. Decisions locked in

- Design tokens live in the same repo as research, in their own top-level folder (`design-tokens/`), not a separate repo.
- Repo shape mirrors the existing work layout: root `docs/`, `research/` (raw + findings + scripts), plus the new `design-tokens/` folder.
- Tagging is explicit: frontmatter tags per file, validated against a canonical glossary file.
- `AGENTS.md` is the single source of truth for agent instructions; `CLAUDE.md` is a one-line import so Claude Code picks it up. No GitHub Copilot instruction file needed for now — Office 365 provides M365 Copilot, not GitHub Copilot, and only Claude Code is reading this repo on either the work or side-project side.
- **Analytics/quant data gets its own top-level sibling folder, `analytics/`, not a `type: analytics` finding.** Same rationale as `design-tokens/`: different cadence, different source of truth. It uses the same raw/summaries split as `research/`. Findings and analytics summaries cross-reference each other via `related_analytics` (in findings frontmatter) and `related_findings` (in analytics summaries frontmatter) rather than one absorbing the other's content. `analytics` is dropped from the `type` enum in §6 since it described a data source, not a research method.
- **Every notional deliverable type gets its own top-level folder** (decided 2026-09-14), rather than grouping several types under one folder. See §3.
- **External-tool artifacts are Markdown stubs** with `source_type`/link frontmatter and a short description, not full copies (2026-09-14). **Click-through and coded prototypes share one `prototypes/` folder**, distinguished by a `type` field (2026-09-14).
- **Corpus changes are authored in `agentic-repo` only**, on a branch, with the repo's checks run before merge. Local clones used by other tools (e.g. the CRUD UI) are read-only copies and never the place to edit content.
- **The public demo runs against a separate demo repo, never the real `agentic-repo`** (2026-09-16). A GitHub Actions workflow in the real repo (scheduled, plus manual run) syncs the curated content to the demo repo using a PAT scoped only to that repo; the demo server holds only a fetch-only credential and resets its checkout to a baseline tag on an hourly cron. For a client environment this needs that platform's equivalent (scoped deploy token/service account and its CI secrets store).
- **Fictional sample content is checked against the real repo before it's treated as done** (2026-09-14): (1) `related_findings` / `related_analytics` values must match real filenames, (2) tags must respect the glossary's own guidance (e.g. no onboarding/first-run drift), (3) fictional entity names get grepped against the full dataset for collisions before use.
- **`SETUP.md` covers general-purpose Windows setup only** (2026-09-14; written 2026-09-30 as [`docs/SETUP.md`](SETUP.md), labeled untested on Windows): venv activation, `python` vs `python3`, PowerShell execution policy, `.gitattributes` line endings. Client/company IT restrictions get documented only once actually encountered.
- ~~Project decisions are tracked outside the repo.~~ **Superseded (2026-09-30):** decisions are now logged in [`docs/decisions.md`](decisions.md), because the repos are the source of truth and must hold enough to build the project.
- **Retrieval is two paths over one source of truth** (2026-09-30): structured search over `findings/` and the index for an agent working in the repo, and Ask the Repo (local RAG) for researchers using the app. See §6.

# 10. Still open

- **Corrections and retrieval:** raw correction files aren't visible to retrieval, and some demo and Ask questions lack real raw evidence.
- **Retrieval:** not yet decided whether the in-repo agent path needs the same evidence-retrieval treatment as Ask the Repo (raw-first verification). A deliberate corpus-level comparison of the two paths stays future work, if one is still wanted.
- **Later:** Figma MCP swap, ingesting additional source formats.