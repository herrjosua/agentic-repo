---
title: Usability Test — AI-Assisted Medical Coding Suggestions
date: 2025-07-29
type: usability-test
status: raw
tags:
  - coding
  - billing
  - usability
  - him
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Usability Test — AI-Assisted Medical Coding Suggestions

## Objective
Test an AI tool that suggests ICD-10/CPT codes based on chart documentation, to see if it speeds up coding without introducing compliance risk (upcoding/downcoding).

## Method
- **Method:** Moderated usability test, 5 chart scenarios, 60 min/session
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(compliance risk perception)* Senior coder immediately flagged that an AI suggesting codes could be seen as steering toward upcoding if not carefully positioned, and wanted explicit documentation that the human coder made the final call, not the AI, in case of an audit.
- **[MEDIUM]** *(accuracy)* Suggested codes matched the coder's own independent choice in 14 of 20 test scenarios across participants; mismatches were mostly specificity-level (e.g., unspecified vs. specified diagnosis) rather than category-level.
- **[MEDIUM]** *(workflow fit)* Coders wanted suggestions ranked/justified with the specific chart text that supports each code, similar to the transparency ask seen in the prior-auth testing.
- **[MEDIUM]** *(speed)* Estimated time savings of 2-3 minutes per chart for straightforward cases; negligible or negative for complex multi-diagnosis charts where coders said they'd ignore the tool anyway.

## Representative Quotes
> "I don't mind a second opinion. I do mind if it looks like the machine picked the code and I just clicked 'accept' — that's an audit nightmare waiting to happen."
> — Medical Coder (certified, senior), P71

> "Show me the sentence in the note that made you suggest that code. If you can't, I don't trust it."
> — Medical Coder, P73

## Recommendations
1. Ensure the UI and underlying audit log make it unambiguous that the human coder is the final decision-maker, with explicit accept/override tracking per code.
2. Add source-text citation for every suggested code, mirroring the transparency pattern requested in prior-auth and chart-review research.

## Follow-ups / Open Questions
- Loop in Compliance on the audit-log design specifically for this feature given the upcoding sensitivity raised.

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
