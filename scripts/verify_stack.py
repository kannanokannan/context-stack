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

The composition checks (X1-X4) read every repository in the manifest from disk,
side by side with this one. CI checks the siblings out that way; locally, run it
from <workspace-root>/context-stack or set STACK_WORKSPACE.

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
    "index_html": f"{RAW}/kannanokannan.github.io/main/index.html",
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

with open("GLOSSARY.md", "r", encoding="utf-8") as fh:
    repo_map_glossary = fh.read()

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

# --------------------------------------------------------- composition
#
# The composition is asserted positively (X1, X2) and its retired wording is
# caught as a regression (X3), across every repository in the manifest - not a
# phrase list over four files. A repository may describe itself; it may not
# describe the stack's shape. COMPOSITION.md is the statement, stack.yaml the data.
#
# Sibling repositories are read from disk, side by side with this one:
# <workspace-root>/<id>/ for every manifest id. CI checks them out that way;
# locally, set STACK_WORKSPACE if they are not in the parent directory.

comp = manifest.get("composition", {})

if not comp.get("decided"):
    warn("C1 composition is undecided in stack.yaml; no gate applied")
else:
    known = {r["id"] for r in repos}
    spec = list(comp.get("specification", []))
    impl = list(comp.get("implementations", []))
    missing = [n for n in spec + impl if n not in known]
    if missing:
        bad("C1 composition names repositories absent from the manifest: %s" % ", ".join(missing))
    elif not spec:
        bad("C1 composition is decided but names no specification repositories")
    else:
        ok("C1 composition: %d specification + %d implementation repositories, all in the manifest"
           % (len(spec), len(impl)))

    canon = " ".join(str(comp.get("canonical_one_line", "")).split())
    roles = comp.get("roles", {}) or {}

    # X1 - the data agrees with itself.
    x1 = []
    if not canon:
        x1.append("canonical_one_line is empty")
    if sorted(k for k, v in roles.items() if v.get("kind") == "specification") != sorted(spec):
        x1.append("roles marked specification differ from the specification list")
    if sorted(k for k, v in roles.items() if v.get("kind") == "implementation") != sorted(impl):
        x1.append("roles marked implementation differ from the implementations list")
    if sorted(roles) != sorted(known):
        x1.append("roles cover %s, manifest has %s" % (sorted(roles), sorted(known)))
    surfaces = list(comp.get("canonical_surfaces", []))
    stray = [s for s in surfaces if s.split("/", 1)[0] not in known]
    if stray:
        x1.append("canonical_surfaces outside the manifest: %s" % ", ".join(stray))
    with open(comp.get("canonical_statement", "COMPOSITION.md"), "r", encoding="utf-8") as fh:
        statement_count = fh.read().count(canon) if canon else 0
    if statement_count != 1:
        x1.append("COMPOSITION.md carries the one-line form %d time(s), expected 1" % statement_count)
    if x1:
        bad("X1 composition data: " + "; ".join(x1))
    else:
        ok("X1 composition data is consistent: roles, lists, surfaces and COMPOSITION.md agree")

    # Load every repository's text files from disk.
    here = os.path.basename(os.path.abspath("."))
    workspace = os.environ.get("STACK_WORKSPACE") or os.path.abspath("..")
    TEXT = (".md", ".txt", ".html", ".js", ".mjs", ".yaml", ".yml", ".json", ".py", ".toml")
    files = {}
    absent = []
    for rid in sorted(known):
        root = os.path.abspath(".") if rid == here else os.path.join(workspace, rid)
        if not os.path.isdir(root):
            absent.append(rid)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in (".git", "node_modules", ".wrangler")]
            for name in filenames:
                if name.endswith(TEXT):
                    path = os.path.join(dirpath, name)
                    rel = os.path.relpath(path, root).replace(os.sep, "/")
                    with open(path, "r", encoding="utf-8", errors="replace") as fh:
                        files[(rid, rel)] = fh.read()
    if absent:
        bad("N2 sibling repositories not found under %s: %s" % (workspace, ", ".join(absent)))
    else:
        ok("N2 all %d repositories read from disk (%d text files)" % (len(known), len(files)))

    # X2 - every canonical surface states the shape, in the canonical words.
    x2 = []
    for s in surfaces:
        rid, rel = s.split("/", 1)
        text = files.get((rid, rel))
        if text is None:
            x2.append("%s missing" % s)
        elif canon not in " ".join(text.split()):
            x2.append("%s does not carry it" % s)
    if x2:
        bad("X2 canonical one-line form: " + "; ".join(x2))
    else:
        ok("X2 all %d canonical surfaces carry the one-line form byte-identically" % len(surfaces))

    # X3 - nothing else states the shape: no retired wording, no paraphrase.
    retired = re.compile("|".join(comp.get("retired_patterns", [])), re.I)
    paraphrase = re.compile("|".join(comp.get("paraphrase_markers", [])), re.I)
    sources = {tuple(s.split("/", 1)) for s in (comp.get("x3_excluded", []) or [])}
    allow = {(a["repo"], a["path"], a["line"]) for a in (comp.get("allowlist", []) or [])}
    seen = set()
    x3 = []
    for (rid, rel), text in sorted(files.items()):
        if (rid, rel) in sources:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            is_retired = bool(retired.pattern) and retired.search(line)
            is_paraphrase = bool(paraphrase.pattern) and paraphrase.search(line) and canon not in line
            if not (is_retired or is_paraphrase):
                continue
            if (rid, rel, stripped) in allow:
                seen.add((rid, rel, stripped))
                continue
            x3.append("%s/%s:%d %s" % (rid, rel, number, stripped[:120]))
    if x3:
        bad("X3 %d line(s) state the shape outside the canonical words:\n      " % len(x3)
            + "\n      ".join(x3))
    else:
        ok("X3 no retired wording or paraphrase in %d files (%d allowlisted line(s))"
           % (len(files), len(seen)))

    # X4 - the allowlist is exact: every entry still matches a real line.
    stale = sorted(allow - seen)
    if stale:
        bad("X4 allowlist entries that no longer match any line: "
            + "; ".join("%s/%s: %s" % (r, p, l[:80]) for r, p, l in stale))
    else:
        ok("X4 every allowlist entry matches a line (%d)" % len(allow))

# --------------------------------------------------------------- summary

print()
if warned:
    print("%d warning(s)" % len(warned))
print("%d passed, %d failed" % (len(passed), len(failed)))
sys.exit(1 if failed else 0)
