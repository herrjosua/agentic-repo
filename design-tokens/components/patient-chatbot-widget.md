---
title: Patient Scheduling Chatbot
component_id: patient-chatbot-widget
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Patient Scheduling Chatbot

**Figma node:** `figma://file/compass-ai-design/node/4055:02`

## Variants
- default

## States
- default
- human-handoff

## Code mapping
`src/components/PatientPortal/SchedulingChatbot.tsx`

## Related Research Findings
- [Patient Scheduling Chatbot](../../research/findings/patient-scheduling-chatbot.md)
- [Rollout And Change Management](../../research/findings/rollout-and-change-management.md)

## Notes
The `human-handoff` state (the 'talk to a person' escape hatch) failed discoverability testing in 2025-06-17 (3/8 participants couldn't find it as a small text link) and needs redesign as a persistent, prominent control before wider rollout.
