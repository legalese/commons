# NOTES: Interpretation Act 1978 (1978 c. 30), row `legalese-sonnet-5.5`

Status: draft, version 0.2.0 (pass 2, the completion pass to "whole", 2026-10-29; pass 1 is version 0.1.0). Written by a single Sonnet 5.5 agent working alone from `BRIEF.md` in each pass; no domain expert has read it against the statute (see `encoding.json`, `not_reviewed`).

## The source is a converter rendering, not the official text

The only source is `../../registers/source-bundle/ukpga-1978-30.txt`: a plain-text rendering made by a converter script from https://www.legislation.gov.uk/ukpga/1978/30/data.xml (version of 2026-01-01).
It is not the official text and it is not marked up.
Nothing here is claimed to be "verified against the official text".
The `.meta.json` beside it, `../../registers/source-bundle/ukpga-1978-30.meta.json`, records its hashes: text sha256 `e6d0e2422aca474ecf24aa71ed164ed40e73a02e2ad8fe834749f00f1936e64b`, which I re-computed with `shasum -a 256` and found equal.
Quotations in the `.l4` files are `-- src:N | ...` lines copied out of that file by script: in pass 1 by `srcrefs.py quote`; in pass 2 by a template expander (the modules `definitions`, `general`, `eu`, `devolved`) and by `tools/gen_schedule1.py` (the module `schedule1`), the same copy, line for line, from the raw file. Whichever script wrote them, `python3 -I srcrefs.py check --refs` reads every one back against the raw file (R1) and checks every `@ref` locator against the quote lines (R2, R3).
The licence note is `SOURCE-LICENSE.md`, which points at `../../SOURCE-LICENSE.md` (Open Government Licence v3.0).

## The target compiler is `unstable`, and why

The brief mandates `@lang en` on every module, `REFUSE` for what the source does not answer, and `#ASSERT REFUSED ... BECAUSE` for testing a refusal.
The `main` compiler rejects each of these (`references/dialects.md` of the writing-l4-rules skill: probe 01 `@lang` is rejected with `unexpected '@'`; probe 02 `REFUSE` with `I could not find a definition for the identifier REFUSE`; probe 03 `REFUSED`; probe 04 `BECAUSE` with `unexpected BECAUSE`; probe 05, `YMD`, which `daydate` users need for a bounds-checked date, is rejected too).
So the target is `unstable`, and `check.sh` is run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
`check.sh` then skips its comparison with a main build, and says so on stderr; no main build was compared.
Pass 2 ran on the binary the run supplied, `l4-unstable-0528`: `--version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d` (re-computed with `shasum -a 256` at the end of the run).
Pass 1 had run on a `dev` build (sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`); the baseline of the six pass-1 test files was taken again on the pass-2 binary before any change, and was the same (905 satisfied, 7 failed in `tests-red.l4`, 0 refused).
`JL4_LIBRARY_PATH` was unset for every run (`env -u JL4_LIBRARY_PATH`).

A conflict between the brief and the skill, noted rather than resolved silently: the writing-l4-rules skill says never to write `@lang en`, and the compiler agrees with a Hint (`A module that declares nothing is English; this line can go.`) on every module.
The brief says every module starts with `@lang en`, so every module does, and every module carries that one Hint and no other diagnostic (checked at the end of pass 2 over all 22 files: the only Error or Warning diagnostics in the deposit are the 7 expected failed assertions of `tests-red.l4`).

## Re-disposition audit

Written on 2026-10-29, before any new L4 of pass 2, and kept current.
Pass 2 is the completion pass the brief calls "whole": every unit of the text has a row, and each row has one of four dispositions (`encoded`, `inert` for one of three reasons, `fork`, `repealed or blank in this text`).
The units, the rows and the tables below are not typed by hand: `tools/units.py` counts the units from the text, `tools/coverage.tsv` holds one row per unit, and `tools/coverage.py` renders both tables here, checks the table against the text and against the modules (`python3 -I tools/coverage.py check ../../registers/source-bundle/ukpga-1978-30.txt tools/coverage.tsv`), and splices them into this file.
The pass-1 table that this audit compares with is kept as extracted data in `tools/pass1-coverage.tsv`.

### What pass 1 gave as reasons, and why none of them stands

Pass 1 marked 111 rows `inert` for reasons that the brief of pass 2 names and withdraws.
Its code A (defined by pointing at another Act or instrument not among the sources), code B (names an institution, court or office), code C (names a territory or a legislature), code D (open-textured, "an interpretive canon") and code E (EU-withdrawal vocabulary), and the phrase "no input from which an answer would differ", are not among the three reasons for `inert` (not operative; machinery; text shown repealed or blank).
A definition is encoded as a row of a defined-term table that returns what the Act states: the members it names, what it includes or excludes, what it points at; the borrowed term or fact that it points at is asked as an input where a rule needs it.
Sections 20(2A) to 20A, 23ZA, 23A, 23B, 23C and 24 are encoded as rules over inputs for the dates and terms that other Acts give.

Pass 1 also marked some sections `encoded` while leaving part of their text out, and those parts are found here by reading the rows at subsection grain: s 14A(6) (the definition of "specified"), s 20(2A) to (6), s 22(1)'s carve-out for s 20(2A) to (6) and s 20A, s 22(2), s 23(2), the second limb of s 23(3) (s 17(2)(a) and deeds), and the "corresponding provision" of s 25(2).
They are rows of their own now.

What stays `inert` is what the three reasons allow: the title, chapter, long title, date of enactment, the cross-headings, the Schedule headings and cross-references and the note to Schedule 1 (reason 1: not operative); s 25(1), a repeal of other enactments by reference to a Schedule that this text shows empty, and s 27, the short title (reason 2: machinery).
The lines of dots, and Schedule 3, which this text shows without a single row, are `repealed or blank in this text`; each such row says what the text shows.
Section 26 stays `encoded` (pass 1 used the date in every "after the commencement" test); it is machinery too, but a disposition of `encoded` is always allowed.

<!-- BEGIN:audit-tables -->
Counted by `tools/units.py` from the text (rule in its header): **436 units**.

| kind of unit | count |
| --- | --- |
| Schedule paragraph | 18 |
| closing words | 16 |
| cross-heading | 21 |
| defined term | 98 |
| defined term (further) | 21 |
| elision | 10 |
| elision mark | 8 |
| front matter | 4 |
| paragraph | 113 |
| section | 18 |
| sub-paragraph | 3 |
| subsection | 61 |
| table row | 45 |
| **total** | **436** |

The pass-1 table had **161 rows** (40 encoded, 111 inert, 10 repealed or blank in this text), at the grain of a section or a Schedule 1 entry; 134 of the 436 units had a row of their own there, so **302 units were missing from it**.
The table below (`coverage.tsv`, rendered under "Coverage table") has **436 rows**, one per unit: 367 encoded, 21 fork, 26 inert, 22 repealed or blank in this text.

### Units that had no row of their own in pass 1 (302)

Grouped by the section or Schedule they sit in; each is now a row.

- `front` (4): `front:title`, `front:chapter`, `front:long title`, `front:date of enactment`
- `s4` (3): `s4`, `s4(a)`, `s4(b)`
- `s6` (4): `s6`, `s6(a)`, `s6(b)`, `s6(c)`
- `s11` (1): `s11`
- `s12` (2): `s12(1)`, `s12(2)`
- `s13` (3): `s13`, `s13(a)`, `s13(b)`
- `s14` (4): `s14`, `s14(a)`, `s14(b)`, `s14.closing`
- `s14A` (11): `s14A(1)`, `s14A(1)(a)`, `s14A(1)(b)`, `s14A(2)`, `s14A(2)(a)`, `s14A(2)(b)`, `s14A(2)(c)`, `s14A(3)`, `s14A(4)`, `s14A(5)`, `s14A(6)`
- `s16` (8): `s16(1)`, `s16(1)(a)`, `s16(1)(b)`, `s16(1)(c)`, `s16(1)(d)`, `s16(1)(e)`, `s16(1).closing`, `s16(2)`
- `s17` (4): `s17(1)`, `s17(2)`, `s17(2)(a)`, `s17(2)(b)`
- `s19` (5): `s19(1)`, `s19(1)(a)`, `s19(1)(b)`, `s19(1)(c)`, `s19(2)`
- `s20` (10): `s20(1)`, `s20(2)`, `s20(2A)`, `s20(2A)(a)`, `s20(2A)(b)`, `s20(2A).closing`, `s20(3)`, `s20(4)`, `s20(5)`, `s20(6)`
- `s20A` (1): `s20A`
- `s21` (3): `s21(1)`, `s21(1)#subordinate legislation`, `s21(2)`
- `s22` (3): `s22(1)`, `s22(2)`, `s22(3)`
- `s23` (4): `s23(1)`, `s23(2)`, `s23(3)`, `s23(4)`
- `s23A` (8): `s23A(1)`, `s23A(2)`, `s23A(2)(a)`, `s23A(2)(b)`, `s23A(3)`, `s23A(3)(a)`, `s23A(3)(b)`, `s23A(4)`
- `s23B` (20): `s23B(1)`, `s23B(1)(a)`, `s23B(1)(b)`, `s23B(2)`, `s23B(2)(a)`, `s23B(2)(b)`, `s23B(2).closing`, `s23B(3)`, `s23B(3)(a)`, `s23B(3)(b)`, `s23B(3)(c)`, `s23B(4)`, `s23B(5)`, `s23B(6)`, `s23B(6)#Welsh zone`, `s23B(6)#Wales`, `s23B(7)`, `s23B(7)(a)`, `s23B(7)(b)`, `s23B(7).closing`
- `s23C` (16): `s23C(1)`, `s23C(1)(a)`, `s23C(1)(b)`, `s23C(1)(c)`, `s23C(1)(d)`, `s23C(1).closing`, `s23C(1A)`, `s23C(2)`, `s23C(3)`, `s23C(3)(a)`, `s23C(3)(b)`, `s23C(3).closing`, `s23C(4)`, `s23C(4)(a)`, `s23C(4)(b)`, `s23C(4).closing`
- `s23ZA` (24): `s23ZA(1)`, `s23ZA(1)(a)`, `s23ZA(1)(b)`, `s23ZA(1).closing`, `s23ZA(2)`, `s23ZA(2)(a)`, `s23ZA(2)(b)`, `s23ZA(2)(c)`, `s23ZA(3)`, `s23ZA(4)`, `s23ZA(4)(a)`, `s23ZA(4)(a)(i)`, `s23ZA(4)(a)(i)#elision`, `s23ZA(4)(a)(ia)`, `s23ZA(4)(a)(ii)`, `s23ZA(4)(b)`, `s23ZA(5)`, `s23ZA(6)`, `s23ZA(6)“corresponding time”`, `s23ZA(6)“devolution legislation”`, `s23ZA(6)(a)`, `s23ZA(6)(b)`, `s23ZA(6)(c)`, `s23ZA(6)(d)`
- `s24` (32): `s24(1)`, `s24(2)`, `s24(3)`, `s24(3A)`, `s24(4)`, `s24(4).row1`, `s24(4).row2`, `s24(4).row2#elision`, `s24(4).row3`, `s24(4).row4`, `s24(4).row5`, `s24(4).row6`, `s24(4).row7`, `s24(4).row8`, `s24(4).row9`, `s24(4).row10`, `s24(4).row11`, `s24(4).row12`, `s24(4).row13`, `s24(4).row14`, `s24(4).row15`, `s24(4).row16`, `s24(4).row17`, `s24(4).closing`, `s24(5)`, `s24(5)(a)`, `s24(5)(b)`, `s24(5)(c)`, `s24(5)(d)`, `s24(5)(e)`, `s24(5)(f)`, `s24(5)(g)`
- `s25` (3): `s25(1)`, `s25(2)`, `s25(3)`
- `sch1` (72): `sch1:heading`, `sch1:reference`, `sch1:note`, `sch1:definitions-heading`, `sch1:Colony`, `sch1:Colony(a)`, `sch1:Colony(b)`, `sch1:Colony(c)`, `sch1:Colony.closing`, `sch1:Committed for trial`, `sch1:Committed for trial(a)`, `sch1:Committed for trial(b)`, `sch1:Committed for trial(b)#elision`, `sch1:County court`, `sch1:County court(a)`, `sch1:County court(b)`, `sch1:Court of Appeal`, `sch1:Court of Appeal(a)`, `sch1:Court of Appeal(b)`, `sch1:Crown Court`, `sch1:Crown Court(a)`, `sch1:Crown Court(b)`, `sch1:High Court`, `sch1:High Court(a)`, `sch1:High Court(b)`, `sch1:Lands Clauses Acts`, `sch1:Lands Clauses Acts(a)`, `sch1:Lands Clauses Acts(b)`, `sch1:Lands Clauses Acts(c)`, `sch1:Magistrates’ court`, `sch1:Magistrates’ court(a)`, `sch1:Magistrates’ court(b)`, `sch1:Police area`, `sch1:Police area#elision`, `sch1:Police area(a)`, `sch1:Police area(b)`, `sch1:The standard scale`, `sch1:The standard scale(a)`, `sch1:The standard scale(b)`, `sch1:The standard scale(c)`, `sch1:Statutory maximum`, `sch1:Statutory maximum(a)`, `sch1:Statutory maximum(b)`, `sch1:Statutory maximum(c)`, `sch1:group:offences`, `sch1:group:offences:p1`, `sch1:group:offences:p1(a)`, `sch1:group:offences:p1(b)`, `sch1:group:offences:p1(c)`, `sch1:group:offences:p1.closing`, `sch1:group:offences:p2`, `sch1:group:offences:p3`, `sch1:group:relationships`, `sch1:group:relationships:p1`, `sch1:group:relationships:p1(a)`, `sch1:group:relationships:p1(b)`, `sch1:group:relationships:p1(c)`, `sch1:group:relationships:p1.closing`, `sch1:group:police-scotland`, `sch1:group:police-scotland:p1`, `sch1:group:police-scotland:p1(a)`, `sch1:group:police-scotland:p1(b)`, `sch1:group:police-scotland:p1(c)`, `sch1:group:police-scotland:p1(d)`, `sch1:group:police-scotland:p1(e)`, `sch1:Assimilated obligation`, `sch1:Assimilated obligation(a)`, `sch1:Assimilated obligation(b)`, `sch1:Assimilated obligation.closing`, `sch1:EEA state`, `sch1:EEA state(a)`, `sch1:EEA state(b)`
- `sch2` (48): `sch2:heading`, `sch2:reference`, `sch2.p1`, `sch2.p1.row1`, `sch2.p1.row2`, `sch2.p1.row3`, `sch2.p1.row4`, `sch2.p1.row5`, `sch2.p1.row6`, `sch2.p1.row7`, `sch2.p2`, `sch2.p2.row1`, `sch2.p2.row2`, `sch2.p2.row3`, `sch2.p2.row4`, `sch2.p2.row5`, `sch2.p2.row6`, `sch2.p3`, `sch2.p3.row1`, `sch2.p3.row2`, `sch2.p3.row3`, `sch2.p3.row4`, `sch2.p3.row5`, `sch2.p3.row6`, `sch2.p3.row7`, `sch2.p3.row8`, `sch2.p3.row9`, `sch2.p3.row10`, `sch2.p4(1)`, `sch2.p4(1)(a)`, `sch2.p4(1)(a)#elision`, `sch2.p4(1)(b)`, `sch2.p4(3)`, `sch2.p4(3)(a)`, `sch2.p4(3)(b)`, `sch2.p4.closing`, `sch2.p5`, `sch2.p5(a)`, `sch2.p5(b)`, `sch2.p5(c)`, `sch2.p6`, `sch2.p6.elision@430`, `sch2.p6.row1`, `sch2.p6.row2`, `sch2.p6.row3`, `sch2.p6.row4`, `sch2.p6.row5`, `sch2.p6.closing`
- `sch3` (2): `sch3:heading`, `sch3:reference`
- `sched` (1): `sched:schedules`
- `xhead` (6): `xhead:General provisions as to enact`, `xhead:Interpretation and constructio`, `xhead:Statutory powers and duties`, `xhead:Repealing enactments`, `xhead:Miscellaneous`, `xhead:Supplementary`

### Verdict on every pass-1 row that was not `encoded`

One line each. The verdict is read from the new table: the dispositions of the units that lie in the pass-1 row's lines.

| pass-1 row | lines | pass-1 disposition | verdict |
| --- | --- | --- | --- |
| Preliminary | 1-5 | inert | keeps `inert`, reason 1 (not operative) |
| s 1 | 6-7 | inert | **moves out of `inert`**: 1 encoded |
| s 20A | 96-98 | inert | **moves out of `inert`**: 1 encoded, 1 inert |
| s 23ZA | 111-134 | inert | **moves out of `inert`**: 23 encoded, 1 repealed or blank in this text |
| s 23A | 135-143 | inert | **moves out of `inert`**: 8 encoded |
| s 23B | 144-162 | inert | **moves out of `inert`**: 20 encoded |
| s 23C | 163-179 | inert | **moves out of `inert`**: 15 encoded, 1 fork |
| s 24 | 180-211 | inert | **moves out of `inert`**: 30 encoded, 2 repealed or blank in this text |
| s 27 | 218-219 | inert | keeps `inert`, reason 2 (machinery) |
| Sch 1 heading | 220-224 | inert | keeps `inert`, reason 1 (not operative) |
| Sch 1 “Associated state” | 226 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Bank of England” | 227 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Bank of Ireland” | 228 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “British Islands” | 229 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “British overseas territory” | 230 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “British possession” | 231 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 line 232 | 232 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 “Building regulations” | 233 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Central funds” | 234 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Charity Commission” | 235 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Church Commissioners” | 236 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Civil partnership” | 237 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Colonial legislature” | 238 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “Colony” | 239-243 | inert | **moves out of `inert`**: 5 encoded |
| Sch 1 “Committed for trial” | 245-247 | inert | **moves out of `inert`**: 2 encoded, 2 repealed or blank in this text |
| Sch 1 line 248 | 248 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 “Comptroller and Auditor General” | 249 | inert | **moves out of `inert`**: 1 encoded, 1 repealed or blank in this text |
| Sch 1 “Consular officer” | 250 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The Corporation Tax Acts” | 251 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “County court” | 252-254 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Court of Appeal” | 255-257 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Court of Judicature” | 258 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Court of summary jurisdiction” | 259 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Crown Court” | 260-262 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Crown Estate Commissioners” | 263 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 line 264 | 264 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 line 265 | 265 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 “Enactment” | 266 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “England” | 267 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Governor-General” | 269 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “Her Majesty’s Revenue and Customs” | 270 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “High Court” | 271-273 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “The Immigration Acts” | 274 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The Income Tax Acts” | 275 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Land” | 276 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Lands Clauses Acts” | 277-280 | inert | **moves out of `inert`**: 4 encoded |
| Sch 1 “Local land charges register” | 281 | inert | **moves out of `inert`**: 1 encoded, 1 repealed or blank in this text |
| Sch 1 “Local policing body” | 282 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “London borough” | 283 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Lord Chancellor” | 284 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Magistrates’ court” | 285-287 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “National Debt Commissioners” | 289 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Northern Ireland legislation” | 290 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Oath” | 291 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Officer of a provider of probation services” | 292 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Officer of Revenue and Customs” | 293 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Ordnance Map” | 294 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Parliamentary Election” | 295 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “PAYE income” | 296 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “PAYE regulations” | 297 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Person” | 298 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Police and crime commissioner” | 299 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Police area” | 300-302 | inert | **moves out of `inert`**: 2 encoded, 2 repealed or blank in this text |
| Sch 1 line 303 | 303 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 “Police Service of Northern Ireland” | 304 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “The Privy Council” | 305 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Provider of probation services” | 306 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Registered” | 307 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Registered medical practitioner” | 308 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Registered provider of social housing” | 309 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “Rules of Court” | 310 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Secretary of State” | 311 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Senior Courts” | 312 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Sent for trial” | 313 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The Sentencing Code” | 314 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Sewerage undertaker” | 315 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Sheriff” | 316 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The standard scale” | 317-320 | inert | **moves out of `inert`**: 4 encoded |
| Sch 1 “Statutory declaration” | 321 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Statutory maximum” | 322-325 | inert | **moves out of `inert`**: 4 encoded |
| Sch 1 “Supreme Court” | 326 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The Tax Acts” | 327 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The Treasury” | 328 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Trust of land” | 329 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “United Kingdom” | 330 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Wales” | 331 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Water undertaker” | 332 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Writing” | 333 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 line 334 | 334 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 line 335 | 335 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 paragraph group | 336-343 | inert | **moves out of `inert`**: 7 encoded, 1 inert |
| Sch 1 paragraph group | 344-349 | inert | **moves out of `inert`**: 5 encoded, 1 inert |
| Sch 1 paragraph group | 350-356 | inert | **moves out of `inert`**: 6 encoded, 1 inert |
| Sch 1 group 357 | 357 | inert | keeps `inert`, reason 1 (not operative) |
| Sch 1 “Assimilated law” | 358 | inert | **moves out of `inert`**: 4 encoded |
| Sch 1 “Assimilated obligation” | 359-362 | inert | **moves out of `inert`**: 4 encoded |
| Sch 1 “The Communities” | 363 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “E.C.S.C. Treaty” | 364 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “EEA agreement” | 365 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “EEA state” | 366-368 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “E.E.C. Treaty” | 369 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Entry date” | 370 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “The EU” | 371 | inert | **moves out of `inert`**: 2 encoded |
| Sch 1 “EU institution” | 372 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “EU instrument” | 373 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Euratom” | 374 | inert | **moves out of `inert`**: 3 encoded |
| Sch 1 “Euratom Treaty” | 375 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “European Court” | 376 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “EU withdrawal agreement” | 377 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Exit day” | 378 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “IP completion day” | 379 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 “Member” | 380 | inert | **moves out of `inert`**: 1 encoded |
| Sch 1 line 381 | 381 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 line 382 | 382 | repealed or blank in this text | keeps `repealed or blank in this text` |
| Sch 1 “The Treaties” | 383 | inert | **moves out of `inert`**: 2 encoded |
| Sch 2 Part I para 4(2) | 416 | inert | **moves out of `inert`**: 1 fork |
| Sch 2 Part I para 4(3) | 417-420 | inert | **moves out of `inert`**: 2 encoded, 2 fork |
| Sch 2 Part I para 4(5) | 422 | inert | **moves out of `inert`**: 1 encoded |
| Sch 2 Part I para 4(6) | 423 | inert | **moves out of `inert`**: 1 fork, 1 repealed or blank in this text |
| Sch 2 Part I para 5 | 424-427 | inert | **moves out of `inert`**: 3 encoded, 1 fork |
| Sch 3 | 439-440 | repealed or blank in this text | keeps its disposition (inert reason 1; the rest, which the text shows as dots or as no row, is `repealed or blank`) |
<!-- END:audit-tables -->

## What the Act answers about time, and what it does not

This is the finding the brief asks for, stated first.

- **It answers when an enactment comes into force (s 4), and the moment: "at the beginning of that day".**
  An Act or a provision of an Act that makes provision for a particular day comes into force at the beginning of that day (s 4(a)).
  One that makes no provision comes into force at the beginning of the day on which the Act receives the Royal Assent (s 4(b)).
  Subordinate legislation is reached by s 4(a) (s 23(1), and Sch 2 para 6 for earlier instruments) and **not** by s 4(b), which s 23(1) excepts.
  So subordinate legislation that says nothing about its coming into force has no answer in the Act.
- **It answers what time standard an Act's references to time use (s 9): Greenwich mean time, subject to s 3 of the Summer Time Act 1972, whose text is not among the sources.**
- **It does NOT say how a period of days, weeks, months or years is counted.**
  The text has no counting rule: no "from", "after", "beginning with", "clear days", "exclusive" or "inclusive" anywhere in it (searched; see "Where I looked" below).
  It does not define "day", "week" or "year".
  It defines "month" as "calendar month" (Sch 1, mark [1850]) and "financial year" for stated matters only (Sch 1, [1889]), and says nothing of how a period of months is counted, of a start on the 31st, or of a start on 29 February.
- **It does NOT mention days of rest, recess or holidays**, nor any closed office.
  There is no rule that moves the last day of a period, for days or for months or years, and so no rule for several in a row.
- **It has no rule on which language version of the text has authority.**
  The only mention of a language is the "Welsh Language Act 1967" in Sch 2 para 5(a).

So the six worked period cases are **named REFUSEs**, not computed dates, and the reusable time module `uk-interpretation-time.l4` says so by name for each item the brief lists.
That is the answer the text gives, and the module is built to hand it back as a refusal with the reason, not as a plausible default (the brief forbids the latter).

## What is encoded

| module | what it holds | tests |
| --- | --- | --- |
| `uk-interpretation-time.l4` (imports only `prelude` and `daydate`) | s 4 commencement (day and moment); s 4(a), 4(b) reach; s 9 time standard; s 13 anticipatory exercise; s 26 and the commencement day; Sch 1 "Month", "Financial year", "Commencement"; named refusals for the six time-computation items | `tests-time.l4` (141) |
| `uk-interpretation-service.l4` | s 7 deemed service by post, and the deemed time | `tests-service.l4` (22) |
| `uk-interpretation-repeals.l4` | ss 2, 15, 16, 17 | `tests-repeals.l4` (42) |
| `uk-interpretation-construction.l4` | ss 3, 6, 8, 10, 11, 12, 14, 14A(1) to (5), 18, 19, 20(1), 20(2), 21 | `tests-construction.l4` (155) |
| `uk-interpretation-application.l4` | ss 5, 22(1) (the Act itself, Part I of Schedule 2), 22(3), 23(1), (3) first limb, (4), 25(2) first half, 25(3) and Sch 2 (Parts I and II), with Sch 1's year and date marks as Sch 2 para 4 reads them | `tests-application.l4` (545) |
| `uk-interpretation-schedule1.l4` (pass 2, **generated** from `tools/schedule1.tsv` by `tools/gen_schedule1.py`) | the whole of Schedule 1 as a table of 110 entries, limbs and groups: what each states, what it points at, how (`means`, `includes`, `pointer`, ...) and its year or date mark; the entry in the text's own words | `tests-schedule1.l4` (1033, generated from the same text) |
| `uk-interpretation-definitions.l4` (pass 2) | the Schedule 1 entries that decide something (British Islands, British possession, colony, colonial legislature, Governor, enactment, land, oath, person, writing, Rules of Court, Bank of England and of Ireland, Parliamentary election, the Tax Acts, the EU entries, offences, relationships, police: Scotland) and Sch 2 paras 4(2), 4(3), 4(5), 4(6) and 5 | `tests-definitions.l4` (241) |
| `uk-interpretation-general.l4` (pass 2) | s 1, s 14A(6), s 22(2), s 23(2), s 23(3) second limb, s 25(2) second half (the corresponding provision, as an explicit not-covered value) | `tests-general.l4` (44) |
| `uk-interpretation-eu.l4` (pass 2) | s 20(2A) to (6), s 20A, and the carve-out of s 22(1) for them | `tests-eu.l4` (58) |
| `uk-interpretation-devolved.l4` (pass 2) | ss 23ZA, 23A, 23B, 23C and 24 | `tests-devolved.l4` (264) |
| (none) | `tests-direct.l4` (94): direct assertions on pass-1 helper functions that the pass-1 tests reach only through a local helper or their callers, so that the coverage table can name an assertion for each function it cites | `tests-direct.l4` |
| (none) | `tests-red.l4`: seven expectations that are meant to fail | `check.sh` expects exactly 7 failed assertions in it |

The six functions the brief names, in `uk-interpretation-time.l4`, with the section that governs each (the text is silent on four):

| brief item | function | text |
| --- | --- | --- |
| 1 the last day of N days or weeks counted from a day | `the last day of a period of days counted from a day`, `the last day of a period of weeks counted from a day` | silent: named REFUSE |
| 2 the last day of N months or years counted after an event | `the last day of a period of months counted after an event`, `the last day of a period of years counted after an event` | Sch 1 "Month" (src:288) defines the word only: named REFUSE |
| 3 a last day that is a day of rest, recess or holiday | `the last day of a period once days of rest, recess and holidays are considered` (takes the caller's `FUNCTION FROM DATE TO BOOLEAN`) | silent: named REFUSE |
| 4 whether a date falls in a period | `the day falls inside a period of days counted from a day`, `the day falls inside a period of months counted after an event` (refuse); `the day falls inside the period` (a helper over a first and last day the caller supplies, **not a rule of the Act**) | silent for counted periods |
| 5 the day, and moment, from which an enactment binds | `section 4 — when the enactment comes into force` | s 4 (src:12-15) |
| 6 the day subordinate legislation comes into force | the same function, with kind `subordinate legislation` | s 4(a) via s 23(1) and Sch 2 para 6; silent for s 4(b) |

The other items of the brief's scope list: deemed service (item 4) is s 7, in `uk-interpretation-service.l4`; what a repeal does (item 5) is ss 15 to 17, in `uk-interpretation-repeals.l4`; the meanings of time words (item 6) are `Schedule 1 — the meaning of the time word, in the text's own words` (month: "calendar month"; financial year: "the twelve months ending with 31st March"; day, week and year: named REFUSE), `Schedule 1 — the meaning of month in` and `Schedule 1 — the financial year`, all in `uk-interpretation-time.l4`.

Days of rest, recess and holiday are an input: the rest-day function takes `FUNCTION FROM DATE TO BOOLEAN`, and the tests supply one (a weekend plus one named holiday, so three days in a row).
No holiday calendar is built in.

**Maintaining it.**
The four hand-written pass-2 modules (`definitions`, `general`, `eu`, `devolved`) and their tests are plain `.l4` files: edit them directly; the `-- src:` lines in them are quotations that `srcrefs.py check --refs` reads back against the raw text.
`uk-interpretation-schedule1.l4` and `tests-schedule1.l4` are **generated**: edit `tools/schedule1.tsv` (which `python3 -I tools/gen_schedule1.py check <raw> tools/schedule1.tsv` verifies field by field against the text) and run `python3 -I tools/gen_schedule1.py gen <raw> tools/schedule1.tsv`; the run in pass 2 reproduced the committed files exactly.
The coverage table in this file is generated from `tools/coverage.tsv` by `python3 -I tools/coverage.py splice NOTES.md <raw> tools/coverage.tsv tools/pass1-coverage.tsv`; do not edit the table between the markers by hand.

## What is not encoded

**No row is out for a pass-1 reason.**
Pass 1 left 111 rows `inert` for reasons the pass-2 brief withdraws; the re-disposition audit above gives the verdict on each, and 107 of the pass-1 rows that were not `encoded` moved out of `inert` or of `repealed or blank`.
What remains out of the encoding is 26 `inert` rows and 22 `repealed or blank in this text` rows:

- `inert`, reason 1 (not operative), 24 rows: the title, chapter number, long title and date of enactment; the six cross-headings between the groups of sections; the word "SCHEDULES"; the headings, reference lines, note and group headings of Schedules 1 and 2 (including the headings of the three groups of "Construction of ..." entries and the heading of the EU entries); the Schedule 3 reference line.
- `inert`, reason 2 (machinery), 2 rows: s 25(1) (repeals the enactments of Schedule 3) and s 27 (short title).
- `repealed or blank in this text`, 22 rows: the lines made only of dots (Sch 1 lines 232, 248, 264, 265, 303, 334, 335, 381 and 382; Sch 2 line 430; the first limb of s 24(4), line 186); the dots inside lines (ss 23ZA(4)(a)(i), the second limb of s 24(4), Sch 1 "Committed for trial" limbs (a) and (b), "Comptroller and Auditor General", "Local land charges register", "Police area" and its limb (b), Sch 2 paras 4(1)(a) and 4(6)); and the Schedule 3 heading, which has no table under it in this text.

What the text does not answer, and what the encoding does about it, is in "What the Act answers about time, and what it does not" above, the fork register (F1 to F27), and "What is needed before relying on this" below.

## Coverage table

One row per unit of the text (the rule is in `tools/units.py`), generated from `tools/coverage.tsv`.
Dispositions: `encoded`, `fork` (the row points at the fork-register entry below and at the rule that encodes the chosen reading, or at the explicit "not covered" value), `inert` (reason 1 not operative, 2 machinery), `repealed or blank in this text` (the detail says what the text shows).
The `where` column names the functions that encode the unit; each is defined in a module and asserted in a tests file, which `tools/coverage.py check` verifies.
A `ctor:` name is a constructor of the Schedule 1 table in `uk-interpretation-schedule1.l4`.
A row id with `#` is a further defined term of an entry, or an elision mark inside a unit.

<!-- BEGIN:coverage-table -->
| id | lines | kind | text | disposition | detail | where |
| --- | --- | --- | --- | --- | --- | --- |
| front:title | 1 | front matter | Interpretation Act 1978 | inert | reason 1 |  |
| front:chapter | 2 | front matter | 1978 c.30 | inert | reason 1 |  |
| front:long title | 3 | front matter | An Act to consolidate the Interpretation Act 1889 and certain other enactments r | inert | reason 1 |  |
| front:date of enactment | 4 | front matter | [20th July 1978] | inert | reason 1 |  |
| xhead:General provisions as to enact | 5 | cross-heading | General provisions as to enactment and operation | inert | reason 1 |  |
| s1 | 6-7 | section | 1 — Words of enactment. Every section of an Act takes effect as a substantive en | encoded |  | `section 1 provides that a section of an Act takes effect as a substantive enactment, for an Act passed on` |
| s2 | 8-9 | section | 2 — Amendment or repeal in same Session. Any Act may be amended or repealed in t | encoded |  | `section 2 permits amendment or repeal in` |
| s3 | 10-11 | section | 3 — Judicial notice. Every Act is a public Act to be judicially noticed as such, | encoded |  | `section 3 provides that the Act is a public Act to be judicially noticed as such` |
| s4 | 12-13 | section | 4 — Time of commencement. An Act or provision of an Act comes into force— | fork | F18 | `section 4 — when the enactment comes into force` |
| s4(a) | 14 | paragraph | (a) where provision is made for it to come into force on a particular day, at th | fork | F5, F6 | `section 4 — when the enactment comes into force`; `section 4 read with section 9 — the clock reading of the moment` |
| s4(b) | 15 | paragraph | (b) where no provision is made for its coming into force, at the beginning of th | fork | F10, F20, F21 | `section 4 — when the enactment comes into force`; `section 4 read with section 9 — the clock reading of the moment` |
| xhead:Interpretation and constructio | 16 | cross-heading | Interpretation and construction | inert | reason 1 |  |
| s5 | 17-18 | section | 5 — Definitions. In any Act, unless the contrary intention appears, words and ex | encoded |  | `section 5 provides that the word is to be construed according to Schedule 1` |
| s6 | 19-20 | section | 6 — Gender and number. In any Act, unless the contrary intention appears,— | encoded |  | `section 6(a) provides that a masculine word includes`; `section 6(b) provides that a feminine word includes`; `section 6(c) provides that a word in one number includes` |
| s6(a) | 21 | paragraph | (a) words importing the masculine gender include the feminine; | encoded |  | `section 6(a) provides that a masculine word includes` |
| s6(b) | 22 | paragraph | (b) words importing the feminine gender include the masculine; | encoded |  | `section 6(b) provides that a feminine word includes` |
| s6(c) | 23 | paragraph | (c) words in the singular include the plural and words in the plural include the | encoded |  | `section 6(c) provides that a word in one number includes` |
| s7 | 24-25 | section | 7 — References to service by post. Where an Act authorises or requires any docum | fork | F11 | `section 7 applies to`; `section 7 deems service to be effected by posting`; `section 7 — the time at which service is deemed to be effected` |
| s8 | 26-27 | section | 8 — References to distance. In the measurement of any distance for the purposes  | encoded |  | `section 8 — the way a distance is measured` |
| s9 | 28-29 | section | 9 — References to time of day. Subject to section 3 of the Summer Time Act 1972  | fork | F6 | `section 9 — the time standard of an expression of time in an Act`; `section 4 read with section 9 — the clock reading of the moment` |
| s10 | 30-31 | section | 10 — References to the Sovereign. In any Act a reference to the Sovereign reigni | encoded |  | `section 10 — the Sovereign a reference is to be construed as` |
| s11 | 32-33 | section | 11 — Construction of subordinate legislation. Where an Act confers power to make | encoded |  | `section 11 provides that an expression used in the subordinate legislation has the meaning which it bears in the Act` |
| xhead:Statutory powers and duties | 34 | cross-heading | Statutory powers and duties | inert | reason 1 |  |
| s12(1) | 35-36 | subsection | 12 — Continuity of powers and duties. (1) Where an Act confers a power or impose | encoded |  | `section 12(1) provides that the power may be exercised, or the duty is to be performed, from time to time as occasion requires` |
| s12(2) | 37 | subsection | (2) Where an Act confers a power or imposes a duty on the holder of an office as | encoded |  | `section 12(2) provides that the power may be exercised, or the duty is to be performed, by the holder for the time being of the office` |
| s13 | 38-39 | section | 13 — Anticipatory exercise of powers. Where an Act which (or any provision of wh | fork | F8 | `the conditions of section 13 are met by`; `section 13 permits an instrument made under the Act to come into force at`; `section 13 permits the power to be exercised on` |
| s13(a) | 40 | paragraph | (a) of bringing the Act or any provision of the Act into force; or | encoded |  | `the conditions of section 13 are met by`; `section 13 permits an instrument made under the Act to come into force at`; `section 13 permits the power to be exercised on` |
| s13(b) | 41 | paragraph | (b) of giving full effect to the Act or any such provision at or after the time  | encoded |  | `the conditions of section 13 are met by`; `section 13 permits an instrument made under the Act to come into force at`; `section 13 permits the power to be exercised on` |
| s14 | 42-43 | section | 14 — Implied power to amend. Where an Act confers power to make— | encoded |  | `section 14 provides a power to revoke, amend or re-enact any instrument made under the power` |
| s14(a) | 44 | paragraph | (a) rules, regulations or byelaws; or | encoded |  | `section 14 provides a power to revoke, amend or re-enact any instrument made under the power` |
| s14(b) | 45 | paragraph | (b) Orders in Council, orders or other subordinate legislation to be made by sta | encoded |  | `section 14 provides a power to revoke, amend or re-enact any instrument made under the power` |
| s14.closing | 46 | closing words | it implies, unless the contrary intention appears, a power, exercisable in the s | encoded |  | `section 14 provides a power to revoke, amend or re-enact any instrument made under the power` |
| s14A(1) | 47-48 | subsection | 14A — Power to include sunset and review provisions in subordinate legislation ( | encoded |  | `section 14A applies to the power or duty` |
| s14A(1)(a) | 49 | paragraph | (a) the power or duty is exercisable by the Scottish Ministers, or | encoded |  | `section 14A applies to the power or duty` |
| s14A(1)(b) | 50 | paragraph | (b) the power or duty is exercisable by any other person within devolved compete | encoded |  | `section 14A applies to the power or duty` |
| s14A(2) | 51 | subsection | (2) The subordinate legislation may include— | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(2)(a) | 52 | paragraph | (a) provision requiring the person to review the effectiveness of the legislatio | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(2)(b) | 53 | paragraph | (b) provision for the legislation to cease to have effect at the end of a specif | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(2)(c) | 54 | paragraph | (c) if the power or duty is being exercised to amend other subordinate legislati | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(3) | 55 | subsection | (3) The provision that may be made by virtue of subsection (2)(a) includes provi | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(4) | 56 | subsection | (4) Subordinate legislation including provision of a kind mentioned in subsectio | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(5) | 57 | subsection | (5) Subordinate legislation including provision of a kind mentioned in subsectio | encoded |  | `section 14A permits subordinate legislation to include` |
| s14A(6) | 58 | subsection | (6) In this section, “specified” means specified in the subordinate legislation. | encoded |  | `section 14A(6) counts the period or day as specified` |
| xhead:Repealing enactments | 59 | cross-heading | Repealing enactments | inert | reason 1 |  |
| s15 | 60-61 | section | 15 — Repeal of repeal. Where an Act repeals a repealing enactment, the repeal do | encoded |  | `section 15 provides that the repeal of a repealing enactment does not revive the enactment previously repealed` |
| s16(1) | 62-63 | subsection | 16 — General savings. (1) Without prejudice to section 15, where an Act repeals  | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1)(a) | 64 | paragraph | (a) revive anything not in force or existing at the time at which the repeal tak | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1)(b) | 65 | paragraph | (b) affect the previous operation of the enactment repealed or anything duly don | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1)(c) | 66 | paragraph | (c) affect any right, privilege, obligation or liability acquired, accrued or in | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1)(d) | 67 | paragraph | (d) affect any penalty, forfeiture or punishment incurred in respect of any offe | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1)(e) | 68 | paragraph | (e) affect any investigation, legal proceeding or remedy in respect of any such  | encoded |  | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s16(1).closing | 69 | closing words | and any such investigation, legal proceeding or remedy may be instituted, contin | encoded |  | `section 16(1) provides that it may be instituted, continued, enforced or imposed as if the repealing Act had not been passed` |
| s16(2) | 70 | subsection | (2) This section applies to the expiry of a temporary enactment as if it were re | encoded |  | `section 16 treats the way the enactment ceases as a repeal by an Act` |
| s17(1) | 71-72 | subsection | 17 — Repeal and re-enactment. (1) Where an Act repeals a previous enactment and  | fork | F12 | `section 17(1) provides that the repealed enactment remains in force on` |
| s17(2) | 73 | subsection | (2) Where an Act repeals and re-enacts, with or without modification, a previous | encoded |  | `section 17(2)(a) provides that a reference to the repealed enactment is a reference to the provision re-enacted` |
| s17(2)(a) | 74 | paragraph | (a) any reference in any other enactment to the enactment so repealed shall be c | encoded |  | `section 17(2)(a) provides that a reference to the repealed enactment is a reference to the provision re-enacted` |
| s17(2)(b) | 75 | paragraph | (b) in so far as any subordinate legislation made or other thing done under the  | encoded |  | `section 17(2)(b) provides that the subordinate legislation or thing has effect as if made or done under the provision re-enacted` |
| xhead:Miscellaneous | 76 | cross-heading | Miscellaneous | inert | reason 1 |  |
| s18 | 77-78 | section | 18 — Duplicated offences. Where an act or omission constitutes an offence under  | encoded |  | `section 18 provides that the offender is liable to be prosecuted under either or any of those Acts or at common law`; `section 18 provides that the offender is not liable to be punished more than once for the same offence` |
| s19(1) | 79-80 | subsection | 19 — Citation of other Acts. (1) Where an Act cites another Act by year, statute | encoded |  | `section 19(1) — the edition a citation is read as referring to` |
| s19(1)(a) | 81 | paragraph | (a) in the case of Acts included in any revised edition of the statutes printed  | encoded |  | `section 19(1) — the edition a citation is read as referring to` |
| s19(1)(b) | 82 | paragraph | (b) in the case of Acts not so included but included in the edition prepared und | encoded |  | `section 19(1) — the edition a citation is read as referring to` |
| s19(1)(c) | 83 | paragraph | (c) in any other case, to the Acts printed by the Queen’s Printer, or under the  | encoded |  | `section 19(1) — the edition a citation is read as referring to` |
| s19(2) | 84 | subsection | (2) An Act may continue to be cited by the short title authorised by any enactme | encoded |  | `section 19(2) provides that the Act may continue to be cited by the short title notwithstanding the repeal of the enactment` |
| s20(1) | 85-86 | subsection | 20 — References to other enactments etc.. (1) Where an Act describes or cites a  | encoded |  | `section 20(1) provides that the portion described or cited includes` |
| s20(2) | 87 | subsection | (2) Where an Act refers to an enactment, the reference, unless the contrary inte | encoded |  | `section 20(2) provides that the reference is a reference to the enactment as amended, extended or applied` |
| s20(2A) | 88 | subsection | (2A) Where— | encoded |  | `section 20(2A) — how the reference is read`; `section 22(1) with its carve-out — the extent to which the provision applies to an Act passed on` |
| s20(2A)(a) | 89 | paragraph | (a) an Act passed on or after IP completion day refers to any treaty relating to | encoded |  | `section 20(2A) — how the reference is read`; `section 22(1) with its carve-out — the extent to which the provision applies to an Act passed on` |
| s20(2A)(b) | 90 | paragraph | (b) the treaty, instrument or document has effect by virtue of section 7A or 7B  | encoded |  | `section 20(2A) — how the reference is read` |
| s20(2A).closing | 91 | closing words | the reference, unless the contrary intention appears and so far as required for  | encoded |  | `section 20(2A) — how the reference is read` |
| s20(3) | 92 | subsection | (3) Subject to subsection (2A), where an Act passed on or after IP completion da | encoded |  | `section 20(3) — how the reference is read`; `section 22(1) with its carve-out — the extent to which the provision applies to an Act passed on` |
| s20(4) | 93 | subsection | (4) Subsection (3) does not determine any question as to whether the reference i | encoded |  | `section 20(4) provides that subsection (3) determines whether the reference is read as a reference to the thing as modified by domestic law`; `section 20(4) — whether the reference is read as a reference to the thing as modified by domestic law` |
| s20(5) | 94 | subsection | (5) Any expression in subsections (2A) to (4) which is defined in the European U | encoded |  | `section 20(5) — the meaning of the expression in subsections (2A) to (4)` |
| s20(6) | 95 | subsection | (6) In this section, “treaty” includes any international agreement (and any prot | encoded |  | `section 20(6) counts the thing as a treaty` |
| s20A | 96-97 | section | 20A — References to certain EU instruments Where an Act passed after the commenc | encoded |  | `section 20A — how the reference is read`; `section 22(1) with its carve-out — the extent to which the provision applies to an Act passed on` |
| xhead:Supplementary | 98 | cross-heading | Supplementary | inert | reason 1 |  |
| s21(1) | 99-100 | subsection | 21 — Interpretation etc. (1) In this Act “Act” includes a local and personal or  | encoded |  | `section 21(1) counts the instrument as an Act`; `section 21(1) counts the instrument as subordinate legislation` |
| s21(1)#subordinate legislation | 99-100 | defined term (further) | 21 — Interpretation etc. (1) In this Act “Act” includes a local and personal or  | encoded |  | `section 21(1) counts the instrument as subordinate legislation` |
| s21(2) | 101 | subsection | (2) This Act binds the Crown. | encoded |  | `section 21(2) provides that the Interpretation Act 1978 binds the Crown` |
| s22(1) | 102-103 | subsection | 22 — Application to Acts and Measures. (1) This Act applies to itself, to any Ac | fork | F9, F14, F15, F26 | `section 22(1) provides that the Interpretation Act 1978 applies to itself`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement`; `the extent to which the provision applies to an Act passed on`; `a Schedule 1 paragraph with the mark applies to the enactment`; `section 22(1) with its carve-out — the extent to which the provision applies to an Act passed on` |
| s22(2) | 104 | subsection | (2) In any of the foregoing provisions of this Act a reference to an Act is a re | encoded |  | `section 22(2) reads the reference as reaching an Act passed on` |
| s22(3) | 105 | subsection | (3) This Act applies to Measures of the General Synod of the Church of England ( | encoded |  | `section 22(3) applies the Act to the Church measure as it applies to Acts` |
| s23(1) | 106-107 | subsection | 23 — Application to other instruments. (1) The provisions of this Act, except se | fork | F19, F20 | `section 23(1) excepts the provision`; `section 23(1) — the extent to which the provision applies to subordinate legislation made after the commencement`; `the extent to which the provision applies to subordinate legislation made on`; `a Schedule 1 paragraph with the mark applies to the enactment` |
| s23(2) | 108 | subsection | (2) In the application of this Act to Acts passed or subordinate legislation mad | fork | F25 | `section 23(2) counts the thing as an enactment`; `section 23(2) names the event for an enactment comprised in subordinate legislation as` |
| s23(3) | 109 | subsection | (3) Sections 9 and 19(1) also apply to deeds and other instruments and documents | encoded |  | `section 23(3) — the extent to which the provision applies to a deed or other instrument or document made on`; `section 23(3) counts the thing as an other enactment in section 17(2)(a)` |
| s23(4) | 110 | subsection | (4) Subsections (1) and (2) of this section do not apply to Orders in Council ma | encoded |  | `the extent to which the provision applies to subordinate legislation made on`; `section 23(4) provides that subsections (1) and (2) do not apply` |
| s23ZA(1) | 111-112 | subsection | 23ZA — Assimilated direct legislation (1) The provisions of this Act (except sec | encoded |  | `section 23ZA(1) excepts the provision`; `section 23ZA(1) — the extent to which the provision applies to assimilated direct legislation` |
| s23ZA(1)(a) | 113 | paragraph | (a) is amended by an Act, subordinate legislation or devolution legislation, and | encoded |  | `section 23ZA(1) — the extent to which the provision applies to assimilated direct legislation` |
| s23ZA(1)(b) | 114 | paragraph | (b) is not subordinate legislation, | encoded |  | `section 23ZA(1) — the extent to which the provision applies to assimilated direct legislation` |
| s23ZA(1).closing | 115 | closing words | as they apply to an Act passed at the corresponding time. | encoded |  | `section 23ZA(1) — the extent to which the provision applies to assimilated direct legislation` |
| s23ZA(2) | 116 | subsection | (2) In their application by virtue of subsection (1)— | encoded |  | `section 23ZA(2)(a) — the Sovereign a reference is to be construed as`; `section 23ZA(2)(b) counts the thing as the Act in the second reference of section 11`; `section 23ZA(2)(c) provides that it may be instituted, continued, enforced or imposed as if the repeal had not been made` |
| s23ZA(2)(a) | 117 | paragraph | (a) section 10 has effect as if the reference to the passing of the Act were a r | encoded |  | `section 23ZA(2)(a) — the Sovereign a reference is to be construed as` |
| s23ZA(2)(b) | 118 | paragraph | (b) section 11 has effect as if the second reference to an Act included a refere | encoded |  | `section 23ZA(2)(b) counts the thing as the Act in the second reference of section 11` |
| s23ZA(2)(c) | 119 | paragraph | (c) section 16(1) has effect as if the reference to the repealing Act not being  | encoded |  | `section 23ZA(2)(c) provides that it may be instituted, continued, enforced or imposed as if the repeal had not been made` |
| s23ZA(3) | 120 | subsection | (3) References in this Act to the repeal of an enactment are to be read, in the  | encoded |  | `section 23ZA(3) names the repeal of the enactment as` |
| s23ZA(4) | 121 | subsection | (4) In Schedule 1— | encoded |  | `section 23ZA(4)(a) counts the assimilated direct legislation as an enactment in the definition of Commencement`; `section 23ZA(4)(b) counts the thing as an enactment in the definition of the Corporation Tax Acts or the Income Tax Acts` |
| s23ZA(4)(a) | 122 | paragraph | (a) in the definition of “Commencement”, the references to an enactment do not i | encoded |  | `section 23ZA(4)(a) counts the assimilated direct legislation as an enactment in the definition of Commencement` |
| s23ZA(4)(a)(i) | 123 | sub-paragraph | (i) any such legislation to which subsection (1) applies, ... | encoded |  | `section 23ZA(4)(a) counts the assimilated direct legislation as an enactment in the definition of Commencement` |
| s23ZA(4)(a)(i)#elision | 123 | elision mark | (i) any such legislation to which subsection (1) applies, ... | repealed or blank in this text | dots mark words repealed or left out |  |
| s23ZA(4)(a)(ia) | 124 | sub-paragraph | (ia) any instrument made on or after exit day under assimilated direct CAP legis | encoded |  | `section 23ZA(4)(a) counts the assimilated direct legislation as an enactment in the definition of Commencement` |
| s23ZA(4)(a)(ii) | 125 | sub-paragraph | (ii) any instrument , not falling within sub-paragraph (ia), made on or after IP | encoded |  | `section 23ZA(4)(a) counts the assimilated direct legislation as an enactment in the definition of Commencement` |
| s23ZA(4)(b) | 126 | paragraph | (b) in the definitions of “The Corporation Tax Acts” and “The Income Tax Acts”,  | encoded |  | `section 23ZA(4)(b) counts the thing as an enactment in the definition of the Corporation Tax Acts or the Income Tax Acts` |
| s23ZA(5) | 127 | subsection | (5) For the application of this Act to assimilated direct legislation which is s | encoded |  | `section 23ZA(5) — the extent to which the provision applies to assimilated direct legislation that is subordinate legislation made on` |
| s23ZA(6) | 128 | subsection | (6) In this section— | encoded |  | `section 23ZA(6) — the corresponding time`; `section 23ZA(6) counts the legislation as devolution legislation` |
| s23ZA(6)“corresponding time” | 129 | defined term | “corresponding time” means the time when the amending Act, subordinate legislati | encoded |  | `section 23ZA(6) — the corresponding time` |
| s23ZA(6)“devolution legislation” | 130 | defined term | “devolution legislation” means— | encoded |  | `section 23ZA(6) counts the legislation as devolution legislation` |
| s23ZA(6)(a) | 131 | paragraph | (a) an Act of the Scottish Parliament, | encoded |  | `section 23ZA(6) counts the legislation as devolution legislation` |
| s23ZA(6)(b) | 132 | paragraph | (b) a Measure or Act of the National Assembly for Wales, | encoded |  | `section 23ZA(6) counts the legislation as devolution legislation` |
| s23ZA(6)(c) | 133 | paragraph | (c) Northern Ireland legislation (for the meaning of which see section 24(5)), o | encoded |  | `section 23ZA(6) counts the legislation as devolution legislation` |
| s23ZA(6)(d) | 134 | paragraph | (d) an instrument made under anything falling within paragraph (a), (b) or (c). | encoded |  | `section 23ZA(6) counts the legislation as devolution legislation` |
| s23A(1) | 135-136 | subsection | 23A — Acts of the Scottish Parliament etc. (1) This Act applies in relation to a | encoded |  | `section 23A — the extent to which the provision applies to the Scottish legislation passed or made on` |
| s23A(2) | 137 | subsection | (2) Except as provided in subsection (3) below, sections 15 to 18 apply to— | encoded |  | `section 23A(2) names the provision among sections 15 to 18`; `section 23A — the extent to which the provision applies to the Scottish legislation passed or made on` |
| s23A(2)(a) | 138 | paragraph | (a) an Act of the Scottish Parliament as they apply to an Act, | encoded |  | `section 23A(2) names the provision among sections 15 to 18`; `section 23A — the extent to which the provision applies to the Scottish legislation passed or made on` |
| s23A(2)(b) | 139 | paragraph | (b) an instrument made under an Act of the Scottish Parliament as they apply to  | encoded |  | `section 23A(2) names the provision among sections 15 to 18`; `section 23A — the extent to which the provision applies to the Scottish legislation passed or made on` |
| s23A(3) | 140 | subsection | (3) In the application of those sections to an Act and to subordinate legislatio | encoded |  | `section 23A(3)(a) counts the thing as an enactment in sections 15 to 18`; `section 23A(3)(b) counts the instrument as subordinate legislation in section 17(2)(b)` |
| s23A(3)(a) | 141 | paragraph | (a) references to an enactment include an enactment comprised in, or in an instr | encoded |  | `section 23A(3)(a) counts the thing as an enactment in sections 15 to 18` |
| s23A(3)(b) | 142 | paragraph | (b) the reference in section 17(2)(b) to subordinate legislation includes an ins | encoded |  | `section 23A(3)(b) counts the instrument as subordinate legislation in section 17(2)(b)` |
| s23A(4) | 143 | subsection | (4) In the application of section 20 to an Act and to subordinate legislation, r | encoded |  | `section 23A(4) counts the thing as an enactment in section 20` |
| s23B(1) | 144-145 | subsection | 23B — Application of this Act to Welsh legislation (1) The provisions of this Ac | encoded |  | `section 23B(1) — the extent to which the provision applies to a Measure or Act enacted on`; `section 23B(1) excepts the provision` |
| s23B(1)(a) | 146 | paragraph | (a) a Measure of the National Assembly for Wales, and | encoded |  | `section 23B(1) — the extent to which the provision applies to a Measure or Act enacted on` |
| s23B(1)(b) | 147 | paragraph | (b) an Act of the National Assembly for Wales, other than the Legislation (Wales | encoded |  | `section 23B(1) — the extent to which the provision applies to a Measure or Act enacted on` |
| s23B(2) | 148 | subsection | (2) The provisions of this Act apply to an instrument— | encoded |  | `section 23B(2) — the extent to which the provision applies to an instrument made on` |
| s23B(2)(a) | 149 | paragraph | (a) made under a Measure or Act of the National Assembly for Wales, and | encoded |  | `section 23B(2) — the extent to which the provision applies to an instrument made on` |
| s23B(2)(b) | 150 | paragraph | (b) made before 1 January 2020, | encoded |  | `section 23B(2) — the extent to which the provision applies to an instrument made on` |
| s23B(2).closing | 151 | closing words | as they apply to other subordinate legislation. | encoded |  | `section 23B(2) — the extent to which the provision applies to an instrument made on` |
| s23B(3) | 152 | subsection | (3) The provisions of this Act apply to an instrument made under an Act of Parli | encoded |  | `section 23B(3) allows the provisions of the Act to apply to the instrument made on` |
| s23B(3)(a) | 153 | paragraph | (a) the instrument is made before 1 January 2020, | encoded |  | `section 23B(3) allows the provisions of the Act to apply to the instrument made on` |
| s23B(3)(b) | 154 | paragraph | (b) the instrument is made (at any time) with any other person who is not a devo | encoded |  | `section 23B(3) allows the provisions of the Act to apply to the instrument made on` |
| s23B(3)(c) | 155 | paragraph | (c) the instrument contains any provision that applies otherwise than in relatio | encoded |  | `section 23B(3) allows the provisions of the Act to apply to the instrument made on` |
| s23B(4) | 156 | subsection | (4) Nothing in subsection (2) or (3) limits the operation of sections 12 to 14A  | encoded |  | `section 23B(4) provides that subsections (2) and (3) do not limit the operation of the provision`; `section 23B(4) provides that section 11 does not apply in relation to the instrument` |
| s23B(5) | 157 | subsection | (5) In the application of this Act to a Measure or Act of the National Assembly  | encoded |  | `section 23B(5) names the passing of the Act or enactment as` |
| s23B(6) | 158 | subsection | (6) In this section, “devolved Welsh authority” , “Welsh zone” and (subject to s | encoded |  | `section 23B(6) — the meaning of the expression` |
| s23B(6)#Welsh zone | 158 | defined term (further) | (6) In this section, “devolved Welsh authority” , “Welsh zone” and (subject to s | encoded |  | `section 23B(6) — the meaning of the expression` |
| s23B(6)#Wales | 158 | defined term (further) | (6) In this section, “devolved Welsh authority” , “Welsh zone” and (subject to s | encoded |  | `section 23B(6) — the meaning of the expression` |
| s23B(7) | 159 | subsection | (7) In relation to a provision that— | encoded |  | `section 23B(7) includes in Wales the area of the Welsh zone beyond the seaward limit of the territorial sea` |
| s23B(7)(a) | 160 | paragraph | (a) relates to fishing, fisheries or fish health, and | encoded |  | `section 23B(7) includes in Wales the area of the Welsh zone beyond the seaward limit of the territorial sea` |
| s23B(7)(b) | 161 | paragraph | (b) is contained in an instrument made after section 45 of the Fisheries Act 202 | encoded |  | `section 23B(7) includes in Wales the area of the Welsh zone beyond the seaward limit of the territorial sea` |
| s23B(7).closing | 162 | closing words | “Wales” includes the area of the Welsh zone beyond the seaward limit of the terr | encoded |  | `section 23B(7) includes in Wales the area of the Welsh zone beyond the seaward limit of the territorial sea` |
| s23C(1) | 163-164 | subsection | 23C — Interpretation of this Act in relation to Welsh legislation (1) In this Ac | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1)(a) | 165 | paragraph | (a) a Measure of the National Assembly for Wales, | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1)(b) | 166 | paragraph | (b) an Act of the National Assembly for Wales (whenever the Act receives Royal A | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1)(c) | 167 | paragraph | (c) an instrument made under such an Act or Measure (whenever the instrument is  | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1)(d) | 168 | paragraph | (d) an instrument made under an Act of Parliament or assimilated direct legislat | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1).closing | 169 | closing words | but the reference in section 16(2) to a temporary enactment does not include an  | encoded |  | `section 23C(1) counts an enactment comprised in the legislation as an enactment` |
| s23C(1A) | 170 | subsection | (1A) In section 14(b), the reference to a statutory instrument includes a Welsh  | encoded |  | `section 23C(1A) counts the instrument as a statutory instrument in section 14(b)` |
| s23C(2) | 171 | subsection | (2) In section 17(2)(b), the reference to subordinate legislation includes an in | encoded |  | `section 23C(2) counts the instrument as subordinate legislation in section 17(2)(b)` |
| s23C(3) | 172 | subsection | (3) In section 18, the reference to an act or omission which constitutes an offe | fork | F27 | `section 23C(3) counts the act or omission as constituting an offence under two or more Acts in section 18` |
| s23C(3)(a) | 173 | paragraph | (a) any legislation to which that section applies, and | encoded |  | `section 23C(3) counts the act or omission as constituting an offence under two or more Acts in section 18` |
| s23C(3)(b) | 174 | paragraph | (b) any legislation to which Part 2 of the Legislation (Wales) Act 2019 applies, | encoded |  | `section 23C(3) counts the act or omission as constituting an offence under two or more Acts in section 18` |
| s23C(3).closing | 175 | closing words | and the reference to “those Acts” is to be read accordingly. | encoded |  | `section 23C(3) counts the act or omission as constituting an offence under two or more Acts in section 18` |
| s23C(4) | 176 | subsection | (4) In section 19(1), references to “another Act” include— | encoded |  | `section 23C(4) counts the legislation as another Act in section 19(1)` |
| s23C(4)(a) | 177 | paragraph | (a) a Measure of the National Assembly for Wales, and | encoded |  | `section 23C(4) counts the legislation as another Act in section 19(1)` |
| s23C(4)(b) | 178 | paragraph | (b) an Act of the National Assembly for Wales (whenever the Act receives Royal A | encoded |  | `section 23C(4) counts the legislation as another Act in section 19(1)` |
| s23C(4).closing | 179 | closing words | and the reference in paragraph (c) to “Acts” is to be read accordingly. | encoded |  | `section 23C(4) counts the legislation as another Act in section 19(1)` |
| s24(1) | 180-181 | subsection | 24 — Application to Northern Ireland. (1) This Act extends to Northern Ireland s | encoded |  | `section 24(1) — the extent to which the provision extends to Northern Ireland for an Act passed on` |
| s24(2) | 182 | subsection | (2) In the application of this Act to Acts passed or subordinate legislation mad | encoded |  | `section 24(2) counts the thing as an enactment`; `section 24(2) counts the name as the event for an enactment comprised in Northern Ireland legislation` |
| s24(3) | 183 | subsection | (3) In the application of section 14 to Acts passed after the commencement of th | encoded |  | `section 24(3) counts the thing as a statutory instrument in section 14` |
| s24(3A) | 184 | subsection | (3A) Section 20A applies to Northern Ireland legislation as it applies to Acts. | encoded |  | `section 24(3A) applies section 20A to the Northern Ireland legislation` |
| s24(4) | 185 | subsection | (4) The following definitions contained in Schedule 1, namely those of— | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row1 | 186 | table row | ... | repealed or blank in this text | the text shows dots where the limb stood |  |
| s24(4).row2 | 187 | table row | The Communities ...; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row2#elision | 187 | elision mark | The Communities ...; | repealed or blank in this text | dots mark words repealed or left out |  |
| s24(4).row3 | 188 | table row | The Corporation Tax Acts; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row4 | 189 | table row | E.C.S.C. Treaty; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row5 | 190 | table row | E.E.C. Treaty; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row6 | 191 | table row | EEA agreement and EEA state; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row7 | 192 | table row | Entry date; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row8 | 193 | table row | The EU or the European Union; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row9 | 194 | table row | EU institution; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row10 | 195 | table row | EU instrument; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row11 | 196 | table row | Euratom, Economic Community and Coal and Steel Community; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row12 | 197 | table row | Euratom Treaty; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row13 | 198 | table row | European Court; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row14 | 199 | table row | The Income Tax Acts; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row15 | 200 | table row | Member (in the expression “member State”); | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row16 | 201 | table row | The Tax Acts ; | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).row17 | 202 | table row | The Treaties or the EU Treaties, | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(4).closing | 203 | closing words | apply, unless the contrary intention appears, to Northern Ireland legislation as | encoded |  | `section 24(4) applies the Schedule 1 definition to Northern Ireland legislation` |
| s24(5) | 204 | subsection | (5) In this section “Northern Ireland legislation” means— | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(a) | 205 | paragraph | (a) Acts of the Parliament of Ireland; | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(b) | 206 | paragraph | (b) Acts of the Parliament of Northern Ireland; | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(c) | 207 | paragraph | (c) Orders in Council under section 1(3) of the Northern Ireland (Temporary Prov | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(d) | 208 | paragraph | (d) Measures of the Northern Ireland Assembly established under section 1 of the | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(e) | 209 | paragraph | (e) Orders in Council under Schedule 1 to the Northern Ireland Act 1974; | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(f) | 210 | paragraph | (f) Acts of the Northern Ireland Assembly; and | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s24(5)(g) | 211 | paragraph | (g) Orders in Council under section 85 of the Northern Ireland Act 1998. | encoded |  | `section 24(5) counts the legislation as Northern Ireland legislation` |
| s25(1) | 212-213 | subsection | 25 — Repeals and savings. (1) The enactments described in Schedule 3 are repeale | inert | reason 2 |  |
| s25(2) | 214 | subsection | (2) Without prejudice to section 17(2)(a), a reference to the Interpretation Act | encoded |  | `section 25(2) provides that the reference is to be construed as referring to the Interpretation Act 1978`; `section 25(2) — the extent to which the corresponding provision applies to a reference made on`; `section 25(2) — the corresponding provision of the Interpretation Act 1978` |
| s25(3) | 215 | subsection | (3) The provisions of this Act relating to Acts passed after any particular time | encoded |  | `section 25(3) — the day that decides which provisions apply to the enactment` |
| s26 | 216-217 | section | 26 — Commencement. This Act shall come into force on 1st January 1979. | fork | F9 | `the day on which the Interpretation Act 1978 comes into force` |
| s27 | 218-219 | section | 27 — Short title. This Act may be cited as the Interpretation Act 1978. | inert | reason 2 |  |
| sched:schedules | 220 | cross-heading | SCHEDULES | inert | reason 1 |  |
| sch1:heading | 221 | cross-heading | SCHEDULE 1 — Words and Expressions Defined | inert | reason 1 |  |
| sch1:reference | 222 | cross-heading | Section 5. | inert | reason 1 |  |
| sch1:note | 223 | cross-heading | Note: The years or dates which follow certain entries in this Schedule are relev | inert | reason 1 |  |
| sch1:definitions-heading | 224 | cross-heading | Definitions | inert | reason 1 |  |
| sch1:Act | 225 | defined term | “Act” means an Act of Parliament. | encoded |  | `ctor:Act`; `section 21(1) counts the instrument as an Act` |
| sch1:Associated state | 226 | defined term | “Associated state” means a territory maintaining a status of association with th | encoded |  | `ctor:Associated state` |
| sch1:Bank of England | 227 | defined term | “Bank of England” means, as the context requires, the Governor and Company of th | encoded |  | `ctor:Bank of England`; `Schedule 1 — what Bank of England and Bank of Ireland mean as the context requires` |
| sch1:Bank of Ireland | 228 | defined term | “Bank of Ireland” means, as the context requires, the Governor and Company of th | encoded |  | `ctor:Bank of Ireland`; `Schedule 1 — what Bank of England and Bank of Ireland mean as the context requires` |
| sch1:British Islands | 229 | defined term | “British Islands” means the United Kingdom, the Channel Islands and the Isle of  | encoded |  | `ctor:British Islands`; `Schedule 1 counts the place as part of the British Islands for an Act passed on` |
| sch1:British overseas territory | 230 | defined term | “British overseas territory” has the same meaning as in the British Nationality  | encoded |  | `ctor:British overseas territory` |
| sch1:British possession | 231 | defined term | “British possession” means any part of Her Majesty’s dominions outside the Unite | encoded |  | `ctor:British possession`; `Schedule 1 counts the territory as a British possession`; `Schedule 1 treats the parts under a central legislature as one British possession` |
| sch1:elision@232 | 232 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Building regulations | 233 | defined term | “Building regulations”, in relation to England and Wales, has the meaning given  | encoded |  | `ctor:Building regulations` |
| sch1:Central funds | 234 | defined term | “Central funds”, in an enactment providing in relation to England and Wales for  | encoded |  | `ctor:Central funds` |
| sch1:Charity Commission | 235 | defined term | “Charity Commission” means the Charity Commission for England and Wales (see sec | encoded |  | `ctor:Charity Commission` |
| sch1:Church Commissioners | 236 | defined term | “Church Commissioners” means the Commissioners constituted by the Church Commiss | encoded |  | `ctor:Church Commissioners` |
| sch1:Civil partnership | 237 | defined term | “Civil partnership” means a civil partnership which exists under or by virtue of | encoded |  | `ctor:Civil partnership` |
| sch1:Colonial legislature | 238 | defined term | “Colonial legislature”, and “legislature” in relation to a British possession, m | encoded |  | `ctor:Colonial legislature`; `Schedule 1 counts the authority as a colonial legislature` |
| sch1:Colonial legislature#legislature | 238 | defined term (further) | “Colonial legislature”, and “legislature” in relation to a British possession, m | encoded |  | `ctor:Colonial legislature`; `Schedule 1 counts the authority as a colonial legislature` |
| sch1:Colony | 239 | defined term | “Colony” means any part of Her Majesty’s dominions outside the British Islands e | encoded |  | `ctor:Colony`; `Schedule 1 counts the territory as a colony`; `Schedule 1 treats the parts under a central legislature as one colony` |
| sch1:Colony(a) | 240 | paragraph | (a) countries having fully responsible status within the Commonwealth; | encoded |  | `ctor:Colony`; `Schedule 1 counts the territory as a colony`; `Schedule 1 treats the parts under a central legislature as one colony` |
| sch1:Colony(b) | 241 | paragraph | (b) territories for whose external relations a country other than the United Kin | encoded |  | `ctor:Colony`; `Schedule 1 counts the territory as a colony`; `Schedule 1 treats the parts under a central legislature as one colony` |
| sch1:Colony(c) | 242 | paragraph | (c) associated states: | encoded |  | `ctor:Colony`; `Schedule 1 counts the territory as a colony`; `Schedule 1 treats the parts under a central legislature as one colony` |
| sch1:Colony.closing | 243 | closing words | and where parts of such dominions are under both a central and a local legislatu | encoded |  | `ctor:Colony`; `Schedule 1 counts the territory as a colony`; `Schedule 1 treats the parts under a central legislature as one colony` |
| sch1:Commencement | 244 | defined term | “Commencement”, in relation to an Act or enactment, means the time when the Act  | encoded |  | `ctor:Commencement`; `Schedule 1 — the commencement of the enactment` |
| sch1:Committed for trial | 245 | defined term | “Committed for trial” means— | encoded |  | `ctor:Committed for trial (b)` |
| sch1:Committed for trial(a) | 246 | paragraph | (a) ... | repealed or blank in this text | the text shows dots where the limb stood |  |
| sch1:Committed for trial(b) | 247 | paragraph | (b) in relation to Northern Ireland, committed in custody or on bail by a magist | encoded |  | `ctor:Committed for trial (b)` |
| sch1:Committed for trial(b)#elision | 247 | elision mark | (b) in relation to Northern Ireland, committed in custody or on bail by a magist | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:elision@248 | 248 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Comptroller and Auditor General | 249 | defined term | “Comptroller and Auditor General” means the Comptroller-General of the receipt a | encoded |  | `ctor:Comptroller and Auditor General` |
| sch1:Comptroller and Auditor General#elision | 249 | elision mark | “Comptroller and Auditor General” means the Comptroller-General of the receipt a | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Consular officer | 250 | defined term | “Consular officer” has the meaning assigned by Article 1 of the Vienna Conventio | encoded |  | `ctor:Consular officer` |
| sch1:The Corporation Tax Acts | 251 | defined term | “The Corporation Tax Acts” means the enactments relating to the taxation of the  | encoded |  | `ctor:The Corporation Tax Acts`; `Schedule 1 counts the enactment among the Corporation Tax Acts` |
| sch1:County court | 252 | defined term | “County court” means— | encoded |  | `ctor:County court (a)`; `ctor:County court (b)` |
| sch1:County court(a) | 253 | paragraph | (a) in relation to England and Wales, the county court established under section | encoded |  | `ctor:County court (a)` |
| sch1:County court(b) | 254 | paragraph | (b) in relation to Northern Ireland, a court held for a division under the Count | encoded |  | `ctor:County court (b)` |
| sch1:Court of Appeal | 255 | defined term | “Court of Appeal” means— | encoded |  | `ctor:Court of Appeal (a)`; `ctor:Court of Appeal (b)` |
| sch1:Court of Appeal(a) | 256 | paragraph | (a) in relation to England and Wales, Her Majesty’s Court of Appeal in England; | encoded |  | `ctor:Court of Appeal (a)` |
| sch1:Court of Appeal(b) | 257 | paragraph | (b) in relation to Northern Ireland, Her Majesty’s Court of Appeal in Northern I | encoded |  | `ctor:Court of Appeal (b)` |
| sch1:Court of Judicature | 258 | defined term | “Court of Judicature” means the Court of Judicature of Northern Ireland. | encoded |  | `ctor:Court of Judicature` |
| sch1:Court of summary jurisdiction | 259 | defined term | “Court of summary jurisdiction”, “summary conviction” and “Summary Jurisdiction  | encoded |  | `ctor:Court of summary jurisdiction` |
| sch1:Court of summary jurisdiction#summary conviction | 259 | defined term (further) | “Court of summary jurisdiction”, “summary conviction” and “Summary Jurisdiction  | encoded |  | `ctor:Court of summary jurisdiction` |
| sch1:Court of summary jurisdiction#Summary Jurisdiction Acts | 259 | defined term (further) | “Court of summary jurisdiction”, “summary conviction” and “Summary Jurisdiction  | encoded |  | `ctor:Court of summary jurisdiction` |
| sch1:Crown Court | 260 | defined term | “Crown Court” means— | encoded |  | `ctor:Crown Court (a)`; `ctor:Crown Court (b)` |
| sch1:Crown Court(a) | 261 | paragraph | (a) in relation to England and Wales, the Crown Court constituted by section 4 o | encoded |  | `ctor:Crown Court (a)` |
| sch1:Crown Court(b) | 262 | paragraph | (b) in relation to Northern Ireland, the Crown Court constituted by section 4 of | encoded |  | `ctor:Crown Court (b)` |
| sch1:Crown Estate Commissioners | 263 | defined term | “Crown Estate Commissioners” means the Commissioners referred to in section 1 of | encoded |  | `ctor:Crown Estate Commissioners` |
| sch1:elision@264 | 264 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:elision@265 | 265 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Enactment | 266 | defined term | “Enactment” includes any assimilated direct legislation but does not include an  | encoded |  | `ctor:Enactment`; `Schedule 1 counts the legislation as an enactment` |
| sch1:England | 267 | defined term | “England” means, subject to any alteration of boundaries under Part IV of the Lo | encoded |  | `ctor:England` |
| sch1:Financial year | 268 | defined term | “Financial year” means, in relation to matters relating to the Consolidated Fund | fork | F7 | `ctor:Financial year`; `Schedule 1 — the financial year` |
| sch1:Governor-General | 269 | defined term | “Governor-General” includes any person who for the time being has the powers of  | encoded |  | `ctor:Governor-General`; `Schedule 1 counts the person as a Governor-General or Governor` |
| sch1:Governor-General#Governor | 269 | defined term (further) | “Governor-General” includes any person who for the time being has the powers of  | encoded |  | `ctor:Governor-General`; `Schedule 1 counts the person as a Governor-General or Governor` |
| sch1:Her Majesty’s Revenue and Customs | 270 | defined term | “Her Majesty’s Revenue and Customs” has the meaning given by section 4 of the Co | encoded |  | `ctor:Her Majesty’s Revenue and Customs` |
| sch1:High Court | 271 | defined term | “High Court” means— | encoded |  | `ctor:High Court (a)`; `ctor:High Court (b)` |
| sch1:High Court(a) | 272 | paragraph | (a) in relation to England and Wales, Her Majesty’s High Court of Justice in Eng | encoded |  | `ctor:High Court (a)` |
| sch1:High Court(b) | 273 | paragraph | (b) in relation to Northern Ireland, Her Majesty’s High Court of Justice in Nort | encoded |  | `ctor:High Court (b)` |
| sch1:The Immigration Acts | 274 | defined term | “The Immigration Acts” has the meaning given by section 61 of the UK Borders Act | encoded |  | `ctor:The Immigration Acts` |
| sch1:The Income Tax Acts | 275 | defined term | “The Income Tax Acts” means all enactments relating to income tax, including any | encoded |  | `ctor:The Income Tax Acts`; `Schedule 1 counts the enactment among the Income Tax Acts` |
| sch1:Land | 276 | defined term | “Land” includes building and other structures, land covered with water, and any  | encoded |  | `ctor:Land`; `Schedule 1 counts the thing as land`; `Schedule 1 and Schedule 2 para 5(b) — land includes the thing in an Act passed on` |
| sch1:Lands Clauses Acts | 277 | defined term | “Lands Clauses Acts” means— | encoded |  | `ctor:Lands Clauses Acts (a)`; `ctor:Lands Clauses Acts (b)`; `ctor:Lands Clauses Acts (c)` |
| sch1:Lands Clauses Acts(a) | 278 | paragraph | (a) in relation to England and Wales, the Lands Clauses Consolidation Act 1845 a | encoded |  | `ctor:Lands Clauses Acts (a)` |
| sch1:Lands Clauses Acts(b) | 279 | paragraph | (b) in relation to Scotland, the Lands Clauses Consolidation (Scotland) Act 1845 | encoded |  | `ctor:Lands Clauses Acts (b)` |
| sch1:Lands Clauses Acts(c) | 280 | paragraph | (c) in relation to Northern Ireland, the enactments defined as such by section 4 | encoded |  | `ctor:Lands Clauses Acts (c)` |
| sch1:Local land charges register | 281 | defined term | “Local land charges register”, in relation to England and Wales, means the regis | encoded |  | `ctor:Local land charges register` |
| sch1:Local land charges register#elision | 281 | elision mark | “Local land charges register”, in relation to England and Wales, means the regis | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Local policing body | 282 | defined term | “Local policing body” has the meaning given by section 101(1) of the Police Act  | encoded |  | `ctor:Local policing body` |
| sch1:London borough | 283 | defined term | “London borough” means a borough described in Schedule 1 to the London Governmen | encoded |  | `ctor:London borough` |
| sch1:London borough#inner London borough | 283 | defined term (further) | “London borough” means a borough described in Schedule 1 to the London Governmen | encoded |  | `ctor:London borough` |
| sch1:London borough#outer London borough | 283 | defined term (further) | “London borough” means a borough described in Schedule 1 to the London Governmen | encoded |  | `ctor:London borough` |
| sch1:Lord Chancellor | 284 | defined term | “Lord Chancellor” means the Lord High Chancellor of Great Britain. | encoded |  | `ctor:Lord Chancellor` |
| sch1:Magistrates’ court | 285 | defined term | “Magistrates’ court” has the meaning assigned to it— | encoded |  | `ctor:Magistrates’ court (a)`; `ctor:Magistrates’ court (b)` |
| sch1:Magistrates’ court(a) | 286 | paragraph | (a) in relation to England and Wales, by section 148 of the Magistrates’ Courts  | encoded |  | `ctor:Magistrates’ court (a)` |
| sch1:Magistrates’ court(b) | 287 | paragraph | (b) in relation to Northern Ireland, by Article 2(2) of the Magistrates’ Courts  | encoded |  | `ctor:Magistrates’ court (b)` |
| sch1:Month | 288 | defined term | “Month” means calendar month. [1850] | fork | F3, F4 | `ctor:Month`; `Schedule 1 — the meaning of month in` |
| sch1:National Debt Commissioners | 289 | defined term | “National Debt Commissioners” means the Commissioners for the Reduction of the N | encoded |  | `ctor:National Debt Commissioners` |
| sch1:Northern Ireland legislation | 290 | defined term | “Northern Ireland legislation” has the meaning assigned by section 24(5) of this | encoded |  | `ctor:Northern Ireland legislation` |
| sch1:Oath | 291 | defined term | “Oath” and “affidavit” include affirmation and declaration, and “swear” includes | encoded |  | `ctor:Oath`; `Schedule 1 counts the word as included in oath, affidavit or swear` |
| sch1:Oath#affidavit | 291 | defined term (further) | “Oath” and “affidavit” include affirmation and declaration, and “swear” includes | encoded |  | `ctor:Oath`; `Schedule 1 counts the word as included in oath, affidavit or swear` |
| sch1:Oath#swear | 291 | defined term (further) | “Oath” and “affidavit” include affirmation and declaration, and “swear” includes | encoded |  | `ctor:Oath`; `Schedule 1 counts the word as included in oath, affidavit or swear` |
| sch1:Officer of a provider of probation services | 292 | defined term | “Officer of a provider of probation services” in relation to England and Wales,  | encoded |  | `ctor:Officer of a provider of probation services` |
| sch1:Officer of Revenue and Customs | 293 | defined term | “Officer of Revenue and Customs” has the meaning given by section 2(1) of the Co | encoded |  | `ctor:Officer of Revenue and Customs` |
| sch1:Ordnance Map | 294 | defined term | “Ordnance Map” means a map made under powers conferred by the Ordnance Survey Ac | encoded |  | `ctor:Ordnance Map` |
| sch1:Parliamentary Election | 295 | defined term | “Parliamentary Election” means the election of a Member to serve in Parliament f | encoded |  | `ctor:Parliamentary Election`; `Schedule 1 counts the election as a Parliamentary election` |
| sch1:PAYE income | 296 | defined term | “PAYE income” has the meaning given by section 683 of the Income Tax (Earnings a | encoded |  | `ctor:PAYE income` |
| sch1:PAYE regulations | 297 | defined term | “PAYE regulations” means regulations under section 684 of that Act. | encoded |  | `ctor:PAYE regulations` |
| sch1:Person | 298 | defined term | “Person” includes a body of persons corporate or unincorporate. [1889] | encoded |  | `ctor:Person`; `Schedule 1 counts the body as a person` |
| sch1:Police and crime commissioner | 299 | defined term | “Police and crime commissioner” means a police and crime commissioner establishe | encoded |  | `ctor:Police and crime commissioner` |
| sch1:Police area | 300 | defined term | “Police area” ... and other expressions relating to the police have the meaning  | encoded |  | `ctor:Police area (a)` |
| sch1:Police area#elision | 300 | elision mark | “Police area” ... and other expressions relating to the police have the meaning  | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Police area(a) | 301 | paragraph | (a) in relation to England and Wales, by section 101(1) of the Police Act 1996; | encoded |  | `ctor:Police area (a)` |
| sch1:Police area(b) | 302 | paragraph | (b) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows dots where the limb stood |  |
| sch1:elision@303 | 303 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:Police Service of Northern Ireland | 304 | defined term | “Police Service of Northern Ireland” and “Police Service of Northern Ireland Res | encoded |  | `ctor:Police Service of Northern Ireland` |
| sch1:Police Service of Northern Ireland#Police Service of Northern Ireland Reserve | 304 | defined term (further) | “Police Service of Northern Ireland” and “Police Service of Northern Ireland Res | encoded |  | `ctor:Police Service of Northern Ireland` |
| sch1:The Privy Council | 305 | defined term | “The Privy Council” means the Lords and others of Her Majesty’s Most Honourable  | encoded |  | `ctor:The Privy Council` |
| sch1:Provider of probation services | 306 | defined term | “Provider of probation services”, in relation to England and Wales, has the mean | encoded |  | `ctor:Provider of probation services` |
| sch1:Registered | 307 | defined term | “Registered” in relation to nurses, to midwives or to nursing associates, means  | encoded |  | `ctor:Registered` |
| sch1:Registered medical practitioner | 308 | defined term | “Registered medical practitioner” means a fully registered person within the mea | encoded |  | `ctor:Registered medical practitioner` |
| sch1:Registered provider of social housing | 309 | defined term | “Registered provider of social housing” and “private registered provider of soci | encoded |  | `ctor:Registered provider of social housing` |
| sch1:Registered provider of social housing#private registered provider of social housing | 309 | defined term (further) | “Registered provider of social housing” and “private registered provider of soci | encoded |  | `ctor:Registered provider of social housing` |
| sch1:Rules of Court | 310 | defined term | “Rules of Court” in relation to any court means rules made by the authority havi | encoded |  | `ctor:Rules of Court`; `Schedule 1 counts the instrument as Rules of Court`; `Schedule 1 includes in the power to make Rules of Court the power to make them for the purpose of an Act` |
| sch1:Secretary of State | 311 | defined term | “Secretary of State” means one of Her Majesty’s Principal Secretaries of State. | encoded |  | `ctor:Secretary of State` |
| sch1:Senior Courts | 312 | defined term | “Senior Courts” means the Senior Courts of England and Wales. | encoded |  | `ctor:Senior Courts` |
| sch1:Sent for trial | 313 | defined term | “Sent for trial” means, in relation to England and Wales, sent by a magistrates' | encoded |  | `ctor:Sent for trial` |
| sch1:The Sentencing Code | 314 | defined term | “The Sentencing Code” means the code contained in the Sentencing Act 2020 (see s | encoded |  | `ctor:The Sentencing Code` |
| sch1:Sewerage undertaker | 315 | defined term | “Sewerage undertaker”, in relation to England and Wales, shall be construed in a | encoded |  | `ctor:Sewerage undertaker` |
| sch1:Sheriff | 316 | defined term | “Sheriff” is to be construed in accordance with section 134(2) and (3) of the Co | encoded |  | `ctor:Sheriff` |
| sch1:The standard scale | 317 | defined term | “The standard scale”, with reference to a fine or penalty for an offence triable | encoded |  | `ctor:The standard scale (a)`; `ctor:The standard scale (b)`; `ctor:The standard scale (c)` |
| sch1:The standard scale(a) | 318 | paragraph | (a) in relation to England and Wales, has the meaning given by section 122 of th | encoded |  | `ctor:The standard scale (a)` |
| sch1:The standard scale(b) | 319 | paragraph | (b) in relation to Scotland, has the meaning given by section 225(1) of the Crim | encoded |  | `ctor:The standard scale (b)` |
| sch1:The standard scale(c) | 320 | paragraph | (c) in relation to Northern Ireland, has the meaning given by Article 5 of the F | encoded |  | `ctor:The standard scale (c)` |
| sch1:Statutory declaration | 321 | defined term | “Statutory declaration” means a declaration made by virtue of the Statutory Decl | encoded |  | `ctor:Statutory declaration` |
| sch1:Statutory maximum | 322 | defined term | “Statutory maximum”, with reference to a fine or penalty on summary conviction f | encoded |  | `ctor:Statutory maximum (a)`; `ctor:Statutory maximum (b)`; `ctor:Statutory maximum (c)` |
| sch1:Statutory maximum(a) | 323 | paragraph | (a) in relation to England and Wales, means the prescribed sum within the meanin | encoded |  | `ctor:Statutory maximum (a)` |
| sch1:Statutory maximum(b) | 324 | paragraph | (b) in relation to Scotland, means the prescribed sum within the meaning of sect | encoded |  | `ctor:Statutory maximum (b)` |
| sch1:Statutory maximum(c) | 325 | paragraph | (c) in relation to Northern Ireland, means the prescribed sum within the meaning | encoded |  | `ctor:Statutory maximum (c)` |
| sch1:Supreme Court | 326 | defined term | “Supreme Court” means the Supreme Court of the United Kingdom. | encoded |  | `ctor:Supreme Court` |
| sch1:The Tax Acts | 327 | defined term | “The Tax Acts” means the Income Tax Acts and the Corporation Tax Acts. | encoded |  | `ctor:The Tax Acts`; `Schedule 1 counts the enactment among the Tax Acts` |
| sch1:The Treasury | 328 | defined term | “The Treasury” means the Commissioners of Her Majesty’s Treasury. | encoded |  | `ctor:The Treasury` |
| sch1:Trust of land | 329 | defined term | “Trust of land” and “trustees of land”, in relation to England and Wales, have t | encoded |  | `ctor:Trust of land` |
| sch1:Trust of land#trustees of land | 329 | defined term (further) | “Trust of land” and “trustees of land”, in relation to England and Wales, have t | encoded |  | `ctor:Trust of land` |
| sch1:United Kingdom | 330 | defined term | “United Kingdom” means Great Britain and Northern Ireland. [12th April 1927] | encoded |  | `ctor:United Kingdom` |
| sch1:Wales | 331 | defined term | “Wales” means the combined area of the counties which were created by section 20 | encoded |  | `ctor:Wales` |
| sch1:Water undertaker | 332 | defined term | “Water undertaker”, in relation to England and Wales, shall be construed in acco | encoded |  | `ctor:Water undertaker` |
| sch1:Writing | 333 | defined term | “Writing” includes typing, printing, lithography, photography and other modes of | encoded |  | `ctor:Writing`; `Schedule 1 counts the mode of representing words as writing`; `Schedule 1 construes the expression referring to writing accordingly` |
| sch1:elision@334 | 334 | elision | ... | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:elision@335 | 335 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:group:offences | 336 | cross-heading | Construction of certain expressions relating to offences | inert | reason 1 |  |
| sch1:group:offences:p1 | 337 | Schedule paragraph | In relation to England and Wales— | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p1(a) | 338 | paragraph | (a) “indictable offence” means an offence which, if committed by an adult, is tr | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p1(b) | 339 | paragraph | (b) “summary offence” means an offence which, if committed by an adult, is triab | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p1(c) | 340 | paragraph | (c) “offence triable either way” means an offence , other than an offence triabl | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p1.closing | 341 | closing words | and the terms “indictable”, “summary” and “triable either way”, in their applica | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p2 | 342 | Schedule paragraph | In the above definitions references to the way or ways in which an offence is tr | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:offences:p3 | 343 | Schedule paragraph | In relation to a term of imprisonment in respect of an offence triable either wa | encoded |  | `ctor:Offences (England and Wales)`; `Schedule 1 counts the offence as an indictable offence`; `Schedule 1 counts the offence as a summary offence`; `Schedule 1 counts the offence as an offence triable either way`; `Schedule 1 construes the term as applied to an offence triable in England and Wales`; `Schedule 1 reads the way an offence is triable without regard to section 22 of the Magistrates' Courts Act 1980`; `Schedule 1 — the general limit in a magistrates' court` |
| sch1:group:relationships | 344 | cross-heading | Construction of certain references to relationships | inert | reason 1 |  |
| sch1:group:relationships:p1 | 345 | Schedule paragraph | In relation to England and Wales— | encoded |  | `ctor:Relationships (England and Wales)`; `Schedule 1 construes the reference to a relationship in accordance with the Family Law Reform Act 1987` |
| sch1:group:relationships:p1(a) | 346 | paragraph | (a) references (however expressed) to any relationship between two persons; | encoded |  | `ctor:Relationships (England and Wales)`; `Schedule 1 construes the reference to a relationship in accordance with the Family Law Reform Act 1987` |
| sch1:group:relationships:p1(b) | 347 | paragraph | (b) references to a person whose father and mother were or were not married to , | encoded |  | `ctor:Relationships (England and Wales)`; `Schedule 1 construes the reference to a relationship in accordance with the Family Law Reform Act 1987` |
| sch1:group:relationships:p1(c) | 348 | paragraph | (c) references cognate with references falling within paragraph (b) above, | encoded |  | `ctor:Relationships (England and Wales)`; `Schedule 1 construes the reference to a relationship in accordance with the Family Law Reform Act 1987` |
| sch1:group:relationships:p1.closing | 349 | closing words | shall be construed in accordance with section 1 of the Family Law Reform Act 198 | encoded |  | `ctor:Relationships (England and Wales)`; `Schedule 1 construes the reference to a relationship in accordance with the Family Law Reform Act 1987` |
| sch1:group:police-scotland | 350 | cross-heading | Construction of certain expressions relating to the police: Scotland | inert | reason 1 |  |
| sch1:group:police-scotland:p1 | 351 | Schedule paragraph | In relation to Scotland— | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:group:police-scotland:p1(a) | 352 | paragraph | (a) references to a police force include references to the Police Service of Sco | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:group:police-scotland:p1(b) | 353 | paragraph | (b) references to a chief officer of police include references to the chief cons | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:group:police-scotland:p1(c) | 354 | paragraph | (c) “police authority” means the Scottish Police Authority; | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:group:police-scotland:p1(d) | 355 | paragraph | (d) the “police area” of the Police Service of Scotland is Scotland and referenc | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:group:police-scotland:p1(e) | 356 | paragraph | (e) references to a constable or chief constable of, or appointed for, any area  | encoded |  | `ctor:Police: Scotland`; `Schedule 1 reads the police reference for Scotland` |
| sch1:eu-heading | 357 | cross-heading | Definitions relating to the EU and the United Kingdom's withdrawal | inert | reason 1 |  |
| sch1:Assimilated law | 358 | defined term | “Assimilated law”, “assimilated direct legislation”, “assimilated direct minor l | encoded |  | `ctor:Assimilated law` |
| sch1:Assimilated law#assimilated direct legislation | 358 | defined term (further) | “Assimilated law”, “assimilated direct legislation”, “assimilated direct minor l | encoded |  | `ctor:Assimilated law` |
| sch1:Assimilated law#assimilated direct minor legislation | 358 | defined term (further) | “Assimilated law”, “assimilated direct legislation”, “assimilated direct minor l | encoded |  | `ctor:Assimilated law` |
| sch1:Assimilated law#assimilated direct principal legislation | 358 | defined term (further) | “Assimilated law”, “assimilated direct legislation”, “assimilated direct minor l | encoded |  | `ctor:Assimilated law` |
| sch1:Assimilated obligation | 359 | defined term | “Assimilated obligation” means an obligation that— | encoded |  | `ctor:Assimilated obligation`; `Schedule 1 counts the obligation as an assimilated obligation` |
| sch1:Assimilated obligation(a) | 360 | paragraph | (a) was created or arose by or under the EU Treaties before IP completion day, a | encoded |  | `ctor:Assimilated obligation`; `Schedule 1 counts the obligation as an assimilated obligation` |
| sch1:Assimilated obligation(b) | 361 | paragraph | (b) forms part of assimilated law, | encoded |  | `ctor:Assimilated obligation`; `Schedule 1 counts the obligation as an assimilated obligation` |
| sch1:Assimilated obligation.closing | 362 | closing words | as modified from time to time. | encoded |  | `ctor:Assimilated obligation`; `Schedule 1 counts the obligation as an assimilated obligation` |
| sch1:The Communities | 363 | defined term | “The Communities” means Euratom, the Economic Community and the Coal and Steel C | encoded |  | `ctor:The Communities`; `Schedule 1 treats a reference to a Community as including the EU` |
| sch1:E.C.S.C. Treaty | 364 | defined term | “E.C.S.C. Treaty” means the Treaty establishing the European Coal and Steel Comm | encoded |  | `ctor:E.C.S.C. Treaty` |
| sch1:EEA agreement | 365 | defined term | “EEA agreement” means the agreement on the European Economic Area signed at Opor | encoded |  | `ctor:EEA agreement`; `Schedule 1 includes the thing in the EEA agreement` |
| sch1:EEA state | 366 | defined term | “EEA state”, in relation to a time, means— | encoded |  | `ctor:EEA state`; `Schedule 1 counts the state as an EEA state at the time` |
| sch1:EEA state(a) | 367 | paragraph | (a) a state which at that time is a member State, or | encoded |  | `ctor:EEA state`; `Schedule 1 counts the state as an EEA state at the time` |
| sch1:EEA state(b) | 368 | paragraph | (b) any other state which at that time is a party to the EEA agreement. [8 Janua | encoded |  | `ctor:EEA state`; `Schedule 1 counts the state as an EEA state at the time` |
| sch1:E.E.C. Treaty | 369 | defined term | “E.E.C. Treaty” means the Treaty establishing the European Economic Community, s | encoded |  | `ctor:E.E.C. Treaty` |
| sch1:Entry date | 370 | defined term | “Entry date” means the date on which the United Kingdom became a member of the C | encoded |  | `ctor:Entry date` |
| sch1:The EU | 371 | defined term | “The EU” or “the European Union” means the European Union, being the Union estab | encoded |  | `ctor:The EU`; `Schedule 1 includes Euratom in the EU where the context permits or requires` |
| sch1:The EU#the European Union | 371 | defined term (further) | “The EU” or “the European Union” means the European Union, being the Union estab | encoded |  | `ctor:The EU`; `Schedule 1 includes Euratom in the EU where the context permits or requires` |
| sch1:EU institution | 372 | defined term | “EU institution” means any institution of the EU. | encoded |  | `ctor:EU institution` |
| sch1:EU instrument | 373 | defined term | “EU instrument” means any instrument issued by an EU institution other than any  | encoded |  | `ctor:EU instrument`; `Schedule 1 counts the instrument as an EU instrument` |
| sch1:Euratom | 374 | defined term | “Euratom”, “Economic Community” and “Coal and Steel Community” mean respectively | encoded |  | `ctor:Euratom` |
| sch1:Euratom#Economic Community | 374 | defined term (further) | “Euratom”, “Economic Community” and “Coal and Steel Community” mean respectively | encoded |  | `ctor:Euratom` |
| sch1:Euratom#Coal and Steel Community | 374 | defined term (further) | “Euratom”, “Economic Community” and “Coal and Steel Community” mean respectively | encoded |  | `ctor:Euratom` |
| sch1:Euratom Treaty | 375 | defined term | “Euratom Treaty” means the Treaty establishing the European Atomic Energy Commun | encoded |  | `ctor:Euratom Treaty` |
| sch1:European Court | 376 | defined term | “European Court” means the Court of Justice of the European Union. | encoded |  | `ctor:European Court` |
| sch1:EU withdrawal agreement | 377 | defined term | “EU withdrawal agreement” means the withdrawal agreement within the meaning of t | encoded |  | `ctor:EU withdrawal agreement` |
| sch1:Exit day | 378 | defined term | “Exit day” (and related expressions) have the same meaning as in the European Un | encoded |  | `ctor:Exit day` |
| sch1:IP completion day | 379 | defined term | “IP completion day” (and related expressions) have the same meaning as in the Eu | encoded |  | `ctor:IP completion day` |
| sch1:Member | 380 | defined term | “Member”, in the expression “member State”, refers to membership of the EU. | encoded |  | `ctor:Member` |
| sch1:elision@381 | 381 | elision | ... | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:elision@382 | 382 | elision | ... | repealed or blank in this text | dots mark words repealed or left out |  |
| sch1:The Treaties | 383 | defined term | “The Treaties” or “the EU Treaties” means the Treaties or EU Treaties as at imme | encoded |  | `ctor:The Treaties` |
| sch1:The Treaties#the EU Treaties | 383 | defined term (further) | “The Treaties” or “the EU Treaties” means the Treaties or EU Treaties as at imme | encoded |  | `ctor:The Treaties` |
| sch2:heading | 384 | cross-heading | SCHEDULE 2 — Application of Act to Existing Enactments | inert | reason 1 |  |
| sch2:reference | 385 | cross-heading | Sections 22, 23. | inert | reason 1 |  |
| sch2:PartI | 386 | cross-heading | Part I — Acts | inert | reason 1 |  |
| sch2.p1 | 387 | Schedule paragraph | 1 — The following provisions of this Act apply to Acts whenever passed:— | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row1 | 388 | table row | Section 6(a) and (c) so far as applicable to enactments relating to offences pun | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row2 | 389 | table row | Section 9 | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row3 | 390 | table row | Section 10 | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row4 | 391 | table row | Section 11 so far as it relates to subordinate legislation made after the year 1 | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row5 | 392 | table row | Section 14A | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row6 | 393 | table row | Section 18 | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p1.row7 | 394 | table row | Section 19(2). | encoded |  | `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2 | 395 | Schedule paragraph | 2 — The following apply to Acts passed after the year 1850:— | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2.row1 | 396 | table row | Section 1 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement`; `section 1 provides that a section of an Act takes effect as a substantive enactment, for an Act passed on` |
| sch2.p2.row2 | 397 | table row | Section 2 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2.row3 | 398 | table row | Section 3 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2.row4 | 399 | table row | Section 6(a) and (c) so far as not applicable to such Acts by virtue of paragrap | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2.row5 | 400 | table row | Section 15 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p2.row6 | 401 | table row | Section 17(1). | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3 | 402 | Schedule paragraph | 3 — The following apply to Acts passed after the year 1889:— | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row1 | 403 | table row | Section 4 | fork | F21 | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row2 | 404 | table row | Section 7 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row3 | 405 | table row | Section 8 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row4 | 406 | table row | Section 12 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row5 | 407 | table row | Section 13 | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row6 | 408 | table row | Section 14 so far as it relates to rules, regulations or byelaws | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row7 | 409 | table row | Section 16(1) | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row8 | 410 | table row | Section 17(2)(a) | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row9 | 411 | table row | Section 19(1) | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p3.row10 | 412 | table row | Section 20(1). | encoded |  | `the whole of the provision applies to an Act passed after the year`; `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` |
| sch2.p4(1) | 413 | Schedule paragraph | 4 — (1) Subject to the following provisions of this paragraph— | encoded |  | `Schedule 2 para 4(1) — a Schedule 1 paragraph with the mark applies to an Act passed before the commencement, on`; `a Schedule 1 paragraph with the mark applies to the enactment` |
| sch2.p4(1)(a) | 414 | paragraph | (a) paragraphs of Schedule 1 at the end of which a year or date . . . is specifi | fork | F14 | `Schedule 2 para 4(1) — a Schedule 1 paragraph with the mark applies to an Act passed before the commencement, on`; `a Schedule 1 paragraph with the mark applies to the enactment` |
| sch2.p4(1)(a)#elision | 414 | elision mark | (a) paragraphs of Schedule 1 at the end of which a year or date . . . is specifi | repealed or blank in this text | dots mark words repealed or left out |  |
| sch2.p4(1)(b) | 415 | paragraph | (b) paragraphs of that Schedule at the end of which no year or date is specified | encoded |  | `Schedule 2 para 4(1) — a Schedule 1 paragraph with the mark applies to an Act passed before the commencement, on`; `a Schedule 1 paragraph with the mark applies to the enactment` |
| sch2.p4(2) | 416 | Schedule paragraph | (2) The definition of “British Islands”, in its application to Acts passed after | fork | F22 | `Schedule 1 counts the place as part of the British Islands for an Act passed on` |
| sch2.p4(3) | 417 | Schedule paragraph | (3) The definition of “colony”, in its application to an Act passed at any time  | encoded |  | `Schedule 2 para 4(3)(a) provides that the Act was passed before the exclusion took effect`; `Schedule 2 para 4(3)(b) provides that the territory ceased after the Act was passed to be part of Her Majesty's dominions`; `Schedule 2 para 4(3) counts the territory as a colony for an Act passed on` |
| sch2.p4(3)(a) | 418 | paragraph | (a) any colony within the meaning of section 18(3) of the Interpretation Act 188 | fork | F23 | `Schedule 2 para 4(3)(a) provides that the Act was passed before the exclusion took effect`; `Schedule 2 para 4(3) counts the territory as a colony for an Act passed on` |
| sch2.p4(3)(b) | 419 | paragraph | (b) any country or territory which ceased after that time to be part of Her Maje | fork | F22 | `Schedule 2 para 4(3)(b) provides that the territory ceased after the Act was passed to be part of Her Majesty's dominions`; `Schedule 2 para 4(3) counts the territory as a colony for an Act passed on` |
| sch2.p4.closing | 420 | closing words | and paragraph (b) of the definition does not apply. | encoded |  | `Schedule 2 para 4(3) counts the territory as a colony for an Act passed on` |
| sch2.p4(4) | 421 | Schedule paragraph | (4) The definition of “Lord Chancellor” does not apply to Acts passed before 1st | encoded |  | `Schedule 2 para 4(4) provides that the definition of Lord Chancellor does not apply to the Act` |
| sch2.p4(5) | 422 | Schedule paragraph | (5) The definition of “person”, so far as it includes bodies corporate, applies  | encoded |  | `Schedule 2 para 4(5) applies the inclusion of bodies corporate in person to a provision of an Act passed on` |
| sch2.p4(6) | 423 | Schedule paragraph | (6) This paragraph applies to . . . the Water Act 1973 as if they were passed af | fork | F24 | `Schedule 2 para 4(6) treats the Act as passed after 1st April 1974`; `Schedule 2 para 4(6) — a Schedule 1 paragraph with the mark applies to an Act treated as passed after 1st April 1974` |
| sch2.p4(6)#elision | 423 | elision mark | (6) This paragraph applies to . . . the Water Act 1973 as if they were passed af | repealed or blank in this text | dots mark words repealed or left out |  |
| sch2.p5 | 424 | Schedule paragraph | 5 — The following definitions shall be treated as included in Schedule 1 for the | encoded |  | `Schedule 2 para 5(a) provides that a reference to England includes the place in an Act passed on`; `Schedule 2 para 5(b) provides that land includes the thing in an Act passed on`; `Schedule 2 para 5(c) gives the meaning of the Summary Jurisdiction (Scotland) Acts in an Act passed on` |
| sch2.p5(a) | 425 | paragraph | (a) in any Act passed before 1st April 1974, a reference to England includes Ber | fork | F22 | `Schedule 2 para 5(a) provides that a reference to England includes the place in an Act passed on` |
| sch2.p5(b) | 426 | paragraph | (b) in any Act passed before the commencement of this Act and after the year 185 | encoded |  | `Schedule 2 para 5(b) provides that land includes the thing in an Act passed on`; `Schedule 1 and Schedule 2 para 5(b) — land includes the thing in an Act passed on` |
| sch2.p5(c) | 427 | paragraph | (c) in any Act passed before the commencement of the Criminal Procedure (Scotlan | encoded |  | `Schedule 2 para 5(c) gives the meaning of the Summary Jurisdiction (Scotland) Acts in an Act passed on` |
| sch2:PartII | 428 | cross-heading | Part II — Subordinate Legislation | inert | reason 1 |  |
| sch2.p6 | 429 | Schedule paragraph | 6 — Sections 4(a), 9 and 19(1), and so much of Schedule 1 as defines the followi | encoded |  | `Part II of Schedule 2 — the extent to which the provision applies to subordinate legislation made before the commencement`; `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.elision@430 | 430 | elision | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | dots mark words repealed or left out |  |
| sch2.p6.row1 | 431 | table row | England; | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.row2 | 432 | table row | Local land charges register and appropriate local land charges register; | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.row3 | 433 | table row | in relation to Scotland, expressions relating to the police; | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.row4 | 434 | table row | United Kingdom; | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.row5 | 435 | table row | Wales, | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p6.closing | 436 | closing words | apply to subordinate legislation made at any time before the commencement of thi | encoded |  | `Part II of Schedule 2 — the extent to which the provision applies to subordinate legislation made before the commencement`; `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p7 | 437 | Schedule paragraph | 7 — The definition in Schedule 1 of “county court”, in relation to England and W | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch2.p8 | 438 | Schedule paragraph | 8 — The definition in Schedule 1 of “enactment”, in so far as it relates to assi | encoded |  | `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on` |
| sch3:heading | 439 | cross-heading | SCHEDULE 3 — ENACTMENTS REPEALED | repealed or blank in this text | the text shows the heading and "Section 25." and no row |  |
| sch3:reference | 440 | cross-heading | Section 25. | inert | reason 1 |  |

Counts: 436 rows: 367 encoded, 21 fork, 26 inert, 22 repealed or blank in this text.
<!-- END:coverage-table -->

## Numbered findings

Each finding says where the evidence is.

1. **Pass 1 counted the Act at the grain of a section, and so did not see most of it.** `tools/units.py` counts 436 units in the text (every non-blank line belongs to exactly one); pass 1 had 161 rows, and 302 of the 436 units had no row of their own. 107 of the 121 pass-1 rows that were not `encoded` moved out of `inert` or `repealed or blank` (the audit tables above).
2. **Pass 1's `encoded` rows left out seven parts of the text.** s 14A(6), s 20(2A) to (6), the carve-out in s 22(1), s 22(2), s 23(2), the second limb of s 23(3), and the "corresponding provision" half of s 25(2). Each now has a function (`uk-interpretation-general.l4`, `-eu.l4`) and the audit names them. None of the pass-1 files was edited to add them.
3. **Schedule 1's years and dates decide nothing for an Act passed on or after 1 January 1979 (F14), and for an earlier Act they cut two ways.** A year mark means "after the year" (an Act passed on 31 December 1889 is not after 1889) and a date mark means "on or after the date" (Sch 2 para 4(1)(a), src:414). 15 entries carry a year, 8 a date, 1 a described date. `tests-schedule1.l4` puts an assertion on each side of every one of them, generated from the brackets in the text.
4. **Schedule 1 "Land" carries the mark [1st January 1979]**, so its list (buildings and other structures, land covered with water, any estate, interest, easement, servitude or right) reaches only an Act passed on or after that day; for an Act passed before it and after 1850, para 5(b) gives another list (messuages, tenements and hereditaments, houses and buildings of any tenure); for an Act passed in or before 1850 neither list applies. The two lists are never both in play for one Act. `Schedule 1 and Schedule 2 para 5(b) — land includes the thing in an Act passed on`, `tests-definitions.l4`.
5. **Sch 2 para 4(6) can leave a Schedule 1 mark undecidable (F24).** An Act "treated as passed after 1st April 1974" is passed on no particular day, so a mark of [1974] or of a later year, or of a date after 2 April 1974, does not say whether the paragraph applies. The function refuses there and answers where every possible day agrees.
6. **The Act orders two events on one day nowhere (F22, F8).** Sch 2 paras 4(2), 4(3)(b) and 5(a), and s 13, compare the day an Act or instrument is passed with the day of another event. A day alone does not order two events on it, so each refuses by name on the very day. The commencement is different: it is the beginning of its day (s 4), so an Act passed on 1 January 1979 is passed after the commencement (F9).
7. **s 20(4) is an exclusion, not a rule.** It says what s 20(3) does not decide (whether the reference is to the EU instrument "as modified by domestic law") and that s 20(2) is untouched. It is encoded as a constant FALSE (`section 20(4) provides that subsection (3) determines ...`) and a named refusal for the question it leaves to s 20(2).
8. **The Act borrows eight facts that it does not give**, and each is an input in the function that needs it, never a built-in: the day the Irish Free State was established (Sch 2 para 4(2)); the day the Welsh Language Act 1967 was passed (para 5(a)); the day the Criminal Procedure (Scotland) Act 1975 came into force (para 5(c)); "IP completion day" and "exit day" (ss 20(2A), 20(3), 21(1), 23ZA(4)); the day s 20A came into force; the day s 45 of the Fisheries Act 2020 came into force (s 23B(7)); the limit s 224(1) of the Sentencing Code lays down (Sch 1 offences); and the meanings that the Government of Wales Act 2006 and the European Union (Withdrawal) Act 2018 give (ss 23B(6), 20(5)). F13 states the rule.
9. **Every definition named in s 24(4) is an entry of Schedule 1.** The 16 names (The Communities, The Corporation Tax Acts, E.C.S.C. Treaty, E.E.C. Treaty, EEA agreement and EEA state, Entry date, The EU or the European Union, EU institution, EU instrument, Euratom, Economic Community and Coal and Steel Community, Euratom Treaty, European Court, The Income Tax Acts, Member, The Tax Acts, The Treaties or the EU Treaties) were each found among the terms of `tools/schedule1.tsv`, so the cross-reference does not dangle. Checked by a script run during pass 2; the script is not shipped.
10. **25 of the 110 Schedule 1 entries only point at another Act or instrument** (`how` = `pointer` in `tools/schedule1.tsv`); 75 say what the word means, 6 what it includes, 2 are "as the context requires", 1 refers, 1 construes. For a pointer the table returns what the entry points at and nothing more, because the pointed-at text is not among the sources (F13 applies).
11. **Schedule 3 has no table in this text, so s 25 cannot say what the Act repealed.** s 25(2)'s "corresponding provision" is therefore a named refusal (`section 25(2) does not say which provision of the Interpretation Act 1978 corresponds to ...`); the half of s 25(2) that is answerable (the corresponding provision "as it applies to Acts passed at the time of the reference") is a function over the provision the caller names.
12. **"And" in s 23C(3) is read as both (F27), and "construed accordingly" in s 23(2) as making and revocation (F25).** Each is a reading of two the text allows; the tests assert the chosen one.

## Fork register

Every ambiguity, the readings seen, the one taken, and the text that licenses it.
"Refuse" means the module returns a named `REFUSE` and the tests assert it with `#ASSERT REFUSED ... BECAUSE`.
`F1` to `F4` are the forks the brief names; the rest are what I found.

| id | question | readings seen | reading taken | text that licenses it |
| --- | --- | --- | --- | --- |
| F1 | Does a period "from" a day count that day; does a period "after" an event; is the last day inside the period? | Exclude the start day (the period begins the day after); include it; last day inside; last day outside. | **None. Refuse** (`the Interpretation Act 1978 has no rule for counting a period of days from a day` and its sisters). | No section counts a period (searched: "beginning with", "clear", "exclusive", "inclusive", "from", "after", "within", "period"; see "Where I looked"). s 20(1) (src:86) closes a range of "words, sections or other parts" and no day is one; it is not read as a rule for periods of time. The helper `the day falls inside the period` takes a first and a last day from the caller and treats both as inside; it is labelled in the module as not a rule of the Act. |
| F2 | Does a rule move a last day off a day of rest, recess or holiday; if so does it reach months and years or only days; what of several in a row? | A rule for days only; for all periods; none. | **None. Refuse** (`the Interpretation Act 1978 has no rule on a period whose last day is a day of rest, recess or holiday`). The tests supply a rest-day function and call it with the last day on a weekday, a Saturday, a Sunday, a Monday holiday (so Saturday, Sunday and Monday are three in a row), with no rest day at all, and with a later Saturday standing for a month- or year-based last day; every call refuses alike. | No such word or rule in the text (0 hits for sunday, holiday, recess, rest day, saturday, weekend, working day, business day, closed, clear day). |
| F3 | What does the text mean by "month" and "year": calendar or fixed length; what follows for a start on the 31st? | A month is a calendar month; a month is 30 days; a year is a calendar year; a year is 365 days. | **"Month" is a calendar month** (Sch 1, src:288), and the module returns that as a value (`a calendar month`). **"Year" has no definition: refuse.** What follows for a start on the 31st is not stated: refuse. `daydate`'s `add months` clamps 31 January to 28 February; it is not imported or used, because the statute does not say that and the statute governs. | Sch 1 "Month" means calendar month [1850] (src:288); "Financial year" is defined for stated matters only (src:268); no definition of "year", "day" or "week". |
| F4 | What of a start on 29 February (one year from 2024-02-29) or on a day the end month lacks (one month from 2025-01-31)? | Roll to 28 February; roll to 1 March; roll to the last day of the month; the day before the anniversary. | **None. Refuse.** The tests run: one month from 2025-01-31, 2024-01-31, 2024-02-29 and 2025-02-28; twelve months from 2024-02-29; six months from 2025-08-31; one year and four years from 2024-02-29; two years from 2024-02-28. | As F3. |
| F5 | An Act says its day is "to be fixed later", and the day is fixed (2026-06-01): which limb of s 4? | Limb (a), a particular day; limb (b), the Royal Assent day, because the Act itself named none; neither. | **Limb (a), once the day is fixed**: day 2026-06-01, at the beginning of that day. **Before it is fixed: refuse.** | s 4(a) (src:14), "where provision is made for it to come into force on a particular day". Provision for a day to be fixed is provision made, and once fixed the day is a particular day. s 4(b) (src:15) needs that "no provision is made", which is not the case. |
| F6 | Does "at the beginning of that day" (s 4) fall within s 9's "whenever an expression of time occurs in an Act, the time referred to shall ... be held to be Greenwich mean time"? | A (the beginning of a day is a point of time on a clock, so GMT governs it); B (it is the boundary between days, not an expression of a clock time, so s 9 does not reach it). | **The commencement function answers in the text's own words** (`the beginning of the day`) and takes neither reading. A separate function (`section 4 read with section 9 — the clock reading of the moment`) gives 00:00:00 Greenwich mean time on reading A, and refuses where summer time is in question. | s 4(a),(b) (src:14-15) and s 9 (src:29). Whether "an expression of time" includes "the beginning of that day" is not stated. |
| F7 | What days does the "financial year" cover? | 1 April to 31 March; or some other twelve months. | **The twelve calendar months ending with 31 March: 1 April of the earlier year to 31 March of the year it ends** (so the year ending 2024 includes 29 February 2024). | Sch 1 "Financial year" (src:268), "the twelve months ending with 31st March", read with "Month" means calendar month (src:288). Limited to the stated matters; the [1889] mark is applied. |
| F8 | s 13 allows an instrument to come into force "at any time after the passing of the Act". Can it come into force at the beginning of the day of Royal Assent? | Yes (the Act is deemed in force from the beginning of that day, so the day is the passing day); no (the beginning of the day is before the passing). | **No**: an instrument that comes into force at the beginning of a day is after the passing only if that day is later than the day of passing. A power exercised on the same day as the passing: **refuse** (a day alone does not say whether a moment on it is after the passing). | s 13 (src:39) "at any time after the passing of the Act", read with s 4 (src:14-15) "at the beginning of that day". |
| F9 | What is "after the commencement of this Act"? | After 1 January 1979 (the day), or on or after it. | **On or after 1 January 1979**, since the Act comes into force at the beginning of that day (s 4(a)) and so an Act passed during that day is after it. Tests sit on 1978-12-31 and 1979-01-01. | s 26 (src:217), s 4(a) (src:14), s 22(1) (src:103), s 23(1) (src:107). |
| F10 | An Act is "passed or published" on 2026-03-10: which is the trigger? | The day of publication; the day of Royal Assent. | **The day of Royal Assent** (called "the day it was passed or made" in the input record). The text has no rule on publication. If only a publication day is known, the text does not say how it relates to the Royal Assent, and the encoding takes no input for it. | s 4(b) (src:15), "the day on which the Act receives the Royal Assent". No other trigger in the text. |
| F11 | s 7: once "the contrary is proved", what time governs? | The proved delivery time; the time the letter was posted; neither. | **Refuse**: the section says the deemed time yields, and not what time then governs. | s 7 (src:25), "unless the contrary is proved, to have been effected at the time at which the letter would be delivered in the ordinary course of post". |
| F12 | s 17(1): is the repealed enactment in force on the day the substituted provisions commence? | Through that day; until its beginning. | **Until its beginning**: in force on each earlier day; on the commencement day the substituted provisions are in force from the first moment. | s 17(1) (src:72) "remains in force until the substituted provisions come into force", with s 4 "at the beginning of that day". |
| F13 | s 21(1) makes some instruments subordinate legislation by dates ("IP completion day", "exit day") that other Acts give. | Build in dates from outside; take the dates as a fact the caller states. | **The caller states whether the instrument is made on or after those days.** | s 21(1) (src:100); the Acts that define the days are not among the sources. |
| F14 | Do the years and dates after Schedule 1 entries bar a definition from Acts passed after the commencement? | Yes, by the date; no, they only matter for earlier Acts. | **No: they matter only for Acts passed before the commencement.** Acts and subordinate legislation passed or made on or after 1 January 1979 take the whole of Schedule 1. | s 22(1) (src:103) "applies ... to any Act passed after the commencement"; Sch 2 para 4 (src:413-415) is headed "Application of Act to Existing Enactments"; Schedule 1's own note (src:223): the years and dates "are relevant for the purposes of paragraph 4 of Schedule 2 (application to existing enactments)". |
| F15 | A provision that Sch 2 Part I does not list (for example s 6(b), s 16(2), s 17(2)(b), s 20(2), s 21): does it reach an Act passed before the commencement? | Yes, by implication; no. | **No: `does not apply`.** | s 22(1) (src:103), "to the extent specified in Part I of Schedule 2". The list is read as the extent. |
| F16 | Which language version of the text has authority? | English only; English and Welsh. | **The text does not say.** Nothing is encoded. | The only mention of a language is the "Welsh Language Act 1967" (Sch 2 para 5(a), src:425). |
| F17 | s 21(2) "This Act binds the Crown": is that "from what moment an enactment binds"? | The brief's "binds" is the commencement of the enactment being interpreted; s 21(2) says whether this Act binds the Crown. | **Different senses.** "Binds" in the brief is treated as coming into force (s 4). s 21(2) is encoded as its own constant. | s 21(2) (src:101); s 4 (src:12-15). |
| F18 | s 4 speaks of "An Act or provision of an Act". Which does the function take? | One function for the Act, one for each provision. | **One record, `An enactment`, that stands for whichever the caller means:** an Act, or a provision of one with its own provision about coming into force. For a provision that names no day of its own while the Act does, the caller says so in the record. | s 4 (src:13). |
| F19 | s 23(1) applies provisions "so far as applicable". Can a function decide that? | Yes, by encoding applicability; no. | **No.** `applies without limit` means only that the Act does not itself cut the provision down; whether the provision is "applicable" to a given instrument is a question about that instrument. The same is done for the "unless the contrary intention appears" of s 23(1): the extent functions for subordinate legislation take no contrary-intention input (the functions of the construction module do, because each of their sections carries its own), because here the contrary intention is a fact about the instrument that the caller weighs after reading the extent. | s 23(1) (src:107). |
| F20 | Subordinate legislation made before the commencement that says nothing about its coming into force. | s 4(b) by analogy with Acts; none. | **Refuse (no rule).** | Sch 2 para 6 (src:429) lists s 4(a) and not 4(b); s 23(1) excepts 4(b). |
| F21 | Sch 2 para 3 applies s 4 to Acts "passed after the year 1889": how are Acts passed in 1889 treated, and what does s 4 give them? | After the year 1889 means the year is greater than 1889. | **An Act passed on or before 31 December 1889 is not reached by s 4: refuse** (`section 4 does not apply to an enactment passed or made in or before 1889, and the Interpretation Act 1978 has no other rule on its coming into force`). | Sch 2 para 3 (src:402-403). |
| F22 | Sch 2 compares the day an Act was passed with the day of another dated event: "after the establishment of the Irish Free State" (para 4(2)), a territory that "ceased after that time" (para 4(3)(b)), "before the Welsh Language Act 1967" (para 5(a)). What of an Act passed on the very day of the event? | The Act is later (or earlier) than the event; it is not; the text does not order two events on one day. | **Refuse**, by a named refusal for each of the three (`Schedule 2 para 4(2) does not say whether an Act passed on the day the Irish Free State was established was passed after it`, `Schedule 2 para 4(3)(b) does not say whether a territory that ceased on the day the Act was passed ceased after it`, `Schedule 2 para 5(a) does not say whether an Act passed on the day the Welsh Language Act 1967 was passed was passed before it`). The day of each event is an input. Same treatment as F8. "Before the commencement" (paras 4(3), 5(b), 5(c)) is not in this fork: the commencement is at the beginning of its day (F9). | Sch 2 para 4(2) (src:416), para 4(3)(b) (src:417, 419), para 5(a) (src:424-425). Each speaks of one event as after or before another, and a day alone does not order two events on it. |
| F23 | Sch 2 para 4(3)(a): a colony "excluded, but in relation only to Acts passed at a later time, by any enactment repealed by this Act". Which Acts are "passed at a later time", when an Act is passed on the day from which the exclusion took effect? | That Act is at a later time, so the exclusion binds it and the colony is not included; that Act is not later, so the colony is included. | **The input is named "the day from which an enactment repealed by this Act excluded it", and an Act passed on that day is passed with the exclusion in force**: the colony is included only for an Act passed on an earlier day. The repealed enactments and s 18(3) of the 1889 Act are not among the sources, so whether the colony is such a colony, and the day, are inputs. | Sch 2 para 4(3)(a) (src:417-418). "From which" gives the first day on which the exclusion operates. |
| F24 | Sch 2 para 4(6): "This paragraph applies to . . . the Water Act 1973 as if they were passed after 1st April 1974." An Act treated as passed after that day is passed on no particular day, so what of a Schedule 1 mark that could go either way (a year of 1974 or later, a date after 2 April 1974)? | Apply the paragraph; do not apply it; the mark does not decide. | **The mark decides only where every possible day gives one answer**: a year before 1974 or a date up to and including 2 April 1974 means the Schedule 1 paragraph applies; any other year or date is **refused** (`Schedule 2 para 4(6) treats the Act as passed after 1st April 1974 and names no day, so the mark of the paragraph is not decided`). | Sch 2 para 4(6) (src:423), read with para 4(1) (src:413-415): a year mark applies to Acts "after the year", a date mark to Acts "on or after the date". |
| F25 | s 23(2): "references to the passing or repeal of an enactment are to be construed accordingly". What do passing and repeal become for an enactment comprised in subordinate legislation? | Making and revocation; the text does not say. | **Making and revocation** (`section 23(2) names the event for an enactment comprised in subordinate legislation as`). s 23(2) does not itself use those two words. s 24(2) and s 23ZA(3) say them in terms for Northern Ireland Orders in Council and assimilated direct legislation, and the same pair is the only one "accordingly" can mean for subordinate legislation. | s 23(2) (src:108); compare s 24(2) (src:182) and s 23ZA(3) (src:120). |
| F26 | s 22(1) applies the Act to Acts passed after the commencement "subject, in the case of section 20(2A) to (6), to the provision made in section 20(2A) or (3) and, in the case of section 20A, to the provision made in that section". What does the carve-out cut? | (a) s 20(2A) to (6) reach only Acts passed on or after IP completion day, and s 20A only Acts passed after its own commencement; (b) they reach every Act passed after 1 January 1979 and "the provision made" is only their own content. | **(a).** The two readings agree for s 20(2A) and (3), which say "an Act passed on or after IP completion day" themselves; they differ for s 20(4) to (6), which under (b) would reach earlier Acts but have nothing to act on there. The module `uk-interpretation-eu.l4` gives `does not apply` for an Act passed before the commencement (F15), and for an Act after it but before the relevant day. "IP completion day" and the day section 20A came into force are inputs (F13); "IP completion day" is a moment and the Act is passed on a day, so an Act passed on that day is read as passed on it. | s 22(1) (src:103); s 20(2A)(a) (src:89); s 20(3) (src:92); s 20A (src:97). |
| F27 | s 23C(3): in s 18 the reference to an act or omission that constitutes an offence under two or more Acts "includes an act or omission which constitutes an offence under (a) any legislation to which that section applies, and (b) any legislation to which Part 2 of the Legislation (Wales) Act 2019 applies". Is "and" both, or either? | Both (an offence under legislation of each kind); either (an offence under legislation of one kind). | **Both**, as written: the inclusion is an act or omission that is an offence under legislation of each kind. An offence under two pieces of Part 2 legislation and none of the other kind is not added by this subsection; the caller's answer apart from it stands. | s 23C(3) (src:172-175). |

## Answer table for the worked cases

The six period cases: the text is silent, and each is a named refusal that the tests assert (`tests-time.l4`, the `§ Periods of days, weeks, months and years` section).

| case | counted from | result | what the text says, with the section |
| --- | --- | --- | --- |
| three years | 2025-07-16 | **REFUSED**: "the Interpretation Act 1978 does not define year and has no rule for counting a period of years after an event" | silent: no definition of "year" and no counting rule; Sch 1 defines "month" and "financial year" only (src:288, 268) |
| five years | 2025-01-15 | **REFUSED**: same | silent, as above |
| five years | 2025-09-01 | **REFUSED**: same | silent, as above |
| thirty days | 2026-01-01 | **REFUSED**: "the Interpretation Act 1978 has no rule for counting a period of days from a day" | silent: no definition of "day" and no counting rule; whether 2026-01-01 is counted is not said (F1) |
| two years | 2024-02-28 | **REFUSED**: the years message | silent; the end of the second year is not given (F3, F4) |
| one year | 2024-02-29 | **REFUSED**: the years message | silent; what a year lacking 29 February does is not said (F4) |
| one month | 2025-01-31 | **REFUSED**: "the Interpretation Act 1978 defines a month as a calendar month but has no rule for counting a period of months after an event" | Sch 1 "Month" means calendar month [1850] (src:288): the word is defined, and what a calendar month after 31 January ends on is not said (F3, F4) |

No computed date appears in this table because the text gives none.
If the reader supplies the missing rule from outside the Act, it is not an answer of this encoding.

The commencement cases (`tests-time.l4`, `§ Section 4`):

| case | result | what the text says, with the section |
| --- | --- | --- |
| an Act is passed (Royal Assent) on 2026-03-10 and says nothing | day **2026-03-10**; moment **"at the beginning of that day"** (the enum value `the beginning of the day`; on reading A of F6 and s 9 it is 00:00:00 Greenwich mean time, a separate function) | s 4(b) (src:15), "where no provision is made for its coming into force, at the beginning of the day on which the Act receives the Royal Assent". If it was only "published" on that day, the text is silent (F10). |
| an Act says its day is to be fixed later, and the day is fixed as 2026-06-01 | day **2026-06-01**; moment "at the beginning of that day". Before the day is fixed: REFUSED ("the enactment provides for a day to be fixed later and none is fixed yet, so neither limb of section 4 gives a day") | s 4(a) (src:14), with F5. |
| subordinate legislation is made on 2026-03-10 and says nothing | **REFUSED**: "the Interpretation Act 1978 has no rule on when subordinate legislation that makes no provision comes into force" | s 23(1) (src:107) applies the Act's provisions to subordinate legislation "except sections 1 to 3 and 4(b)"; Sch 2 para 6 (src:429) lists s 4(a) only for earlier instruments. s 4(a) does apply, so subordinate legislation that names a day takes it, at the beginning of that day (tested). |

Further answers from pass 2, each asserted in the named tests file (the days and counts the Act borrows from other texts are inputs, and the tests pick illustrations, which are not claims about those texts):

| case | result | what the text says, with the section |
| --- | --- | --- |
| is the Republic of Ireland in the "British Islands" for an Act passed 1950-01-01 (Irish Free State day given as 1922-12-06)? | **yes** (`tests-definitions.l4`, § "British Islands"); for an Act passed on or after 1979-01-01: **no**; for an Act passed on 1922-12-06 itself: **REFUSED** (F22) | Sch 1 "British Islands" (src:229) and Sch 2 para 4(2) (src:416) |
| is a messuage "land" in an Act passed 1900-01-01? in one passed 2000-01-01? | **yes**; **no** (Sch 1 "Land" does not name it). A building: **no** for 1900; **yes** for 2000 | Sch 1 "Land" [1st January 1979] (src:276), Sch 2 para 4(1) (src:413-415) and para 5(b) (src:426); `tests-definitions.l4`, § "Land" |
| does s 6(b) reach an Act passed 1960-01-01? | **`does not apply`** | s 22(1) (src:103) with Sch 2 Part I, which does not list it (F15); `tests-direct.l4` |
| does s 20(3) reach an Act passed 2020-12-30, with IP completion day given as 2020-12-31? | **`does not apply`**; for an Act passed 2020-12-31: **`applies without limit`** | s 22(1) (src:103), s 20(3) (src:92) (F26); `tests-eu.l4` |
| does s 9 reach a Measure of the National Assembly for Wales enacted 2010-01-01? s 1? | s 9: **`applies without limit`**; s 1: **`does not apply`** | s 23B(1) (src:145) "except sections 1 to 3"; `tests-devolved.l4` |
| are the provisions of the Act applied to an instrument made 2025-01-01 by the Welsh Ministers under an Act of Parliament, made alone, with nothing in it that applies other than in Wales? | **no** (`section 23B(3) allows ...` is FALSE) | s 23B(3) (src:152-155): "only if" it was made before 1 January 2020, made with another person, or contains a provision that applies otherwise than in relation to Wales |
| a Schedule 1 paragraph marked `[1889]`, for an Act treated as passed after 1 April 1974 (the Water Act 1973) | **applies**; marked `[1974]` or `[1st January 1979]`: **REFUSED** (F24) | Sch 2 para 4(6) (src:423) with para 4(1) |
| which provision of this Act "corresponds" to a provision of the Interpretation Act 1889 (s 25(2))? | **REFUSED** (the Act does not say); the extent to which a provision the caller names applies to a reference made on a given day is answered | s 25(2) (src:214); Schedule 3 shows no rows in this text |
| for an enactment comprised in Northern Ireland legislation that is an Order in Council, may the "making" be read as its "passing" (s 24(2)), and the "revocation" as its "repeal"? | **yes** for an Act passed or subordinate legislation made on or after 1979-01-01; **no** before it, and **no** where it is not an Order in Council | s 24(2) (src:182); `tests-devolved.l4` |

Other answers the encoding gives from the text, with the section, are in the coverage table's `where it is encoded` column.

## Where I looked for the items the text does not answer

"No ambiguities found" is not the claim; this is where the searches were run (case-insensitive, over `../../registers/source-bundle/ukpga-1978-30.txt`, 440 lines), and what they returned.

| search | hits |
| --- | --- |
| `sunday`, `holiday`, `recess`, `rest day`, `saturday`, `weekend`, `working day`, `business day`, `closed`, `clear day` | 0 |
| `week`, `fortnight`, `beginning with`, `inclusive` | 0 (the one hit on `exclusive` is "exclusively so triable", Sch 1 line 338) |
| `midnight`, `o'clock`, `hour`, `minute`, `noon` | 0 |
| `publish`, `publication`, `gazette`, `printed` | 2, both in s 19(1) (lines 81 and 83, "printed by authority", "printed by the Queen's Printer"), unrelated to coming into force; "publish" and "publication" 0 |
| `language`, `authentic`, `version`, `official` | 1: "Welsh Language Act 1967", Sch 2 para 5(a) |
| `royal assent` | 4: s 4(b), s 23B(1)(b), s 23C(1)(b) and s 23C(4)(b) |
| `period` | 3: s 9 ("the period of summer time"), s 14A(2)(a) and (b) ("specified period") |
| `calendar` | 1: Sch 1 "Month" |
| `year`, `day` | the definitions and bars of Sch 1 and Sch 2 (years such as 1850 and 1889 as bars; "at the end of a specified day or a specified period" in s 14A) and s 4; none defines either word |

## What check.sh prints

Run as `cd <this directory> && env -u JL4_LIBRARY_PATH L4=<the supplied l4-unstable-0528> L4_TARGET=unstable ./check.sh`; it exited 0, at the end of pass 2, after the last edit to any `.l4` file.
Standard output, exactly:

```
module                                    errors satisfied  failed  refused  expected
tests-application.l4                           0       545       0        0         0
tests-construction.l4                          0       155       0        0         0
tests-definitions.l4                           0       241       0        0         0
tests-devolved.l4                              0       264       0        0         0
tests-direct.l4                                0        94       0        0         0
tests-eu.l4                                    0        58       0        0         0
tests-general.l4                               0        44       0        0         0
tests-red.l4                                   7         0       7        0         7
tests-repeals.l4                               0        42       0        0         0
tests-schedule1.l4                             0      1033       0        0         0
tests-service.l4                               0        22       0        0         0
tests-time.l4                                  0       141       0        0         0
uk-interpretation-application.l4               0         0       0        0         0
uk-interpretation-construction.l4              0         0       0        0         0
uk-interpretation-definitions.l4               0         0       0        0         0
uk-interpretation-devolved.l4                  0         0       0        0         0
uk-interpretation-eu.l4                        0         0       0        0         0
uk-interpretation-general.l4                   0         0       0        0         0
uk-interpretation-repeals.l4                   0         0       0        0         0
uk-interpretation-schedule1.l4                 0         0       0        0         0
uk-interpretation-service.l4                   0         0       0        0         0
uk-interpretation-time.l4                      0         0       0        0         0
TOTAL (22 modules)                             7      2639       7        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Standard error, one line: `check.sh: the target is unstable, so the main check was skipped.`

The baseline taken before any change in pass 2, on the same binary, was 11 modules: 905 satisfied (545 / 155 / 42 / 22 / 141), 7 failed in `tests-red.l4`, 0 refused.
Those six lines are unchanged in the table above (the pass-1 modules, tests and `check.sh` have not been modified since the deposit was copied in; see "Changes to existing modules").
The 1734 satisfied assertions that are new are 1033 (`tests-schedule1.l4`, generated from the text), 241, 264, 94, 58 and 44.

How to read it.
The numbers are error diagnostics, assertions satisfied, assertions failed, assertions refused, and the failures the file is expected to have.
`tests-red.l4` has 7 failed assertions, all expected (`expected_failed` in `check.sh` and `expected_red` in `encoding.json`), so its 7 errors are the same 7.
Every new test file asserts exactly as many assertions as it satisfies: `grep -c '^#ASSERT'` gives 241, 264, 94, 58, 44 and 1033 for the six, the same numbers.
There are **0 refused assertions**: a plain `#ASSERT` over an expression that refuses would print `assertion refused` and count there, and none does.
The refusals that the tests mean are written `#ASSERT REFUSED ... BECAUSE "<reason>"`, which pins the reason as well; there are 101 of them across the test files.
No other diagnostic exists: each module prints the one `@lang en` Hint described above and nothing else.
`srcrefs.py check --refs` over all 22 files prints `604 src: lines, 290 runs, 387 locators, 0 problems` (baseline before pass 2: `194 src: lines, 71 runs, 106 locators, 0 problems`).
`tools/coverage.py check` prints `436 units, 436 rows, {'inert': 26, 'encoded': 367, 'fork': 21, 'repealed or blank in this text': 22}, 0 problems`.
`tools/gen_schedule1.py check` prints `schedule1 check: 110 rows, 0 problems`.
The sweep `l4 check <file> | grep -E 'is at the end of the file|follows code on its line'` over all 22 files prints nothing.
The counts are a point-in-time record from the `l4` build named above; canon has no CI that re-runs them.

## Mutation check

**Pass 1.**
The assertions were tested against 24 hand-made mutations of the modules (one change each: an operator, a boundary year, a deleted condition, a refusal turned into a value, a refusal that no longer refuses).
Each mutation was applied to a copy and the module's own test file run; **all 24 were caught** (at least one assertion failed or refused).
The mutated lines include: s 4(b) reaching subordinate legislation; the 1889 bar moved to 1888; the financial year starting a day early; a period function that computes a date; the rest-day function that returns its input; s 9 ignoring summer time; s 7 dropping the pre-paid condition; s 17(1) in force through the commencement day; s 20(1) excluding the first part; s 23(1) no longer excepting s 4(b); the England mark date moved a day; the Church Assembly bar read as on or after.
Those 24 were run on the pass-1 modules; they were not re-run in pass 2 because pass 2 did not change those modules or their tests.

**Pass 2.**
34 hand-made mutations of the five new hand-written modules (`schedule1` is generated from the table and its tests are generated from the text, so it was not mutated), one change each, each applied to a copy and the module's own test file run.
**33 were caught** (at least one assertion failed); **1 survived**, and 1 of the 33 was caught only after tests were added:

| module | mutated line | result |
| --- | --- | --- |
| definitions | British Islands: `AT LEAST` the commencement day made `GREATER THAN` | caught |
| definitions | British Islands: Irish Free State day, `GREATER THAN` made `AT LEAST` (the same-day refusal gone) | caught |
| definitions | para 5(a) Wales: `LESS THAN` made `AT MOST` (the same-day refusal gone) | caught |
| definitions | para 5(a) Berwick upon Tweed: `LESS THAN` 1 April 1974 made `AT MOST` | caught |
| definitions | Schedule 1 "Colony": the associated-state exception deleted | caught |
| definitions | para 4(3)(a): `LESS THAN` made `AT MOST` | caught |
| definitions | para 4(3)(b): `GREATER THAN` made `AT LEAST` | caught |
| definitions | "Land": a messuage counted | caught |
| definitions | para 5(b): `GREATER THAN 1850` made `AT LEAST` | caught |
| definitions | para 4(6): year `LESS THAN 1974` made `AT MOST` | caught |
| definitions | para 4(6): the date bound 2 April moved to 3 April | caught |
| definitions | "Person": `OR` made `AND` | caught |
| definitions | "EU instrument": the exclusion of assimilated direct legislation removed | caught |
| definitions | offences (c): the Part V exclusion removed | caught |
| definitions | general limit: the test for "triable either way" negated | caught |
| definitions | para 5(a) Wales: a clause `day LESS THAN 1 January 1900` added in front | **survived**: it differs from the original only when the caller gives a Welsh Language Act day before 1900, which no test supplies and which is not the day of the Act named; no reading of the text calls for such a test |
| general | s 1: `applies without limit` made `does not apply` | caught |
| general | s 22(2): a reference to an enactment made limited | caught |
| general | s 23(2): `OR` made `AND` | caught |
| general | s 23(2): repeal named `repeal` instead of `revocation` | caught |
| eu | s 20(2A): `AT LEAST` IP completion day made `GREATER THAN` | caught |
| eu | s 20(3): the "subject to (2A)" test negated | caught |
| eu | s 20A: `AT LEAST` its commencement day made `GREATER THAN` | caught |
| eu | the carve-out for s 20(4) cut at the day of s 20A instead of IP completion day | **survived the first run** (the tests for s 20(4) to (6) used days that both bounds agree on); caught once four assertions were added to `tests-eu.l4` that sit on IP completion day itself (s 20(3) to (6)) |
| devolved | s 23ZA(1): s 13 no longer excepted | caught |
| devolved | s 23ZA(4)(a): exit day replaced by IP completion day | caught |
| devolved | s 23B(1): `LESS THAN` 1 January 2020 made `AT MOST` | caught |
| devolved | s 23B(3): the same | caught |
| devolved | s 23B(7): `AT LEAST` made `GREATER THAN` | caught |
| devolved | s 23C(3): `AND` made `OR` | caught |
| devolved | s 24(2): "making" replaced by "revocation" | caught |
| devolved | s 24(3): `an Act` replaced by `subordinate legislation` | caught |
| devolved | s 24(4): "The Tax Acts" no longer applied | caught |
| devolved | s 23A(2): s 17(2)(b) no longer named | caught |

The survivor of the first run is a finding about the tests, not noise: a boundary test has to sit on the boundary that the mutant moved, and a pair of days that the original and the mutant both put on the same side proves nothing.
The mutation script is not shipped (it holds scratch paths); the list above is the record.

## Jural relations

This Act is a statute about how other enactments are read, so most of it is not a relation between parties at all (a rule of construction, a definition, a date).
Hohfeld relations appear where the text itself speaks of a power, a duty, a right, a liability or an immunity; they are listed below with the words of the text and the function that encodes the sentence.
(A Hohfeld table classifies; the function is what runs.)

| section | the text's words | Hohfeld incident (holder) | correlative | encoded by |
| --- | --- | --- | --- | --- |
| s 12(1) | "the power may be exercised, or the duty is to be performed, from time to time as occasion requires" | power (the donee of the power); duty (the person on whom it is imposed) | liability (those subject to the power); claim-right (those to whom the duty is owed) | `section 12(1) provides that the power may be exercised, or the duty is to be performed, from time to time as occasion requires` |
| s 12(2) | "by the holder for the time being of the office" | power and duty pass to each successive office-holder | liability; claim-right, as above | `section 12(2) provides that the power may be exercised, or the duty is to be performed, by the holder for the time being of the office` |
| s 13 | an instrument may be made, or a power exercised, "at any time after the passing of the Act" to bring the Act into force or give it full effect | power (the maker), anticipatory | liability (the instrument's addressees, once in force) | `section 13 permits the power to be exercised on`, `section 13 permits an instrument made under the Act to come into force at` |
| s 14 | "a power ... to revoke, amend or re-enact" an instrument | power (the maker of the instrument) | liability (the instrument and those under it to being changed) | `section 14 provides a power to revoke, amend or re-enact any instrument made under the power` |
| s 14A(2) | the subordinate legislation "may include" provision for review or expiry | privilege, or liberty (the maker) | no-right (anyone who would insist that it leave such provision out) | `section 14A permits subordinate legislation to include` |
| s 16(1)(c) | "any right, privilege, obligation or liability acquired, accrued or incurred" under the enactment repealed | immunity of each of those incidents from being lost by the repeal | disability of the repealing enactment to divest it | `section 16(1) provides that the repeal of an enactment by an Act does not revive or affect` |
| s 16(1)(d), (e), closing words | "any penalty, forfeiture or punishment incurred", and "any investigation, legal proceeding or remedy", "may be instituted, continued or enforced" | power (the enforcing authority, the party to the proceeding) | liability (the person who incurred the penalty or is subject to the proceeding) | `section 16(1) provides that it may be instituted, continued, enforced or imposed as if the repealing Act had not been passed` |
| s 18 | "liable to be prosecuted and punished under either or any of those Acts or at common law" | liability (the offender) | power (the prosecutor) | `section 18 provides that the offender is liable to be prosecuted under either or any of those Acts or at common law` |
| s 18 | "shall not be liable to be punished more than once for the same offence" | immunity (the offender) | disability (the court and the prosecutor) | `section 18 provides that the offender is not liable to be punished more than once for the same offence` |
| s 19(2) | "may continue to be cited by the short title" | privilege (anyone citing the Act) | no-right | `section 19(2) provides that the Act may continue to be cited by the short title notwithstanding the repeal of the enactment` |
| s 21(2) | "This Act binds the Crown" | liability (the Crown, to the Act's operation) | power (Parliament, over the Crown) | `section 21(2) provides that the Interpretation Act 1978 binds the Crown` |

Everything else in the Act is a rule of construction, a definition, a rule of application or a date, and is not a relation between persons; it is encoded as a function over the text and listed in the coverage table.

## Changes to existing modules

**None.**
No pass-1 module, test file, `check.sh` or `srcrefs.py` was edited in pass 2, and no defect was found in them that the text shows.
Evidence: every one of those 14 files still carries the modification time of the moment the deposit was copied in (15:06:23 on 2026-10-29), and every file written in pass 2 is later; the baseline (905 satisfied, 7 failed in `tests-red.l4`, 0 refused) was taken before any change and is the same in the final run.
`Provision of the Act` in `uk-interpretation-application.l4` stops at section 21 and was not widened: the provisions from s 20(2A) on that need an extent have a type of their own in `uk-interpretation-eu.l4`, and the devolved sections use the existing type.

## What is needed before relying on this

1. **A read against the official text.** The source is a converter rendering, not the official text (above). No domain expert has read this encoding against the statute.
2. **Rulings on the forks.** F1 to F27 are readings I took from the text alone; the ones that change an answer most are F14 (what the years and dates bar), F15 (an unlisted provision does not reach an earlier Act), F19 ("so far as applicable"), F22 (two events on one day), F24 (a mark that goes either way), F26 (what the carve-out cuts) and F27 ("and" in s 23C(3)).
3. **The inputs, filled in by the caller from the Acts that give them** (finding 8): the days, the limit and the meanings the Act borrows. A caller who fills them wrongly gets wrong answers from right functions.
4. **The text of Schedule 3**, if s 25(2)'s "corresponding provision" is to be computed and not supplied.
5. **"So far as applicable" and "unless the contrary intention appears"** are facts about the instrument that the caller weighs after reading the extent (F19); no function decides them.
6. **The main compiler.** The target is `unstable`; nothing here was run on a `main` build.
7. **A holiday calendar and a counting rule**, from outside the Act, if the six period cases are to be answered; the Act has none (above).

## Open questions for a domain expert

1. Does anything outside this Act, in the law the reader works under, supply the counting rule and the rest-day rule that the six refused cases need? The Act does not, and this encoding has no source for them. If one is found, it belongs in its own module with its own `@ref`s, beside this one.
2. s 9 and s 4 (F6): does "the beginning of that day" count as "an expression of time" in an Act, so that Greenwich mean time governs it?
3. s 9 is subject to s 3 of the Summer Time Act 1972, whose text is not among the sources. What does it say, and should the summer-time refusal become a rule?
4. Schedule 3 shows no rows in this text. Does the official text have a table of enactments repealed there? s 25(2)'s "corresponding provision" needs it.
5. F14: is it right that the years and dates after Schedule 1 entries bar a definition only for Acts passed before the commencement?
6. s 7 (F11): what time governs once the contrary is proved?
7. The dates "IP completion day" and "exit day" (ss 20(2A), 20(3), 21(1), 23ZA(4)), and the days of the other Acts the text points at (finding 8), are given by other Acts. Which are they, and should any function take them as constants?
8. The devolved provisions (ss 23ZA, 23A, 23B, 23C, 24) are now encoded as rules over inputs: the kind of legislation, whether it is amended, the day it was made, and what the Government of Wales Act 2006 and the Scotland Act 1998 say. Is that the right division, or should the taxonomy of Scottish, Welsh and Northern Irish legislation be built in the encodings of those jurisdictions' statutes and imported here?
9. s 13 (F8): is an instrument that comes into force at the beginning of the day of the Royal Assent "after the passing of the Act"?
10. F22: for an Act passed on the very day of the event that Sch 2 paras 4(2), 4(3)(b) or 5(a) compares it with, is it after (or before) that event?
11. F25: for an enactment comprised in subordinate legislation, are the "passing" and "repeal" that s 23(2) speaks of the making and the revocation?
12. F26: does the carve-out in s 22(1) cut s 20(2A) to (6) off at IP completion day, or is it only the content of (2A) and (3)?
13. F27: does "and" in s 23C(3) mean an offence under legislation of both kinds, or either?

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `tools`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 499 numbered scenarios over every Part, section and Schedule of the Act, including cases where the text is silent.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for, and ran it against this encoding.
`ANSWERS.md` is not kept in this folder; the scenario numbers `S<n>` in `tests-independent.l4` refer to it, and each assertion carries its provision and text line.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against this encoding | 459 | 454 | 1 | 4 |
| after the reconciliation below (no change to any encoding module) | 459 | 459 | 0 | 0 |

The 40 scenarios the encoding has no function for are the `GAP` lines in the test file (40 + 459 = 499); they are limits of the encoding, not passes.
Of the 454 first-run passes, 18 are `#ASSERT REFUSED` where the encoding refused, and the reviewer lists nine groups of scenarios (S5/S7, S67/S68, S83/S84, S128/S130, S149 to S151, S163/S164, S328/S330, S411/S412, S236/S237) that make the identical call because the encoding has no input to tell them apart (a power from a duty, a contrary intention that is express from one that is implied).
The number 459 is therefore not 459 independent checks.

**What the five disagreements turned out to be: none was an encoding defect.**

- **S310 was the independent author's mistake on the text.**
  The author applied the bracketed date of Schedule 1 "EEA agreement" (8 January 2007) to an Act passed on 7 January 2007.
  The note to Schedule 1, the heading of Schedule 2 and section 22(1) confine the brackets to Schedule 2 paragraph 4 (application to existing enactments); an Act passed after the commencement takes all of Schedule 1.
  That is this encoding's fork F14, and the assertion is rewritten to the encoding's answer with a `-- RECONCILED` comment quoting the original.
  The reviewer's own note (A11) records that it still finds the practical result odd, since a 2007 date can only matter for a later Act.
- **S50, S53, S60 and S138 differ only in how "no" is spelled.**
  Each asked for a plain NO from a rule that has no yes/no function, only a value function (the way a distance is measured, the time standard, the Sovereign, the edition cited).
  Where a contrary intention appears, the value function refuses, and a refusal passed through `NOT` stays a refusal.
  Each is rewritten as `#ASSERT REFUSED`, with the original in the comment above it.

**The encoding's silence convention is split, and the independent author noticed.**
Value-returning functions refuse where the section gives no answer; the yes/no "provides that" and "counts" functions return `FALSE` for "the section does not provide it".
The reviewer's S83, S84, S231, S236 and S237 are asserted with `NOT (...)` for that reason.
Both are legitimate readings of silence; a caller who combines the two kinds should expect the difference.

**Known limits shown by the gaps** (the reviewer's wording, from the test file).
No function compares a clock time with a commencement (S10, S11, S13); the Scottish and Northern Irish limbs of the court entries have no jurisdiction lookup; the London borough entry takes no borough number; entries held as text only cannot be asked a negative (the standard scale's "triable only summarily" condition, "registered medical practitioner"); "clear days" has no function; the days on which IP completion day and exit day fall are inputs.
The others are one-line comments in the file.

**Check.** `check.sh` with `tests-independent.l4` in the folder: 23 modules, 3098 satisfied, 7 failed (the expected seven), 0 refused, run on 2026-10-29 with the same binary as the other counts in this file.
