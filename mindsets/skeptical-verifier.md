---
title: "The Skeptical Verifier"
date: 2025-12-01
status: final
designer: Sam Okafor
tags: ["trust-in-ai", "ambient-scribe", "prior-auth", "coding", "him", "project-cross-cutting"]
related_findings: ["../research/findings/him-coding-and-billing.md", "../research/findings/prior-authorization.md", "../research/findings/ambient-scribe-post-ga-refinements.md"]
source_type: native
segment: "Wants explicit, visible verification affordances for any AI output before relying on it"
---

## Overview
**Evidence basis:** Inferred. The segment is the designer's synthesis of `raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md:31`, `raw/2025-04-08-usability-test-prior-auth-ai-v1/session-notes.md:31,34` and `raw/2025-07-29-usability-test-ai-coding-billing-suggestions/session-notes.md:28,37`; no session states it. Confidence signals are from `raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md:32,43` and `raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md:36-37`. The as-of notes are from `raw/2026-06-23-interview-medical-coder-review-override-habits/session-notes.md:31,33`, `raw/2026-03-19-interview-primary-care-physician-incidental-content-at-sign-off/session-notes.md:32`, `raw/2026-06-30-interview-rheumatologist-medication-lines-in-scribe-drafts/session-notes.md:31`, `raw/2026-07-28-interview-orthopedics-physician-assistant-exam-findings-in-scribe-drafts/session-notes.md:29` and `raw/2026-09-22-interview-returning-internal-medicine-physician-edits-and-trust-over-time/session-notes.md:31`.

Not a persona — an attitudinal segment, the designer's synthesis of three sessions, seen in
physicians, utilization review nurses and coders in 2025. It was first raised as a pattern in
prior-auth v1, where "show your work" was mentioned unprompted by 3 of 4 (2025-04-08 `:31`),
before `him-coding-and-billing.md`'s "show your work" observation.

## Implications
Doesn't want AI output hidden or auto-applied — wants citations, confidence signals, or an
audit-visible human-decision boundary before trusting a draft, whether that draft is a prior-auth
justification, a coding suggestion, or a transcribed note. Confidence signals were the 2025-09-23
study's recommendation (`:43`), which P09 then welcomed in the GA-candidate round (2026-01-13
`:36`). Design response should default to
visible, checkable provenance rather than trying to earn trust through accuracy alone — this
echoes the ambient-scribe finding that accuracy improvements alone didn't change reading behavior
for this same kind of user.

As of 2026-09-22: a coder said that under quota, on a simple, single-diagnosis chart, the
suggested code would probably be accepted as shown unless something jumped out, and the citation
opened only when a suggestion looks off (2026-06-23 `:31`, `:33`). And visible signals only cover
what they mark: four later interviews describe errors in lines the confidence underline doesn't
mark (2026-03-19 `:32`, 2026-06-30 `:31`, 2026-07-28 `:29`, 2026-09-22 `:31`).
