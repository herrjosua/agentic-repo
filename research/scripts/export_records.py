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
                                                # print a single record by its id field (with its
                                                # full raw markdown content included, for editing),
                                                # or nothing (exit 1) if no record matches
    python export_records.py --kind raw --summary
                                                # list mode: strip html/searchText for a lightweight
                                                # payload; has no effect combined with --id
"""
import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import frontmatter
from build_search_ui import (  # noqa: E402
    RESEARCH_ROOT,
    SKIPPED,
    build_analytics_records,
    build_component_records,
    build_deliverable_records,
    build_findings_records,
    build_raw_records,
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
                         help="Print only the single record whose id matches exactly, including "
                              "its full raw markdown content (rawContent field). "
                              "Exits 1 with an error on stderr if no record matches, or if "
                              "the matching record's file is invalid (other invalid records "
                              "are skipped with a warning and don't affect it).")
    parser.add_argument("--summary", action="store_true",
                         help="Strip the html and searchText fields from each record, for a "
                              "lightweight list payload. Has no effect combined with --id, "
                              "since a single fully-fetched record is small regardless.")
    args = parser.parse_args()

    records = load_all_records()

    if args.kind:
        records = [r for r in records if r["kind"] == args.kind]

    if args.id is not None:
        match = next((r for r in records if r["id"] == args.id), None)
        if match is None and args.id in SKIPPED and (
                args.kind is None or args.id.startswith(f"{args.kind}:")):
            print(f"❌ Record {args.id!r} is invalid ({SKIPPED[args.id]})", file=sys.stderr)
            sys.exit(1)
        if match is None:
            print(f"❌ No record found with id {args.id!r}", file=sys.stderr)
            sys.exit(1)
        file_path = (RESEARCH_ROOT / match["path"]).resolve()
        post = frontmatter.load(file_path)
        match["rawContent"] = post.content
        print(json.dumps(match, ensure_ascii=False))
        return

    if args.summary:
        records = [
            {k: v for k, v in r.items() if k not in ("html", "searchText")}
            for r in records
        ]

    print(json.dumps(records, ensure_ascii=False))


if __name__ == "__main__":
    main()
