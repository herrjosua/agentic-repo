#!/usr/bin/env python3
"""
sync_figma_tokens.py — pull variables and components from Figma and regenerate the
design-tokens/ layer: tokens.tokens.json (DTCG format, canonical), design.md (generated
reference view), and components/*.md (one per component, generated fields only — hand-written
"Related Research Findings" and "Notes" sections are preserved on re-sync).

Two fetch paths, per the plan (§4):
  - REST API (this script's default): GET /v1/files/{key}/variables/local and the file's node
    tree for components. This is the fallback used on the work repo, where Figma MCP isn't
    available yet.
  - Figma MCP (side-project repo, once available): intended to replace the REST fetch functions
    below with MCP tool calls (get_variable_defs, get_metadata, etc.) once wired up in that repo.
    Not implemented here — this script currently only supports the REST path. See the "MCP swap"
    note at the bottom of this file for what that migration should touch.

Figma for Government (GovCloud) support: the REST API base URL differs from commercial Figma
(`api.figma-gov.com` vs `api.figma.com`). Set FIGMA_API_BASE_URL in the environment or .env to
override it — see the "Requires" section below. Everything else about the REST path (auth,
endpoints, response shapes) is the same between commercial and GovCloud, since GovCloud gets
full Enterprise-tier API access. This script does not talk to the Figma MCP server at all
currently (see above), so no GovCloud-specific MCP handling is needed here — check with your
security team before using Figma for Government's MCP server through any other client, since
Figma's own documentation notes it isn't yet inside their FedRAMP authorization boundary.

IMPORTANT — known Figma API limitation: the Variables REST API
(/v1/files/:key/variables/local) requires a Full seat in an Enterprise org. Free, Professional,
and Organization plans don't get it either — paying for a non-Enterprise plan doesn't change
this. Figma for Government does include it, since it's built on the Enterprise feature set. If
your plan doesn't include it, --skip-variables lets you still sync components, or you can
maintain tokens.tokens.json by hand and use this script only to regenerate design.md from it
(--regenerate-design-only).

Requires:
    pip install requests python-dotenv
    FIGMA_TOKEN          Personal access token (Figma > Account Settings > Personal Access Tokens)
    FIGMA_FILE_KEY       The file key from the Figma file URL (figma.com/design/<FILE_KEY>/...)
    FIGMA_API_BASE_URL   Optional. Overrides the REST API host. Defaults to https://api.figma.com
                         (commercial). Set to https://api.figma-gov.com for Figma for Government.

    All variables can be set in the shell environment, or in a .env file in the current
    working directory (FIGMA_TOKEN=..., one per line, no quotes, no `export`). A .env file is
    loaded automatically via python-dotenv if present — see NOTE below if that package isn't
    installed. Never commit a .env file; add it to .gitignore.

Usage:
    python sync_figma_tokens.py                       # full sync: variables + components
    python sync_figma_tokens.py --skip-variables       # components only
    python sync_figma_tokens.py --skip-components      # variables only
    python sync_figma_tokens.py --regenerate-design-only   # no network; rebuild design.md from
                                                            # the existing tokens.tokens.json
    python sync_figma_tokens.py --dry-run              # fetch + transform, print what would
                                                            # change, write nothing
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()  # loads .env from the current working directory, if present; no-op if absent
except ImportError:
    print(
        "NOTE: python-dotenv not installed — .env files won't be loaded automatically. "
        "Falling back to shell-exported environment variables only. "
        "Run: pip install python-dotenv (or export FIGMA_TOKEN/FIGMA_FILE_KEY manually).",
        file=sys.stderr,
    )

SCRIPT_DIR = Path(__file__).resolve().parent
DT_ROOT = SCRIPT_DIR.parent  # design-tokens/
TOKENS_FILE = DT_ROOT / "tokens.tokens.json"
DESIGN_MD_FILE = DT_ROOT / "design.md"
COMPONENTS_DIR = DT_ROOT / "components"

# Defaults to commercial Figma; override with FIGMA_API_BASE_URL for Figma for Government
# (https://api.figma-gov.com) or any other alternate host. Read once at import time, same as
# FIGMA_TOKEN/FIGMA_FILE_KEY below — load_dotenv() above has already run by this point, so a
# value set in .env is picked up here too, not just from the shell environment.
FIGMA_API_BASE = os.environ.get("FIGMA_API_BASE_URL", "https://api.figma.com").rstrip("/") + "/v1"


# --------------------------------------------------------------------------
# Fetch (network) — the only functions that need FIGMA_TOKEN/FIGMA_FILE_KEY.
# Everything below this section is pure transform/write and fully testable offline.
# --------------------------------------------------------------------------

def _get_credentials():
    token = os.environ.get("FIGMA_TOKEN")
    file_key = os.environ.get("FIGMA_FILE_KEY")
    if not token or not file_key:
        sys.exit(
            "Missing FIGMA_TOKEN and/or FIGMA_FILE_KEY environment variables.\n"
            "Set both, or use --regenerate-design-only to rebuild design.md from the existing "
            "tokens.tokens.json without any network access."
        )
    return token, file_key


def fetch_figma_variables(token, file_key):
    """GET /v1/files/:key/variables/local.
    Requires a Full seat in an Enterprise org (or Figma for Government, which includes the same
    tier of API access) — will 403 otherwise. Returns raw Figma API JSON."""
    import requests  # imported here so --regenerate-design-only never requires the dependency
    resp = requests.get(
        f"{FIGMA_API_BASE}/files/{file_key}/variables/local",
        headers={"X-Figma-Token": token},
        timeout=30,
    )
    if resp.status_code == 403:
        sys.exit(
            "Figma returned 403 fetching variables. The Variables REST API requires a Full seat "
            "in an Enterprise org (Figma for Government includes this; Free/Professional/"
            "Organization do not, regardless of paid status). Use --skip-variables to sync "
            "components only, or maintain tokens.tokens.json by hand and run "
            "--regenerate-design-only to refresh design.md.\n"
            f"If you're on Figma for Government, also confirm FIGMA_API_BASE_URL is set to "
            f"https://api.figma-gov.com — currently resolving requests against {FIGMA_API_BASE}."
        )
    resp.raise_for_status()
    return resp.json()


def fetch_figma_file_nodes(token, file_key):
    """GET /v1/files/:key — the full document tree, used to find COMPONENT_SET / COMPONENT nodes."""
    import requests
    resp = requests.get(
        f"{FIGMA_API_BASE}/files/{file_key}",
        headers={"X-Figma-Token": token},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


# --------------------------------------------------------------------------
# Transform — Figma API shapes -> our DTCG-ish tokens dict / component records.
# --------------------------------------------------------------------------

def figma_variables_to_dtcg(variables_json):
    """Convert a Figma /variables/local response into our tokens.tokens.json shape.

    This is intentionally a light, opinionated mapping (Figma's variable collections/modes ->
    our color/spacing/typography/radius/size top-level groups by variable name prefix), not a
    generic DTCG converter — it matches the naming convention already used in this file
    (color.primitive.*, color.semantic.*, spacing.*, etc). Extend the PREFIX_TO_GROUP mapping
    below if new variable naming conventions are introduced in Figma.
    """
    meta = variables_json.get("meta", {})
    variables = meta.get("variables", {})
    collections = meta.get("variableCollections", {})

    PREFIX_TO_GROUP = {
        "color/": "color",
        "spacing/": "spacing",
        "radius/": "radius",
        "size/": "size",
        "typography/": "typography",
    }

    DIMENSION_GROUPS = {"spacing", "radius", "size"}

    tokens = {}
    for var in variables.values():
        name = var.get("name", "")  # e.g. "color/semantic/action/primary"
        group = next((g for prefix, g in PREFIX_TO_GROUP.items() if name.startswith(prefix)), None)
        if group is None:
            continue  # unrecognized naming convention — skip rather than guess
        path_parts = name.split("/")[1:]  # drop the group prefix segment

        collection = collections.get(var.get("variableCollectionId"), {})
        modes = collection.get("modes", [])
        default_mode_id = modes[0]["modeId"] if modes else None
        value = var.get("valuesByMode", {}).get(default_mode_id)
        if value is None:
            continue

        node = tokens.setdefault(group, {"$type": "dimension" if group in DIMENSION_GROUPS else group})
        cursor = node
        for part in path_parts[:-1]:
            cursor = cursor.setdefault(part, {})
        cursor[path_parts[-1]] = {"$value": _figma_value_to_dtcg(group, value)}

    return tokens


def _figma_value_to_dtcg(group, value):
    if group == "color" and isinstance(value, dict) and "r" in value:
        r, g, b = (round(value[c] * 255) for c in "rgb")
        return f"#{r:02X}{g:02X}{b:02X}"
    return value


def figma_nodes_to_components(file_json):
    """Walk the document tree and return a list of {slug, name, node_id, variants} for every
    top-level COMPONENT_SET (variants) or standalone COMPONENT node found."""
    components = []

    def walk(node):
        if node.get("type") == "COMPONENT_SET":
            variants = []
            for child in node.get("children", []):
                # Figma component-set children are named like "State=Default, Size=Small"
                variants.append(child.get("name", ""))
            components.append(dict(
                name=node.get("name", "Unnamed"),
                node_id=node.get("id", ""),
                variants=variants or ["default"],
            ))
            return  # don't recurse into a component-set's children — they're variants, not separate components
        if node.get("type") == "COMPONENT":
            components.append(dict(
                name=node.get("name", "Unnamed"),
                node_id=node.get("id", ""),
                variants=["default"],
            ))
        for child in node.get("children", []):
            walk(child)

    document = file_json.get("document", {})
    walk(document)
    return components


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


# --------------------------------------------------------------------------
# Write — tokens.tokens.json, design.md (fully generated), components/*.md (merge-safe)
# --------------------------------------------------------------------------

def write_tokens_json(tokens, dry_run=False):
    content = json.dumps(tokens, indent=2) + "\n"
    if dry_run:
        print(f"[dry-run] would write {TOKENS_FILE} ({len(content)} bytes)")
        return
    TOKENS_FILE.write_text(content, encoding="utf-8")
    print(f"✅ Wrote {TOKENS_FILE}")


def _walk_tokens_for_table(node, path, rows):
    if isinstance(node, dict) and "$value" in node:
        rows.append((".".join(path), node["$value"], node.get("$description", "")))
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            _walk_tokens_for_table(child, path + [key], rows)


def generate_design_md(tokens, dry_run=False):
    """Fully regenerate design.md from tokens.tokens.json. This is a mechanical walk of every
    token leaf — any human-authored rationale should live in a token's own $description field in
    tokens.tokens.json (the canonical source), not be hand-added to design.md, since this file is
    fully overwritten on every sync."""
    lines = [
        "---",
        "title: Design System — Generated Token Reference",
        "generated_from: tokens.tokens.json",
        "generator: sync_figma_tokens.py",
        "status: generated",
        "---",
        "",
        "# Design System — Token Reference",
        "",
        "**Do not hand-edit this file.** Regenerated by `sync_figma_tokens.py` from "
        "`tokens.tokens.json`, which is the canonical source. Add rationale as a token's "
        "`$description` in that file, not here.",
        "",
    ]

    for group_name, group in tokens.items():
        rows = []
        _walk_tokens_for_table(group, [], rows)
        if not rows:
            continue
        lines.append(f"## {group_name.capitalize()}\n")
        lines.append("| Token | Value | Notes |")
        lines.append("|---|---|---|")
        for token_path, value, desc in rows:
            display_value = value if isinstance(value, str) else json.dumps(value)
            lines.append(f"| `{group_name}.{token_path}` | `{display_value}` | {desc} |")
        lines.append("")

    lines.append(
        "## Components\n\nSee `components/*.md` for one file per component, including Figma node "
        "reference and code mapping.\n"
    )

    content = "\n".join(lines)
    if dry_run:
        print(f"[dry-run] would write {DESIGN_MD_FILE} ({len(content)} bytes)")
        return
    DESIGN_MD_FILE.write_text(content, encoding="utf-8")
    print(f"✅ Wrote {DESIGN_MD_FILE}")


HAND_AUTHORED_SECTIONS = ("## Related Research Findings", "## Notes")


def sync_component_file(component, dry_run=False):
    """Create or update components/<slug>.md. Generated fields (title, Figma node, variants,
    code mapping placeholder) are always overwritten. Hand-authored sections
    (## Related Research Findings, ## Notes) are preserved verbatim if the file already exists —
    those are where a researcher/designer records why a finding or decision applies to this
    component, and shouldn't be clobbered by a token/component re-sync."""
    slug = slugify(component["name"])
    path = COMPONENTS_DIR / f"{slug}.md"

    preserved = {}
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        for section in HAND_AUTHORED_SECTIONS:
            pattern = re.escape(section) + r"\n(.*?)(?=\n## |\Z)"
            m = re.search(pattern, existing, re.DOTALL)
            if m:
                preserved[section] = m.group(1).strip()

    lines = [
        "---",
        f"title: {component['name']}",
        f"component_id: {slug}",
        "status: generated",
        "generated_from: Figma (via sync_figma_tokens.py)",
        "---",
        "",
        f"# {component['name']}",
        "",
        f"**Figma node:** `figma://file/{os.environ.get('FIGMA_FILE_KEY', '<file-key>')}/node/{component['node_id']}`",
        "",
        "## Variants",
    ]
    for v in component["variants"]:
        lines.append(f"- {v}")
    lines.append("")
    lines.append("## States")
    lines.append("- TODO — Figma's API doesn't expose interaction states directly; fill in from the file or Code Connect.")
    lines.append("")
    lines.append("## Code mapping")
    lines.append("TODO — populate via Code Connect once set up, or by hand.")
    lines.append("")

    for section in HAND_AUTHORED_SECTIONS:
        lines.append(section)
        lines.append(preserved.get(section, "TODO"))
        lines.append("")

    content = "\n".join(lines)
    if dry_run:
        action = "update" if path.exists() else "create"
        print(f"[dry-run] would {action} {path}")
        return
    path.write_text(content, encoding="utf-8")
    action = "Updated" if preserved else "Created"
    print(f"✅ {action} {path}")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skip-variables", action="store_true")
    parser.add_argument("--skip-components", action="store_true")
    parser.add_argument("--regenerate-design-only", action="store_true",
                        help="No network. Rebuild design.md from the existing tokens.tokens.json.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and transform, but write nothing.")
    args = parser.parse_args()

    if args.regenerate_design_only:
        if not TOKENS_FILE.exists():
            sys.exit(f"{TOKENS_FILE} does not exist — nothing to regenerate from.")
        tokens = json.loads(TOKENS_FILE.read_text(encoding="utf-8"))
        generate_design_md(tokens, dry_run=args.dry_run)
        return

    token, file_key = _get_credentials()

    tokens = json.loads(TOKENS_FILE.read_text(encoding="utf-8")) if TOKENS_FILE.exists() else {}

    if not args.skip_variables:
        variables_json = fetch_figma_variables(token, file_key)
        tokens = figma_variables_to_dtcg(variables_json)
        write_tokens_json(tokens, dry_run=args.dry_run)

    generate_design_md(tokens, dry_run=args.dry_run)

    if not args.skip_components:
        COMPONENTS_DIR.mkdir(exist_ok=True)
        file_json = fetch_figma_file_nodes(token, file_key)
        components = figma_nodes_to_components(file_json)
        for c in components:
            sync_component_file(c, dry_run=args.dry_run)
        print(f"Synced {len(components)} component(s).")

    print("Done." if not args.dry_run else "Dry run complete — nothing written.")


# --------------------------------------------------------------------------
# MCP swap (v0.6, side-project repo only, per the roadmap)
#
# Once Figma MCP is available in a given repo, the two fetch_figma_* functions above are what
# to replace: swap fetch_figma_variables()'s REST call for the MCP get_variable_defs tool, and
# fetch_figma_file_nodes()'s REST call for get_metadata / get_design_context. The transform and
# write functions (figma_variables_to_dtcg, figma_nodes_to_components, write_tokens_json,
# generate_design_md, sync_component_file) shouldn't need to change — they operate on plain
# dicts, not on the REST response shape specifically, though the exact key names coming back
# from MCP tools should be checked against what figma_variables_to_dtcg/figma_nodes_to_components
# expect. Also add Code Connect component mapping at that point, per the roadmap. Note that a
# GovCloud MCP swap specifically should not be attempted until Figma for Government's MCP server
# is confirmed inside your org's FedRAMP authorization boundary — see the module docstring.
# --------------------------------------------------------------------------


if __name__ == "__main__":
    main()
