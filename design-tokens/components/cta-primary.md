---
title: Primary CTA button
figma_node: "12:412"
---

# Primary CTA button

Standard primary action button. Uses `color.primary.500` /
`color.primary.600` and `radius.button`.

## Variants

- `default`, `disabled`, `loading`

## States

- `rest`, `hover`, `pressed`, `focus`

## Code mapping

- `src/components/Button.tsx` (`variant="primary"`)

## Open note

Usability testing (2026-09-11) found this insufficiently distinct from the
secondary button in the onboarding context specifically — see
`research/findings/onboarding.md`. Not a global issue with this component.
