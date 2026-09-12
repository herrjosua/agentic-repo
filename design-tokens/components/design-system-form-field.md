---
title: Form Field (Design System)
component_id: design-system-form-field
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Form Field (Design System)

**Figma node:** `figma://file/compass-ai-design/node/3990:05`

## Variants
- text
- select
- textarea

## States
- default
- focus
- error

## Code mapping
`src/design-system/FormField/FormField.tsx`

## Related Research Findings
- [Accessibility Cross Cutting](../../research/findings/accessibility-cross-cutting.md)

## Notes
The `error` state's message is not yet programmatically associated with its input (missing aria-describedby) per the 2025-07-01 audit — flagged as high priority given how widely this component is used.
