---
title: Ambient Scribe — Post-GA Refinements
date: 2026-02-17
type: synthesis
status: synthesized
researcher: Priya Patel
reviewed_by: Jordan Lee
tags:
  - ambient-scribe
  - medication-safety
  - sso
  - mfa
  - phi
  - longitudinal
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - ambient-scribe.md
  - governance-and-phi.md
---

# Ambient Scribe — Post-GA Refinements

## Overview
Two follow-up threads opened by [ambient-scribe.md](ambient-scribe.md)'s GA-candidate round and
by an open edge case noted directly in the `encounter-view` component — neither a launch blocker,
both worth closing before they harden into permanent gaps.

- **A distinct sound-alike-medication flag outperforms generic confidence highlighting for this
  specific error class.** The GA-candidate round treated sound-alike medication errors as an
  ongoing monitoring item, relying on the general `confidence-highlighted` variant to surface
  them. A concept test of a dedicated, visually distinct flag found 5 of 6 participants correctly
  recognized it as categorically different from generic low confidence — but also surfaced a new
  risk: 2 of 6 participants said the flag's specificity made them trust *unflagged* medication
  lines more than they should. Any rollout needs to actively counter that over-trust framing, not
  just ship the flag.
- **Session lock during active dictation currently reads as silent data loss, even though it
  isn't.** The `locked` state's interaction with an in-progress recording was flagged as
  unresolved in `encounter-view`'s own notes, sourced from a May 2025 SSO/MFA interview side
  comment. Direct observation confirms the practical impact: 4 of 5 clinicians assumed a locked
  session had destroyed their draft and restarted dictation from scratch, even though the draft
  is preserved server-side. IT Security confirmed the idle-timeout policy itself is fixed, but an
  explicit "paused, draft preserved" state is a UI-only fix, not a policy change.
- Both threads point the same direction: **the underlying safety/reliability behavior is already
  correct (drafts are preserved; sound-alike names are technically detectable) — what's missing is
  UI that tells the clinician that, specifically and distinctly, rather than relying on a generic
  low-confidence signal to carry two very different kinds of meaning.**

## Evidence Trail
- **2026-02-10** — [Usability Test — Ambient Scribe Sound-Alike Medication Flag Concept](../raw/2026-02-10-ambient-scribe-medication-flag-concept/session-notes.md) *(`usability-test`)*
- **2026-02-17** — [Contextual Inquiry — Session Lock During Active Ambient Scribe Dictation](../raw/2026-02-17-session-lock-during-dictation/session-notes.md) *(`contextual-inquiry`)*

## Related Findings
- [Ambient AI Scribe](ambient-scribe.md)
- [AI Governance, PHI & Compliance](governance-and-phi.md)
