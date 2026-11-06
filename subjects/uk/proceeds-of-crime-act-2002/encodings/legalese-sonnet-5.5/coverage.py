#!/usr/bin/env python3
"""Coverage table builder and audit for the POCA Part 7 / Schedule 9 encoding.

  python3 -I coverage.py audit            parse both source texts into rows, print the counts and the lines no row owns
  python3 -I coverage.py list             print every row (label, kind, lines) -- the skeleton to give dispositions to
  python3 -I coverage.py check            every row must resolve to a disposition in coverage-map.tsv (no 'deferred'); print counts
  python3 -I coverage.py write NOTES.md   replace the region between the COVERAGE markers in NOTES.md with the table

Rows: part heading, cross heading, section, subsection, lettered paragraph (depth 1), schedule part/paragraph,
defined term.  Every non-blank line belongs to exactly one FINEST row (its own paragraph, subsection, section or heading);
the audit counts them.  Schedule 9 paragraph numbers are NOT in the deposited text; they are assigned in order of the
headings (see the fork register, F1).

coverage-map.tsv: label <TAB> disposition <TAB> rules / reason <TAB> tests / fork.  A row with no entry of its own takes
its parent's entry (strip the last (..) group, or a trailing term in quotes); the first entry found wins.
"""
import os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.environ.get("RAW_DIR", os.path.join(HERE, "..", "..", "..", "inputs"))
FILES = [("part7", "ukpga-2002-29-part-7.txt"), ("sch9", "ukpga-2002-29-schedule-9.txt")]


def nfc(s):
    return unicodedata.normalize("NFC", s)


def successors(p):
    out = [chr(ord(p[0]) + 1), p + "a"]
    if len(p) > 1:
        out.append(p[:-1] + chr(ord(p[-1]) + 1))
    return out


class Row:
    def __init__(self, label, kind, start, src, parent=None):
        self.label, self.kind, self.start, self.end, self.src, self.parent = label, kind, start, start, src, parent

    def span(self):
        return f"{self.start}-{self.end}" if self.end != self.start else f"{self.start}"


def parse(src, fname):
    path = os.path.join(RAWDIR, fname)
    lines = open(path, encoding="utf-8").read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    rows, finest = [], {}
    is_sch = src == "sch9"
    sec = sub = par = head = None
    prev_letter = None
    para_no = 0
    pending_implicit = False
    sec_label = None

    def add(label, kind, i, parent):
        r = Row(label, kind, i, src, parent)
        rows.append(r)
        return r

    for i, raw in enumerate(lines, 1):
        line = raw.rstrip("\r")
        if not line.strip():
            continue
        # --- tab-led lines: headings
        if line.startswith("\t"):
            text = line.strip()
            if is_sch:
                if re.match(r"^(SCHEDULE|PART|Part)\b", text):
                    head = add(f'sch 9 heading "{text}"', "heading", i, None)
                    sec = sub = par = None
                    pending_implicit = text.upper().startswith("PART")
                else:
                    para_no += 1
                    pending_implicit = False
                    sec = add(f"sch 9 para {para_no}", "section", i, None)
                    sub = par = head = None
                    prev_letter = None
                finest[i] = sec if sec and sec.start == i else head
                (sec if sec and sec.start == i else head).end = i
                continue
            if i == 1:
                head = add("part 7 heading", "heading", i, None)
            else:
                head = add(f'part 7 heading "{text}"', "heading", i, None)
            sec = sub = par = None
            finest[i] = head
            head.end = i
            continue
        # --- section heading (Part 7)
        m = re.match(r"^(\d+[A-Z]*)\t(.*)$", line)
        if m and not is_sch:
            sec = add(f"s {m.group(1)}", "section", i, None)
            sub = par = head = None
            prev_letter = None
            finest[i] = sec
            sec.end = i
            continue
        # implicit schedule paragraph after a PART heading with no paragraph heading
        if is_sch and pending_implicit and sec is None:
            para_no += 1
            sec = add(f"sch 9 para {para_no}", "section", i, None)
            pending_implicit = False
            sub = par = None
            prev_letter = None
        owner = sec
        m = re.match(r"^\((\d+[A-Z]*)\) ", line)
        if m and sec is not None:
            sub = add(f"{sec.label}({m.group(1)})", "subsection", i, sec)
            par = None
            prev_letter = None
            finest[i] = sub
            for r in (sub, sec):
                r.end = i
            continue
        m = re.match(r"^\(([a-z]+)\) ", line)
        if m and sub is not None or (m and sec is not None):
            lab = m.group(1)
            base = sub if sub is not None else sec
            depth1 = False
            if prev_letter is None:
                depth1 = lab == "a"
            else:
                depth1 = lab in successors(prev_letter)
            if depth1:
                par = add(f"{base.label}({lab})", "paragraph", i, base)
                prev_letter = lab
                finest[i] = par
                for r in (par, base, sec):
                    r.end = i
                continue
        # --- continuation line
        tgt = par or sub or sec or head
        if tgt is None:
            print(f"UNOWNED {fname}:{i}: {line[:60]}", file=sys.stderr)
            continue
        finest[i] = tgt
        tgt.end = i
        for r in (par, sub, sec):
            if r is not None:
                r.end = i
    return lines, rows, finest


TERM_RE = re.compile(r"[“\"]([^”\"]{1,70})[”\"]\s*(?:\(\s*)?(means|has the same meaning|has the meaning|includes|is|are)\b")
PAREN_RE = re.compile(r"\(\s*[“\"]([^”\"]{1,60})[”\"]\s*\)")
# definitions the text gives without quotation marks: (parent label, phrase that must occur within the parent's lines, term name)
EXTRA_TERMS = [
    ("s 330(5)", "The required disclosure is", "the required disclosure"),
    ("s 330(5A)", "The laundered property is", "the laundered property"),
    ("s 330(9)", "A disclosure to a nominated officer is", "a disclosure to a nominated officer"),
    ("s 330(10)", "in privileged circumstances if", "information that comes to an adviser in privileged circumstances"),
    ("s 330(13)", "An appropriate body is", "an appropriate body"),
    ("s 330(14)", "A relevant professional adviser is", "a relevant professional adviser"),
    ("s 331(5)", "The required disclosure is", "the required disclosure"),
    ("s 331(5A)", "The laundered property is", "the laundered property"),
    ("s 331(9)", "An appropriate body is", "an appropriate body"),
    ("s 332(5)", "The required disclosure is", "the required disclosure"),
    ("s 332(5A)", "The laundered property is", "the laundered property"),
    ("s 332(5B)", "The applicable section is", "the applicable section"),
    ("s 335(1)", "The appropriate consent is", "the appropriate consent"),
    ("s 335(5)", "The notice period is", "the notice period"),
    ("s 335(6)", "The moratorium period is", "the moratorium period"),
    ("s 335(7)", "A working day is", "a working day"),
    ("s 335(9)", "A nominated officer is", "a nominated officer"),
    ("s 336(7)", "The notice period is", "the notice period"),
    ("s 336(8)", "The moratorium period is", "the moratorium period"),
    ("s 336(9)", "A working day is", "a working day"),
    ("s 336(11)", "A nominated officer is", "a nominated officer"),
    ("s 337(5)", "A disclosure to a nominated officer is", "a disclosure to a nominated officer"),
    ("s 338(5)", "A disclosure to a nominated officer is", "a disclosure to a nominated officer"),
    ("s 340(2)", "Criminal conduct is", "criminal conduct"),
    ("s 340(3)", "Property is criminal property if", "criminal property"),
    ("s 340(5)", "A person benefits from conduct if", "benefits from conduct"),
    ("s 340(9)", "Property is all property", "property"),
    ("s 340(11)", "Money laundering is", "money laundering"),
    ("s 340(14)", "Deposit-taking body", "deposit-taking body"),
    ("s 340(14C)", "Electronic money institution", "electronic money institution"),
    ("s 340(15)", "Information order", "information order"),
    ("s 340(16)", "Payment institution", "payment institution"),
    ("s 340(17)", "Business relationship", "business relationship"),
    ("s 339ZG(2)", "Disclosure request", "disclosure request"),
    ("s 339ZG(3)", "NCA authorised officer", "NCA authorised officer"),
    ("s 339ZG(4)", "Nominated officer", "nominated officer"),
    ("s 339ZG(5)", "Relevant undertaking", "relevant undertaking"),
    ("s 339ZG(6)", "Required disclosure", "required disclosure"),
    ("s 339ZG(7)", "Required notification", "required notification"),
    ("s 339ZD(4)", "A joint disclosure report is", "a joint disclosure report"),
    ("s 339ZD(6)", "The applicable period is", "the applicable period"),
    ("s 339ZK(2)", "Privileged information", "privileged information"),
    ("s 339ZH(6)", "external request", "external request"),
    ("s 336D(2)", "The court", "the court"),
    ("s 336D(3)", "Interested person", "interested person"),
    ("s 336D(4)", "Moratorium period", "moratorium period"),
    ("s 336D(5)", "Relevant disclosure", "relevant disclosure"),
    ("s 336D(6)", "Relevant property", "relevant property"),
    ("s 336D(7)", "senior officer", "senior officer (Crown Court)"),
    ("s 336D(8)", "senior officer", "senior officer (sheriff)"),
    ("s 336D(9)", "Working day", "working day"),
    ("sch 9 para 3(1)", "the Capital Requirements Regulation", "the Capital Requirements Regulation"),
    ("sch 9 para 3(1)", "the Emission Allowance Auctioning Regulation", "the Emission Allowance Auctioning Regulation"),
    ("sch 9 para 3(1)", "the Markets in Financial Instruments Directive", "the Markets in Financial Instruments Directive"),
    ("sch 9 para 3(1)", "the Solvency 2 Directive", "the Solvency 2 Directive"),
]


def collect(strip_terms=False):
    allrows, finests, srclines = [], {}, {}
    for src, fname in FILES:
        lines, rows, finest = parse(src, fname)
        srclines[src] = lines
        finests[src] = finest
        allrows.extend(rows)
    # defined terms
    byl = {r.label: r for r in allrows}
    terms = []
    for r in list(allrows):
        if r.kind not in ("subsection", "paragraph", "section"):
            continue
        # only take terms from the row's own lines (the finest ones), to avoid duplicates up the tree
        lines = srclines[r.src]
        own = [i for i, row in finests[r.src].items() if row is r]
        for i in own:
            for rx, kind in ((TERM_RE, "t"), (PAREN_RE, "p")):
                for m in rx.finditer(nfc(lines[i - 1])):
                    name = m.group(1).strip()
                    t = Row(f"{r.label} “{name}”", "term", i, r.src, r)
                    if not any(x.label == t.label for x in terms):
                        terms.append(t)
    for parent, phrase, name in EXTRA_TERMS:
        p = byl.get(parent)
        if p is None:
            print(f"EXTRA TERM parent missing: {parent}", file=sys.stderr)
            continue
        lines = srclines[p.src]
        hit = [i for i in range(p.start, p.end + 1) if phrase.lower() in lines[i - 1].lower()]
        if not hit:
            print(f"EXTRA TERM phrase not found in {parent}: {phrase!r}", file=sys.stderr)
            continue
        t = Row(f"{parent} “{name}”", "term", hit[0], p.src, p)
        if not any(x.label == t.label for x in terms):
            terms.append(t)
    return allrows, terms, finests, srclines


def load_map():
    m = {}
    p = os.path.join(HERE, "coverage-map.tsv")
    if os.path.exists(p):
        for ln in open(p, encoding="utf-8"):
            if ln.startswith("#") or not ln.strip():
                continue
            f = ln.rstrip("\n").split("\t")
            while len(f) < 4:
                f.append("")
            m[nfc(f[0])] = f[1:4]
    return m


def resolve(label, m):
    lab = nfc(label)
    while True:
        if lab in m:
            return m[lab], lab
        n = re.sub(r"\s*“[^”]*”$", "", lab)
        if n == lab:
            n = re.sub(r"\([^()]*\)$", "", lab)
        if n == lab:
            n = re.sub(r"^(s \d+[A-Z]*)\(.*$", r"\1", lab)
        if n == lab or not n:
            return None, None
        lab = n


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "audit"
    rows, terms, finests, srclines = collect()
    kinds = {}
    for r in rows + terms:
        kinds[r.kind] = kinds.get(r.kind, 0) + 1
    total = 0
    for src in finests:
        total += len(finests[src])
    nonblank = {s: sum(1 for l in srclines[s] if l.strip()) for s in srclines}
    if cmd == "audit":
        print("non-blank text lines:", nonblank, "total", sum(nonblank.values()))
        print("lines owned by a finest row:", {s: len(finests[s]) for s in finests}, "total", total)
        print("rows by kind:", kinds, "total rows", len(rows) + len(terms))
        miss = [(s, i) for s in srclines for i, l in enumerate(srclines[s], 1) if l.strip() and i not in finests[s]]
        print("non-blank lines with no row:", miss)
        return 0 if not miss and total == sum(nonblank.values()) else 1
    if cmd == "list":
        for r in rows + terms:
            print(f"{r.src}\t{r.kind}\t{r.span()}\t{r.label}")
        return 0
    m = load_map()
    unresolved, counts = [], {}
    table = []
    for r in sorted(rows + terms, key=lambda r: (r.src != "part7", r.start, r.kind != "section")):
        res, via = resolve(r.label, m)
        # a section-level entry covers the section row itself and nothing below it: a subsection with no entry of its own is unresolved
        if res is not None and r.kind != "section" and via != nfc(r.label) and re.match(r"^(s \d+[A-Z]*|sch 9 para \d+)$", via):
            res = None
        if res is None:
            unresolved.append(r.label)
            continue
        disp = res[0].split(":")[0]
        counts[disp] = counts.get(disp, 0) + 1
        table.append((r, res, via))
    if cmd == "check":
        print("rows:", len(rows) + len(terms), "unresolved (deferred):", len(unresolved))
        for u in unresolved[:int(os.environ.get("MAXU","80"))]:
            print("  UNRESOLVED", u)
        print("by disposition:", counts)
        bad = [t for t in table if t[1][0].startswith("deferred") or t[1][0] == "out-of-scope"]
        print("forbidden dispositions:", len(bad))
        return 0 if not unresolved and not bad else 1
    if cmd == "write":
        notes = sys.argv[2]
        out = ["| row | src lines | disposition | where it is encoded / why | test or fork |", "|---|---|---|---|---|"]
        for r, res, via in table:
            src = "p7" if r.src == "part7" else "s9"
            out.append(f"| {r.label} | {src}:{r.span()} | {res[0]} | {res[1]} | {res[2]} |")
        body = "\n".join(out)
        text = open(notes, encoding="utf-8").read()
        a, b = "<!-- COVERAGE:BEGIN -->", "<!-- COVERAGE:END -->"
        i, j = text.index(a), text.index(b)
        summ = "Counts by disposition: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + f"; rows {len(table)}; unresolved {len(unresolved)}.\n\n"
        open(notes, "w", encoding="utf-8").write(text[: i + len(a)] + "\n" + summ + body + "\n" + text[j:])
        print("wrote", len(table), "rows;", counts, "unresolved", len(unresolved))
        return 0 if not unresolved else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
