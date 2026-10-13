#!/usr/bin/env python3
"""int-gen-graph.py: read the IMPORT lines of every .l4 file in the deposit and write
  graph.md          a table of every module, its kind and its imports (for NOTES.md),
  modules-order.json  the modules in dependency order (for encoding.json), and prints any cycle or any import that names no file.
The order: the two shared modules; then, group by group, the group's rule modules and then its tests; then the integration
modules and their tests.  Within each block a module comes after everything it imports."""
import pathlib, re, json, sys, collections

DEP = pathlib.Path(__file__).resolve().parent  # this script sits in the deposit beside the modules it reads
if len(sys.argv) != 2:
    sys.exit("usage: %s OUTDIR   (a directory that exists; the generated files are written there, not into the deposit)" % sys.argv[0])
WORK = pathlib.Path(sys.argv[1])
BUILTIN = {"prelude", "daydate"}

mods = sorted(p.stem for p in DEP.glob("*.l4"))
imports = {}
for m in mods:
    imps = []
    for l in (DEP / (m + ".l4")).read_text(encoding="utf-8").split("\n"):
        mm = re.match(r"^IMPORT\s+`?([^`\s]+)`?\s*$", l)
        if mm:
            imps.append(mm.group(1))
    imports[m] = imps

problems = []
for m, imps in imports.items():
    for i in imps:
        if i not in BUILTIN and i not in imports:
            problems.append("%s imports %s, which is not a file" % (m, i))


def kind(m):
    if m in ("domain", "il-interpretation-time"):
        return "shared"
    if m.startswith("ind-"):
        return "independent test (%s)" % m[:5]
    if m.startswith("int-tests-"):
        return "integration test"
    if m.startswith("int-"):
        return "integration"
    if "-tests-" in m:
        return "test of %s" % m[:2]
    return "rule module of %s" % m[:2]


def topo(block):
    block = list(block)
    done, out = set(), []
    remaining = {m: [i for i in imports[m] if i in block] for m in block}
    while remaining:
        ready = sorted(m for m, deps in remaining.items() if all(d in done for d in deps))
        if not ready:
            problems.append("cycle among: " + ", ".join(sorted(remaining)))
            out.extend(sorted(remaining))
            break
        m = ready[0]
        out.append(m)
        done.add(m)
        del remaining[m]
    return out


order = ["il-interpretation-time", "domain"]
for g in range(1, 9):
    rule = [m for m in mods if m.startswith("g%d-" % g) and "-tests-" not in m]
    tests = [m for m in mods if m.startswith("g%d-" % g) and "-tests-" in m]
    # the red file last, the fixtures first among the tests
    order += topo(rule)
    t = topo(tests)
    t = [x for x in t if not x.endswith("-tests-red")] + [x for x in t if x.endswith("-tests-red")]
    order += t
irule = [m for m in mods if m.startswith("int-") and not m.startswith("int-tests-")]
itest = [m for m in mods if m.startswith("int-tests-")]
order += topo(irule)
t = topo(itest)
t = [x for x in t if not x.endswith("-tests-red")] + [x for x in t if x.endswith("-tests-red")]
order += t
# the independent tests (ind-a, ind-b, ind-c), each after everything else, the files that state the readings not taken last
for a in ("ind-a", "ind-b", "ind-c"):
    block = topo([m for m in mods if m.startswith(a + "-")])
    order += [x for x in block if not x.endswith(("-tests-ambiguous", "-tests-disagree"))] + [x for x in block if x.endswith(("-tests-ambiguous", "-tests-disagree"))]
missing = [m for m in mods if m not in order and not m.startswith("int-scratch")]
if missing:
    problems.append("not placed: " + ", ".join(missing))

# check the order is topological
pos = {m: i for i, m in enumerate(order)}
for m in order:
    for i in imports[m]:
        if i in pos and pos[i] > pos[m]:
            problems.append("order puts %s before its import %s" % (m, i))

(WORK / "modules-order.json").write_text(json.dumps([m + ".l4" for m in order], indent=1) + "\n", encoding="utf-8")
rows = ["| module | kind | imports |", "| --- | --- | --- |"]
for m in order:
    imps = [i for i in imports[m]]
    shown = ", ".join("`%s`" % i for i in imps) if imps else "nothing"
    rows.append("| `%s` | %s | %s |" % (m, kind(m), shown))
(WORK / "graph.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

# group-level summary: which group's modules each integration module imports
cross = collections.OrderedDict()
for m in irule:
    gs = collections.Counter(re.match(r"^g(\d)-", i).group(1) for i in imports[m] if re.match(r"^g\d-", i))
    cross[m] = dict(gs)
(WORK / "graph-int.json").write_text(json.dumps(cross, indent=1), encoding="utf-8")
print("modules:", len(mods), "ordered:", len(order))
print("group modules importing another group:", [m for m in mods if re.match(r"^g\d-", m) and any(re.match(r"^g\d-", i) and i[:2] != m[:2] for i in imports[m])])
print("problems:", problems or "none")
for m, gs in cross.items():
    print(m, "imports modules of groups", sorted(gs))
