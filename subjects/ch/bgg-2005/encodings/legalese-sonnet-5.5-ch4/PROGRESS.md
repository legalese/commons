# PROGRESS: BGG chapter 4 (Art 90 to 112), run dst-bgg4

Re-read this file, NOTES.md and the text after any compaction, not a summary.
The numbers are in NOTES.md ("What check.sh prints"), which a script writes; this file keeps no counts, so it cannot disagree with them.

Paths: RUN = <scratchpad>/runs/dst-bgg4
Deposit folder = RUN/deposit/encodings/legalese-sonnet-5.5-ch4 (all .l4 flat, bgg4-*.l4 mine, bgg3-*.l4 READ-ONLY).
Scratch (not deposited) = RUN/work: source templates `src/*.l4.t`, `build.py`, `mkseat.py`, `mknotes.py`, `notes_body.py`, `notes_findings.py`.
Binaries: L4 = <scratchpad>/bin/l4-main-110 (1.6.110) ; L4_MAIN = <scratchpad>/bin/l4-main-109 (1.6.109).
Do NOT call the advisor tool (brief forbids), no web, no subagents, do not read other runs, do not git add/commit.

## Status (all done on 2026-11-18)

- [x] bgg4-nouns
- [x] bgg4-appealable (Art 90-94) + tests
- [x] bgg4-grounds (Art 95-98) + tests
- [x] bgg4-new-submissions (Art 99) + tests
- [x] bgg4-time-limit (Art 100-101) + tests
- [x] bgg4-procedure (Art 102-107) + tests
- [x] bgg4-simplified (Art 108-109) + tests
- [x] bgg4-cantonal (Art 110-112) + tests
- [x] bgg4-seams + tests
- [x] bgg4-seat, bgg4-cases-seat
- [x] coverage.py, quotecheck.py, check.sh, srcrefs.py (0 problems)
- [x] NOTES.md, encoding.json, SOURCE-LICENSE.md

## Decisions taken (with what licenses each)

- D1. The brief says chapter 3 defines an appeal-kind type; it defines none (the DECLAREs of bgg3-nouns are listed in NOTES.md, finding 1), so bgg4-nouns defines `Kind of appeal` once.
- D2. Conventions copied from chapter 3: MAYBE BOOLEAN answers; names `Art 74(1) ...`; a failed "wenn" in a limb is JUST FALSE (reading (a), listed for a lawyer); a grant or power whose gate failed is NOTHING (ruling 2026-11-12); a bare duty of the cantons not done is NOTHING (chapter 3's F5, here F27); regulative rules are run with #TRACE and the same duty is also a decision function.
- D3. Day counting: the day after the notification is day 1 (F9); the days that rules outside the text leave out of the count are an input (F10).
- D4. The seams to chapter 3 are in layer 1 (bgg4-seams.l4); layer 2 only calls them.
- D5. E1 option C: the record of "may I appeal, and by when?" gives one answer per section (F28); option B only by hand, in the Art 90 to 93 composite (F4).
- D6. Seat polarity (independent reader, 2026-11-18): only the `@export` wording of the Art 109(1) seat question was changed, to the meaning its function has (the one condition the person's kind of appeal turns on is absent), and a two-line note was put above it saying what `JUST TRUE` and `NOTHING` mean there.
  At that edit the DECIDE name, every input and every case were unchanged, so no answer changed (D7 later changed this question's inputs and cases).
  The wording and the note are in the `q(...)` call for that question in `RUN/work/mkseat.py` (its `extra=` argument), so regenerating the seat file keeps them; NOTES.md has a section "Seat polarity (independent reader)" with the old and the new wording.
  The team lead's NOTES.md section "What the traces don't tell you" is not generated from findings: `notes_body.py` copies it from `RUN/work/lead_traces_section.md`, so `mknotes.py` puts it back unchanged.
- D7. Blind-test repairs (2026-11-18): Art 74 is derived in `bgg4-seams.l4` for the civil appeal and seven inputs were appended to the Art 109(1) seat question (fork F32; fork F26 now lists what is still not derived); `Art 107(3) the Court is bound by the period of 15 days` answers JUST TRUE where the exception of the second sentence is not made out (F34); `Art 107(1)` is a bar with no input and answers JUST FALSE (F33).
  The value limit as a field of the three records was not added (NOTES, "What the text does not answer").
  Every expected value that changed, with old and new, is in NOTES.md under "Independent reader (blind test), repairs"; no DECIDE name changed.
  The edits are in the templates `RUN/work/src/bgg4-seams.l4.t`, `bgg4-procedure.l4.t`, `bgg4-tests-seams.l4.t` and `bgg4-tests-procedure.l4.t`, and in `mkseat.py`, `seatdesc.py` and `coverage_data.py`, so a rebuild keeps them.

## How to rebuild (every command in the foreground)

1. `python3 RUN/work/build.py` expands the `@@Q n m@@` quote lines and `@@REF text@@` locators of the templates from the text file.
2. `DEP=<deposit folder> python3 RUN/work/mkseat.py` writes bgg4-seat.l4 and bgg4-cases-seat.l4 from the layer-1 signatures.
3. `L4=<l4 1.6.110> L4_MAIN=<l4 1.6.109> ./check.sh > RUN/work/check-out.txt` in the deposit folder.
4. `python3 -I srcrefs.py check --refs <text file> bgg4-*.l4`, `python3 -I quotecheck.py <text file>,<chapter 3 text file> bgg4-*.l4`, `python3 -I coverage.py <text file>`.
5. `L4=... L4_MAIN=... ./traces.sh <file>` per test file, and `L4=... python3 -I tracetable.py` for the table of traces.
6. `RUN=... DEP=... L4=... L4_MAIN=... python3 RUN/work/mknotes.py` writes NOTES.md and encoding.json (it stops with a list of problems if a count or a finding no longer holds).

## Files written

The `bgg4-*.l4` modules, tests and seat files; `check.sh`, `fetch-main-l4.sh` and `srcrefs.py` (given); `coverage.py`, `coverage_rows.py`, `coverage_data.py`, `quotecheck.py`, `traces.sh`, `tracetable.py`; `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md` (a copy), this file.
