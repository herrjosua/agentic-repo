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
tags: [...]
related_components: [...]
related_findings: [...]
related_analytics: [...]
```

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

## Git discipline
Every synthesis is its own commit; say what raw evidence triggered the change. Never rewrite
`raw/` or `analytics/raw/` file history.