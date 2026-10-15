---
title: "HIM: Coding, Billing & Release of Information"
date: 2026-10-06
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - 42-cfr-part-2
  - ai-generated-content
  - audit-trail
  - billing
  - coding
  - compliance
  - documentation
  - him
  - phi
  - release-of-information
  - training
  - trust-in-ai
  - usability
  - workflow
  - project-him
related_components:
  - coding-suggestion-panel
  - roi-redaction-tool
related_findings:
  - governance-and-phi.md
  - prior-authorization.md
  - scope-boundaries-and-workflow-fit.md
---

# HIM: Coding, Billing & Release of Information

## Overview
Two contextual/usability sessions in HIM (July 2025) surfaced a shared theme — extremely low risk
tolerance for anything that could look like automated judgment on a compliance-sensitive task —
from two different angles: release-of-information redaction, and AI-assisted medical coding. Ten
follow-up interviews (March–October 2026, after the ambient scribe's January 2026 GA) refine both
threads; see "Since GA" below.

- **Release of information (contextual inquiry) is the higher-stakes of the two.** Staff described
  ROI as the one area where a mistake has caused real incidents (wrong record released, or
  behavioral-health notes not correctly given the stricter 42 CFR Part 2 handling). Any AI
  assistance here would need to be "suggest and highlight for human review only," never
  auto-redact-and-release. This session also surfaced a standalone platform gap — there's no
  structured way to flag a note as Part 2-protected in the EHR — that recurred again independently
  in the October behavioral health research (see
  [scope-boundaries-and-workflow-fit.md](scope-boundaries-and-workflow-fit.md)) and was found
  unchanged in ROI (March 2026) and on the coding side (August 2026), making it a gap confirmed in
  three threads (ROI, behavioral health and coding) worth fixing regardless of any AI plans.
- **AI-assisted coding suggestions (usability test) surfaced the same underlying concern in a
  different shape**: the senior coder's objection wasn't accuracy (suggestions matched the coder's
  own independent choice in 14 of 20 test scenarios) but audit posture — they wanted it explicit in
  the UI and audit log that the human coder made the final call, to avoid the suggestion looking
  like it steered toward upcoding. This is the same "show your work" / attribution-of-decision
  pattern seen in prior authorization testing (see [prior-authorization.md](prior-authorization.md)).

Recommendation: any AI feature touching this department needs an explicit, audit-log-visible
human-decision boundary as a baseline requirement, not a design nicety — this shows up whether the
task is redaction, coding, or (per the prior-auth findings) authorization drafting. The 2026
interviews show the boundary is necessary but not sufficient on its own: it has to come with
productivity targets that don't reward unreviewed acceptance, and with someone who can see each
coder's decisions (see below).

## Since GA: 2026 Follow-up Interviews
Ten 1:1 interviews between March and October 2026 (P120–P129, each new to this research) revisited
both threads after the ambient scribe went GA. Neither the coding suggester nor an ROI redaction
tool has been built or piloted, so reactions to the suggester come from walkthroughs of the July
2025 screens. The only CRITICAL finding in the 2026 set is on coding: a coding auditor would
recommend Compliance not sign off on the suggester without a per-code decision record
(2026-04-21). That refines rather than replaces the ROI point above: the Part 2 incident exposure
staff described in July 2025 still stands, and Part 2 handling is still fully manual. Every figure
below is an informal participant estimate, not a count.

- **Accept-by-default under productivity targets.** A production coder said that on simple,
  single-diagnosis charts they would accept a suggested code as shown unless something jumped out,
  as they already do with prompts in their current tools, and tied this to the charts-per-hour
  quota rather than to trust in the tool (2026-06-23, HIGH). On complex charts they would ignore
  suggestions and code from the note, as coders said in July 2025 (2026-06-23, MEDIUM). A coding
  supervisor's main worry was leadership raising targets as soon as a suggester went live, before
  anyone had measured the time saved, with the informal July 2025 estimate of 2–3 minutes per
  simple chart applied to every chart (2026-08-11, HIGH). A senior coder expected that saving to "mostly
  disappear" on all but the simplest visits once citation checks are included (informal guess;
  2026-10-06, MEDIUM). The supervisor recommended keeping targets unchanged during any pilot and
  revisiting them only after measured time per chart, split by simple and complex charts,
  alongside claim denial and rework rates.
- **A per-code decision record, visible to more than auditors.** A coding auditor could not defend
  a code in an external audit or a claim denial appeal without a per-code record of what the tool
  suggested, what the coder accepted or overrode and what they changed it to, with user and
  timestamp; an encounter-level "AI assistance was used" flag isn't enough, and they want the
  record treated as release-blocking (2026-04-21, CRITICAL). For at least the first year they would audit
  codes accepted without edits at a higher rate, "maybe double the usual sample" (informal;
  2026-04-21, MEDIUM), and want the log filterable by acceptance status. A senior coder reached the
  same requirement independently, called it a precondition for using the tool at all, and wants it
  visible to the coder in the coding view (2026-10-06, HIGH). A supervisor wants per-coder accept,
  edit and override rates for training and coaching, not only audit (2026-08-11, MEDIUM), and a
  revenue cycle analyst wants "suggested and accepted" vs. "entered by coder" visible in claim-edit
  review (2026-07-14, MEDIUM). This splits July 2025's accept/override into three outcomes:
  accepted, edited and overridden.
- **Specificity, citations and scribe-drafted notes.** A coder said scribe-drafted notes often
  leave out the specificity coding depends on (laterality, acute vs. chronic, type or stage, and
  the link between conditions), so they query physicians or code to the unspecified level more
  often than with physician-typed notes (2026-03-10, HIGH). A CDI specialist said these notes read
  as complete, which makes gaps harder to spot and costs "a few extra minutes per note" (informal;
  2026-05-12, HIGH). A senior coder would not accept any suggested code without a source citation
  down to the specificity level, partly to check the suggester isn't echoing a sentence the
  physician didn't catch at sign-off (2026-10-06, MEDIUM). The production coder would open a
  citation only when a suggestion looked off, which means least often on the charts they'd accept
  by default (2026-06-23, MEDIUM). When the note doesn't support a specific code, the tool should
  say so rather than quietly suggest the unspecified code (2026-03-10), or offer a draft,
  non-leading query for CDI instead of a code (2026-05-12, MEDIUM). Coders can't see which
  sentences the scribe drafted while coding (2026-03-10, MEDIUM). The coder's sense that physician
  queries have risen since GA is an impression; no query counts were reviewed (2026-03-10, MEDIUM).
- **Claim denials.** A revenue cycle analyst said coding-related claim denials almost never come
  from the wrong code category but from specificity: an unspecified diagnosis, a missing
  laterality or a diagnosis that doesn't support the medical necessity of the procedure, which
  they put at "probably two-thirds or more" of those they work (informal, no report in front of
  them; 2026-07-14, HIGH). They would judge any pilot on the claim denial rate and rework, with
  coder throughput second (2026-07-14, LOW). Separately, coders can't see that a CDI query is
  already open on an encounter, a gap that predates the scribe (2026-05-12, LOW).
- **Release of information since GA.** Two ROI specialists held the suggest-only position: a
  person redacts and a person releases (2026-06-02, MEDIUM; 2026-09-08, HIGH), and each flagged
  item should show why it was flagged (2026-06-02). One would accept batch pre-highlighting, but
  only for low-risk requests where patients ask for their own records, with every record still
  opened, checked and released by a specialist; attorney, insurer and possible Part 2 requests
  stay one at a time (2026-09-08, HIGH). Scribe-drafted notes capture incidental third-party and
  sensitive content said in passing, which has to be found and redacted page by page, in "maybe
  one in five or six" scribe-drafted notes (informal guess, varies by clinic; 2026-06-02, HIGH);
  the specialist worried most about what a tool wouldn't flag. The backlog sits with the
  second-level Part 2 review, which only a few senior specialists can do, and turnaround on those
  requests has slipped from about a week to closer to two (informal; 2026-03-31, MEDIUM).
  Turnaround depends mostly on who is asking: "within a few days" for patients' own recent
  records, about a week for insurers and "often two weeks or more" for attorneys (all informal
  impressions; 2026-09-08, MEDIUM). Whether scribe generation metadata is part of the released
  record is unresolved; see [governance-and-phi.md](governance-and-phi.md) (2026-06-02, HIGH).
- **Part 2 knowledge still lives on a printed sheet.** ROI specialists identify Part 2 records from
  memory and a printed sheet of clinics and note types, and send any substance-use mention to the
  stricter review to be safe (2026-03-31, HIGH). Coders use an adapted version of the same sheet to
  know what not to copy into queries, and nobody owns keeping it current (2026-08-11, MEDIUM). Both
  said scribe-drafted notes can capture more of that content.

From the signer's side, outside the ten interviews above: one Physician Assistant (primary care)
said most coder and CDI queries they receive on scribe-drafted notes ask for acuity or whether one
condition is due to another, which they decided at the visit but the signed note didn't state
outright, at "two or three a week" (informal impression; 2026-08-25, HIGH); see
[ambient-scribe.md](ambient-scribe.md).

## Evidence Trail
- **2025-07-15** — [Contextual Inquiry — Health Information Management (Release of Information)](../raw/2025-07-15-contextual-inquiry-him-release-of-information/session-notes.md) *(`contextual-inquiry`)*
- **2025-07-29** — [Usability Test — AI-Assisted Medical Coding Suggestions](../raw/2025-07-29-usability-test-ai-coding-billing-suggestions/session-notes.md) *(`usability-test`)*
- **2026-03-10** — [Interview — Medical Coder on Coding from AI-Drafted Notes](../raw/2026-03-10-interview-medical-coder-coding-from-ai-drafted-notes/session-notes.md) *(`interview`)*
- **2026-03-31** — [Interview — HIM Supervisor on ROI Volume and Part 2 Handling](../raw/2026-03-31-interview-him-supervisor-roi-volume-and-part-2/session-notes.md) *(`interview`)*
- **2026-04-21** — [Interview — Coding Auditor on Override Tracking and Audit Trail](../raw/2026-04-21-interview-coding-auditor-override-audit-trail/session-notes.md) *(`interview`)*
- **2026-05-12** — [Interview — CDI Specialist on Documentation Gaps in AI-Drafted Notes](../raw/2026-05-12-interview-cdi-specialist-documentation-gaps/session-notes.md) *(`interview`)*
- **2026-06-02** — [Interview — HIM Specialist on Releasing AI-Drafted Notes](../raw/2026-06-02-interview-him-specialist-roi-ai-drafted-notes/session-notes.md) *(`interview`)*
- **2026-06-23** — [Interview — Medical Coder on Review and Override Habits](../raw/2026-06-23-interview-medical-coder-review-override-habits/session-notes.md) *(`interview`)*
- **2026-07-14** — [Interview — Revenue Cycle Analyst on Claim Denials and Coding](../raw/2026-07-14-interview-revenue-cycle-analyst-claim-denials/session-notes.md) *(`interview`)*
- **2026-08-11** — [Interview — HIM Supervisor on Coding Team Oversight](../raw/2026-08-11-interview-him-supervisor-coding-team-oversight/session-notes.md) *(`interview`)*
- **2026-08-25** — [Interview — Primary Care Physician Assistant on Coder and CDI Queries](../raw/2026-08-25-interview-primary-care-physician-assistant-coder-and-cdi-queries/session-notes.md) *(`interview`)*
- **2026-09-08** — [Interview — HIM Specialist on ROI Request Turnaround](../raw/2026-09-08-interview-him-specialist-roi-request-turnaround/session-notes.md) *(`interview`)*
- **2026-10-06** — [Interview — Senior Medical Coder on AI Coding Suggestions](../raw/2026-10-06-interview-senior-medical-coder-ai-suggestions-concept/session-notes.md) *(`interview`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
- [AI-Assisted Prior Authorization](prior-authorization.md)
- [Scope Boundaries & Workflow Fit](scope-boundaries-and-workflow-fit.md)
