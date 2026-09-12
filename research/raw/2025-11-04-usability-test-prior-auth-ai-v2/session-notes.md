---
title: Usability Test — AI-Assisted Prior Authorization Drafting (v2, Follow-up)
date: 2025-11-04
type: usability-test
status: raw
tags:
  - prior-auth
  - usability
  - utilization-management
  - v2
  - longitudinal
related_components:
  - prior-auth-drafting-panel
related_findings:
  - ../../findings/prior-authorization.md
---

# Usability Test — AI-Assisted Prior Authorization Drafting (v2, Follow-up)

## Objective
Re-test the prior authorization tool after the outdated-diagnosis-code fix and addition of inline source citations (from April findings), scoped to the 'straightforward' case definition the supervisor helped define.

## Method
- **Method:** Moderated usability test, 4 case scenarios (2 straightforward, 2 complex), 60 min/session
- **Researcher:** J. Alvarez
- **Full participant roster:** see `participants.md` in this folder

## Key Findings
- **[LOW]** *(accuracy (resolved))* The outdated diagnosis code issue from v1 did not recur in any of the 4 test cases; citations now correctly reference the most recent active diagnosis.
- **[LOW]** *(transparency (resolved))* Inline source citations were well-received and used actively — 3 of 4 participants clicked into at least one citation to verify before accepting, which participants described as appropriately fast rather than as friction.
- **[MEDIUM]** *(scope boundary)* On the 2 complex cases (intentionally outside the agreed 'straightforward' scope), the tool still struggled, confirming the supervisor's April instinct that scope limitation was the right call rather than something to fix immediately.
- **[MEDIUM]** *(time savings (confirmed))* For straightforward cases, drafting time was confirmed at ~5 minutes vs. ~15 minutes manual, consistent with April's estimate, now measured directly rather than estimated.

## Representative Quotes
> "This is what I wanted in April. It shows its work, it got the codes right, and it didn't try to be a hero on the complicated case — it basically said 'this one's harder, take the wheel.'"
> — Utilization Review Nurse (supervisor), P17 (returning from v1)

## Recommendations
1. Recommend this tool for pilot expansion within the agreed straightforward-case scope; do not expand scope to complex cases without a separate, dedicated round of model work and testing.
2. Use the clear before/after (v1 to v2) data here as a model for how to communicate iterative improvement to executives, tying back to the January request for shared success metrics.

## Follow-ups / Open Questions
- Define what 'pilot expansion' means concretely — how many nurses, how many weeks, what's the go/no-go metric.

## Related
- Synthesized into: [prior-authorization.md](../../findings/prior-authorization.md)
