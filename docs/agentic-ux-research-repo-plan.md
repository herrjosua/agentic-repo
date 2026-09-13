**Status:** Draft for review

**Scope:** Applies to both the work version (Figma MCP not yet available) and the side-project version (Figma MCP available)

# 1. What this is actually solving

Two related problems, one repo:

1. **Research memory.** Findings get captured in the moment, then forgotten. Six months later nobody can answer "did we already test this?" without digging through old decks. You want an agent that can be pinged and pull up the actual finding, with sourcing.
2. **Design ops / tokens.** Figma holds the canonical visual language, but it's opaque to anything outside Figma. You want that translated into a form an agent (and a human skimming git) can read directly — without hand-copying token values every time the file changes.

Both are the same underlying pattern: **turn something that lives in a tool's proprietary format into git-tracked Markdown that an agent can query later.** So one repo, two content types (research notes, design tokens), one retrieval layer.

# 2. Architecture: three layers, not one pile of files

The failure mode with "just dump everything into markdown files" is that six months in, the agent either drowns in raw notes or hallucinates a synthesis it never actually did. The pattern that's held up in practice (this mirrors Andrej Karpathy's "LLM Wiki" approach, and how Claude Code's own CLAUDE.md system is structured) is three layers:

| Layer | Contents | Who/what writes it | Mutability |
| --- | --- | --- | --- |
| **Raw** | Interview transcripts, usability test notes, session recordings' text, raw Figma exports | You, during/right after a session | Append-only, never edited |
| **Synthesized** | Per-topic or per-feature findings, written in your own words, cross-referenced | Agent, on your instruction, reviewed by you | Living — gets revised as new raw evidence comes in |
| **Schema/index** | Frontmatter tags, a top-level index file, a glossary of recurring terms/personas | Script (Python) + agent | Regenerated, not hand-maintained |

The reason this matters for your "ping it in 6 months" use case: if you only have raw notes, the agent has to re-derive the finding every time and may derive it differently each time. If you only have synthesized notes with no raw layer, you can't audit *why* the agent concluded something, and corrections don't have anywhere to attach. Keep both, and keep them visibly separate.

# 3. Proposed repo structure

Matches the shape you're already using on the work repo (`agentic-repo/` root, `docs/`, `research/`), with design tokens and analytics added as sibling folders rather than separate repos:

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
│       └── sync_figma_tokens.py # pulls via Figma MCP/API, writes tokens.tokens.json + design.md
├── analytics/
│   ├── raw/
│   │   └── YYYY-MM-DD-topic/
│   │       └── snapshot.csv     # untouched export from whatever analytics tool is in use
│   ├── summaries/
│   │   └── <topic>.md           # synthesized interpretation, human-written
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
- **`tokens.tokens.json` is the canonical source**, and `design.md` is a *generated* view of it — never hand-edited. This is the same split Google's DESIGN.md project and the community `designtoken.md` spec use: DTCG JSON for deterministic, tool-interoperable values; a markdown layer on top for the rationale and context an agent needs but a token file can't express (why this shade of blue, when not to use it, what it maps to in code).
- **`AGENTS.md`** is what makes the "ping it in 6 months" step actually work — it tells any agent session, cold, how the repo is organized, what the frontmatter/tag schema means, and where to look first. See §5 for how this plays with Claude Code specifically, and with Copilot on the work side.

# 4. Design tokens pipeline (the Figma Make / design ops piece)

Current state of Figma's MCP server as of this year, since it's moved fast:

- Figma ships an **official MCP server** — originally a local server requiring Figma desktop, now also available as a **remote hosted server** (no desktop app needed). It exposes variables, component structure, styles, and — if you've set up Code Connect — the mapping from a Figma component to your actual code component.
- As of the most recent update, Figma Make integrates with the MCP server too, so an agent can read the underlying code of a Make file, not just the design.
- Token export increasingly lands in **DTCG format** (`$value`/`$type`, stable spec as of late 2025), which is what Figma, Style Dictionary, Tokens Studio, and Penpot all now read/write — so it's the right canonical format to standardize on rather than inventing your own JSON shape.

Pipeline:

1. `sync_figma_tokens.py` calls the Figma MCP server (or REST API as fallback where MCP isn't available yet — i.e., your current work situation) to pull variables/styles.
2. Writes them straight to `tokens.tokens.json` in DTCG format.
3. Runs a generator step that produces `design.md` from that JSON — token values plus whatever rationale/aliasing notes you've added in frontmatter. This is the file the agent actually reads when a research finding references "the primary CTA color" or when you're asking it to check a proposed change against the existing system.
4. Same script (or a sibling) walks components and writes/updates one `.md` per component in `design-tokens/components/`, pulling variant/state data from Figma and the Figma-to-code mapping from Code Connect if you have it set up.

For the work version specifically, since MCP isn't available there yet: steps 1–2 fall back to the plain Figma REST API (variables endpoint), which gets you 80% of the way — you lose the live component/code-mapping context Code Connect would give you, but token sync still works.

# 5. Making the agent instructions portable (Claude Code + Copilot)

Since the side project runs on Claude Code and the work repo will likely need Claude Code and/or Copilot: write the actual instructions once, in the tool-agnostic format, and point the tool-specific files at it rather than maintaining two versions.

- **`AGENTS.md` at the repo root is the canonical file.** It's now the broadest-compatibility format — Copilot, Cursor, Codex, Gemini CLI, and others read it natively, and it's stewarded by the Agentic AI Foundation at the Linux Foundation rather than any single vendor. Keep it lean (roughly 20–30 lines): repo purpose, where raw vs. synthesized content lives, the frontmatter/tag schema, and the one command to run (`build_index.py`) after adding a finding. Don't duplicate the README into it — that's been shown to measurably hurt agent performance rather than help it.
- **Claude Code is the one holdout that doesn't read `AGENTS.md` natively.** It looks for `CLAUDE.md`. The fix is a one-line `CLAUDE.md` at the root that just imports the real file:

```
    [at]AGENTS.md
```

    That's the whole file. Claude Code follows the import and treats `AGENTS.md`'s contents as its own instructions. Add anything *Claude Code–specific* (subagents, hooks, custom skills for this repo) below that import line in `CLAUDE.md` — that content stays out of `AGENTS.md` since Copilot and other tools wouldn't know what to do with it.

- **GitHub Copilot is a separate product from Microsoft 365 Copilot** — worth flagging since it's an easy mix-up. An Office 365 subscription includes M365 Copilot (Word/Excel/Outlook/Teams), which has no concept of a git repo and won't read `AGENTS.md`. GitHub Copilot — the one that reads repo instruction files and would actually work in `agentic-repo` — needs its own seat (GitHub Copilot Business/Enterprise or individual), separate from Office 365. Until/unless that's provisioned, Claude Code is the only agent reading instructions in this repo, on both the work and side-project versions.
- Net effect for now: **`AGENTS.md` + the one-line `CLAUDE.md` import is the whole setup.** No need for `.github/copilot-instructions.md` unless a GitHub Copilot seat gets added later — revisit at that point, not before.

# 6. Research capture and retrieval

**Frontmatter schema** for every file in `raw/`, `findings/`, and `analytics/summaries/` — keep it small and consistent, since this is what the index script and the agent both rely on:

```yaml
---
title: Onboarding flow usability test
date: 2026-09-11
type: usability-test        # usability-test | interview | survey | synthesis
status: raw                 # raw | synthesized | superseded
tags: [onboarding, first-run, mobile]
related_components: [onboarding-carousel, cta-primary]
related_findings: [onboarding.md]
related_analytics: [onboarding-funnel-dropoff.md]
---
```

**Retrieval strategy — don't over-build this.** For a corpus this size (a personal or small-team research archive, not thousands of documents), a vector database and embeddings pipeline is very likely overkill and adds a maintenance burden (re-embedding on every edit, drift between the index and the files). The better-fit pattern, matching what's worked for markdown-based agent knowledge bases at this scale: let the agent do a **structured search over the compiled `findings/` layer first** (grep/glob + frontmatter tags), fall back to `raw/` only when it needs to verify or quote something. Reserve embeddings/RAG for the point where you've actually hit a scaling problem — too many findings files for keyword search to be reliable — rather than building it preemptively.

`build_index.py` maintains `findings/_index.md`: a flat table of topic → tags → related components → last-updated date → which raw sessions back it. That index file is small enough to fit entirely in an agent's context, which means the "ping it in 6 months" query can usually be answered from the index plus one or two finding files, not a full-repo search.

# 7. Git as the audit trail

This is the part that makes the research side trustworthy rather than just "a chatbot's opinion of what we found":

- Every synthesis is a commit. Commit messages should say what raw evidence triggered the update.
- Never rewrite `raw/` files — if a note was wrong, add a correction file that references it, don't edit history.
- `findings/` files can be freely revised, but git log is the record of *how the conclusion evolved*, which matters when someone asks "didn't we think X six months ago?"

# 8. Suggested build order

1. **Repo skeleton + frontmatter/tag schema + `AGENTS.md`/`CLAUDE.md` pointer** — get the shape right before generating content, since restructuring later means rewriting file paths in every cross-reference.
2. **`new_research_session.py`** — lowers the friction for capturing raw notes, which is the step most likely to get skipped under deadline pressure.
3. **Token sync (`sync_figma_tokens.py`) against the REST API first**, DTCG output only — get the design ops half producing something real before layering MCP on.
4. **`build_index.py`** — once you have a handful of real findings files, not before (no point indexing an empty repo), including the tag-glossary validation.
5. **Swap in Figma MCP** for the side project once available, add Code Connect component mapping.
6. **Re-evaluate retrieval** only if/when keyword + index search starts missing things.

# 9. Decisions locked in

- Design tokens live in the same repo as research, in their own top-level folder (`design-tokens/`), not a separate repo.
- Repo shape mirrors the existing work layout: root `docs/`, `research/` (raw + findings + scripts), plus the new `design-tokens/` folder.
- Tagging is explicit: frontmatter tags per file, validated against a canonical glossary file.
- `AGENTS.md` is the single source of truth for agent instructions; `CLAUDE.md` is a one-line import so Claude Code picks it up. No GitHub Copilot instruction file needed for now — Office 365 provides M365 Copilot, not GitHub Copilot, and only Claude Code is reading this repo on either the work or side-project side.
- **Analytics/quant data gets its own top-level sibling folder, `analytics/`, not a `type: analytics` finding.** Same rationale as `design-tokens/`: different cadence, different source of truth. It uses the same raw/summaries split as `research/`. Findings and analytics summaries cross-reference each other via `related_analytics` (in findings frontmatter) and `related_findings` (in analytics summaries frontmatter) rather than one absorbing the other's content. `analytics` is dropped from the `type` enum in §6 since it described a data source, not a research method.

# 10. Still open

- None currently.