#!/usr/bin/env python3
"""Build the coverage rows for the Employment Claims Act 2016 from the raw text, and check them.

usage:  python3 -I coverage.py RAW [DISPOSITIONS.tsv]
  RAW               ECA2016.txt (the deposited rendering)
  DISPOSITIONS.tsv  coverage-dispositions.tsv : row-id-prefix <TAB> disposition <TAB> reason-or-target <TAB> where

With only RAW it lists the rows (id, kind, line range, first words).
With the TSV it also resolves a disposition for EVERY row (a row inherits from the longest matching
prefix of its id) and prints the NOTES.md coverage table, the counts per disposition, and the audit:
every non-blank line of RAW is either page furniture (listed by class) or falls in exactly one row.
"""
import re, sys, collections

FURN = [
    ("page header/footer", re.compile(r"^\s*Informal Consolidation . version in force from 1/4/2025\s*$")),
    ("page header/footer", re.compile(r"^\s*\d+\s+Employment Claims Act 2016\s+2020 Ed\.\s*$")),
    ("page header/footer", re.compile(r"^\s*2020 Ed\.\s+Employment Claims Act 2016\s+\d+\s*$")),
    ("page header/footer", re.compile(r"^\s*2020 Ed\.\s+Employment Claims Act 2016\s*$")),
    ("page number", re.compile(r"^\s*(\d+|[ivx]+)\s*$")),
    ("amendment note", re.compile(r"^\s*\[[^\]]*\]\s*$")),
    ("amendment note, cut off before its closing bracket", re.compile(r"^\s*\[\d+[A-Z]?\s*$")),
]

def furniture_class(line):
    for name, p in FURN:
        if p.match(line):
            return name
    return None

def load(raw):
    return open(raw, encoding="utf-8").read().split("\n")

def next_letter(c):
    return chr(ord(c) + 1)

ROMAN = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
ROMAN_SEQ = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]

def build_rows(L):
    n = len(L)
    def sig(i):  # significant line: not blank, not furniture
        return L[i - 1].strip() and furniture_class(L[i - 1]) is None
    starts = []   # (line, id, kind)
    # fixed front matter and back matter anchors found by search
    def find(pat, lo=1, hi=None):
        hi = hi or n
        for i in range(lo, hi + 1):
            if re.search(pat, L[i - 1]):
                return i
        raise SystemExit("anchor not found: " + pat)
    body = find(r"^\s*PART 1\s*$", 100)
    sched = find(r"^\s*FIRST SCHEDULE\s*$", body)
    hist = find(r"^\s*LEGISLATIVE HISTORY\s*$", sched)
    comp = find(r"^\s*COMPARATIVE TABLE\s*$", hist)
    arr = find(r"^ARRANGEMENT OF SECTIONS", 1)
    longtitle = find(r"^An Act to facilitate", arr)
    enact = find(r"^\s*\[1 April 2017\]", longtitle)
    starts.append((1, "front", "front matter: title page"))
    starts.append((arr, "arrangement", "arrangement of sections"))
    starts.append((longtitle, "long-title", "long title"))
    starts.append((enact, "enactment", "date of enactment"))

    cur_sec = 0
    cur_sub = None
    cur_para = None
    cur_term = None
    cur_roman = 0
    cur_parent_id = None
    cur_sub_id = None
    cur_cap = 0
    expect_sec = 1
    in_sched = False
    sec_start_lines = {}
    i = body
    while i < sched:
        line = L[i - 1]
        s = line.strip()
        if not sig(i):
            i += 1
            continue
        m = re.match(r"^PART (\d+)\s*$", s)
        if m:
            starts.append((i, f"part{m.group(1)}", f"heading: Part {m.group(1)}"))
            i += 1
            continue
        m = re.match(r"^Division (\d+) .+", s)
        if m:
            starts.append((i, f"div{m.group(1)}", f"heading: Division {m.group(1)}"))
            i += 1
            continue
        # section start
        m = re.match(r"^(\d+)\.(?:—\((\d+)\))?\s*(.*)$", s)
        if m and int(m.group(1)) == expect_sec and (m.group(2) or len(m.group(3)) > 2):
            sec = int(m.group(1))
            cur_sec = sec
            expect_sec += 1
            sec_start_lines[sec] = i
            cur_sub = None
            cur_para = None
            cur_term = None
            cur_roman = 0
            cur_parent_id = None
            cur_sub_id = None
            cur_cap = 0
            if m.group(2):
                cur_sub = int(m.group(2))
                starts.append((i, f"s{sec}({cur_sub})", f"s {sec}({cur_sub})"))
            else:
                starts.append((i, f"s{sec}", f"s {sec}"))
            i += 1
            continue
        # subsection
        m = re.match(r"^\((\d+)([A-Z]?)\)\s", s)
        if m and cur_sec and (cur_sub is None or int(m.group(1)) == cur_sub + 1 or (m.group(2) and int(m.group(1)) == cur_sub)):
            # accept numbered subsection in sequence
            num = int(m.group(1))
            if cur_sec in (5, 19, 29) and False:
                pass
            if cur_sub is None or num == cur_sub + 1:
                cur_sub = num
                cur_para = None
                cur_term = None
                cur_roman = 0
                cur_parent_id = None
                cur_sub_id = None
                cur_cap = 0
                starts.append((i, f"s{cur_sec}({cur_sub})", f"s {cur_sec}({cur_sub})"))
                i += 1
                continue
        # defined term (in s 2(1), 5(5), 19(5), 29(3))
        m = re.match(r"^“([^”]+)”", s)
        if m and cur_sec in (2, 5, 19, 29):
            cur_term = m.group(1)
            cur_para = None
            cur_roman = 0
            cur_parent_id = None
            cur_sub_id = None
            cur_cap = 0
            sid = f"s{cur_sec}({cur_sub or 1})/“{cur_term}”"
            starts.append((i, sid, f"s {cur_sec}({cur_sub or 1}) “{cur_term}”"))
            i += 1
            continue
        # paragraph
        m = re.match(r"^\(([a-z])\)\s", s)
        if m:
            c = m.group(1)
            want = "a" if cur_para is None else next_letter(cur_para)
            if c == want:
                cur_para = c
                cur_roman = 0
                parent = f"s{cur_sec}({cur_sub})" if cur_sub else f"s{cur_sec}"
                if cur_term:
                    parent = f"s{cur_sec}({cur_sub or 1})/“{cur_term}”"
                cur_parent_id = f"{parent}({c})"
                cur_sub_id = cur_parent_id
                cur_cap = 0
                starts.append((i, cur_parent_id, f"{parent.replace('s' + str(cur_sec), 's ' + str(cur_sec), 1)}({c})"))
                i += 1
                continue
        # sub-paragraph (i), (ii), ... in sequence under the current paragraph
        m = re.match(r"^\(([ivx]+)\)\s", s)
        if m and cur_parent_id and cur_para is not None and m.group(1) == ROMAN_SEQ[cur_roman]:
            cur_roman += 1
            cur_sub_id = f"{cur_parent_id}({m.group(1)})"
            cur_cap = 0
            starts.append((i, cur_sub_id, f"sub-paragraph ({m.group(1)}) of {cur_parent_id}"))
            i += 1
            continue
        # capital-letter paragraph (A), (B), ... in sequence under the current sub-paragraph
        m = re.match(r"^\(([A-Z])\)\s", s)
        if m and cur_sub_id and m.group(1) == chr(ord("A") + cur_cap):
            cur_cap += 1
            starts.append((i, f"{cur_sub_id}({m.group(1)})", f"paragraph ({m.group(1)}) of {cur_sub_id}"))
            i += 1
            continue
        i += 1
    # headings: look back from each section start for a marginal heading
    sec_starts = [(ln, sid) for ln, sid, _ in starts if re.fullmatch(r"s\d+(\(1\))?", sid) and "/" not in sid]
    first_of_sec = {}
    for ln, sid in sec_starts:
        sec = int(re.match(r"s(\d+)", sid).group(1))
        first_of_sec.setdefault(sec, ln)
    for sec, ln in first_of_sec.items():
        j = ln - 1
        head = []
        while j > body and (not L[j - 1].strip() or furniture_class(L[j - 1])):
            j -= 1
        # collect consecutive heading-ish lines
        while j > body and sig(j) and not re.match(r"^\s*(PART|Division)\b", L[j - 1]) and not re.search(r"(?<!etc)[;.—]\s*$", L[j - 1]) and not re.match(r"^\s*\(", L[j - 1]) and len(head) < 3:
            head.append(j)
            j -= 1
            # allow a blank line between two heading lines only when the pair is a known wrap
        if head:
            hs = min(head)
            starts.append((hs, f"s{sec}/heading", f"heading of s {sec}"))
    # schedules
    sched_marks = [(find(r"^\s*FIRST SCHEDULE\s*$", sched), 1), (find(r"^\s*SECOND SCHEDULE\s*$", sched), 2),
                   (find(r"^\s*THIRD SCHEDULE\s*$", sched), 3), (find(r"^\s*FOURTH SCHEDULE\s*$", sched), 4)]
    sched_end = {1: sched_marks[1][0], 2: sched_marks[2][0], 3: sched_marks[3][0], 4: hist}
    for ln, k in sched_marks:
        starts.append((ln, f"sch{k}", f"Schedule {k}: heading, sections referred to, title"))
        expect = None
        i = ln + 1
        item_pat = re.compile(r"^(\d+[A-Z]?)\.\s+\S")
        last_item_num = 0
        while i < sched_end[k]:
            if sig(i):
                s = L[i - 1].strip()
                m = item_pat.match(s)
                if m:
                    num = m.group(1)
                    base = int(re.match(r"\d+", num).group(0))
                    if base >= last_item_num:
                        last_item_num = base
                        starts.append((i, f"sch{k}/item{num}", f"Schedule {k} item {num}"))
                m2 = re.match(r"^(Matters under .+|Matters under .+\n)", s)
                if m2 and k == 2:
                    starts.append((i, f"sch2/group{i}", "Schedule 2 group heading"))
            i += 1
    starts.append((hist, "history", "legislative history (not part of the Act)"))
    starts.append((comp, "comparative", "comparative table (not part of the Act)"))
    # sort, dedupe by line (keep the most specific: later in list wins on the same line)
    byline = {}
    for ln, sid, desc in starts:
        byline.setdefault(ln, []).append((sid, desc))
    rows = []
    lines_sorted = sorted(byline)
    for idx, ln in enumerate(lines_sorted):
        for sid, desc in byline[ln]:
            rows.append([ln, sid, desc])
    return rows, n

def tile(L, rows):
    # row range = from its start line to the line before the next distinct start line
    starts_sorted = sorted({r[0] for r in rows})
    out = []
    n = len(L)
    for ln, sid, desc in rows:
        nxt = [s for s in starts_sorted if s > ln]
        end = (nxt[0] - 1) if nxt else n
        # trim trailing blanks and furniture
        while end > ln and (not L[end - 1].strip() or furniture_class(L[end - 1])):
            end -= 1
        out.append((ln, end, sid, desc))
    return out

import glob, os, fnmatch

def load_refs(folder):
    """(file, tag, first, last) for every @ref in the layer-1 modules; tag is the section tag of the function the @ref sits above."""
    refs = []
    for f in sorted(glob.glob(os.path.join(folder, "eca-*.l4"))):
        base = os.path.basename(f)
        if re.match(r"eca-(tests|cases|seat)", base) or base == "eca-nouns.l4":
            continue
        lines = open(f, encoding="utf-8").read().split("\n")
        for k, l in enumerate(lines):
            m = re.match(r"^@ref (.*) \(src:(\d+)(?:-(\d+))?\)\s*$", l)
            if not m:
                continue
            name = None
            for l2 in lines[k + 1:k + 40]:
                m2 = re.match(r"^`([^`]+)` MEANS", l2)
                if m2:
                    name = m2.group(1)
                    break
            if name is None:
                continue
            tag = name if len(name) <= 56 else name[:53] + "..."
            refs.append((base[4:-3], tag, int(m.group(2)), int(m.group(3) or m.group(2)), name))
    return refs

def load_tsv(path):
    ent = []
    for l in open(path, encoding="utf-8").read().split("\n"):
        if not l.strip() or l.startswith("#"):
            continue
        parts = l.split("\t")
        while len(parts) < 4:
            parts.append("")
        ent.append(parts[:4])
    return ent

def match_tsv(ent, rid):
    best = None
    for pat, disp, why, where in ent:
        if pat.endswith("$"):
            if pat[:-1] == rid:
                score = (4, len(pat))
            else:
                continue
        elif pat == rid:
            score = (3, len(pat))
        elif ("*" in pat or "?" in pat) and fnmatch.fnmatchcase(rid, pat):
            score = (1, len(pat))
        elif rid.startswith(pat + "(") or rid.startswith(pat + "/"):
            score = (2, len(pat))
        else:
            continue
        if best is None or score > best[0]:
            best = (score, disp, why, where, pat)
    return best

def main():
    raw = sys.argv[1]
    tsv = sys.argv[2] if len(sys.argv) > 2 else None
    L = load(raw)
    rows, n = build_rows(L)
    rows_t = tile(L, rows)
    if not tsv:
        for ln, end, sid, desc in rows_t:
            first = L[ln - 1].strip()[:60]
            print(f"{ln:5d}-{end:<5d} {sid:34s} {first}")
        return
    here = os.path.dirname(os.path.abspath(__file__))
    refs = load_refs(here)
    ent = load_tsv(tsv)
    out = []
    problems = []
    for ln, end, sid, desc in rows_t:
        over = [r for r in refs if r[2] <= end and r[3] >= ln]
        m = match_tsv(ent, sid)
        if m and m[1] == "fork":
            disp, why, where = "fork", m[2], m[3]
        elif m and m[1] == "inert" and m[2].startswith("1") and "heading" in m[2]:
            # a heading marked inert reason 1 stays inert even when an enclosing @ref range happens to span its line
            disp, why, where = "inert", m[2], m[3]
        elif over:
            if m and m[1] != "encoded":
                problems.append(f"CONFLICT {sid}: the TSV says {m[1]} but the encoding cites lines {ln}-{end}")
            disp, why = "encoded", ""
            where = ""
        elif m:
            disp, why, where = m[1], m[2], m[3]
        else:
            problems.append(f"UNRESOLVED {sid} lines {ln}-{end}")
            disp, why, where = "UNRESOLVED", "", ""
        if disp == "encoded" and not where:
            tags = []
            for r in over:
                t = f"{r[0]}: {r[1]}"
                if t not in tags:
                    tags.append(t)
            where = "; ".join(tags[:2]) + (f"; +{len(tags) - 2} more" if len(tags) > 2 else "")
        if disp == "fork" and over and not where:
            tags = []
            for r in over:
                t = f"{r[0]}: {r[1]}"
                if t not in tags:
                    tags.append(t)
            where = "; ".join(tags[:2]) + (f"; +{len(tags) - 2} more" if len(tags) > 2 else "")
        out.append((ln, end, sid, desc, disp, why, where))
    # audit: every non-blank line is furniture or in exactly one row
    cover = collections.Counter()
    for ln, end, *_ in out:
        for k in range(ln, end + 1):
            cover[k] += 1
    furn = collections.Counter()
    uncovered = []
    multi = []
    sigcount = 0
    for k in range(1, len(L) + 1):
        t = L[k - 1]
        if not t.strip():
            continue
        fc = furniture_class(t)
        if fc:
            furn[fc] += 1
            continue
        sigcount += 1
        if cover[k] == 0:
            uncovered.append(k)
        elif cover[k] > 1:
            multi.append(k)
    # every significant line of an encoded or fork row lies inside some @ref range
    covered = set()
    for r in refs:
        covered.update(range(r[2], r[3] + 1))
    outside = []
    for ln, end, sid, desc, disp, why, where in out:
        if disp in ("encoded", "fork"):
            for k in range(ln, end + 1):
                if L[k - 1].strip() and furniture_class(L[k - 1]) is None and k not in covered:
                    outside.append((sid, k))
    # rows by kind, counted from the rows themselves, to set beside the independent marker count
    kinds = collections.Counter()
    for ln, end, sid, desc, *_ in out:
        first = re.sub(r"\s+", " ", L[ln - 1].strip())
        if re.match(r"^\d+\.(—\(\d+\))? ", first) and re.fullmatch(r"s\d+(\(\d+\))?", sid):
            kinds["section"] += 1
        elif re.fullmatch(r"s\d+\(\d+[A-Z]?\)", sid) and re.match(r"^\(\d+[A-Z]?\) ", first):
            kinds["numbered subsection (not a section's first)"] += 1
        elif re.search(r"/“[^”]+”$", sid):
            kinds["defined term"] += 1
        elif re.match(r"sch\d/item", sid):
            kinds["schedule item"] += 1
        elif re.search(r"\([a-zA-Z]+\)$", sid):
            kinds["lettered, roman or capital-letter paragraph"] += 1
        elif sid.endswith("/heading"):
            kinds["section heading"] += 1
    cnt = collections.Counter()
    reasons = collections.Counter()
    for r in out:
        cnt[r[4]] += 1
        if r[4] == "inert":
            reasons[r[5].split()[0] if r[5] else "?"] += 1
    mode = sys.argv[3] if len(sys.argv) > 3 else "table"
    if mode == "table":
        print("| Row | Lines | Begins | Disposition | Reason, fork or where it is encoded |")
        print("| --- | --- | --- | --- | --- |")
        for ln, end, sid, desc, disp, why, where in out:
            label = sid.replace("|", "\\|")
            begins = re.sub(r"\s+", " ", L[ln - 1].strip())[:44].replace("|", "\\|")
            if disp == "inert":
                cell = f"reason {why}" + (f": {where}" if where else "")
            elif disp == "fork":
                cell = f"{why}" + (f"; encoded: {where}" if where else "")
            elif disp == "encoded":
                cell = where
            else:
                cell = (why + " " + where).strip()
            print(f"| {label} | {ln}-{end} | {begins} | {disp} | {cell} |")
    print("", file=sys.stderr)
    print(f"rows: {len(out)}", file=sys.stderr)
    for k in ("encoded", "fork", "inert", "repealed-or-blank", "UNRESOLVED"):
        if cnt[k]:
            print(f"  {k}: {cnt[k]}" + (f"  (by reason: {dict(sorted(reasons.items()))})" if k == "inert" else ""), file=sys.stderr)
    print(f"audit: {len(L)} lines in the file; {sum(furn.values())} page-furniture lines {dict(furn)}; {sigcount} other non-blank lines; "
          f"{len(uncovered)} in no row {uncovered[:12]}; {len(multi)} in more than one row {multi[:12]}", file=sys.stderr)
    print("rows by kind (from the rows themselves): " + "; ".join(f"{k} {v}" for k, v in sorted(kinds.items())), file=sys.stderr)
    print(f"cited: {len(outside)} significant lines of encoded or fork rows lie outside every @ref range {outside[:6]}", file=sys.stderr)
    for pmsg in problems:
        print("PROBLEM", pmsg, file=sys.stderr)
    if problems or uncovered or multi or outside:
        sys.exit(1)

def units(raw):
    """An independent count of text units by marker, made without the row builder, to compare with the rows."""
    L = load(raw)
    n = len(L)
    def idx(pat, lo=1):
        for i in range(lo, n + 1):
            if re.search(pat, L[i - 1]):
                return i
    body = idx(r"^\s*PART 1\s*$", 100)
    sched = idx(r"^\s*FIRST SCHEDULE\s*$", body)
    hist = idx(r"^\s*LEGISLATIVE HISTORY\s*$", sched)
    secs = subs = paras = terms = parts = divs = romans = caps = 0
    for i in range(body, sched):
        t = L[i - 1].strip()
        if re.match(r"^\d+\.(—\(\d+\))?\s", t) and not re.match(r"^\d+\.\s*$", t):
            secs += 1
        elif re.match(r"^\(\d+[A-Z]?\)\s", t):
            subs += 1
        elif re.match(r"^\([A-Z]\)\s", t):
            caps += 1
        elif re.match(r"^\((ii|iii|iv|vi|vii|viii|ix)\)\s", t):
            romans += 1
        elif re.match(r"^\([a-z]\)\s", t):
            paras += 1
        elif re.match(r"^“[^”]+”", t):
            terms += 1
        elif re.match(r"^PART \d+\s*$", t):
            parts += 1
        elif re.match(r"^Division \d+ ", t):
            divs += 1
    items = {k: 0 for k in (1, 2, 3, 4)}
    marks = [idx(r"^\s*FIRST SCHEDULE\s*$", sched), idx(r"^\s*SECOND SCHEDULE\s*$", sched), idx(r"^\s*THIRD SCHEDULE\s*$", sched), idx(r"^\s*FOURTH SCHEDULE\s*$", sched), hist]
    for k in range(4):
        for i in range(marks[k], marks[k + 1]):
            if re.match(r"^\s*\d+[A-Z]?\.\s+\S", L[i - 1]):
                items[k + 1] += 1
    print(f"independent count by marker: sections {secs}; numbered subsections {subs}; lettered paragraphs {paras} (this count includes each line that begins (i), which is a letter or the first roman numeral); roman sub-paragraphs (ii) and later {romans}; capital-letter paragraphs {caps}; defined terms {terms}; Parts {parts}; Divisions {divs}; schedule items {items} (total {sum(items.values())})")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "units":
        units(sys.argv[1])
    else:
        main()
