---
title: Interview — Rheumatologist on Medication Lines in Scribe Drafts
date: 2026-06-30
type: interview
status: raw
researcher: Priya Patel
tags:
  - ambient-scribe
  - documentation
  - medication-safety
  - clinician-workflow
related_components:
  - ambient-scribe-widget
related_findings:
  - ../../findings/ambient-scribe.md
---

# Interview — Rheumatologist on Medication Lines in Scribe Drafts

## Objective
Earlier ambient-scribe sessions tested medication accuracy in drafts: dosage errors in v0.1 and v0.2 (2025-02-25-usability-test-ambient-scribe-v01/session-notes.md:30; 2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:31), sound-alike drug names at the GA release candidate (2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:31), and a concept for a distinct sound-alike medication flag (2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md:21-27). Since GA, a family physician in an ambulatory primary care clinic described checking each medication change in the plan against the order they had placed (2026-03-24-interview-family-physician-plan-and-medication-changes-at-sign-off/session-notes.md:28, :32). No raw session dated on or before this one mentions a specialty clinic, rheumatology, a dose taper or a weekly dosing schedule. This session asked a rheumatologist, about six months after the January 2026 GA, how they check the medication lines in a draft when a patient's medication list is long and doses change often.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is a rheumatologist in an ambulatory specialty clinic, mid-career. They opted in to the ambient scribe after the January 2026 GA and use it for most visits. The scribe drafts the visit note only; the clinician enters orders, including medication orders, separately. Low-confidence transcription is shown with a subtle underline. The distinct medication flag tested on 2026-02-10 has not shipped; there is no medication-specific marking beyond the confidence underline. They did not take part in any earlier session, and the researcher did not share what other participants had said. This is an interview about their own practice; nothing was shown or observed.

## Key Findings
- **[HIGH]** *(long lists)* Many of their patients have long medication lists: disease-modifying drugs, a steroid, supplements, and drugs for other conditions managed by other clinicians. At most visits only one or two of those lines change. In the draft, a line that changed at this visit and a line that was only mentioned while going through the list look the same, and the underline marks only where the scribe was unsure what it heard. To find what changed they read the whole medication section against the orders they placed and the patient's current list. They put a long list at "fifteen lines, give or take" for many of their patients, an informal impression, not a count.
- **[HIGH]** *(dose schedules)* In their account, dose changes in their clinic are often schedules rather than a single number: a prednisone taper stepped down over several weeks, or methotrexate taken once a week, where the day matters. They said the draft sometimes keeps the first step of a taper and drops the rest, or writes the methotrexate dose without "weekly". Those lines are usually not underlined, because each word was heard clearly. They rewrite the schedule by hand before signing. They put an incomplete taper at "a few times a month", an informal impression.
- **[MEDIUM]** *(whose dose)* Patients often say what they actually take, which can differ from what was prescribed ("I've been taking half"). The draft records the dose that was said without saying who said it, so a patient's report can read like the clinician's decision. They check whether each dose in the draft is what the patient reported or what they decided, and reword it so the note says which. This is one rheumatologist's practice; whether other clinicians make the same check is not known.
- **[LOW]** *(what would help)* Asked what would help, without being shown anything, they said a way to see which medication lines changed at this visit. That is an expectation; nothing was shown, and the distinct medication flag was not discussed with them.

## Representative Quotes
> "Fifteen medications and one of them changed today. The draft doesn't tell me which one, so I read all fifteen."
> — Physician (Rheumatology), P149

> "It got the first dose right. The rest of the taper just isn't there."
> — Physician (Rheumatology), P149

## Recommendations
1. Share with the ambient scribe team that, in this rheumatologist's account, multi-step dose schedules (tapers, weekly dosing) are where medication lines go wrong without being underlined, because each word is heard clearly.
2. When drafts are evaluated, include specialty-clinic visits with long medication lists and multi-step dose schedules, not only single dose changes.
3. Explore, as an open design question, whether a draft could show which medication lines changed at this visit and whether a dose is the patient's report or the clinician's decision; neither has been designed or tested.

## Follow-ups / Open Questions
- How often a dose schedule is written incompletely is not measured; "a few times a month" is one rheumatologist's impression.
- Whether other specialists, or NPs and PAs in specialty clinics, check medication lines the same way is not known; this is one interview.
- Whether the distinct medication flag, which targets sound-alike names, would help with dose schedules is untested; it has not shipped.

## Related
- Earlier sessions: [2025-02-25 v0.1 usability test](../2025-02-25-usability-test-ambient-scribe-v01/session-notes.md), [2025-09-23 v0.2 usability test](../2025-09-23-usability-test-ambient-scribe-v02/session-notes.md), [2026-01-13 GA release candidate](../2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md), [2026-02-10 medication flag concept](../2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md), [2026-03-24 family physician interview](../2026-03-24-interview-family-physician-plan-and-medication-changes-at-sign-off/session-notes.md)
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md)
