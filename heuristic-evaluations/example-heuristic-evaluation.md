---
title: "Onboarding Wizard — Heuristic Evaluation"
date: 2026-02-05
status: final
tags: ["onboarding", "heuristic-evaluation"]
related_findings: ["onboarding"]
source_type: native
method: "heuristic-evaluation"
evaluator: "Jordan Lee"
scope: "6-step onboarding wizard (signup through first workspace created)"
severity_scale: "Nielsen 0-4"
---

## Scope
Full onboarding wizard, steps 1–6, desktop web only.

## Issues found
| Issue | Heuristic violated | Severity | Location |
|---|---|---|---|
| Step 3 wording implies "connect calendar" is optional when it's required | Match between system and real world | 3 | Step 3 |
| No way to go back without losing entered data | User control and freedom | 3 | Steps 2–5 |
| Progress indicator doesn't reflect actual step count on mobile | Consistency and standards | 2 | Sidebar, mobile view |

## Recommendations
Prioritize the step 3 wording fix (matches usability study finding) and the
back-navigation data-loss issue before the mobile indicator fix.
