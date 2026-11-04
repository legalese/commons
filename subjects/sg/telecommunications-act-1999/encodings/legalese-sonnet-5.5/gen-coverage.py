#!/usr/bin/env python3
"""Build the coverage table for the Telecommunications Act 1999 deposit and for every instrument deposited under it, by script, from the texts.

Run:  python3 -I gen-coverage.py     (writes COVERAGE.md; exit 0 when no row is `pending`, 1 on a failed check, 2 while any row is `pending`)

Inputs, never edited: subjects/sg/telecommunications-act-1999/registers/source-bundle/TA1999.txt and the instrument texts under
subjects/sg/telecommunications-*/registers/source-bundle/.

Dispositions.  Each row gets exactly one, found by the script and not by the encoder's say-so:
  encoded   every content line of the row lies inside the locator (src:A-B or src:ID:A-B) of an @ref in a rule module; srcrefs.py --strict
            has checked that each locator is a verbatim quotation of exactly those lines (./srcrefs-all.sh).
  inert     the row is listed in INERT with one of the three reasons the brief allows: 1 not operative; 2 machinery per the Guide
            (boards, offices, the Act's own commencement, short title, regulation-making powers, savings that affect no one now,
            amendments of other Acts); 3 shown repealed or blank.
  fork      the row is listed in FORK, pointing at the fork-register entry; the same lines are also quoted by the rule that encodes the chosen reading.
  pending   none of the above.  This is the working state and is never an allowed final state: the script exits 2 while any remain.
There is no `deferred` and no `out-of-scope`.  A row that `source not obtained` applies to is an instrument whose text is not deposited
(see SOURCE_NOT_OBTAINED); it never applies to a provision of the Act.
"""
import re, sys, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
SUBJ = os.path.normpath(os.path.join(HERE, "../../.."))
SRC = os.path.join(SUBJ, "telecommunications-act-1999/registers/source-bundle/TA1999.txt")
lines = open(SRC, encoding="utf-8").read().split("\n")
T1, T2, M = "1", "2", "M"

REASON = {"1": "not operative", "2": "machinery", "3": "repealed or blank"}
# ---- INERT: row id (prefix match) -> (reason code, what the row is) -----------------------------------------
INERT = {
 "cover and Revised Edition notice": ("1", "Cover page and edition notice of the Law Revision Commission: not part of the Act."),
 "arrangement of sections": ("1", "Table of contents: not part of the Act (it lists the 98 sections, each with its own row)."),
 "long title and date of commencement": ("1", "The long title (a purpose clause that creates no rule) and the date the Act began, 1 December 1999 (the Act's own commencement is machinery, reason 2)."),
 "legislative history": ("1", "Legislative history and comparative table: a service of the Law Revision Commission, which says it is not part of the Act; read for the dates of amendments and for the 2000 Revised Edition numbering."),
 "Part ": ("1", "Part heading: structural, no operative text."),
 "s 1": ("2", "Short title: names the Act and enacts nothing."),
}
# ---- FORK: row id (prefix) -> pointer ----------------------------------------------------------------------
FORK = {
 's 2 "equipment"': "FORK 1 (whether `radio-communication equipment` is the two s 2 definitions put together) and FORK 6 (whether the words before 1 Feb 2012 cover a broadcast receiver); pointers in TV-QUESTION.md section 4; the lines are quoted by the rule for the reading taken",
 's 2 "radio-communication"': "FORK 1: whether `radio-communication equipment` is the two s 2 definitions put together; pointer in TV-QUESTION.md section 4; the lines are quoted by the rule for the reading taken",
 's 53(1)': "FORK 2: whether the closing words carry the extra verbs of s 3(2)(a) into the offence; pointer in TV-QUESTION.md section 4; the lines are quoted by the rule for the reading taken",
 's 95': "FORK 3: the reach of s 95 for broadcasting apparatus (two readings, both encoded); pointer in TV-QUESTION.md section 4",
}
FORK_I = {
 "Rg 6 as amended by S 478/2005: reg 8": "FORK 4: what reg 22(1)'s approval is (two readings); pointer in TV-QUESTION.md section 4",
 "N 1 (Revised Edition): The Schedule item 11": "FORK 5: what item 11(e) names (two readings); pointer in TV-QUESTION.md section 4",
}
# ---- INERT_I: instrument provision rows that are inert (id = the row id as printed in COVERAGE.md) ----
INERT_I = {
 "Rg 5 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the regulations"),
 "N 1 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the Notification"),
 "Comp Regs as made (S 516/2001): front matter (title, arrangement, enacting words)": ("2", "machinery: the title, the arrangement of regulations and the enacting words naming the regulation-making power (s 64) and the Minister's approval; the enacting words are quoted beside reg 1 in sgta-i-comp.l4"),
 "Comp Regs as amended by S 706/2005: front matter (title, arrangement, enacting words)": ("2", "machinery: the title, the arrangement of regulations and the enacting words naming the regulation-making power (s 64) and the Minister's approval; the enacting words are quoted beside reg 1 in sgta-i-comp.l4"),
 "Rg 1 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the regulations"),
 "Rg 3 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the regulations"),
 "Rg 4 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the regulations"),
 "Rg 6 (Revised Edition): reg 1": ("2", "machinery: citation (short title) of the regulations"),
 "O 3 as made (S 549/1998): front matter (title, arrangement, enacting words)": ("1", "title, \"First published\" line, number and arrangement of paragraphs: not operative; the enacting words naming s 130 of the TAS Act and the Minister are quoted by the module"),
 "O 3 (Revised Edition): front matter (title, arrangement, enacting words)": ("1", "running head, title and arrangement of paragraphs of the 1999 Revised Edition: not operative; the paragraphs are quoted by the module"),
 "Wiring Work Regs 2024 as made (S 559/2024): front matter (title, arrangement, enacting words)": ("1", "title, \"First published\" line, number and arrangement of regulations: not operative; the enacting words naming s 97 of the Act and the Authority's and the Minister's parts are quoted by the module"),
 "N 1 as amended by S 588/2023: front matter (title, arrangement, enacting words)": ("1", "title, \"First published\" line, number and the name of the Notification: not operative; the enacting words naming s 96 and the Minister, and the commencement paragraph, are quoted by the module"),
 "In-vehicle unit exemption as made (S 381/2024): front matter (title, arrangement, enacting words)": ("1", "title, \"First published\" line, number, arrangement of paragraphs and the name of the Notification: not operative; the enacting words naming s 96 and the Minister are quoted by the module"),
}
# instruments whose text could not be obtained: (label, made under, where looked, what each place answered)
SOURCE_NOT_OBTAINED = []

# ---- parse --------------------------------------------------------------------------------------
def is_furniture(s):
    t = s.strip()
    return (not t) or t.startswith("Informal Consolidation") or re.match(r"^\d+\s+Telecommunications Act 1999\s+2020 Ed\.?$", t) \
        or re.match(r"^2020 Ed\.\s+Telecommunications Act 1999\s+\d+$", t) or re.match(r"^\d+$", t)

# locate the structural landmarks
n_body = next(i for i, s in enumerate(lines) if s.strip() == "Short title")
n_arr = next(i for i, s in enumerate(lines) if s.strip() == "ARRANGEMENT OF SECTIONS")
n_hist = next(i for i, s in enumerate(lines) if s.strip() == "LEGISLATIVE HISTORY")
n_long = next(i for i, s in enumerate(lines) if s.startswith("An Act to provide for the operation"))
body_end = n_hist  # exclusive

sec_re = re.compile(r"^\s*(\d{1,2})\.(?:—\((\d+[A-Z]?)\))?\s+\S")
secs = []  # (number, start line index)
expect = 1
for i in range(n_body, body_end):
    m = sec_re.match(lines[i])
    if m and int(m.group(1)) == expect:
        secs.append((expect, i)); expect += 1
found = [n for n, _ in secs]
ok_sections = found == list(range(1, 99))

# arrangement of sections: numbers listed
arr_numbers = set()
for s in lines[n_arr:n_long]:
    for m in re.finditer(r"(?:^|\s)(\d{1,2})\.(?:\s|$)", s):
        arr_numbers.add(int(m.group(1)))
missing_in_arr = sorted(set(found) - arr_numbers)

# part headings
parts = []  # (label, line index)
for i in range(n_body, body_end):
    m = re.match(r"^\s*PART\s+(\d+[A-Z]?)\s*$", lines[i])
    if m: parts.append((m.group(1), i))

def part_of(idx):
    p = None
    for lab, i in parts:
        if i <= idx: p = lab
    return p

def heading_before(start):
    """the heading lines directly above the section's first line"""
    out = []; i = start - 1
    while i >= 0 and not lines[i].strip(): i -= 1
    while i >= 0 and lines[i].strip() and not is_furniture(lines[i]) and not re.match(r"^\s*\[", lines[i]) and not re.match(r"^\s*PART", lines[i]):
        out.insert(0, lines[i].strip()); i -= 1
        if len(out) >= 3: break
    h = " ".join(out)
    return h

rows = []  # dict rows
def add(kind, ident, start, end, tier, disp, module, reason, extra=""):
    rows.append(dict(kind=kind, id=ident, start=start + 1, end=end + 1, tier=tier, disp=disp, module=module, reason=reason, extra=extra))

# front matter and arrangement
add("front", "cover and Revised Edition notice", 0, n_arr - 1, "-", "pending", "", "")
add("front", "arrangement of sections", n_arr, n_long - 1, "-", "pending", "", "")
add("long title", "long title and date of commencement", n_long, n_body - 1, "-", "pending", "", "")

mark_re = re.compile(r"^\s*\[(\d+[A-Z]{0,2})\s*$")
old_nos = {}
for k, (n, st) in enumerate(secs):
    en = (secs[k + 1][1] - 1) if k + 1 < len(secs) else body_end - 1
    # trim the heading belonging to the next section and any Part heading from this section's range
    hs = heading_before(secs[k + 1][1]) if k + 1 < len(secs) else ""
    if k + 1 < len(secs):
        j = secs[k + 1][1] - 1
        while j > st and (not lines[j].strip() or (lines[j].strip() and not is_furniture(lines[j]) and (hs and lines[j].strip() in hs)) or re.match(r"^\s*PART\s", lines[j]) or re.match(r"^\s*\[[^\]\n]*\]?\s*$", lines[j]) or re.match(r"^\s*[A-Z][A-Z ,.'\-]+$", lines[j].strip())):
            j -= 1
        # keep the range simple: section k ends where next heading begins; headings/Parts are their own rows below
        en = j
    # old number marker inside range
    om = None
    for j in range(st, en + 1):
        mm = mark_re.match(lines[j])
        if mm: om = mm.group(1); break
    old_nos[n] = om
    head = heading_before(st)
    add("section", f"s {n}", st, en, "-", "pending", "", "", extra=f"{head} | 2000 Ed. s {om or '?'} | Part {part_of(st)}")

# part rows
for lab, i in parts:
    add("part", f"Part {lab}", i, i, "-", "pending", "", "")

# sub-rows: subsections / paragraphs / definitions, within each section range
sub_re = re.compile(r"^\s{0,24}\((\d+[A-Z]{0,2})\)\s")
par_re = re.compile(r"^\s{0,60}\(([a-z]{1,2})\)\s")
rom_re = re.compile(r"^(i|ii|iii|iv|v|vi|vii|viii|ix|x)$")
cap_re = re.compile(r"^\s{0,80}\(([A-Z])\)\s")
sub_rows = []
for k, (n, st) in enumerate(secs):
    srow = next(r for r in rows if r["kind"] == "section" and r["id"] == f"s {n}")
    st0, en0 = srow["start"] - 1, srow["end"] - 1
    tier, disp = srow["tier"], srow["disp"]
    cur_sub = None; last_letter = None; last_rom = None
    # the first line of the section may itself open subsection (1)
    m0 = sec_re.match(lines[st0])
    if m0 and m0.group(2): cur_sub = m0.group(2); sub_rows.append((st0, f"s {n}({cur_sub})", "subsection", n))
    for j in range(st0 + 1, en0 + 1):
        s = lines[j]
        if is_furniture(s): continue
        if n == 2 and s.lstrip().startswith("“"):
            term = re.match(r"^\s*“([^”]+)”", s).group(1)
            sub_rows.append((j, f"s 2 \"{term}\"", "definition", n)); cur_sub = None; continue
        m = sub_re.match(s)
        if m and n != 2:
            cur_sub = m.group(1); last_letter = None; last_rom = None
            sub_rows.append((j, f"s {n}({cur_sub})", "subsection", n)); continue
        m = par_re.match(s)
        if m and n != 2:
            tok = m.group(1)
            nxt = chr(ord(last_letter) + 1) if last_letter and len(last_letter) == 1 else None
            if rom_re.match(tok) and tok != nxt and last_letter is not None:
                last_rom = tok
                sub_rows.append((j, f"s {n}({cur_sub or '-'})({last_letter})({tok})", "sub-paragraph", n))
            else:
                last_letter = tok; last_rom = None
                sub_rows.append((j, f"s {n}({cur_sub or '-'})({tok})", "paragraph", n))
            continue
        m = cap_re.match(s)
        if m and n != 2:
            sub_rows.append((j, f"s {n}({cur_sub or '-'})({last_letter or '-'})({last_rom or '-'})({m.group(1)})", "sub-sub-paragraph", n))
# convert sub rows to ranges up to next sub row or section end
by_sec_end = {r["id"]: r["end"] - 1 for r in rows if r["kind"] == "section"}
for idx, (st, ident, kind, n) in enumerate(sub_rows):
    nxt_start = sub_rows[idx + 1][0] if idx + 1 < len(sub_rows) and sub_rows[idx + 1][3] == n else by_sec_end[f"s {n}"] + 1
    en = nxt_start - 1
    while en > st and not lines[en].strip(): en -= 1
    add(kind, ident, st, en, "-", "pending", "", "")

# back matter
add("back", "legislative history", n_hist, len(lines) - 1, "-", "pending", "", "")

rows.sort(key=lambda r: (r["start"], 0 if r["kind"] in ("front","long title","part") else 1 if r["kind"]=="section" else 2))

# ---- locators in the rule modules ---------------------------------------------------------------------------
ACT_SKIP = re.compile(r"^sgta-(tests|tv-|i-|nouns|ta-vintage)")
act_mods = sorted(f for f in glob.glob(os.path.join(HERE, "sgta-*.l4")) if not ACT_SKIP.match(os.path.basename(f)))
inst_mods = sorted(glob.glob(os.path.join(HERE, "sgta-i-*.l4")))
loc_plain = re.compile(r"src:(\d+)(?:-(\d+))?(?![\d:A-Za-z])")
loc_id = re.compile(r"src:([A-Za-z][A-Za-z0-9.-]*):(\d+)(?:-(\d+))?")
act_cov = {}      # line -> set(module)
inst_cov = {}     # (stem, line) -> set(module)
for f in act_mods:
    for ln in open(f, encoding="utf-8").read().split("\n"):
        if "@ref" not in ln: continue
        for m in loc_plain.finditer(ln):
            a = int(m.group(1)); b = int(m.group(2) or a)
            for x in range(a, b + 1): act_cov.setdefault(x, set()).add(os.path.basename(f))
for f in inst_mods + act_mods:
    for ln in open(f, encoding="utf-8").read().split("\n"):
        if "@ref" not in ln: continue
        for m in loc_id.finditer(ln):
            a = int(m.group(2)); b = int(m.group(3) or a)
            for x in range(a, b + 1): inst_cov.setdefault((m.group(1), x), set()).add(os.path.basename(f))

def inert_of(rid):
    best = None
    for k, v in INERT.items():
        if rid == k or (k.endswith(" ") and rid.startswith(k)) or (not k.endswith(" ") and (rid.startswith(k + "(") or rid.startswith(k + " "))):
            if best is None or len(k) > len(best[0]): best = (k, v)
    return best[1] if best else None
def fork_of(rid):
    best = None
    for k, v in FORK.items():
        if k and (rid == k or rid.startswith(k + "(") or rid.startswith(k + " ") or rid.startswith(k + '"')):
            if best is None or len(k) > len(best[0]): best = (k, v)
    return best[1] if best else None

mark_line = re.compile(r"^\s*\[[^\]\n]*\]?\s*$")
rep_word = re.compile(r"Deleted|Repealed|Omitted|Spent", re.I)
def is_mark(s): return bool(mark_line.match(s)) and not rep_word.search(s)
def content(r):
    return [i for i in range(r["start"], r["end"] + 1) if lines[i - 1].strip() and re.search(r"[A-Za-z0-9]", lines[i - 1]) and not is_furniture(lines[i - 1]) and not is_mark(lines[i - 1])]
def repealed(r):
    cl = content(r)
    return bool(cl) and bool(re.search(r"\[(Deleted|Repealed|Omitted)", lines[cl[0] - 1], re.I)) and all(rep_word.search(lines[i - 1]) or is_mark(lines[i - 1]) for i in cl)

for r in rows:
    r["modules"] = ""
    fk = fork_of(r["id"]); iv = inert_of(r["id"])
    cl = content(r)
    mods = set()
    cov = all(i in act_cov for i in cl) if cl else False
    for i in cl: mods |= act_cov.get(i, set())
    anycov = any(i in act_cov for i in cl)
    if iv and not anycov:
        r["disp"], r["tier"], r["reason"] = "inert", iv[0], iv[1]
    elif repealed(r) and not anycov:
        r["disp"], r["tier"], r["reason"] = "inert", "3", "shown repealed or blank: " + lines[cl[0] - 1].strip()[:90]
    elif fk and cov:
        r["disp"], r["reason"], r["modules"] = "fork", fk, ", ".join(sorted(mods))
    elif cov:
        r["disp"], r["reason"], r["modules"] = "encoded", "", ", ".join(sorted(mods))
    else:
        r["disp"], r["reason"] = "pending", ("%d of %d content lines quoted by an @ref" % (sum(1 for i in cl if i in act_cov), len(cl)))
        if iv: r["disp"], r["tier"], r["reason"] = "inert", iv[0], iv[1]
# a section row follows its sub-rows
for r in rows:
    if r["kind"] != "section": continue
    iv = inert_of(r["id"])
    if iv: r["disp"], r["tier"], r["reason"], r["modules"] = "inert", iv[0], iv[1], ""; continue
    subs = [x for x in rows if x["kind"] in ("subsection", "paragraph", "sub-paragraph", "sub-sub-paragraph", "definition") and r["start"] <= x["start"] and x["end"] <= r["end"]]
    cl = content(r)
    uncovered_main = [i for i in cl if i not in act_cov]
    if r["disp"] == "pending" and subs and all(x["disp"] != "pending" for x in subs) and not uncovered_main:
        r["disp"] = "encoded"
    if r["disp"] == "pending":
        npend = sum(1 for x in subs if x["disp"] == "pending")
        r["reason"] = "%d of its %d sub-rows pending; %d of %d content lines quoted" % (npend, len(subs), len(cl) - len(uncovered_main), len(cl))
    else:
        ms = set()
        for i in cl: ms |= act_cov.get(i, set())
        r["modules"] = ", ".join(sorted(ms))
        fks = [x for x in subs if x["disp"] == "fork"]
        if fks: r["reason"] = "contains fork rows: " + ", ".join(sorted({x["reason"].split(":")[0] for x in fks}))
        ins = [x for x in subs if x["disp"] == "inert"]
        if ins: r["reason"] = (r["reason"] + "; " if r["reason"] else "") + "%d sub-rows inert (%s)" % (len(ins), ", ".join(sorted({x['tier'] for x in ins})))

# ---- instrument rows ------------------------------------------------------------------------------------------
LABEL = {"CANC": "Cancellation Notification 2011", "RG1": "Rg 1", "RG3": "Rg 3", "RG4": "Rg 4", "RG5": "Rg 5", "RG6": "Rg 6", "N1": "N 1", "COMP": "Comp Regs", "IW": "Internal Wiring Regs", "RESELL": "Resellers Notification", "TRUSTS": "Prescribed Trusts Regs", "O3": "O 3", "DEAL99": "Rg 7 (1999 Ed.)", "RADIO99": "Rg 3 (1999 Ed.)", "ERP": "In-vehicle unit exemption", "WW": "Wiring Work Regs 2024"}
furn_i = re.compile(r"^\s*(\[CAP\.? ?323.*|\[G\.N\. No.*|(?:S\s*\d+/\d{4}[;,\s]*)+\]|\[[A-Z]{2,}/[A-Z0-9/.-]+.*|\d{1,3}|S\s*\d+/\d{4}|\d+\s+S\s*\d+/\d{4}|S\s*\d+/\d{4}\s+\d+|First published in the Government Gazette.*|No\. S\s*\d+|THE SINGAPORE.*|\d+\.\d+\.\d{4}|Telecommunication \(Dealers\)|CAP\. 323, (?:Rg|O) \d+\]\s+(?:Radio-communication )?Regulations\s+\[\d{4} Ed\. p\. \d+|p\. \d+\s+\d{4} Ed\.\]\s+(?:Radio-communication )?Regulations\s+\[CAP\. 323, Rg \d+|\d+\s+S\s*\d+/\d{4}|S\s*\d+/\d{4}\s+\d+)\s*$")
def heading_set(ls):
    """indices of heading lines: an all-capitals line, or a run of 1 to 3 short lines between blank lines whose last line has no closing punctuation"""
    hs = set(); n = len(ls); i = 0
    while i < n:
        if not ls[i].strip(): i += 1; continue
        j = i
        while j < n and ls[j].strip(): j += 1
        run = list(range(i, j))
        txt = [ls[k].strip() for k in run]
        allcaps = all(re.sub(r"[^A-Za-z]", "", t) and re.sub(r"[^A-Za-z]", "", t).isupper() for t in txt)
        if allcaps and all(len(t) < 100 for t in txt) and not re.match(r"^\(?[A-Z0-9]{1,3}\)?\.?$", txt[0]): hs.update(run)
        elif len(run) <= 3 and all(len(t) < 100 for t in txt) and txt[0][0].isupper() and (not re.search(r"[.;:,—\-)]$", txt[-1]) or txt[-1].endswith("etc.")) and all(not re.match(r"^[\(\d\[]", t) for t in txt): hs.update(run)
        i = j
    for i in range(n):
        t = ls[i].strip(); lt = re.sub(r"[^A-Za-z]", "", t)
        if len(lt) >= 4 and lt.isupper() and len(t) < 100 and not furn_i.match(ls[i]): hs.add(i)
    # a heading sits directly above a numbered provision with no blank line between
    for i in range(n):
        if row_start_i.match(ls[i]) and not furn_i.match(ls[i]):
            k = i - 1; c = 0
            while k >= 0 and ls[k].strip() and c < 3:
                t = ls[k].strip()
                ok_t = len(t) < 100 and (not re.search(r"[.;:,—\-)]$", t) or t.endswith("etc.")) and not re.match(r"^[\(\d\[]", t)
                if ok_t and (t[0].isupper() or (k > 0 and ls[k - 1].strip() and ls[k - 1].strip()[0].isupper() and len(ls[k - 1].strip()) < 100)): hs.add(k); k -= 1; c += 1
                else: break
    return hs
row_start_i = re.compile(r"^\s{0,14}(\d{1,3}[A-Z]{0,2})\.\s*(?:[—–-]\s*)?(?:\(\d+[A-Z]?\))?\s*\S")
sched_i = re.compile(r"^\s*(?:THE\s+)?(FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH|EIGHTH|NINTH|TENTH)?\s*SCHEDULE\b")
HEAD_CACHE = {}
inst_rows = []   # dict: file, stem, label, id, kind, start, end, disp, reason, modules
inst_files = []
for d in sorted(glob.glob(os.path.join(SUBJ, "telecommunications-*"))):
    if os.path.basename(d) == "telecommunications-act-1999": continue
    for p in sorted(glob.glob(os.path.join(d, "registers/source-bundle/*.txt"))):
        if "-GAZ" in os.path.basename(p) or "-OCR" in os.path.basename(p) or "-AID-" in os.path.basename(p): continue   # the e-Gazette copies (-GAZ) deposited for comparison with the IMDA copies, and the OCR text (-OCR) the Gazette's copy replaced, are not rows
        inst_files.append((d, p))
for d, p in inst_files:
    stem = os.path.basename(p)[:-4]
    ls = open(p, encoding="utf-8").read().split("\n")
    m = re.match(r"TA1999-([A-Z0-9]+)(?:-(S\d+)-(\d{4}))?$", stem)
    base = LABEL.get(m.group(1), m.group(1))
    label = base + (" as amended by " + m.group(2).replace("S", "S ") + "/" + m.group(3) if m.group(2) else (" (Revised Edition)" if m.group(1) in ("RG1","RG3","RG4","RG5","RG6","N1","O3") else ""))
    # the three texts as MADE (before any Revised Edition) are labelled so, not "as amended by"
    for _mk in ("S 114/2001", "S 115/2001", "S 516/2001", "S 549/1998", "S 381/2024", "S 559/2024", "S 185/2003", "S 22/2011"):
        label = label.replace(" as amended by " + _mk, " as made (" + _mk + ")")
    if m.group(2) and m.group(1) in ("RG1","RG3","RG4","RG5","RG6","N1","COMP") : pass
    # body start: the line holding "may be cited", backed up over a heading
    arr = next((i for i, s in enumerate(ls) if "ARRANGEMENT OF" in s.upper()), 0)
    bs = next((i for i in range(arr, len(ls)) if "may be cited" in ls[i] or "MAY BE CITED" in ls[i].upper()), None)
    if bs is None: bs = next((i for i in range(arr, len(ls)) if re.match(r"^\s*Citation( and commencement)?\s*$", ls[i])), arr)
    k = bs
    while k > arr and ls[k - 1].strip() and not re.match(r"^\s*\d", ls[k - 1]): k -= 1
    bs = k
    starts = []; group = ""; last = 0
    for i in range(bs, len(ls)):
        s = ls[i]
        sm = sched_i.match(s)
        if sm and len(s.strip()) < 60:
            group = s.strip(); last = 0; starts.append((i, "heading:" + group)); continue
        pm = re.match(r"^\s*PART\s+([IVX]+)\s*$", s)
        if pm and group:
            base_g = re.sub(r" Part [IVX]+$", "", group); group = base_g + " Part " + pm.group(1); last = 0; starts.append((i, "heading:" + group)); continue
        mm = row_start_i.match(s)
        if mm and not furn_i.match(s):
            n = mm.group(1); ni = int(re.match(r"\d+", n).group(0))
            if ni == last + 1 or (ni > last and ni <= last + 4) or (last == 0 and ni <= 4):
                last = ni; starts.append((i, (("reg " if not group else " ".join(w.capitalize() if (w.isupper() and not re.match(r"^[IVX]+$", w)) else w for w in group.split()) + " item ") + n)))
    # rows
    made = next((i for i in range(bs, len(ls)) if re.match(r"^\s*Made (this|on)\b", ls[i])), None)
    first_start = starts[0][0] if starts else len(ls)
    inst_rows.append(dict(stem=stem, label=label, id=label + ": front matter (title, arrangement, enacting words)", kind="front", start=1, end=max(first_start, 1), path=p))
    for j, (i, rid) in enumerate(starts):
        if rid.startswith("heading:"): continue
        e = (made - 1) if made is not None else len(ls) - 1
        for (i2, rid2) in starts[j + 1:]:
            e = i2 - 1; break
        inst_rows.append(dict(stem=stem, label=label, id=label + ": " + rid, kind="provision", start=i + 1, end=e + 1, path=p))
    if made is not None:
        inst_rows.append(dict(stem=stem, label=label, id=label + ": date of making, signature and file reference", kind="back", start=made + 1, end=len(ls), path=p))
for r in inst_rows:
    ls = open(r["path"], encoding="utf-8").read().split("\n")
    hs = HEAD_CACHE.setdefault(r["path"], heading_set(ls))
    cl = [i for i in range(r["start"], r["end"] + 1) if i <= len(ls) and ls[i - 1].strip() and re.search(r"[A-Za-z0-9]", ls[i - 1]) and not furn_i.match(ls[i - 1]) and ((i - 1) not in hs or (r["kind"] == "provision" and i == r["start"]))]
    r["ncontent"] = len(cl)
    ms = set()
    for i in cl: ms |= inst_cov.get((r["stem"], i), set())
    covered = bool(cl) and all((r["stem"], i) in inst_cov for i in cl)
    r["modules"] = ", ".join(sorted(ms))
    if r["kind"] == "front" and not any((r["stem"], i) in inst_cov for i in cl):
        r["disp"], r["reason"] = "inert", "1: title, arrangement of regulations and enacting words: not operative"
    elif r["kind"] == "back":
        r["disp"], r["reason"] = "inert", "1: date of making, signature and file reference: not operative"
    elif not cl:
        r["disp"], r["reason"] = "inert", "3: blank or page furniture only"
    elif covered and r["id"] in FORK_I:
        r["disp"], r["reason"] = "fork", FORK_I[r["id"]]
    elif covered:
        r["disp"], r["reason"] = "encoded", ""
    else:
        iv = INERT_I.get(r["id"]) if "INERT_I" in globals() else None
        if iv: r["disp"], r["reason"] = "inert", iv[0] + ": " + iv[1]
        else: r["disp"], r["reason"] = "pending", "%d of %d content lines quoted" % (sum(1 for i in cl if (r["stem"], i) in inst_cov), len(cl))

# ---- checks -------------------------------------------------------------------------------------
top = [r for r in rows if r["kind"] in ("front", "long title", "section", "back")]
covered = set()
for r in top:
    for ln in range(r["start"], r["end"] + 1): covered.add(ln)
nonblank = [i + 1 for i, s in enumerate(lines) if s.strip()]
uncovered = [ln for ln in nonblank if ln not in covered]
part_lines = {r["start"] for r in rows if r["kind"] == "part"}
unrecognised = []
for ln in uncovered:
    s = lines[ln - 1]
    nxt = next((r for r in top if r["kind"] == "section" and r["start"] > ln), None)
    if ln in part_lines or is_furniture(s) or is_mark(s) or re.match(r"^\s*[A-Z][A-Z ,.'\-]+$", s.strip()) or (nxt and nxt["start"] - ln <= 8):
        continue
    unrecognised.append(ln)
act_pending = [r for r in rows if r["disp"] == "pending"]
inst_pending = [r for r in inst_rows if r["disp"] == "pending"]
checks = [
    ("sections found are exactly 1..98 in order", ok_sections),
    ("every section number appears in the arrangement of sections", not missing_in_arr),
    ("non-blank lines not inside any section/front/back row and not a heading, Part heading or page furniture", len(unrecognised) == 0),
    ("every inert row has one of the three allowed reasons", all(r["tier"] in REASON for r in rows if r["disp"] == "inert") ),
    ("no row of the Act is pending", not act_pending),
    ("no instrument row is pending", not inst_pending),
]

# ---- write COVERAGE.md ----------------------------------------------------------------------------
def esc(s): return str(s).replace("|", "\\|")
out = []
out.append("# Coverage table: Telecommunications Act 1999 (2020 Revised Edition deposit) and the instruments deposited under it\n")
out.append("Generated by `gen-coverage.py` from the deposited texts and from the `@ref` locators of the rule modules; do not edit by hand.\n")
out.append("Dispositions: `encoded` (every content line of the row is quoted and cited by a rule: see the module column), `inert` (reason 1 not operative, 2 machinery, 3 repealed or blank), `fork` (a fork-register entry; the lines are also quoted by the rule for the chosen reading), `pending` (working state; the final table has none).\n")
out.append("`2000 Ed. s` is the number the Law Revision Commission's margin marker gives the section in the 2000 Revised Edition; the pre-2020 instruments cite those numbers.\n")
cnt = {}
for r in rows: cnt[("Act", r["kind"], r["disp"])] = cnt.get(("Act", r["kind"], r["disp"]), 0) + 1
for r in inst_rows: cnt[("Instruments", r["kind"], r["disp"])] = cnt.get(("Instruments", r["kind"], r["disp"]), 0) + 1
out.append("## Counts\n")
out.append("| text | row kind | disposition | rows |\n|---|---|---|---|")
for (t, k, d), c in sorted(cnt.items()): out.append(f"| {t} | {k} | {d} | {c} |")
out.append("")
out.append("## Checks\n")
for name, ok in checks: out.append(f"- {'PASS' if ok else 'FAIL'}: {name}")
out.append(f"- Act: {len(act_pending)} pending rows; instruments: {len(inst_pending)} pending rows; {len(inst_files)} instrument text files parsed.")
out.append("")
out.append("## Sections of the Act (one row each)\n")
out.append("| s | heading | 2000 Ed. s | Part | lines | disposition | module | note |\n|---|---|---|---|---|---|---|---|")
for r in rows:
    if r["kind"] != "section": continue
    head, old, part = [x.strip() for x in r["extra"].split("|")]
    out.append(f"| {r['id'][2:]} | {esc(head)} | {old.replace('2000 Ed. s ','')} | {part.replace('Part ','')} | {r['start']}-{r['end']} | {r['disp']}{(' (' + r['tier'] + ')') if r['disp']=='inert' else ''} | {r['modules']} | {esc(r['reason'])} |")
out.append("")
out.append("## Every other row of the Act (subsections, paragraphs, defined terms, Parts, front and back matter)\n")
out.append("| row | kind | lines | disposition | module | note |\n|---|---|---|---|---|---|")
for r in rows:
    if r["kind"] == "section": continue
    out.append(f"| {esc(r['id'])} | {r['kind']} | {r['start']}-{r['end']} | {r['disp']}{(' (' + r['tier'] + ')') if r['disp']=='inert' else ''} | {r['modules']} | {esc(r['reason'])} |")
out.append("")
out.append("## Instruments made under the Act: one row per provision of each deposited text\n")
out.append("Source of the list: IMDA's Telecommunications Act 1999 page (https://www.imda.gov.sg/regulations-and-licensing-listing/telecommunications-act-1999), fetched 2026-11-03: 40 PDFs, each deposited with its text under `subjects/sg/telecommunications-*/registers/source-bundle/`.")
out.append("The page lists nothing after S 100/2016 (Rg 5), S 726/2014 (N 1) or S 725/2014 (Rg 6); whether the list is current is not established.")
out.append("A provision's `lines` are lines of its own text file. An amending instrument's row is the provision of the amending instrument (its own words), not the amended text.")
out.append("The instruments under the Broadcasting Act are in the Broadcasting Act folder's own table.\n")
out.append("| provision | lines | disposition | module | note |\n|---|---|---|---|---|")
for r in inst_rows:
    out.append(f"| {esc(r['id'])} | {r['start']}-{r['end']} | {r['disp']} | {r['modules']} | {esc(r['reason'])} |")
if SOURCE_NOT_OBTAINED:
    out.append("")
    out.append("## Instruments whose text was not obtained (`source not obtained`)\n")
    out.append("| instrument | made under | where I looked and what each place answered |\n|---|---|---|")
    for a, b, c in SOURCE_NOT_OBTAINED: out.append(f"| {esc(a)} | {esc(b)} | {esc(c)} |")
open(os.path.join(HERE, "COVERAGE.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")

print("Act rows:", len(rows), " sections:", len(secs), " sub-rows:", len(sub_rows), "| instrument rows:", len(inst_rows), "in", len(inst_files), "files")
print("counts:", {f"{t}/{d}": sum(c for (tt, k, dd), c in cnt.items() if tt == t and dd == d) for t in ("Act", "Instruments") for d in ("encoded", "inert", "fork", "pending")})
for name, ok in checks: print(("PASS " if ok else "FAIL ") + name)
print("unrecognised lines:", unrecognised[:20])
hard = [ok for (name, ok) in checks[:4]]
sys.exit(1 if not all(hard) else (2 if (act_pending or inst_pending) else 0))
