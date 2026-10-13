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

Since reaffirmed and extended by the 2026 HIM interviews. A per-code record of what was suggested and whether the coder accepted, edited or overrode it, with user and timestamp and filterable by status, should be treated as release-blocking (2026-04-21). It should be visible to the coder in the coding view (2026-10-06), to supervisors as per-coder accept, edit and override rates (2026-08-11), and in claim-edit review (2026-07-14). Every suggestion needs a source-text citation down to the specificity level; don't show a suggestion that has no citation (2026-10-06). When the note doesn't support a specific code, say so rather than quietly suggesting the unspecified code (2026-03-10), or offer a draft, non-leading query for CDI instead of a code (2026-05-12). Expect accept-by-default on simple charts under productivity quotas, and test whether showing the citation inline changes how often coders read it (2026-06-23). The generated States list has no `edited` state yet; adding one needs a Figma change, not a hand edit here.
