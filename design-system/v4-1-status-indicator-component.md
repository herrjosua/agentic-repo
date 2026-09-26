---
title: "Design System — v4.1 Snapshot (Shared Status-Indicator Component)"
date: 2026-01-22
status: final
designer: Sam Okafor
tags: ["design-system", "accessibility", "wcag", "components"]
related_findings: ["../research/findings/accessibility-cross-cutting.md"]
source_type: native
version: "v4.1"
related_style_guide: ""
---

## Overview
Snapshot of the shared component library as of v4.1, adding a single `status-indicator` component
(icon + text-label variants: needs-attention / in-progress / resolved) to replace the three
independent color-only status-dot instances confirmed in
`accessibility-screenings/status-indicator-remediation-screening.md`.

## Components
`status-indicator` (new) — replaces the bespoke dot markup in `care-gap-badge` and
`alert-triage-queue`; the legacy ExtJS admin console's instance is tracked separately since that
console isn't built on this component library. Icon+text pairing keeps the at-a-glance
scannability color gave without relying on color alone, satisfying 1.4.1.

Note: no Compass-AI-specific style guide exists yet to link here as `related_style_guide` —
`style-guide/` currently only holds the unrelated Fernway foundations doc — so that field is left
blank pending one.
