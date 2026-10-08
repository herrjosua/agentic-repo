---
title: Care Gap Badge
component_id: care-gap-badge
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Care Gap Badge

**Figma node:** `figma://file/compass-ai-design/node/4008:47`

## Variants
- default (do not ship — see notes)

## States
- default
- dismissed/snoozed (requested, not yet built)

## Code mapping
`src/components/Dashboard/CareGapBadge.tsx`

## Related Research Findings
- [Clinician Experience Documentation Burden](../../research/findings/clinician-experience-documentation-burden.md)

## Notes
The 2025-05-06 usability test found the badge color scheme confused with the acuity color-coding already used elsewhere in the EHR, risking a documentation-quality flag being misread as a clinical-acuity flag. The 2026-01-08 status-indicator screening confirmed this component renders status as color-only dots; the v4.1 design-system snapshot (`design-system/v4-1-status-indicator-component.md`) replaces that color-only markup with a shared icon+text `status-indicator`. Whether the new indicator also resolves the confusion with acuity colors isn't recorded.
