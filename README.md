# agentic-repo

A git-tracked research memory, design-ops mirror, and analytics archive for the Compass AI
program: UX research findings an agent can be pinged about months later, a Markdown view of the
Figma design system so an agent doesn't need Figma access to reference it, and quant/analytics
evidence kept separate from — but cross-linked with — the qualitative findings it supports.

- **For agents:** see `AGENTS.md` (Claude Code reads `CLAUDE.md`, which imports it).
- **For humans:** start at `research/_index.md` for a scan of everything researched so far,
  `analytics/_index.md` for synthesized quant evidence, or `design-tokens/design.md` for the
  current token/component reference.
- **Setup:** [`docs/SETUP.md`](docs/SETUP.md) walks through a first install step by step.
- **Project background & build plan:** [`docs/`](docs/README.md) — including the plan and the
  decision log, [`docs/decisions.md`](docs/decisions.md).
- **Web UI:** a separate app, [Research Repo CRUD UI](https://github.com/herrjosua/research-repo-crud-ui), provides
  multi-user login, a full create/read/update/delete interface, and git-based edit attribution on
  top of this repo's content. It reads and writes this repo's markdown files (via its own Python
  scripts, unchanged) but is not stored inside it, to avoid risking this repo's working content.

> This repository's content (research sessions, findings, design tokens, analytics) is **entirely
> fictional sample data** for a hypothetical healthcare organization ("Meridian Health Network")
> and its "Compass AI" modernization program. No real patients, staff, or PHI are represented.

## Development

Requires Python 3.13.

```
pip install -r requirements-dev.txt
```

See [`docs/SETUP.md`](docs/SETUP.md) for the full walkthrough (virtualenv, first session, index,
search UI, Figma access, Windows notes).

Run the test suite:

```
pytest
```

Lint and type-check:

```
ruff check .
mypy
```

CI (`.github/workflows/ci.yml`) runs all of the above, plus `build_index.py --check`,
`build_search_ui.py --check`, and `pip-audit`, on every push and pull request to `main`.

`research/scripts/` contains runnable tooling beyond the checks above — `new_research_session.py`,
`build_index.py`, `build_search_ui.py`. See `AGENTS.md` for full usage.

A public demo of the CRUD UI runs on this repo's content at https://ux-research.joshuabock.com.
Visitors can edit it, but an hourly reset discards their edits — see [`docs/demo-deploy.md`](docs/demo-deploy.md) for how it's kept
in sync and reset.

## AI-Assisted Development

This project was built by Joshua Bock with AI assistance from Claude — used both as the AI agent this tooling is designed to work with, and as a development collaborator throughout the build (planning, implementation, testing, and code review), under direct human review and direction at every step.

## License

MIT — see [LICENSE](LICENSE).
