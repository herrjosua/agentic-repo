---
title: "Onboarding Wizard — Accessibility Screening"
date: 2026-02-06
status: final
designer: Sam Okafor
tags: ["onboarding", "accessibility"]
related_findings: []
source_type: native
wcag_level: "AA"
scope: "6-step onboarding wizard"
issues_found: 3
---

## Scope
Onboarding wizard, steps 1–6, screened against WCAG 2.1 AA using keyboard-only
navigation and VoiceOver.

## Issues found
| Issue | WCAG criterion | Severity | Location |
|---|---|---|---|
| Calendar-connect button has no accessible label, reads as "button" | 4.1.2 Name, Role, Value | High | Step 3 |
| Focus order skips the "Skip this step" link | 2.4.3 Focus Order | Medium | Step 3 |
| Error message color contrast is 3.2:1, below the 4.5:1 minimum | 1.4.3 Contrast (Minimum) | Medium | Steps 2, 4 |

## Recommendations
Fix the calendar-connect button label first — it's a full blocker for
screen-reader users completing the required step.
