---
title: Interview — Nurse Practitioner on Session Lock and Shared Exam-Room Workstations
date: 2026-04-28
type: interview
status: raw
researcher: Priya Patel
tags:
  - ambient-scribe
  - sso
  - authentication
  - clinician-workflow
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ../../findings/ambient-scribe.md
---

# Interview — Nurse Practitioner on Session Lock and Shared Exam-Room Workstations

## Objective
The 2026-02-17 contextual inquiry found that a session lock during active dictation freezes the ambient-scribe widget with no message, and that all 4 shadowed clinicians assumed the draft was lost and started dictating again, although the draft survives server-side (2026-02-17-session-lock-during-dictation/session-notes.md:38-41, read with correction-2026-09-27.md in that folder). A recovery flow with an explicit paused, draft-preserved state is designed but has not shipped. That session did not look at exam-room workstations shared by several clinicians. This session asked a primary care nurse practitioner, two months later, what a lock looks like in their visits and how a shared workstation affects it.

## Method
- **Method:** 1:1 interview, 45 min
- **Researcher:** Priya Patel
- **Full participant roster:** see `participants.md` in this folder
- **Context:** The participant is a nurse practitioner in an ambulatory primary care clinic, about five years in that role. They use the ambient scribe for most visits. Exam rooms in their clinic have a workstation that clinicians share across the day, signing in with a badge tap. The idle timeout is 10 minutes and is not adjustable per feature (2026-02-17-session-lock-during-dictation/session-notes.md:49-50). The paused state has not shipped, so a lock still freezes the widget with no message. They did not take part in any earlier session, including the 2026-02-17 inquiry. This is an interview about their own practice; nothing was shown or observed.

## Key Findings
- **[HIGH]** *(lock during a visit)* A lock happens to them when they step away from the workstation during a visit, typically for the physical exam, and the idle timeout fires while the scribe is listening. When they come back the widget looks frozen and shows no message. Their practice is to re-authenticate and scroll through the draft to see what is still there before they say anything more. They described learning this after re-dictating a visit summary early on and then finding the original draft intact; that is their account of their own practice, not an observed change. They put locks at "most afternoons, at least once", an informal impression.
- **[HIGH]** *(shared workstations)* Two or more clinicians use the same exam-room workstation on a clinic day, each signing in with a badge tap. They do not know what happens to their in-progress draft if a colleague signs in on that workstation while their session is locked, and they did not want to find out with a patient's visit. So they stop the scribe before leaving a room, even mid-visit, and start it again when they return. That avoids the question but splits one visit across several recordings, which they then have to read as one draft. How the product behaves in that case is not recorded in the corpus and was not settled here.
- **[MEDIUM]** *(framing)* They described the lock as one more sign-in in a day full of them, not as a safety behavior. That matches the framing the 2026-02-17 inquiry recorded ("one more annoying re-login", 2026-02-17-session-lock-during-dictation/session-notes.md:45-48); it is this participant's own description, and the earlier finding was not put to them.
- **[MEDIUM]** *(what would help)* Asked what they would want to see after a lock, without being shown anything, they said a message that the draft is saved and whose session it belongs to. That is an expectation; the paused state has not shipped and was not shown.

## Representative Quotes
> "I come back from the exam table and it's just sitting there. No message. I badge back in and scroll through before I say another word."
> — Nurse Practitioner (primary care), P148

> "Two of us use that room. I don't know what happens to my recording if someone else taps in, so I stop it before I walk out."
> — Nurse Practitioner (primary care), P148

## Recommendations
1. Add the shared exam-room workstation to the review of the paused-state recovery flow: what a clinician sees after a lock when a colleague has signed in on the same workstation.
2. Make sure the paused-state message says whose draft is preserved, not only that a draft is.
3. When the paused state ships, re-test whether clinicians still stop the scribe before leaving a shared room, as well as whether they still re-dictate.

## Follow-ups / Open Questions
- What happens to an in-progress draft when another clinician signs in on the same workstation during a lock is not recorded in the corpus and was not settled here.
- How often locks interrupt a visit is not measured; "most afternoons, at least once" is one nurse practitioner's impression.
- Whether other clinicians stop the scribe before leaving a shared room is not known; this is one interview.
- Whether the paused state changes behavior can only be tested once it ships, as the 2026-02-17 inquiry already noted.

## Related
- Earlier sessions: [2026-02-17 session lock contextual inquiry](../2026-02-17-session-lock-during-dictation/session-notes.md) and its [correction](../2026-02-17-session-lock-during-dictation/correction-2026-09-27.md)
- Synthesized into: [ambient-scribe.md](../../findings/ambient-scribe.md), [encounter-view component Notes](../../../design-tokens/components/encounter-view.md)
