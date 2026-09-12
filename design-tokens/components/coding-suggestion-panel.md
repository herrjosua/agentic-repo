---
title: Medical Coding Suggestion Panel
component_id: coding-suggestion-panel
status: generated
generated_from: Figma (via sync_figma_tokens.py — not yet built; hand-authored here to match intended shape)
---

# Medical Coding Suggestion Panel

**Figma node:** `figma://file/compass-ai-design/node/4061:09`

## Variants
- default

## States
- suggested
- accepted
- overridden

## Code mapping
`src/components/HIM/CodingSuggestionPanel.tsx`

## Related Research Findings
- [Him Coding And Billing](../../research/findings/him-coding-and-billing.md)

## Notes
Audit-log visibility for the `overridden` state is a hard requirement per the 2025-07-29 finding — the human coder's final decision must be unambiguous in both UI and audit log to avoid upcoding-liability concerns.
