#!/usr/bin/env python3
"""Generate nii-schedule-j-tables.l4 from the two tables of Schedule J in the deposited source.

Every figure in the generated module is read from a cell of the source table, with ONE exception
(CORRECTIONS below, added 2026-11-09): seven cells of the permanent table, four of them also in the
temporary table, that the Hebrew Wikisource consolidation prints wrongly. For those the generator
checks that the source still prints the consolidation's wrong figure, writes the OFFICIAL figure
(read by hand from the page image of the amending instrument, which is not in the
Wikisource consolidation; the instruments' PDFs are in registers/source-bundle/amending-laws/) and writes the instrument's own words as `ext:` comment lines (transcribed from the page
images by hand, so not checked mechanically against any file; tools/hebcheck.py skips them). If
the source ever prints the official figure, the generator says so and still writes it, so the
correction can then be deleted from CORRECTIONS. A cell "–" becomes NOTHING. A cell "X {{ח:הערה|(הוראת שעה בשנים 2024 עד 2027: Y)}}" gives the
printed figure X, and Y for the separate row or totals row the generator emits for 2024-2027.
Any cell of another shape stops the generator, so a change in the source cannot slip through.

The rows are laid out with positional OF construction under one ruler comment per table, the
column widths computed here (writing-l4-rules SKILL.md, "Statutory tables: generate the layout,
do not type it"). No ditto is used: every row is written out whole.

Usage: python3 -I schedule_j.py SOURCE.wiki.txt OUT.l4
"""
import re
import sys

SRC_PATH, OUT = sys.argv[1], sys.argv[2]
SRC = open(SRC_PATH, encoding="utf-8").read().split("\n")

TABLES = [
    # (key, title, label line, first heading line, first item line, totals line, col D note)
    ("temporary", "the temporary version, for 2025-2026", 4714, 4716, 4720, 4730, True),
    ("permanent", "the permanent version", 4732, 4734, 4738, 4748, False),
]

BRANCH = {
    "אימהות": "`maternity`",
    "אימהות – מבוטח שאינו עובד ואינו עובד עצמאי": "`maternity`",
    "ילדים": "`children`",
    "נפגעי עבודה": "`work injury`",
    "נפגעי תאונות": "`accident injury`",
    "אבטלה": "`unemployment`",
    "זכויות עובדים בהליכי חדלות פירעון": "`employees' rights in insolvency proceedings`",
    "נכות": "`disability`",
    "סיעוד": "`long-term care`",
    "אזרחים ותיקים ושאירים": "`senior citizens and survivors`",
}

# The consolidation's seven wrong cells (CORRECTED 2026-11-09; NOTES.md, "Correction 2026-11-09").
# Columns are indexes into the nine figure columns of RULER: 0 C above the threshold, employee;
# 3 C not above the threshold, employee; 6 D upper part. Each entry: column index, the figure the
# consolidation prints, the figure the official text prints, the ext: tag of the instrument.
CORRECTIONS = {
    ("permanent", "1"):  [(3, "0.16", "0.15", "SH2023-p813")],
    ("permanent", "3"):  [(3, "1.47", "1.32", "SH2023-p813")],
    ("permanent", "6"):  [(0, "0.33", "0.37", "SH2382-p756")],
    ("permanent", "7"):  [(0, "0.04", "0.06", "SH2382-p756")],
    ("permanent", "9"):  [(0, "0.28", "0.33", "SH2382-p756")],
    ("permanent", "10"): [(3, "1.67", "1.52", "SH2023-p813"), (6, "1.52", "3.85", "SH2023-p813")],
    ("temporary", "6"):  [(0, "0.33", "0.37", "SH2382-p756")],
    ("temporary", "7"):  [(0, "0.04", "0.06", "SH2382-p756")],
    ("temporary", "9"):  [(0, "0.28", "0.33", "SH2382-p756")],
    ("temporary", "10"): [(6, "1.52", "3.85", "SH2023-p813")],
}
COLNAME = {
    0: "column C, above the threshold, employee",
    3: "column C, not above the threshold, employee",
    6: "column D, upper part of the wage",
}

# The instruments' own words, transcribed BY HAND from the page images (Sefer HaChukim pages read
# as images, 2026-11-09), not copied from a file and not checked mechanically. Rows are written in
# the order of the consolidation's table (item, branch, the six figures of column C, the two of
# column D, column E); the page prints them right to left. "–" is a dash on the page.
EXT_BLOCK = [
    "-- ext:[SH2382-p755] | (2) בלוח י׳, בטור ג׳ שכותרתו ״אחוזים מההכנסה או מהשכר לפי סעיפים 337(א) ו־340(א)״, בכותרת המשנה ״על חלק העולה על 60% מהשכר הממוצע״, בטור המשנה ״לעובד״, במקום האחוזים המפורטים בו יבוא:",
    "-- ext:[SH2382-p755] | items 1 to 5 of the column: 1.40 | – | 2.08 | 1.96 | 0.13",
    "-- ext:[SH2382-p756] | items 6 to 10 of the column, then the total: 0.37 | 0.06 | 2.28 | 0.33 | 5.89 | 14.50",
    "-- ext:[SH2023-p813] | שיעור דמי ביטוח בעד שנת 2009 ואילך",
    "-- ext:[SH2023-p813] | 1 | אימהות | 1.03 | 0.82 | – | 0.15 | 0.56 | – | 0.87 | 0.04 | 0.09",
    "-- ext:[SH2023-p813] | 3 | ילדים | 2.08 | 2.40 | 2.64 | 1.32 | 1.39 | 1.10 | – | – | 0.10",
    "-- ext:[SH2023-p813] | 10 | זקנה ושאירים | 5.89 | 5.21 | 5.76 | 1.52 | 3.09 | 2.40 | 3.85 | 0.22 | 0.25",
    "-- ext:[SH2023-p813] | סך הכל | 12.43 | 11.23 | 11.05 | 3.85 | 6.72 | 4.61 | 7.00 | 0.40 | 0.69",
]
EXT_BLOCK_WRONG = [
    "-- ext:[SH2203-p259] | (א) בתקופה שמיום י״א באב התשס״ט (1 באוגוסט 2009) ועד יום כ״ה באדר ב׳ התשע״א (31 במרץ 2011) ייקרא לוח י׳ בחוק הביטוח הלאומי כך: [...] בטור ג׳, [...] בכותרת המשנה ״על החלק שאינו עולה על 60% מהשכר הממוצע״, בטור המשנה ״לעובד״, במקום האחוזים המפורטים בו, יקראו:",
    "-- ext:[SH2203-p259] | the ten figures and the total: 0.16 | – | 1.47 | 0.41 | 0.02 | 0.04 | 0.01 | 0.41 | 0.06 | 1.67 | 4.25",
    "-- ext:[SH2429-p266] | במקום האחוזים המפורטים בו יקראו:",
    "-- ext:[SH2429-p266] | the ten figures and the total: 1.27 | – | 2.08 | 1.47 | 0.11 | 0.33 | 0.04 | 2.28 | 0.28 | 5.89 | 13.75",
]

NOTE = re.compile(r"^([0-9]+\.[0-9]+) \{\{ח:הערה\|\(הוראת שעה בשנים 2024 עד 2027: ([0-9]+\.[0-9]+)\)\}\}$")
NUM = re.compile(r"^[0-9]+\.[0-9]+$")

RULER = ("item, branch,"
         " C above: employee, self-employed, neither;"
         " C not above: employee, self-employed, neither;"
         " D upper, D not above; E")


def cells(n):
    line = SRC[n - 1]
    return re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", line)


def parse_cell(c, line_no):
    """-> (printed, in_2024_2027) as L4 text, e.g. ('JUST 1.96', 'JUST 2.06')."""
    c = c.strip()
    if c == "–":
        return "NOTHING", "NOTHING"
    if NUM.match(c):
        return f"JUST {c}", f"JUST {c}"
    m = NOTE.match(c)
    if m:
        return f"JUST {m.group(1)}", f"JUST {m.group(2)}"
    sys.exit(f"schedule_j.py: unexpected cell at source line {line_no}: {c!r}")


def parse_total(c, line_no):
    c = c.strip()
    if NUM.match(c):
        return c, c
    m = NOTE.match(c)
    if m:
        return m.group(1), m.group(2)
    sys.exit(f"schedule_j.py: unexpected totals cell at source line {line_no}: {c!r}")


def layout(rows):
    """rows: list of list of str. Pad each column to its widest entry, comma-separated."""
    last = len(rows[0]) - 1
    widths = [max(len(r[i]) for r in rows) + (1 if i < last else 0) for i in range(len(rows[0]))]
    out = []
    for r in rows:
        parts = [(r[i] + ("," if i < last else "")).ljust(widths[i]) for i in range(len(r))]
        out.append(" ".join(parts).rstrip())
    return out


def name(key, what):
    return f"`Schedule J ({key} version), {what}`"


out = []
w = out.append
w("IMPORT prelude")
w("IMPORT `nii-il04-nouns`")
w("")
w("-- National Insurance Law, Schedule J (לוח י׳): THE TWO TABLES, AS DATA.")
w("--")
w("-- GENERATED by tools/schedule_j.py from the deposited source; do not edit by hand. Edit the")
w("-- generator and run it again (python3 -I tools/schedule_j.py SOURCE nii-schedule-j-tables.l4),")
w("-- then tools/srcquote.py over the result. Each row's `src:` line is the source row it was read")
w("-- from; a reviewer checks a row by reading the two lines one above the other, EXCEPT the ten rows")
w("-- marked CORRECTED 2026-11-09 (six in the permanent table, four in the temporary one): in those")
w("-- the consolidation prints a wrong figure in the cells named in the comment, and the figure the")
w("-- row encodes is the OFFICIAL one, read from the amending instrument's page (the `ext:` lines")
w("-- under the first heading). Those rows carry no `src:` line: the consolidation's line is quoted as a plain")
w("-- comment that begins \"consolidation prints (its error, revision 2763716):\".")
w("--")
w("-- Figures are percentages as printed (1.40 means 1.40%). A cell printed \"–\" is NOTHING.")
w("-- Item 4 and the totals row carry the editors' note \"(הוראת שעה בשנים 2024 עד 2027: …)\" in some")
w("-- cells; for each such row the generator emits the row as printed AND the row as read in")
w("-- 2024-2027, with the noted figure in place of the printed one. Which rows apply in which year")
w("-- is decided in nii-schedule-j.l4, not here.")
w("")
w("§ `Schedule J — the two tables, as printed`")
w("--@SRC 4709-4711")
w("")
w("-- CORRECTED 2026-11-09: SEVEN cells of the consolidation's permanent table, four of them also in its")
w("-- temporary table, are not what the official text prints (NOTES.md, \"Correction 2026-11-09\"). They")
w("-- entered the consolidation together, in Hebrew Wikisource revision 2763716 (2023-05-31), which")
w("-- updated the table from the expired 2014 and 2009 texts and left cells behind. The official text of")
w("-- each cell is below, transcribed by hand from the page image of the instrument (not checked")
w("-- mechanically against any file). The instruments are deposited in ../../registers/source-bundle/")
w("-- amending-laws/: 18_lsr_301505-pp755-756-extract.pdf is Sefer HaChukim 2382,")
w("-- 16_lsr_299994-pp809-814-819-824-extract.pdf is 2023, 18_lsr_301061-pp250-257-259-extract.pdf is 2203,")
w("-- 19_lsr_301628-p266-extract.pdf is 2429 (each with a SOURCES.json entry):")
for ln in EXT_BLOCK:
    w(ln)
w("-- Where the consolidation's figures come from: the interim text of 1 August 2009 to 31 March 2011 and the")
w("-- temporary text for 2014, both expired:")
for ln in EXT_BLOCK_WRONG:
    w(ln)
w("")
for key, title, label, head, first, total, _ in TABLES:
    w(f"§§ `Schedule J, {title}`")
    w(f"--@SRC {label - 1}-{label}")
    w(f"--@SRC {head}-{head + 3}")
    w("")
    printed_rows, read_rows, names = [], [], []
    for n in range(first, first + 10):
        cs = cells(n)
        if len(cs) != 11:
            sys.exit(f"schedule_j.py: source line {n} has {len(cs)} cells, expected 11")
        item = cs[0].strip().rstrip(".")
        branch = BRANCH.get(cs[1].strip())
        if branch is None:
            sys.exit(f"schedule_j.py: unknown branch at source line {n}: {cs[1]!r}")
        pr, rd = zip(*(parse_cell(c, n) for c in cs[2:]))
        pr, rd = list(pr), list(rd)
        for idx, wrong, right, tag in CORRECTIONS.get((key, item), []):
            if pr[idx] == f"JUST {right}":
                print(f"schedule_j.py: source line {n}: the consolidation already prints {right}; the correction for item {item} can be deleted from CORRECTIONS")
            elif pr[idx] != f"JUST {wrong}":
                sys.exit(f"schedule_j.py: source line {n}, item {item}: expected the consolidation's {wrong} (or the official {right}), found {pr[idx]!r}")
            pr[idx] = rd[idx] = f"JUST {right}"
        printed_rows.append((n, item, [item, branch] + list(pr)))
        if pr != rd:
            read_rows.append((n, item, [item, branch] + list(rd)))
    body = layout([r for _, _, r in printed_rows] + [r for _, _, r in read_rows])
    k = 0
    w(f"--          {RULER}")
    for n, item, _ in printed_rows:
        nm = name(key, f"item {item}")
        names.append(nm)
        w(f"@ref National Insurance Law, Schedule J ({title}), item {item} (source line {n})")
        fixes = CORRECTIONS.get((key, item), [])
        for idx, wrong, right, tag in fixes:
            w(f"-- CORRECTED 2026-11-09: the consolidation prints {wrong} in {COLNAME[idx]} (quoted next, as a plain comment, not as a source line); that is its error.")
            w(f"-- The official text prints {right} there (ext:[{tag}] above), and {right} is what this row encodes.")
        w(f"--@CONS {n}" if fixes else f"--@SRC {n}")
        w(f"{nm} MEANS `A row of Schedule J` OF {body[k]}")
        k += 1
        w("")
    w(f"-- The same items with the figure the editors note for 2024-2027 in place of the printed one.")
    noted = {}
    for n, item, _ in read_rows:
        nm = name(key, f"item {item}, with the figures noted for 2024-2027")
        noted[item] = nm
        w(f"@ref National Insurance Law, Schedule J ({title}), item {item}, editorial note \"(הוראת שעה בשנים 2024 עד 2027: …)\" (source line {n})")
        w(f"--@SRC {n}")
        w(f"{nm} MEANS `A row of Schedule J` OF {body[k]}")
        k += 1
        w("")
    w(f"@ref National Insurance Law, Schedule J ({title}), items 1-10 (source lines {first}-{first + 9})")
    w("GIVETH A LIST OF `A row of Schedule J`")
    w(f"{name(key, 'items as printed')} MEANS")
    w("    LIST " + ("\n       , ".join(names)))
    w("")
    w(f"@ref National Insurance Law, Schedule J ({title}), items 1-10, with the editorial notes for 2024-2027 (source lines {first}-{first + 9})")
    w("GIVETH A LIST OF `A row of Schedule J`")
    w(f"{name(key, 'items as read in 2024-2027')} MEANS")
    sel = [noted.get(nm.split("item ")[1].rstrip("`"), nm) for nm in names]
    w("    LIST " + ("\n       , ".join(sel)))
    w("")
    tc = cells(total)
    if len(tc) != 11 or tc[1].strip() != "סך הכל":
        sys.exit(f"schedule_j.py: source line {total} is not the totals row")
    tp, tr = zip(*(parse_total(c, total) for c in tc[2:]))
    tl = layout([list(tp), list(tr)])
    w(f"--          C above: employee, self-employed, neither; C not above: employee, self-employed, neither; D upper, D not above; E")
    w(f"@ref National Insurance Law, Schedule J ({title}), totals row (source line {total})")
    w(f"--@SRC {total}")
    w(f"{name(key, 'totals as printed')}           MEANS `The totals row of Schedule J` OF {tl[0]}")
    w(f"@ref National Insurance Law, Schedule J ({title}), totals row, editorial notes for 2024-2027 (source line {total})")
    w(f"{name(key, 'totals as read in 2024-2027')} MEANS `The totals row of Schedule J` OF {tl[1]}")
    w("")

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"schedule_j.py: wrote {OUT}")
