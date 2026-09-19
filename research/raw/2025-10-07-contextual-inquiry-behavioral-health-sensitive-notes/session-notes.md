---
title: Contextual Inquiry — Behavioral Health Unit, Sensitive Note Handling
date: 2025-10-07
type: contextual-inquiry
status: raw
tags:
  - behavioral-health
  - 42-cfr-part-2
  - phi
  - sensitive-notes
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/scope-boundaries-and-workflow-fit.md
---

# Contextual Inquiry — Behavioral Health Unit, Sensitive Note Handling

## Objective
Understand how behavioral health documentation is currently handled given its extra legal protections, to determine whether/how any Compass AI documentation tools (like the ambient scribe) could safely extend here, if at all.

## Method
- **Method:** In-person shadowing + informal interview, 1 session, 2 hours
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[HIGH]** *(scope caution)* Clinician was firm that any AI tool listening to or drafting behavioral health session notes raises consent and 42 CFR Part 2 questions well beyond what's been addressed for general medical encounters so far — this population should not be included in any near-term ambient scribe rollout without a dedicated legal/consent review.
- **[HIGH]** *(existing gap)* Reiterates the July HIM finding: there is still no structured way to flag a note as Part-2 protected in the EHR, which independently limits any AI feature's ability to know to treat such notes differently even if it wanted to.
- **[MEDIUM]** *(documentation style)* Behavioral health notes are more narrative and clinically nuanced than typical med-surg notes, which the clinician felt would be especially hard for a generic ambient scribe to draft accurately even setting aside the legal question.

## Representative Quotes
> "I'm not against AI. I'm against AI listening to a session about someone's substance use history before we've even figured out how to flag that note as protected in the first place."
> — Behavioral Health Clinician, P95

> "You'd need a completely separate conversation with legal before this unit is anywhere near a pilot."
> — Behavioral Health Unit Charge Nurse, P97

## Recommendations
1. Formally exclude behavioral health and substance use encounters from any ambient scribe pilot scope until a dedicated legal/consent review is completed — recommend this be an explicit, documented scope boundary in the 2026 roadmap, not just an informal assumption.
2. Escalate the recurring 'no structured way to flag Part 2 notes' finding (now raised independently in two separate research threads, HIM in July and here) as a standalone platform gap worth fixing regardless of AI plans.

## Follow-ups / Open Questions
- Confirm with Legal whether a consent review for this population is even on a timeline, or needs to be requested.

## Related
- Synthesized into: [scope-boundaries-and-workflow-fit.md](../../findings/scope-boundaries-and-workflow-fit.md)
