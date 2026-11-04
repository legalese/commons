# PROGRESS -- part ssc5 (lines 2444-3094 of ukpga-1992-4.txt: Parts VI to X, ss 112-150)

Working log. After any compaction re-read this file, NOTES.md and the text, not a summary.
Status as of the last full run (after the 2026-11-04 independent-review triage): all layer 1, tests, seat and cases written; `check.sh` exits 0 (15 modules, 1038 assertions satisfied, 0 failed, 0 refused, main build identical); `srcrefs.py check --refs` and `--strict` report 0 problems; NOTES.md assembled, with a section "Changes after the independent review (ssc5)".

## Tooling (outside the deposit, in ../../../work/ i.e. runs/iaw-ssc5/work/)

- `work/src/*.l4` are TEMPLATES. A line `@@ref LABEL | N M` expands (work/expand.py) to the verbatim `-- src:` quote lines of raw lines N..M plus `@ref LABEL (src:N-M)`.
  Edit templates, never the expanded files in the deposit. `work/final.sh` expands, runs both srcrefs gates, runs `check.sh` against the stable and main binaries into `work/check-final.txt`, and rebuilds NOTES.md.
- `work/t.sh FILE` runs one file on the stable binary and prints satisfied / failed / errors / warnings.
- `work/units.py` splits the range into units (every non-blank line of 2444-3094 is a unit start); `work/cov.txt` assigns dispositions by line range; `work/mkcov.py` (modes `table`, `audit`, `jural`) builds the coverage table, the audit counts and the jural table; `work/mkmarg.py` (modes `a`, `b`, `c`) builds the marginal-readings tables from the FALSE-kind and NOTHING-kind comments.
- NOTES.md is assembled by `work/mknotes.py` from `work/notes_head.md`, `notes_forks.md`, `notes_seams.md`, `notes_findings.md`, `notes_binary.md` and the generated tables; edit the fragment, not NOTES.md.
- `work/gen122.py` generated the 62 s 122(1) definition records once (output pasted into the part 6 template; not re-run). `work/genseat.py` and `work/gencases.py` write the seat and case templates.
- Binary: `scratchpad/bin/l4-stable-98` (stable 1.6.98); main-build comparison via check.sh with L4_MAIN (`l4-main-108`). Both are the lead's; do not delete them.

## Decisions taken (decision procedure applied uniformly; NOTES.md has the register)

- P1 "X if C1..Cn" (entitlement or status): all hold -> JUST TRUE; a failed "if" -> JUST FALSE (reading (a), marginal). It does not extend to a computation rule such as s 143(3) (a day of absence is disregarded if ...), which answers NOTHING when the "if" fails.
- P2 "any person who C1..Cn shall be entitled" (relative clause): all hold -> JUST TRUE; else NOTHING (limited by its own wording, reading (b), marginal).
- P3 flat negative "No person shall be entitled ... [unless C]": the triggering case -> JUST FALSE. A function named for the bar's own condition (`s 134(1) ... barred ... by capital`, `s 134(2)`, `s 140A(2)`/(3) "as far as ... goes", `s 146`) tests it and answers both ways; a function named for an effect other provisions can also bring about (`s 113(1) ... disqualified`, `s 134(4) ... not payable`) answers JUST TRUE where the text says so and NOTHING otherwise. An "unless"/"except" triggered against a requirement or deeming (ss 143(2), 139(5), 122(1), 137(1)) -> JUST FALSE. A grant limited to a stated period or "while" a state lasts (ss 113(1), 116(1), 127(b), 145A(1)) -> NOTHING outside it (reading (b)).
- P4 "means" definition: match -> TRUE, no match -> JUST FALSE. "is"/"are"/"includes": match -> TRUE, otherwise NOTHING. "That is to say" (s 139(1)) and "shall be taken to consist of" (s 116(3)) are read as "means" (marginal reading (c)).
- P5 a power to make regulations/orders: inert (2, machinery), except where the section states its own limit or default (s 122(6B), s 140(4ZA), s 148(3)(b)), or another part's seam needs a function (ss 117, 119, 120).
- P6 an opening conditional gives NOTHING when its scene is absent. P7 prescribed figures are inputs; figures the Act states are written in the code with the line quoted. P8 a judgment handed to someone else is a plain input.
- Eight forks, F1 to F8, in NOTES.md (Fork register). Changes made in the closing pass: s 148(3)(b) now answers JUST 10 for an order naming exactly 10 (fork F5); the K2 input in s 124(1A) is named `s 173(a) the person is under 5` as the plan names it; K3 comments were added to parts 6, 7, 8 and 10; line 2714 is labelled as the paragraph substituted for s 124(1)(c); the s 144 heading is inert 1, not blank.
- Lettered limbs of ss 122(1), 137(1), 145A(5), 150(2) lost their labels in the text; they are cited by their first words and line numbers.

## Status

- [x] ssc5-logic (+ tests-logic 32), part6 (+ tests 249), part7 (+ tests 220), part8 (+ tests 155), part9 (+ tests 134), part10 (+ tests 102)
- [x] seat (51 questions) + seat cases (146)
- [x] cov.txt complete (651 units, 651 rows), NOTES.md assembled
- [x] check.sh and srcrefs (--refs and --strict) clean on the full set

## Files written (all in DEPOSIT)

ssc5-logic.l4, ssc5-part6.l4 ... ssc5-part10.l4, ssc5-tests-logic.l4, ssc5-tests-part6.l4 ... ssc5-tests-part10.l4, ssc5-seat.l4, ssc5-cases-seat.l4, NOTES.md, PROGRESS.md.
No NEEDS-CORE.md.
