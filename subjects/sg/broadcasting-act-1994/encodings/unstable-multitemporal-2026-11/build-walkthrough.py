#!/usr/bin/env python3
"""Build WALKTHROUGH.md from walkthrough-template.md.

  L4=/path/to/unstable/l4 L4_MAIN=/path/to/main/l4 python3 -I build-walkthrough.py

What it does, in order:
  1. writes the generated block of #EVAL directives (the same table of conduct-day and reading-day pairs) into
     sgbau-walkthrough.l4 and into each alternative-way file in findings/;
  2. runs `l4 run` on each file with the unstable build, and on the probe file with the stable build, and keeps
     what was printed, keyed by file and line;
  3. fills walkthrough-template.md: {{code}} copies lines from a module with their line numbers, {{run}} copies a
     directive and what it printed, {{pairs}} and {{ways}} and {{table}} copy printed values, {{diag}} copies a
     stable-build diagnostic verbatim.
Nothing printed is retyped.  The one hand-written thing is EXPECTED, the table of what the text says for each
pair, written from the Gazette texts before the stable row was read (it is the same table as in
gen-tests-schedule.py, extended with the edge days); the script compares each printed value with it and marks the
rows that differ.  It also checks the claims of the walkthrough's top section against the printed values, and stops
if one is false.
"""
import datetime
import os
import re
import subprocess
import sys

ROW = os.path.dirname(os.path.abspath(__file__))
L4 = os.environ.get("L4")
L4_MAIN = os.environ.get("L4_MAIN")
if not L4 or not L4_MAIN:
    sys.exit("set L4 (the unstable build) and L4_MAIN (the stable build)")

try:
    from zoneinfo import ZoneInfo
    TODAY = datetime.datetime.now(ZoneInfo("Asia/Singapore")).date()
except Exception:  # pragma: no cover
    TODAY = datetime.date.today()

THREE = "`the First Schedule of three items`"
TVRO = "`the First Schedule of the TVRO system only`"
REF = "REFUSED"

# --------------------------------------------------------------------------------------------------------------
# The pairs.  (id, conduct day, reading day, expected text, what the pair is)
# A day is (d, m, y) or "today".  Expected: THREE, TVRO or REF, written by hand from the sources:
#   S 549/2012 cl 1: deemed in operation from 1 January 2011; first published 31 October 2012 (5.00 pm);
#   the 2003 Revised Edition operates from 31 July 2003 (the first deposited edition).
#   The text of S 549/2012 governs conduct on or after 1 Jan 2011 for a reader on or after 31 Oct 2012;
#   the three-item text governs everything else on or after 31 Jul 2003; before that, not covered.
# --------------------------------------------------------------------------------------------------------------
PAIRS = [
    ("P01", (1, 6, 2011), (1, 8, 2012), THREE, "conduct in 2011, read before 31 October 2012"),
    ("P02", (1, 6, 2011), (31, 10, 2012), TVRO, "conduct in 2011, read on 31 October 2012"),
    ("P03", (1, 6, 2011), (1, 11, 2012), TVRO, "conduct in 2011, read on 1 November 2012"),
    ("P04", (1, 6, 2011), (1, 1, 2020), TVRO, "conduct in 2011, read in 2020"),
    ("P05", (31, 12, 2010), (1, 8, 2012), THREE, "conduct in 2010, read before 31 October 2012"),
    ("P06", (31, 12, 2010), (1, 11, 2012), THREE, "conduct in 2010, read after 31 October 2012"),
    ("P07", (1, 6, 2011), (30, 10, 2012), THREE, "read the day before it was published"),
    ("P08", (30, 10, 2012), (1, 11, 2012), TVRO, "conduct the day it was made"),
    ("P09", (31, 10, 2012), (1, 11, 2012), TVRO, "conduct the day it was published"),
    ("P10", (1, 11, 2012), (1, 11, 2012), TVRO, "conduct the day after it was published"),
    ("P11", (31, 10, 2012), (30, 10, 2012), THREE, "conduct the day it was published, read the day before"),
    ("P12", (1, 1, 2011), (1, 11, 2012), TVRO, "conduct on the first day it is deemed to operate"),
    ("P13", "today", "today", TVRO, "conduct today, read today"),
    ("P14", (30, 7, 2003), "today", REF, "conduct the day before the first deposited edition"),
    ("P15", (31, 7, 2003), "today", THREE, "conduct on the first day of the first deposited edition"),
]
PAIR = {p[0]: p for p in PAIRS}
# What each text says about a television set, a radio set, a satellite dish system.
VERDICT = {THREE: ("TRUE", "TRUE", "TRUE"), TVRO: ("FALSE", "FALSE", "TRUE")}

# The ways of writing the rule that are run on every pair: id, file, the wrapper's name.
ALT = [
    ("W0", "findings/alt-w0-no-publication-gate.l4"),
    ("W1NOW", "findings/alt-w1-now-gate.l4"),
    ("W3", "findings/alt-w3-selector.l4"),
    ("W4", "findings/alt-w4-version-table.l4"),
    ("REV", "findings/alt-reverse-mapping.l4"),
    ("DEC", "findings/alt-decorators.l4"),
]
WAYS_ORDER = ["W1", "W2", "W0", "W3", "W4", "W1NOW", "REV", "DEC"]
WAY_NAME = {
    "W1": "W1, the chosen way",
    "W2": "W2, rule-effective axis pinned",
    "W0": "W0, no reader gate",
    "W3": "W3, selector outside",
    "W4": "W4, table of versions",
    "W1NOW": "W1-NOW, gate on NOW at 5.00 pm",
    "REV": "reverse mapping",
    "DEC": "decorators",
}
MARK_B = "-- BEGIN GENERATED PAIRS"
MARK_E = "-- END GENERATED PAIRS"


def day(x):
    if x == "today":
        return (TODAY.day, TODAY.month, TODAY.year)
    return x


def dstr(x):
    d, m, y = day(x)
    return f"{d} {datetime.date(y, m, d).strftime('%b')} {y}"


def date_l4(x):
    d, m, y = day(x)
    return f"(Date {d} {m} {y})"


# --------------------------------------------------------------------------------------------------------------
# 1. write the generated blocks
# --------------------------------------------------------------------------------------------------------------
def write_block(path, lines):
    full = os.path.join(ROW, path)
    text = open(full, encoding="utf-8").read().split("\n")
    b = next(i for i, l in enumerate(text) if l.startswith(MARK_B))
    e = next(i for i, l in enumerate(text) if l.startswith(MARK_E))
    new = text[: b + 1] + lines + text[e:]
    open(full, "w", encoding="utf-8").write("\n".join(new))


LINEMAP = {}  # (file, line) -> (way, pair id, what)


def generate():
    for way, path in ALT:
        lines = []
        for pid, c, r, _, _ in PAIRS:
            lines.append(f"#EVAL `the text under this way` {date_l4(c)} {date_l4(r)}   -- {pid}")
        write_block(path, lines)
    lines = []
    for pid, c, r, _, _ in PAIRS:
        a = f"{date_l4(c)} {date_l4(r)}"
        lines.append(f"#EVAL `Which text of the First Schedule applied` {a}   -- {pid} W1 text")
        lines.append(f"#EVAL `the licensing rule catches a television` {a}   -- {pid} W1 television")
        lines.append(f"#EVAL `the licensing rule catches a radio` {a}   -- {pid} W1 radio")
        lines.append(f"#EVAL `the licensing rule catches a satellite dish` {a}   -- {pid} W1 dish")
        lines.append(f"#EVAL `the text, with the rule-effective axis pinned` {a}   -- {pid} W2 text")
    lines.append(f"#EVAL `the text, with the reading day left to the clock` {date_l4(('today'))}   -- P13 clock")
    write_block("sgbau-walkthrough.l4", lines)


# --------------------------------------------------------------------------------------------------------------
# 2. run, and parse what was printed
# --------------------------------------------------------------------------------------------------------------
def run(binary, path):
    env = {k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"}
    p = subprocess.run([binary, "run", path], cwd=ROW, capture_output=True, text=True, env=env)
    return p.stdout + p.stderr


def parse(out):
    """Blocks of l4 run output: {line: [dict(sev, src, msg, raw)]}, first occurrence of each only."""
    res = {}
    lines = out.split("\n")
    i = 0
    seen = set()
    while i < len(lines):
        if lines[i].startswith("File:"):
            j = i + 1
            while j < len(lines) and (lines[j].startswith(" ") or lines[j] == ""):
                j += 1
            blk = lines[i:j]
            i = j
            rng = next((l.split(":", 1)[1].strip() for l in blk if l.strip().startswith("Range:")), None)
            sev = next((l.split(":", 1)[1].strip() for l in blk if l.strip().startswith("Severity:")), "")
            src = next((l.split(":", 1)[1].strip() for l in blk if l.strip().startswith("Source:")), "")
            mi = next((k for k, l in enumerate(blk) if l.strip().startswith("Message:")), None)
            if rng is None or mi is None:
                continue
            first = blk[mi].split("Message:", 1)[1].strip()
            rest = [l[4:] if l.startswith("    ") else l.strip() for l in blk[mi + 1 :]]
            while rest and rest[-1].strip() == "":
                rest.pop()
            msg_lines = ([first] if first else []) + rest
            raw = ["Range:    " + rng, "Severity: " + sev.replace("DiagnosticSeverity_", ""), "Message:"] + [
                "    " + l if l.strip() else "" for l in ([first] if first else []) + rest
            ]
            key = (rng, sev, tuple(msg_lines))
            if key in seen:
                continue
            seen.add(key)
            ln = int(rng.split(":")[0])
            res.setdefault(ln, []).append(
                dict(sev=sev.replace("DiagnosticSeverity_", ""), src=src, msg=" ".join(m.strip() for m in msg_lines if m.strip()), raw=raw)
            )
        else:
            i += 1
    return res


RESULTS = {}  # file -> {line: [..]}


def results_for(path, binary=None):
    key = (path, binary or L4)
    if key not in RESULTS:
        RESULTS[key] = parse(run(binary or L4, path))
    return RESULTS[key]


def printed(path, line, binary=None):
    """What was printed for the directive on `line`: a short string."""
    blocks = results_for(path, binary).get(line, [])
    ev = [b for b in blocks if b["src"] == "eval"]
    if ev:
        b = ev[0]
        if b["sev"] == "Warning" and b["msg"].startswith("The model refuses to answer"):
            return REF
        return b["msg"]
    errs = [b for b in blocks if b["sev"] == "Error"]
    if errs:
        return "ERROR: " + errs[0]["msg"]
    return "(nothing printed)"


def file_lines(path):
    return open(os.path.join(ROW, path), encoding="utf-8").read().split("\n")


def find_line(path, anchor, nth=1):
    n = 0
    for i, l in enumerate(file_lines(path), 1):
        if anchor in l:
            n += 1
            if n == nth:
                return i
    sys.exit(f"anchor not found in {path}: {anchor!r}")


# --------------------------------------------------------------------------------------------------------------
# 3. the tables of results
# --------------------------------------------------------------------------------------------------------------
W = {}  # way -> pair -> printed text ; and W1 verdicts


def collect():
    # W1 and W2 and the verdicts: the walkthrough module
    path = "sgbau-walkthrough.l4"
    lines = file_lines(path)
    W1V = {}
    for ln, l in enumerate(lines, 1):
        m = re.search(r"-- (P\d+) (W1|W2) (text|television|radio|dish)$", l)
        if m:
            pid, way, what = m.groups()
            val = printed(path, ln)
            if what == "text":
                W.setdefault(way, {})[pid] = val
                W1V.setdefault((way, pid), {})["line"] = ln
            else:
                W1V.setdefault((way, pid), {})[what] = (val, ln)
        m = re.search(r"-- (P\d+) clock$", l)
        if m:
            W.setdefault("CLOCK", {})[m.group(1)] = printed(path, ln)
            W.setdefault("CLOCKLINE", {})[m.group(1)] = ln
    W["VERD"] = W1V
    for way, path in ALT:
        for ln, l in enumerate(file_lines(path), 1):
            m = re.search(r"-- (P\d+)$", l)
            if m and l.startswith("#EVAL `the text under this way`"):
                W.setdefault(way, {})[m.group(1)] = printed(path, ln)
                W.setdefault(way + "LINE", {})[m.group(1)] = ln


def short(v):
    if v == THREE:
        return "A"
    if v == TVRO:
        return "B"
    if v == REF:
        return "refused"
    if v.startswith("ERROR") or v.startswith("(nothing"):
        return "no value"
    return v


def expected(pid):
    return PAIR[pid][3]


def mark(pid, v):
    return "" if v == expected(pid) else " **differs**"


# --------------------------------------------------------------------------------------------------------------
# 4. template directives
# --------------------------------------------------------------------------------------------------------------
GLOSS = {
    "RED": [
        "`RULES EFFECTIVE DATE` asks which day's version of the law is being used.",
        "Its axis is rule-effective time, the tutorial's question \"Which version of the law applies?\".",
        "Unless told otherwise it follows the day of the conduct.",
    ],
    "EUR": [
        "`EVAL UNDER RULES EFFECTIVE AT` d x works out x using the version of the law in force on day d, whatever day the facts belong to.",
        "It moves rule-effective time (\"Which version of the law applies?\").",
    ],
    "EAS": [
        "`EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.",
        "It moves system time (\"When is this evaluation actually running?\").",
    ],
    "EUV": [
        "`EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.",
        "It moves valid time (\"When did, or does, the fact hold in the world?\").",
        "Here d is the day of the conduct.",
    ],
    "TODAY": [
        "`TODAY` is the day on which the question is being asked.",
        "It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.",
    ],
}


def d_uses(args):
    out = []
    for a in args.split():
        sents = GLOSS[a]
        out.append("- " + sents[0])
        out.extend("  " + x for x in sents[1:])
    return "\n".join(out)


def d_code(args):
    parts = [x.strip() for x in args.split("|")]
    path, anchor, n = parts[0], parts[1], int(parts[2])
    nth = int(parts[3]) if len(parts) > 3 else 1
    start = find_line(path, anchor, nth)
    lines = file_lines(path)[start - 1 : start - 1 + n]
    while lines and lines[-1].strip() == "":
        lines.pop()
    end = start + len(lines) - 1
    width = len(str(end))
    body = "\n".join(f"{start + i:>{width}}  {l}" for i, l in enumerate(lines))
    where = f"{path}:{start}" if start == end else f"{path}:{start}-{end}"
    return f"`{where}`\n\n```\n{body}\n```"


def d_run(args):
    parts = [x.strip() for x in args.split("|")]
    path, anchor = parts[0], parts[1]
    ln = find_line(path, anchor)
    text = file_lines(path)[ln - 1]
    blocks = results_for(path).get(ln, [])
    out = [f"`{path}:{ln}`", "", "```", f"{ln:>5}  {text}", "```", "", "`l4 run` printed:", "", "```"]
    if not blocks:
        out.append("(nothing printed for this line)")
    for b in blocks:
        if b["src"] == "eval" or b["sev"] in ("Error", "Warning"):
            out.append(b["msg"])
    out.append("```")
    return "\n".join(out)


def d_pairs(args):
    ids = args.split()
    rows = ["| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |", "|---|---|---|---|---|---|---|---|"]
    for pid in ids:
        _, c, r, exp, what = PAIR[pid]
        v = W["VERD"][("W1", pid)]
        t = W["W1"][pid]
        tv, rd, dh = (v[k][0] for k in ("television", "radio", "dish"))
        ln = v["line"]
        rows.append(
            f"| {pid} | {dstr(c)} | {dstr(r)} | {t}{mark(pid, t)} | {tv} | {rd} | {dh} | `sgbau-walkthrough.l4:{ln}-{ln + 3}` |"
        )
    return "\n".join(rows)


def way_table(way, path, lines):
    rows = ["| pair | conduct day | reading day | printed | the text says |", "|---|---|---|---|---|"]
    for pid, c, r, exp, what in PAIRS:
        v = W[way][pid]
        rows.append(f"| {pid} | {dstr(c)} | {dstr(r)} | {short(v)}{mark(pid, v)} | {short(exp)} |")
    lo, hi = min(lines.values()), max(lines.values())
    rows.append("")
    rows.append(f"Printed by the directives at `{path}:{lo}-{hi}`, one for each pair, in the order of the table.")
    return "\n".join(rows)


def d_ways(args):
    way = args.strip()
    return way_table(way, dict(ALT)[way], W[way + "LINE"])


def d_w2(args):
    return way_table("W2", "sgbau-walkthrough.l4", {pid: W["VERD"][("W2", pid)]["line"] for pid, *_ in PAIRS})


def d_table(args):
    head = "| pair | conduct day | reading day | the text says | " + " | ".join(WAY_NAME[w] for w in WAYS_ORDER) + " |"
    sep = "|---|---|---|---|" + "---|" * len(WAYS_ORDER)
    rows = [head, sep]
    for pid, c, r, exp, what in PAIRS:
        cells = []
        for w in WAYS_ORDER:
            v = W[w][pid]
            cells.append(short(v) + ("" if v == exp else " (differs)"))
        rows.append(f"| {pid} | {dstr(c)} | {dstr(r)} | {short(exp)} | " + " | ".join(cells) + " |")
    legend = f"A = {THREE}; B = {TVRO}; refused = the model refuses to answer; no value = the build printed an error instead of a value."
    return "\n".join(rows) + "\n\n" + legend


def d_diag(args):
    parts = [x.strip() for x in args.split("|")]
    path, anchor, which = parts[0], parts[1], parts[2]
    binary = L4_MAIN if which == "main" else L4
    ln = find_line(path, anchor)
    text = file_lines(path)[ln - 1]
    blocks = results_for(path, binary).get(ln, [])
    out = [f"`{path}:{ln}`", "", "```", f"{ln:>5}  {text}", "```", "", "printed:", "", "```"]
    if not blocks:
        out.append("(nothing printed for this line)")
    for k, b in enumerate(blocks):
        if k:
            out.append("")
        out.extend(b["raw"])
    out.append("```")
    return "\n".join(out)


def d_pairlist(args):
    rows = ["| pair | conduct day | reading day | what the pair is |", "|---|---|---|---|"]
    for pid, c, r, exp, what in PAIRS:
        rows.append(f"| {pid} | {dstr(c)} | {dstr(r)} | {what} |")
    return "\n".join(rows)


def d_var(args):
    return {
        "TODAY": f"{TODAY.day} {TODAY.strftime('%B')} {TODAY.year}",
        "L4VERSION": subprocess.run([L4, "--version"], capture_output=True, text=True).stdout.strip(),
        "MAINVERSION": subprocess.run([L4_MAIN, "--version"], capture_output=True, text=True).stdout.strip(),
        "LEGEND_A": THREE,
        "LEGEND_B": TVRO,
    }[args.strip()]


def d_val(args):
    """{{val W1 text P01}} -> the printed value, mechanically."""
    way, what, pid = args.split()
    if way in ("W1", "W2") and what == "text":
        return W[way][pid]
    if way == "W1":
        return W["VERD"][("W1", pid)][what][0]
    return W[way][pid]


DIRECTIVES = {
    "uses": d_uses, "code": d_code, "run": d_run, "pairs": d_pairs, "ways": d_ways, "w2": d_w2,
    "table": d_table, "pairlist": d_pairlist, "diag": d_diag, "var": d_var, "val": d_val,
}


# --------------------------------------------------------------------------------------------------------------
# 5. the claims of the top section, checked against what was printed
# --------------------------------------------------------------------------------------------------------------
def check_claims():
    bad = []

    def need(cond, msg):
        if not cond:
            bad.append(msg)

    t = W["W1"]
    v = W["VERD"]
    need(t["P01"] == THREE and t["P02"] == TVRO, "step 1/2: the same conduct, two readers, two texts")
    need(all(t[p] == exp for p, _, _, exp, _ in PAIRS), "W1 does not print the hand-written table on every pair")
    need(t["P05"] == t["P06"] == THREE, "step 3: conduct in 2010 reads the three-item text for both readers")
    need(v[("W1", "P05")]["television"][0] == "TRUE" == v[("W1", "P06")]["television"][0], "step 3: the licensing rule, as encoded, catches the television for both readers")
    need(v[("W1", "P01")]["television"][0] == "TRUE" and v[("W1", "P03")]["television"][0] == "FALSE", "steps 1 and 2: the licensing rule, as encoded, catches the television for the reader of August 2012 and does not for the reader of November 2012")
    need(sum(1 for w in WAYS_ORDER if all(W[w][p].startswith(("ERROR", "(nothing")) for p, *_ in PAIRS)) == 1, "step 7g: exactly one way prints no value at all")
    need(t["P07"] == THREE and t["P02"] == TVRO, "step 4: the reader gate falls between 30 and 31 October 2012")
    need(t["P06"] == THREE and t["P12"] == TVRO, "step 4: the conduct gate falls between 31 Dec 2010 and 1 Jan 2011")
    need(v[("W1", "P13")]["television"][0] == "FALSE" and v[("W1", "P13")]["dish"][0] == "TRUE", "step 5: today the First Schedule, as encoded, lists the dish and not the television")
    need(v[("W1", "P01")]["radio"][0] == "TRUE" and v[("W1", "P02")]["radio"][0] == "FALSE", "step 6: the radio follows the television")
    need(all(v[("W1", p)]["dish"][0] == "TRUE" for p, _, _, e, _ in PAIRS if e != REF), "step 6: the dish is TRUE wherever covered")
    need(W["W2"] == W["W1"], "step 7a: W2 differs from W1")
    need(W["W4"] == W["W1"], "step 7d: W4 differs from W1")
    need(W["W0"]["P01"] == TVRO and W["W0"]["P07"] == TVRO, "step 7b: W0 should tell a pre-publication reader the new text")
    need(all(W["W0"][p] == W["W1"][p] for p in ("P02", "P03", "P05", "P12")), "step 7b: W0 should agree where the reader is after publication")
    need(W["W3"]["P01"] == THREE and W["W3"]["P02"] == TVRO, "step 7c: W3 right for one day")
    need(W["W1NOW"]["P02"] == THREE and W["W1"]["P02"] == TVRO, "step 7e: the NOW gate differs on 31 October 2012")
    need(W["REV"]["P06"] == TVRO and W["W1"]["P06"] == THREE, "step 7f: the reverse mapping gets conduct in 2010 wrong")
    need(all(W["DEC"][p].startswith(("ERROR", "(nothing")) for p, *_ in PAIRS), "step 7g: decorators print no value")
    mp = "findings/walkthrough-main-probe.l4"
    for anchor in ("#EVAL `RULES EFFECTIVE DATE`", "#EVAL `EVAL UNDER RULES EFFECTIVE AT`", "#EVAL `EVAL UNDER VALID TIME`", "#EVAL `EVAL AS OF SYSTEM TIME`"):
        ln = find_line(mp, anchor)
        need(any("could not find a definition" in b["msg"] for b in results_for(mp, L4_MAIN).get(ln, [])), "step 8: the stable build should not know " + anchor)
    tl = find_line("findings/walkthrough-main-probe-today.l4", "#EVAL TODAY")
    need(any(b["src"] == "eval" and b["msg"].startswith("DATE OF") for b in results_for("findings/walkthrough-main-probe-today.l4", L4_MAIN).get(tl, [])), "step 8: TODAY should print a date on the stable build")
    if bad:
        sys.exit("CLAIM CHECK FAILED:\n  " + "\n  ".join(bad))


def render():
    tpl = open(os.path.join(ROW, "walkthrough-template.md"), encoding="utf-8").read().split("\n")
    out = []
    for l in tpl:
        m = re.fullmatch(r"\{\{(\w+)\s*(.*?)\}\}", l.strip())
        if m and m.group(1) in DIRECTIVES:
            out.append(DIRECTIVES[m.group(1)](m.group(2)))
        else:
            # inline {{var X}}, {{val ...}}
            def sub(mm):
                return DIRECTIVES[mm.group(1)](mm.group(2))

            out.append(re.sub(r"\{\{(var|val)\s+([^}]*)\}\}", sub, l))
    return "\n".join(out)


def main():
    generate()
    collect()
    # the probe for the stable build is a plain file, run on the main build
    check_claims()
    text = render()
    open(os.path.join(ROW, "WALKTHROUGH.md"), "w", encoding="utf-8").write(text)
    print("WALKTHROUGH.md written;", len(text.split("\n")), "lines; claims checked")


if __name__ == "__main__":
    main()
