---
title: Interview — Medical Coder on Review and Override Habits
date: 2026-06-23
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - coding
  - trust-in-ai
  - audit-trail
  - workflow
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Interview — Medical Coder on Review and Override Habits

## Objective
Understand how a production coder actually reviews and overrides prompts from the tools they already use, and what that suggests about how they would treat suggestions from the AI coding-suggestion concept if it were ever built. The question behind it is whether the human-final-decision model from July 2025 holds up under productivity quotas, or whether accept-by-default would set in on simple charts.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The AI coding-suggestion tool is still a concept from July 2025 and has not been built or piloted; 42 CFR Part 2 handling is still manual. The participant codes mostly outpatient encounters under a daily productivity quota and has coded from scribe-drafted notes since GA. They have not used the suggester; their expectations come from a walkthrough of the July 2025 screens during this session and from how they use the prompts and edits in their current coding tools.

## Key Findings
- **[HIGH]** *(override habits)* On simple charts they already click through the prompts their current tools raise (edit warnings, "are you sure" checks) without reading most of them, because the quota is counted in charts per hour and the prompts are usually right or irrelevant. They expect they would do the same with a suggester: on a simple, single-diagnosis visit the suggested code would probably be accepted as shown unless something jumped out. They said this plainly and without much discomfort, and connected it to the quota, not to trust in the tool.
- **[MEDIUM]** *(complex charts)* On complex, multi-diagnosis charts they said they would ignore suggestions and code from the note as they do now, because checking someone else's list takes longer than building their own. This matches what coders said in the July 2025 test about complex charts.
- **[MEDIUM]** *(citations)* They liked the idea of the source-text citation for each suggested code, but said they would open it only when a suggestion looks off: an unexpected code, an unusual specificity level or a code they wouldn't have thought of. On a routine chart where the suggestion matches what they expected, they wouldn't check it. They pointed out that this means the citation gets looked at least on exactly the charts where they'd be accepting by default.

## Representative Quotes
> "Honestly? If it's a simple visit and the code looks right, I'm clicking accept. I've got a number to hit by the end of the day. The quota wins. It always wins."
> — Medical Coder, P125

## Recommendations
1. Don't assume the human-final-decision model guarantees review. Design for accept-by-default on simple charts, and take that into account in the audit sampling the coding auditor proposed in April 2026 (higher sampling of codes accepted without edits).
2. Raise with HIM leadership whether productivity quotas would need adjusting for charts coded with AI assistance, so the quota doesn't reward unreviewed acceptance.
3. Test whether surfacing the citation inline, rather than behind a click, changes how often coders read it on routine charts.

## Follow-ups / Open Questions
- How are current quotas set, and do they differ for inpatient and outpatient coders?
- Is there existing data on how often coders dismiss prompts in the current tools without changing anything?

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
