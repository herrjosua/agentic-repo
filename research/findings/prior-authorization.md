---
title: AI-Assisted Prior Authorization
date: 2026-09-17
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - longitudinal
  - nursing
  - prior-auth
  - trust-in-ai
  - usability
  - utilization-management
  - v1
  - v2
  - project-prior-auth
related_components:
  - prior-auth-drafting-panel
related_findings:
  - governance-and-phi.md
---

# AI-Assisted Prior Authorization

## Overview
AI-drafted prior authorization justifications were tested in two rounds (v1, Apr 2025; v2, Nov
2025) with the same utilization review nurse supervisor across both, which mattered for tracking
whether fixes actually landed.

- **v1** surfaced a correctness bug (citing outdated diagnosis codes) serious enough that
  participants said it would likely cause payer denials — not a UX problem, a data-freshness/model
  fix. It also surfaced a durable requirement: nurses want inline citations to the specific chart
  text behind each suggestion ("show your work"), not just a black-box draft.
- **v2**, after both fixes landed, confirmed the outdated-code issue did not recur and that the
  citation feature is actively used (3 of 4 participants checked at least one citation before
  accepting) rather than being ignored as friction.
- **Scope discipline held.** After v1, the team limited pilot scope to "straightforward" cases,
  with the nursing supervisor helping define them, and kept complex cases out of that scope. v2
  tested 2 straightforward and 2 complex cases, and confirmed
  complex cases still aren't ready — validating that the scope limitation, not a rushed fix, was
  the right call. This same "citation transparency" requirement has since shown up independently in
  the medical coding work — see [him-coding-and-billing.md](him-coding-and-billing.md).
- **Time savings:** ~5 min vs. ~15 min manual for straightforward cases, confirmed (not just
  estimated) in v2.
- **2026: the utilization review pilot, from two nurses in it.** A limited pilot of the drafting
  panel has run in the utilization review department since early 2026, on straightforward cases
  only; complex cases stay manual, and it is not generally available or in other departments
  (2026-06-16). P19, returning from v1 (not v2), and P144, who joined the department after both
  tests, use it on their own straightforward cases; neither is the supervisor the tests followed.
  Figures are informal participant estimates. P19 described a straightforward case as "one
  request, one current diagnosis, criteria we see every week" and put roughly half of a week's
  cases as looking like that at intake, but some stop being straightforward once they are into the
  chart, and they finish those by hand (2026-06-16, HIGH). So the scope holds as a rule, but in
  daily work the nurse applies it partway through a case, not in advance as in testing. Both nurses
  open citations on every case: P19 checks the diagnosis and the date of the most recent
  supporting note first (2026-06-16, MEDIUM), and P144 checks that each cited entry says what the
  draft says, not only that it exists (2026-09-17, MEDIUM). That confirms the citation requirement
  outside testing, and shows that a count of citations opened, as in v2, doesn't record what was
  checked. Requests following a claim denial, requests covering several services and long
  histories are still done by hand (2026-06-16, MEDIUM); P144 starts a claim-denial case from the
  denial letter's reason and prepares calls with the health plan by hand (2026-09-17, MEDIUM).
  Still open: how the pilot is performing (no time, accuracy or claim-denial data is recorded; the
  only time figures remain v1's estimate and v2's measurement on 2 straightforward cases), how
  often a case leaves the draft partway through, and whether a submitted request keeps its
  citations.

Status: v2 recommended pilot expansion, strictly within the agreed straightforward-case scope. A
limited pilot on straightforward cases has run in the utilization review department since early
2026 (2026-06-16); whether it has expanded, and how it is performing, is not recorded.

## Evidence Trail
- **2025-04-08** — [Usability Test — AI-Assisted Prior Authorization Drafting (v1)](../raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md) *(`usability-test`)*
- **2025-11-04** — [Usability Test — AI-Assisted Prior Authorization Drafting (v2, Follow-up)](../raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md) *(`usability-test`)*
- **2026-06-16** — [Interview — Returning Utilization Review Nurse on Pilot Case Scope](../raw/2026-06-16-interview-utilization-review-nurse-case-scope/session-notes.md) *(`interview`)*
- **2026-09-17** — [Interview — Utilization Review Nurse on Checking Citations](../raw/2026-09-17-interview-utilization-review-nurse-citation-checking/session-notes.md) *(`interview`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
