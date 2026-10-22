# PROGRESS (run porridge-uk-cda-b, Criminal Damage Act 1971, legalese-sonnet-5.5)

Re-read this file, NOTES.md and the text (../../registers/source-bundle/ukpga-1971-48.txt) after any compaction, not a summary.

## Modules (layer 1) and their dependency order

| module | covers |
|---|---|
| `cda-nouns.l4` | nouns only: Thing, Connection, Property facts, Damage, Belief, Lawful excuse facts, Offence, the three sets of facts for ss 1 to 3 |
| `cda-s10-interpretation.l4` | s 10(1) property, s 10(2) to (4) belonging, s 10(5) computers |
| `cda-s5-lawful-excuse.l4` | s 5(1) to (5) |
| `cda-s1-s3-offences.l4` | ss 1, 2, 3 |
| `cda-s4-punishment.l4` | s 4 (ceilings on indictment; summary not stated) |
| `cda-s6-s9-proceedings.l4` | s 6, s 7(2), s 9 |
| `cda-s11-s12-extent.l4` | s 12(1) commencement, s 11(1), s 11(11), s 12(3), (6) |
| `cda-fixtures.l4` | named example facts shared by the test modules (no rules, no assertions) |
| `cda-tests-*.l4` | definitions, lawful-excuse, offences, punishment, proceedings, extent |
| `cda-seat.l4`, `cda-cases-seat.l4` | layer 2: 27 questions and 80 worked cases |

## Status

- [x] sources read, skills read, binary checked (1.6.98, sha256 matches)
- [x] coverage table drafted and finalised in NOTES.md
- [x] nouns
- [x] layer-1 modules
- [x] layer-1 tests
- [x] seat + cases
- [x] srcrefs check, check.sh, NOTES.md, encoding.json, SOURCE-LICENSE.md
- [x] advisor review applied: check.sh output in NOTES.md and encoding.json re-captured from the final tree; stray files removed

## Decisions taken (with the text that licenses each)

All recorded as forks F1 to F15 in NOTES.md with readings and licence.
The structural ones:
- Section 5 applies by limb (s 5(1)): the Offence enum has a constructor per limb that s 5(1) or s 4 treats differently (fork F2).
- Co-owned property is "belonging to another" (s 10(2), fork F4).
- Every word of state of mind or judgment is a stated fact (fork F11).
- A rule outside its section's reach returns an explicit "says nothing" constructor, never FALSE (forks F8, F13).
- The commencement date is derived from the bracketed date under the long title (s 12(1), fork F7).

## Files written

BRIEF.md (copy), check.sh and srcrefs.py (copied from the skill's assets, unchanged), PROGRESS.md, NOTES.md, encoding.json, SOURCE-LICENSE.md, and the sixteen `cda-*.l4` files listed above.
A throwaway generator `zz-gen-cases.py` was used to write `cda-cases-seat.l4`; it was deleted at the end of the run (checked: it is not in this folder).
Two transient writes happened outside this folder and were removed: an empty `/tmp/dummy` from a command that hung, and a copy of `check.sh`'s output in the parent scratch folder used to build NOTES.md.
