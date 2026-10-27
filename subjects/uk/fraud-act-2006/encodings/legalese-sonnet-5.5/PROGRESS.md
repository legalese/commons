# PROGRESS (porridge-uk-fraud-b, Fraud Act 2006, legalese-sonnet-5.5)

Re-read this file, NOTES.md and the text (`../../registers/source-bundle/ukpga-2006-35.txt`) after any compaction, not a summary.

## How I work (so a resumed session can continue)

- Scratch dir (outside the deposit): `<scratchpad>/fraud-b-work/` holds `env.sh` (paths), `expand.py` (expands `--@Q N [M]` marker lines in `tpl/*.l4` into `-- src:N | text` quote lines by calling `srcrefs.py quote` on the raw text), and `build.sh MODULE...` (expand a template into the deposit folder, run it, print diagnostics).
- The DEPOSIT `.l4` files are the expanded output.  Edit the template in `tpl/`, then run `build.sh`; do not hand-edit the deposit copy.
- Gate commands (run from the deposit folder): `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` and `python3 -I srcrefs.py check --refs <raw text> fraud-*.l4` (must report 0 problems).
- Binary: L4_BIN 1.6.98 (main, 7689b0d), sha256 82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e, verified.

## Status (final)

DONE.  All units below are written and pass `check.sh` (17 files, 0 errors, 343 assertions satisfied, 0 failed, 0 refused) and `srcrefs check` (196 src: lines, 40 runs, 96 locators, 0 problems).

Layer 1 (objective, isomorphic):
- `fraud-nouns.l4` nouns only
- `fraud-dates.l4` YMD shim, date of enactment (src:4), 2 May 2022 (src:344)
- `fraud-s15.l4` s 15(1) in force on a day appointed (input), s 15(2) extent, s 15(3)
- `fraud-penalty.l4` the penalty shape shared by ss 1(3), 6(2), 7(2), 9(6), 11(3); NI reading of ss 1(4), 6(3), 7(3), 9(7), 11(4); Sch 2 para 1
- `fraud-s01-s05.l4` ss 1 to 5
- `fraud-s06-s08.l4` ss 6 to 8
- `fraud-s09.l4` s 9 (s 9(4) and s 10 blank, quoted at foot)
- `fraud-s11.l4` s 11
- `fraud-s12-s13.l4` ss 12, 13
- `fraud-sch2.l4` Sch 2 paras 3 to 11 (para 1 is in fraud-penalty, para 2 inert)

Tests: `fraud-tests-s01-s05.l4` (71), `fraud-tests-s06-s09.l4` (37), `fraud-tests-s11-s13.l4` (53), `fraud-tests-sch2.l4` (30), `fraud-tests-penalty-s15.l4` (43).

Layer 2 (seat): `fraud-seat.l4` (17 exported questions), `fraud-cases-seat.l4` (109 assertions, at least one per question, plus asserted not-covered values).

Documents: `NOTES.md` (seat, jural relations, coverage table of 31 rows with no `deferred`, fork register F1 to F20, findings 1 to 20, what the stable binary does not accept, the check.sh output, what is owed), `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.

Positive control done in scratch: two deliberately false assertions appended to a copy of the seat cases were counted as failed 2.

Nothing was added to git, committed or pushed.

## Decisions taken (with the text that licenses each)

- Offences are BOOLEAN predicates over fact records ("elements made out"), not deontics (phrasebook 5.7): the Act states liability, not a duty to do or omit something.
- Penalty is a ceiling: `MAYBE Penalty`, NOTHING when s 15(2) says the sections do not extend to the place (Scotland, anywhere else).
- Reading of ss 1(4)/6(3)/7(3)/9(7)/11(4): Northern Ireland = six months (fork F2).
- Sch 2 para 1: "before 2 May 2022" strict; 2 May 2022 itself is not before.
- s 11(2)(c) "but intends" qualifies both (i) and (ii) (fork F6).
- s 2(5) "may be regarded as made" read as counting (fork F8).
- s 2(2)(b): awareness that it might be untrue or misleading suffices (fork F7).
- s 6(1): no mental element added (fork F9).
- s 9: who is within the reach of s 993 CA 2006 and "fraudulent purpose" are asked as facts (Companies Act not among sources).
- Dishonesty is a bare input (fork F1).
- Sch 2 paras 4 to 10 encoded in layer 1 only (not asked in the seat): the saved provisions are in other Acts.

The fork numbers F1 to F20 in the comments of the `.l4` files refer to the fork register in `NOTES.md`; the finding numbers refer to its findings.

## Files written

BRIEF.md (copy), check.sh, srcrefs.py (given), PROGRESS.md, NOTES.md, encoding.json, SOURCE-LICENSE.md, and the 17 .l4 files listed above.
