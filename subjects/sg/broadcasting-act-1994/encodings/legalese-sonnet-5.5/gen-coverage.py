#!/usr/bin/env python3
"""Coverage table for the Broadcasting Act 1994 encoding (a tool, not law).

usage: python3 -I gen-coverage.py rows  TEXT            -> prints the row list (id, lines, first words)
       python3 -I gen-coverage.py table TEXT DISP.tsv    -> prints the markdown coverage table and the totals
       python3 -I gen-coverage.py audit TEXT DISP.tsv DIR -> checks the table against the .l4 files in DIR

How rows are made.  TEXT is the deposited text.  Every line from 1 to the last belongs to exactly ONE row,
so every non-blank line of the text falls in some row by construction; the script then PROVES it by
re-deriving the set of row lines and comparing it with the set of non-blank lines.
A row starts at: the cover; a PART heading; a section's marginal heading (or the section line itself when it has none);
a subsection marker "(n)" that continues the sequence; a paragraph marker "(x)" that continues the sequence;
a defined term of s 2(1); each item of a Schedule.  A row ends where the next begins.
Page furniture (running heads, "Informal Consolidation" footers, page numbers) is NOT a row: it is counted
under the row it sits in, and listed in the totals line.  Amendment notes "[Act 38 of 2022 wef ...]" likewise
sit in the row above them.

DISP.tsv has one entry per line: START END DISPOSITION MODULE NOTE (tab separated).
A row takes the disposition of the entry whose line range contains the row's first line; a later entry
overrides an earlier one.  Rows with no entry are 'deferred'.
Dispositions: encoded, inert1, inert2, inert3, fork, repealed, notobtained, deferred.
"""
import re, sys, collections, os

FURN = [
    re.compile(r"^\s*Informal Consolidation . version in force from"),
    re.compile(r"^\s*\d+\s+Broadcasting Act 1994\s+2020 Ed\.\s*$"),
    re.compile(r"^\s*2020 Ed\.\s+Broadcasting Act 1994\s+\d+\s*$"),
    re.compile(r"^\s*[ivx]+\s*$"),
    re.compile(r"^\s*\.?\s*[ivx]+\s*$"),
    re.compile(r"^\s*(FIRST|SECOND|THIRD|FOURTH) SCHEDULE . continued\s*$"),
]
ANNOT = re.compile(r"^\s*\[(Act |S |G\.N\.|\d+/\d{4}|Deleted|\d+ of)")


def is_furn(l):
    return any(p.match(l) for p in FURN)


def lines_of(path):
    return open(path, encoding="utf-8").read().split("\n")


def nextletter(prev):
    # (a)->(b) ... (z)->(za)? we only need a..z and aa-style are not present in BA
    if prev is None:
        return {"a"}
    if len(prev) == 1 and prev != "z":
        return {chr(ord(prev) + 1)}
    return set()


def build_rows(L):
    n = len(L)
    rows = []  # dict(id, kind, start, end(inclusive), label)
    # region boundaries
    first_sec = None
    sched_start = None
    hist_start = None
    for i, l in enumerate(L, 1):
        if first_sec is None and re.match(r"^\s*1\.\s+This Act is the Broadcasting Act 1994", l):
            first_sec = i
        if sched_start is None and re.match(r"^\s+FIRST SCHEDULE\s*$", l) and i > 4000:
            sched_start = i
        if hist_start is None and re.match(r"^\s+LEGISLATIVE HISTORY\s*$", l):
            hist_start = i
    assert first_sec and sched_start and hist_start, (first_sec, sched_start, hist_start)

    def add(rid, kind, start, label=""):
        rows.append(dict(id=rid, kind=kind, start=start, end=None, label=label))

    # front matter: cover (1-ish up to the Arrangement), arrangement, long title/enacting
    add("front:cover", "front", 1, "title page and 2020 Revised Edition notice")
    arr = next(i for i, l in enumerate(L, 1) if re.match(r"^\s*ARRANGEMENT OF SECTIONS", l))
    add("front:arrangement", "front", arr, "Arrangement of Sections (contents list)")
    lt = next(i for i, l in enumerate(L, 1) if l.startswith("An Act to regulate dealing in"))
    add("front:long-title", "front", lt, "long title")
    cm = next(i for i, l in enumerate(L, 1) if re.match(r"^\s+\[1 October 1994\]", l))
    add("front:commencement", "front", cm, "commencement note [1 October 1994]")

    # body: sections
    sec_re = re.compile(r"^\s*(\d+[A-Z]?)\.(?:\s*[—-]\s*\(|\s)")
    last_sec_no = 0
    last_sec_suffix = ""
    secs = []  # (line, label, num)
    for i in range(first_sec, sched_start):
        l = L[i - 1]
        m = sec_re.match(l)
        if not m:
            continue
        lab = m.group(1)
        num = int(re.match(r"\d+", lab).group())
        suf = lab[len(str(num)):]
        ok = (num == last_sec_no + 1 and suf == "") or (num == last_sec_no and suf and suf > last_sec_suffix) or (num == last_sec_no + 1 and suf == "")
        if lab == "1":
            ok = True
        if ok:
            secs.append((i, lab, num))
            last_sec_no, last_sec_suffix = num, suf
    # headings: look back from each section line
    def back_heading(i):
        j = i - 1
        # skip blanks / furniture
        while j >= 1 and (L[j - 1].strip() == "" or is_furn(L[j - 1])):
            j -= 1
        top = j
        # heading block: consecutive non-blank non-furniture lines ending at j, that are not body text
        k = j
        while k >= 1 and L[k - 1].strip() != "" and not is_furn(L[k - 1]):
            k -= 1
        block = [L[x - 1].strip() for x in range(k + 1, j + 1)]
        # a marginal heading has no terminal body punctuation and is short
        if block and len(block) <= 3 and (not re.search(r"[.;—:,\]]$", block[-1]) or block[-1].endswith(", etc."))  and not re.match(r"^\(?[0-9a-z]+\)", block[0]) and len(" ".join(block)) < 150:
            return k + 1, " ".join(block)
        return None, ""

    part_re = re.compile(r"^\s*PART \d+[A-Z]?\s*$")
    # PART headings
    parts = []
    for i in range(cm + 1, sched_start):
        if part_re.match(L[i - 1]):
            parts.append(i)
    for p in parts:
        add("part:" + L[p - 1].strip().replace("PART ", ""), "part", p, "Part heading")
    # Division headings of Part 10A
    for i in range(first_sec, sched_start):
        if re.match(r"^\s*Division \d+ . ", L[i - 1]) or re.match(r"^\s+Division \d+", L[i - 1]):
            add("division:" + re.match(r"^\s*(Division \d+)", L[i - 1]).group(1).replace(" ", ""), "part", i, "Division heading")
    sec_start = {}
    for (i, lab, num) in secs:
        hs, hl = back_heading(i)
        lower = secs[secs.index((i, lab, num)) - 1][0] if secs.index((i, lab, num)) > 0 else cm
        st = hs if (hs and hs > lower) else i
        # do not swallow a PART line into the heading
        if st < i and any(st <= p <= i for p in parts):
            st = max(p for p in parts if st <= p <= i) + 1
            # skip any PART title line directly after the PART line
            while st < i and (L[st - 1].strip() == "" or is_furn(L[st - 1]) or re.match(r"^\s*[A-Z][A-Z ,\-—’'()]+$", L[st - 1].strip())):
                st += 1
        sec_start[lab] = (st, i, hl)
        if st < i:
            add("s" + lab + ":heading", "heading", st, hl or "marginal heading")
        add("s" + lab, "section", i, "")
    # subsection / paragraph / definition rows inside each section
    for idx, (i, lab, num) in enumerate(secs):
        end = (secs[idx + 1][0] - 1) if idx + 1 < len(secs) else sched_start - 1
        st = sec_start[lab][0]
        # section row already added at st; now split inside [i, end]
        prev_sub = None
        prev_para = None
        sub_re = re.compile(r"^\s*(?:\d+[A-Z]?\.\s*[—-]\s*)?\((\d+[A-Z]*)\)\s")
        para_re = re.compile(r"^\s*\(([a-z]{1,2})\)\s")
        is_s2 = (lab == "2")
        in_defs = False
        for j in range(i, end + 1):
            l = L[j - 1]
            m = sub_re.match(l)
            if m:
                sn = m.group(1)
                ok = False
                if prev_sub is None:
                    ok = sn == "1" or (j == i)
                else:
                    pn = int(re.match(r"\d+", prev_sub).group())
                    sm = re.match(r"(\d+)([A-Z]*)", sn)
                    cn, cs = int(sm.group(1)), sm.group(2)
                    pm = re.match(r"(\d+)([A-Z]*)", prev_sub)
                    ppn, pps = int(pm.group(1)), pm.group(2)
                    ok = (cn == ppn + 1 and cs == "") or (cn == ppn and cs > pps and len(cs) == 1)
                    if is_s2 and in_defs:
                        ok = ok  # only (2).. after the definitions
                if ok:
                    prev_sub = sn
                    prev_para = None
                    if j != st:
                        add("s%s(%s)" % (lab, sn), "subsection", j, "")
                    else:
                        pass
                    in_defs = (is_s2 and sn == "1")
                    # the first subsection starts on the section line: relabel section row
                    if j == i and not (j != st):
                        pass
                    continue
            if is_s2 and prev_sub == "1" and re.match(r"^\s*“[^”]+”", l) and (L[j - 2].strip() == "" or is_furn(L[j - 2]) or ANNOT.match(L[j - 2])):
                term = re.match(r"^\s*“([^”]+)”", l).group(1)
                add("s2(1)-def:" + term, "definition", j, term)
                continue
            if is_s2 and prev_sub == "1":
                continue  # paragraphs inside a definition stay in the definition row
            m = para_re.match(l)
            if m and prev_sub is not None:
                px = m.group(1)
                if px in nextletter(prev_para) or (prev_para is None and px == "a"):
                    prev_para = px
                    add("s%s(%s)(%s)" % (lab, prev_sub, px), "paragraph", j, "")
                    continue
            elif m and prev_sub is None:
                px = m.group(1)
                if px in nextletter(prev_para):
                    prev_para = px
                    add("s%s(%s)" % (lab, px), "paragraph", j, "")
                    continue
        # when the section line itself carries "(1)", rename: section row id covers the chapeau of (1)
    # schedules
    sched_items = [
        (sched_start, "sch1:heading", "First Schedule heading"),
    ]
    for i in range(sched_start, hist_start):
        l = L[i - 1]
        if re.match(r"^\s+(FIRST|SECOND|THIRD|FOURTH) SCHEDULE\s*$", l) and not re.search("continued", l):
            nm = re.match(r"^\s+(FIRST|SECOND|THIRD|FOURTH)", l).group(1).lower()
            add("sch-" + nm + ":heading", "schedule", i, nm + " schedule heading and title")
    # items
    cur = None
    for i in range(sched_start, hist_start):
        l = L[i - 1]
        m = re.match(r"^\s+(FIRST|SECOND|THIRD|FOURTH) SCHEDULE\s*$", l)
        if m and "continued" not in l:
            cur = m.group(1).lower()
        if cur is None:
            continue
        if cur in ("first", "second"):
            mm = re.match(r"^\s*(\d+)\.\s+\S", l)
            if mm:
                add("sch-%s:item-%s" % (cur, mm.group(1)), "schedule", i, "item " + mm.group(1))
            if re.match(r"^\s*In this Schedule", l) or re.match(r"^\s*For the purposes of this Schedule", l):
                add("sch-%s:interpretation" % cur, "schedule", i, "interpretation paragraph")
        elif cur == "third":
            if re.match(r"^\s*1\. Subscription nationwide television", l):
                add("sch-third:row-1", "schedule", i, "table row 1 (service; providers (a) and (b))")
        elif cur == "fourth":
            if re.match(r"^\s+PART [12]\s*$", l):
                add("sch-fourth:part-" + l.strip().split()[-1], "schedule", i, "Part heading")
            mm = re.match(r"^\s*(\d+)\.\s+(\S.*)", l)
            if mm and re.match(r"^\s*(1|2)\. (Social media service|App distribution service)\.", l):
                add("sch-fourth:part-1-item-" + mm.group(1), "schedule", i, "item " + mm.group(1))
            if re.match(r"^\s*1\. In this Schedule", l):
                add("sch-fourth:p2-item-1", "schedule", i, "item 1 (definitions chapeau)")
            mm = re.match(r"^\s*“(app|app distribution service)”", l)
            if mm:
                add("sch-fourth:def:" + mm.group(1), "definition", i, mm.group(1))
    add("history:legislative-history", "history", hist_start, "Legislative History (the text says it is not part of the Act), abbreviations, comparative table")
    # sort, dedupe by start line (keep first), compute ends
    rows.sort(key=lambda r: (r["start"], 0 if r["kind"] in ("part",) else 1))
    out = []
    seen = set()
    for r in rows:
        if r["start"] in seen:
            # same start line: keep the more specific one (a subsection marker beats a section row only if the line is the section line)
            continue
        seen.add(r["start"])
        out.append(r)
    rows = out
    for k, r in enumerate(rows):
        r["end"] = (rows[k + 1]["start"] - 1) if k + 1 < len(rows) else n
    return rows


def fix_first_subsection_ids(rows, L):
    """A section line such as '8.—(1) A person ...' starts the section row AND subsection (1).
    Name that row s8(1) (with the marginal heading) rather than s8."""
    for r in rows:
        if r["kind"] != "section":
            continue
        lab = r["id"][1:]
        # first non-heading line of the row
        j = r["start"]
        if j <= r["end"] and re.match(r"^\s*%s\.\s*[—-]\s*\(1[A-Z]?\)" % re.escape(lab), L[j - 1]):
            r["id"] = "s%s(1)" % lab
            r["kind"] = "subsection"
    return rows


def is_blank_or_furn(l):
    return l.strip() == "" or is_furn(l)


def load_disp(path):
    ents = []
    if path and os.path.exists(path):
        for ln in open(path, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("#"):
                continue
            p = ln.split("\t")
            while len(p) < 5:
                p.append("")
            ents.append((int(p[0]), int(p[1]), p[2], p[3], p[4]))
    return ents


def disp_for(r, ents):
    d = ("deferred", "", "")
    for (a, b, dd, mod, note) in ents:
        if a <= r["start"] <= b:
            d = (dd, mod, note)
    return d


def audit(L, rows, ents, folder):
    """Checks the table against the .l4 files in FOLDER; exits 1 on any finding.
    (1) no row is 'deferred'; (2) every 'encoded' row has at least one @ref of a layer-1 module overlapping its text lines;
    (3) every other row is overlapped by no @ref, or is reported (information); (4) every @ref in a layer-1 module is followed by a
    rule whose name occurs in a tests file or a cases file (a rule nothing asserts is a finding); (5) each fork row names an F-BA entry."""
    import glob
    refs = []
    irefs = []
    heads = []
    tests_text = ""
    for pth in sorted(glob.glob(os.path.join(folder, "sgba-*.l4"))):
        b = os.path.basename(pth)[:-3]
        txt = open(pth, encoding="utf-8").read()
        if b.startswith("sgba-tests") or b.endswith("cases-seat") or b.startswith("sgba-tv-cases"):
            tests_text += txt + "\n"
            continue
        if b.endswith("-seat") or b == "sgba-tv-s9a":
            continue  # seat modules carry questions, not provisions
        instr = b.startswith("sgba-i-")  # an instrument's locators are lines of its own deposit: they take part in the test-name check only
        lines = txt.split("\n")
        for k, ln in enumerate(lines):
            m = re.match(r"^@ref (.*) \(src:(\d+)(?:-(\d+))?\)\s*$", ln)
            if not m:
                continue
            lo, hi = int(m.group(2)), int(m.group(3) or m.group(2))
            name = None
            for ln2 in lines[k + 1:k + 40]:
                mm = re.match(r"^(?:DECIDE\s+)?`([^`]+)`", ln2)
                if mm:
                    name = mm.group(1)
                    break
                if ln2.startswith("DECLARE "):
                    break
            if instr:
                irefs.append((lo, hi, b, m.group(1), name))
            else:
                refs.append((lo, hi, b, m.group(1), name))
    bad = 0
    def content(i):
        l = L[i - 1]
        return l.strip() and not is_furn(l) and not ANNOT.match(l)
    for r in rows:
        d, mod, note = disp_for(r, ents)
        cl = [i for i in range(r["start"], r["end"] + 1) if content(i)]
        hit = [x for x in refs if any(x[0] <= i <= x[1] for i in cl)]
        if d == "deferred":
            print("FINDING deferred row:", r["id"]); bad += 1
        if d == "encoded" and cl and not hit:
            print("FINDING encoded row with no @ref over it:", r["id"], "%d-%d" % (r["start"], r["end"])); bad += 1
        if d != "encoded" and hit and d not in ("fork",):
            print("INFO row %s is '%s' but @ref(s) overlap it: %s" % (r["id"], d, "; ".join(sorted(set(h[2] for h in hit)))))
        if d == "fork" and not re.search(r"F-BA-\d+", note):
            print("FINDING fork row without an F-BA entry in its note:", r["id"]); bad += 1
    # every rule head in a layer-1 or instrument module, not only the first after each @ref, must be named in a tests or cases file
    heads = []
    for pth in sorted(glob.glob(os.path.join(folder, "sgba-*.l4"))):
        b = os.path.basename(pth)[:-3]
        if b.startswith("sgba-tests") or b.endswith("cases-seat") or b.endswith("-seat") or b.startswith("sgba-tv-") or b in ("sgba-nouns", "sgba-vintage"):
            continue
        for ln in open(pth, encoding="utf-8"):
            mm = re.match(r"^(?:DECIDE\s+)?`([^`]+)`\s+(?:MEANS|IS|IF)\b", ln)
            if mm:
                heads.append((b, mm.group(1)))
    for (b, name) in heads:
        if name not in tests_text:
            print("FINDING rule head never named in a tests or cases file: `%s` (%s)" % (name, b)); bad += 1
    seen = set()
    for (lo, hi, mod, cite, name) in refs + irefs:
        if name is None:
            print("FINDING @ref with no rule head after it: %s (%s src:%d-%d)" % (cite, mod, lo, hi)); bad += 1
        elif name not in tests_text and (mod, name) not in seen:
            seen.add((mod, name))
            print("FINDING rule never named in a tests or cases file: `%s` (%s, @ref %s)" % (name, mod, cite)); bad += 1
    print("audit: %d rows, %d @refs in layer-1 modules, %d @refs in instrument modules, %d rule heads checked, %d findings" % (len(rows), len(refs), len(irefs), len(heads), bad))
    sys.exit(1 if bad else 0)


def main():
    cmd = sys.argv[1]
    L = lines_of(sys.argv[2])
    if L and L[-1] == "":
        L = L[:-1]
    rows = fix_first_subsection_ids(build_rows(L), L)
    # proof: every non-blank line is in exactly one row
    cover = collections.Counter()
    for r in rows:
        for x in range(r["start"], r["end"] + 1):
            cover[x] += 1
    nonblank = [i for i, l in enumerate(L, 1) if l.strip()]
    missing = [i for i in nonblank if cover[i] != 1]
    assert not missing, "lines not in exactly one row: %s" % missing[:10]
    furn = sum(1 for i in nonblank if is_furn(L[i - 1]))
    if cmd == "rows":
        for r in rows:
            print("%s\t%d-%d\t%s\t%s" % (r["id"], r["start"], r["end"], r["kind"], (r["label"] or L[r["start"] - 1].strip())[:70]))
        print("# %d rows; %d non-blank lines, all in exactly one row; %d of them page furniture" % (len(rows), len(nonblank), furn), file=sys.stderr)
        return
    if cmd == "audit":
        return audit(L, rows, load_disp(sys.argv[3]), sys.argv[4])
    ents = load_disp(sys.argv[3])
    tot = collections.Counter()
    print("| row | lines | text (first words) | disposition | module | note |")
    print("| --- | --- | --- | --- | --- | --- |")
    names = dict(encoded="encoded", inert1="inert (1) not operative", inert2="inert (2) machinery", inert3="inert (3) repealed or blank text", fork="fork", repealed="repealed or blank in this text", notobtained="source not obtained", deferred="DEFERRED")
    for r in rows:
        d, mod, note = disp_for(r, ents)
        tot[d] += 1
        txt = (r["label"] or L[r["start"] - 1].strip())
        txt = re.sub(r"\s+", " ", txt)[:60].replace("|", "/")
        print("| %s | %d-%d | %s | %s | %s | %s |" % (r["id"].replace("|", "/"), r["start"], r["end"], txt, names.get(d, d), mod, note.replace("|", "/")))
    print()
    print("Totals: %d rows; " % len(rows) + "; ".join("%s %d" % (names.get(k, k), v) for k, v in sorted(tot.items())))
    print("Every one of the %d non-blank lines of the text is in exactly one row (%d of them page furniture, kept in the row they sit in)." % (len(nonblank), furn))


if __name__ == "__main__":
    main()
