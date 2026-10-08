---
title: Ambient AI Scribe
date: 2026-01-13
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - ambient-scribe
  - documentation
  - ga-release
  - longitudinal
  - usability
  - v0.1
  - v0.2
  - project-ambient-scribe
related_components:
  - ambient-scribe-widget
  - encounter-view
related_findings:
  - governance-and-phi.md
  - clinician-experience-documentation-burden.md
  - ambient-scribe-post-ga-refinements.md
---

# Ambient AI Scribe

## Overview
The ambient AI scribe has moved from a formative concept (v0.1, Feb 2025) through iteration
(v0.2, Sep 2025) to a GA release candidate (Jan 2026). 3 of the original 5 participants
returned for v0.2, and at least one (P09) also took part in the GA-candidate round, for
longitudinal comparison.

- **PHI handling:** The critical draft-retention/audit gap found in v0.1 was fixed by v0.2 and has
  remained stable through the GA candidate — drafts auto-expire after 10 minutes of inactivity and
  the behavior is documented for Compliance. No PHI-handling issues have recurred since.
- **Accuracy:** Medication dosage errors dropped from 3/5 sessions (v0.1) to 1/5 (v0.2); the
  remaining error type is misheard similar-sounding drug names. The GA-candidate round recommended
  treating it as a post-GA monitoring item rather than a pre-GA blocker, and recommended a post-GA
  monitoring dashboard for it; the 2026-02-10 session still refers to that dashboard as recommended.
- **Trust calibration was the hardest problem, and accuracy alone didn't solve it.** Returning
  participants read every line in both v0.1 and v0.2 despite the accuracy improvement between them —
  trust didn't move with correctness. The GA-candidate round introduced per-line confidence
  highlighting, and for the first time participants reported actually skimming high-confidence
  lines. This is the strongest evidence so far that *visible uncertainty*, not raw accuracy, is the
  lever that changes reviewing behavior.
- **Recommendation status:** The GA-candidate session recommends GA release, with sound-alike
  medication errors tracked as a post-GA metric rather than delaying release.

Open thread: this tool's rollout scope has been deliberately kept away from behavioral health /
substance-use encounters — see [scope-boundaries-and-workflow-fit.md](scope-boundaries-and-workflow-fit.md).

## Evidence Trail
- **2025-02-25** — [Usability Test — Ambient AI Scribe Prototype v0.1](../raw/2025-02-25-usability-test-ambient-scribe-v01/session-notes.md) *(`usability-test`)*
- **2025-09-23** — [Usability Test — Ambient AI Scribe Prototype v0.2 (Follow-up)](../raw/2025-09-23-usability-test-ambient-scribe-v02/session-notes.md) *(`usability-test`)*
- **2026-01-13** — [Usability Test — Ambient AI Scribe GA Release Candidate (Final Validation)](../raw/2026-01-13-usability-test-ambient-scribe-ga-release-candidate/session-notes.md) *(`usability-test`)*
- **2026-01-27** — [Dashboard review — Ambient scribe GA candidate adoption](../raw/2026-01-27-dashboard-review-ambient-scribe-ga-adoption/session-notes.md) *(`analytics`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
- [Clinician Experience & Documentation Burden](clinician-experience-documentation-burden.md)
- [Ambient Scribe — Post-GA Refinements](ambient-scribe-post-ga-refinements.md)
