---
title: ED Intake Form
component_id: ed-intake-form
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# ED Intake Form

**Figma node:** `figma://file/compass-ai-design/node/4071:04`

## Variants
- clinical-triage
- registration

## States
- default

## Code mapping
`src/components/ED/IntakeForm.tsx`

## Related Research Findings
- [Scope Boundaries And Workflow Fit](../../research/findings/scope-boundaries-and-workflow-fit.md)

## Notes
No AI feature is currently scoped against this component for ED intake nurses during peak hours, per the 2025-04-22 finding on interruption frequency. The registration clerk's insurance-card photo pre-fill idea is a separate, smaller candidate not yet built here.

Revisited in 2026, still with nothing scoped: the intake nurse from that study described peak interruptions as unchanged and starts the paper triage sheet at the top of every peak shift, so anything scoped here must work alongside paper and survive re-entry from it; post-peak re-entry, not intake itself, is where they saw a tool might help most (2026-04-14). An ED charge nurse confirmed the boundary covers peak hours, not the whole shift (2026-05-19). Whether the pre-fill idea has been piloted isn't recorded.
