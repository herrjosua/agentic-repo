---
title: Interview — Family Physician on the Plan Section and Medication Changes at Sign-Off
date: 2026-03-24
type: interview
status: raw
researcher: Priya Patel
tags:
  - ambient-scribe
  - documentation
  - medication-safety
  - clinician-workflow
  - trust-in-ai
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/ambient-scribe.md
---

# Interview — Family Physician on the Plan Section and Medication Changes at Sign-Off

## Objective
Earlier ambient-scribe sessions tested medication accuracy in drafts: dosage errors in v0.1 and v0.2, sound-alike drug names at the GA release candidate, and a concept for a distinct sound-alike medication flag (2026-02-10). The plan section has so far come up only from the reader's side: a care coordinator goes straight to the plan and the medication list in the visit notes they read before an outreach call (2026-03-03-interview-care-coordinator-chart-review-scribe-notes/session-notes.md:31, :43), and the 2026-03-17 clinic nurse interview (2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes) heard that plan items sometimes land in the body of the note rather than the plan (2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md:30). None of those sessions asked the person who signs the draft how they check the plan section, where decisions made during the visit, including medication changes, are supposed to end up. This session asked a family physician, two months after the January 2026 GA, how they check the plan and the medication lines in a draft before they sign.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is a family medicine physician in an ambulatory primary care clinic, mid-career. They opted in to the ambient scribe after the January 2026 GA. The scribe drafts the visit note only; the clinician enters orders, including medication orders, separately. Low-confidence transcription is shown with a subtle underline. The distinct sound-alike medication flag tested on 2026-02-10 has not shipped; there is no distinct medication marking beyond the confidence underline. They did not take part in any earlier session. This is an interview about their own practice; nothing was shown or observed.

## Key Findings
- **[HIGH]** *(plan section)* When a decision is talked through over several minutes, the draft sometimes puts the reasoning in the assessment and only part of the decision in the plan, or leaves a follow-up interval in the body of the note. Before signing they read the plan against what they remember deciding and move or add items by hand. They put it at "a couple of times on a full clinic day", an informal impression, not a count.
- **[HIGH]** *(medication changes)* They enter medication orders themselves, so they know what they decided; the question at sign-off is whether the note says the same thing. Their main check is that every medication change in the plan matches the order they placed, and that it is written as a decision. When the draft words a change tentatively, as it was discussed rather than as it was decided, they rewrite it. They said they make this check on every medication line, underlined or not.
- **[MEDIUM]** *(sound-alike names)* They recalled one sound-alike drug name since GA, glyburide written where glipizide had been said, and said it was underlined. It is one recollection, not a rate; the GA release-candidate round records sound-alike names as a known, monitored error type (2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:31). They said they would check medication lines against the order whether or not anything marked them, because a wrong name can be heard confidently.

## Representative Quotes
> "I put the order in myself, so I know what I decided. The question is whether the note says the same thing."
> — Physician (Family Medicine), P147

> "'We talked about lowering the dose' isn't a plan. I change it to what we actually did."
> — Physician (Family Medicine), P147

## Recommendations
1. Share with the ambient scribe team that decisions made during the visit, especially medication changes and follow-up intervals, need to reach the plan section, worded as decisions.
2. When drafts are evaluated, check the plan section's completeness against what was decided in the visit, not only transcription accuracy.
3. When the distinct medication flag's design is next reviewed, note that this physician checks every medication line against the order regardless of marking; whether a flag would change that is untested.

## Follow-ups / Open Questions
- How often plan items land outside the plan section is not measured; "a couple of times on a full clinic day" is one physician's impression.
- Whether NPs and PAs, or other physicians, check the plan and medication lines the same way is not known; this is one interview.
- Whether the distinct medication flag would change how signers check medication lines is untested; it has not shipped.

## Related
- Earlier sessions: [2026-01-13 GA release candidate](../2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md), [2026-02-10 medication flag concept](../2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md), [2026-03-03 care coordinator interview](../2026-03-03-interview-care-coordinator-chart-review-scribe-notes/session-notes.md), [2026-03-17 clinic nurse interview](../2026-03-17-interview-clinic-nurse-reading-scribe-drafted-notes/session-notes.md)
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
