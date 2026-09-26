---
title: "The Skeptical Verifier"
date: 2025-12-01
status: final
designer: Sam Okafor
tags: ["trust-in-ai", "ambient-scribe", "prior-auth", "coding", "him"]
related_findings: ["../research/findings/him-coding-and-billing.md", "../research/findings/prior-authorization.md", "../research/findings/ambient-scribe-post-ga-refinements.md"]
source_type: native
segment: "Wants explicit, visible verification affordances for any AI output before relying on it — regardless of clinical role"
---

## Overview
Not a persona — an attitudinal segment that recurs across physicians, nurses, and HIM coders
regardless of department or identity, first named explicitly as a pattern in
`him-coding-and-billing.md`'s "show your work" observation.

## Implications
Doesn't want AI output hidden or auto-applied — wants citations, confidence signals, or an
audit-visible human-decision boundary before trusting a draft, whether that draft is a prior-auth
justification, a coding suggestion, or a transcribed note. Design response should default to
visible, checkable provenance rather than trying to earn trust through accuracy alone — this
echoes the ambient-scribe finding that accuracy improvements alone didn't change reading behavior
for this same kind of user.
