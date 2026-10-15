---
title: Ambient AI Scribe
date: 2026-01-13
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - ambient-scribe
  - documentation
  - ga-release
  - longitudinal
  - usability
  - v0.1
  - v0.2
  - project-ambient-scribe
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - governance-and-phi.md
  - clinician-experience-documentation-burden.md
  - ambient-scribe-post-ga-refinements.md
---

# Ambient AI Scribe

## Overview
The ambient AI scribe has moved from a formative concept (v0.1, Feb 2025) through iteration
(v0.2, Sep 2025) to a GA release candidate (Jan 2026). 3 of the original 5 participants
returned for v0.2, and at least one (P09) also took part in the GA-candidate round, for
longitudinal comparison.

- **PHI handling:** The critical draft-retention/audit gap found in v0.1 was fixed by v0.2 and has
  remained stable through the GA candidate — drafts auto-expire after 10 minutes of inactivity and
  the behavior is documented for Compliance. No PHI-handling issues have recurred since.
- **Accuracy:** Medication dosage errors dropped from 3/5 sessions (v0.1) to 1/5 (v0.2); the
  remaining error type is misheard similar-sounding drug names. The GA-candidate round recommended
  treating it as a post-GA monitoring item rather than a pre-GA blocker, and recommended a post-GA
  monitoring dashboard for it; the 2026-02-10 session still refers to that dashboard as recommended.
- **Trust calibration was the hardest problem, and accuracy alone didn't solve it.** Returning
  participants read every line in both v0.1 and v0.2 despite the accuracy improvement between them —
  trust didn't move with correctness. The GA-candidate round introduced per-line confidence
  highlighting, and for the first time participants reported actually skimming high-confidence
  lines. This is the strongest evidence so far that *visible uncertainty*, not raw accuracy, is the
  lever that changes reviewing behavior.
- **Recommendation status:** The GA-candidate session recommends GA release, with sound-alike
  medication errors tracked as a post-GA metric rather than delaying release.

Open thread: this tool's rollout scope has been deliberately kept away from behavioral health /
substance-use encounters — see [scope-boundaries-and-workflow-fit.md](scope-boundaries-and-workflow-fit.md).

## Since GA: 2026 Physician, NP and PA Interviews
This section adds 2026 interview accounts and does not revise the findings above; where an account
differs from them, it is labelled. Nine 1:1 interviews between March and October 2026 asked
physicians, NPs and PAs who use the scribe about their own practice: seven new participants (P146
to P149 and P151 to P153) and two returning ones, P118 (Nurse Practitioner) and P09 (Physician,
Internal Medicine), both returning from 2026-01-13-usability-test-ambient-scribe-ga-release-candidate. All nine are ambulatory; there are no inpatient, ED or
behavioral health sessions, and those settings remain a gap. Nothing was shown or observed, and
every figure below is an informal participant estimate, not a count.

- **What gets edited.** One Physician (Internal Medicine) removes things said in the room that they
  would not have written themselves (small talk, a patient's remarks about a relative's health, a family member's
  comments, their own asides) at "most visits, a line or two" (2026-03-19, HIGH). One Physician
  (Family Medicine) moves or adds plan items when a decision talked through over several minutes
  lands partly outside the plan, "a couple of times on a full clinic day" (2026-03-24, HIGH). P09
  said most of their edits now are not misheard words but the order of events in the history, at
  "a few notes most weeks" (2026-09-22, HIGH).
- **Errors the underline doesn't point to (differs from the Overview).** The Overview reads the
  confidence underline as the lever that changes reviewing. In four of these accounts the lines
  that need fixing are usually not underlined, because each word was heard clearly: incidental
  content (2026-03-19), dose schedules (2026-06-30), the side of an exam finding (2026-07-28) and
  the order of events (2026-09-22). The underline marks where the scribe was unsure what it heard
  (2026-03-19, MEDIUM).
- **What is read in full or skimmed.** P118 reads the assessment and plan in full on every draft
  and skims history sections where nothing is underlined, at "a minute or two a note"
  (2026-05-26, MEDIUM). P09 still skims history sections with nothing underlined on routine
  follow-ups and reads the assessment and plan in full; since catching, in the spring, a draft with
  two symptoms in the wrong order and nothing underlined, they read the whole history when a visit
  is about a new problem (2026-09-22, MEDIUM). One Physician (Internal Medicine) reads the whole
  draft to catch incidental content (2026-03-19, MEDIUM), and one Physician Assistant (orthopedics
  clinic) checks the side, then every exam number, then the assessment and plan, reading history
  sections more quickly (2026-07-28, MEDIUM).
- **Returning participants describe their own practice, not a measured change.** P09's account
  can't be compared directly with their earlier sessions, which were moderated tests (2026-09-22).
  P118's skimming can't be compared with January either, because the January round recorded 4 of 6
  participants skimming without saying who (2026-05-26). Asked whether they trust the scribe more than in January, P09 said it
  depends on the section and did not describe their trust as having grown overall (2026-09-22,
  MEDIUM).
- **Medication lines.** One Physician (Family Medicine) checks every medication change in the plan
  against the order they placed, underlined or not, and rewrites changes worded as discussed rather
  than decided (2026-03-24, HIGH); they recalled one sound-alike name since GA, glyburide written
  where glipizide had been said, which was underlined, one recollection and not a rate
  (2026-03-24, MEDIUM). One Physician (Rheumatology) reads the whole medication section of long
  lists to find the one or two lines that changed (2026-06-30, HIGH), rewrites multi-step dose
  schedules the draft writes incompletely, such as a prednisone taper or methotrexate without
  "weekly", at "a few times a month" (2026-06-30, HIGH), and checks whether each dose is the
  patient's report or their own decision (2026-06-30, MEDIUM). The distinct medication flag has
  not shipped; both accounts describe drafts with the confidence underline only.
- **Exam findings.** One Physician Assistant (orthopedics clinic) said the draft sometimes leaves
  the side out of an exam line, or gives every line the side of the main complaint, at "maybe one
  note in ten", and sometimes attaches a number to the wrong movement or drops a minus; they check
  the side on every exam line and every measurement before signing (2026-07-28, HIGH).
- **Queries.** One Physician Assistant (primary care) said most coder and CDI queries they receive
  on scribe-drafted notes ask for acuity or whether one condition is due to another, which they
  decided at the visit but the signed note didn't state outright, at "two or three a week"
  (2026-08-25, HIGH), and that answering days later depends on memory because the note reads as
  complete (2026-08-25, HIGH). They now check the assessment for acuity and condition links before
  signing (2026-08-25, MEDIUM). For the coder and CDI side, see
  [him-coding-and-billing.md](him-coding-and-billing.md).
- **Session lock on shared workstations.** One Nurse Practitioner (primary care) is locked out when
  the idle timeout fires while they are at the exam table, "most afternoons, at least once"; the
  widget shows no message, and they re-authenticate and scroll through the draft before saying
  more (2026-04-28, HIGH). Because they don't know what happens to an in-progress draft if a
  colleague signs in on the shared workstation during a lock, they stop the scribe before leaving
  the room, which splits one visit across several recordings (2026-04-28, HIGH). The paused state
  has not shipped.
- **Opting in.** One Physician (Internal Medicine resident) did not opt in at GA: writing their own
  notes was how they worked out their assessment while learning, and they did not describe doubt
  about the draft's accuracy as a reason (2026-10-08, MEDIUM). They opted in "about three months
  into clinic" and still write the assessment themselves for a new problem (2026-10-08, MEDIUM).
  One resident's account can't explain the attending/resident adoption gap in the 2026-01-27
  dashboard review.
- **NPs and PAs.** P118, the Physician Assistant (orthopedics clinic) and the Physician Assistant
  (primary care) did not describe anything that works differently for them as an NP or PA
  (2026-05-26, 2026-07-28, 2026-08-25, LOW).

## Evidence Trail
- **2025-02-25** — [Usability Test — Ambient AI Scribe Prototype v0.1](../raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md) *(`usability-test`)*
- **2025-09-23** — [Usability Test — Ambient AI Scribe Prototype v0.2 (Follow-up)](../raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md) *(`usability-test`)*
- **2026-01-13** — [Usability Test — Ambient AI Scribe GA Release Candidate (Final Validation)](../raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md) *(`usability-test`)*
- **2026-01-27** — [Dashboard review — Ambient scribe GA candidate adoption](../raw/2026-01-27-dashboard-review-ambient-scribe-ga-adoption/session-notes.md) *(`analytics`)*
- **2026-03-19** — [Interview — Primary Care Physician on Incidental Content in Scribe Drafts](../raw/2026-03-19-interview-primary-care-physician-incidental-content-at-sign-off/session-notes.md) *(`interview`)*
- **2026-03-24** — [Interview — Family Physician on the Plan Section and Medication Changes at Sign-Off](../raw/2026-03-24-interview-family-physician-plan-and-medication-changes-at-sign-off/session-notes.md) *(`interview`)*
- **2026-04-28** — [Interview — Nurse Practitioner on Session Lock and Shared Exam-Room Workstations](../raw/2026-04-28-interview-nurse-practitioner-session-lock-shared-workstations/session-notes.md) *(`interview`)*
- **2026-05-26** — [Interview — Returning Nurse Practitioner on Champion Training and Review Habits](../raw/2026-05-26-interview-returning-nurse-practitioner-training-and-review-habits/session-notes.md) *(`interview`)*
- **2026-06-30** — [Interview — Rheumatologist on Medication Lines in Scribe Drafts](../raw/2026-06-30-interview-rheumatologist-medication-lines-in-scribe-drafts/session-notes.md) *(`interview`)*
- **2026-07-28** — [Interview — Orthopedics Physician Assistant on Exam Findings in Scribe Drafts](../raw/2026-07-28-interview-orthopedics-physician-assistant-exam-findings-in-scribe-drafts/session-notes.md) *(`interview`)*
- **2026-08-25** — [Interview — Primary Care Physician Assistant on Coder and CDI Queries](../raw/2026-08-25-interview-primary-care-physician-assistant-coder-and-cdi-queries/session-notes.md) *(`interview`)*
- **2026-09-22** — [Interview — Returning Internal Medicine Physician on Edits and Trust Over Time](../raw/2026-09-22-interview-returning-internal-medicine-physician-edits-and-trust-over-time/session-notes.md) *(`interview`)*
- **2026-10-08** — [Interview — Internal Medicine Resident on Opting In to the Scribe](../raw/2026-10-08-interview-internal-medicine-resident-opting-in-to-the-scribe/session-notes.md) *(`interview`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
- [Clinician Experience & Documentation Burden](clinician-experience-documentation-burden.md)
- [Ambient Scribe — Post-GA Refinements](ambient-scribe-post-ga-refinements.md)
