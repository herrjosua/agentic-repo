---
title: Interview — Senior Medical Coder on AI Coding Suggestions
date: 2026-10-06
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - coding
  - trust-in-ai
  - audit-trail
  - ai-generated-content
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
  - ../../findings/prior-authorization.md
---

# Interview — Senior Medical Coder on AI Coding Suggestions

## Objective
Get a senior coder's first reaction to the AI coding-suggestion concept (July 2025 prototype, not built or piloted), seen with fresh eyes, now that coders have been coding from scribe-drafted notes for most of 2026. The question was what would have to be true before a senior coder would use it at all. The participant is a different person from P71, the senior coder in the July 2025 usability test, and from P120 (March 2026 interview). They did not take part in the July 2025 session or any earlier session.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The AI coding-suggestion tool is still a concept from July 2025 and has not been built or piloted; 42 CFR Part 2 handling is still manual. The participant is a senior coder who handles complex inpatient and outpatient encounters, answers other coders' questions and has supported responses to external audits. They have coded from scribe-drafted notes since GA. They had not seen the July 2025 screens before; they reacted to a walkthrough of them during this session.

## Key Findings
- **[HIGH]** *(audit posture)* Before anything else, they wanted it to be clear that the coder makes every coding decision and the tool only suggests. They would want a visible, per-code record of what was suggested and what the coder did with it (accepted, edited or overridden), which they could see themselves while coding, not only something auditors could pull later. They called this the precondition for using the tool at all, not a feature to add later. It matches what the July 2025 senior coder and the April 2026 coding auditor asked for, reached independently.
- **[MEDIUM]** *(citations)* A source citation for every suggested code was non-negotiable for them: the sentence or sentences in the note that support the code, including the specificity. A code without a citation is one they would not accept, however likely it looked. Because so much of the documentation is now scribe-drafted, they said the citation is also how they'd check that the note actually supports the code and that the suggester isn't just echoing a sentence the physician didn't catch at sign-off.
- **[MEDIUM]** *(speed)* Told about the July 2025 estimate of 2-3 minutes saved per simple chart, they said a saving like that matters only if checking a suggestion stays quicker than coding the chart themselves. If they have to open every citation, compare it with the note and then record why they changed a code, they expect the saving to "mostly disappear" on anything but the simplest visits. They saw this as an informal guess, not something they'd measured.

## Representative Quotes
> "The tool can suggest whatever it wants. I'm the one who codes. If the screen doesn't show that, code by code, I'm not touching it."
> — Medical Coder (senior), P129

> "No citation, no code. I don't care how confident it looks. Show me where in the note it's coming from, because half the time now nobody typed that note."
> — Medical Coder (senior), P129

## Recommendations
1. Keep the per-code suggested / accepted / edited / overridden record as a release-blocking requirement, and make it visible to the coder in the coding view as well as to auditors and supervisors.
2. Require a source-text citation, down to the specificity level, for every suggested code. Don't show a suggestion that has no citation. This is consistent with the transparency pattern from prior-auth research.
3. In any pilot, measure the time to review a suggestion, citation check included, not only the end-to-end time per chart, so the 2-3 minute estimate is checked against how coders actually review.

## Follow-ups / Open Questions
- How long does a citation check take in practice? This could be timed in a future test of the concept screens.
- Would senior coders accept a lighter review path for simple charts if sampling caught problems, or is per-code review a hard line?

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md), [prior-authorization.md](../../findings/prior-authorization.md)
