# Interpretation (Jersey) Law 1954 in L4: the `legalese-2026-10` row

This row encodes the Interpretation (Jersey) Law 1954 (L.17/1954), Articles 1 to 18 and the Schedule, in all seven consolidated texts on jerseylaw.je (1 January 2019 to the present), from the seat of the reader of an enactment.
It is a draft written for the `unstable` build of `l4`; no `main` build has read it, and no domain expert has read it against the Law.
Read `NOTES.md` first: it opens with the places where the text did not say what the brief said, and carries the coverage table, the vintage table, the six forks, what the Law does not say, and the output of `check.sh`.

## Running the check

```
L4=/path/to/l4 ./check.sh
```

It needs the prerelease `unstable-20261026-6325439` (sha256 in `encoding.json`; `check.sh` compares it).
It leaves `JL4_LIBRARY_PATH` unset, runs each module under `nice`, one after another, prints the errors, satisfied, failed, refused and warning counts of every module, and exits 0 only if every count is as expected and `srcrefs.py check --refs` finds no problem.
The last full run, on 2026-10-28, is GREEN: 29 modules, 1228 assertions satisfied, none failed, refused or warned, and 599 quotation lines with 0 problems.
The source texts are expected at `../../source/` (the `.txt` files named in `encoding.json`); set `RAW` to the current text if they are elsewhere.

## The modules, in dependency order

| Module | What it holds |
|---|---|
| `je54-nouns.l4` | the types only (`DECLARE`), imported by all the others |
| `je54-vintage.l4` | which text of the Law was in force on a day; the Law's own days; Article 18 |
| `je54-art01-commencement.l4` | Article 1: enactment, passing, commencement, promulgation; the V1 rules of Articles 1(2), 1(5), 1(6) |
| `je54-schedule-definitions.l4` | Article 4 and the Schedule: the defined words, "means" against "includes", Part 2, midnight and month |
| `je54-gaps.l4` | what the Law does not say, as questions that refuse |
| `je54-art01-by-date.l4` | Article 1 asked with dates, on the three readings of fork I1 |
| `je54-art02-05-words.l4` | Articles 2, 3 and 5: gender and number, bodies corporate, commonly used names |
| `je54-art07-service-by-post.l4` | Article 7: service by post |
| `je54-art08-bankruptcy.l4` | Article 8: a person becoming bankrupt, limb by limb and text by text |
| `je54-art09-10-references.l4` | Articles 9 and 10: references by number, to enactments, subordinate enactments |
| `je54-art11-powers.l4` | Articles 11 and 11A: powers and duties, appointing to an office; Articles 11(3) and 11(4) as V1 has them |
| `je54-art12-15-penalties-forms.l4` | Articles 12 to 15: offences, penalties, forms, distance |
| `je54-v1-arts-6-16-17.l4` | Articles 6, 16 and 17 as V1 has them; refusals for the later texts |
| `je54-seat.l4` | the exported questions, Articles 1 to 8 and the Schedule |
| `je54-seat-powers-and-penalties.l4` | the exported questions, Articles 6 and 9 to 17 |

Every module except `je54-nouns.l4` and `je54-seat-powers-and-penalties.l4` has a tests module beside it, `je54-tests-<same name>.l4`, with expected values written by hand from the source; `je54-tests-seat.l4` covers both seat modules.
`je54-tests-crosschecks.l4` applies the Law to commencement dates of the Charities (Jersey) Law 2014; it tests the Law's reading of instruments it does not contain and is kept apart for that reason.

## Other files

- `BRIEF.md`: the specification this row was written to.
- `srcrefs.py`: the checker for the quotation lines (`-- src:N | text`) and the `@ref` locators.
- `SOURCE-LICENSE.md`: the terms of the quoted text.
- `encoding.json`: the facts about this encoding.
- `tools/extract_law.py`: how the `.txt` sources were made from the pages.
