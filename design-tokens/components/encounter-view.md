---
title: Encounter View
component_id: encounter-view
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Encounter View

**Figma node:** `figma://file/compass-ai-design/node/4021:12`

## Variants
- default
- with-ambient-scribe-panel

## States
- default
- locked (session timeout)

## Code mapping
`src/components/Encounter/EncounterView.tsx`

## Related Research Findings
- [Ambient Scribe](../../research/findings/ambient-scribe.md)

## Notes
The `locked` state's interaction with an in-progress ambient scribe recording is an open edge case flagged by the 2025-05-20 SSO/MFA interview — not yet resolved in this component.
