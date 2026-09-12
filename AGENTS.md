# agentic-repo — Agent Instructions

This repo is two things sharing one retrieval layer: a UX research memory (`research/`) and a
design-ops mirror of Figma (`design-tokens/`). Both turn a tool's proprietary format into
git-tracked Markdown you can query directly.

## Where things live
- `research/raw/YYYY-MM-DD-topic-slug/` — one folder per research session (`session-notes.md` +
  `participants.md`). **Append-only. Never edit or rewrite a file here.** If a raw note was wrong,
  add a new file that references and corrects it.
- `research/findings/<topic>.md` — synthesized, living per-topic conclusions. These ARE meant to be
  revised as new raw evidence comes in. Every finding must cite the raw session(s) that back it.
- `research/findings/tags.md` — canonical tag glossary. Before using a new tag, check it's here.
- `research/_index.md` — flat topic → tags → components → last-updated → raw-sources table.
- `design-tokens/tokens.tokens.json` — canonical DTCG token source. Never hand-edit.
- `design-tokens/design.md` and `design-tokens/components/*.md` — generated views of the tokens
  file; treat as read-only output, not source.

## Frontmatter (every file in `raw/` and `findings/`)
```yaml
title: ...
date: YYYY-MM-DD
type: usability-test | interview | survey | contextual-inquiry | accessibility-audit | analytics | synthesis
status: raw | synthesized | superseded
tags: [...]
related_components: [...]
related_findings: [...]
```

## Retrieval strategy
Search `findings/` first (grep/glob + frontmatter tags). Fall back to `raw/` only to verify or
quote a specific session. Do not build or suggest a vector/embeddings pipeline — out of scope until
keyword + tag search actually proves insufficient at scale.

## After adding a finding
Run `research/scripts/build_index.py` to refresh `research/_index.md` (use `--check` in CI to
catch drift, undefined tags, and dangling `related_findings` links without writing).

## Starting a new session
Run `research/scripts/new_research_session.py --title ... --type ... --topic-slug ... --tags ...`
to scaffold a new `raw/YYYY-MM-DD-topic-slug/` folder instead of creating one by hand.

## Git discipline
Every synthesis is its own commit; say what raw evidence triggered the change. Never rewrite `raw/`
file history.
