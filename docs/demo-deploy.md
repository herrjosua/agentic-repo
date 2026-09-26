# Demo deploy — what's still unwired

The demo isolation pieces that don't depend on a live server exist as of this writing: the
`research-repo-demo` repo, the `sync-demo.yml` GitHub Actions workflow that keeps it in sync with
this repo's `research/` and `design-tokens/`, the `demo-baseline` tag it force-moves each run, and
`research/scripts/reset_demo.sh`, ready to reset a checkout back to that tag. See AGENTS.md →
"Demo repo sync" for how those fit together.

Two things remain before this is fully live, both blocked on the CRUD UI's webhost deployment
existing:

1. **The demo server's own fetch-only credential.** Whatever process pulls `research-repo-demo`
   onto the demo server needs its own read-only credential to that repo — separate from
   `DEMO_REPO_PAT`, which is scoped for the sync workflow's push access and shouldn't be reused
   for this.
2. **Scheduling `reset_demo.sh`.** Once the server exists, point an hourly cron entry (or
   equivalent scheduler) at it from within its `research-repo-demo` checkout. If the demo
   server's Python 3 interpreter isn't on `PATH` as `python3`, set `PYTHON_BIN` in that cron
   entry's environment to override it — the script falls back to `python3` when unset.

Also out of scope here: wiring the CRUD UI itself (pointing `AGENTIC_REPO_ROOT` at the demo repo
path) — that's separate, already-scoped work for once an actual server exists.
