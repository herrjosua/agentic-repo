# agentic-repo

A git-tracked research memory, design-ops mirror, and analytics archive for the Compass AI
program: UX research findings an agent can be pinged about months later, a Markdown view of the
Figma design system so an agent doesn't need Figma access to reference it, and quant/analytics
evidence kept separate from — but cross-linked with — the qualitative findings it supports.

- **For agents:** see `AGENTS.md` (Claude Code reads `CLAUDE.md`, which imports it).
- **For humans:** start at `research/_index.md` for a scan of everything researched so far,
  `analytics/_index.md` for synthesized quant evidence, or `design-tokens/design.md` for the
  current token/component reference.
- **Project background & build plan:** `docs/`
- **Web UI:** a separate app, [Research Repo CRUD UI](../Research%20Repo%20CRUD%20UI), provides
  multi-user login, a full create/read/update/delete interface, and git-based edit attribution on
  top of this repo's content. It reads and writes this repo's markdown files (via its own Python
  scripts, unchanged) but is not stored inside it, to avoid risking this repo's working content.

> This repository's content (research sessions, findings, design tokens, analytics) is **entirely
> fictional sample data** for a hypothetical healthcare organization ("Meridian Health Network")
> and its "Compass AI" modernization program. No real patients, staff, or PHI are represented.
