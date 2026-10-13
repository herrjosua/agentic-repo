---
title: AI Governance, PHI & Compliance
date: 2026-06-02
type: synthesis
status: synthesized
researcher: Priya Patel
tags:
  - ai-generated-content
  - ai-strategy
  - audit-trail
  - cmio
  - de-identification
  - executive
  - governance
  - hipaa
  - kickoff
  - legal-record
  - phi
  - privacy
  - retro
  - roadmap
  - year-end
  - project-cross-cutting
related_components: []
related_findings:
  - ambient-scribe.md
  - scope-boundaries-and-workflow-fit.md
  - ambient-scribe-post-ga-refinements.md
  - him-coding-and-billing.md
---

# AI Governance, PHI & Compliance

## Overview
This is the connective tissue for the whole program: four sessions across the year — two
executive-level sessions, the initial kickoff (Jan 2025) and the year-end retro (Dec 2025), with a
Privacy Officer interview (Mar 2025) and a CMIO interview (Aug 2025) in between. Two 2026 HIM
interviews (Apr and Jun 2026) add to the open attestation question below.

- **The shared-metrics gap identified in January was real and took all year to close.** At kickoff,
  the CIO and VP Clinical Informatics couldn't agree on what "success" meant. By December's retro,
  the same two executives (plus Privacy and CMIO) had converged on two headline 2026 metrics:
  documentation time saved, and PHI incidents (target: zero). This is the single clearest before/after
  in the whole research program and should anchor how the 2026 roadmap is framed.
- **De-identification and audit-trail requirements (Privacy Officer, Mar) turned out to be
  non-negotiable engineering constraints, not policy nice-to-haves**: Safe Harbor-level
  de-identification for any fine-tuning/eval data, and model-version + input provenance logging for
  anything that becomes part of the legal record. These constraints were later validated as
  workable by the CMIO's August interview, which proposed a concrete attestation model (once a
  clinician signs AI-assisted content, it carries the same liability as if they'd typed it, with
  generation metadata kept in an internal audit log only) — but that model still needs formal
  Legal/Compliance ratification, it is not yet policy.
- **PHI-sensitivity-ordered rollout sequencing** (lowest-sensitivity workflows first: scheduling →
  admin/coding → documentation → clinical-decision-adjacent) was proposed independently by
  executives in January and reaffirmed by the CMIO in August — it's held up as a stable planning
  principle across two separate conversations eight months apart.
- **A recurring cross-cutting finding was explicitly named as a category, not just fixed three
  times**: the CIO used the color-only status indicator accessibility bug (found independently in
  three separate audits — see [accessibility-cross-cutting.md](accessibility-cross-cutting.md)) as
  the example of a pattern research should flag as such, not file as three unrelated tickets.
- **The attestation model says where generation metadata lives, not who can read it or whether
  it's part of the record.** A coding auditor agreed the metadata should stay off the permanent
  chart, but said "internal" has to include the people who audit codes, not only IT (2026-04-21,
  HIGH). They also want a per-code record of what an AI coding suggester suggested and what the
  coder did with it treated as release-blocking (CRITICAL; see
  [him-coding-and-billing.md](him-coding-and-billing.md)). An ROI specialist didn't know whether
  the scribe's drafts or transcripts are part of the designated record set or legal record, or
  whether a requester could ask for them, and had had no ROI guidance on it since GA. One
  attorney's request for "all versions and drafts" of a visit note was escalated, and they didn't
  hear how it was resolved (2026-06-02, HIGH).

Two items still need to move from "informally agreed in a meeting" to an actual governance
document: the 2026 headline metrics, and the AI-content attestation model. Ratifying the
attestation model now also has to settle who can read the internal audit log and whether scribe
generation metadata is part of the designated record set.

## Evidence Trail
- **2025-01-14** — [AI Strategy Kickoff — Executive Alignment Interview](../raw/2025-01-14-stakeholder-interview-ai-strategy-kickoff/session-notes.md) *(`interview`)*
- **2025-03-24** — [Interview — Privacy/Compliance Officer on De-Identification & Audit Trail Requirements](../raw/2025-03-24-interview-privacy-officer-deidentification-requirements/session-notes.md) *(`interview`)*
- **2025-08-12** — [Interview — CMIO on Governance for AI-Generated Content in the Legal Record](../raw/2025-08-12-interview-cmio-ai-generated-content-governance/session-notes.md) *(`interview`)*
- **2025-12-16** — [Executive Steering Committee — Year-End Retro & 2026 Roadmap Input](../raw/2025-12-16-stakeholder-interview-executive-steering-committee-retro/session-notes.md) *(`interview`)*
- **2026-04-21** — [Interview — Coding Auditor on Override Tracking and Audit Trail](../raw/2026-04-21-interview-coding-auditor-override-audit-trail/session-notes.md) *(`interview`)*
- **2026-06-02** — [Interview — HIM Specialist on Releasing AI-Drafted Notes](../raw/2026-06-02-interview-him-specialist-roi-ai-drafted-notes/session-notes.md) *(`interview`)*

## Related Findings
- [Ambient AI Scribe](ambient-scribe.md)
- [Scope Boundaries & Workflow Fit](scope-boundaries-and-workflow-fit.md)
- [Ambient Scribe — Post-GA Refinements](ambient-scribe-post-ga-refinements.md)
- [HIM: Coding, Billing & Release of Information](him-coding-and-billing.md)
