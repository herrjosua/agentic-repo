---
title: AI-Assisted Prior Authorization
date: 2025-11-04
type: synthesis
status: synthesized
tags:
  - longitudinal
  - prior-auth
  - usability
  - utilization-management
  - v1
  - v2
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
- **Scope discipline held.** The team deliberately limited v1 testing to "straightforward" cases
  (defined jointly with the nursing supervisor) and kept complex cases out of scope. v2 confirmed
  complex cases still aren't ready — validating that the scope limitation, not a rushed fix, was
  the right call. This same "citation transparency" requirement has since shown up independently in
  the medical coding work — see [him-coding-and-billing.md](him-coding-and-billing.md).
- **Time savings:** ~5 min vs. ~15 min manual for straightforward cases, confirmed (not just
  estimated) in v2.

Status: recommended for pilot expansion, strictly within the agreed straightforward-case scope.

## Evidence Trail
- **2025-04-08** — [Usability Test — AI-Assisted Prior Authorization Drafting (v1)](../raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md) *(`usability-test`)*
- **2025-11-04** — [Usability Test — AI-Assisted Prior Authorization Drafting (v2, Follow-up)](../raw/2025-11-04-usability-test-prior-auth-ai-v2/session-notes.md) *(`usability-test`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
