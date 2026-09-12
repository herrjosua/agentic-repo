---
title: Accessibility Audit — New Design System Component Library
date: 2025-07-01
type: accessibility-audit
status: raw
tags:
  - accessibility
  - wcag
  - design-system
  - components
related_components:
  - design-system-form-field
  - design-system-modal
related_findings:
  - ../../findings/accessibility-cross-cutting.md
---

# Accessibility Audit — New Design System Component Library

## Objective
Audit the new component library (buttons, form fields, modals, data tables) intended to replace legacy ExtJS components across Compass AI interfaces, before wide adoption.

## Method
- **Method:** Manual WCAG 2.1 AA audit + automated scan (axe), component-by-component
- **Researcher:** J. Alvarez
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(form validation)* Inline error messages on form fields are not programmatically associated with their inputs (missing aria-describedby), so screen reader users aren't told which field has an error or why.
- **[MEDIUM]** *(focus visibility)* Custom-styled buttons have a focus outline that fails the 3:1 non-text contrast requirement against the button's own background in the 'primary' variant.
- **[MEDIUM]** *(modal)* New modal component correctly traps focus and supports Esc to close (improvement over the legacy console audited in March), but does not return focus to the triggering element on close.
- **[LOW]** *(documentation)* Component documentation site doesn't yet include accessibility usage notes for engineers implementing the components.

## Representative Quotes
> "The good news is the modal problem from the legacy audit is actually fixed here. The bad news is we found a new one in forms."
> — Accessibility Specialist (internal), Internal SME

## Recommendations
1. Fix the form-field error association before the library is adopted broadly — this is a common, high-impact pattern used everywhere.
2. Add accessibility usage notes to component documentation as components are adopted, not retroactively.

## Follow-ups / Open Questions
- Re-audit after fixes land, focused specifically on forms and focus-return behavior.

## Related
- Synthesized into: [accessibility-cross-cutting.md](../../findings/accessibility-cross-cutting.md)
