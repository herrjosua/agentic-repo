---
title: "Design System — v4.1 Snapshot (Shared Status-Indicator Component)"
date: 2026-01-22
status: final
designer: Sam Okafor
tags: ["design-system", "accessibility", "wcag", "components", "project-design-system"]
related_findings: ["../research/findings/accessibility-cross-cutting.md"]
source_type: native
version: "v4.1"
related_style_guide: ""
---

## Overview
**Evidence basis:** Mixed. Observed (the color-only status pattern, from `raw/2025-03-10-accessibility-audit-legacy-extjs-admin-console/session-notes.md:31` and `raw/2025-11-18-accessibility-audit-mobile-clinician-app/session-notes.md:32,44,47`, with `raw/2025-07-01-accessibility-audit-new-design-system-components/session-notes.md:29-32` recording no such finding; the shared markup in the two components, from `accessibility-screenings/status-indicator-remediation-screening.md:22,25`); illustrative (the component itself is the designer's build, and hasn't been re-screened).

Snapshot of the shared component library as of v4.1, adding a single `status-indicator` component
(icon + text-label variants: needs-attention / in-progress / resolved) to replace the color-only
status-dot markup in the two live components confirmed in
`accessibility-screenings/status-indicator-remediation-screening.md` (`care-gap-badge` and
`alert-triage-queue`). That screening found the two share one underlying markup pattern (`:22`,
`:25`), and that shared root is what this component replaces. The same color-only pattern was
also found in the legacy console (2025-03-10 `:31`) and the mobile app (2025-11-18 `:32`). The
mobile audit counted it in three audits, including the design system (`:44`), but left open
whether one shared root sits behind every surface (`:47`), and the July 2025 design-system audit
records no color-only status finding (2025-07-01 `:29-32`). A shared root beyond these two
components isn't recorded.

## Components
`status-indicator` (new) — replaces the bespoke dot markup in `care-gap-badge` and
`alert-triage-queue`; the legacy ExtJS admin console's instance is tracked separately since that
console isn't built on this component library. Icon+text pairing keeps the at-a-glance
scannability color gave without relying on color alone; intended to satisfy 1.4.1; not yet
re-screened.

Note: no Compass-AI-specific style guide exists yet to link here as `related_style_guide` —
`style-guide/` currently only holds the unrelated Fernway foundations doc — so that field is left
blank pending one.
