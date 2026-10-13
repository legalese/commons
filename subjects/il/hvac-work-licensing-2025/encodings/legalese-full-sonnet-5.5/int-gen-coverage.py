#!/usr/bin/env python3
"""int-gen-coverage.py: read the coverage table of each FRAGMENT-Gk.md in the deposit and write coverage-all.tsv
(columns: provision, disposition, module, group), plus a summary of counts per group and disposition to stdout.
No Hebrew is read or written here.  The tables are parsed by their header cells, because the eight encoders chose different columns."""
import pathlib, re, sys, collections

DEP = pathlib.Path(__file__).resolve().parent  # this script sits in the deposit beside the modules it reads
out_rows = []
summary = collections.OrderedDict()
DISPS = ("encoded", "inert", "refused", "out-of-scope", "deferred")


def cells(line):
    line = line.strip()
    assert line.startswith("|") and line.endswith("|"), line[:60]
    parts = re.split(r"(?<!\\)\|", line[1:-1])
    return [c.strip() for c in parts]


def clean(c):
    c = re.sub(r"<br>.*", "", c)
    c = c.replace("**", "").replace("`", "").strip()
    return c


def find_table(text):
    """The first table after a heading that contains 'Coverage'."""
    lines = text.split("\n")
    start = None
    for i, l in enumerate(lines):
        if re.match(r"^##\s+(\(1\)\s+|1\.\s+)?Coverage", l):
            start = i
            break
    if start is None:
        raise SystemExit("no coverage heading")
    j = start
    while j < len(lines) and not lines[j].startswith("|"):
        j += 1
    hdr = cells(lines[j])
    rows = []
    k = j + 2
    while k < len(lines) and lines[k].startswith("|"):
        rows.append(cells(lines[k]))
        k += 1
    return hdr, rows


def norm_prov(g, hdr, row):
    h = [x.lower() for x in hdr]
    def col(name):
        for i, x in enumerate(h):
            if x == name:
                return i
        return None
    idc = 0
    prov_i = col("provision")
    first = clean(row[idc])
    if g == 3:                       # columns: Law | provision (a description) | ...
        return "s." + first
    if g == 2:                       # id is the Law's numbering; the provision column is a description
        return ("s." + first) if re.match(r"^\d", first) else first
    if g == 8:
        return clean(row[prov_i]) if prov_i is not None else first
    if prov_i is not None:
        p = clean(row[prov_i])
        if len(p) <= 40:
            return p
    return first


for g in range(1, 9):
    text = (DEP / ("FRAGMENT-G%d.md" % g)).read_text(encoding="utf-8")
    hdr, rows = find_table(text)
    h = [x.lower() for x in hdr]
    disp_i = h.index("disposition")
    mod_i = h.index("module")
    cnt = collections.Counter()
    for r in rows:
        if len(r) != len(hdr):
            raise SystemExit("G%d: a row has %d cells, header has %d: %s" % (g, len(r), len(hdr), r[0]))
        prov = norm_prov(g, hdr, r)
        disp = clean(r[disp_i]).lower()
        m = re.match(r"^(encoded|inert|refused|out-of-scope|deferred)\b", disp)
        if m:
            disp = m.group(1)
        if disp not in DISPS:
            raise SystemExit("G%d %s: odd disposition %r" % (g, prov, disp))
        mod = clean(r[mod_i])
        out_rows.append((prov, disp, mod, "G%d" % g))
        cnt[disp] += 1
    summary["G%d" % g] = (len(rows), cnt)

tsv = ["provision\tdisposition\tmodule\tgroup"] + ["\t".join(r) for r in out_rows]
(DEP / "coverage-all.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
print("group  rows  " + "  ".join(DISPS))
tot = collections.Counter(); totn = 0
for g, (n, cnt) in summary.items():
    print("%-5s %5d  " % (g, n) + "  ".join("%12d" % cnt[d] for d in DISPS))
    tot.update(cnt); totn += n
print("%-5s %5d  " % ("ALL", totn) + "  ".join("%12d" % tot[d] for d in DISPS))
