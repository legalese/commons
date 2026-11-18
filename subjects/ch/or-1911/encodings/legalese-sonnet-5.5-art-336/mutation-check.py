#!/usr/bin/env python3
"""Mutation check: break one thing at a time in a COPY of the encoding and see whether the checks go red.
A mutant that leaves every module green is a gap in the tests, and is recorded in NOTES.md.
Usage:  L4=/path/to/l4 python3 -I mutation-check.py   (about two minutes)
Each mutant is one edit to one line of a layer-1 module, in a temporary copy of
this folder; the real files are never touched. A mutant is KILLED when some
module then shows an error diagnostic or a refused assertion, or a trace
disagrees with its EXPECT comment. A line number that no longer holds the
pattern is reported as SKIP (the module changed since this script was written)."""
import os, shutil, subprocess, pathlib, re, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE
L4 = os.environ["L4"]
WORK = pathlib.Path(tempfile.mkdtemp(prefix="or336-mut-")) / "copy"

# (file, line number (1-based), old substring on that line, new substring, label)
M = [
 ("or336-art336.l4", 46, "IF NOT (facts's", "IF (facts's", "1(a): drop the 'because' test"),
 ("or336-art336.l4", 49, " OR facts's", " AND facts's", "1(a): exceptions need both, not either"),
 ("or336-art336.l4", 68, " OR facts's", " AND facts's", "1(b): exceptions need both, not either"),
 ("or336-art336.l4", 86, "IF NOT (facts's", "IF (facts's", "1(c): 'ausschliesslich' dropped"),
 ("or336-art336.l4", 104, "IF NOT (facts's", "IF (facts's", "1(d): good faith ignored"),
 ("or336-art336.l4", 124, " AND NOT (", " AND (", "1(e): voluntary assumption reversed"),
 ("or336-art336.l4", 172, "EQUALS Employee", "EQUALS Employer", "2(a): wrong party"),
 ("or336-art336.l4", 199, "EQUALS Employee", "EQUALS Employer", "2(b): wrong party"),
 ("or336-art336.l4", 228, "EQUALS Employee", "EQUALS Employer", "2(c): wrong party"),
 ("or336-art336.l4", 257, "EQUALS Employee", "EQUALS Employer", "2: wrong party"),
 ("or336-art336.l4", 203, "IF NOT (`the employee", "IF (`the employee", "2(b): protection test reversed"),
 ("or336-art336.l4", 214, "OR  `Art 336(3)", "AND `Art 336(3)", "2(b): 336(3) required as well as the status"),
 ("or336-art336.l4", 284, "AT MOST", "LESS THAN", "3: last day exclusive"),
 ("or336-art336.l4", 282, "IF NOT (facts's", "IF (facts's", "3: transfer test reversed"),
 ("or336-art336.l4", 232, "IF NOT (facts's", "IF (facts's", "2(c): mass dismissal test reversed"),
 ("or336-art336a.l4", 80, "6 TIMES", "5 TIMES", "336a(2): five months"),
 ("or336-art336a.l4", 115, "2 TIMES", "3 TIMES", "336a(3): three months"),
 ("or336-art336a.l4", 77, "LESS THAN 0", "LESS THAN 1", "336a(2): a wage of 0 refused"),
 ("or336-art336a.l4", 112, "LESS THAN 0", "AT MOST 0", "336a(3): a wage of 0 refused"),
 ("or336-art336a.l4", 141, "IF two AT MOST six", "IF two AT LEAST six", "336a: the higher ceiling governs"),
 ("or336-art336a.l4", 160, "AT MOST cap", "LESS THAN cap", "336a: cap exclusive"),
 ("or336-art336a.l4", 95, "THEN JUST FALSE", "THEN JUST TRUE", "336a(2): damages reserved reversed"),
 ("or336-art336b.l4", 63, "GREATER THAN", "AT LEAST", "336b(1): the last day exclusive"),
 ("or336-art336b.l4", 54, "IF NOT (objection's", "IF (objection's", "336b(1): writing test reversed"),
 ("or336-art336b.l4", 60, "IF NOT (objection's", "IF (objection's", "336b(1): to-the-giver test reversed"),
 ("or336-art336b.l4", 120, "PLUS 180", "PLUS 179", "336b(2): 179 days"),
 ("or336-art336b.l4", 140, "AT MOST", "LESS THAN", "336b(2): no action, last day exclusive"),
 ("or336-art336b.l4", 150, "AT MOST", "LESS THAN", "336b(2): action on the last day is late"),
 ("or336-art336b.l4", 167, "WITHIN 180", "WITHIN 179", "336b(2) regulative: 179 days"),
 ("or336-art336b.l4", 83, "WITHIN `the days", "WITHIN 1 PLUS `the days", "336b(1) regulative: one day extra"),
]

# Mutants in the employer's seat, in the questions for the employer as the party that RECEIVED the notice
# (21 to 25). (file, text of a line in the question, text to replace on the first later line that holds it, replacement, label).
SEAT_M = [
 ("or336-seat-employer.l4", "DECIDE `As the employer, can I assert my claim for compensation", "`my employee and I agreed on continuing the employment`", "FALSE", "21: agreement ignored"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, can I assert my claim for compensation", "IS `the day I made my objection`", "IS `the last day of my employee's notice period`", "21: day made and last day swapped"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, is my objection to my employee's notice valid", "IS `the day I made my objection`", "IS `the last day of my employee's notice period`", "22: day made and last day swapped"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, is my objection to my employee's notice valid", "`the objection was directed against the notice` IS `my objection was directed against my employee's notice`", "`the objection was directed against the notice` IS TRUE", "22: against-the-notice fixed TRUE"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, is my objection to my employee's notice valid", "IS `my objection was made to my employee, who gave the notice`", "IS `my objection to my employee's notice was made in writing`", "22: to-the-giver taken from the writing input"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, what is the last day I can object", "`Art 336b(1) the last day to object`", "`Art 336b(2) the last day to bring the action`", "23: wrong rule (the 180-day day)"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, what is the last day I can bring my action", "`Art 336b(2) the last day to bring the action`", "`Art 336b(1) the last day to object`", "24: wrong rule (the objection day)"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, has my claim been forfeited", "IS `I have brought an action`", "IS FALSE", "25: action brought fixed FALSE"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, has my claim been forfeited", "IS `the day I brought the action`", "IS `the day I am asking about`", "25: day brought taken from the day asked about"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, has my claim been forfeited", "IS `the day I am asking about`", "IS `the day the employment ended`", "25: day asked about taken from the end of the employment"),
 ("or336-seat-employer.l4", "DECIDE `As the employer, has my claim been forfeited", "`the day the employment ended` IS `the day the employment ended`", "`the day the employment ended` IS `the day I am asking about`", "25: end of the employment taken from the day asked about"),
]

def run_all(d):
    bad = []
    for f in sorted(d.glob("or336-*.l4")):
        p = subprocess.run([L4, "run", f.name], cwd=d, capture_output=True, text=True,
                           env={k: v for k, v in os.environ.items() if k != "JL4_LIBRARY_PATH"})
        out = p.stdout + p.stderr
        err = out.count("DiagnosticSeverity_Error")
        ref = len(re.findall(r"assertion refused", out))
        if err or ref:
            bad.append(f"{f.name}: errors={err} refused={ref}")
    t = subprocess.run([sys.executable, str(SRC / "check-traces.py"), str(d / "or336-traces.l4")],
                       capture_output=True, text=True, env={**os.environ, "L4_MAIN": ""})
    if t.returncode:
        bad.append("traces: " + t.stdout.strip().splitlines()[-1])
    return bad

survived = 0
tests_missed = 0
n_layer1 = n_seat = 0
for entry in M + SEAT_M:
    fn, ln, old, new, label = entry
    seat = entry in SEAT_M
    if WORK.exists():
        shutil.rmtree(WORK)
    shutil.copytree(SRC, WORK, ignore=shutil.ignore_patterns("*.md", "*.json", "__pycache__"))
    p = WORK / fn
    lines = p.read_text(encoding="utf-8").split("\n")
    if isinstance(ln, str):   # a seat mutant: the first line holding `old` after the line holding the anchor text
        anchor = next((k for k, l in enumerate(lines) if ln in l), None)
        j = None if anchor is None else next((k for k in range(anchor, len(lines)) if old in lines[k]), None)
    else:
        j = ln - 1
    if j is None or old not in lines[j]:
        print(f"SKIP  {fn}:{ln} {label}: pattern {old!r} not found where expected")
        continue
    lines[j] = lines[j].replace(old, new, 1)
    p.write_text("\n".join(lines), encoding="utf-8")
    bad = run_all(WORK)
    if seat:
        n_seat += 1
    else:
        n_layer1 += 1
    where = f"{fn}:{j + 1}"
    if bad:
        by_tests = any(b.startswith(("or336-tests", "traces")) for b in bad)
        by_cases = any(b.startswith("or336-cases") for b in bad)
        if seat:
            print(f"KILLED   {where} {label}  <- seat cases: {'yes' if by_cases else 'NO'}")
            if not by_cases:
                tests_missed += 1
        else:
            if not by_tests:
                tests_missed += 1
            print(f"KILLED   {where} {label}  <- layer-1 tests/traces: {'yes' if by_tests else 'NO'}; seat cases: {'yes' if by_cases else 'no'}")
    else:
        survived += 1
        print(f"SURVIVED {where} {label}")
shutil.rmtree(WORK.parent, ignore_errors=True)
print(f"{n_layer1 + n_seat} mutants ({n_layer1} in layer 1, {n_seat} in the employer's seat), {survived} survived every check, {tests_missed} were not caught by the checks meant to catch them (layer-1 mutants: the layer-1 tests and traces; seat mutants: the seat cases)")
