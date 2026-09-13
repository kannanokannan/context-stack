#!/usr/bin/env python3
"""Gate the published Context Stack registries against stack.yaml.

REPO_MAP.md lives in this repository and is read from the local checkout, so a
pull request that breaks it fails on that pull request. The other two registries
live in sibling repositories and are fetched from their published main, so this
check answers the question that actually matters: do the registries people and
agents read agree with the manifest right now.

A consequence worth stating: a change made in the website or MCP repository is
not caught until this check next runs. The workflow therefore runs on a schedule
as well as on pull requests.

Run from the repository root:  python3 scripts/verify_stack.py
Exit code 0 if every check passes, 1 otherwise. Warnings never fail the run.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

import yaml

RAW = "https://raw.githubusercontent.com/kannanokannan"

SURFACES = {
    "repositories_html": f"{RAW}/kannanokannan.github.io/main/repositories.html",
    "mcp_projects": f"{RAW}/context-stack-mcp/main/src/stack-catalog.js",
}

passed = []
failed = []
warned = []


def ok(msg):
    passed.append(msg)
    print("PASS  " + msg)


def bad(msg):
    failed.append(msg)
    print("FAIL  " + msg)


def warn(msg):
    warned.append(msg)
    print("WARN  " + msg)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "verify_stack"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


# --------------------------------------------------------------- manifest

with open("stack.yaml", "r", encoding="utf-8") as fh:
    manifest = yaml.safe_load(fh)

repos = manifest["repositories"]
ids = [r["id"] for r in repos]

if len(set(ids)) == len(ids):
    ok("M1 manifest ids are unique (%d repositories)" % len(ids))
else:
    bad("M1 manifest has duplicate ids")

slug_bad = [r["id"] for r in repos if not r["repo"].endswith("/" + r["id"])]
if not slug_bad:
    ok("M2 every manifest repo URL ends in its own id")
else:
    bad("M2 repo URL does not match id: %s" % ", ".join(slug_bad))

lic_bad = [r["id"] for r in repos if r.get("license") != "Apache-2.0"]
if not lic_bad:
    ok("M3 every repository is recorded as Apache-2.0")
else:
    bad("M3 non-Apache-2.0 entries: %s" % ", ".join(lic_bad))

known = {"repo_map", "repositories_html", "mcp_projects"}
surf_bad = sorted({s for r in repos for s in r["surfaces"]} - known)
if not surf_bad:
    ok("M4 no unknown surface names in the manifest")
else:
    bad("M4 unknown surface name(s): %s" % ", ".join(surf_bad))


def expected(surface):
    return [r["id"] for r in repos if surface in r["surfaces"]]


# --------------------------------------------------------------- REPO_MAP.md

with open("REPO_MAP.md", "r", encoding="utf-8") as fh:
    repo_map = fh.read()

table = re.findall(r"^\| `([^`]+)` \| `([^`]+)` \|", repo_map, re.M)
sections = re.findall(r"^### `([^`]+)`", repo_map, re.M)
want = expected("repo_map")

if [t[0] for t in table] == want:
    ok("G1 REPO_MAP.md table matches the manifest, in order (%d)" % len(want))
else:
    bad("G1 REPO_MAP.md table is %s, manifest says %s" % ([t[0] for t in table], want))

if sections == want:
    ok("G2 REPO_MAP.md ownership sections match the manifest, in order (%d)" % len(want))
else:
    bad("G2 REPO_MAP.md sections are %s, manifest says %s" % (sections, want))

if [t[0] for t in table] == sections:
    ok("G3 REPO_MAP.md table order equals section order")
else:
    bad("G3 REPO_MAP.md table order does not equal section order")

url_bad = []
by_id = {r["id"]: r for r in repos}
for slug, url in table:
    entry = by_id.get(slug)
    if entry and not entry["repo"].endswith(url.split("github.com/")[-1].strip("/")):
        url_bad.append(slug)
if not url_bad:
    ok("G4 REPO_MAP.md URLs agree with the manifest")
else:
    bad("G4 REPO_MAP.md URL mismatch: %s" % ", ".join(url_bad))

# --------------------------------------------------------------- siblings

offline = False
fetched = {}
for name, url in SURFACES.items():
    try:
        fetched[name] = fetch(url)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as exc:
        offline = True
        bad("N1 could not fetch %s (%s)" % (name, exc))

if not offline:
    html = fetched["repositories_html"]
    found = sorted(set(re.findall(r"github\.com/kannanokannan/([A-Za-z0-9._-]+)", html)))
    want = sorted(expected("repositories_html"))
    if found == want:
        ok("G5 repositories.html lists exactly the manifest set (%d)" % len(want))
    else:
        bad("G5 repositories.html lists %s, manifest says %s" % (found, want))

    js = fetched["mcp_projects"]
    block = js.split("export const projects")[1].split("export const resources")[0]
    found = re.findall(r"repo:\s*`\$\{gh\}/([A-Za-z0-9._-]+)`", block)
    want = expected("mcp_projects")
    if found == want:
        ok("G6 stack-catalog.js projects[] matches the manifest, in order (%d)" % len(want))
    else:
        bad("G6 stack-catalog.js projects[] is %s, manifest says %s" % (found, want))

    if "contextboundary-gw" in js:
        ok("G7 the reference gateway is reachable through the MCP catalog")
    else:
        bad("G7 contextboundary-gw appears nowhere in stack-catalog.js")

# --------------------------------------------- composition (warning only)

comp = manifest.get("composition", {})
if comp.get("decided"):
    bad("C1 composition is marked decided but this check has not been implemented yet")
else:
    three = "three sibling projects" in open("GLOSSARY.md", encoding="utf-8").read()
    four = (not offline) and "plus Griha as the product layer" in fetched["mcp_projects"]
    if three and four:
        warn("C1 stack composition is stated as THREE in GLOSSARY.md and FOUR in "
             "stack-catalog.js. Undecided, so not failing. Record the answer in "
             "stack.yaml -> composition to turn this into a gate.")
    else:
        warn("C1 composition is undecided in stack.yaml; no gate applied")

# --------------------------------------------------------------- summary

print()
if warned:
    print("%d warning(s)" % len(warned))
print("%d passed, %d failed" % (len(passed), len(failed)))
sys.exit(1 if failed else 0)
