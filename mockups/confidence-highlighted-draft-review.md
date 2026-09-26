---
title: "Confidence-Highlighted Draft Review — Hi-Fi Mockup (GA Candidate)"
date: 2026-01-05
status: final
designer: Sam Okafor
tags: ["ambient-scribe", "trust-in-ai", "documentation"]
related_findings: ["../research/findings/ambient-scribe.md"]
source_type: native
fidelity: "hi-fi"
figma_url: ""
---

## Overview
Hi-fi visual design for per-line confidence highlighting in the draft-review surface, built for
the Jan 2026 GA-candidate round — the feature that produced the program's clearest
trust-calibration result to date (visible uncertainty, not raw accuracy, changed reviewing
behavior).

## Notes
Three-tier treatment: high-confidence lines render as default text with no marking (deliberately
inviting skimming); medium-confidence lines get a subtle dotted underline; low-confidence lines
get a solid underline plus an on-hover explanation. Deliberately avoids color-only signaling, per
the cross-cutting accessibility finding — the tiers are distinguishable by underline style, not
color alone.
