#!/usr/bin/env bash
# Resets a research-repo-demo checkout back to the demo-baseline tag and rebuilds its
# index, so the public CRUD UI demo can't accumulate visitor edits between resets:
# force-fetches tags from origin, hard-resets to demo-baseline, then reruns
# build_index.py with $PYTHON_BIN (default: python3).
#
# Documents the demo's hourly reset. The scheduled job on the demo host runs these same
# steps inline rather than calling this script. See docs/demo-deploy.md.
set -euo pipefail

# Wrapped in main(), called only after the whole file is parsed: this script runs from inside
# the clone it resets, so `git reset --hard` below can rewrite this very file mid-run, and an
# unwrapped script would have bash reading those rewritten bytes partway through.
main() {
  cd "$(dirname "$0")/../.."

  # --tags --force: demo-baseline is force-moved on GitHub on every demo sync, and a plain
  # fetch will not update a local tag that already exists, so this script would silently keep
  # resetting to a stale commit. This is intentionally different from research-repo-crud-ui's
  # scripts/deploy.sh, which must NOT force-fetch tags.
  git fetch --tags --force origin
  git reset --hard demo-baseline

  PYTHON_BIN="${PYTHON_BIN:-python3}"
  "$PYTHON_BIN" research/scripts/build_index.py
}

main "$@"
