# PROGRESS: piece ei4 (Act Parts VI to VIII.3), final state

Written by the piece agent `ei4` (Sonnet 5.5) on 2026-10-24. This describes the folder as it is now.

## Where things are

- Brief: the piece folder's `BRIEF.md` (two levels above this folder). Inputs: the piece folder's `inputs/`. My ranges: lines 1804-2108 and 2689-2762 of `S.C.-1996-c.-23.txt`.
- Binary: the stable `l4` 1.6.98 (sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`).
- Check: `L4=<that binary> L4_TARGET=unstable ./check.sh` in this folder; and `python3 -I srcrefs.py check --refs ../../../../../registers/source-bundle/S.C.-1996-c.-23.txt ei4-*.l4`.

## What is done

Every part of the range is encoded and tested; nothing is pending.
Every module's quote lines are already expanded (each is a verbatim slice of the raw file, checked by `srcrefs.py`).

| file | covers | assertions satisfied |
| --- | --- | --- |
| `ei4-part-vi-review.l4`, `ei4-tests-part-vi-review.l4` | ss 111 to 115, 116 to 123 (repealed) | 43 |
| `ei4-part-vi-investigation-and-proof.l4`, `ei4-tests-part-vi-investigation-and-proof.l4` | ss 124, 125 | 81 |
| `ei4-part-vi-certificates-and-inspections.l4`, `ei4-tests-part-vi-certificates-and-inspections.l4` | s 126, ss 127, 128 (repealed) | 119 |
| `ei4-part-vi-proceedings-and-evidence.l4`, `ei4-tests-part-vi-proceedings-and-evidence.l4` | ss 129 to 134 | 59 |
| `ei4-part-vi-offences-and-sin.l4`, `ei4-tests-part-vi-offences-and-sin.l4` | ss 135 to 143 | 59 |
| `ei4-part-vii-benefit-repayment.l4`, `ei4-tests-part-vii-benefit-repayment.l4` | ss 144 to 152 | 94 |
| `ei4-parts-viii-viii3.l4`, `ei4-tests-parts-viii-viii3.l4` | ss 153 to 153.4 | 48 |
| `ei4-seat.l4`, `ei4-cases-seat.l4` | layer 2: 76 questions, each with at least one case | 160 |

Total 663 assertions satisfied, none failed, none refused, none expected to fail; `NOTES.md` and this file complete the 18 files.
The coverage table has 167 rows over the 48 sections the index assigns to this piece, plus the Part and division headings; every non-blank raw line of the ranges lies inside a row.

## Decisions taken (each licensed by the section named in NOTES.md)

- No DEONTIC rule: a DEONTIC cannot be compared in an `#ASSERT`, and the seat form needs plain answers. A duty is a BOOLEAN, with a DATE rule where the text sets a time; a power or permission is a BOOLEAN whose FALSE means "this section does not give it".
- A fact decided outside the range is a plain input marked `out of range`; a judgment the text hands to the Commission, a judge or the Minister is a BOOLEAN input named for that satisfaction.
- Day counting follows the keel's fork F4; Part VII does not round; the maximum yearly insurable earnings and the Income Tax Act figures are inputs.
- The one code fix the tests forced: `NOT (a) OR b` on one line reads as `NOT (a OR b)`, so s 137's limits needed `((NOT (a)) OR b)`.
- A correction for the keel: Part VI has no definition of "overpayment of benefits" (see "Needs from the core" in NOTES.md).

## For the lead

The forks are F-ei4-1 to F-ei4-17 in NOTES.md; the inputs to wire at the merge are in "Cross-references out of my ranges" (31 rows).
