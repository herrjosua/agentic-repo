#!/usr/bin/env python3
"""
export_records.py — print every research repo record (raw sessions, findings, components,
analytics summaries, and feature-002 deliverables) as a single JSON array on stdout.

This is a thin wrapper, not a new data source: it imports the same loader functions
build_search_ui.py already uses to build search.html's embedded dataset
(build_raw_records, build_findings_records, build_component_records, build_analytics_records,
build_deliverable_records) and prints their combined output as JSON instead of wrapping it in
an HTML/JS template. No parsing logic is duplicated here — if the record shape ever changes,
it changes in build_search_ui.py and this script picks it up automatically.

Written for the separate Research Repo CRUD UI app: its Node/Express backend shells out to this
script (child_process.execFile) to get a machine-readable list of every record in the repo,
rather than scraping the <script id="research-data"> JSON blob out of search.html.

Requires: pip install python-frontmatter (same requirement as build_search_ui.py, which this
script imports from)

Usage:
    python export_records.py                  # prints all records as a JSON array
    python export_records.py --kind raw        # filter to one kind: raw | finding | component |
                                                # analytics | deliverable
    python export_records.py --id raw:2026-01-19-onboarding-usability-test
                                                # print a single record by its id field, or
                                                # nothing (exit 1) if no record matches
"""
import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_search_ui import (  # noqa: E402
    build_raw_records,
    build_findings_records,
    build_component_records,
    build_analytics_records,
    build_deliverable_records,
    build_search_text,
)

VALID_KINDS = {"raw", "finding", "component", "analytics", "deliverable"}


def load_all_records():
    records = (
        build_raw_records()
        + build_findings_records()
        + build_component_records()
        + build_analytics_records()
        + build_deliverable_records()
    )
    for r in records:
        r["searchText"] = build_search_text(r)
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kind", choices=sorted(VALID_KINDS), default=None,
                         help="Only include records of this kind. Omit to include all kinds.")
    parser.add_argument("--id", default=None,
                         help="Print only the single record whose id matches exactly. "
                              "Exits 1 with an error on stderr if no record matches.")
    args = parser.parse_args()

    records = load_all_records()

    if args.kind:
        records = [r for r in records if r["kind"] == args.kind]

    if args.id is not None:
        match = next((r for r in records if r["id"] == args.id), None)
        if match is None:
            print(f"❌ No record found with id {args.id!r}", file=sys.stderr)
            sys.exit(1)
        print(json.dumps(match, ensure_ascii=False))
        return

    print(json.dumps(records, ensure_ascii=False))


if __name__ == "__main__":
    main()
