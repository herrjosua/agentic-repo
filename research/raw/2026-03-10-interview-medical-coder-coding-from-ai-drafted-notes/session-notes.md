---
title: Interview — Medical Coder on Coding from AI-Drafted Notes
date: 2026-03-10
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - coding
  - documentation
  - ai-generated-content
  - trust-in-ai
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Interview — Medical Coder on Coding from AI-Drafted Notes

## Objective
Two months after the ambient scribe went GA in January 2026, understand how coding from scribe-drafted notes differs from coding notes the physician typed, and what a coder would expect from the AI coding-suggestion concept (tested as a prototype in July 2025, not built or piloted) now that much of the documentation it would read is itself AI-drafted.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** Participant codes outpatient and some inpatient encounters daily and has coded from scribe-drafted notes since GA. They did not take part in the July 2025 usability test; their view of the coding-suggestion concept comes from a walkthrough of the July 2025 screens during this session.

## Key Findings
- **[HIGH]** *(documentation gaps)* Scribe-drafted notes often capture what was discussed in the visit but leave out the specificity coding depends on: laterality, acute vs. chronic, type or stage (they gave heart failure type and CKD stage as examples), and the "due to" link between two conditions. When it's missing the coder has two options, query the physician or code to the unspecified level, and they said they are doing both more often than with notes physicians typed from their own templates. They noted the July 2025 prototype's mismatches were mostly at the specificity level too, and expect a suggester reading these notes to hit the same wall.
- **[MEDIUM]** *(trust in AI-drafted notes)* Nothing in the signed note shows which sentences the scribe drafted and which the physician typed or edited. When a sentence looks off (e.g., a diagnosis in the assessment that nothing else in the note supports), the coder can't tell whether it's a documentation problem worth a query or something the scribe picked up from the conversation that the physician didn't catch at sign-off. They weren't asking for a marker on the permanent chart, just "something I can see while I'm coding".
- **[MEDIUM]** *(query volume)* Coder's impression is that queries back to physicians have gone up since GA, and that physicians are slower to answer queries about notes "they didn't really write". This is qualitative only: they had no count, and no department query data was reviewed in this session.

## Representative Quotes
> "I'm coding off what the doctor says happened. Now I read a sentence and I honestly don't know if the doctor said it or the scribe thing filled it in. Who wrote this? I can't tell you, and I'm the one putting a code on it."
> — Medical Coder (certified), P120

> "If the suggester is reading the same notes I'm reading, it's going to land on unspecified too. It'll just get there faster than me."
> — Medical Coder (certified), P120

## Recommendations
1. Collect the specificity elements coders most often query on scribe-drafted notes (laterality, acuity, type/stage, condition linkage) and share them with the ambient scribe team as input to the drafting prompts and note structure.
2. For the coding-suggestion concept, design for under-specified input: when the note doesn't support a specific code, the tool should say so rather than quietly suggest the unspecified code.
3. Raise with Compliance whether scribe-drafted vs. clinician-edited provenance could be shown in the coding view only, consistent with the CMIO's August 2025 model of no marker on the permanent chart.

## Follow-ups / Open Questions
- Get actual physician query counts from HIM leadership for the months before and after GA, to check the coder's impression.
- Find out whether the scribe's generation metadata is captured at sentence level, and whether it could reach the coding workflow at all.

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
