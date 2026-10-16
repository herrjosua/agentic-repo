---
title: Compass AI Practice Setup — Connect Calendar with Fields Read and IT Approval
date: 2026-03-17
status: draft
designer: Priya Patel
tags:
  - onboarding
  - wireframe
  - scheduling
  - phi
  - project-onboarding
related_findings:
  - ../research/findings/compass-ai-practice-setup.md
source_type: native
fidelity: lo-fi
flow_ref: user-flows/compass-ai-practice-setup-five-step-flow.md
---

# Compass AI Practice Setup — Connect Calendar with Fields Read and IT Approval

## Description
**Evidence basis:** Mixed. Observed: the problem and the two recommendations this applies are stated in `raw/2026-02-03-usability-test-compass-ai-practice-setup-flow/session-notes.md:33-34,36-38,51-52,58-59,61-62,67-68,74-76` and `raw/2026-02-24-interview-it-administrator-schedule-access-and-staff-invites/session-notes.md:26,29,36-37,40-41`, and each line below cites its source. Illustrative: the screen's elements and their order are this record's layout; no session saw or tested it.

Lo-fi layout for step 3 of the Compass AI practice setup flow, Connect calendar
([`compass-ai-practice-setup-five-step-flow.md`](../user-flows/compass-ai-practice-setup-five-step-flow.md)),
with two of the recorded recommendations applied:
- "List the fields read from the appointment schedule on the Connect calendar step." (2026-02-03
  `session-notes.md:74`)
- "Add a "Send to IT for approval" path on Connect calendar for an administrator who can't approve
  the access themselves." (`:75-76`) The 2026-02-24 interview recommends the same route:
  "On Connect calendar, route an administrator who can't approve schedule access to IT,
  consistent with the "Send to IT for approval" path recommended on 2026-02-03" (2026-02-24
  `session-notes.md:40`).

No decision on either recommendation is recorded
([readout](../research-readouts/compass-ai-practice-setup-q1-readout.md) `:152`); this wireframe
shows what applying them would put on the screen, not a decision to build it. This is about admin
setup of Compass AI, not staff training.

**The problem it answers.** In the 2026-02-03 usability test, 3 of 4 Practice Administrators (P154,
P155, P157) "stopped at Connect calendar and wouldn't connect it: it gives Compass AI access to
patient appointments, and they did not think they could approve that. Each said it was IT's
decision." P156 asked the moderator whether it was theirs to approve before going on (2026-02-03
`:51`). Both IT Administrators (P158, P159) connected it "only after asking which fields are read
(for example, whether visit reasons are included). The screen doesn't list them" (`:52`).
- "That's patient names and visit reasons. That's not my call — that's IT's." — Practice
  Administrator, P154 (`:58-59`)
- "Is this mine to say yes to? I'd normally send anything like this to IT." — Practice
  Administrator, P156 (`:61-62`)
- "Before I connect it I want to know what it pulls. Times and providers, fine. Visit reasons,
  that's a different conversation." — IT Administrator, P158 (`:67-68`)

In the IT Administrator's account on 2026-02-24, any new system that reads the appointment
schedule needs a privacy review request first, and a Practice Administrator can't start one
(2026-02-24 `:29`): "A practice admin can't put in that request. They call us, we file it. If the
screen just asks them to click connect, it's asking the wrong person." — IT Administrator, P160
(`:36-37`). That is one IT Administrator's account of the process, not a review of its records
(`:26`).

## Details
The screen's elements, in order, and what each is for. Colour, size, type, exact placement and
visual styling aren't specified.

1. **Step name: Connect calendar.** The step's name in the build (2026-02-03 `:33`).
2. **What connecting does.** One statement that connecting gives Compass AI read access to the
   practice's appointment schedule, which is what the step does in the build (`:33-34`).
3. **Fields read (placeholder).** A list of the fields Compass AI reads from the appointment
   schedule, per the first recommendation (`:74`). Left as a placeholder: which fields are read
   isn't on the screen or in the notes (`:52`), and the 2026-02-24 interview recommends confirming
   with IT whether a privacy review request has been filed "and list the fields it covers"
   (2026-02-24 `:41`). The list is filled from that, not from what participants asked about.
   P158's "Times and providers, fine. Visit reasons, that's a different conversation." (2026-02-03
   `:67-68`) is what P158 wanted to know, not a list of fields read.
4. **Connect.** The action that connects the calendar, for an administrator who can approve the
   access. Completing the step stays the only way past it: the build has no "Connect later" and no
   "Skip for now" (`:36-37`), and this wireframe adds neither.
5. **Send to IT for approval.** A second path for an administrator who can't approve the access
   themselves, per the second recommendation (`:75-76`; 2026-02-24 `:40`). What IT receives,
   whether the setup stays open and how the administrator comes back to it aren't recorded or
   designed here; see the wireflow
   ([`compass-ai-connect-calendar-send-to-it.md`](../wireflows/compass-ai-connect-calendar-send-to-it.md)).

Not covered:
- **Who should see which path.** The notes don't record how the screen would tell an
  administrator who can approve from one who can't; this wireframe shows both paths to everyone.
- **Whether the step stays required.** The only rationale on record is the designer's statement
  at session setup that "the calendar step is required because the scribe attaches recordings to
  scheduled encounters" (2026-02-03 `:38`), which no session tested (finding `:42-44`).
