---
title: Modal (Design System)
component_id: design-system-modal
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Modal (Design System)

**Figma node:** `figma://file/compass-ai-design/node/3990:22`

## Variants
- default
- confirmation

## States
- open
- closing

## Code mapping
`src/design-system/Modal/Modal.tsx`

## Related Research Findings
- [Accessibility Cross Cutting](../../research/findings/accessibility-cross-cutting.md)

## Notes
Correctly traps focus and supports Esc-to-close (an improvement over the legacy admin console modal). Does not yet return focus to the triggering element on close, per the 2025-07-01 audit.
