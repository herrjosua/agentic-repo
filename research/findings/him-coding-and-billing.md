---
title: "HIM: Coding, Billing & Release of Information"
date: 2025-07-29
type: synthesis
status: synthesized
tags:
  - billing
  - coding
  - compliance
  - him
  - phi
  - release-of-information
  - usability
  - workflow
related_components:
  - coding-suggestion-panel
  - roi-redaction-tool
related_findings:
  - governance-and-phi.md
---

# HIM: Coding, Billing & Release of Information

## Overview
Two contextual/usability sessions in HIM (July 2025) surfaced a shared theme — extremely low risk
tolerance for anything that could look like automated judgment on a compliance-sensitive task —
from two different angles: release-of-information redaction, and AI-assisted medical coding.

- **Release of information (contextual inquiry) is the higher-stakes of the two.** Staff described
  ROI as the one area where a mistake has caused real incidents (wrong record released, or
  behavioral-health notes not correctly given the stricter 42 CFR Part 2 handling). Any AI
  assistance here would need to be "suggest and highlight for human review only," never
  auto-redact-and-release. This session also surfaced a standalone platform gap — there's no
  structured way to flag a note as Part 2-protected in the EHR — that recurred again independently
  in the October behavioral health research (see
  [scope-boundaries-and-workflow-fit.md](scope-boundaries-and-workflow-fit.md)), making it a
  two-source-confirmed gap worth fixing regardless of any AI plans.
- **AI-assisted coding suggestions (usability test) surfaced the same underlying concern in a
  different shape**: the senior coder's objection wasn't accuracy (14/20 suggestions matched
  independent human judgment) but audit posture — she wanted it explicit in the UI and audit log
  that the human coder made the final call, to avoid the suggestion looking like it steered toward
  upcoding. This is the same "show your work" / attribution-of-decision pattern seen in prior
  authorization testing (see [prior-authorization.md](prior-authorization.md)).

Recommendation: any AI feature touching this department needs an explicit, audit-log-visible
human-decision boundary as a baseline requirement, not a design nicety — this shows up whether the
task is redaction, coding, or (per the prior-auth findings) authorization drafting.

## Evidence Trail
- **2025-07-15** — [Contextual Inquiry — Health Information Management (Release of Information)](../raw/2025-07-15-contextual-inquiry-him-release-of-information/session-notes.md) *(`contextual-inquiry`)*
- **2025-07-29** — [Usability Test — AI-Assisted Medical Coding Suggestions](../raw/2025-07-29-usability-test-ai-coding-billing-suggestions/session-notes.md) *(`usability-test`)*

## Related Findings
- [AI Governance, PHI & Compliance](governance-and-phi.md)
