# NOTES: Acts Interpretation Act 1901 (Australia), encoding `legalese-sonnet-5.5`

Status: **draft**. No domain expert has read this against the text.
Edition encoded: Acts Interpretation Act 1901 (Act No. 2, 1901), Compilation No. 39, compilation date 28 March 2026, includes amendments to Act No. 4, 2026 (register id C2026C00117).
Source file: `../../registers/source-bundle/C1901A00002.txt`, which is a converter's plain-text rendering of the Federal Register of Legislation text, not the official text (see `SOURCE-LICENSE.md`).
Method: one Sonnet 5.5 agent working alone from `BRIEF-pass1.md` (pass 1), then one Sonnet 5.5 agent working alone from the pass-2 brief (completion to "whole"); pass 1 recorded that no other encoding of this Act was read, and pass 2 read none.
Built and checked with `l4` 1.6.98 (main, 7689b0d, 2026-10-19), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`; `check.sh` also ran every module with the main build `l4` 1.6.102 (main, e4f2553, 2026-10-26), sha256 `caa15c9e47b41829397124e322f095ed5c4f5edabc03509b5294c3dfc992f743`, and the two read every module the same.

## Seat

The seat is a person who has a time limit to meet under an Act (to apply, object, appeal, reply or pay), or who needs to know when something takes effect, asking on which day their period ends and which of their days count.
The Acts Interpretation Act is a rulebook for reading other Acts, so the only questions an individual asks of it directly are about counting time (ss 2G, 36, 37A), when an Act comes into operation (ss 3, 3A), when a posted document counts as served (s 29), and a few kindred limits and entitlements.
The person's counterparty is nearly always an official: the Minister, the decision-maker, the court.
An official is never a seat, so the official's side of each relation appears only as facts the person states about them (whether the appointer has directed otherwise, whether the Minister has granted an extension, on which day the Minister received the report) and as what the person is owed (reasons, and the laying of their report before Parliament).
The seat layer is `au-seat.l4` (questions) and `au-cases-seat.l4` (worked cases).

## Scope

Pass 2 (2026-10-29) brings the encoding to "whole": every one of the 1,044 units counted in the coverage table has exactly one disposition, and nothing is left out because it is "interpretive", "addressed to an official" or "refers to another Act".
By section row, 74 of the 83 body sections are `encoded`, 8 are `fork` (ss 2M, 3, 3A, 11A, 15AA, 29, 34, 37A; a `fork` row is also encoded, and the fork is the reading it took) and 1 is `inert` (s 1A, the simplified outline, reason 1).
The Act has no Schedules.
Layer 1 follows the Act's own structure, one module per Part where there is something to encode, plus one self-contained module for every rule that counts time.
Pass 2 added a `-more` or `-terms` or `-readings` or `-ministers` module beside the pass-1 module for a Part rather than editing the pass-1 module (the existing modules are unchanged: see "Changes to existing modules" below).

| file | what it holds |
|---|---|
| `au-interpretation-time.l4` | Imports only `prelude` and `daydate`. s 2B business day, calendar month, calendar year, financial year; s 2G months; s 2M sitting days; s 3 and s 3A commencement; s 29 service by post; s 36 calculating time; s 37A attaining an age. Holidays and closed days are always inputs. |
| `au-part1-application.l4` | ss 1, 2, 2A; the Act's own assent and commencement dates (endnote 3). |
| `au-part2-definitions.l4` | The s 2B definitions that compute (places, document, contravene, prescribed, Proclamation, Senior Counsel); ss 2C to 2F, 2H, 2J, 2K. |
| `au-part2-terms.l4` | New. The tables of meanings: the 77 terms of s 2B and the 18 terms defined inside the section that uses them (ss 2F(7), 15B(4), 19B(7), 19C(6), 19D(5), 21(2), 25B(3), 33A(4), 34B(2), 34C(1), 36(3), 40A(6)), each as one constant that says how the Act states the meaning, what it includes and leaves out, under what condition, and what it points at. |
| `au-part2-more.l4` | New. ss 2C(2), 2CA(2), 2F(2), (3), (6), (7), 2K(2), 2L, 2M(3). |
| `au-part3-commencement.l4`, `au-part3-more.l4` | s 4 (powers before commencement), s 6 (evidence of the date of assent); new: s 4(3), s 4(6). |
| `au-part4-repeal.l4`, `au-part4-more.l4` | ss 7, 10, 10A, 11, 11B; new: s 11A (where an inserted definition or item goes). |
| `au-part5-interpretation.l4` | ss 13, 15AB(1), 15B, 15C, 18B, 25A to 25D. |
| `au-part5-readings.l4` | New. ss 12, 15A, 15AA, 15AB(2), (3), 15AC, 15AD, 15B(3), (3A), (4)(b), 16, 16A, 16B, 16BA, 16C, 17A, 18A, 18B(4) to (6), 20, 21, 23. |
| `au-part5-ministers.l4` | New. ss 19 to 19E (references to Ministers and Departments, substituted reference orders, Commonwealth agreements, machinery of government changes). |
| `au-part6-service.l4`, `au-part6-more.l4` | s 28A; new: s 29(2). |
| `au-part7-powers.l4`, `au-part7-more.l4` | ss 33(4)(b), 33A(1)(ba) and (c), 33AB, 34A, 34B(1), 34C; new: the rest of ss 33, 33A, 33AA, 33B, 34, 34AAA, 34AAB, 34AA, 34AB, 34B(1A), 34C(5), 34C(6)(b). |
| `au-part8-distance.l4`, `au-part8-more.l4` | s 35; new: s 37. |
| `au-part9-citation.l4`, `au-part9-more.l4` | ss 38, 39, 40, 40A; new: s 40A(4). |
| `au-part10-11-instruments.l4` | ss 46, 46AA, 47, 51. |
| `au-seat.l4`, `au-cases-seat.l4` | Layer 2: the seat's questions and worked cases. Unchanged in pass 2. |
| `au-tests-*.l4` | One test file per module (new modules: `au-tests-part2-terms`, `-part2-more`, `-part3-more`, `-part4-more`, `-part5-readings`, `-part5-ministers`, `-part6-more`, `-part7-more`, `-part8-more`, `-part9-more`), expected values written from the text. |
| `units.py`, `coverage.tsv`, `covtable.py` | New. `units.py` counts the units from the text; `coverage.tsv` is the one row per unit; `covtable.py` renders the audit and coverage blocks of this file from the TSV. |

Every rule (every function) has an `@ref` with `src:` locators (the `DECLARE`d vocabulary of choices has none), and every quoted text line begins `-- src:N |` where N is the line number in `../../registers/source-bundle/C1901A00002.txt`.
What `srcrefs.py` checks is printed under the heading on what `check.sh` prints, below.

### What is asked rather than computed

Nothing is left unencoded, but the text hands some answers to someone or something outside it, and those are inputs, never guessed.

- **Time of day and zone.** A moment is a day plus hour, minute and second with no time zone. Section 37 is encoded as a rule that returns which legal time a reference to time means (the Act's own, if it states one, otherwise the legal time in the State or part of the Commonwealth); the legal times themselves are not listed in the text, so the name of the time is an input.
- **Public holidays and office closures.** Never listed by the Act. Every question asks for them as one list of days.
- **Weeks and years.** The Act never says how long they are (finding 5). The ordinary answer is NOTHING, and a separately named ALTERNATIVE READING function shows the 7-day and 12-month result.
- **Judgments left to someone else.** Whether a relationship is "as a couple", whether a contrary intention appears, whether a person is of the opinion that compliance is not reasonably possible, what extension a Minister grants, whether a Minister considers an extension reasonable, whether a power is conferred on a person "as such": all inputs.
- **Borrowed terms.** The definitions in s 2B and elsewhere that take their meaning from another Act return a pointer ("the same meaning as in the Public Service Act 1999") and no meaning; the borrowed meaning is asked of that Act as a fact when a rule needs it.
- **Machinery of government.** Sections 19 to 19E are encoded as decision tables that return a description of whom a reference means; what the Administrative Arrangements Order says on a given day is not in the text, so the facts a cell turns on are BOOLEAN inputs.
- **Dates the text does not give.** The date s 16C(2) commenced (fork F18) and the date s 33(2A) commenced (fork F19) are not derivable from the text, so "the Act was passed after it" is an input.

### Reading a result: FALSE and NOTHING

The rule in force for this row, from 2026-10-29 (assumed, not ruled by a lawyer; it replaces the convention this section stated before, under which a BOOLEAN function could return FALSE where the text is silent):

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a definition that says "means", a condition introduced by "if", "only if", "as long as" or "unless", or a list the text closes with "only" or an equivalent. Where the text lists things without closing the list, says "includes", leaves a term undefined, is silent, or points to a power or authority outside the text, the function answers `NOTHING`, and a comment on that branch names which of those it is. The function's name carries the scope its `FALSE` claims ("under section 47 ...", not "may I ..."), and a seat question that asks Act-wide inherits `NOTHING` wherever the Act points outside itself.

In plain words: `JUST FALSE` (or `FALSE`) is the Act's own "no"; `NOTHING` is "the Act does not say". A caller must not read `NOTHING` as "no".

**Checked on 2026-10-29 under this rule.** The 21 `JUST FALSE` sites in the modules (20 code lines in 15 functions) were read against the text by a second reader: 20 rest on the text's own flat negative ("does not", "is not", "shall not be", "may not") and were kept; the reader counted a bare statutory negative as the text saying no in its own words, which is a reading for a lawyer to confirm. Seven `MAYBE BOOLEAN` functions whose `JUST` wraps an expression can also answer `FALSE`: one, s 20 ("includes"), moved to `NOTHING` with its assertion; three were kept on the text's own "may not", "only" and "must be in writing"; and three are marginal and for a lawyer, s 16C(2) ("shall be read as a reference to"), s 46(2) and s 47 ("to the extent to which it is not in excess", where the author of the independent tests also expected `JUST FALSE`). **Not changed, and open:** 17 of the 129 plain-`BOOLEAN` functions answer `FALSE` for a catch-all value (`any other material`, `anyone else`, `any other method` and the like), eight with a literal `FALSE` arm and nine through `NOT (x EQUALS <catch-all>)`; examples are `is part of the Act` (s 13), `a reference to a Minister is taken to include` (s 19(4)) and `service by this method is permitted` (s 28A). Under the rule they would be `MAYBE BOOLEAN` with `NOTHING`, and their callers would change with them. That change is not made in this pass; the count is a floor. Function names were not changed to carry their section.

- **A catch-all value** (`any other material`, `something else ...`, `in some other way ...`): under the rule above it answers NOTHING unless the text closes the list. The first group of examples that follows is how the plain-`BOOLEAN` functions listed as open above still behave (they answer FALSE; this is the state before the rule, kept so that the reader of a test does not take that FALSE as a ruling that the answer is no). Examples: a contents list or endnotes under s 13 (`is part of the Act` gives FALSE for `any other material`: s 13 does not make them part of the Act, and does not say they are not); a Queen's Counsel under a King (`is Senior Counsel` is FALSE when neither the rank nor the matching Sovereign is given: the definition does not reach it).
  The reviewer's scenarios 54, 138, 204, 224, 225, 382 and 452 are cases of this kind (the topics of 138, 204, 382 and 452 were not in the message that reported them, so they are not described here).
- **A case the function cannot be asked**, because its input type has no value for it: an unincorporated association (reviewer's scenario 383, the kinds of person in s 2C), a period expressed to end after, to begin before, or to end by a day (scenarios 542 to 544, the expressions in the s 36(1) table), and a New Zealand law-making body (scenario 574, the bodies in s 38). Asking needs a new value in the enumeration; the encoding answers nothing for them, and does not answer FALSE for them either.
- **A defined-term lookup compares exact strings.** `section 2B names M as covered by T` answers TRUE for the whole phrase as the Act prints it, for each item of a printed list, and for the article or singular form of a bare noun in such a list (`a lien`, `a substitution`); any other wording of the same idea (`liens`, `a mortgage`) is not named, because the table records what the Act prints and not what it might mean.


<!-- BEGIN audit -->
## Re-disposition audit

This section was written before any new L4 and is kept current: it is generated from `coverage.tsv` by `covtable.py`, and `coverage.tsv` is built on the units `units.py` counts from the text.
The text is `../../registers/source-bundle/C1901A00002.txt`, a converter's plain-text rendering (not the official text), 1,880 lines: the Act is lines 24 to 914 and the endnotes are lines 915 to 1880.
A unit is a Part heading, a section, a subsection, a paragraph, a sub-paragraph, a table row, a defined-term entry, a Note or an Example; the compilation's own apparatus (front matter, endnote headings, abbreviation-key entries, endnote 3 rows, endnote 4 entries) is counted apart.

### The counts

| unit | counted in the text | rows in the pass-1 table | rows now |
|---|---|---|---|
| Part headings | 11 | 0 | 11 |
| sections | 83 | 83 | 83 |
| subsections | 157 | 0 | 157 |
| paragraphs | 267 | 0 | 267 |
| sub-paragraphs | 42 | 0 | 42 |
| table rows | 17 | 7 | 17 |
| defined terms | 95 | 77 | 95 |
| Notes | 31 | 0 | 31 |
| Examples | 17 | 0 | 17 |
| front matter lines | 23 | 2 | 23 |
| endnote headings | 4 | 1 | 4 |
| abbreviation-key entries (endnote 2) | 41 | 0 | 41 |
| legislation history rows (endnote 3) | 79 | 0 | 79 |
| amendment history entries (endnote 4) | 177 | 49 | 177 |
| **the Act (lines 24 to 914)** | **720** | **170** | **720** |
| **the compilation's apparatus (lines 1 to 23 and 915 to 1880)** | **324** | **52** | **324** |
| **all** | **1044** | **222** | **1044** |

The pass-1 table had 222 rows: the 83 sections, the 77 terms of s 2B, 10 rows for s 36 (7 table items and subsections (1) to (3)), the 49 section numbers endnote 4 shows repealed, and 3 rows for the front matter and the endnotes (the Schedules row is not a unit: the Act has none).
Pass 1 also folded subsections and paragraphs into a section row ("encoded in part") and named the inert ones in prose; those are now rows of their own.

### Units that were not rows in the pass-1 table

Every unit of the Act below the section level, every defined term outside s 2B, every Note and Example, every Part heading, and the endnote tables had no row.
They are all rows now (see the coverage table); by kind they are:

- Part headings: 11 not rows before.
- sections: 0 not rows before.
- subsections: 157 not rows before.
- paragraphs: 267 not rows before.
- sub-paragraphs: 42 not rows before.
- table rows: 10 not rows before.
- defined terms: 18 not rows before.
- Notes: 31 not rows before.
- Examples: 17 not rows before.
- front matter lines: 21 not rows before.
- endnote headings: 3 not rows before.
- abbreviation-key entries (endnote 2): 41 not rows before.
- legislation history rows (endnote 3): 79 not rows before.
- amendment history entries (endnote 4): 128 not rows before.

### Verdicts on every row pass 1 did not call `encoded`

Pass 1 gave 32 body sections and 56 s 2B terms the disposition `inert`, and named 41 more subsections or paragraphs `inert` inside sections it called `encoded` ("in part").
Each is listed with its verdict.
`moves to encoded` means the stated reasons for `inert` do not stand under the brief of this pass ("addresses an official", "an interpretive canon", "borrows another Act", "no input from which an answer would differ"), and the rule is written in the module named.
A verdict that keeps `inert` names which of the three reasons licenses it.

| unit | pass 1 | verdict |
|---|---|---|
| s 1A | inert | keeps `inert` (reason 1, not operative) |
| s 2B "acting SES employee" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Administrative Arrangements Order" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; limb (b)(ii) checked and kept whole: it revokes and substitutes in one instrument, one concept) |
| s 2B "affidavit" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "appoint" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "APS employee" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Australian citizen" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Australian Privacy Principle" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Australian Standard" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "charitable" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "charitable purpose" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "charity" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "commencement" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Consolidated Revenue Fund" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Constitution" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "contiguous zone" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "continental shelf" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "court exercising federal jurisdiction" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "court of summary jurisdiction" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "estate" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "exclusive economic zone" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Executive Council" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "federal court" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Gazette" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Government Printer" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Governor of a State" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Governor-General" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "High Court" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "individual" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "insolvent under administration" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Jervis Bay Territory" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "judge" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "justice of the peace" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "land" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "legislative instrument" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Magistrate" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Minister" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "modifications" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "Northern Territory" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "notifiable instrument" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "oath" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Parliament" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "penalty unit" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "record" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the list checked and kept whole: one concept) |
| s 2B "regulations" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "seat of Government" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "SES employee" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Sovereign" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Standards Australia" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "State" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "statutory declaration" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Stipendiary Magistrate" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "swear" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "territorial sea" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "Territory" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "United Kingdom" | inert | moves to encoded: au-part2-terms.l4 (table of meanings) |
| s 2B "writing" | inert | moves to encoded: au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2C(2) | inert | moves to encoded: au-part2-more.l4 `the express reference implies that the expression excludes bodies corporate` |
| s 2CA(2) | inert | moves to encoded: au-part2-more.l4 `a reference to the spouse in the Act covers the person` |
| s 2F(2) | inert | moves to encoded: au-part2-more.l4 `must be taken into account in deciding whether they have a relationship as a couple` |
| s 2F(3) | inert | moves to encoded: au-part2-more.l4 `a particular finding about it is necessary` |
| s 2K(2) | inert | moves to encoded: au-part2-more.l4 `the power to make rules of court includes a power to make them for the purpose of the Act` |
| s 2L | inert | moves to encoded: au-part2-more.l4 `the standard the reference is a reference to` |
| s 2M(3) | inert | moves to encoded: au-part2-more.l4 `the House is taken to have adjourned` |
| s 4(3) | inert | moves to encoded: au-part3-more.l4 `anything may be done before the start time` |
| s 4(6) | inert | moves to encoded: au-part3-more.l4 `a single instrument may be made partly under subsection (2) and partly under an existing power` |
| s 11A | inert | moves to fork: au-part4-more.l4 (1) `the position of the inserted definition among the definitions, counting from 0`; (2) `the position of the inserted item among the items, counting from 0` |
| s 11A(1) | inert | moves to fork: as s 11A |
| s 11A(2) | inert | moves to fork: as s 11A |
| s 12 | inert | moves to encoded: au-part5-readings.l4 `has effect as a substantive enactment without introductory words` |
| s 15A | inert | moves to encoded: au-part5-readings.l4 `section 15A treats the enactment` |
| s 15AA | inert | moves to fork: au-part5-readings.l4 `the interpretation to be preferred` |
| s 15AB(2) | inert | moves to encoded: as s 15AB |
| s 15AB(3) | inert | moves to encoded: as s 15AB |
| s 15AC | inert | moves to encoded: au-part5-readings.l4 `the ideas are taken to be different merely because different forms of words were used` |
| s 15AD | inert | moves to encoded: au-part5-readings.l4 (a) `the example is exhaustive`; (b) `the example may extend the operation of the provision` |
| s 15B(3) | inert | moves to encoded: as s 15B |
| s 15B(3A) | inert | moves to encoded: as s 15B |
| s 16 | inert | moves to encoded: au-part5-readings.l4 `a reference in an Act is construed as a reference to` |
| s 16A | inert | moves to encoded: au-part5-readings.l4 `a reference to the Governor-General is deemed to include`, `the reference is read as acting with the advice of the Executive Council` |
| s 16B | inert | moves to encoded: au-part5-readings.l4 `a reference to the Governor of a State is deemed to include` |
| s 16BA | inert | moves to encoded: au-part5-readings.l4 `a reference to a judge includes` |
| s 16C | inert | moves to encoded: au-part5-readings.l4 (1), (3) `a reference to a Stipendiary Magistrate includes`; (2), (3) `a reference to a Magistrate includes` |
| s 16C(1) | inert | moves to encoded: as s 16C |
| s 16C(2) | inert | moves to fork: as s 16C |
| s 16C(3) | inert | moves to encoded: as s 16C |
| s 17A | inert | moves to encoded: au-part5-readings.l4 `the words are deemed to refer to the Government Printer` |
| s 18A | inert | moves to encoded: au-part5-readings.l4 `has a corresponding meaning` |
| s 18B(4) | inert | moves to encoded: as s 18B |
| s 18B(5) | inert | moves to encoded: as s 18B |
| s 18B(6) | inert | moves to encoded: as s 18B |
| s 19 | inert | moves to encoded: au-part5-ministers.l4 (1) `the Ministers a reference means`; (2) `may be used to work out which Minister is referred to`; (3) `the most Ministers by or in relation to whom the thing must be done in a particular case`; (4) `a reference to a Minister is taken to include` |
| s 19(1) | inert | moves to encoded: as s 19 |
| s 19(2) | inert | moves to encoded: as s 19 |
| s 19(3) | inert | moves to encoded: as s 19 |
| s 19(4) | inert | moves to encoded: as s 19 |
| s 19A | inert | moves to encoded: au-part5-ministers.l4 (1) `the Departments a reference means`; (2) `may be used to work out which Department is identified` |
| s 19A(1) | inert | moves to encoded: as s 19A |
| s 19A Example @469 | inert | moves to encoded: asserted as a test |
| s 19A(2) | inert | moves to encoded: as s 19A |
| s 19B | inert | moves to encoded: au-part5-ministers.l4 (1) `section 19B applies`; (2), (6) `the Governor-General may make a substituted reference order`; (3) `the day on and after which the order has effect`, `the order is in effect on`; (4) `has effect according to its terms`; (5) `is a legislative instrument`; (7) `is an authority within section 19B` |
| s 19B(1) | inert | moves to encoded: as s 19B |
| s 19B(2) | inert | moves to encoded: as s 19B |
| s 19B(3) | inert | moves to encoded: as s 19B |
| s 19B(4) | inert | moves to encoded: as s 19B |
| s 19B(5) | inert | moves to encoded: as s 19B |
| s 19B(6) | inert | moves to encoded: as s 19B |
| s 19B(7) | inert | moves to encoded: as s 19B |
| s 19C | inert | moves to encoded: au-part5-ministers.l4 (1) `section 19C applies`; (2) `the authorities an agreement is taken to refer to`; (3) `may be used to work out which authority is taken to be referred to`; (4) `is a determination for the purposes of item 3`; (5) `the most Ministers by or in relation to whom the agreement requires the thing to be done in a particular case`; (6) `is an authority within section 19C` |
| s 19C(1) | inert | moves to encoded: as s 19C |
| s 19C(2) | inert | moves to encoded: as s 19C |
| s 19C(3) | inert | moves to encoded: as s 19C |
| s 19C(4) | inert | moves to encoded: as s 19C |
| s 19C(5) | inert | moves to encoded: as s 19C |
| s 19C(6) | inert | moves to encoded: as s 19C |
| s 19D | inert | moves to encoded: au-part5-ministers.l4 (1), (2), (4) `the purported exercise is not invalid merely because of the change`; (3) `a machinery of government change occurs`; (5) `is an authority within section 19D` |
| s 19D(1) | inert | moves to encoded: as s 19D |
| s 19D(2) | inert | moves to encoded: as s 19D |
| s 19D(3) | inert | moves to encoded: as s 19D |
| s 19D(4) | inert | moves to encoded: as s 19D |
| s 19D(5) | inert | moves to encoded: as s 19D |
| s 19E | inert | moves to encoded: au-part5-ministers.l4 `the exercise is not invalid merely because the power is conferred on the other Minister` |
| s 20 | inert | moves to encoded: au-part5-readings.l4 `a reference to the holder or occupier includes the person` |
| s 21 | inert | moves to encoded: au-part5-readings.l4 `a reference in an Act to it is construed as` |
| s 21(1) | inert | moves to encoded: as s 21 |
| s 21(2) | inert | moves to encoded: as s 21 |
| s 23 | inert | moves to encoded: au-part5-readings.l4 (a) `words importing a gender include`; (b) `words in a number include` |
| s 25B(3) | inert | moves to encoded: the term table au-part2-terms.l4 |
| s 29(2) | inert | moves to encoded: au-part6-more.l4 `section 29 stops section 160 of the Evidence Act 1995 operating` |
| s 33(1) | inert | moves to encoded: as s 33 |
| s 33(2A) | inert | moves to fork: as s 33 |
| s 33(2B) | inert | moves to encoded: as s 33 |
| s 33(3) | inert | moves to encoded: as s 33 |
| s 33(3AA) | inert | moves to encoded: as s 33 |
| s 33(3A) | inert | moves to encoded: as s 33 |
| s 33(3AB) | inert | moves to encoded: as s 33 |
| s 33(3AC) | inert | moves to encoded: as s 33 |
| s 33(3B) | inert | moves to encoded: as s 33 |
| s 33(5) | inert | moves to encoded: as s 33 |
| s 33AA | inert | moves to encoded: au-part7-more.l4 `the power to make the appointment includes a power of reappointment` |
| s 33A(2) | inert | moves to encoded: as s 33A |
| s 33A(3) | inert | moves to encoded: as s 33A |
| s 33A(4) | inert | moves to encoded: as s 33A |
| s 33B | inert | moves to encoded: au-part7-more.l4 (1) `section 33B applies to the body`; (2) `the body may permit its members to participate by this means`; (3) `the member is taken to be present at the meeting and to form part of any quorum`; (4) `all the members may participate by this means`; (5) `the meeting may be held at that number of places at the same time` |
| s 33B(1) | inert | moves to encoded: as s 33B |
| s 33B(2) | inert | moves to encoded: as s 33B |
| s 33B(3) | inert | moves to encoded: as s 33B |
| s 33B(4) | inert | moves to encoded: as s 33B |
| s 33B(5) | inert | moves to encoded: as s 33B |
| s 34 | inert | moves to fork: au-part7-more.l4 `the person authorised to hear and determine the matter has authority to do this` |
| s 34AAA | inert | moves to encoded: au-part7-more.l4 `the person who exercises the power or performs the function or duty` |
| s 34AAB | inert | moves to encoded: au-part7-more.l4 (1) `the Minister may authorise this person to act on the Minister's behalf`; (2) `the authorisation extends to the function, duty or power`; (3) `an authorisation may be expressed in this way`, `the authorisation continues to have effect`; (4) `the authorisation may be revoked at any time`; (5) `it complies with subsection 34AAB(5)`; (6) `section 34AAB stops the giving of an authorisation under that other power` |
| s 34AAB(1) | inert | moves to encoded: as s 34AAB |
| s 34AAB(2) | inert | moves to encoded: as s 34AAB |
| s 34AAB(3) | inert | moves to encoded: as s 34AAB |
| s 34AAB(4) | inert | moves to encoded: as s 34AAB |
| s 34AAB(5) | inert | moves to encoded: as s 34AAB |
| s 34AAB(6) | inert | moves to encoded: as s 34AAB |
| s 34AA | inert | moves to encoded: au-part7-more.l4 `the power of delegation includes delegating to a delegate described in this way` |
| s 34AB | inert | moves to encoded: au-part7-more.l4 (1)(a) `the delegation may be made in this way`; (1)(b) `the power to delegate is among the powers that may be delegated`; (1)(c) `for the purposes of the Act it is deemed to have been performed or exercised by the authority`; (1)(d) `the delegation prevents the authority from performing or exercising the function, duty or power`; (1)(e) `section 34A applies to the authority as if it were a person`; (2) `the delegation is taken to include the additional functions, duties or powers on this day`; (3) `the delegation is taken to include the functions, duties or powers as altered on this day` |
| s 34AB(1) | inert | moves to encoded: as s 34AB |
| s 34AB(2) | inert | moves to encoded: as s 34AB |
| s 34AB(3) | inert | moves to encoded: as s 34AB |
| s 34B(1A) | inert | moves to encoded: as s 34B |
| s 34B(2) | inert | moves to encoded: as s 34B |
| s 34C(5) | inert | moves to encoded: au-part7-more.l4 `the Minister may grant the extension` |
| s 34C(6)(b) | inert | moves to encoded: au-part7-more.l4 `the person furnishes the report within the period as extended` |
| s 37 | inert | moves to encoded: au-part8-more.l4 `the time a reference to time in an Act means` |
| s 40A(4) | inert | moves to encoded: au-part9-more.l4 `the Part that decides whether a provision of the old legislation corresponds to one of the new`, `the old provision corresponds to the new provision for section 40A` |
| s 40A(6) | inert | moves to encoded: the term table au-part2-terms.l4 |

### Every row that is not `encoded` now

Forks are listed with the fork-register entry that licenses each reading; inert rows with the reason number; repealed rows with what the text shows.
The Notes (31), the endnote tables and the front matter are listed by group, because every row of a group has the same verdict.

| unit | disposition | verdict |
|---|---|---|
| all 23 front matter lines | inert (reason 1, not operative) | keeps `inert`: title, number, compilation details or heading of the compilation; states no rule of the Act |
| Part 1 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 1A | inert (reason 1, not operative) | keeps `inert`: a simplified outline: summarises the Parts and states no rule of its own; every line is stated by the section it summarises |
| s 1A "Part 5"(a) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 5"(b) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 5"(c) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 5"(d) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 7"(a) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 7"(b) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| s 1A "Part 7"(c) | inert (reason 1, not operative) | keeps `inert`: as s 1A |
| all 31 Notes | inert (reason 1, not operative) | keeps `inert`: a Note: it explains and cross-refers, and is not operative text |
| Part 2 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 2B "business day" | fork (F16) | moved from `encoded` to `fork`: F16 |
| s 2B "sitting day" | fork (F13) | moved from `encoded` to `fork`: F13 |
| s 2M | fork (F13) | moved from `encoded` to `fork`: F13 |
| s 2M(1) | fork (F13) | moved from `encoded` to `fork`: F13 |
| s 2M(2) | fork (F13) | moved from `encoded` to `fork`: F13 |
| Part 3 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 3 | fork (F8) | moved from `encoded` to `fork`: F8 |
| s 3A | fork (F6) | moved from `encoded` to `fork`: F6, F7 |
| s 3A(1) | fork (F6) | moved from `encoded` to `fork`: F6, F7 |
| s 3A(2) | fork (F6) | moved from `encoded` to `fork`: F6, F7 |
| s 3A(3) | fork (F6) | moved from `encoded` to `fork`: F6, F7 |
| Part 4 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 11A | fork (F22) | moved from `inert` to `fork`: F22 |
| s 11A(1) | fork (F22) | moved from `inert` to `fork`: F22 |
| s 11A(2) | fork (F22) | moved from `inert` to `fork`: F22 |
| Part 5 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 15AA | fork (F20) | moved from `inert` to `fork`: F20 |
| s 16C(2) | fork (F18) | moved from `inert` to `fork`: F18 |
| s 16C(2)(a) | fork (F18) | moved from `inert` to `fork`: F18 |
| s 16C(2)(b) | fork (F18) | moved from `inert` to `fork`: F18 |
| s 19 table item 3(c) | fork (F21) | moved from `inert` to `fork`: F21 |
| Part 6 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 29 | fork (F14) | moved from `encoded` to `fork`: F14 |
| s 29(1) | fork (F14) | moved from `encoded` to `fork`: F14 |
| Part 7 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 33(2A) | fork (F19) | moved from `inert` to `fork`: F19 |
| s 33(4)(b) | fork (F11) | moved from `encoded` to `fork`: F11 |
| s 33A(1)(ba) | fork (F10) | moved from `encoded` to `fork`: F10 |
| s 33A(1)(c) | fork (F10) | moved from `encoded` to `fork`: F10 |
| s 33A(1)(c)(i) | fork (F10) | moved from `encoded` to `fork`: F10 |
| s 33A(1)(c)(ii) | fork (F10) | moved from `encoded` to `fork`: F10 |
| s 33A(1)(c)(iii) | fork (F10) | moved from `encoded` to `fork`: F10 |
| s 34 | fork (F23) | moved from `inert` to `fork`: F23 |
| s 34C "periodic report" | fork (F17) | moved from `n/a (not a row in pass 1)` to `fork`: F17 |
| s 34C(3) | fork (F12) | moved from `encoded` to `fork`: F12 |
| s 34C(6)(a) | fork (F12) | moved from `encoded` to `fork`: F12 |
| s 34C(6)(c) | fork (F12) | moved from `encoded` to `fork`: F12 |
| s 34C(7)(b) | fork (F12) | moved from `encoded` to `fork`: F12 |
| Part 8 | inert (reason 1, not operative) | keeps `inert`: heading |
| s 36(1) | fork (F4) | moved from `encoded` to `fork`: F4 (the length of a week and of a year is not stated) |
| s 36(2) | fork (F3) | moved from `encoded` to `fork`: F3, F9 |
| s 36(2)(a) | fork (F3) | moved from `encoded` to `fork`: F3, F9 |
| s 36(2)(b) | fork (F3) | moved from `encoded` to `fork`: F3, F9 |
| s 36(3) | fork (F5) | moved from `encoded` to `fork`: F5 |
| s 36 "holiday" | fork (F5) | moved from `n/a (not a row in pass 1)` to `fork`: F5 |
| s 36(3)(a) | fork (F5) | moved from `encoded` to `fork`: F5 |
| s 36(3)(b) | fork (F5) | moved from `encoded` to `fork`: F5 |
| s 37A | fork (F15) | moved from `encoded` to `fork`: F15 |
| Part 9 | inert (reason 1, not operative) | keeps `inert`: heading |
| Part 10 | inert (reason 1, not operative) | keeps `inert`: heading |
| Part 11 | inert (reason 1, not operative) | keeps `inert`: heading |
| all 4 endnote headings | inert (reason 1, not operative) | keeps `inert`: endnote text: the compilation's own record |
| all 41 abbreviation-key entries (endnote 2) | inert (reason 1, not operative) | keeps `inert`: abbreviation key entry: explains the endnotes |
| all 78 legislation history rows (endnote 3) | inert (reason 1, not operative) | keeps `inert`: legislation history row: an amending law and its dates; records history and states no rule |
| all 103 amendment history entries (endnote 4) (of this group) | inert (reason 1, not operative) | keeps `inert`: amendment history entry |
| all 74 amendment history entries (endnote 4) (of this group) | repealed or blank in this text | keeps `repealed`: the text shows it repealed |

<!-- END audit -->

## Jural relations

Each relation is stated once in layer 1, from neither side, and the seat asks the paired question where the person holds the right, privilege, power or immunity or owes the duty or liability.
Most of an interpretation Act creates no relation between two parties: it says how other legislation is to be read, so the last row lists every provision that creates none, once.
The table covers the whole text; a provision in neither a relation row nor the `none` row would be a gap (checked against the section list in the coverage table).

| provision | holder (right, privilege, power, immunity) | other party (duty, no-right, liability, disability) | relation | L4 rule | seat question |
|---|---|---|---|---|---|
| s 36(2) | the person who must do a thing: privilege to do it on the next day that is not a Saturday, a Sunday or a holiday | the other side (the authority or party to whom it is done): no-right to treat it as late | privilege / no-right | `the last day on which the thing may be done` | What is the last day on which I may act ... (s 36(2))?; Am I in time ...? |
| s 4(2), (3) | the person on whom an enacted Act will confer a power at a start time: privilege to exercise it, and to do what enables it, before the start time | anyone who would say the power does not yet exist: no-right | privilege / no-right | `section 4 allows the power to be exercised before the start time`, `anything may be done before the start time` | not asked (addresses the maker of an appointment or instrument) |
| s 7(2) | a person holding a right, privilege, obligation or liability acquired, accrued or incurred: immunity from loss by repeal or amendment (and liability to a penalty already incurred) | the repealing or amending Act: disability, unless a contrary intention appears | immunity / disability | `what a repeal or amendment does to` | What happens to what I already have or owe when the Act is repealed or amended? |
| s 25A | the person who keeps a record by a device: privilege to comply by producing a writing that reproduces the information in a form the court, tribunal or person can understand | the court, tribunal or person: no-right to demand more, unless it otherwise directs | privilege / no-right | `the requirement is complied with` | not asked |
| s 25B(2) | a body whose constitution an Act alters: immunity from the alteration affecting its identity, functions, powers, property, rights, liabilities, proceedings or inquiries | anyone who would say it did: disability | immunity / disability | `an alteration of the constitution of a body affects its identity, functions, powers, property, rights, liabilities or obligations` | not asked |
| s 25C | the person filing a prescribed form: privilege that substantial compliance is enough | the receiving body: no-right to reject a form for want of strict compliance | privilege / no-right | `the form requirement is met` | Does my form meet the requirement if it does not comply strictly with the prescribed form? |
| s 25D | the person affected by a decision: claim to reasons setting out the findings of fact and referring to the evidence | the decision-maker: duty | claim / duty | `the written reasons are complete` | Are the written reasons I was given complete? |
| s 28A | the person serving: power to serve by a listed method (or by another method another law or a court authorises) | the person served: liability to be served in that way | power / liability | `service by this method is permitted` | Was the document served on me in a way the Acts Interpretation Act allows? |
| s 29(1) | the person serving a document by post: power to effect service by posting; the person served: power to rebut by proving the contrary | the person served: liability to be treated as served on the ordinary delivery day; the person serving: liability to that day being displaced | power / liability, twice | `the day service by post is taken to be effected` | On which day am I taken to have been served by post? |
| s 29(2) | a person who relies on section 160 of the Evidence Act 1995: the continued operation of that section | whoever would say section 29 displaces it: disability | immunity / disability | `section 29 stops section 160 of the Evidence Act 1995 operating` | not asked (the Evidence Act is not in the text) |
| s 33(1) | the holder of a power: privilege to exercise it from time to time as the occasion requires; the person owed a function or duty: claim to its performance each time | anyone who would object to a repeated exercise: no-right; the holder of the function or duty: duty | privilege / no-right; claim / duty | `what section 33(1) says is to be done` | not asked (addresses the holder of the power) |
| s 33(2A) | the person, court or body that "may" do a thing: privilege to do it or not, at its discretion | anyone who would require it to be done: no-right | privilege / no-right | `the act or thing may be done at the discretion of the person, court or body` | not asked |
| s 33(2B) | a body that holds a power, function or duty: immunity from the exercise or performance being affected merely by a vacancy in its membership | anyone who would challenge the exercise on that ground: disability | immunity / disability | `the exercise or performance is affected merely because of a vacancy in the membership` | not asked |
| s 33(3), (3AA), (3A), (3AB), (3AC) | the maker of an instrument: power to repeal, rescind, revoke, amend or vary it in like manner, to make it as to some only of the matters, and to identify a matter by a class | those the instrument binds: liability | power / liability | `the power to make the instrument includes the power to do this to it`, `the condition that governs doing this to the instrument`, `the power includes making the instrument in this way`, `the person or authority may identify the matter by reference to a class or classes of matters`, `it is a matter for subsections 33(3A) and 33(3AB)` | not asked |
| s 33(3B) | the maker of an instrument: immunity from being taken, by implication, to lack power over an aspect of a matter merely because the Act makes provision for another aspect | anyone who would argue the implication: disability | immunity / disability | `the power is taken, by implication, not to include power to make provision for a particular aspect of a matter` | not asked |
| s 33(4) | the person or authority that appoints: power to appoint a person to act (until a person is appointed or 12 months have run), to remove or suspend an appointee, and to appoint someone temporarily | the acting appointee and the person removed or suspended: liability | power / liability, bounded by 12 months | `the power to make appointments includes this`, `the day the acting appointment under section 33(4) ends`, `the last day of the 12 months for an acting appointment under section 33(4)` | On which day do the 12 months of an appointment to act under a power to appoint run out? |
| s 33(4) proviso | the person or authority whose recommendation, approval or consent is required: immunity from an acting appointment or removal being made without it | the appointer: disability | immunity / disability | `the power may be exercised as the proviso to section 33(4) requires` | not asked |
| s 33(5) | the maker of an instrument prescribing penalties: power to require a statutory declaration despite the limit on penalties | those the instrument binds: liability | power / liability | `the limit on penalties prevents the instrument from requiring a statutory declaration` | not asked |
| s 33AA | the person or body that appoints: power to reappoint | the person reappointed: liability | power / liability | `the power to make the appointment includes a power of reappointment` | not asked |
| s 33AB | the person acting under a purported appointment, and those who dealt with them: immunity from invalidity on the listed grounds alone | anyone who would challenge: disability | immunity / disability | `the thing done is invalid merely because of this ground` | not asked (addresses the effect on third parties) |
| s 33A(1)(a), (b) | the appointer: power to limit the appointment to stated circumstances, to fix its terms, conditions, remuneration and allowances, and to end it at any time | the acting appointee: liability | power / liability | `the appointer may do this under section 33A(1)` | the acting questions take whether the appointer has directed otherwise as a fact |
| s 33A(1)(ba), (c) | the appointee: privilege to act in the office until the 12-month limit, the direction or the filling of the vacancy | the appointer: no-right to hold the appointee to a longer term | privilege / no-right | `the last day the appointee may act in a vacant office`, `the day the continued acting ends` | Until which day may I keep acting ...? |
| s 33A(1)(d) | the acting appointee: power to end the appointment by resigning in writing delivered to the appointer | the appointer: liability | power / liability | `the appointment ceases to have effect on the appointee's resignation` | not asked |
| s 33A(1)(e), (2) | the person acting: power to exercise all the powers of the holder and to be treated as the holder under the Act; the persons owed the functions and duties: claim to their performance | those subject to the powers: liability; the person acting: duty | power / liability; claim / duty | `the appointee has this while acting in the office`, `the person acting by operation of law has this while acting in the office` | not asked |
| s 33A(3) | the person purporting to act, and those who dealt with them: immunity from invalidity because the occasion to act had not arisen or had ceased | anyone who would challenge: disability | immunity / disability | `the thing done is invalid merely because of this ground for purported acting` | not asked |
| s 33B(2), (4), (5) | a body established by an Act: power to permit its members to take part by telephone, closed-circuit television or other means, all of them, at 2 or more places at once | its members: liability | power / liability | `the body may permit its members to participate by this means`, `all the members may participate by this means`, `the meeting may be held at that number of places at the same time` | not asked |
| s 33B(3) | a member taking part under a permission: immunity from being treated as absent or outside the quorum | the body and anyone counting the quorum: disability | immunity / disability | `the member is taken to be present at the meeting and to form part of any quorum` | not asked |
| s 34 | a person authorised by law or by consent to hear and determine a matter: power to receive evidence, examine witnesses and administer an oath or affirmation | the witnesses called: liability | power / liability | `the person authorised to hear and determine the matter has authority to do this` | not asked |
| s 34AAA | the person for the time being holding the office or position: power to exercise the power or function conferred on the office | the former holder of the office: disability (no longer able to exercise it) | power / disability of the former holder; the duty to perform a conferred function or duty falls on the person for the time being holding the office, and the person it is owed to holds the claim | `the person who exercises the power or performs the function or duty` | not asked |
| s 34AAB(1) to (3) | the authorising Minister: power to authorise a Minister who does not administer the Act or provision, or a member of the Executive Council who is not a Minister, to act on the Minister's behalf, under the Act, provision or instruments under it, for a period or while a circumstance lasts or until a new office-holder is appointed | the person authorised: liability | power / liability | `the Minister may authorise this person to act on the Minister's behalf`, `the authorisation extends to the function, duty or power`, `an authorisation may be expressed in this way`, `the authorisation continues to have effect` | not asked |
| s 34AAB(4) | the authorising Minister: power to revoke the authorisation at any time | the person authorised: liability | power / liability | `the authorisation may be revoked at any time` | not asked |
| s 34AAB(5) | whoever relies on an authorisation or its revocation: claim that it is in writing | the authorising Minister: duty | claim / duty | `it complies with subsection 34AAB(5)` | not asked |
| s 34AA | a person or body with a power to delegate: power to delegate to whoever holds, occupies or performs the duties of an office, even one created later | the delegate: liability | power / liability | `the power of delegation includes delegating to a delegate described in this way` | not asked |
| s 34AB(1)(a), (b) | the authority: power to delegate generally or as the instrument provides | the delegate: liability, and disability to delegate the power to delegate on | power / liability; immunity / disability | `the delegation may be made in this way`, `the power to delegate is among the powers that may be delegated` | not asked |
| s 34AB(1)(c), (d) | the delegate: power to perform or exercise the delegated function, duty or power so that it counts as the authority's; the authority: privilege to go on performing or exercising it itself | the authority: liability to be treated as having performed what the delegate performs; those affected: no-right to insist on the delegate alone | power / liability; privilege / no-right | `for the purposes of the Act it is deemed to have been performed or exercised by the authority`, `the delegation prevents the authority from performing or exercising the function, duty or power` | not asked |
| s 34AB(2), (3) | the delegate: power over additional or altered functions, duties or powers on and after the day the amendment takes effect | the delegator: liability | power / liability | `the delegation is taken to include the additional functions, duties or powers on this day`, `the delegation is taken to include the functions, duties or powers as altered on this day` | not asked |
| s 34A | the delegate: privilege to act on the delegate's own opinion, belief or state of mind | the delegator and those affected: no-right to insist on the delegator's | privilege / no-right | `the delegate may act on the delegate's own opinion, belief or state of mind` | not asked |
| s 34B(1), (1A) | the person required to present a paper: privilege to comply by presenting in accordance with the House's rules or by delivery to the Clerk and recording | the House and anyone alleging non-compliance: no-right | privilege / no-right | `it is sufficient compliance in relation to a House`, `the paper is deemed to have been presented to the House as the Act or law describes` | not asked |
| s 34C(2) | the Minister: claim to the report by the end of 6 months | the person: duty to furnish a periodic report | claim / duty | `the last day to furnish a periodic report to the Minister` | By which day must I furnish my periodic report to the Minister? |
| s 34C(4) | the person: power to apply for an extension within the specified period | the Minister: liability | power / liability | `the person may apply for an extension` | Can I still ask the Minister for more time to furnish my report? |
| s 34C(5) | the Minister: power to grant such extension as is reasonable | the person: liability | power / liability | `the Minister may grant the extension` | the extended last day is an input to the s 34C(6), (7) questions |
| s 34C(6)(b) | the Minister: claim to the report within the extended period | the person who applied: duty | claim / duty | `the person furnishes the report within the period as extended` | not asked separately: the s 36 questions with the extended last day |
| s 34C(7)(a) | the Minister: claim to a written statement of reasons within 14 days after the late end | the person: duty to explain | claim / duty | `the last day to furnish the statement explaining why the report was late` | By which day must I explain in writing why my report was late? |
| s 34C(3), (6)(a), (6)(c), (7)(b) | each House of the Parliament (not a seat); the person is owed that their report and statements are laid | the Minister: duty to cause the copy to be laid within the stated sitting days | claim / duty | `the last day for the Minister to lay ...` (four rules) | By which day must the Minister lay my report ...? (four questions) |
| s 19B(2) to (6), s 19C(4) | the Governor-General: power to make a substituted reference order; the Minister administering the relevant Department: power to make a determination | those the order or determination affects: liability | power / liability | `the Governor-General may make a substituted reference order`, `the order is in effect on`, `is a determination for the purposes of item 3` | not asked |
| s 19D, 19E | an authority or Minister who purported to exercise a power, and those who dealt with them: immunity from invalidity merely because of a machinery of government change, or because the power is conferred on the other Minister | anyone who would challenge: disability | immunity / disability | `the purported exercise is not invalid merely because of the change`, `the exercise is not invalid merely because the power is conferred on the other Minister` | not asked |
| s 46(2), (3), 46AA, 47 | the maker of an instrument or resolution: immunity from invalidity to the extent it is within power; the authority: power to go on amending an instrument an Act has amended; power to incorporate matter by reference | those the instrument binds: disability or liability | immunity / disability; power / liability | `this part of the instrument is valid`, `an amendment of the instrument by an Act prevents the authority from later amending or repealing it`, `the instrument may apply, adopt or incorporate the matter at this time`, `this part of the resolution is valid` | not asked |
| s 51 | the Governor-General: power to make regulations | those the regulations bind: liability | power / liability | `the Governor-General may make regulations prescribing the matter` | not asked |
| every other provision: ss 1, 1A, 2, 2A, 2B to 2M, 3, 3A, 4(1), (4) to (7), 6, 7(1), (3), (4), 10, 10A, 11, 11A, 11B, 12, 13, 15A, 15AA, 15AB, 15AC, 15AD, 15B, 15C, 16, 16A, 16B, 16BA, 16C, 17A, 18A, 18B, 19, 19A, 19C, 20, 21, 23, 25B(1), (1A), (3), 33B(1), 35, 36(1), (3), 37, 37A, 38, 39, 40, 40A, 46(1) and the Notes, Examples, outline and endnotes | none | none | none: definitions, counting rules, rules of reading and tables that say what a reference means or when a day falls; they fix WHEN a relation starts or ends, or WHO or WHAT a word names, and create no claim, privilege, power or immunity of their own | the corresponding rules in `au-part2-definitions.l4`, `au-part2-terms.l4`, `au-interpretation-time.l4`, `au-part3-more.l4`, `au-part4-more.l4`, `au-part4-repeal.l4`, `au-part5-interpretation.l4`, `au-part5-readings.l4`, `au-part5-ministers.l4`, `au-part8-more.l4`, `au-part9-citation.l4`, `au-part9-more.l4`, `au-part10-11-instruments.l4` | the counting and commencement questions |

<!-- BEGIN coverage -->
## Coverage table

One row per unit counted by `units.py` from the text: 720 in the Act and 324 in the compilation's apparatus.
The table is generated from `coverage.tsv` by `covtable.py`; edit the TSV, never this block.
A paragraph, sub-paragraph, table row, Note or Example that has no rule of its own says `as` and the row above it.

### Summary of dispositions

| group | encoded | fork | inert 1 | inert 2 | inert 3 | repealed or blank in this text | total |
|---|---|---|---|---|---|---|---|
| Part headings | 0 | 0 | 11 | 0 | 0 | 0 | 11 |
| sections | 74 | 8 | 1 | 0 | 0 | 0 | 83 |
| subsections | 143 | 14 | 0 | 0 | 0 | 0 | 157 |
| paragraphs | 247 | 13 | 7 | 0 | 0 | 0 | 267 |
| sub-paragraphs | 39 | 3 | 0 | 0 | 0 | 0 | 42 |
| table rows | 17 | 0 | 0 | 0 | 0 | 0 | 17 |
| defined terms | 91 | 4 | 0 | 0 | 0 | 0 | 95 |
| Notes | 0 | 0 | 31 | 0 | 0 | 0 | 31 |
| Examples | 17 | 0 | 0 | 0 | 0 | 0 | 17 |
| front matter lines | 0 | 0 | 23 | 0 | 0 | 0 | 23 |
| endnote headings | 0 | 0 | 4 | 0 | 0 | 0 | 4 |
| abbreviation-key entries (endnote 2) | 0 | 0 | 41 | 0 | 0 | 0 | 41 |
| legislation history rows (endnote 3) | 1 | 0 | 78 | 0 | 0 | 0 | 79 |
| amendment history entries (endnote 4) | 0 | 0 | 103 | 0 | 0 | 74 | 177 |
| **the Act** | 628 | 42 | 50 | 0 | 0 | 0 | 720 |
| **the compilation's apparatus** | 1 | 0 | 249 | 0 | 0 | 74 | 324 |
| **all units** | 629 | 42 | 299 | 0 | 0 | 74 | 1044 |

A `fork` row is also encoded: it points at the fork-register entry and at the rule that encodes the chosen reading, and it is counted under `fork` only.

### Rows: the Act

| unit | lines | disposition | where it is encoded, or why not |
|---|---|---|---|
| Part 1 | 24 | inert (reason 1, not operative) | heading |
| s 1 | 25 | encoded | au-part1-application.l4 `the short title of this Act` |
| s 1A | 27 | inert (reason 1, not operative) | a simplified outline: summarises the Parts and states no rule of its own; every line is stated by the section it summarises |
| s 1A "Part 5"(a) | 39 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 5"(b) | 40 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 5"(c) | 41 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 5"(d) | 42 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 7"(a) | 45 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 7"(b) | 46 | inert (reason 1, not operative) | as s 1A |
| s 1A "Part 7"(c) | 47 | inert (reason 1, not operative) | as s 1A |
| s 2 | 52 | encoded | au-part1-application.l4 `a provision of this Act applies to the Act or provision` |
| s 2(1) | 53 | encoded | as s 2 |
| s 2 Note @54 | 54 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2(2) | 55 | encoded | as s 2 |
| s 2A | 56 | encoded | au-part1-application.l4 `this Act binds the Crown in each of its capacities` |
| Part 2 | 58 | inert (reason 1, not operative) | heading |
| s 2B | 59 | encoded | the term tables au-part2-terms.l4; the computing definitions are in au-part2-definitions.l4 and au-interpretation-time.l4 |
| s 2B "acting SES employee" | 61 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Administrative Arrangements Order" | 62 | encoded | au-part2-terms.l4 (table of meanings; limb (b)(ii) checked and kept whole: it revokes and substitutes in one instrument, one concept) |
| s 2B "Administrative Arrangements Order"(a) | 63 | encoded | as s 2B |
| s 2B "Administrative Arrangements Order"(b) | 64 | encoded | as s 2B |
| s 2B "Administrative Arrangements Order"(b)(i) | 65 | encoded | as s 2B |
| s 2B "Administrative Arrangements Order"(b)(ii) | 66 | encoded | as s 2B |
| s 2B Note @67 | 67 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "affidavit" | 68 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "appoint" | 69 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "APS employee" | 70 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Australia" | 71 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B Note @72 | 72 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "Australian citizen" | 73 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Australian Privacy Principle" | 74 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Australian Standard" | 75 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "business day" | 76 | fork (F16) | F16; au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "calendar month" | 77 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "calendar year" | 78 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "charitable" | 79 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "charitable purpose" | 80 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "charity" | 81 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "commencement" | 82 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B Note @83 | 83 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "Commonwealth" | 84 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B Note @85 | 85 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "Consolidated Revenue Fund" | 86 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Constitution" | 87 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "contiguous zone" | 88 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "continental shelf" | 89 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "contravene" | 90 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "court exercising federal jurisdiction" | 91 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "court of summary jurisdiction" | 92 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "de facto partner" | 93 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "document" | 94 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members); the rule is in the module the section row names |
| s 2B "document"(a) | 95 | encoded | as s 2B |
| s 2B "document"(b) | 96 | encoded | as s 2B |
| s 2B "document"(c) | 97 | encoded | as s 2B |
| s 2B "document"(d) | 98 | encoded | as s 2B |
| s 2B "estate" | 99 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "exclusive economic zone" | 100 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Executive Council" | 101 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "external Territory" | 102 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B Note @103 | 103 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "federal court" | 104 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "financial year" | 105 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "foreign country" | 106 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Gazette" | 107 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Government Printer" | 108 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B Note @109 | 109 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "Governor of a State" | 110 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Governor-General" | 111 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "High Court" | 112 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "individual" | 113 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "insolvent under administration" | 114 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "internal Territory" | 115 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Jervis Bay Territory" | 116 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "judge" | 117 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "justice of the peace" | 118 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "land" | 119 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "law of the Commonwealth" | 120 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "legislative instrument" | 121 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Magistrate" | 122 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Minister" | 123 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B Note @124 | 124 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "modifications" | 125 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2B "month" | 126 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Northern Territory" | 127 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "notifiable instrument" | 128 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "oath" | 129 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Parliament" | 130 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "penalty unit" | 131 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "person" | 132 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "prescribed" | 133 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Proclamation" | 134 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B Note @135 | 135 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2B "record" | 136 | encoded | au-part2-terms.l4 (table of meanings; the list checked and kept whole: one concept) |
| s 2B "regulations" | 137 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "rules of court" | 138 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "seat of Government" | 139 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Senior Counsel" | 140 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Senior Counsel"(a) | 141 | encoded | as s 2B |
| s 2B "Senior Counsel"(b) | 142 | encoded | as s 2B |
| s 2B "SES employee" | 143 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "sitting day" | 144 | fork (F13) | F13; au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Sovereign" | 145 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "spouse" | 146 | encoded | au-part2-terms.l4 (table of meanings); the rule is in the module the section row names |
| s 2B "Standards Australia" | 147 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "State" | 148 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "statutory declaration" | 149 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Stipendiary Magistrate" | 150 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "swear" | 151 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "territorial sea" | 152 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "Territory" | 153 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "United Kingdom" | 154 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2B "writing" | 155 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 2C | 156 | encoded | au-part2-definitions.l4 `is included in an expression denoting persons generally` |
| s 2C(1) | 157 | encoded | as s 2C |
| s 2C(2) | 158 | encoded | au-part2-more.l4 `the express reference implies that the expression excludes bodies corporate` |
| s 2CA | 159 | encoded | au-part2-definitions.l4 `is the spouse of the other person` |
| s 2CA(1) | 160 | encoded | as s 2CA |
| s 2CA(2) | 161 | encoded | au-part2-more.l4 `a reference to the spouse in the Act covers the person` |
| s 2CA Example @162 | 162 | encoded | asserted as a test |
| s 2D | 163 | encoded | au-part2-definitions.l4 `are de facto partners` |
| s 2D(a) | 165 | encoded | as s 2D |
| s 2D(b) | 166 | encoded | as s 2D |
| s 2E | 167 | encoded | au-part2-definitions.l4 `are in a registered relationship` |
| s 2F | 169 | encoded | au-part2-definitions.l4 `are in a de facto relationship`, `are related by family` |
| s 2F(1) | 170 | encoded | as s 2F |
| s 2F(1)(a) | 171 | encoded | as s 2F |
| s 2F(1)(b) | 172 | encoded | as s 2F |
| s 2F(1)(c) | 173 | encoded | as s 2F |
| s 2F(2) | 174 | encoded | au-part2-more.l4 `must be taken into account in deciding whether they have a relationship as a couple` |
| s 2F(2)(a) | 175 | encoded | as s 2F(2) |
| s 2F(2)(b) | 176 | encoded | as s 2F(2) |
| s 2F(2)(c) | 177 | encoded | as s 2F(2) |
| s 2F(2)(d) | 178 | encoded | as s 2F(2) |
| s 2F(2)(e) | 179 | encoded | as s 2F(2) |
| s 2F(2)(f) | 180 | encoded | as s 2F(2) |
| s 2F(2)(g) | 181 | encoded | as s 2F(2) |
| s 2F(2)(h) | 182 | encoded | as s 2F(2) |
| s 2F(3) | 183 | encoded | au-part2-more.l4 `a particular finding about it is necessary` |
| s 2F(4) | 184 | encoded | as s 2F |
| s 2F(4)(a) | 185 | encoded | as s 2F |
| s 2F(4)(b) | 186 | encoded | as s 2F |
| s 2F(5) | 187 | encoded | as s 2F |
| s 2F(6) | 188 | encoded | as s 2F |
| s 2F(6)(a) | 189 | encoded | as s 2F |
| s 2F(6)(b) | 190 | encoded | as s 2F |
| s 2F(6)(c) | 191 | encoded | as s 2F |
| s 2F "adopted" | 193 | encoded | au-part2-terms.l4 (table of meanings) |
| s 2F(7) | 193 | encoded | au-part2-more.l4 `counts as an adoption for the purposes of subsection (6)`, and the term table au-part2-terms.l4 |
| s 2G | 194 | encoded | au-interpretation-time.l4 `the last day of` n `calendar months starting on`, `the last day of a month starting on` |
| s 2G(1) | 195 | encoded | as s 2G |
| s 2G(1)(a) | 196 | encoded | as s 2G |
| s 2G(1)(b) | 197 | encoded | as s 2G |
| s 2G(1)(b)(i) | 198 | encoded | as s 2G |
| s 2G(1)(b)(ii) | 199 | encoded | as s 2G |
| s 2G Example 1 @200 | 200 | encoded | asserted as a test |
| s 2G Example 2 @201 | 201 | encoded | asserted as a test |
| s 2G(2) | 202 | encoded | as s 2G |
| s 2G(2)(a) | 203 | encoded | as s 2G |
| s 2G(2)(b) | 204 | encoded | as s 2G |
| s 2G(2)(b)(i) | 205 | encoded | as s 2G |
| s 2G(2)(b)(ii) | 206 | encoded | as s 2G |
| s 2G Example 1 @207 | 207 | encoded | asserted as a test |
| s 2G Example 2 @208 | 208 | encoded | asserted as a test |
| s 2H | 209 | encoded | au-part2-definitions.l4 `is a law of the Commonwealth, apart from the Territory exclusion` |
| s 2J | 211 | encoded | au-part2-definitions.l4 `the reference is taken to include the document` |
| s 2J(a) | 213 | encoded | as s 2J |
| s 2J(b) | 214 | encoded | as s 2J |
| s 2J(c) | 215 | encoded | as s 2J |
| s 2J(d) | 216 | encoded | as s 2J |
| s 2J(e) | 217 | encoded | as s 2J |
| s 2J Note @219 | 219 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 2K | 220 | encoded | au-part2-definitions.l4 `are rules of court` |
| s 2K(1) | 221 | encoded | as s 2K |
| s 2K(2) | 222 | encoded | au-part2-more.l4 `the power to make rules of court includes a power to make them for the purpose of the Act` |
| s 2L | 223 | encoded | au-part2-more.l4 `the standard the reference is a reference to` |
| s 2M | 225 | fork (F13) | F13; au-interpretation-time.l4 `is a sitting day`, `the sitting day that is the n-th after` |
| s 2M(1) | 226 | fork (F13) | F13; as s 2M |
| s 2M(2) | 227 | fork (F13) | F13; as s 2M |
| s 2M Example 1 @228 | 228 | encoded | asserted as a test |
| s 2M Example 2 @229 | 229 | encoded | asserted as a test |
| s 2M(3) | 230 | encoded | au-part2-more.l4 `the House is taken to have adjourned` |
| s 2M(3)(a) | 231 | encoded | as s 2M(3) |
| s 2M(3)(b) | 232 | encoded | as s 2M(3) |
| s 2M(3)(c) | 233 | encoded | as s 2M(3) |
| Part 3 | 234 | inert (reason 1, not operative) | heading |
| s 3 | 235 | fork (F8) | F8; au-interpretation-time.l4 `the moment the enactment comes into operation` |
| s 3A | 237 | fork (F6) | F6, F7; au-interpretation-time.l4 `the day the enactment commences` |
| s 3A(1) | 238 | fork (F6) | F6, F7; as s 3A |
| s 3A(2) | 239 | fork (F6) | F6, F7; as s 3A |
| s 3A(3) | 240 | fork (F6) | F6, F7; as s 3A |
| s 4 | 241 | encoded | au-part3-commencement.l4 `section 4 allows the power to be exercised before the start time` etc. |
| s 4(1) | 243 | encoded | as s 4 |
| s 4(1)(a) | 244 | encoded | as s 4 |
| s 4(1)(b) | 245 | encoded | as s 4 |
| s 4(2) | 247 | encoded | as s 4 |
| s 4(3) | 248 | encoded | au-part3-more.l4 `anything may be done before the start time` |
| s 4(4) | 249 | encoded | as s 4 |
| s 4(4)(a) | 250 | encoded | as s 4 |
| s 4(4)(b) | 251 | encoded | as s 4 |
| s 4(4)(c) | 252 | encoded | as s 4 |
| s 4(5) | 253 | encoded | as s 4 |
| s 4(6) | 255 | encoded | au-part3-more.l4 `a single instrument may be made partly under subsection (2) and partly under an existing power` |
| s 4(7) | 257 | encoded | as s 4 |
| s 6 | 258 | encoded | au-part3-commencement.l4 `the printed date is evidence of the date of assent, and is to be judicially noticed` |
| Part 4 | 260 | inert (reason 1, not operative) | heading |
| s 7 | 261 | encoded | au-part4-repeal.l4 `what a repeal or amendment does to` etc. |
| s 7(1) | 263 | encoded | as s 7 |
| s 7(2) | 265 | encoded | as s 7 |
| s 7(2)(a) | 266 | encoded | as s 7 |
| s 7(2)(b) | 267 | encoded | as s 7 |
| s 7(2)(c) | 268 | encoded | as s 7 |
| s 7(2)(d) | 269 | encoded | as s 7 |
| s 7(2)(e) | 270 | encoded | as s 7 |
| s 7 Note @272 | 272 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 7(3) | 274 | encoded | as s 7 |
| s 7(3)(a) | 275 | encoded | as s 7 |
| s 7(3)(b) | 276 | encoded | as s 7 |
| s 7(3)(c) | 277 | encoded | as s 7 |
| s 7(3)(d) | 278 | encoded | as s 7 |
| s 7(4) | 279 | encoded | as s 7 |
| s 10 | 280 | encoded | au-part4-repeal.l4 `a reference to the short title of another Act includes that Act as amended from time to time` etc. |
| s 10(a) | 282 | encoded | as s 10 |
| s 10(b) | 283 | encoded | as s 10 |
| s 10(c) | 284 | encoded | as s 10 |
| s 10A | 285 | encoded | au-part4-repeal.l4 `a reference to a citation of a law of a State or Territory includes that law ...` etc. |
| s 10A(a) | 287 | encoded | as s 10A |
| s 10A(b) | 288 | encoded | as s 10A |
| s 10A(c) | 289 | encoded | as s 10A |
| s 11 | 290 | encoded | au-part4-repeal.l4 `an Act may be altered, amended or repealed in the same session of Parliament in which it was passed` |
| s 11A | 292 | fork (F22) | F22; au-part4-more.l4 (1) `the position of the inserted definition among the definitions, counting from 0`; (2) `the position of the inserted item among the items, counting from 0` |
| s 11A(1) | 294 | fork (F22) | F22; as s 11A |
| s 11A(2) | 296 | fork (F22) | F22; as s 11A |
| s 11A(2)(a) | 297 | encoded | as s 11A |
| s 11A(2)(b) | 298 | encoded | as s 11A |
| s 11B | 300 | encoded | au-part4-repeal.l4 `the term has that meaning in the non-amending provision` |
| s 11B(1) | 301 | encoded | as s 11B |
| s 11B(2) | 302 | encoded | as s 11B |
| s 11B(2)(a) | 303 | encoded | as s 11B |
| s 11B(2)(b) | 304 | encoded | as s 11B |
| s 11B(2)(c) | 305 | encoded | as s 11B |
| s 11B Note @307 | 307 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 11B(3) | 308 | encoded | as s 11B |
| Part 5 | 309 | inert (reason 1, not operative) | heading |
| s 12 | 310 | encoded | au-part5-readings.l4 `has effect as a substantive enactment without introductory words` |
| s 13 | 312 | encoded | au-part5-interpretation.l4 `is part of the Act` |
| s 13(1) | 313 | encoded | as s 13 |
| s 13(1)(a) | 314 | encoded | as s 13 |
| s 13(1)(b) | 315 | encoded | as s 13 |
| s 13(2) | 317 | encoded | as s 13 |
| s 13(2)(a) | 318 | encoded | as s 13 |
| s 13(2)(b) | 319 | encoded | as s 13 |
| s 13(2)(c) | 320 | encoded | as s 13 |
| s 13(2)(d) | 321 | encoded | as s 13 |
| s 13(3) | 322 | encoded | as s 13 |
| s 13(3)(a) | 323 | encoded | as s 13 |
| s 13(3)(b) | 324 | encoded | as s 13 |
| s 13(3)(c) | 325 | encoded | as s 13 |
| s 13 Note @326 | 326 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 15A | 327 | encoded | au-part5-readings.l4 `section 15A treats the enactment` |
| s 15AA | 329 | fork (F20) | F20; au-part5-readings.l4 `the interpretation to be preferred` |
| s 15AB | 331 | encoded | au-part5-interpretation.l4 `consideration may be given to the material` (1); au-part5-readings.l4 (2) `section 15AB(2) lists`, `listed material may be considered under section 15AB(1)`; (3) `regard must be had to` |
| s 15AB(1) | 332 | encoded | as s 15AB |
| s 15AB(1)(a) | 333 | encoded | as s 15AB |
| s 15AB(1)(b) | 334 | encoded | as s 15AB |
| s 15AB(1)(b)(i) | 335 | encoded | as s 15AB |
| s 15AB(1)(b)(ii) | 336 | encoded | as s 15AB |
| s 15AB(2) | 337 | encoded | as s 15AB |
| s 15AB(2)(a) | 338 | encoded | as s 15AB |
| s 15AB(2)(b) | 339 | encoded | as s 15AB |
| s 15AB(2)(c) | 340 | encoded | as s 15AB |
| s 15AB(2)(d) | 341 | encoded | as s 15AB |
| s 15AB(2)(e) | 342 | encoded | as s 15AB |
| s 15AB(2)(f) | 343 | encoded | as s 15AB |
| s 15AB(2)(g) | 344 | encoded | as s 15AB |
| s 15AB(2)(h) | 345 | encoded | as s 15AB |
| s 15AB(3) | 346 | encoded | as s 15AB |
| s 15AB(3)(a) | 347 | encoded | as s 15AB |
| s 15AB(3)(b) | 348 | encoded | as s 15AB |
| s 15AC | 349 | encoded | au-part5-readings.l4 `the ideas are taken to be different merely because different forms of words were used` |
| s 15AC(a) | 351 | encoded | as s 15AC |
| s 15AC(b) | 352 | encoded | as s 15AC |
| s 15AD | 354 | encoded | au-part5-readings.l4 (a) `the example is exhaustive`; (b) `the example may extend the operation of the provision` |
| s 15AD(a) | 356 | encoded | as s 15AD |
| s 15AD(b) | 357 | encoded | as s 15AD |
| s 15B | 358 | encoded | au-part5-interpretation.l4 (1), (2), (4)(a); au-part5-readings.l4 (3) `an Act in force in an external Territory is taken to have effect in its coastal sea as if it were part of the Territory`; (3A) `the reference to the external Territories is taken to include the coastal sea`; (4)(b) `is in the coastal sea of an external Territory` |
| s 15B(1) | 360 | encoded | as s 15B |
| s 15B(2) | 361 | encoded | as s 15B |
| s 15B(3) | 363 | encoded | as s 15B |
| s 15B(3A) | 364 | encoded | as s 15B |
| s 15B "coastal sea" | 366 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 15B(4) | 366 | encoded | as s 15B |
| s 15B(4)(a) | 367 | encoded | as s 15B |
| s 15B(4)(a)(i) | 368 | encoded | as s 15B |
| s 15B(4)(a)(ii) | 369 | encoded | as s 15B |
| s 15B(4)(b) | 371 | encoded | as s 15B |
| s 15B(4)(b)(i) | 372 | encoded | as s 15B |
| s 15B(4)(b)(ii) | 373 | encoded | as s 15B |
| s 15C | 375 | encoded | au-part5-interpretation.l4 `the jurisdiction the provision vests in the court` |
| s 15C(a) | 377 | encoded | as s 15C |
| s 15C(b) | 378 | encoded | as s 15C |
| s 15C(c) | 379 | encoded | as s 15C |
| s 16 | 380 | encoded | au-part5-readings.l4 `a reference in an Act is construed as a reference to` |
| s 16A | 382 | encoded | au-part5-readings.l4 `a reference to the Governor-General is deemed to include`, `the reference is read as acting with the advice of the Executive Council` |
| s 16A(a) | 384 | encoded | as s 16A |
| s 16A(b) | 385 | encoded | as s 16A |
| s 16B | 387 | encoded | au-part5-readings.l4 `a reference to the Governor of a State is deemed to include` |
| s 16BA | 389 | encoded | au-part5-readings.l4 `a reference to a judge includes` |
| s 16C | 391 | encoded | au-part5-readings.l4 (1), (3) `a reference to a Stipendiary Magistrate includes`; (2), (3) `a reference to a Magistrate includes` |
| s 16C(1) | 392 | encoded | as s 16C |
| s 16C(2) | 393 | fork (F18) | F18; as s 16C |
| s 16C(2)(a) | 394 | fork (F18) | F18; as s 16C |
| s 16C(2)(b) | 395 | fork (F18) | F18; as s 16C |
| s 16C(3) | 396 | encoded | as s 16C |
| s 17A | 397 | encoded | au-part5-readings.l4 `the words are deemed to refer to the Government Printer` |
| s 18A | 399 | encoded | au-part5-readings.l4 `has a corresponding meaning` |
| s 18B | 401 | encoded | au-part5-interpretation.l4 `the person may be referred to by this chair title` (1)-(3); au-part5-readings.l4 (4)-(6) |
| s 18B(1) | 403 | encoded | as s 18B |
| s 18B(1)(a) | 404 | encoded | as s 18B |
| s 18B(1)(b) | 405 | encoded | as s 18B |
| s 18B(1)(c) | 406 | encoded | as s 18B |
| s 18B(1)(d) | 407 | encoded | as s 18B |
| s 18B(2) | 408 | encoded | as s 18B |
| s 18B(2)(a) | 409 | encoded | as s 18B |
| s 18B(2)(b) | 410 | encoded | as s 18B |
| s 18B(2)(c) | 411 | encoded | as s 18B |
| s 18B(3) | 412 | encoded | as s 18B |
| s 18B(4) | 414 | encoded | as s 18B |
| s 18B(4)(a) | 415 | encoded | as s 18B |
| s 18B(4)(b) | 416 | encoded | as s 18B |
| s 18B(4)(c) | 417 | encoded | as s 18B |
| s 18B(4)(d) | 418 | encoded | as s 18B |
| s 18B(5) | 419 | encoded | as s 18B |
| s 18B(5)(a) | 420 | encoded | as s 18B |
| s 18B(5)(b) | 421 | encoded | as s 18B |
| s 18B(5)(c) | 422 | encoded | as s 18B |
| s 18B(6) | 423 | encoded | as s 18B |
| s 19 | 424 | encoded | au-part5-ministers.l4 (1) `the Ministers a reference means`; (2) `may be used to work out which Minister is referred to`; (3) `the most Ministers by or in relation to whom the thing must be done in a particular case`; (4) `a reference to a Minister is taken to include` |
| s 19(1) | 425 | encoded | as s 19 |
| s 19 table item 1 | 429 | encoded | as s 19 |
| s 19 table item 2 | 432 | encoded | as s 19 |
| s 19 table item 2(a) | 434 | encoded | as s 19 |
| s 19 table item 2(b) | 435 | encoded | as s 19 |
| s 19 table item 3 | 437 | encoded | as s 19 |
| s 19 table item 3(a) | 439 | encoded | as s 19 |
| s 19 table item 3(b) | 440 | encoded | as s 19 |
| s 19 table item 3(c) | 441 | fork (F21) | F21; as s 19 |
| s 19 table item 4 | 442 | encoded | as s 19 |
| s 19(2) | 445 | encoded | as s 19 |
| s 19(2)(a) | 446 | encoded | as s 19 |
| s 19(2)(b) | 447 | encoded | as s 19 |
| s 19 Note @448 | 448 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19(3) | 449 | encoded | as s 19 |
| s 19(4) | 451 | encoded | as s 19 |
| s 19A | 452 | encoded | au-part5-ministers.l4 (1) `the Departments a reference means`; (2) `may be used to work out which Department is identified` |
| s 19A(1) | 453 | encoded | as s 19A |
| s 19A table item 1 | 458 | encoded | as s 19A |
| s 19A table item 2 | 461 | encoded | as s 19A |
| s 19A table item 2(a) | 463 | encoded | as s 19A |
| s 19A table item 2(b) | 464 | encoded | as s 19A |
| s 19A table item 2(c) | 465 | encoded | as s 19A |
| s 19A table item 3 | 466 | encoded | as s 19A |
| s 19A Example @469 | 469 | encoded | asserted as a test |
| s 19A(2) | 470 | encoded | as s 19A |
| s 19A(2)(a) | 471 | encoded | as s 19A |
| s 19A(2)(b) | 472 | encoded | as s 19A |
| s 19A Note @473 | 473 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19B | 474 | encoded | au-part5-ministers.l4 (1) `section 19B applies`; (2), (6) `the Governor-General may make a substituted reference order`; (3) `the day on and after which the order has effect`, `the order is in effect on`; (4) `has effect according to its terms`; (5) `is a legislative instrument`; (7) `is an authority within section 19B` |
| s 19B(1) | 476 | encoded | as s 19B |
| s 19B(1)(a) | 477 | encoded | as s 19B |
| s 19B(1)(b) | 478 | encoded | as s 19B |
| s 19B(1)(b)(i) | 479 | encoded | as s 19B |
| s 19B(1)(b)(ii) | 480 | encoded | as s 19B |
| s 19B(1)(b)(iii) | 481 | encoded | as s 19B |
| s 19B(1)(b)(iv) | 482 | encoded | as s 19B |
| s 19B(2) | 484 | encoded | as s 19B |
| s 19B(2)(a) | 485 | encoded | as s 19B |
| s 19B(2)(b) | 486 | encoded | as s 19B |
| s 19B Note 1 @487 | 487 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19B Note 2 @488 | 488 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19B(3) | 489 | encoded | as s 19B |
| s 19B(4) | 490 | encoded | as s 19B |
| s 19B Note @491 | 491 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19B(5) | 492 | encoded | as s 19B |
| s 19B(6) | 494 | encoded | as s 19B |
| s 19B Note @495 | 495 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19B(6)(a) | 496 | encoded | as s 19B |
| s 19B(6)(b) | 497 | encoded | as s 19B |
| s 19B(7) | 499 | encoded | as s 19B |
| s 19B "authority" | 500 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 19B(7)(a) | 501 | encoded | as s 19B |
| s 19B(7)(b) | 502 | encoded | as s 19B |
| s 19B(7)(c) | 503 | encoded | as s 19B |
| s 19B(7)(d) | 504 | encoded | as s 19B |
| s 19B Note @505 | 505 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19C | 506 | encoded | au-part5-ministers.l4 (1) `section 19C applies`; (2) `the authorities an agreement is taken to refer to`; (3) `may be used to work out which authority is taken to be referred to`; (4) `is a determination for the purposes of item 3`; (5) `the most Ministers by or in relation to whom the agreement requires the thing to be done in a particular case`; (6) `is an authority within section 19C` |
| s 19C(1) | 508 | encoded | as s 19C |
| s 19C(1)(a) | 509 | encoded | as s 19C |
| s 19C(1)(b) | 510 | encoded | as s 19C |
| s 19C(1)(b)(i) | 511 | encoded | as s 19C |
| s 19C(1)(b)(ii) | 512 | encoded | as s 19C |
| s 19C(1)(b)(iii) | 513 | encoded | as s 19C |
| s 19C(1)(b)(iv) | 514 | encoded | as s 19C |
| s 19C(2) | 516 | encoded | as s 19C |
| s 19C table item 1 | 521 | encoded | as s 19C |
| s 19C table item 2 | 524 | encoded | as s 19C |
| s 19C table item 3 | 527 | encoded | as s 19C |
| s 19C table item 3(a) | 530 | encoded | as s 19C |
| s 19C table item 3(b) | 531 | encoded | as s 19C |
| s 19C(3) | 532 | encoded | as s 19C |
| s 19C(3)(a) | 533 | encoded | as s 19C |
| s 19C(3)(b) | 534 | encoded | as s 19C |
| s 19C Note @535 | 535 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19C(4) | 536 | encoded | as s 19C |
| s 19C Note 1 @537 | 537 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19C Note 2 @538 | 538 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19C(5) | 539 | encoded | as s 19C |
| s 19C(6) | 541 | encoded | as s 19C |
| s 19C "authority" | 542 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 19C(6)(a) | 543 | encoded | as s 19C |
| s 19C(6)(b) | 544 | encoded | as s 19C |
| s 19C(6)(c) | 545 | encoded | as s 19C |
| s 19C(6)(d) | 546 | encoded | as s 19C |
| s 19C Note @547 | 547 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19D | 548 | encoded | au-part5-ministers.l4 (1), (2), (4) `the purported exercise is not invalid merely because of the change`; (3) `a machinery of government change occurs`; (5) `is an authority within section 19D` |
| s 19D(1) | 550 | encoded | as s 19D |
| s 19D(1)(a) | 551 | encoded | as s 19D |
| s 19D(1)(b) | 552 | encoded | as s 19D |
| s 19D(1)(c) | 553 | encoded | as s 19D |
| s 19D(2) | 554 | encoded | as s 19D |
| s 19D(3) | 556 | encoded | as s 19D |
| s 19D(3)(a) | 557 | encoded | as s 19D |
| s 19D(3)(b) | 558 | encoded | as s 19D |
| s 19D(3)(c) | 559 | encoded | as s 19D |
| s 19D(3)(d) | 560 | encoded | as s 19D |
| s 19D(4) | 562 | encoded | as s 19D |
| s 19D(4)(a) | 563 | encoded | as s 19D |
| s 19D(4)(b) | 564 | encoded | as s 19D |
| s 19D(4)(c) | 565 | encoded | as s 19D |
| s 19D(5) | 567 | encoded | as s 19D |
| s 19D "authority" | 568 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 19D(5)(a) | 569 | encoded | as s 19D |
| s 19D(5)(b) | 570 | encoded | as s 19D |
| s 19D(5)(c) | 571 | encoded | as s 19D |
| s 19D(5)(d) | 572 | encoded | as s 19D |
| s 19D Note @573 | 573 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 19E | 574 | encoded | au-part5-ministers.l4 `the exercise is not invalid merely because the power is conferred on the other Minister` |
| s 20 | 576 | encoded | au-part5-readings.l4 `a reference to the holder or occupier includes the person` |
| s 20(a) | 578 | encoded | as s 20 |
| s 20(b) | 579 | encoded | as s 20 |
| s 21 | 580 | encoded | au-part5-readings.l4 `a reference in an Act to it is construed as` |
| s 21(1) | 581 | encoded | as s 21 |
| s 21(1)(a) | 582 | encoded | as s 21 |
| s 21(1)(b) | 583 | encoded | as s 21 |
| s 21(2) | 584 | encoded | as s 21 |
| s 21 "office" | 585 | encoded | au-part2-terms.l4 (table of meanings) |
| s 21 "officer" | 586 | encoded | au-part2-terms.l4 (table of meanings) |
| s 23 | 587 | encoded | au-part5-readings.l4 (a) `words importing a gender include`; (b) `words in a number include` |
| s 23(a) | 589 | encoded | as s 23 |
| s 23(b) | 590 | encoded | as s 23 |
| s 25A | 591 | encoded | au-part5-interpretation.l4 `the requirement is complied with` |
| s 25B | 593 | encoded | au-part5-interpretation.l4 `a reference to the former name is read as a reference to the new name`, `an alteration of the constitution of a body affects ...` |
| s 25B(1) | 594 | encoded | as s 25B |
| s 25B(1)(a) | 595 | encoded | as s 25B |
| s 25B(1)(b) | 596 | encoded | as s 25B |
| s 25B(1A) | 597 | encoded | as s 25B |
| s 25B(2) | 598 | encoded | as s 25B |
| s 25B(2)(a) | 599 | encoded | as s 25B |
| s 25B(2)(b) | 600 | encoded | as s 25B |
| s 25B(2)(c) | 601 | encoded | as s 25B |
| s 25B(2)(d) | 602 | encoded | as s 25B |
| s 25B(3) | 603 | encoded | the term table au-part2-terms.l4 |
| s 25B "office" | 604 | encoded | au-part2-terms.l4 (table of meanings) |
| s 25C | 605 | encoded | au-part5-interpretation.l4 `the form requirement is met` |
| s 25D | 607 | encoded | au-part5-interpretation.l4 `the written reasons are complete` |
| Part 6 | 609 | inert (reason 1, not operative) | heading |
| s 28A | 610 | encoded | au-part6-service.l4 `service by this method is permitted` |
| s 28A(1) | 611 | encoded | as s 28A |
| s 28A(1)(a) | 612 | encoded | as s 28A |
| s 28A(1)(a)(i) | 613 | encoded | as s 28A |
| s 28A(1)(a)(ii) | 614 | encoded | as s 28A |
| s 28A(1)(b) | 615 | encoded | as s 28A |
| s 28A Note @616 | 616 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 28A(2) | 617 | encoded | as s 28A |
| s 28A(2)(a) | 618 | encoded | as s 28A |
| s 28A(2)(b) | 619 | encoded | as s 28A |
| s 29 | 620 | fork (F14) | F14; au-interpretation-time.l4 `the day service by post is taken to be effected` |
| s 29(1) | 621 | fork (F14) | F14; as s 29 |
| s 29(2) | 622 | encoded | au-part6-more.l4 `section 29 stops section 160 of the Evidence Act 1995 operating` |
| Part 7 | 623 | inert (reason 1, not operative) | heading |
| s 33 | 624 | encoded | au-part7-powers.l4 (4)(b) `the last day of the 12 months for an acting appointment under section 33(4)`; au-part7-more.l4 (1) `what section 33(1) says is to be done`; (2A) `the act or thing may be done at the discretion of the person, court or body`; (2B) `the exercise or performance is affected merely because of a vacancy in the membership`; (3) `the power to make the instrument includes the power to do this to it`; (3AA) `the condition that governs doing this to the instrument`; (3A) `the power includes making the instrument in this way`; (3AB) `the person or authority may identify the matter by reference to a class or classes of matters`; (3AC) `it is a matter for subsections 33(3A) and 33(3AB)`; (3B) `the power is taken, by implication, not to include power to make provision for a particular aspect of a matter`; (4) `the power to make appointments includes this`, `the power may be exercised as the proviso to section 33(4) requires`, `the day the acting appointment under section 33(4) ends`; (5) `the limit on penalties prevents the instrument from requiring a statutory declaration` |
| s 33(1) | 626 | encoded | as s 33 |
| s 33(2A) | 628 | fork (F19) | F19; as s 33 |
| s 33(2B) | 630 | encoded | as s 33 |
| s 33(3) | 632 | encoded | as s 33 |
| s 33(3AA) | 633 | encoded | as s 33 |
| s 33(3AA)(a) | 634 | encoded | as s 33 |
| s 33(3AA)(b) | 635 | encoded | as s 33 |
| s 33 Example @637 | 637 | encoded | asserted as a test |
| s 33(3A) | 641 | encoded | as s 33 |
| s 33(3AB) | 642 | encoded | as s 33 |
| s 33(3AB)(a) | 643 | encoded | as s 33 |
| s 33(3AB)(b) | 644 | encoded | as s 33 |
| s 33 Note @646 | 646 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 33(3AC) | 647 | encoded | as s 33 |
| s 33(3B) | 648 | encoded | as s 33 |
| s 33(4) | 650 | encoded | as s 33 |
| s 33(4)(a) | 651 | encoded | as s 33 |
| s 33(4)(b) | 652 | fork (F11) | F11; au-part7-powers.l4 `the last day of the 12 months for an acting appointment under section 33(4)` |
| s 33(5) | 656 | encoded | as s 33 |
| s 33AA | 657 | encoded | au-part7-more.l4 `the power to make the appointment includes a power of reappointment` |
| s 33AB | 659 | encoded | au-part7-powers.l4 `the thing done is invalid merely because of this ground` |
| s 33AB(a) | 661 | encoded | as s 33AB |
| s 33AB(b) | 662 | encoded | as s 33AB |
| s 33AB(c) | 663 | encoded | as s 33AB |
| s 33AB(d) | 664 | encoded | as s 33AB |
| s 33A | 665 | encoded | au-part7-powers.l4 (1)(ba) `the last day the appointee may act in a vacant office`; (1)(c) `the day the continued acting ends`; au-part7-more.l4 (1) `section 33A(1) applies to the appointment`; (1)(a), (b) `the appointer may do this under section 33A(1)`; (1)(d) `the appointment ceases to have effect on the appointee's resignation`; (1)(e) `the appointee has this while acting in the office`; (2) `the person acting by operation of law has this while acting in the office`; (3) `the thing done is invalid merely because of this ground for purported acting`; (4) the term table au-part2-terms.l4 |
| s 33A(1) | 667 | encoded | as s 33A |
| s 33A(1)(a) | 668 | encoded | as s 33A |
| s 33A(1)(b) | 669 | encoded | as s 33A |
| s 33A(1)(b)(i) | 670 | encoded | as s 33A |
| s 33A(1)(b)(ii) | 671 | encoded | as s 33A |
| s 33A(1)(ba) | 672 | fork (F10) | F10; au-part7-powers.l4 `the last day the appointee may act in a vacant office` |
| s 33A(1)(c) | 673 | fork (F10) | F10; au-part7-powers.l4 `the day the continued acting ends` |
| s 33A(1)(c)(i) | 674 | fork (F10) | F10; as s 33A(1)(c) |
| s 33A(1)(c)(ii) | 675 | fork (F10) | F10; as s 33A(1)(c) |
| s 33A(1)(c)(iii) | 676 | fork (F10) | F10; as s 33A(1)(c) |
| s 33A(1)(d) | 678 | encoded | as s 33A |
| s 33A(1)(e) | 679 | encoded | as s 33A |
| s 33A(1)(e)(i) | 680 | encoded | as s 33A |
| s 33A(1)(e)(ii) | 681 | encoded | as s 33A |
| s 33A(2) | 683 | encoded | as s 33A |
| s 33A(2)(a) | 684 | encoded | as s 33A |
| s 33A(2)(b) | 685 | encoded | as s 33A |
| s 33A(3) | 686 | encoded | as s 33A |
| s 33A(4) | 688 | encoded | as s 33A |
| s 33A "office" | 689 | encoded | au-part2-terms.l4 (table of meanings) |
| s 33B | 690 | encoded | au-part7-more.l4 (1) `section 33B applies to the body`; (2) `the body may permit its members to participate by this means`; (3) `the member is taken to be present at the meeting and to form part of any quorum`; (4) `all the members may participate by this means`; (5) `the meeting may be held at that number of places at the same time` |
| s 33B(1) | 691 | encoded | as s 33B |
| s 33B(2) | 692 | encoded | as s 33B |
| s 33B(2)(a) | 693 | encoded | as s 33B |
| s 33B(2)(b) | 694 | encoded | as s 33B |
| s 33B(2)(c) | 695 | encoded | as s 33B |
| s 33B(3) | 696 | encoded | as s 33B |
| s 33B(4) | 697 | encoded | as s 33B |
| s 33B(5) | 698 | encoded | as s 33B |
| s 34 | 699 | fork (F23) | F23; au-part7-more.l4 `the person authorised to hear and determine the matter has authority to do this` |
| s 34AAA | 701 | encoded | au-part7-more.l4 `the person who exercises the power or performs the function or duty` |
| s 34AAB | 703 | encoded | au-part7-more.l4 (1) `the Minister may authorise this person to act on the Minister's behalf`; (2) `the authorisation extends to the function, duty or power`; (3) `an authorisation may be expressed in this way`, `the authorisation continues to have effect`; (4) `the authorisation may be revoked at any time`; (5) `it complies with subsection 34AAB(5)`; (6) `section 34AAB stops the giving of an authorisation under that other power` |
| s 34AAB(1) | 704 | encoded | as s 34AAB |
| s 34AAB(1)(a) | 705 | encoded | as s 34AAB |
| s 34AAB(1)(b) | 706 | encoded | as s 34AAB |
| s 34AAB(2) | 708 | encoded | as s 34AAB |
| s 34AAB(3) | 709 | encoded | as s 34AAB |
| s 34AAB(3)(a) | 710 | encoded | as s 34AAB |
| s 34AAB(3)(b) | 711 | encoded | as s 34AAB |
| s 34AAB(4) | 712 | encoded | as s 34AAB |
| s 34AAB(5) | 713 | encoded | as s 34AAB |
| s 34AAB(6) | 714 | encoded | as s 34AAB |
| s 34AA | 715 | encoded | au-part7-more.l4 `the power of delegation includes delegating to a delegate described in this way` |
| s 34AB | 717 | encoded | au-part7-more.l4 (1)(a) `the delegation may be made in this way`; (1)(b) `the power to delegate is among the powers that may be delegated`; (1)(c) `for the purposes of the Act it is deemed to have been performed or exercised by the authority`; (1)(d) `the delegation prevents the authority from performing or exercising the function, duty or power`; (1)(e) `section 34A applies to the authority as if it were a person`; (2) `the delegation is taken to include the additional functions, duties or powers on this day`; (3) `the delegation is taken to include the functions, duties or powers as altered on this day` |
| s 34AB(1) | 719 | encoded | as s 34AB |
| s 34AB(1)(a) | 720 | encoded | as s 34AB |
| s 34AB(1)(b) | 721 | encoded | as s 34AB |
| s 34AB(1)(c) | 722 | encoded | as s 34AB |
| s 34AB(1)(d) | 723 | encoded | as s 34AB |
| s 34AB(1)(e) | 724 | encoded | as s 34AB |
| s 34AB(2) | 726 | encoded | as s 34AB |
| s 34AB(2)(a) | 727 | encoded | as s 34AB |
| s 34AB(2)(b) | 728 | encoded | as s 34AB |
| s 34AB(2)(c) | 729 | encoded | as s 34AB |
| s 34AB(3) | 732 | encoded | as s 34AB |
| s 34AB(3)(a) | 733 | encoded | as s 34AB |
| s 34AB(3)(b) | 734 | encoded | as s 34AB |
| s 34AB(3)(c) | 735 | encoded | as s 34AB |
| s 34A | 737 | encoded | au-part7-powers.l4 `the delegate may act on the delegate's own opinion, belief or state of mind` |
| s 34A(a) | 739 | encoded | as s 34A |
| s 34A(b) | 740 | encoded | as s 34A |
| s 34B | 742 | encoded | au-part7-powers.l4 (1) `it is sufficient compliance in relation to a House`; au-part7-more.l4 (1A) `the paper is deemed to have been presented to the House as the Act or law describes`, `the person by whom the presentation is deemed to have been effected or caused`; (2) the term table au-part2-terms.l4 ("paper") |
| s 34B(1) | 743 | encoded | as s 34B |
| s 34B(1)(a) | 744 | encoded | as s 34B |
| s 34B(1)(b) | 745 | encoded | as s 34B |
| s 34B(1)(c) | 746 | encoded | as s 34B |
| s 34B(1A) | 747 | encoded | as s 34B |
| s 34B(1A)(а) | 748 | encoded | as s 34B |
| s 34B(1A)(b) | 749 | encoded | as s 34B |
| s 34B "paper" | 751 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 34B(2) | 751 | encoded | as s 34B |
| s 34B(2)(a) | 752 | encoded | as s 34B |
| s 34B(2)(b) | 753 | encoded | as s 34B |
| s 34B(2)(c) | 754 | encoded | as s 34B |
| s 34C | 755 | encoded | au-part7-powers.l4 the rules named `the last day ...` and `section 34C applies to`; au-part7-more.l4 (5) `the Minister may grant the extension`; (6)(b) `the person furnishes the report within the period as extended` |
| s 34C(1) | 756 | encoded | as s 34C |
| s 34C "periodic report" | 757 | fork (F17) | F17; au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 34C(1)(a) | 758 | encoded | as s 34C |
| s 34C(1)(b) | 759 | encoded | as s 34C |
| s 34C "person" | 761 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 34C(2) | 762 | encoded | as s 34C |
| s 34C(3) | 763 | fork (F12) | F12; au-part7-powers.l4 `the last day for the Minister to lay the report before a House` |
| s 34C(4) | 764 | encoded | as s 34C |
| s 34C(5) | 765 | encoded | au-part7-more.l4 `the Minister may grant the extension` |
| s 34C(6) | 766 | encoded | as s 34C |
| s 34C(6)(a) | 767 | fork (F12) | F12; au-part7-powers.l4 `the last day for the Minister to lay the extension statement before a House` |
| s 34C(6)(b) | 768 | encoded | au-part7-more.l4 `the person furnishes the report within the period as extended` |
| s 34C(6)(c) | 769 | fork (F12) | F12; au-part7-powers.l4 `the last day for the Minister to lay the extended report before a House` |
| s 34C(7) | 770 | encoded | as s 34C |
| s 34C(7)(a) | 771 | encoded | as s 34C |
| s 34C(7)(b) | 772 | fork (F12) | F12; au-part7-powers.l4 `the last day for the Minister to lay the late-report statement before a House` |
| s 34C(7A) | 773 | encoded | as s 34C |
| s 34C(7A)(a) | 774 | encoded | as s 34C |
| s 34C(7A)(b) | 775 | encoded | as s 34C |
| s 34C(8) | 776 | encoded | as s 34C |
| Part 8 | 777 | inert (reason 1, not operative) | heading |
| s 35 | 778 | encoded | au-part8-distance.l4 `the distance for the purposes of an Act` |
| s 36 | 780 | encoded | au-interpretation-time.l4 (see the rows below) |
| s 36(1) | 781 | fork (F4) | F4 (the length of a week and of a year is not stated); au-interpretation-time.l4 `the first day of the period`, `the last day of the period`, `the last day of a period of` |
| s 36 table item 1 | 786 | encoded | as s 36 |
| s 36 table item 2 | 789 | encoded | as s 36 |
| s 36 table item 3 | 792 | encoded | as s 36 |
| s 36 table item 4 | 795 | encoded | as s 36 |
| s 36 table item 5 | 798 | encoded | as s 36 |
| s 36 table item 6 | 801 | encoded | as s 36 |
| s 36 table item 7 | 804 | encoded | as s 36 |
| s 36 Example 1 @807 | 807 | encoded | asserted as a test |
| s 36 Example 2 @808 | 808 | encoded | asserted as a test |
| s 36 Example 3 @809 | 809 | encoded | asserted as a test |
| s 36 Example 4 @810 | 810 | encoded | asserted as a test |
| s 36 Example 5 @811 | 811 | encoded | asserted as a test |
| s 36 Example 6 @812 | 812 | encoded | asserted as a test |
| s 36 Example 7 @813 | 813 | encoded | asserted as a test |
| s 36(2) | 814 | fork (F3) | F3, F9; au-interpretation-time.l4 `the last day on which the thing may be done`, `the thing is done within the time allowed` |
| s 36(2)(a) | 815 | fork (F3) | F3, F9; as s 36(2) |
| s 36(2)(b) | 816 | fork (F3) | F3, F9; as s 36(2) |
| s 36 Example @818 | 818 | encoded | asserted as a test |
| s 36(3) | 819 | fork (F5) | F5; au-interpretation-time.l4 `is a holiday for the time for doing a thing` |
| s 36 "holiday" | 820 | fork (F5) | F5; au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 36(3)(a) | 821 | fork (F5) | F5; as s 36(3) |
| s 36(3)(b) | 822 | fork (F5) | F5; as s 36(3) |
| s 37 | 823 | encoded | au-part8-more.l4 `the time a reference to time in an Act means` |
| s 37A | 825 | fork (F15) | F15; au-interpretation-time.l4 `the moment a person attains the age` |
| Part 9 | 827 | inert (reason 1, not operative) | heading |
| s 38 | 828 | encoded | au-part9-citation.l4 `the term by which an Act of this body may be referred to` |
| s 38(1) | 829 | encoded | as s 38 |
| s 38(2) | 830 | encoded | as s 38 |
| s 38(3) | 831 | encoded | as s 38 |
| s 38(4) | 832 | encoded | as s 38 |
| s 39 | 833 | encoded | au-part9-citation.l4 `the number given to the Act` |
| s 40 | 835 | encoded | au-part9-citation.l4 `it may be cited this way in an Act, instrument or document` |
| s 40(1A) | 837 | encoded | as s 40 |
| s 40(1A)(a) | 838 | encoded | as s 40 |
| s 40(1A)(a)(i) | 839 | encoded | as s 40 |
| s 40(1A)(a)(ii) | 840 | encoded | as s 40 |
| s 40(1A)(a)(iii) | 841 | encoded | as s 40 |
| s 40(1A)(b) | 842 | encoded | as s 40 |
| s 40(1A)(b)(i) | 843 | encoded | as s 40 |
| s 40(1A)(b)(ii) | 844 | encoded | as s 40 |
| s 40(1A)(b)(iii) | 845 | encoded | as s 40 |
| s 40(1A)(b)(iv) | 846 | encoded | as s 40 |
| s 40(1A)(b)(v) | 847 | encoded | as s 40 |
| s 40(1) | 849 | encoded | as s 40 |
| s 40(1)(b) | 850 | encoded | as s 40 |
| s 40(1)(c) | 851 | encoded | as s 40 |
| s 40(1)(d) | 852 | encoded | as s 40 |
| s 40(2) | 853 | encoded | as s 40 |
| s 40A | 854 | encoded | au-part9-citation.l4 `the reference is taken to include the corresponding old provision and any relevant earlier law` (1)-(3), (5); au-part9-more.l4 (4); the term table au-part2-terms.l4 (6) |
| s 40A(1) | 855 | encoded | as s 40A |
| s 40A(1)(a) | 856 | encoded | as s 40A |
| s 40A(1)(b) | 857 | encoded | as s 40A |
| s 40A(1)(c) | 859 | encoded | as s 40A |
| s 40A(1)(d) | 860 | encoded | as s 40A |
| s 40A(2) | 861 | encoded | as s 40A |
| s 40A(2)(a) | 862 | encoded | as s 40A |
| s 40A(2)(b) | 863 | encoded | as s 40A |
| s 40A(2)(c) | 864 | encoded | as s 40A |
| s 40A(2)(d) | 865 | encoded | as s 40A |
| s 40A(3) | 866 | encoded | as s 40A |
| s 40A(3)(a) | 867 | encoded | as s 40A |
| s 40A(3)(b) | 868 | encoded | as s 40A |
| s 40A(4) | 869 | encoded | au-part9-more.l4 `the Part that decides whether a provision of the old legislation corresponds to one of the new`, `the old provision corresponds to the new provision for section 40A` |
| s 40A(4)(a) | 870 | encoded | as s 40A(4) |
| s 40A(4)(b) | 871 | encoded | as s 40A(4) |
| s 40A(5) | 872 | encoded | as s 40A |
| s 40A(6) | 873 | encoded | the term table au-part2-terms.l4 |
| s 40A "new ASIC legislation" | 874 | encoded | au-part2-terms.l4 (table of meanings) |
| s 40A "new corporations legislation" | 875 | encoded | au-part2-terms.l4 (table of meanings) |
| s 40A "old ASIC legislation" | 876 | encoded | au-part2-terms.l4 (table of meanings) |
| s 40A "old corporations legislation" | 877 | encoded | au-part2-terms.l4 (table of meanings) |
| s 40A "relevant earlier law" | 878 | encoded | au-part2-terms.l4 (table of meanings; the printed list is also split into its members) |
| s 40A(6)(a) | 879 | encoded | as s 40A(6) |
| s 40A(6)(b) | 880 | encoded | as s 40A(6) |
| Part 10 | 881 | inert (reason 1, not operative) | heading |
| s 46 | 882 | encoded | au-part10-11-instruments.l4 `this Act applies to the instrument as if it were an Act ...` etc. |
| s 46(1) | 883 | encoded | as s 46 |
| s 46(1)(a) | 884 | encoded | as s 46 |
| s 46(1)(b) | 885 | encoded | as s 46 |
| s 46(1)(c) | 886 | encoded | as s 46 |
| s 46(2) | 887 | encoded | as s 46 |
| s 46(3) | 888 | encoded | as s 46 |
| s 46 Note @889 | 889 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 46AA | 890 | encoded | au-part10-11-instruments.l4 `the instrument may apply, adopt or incorporate the matter at this time` |
| s 46AA(1) | 891 | encoded | as s 46AA |
| s 46AA(1)(a) | 892 | encoded | as s 46AA |
| s 46AA(1)(a)(i) | 893 | encoded | as s 46AA |
| s 46AA(1)(a)(ii) | 894 | encoded | as s 46AA |
| s 46AA(1)(a)(iii) | 895 | encoded | as s 46AA |
| s 46AA(1)(b) | 896 | encoded | as s 46AA |
| s 46AA(1)(b)(i) | 897 | encoded | as s 46AA |
| s 46AA(1)(b)(ii) | 898 | encoded | as s 46AA |
| s 46AA(2) | 899 | encoded | as s 46AA |
| s 46AA(3) | 900 | encoded | as s 46AA |
| s 46AA(3)(a) | 901 | encoded | as s 46AA |
| s 46AA(3)(b) | 902 | encoded | as s 46AA |
| s 46AA Note 1 @903 | 903 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 46AA Note 2 @904 | 904 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 46AA(4) | 906 | encoded | as s 46AA |
| s 46AA Note @907 | 907 | inert (reason 1, not operative) | a Note: it explains and cross-refers, and is not operative text |
| s 47 | 908 | encoded | au-part10-11-instruments.l4 `this part of the resolution is valid` |
| Part 11 | 910 | inert (reason 1, not operative) | heading |
| s 51 | 911 | encoded | au-part10-11-instruments.l4 `the Governor-General may make regulations prescribing the matter` (a regulation-making power: machinery, reason 2, kept encoded because pass 1 encoded it and the rule is free of cost) |
| s 51(a) | 913 | encoded | as s 51 |
| s 51(b) | 914 | encoded | as s 51 |

### Rows: the compilation's apparatus

| unit | lines | disposition | where it is encoded, or why not |
|---|---|---|---|
| front matter @1 | 1 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @2 | 2 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @3 | 3 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @4 | 4 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @5 | 5 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @6 | 6 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @7 | 7 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @8 | 8 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @9 | 9 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @10 | 10 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @11 | 11 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @12 | 12 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @13 | 13 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @14 | 14 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @15 | 15 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @16 | 16 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @17 | 17 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @18 | 18 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @19 | 19 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @20 | 20 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @21 | 21 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @22 | 22 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| front matter @23 | 23 | inert (reason 1, not operative) | title, number, compilation details or heading of the compilation; states no rule of the Act |
| endnote 1 | 916-934 | inert (reason 1, not operative) | endnote text: the compilation's own record |
| endnote 2 | 935-982 | inert (reason 1, not operative) | endnote text: the compilation's own record |
| en2 key ad | 936 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key orig | 937 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key am | 938 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key p | 939 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key amdt | 940 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key para | 941 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key C[x] | 942 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key ch | 944 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key pres | 945 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key cl | 946 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key prev | 947 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key cont. | 948 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key (prev…) | 949 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key def | 950 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key pt | 951 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key Dict | 952 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key r | 953 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key disallowed | 954 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key reloc | 955 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key div | 956 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key renum | 957 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key ed | 958 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key rep | 959 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key exp | 960 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key rs | 961 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key s | 963 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key gaz | 964 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key LA | 966 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key sch | 967 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key LIA | 968 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key SLI | 969 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key (md) | 970 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key SR | 971 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key sub ch | 973 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key (md not incorp) | 974 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key sub div | 975 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key sub pt | 977 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key mod | 978 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key underlining | 979 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key No. | 980 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| en2 key Ord | 982 | inert (reason 1, not operative) | abbreviation key entry: explains the endnotes |
| endnote 3 | 983-1391 | inert (reason 1, not operative) | endnote text: the compilation's own record |
| en3 Acts Interpretation Act 1901 (2, 1901) | 989 | encoded | au-part1-application.l4 `the day this Act was assented to`, `the day this Act commenced` |
| en3 Acts Interpretation Act 1916 (4, 1916) | 993 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1918 (8, 1918) | 998 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1930 (23, 1930) | 1003 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1932 (24, 1932) | 1008 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1937 (10, 1937) | 1013 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1941 (7, 1941) | 1018 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Defence (Transitional Provisions) Act 1947 (78, 1947) | 1023 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1948 (79, 1948) | 1028 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act 1950 (80, 1950) | 1033 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1957 (69, 1957) | 1038 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1963 (19, 1963) | 1043 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1964 (52, 1964) | 1048 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision (Decimal Currency) Act 1966 (93, 1966) | 1053 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Act 1973 (79, 1973) | 1058 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act 1973 (216, 1973) | 1063 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Citation Act 1976 (37, 1976) | 1068 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 1976 (144, 1976) | 1073 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 1978 (35, 1978) | 1078 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 1980 (1, 1980) | 1083 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act 1981 (61, 1981) | 1088 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Amendments) Act (No. 1) 1982 (26, 1982) | 1093 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Amendments) Act (No. 2) 1982 (80, 1982) | 1099 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Amendments) Act (No. 2) 1982 (80, 1982) (second row, line 1104) | 1104 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act (No. 1) 1983 (39, 1983) | 1109 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 1984 (27, 1984) | 1114 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act (No. 2) 1984 (165, 1984) | 1120 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Public Service Reform Act 1984 (63, 1984) | 1125 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act (No. 2) 1984 (165, 1984) (second row, line 1131) | 1131 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act (No. 1) 1984 (72, 1984) | 1136 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act (No. 2) 1985 (193, 1985) | 1141 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Administrative Arrangements Act 1987 (92, 1987) | 1146 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Crimes Legislation Amendment Act 1987 (120, 1987) | 1151 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law (Miscellaneous Provisions) Act 1987 (141, 1987) | 1156 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statutory Instruments (Tabling and Disallowance) Legislation Amendment Act 1988 (99, 1988) | 1161 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment Act 1988 (120, 1988) | 1166 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Crimes Legislation Amendment Act 1989 (108, 1989) | 1171 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Corporations Legislation Amendment Act 1990 (110, 1990) | 1176 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment Act 1990 (115, 1990) | 1181 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment Act 1991 (136, 1991) | 1186 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Territories Law Reform Act 1992 (104, 1992) | 1191 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment Act 1994 (84, 1994) | 1196 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Evidence (Transitional Provisions and Consequential Amendments) Act 1995 (3, 1995) | 1201 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Audit (Transitional and Miscellaneous) Amendment Act 1997 (152, 1997) | 1206 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Financial Sector Reform (Amendments and Transitional Provisions) Act 1998 (54, 1998) | 1211 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 1998 (125, 1998) | 1216 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Public Employment (Consequential and Transitional) Amendment Act 1999 (146, 1999) | 1221 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Corporate Law Economic Reform Program Act 1999 (156, 1999) | 1226 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Australian Security Intelligence Organisation Legislation Amendment Act 1999 (161, 1999) | 1231 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Federal Magistrates (Consequential Amendments) Act 1999 (194, 1999) | 1236 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Corporations (Repeals, Consequentials and Transitionals) Act 2001 (55, 2001) | 1241 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Intelligence Services (Consequential Provisions) Act 2001 (153, 2001) | 1246 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act 2002 (63, 2002) | 1251 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment (Court Procedures) Act 2003 (46, 2003) | 1256 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Legislative Instruments Act 2003 (139, 2003) | 1261 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Legislative Instruments (Transitional Provisions and Consequential Amendments) Act 2003 (140, 2003) | 1266 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Financial Framework Legislation Amendment Act 2005 (8, 2005) | 1271 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment (Legislative Instruments) Act 2005 (133, 2005) | 1276 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act 2008 (73, 2008) | 1281 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Same-Sex Relationships (Equal Treatment in Commonwealth Laws—Superannuation) Act 2008 (134, 2008) | 1286 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Evidence Amendment Act 2008 (135, 2008) | 1291 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts Interpretation Amendment Act 2011 (46, 2011) | 1296 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Privacy Amendment (Enhancing Privacy Protection) Act 2012 (197, 2012) | 1301 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Federal Circuit Court of Australia (Consequential Amendments) Act 2013 (13, 2013) | 1306 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Charities (Consequential Amendments and Transitional Provisions) Act 2013 (96, 2013) | 1311 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Statute Law Revision Act (No. 1) 2015 (5, 2015) | 1316 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts and Instruments (Framework Reform) Act 2015 (10, 2015) | 1321 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts and Instruments (Framework Reform) (Consequential Provisions) Act 2015 (126, 2015) | 1327 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Acts and Instruments (Framework Reform) (Consequential Provisions) Act 2015 (126, 2015) (second row, line 1332) | 1332 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment (Northern Territory Local Court) Act 2016 (26, 2016) | 1337 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Territories Legislation Amendment Act 2016 (33, 2016) | 1342 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Marriage Amendment (Definition and Religious Freedoms) Act 2017 (129, 2017) | 1347 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Intelligence Services Amendment (Establishment of the Australian Signals Directorate) Act 2018 (25, 2018) | 1352 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Legislation Amendment (Sunsetting Review and Other Measures) Act 2018 (78, 2018) | 1357 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Civil Law and Justice Legislation Amendment Act 2018 (C2018A00130) (130, 2018) | 1367 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Office of National Intelligence (Consequential and Transitional Provisions) Act 2018 (C2018A00156) (156, 2018) | 1372 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 National Security Legislation Amendment (Comprehensive Review and Other Measures No. 2) Act 2023 (C2023A00053) (53, 2023) | 1377 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Crown References Amendment Act 2024 (C2024A00115) (115, 2024) | 1382 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| en3 Law and Justice Legislation Amendment (New South Wales Local Court) Act 2026 (C2026A00004) (4, 2026) | 1387 | inert (reason 1, not operative) | legislation history row: an amending law and its dates; records history and states no rule |
| endnote 4 | 1392-1880 | inert (reason 1, not operative) | endnote text: the compilation's own record |
| en4 Part 1 | 1395 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part I heading | 1396-1398 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 1 heading | 1399-1400 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 1 | 1401-1402 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 1A | 1403-1405 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2 | 1406-1410 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2A | 1411-1416 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 2 | 1417 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 2 (again, #2) | 1418-1419 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2B | 1420-1422 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2C | 1423-1424 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2CA | 1425-1426 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2D | 1427-1428 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2E | 1429-1430 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2F | 1431-1432 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2G | 1433-1434 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2H | 1435-1436 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2J | 1437-1438 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2K | 1439-1440 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2L | 1441-1442 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 2M | 1443-1444 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 3 | 1445 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part II heading | 1446-1448 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 3 heading | 1449-1450 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 3 | 1451-1452 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 3 | 1453-1454 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 3A | 1455-1456 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 4 | 1457-1460 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 5 | 1461-1463 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 6 | 1464-1465 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 4 | 1466 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part III heading | 1467-1469 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 4 heading | 1470-1471 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 7 | 1472-1473 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 7 | 1474-1475 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 8 | 1476-1477 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 8A | 1478-1480 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 8B | 1481-1483 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 8C | 1484-1486 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 9 | 1487-1488 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 10 | 1489-1491 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 10A | 1492-1496 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 11 | 1497-1498 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 11A | 1499-1500 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 11B | 1501-1502 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 5 | 1503 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part IV heading | 1504-1506 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 5 heading | 1507-1508 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 12 | 1509-1510 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 13 | 1511-1514 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 14 | 1515-1516 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 14A | 1517-1519 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 14B | 1520-1522 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 15 | 1523-1524 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 15A | 1525-1527 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15AA | 1528-1531 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15AB | 1532-1533 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15AC | 1534-1535 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15AD | 1536-1538 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15AE | 1539-1541 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 15B | 1542-1544 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 15C | 1545-1548 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part V heading | 1549-1551 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Heading preceding s 16 | 1552-1553 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 16 | 1554-1555 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 16A | 1556-1558 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 16B | 1559-1561 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 16BA | 1562-1564 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 16C | 1565-1567 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 17 | 1568-1570 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 17AA | 1571-1573 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 17A | 1574-1576 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 18 | 1577-1579 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 18A | 1580-1582 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 18B | 1583-1586 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 18C | 1587-1589 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 19 | 1590-1592 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 19A | 1593-1601 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 19B | 1602-1608 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 19BA | 1609-1612 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 19BAA | 1613-1615 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 19BB | 1616-1619 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 19BC | 1620-1623 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 19BD | 1624-1626 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 19C | 1627-1630 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 19D | 1631-1633 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 19E | 1634-1635 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 20 | 1636-1638 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 21 | 1639-1640 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 22 | 1641-1643 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 22A | 1644-1646 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 22B | 1647-1649 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 22C | 1650-1652 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 23 | 1653-1655 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 24 | 1656-1658 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 25 | 1659-1662 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 25A | 1663-1664 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 25B | 1665-1667 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 25C | 1668-1670 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 25D | 1671-1672 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 25E | 1673-1675 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 6 | 1676 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part VI heading | 1677-1679 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 6 heading | 1680-1681 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 26 | 1682-1683 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 26 | 1684-1686 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 27 | 1687-1689 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 27A | 1690-1692 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 28 | 1693-1694 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 s 28A | 1695-1698 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 29 | 1699-1701 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 30 | 1702-1704 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 31 | 1705-1706 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 Part 7 | 1707 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part VII heading | 1708-1710 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 7 heading | 1711-1712 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 32 | 1713-1715 | repealed or blank in this text | the text shows it repealed: rep No 10, 1937 |
| en4 Heading preceding s 33 | 1716-1717 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 33 | 1718-1719 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 33AA | 1720-1721 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 33AB | 1722-1723 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 33A | 1724-1726 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 33B | 1727-1729 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34 | 1730-1732 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34AAA | 1733-1734 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34AAB | 1735-1736 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34AA | 1737-1739 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34AB | 1740-1742 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34A | 1743-1746 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34B | 1747-1749 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 34C | 1750-1752 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 8 | 1753 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part VIII heading | 1754-1756 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 8 heading | 1757-1758 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 35 | 1759-1760 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 35 | 1761-1762 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 36 | 1763-1765 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 37 | 1766-1767 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 37A | 1768-1769 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 9 | 1770 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part IX heading | 1771-1773 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 9 heading | 1774-1776 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 38 | 1777-1778 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 38 | 1779-1780 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 39 | 1781-1782 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 40 | 1783-1784 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 40A | 1785-1788 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part X heading | 1789-1791 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 Part X | 1792-1793 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 Heading preceding s 41 | 1794-1796 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 41 | 1797-1799 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 42 | 1800-1803 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 43 | 1804-1807 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 44 | 1808-1810 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 45 | 1811-1813 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 45A | 1814-1816 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 s 45B | 1817-1819 | repealed or blank in this text | the text shows it repealed: rep No 120, 1987 |
| en4 Part 10 | 1820 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part XI heading | 1821-1824 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 10 heading | 1825-1827 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 46 | 1828-1830 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 46 | 1831-1835 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 46A | 1836-1839 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 46AA | 1840-1842 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 s 46B | 1843-1846 | repealed or blank in this text | the text shows it repealed: rep No 10, 2015 |
| en4 s 47 | 1847-1849 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part 11 | 1850 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Part XII heading | 1851-1853 | repealed or blank in this text | the text shows it repealed: rep No 46, 2011 |
| en4 Part 11 heading | 1854-1855 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |
| en4 Heading preceding s 48 | 1856-1858 | repealed or blank in this text | the text shows it repealed: rep No 52, 1964 |
| en4 s 48 | 1859-1862 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 48A | 1863-1865 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 48B | 1866-1868 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 49 | 1869-1872 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 49A | 1873-1875 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 50 | 1876-1878 | repealed or blank in this text | the text shows it repealed: rep No 140, 2003 |
| en4 s 51 | 1879-1880 | inert (reason 1, not operative) | amendment history entry: records which law changed the provision; states no rule |

<!-- END coverage -->

## Fork register

Each fork is a place the text leaves open or can be read two ways.
The fork ids F1 to F6 are also the headings of tests in `au-tests-time.l4`.
F1 to F17 are from pass 1; F18 to F23 were found in pass 2.
The coverage table marks every unit that rests on a fork with `fork` and the fork id in its note.
F18 and F19 are dates the text does not give; F20 to F23 are choices the text does not decide.

| id | question | readings seen | reading taken | text that licenses it |
|---|---|---|---|---|
| F1 | Does a period "from" a day, or "after" it, count that day? | (A) the day is excluded; (B) it is counted, so that s 2G, which counts months from "the start of any day", applies from that day | (A) for "from" and "after"; the day is counted for "at, on or with" and "between". A month from 15 December therefore ends on 15 January, whereas a month starting on 15 December ends on 14 January | s 36(1) table items 5 and 6; Examples 5, 6 and 7; s 2G(1) Example 1 |
| F2 | Is the last day inside the period? | (A) always; (B) never; (C) depends on the wording | (C): items 3 and 4 ("until", "end at, on or with") include it; item 7 ("end before") excludes it | s 36(1) table items 3, 4, 7; Examples 3, 4, 7 |
| F3 | Does the rest-day rule move the last day of a period counted in months or years, and what if several days in a row are rest days? | (A) only periods in days; (B) any period; (C) the next day, or the next day that is not a Saturday, a Sunday or a holiday | (B) and the next day that is not one: consecutive Saturday, Sunday and a holiday Monday are skipped together | s 36(2) speaks of "the last day for doing the thing" with no unit and of "the next day that is not a Saturday, a Sunday or a holiday" |
| F4 | How long is a week, and a year? | (A) not stated, so no answer; (B) a week is 7 days and a year is 12 months | (A) in the ordinary rules (NOTHING); (B) only in separately named ALTERNATIVE READING functions and in the seat question that says in its title that the Act does not state it | The body never mentions a week; "year" is defined nowhere (it appears in "calendar month", "calendar year" and "financial year", in examples, in s 37A and in ss 39 and 40); s 2G defines only the month |
| F5 | What is a "holiday" in s 36? | (A) a public holiday only; (B) the union of a public holiday in the place and a day the office is closed for the whole day; (C) both limbs at once (a day that is both) | (B). Saturdays and Sundays are named in s 36(2) and computed; the person lists the other days as one list. Kept apart from a "business day" (s 2B), which ignores office closures | s 36(3)(a) and (b); s 2B "business day" |
| F6 | Does s 3A fill the gap for an instrument that says nothing about commencement? | (A) yes, by analogy; (B) no: s 3A speaks of an Act and of Royal Assent | (B): an instrument that says nothing gets NOTHING from this text | s 3A(1), (2), (3) ("An Act", "the Royal Assent"); the Note to s 2(1) sends legislative instruments to the Legislation Act 2003, which is not in the text |
| F7 | What does "passed" mean in "an Act passed on 2026-03-10"? | (A) the day of Royal Assent; (B) the day Parliament finished passing it | (A): the input is the day of Royal Assent | s 3A(2) counts from "the day on which that Act receives the Royal Assent"; s 39 uses "assents thereto" |
| F8 | An Act that says it commences on a day to be fixed later: does s 3 (start of the day) reach the day once fixed? | (A) yes, a fixed day is "a particular day"; (B) no, because the Act was not "expressed to come into operation on a particular day" | (A): once fixed, the start of that day; until fixed, no day. Section 3A does not apply either way | s 3; s 3A(1) |
| F9 | When s 36(2) moves the last day on, are the days between the original last day and the rolled-on day still in time? (A Sunday between a Saturday last day and the Monday is the case.) | (A) yes, the period is taken to run to the rolled-on day, so every day up to it is in time; (B) only the original last day and the next day that is not a Saturday, a Sunday or a holiday are in time | (A), which is what `the thing is done within the time allowed` does: acting on a rest day between the two is within time (whether the office will receive it is a separate matter). An author who wants (B) changes the upper bound in that function (`au-interpretation-time.l4`, a comment there cites this fork) to: the day AT MOST the last day for doing the thing, OR the day EQUALS the rolled-on day. No test expectation changes under (A) | s 36(2) names the last day and "the next day that is not" a rest day, and says nothing about a rest day between them; the Example (31 March a Saturday, application on Monday 2 April) does not discuss the days between |
| F10 | In s 33A(1)(ba), from when are the 12 months of acting counted? | (A) from the first day of acting, that day included; (B) from the day after | (A): the paragraph says the appointee must not act "for more than 12 months", a length of time acted. Contrast (c)(iii), "12 months from the day of the vacancy", which is item 5 of the s 36 table (day excluded) | s 33A(1)(ba), (c)(iii); s 36(1) item 5 |
| F11 | Does s 36(2) move the last day of an acting appointment's 12 months (s 33(4)(b))? | (A) yes; (B) no | (B): nothing is "done" on the day an appointment expires. The 12 months run from the day after the office was created or became vacant (item 6) | s 33(4)(b) ("the expiration of 12 months after"); s 36(2) ("a thing to be done") |
| F12 | In s 34C, which day ends "within 15 sitting days of that House after the day on which he or she receives the report", and is s 36(2) applied? | (A) the 15th sitting day strictly after the day of receipt, no rest-day shift; (B) the 15th, shifted if it is a Saturday, Sunday or holiday | (A): a sitting day is a day the House actually sits, so it is not treated as a rest day. The text does not say what happens if the 15th sitting day is a Saturday | s 34C(3), (6), (7)(b); s 36(1) item 6; s 2M |
| F13 | What is a sitting day for the House when a sitting runs past midnight? | (A) every calendar day on which the House sits at any time; (B) only the day the sitting began, with later days part of it | (B), as the Examples say. The encoding takes the days on which a sitting BEGAN | s 2M(1), (2) and Examples 1 and 2 |
| F14 | How many days is "the ordinary course of post"? | (A) the Act fixes a number; (B) it does not | (B): the delivery day is an input; the rule only says that service is taken to be effected then, unless the contrary is proved | s 29(1) |
| F15 | A person born on 29 February attains an age in a year with no 29 February: which day? | (A) 28 February; (B) 1 March; (C) the Act does not say | (C): NOTHING | s 37A ("the relevant anniversary of the date of the birth"); contrast s 2G, which has an end-of-month rule for months only |
| F16 | Is a "business day" the same as a day that is not a "holiday"? | (A) yes; (B) no | (B): a business day ignores office closures | s 2B "business day" ("not a Saturday, a Sunday or a public holiday"); s 36(3)(b) |
| F17 | Is a period that ends before 30 June 1983 a "periodic report" period? | (A) yes; (B) no | (B): the definition covers a period that ends on or after 30 June 1983, so for an earlier one s 34C(2) gives NOTHING | s 34C(1) ("ends on or after 30 June 1983") |
| F18 | Which Acts does s 16C(2) cover, an Act "passed after the date of commencement of this section"? | (A) take the date as an input; (B) 19 June 1973; (C) 1 July 1973 | (A): whether the Act was passed after the date is an input (`the Act was passed after the date of commencement of section 16C`), and for an earlier Act subsection (2) says nothing about the named titles | s 16C(2); endnote 4 ("s 16C ad No 79, 1973"); endnote 3 gives Act No 79, 1973 as "s 4(2): 1 July 1973 ... Remainder: 19 June 1973" and does not say which of its provisions inserted s 16C |
| F19 | Which Acts does s 33(2A) cover, an Act "assented to after the commencement of this subsection"? | (A) take the date as an input; (B) pick a date from endnote 4 | (A): `the Act was assented to after the commencement of subsection 33(2A)` is an input | s 33(2A); endnote 4 lists the Acts that amended s 33 (No 7, 1941; No 27, 1984; No 141, 1987; No 146, 1999; No 46, 2011; No 10, 2015) without saying which inserted subsection (2A) |
| F20 | Under s 15AA, what if two interpretations best achieve the purpose equally, or none does? | (A) the first; (B) all of them; (C) the section gives no preferred interpretation | (C): NOTHING. The rule returns JUST an interpretation only when exactly one candidate is marked as best achieving the purpose or object | s 15AA ("the interpretation that would best achieve ... is to be preferred to each other interpretation") names no tie-break |
| F21 | In the s 19 table, item 3, is paragraph (c) ("in any case") an alternative to (a) and (b) or an addition to them? | (A) an alternative; (B) an addition | (B): the result is a LIST, the Minister found under (a) or (b) and also any other Minister administering the Department that deals with the matters of the Minister so found | s 19(1) table item 3(a), (b), (c) ("or" joins (a) and (b), then "or" before (c), which opens "in any case") |
| F22 | Under s 11A, where does an inserted definition or item go if its letters equal an existing one's, or (for a list or table) it was not arranged alphabetically? | (A) before the equal one; (B) after it; (C) the section gives no position | (C): NOTHING. Letters are compared with case, spaces and hyphens ignored | s 11A(1) ("appropriate alphabetical position, determined on a letter-by-letter basis"); s 11A(2)(b) ("immediately before the insertion, the list or table was arranged alphabetically") |
| F23 | Does "authorised by law, or by consent of parties, to hear and determine any matter" in s 34 qualify every person in the list (court, Judge, justice of the peace, officer, commissioner, arbitrator) or only "other person"? | (A) every person in the list; (B) only "other person", so a court has the powers in any case | (A): the source of authority (law, consent, or none) is the input, and the kind of person is not asked | s 34 ("Any court, Judge, justice of the peace, officer, commissioner, arbitrator, or other person authorised by law, or by consent of parties, to hear and determine any matter") |

## What the text turns out to say

Each finding says what the text says on reading, in the order they arose.
"Asserted." means a case in this folder asserts it, with the expected value written from the text before the run.

1. Saying a period runs "from" a day, or "after" it, leaves that day out: a person with 28 days after a decision on 2 August has a period that begins on 3 August (Example 6), and the 7 days before 8 May are 1 to 7 May (Example 7). Asserted.
2. The end of a period of months is the day before the corresponding day, or the end of the month when there is none: a month starting on 31 August ends at the end of September (s 2G(1) Example 2), and 6 months starting on 31 October end at the end of April (s 2G(2) Example 2). Asserted.
3. Counting the starting day or not changes the answer by a day even for a month: a month from 15 December ends on 15 January, while a month starting on 15 December ends on 14 January. The wording of the period, not the arithmetic, decides which applies. Asserted.
4. A month from 31 January 2025 begins on 1 February and ends on 28 February 2025, whether or not 31 January is counted, because February has no 31st. Asserted.
5. The Act never says how long a week or a year is. The word "week" does not occur in the body of the Act at all. "Year" is defined nowhere: it appears in "calendar month" ("the 12 months of the year"), in "calendar year" and "financial year" (each "a period of 12 months"), in examples (ss 2G and 36), in s 37A ("an age expressed in years"), and as "the secular year" or "the year it was made" in ss 39 and 40. Section 2G defines only the month. So three years from 16 July 2025, five years from 15 January 2025 and from 1 September 2025, two years from 28 February 2024 and one year from 29 February 2024 have no answer in the text. Asserted (NOTHING), with the 7-day / 12-month result separately asserted as an alternative reading.
6. Section 36(2) moves the last day of ANY period, including one counted in months or years, and moves it past several rest days in a row: the next day that is not a Saturday, a Sunday or a holiday. The text's own example (31 March a Saturday, application on Monday 2 April) is asserted. Asserted.
7. A "holiday" for the time for doing a thing is a public holiday in the place where it is to be done, or a day the office is closed for the whole day. The Act lists neither, so no encoding can be complete; the person supplies the days. A business day (s 2B) is a different test and ignores office closures. Asserted.
8. An Act that says nothing about commencement commences on the 28th day after the day it receives the Royal Assent (s 3A(2)); an Act to alter the Constitution commences on the day of Royal Assent (s 3A(3)); and an Act, or provision, expressed to commence on a particular day does so at the start of that day (s 3). An Act assented to on 10 March 2026 and silent therefore commences at the start of 7 April 2026. Asserted.
9. Section 3A applies to an Act "so far as it provides for its commencement" only when the Act is silent (s 3A(1)); it says nothing about an Act that names a day to be fixed later, so until that day is fixed the text gives no day, and once it is fixed as 1 June 2026 the Act commences at the start of that day (s 3, reading F8). Asserted.
10. The Act gives no default commencement for subordinate legislation. Section 3A speaks of an Act and its Royal Assent; the Note to s 2(1) says the Act also applies to legislative instruments and notifiable instruments, and a Note to s 46 says the Legislation Act 2003 contains the parallel. That Act is not in the text, so a legislative instrument made on 10 March 2026 that says nothing has no commencement day in this text. Asserted (NOTHING).
11. Service by post is taken to be effected at the time the letter would be delivered in the ordinary course of post, unless the contrary is proved; the Act gives no number of days (s 29(1)). Asserted.
12. A person attains an age at the START of the anniversary of the date of birth (s 37A). For a birth on 29 February and an anniversary year with no 29 February, the Act says nothing. Asserted (NOTHING).
13. Under s 28A the methods listed for a natural person (delivery to them personally; leaving it at, or posting it to, the last known place of residence or business) and for a body corporate (leaving it at, or posting it to, the head, a registered or a principal office) are DISJOINT: personal delivery is not listed for a body corporate, nor head-office service for a natural person. Section 28A(2) preserves any other law or court order that authorises another method. Asserted.
14. For a periodic report with no period specified, the deadline is 6 months after the end of the period reported on, "after" leaving the last day out (s 34C(2)). The Act "requires" the report, so s 36(2) can move it: a period ending 31 August 2025 has its 6 months end on 28 February 2026, a Saturday, so Monday 2 March 2026. Asserted.
15. For the statement explaining a late report the deadline is 14 days after the end of the specified period or extension (s 34C(7)(a)), moved by s 36(2) in the same way. Asserted.
16. The sitting-day deadlines of s 34C (15 sitting days for a report, 3 for a statement) count sitting days strictly after the day of receipt (or of the grant), and a sitting that runs past midnight counts only for the day it began. The text does not say whether s 36(2) can move a last day that is a sitting day falling on a Saturday (fork F12). Asserted for the counting; the Saturday case is not answered.
17. Sections 34C(7A) and (8) take three bodies (ASIO, the Australian Signals Directorate, the Office of National Intelligence) out of s 34C(3), and (6)(c) is disregarded for them after an extension; the Australian Secret Intelligence Service is outside the section altogether. Asserted.
18. The two twelve-month limits on acting appointments count differently: for a vacant office the appointee must not act "for more than 12 months" (first day of acting counted), whereas an acting appointee who stays on after the office they were acting in becomes vacant may continue until the first of a direction, the vacancy being filled, or "a period of 12 months from the day of the vacancy" ends (the vacancy day is not counted). Asserted.
19. The listed rights, privileges, obligations and liabilities accrued before a repeal or amendment survive it, and a repeal does not revive what was not in force; both are subject to a contrary intention (s 7(2), s 2(2)). Repealing the repealing Act revives the old Act only if express provision is made (s 7(1)). Asserted.
20. Under s 46AA an instrument may apply or incorporate an Act, a disallowable legislative instrument or rules of court "as in force from time to time", but any other instrument or writing only as in force or existing when the instrument commences or at a time before it. A form is outside the section (s 46AA(4)). Asserted.
21. The Act's own dates are in endnote 3: assent 12 July 1901, commencement 12 July 1901. They are carried as two values with an `@ref` to the endnote. Asserted (the two values).
22. The s 2B definitions of "Australia" and "Commonwealth", in a geographical sense, include Norfolk Island, the Territory of Christmas Island and the Territory of Cocos (Keeling) Islands but no other external Territory. Asserted.
23. The 95 defined terms (77 in s 2B, 18 elsewhere) are each stated in one of eight ways: a meaning, what is included, a meaning and what is included, a list of the things meant, the meaning of another Act, the meaning given by another Act, explained by another section, affected by another section. A term defined as "has the same meaning as in" another Act returns a pointer and no meaning. Asserted (257 assertions, and 165 more for the member lists, see finding 36 in `au-tests-part2-terms.l4`).
24. Under s 11A, an inserted definition or item goes where its letters place it, compared letter by letter with case, spaces and hyphens ignored: "Australian citizen" goes after "Australia" and before "business day" (position 2 of the list affidavit, Australia, business day, oath), and "Chairs" goes after chairperson and before chairwoman (position 3). A new item whose letters equal an existing one's has no position in the text (fork F22). For a list or table, the section applies only if the list was arranged alphabetically immediately before the insertion. Asserted.
25. Section 15AA prefers "the interpretation that would best achieve the purpose or object", whether or not the purpose is expressly stated. With two interpretations that achieve it equally the text names no preference (fork F20). Asserted.
26. The tables of ss 19, 19A and 19C turn on how a provision refers to a Minister, a Department or an authority, and give a description of whom it means ("the Minister, or any of the Ministers, administering the provision on the relevant day, in relation to the relevant matter"), not a name; who that is on a given day is in the Administrative Arrangements Order, which is not in the text. A substituted reference order (s 19B) is in effect on and after the day it specifies. Asserted.
27. Section 33(3AA) changes the "like conditions" of s 33(3) only for repeal, rescission and revocation, and only for a condition that must be satisfied before the instrument is made and can stop being satisfied afterwards (the "ongoing condition", as in the Example of a permission given to a person of good character): the condition then is the ongoing condition ceasing to be satisfied. For an amendment or a variation the like conditions stand. Asserted.
28. The proviso to s 33(4) names two powers and no others: the power to appoint a person to act, and the power of removal, are exercisable only on the recommendation or with the approval or consent of the other person or authority where the power to appoint is. The powers to suspend and to appoint temporarily are not named in it. Asserted.
29. Under s 34AAB(1) a Minister who administers an Act or provision may authorise a Minister who does not administer it, or a member of the Executive Council who is not a Minister, but not a Minister who does administer it. The authorisation reaches the functions under the Act or provision and under an instrument having effect under it (subsection (2)), and an authorisation expressed to continue until another person is appointed to the authorising Minister's office ends on that appointment or on revocation. Asserted.
30. Under s 34AB(1)(b) the power to delegate is not among the powers that may be delegated, and under (d) a delegation does not stop the authority performing the function itself. Under (2) and (3) a delegation in force immediately before an amendment takes effect includes the added functions (if all were delegated) or the functions as altered (if one or more were), on and after the day the amendment takes effect, that day included. Asserted.
31. Under s 33B a body established by an Act, whether or not incorporated, may permit members to take part by telephone, closed-circuit television or other means; a member who does is taken to be present and in the quorum; a meeting may be held at 2 or more places at once. Asserted.
32. An extension granted under s 34C(5) is a period with its own last day, and s 34C(6)(b) makes the person furnish the report within it. Section 36(2) moves that last day like any other: with the last day Saturday 28 February 2026 the report may be furnished on Monday 2 March 2026, or on Tuesday 3 March 2026 if 2 March is a holiday. Asserted.
33. Section 34 gives the power to receive evidence, examine witnesses and administer an oath or affirmation to any person authorised by law or by consent to hear and determine the matter (fork F23); the oath or affirmation is to witnesses legally called before them. Asserted.
34. Section 29(2) says that the deeming in s 29 leaves section 160 of the Evidence Act 1995 working; what that section says is not in the text, so whether it would operate is an input and the answer is that s 29 does not stop it. Asserted.
35. Section 37 makes a reference to time in an Act mean the legal time in the State or part of the Commonwealth unless the Act specifically states otherwise. Asserted.
36. Where a definition prints a list of alternatives or items, the table lists the phrase as printed AND each item, so a lookup of an item the Act names succeeds (review fix 2026-10-29; the first version stored some lists as one string). A list is split where its items are nouns or noun phrases the definition names; it is kept whole where an "or" or "and" joins verbs, conditions or the parts of one thing. Asserted (165 assertions at the end of `au-tests-part2-terms.l4`: the printed phrase, each item, the article form, and one unlisted thing that is still not named). The entries are in the table below.

### Which printed lists are split into members

The sweep was a script over every `members it names` and `members it leaves out` string of the 95 entries (68 strings in all; the two in `members it leaves out` are single phrases), not a reading from memory.
Each entry was decided from the source text.
Of the 215 members now stored, 150 are strings printed in the cited lines and 65 are derived: the article or singular form of a bare noun (`a lien`, `a substitution`), `any` put before an item of the list in `estate`, or the Act's shared head repeated for each alternative (`a justice of the peace for part of a State`, `the activities of a person`).

| entry | members before | members after | what was split |
|---|---|---|---|
| s 2B "document" | 4 | 26 | limbs (b), (c) and (d): marks, figures, symbols, perforations; sounds, images, writings; a map, plan, drawing, photograph; limb (a) has no list |
| s 2B "estate" | 1 | 25 | the eight nouns of "any estate, interest, charge, right, title, claim demand, lien or encumbrance at law or in equity" (the text prints "claim demand" with no comma, and it is kept as one item) |
| s 2B "justice of the peace" | 1 | 4 | for a State; for part of a State; for a Territory |
| s 2B "land" | 1 | 7 | messuages, tenements, hereditaments |
| s 2B "modifications" | 1 | 7 | additions, omissions, substitutions |
| s 2B "writing" | 1 | 9 | words, figures, drawings, symbols |
| s 15B(4) "coastal sea" | 5 | 11 | "the airspace over, and the sea-bed and subsoil beneath, any such sea" as three phrases and three nouns |
| ss 19B(7), 19C(6), 19D(5) "authority" | 4 each | 11 each | limb (d): an office (including an APS employee's office and any other appointment or position); the holder of an office |
| s 34B(2) "paper" | 3 | 17 | an ordinance, rule, regulation or by-law; any other document or instrument |
| s 34C(1) "periodic report" | 2 | 16 | the activities, operations, business, affairs of a person; the administration, operation, working of an Act or part of an Act |
| s 34C(1) "person" | 1 | 21 | the ten alternatives, from body corporate to other body however described |
| s 36(3) "holiday" | 2 | 3 | the closure itself, after the dash in limb (b), is also listed; limbs (a) and (b) stay whole |
| s 40A(6) "relevant earlier law" | 2 | 4 | the two limbs are also listed without their bracketed qualifier |

Checked and left whole, with the reason:

- s 2B "Administrative Arrangements Order" limb (b)(ii), "revokes a primary AAO and substitutes a new primary AAO": one instrument that does both, so neither half alone is named.
- s 2B "record", "information stored or recorded by means of a computer": "stored or recorded" are two verbs for one kind of information, not alternative members.
- s 15B(4) "coastal sea" limbs (a)(ii) and (b)(ii), "the sea on the landward side of ... and not within the limits of ...": one place described by two conditions.
- s 36(3) "holiday" limbs (a) and (b): the "or" in "to be or may be done" joins verbs, and limb (b) is a conditional limb; the closure is also listed on its own (above).
- Entries that were already split and pass: oath, affidavit, swear, internal Territory, Australia, Commonwealth, Senior Counsel, the Administrative Arrangements Order limb (b)(i), and limbs (a) to (c) of "authority".
- Entries with no list: contravene, court exercising federal jurisdiction, Government Printer, and the four "office" and "officer" entries.


## Changes to existing modules

One change to a pass-1 module, and it is a comment: `au-interpretation-time.l4`, four lines above `the thing is done within the time allowed` that cite fork F9 and say where an author who wants the literal reading would change the function.
No code and no test expectation changed.
Why: a test author found that a Sunday between a Saturday last day and the Monday counts as in time, and the behaviour was registered as F9 but was not cited where it happens.
The text that licenses the reading is s 36(2) (src:814-818).
Of the files that were in this folder at the start of pass 2, I edited only that comment. I did not edit the rest (pass-1 `au-*.l4`, `srcrefs.py`, `check.sh`, `fetch-main-l4.sh`, `SOURCE-LICENSE.md`): no assertion failed that the text supports, and no citation was found wrong.
Not by me, and not yet explained here: nine files were rewritten at 16:41:05 on 2026-10-29, after my pass-2 report and before the review fixes above, and their sizes differ from the sizes I recorded earlier that day.
They are `au-cases-seat.l4` (26,662 to 28,615 bytes), `au-part1-application.l4` (2,832 to 2,850), `au-part7-powers.l4` (26,068 to 26,077), `au-tests-part1.l4` (1,138 to 1,165), `au-tests-part3.l4` (2,635 to 2,734), `au-tests-time.l4` (22,932 to 25,173), `au-tests-part7.l4` (11,697 to 12,390), and two pass-2 files, `au-tests-part7-more.l4` (29,793 to 30,306) and `au-part5-ministers.l4` (same size, new time).
I have no copy from before that edit, so I cannot say what changed in them; the assertion counts of the test files are the same as before (8, 17, 60, 124, 134, 208, 97), and `check.sh` and `srcrefs.py` pass on the folder as it now stands.
Whoever made those edits owes this section a line for each file: what changed, why, and the text that licenses it.
(`NOTES.md`, `PROGRESS.md` and `encoding.json` are the bookkeeping files and are rewritten as the brief requires.)
`check.sh` and `fetch-main-l4.sh` were already in the folder in the form that runs the main build as well; `check.sh.pass1` is the earlier script.

After review, two pass-2 files were also edited, which are not changes to a pass-1 module: `au-part2-terms.l4` (member lists, see "Which printed lists are split into members") and `au-tests-part2-terms.l4` (165 assertions added).

- **2026-10-29, the rule stated in "Reading a result: FALSE and NOTHING":** `a reference to the holder or occupier includes the person` (s 20) now answers `NOTHING` for a person who neither holds nor occupies the office nor performs its duties, where it answered `JUST FALSE`: section 20 says the reference "includes" the two groups, an open list. One assertion restated (`au-tests-part5-readings.l4`, with a `-- RECONCILED 2026-10-29` comment quoting the original). `check.sh` after the change: 45 modules, 2,041 satisfied, 0 failed, 0 refused, every module `same` on 1.6.102.

## Answer table: the worked cases

Each answer was written from the text before it was run; the seat cases in `au-cases-seat.l4` and the time tests in `au-tests-time.l4` assert them.
Every move below is by s 36(2), and happens only where an Act requires or allows a thing to be done within the period; the weekday of the unmoved last day is given so a reader can see why.

| case | answer | text |
|---|---|---|
| three years from 2025-07-16 | The text is silent on the length of a year (finding 5). Alternative reading (a year is 12 months): from 17 July 2025, 36 months end on 16 July 2028, a Sunday. If an Act requires or allows a thing to be done within the period, s 36(2) moves the last day to Monday 17 July 2028; otherwise it stays 16 July 2028. | s 36(1) item 5; s 2G; no definition of "year" (fork F4) |
| five years from 2025-01-15 | Text silent. Alternative reading: ends 15 January 2030, a Tuesday. | same |
| five years from 2025-09-01 | Text silent. Alternative reading: ends 1 September 2030, a Sunday. If an Act requires or allows a thing to be done within the period, moved to Monday 2 September 2030; otherwise it stays 1 September 2030. | same |
| thirty days from 2026-01-01 | The period is 2 to 31 January 2026 ("from" leaves out 1 January). 31 January is a Saturday. If an Act requires or allows a thing to be done within the period, s 36(2) moves the last day to Monday 2 February 2026 (to Tuesday 3 February if 2 February is a holiday or the office is closed all day); otherwise it stays 31 January 2026. | s 36(1) item 5; s 36(2), (3) |
| two years from 2024-02-28 | Text silent. Alternative reading: from 29 February 2024, 24 months end on 28 February 2026, a Saturday. If an Act requires or allows a thing to be done within the period, moved to Monday 2 March 2026; otherwise it stays 28 February 2026. | same as three years |
| one year from 2024-02-29 | Text silent. Alternative reading: from 1 March 2024, 12 months end immediately before 1 March 2025, which is 28 February 2025, a Friday. | s 2G(2); fork F4 |
| one month from 2025-01-31 | From 1 February 2025 the month ends immediately before 1 March 2025: 28 February 2025, a Friday. | s 36(1) item 5; s 2G(1) |
| an Act passed on 2026-03-10 that says nothing about when it comes into force | Commences on the 28th day after the day of Royal Assent (10 March plus 28 days): 7 April 2026, a Tuesday, at the start of that day. | s 3A(2); s 3 |
| an Act that says it comes into force on a day to be fixed later, the day being fixed as 2026-06-01 | Section 3A does not apply (s 3A(1)). Until the day is fixed the text gives no day. Once fixed, it comes into operation at the start of 1 June 2026, a Monday (fork F8). | s 3A(1); s 3 |
| subordinate legislation made on 2026-03-10 that says nothing about when it comes into force | The text is silent: s 3A speaks of an Act and its Royal Assent, and the Legislation Act 2003, which the Notes to ss 2 and 46 point to for such instruments, is not in the text (fork F6). | s 3A; Notes to ss 2(1) and 46 |

## The seat's questions

31 questions, each with `@export` and an `@desc` on every input, grouped under `§§` headings in the text's order (9 groups).

- Does the Acts Interpretation Act 1901 apply to the Act that binds me (s 2)?
- Is this day a business day (s 2B)?
- On which day does the financial year that includes my day end (s 2B)?
- Which day is the Nth sitting day of the House after my day (ss 2M, 36)?
- On which day does the Act or instrument that binds me come into operation (ss 3, 3A)?
- At what moment does the Act or instrument that binds me come into operation (ss 3, 3A)?
- What happens to what I already have or owe when the Act is repealed or amended (s 7(2))?
- Does repealing the Act that repealed my old Act bring my old Act back (s 7(1))?
- Does my form meet the requirement if it does not comply strictly with the prescribed form (s 25C)?
- Are the written reasons I was given complete (s 25D)?
- Was the document served on me in a way the Acts Interpretation Act allows (s 28A)?
- On which day am I taken to have been served by post (s 29)?
- Until which day may I keep acting in a vacant office (s 33A(1)(ba))?
- Until which day may I keep acting after the office I was acting in became vacant (s 33A(1)(c))?
- On which day do the 12 months of an appointment to act under a power to appoint run out (s 33(4))?
- By which day must I furnish my periodic report to the Minister (s 34C(2))?
- Can I still ask the Minister for more time to furnish my report (s 34C(4))?
- By which day must I explain in writing why my report was late (s 34C(7))?
- By which day must the Minister lay my report before a House, when no extension was granted (s 34C(3))?
- By which day must the Minister lay my report before a House, when an extension was granted (s 34C(6)(c))?
- By which day must the Minister lay my explanation and the extension before a House (s 34C(6)(a))?
- By which day must the Minister lay my explanation for a late report before a House (s 34C(7)(b))?
- Does the day I am counting from count as part of my period (s 36(1))?
- On which day does my period begin (s 36(1))?
- On which day does my period of days, weeks, months or years end (ss 2G, 36)?
- On which day would my period end if a week were 7 days and a year were 12 months (a reading the Act does not state)?
- On which day does my period end when the Act ends it at, with, or before a named day (s 36(1))?
- Is the last day of my period a day I cannot act on, because it is a Saturday, a Sunday or a holiday (s 36(2), (3))?
- What is the last day on which I may act, if my period ends on a Saturday, a Sunday or a holiday (s 36(2))?
- Am I in time if I act on this day (s 36)?
- At what moment do I attain a given age (s 37A)?

The seat layer does not ask about s 4 (a power exercised before an Act commences), s 6 (evidence of the date of assent), ss 33 and 33B to 34AB apart from the acting limits, or Parts 9, 10 and 11 (how Acts and instruments are cited, made and read), because a person with a time limit to meet has no question of their own on them. They are encoded in layer 1 (see the coverage table), and pass 2 did not change the seat layer.

## What the stable binary does not accept

Measured with `l4` 1.6.98 (main, 7689b0d, 2026-10-19) in this run.

- **`YMD` is not defined** in the 1.6.98 prelude. Every module writes dates as `Date day month year`, and this encoding defines no shim for it.
- **`NOT a OR b` parses as `NOT (a OR b)`.** Every `NOT` is parenthesised. A sitting-day rule written without the brackets returned the wrong answer on one assertion, found by that assertion and fixed in the module.
- **`x NOT EQUALS y` is a parse error** ("unexpected ("). Write `NOT (x EQUALS y)`.
- **A constructor pattern binds its fields by position.** `WHEN `a constructor` d THEN` names the first field; there is no way to leave a field out.
- **A multi-line `LIST` with leading commas breaks layout**, so every list in the tests is a one-line named fixture.
- **`IMPORT` of a hyphenated module name needs backticks**, and finds only modules in the same folder; a name defined in two imported modules cannot be used (the daydate names `the day before`, `the day after`, `the later of` and `the earlier of` collided with names I had chosen).
- **`daydate`'s `add months` and `add years` clamp** (31 January plus one month is 28 February), so they are not used: s 2G is written from the text.
- **`Date d m y` is lenient**: `Date 31 2 2025` rolls over to 3 March 2025. The module checks `Days in month` where a non-existent day matters (s 37A).
- **`l4 batch` cannot re-print a seat file with a `LIST OF` input that is not the last input of its `GIVEN`.** It reports `incorrect indentation (got 3, should be greater than 43)` at the next input. The same file passes `l4 check` and `l4 run`. So every seat question puts its single list last, and the two lists the module takes (public holidays; closed days) are asked as one.
- **`l4 batch` cannot re-print a lambda (`GIVEN x YIELD ...`) in the exporting file.** It reports that it "could not find a definition for the identifier" the lambda's variable, again while `l4 check` and `l4 run` pass. The seat uses a named helper instead; the layer-1 modules, which batch loads rather than re-prints, still use lambdas.
- After those two were avoided, all 31 seat questions ran through `l4 batch` with a JSON row each, with no error.
- **A mixfix name may not end in a keyword segment, and `GIVEN` order must be the order the arguments appear in the name.** A rule is written as its name followed by its arguments (`the position of the inserted item among the items, counting from 0` addition ...), and a name that put an argument in the middle or ended on a word such as `of` or `means` was rejected, with an error that points at the next token.
- **`new` is a keyword**, so a parameter cannot be called `new`.
- **A one-line `GIVEN a IS A LIST OF X, b IS A Y` is a parse error**; each input goes on its own line.
- **The prelude `sort` takes numbers only.** Putting strings in order is done by a recursive check that each key is `AT MOST` the next (`LESS THAN` and `AT MOST` work on strings).
- **`REPLACE` takes the text, then what to find, then what to put in its place**; the wrong order fails with `Data.Text.replace: empty input`, which does not say which argument was wrong.
- **List patterns `WHEN x FOLLOWED BY rest` and `x FOLLOWED BY EMPTY` work**, and `CONSIDER ... OTHERWISE` is accepted.
- Not tried here, avoided because the brief says the stable binary rejects them: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section-level `GIVEN`, `TYPICALLY`, sets.

## What check.sh prints

`L4=<l4 1.6.98> L4_MAIN=<l4 1.6.102> ./check.sh` (the default target `main`: every module is run with both binaries), exit status 0.
The baseline before pass 2 was 24 modules, 560 assertions satisfied, 0 errors, 0 failed, 0 refused, every module the same on the main build; every one of those 24 modules still gives the same counts (`au-interpretation-time.l4` gained a comment only), and pass 2 added 20 modules and 926 satisfied assertions (761 when first written, 165 after review).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.102 (main, e4f2553, 2026-10-26)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
au-cases-seat.l4                               0       124       0        0         0 |      0       124       0        0  same
au-interpretation-time.l4                      0         0       0        0         0 |      0         0       0        0  same
au-part1-application.l4                        0         0       0        0         0 |      0         0       0        0  same
au-part10-11-instruments.l4                    0         0       0        0         0 |      0         0       0        0  same
au-part2-definitions.l4                        0         0       0        0         0 |      0         0       0        0  same
au-part2-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part2-terms.l4                              0         0       0        0         0 |      0         0       0        0  same
au-part3-commencement.l4                       0         0       0        0         0 |      0         0       0        0  same
au-part3-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part4-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part4-repeal.l4                             0         0       0        0         0 |      0         0       0        0  same
au-part5-interpretation.l4                     0         0       0        0         0 |      0         0       0        0  same
au-part5-ministers.l4                          0         0       0        0         0 |      0         0       0        0  same
au-part5-readings.l4                           0         0       0        0         0 |      0         0       0        0  same
au-part6-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part6-service.l4                            0         0       0        0         0 |      0         0       0        0  same
au-part7-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part7-powers.l4                             0         0       0        0         0 |      0         0       0        0  same
au-part8-distance.l4                           0         0       0        0         0 |      0         0       0        0  same
au-part8-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-part9-citation.l4                           0         0       0        0         0 |      0         0       0        0  same
au-part9-more.l4                               0         0       0        0         0 |      0         0       0        0  same
au-seat.l4                                     0         0       0        0         0 |      0         0       0        0  same
au-tests-part1.l4                              0         8       0        0         0 |      0         8       0        0  same
au-tests-part10-11.l4                          0        27       0        0         0 |      0        27       0        0  same
au-tests-part2-more.l4                         0        41       0        0         0 |      0        41       0        0  same
au-tests-part2-terms.l4                        0       422       0        0         0 |      0       422       0        0  same
au-tests-part2.l4                              0        62       0        0         0 |      0        62       0        0  same
au-tests-part3-more.l4                         0        12       0        0         0 |      0        12       0        0  same
au-tests-part3.l4                              0        17       0        0         0 |      0        17       0        0  same
au-tests-part4-more.l4                         0        15       0        0         0 |      0        15       0        0  same
au-tests-part4.l4                              0        30       0        0         0 |      0        30       0        0  same
au-tests-part5-ministers.l4                    0        97       0        0         0 |      0        97       0        0  same
au-tests-part5-readings.l4                     0       122       0        0         0 |      0       122       0        0  same
au-tests-part5.l4                              0        41       0        0         0 |      0        41       0        0  same
au-tests-part6-more.l4                         0         2       0        0         0 |      0         2       0        0  same
au-tests-part6.l4                              0        15       0        0         0 |      0        15       0        0  same
au-tests-part7-more.l4                         0       208       0        0         0 |      0       208       0        0  same
au-tests-part7.l4                              0        60       0        0         0 |      0        60       0        0  same
au-tests-part8-more.l4                         0         3       0        0         0 |      0         3       0        0  same
au-tests-part8.l4                              0         5       0        0         0 |      0         5       0        0  same
au-tests-part9-more.l4                         0         4       0        0         0 |      0         4       0        0  same
au-tests-part9.l4                              0        37       0        0         0 |      0        37       0        0  same
au-tests-time.l4                               0       134       0        0         0 |      0       134       0        0  same
TOTAL (44 modules)                             0      1486       0        0           |      0      1486       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs <raw text> <every au-*.l4>` printed:

```
srcrefs check: 913 src: lines, 280 runs, 314 locators, 0 problems
```

`python3 -I srcrefs.py check --strict <raw text> <every au-*.l4>` printed:

```
srcrefs check: 913 src: lines, 280 runs, 314 locators, 0 problems
```

(The pass-1 baseline for both was `425 src: lines, 80 runs, 108 locators, 0 problems`.)

`l4 check` over each of the 44 `au-*.l4` files printed `Check succeeded.` and nothing else, so there are 0 layout warnings ("is at the end of the file", "follows code on its line") and 0 warnings of any kind.
`l4 batch` was not re-run in pass 2: the seat layer is unchanged.

Earlier in the work, one assertion in `au-tests-time.l4` failed because of a defect in the module (the `NOT a OR b` precedence trap above); the module was fixed and the expected value was left alone.

Two assertions failed on a first run later and were not findings about the text; both were mistakes in my hand-written expected values, found by re-deriving them from the text and a calendar, not by copying the program's answer:

- `au-tests-part7.l4`, a periodic report whose period ended on 30 June 1983: I wrote 30 December 1983 for the end of the 6 months. Six months after 30 June begin on 1 July and end immediately before 1 January, which is 31 December 1983, a Saturday, so Monday 2 January 1984.
- `au-cases-seat.l4`, acting on 2 February 2026 when that Monday is a listed holiday and the last day is Saturday 31 January: I wrote not in time. Section 36(2) lets the thing be done on the next day that is not a rest day (3 February) and says nothing to forbid the days before it; the program was right and the case now records fork F9.

In pass 2 one assertion in `au-tests-part4-more.l4` (s 11A) failed on its first run, and it was a mistake in my hand-written expected value, not a finding about the text: I wrote position 1 for inserting "Chairs" into chair, chairman, chairperson, chairwoman. Its letters are chairs, which come after chairman (m before s) and chairperson (p before s) and before chairwoman (s before w), so the position is 3; a comment on the next assertion also mislabelled an equal-letters case. I re-derived both from the text, and did not copy the program's answer.
Four mutations were then made to a copy of `au-part7-more.l4` to check that `au-tests-part7-more.l4` can fail: `AT LEAST` changed to `GREATER THAN` on the day an amendment takes effect (s 34AB(2), (3)), the s 33(3AA) amendment case made to return the ongoing condition, the s 33(4) proviso extended to suspension, and the s 33B(5) place count lowered from 2 to 1. Each made at least one assertion fail; the copy was deleted.

## What would need doing before this encoding is worth relying on

1. A lawyer who knows Commonwealth drafting should read every fork in the register against the Act, in particular F1 to F5 (the counting rules), F8 (a day fixed later), and F18 to F23 (found in pass 2).
2. The dates of commencement of s 16C and of s 33(2A) are not in the text (F18, F19). They need the amending Acts (No 79, 1973 for s 16C; the Acts listed in endnote 4 under s 33 for subsection (2A)), or the Federal Register's own history, to turn the two inputs into dates.
3. The Legislation Act 2003 is not in the text, and the Acts Interpretation Act points at it for legislative and notifiable instruments (the Notes to ss 2(1), 33(3AB) and 46). Without it, the commencement of subordinate legislation is NOTHING here.
4. The question of how long a week and a year are needs an authority outside this Act (a case, or the Legislation Act 2003); the ALTERNATIVE READING functions assume 7 days and 12 months.
5. Public holidays and office closures must be supplied by the person for each place; no list is bundled.
6. Time of day and time zone (s 37) are not modelled; an Act in force from "the start of a day" is a day plus 00:00:00 with no zone, and the legal time of a place is a string the caller supplies.
7. What the Administrative Arrangements Order says on a given day (ss 19 to 19C), the meaning of every term that s 2B borrows from another Act, and section 160 of the Evidence Act 1995 (s 29(2)) are outside the text; the encoding asks for them as facts.
8. The seat's page for Legalese Cloud has not been deployed; only `l4 batch` was run against the questions, and the seat layer was not changed in pass 2 (it covers the counting and commencement questions, not the new Part 5 and Part 7 rules).
9. The text is a converter's rendering. Its wording has not been compared line by line with the official compilation, although every `-- src:` line was produced mechanically from it and `srcrefs.py` checks the quotes against it.
10. Several new rules are gates that return NOTHING for "the provision says nothing about this case", and a few (for example s 33B(2), s 34AAB(5)) are close to restatements of the text with a BOOLEAN input; they record that the provision was read and what it answers, and a domain reader should say whether any is worth a richer model.

## Files

- `BRIEF-pass1.md`
- `NOTES.md`
- `PROGRESS.md`
- `SOURCE-LICENSE.md`
- `au-cases-seat.l4`
- `au-interpretation-time.l4`
- `au-part1-application.l4`
- `au-part10-11-instruments.l4`
- `au-part2-definitions.l4`
- `au-part2-more.l4`
- `au-part2-terms.l4`
- `au-part3-commencement.l4`
- `au-part3-more.l4`
- `au-part4-more.l4`
- `au-part4-repeal.l4`
- `au-part5-interpretation.l4`
- `au-part5-ministers.l4`
- `au-part5-readings.l4`
- `au-part6-more.l4`
- `au-part6-service.l4`
- `au-part7-more.l4`
- `au-part7-powers.l4`
- `au-part8-distance.l4`
- `au-part8-more.l4`
- `au-part9-citation.l4`
- `au-part9-more.l4`
- `au-seat.l4`
- `au-tests-part1.l4`
- `au-tests-part10-11.l4`
- `au-tests-part2-more.l4`
- `au-tests-part2-terms.l4`
- `au-tests-part2.l4`
- `au-tests-part3-more.l4`
- `au-tests-part3.l4`
- `au-tests-part4-more.l4`
- `au-tests-part4.l4`
- `au-tests-part5-ministers.l4`
- `au-tests-part5-readings.l4`
- `au-tests-part5.l4`
- `au-tests-part6-more.l4`
- `au-tests-part6.l4`
- `au-tests-part7-more.l4`
- `au-tests-part7.l4`
- `au-tests-part8-more.l4`
- `au-tests-part8.l4`
- `au-tests-part9-more.l4`
- `au-tests-part9.l4`
- `au-tests-time.l4`
- `check.sh`
- `check.sh.pass1`
- `coverage.tsv`
- `covtable.py`
- `encoding.json`
- `fetch-main-l4.sh`
- `srcrefs.py`
- `units.py`

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage.tsv`, `covtable.py`, `units.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 618 numbered scenarios over every Part and section of the Act, including cases where the text is silent.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (547 scenarios, 555 assertions, because a few scenarios carry two), and ran it against this encoding with the stable binary.
`ANSWERS.md` is not kept in this folder; the scenario numbers in `tests-independent.l4` refer to it, and each assertion carries its provision and text line.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 555 | 546 | 9 | 0 |
| after the terms-table fix and the reconciliation below | 555 | 555 | 0 | 0 |

The 71 scenarios the encoding has no function for are listed in the comment block at the end of the test file (`-- GAP` lines, grouped as the author reported them; 547 + 71 = 618); they are limits of the encoding, not passes.
Dates in the reviewer's file are written `Date day month year`, as in the encoding (the reviewer wrote them with the encoding's local `YMD` shim, and the lead rewrote every use); nothing else in the file was changed except as listed below.

**What the nine disagreements turned out to be.**

- **Three were an encoder defect, now fixed.**
  The terms table kept some definitions' members as one string where the Act prints a list, so "a lien" was not named as an estate, "a substitution" not as a modification, and "a justice of the peace for a State" not as a justice of the peace.
  A script then swept every `members it names` and `members it leaves out` string: 15 entries now hold the printed phrase and each item in it, 4 were checked and left whole with a stated reason, and the details are in the section "Which printed lists are split into members".
  The reviewer's follow-up probes ("regulation" as a paper in s 34B(2), "board" as a person in s 34C(1)) found the same defect in two more entries; both are fixed.
- **Five were the independent author's wording, reconciled in the test file.**
  Scenarios 153, 336, 337, 338 and 341 asked for `JUST FALSE` where the Act is silent; the encoding's stated convention for "the section does not give it" is `NOTHING`, and the author agrees that is the more accurate answer.
  Each is rewritten in place with a `-- RECONCILED` comment above it that quotes the original assertion; none is deleted.
- **One is a genuine fork (scenario 547, s 36(2)).**
  The author reads "the thing may be done on the next day that is not a Saturday, a Sunday or a holiday" literally, so a Sunday between a Saturday last day and the Monday is not a permitted day; the encoding treats the period as extended to the rolled day, so the Sunday is in time.
  That is fork F9, which was registered in pass 1 with both readings; the assertion now states the encoding's reading and the comment above it quotes the author's.

**Known limits shown by the gaps and by the author's silence cases.**
Some closed lists with a catch-all value answer `FALSE` where the Act is silent (Queen's Counsel under a King, the contents list and endnotes under s 13, an unlisted way of serving under s 28A, an unlisted act at a hearing under s 34), and the pass-2 functions answer `NOTHING`; `FALSE` from those functions means "the section does not give it", not "the Act says no" (section "Reading a result: FALSE and NOTHING"). (Superseded on 2026-10-29: under the rule now stated in that section a plain-`BOOLEAN` function should not answer `FALSE` for silence; the 17 that still do are listed there as open.)
A few cases cannot be asked at all because the type has no value for them (an unincorporated association under s 28A, a period expressed to end after or begin before a day under s 36(1), the Parliament of New Zealand under s 38).
The defined-terms table says whether a named member is covered but has no function that applies a definition to a new case.
The others are one-line comments in the file.

**Independence caveat.** At 08:58Z, after the test author's `ANSWERS.md` was last changed (08:35Z) and before it wrote `tests-independent.l4` (09:05Z), the harness delivered into its session the contents of a backlog file and of three of the lead's scripts (reconciliation, review set-up, verification) and the path of a fourth.
Its tool calls show no other access to the lead's files.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 45 modules, 2041 satisfied, 0 failed, 0 refused, and every module `same` on the `main` build, run on 2026-10-29.
