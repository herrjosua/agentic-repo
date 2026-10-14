---
title: Prior Authorization Drafting Panel
component_id: prior-auth-drafting-panel
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Prior Authorization Drafting Panel

**Figma node:** `figma://file/compass-ai-design/node/4033:41`

## Variants
- straightforward-case
- complex-case (out of scope)

## States
- drafting
- citation-expanded
- submitted

## Code mapping
`src/components/UtilizationManagement/PriorAuthDraftingPanel.tsx`

## Related Research Findings
- [Prior Authorization](../../research/findings/prior-authorization.md)
- [Him Coding And Billing](../../research/findings/him-coding-and-billing.md)

## Notes
Inline source citations (the `citation-expanded` state) were added directly in response to the 2025-04-08 v1 testing finding that nurses wanted to see the chart text behind each suggestion. Validated as actively used, not ignored, in 2025-11-04 v2 testing.

In the limited utilization review pilot (straightforward cases only, since early 2026), two pilot nurses open citations on every case: one checks the diagnosis and the date of the most recent supporting note first (2026-06-16; the session recommends keeping dates prominent), the other checks that each cited entry says what the draft says (2026-09-17). Cases also leave the panel partway through when they turn out not to be straightforward and are finished by hand (2026-06-16). Whether the `submitted` state keeps its citations, for reuse if the health plan asks about a case later, isn't recorded (2026-09-17).
