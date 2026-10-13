---
title: Interview — CDI Specialist on Documentation Gaps in AI-Drafted Notes
date: 2026-05-12
type: interview
status: raw
researcher: Priya Patel
tags:
  - him
  - coding
  - documentation
  - ai-generated-content
  - workflow
related_components:
  - coding-suggestion-panel
related_findings:
  - ../../findings/him-coding-and-billing.md
---

# Interview — CDI Specialist on Documentation Gaps in AI-Drafted Notes

## Objective
Understand how scribe-drafted notes have changed clinical documentation integrity (CDI) review since the ambient scribe went GA in January 2026, and how a CDI specialist would want the AI coding-suggestion concept (July 2025 prototype, not built or piloted) to behave when the documentation behind a code is incomplete.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** Participant does concurrent and retrospective CDI review on inpatient and some outpatient encounters and writes physician queries. They work alongside the coding team but sit in a separate queue.

## Key Findings
- **[HIGH]** *(documentation gaps)* Scribe-drafted notes are fluent and well organized, so they read as complete. What's missing (acuity, severity, the clinical indicators that support a diagnosis, the link between conditions) is harder to spot than in a sparse typed note, where a gap was obvious at a glance. They said a scribe-drafted note now takes a more deliberate read, by their own informal count a few extra minutes per note, because they can no longer rely on a note "looking thin" to tell them where to look.
- **[MEDIUM]** *(queries)* Wants the coding-suggestion concept to suggest queries, not codes, when the documentation is incomplete. Their worry is that a suggested code on an under-specified note pushes the coder either to an unspecified code or toward a leading query. They'd want a draft query that states the clinical indicators found and asks the physician to clarify, in non-leading language Compliance has approved.
- **[LOW]** *(workflow)* There is no hand-off signal between CDI and coding. Coders can't see that a CDI query is already open on an encounter, so an encounter sometimes gets coded before the answer comes back, or the physician gets a second, near-duplicate query from the coder. They described this as an annoyance that predates the scribe, not something GA caused.

## Representative Quotes
> "The note sounds finished. That's the problem. It reads like a really good note, and then you go looking for the acuity and it's just not in there."
> — Clinical Documentation Integrity Specialist, P123

> "Don't hand me a code. Hand me the question I should be asking the doctor."
> — Clinical Documentation Integrity Specialist, P123

## Recommendations
1. For under-specified documentation, have the coding-suggestion concept output a draft query routed to CDI instead of a code, with query wording reviewed by Compliance so it stays non-leading.
2. Share CDI's list of the specificity elements most often missing from scribe-drafted notes with the ambient scribe team, alongside the coders' list.
3. Separately from any AI work, look at a simple "query open" indicator on the encounter that coders can see.

## Follow-ups / Open Questions
- Confirm with Compliance which query templates are already approved, and whether AI-drafted query text would need its own review.
- Get CDI query counts for the months before and after GA.

## Related
- Synthesized into: [him-coding-and-billing.md](../../findings/him-coding-and-billing.md)
