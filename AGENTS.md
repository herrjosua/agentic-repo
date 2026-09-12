# Agent instructions for agentic-repo

## Structure
- `research/raw/` — append-only. Never edit after creation.
- `research/findings/` — synthesized, living documents. One per topic.
- `research/_index.md` — generated index: topic -> finding -> raw sources -> tags. Rebuild with `research/scripts/build_index.py`.
- `design-tokens/tokens.tokens.json` — canonical source of truth (DTCG format). Never hand-edit.
- `design-tokens/design.md` — generated from tokens.tokens.json. Never hand-edit directly.
- `design-tokens/components/` — one file per component: variants, states, Figma node ref, code mapping.

## Frontmatter schema (research/raw and research/findings)
title, date, type (usability-test | interview | survey | analytics | synthesis),
status (raw | synthesized | superseded), tags, related_components, related_findings

## Workflow
After adding or editing a finding, run `research/scripts/build_index.py` to refresh the index.
Tags must exist in `research/findings/tags.md` — do not introduce a new tag without adding it there first.
