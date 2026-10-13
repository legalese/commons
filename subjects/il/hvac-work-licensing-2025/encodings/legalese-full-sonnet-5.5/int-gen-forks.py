#!/usr/bin/env python3
"""int-gen-forks.py: build the fork index from the eight FRAGMENT-Gk.md files: for every fork, its id, its group, and one line on the
reading taken.  The fork headings differ by group (a level-3 heading, a bold line, a bold bullet, a table row), so each group has its own
pattern; the line on the reading taken is the first sentence of the fork's block that says what was taken, found mechanically.
Writes forks-index.md (a table, for NOTES.md) and forks-index.tsv to the work directory; prints counts per group.  Hebrew is not touched
except that a run of Hebrew inside a sentence copied from a FRAGMENT is replaced by a marker."""
import pathlib, re, sys, collections

DEP = pathlib.Path(__file__).resolve().parent  # this script sits in the deposit beside the modules it reads
if len(sys.argv) != 2:
    sys.exit("usage: %s OUTDIR   (a directory that exists; the generated files are written there, not into the deposit)" % sys.argv[0])
WORK = pathlib.Path(sys.argv[1])

HEB = re.compile("[\u0590-\u05FF]+(?:[ \u0590-\u05FF\u2026\u05BE\u05F3\u05F4\"'.,-]*[\u0590-\u05FF])?")


def noheb(text):
    """The index is for NOTES.md, which carries no Hebrew (Hebrew is copied only by srcrefs.py): a run of Hebrew in a sentence taken from a FRAGMENT is replaced by a marker; the FRAGMENT line shown has the words."""
    return HEB.sub("[Hebrew, see the FRAGMENT]", text)


START = {
    1: re.compile(r"^### (F\d+)\.\s*(.*)$"),
    2: re.compile(r"^\*\*(F[A-Z]\d+[a-z]?)\b\s*(.*?)\*\*\s*$"),
    3: re.compile(r"^\*\*((?:S\d+[A-Za-z0-9\-]*|COM))\b[ ,(:]?\s*(.*?)\*\*\s*$"),
    4: re.compile(r"^- \*\*((?:F|C|G)-[A-Za-z0-9\-]+)\b\s*(.*?)\*\*(.*)$"),
    5: re.compile(r"^\*\*(F-[A-Z0-9\-]+)\b\s*(.*?)\*\*\s*$"),
    6: re.compile(r"^- \*\*(F-[A-Z0-9\-]+)\b\s*,?\s*(.*?)\*\*(.*)$"),
    7: re.compile(r"^### (F-[A-Za-z0-9\-]+)\b\s*(.*)$"),
}
G8_ROW = re.compile(r"^\| (F\d+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|\s*$")
G5_TABLE = re.compile(r"^\| (F-P\d+) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|\s*$")


def forks_region(text):
    lines = text.split("\n")
    s = None
    for i, l in enumerate(lines):
        if re.match(r"^##\s+(\(2\)\s+|2\.\s+)Forks", l):
            s = i
            break
    if s is None:
        raise SystemExit("no forks heading")
    e = len(lines)
    for j in range(s + 1, len(lines)):
        if re.match(r"^## ", lines[j]):
            e = j
            break
    return s, lines[s:e]


ABBREV = re.compile(r"(\b(?:s|ss|IL|no|e\.g|cf|vs|ch|reg|art|para|pp|p)\.)\s")


def protect(t):
    t = ABBREV.sub(lambda m: m.group(1).replace(".", "\u2024") + " ", t)
    t = re.sub(r"\b(s|ss|IL s|IL ss|reg|regs)\.(?=[\w(])", lambda m: m.group(0).replace(".", "\u2024"), t)
    return re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\u2024" + m.group(2), t)


def sentence_taken(block):
    flat = " ".join(x.strip() for x in block if x.strip())
    flat = protect(re.sub(r"\s+", " ", flat))
    for pat in (r"(Reading taken[^.]*?[:.]\s?[^.]*\.)", r"(Reading taken\s*\([^)]*\)[^.]*\.)", r"(\bTaken[:,]?\s[^.]*\.)", r"(Taken and alternative[^.]*\.)",
                r"(\bTaken \(assumed[^.]*\.)", r"(\(taken\)[^.]*\.)", r"([^.]*\btaken\b[^.]*\.)"):
        m = re.search(pat, flat)
        if m:
            t = m.group(1).strip()
            if len(t) < 40:
                r = re.search(r"((?:Readings?|Why)[^.]*\.)", flat)
                if r and r.group(1).strip() != t and not t.startswith("Reading"):
                    t = t + " [" + r.group(1).strip()[:200] + "]"
            t = t.replace("\u2024", ".")
            return t[:300] + ("..." if len(t) > 300 else "")
    return ((flat[:200] + "...") if flat else "").replace("\u2024", ".")


rows = []
for g in range(1, 9):
    text = (DEP / ("FRAGMENT-G%d.md" % g)).read_text(encoding="utf-8")
    s, region = forks_region(text)
    found = []
    if g == 8:
        for i, l in enumerate(region):
            m = G8_ROW.match(l)
            if m:
                found.append((i, m.group(1), m.group(2), [m.group(4)], ""))
    else:
        pat = START[g]
        for i, l in enumerate(region):
            m = pat.match(l)
            if m:
                rest = m.group(3) if g in (4, 6) and m.lastindex and m.lastindex >= 3 else ""
                found.append((i, m.group(1), m.group(2).strip(" .:*"), None, rest))
        if g == 5:
            for i, l in enumerate(region):
                m = G5_TABLE.match(l)
                if m:
                    found.append((i, m.group(1), "period " + m.group(2) + ", " + m.group(3), ["Kind " + m.group(4) + "; IL s.10(c) " + m.group(5) + "; taken."], ""))
        found.sort()
    for idx, (i, fid, title, block, rest) in enumerate(found):
        if block is None:
            nxt = found[idx + 1][0] if idx + 1 < len(found) else len(region)
            # the block ends at the next fork start, or at the next heading of level 3
            blk = []
            for l in region[i + 1:nxt]:
                if l.startswith("### ") and g not in (1, 7):
                    break
                blk.append(l)
            block = ([rest] if rest.strip() else []) + blk
        taken = sentence_taken(block)
        rows.append((fid, "G%d" % g, noheb(title), noheb(taken), s + i + 1))

# Owner rulings on forks (int-rulings.tsv, beside this script): appended to the row of the fork they rule on.
rulings = {}
rpath = DEP / "int-rulings.tsv"
if rpath.exists():
    for line in rpath.read_text(encoding="utf-8").split("\n"):
        if line.strip() and not line.startswith("#"):
            c = line.split("\t")
            rulings[(c[0], c[1])] = "RULED %s by the owner: option %s; condition: %s; the owner's words, verbatim: \"%s\"" % (c[5], c[2], c[3], c[4])
rows = [(fid, grp, title, (taken + " " + rulings[(fid, grp)]) if (fid, grp) in rulings else taken, ln) for fid, grp, title, taken, ln in rows]
missing = [k for k in rulings if not any((r[0], r[1]) == k for r in rows)]
if missing:
    sys.exit("int-rulings.tsv names a fork that no FRAGMENT registers: %s" % missing)

tsv = ["fork\tgroup\ttitle\treading taken\tFRAGMENT line"] + ["\t".join([r[0], r[1], r[2], r[3], str(r[4])]) for r in rows]
(WORK / "forks-index.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
md = ["| fork | group | what it is about | reading taken (first sentence that says so) | FRAGMENT line |", "| --- | --- | --- | --- | --- |"]
for fid, grp, title, taken, ln in rows:
    esc = lambda x: x.replace("|", "\\|")
    md.append("| `%s` | %s | %s | %s | %s |" % (fid, grp, esc(title), esc(taken), "FRAGMENT-%s.md:%d" % (grp, ln)))
(WORK / "forks-index.md").write_text("\n".join(md) + "\n", encoding="utf-8")
c = collections.Counter(r[1] for r in rows)
print("forks per group:", dict(sorted(c.items())), "total", len(rows))
empty = [r[0] + "/" + r[1] for r in rows if not r[3]]
print("forks with no taken sentence:", empty)
