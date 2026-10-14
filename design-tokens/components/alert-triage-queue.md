---
title: Alert Triage Queue
component_id: alert-triage-queue
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Alert Triage Queue

**Figma node:** `figma://file/compass-ai-design/node/4041:19`

## Variants
- chronological
- ai-ranked

## States
- default
- override-in-progress

## Code mapping
`src/components/CareCoordination/AlertTriageQueue.tsx`

## Related Research Findings
- [Care Coordination Triage](../../research/findings/care-coordination-triage.md)
- [Accessibility Cross Cutting](../../research/findings/accessibility-cross-cutting.md)

## Notes
Icon touch targets in this component were found at 32px (below the `size.touch-target-min` token of 44px) in the 2025-11-18 mobile accessibility audit. The 2025-08-26 usability test found no way to note why a coordinator overrode the ranking; override-reason capture is designed and in review (`wireflows/alert-triage-override-reason-capture.md`), not built.

Since extended by the 2026 coordinator interviews, with the queue still not built. Group alerts by patient before any ranking is applied, since repeat alerts for the same patient are the main noise for a coordinator on a high-risk panel (2026-08-04). The override reason list is missing the most common reason a coordinator gave for moving an alert: something the patient or a family member said on the phone that isn't in the chart yet. As drafted, that reason would land in "other" (2026-07-07). Reasons need to be one tap rather than free text (2026-07-07). Who sees them is unsettled: a supervisor would use them for coaching as well as model tuning (2026-05-05). Those last points belong to the in-review wireflow, not this component's generated parts.
