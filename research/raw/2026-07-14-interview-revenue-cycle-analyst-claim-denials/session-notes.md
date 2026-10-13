---
title: Interview — Revenue Cycle Analyst on Claim Denials and Coding
date: 2026-07-14
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - billing
  - coding
  - compliance
  - audit-trail
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Interview — Revenue Cycle Analyst on Claim Denials and Coding

## Objective
Bring a revenue cycle view into the HIM research: understand where claim denials actually come from on the billing side, how coding contributes, and what a revenue cycle analyst would expect from the AI coding-suggestion concept (July 2025 prototype, not built or piloted) if it were ever built.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The AI coding-suggestion tool is still a concept from July 2025 and has not been built or piloted; 42 CFR Part 2 handling is still manual. The participant works claim denials and claim-edit review on the billing side and routes coding-related denials back to HIM. They had not seen the July 2025 screens before this session.

## Key Findings
- **[HIGH]** *(claim denials)* In their experience, coding-related claim denials almost never come from the wrong code category. They come from specificity: an unspecified diagnosis where the coverage policy wants a specified one, a missing laterality or a diagnosis that doesn't support the medical necessity of the procedure billed. By their own informal estimate "most" of the coding-related denials they work, "probably two-thirds or more", are specificity problems, but they stressed they had no report in front of them. They said this is the same gap coders and CDI described, seen from the claim end, and that it hasn't improved since the scribe went GA.
- **[MEDIUM]** *(audit)* When they review a claim edit or work a denial, they want to see whether a code was suggested by a tool and accepted, or entered by the coder. Today they can see who coded the encounter but nothing about how. If a suggester went live, they'd want that visible in claim-edit review so they can tell whether a pattern of denials is coming from the tool or from a particular coder, which supports the coding auditor's per-code record from April 2026.
- **[LOW]** *(metrics)* Time saved per chart would matter much less to revenue cycle than the denial rate. A tool that made coding faster but held the denial rate flat wouldn't be worth much to them, and one that pushed more charts to unspecified codes faster could make it worse. They'd want any pilot measured on denials and rework, not only coder throughput.

## Representative Quotes
> "It's almost never the wrong family of codes. It's that it's unspecified, or it's missing the side, or the diagnosis doesn't hold up the procedure. That's what bounces. The category's fine."
> — Revenue Cycle Analyst (Billing), P126

## Recommendations
1. If the coding-suggestion concept is pursued, design and evaluate it against specificity, not only category match; the July 2025 test's 14-of-20 match rate counted specificity mismatches as misses, which is the right bar for revenue cycle.
2. Include "suggested and accepted" vs. "entered by coder" in what claim-edit review can see, alongside the per-code audit record.
3. Define pilot success metrics with revenue cycle: coding-related denial rate and rework, with throughput as a secondary measure.

## Follow-ups / Open Questions
- Pull a real breakdown of coding-related claim denials by reason to check the informal "two-thirds or more" estimate.
- Has the coding-related denial rate moved since the scribe went GA in January 2026?

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
