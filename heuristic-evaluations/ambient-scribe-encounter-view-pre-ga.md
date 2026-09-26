---
title: "Ambient Scribe Encounter-View — Heuristic Evaluation (Pre-GA)"
date: 2025-12-20
status: final
tags: ["ambient-scribe", "heuristic-evaluation", "sso", "mfa", "documentation"]
related_findings: ["../research/findings/ambient-scribe-post-ga-refinements.md"]
source_type: native
method: "heuristic-evaluation"
evaluator: "Jordan Lee"
scope: "encounter-view and ambient-scribe-widget, pre-GA (ahead of the Jan 2026 GA-candidate usability round)"
severity_scale: "Nielsen 0-4"
---

## Scope
Expert review of `encounter-view` and `ambient-scribe-widget` against Nielsen's heuristics,
conducted ahead of the GA-candidate usability round to catch structural issues that moderated
testing might miss until much later.

## Issues found
| Issue | Heuristic violated | Severity | Location |
|---|---|---|---|
| Session lock during active dictation gives no distinct state — reads identically to an idle timeout with nothing in progress | Visibility of system status | 3 | `encounter-view`, locked state |
| The generic low-confidence underline is the only signal for both "uncertain transcription" and "medication name worth double-checking" | Recognition rather than recall | 2 | `ambient-scribe-widget`, confidence-highlighted variant |
| No way to tell a paused-but-preserved draft from a discarded one without re-authenticating first | Visibility of system status | 3 | `encounter-view`, locked state |

## Recommendations
Prioritize the session-lock state — it's a trust-eroding false signal, not a cosmetic gap, and
this expert-review pass predates any direct observation of clinician impact. Flag the
confidence-signal overload as worth a dedicated concept test before shipping any new flag type on
top of the existing generic variant.

## Related Findings
- [Ambient Scribe — Post-GA Refinements](../research/findings/ambient-scribe-post-ga-refinements.md)
