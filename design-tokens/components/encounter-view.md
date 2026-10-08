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
The `locked` state's interaction with an in-progress ambient scribe recording was flagged as an open edge case in the 2025-05-20 SSO/MFA interview and studied in the 2026-02-17 contextual inquiry: a session lock mid-recording freezes the ambient-scribe widget with no message, and all 4 shadowed clinicians assumed the draft was lost, even though it survives server-side (the session notes say "4 of 5"; see that folder's `correction-2026-09-27.md`). A recovery flow with an explicit paused, draft-preserved state is designed and in review (`user-flows/ambient-scribe-session-lock-recovery.md`); it isn't reflected in this component's states yet.
