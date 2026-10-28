# Legislation (Jersey) Law 2021 (L.8/2021) in L4: row `legalese-2026-10`

This row encodes the whole Legislation (Jersey) Law 2021 in the L4 language, from the seat of the reader of an enactment: someone who has to know when an enactment bound them, what it lets be done to them, and which text of an enactment they can rely on.
The Law says how Jersey legislation is made, when it comes into force, what repeal and expiry do, what a power to make subordinate legislation carries, how legislation is consolidated, revised and published, and which versions are official.
Both deposited texts are covered: the text in force from 28 September 2021 and the text in force from 11 January 2024.

Status: draft, not reviewed by a domain expert.
It is written for the `unstable` compiler (binary `unstable-20261026-6325439`); no `main` build has read it.
`NOTES.md` is the file to read first: what is encoded, the coverage table, the fork register, what the Law does not say, the answers to the headline questions, and the open questions.

## Run it

```
./check.sh
```

`check.sh` runs every `je21-*.l4` module (one at a time, `nice -n 15`), counts errors, warnings, assertions satisfied, failed and refused per module by reading the line after every `Message:`, checks every quotation and `@ref` locator against the source text with `srcrefs.py check --refs`, and exits 0 only when everything is green.
Set `L4=/path/to/l4` if the binary named at the top of `check.sh` is not there; set `RAW=` if the source text is not at `../../source/l_8_2021.current.txt`.
Leave `JL4_LIBRARY_PATH` unset.

Quotations in the modules are `-- src:N | text` lines (`src:l_8_2021_20240110:N` for the earlier text), written by `srcrefs.py quote` and never retyped.

## The modules, in dependency order

Rule modules (each imports `prelude`, `daydate` and `je21-nouns` unless noted):

1. `je21-nouns.l4`: the nouns, `DECLARE` only.
2. `je21-art01-definitions.l4`: Article 1 definitions.
3. `je21-art02-making.l4`: Article 2, how Jersey legislation is made (one function per text of 2(1)).
4. `je21-art03-commencement.l4`: Article 3, commencement. It imports only the nouns and is meant to be copied by hand into other encodings.
5. `je21-art04-08-effects.l4`: Articles 4 to 8 (imports `art02`).
6. `je21-art09-10-subordinate-powers.l4`: Articles 9 and 10 (imports `art02`).
7. `je21-art11-annulment.l4`: Article 11 (imports `art02`).
8. `je21-part3a-consolidation.l4`: Articles 12 to 14.
9. `je21-schedule1.l4`: Schedule 1 and Article 15(4) to (7).
10. `je21-art15-16-revision-publication.l4`: Article 15(8) and (9), Article 16.
11. `je21-art17-18-official-versions.l4`: Articles 17 and 18.
12. `je21-part4-office.l4`: Article 22 (imports `art01`).
13. `je21-art26-commencement.l4`: Article 26 and the endnotes' commencement and versions (imports `art03`).

The questions a reader asks, `@export`ed in the reader's words (63 of them):

14. `je21-seat-defaults.l4`: the default reading of each fork, used by the exported questions.
15. `je21-seat-1-making-and-commencement.l4`: the Law itself, what an instrument is, making, commencement.
16. `je21-seat-2-powers-and-effects.l4`: Articles 4 to 11.
17. `je21-seat-3-versions-and-publication.l4`: Articles 12 to 18 and 22, Schedule 1.

Tests, one module for each rule module and each seat module (923 assertions; expected values written by hand from the text):

`je21-tests-art01-definitions.l4`, `je21-tests-art02-making.l4`, `je21-tests-art03-commencement.l4`, `je21-tests-art04-08-effects.l4`, `je21-tests-art09-10-subordinate-powers.l4`, `je21-tests-art11-annulment.l4`, `je21-tests-part3a-consolidation.l4`, `je21-tests-schedule1.l4`, `je21-tests-art15-16-revision-publication.l4`, `je21-tests-art17-18-official-versions.l4`, `je21-tests-part4-office.l4`, `je21-tests-art26-commencement.l4`, `je21-tests-seat-1-making-and-commencement.l4`, `je21-tests-seat-2-powers-and-effects.l4`, `je21-tests-seat-3-versions-and-publication.l4`.

## Other files

- `NOTES.md`: the reviewer's file (eleven numbered sections).
- `encoding.json`: the machine-readable description of the row.
- `check.sh`, `srcrefs.py`: the check and the quotation checker.
- `SOURCE-LICENSE.md`: terms of the source text.
- `BRIEF.md`: the brief this row was written to.
- `tools/extract_law.py`: how the source `.txt` files were made.
