# NOTES: the Interpretation Act (British Columbia), RSBC 1996, c. 238, in L4

Row: `legalese-sonnet-5.5`.
Pass 2 completes the draft that pass 1 wrote, to "whole": every unit of the text has a row in the coverage table, with exactly one disposition.
A single Sonnet 5.5 agent wrote both passes, working alone from the briefs, with no subagents and no other encoding to copy from.
Status: **draft**. No domain expert has read it against the statute.

## 0. What this is, and the status of the source

**What it is.**
An English L4 encoding of the Interpretation Act (British Columbia), RSBC 1996, c. 238, written to be reused.
An encoding of any other British Columbia enactment can `IMPORT` `bc-interpretation-time` and ask when a period ends, whether a day falls inside it, what a holiday does to it, and from what day and moment an enactment binds.
It can also `IMPORT` `bc-interpretation-terms` and ask whether the Act defines a term, how, and what the definition names, leaves out or points at.
The other modules answer, one rule at a time, what the Act's rules of reading, powers, appointments, repeals and citations say about a case.

**The source.**
`RSBC-1996-c.-238.txt` (consolidation current to 2026-10-13; text sha256 `2d0b9b39ee02996f119a4fd91d42f1e1fc3f2446f8482bd6ad90b9ae4a2ce862`, the value `shasum -a 256` gives for the file in `../../registers/source-bundle/`, checked in this pass).
It is a plain-text rendering made by a converter script from the King's Printer consolidation.
**It is not the official text, and nothing here is verified against the official text.**
Quotations in the modules are copied from that file by `srcrefs.py` (`-- src:N | ...` lines, `N` a line of the file); `python3 -I srcrefs.py check --strict <the .txt> <module>` confirms that every `@ref` locator spans the lines its quotations come from.
The licence note for the text is `../../SOURCE-LICENSE.md`; `SOURCE-LICENSE.md` points at it and does not repeat it.

One rendering oddity, which appears three times and matters most for the first: the paragraphs (a) and (b) of the definition of "regulation" are printed after the semicolon that ends the definition (src:14-16), and the same happens to "insurance company" (src:257-259) and "final agreement" (src:334-336); see fork F-rendering-order.

**Target compiler: `unstable`.**
The brief mandates `REFUSE` for what the text does not answer, and `main` rejects `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` and `YMD` (`dialects.md` of the writing-l4-rules skill).
`check.sh` defaults to `unstable` here and says so on stderr.
**No run against a `main` build was made**, so nothing here claims these modules read on `main`.

**Pinned binary.**
`/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d` (`shasum -a 256`, computed in this pass).
Its `--version` line is `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`.
`JL4_LIBRARY_PATH` was left unset throughout.
Pass 1 was run with a different binary (`/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`); the baseline of section 5 was reproduced with the pass-2 binary before any change and gave the same numbers.

### Modules (reading order; each starts `@lang en`)

| file | imports | what it holds |
| --- | --- | --- |
| `bc-interpretation-time.l4` | `prelude`, `daydate` | pass 1. Counting periods (ss 25.2 to 25.4), what holidays and closed offices do (ss 25(3), 25(4), 25.5, 29 "holiday"), whether a day is inside a period, the moment of commencement in Pacific Time (ss 3, 4, 26), regulations (s 3(5)), proclamations (s 16(2)), appointments (s 20(3), (4)), age (s 25.1), the time words of s 29 |
| `bc-interpretation-definitions.l4` | `prelude`, `daydate` | pass 1; ss 18, 24, 28(1) and 38 changed in pass 2 (finding 2, section "Changes to existing modules"). Ss 1 ("regulation", "enactment"), 2(1), 5(1), 14, 18, 24, 28(1), 29 (deliver, mail, minor), 33(1), 38, 42(2) |
| `bc-interpretation-repeal.l4` | `prelude`, `daydate` | pass 1; s 4(4) changed in pass 2 (finding 2, section "Changes to existing modules"). Ss 4(4), 32, 35, 36(1)(a), (d), (e) |
| `bc-interpretation-terms.l4` | `prelude`, `daydate` | pass 2. The catalogue of the defined terms of ss 1, 8.1(1), 29, 29.1(1), 29.2 and 32(1): one constant per entry (121) and one per cross-reference (14), lookup rules by term and scope, the membership rule, a few computable definitions, and the Schedule as 52 legs |
| `bc-interpretation-reading.l4` | `prelude`, `daydate`, `bc-interpretation-definitions` | pass 2. The rules of reading and form: ss 2(2), 2(3), 6, 7, 8, 8.1(2), 8.1(3), 9, 10, 11(1), 11(2), 12, 13, 15, 28(2) to (4), 30, 31, 33(2) to (6), 39, 40, 42(1), 43, 44 |
| `bc-interpretation-powers.l4` | `prelude` | pass 2. Corporate capacities, judges' powers, the demise of the Crown, included powers, acting for ministers and public officers, ancillary powers, regulation-making powers: ss 17, 19, 21, 22, 23, 27, 41 |
| `bc-interpretation-commencement.l4` | `prelude` | pass 2. Ss 3(4), 5(2), 16(1), 16(3), 20(1), 20(2), 20(5) |
| `bc-interpretation-periods.l4` | `prelude`, `daydate` | pass 2. Ss 25(1) (the reference day) and 25(2) (deeds and other instruments) |
| `bc-interpretation-replacement.l4` | `prelude`, `bc-interpretation-repeal` | pass 2. Ss 34, 36(1)(b), 36(1)(c), 37 |

New modules sit beside the old ones and `IMPORT` what they reuse; none copies a rule from another.
`bc-interpretation-terms.l4` has a block between `-- >>> GENERATED` and `-- <<< GENERATED` that `gen-terms.py` writes from `terms-data.py` (finding 4 says what that does and does not show).

### Calling the time module

```l4
IMPORT `bc-interpretation-time`

-- The caller's own holidays (the text names most holidays but dates almost none of them).
GIVEN d IS A DATE
GIVETH A BOOLEAN
`my other holidays` d MEANS d EQUALS YMD 2026 4 3

-- The WHOLE calendar: the text's own Sundays and 26 December, plus the caller's.
GIVEN d IS A DATE
GIVETH A BOOLEAN
`my holidays` d MEANS `s 29 a day is a holiday` `my other holidays` d

-- 30 days from 2026-01-01: 2026-01-31 (the reference day is not counted).
#EVAL `the last day of a period of days counted from a day` (YMD 2026 1 1) 30

-- 30 days from 2026-03-06, for doing an act: the span is 2026-03-07 to 2026-04-06.
-- The 30th day is Sunday 2026-04-05, a holiday, so the end moves to Monday 2026-04-06.
#EVAL `the span of days of a period for doing an act` `my holidays` (YMD 2026 3 6) `The reference day is before the period` (`Period of time` WITH `unit` IS Days, `how many` IS 30, `clear` IS FALSE)

-- An Act with no other date of commencement, assent on 2026-03-10: binds from 00:00 Pacific Time that day.
#EVAL `the moment from which a portion of an Act binds` (JUST (YMD 2026 3 10)) `It provides no date of commencement`
```

I re-ran that snippet in this pass with the pinned binary; the three results are the ones in the comments (31 January 2026; 7 March to 6 April 2026; 10 March 2026, 0 hours 0 minutes).

**Two things to know before calling the time module, sorted by how they fail.**
*Loud:* a count that is not one or more whole units, a month or year that cannot be counted as the text says, and every case the text does not answer, return a named `REFUSE` (a warning, and a refused assertion in a test).
*Silent:* the holiday function you pass is used as the whole calendar.
It is not topped up with Sundays, so a calendar that omits `s 29 a day is a holiday` leaves a Sunday end alone and returns a plausible, wrong date with no diagnostic (test: `bc-tests-time-holidays.l4`, section "The calendar passed in is the whole calendar").

**One more silent failure, in the new modules.**
Every rule of the Act applies "unless a contrary intention appears" (s 2(1)).
The new rules do not ask for that input; the caller asks `s 2(1) a provision of this Act applies to an enactment` (in `bc-interpretation-definitions.l4`) first, and a caller who does not gets an answer that ignores a contrary intention, with no diagnostic (finding 3).


## Re-disposition audit

Written before any pass-2 L4, from the text and pass 1's coverage table (frozen as `NOTES-pass1.md`), and kept current as the work lands.
`units.py` counts the text's units from the text file; `coverage.py audit` compares them with pass 1's table.
Both run as `python3 -I units.py ../../registers/source-bundle/RSBC-1996-c.-238.txt` and `python3 -I coverage.py ../../registers/source-bundle/RSBC-1996-c.-238.txt audit`.

**Counts.**

| what | count |
| --- | --- |
| units in the text (title lines, section headings, section bodies and subsections, paragraphs and sub-paragraphs, defined-term entries, cross-reference entries of s 29, the Schedule paragraph) | 416 |
| title lines (the Act's title, the chapter) | 2 |
| section headings (52 sections, the Schedule heading) | 53 |
| section bodies and subsections (a section with no subsections counts once) | 124 |
| paragraphs and sub-paragraphs | 104 |
| defined-term entries (s 1: 6; s 8.1(1): 3; s 29: 88; s 29.1(1): 8; s 29.2(1) and (2): 10 terms, one unit each; s 32(1): 3; an entry that defines several words at once, such as "bank or chartered bank", is one unit) | 118 |
| cross-reference entries in the preamble of s 29 (`["calendar year", see "year"]`) | 14 |
| Schedule paragraph | 1 |
| rows in pass 1's coverage table | 57 (52 sections and the Schedule, 4 repealed sub-provisions) |
| units with no row in pass 1's table | 359 (416 minus the 53 heading rows and the 4 repealed sub-provisions that had rows) |
| rows in the coverage table now | 416 (one per unit; section 1 below) |

Pass 1's table had one row per section, so every subsection, paragraph, defined term and cross-reference entry below was without a row of its own.
The ones with no row are listed here by section, exactly as `coverage.py audit` prints them:

- title line 5
- title line 6
- s 1; s 1 "Act"; s 1 "enact"; s 1 "enactment"; s 1 "public officer"; s 1 "regulation"; s 1 "regulation" (a); s 1 "regulation" (b); s 1 "repeal"
- s 2(1); s 2(2); s 2(3)
- s 3(1); s 3(2); s 3(3); s 3(3.1); s 3(3.1)(a); s 3(3.1)(b); s 3(4); s 3(5)
- s 4(1); s 4(2); s 4(3); s 4(4)
- s 5(1); s 5(2); s 5(2)(a); s 5(2)(b)
- s 6
- s 7(1); s 7(2)
- s 8
- s 8.1(1); s 8.1(1) "Declaration"; s 8.1(1) "Indigenous peoples"; s 8.1(1) "regulation"; s 8.1(2); s 8.1(3)
- s 9
- s 10
- s 11(1); s 11(1)(a); s 11(1)(b); s 11(2); s 11(3)
- s 12
- s 13
- s 14(1); s 14(2)
- s 15(1); s 15(2)
- s 16(1); s 16(2); s 16(3)
- s 17(1); s 17(1)(a); s 17(1)(b); s 17(1)(c); s 17(1)(d); s 17(1)(e); s 17(1)(f); s 17(2); s 17(3)
- s 18(1); s 18(2); s 18(2)(a); s 18(2)(b); s 18(2)(c); s 18(2)(d)
- s 19(1); s 19(2)
- s 20(1); s 20(2); s 20(3); s 20(4); s 20(4)(a); s 20(4)(b); s 20(4)(c); s 20(4)(d); s 20(4)(e); s 20(5)
- s 21
- s 22; s 22(a); s 22(b); s 22(c); s 22(d); s 22(e); s 22(f)
- s 23(1); s 23(2); s 23(3); s 23(4); s 23(5)
- s 24
- s 25(1); s 25(1)(a); s 25(1)(b); s 25(1)(c); s 25(2); s 25(3); s 25(3)(a); s 25(3)(b); s 25(4); s 25(4)(a); s 25(4)(b); s 25(4)(b)(i); s 25(4)(b)(ii)
- s 25.1
- s 25.2(1); s 25.2(2); s 25.2(2)(a); s 25.2(2)(b); s 25.2(3); s 25.2(3)(a); s 25.2(3)(b)
- s 25.3(1); s 25.3(1)(a); s 25.3(1)(b); s 25.3(2); s 25.3(2)(a); s 25.3(2)(b); s 25.3(3)
- s 25.4(1); s 25.4(1)(a); s 25.4(1)(b); s 25.4(2); s 25.4(2)(a); s 25.4(2)(b); s 25.4(3)
- s 25.5(1); s 25.5(2)
- s 26(1); s 26(2)
- s 27(1); s 27(2); s 27(3); s 27(4); s 27(5); s 27(6); s 27(7)
- s 28(1); s 28(2); s 28(3); s 28(4)
- s 29; s 29 see calendar year; s 29 see Canada; s 29 see chartered bank; s 29 see civil engineer; s 29 see Crown, the; s 29 see King, the; s 29 see mining engineer; s 29 see oath; s 29 see Queen, the; s 29 see solicitor; s 29 see Sovereign, the; s 29 see swear; s 29 see Treasurer; s 29 see Treasury; s 29 "acquire"; s 29 "affidavit or oath"; s 29 "bank or chartered bank"; s 29 "barrister or solicitor or barrister and solicitor"; s 29 "British Columbia land surveyor"; s 29 "Cascade Mountains"; s 29 "commencement, with reference to an enactment"; s 29 "commercial paper"; s 29 "consolidated revenue fund, consolidated revenue or consolidated revenue fund of the Province"; s 29 "corporation"; s 29 "correctional centre"; s 29 "county"; s 29 "Court of Appeal"; s 29 "credit union"; s 29 "Criminal Code"; s 29 "deliver, with reference to a notice or other document"; s 29 "Deputy Provincial Secretary"; s 29 "dispose"; s 29 "electoral district"; s 29 "Executive Council"; s 29 "Gazette"; s 29 "government or government of British Columbia"; s 29 "government agent"; s 29 "government of Canada or Canada"; s 29 "Governor, Governor of Canada or Governor General"; s 29 "Governor in Council or Governor General in Council"; s 29 "Great Seal"; s 29 "Her Majesty, His Majesty, the Queen, the King, the Crown or the Sovereign"; s 29 "herein used in a section or part of an enactment"; s 29 "holiday"; s 29 "holiday" (a); s 29 "holiday" (b); s 29 "holiday" (c); s 29 "holiday" (d); s 29 "insurance company"; s 29 "insurance company" (a); s 29 "insurance company" (b); s 29 "judicial district"; s 29 "justice"; s 29 "land"; s 29 "land title legislation, prior to October 31, 1979"; s 29 "lawyer"; s 29 "Legislative Assembly"; s 29 "Legislature"; s 29 "Lieutenant Governor"; s 29 "Lieutenant Governor in Council"; s 29 "mail"; s 29 "may"; s 29 "medical practitioner"; s 29 "mentally disordered person, mentally incompetent person, mentally ill person or person with a mental disorder"; s 29 "minister"; s 29 "minor"; s 29 "month"; s 29 "municipality"; s 29 "municipality" (a); s 29 "municipality" (b); s 29 "must"; s 29 "newspaper, in a provision requiring publication in a newspaper"; s 29 "now"; s 29 "nurse practitioner"; s 29 "obligation"; s 29 "peace officer"; s 29 "peace officer" (a); s 29 "peace officer" (b); s 29 "peace officer" (c); s 29 "person"; s 29 "personal representative"; s 29 "prescribed"; s 29 "proclamation"; s 29 "professional engineer, civil engineer or mining engineer or words implying recognition of any person as a professional engineer or member of the engineering profession"; s 29 "property"; s 29 "Province"; s 29 "province, when used as meaning a part of Canada"; s 29 "Provincial Court"; s 29 "Provincial Treasurer or Treasurer"; s 29 "Provincial Treasury or Treasury"; s 29 "Railway Belt"; s 29 "record"; s 29 "regional district"; s 29 "registered mail"; s 29 "registrar of a court"; s 29 "Registrar of Companies"; s 29 "Registrar of Titles or registrar"; s 29 "right"; s 29 "Rules of Court, when used in relation to a court"; s 29 "Rules of Court, when used in relation to a court" (a); s 29 "Rules of Court, when used in relation to a court" (b); s 29 "rural area"; s 29 "savings institution"; s 29 "savings institution" (a); s 29 "savings institution" (b); s 29 "savings institution" (c); s 29 "savings institution" (d); s 29 "school district"; s 29 "security"; s 29 "shall"; s 29 "Supreme Court"; s 29 "sureties"; s 29 "Surveyor General or Surveyor General of British Columbia"; s 29 "trust company"; s 29 "trust company" (a); s 29 "trust company" (b); s 29 "will"; s 29 "words"; s 29 "writing, written, or a term of similar import"; s 29 "year"; s 29 "youth custody centre"
- s 29.1(1); s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement"; s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" (a); s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" (b); s 29.1(1) "settlement legislation"; s 29.1(1) "tax treatment agreement"; s 29.1(1) "treaty first nation, as the context requires"; s 29.1(1) "treaty first nation, as the context requires" (a); s 29.1(1) "treaty first nation, as the context requires" (b); s 29.1(1) "treaty first nation child"; s 29.1(1) "treaty first nation child" (a); s 29.1(1) "treaty first nation child" (b); s 29.1(1) "treaty first nation constituent, in relation to a treaty first nation"; s 29.1(1) "treaty first nation member, in relation to a treaty first nation"; s 29.1(1) "treaty lands, in relation to a treaty fi"; s 29.1(3); s 29.1(4)
- s 29.2(1); s 29.2(1) Nisg̱a'a child; s 29.2(1) Nisg̱a'a citizen; s 29.2(1) Nisg̱a'a Government; s 29.2(1) Nisg̱a'a Lands; s 29.2(1) Nisg̱a'a laws; s 29.2(1) Nisg̱a'a Lisims Government; s 29.2(1) Nisg̱a'a Nation; s 29.2(1) Nisg̱a'a Village; s 29.2(1) Nisg̱a'a Village Government; s 29.2(2); s 29.2(2) Nisg̱a'a Final Agreement
- s 30
- s 31
- s 32(1); s 32(1) "amended, in respect of a domestic enactment"; s 32(1) "amended, in respect of a domestic enactment" (a); s 32(1) "amended, in respect of a domestic enactment" (b); s 32(1) "domestic enactment"; s 32(1) "foreign enactment"; s 32(2); s 32(3); s 32(4); s 32(5)
- s 33(1); s 33(2); s 33(3); s 33(4); s 33(5); s 33(6)
- s 34
- s 35(1); s 35(1)(a); s 35(1)(b); s 35(1)(c); s 35(1)(d); s 35(1)(e); s 35(2)
- s 36(1); s 36(1)(a); s 36(1)(b); s 36(1)(c); s 36(1)(d); s 36(1)(e)
- s 37(1); s 37(2); s 37(3)
- s 38
- s 39
- s 40(1); s 40(1)(a); s 40(1)(b); s 40(2)
- s 41(1); s 41(1)(a); s 41(1)(b); s 41(1)(c); s 41(1)(d); s 41(1)(e); s 41(1)(f); s 41(2)
- s 42(1); s 42(2); s 42(2)(a); s 42(2)(b); s 42(2)(c)
- s 43; s 43(a); s 43(b); s 43(c); s 43(d)
- s 44
- Schedule paragraph

**Verdicts on every pass-1 row that was not `encoded`** (28 `inert` rows and 4 `repealed or blank in this text` rows).
Pass 1 used reasons that the pass-2 brief withdraws ("no condition to compute", "a canon", "a cross-reference to another Act", "addresses an official"), so each row is re-derived from the text.
Reasons: 1 not operative; 2 machinery; 3 shown repealed or blank.

| pass-1 row | pass-1 reason | verdict | where it goes |
| --- | --- | --- | --- |
| s 6 Effect of private Acts | canon, no condition | moves to `encoded` | reading: a function over the kind of Act and whether the Act mentions the right |
| s 7 Enactment always speaking | canon | moves to `encoded` | reading: the day an enactment is read as of (7(1)); present tense applies as circumstances arise (7(2)) |
| s 8 Enactment remedial | canon | moves to `encoded` | reading: the construction to adopt among candidates, the open-textured judgment taken as an input |
| s 8.1 Section 35 and Declaration | canon; points at other Acts | moves to `encoded` | terms: the three defined terms of 8.1(1) with their own scope; reading: 8.1(2) and (3) |
| s 9 Title and preamble | canon | moves to `encoded` | reading |
| s 10 Enacting clause | drafting form | moves to `encoded`; a fork (F-open-list) | reading: the permitted wording, quoted from the text and compared as a string; s 10 is a rule about other Acts' enacting clauses, not the enacting words of this Act |
| s 11 Reference aids | canon; power of the LGiC | 11(1), (2) move to `encoded`; 11(3) keeps `inert`, reason 2 | 11(3) is a regulation-making power (machinery); reading carries (1) and (2) |
| s 12 Definitions and interpretation provisions | canon of scope | moves to `encoded` | reading |
| s 13 Expressions in regulations | canon | moves to `encoded` | reading |
| s 15 Power of repeal and amendment | statement of capacity | moves to `encoded` | reading: what the Legislature has reserved; it is the individual's exposure (Hohfeld: liability) |
| s 17 Corporate rights and powers | capacities | moves to `encoded` | powers: a function over the power and the corporation's facts |
| s 19 Powers to judges and court officers | capacity, procedure | moves to `encoded` | powers |
| s 21 Demise of Crown | savings rule | moves to `encoded` | powers |
| s 22 Included powers | what words include | moves to `encoded`; a fork (F-open-list) | powers: six listed powers, open list |
| s 23 Powers to act for ministers and public officers | what words include | moves to `encoded`; 23(2) a fork (F-adm) | powers |
| s 27 Ancillary powers | what a grant includes | all seven subsections move to `encoded` | powers; 27(4) concerns regulation-making powers in general and is a rule of reading, not the grant of a power, so it is not machinery |
| s 29.1 Treaty first nations definitions | points at other Acts | 29.1(1) moves to `encoded` (eight entries and their paragraphs); 29.1(2) `repealed`; 29.1(3), (4) keep `inert`, reason 2 | terms; 29.1(3) and (4) are regulation-making powers |
| s 29.2 Nisga'a definitions | cross-reference | moves to `encoded` | terms: ten entries, each pointing at the Agreement or its Act |
| s 30 Metric expressions | cross-reference | moves to `encoded` | reading: which source a metric expression takes its meaning from, in the order the text gives |
| s 31 Common names | canon | moves to `encoded` | reading |
| s 34 Amending enactment part of enactment amended | canon | moves to `encoded` | replacement |
| s 37 No implications from repeal | canon | moves to `encoded` | replacement: for each act and each inference, whether the inference may be drawn |
| s 39 Supreme Court Act definitions | cross-reference | moves to `encoded` | reading |
| s 40 Community Charter and Local Government Act definitions | cross-reference | moves to `encoded` | reading, with the exception of 40(2) tested on both sides |
| s 41 Powers to make regulations | what a grant includes | moves to `encoded` | powers: what a regulation-making power extends to; the penalty ceiling bears on the individual (41(1)(e), (f)) |
| s 43 Citation of Acts | citation | moves to `encoded`; a fork (F-open-list) | reading |
| s 44 Mutatis mutandis | canon | moves to `encoded` | reading |
| Schedule | boundary can be quoted, not computed | moves to `encoded` as data | terms: the legal description split into its legs, with a test of the count and the end points; the limit (no point-in-line test) is stated in the finding |
| 29.1(2) [Repealed 2011-11-42.] | 3 | keeps `repealed or blank in this text` | reason 3 |
| 29 "savings institution" (e) [Repealed 2004-23-21.] | 3 | keeps `repealed or blank in this text` | reason 3 |
| 36(1)(f) [Repealed 2018-5-6.] | 3 | keeps `repealed or blank in this text` | reason 3 |
| 36(2) [Repealed 2018-5-6.] | 3 | keeps `repealed or blank in this text` | reason 3 |

**Rows pass 1 marked `encoded` for part of a section, whose remainder it left inert.**
Each remainder is re-derived from the text and moves to `encoded` unless it is listed under "stays inert" below:

- s 1: "Act", "enact", "public officer", "repeal" (terms, with a rule for "Act"); s 2(2), (3); s 3(4); s 5(2); s 16(1), (3); s 20(1), (2), (5); s 25(1), (2); s 28(2), (3), (4); s 29 (88 entries, 14 cross-references and their paragraphs; pass 1 encoded eight of the terms: "commencement", "now", "month", "year", "holiday", "deliver", "mail", "minor"); s 33(2) to (6); s 36(1)(b), (c); s 42(1).
- s 29 "holiday" (a) to (d) beyond Sunday and 26 December: terms lists every named holiday; the dates stay an input of the time module because the text gives none.

**What stays `inert` after pass 2, with its reason.** Title lines and section headings (reason 1): 2 + 53 units. s 11(3), s 29.1(3), s 29.1(4) (reason 2: powers of the Lieutenant Governor in Council to make regulations). Nothing else.
**What stays `repealed or blank in this text`** (reason 3): s 29 "savings institution" (e), s 29.1(2), s 36(1)(f), s 36(2).

`fork` rows are in the coverage table (section 1); each names its fork in section 2.

## 1. Coverage table

One row per unit of the text, 416 rows, built by `python3 -I coverage.py ../../registers/source-bundle/RSBC-1996-c.-238.txt table` from the text (`units.py`), `coverage-dispositions.tsv` (the disposition and the note) and the `@ref` locators of the modules (the "where" column).
`python3 -I coverage.py ../../registers/source-bundle/RSBC-1996-c.-238.txt check` fails if any unit has no disposition or if an `encoded` or `fork` unit's line is cited by no `@ref` in a non-test module; it printed, for this table, no failure and these counts:

| disposition | units |
| --- | --- |
| encoded | 186 |
| fork | 168 |
| inert, reason 1 (not operative) | 55 |
| inert, reason 2 (machinery) | 3 |
| repealed or blank in this text (reason 3) | 4 |
| total | 416 |

Dispositions are `encoded`, `inert-1`, `inert-2`, `inert-3` (none: a repealed unit is `repealed`), `fork` and `repealed`; there is no `out-of-scope` and no `deferred`.
The "where" column is computed: it lists, most relevant first, the modules and rules whose `@ref` locator covers the unit's line, so it cannot name a rule that does not cite the unit.
A unit that a rule cites only as part of a longer block (a section's lead-in, a run of paragraphs) shows that rule.
Line numbers are lines of `RSBC-1996-c.-238.txt`.
A `fork` row names its fork in the note; the fork is in section 2 with every reading and the licensing text, and the rule that carries the chosen reading is in the "where" column.
For the entries of the catalogue the fork is decided by the verb and the `closed` flag of the entry (`coverage.py`, `resolve_auto`): "means and includes" is F-means-and-includes and F-open-list; "includes" is F-open-list; a "means" with a closed list is F-means-closed. A few rows carry a fork that the rule does not infer, named in the note (for example "affidavit or oath", F-affidavit).

| unit | line | disposition | where | note |
| --- | --- | --- | --- | --- |
| title line 5 | 5 | inert-1 |  | reason 1: the title and chapter lines of the Act |
| title line 6 | 6 | inert-1 |  | reason 1: the title and chapter lines of the Act |
| s 1 heading | 8 | inert-1 |  | reason 1: a section heading (not operative) |
| s 1 | 9 | encoded | `terms`: `Where a definition applies` | lead-in line: where the s 1 definitions apply |
| s 1 "Act" | 10 | fork | `terms`: `s 1 definition of Act`; `terms`: `s 1 an instrument is an Act` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 1 "enact" | 11 | fork | `terms`: `s 1 definition of enact` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 1 "enactment" | 12 | fork | `definitions`: `s 1 a thing is an enactment`; `terms`: `s 1 definition of enactment`; `time`: `s 3(5) does not say when a regulation of any other class that...` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 1 "public officer" | 13 | fork | `terms`: `s 1 definition of public officer`; `time`: `s 3(5) does not say when a regulation of any other class that...` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 1 "regulation" | 14 | fork | `definitions`: `s 1 an instrument is a regulation`; `terms`: `s 1 definition of regulation`; `time`: `s 3(5) does not say when a regulation of any other class that...` | F-rendering-order: the paragraphs (a) and (b) are printed after the semicolon; read as qualifying "enacted" |
| s 1 "regulation" (a) | 15 | fork | `definitions`: `s 1 an instrument is a regulation`; `terms`: `s 1 definition of regulation` | F-rendering-order, as for the entry |
| s 1 "regulation" (b) | 16 | fork | `definitions`: `s 1 an instrument is a regulation`; `terms`: `s 1 definition of regulation` | F-rendering-order, as for the entry |
| s 1 "repeal" | 17 | fork | `terms`: `s 1 definition of repeal` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 2 heading | 19 | inert-1 |  | reason 1: a section heading (not operative) |
| s 2(1) | 20 | fork | `definitions`: `s 2(1) a provision of this Act applies to an enactment` | F-contrary-intention: the caller says whether a contrary intention appears |
| s 2(2) | 21 | encoded | `reading`: `s 2(2) the provisions of this Act apply to the enactment`; `reading`: `s 2(2) speaks only of this Act; s 2(1) governs another enactment` | applies to this Act only; another enactment is a refusal that points at s 2(1) (finding 3) |
| s 2(3) | 22 | encoded | `reading`: `s 2(3) speaks only of a rule of construction that is applicab...`; `reading`: `s 2(3) a rule of construction is preserved by this Act` | applies AND NOT inconsistent |
| s 3 heading | 24 | inert-1 |  | reason 1: a section heading (not operative) |
| s 3(1) | 25 | fork | `time`: `s 3 does not say that the day an Act was passed or published ...`; `time`: `s 3(1) the date of assent to an Act` | F-assent: the date of assent, and the refusal for "passed or published" |
| s 3(2) | 26 | fork | `time`: `s 3 does not say that the day an Act was passed or published ...`; `time`: `s 3(2) the date of commencement of a portion of an Act`; `time`: `the moment from which a portion of an Act binds` | F-assent and F-fixed-later |
| s 3(3) | 27 | encoded | `time`: `s 3(2) the date of commencement of a portion of an Act`; `time`: `s 3(3) the day the commencement provision and the title of an...` |  |
| s 3(3.1) | 28 | fork | `time`: `s 3(3.1) a portion comes into force on a day earlier than the...` | F-retroactive: the day is returned; how far the retroactivity reaches is not computed |
| s 3(3.1)(a) | 29 | fork | `time`: `s 3(3.1) a portion comes into force on a day earlier than the...` | F-retroactive: the day is returned; how far the retroactivity reaches is not computed |
| s 3(3.1)(b) | 30 | fork | `time`: `s 3(3.1) a portion comes into force on a day earlier than the...` | F-retroactive: the day is returned; how far the retroactivity reaches is not computed |
| s 3(4) | 31 | encoded | `commencement`: `s 3(4) speaks only of the date of assent and the date of sign...`; `commencement`: `s 3(4) the date is part of the Act` | which dates are part of the Act |
| s 3(5) | 32 | fork | `time`: `s 3(5) does not say when a regulation of any other class that...`; `time`: `s 3(5) the day a regulation comes into force`; `time`: `the moment from which a regulation binds` | F-regulation-silent: a regulation of any other class that names no day is a refusal |
| s 4 heading | 34 | inert-1 |  | reason 1: a section heading (not operative) |
| s 4(1) | 35 | encoded | `time`: `s 4(1) the beginning of a day`; `time`: `the moment from which a portion of an Act binds`; `time`: `the moment from which a regulation binds` | the beginning of the day (F-moment: the text answers) |
| s 4(2) | 36 | fork | `time`: `s 4(2) the moment an enactment that is repealed and replaced ...` | F-cessation |
| s 4(3) | 37 | fork | `time`: `s 4(3) the end of a day`; `time`: `s 4(3) the moment any other enactment ceases to have effect` | F-cessation |
| s 4(4) | 38 | encoded | `repeal`: `s 4(4) speaks only of an enactment that has expired or otherw...`; `repeal`: `s 4(4) the enactment is deemed to be repealed for the purpose...` |  |
| s 5 heading | 40 | inert-1 |  | reason 1: a section heading (not operative) |
| s 5(1) | 41 | encoded | `definitions`: `s 5(1) a thing done before commencement has effect on a day` |  |
| s 5(2) | 42 | encoded | `commencement`: `s 5(2) speaks only of an enactment to come into force or be r...`; `commencement`: `s 5(2)(a) the proclamation or regulation may apply to the com...`; `commencement`: `s 5(2)(b) the proclamations or regulations may be issued at d...` | two functions, one for (a) and one for (b), over how the enactment comes into force |
| s 5(2)(a) | 43 | encoded | `commencement`: `s 5(2) speaks only of an enactment to come into force or be r...`; `commencement`: `s 5(2)(a) the proclamation or regulation may apply to the com...` | two functions, one for (a) and one for (b), over how the enactment comes into force |
| s 5(2)(b) | 44 | encoded | `commencement`: `s 5(2) speaks only of an enactment to come into force or be r...`; `commencement`: `s 5(2)(b) the proclamations or regulations may be issued at d...` | two functions, one for (a) and one for (b), over how the enactment comes into force |
| s 6 heading | 46 | inert-1 |  | reason 1: a section heading (not operative) |
| s 6 | 47 | encoded | `reading`: `s 6 speaks only of a provision in a private Act`; `reading`: `s 6 what a provision in an Act does to a person's right` | a function over the kind of Act; any other Act is a refusal |
| s 7 heading | 49 | inert-1 |  | reason 1: a section heading (not operative) |
| s 7(1) | 50 | fork | `reading`: `s 7(1) the day as of which an enactment is read` | F-always-speaking: the day as of which the enactment is read |
| s 7(2) | 51 | encoded | `reading`: `s 7(2) speaks only of a provision expressed in the present tense`; `reading`: `s 7(2) does not say whether a provision applies to a circumst...`; `reading`: `s 7(2) the provision applies to the circumstance as it arises` | a present-tense provision applies; a circumstance arising while the enactment is not in force is a refusal |
| s 8 heading | 53 | inert-1 |  | reason 1: a section heading (not operative) |
| s 8 | 54 | encoded | `reading`: `s 8 names no construction when none is said to best ensure th...`; `reading`: `s 8 does not choose between constructions that equally best e...`; `reading`: `s 8 the construction to give to an enactment` | the judgment of which construction best ensures the objects is an input (finding 5) |
| s 8.1 heading | 56 | inert-1 |  | reason 1: a section heading (not operative) |
| s 8.1(1) | 57 | encoded | `terms`: `Where a definition applies` | lead-in line: "In this section" |
| s 8.1(1) "Declaration" | 58 | encoded | `terms`: `s 8.1(1) definition of Declaration` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 8.1(1) "Indigenous peoples" | 59 | encoded | `terms`: `s 8.1(1) definition of Indigenous peoples` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 8.1(1) "regulation" | 60 | encoded | `terms`: `s 8.1(1) definition of regulation` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 8.1(2) | 61 | encoded | `reading`: `s 8.1(2) a construction of an enactment is open` |  |
| s 8.1(3) | 62 | encoded | `reading`: `s 8.1(3) speaks only of an Act and a regulation`; `reading`: `s 8.1(3) a construction of the enactment is open` |  |
| s 9 heading | 64 | inert-1 |  | reason 1: a section heading (not operative) |
| s 9 | 65 | encoded | `reading`: `s 9 speaks only of the title and the preamble`; `reading`: `s 9 the part is part of the enactment`; `reading`: `s 9 the part is intended to assist in explaining the meaning ...`; and 1 more |  |
| s 10 heading | 67 | inert-1 |  | reason 1: a section heading (not operative) |
| s 10 | 68 | fork | `reading`: `s 10 does not say that an enacting clause in another form is ...`; `reading`: `s 10 the enacting clause of an Act of the Legislature may be ...`; `reading`: `the form of enacting clause that s 10 gives` | F-open-list: "may be in the following form" does not forbid another form |
| s 11 heading | 70 | inert-1 |  | reason 1: a section heading (not operative) |
| s 11(1) | 71 | encoded | `reading`: `s 11(1) speaks only of a head note, a reference after the end...`; `reading`: `s 11(1)(a) the part is part of the enactment`; `reading`: `s 11(1)(b) the part must be considered to have been added edi...`; and 1 more |  |
| s 11(1)(a) | 72 | encoded | `reading`: `s 11(1) speaks only of a head note, a reference after the end...`; `reading`: `s 11(1)(a) the part is part of the enactment`; `reading`: `s 11(1)(b) the part must be considered to have been added edi...`; and 1 more |  |
| s 11(1)(b) | 73 | encoded | `reading`: `s 11(1)(b) the part must be considered to have been added edi...` |  |
| s 11(2) | 74 | encoded | `reading`: `s 11(2) speaks only of italicized text in square brackets, af...`; `reading`: `s 11(2) subsection (1)(a) and (b) apply to the text in square...` |  |
| s 11(3) | 75 | inert-2 |  | reason 2: a regulation-making power of the Lieutenant Governor in Council |
| s 12 heading | 77 | inert-1 |  | reason 1: a section heading (not operative) |
| s 12 | 78 | encoded | `reading`: `s 12 speaks only of the enactment that contains the definitio...`; `reading`: `s 12 the definition or interpretation provision applies in th...` |  |
| s 13 heading | 80 | inert-1 |  | reason 1: a section heading (not operative) |
| s 13 | 81 | encoded | `reading`: `s 13 the meaning of an expression used in a regulation` |  |
| s 14 heading | 83 | inert-1 |  | reason 1: a section heading (not operative) |
| s 14(1) | 84 | fork | `definitions`: `s 14 an enactment binds the government` | F-government |
| s 14(2) | 85 | fork | `definitions`: `s 14 an enactment binds the government` | F-government |
| s 15 heading | 87 | inert-1 |  | reason 1: a section heading (not operative) |
| s 15(1) | 88 | encoded | `reading`: `s 15(1) the Act is construed as reserving to the Legislature ...` |  |
| s 15(2) | 89 | encoded | `reading`: `s 15(2) speaks only of an Act passed in the same session of t...`; `reading`: `s 15(2) an Act may be amended or repealed by an Act passed in...` |  |
| s 16 heading | 91 | inert-1 |  | reason 1: a section heading (not operative) |
| s 16(1) | 92 | encoded | `commencement`: `s 16(1) speaks only of a proclamation`; `commencement`: `s 16(1) a proclamation must mention that it is issued under a...`; `time`: `s 16(2) does not say when a proclamation takes effect if it i...`; and 1 more |  |
| s 16(2) | 93 | fork | `time`: `s 16(2) does not say when a proclamation takes effect if it i...`; `time`: `s 16(2) the day a proclamation takes effect` | F-proclamation |
| s 16(3) | 94 | encoded | `commencement`: `s 16(3) speaks only of an enactment expressed to come into fo...`; `commencement`: `s 16(3) judicial notice must be taken of the issue of the pro...`; `commencement`: `s 16(3) the issue of the proclamation must be specially pleaded` |  |
| s 17 heading | 96 | inert-1 |  | reason 1: a section heading (not operative) |
| s 17(1) | 97 | fork | `powers`: `s 17(1) a corporation has perpetual succession`; `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(1)(a) | 98 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(1)(b) | 99 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(1)(c) | 100 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(1)(d) | 101 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list, and F-limit-or-scope: "other than land" marks the edge of paragraph (d); land is a refusal, not FALSE |
| s 17(1)(e) | 102 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(1)(f) | 103 | fork | `powers`: `s 17(1) lists what a corporation may do and does not say it m...`; `powers`: `s 17(1) a corporation may do the thing` | F-open-list: "may do the following" lists what a corporation may do |
| s 17(2) | 104 | fork | `powers`: `s 17(2) says what a majority of the members may do and does n...`; `powers`: `s 17(2) is not given a number acting that is more than the nu...`; `powers`: `s 17(2) the members who act may bind the others and the corpo...` | F-majority: more than half; exactly half or fewer is a refusal |
| s 17(3) | 105 | fork | `powers`: `s 17(3) speaks only of a member who does not contravene the e...`; `powers`: `s 17(3) the member is exempt from personal liability for the ...` | F-established: whether a corporation incorporated under a general statute is "established by an enactment" is an input, not decided |
| s 18 heading | 107 | inert-1 |  | reason 1: a section heading (not operative) |
| s 18(1) | 108 | encoded | `definitions`: `s 18(1) a majority of the persons may do the act`; `definitions`: `s 18(1) applies only where more than 2 persons are to do the act`; `definitions`: `s 18(1) says what a majority of them may do and does not say ...` |  |
| s 18(2) | 109 | encoded | `definitions`: `s 18(2) applies only to a body of 3 or more members`; `definitions`: `s 18(2) the threshold of one half, before it is rounded up to...`; `definitions`: `s 18(2) the number the members present must reach to constitu...` |  |
| s 18(2)(a) | 110 | encoded | `definitions`: `s 18(2) the threshold of one half, before it is rounded up to...`; `definitions`: `s 18(2) the number the members present must reach to constitu...` |  |
| s 18(2)(b) | 111 | encoded | `definitions`: `s 18(2)(b) does not say what constitutes a quorum when the nu...`; `definitions`: `s 18(2) the threshold of one half, before it is rounded up to...`; `definitions`: `s 18(2) the number the members present must reach to constitu...` |  |
| s 18(2)(c) | 112 | encoded | `definitions`: `s 18(2)(c) speaks only of an act or thing done at a meeting a...`; `definitions`: `s 18(2)(c) says what a majority of the members present may do...`; `definitions`: `s 18(2)(c) the act is deemed to have been done by the associa...` |  |
| s 18(2)(d) | 113 | encoded | `definitions`: `s 18(2)(d) speaks only of a vacancy where the number of membe...`; `definitions`: `s 18(2)(d) a vacancy does not impair the right of the members...` |  |
| s 19 heading | 115 | inert-1 |  | reason 1: a section heading (not operative) |
| s 19(1) | 116 | encoded | `powers`: `s 19(1) speaks only of judicial or quasi judicial powers give...`; `powers`: `s 19(1) the holder exercises the power in the holder's offici...` |  |
| s 19(2) | 117 | encoded | `powers`: `s 19(2) speaks only of an appeal given under an enactment fro...`; `powers`: `s 19(2) an appeal lies from the decision of the court or judg...` |  |
| s 20 heading | 119 | inert-1 |  | reason 1: a section heading (not operative) |
| s 20(1) | 120 | encoded | `commencement`: `s 20(1) an instrument is an appointing instrument` |  |
| s 20(2) | 121 | fork | `commencement`: `s 20(2) speaks only of an authority under an enactment to app...`; `commencement`: `s 20(2) names appointment during pleasure and does not say th...`; `commencement`: `s 20(2) does not say what an appointment during pleasure allo...`; and 1 more | F-pleasure |
| s 20(3) | 122 | encoded | `time`: `s 20(3) the moment an appointment begins` |  |
| s 20(4) | 123 | encoded | `time`: `s 20(4) the moment an appointment ends` |  |
| s 20(4)(a) | 124 | encoded | `time`: `s 20(4) the moment an appointment ends` |  |
| s 20(4)(b) | 125 | encoded | `time`: `s 20(4) the moment an appointment ends` |  |
| s 20(4)(c) | 126 | encoded | `time`: `s 20(4) the moment an appointment ends` |  |
| s 20(4)(d) | 127 | encoded | `time`: `s 20(4) the moment an appointment ends` |  |
| s 20(4)(e) | 128 | fork | `time`: `s 20(4) the moment an appointment ends` | F-appointment: when a resignation takes effect is not covered |
| s 20(5) | 129 | encoded | `commencement`: `s 20(5) says where section 4 does not apply and does not say ...`; `commencement`: `s 20(5) section 4 applies to the instrument or enactment` |  |
| s 21 heading | 131 | inert-1 |  | reason 1: a section heading (not operative) |
| s 21 | 132 | encoded | `powers`: `s 21 speaks only of a person who held or exercised an office ...`; `powers`: `s 21 the commission or appointment must be renewed`; `powers`: `s 21 the person continues in the duties and functions of the ...`; and 1 more |  |
| s 22 heading | 134 | inert-1 |  | reason 1: a section heading (not operative) |
| s 22 | 135 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(a) | 136 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(b) | 137 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(c) | 138 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(d) | 139 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(e) | 140 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 22(f) | 141 | fork | `powers`: `s 22 speaks only of words in an enactment authorizing the app...`; `powers`: `s 22 lists the powers such words include and does not say the...`; `powers`: `s 22 words authorizing the appointment of a public officer in...` | F-open-list: "include" lists powers that words authorizing an appointment include |
| s 23 heading | 143 | inert-1 |  | reason 1: a section heading (not operative) |
| s 23(1) | 144 | fork | `powers`: `s 23(1) lists whom words naming a minister include and does n...`; `powers`: `s 23(1) the words naming a minister include` | F-open-list: "include" lists whom the words naming a minister include |
| s 23(2) | 145 | fork | `powers`: `s 23(2) speaks only of a deputy minister who is absent or una...`; `powers`: `s 23(2) names an assistant deputy minister or an official aut...`; `powers`: `s 23(2) the official has the powers and must perform the duti...` | F-adm: whether "authorized by the minister" qualifies the assistant deputy minister |
| s 23(3) | 146 | fork | `powers`: `s 23(3) lists whom words naming a public officer include and ...`; `powers`: `s 23(3) the words naming a public officer include` | F-open-list |
| s 23(4) | 147 | encoded | `powers`: `s 23(4) section 23 applies` |  |
| s 23(5) | 148 | encoded | `powers`: `s 23(1) the words naming a minister include` | folded into the s 23(1) function as an input |
| s 24 heading | 150 | inert-1 |  | reason 1: a section heading (not operative) |
| s 24 | 151 | fork | `definitions`: `s 24 speaks only of an enactment that provides that a documen...`; `definitions`: `s 24 does not say what follows where the context indicates th...`; `definitions`: `s 24 the document is admissible in evidence in any proceeding`; and 1 more | F-limit-or-scope: "unless the context indicates that the document is conclusive evidence" marks the edge of the rule; a case outside it is a refusal, not FALSE |
| s 25 heading | 153 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25(1) | 154 | fork | `periods`: `s 25(1) defines reference day for sections 25.2 to 25.4 only`; `periods`: `s 25(1) names three kinds of reference day and no others`; `periods`: `s 25(1) a thing a period is counted from is a reference day`; and 1 more | F-means-closed: "reference day means any of the following" |
| s 25(1)(a) | 155 | fork | `periods`: `s 25(1) names three kinds of reference day and no others`; `periods`: `s 25(1) a thing a period is counted from is a reference day`; `periods`: `s 25(1) the reference day` | F-means-closed: "reference day means any of the following" |
| s 25(1)(b) | 156 | fork | `periods`: `s 25(1) names three kinds of reference day and no others`; `periods`: `s 25(1) a thing a period is counted from is a reference day`; `periods`: `s 25(1) the reference day` | F-means-closed: "reference day means any of the following" |
| s 25(1)(c) | 157 | fork | `periods`: `s 25(1) names three kinds of reference day and no others`; `periods`: `s 25(1) a thing a period is counted from is a reference day`; `periods`: `s 25(1) the reference day` | F-means-closed: "reference day means any of the following" |
| s 25(2) | 158 | encoded | `periods`: `s 25(2) speaks only of a deed, conveyance or other legal inst...`; `periods`: `s 25(2) section 25 and sections 25.1 to 25.5 apply to the doc...` |  |
| s 25(3) | 159 | fork | `time`: `the holiday calendar supplied has no day free of holidays wit...`; `time`: `walk forward from a day to the first day that is not a holiday`; `time`: `s 25(3) the beginning or end of a period for doing an act, mo...`; and 1 more | F-holiday-scope, F-near-end and F-consecutive |
| s 25(3)(a) | 160 | fork | `time`: `the holiday calendar supplied has no day free of holidays wit...`; `time`: `walk forward from a day to the first day that is not a holiday`; `time`: `s 25(3) the beginning or end of a period for doing an act, mo...`; and 1 more | F-holiday-scope, F-near-end and F-consecutive |
| s 25(3)(b) | 161 | fork | `time`: `the holiday calendar supplied has no day free of holidays wit...`; `time`: `walk forward from a day to the first day that is not a holiday`; `time`: `walk backward from a day to the first day that is not a holiday`; and 2 more | F-holiday-scope, F-near-end and F-consecutive |
| s 25(4) | 162 | fork | `time`: `the office calendar supplied has no open day within a year`; `time`: `s 25(4) the beginning or end of a period for doing an act in ...` | F-office |
| s 25(4)(a) | 163 | fork | `time`: `the office calendar supplied has no open day within a year`; `time`: `walk forward from a day to the first day the office is open`; `time`: `s 25(4) the beginning or end of a period for doing an act in ...` | F-office |
| s 25(4)(b) | 164 | fork | `time`: `the office calendar supplied has no open day within a year`; `time`: `walk backward from a day to the first day the office is open`; `time`: `s 25(4) the beginning or end of a period for doing an act in ...` | F-office |
| s 25(4)(b)(i) | 165 | fork | `time`: `the office calendar supplied has no open day within a year`; `time`: `walk backward from a day to the first day the office is open`; `time`: `s 25(4) the beginning or end of a period for doing an act in ...` | F-office |
| s 25(4)(b)(ii) | 166 | fork | `time`: `the office calendar supplied has no open day within a year`; `time`: `walk backward from a day to the first day the office is open`; `time`: `s 25(4) the beginning or end of a period for doing an act in ...` | F-office |
| s 25.1 heading | 168 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25.1 | 169 | fork | `time`: `s 25.1 does not say which day is the anniversary of a birth o...`; `time`: `s 25.1 the day a person reaches an age expressed in years`; `time`: `s 25.1 a person has reached an age on a day` | F-age: a birth on 29 February in a year without one is a refusal |
| s 25.2 heading | 171 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25.2(1) | 172 | encoded | `time`: `s 25.2(1) the number of days in a week` |  |
| s 25.2(2) | 173 | fork | `time`: `s 25.2 beginning or end of a period of days`; `time`: `ss 25.2 to 25.4 count a whole number of one or more days, wee...`; `time`: `the beginning or end of a period`; and 1 more | F-count, F-position and F-whole |
| s 25.2(2)(a) | 174 | fork | `time`: `s 25.2 beginning or end of a period of days`; `time`: `the span of days of a period counted from a reference day` | F-count, F-position and F-whole |
| s 25.2(2)(b) | 175 | fork | `time`: `s 25.2 beginning or end of a period of days`; `time`: `the span of days of a period counted from a reference day` | F-count, F-position and F-whole |
| s 25.2(3) | 176 | fork | `time`: `s 25.2 beginning or end of a period of days` | F-clear, and F-clear-ends: which end "is one day later" |
| s 25.2(3)(a) | 177 | fork | `time`: `s 25.2 beginning or end of a period of days` | F-clear, and F-clear-ends: which end "is one day later" |
| s 25.2(3)(b) | 178 | fork | `time`: `s 25.2 beginning or end of a period of days` | F-clear, and F-clear-ends: which end "is one day later" |
| s 25.3 heading | 180 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25.3(1) | 181 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months`; `time`: `ss 25.2 to 25.4 count a whole number of one or more days, wee...`; and 1 more | F-month, F-position, F-unit and F-whole |
| s 25.3(1)(a) | 182 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-month, F-position, F-unit and F-whole |
| s 25.3(1)(b) | 183 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-month, F-position, F-unit and F-whole |
| s 25.3(2) | 184 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-clear |
| s 25.3(2)(a) | 185 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-clear |
| s 25.3(2)(b) | 186 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-clear |
| s 25.3(3) | 187 | fork | `time`: `s 25.3 does not say how to shift a clear month by a day when ...`; `time`: `s 25.3 beginning or end of a period of months` | F-start-day, and F-clear: whether the last-day rule is applied to the result of (1) and (2) together or to (1) alone |
| s 25.4 heading | 189 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25.4(1) | 190 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years`; `time`: `ss 25.2 to 25.4 count a whole number of one or more days, wee...`; and 1 more | F-unit and F-whole: calendar years, and a count that is not a whole number is a refusal |
| s 25.4(1)(a) | 191 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-unit and F-whole: calendar years, and a count that is not a whole number is a refusal |
| s 25.4(1)(b) | 192 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-unit and F-whole: calendar years, and a count that is not a whole number is a refusal |
| s 25.4(2) | 193 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-clear |
| s 25.4(2)(a) | 194 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-clear |
| s 25.4(2)(b) | 195 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-clear |
| s 25.4(3) | 196 | fork | `time`: `s 25.4 does not say how to shift a clear year by a day when t...`; `time`: `s 25.4 beginning or end of a period of years` | F-start-day, and F-clear: whether the 29 February rule is applied to the result of (1) and (2) together or to (1) alone |
| s 25.5 heading | 198 | inert-1 |  | reason 1: a section heading (not operative) |
| s 25.5(1) | 199 | encoded | `time`: `s 25.5(1) a day specified for doing an act, moved off a holiday` |  |
| s 25.5(2) | 200 | encoded | `time`: `s 25.5(2) a day specified for doing an act in a business offi...` |  |
| s 26 heading | 202 | inert-1 |  | reason 1: a section heading (not operative) |
| s 26(1) | 203 | fork | `time`: `s 26 the UTC moment of a Pacific Time moment`; `time`: `s 26(1) the number of hours Pacific Time is behind UTC`; `time`: `the moment from which a portion of an Act binds`; and 1 more | F-offset: 7 hours all year |
| s 26(2) | 204 | encoded | `time`: `s 26 the UTC moment of a Pacific Time moment`; `time`: `s 26(1) the number of hours Pacific Time is behind UTC`; `time`: `the moment from which a portion of an Act binds`; and 1 more |  |
| s 27 heading | 206 | inert-1 |  | reason 1: a section heading (not operative) |
| s 27(1) | 207 | encoded | `powers`: `s 27(1) speaks only of a thing that an enactment requires or ...`; `powers`: `s 27(1) the thing may be done by or before the official` |  |
| s 27(2) | 208 | encoded | `powers`: `s 27(2) speaks only of the powers necessary to enable the per...`; `powers`: `s 27(2) the power is deemed to be given` |  |
| s 27(3) | 209 | encoded | `powers`: `s 27(3) speaks only of a power conferred or a duty imposed`; `powers`: `s 27(3) when a power may be exercised or a duty must be perfo...` |  |
| s 27(4) | 210 | fork | `powers`: `s 27(4) speaks only of an enactment that confers a power to m...`; `powers`: `s 27(4) lists what a power to make regulations includes and d...`; `powers`: `s 27(4) a power to make regulations includes the power`; and 1 more | F-open-list: "includes a power ... to repeal or amend the regulations and make others" |
| s 27(5) | 211 | encoded | `powers`: `s 27(5) speaks only of an act of the Lieutenant Governor in C...`; `powers`: `s 27(5) the one who must do the other act has the power to do it` |  |
| s 27(6) | 212 | fork | `powers`: `s 27(6) speaks only of the person given the power to enter in...`; `powers`: `s 27(6) the person may enter into the agreement and carry out...` | F-open-list: "includes the power for the person with whom the agreement is to be made" |
| s 27(7) | 213 | fork | `powers`: `s 27(7) speaks only of a power to inspect or to require the p...`; `powers`: `s 27(7) lists what such a power includes and does not say it ...`; `powers`: `s 27(7) the power to inspect or require the production of rec...` | F-open-list |
| s 28 heading | 215 | inert-1 |  | reason 1: a section heading (not operative) |
| s 28(1) | 216 | encoded | `definitions`: `s 28(1) speaks only of a form prescribed under an enactment`; `definitions`: `s 28(1) does not say what follows for a deviation that affect...`; `definitions`: `s 28(1) the deviation does not invalidate the form used` |  |
| s 28(2) | 217 | fork | `reading`: `s 28(2) speaks only of persons of any gender and corporations`; `reading`: `s 28(2) a gender specific term includes` | F-open-list: "include all genders and include corporations" |
| s 28(3) | 218 | encoded | `reading`: `s 28(3) a word in one number includes the other number` |  |
| s 28(4) | 219 | encoded | `reading`: `s 28(4) speaks only of another part of speech or grammatical ...`; `reading`: `s 28(4) the form has a corresponding meaning` |  |
| s 29 heading | 221 | inert-1 |  | reason 1: a section heading (not operative) |
| s 29 | 222 | encoded | `terms`: `s 29 cross-reference from calendar year`; `terms`: `s 29 cross-reference from Canada`; `terms`: `s 29 cross-reference from chartered bank`; and 11 more | lead-in line of s 29 |
| s 29 see calendar year | 222 | encoded | `terms`: `s 29 cross-reference from calendar year` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Canada | 222 | encoded | `terms`: `s 29 cross-reference from Canada` | a cross-reference entry: its own rule in the catalogue |
| s 29 see chartered bank | 222 | encoded | `terms`: `s 29 cross-reference from chartered bank` | a cross-reference entry: its own rule in the catalogue |
| s 29 see civil engineer | 222 | encoded | `terms`: `s 29 cross-reference from civil engineer` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Crown, the | 222 | encoded | `terms`: `s 29 cross-reference from Crown, the` | a cross-reference entry: its own rule in the catalogue |
| s 29 see King, the | 222 | encoded | `terms`: `s 29 cross-reference from King, the` | a cross-reference entry: its own rule in the catalogue |
| s 29 see mining engineer | 222 | encoded | `terms`: `s 29 cross-reference from mining engineer` | a cross-reference entry: its own rule in the catalogue |
| s 29 see oath | 222 | encoded | `terms`: `s 29 cross-reference from oath` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Queen, the | 222 | encoded | `terms`: `s 29 cross-reference from Queen, the` | a cross-reference entry: its own rule in the catalogue |
| s 29 see solicitor | 222 | encoded | `terms`: `s 29 cross-reference from solicitor` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Sovereign, the | 222 | encoded | `terms`: `s 29 cross-reference from Sovereign, the` | a cross-reference entry: its own rule in the catalogue |
| s 29 see swear | 222 | encoded | `terms`: `s 29 cross-reference from swear` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Treasurer | 222 | encoded | `terms`: `s 29 cross-reference from Treasurer` | a cross-reference entry: its own rule in the catalogue |
| s 29 see Treasury | 222 | encoded | `terms`: `s 29 cross-reference from Treasury` | a cross-reference entry: its own rule in the catalogue |
| s 29 "acquire" | 223 | fork | `terms`: `s 29 definition of acquire` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "affidavit or oath" | 224 | fork | `terms`: `s 29 definition of affidavit`; `terms`: `s 29 definition of swear` | F-affidavit and F-open-list: "made under the Evidence Act" is read as qualifying the solemn declaration only |
| s 29 "bank or chartered bank" | 225 | encoded | `terms`: `s 29 definition of bank` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "barrister or solicitor or barrister and solicitor" | 226 | encoded | `terms`: `s 29 definition of barrister` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "British Columbia land surveyor" | 227 | encoded | `terms`: `s 29 definition of British Columbia land surveyor` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Cascade Mountains" | 228 | encoded | `terms`: `s 29 definition of Cascade Mountains` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "commencement, with reference to an enactment" | 229 | encoded | `terms`: `s 29 definition of commencement`; `time`: `s 29 the commencement of an enactment` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "commercial paper" | 230 | fork | `terms`: `s 29 definition of commercial paper` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "consolidated revenue fund, consolidated revenue or consolidated revenue fund of the Province" | 231 | encoded | `terms`: `s 29 definition of consolidated revenue fund` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "corporation" | 232 | fork | `terms`: `s 29 definition of corporation`; `terms`: `s 29 a body is a corporation` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "correctional centre" | 233 | encoded | `terms`: `s 29 definition of correctional centre` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "county" | 234 | encoded | `terms`: `s 29 definition of county` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Court of Appeal" | 235 | encoded | `terms`: `s 29 definition of Court of Appeal` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "credit union" | 236 | encoded | `terms`: `s 29 definition of credit union` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Criminal Code" | 237 | encoded | `terms`: `s 29 definition of Criminal Code` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "deliver, with reference to a notice or other document" | 238 | fork | `definitions`: `s 29 the day a notice or other document is delivered`; `terms`: `s 29 definition of deliver` | F-deemed-service: when a mailed document is received is a refusal; "deliver includes mail" and "mail includes deliver" point at each other, and no rule follows the pointer |
| s 29 "Deputy Provincial Secretary" | 239 | fork | `terms`: `s 29 definition of Deputy Provincial Secretary` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "dispose" | 240 | fork | `terms`: `s 29 definition of dispose` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "electoral district" | 241 | encoded | `terms`: `s 29 definition of electoral district` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Executive Council" | 242 | encoded | `terms`: `s 29 definition of Executive Council` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Gazette" | 243 | encoded | `terms`: `s 29 definition of Gazette` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "government or government of British Columbia" | 244 | encoded | `terms`: `s 29 definition of government` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "government agent" | 245 | encoded | `terms`: `s 29 definition of government agent` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "government of Canada or Canada" | 246 | fork | `terms`: `s 29 definition of government of Canada` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "Governor, Governor of Canada or Governor General" | 247 | fork | `terms`: `s 29 definition of Governor` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Governor in Council or Governor General in Council" | 248 | fork | `terms`: `s 29 definition of Governor in Council` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "Great Seal" | 249 | encoded | `terms`: `s 29 definition of Great Seal` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Her Majesty, His Majesty, the Queen, the King, the Crown or the Sovereign" | 250 | encoded | `terms`: `s 29 definition of Her Majesty` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "herein used in a section or part of an enactment" | 251 | encoded | `terms`: `s 29 definition of herein`; `terms`: `s 29 what the word herein refers to` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "holiday" | 252 | fork | `terms`: `s 29 definition of holiday`; `time`: `s 29 a day is a holiday` | F-saturday and F-open-list: dates the text gives are Sunday and 26 December only |
| s 29 "holiday" (a) | 253 | fork | `terms`: `s 29 definition of holiday`; `time`: `s 29 a day is a holiday` | F-saturday |
| s 29 "holiday" (b) | 254 | fork | `terms`: `s 29 definition of holiday`; `time`: `s 29 a day is a holiday` | F-saturday |
| s 29 "holiday" (c) | 255 | fork | `terms`: `s 29 definition of holiday`; `time`: `s 29 a day is a holiday` | F-saturday |
| s 29 "holiday" (d) | 256 | fork | `terms`: `s 29 definition of holiday`; `time`: `s 29 a day is a holiday` | F-saturday |
| s 29 "insurance company" | 257 | fork | `terms`: `s 29 definition of insurance company` | F-rendering-order: the paragraphs (a) and (b) are printed after the semicolon |
| s 29 "insurance company" (a) | 258 | fork | `terms`: `s 29 definition of insurance company` | F-rendering-order |
| s 29 "insurance company" (b) | 259 | fork | `terms`: `s 29 definition of insurance company` | F-rendering-order |
| s 29 "judicial district" | 260 | encoded | `terms`: `s 29 definition of judicial district` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "justice" | 261 | fork | `terms`: `s 29 definition of justice` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "land" | 262 | fork | `terms`: `s 29 definition of land` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "land title legislation, prior to October 31, 1979" | 263 | fork | `terms`: `s 29 definition of land title legislation`; `terms`: `s 29 the land title legislation on a day` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "lawyer" | 264 | encoded | `terms`: `s 29 definition of lawyer` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Legislative Assembly" | 265 | encoded | `terms`: `s 29 definition of Legislative Assembly` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Legislature" | 266 | encoded | `terms`: `s 29 definition of Legislature` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Lieutenant Governor" | 267 | fork | `terms`: `s 29 definition of Lieutenant Governor` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Lieutenant Governor in Council" | 268 | fork | `terms`: `s 29 definition of Lieutenant Governor in Council` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "mail" | 269 | fork | `definitions`: `s 29 does not make a deposit that is outside Canada or withou...`; `definitions`: `s 29 does not say when a mailed notice or other document is r...`; `terms`: `s 29 definition of mail`; and 1 more | F-deemed-service, F-means-and-includes and F-open-list |
| s 29 "may" | 270 | encoded | `terms`: `s 29 definition of may`; `terms`: `s 29 how may, must and shall are construed` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "medical practitioner" | 271 | encoded | `terms`: `s 29 definition of medical practitioner` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "mentally disordered person, mentally incompetent person, mentally ill person or person with a mental disorder" | 272 | encoded | `terms`: `s 29 definition of mentally disordered person` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "minister" | 273 | encoded | `terms`: `s 29 definition of minister` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "minor" | 274 | encoded | `definitions`: `s 29 a person is a minor`; `terms`: `s 29 definition of minor` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "month" | 275 | fork | `terms`: `s 29 definition of month`; `time`: `s 29 month: the following month has no day numerically corres...`; `time`: `s 29 the day on which the month following a month that begins...`; and 1 more | F-month-def |
| s 29 "municipality" | 276 | fork | `terms`: `s 29 definition of municipality` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "municipality" (a) | 277 | fork | `terms`: `s 29 definition of municipality` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "municipality" (b) | 278 | fork | `terms`: `s 29 definition of municipality` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "must" | 279 | encoded | `terms`: `s 29 definition of must`; `terms`: `s 29 how may, must and shall are construed` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "newspaper, in a provision requiring publication in a newspaper" | 280 | encoded | `terms`: `s 29 definition of newspaper`; `terms`: `s 29 newspaper is defined only in a provision requiring publi...`; `terms`: `s 29 a publication is a newspaper` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "now" | 281 | encoded | `terms`: `s 29 definition of now`; `time`: `s 29 the time that the word now refers to` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "nurse practitioner" | 282 | encoded | `terms`: `s 29 definition of nurse practitioner` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "obligation" | 283 | fork | `terms`: `s 29 definition of obligation` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "peace officer" | 284 | fork | `terms`: `s 29 definition of peace officer` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "peace officer" (a) | 285 | fork | `terms`: `s 29 definition of peace officer` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "peace officer" (b) | 286 | fork | `terms`: `s 29 definition of peace officer` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "peace officer" (c) | 287 | fork | `terms`: `s 29 definition of peace officer` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "person" | 288 | fork | `terms`: `s 29 definition of person` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "personal representative" | 289 | fork | `terms`: `s 29 definition of personal representative` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "prescribed" | 290 | encoded | `terms`: `s 29 definition of prescribed`; `terms`: `s 29 a thing is prescribed` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "proclamation" | 291 | encoded | `terms`: `s 29 definition of proclamation`; `terms`: `s 29 an instrument is a proclamation` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "professional engineer, civil engineer or mining engineer or words implying recognition of any person as a professional engineer or member of the engineering profession" | 292 | encoded | `terms`: `s 29 definition of professional engineer` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "property" | 293 | fork | `terms`: `s 29 definition of property` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Province" | 294 | fork | `terms`: `s 29 definition of Province` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "province, when used as meaning a part of Canada" | 295 | fork | `terms`: `s 29 definition of province` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Provincial Court" | 296 | encoded | `terms`: `s 29 definition of Provincial Court` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Provincial Treasurer or Treasurer" | 297 | fork | `terms`: `s 29 definition of Provincial Treasurer` | F-means-and-includes and F-open-list: the verb is "means and includes", read as open, so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Provincial Treasury or Treasury" | 298 | encoded | `terms`: `s 29 definition of Provincial Treasury` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Railway Belt" | 299 | encoded | `terms`: `s 29 definition of Railway Belt` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "record" | 300 | fork | `terms`: `s 29 definition of record` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "regional district" | 301 | encoded | `terms`: `s 29 definition of regional district` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "registered mail" | 302 | fork | `terms`: `s 29 definition of registered mail` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "registrar of a court" | 303 | fork | `terms`: `s 29 definition of registrar of a court` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Registrar of Companies" | 304 | encoded | `terms`: `s 29 definition of Registrar of Companies` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Registrar of Titles or registrar" | 305 | encoded | `terms`: `s 29 definition of Registrar of Titles` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "right" | 306 | fork | `terms`: `s 29 definition of right` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "Rules of Court, when used in relation to a court" | 307 | fork | `terms`: `s 29 definition of Rules of Court` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "Rules of Court, when used in relation to a court" (a) | 308 | fork | `terms`: `s 29 definition of Rules of Court` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "Rules of Court, when used in relation to a court" (b) | 309 | fork | `terms`: `s 29 definition of Rules of Court` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "rural area" | 310 | encoded | `terms`: `s 29 definition of rural area`; `terms`: `s 29 territory is a rural area` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "savings institution" | 311 | fork | `terms`: `s 29 definition of savings institution` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "savings institution" (a) | 312 | fork | `terms`: `s 29 definition of savings institution` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "savings institution" (b) | 313 | fork | `terms`: `s 29 definition of savings institution` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "savings institution" (c) | 314 | fork | `terms`: `s 29 definition of savings institution` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "savings institution" (d) | 315 | fork | `terms`: `s 29 definition of savings institution` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "savings institution" (e) | 316 | repealed |  | reason 3: shown as "[Repealed 2004-23-21.]" |
| s 29 "school district" | 317 | encoded | `terms`: `s 29 definition of school district` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "security" | 318 | fork | `terms`: `s 29 definition of security` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "shall" | 319 | encoded | `terms`: `s 29 definition of shall`; `terms`: `s 29 how may, must and shall are construed` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Supreme Court" | 320 | encoded | `terms`: `s 29 definition of Supreme Court` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "sureties" | 321 | encoded | `terms`: `s 29 definition of sureties`; `terms`: `s 29 the number of persons sufficient as sureties or as security` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "Surveyor General or Surveyor General of British Columbia" | 322 | encoded | `terms`: `s 29 definition of Surveyor General` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "trust company" | 323 | fork | `terms`: `s 29 definition of trust company` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "trust company" (a) | 324 | fork | `terms`: `s 29 definition of trust company` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "trust company" (b) | 325 | fork | `terms`: `s 29 definition of trust company` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29 "will" | 326 | encoded | `terms`: `s 29 definition of will` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29 "words" | 327 | fork | `terms`: `s 29 definition of words` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "writing, written, or a term of similar import" | 328 | fork | `terms`: `s 29 definition of writing` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 29 "year" | 329 | fork | `terms`: `s 29 definition of year`; `terms`: `s 29 definition of calendar year`; `terms`: `s 29 definition of dominical year`; and 3 more | F-month-def |
| s 29 "youth custody centre" | 330 | encoded | `terms`: `s 29 definition of youth custody centre` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1 heading | 332 | inert-1 |  | reason 1: a section heading (not operative) |
| s 29.1(1) | 333 | encoded | `terms`: `Where a definition applies` | lead-in line: "Insofar as they can be applied ... in all enactments relating to treaty first nation matters" |
| s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" | 334 | fork | `terms`: `s 29.1(1) definition of final agreement` | F-rendering-order: the paragraphs (a) and (b) are printed after the semicolon |
| s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" (a) | 335 | fork | `terms`: `s 29.1(1) definition of final agreement` | F-rendering-order |
| s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" (b) | 336 | fork | `terms`: `s 29.1(1) definition of final agreement` | F-rendering-order |
| s 29.1(1) "settlement legislation" | 337 | encoded | `terms`: `s 29.1(1) definition of settlement legislation` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1(1) "tax treatment agreement" | 338 | encoded | `terms`: `s 29.1(1) definition of tax treatment agreement` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1(1) "treaty first nation, as the context requires" | 339 | fork | `terms`: `s 29.1(1) definition of treaty first nation` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation, as the context requires" (a) | 340 | fork | `terms`: `s 29.1(1) definition of treaty first nation` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation, as the context requires" (b) | 341 | fork | `terms`: `s 29.1(1) definition of treaty first nation` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation child" | 342 | fork | `terms`: `s 29.1(1) definition of treaty first nation child` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation child" (a) | 343 | fork | `terms`: `s 29.1(1) definition of treaty first nation child` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation child" (b) | 344 | fork | `terms`: `s 29.1(1) definition of treaty first nation child` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 29.1(1) "treaty first nation constituent, in relation to a treaty first nation" | 345 | encoded | `terms`: `s 29.1(1) definition of treaty first nation constituent` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1(1) "treaty first nation member, in relation to a treaty first nation" | 346 | encoded | `terms`: `s 29.1(1) definition of treaty first nation member` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1(1) "treaty lands, in relation to a treaty fi" | 347 | encoded | `terms`: `s 29.1(1) definition of treaty lands` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.1(2) | 348 | repealed |  | reason 3: shown as "[Repealed 2011-11-42.]" |
| s 29.1(3) | 349 | inert-2 |  | reason 2: a regulation-making power of the Lieutenant Governor in Council |
| s 29.1(4) | 350 | inert-2 |  | reason 2: a regulation-making power of the Lieutenant Governor in Council |
| s 29.2 heading | 352 | inert-1 |  | reason 1: a section heading (not operative) |
| s 29.2(1) | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; `terms`: `s 29.2(1) definition of Nisg̱a'a Government`; and 6 more | lead-in line of s 29.2(1) |
| s 29.2(1) Nisg̱a'a child | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; `terms`: `s 29.2(1) definition of Nisg̱a'a Government`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a citizen | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a Government`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Government | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Government`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Lands | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Lands`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a laws | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a laws`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Lisims Government | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Lisims Government`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Nation | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Nation`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Village | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Village`; `terms`: `s 29.2(1) definition of Nisg̱a'a Village Government`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(1) Nisg̱a'a Village Government | 353 | encoded | `terms`: `s 29.2(1) definition of Nisg̱a'a Village Government`; `terms`: `s 29.2(1) definition of Nisg̱a'a child`; `terms`: `s 29.2(1) definition of Nisg̱a'a citizen`; and 6 more | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 29.2(2) | 354 | encoded | `terms`: `s 29.2(2) definition of Nisg̱a'a Final Agreement` |  |
| s 29.2(2) Nisg̱a'a Final Agreement | 354 | encoded | `terms`: `s 29.2(2) definition of Nisg̱a'a Final Agreement` | a definition given in words, a cross-reference or a pointer to another Act, carried as data |
| s 30 heading | 356 | inert-1 |  | reason 1: a section heading (not operative) |
| s 30 | 357 | encoded | `reading`: `s 30 gives no meaning to a metric expression that neither sou...`; `reading`: `s 30 the meaning of a metric expression or symbol` |  |
| s 31 heading | 359 | inert-1 |  | reason 1: a section heading (not operative) |
| s 31 | 360 | encoded | `reading`: `s 31 what the commonly applied name means` |  |
| s 32 heading | 362 | inert-1 |  | reason 1: a section heading (not operative) |
| s 32(1) | 363 | encoded | `terms`: `Where a definition applies` | lead-in line: "In this section" |
| s 32(1) "amended, in respect of a domestic enactment" | 364 | fork | `terms`: `s 32(1) definition of amended`; `terms`: `s 32(1) a change to a domestic enactment counts as an amendment` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 32(1) "amended, in respect of a domestic enactment" (a) | 365 | fork | `repeal`: `s 32 the day whose text of the named enactment the reference ...`; `terms`: `s 32(1) definition of amended`; `terms`: `s 32(1) a change to a domestic enactment counts as an amendment` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 32(1) "amended, in respect of a domestic enactment" (b) | 366 | fork | `repeal`: `s 32 the day whose text of the named enactment the reference ...`; `terms`: `s 32(1) definition of amended`; `terms`: `s 32(1) a change to a domestic enactment counts as an amendment` | F-open-list: the verb is "includes", so a thing the entry does not name is a refusal, not FALSE |
| s 32(1) "domestic enactment" | 367 | fork | `terms`: `s 32(1) definition of domestic enactment`; `terms`: `s 32(1) an enactment is a domestic enactment` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 32(1) "foreign enactment" | 368 | fork | `terms`: `s 32(1) definition of foreign enactment`; `terms`: `s 32(1) an enactment is a foreign enactment` | F-means-closed: "means" with a list closes it; the rival reading leaves it open |
| s 32(2) | 369 | encoded | `repeal`: `s 32 the day whose text of the named enactment the reference ...` |  |
| s 32(3) | 370 | encoded | `repeal`: `s 32 the day whose text of the named enactment the reference ...` |  |
| s 32(4) | 371 | encoded | `repeal`: `s 32 the day whose text of the named enactment the reference ...` |  |
| s 32(5) | 372 | encoded | `repeal`: `s 32 the day whose text of the named enactment the reference ...` |  |
| s 33 heading | 374 | inert-1 |  | reason 1: a section heading (not operative) |
| s 33(1) | 375 | encoded | `definitions`: `s 33(1) a number is in a series referred to by its first and ...` |  |
| s 33(2) | 376 | encoded | `reading`: `s 33(2) speaks only of a Part, division, section, schedule, a...`; `reading`: `s 33(2) the enactment a reference to a Part, division, sectio...` |  |
| s 33(3) | 377 | encoded | `reading`: `s 33(3) speaks only of a subsection, paragraph, subparagraph ...`; `reading`: `s 33(3) the section, subsection, paragraph or subparagraph a ...` |  |
| s 33(4) | 378 | encoded | `reading`: `s 33(4) a reference to regulations is a reference to these re...` |  |
| s 33(5) | 379 | encoded | `reading`: `s 33(5) the division or line of the other enactment a referen...` |  |
| s 33(6) | 380 | fork | `reading`: `s 33(6) says what an Act in that reference includes and does ...`; `reading`: `s 33(6) an Act in a reference to a matter under an Act includ...` | F-open-list: "includes regulations enacted under the authority of that Act" |
| s 34 heading | 382 | inert-1 |  | reason 1: a section heading (not operative) |
| s 34 | 383 | encoded | `replacement`: `s 34 speaks only of an amending enactment`; `replacement`: `s 34 the enactment is construed as part of the enactment that...` |  |
| s 35 heading | 385 | inert-1 |  | reason 1: a section heading (not operative) |
| s 35(1) | 386 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(1)(a) | 387 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(1)(b) | 388 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(1)(c) | 389 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(1)(d) | 390 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(1)(e) | 391 | encoded | `repeal`: `s 35(1) the repeal leaves the matter unaffected` |  |
| s 35(2) | 392 | encoded | `repeal`: `s 35(2) the basis on which an investigation, proceeding or re...` |  |
| s 36 heading | 394 | inert-1 |  | reason 1: a section heading (not operative) |
| s 36(1) | 395 | encoded | `repeal`: `s 36(1) applies only where another enactment is substituted f...`; `replacement`: `s 36(1)(b) the proceeding must be continued under and in conf...`; `replacement`: `s 36(1)(c) the procedure established by the new enactment mus...` |  |
| s 36(1)(a) | 396 | encoded | `repeal`: `s 36(1)(a) a person acting under the former enactment must co...` |  |
| s 36(1)(b) | 397 | encoded | `replacement`: `s 36(1)(b) speaks only of a proceeding commenced under the fo...`; `replacement`: `s 36(1)(b) the proceeding must be continued under and in conf...` |  |
| s 36(1)(c) | 398 | encoded | `replacement`: `s 36(1)(c) names three situations in which the procedure of t...`; `replacement`: `s 36(1)(c) the procedure established by the new enactment mus...` |  |
| s 36(1)(d) | 399 | encoded | `repeal`: `s 36(1)(d) the penalty that may be imposed or adjusted` |  |
| s 36(1)(e) | 400 | encoded | `repeal`: `s 36(1)(e) a regulation made under the former enactment remai...` |  |
| s 36(1)(f) | 401 | repealed |  | reason 3: shown as "[Repealed 2018-5-6.]" |
| s 36(2) | 402 | repealed |  | reason 3: shown as "[Repealed 2018-5-6.]" |
| s 37 heading | 404 | inert-1 |  | reason 1: a section heading (not operative) |
| s 37(1) | 405 | encoded | `replacement`: `s 37 says what must not be read into a repeal, amendment, con...`; `replacement`: `s 37 the thing may be read into what is done` | the grid of what is done by what is read in: 11 cells named by the text, 19 refused |
| s 37(2) | 406 | encoded | `replacement`: `s 37 says what must not be read into a repeal, amendment, con...`; `replacement`: `s 37 the thing may be read into what is done` | the grid of what is done by what is read in: 11 cells named by the text, 19 refused |
| s 37(3) | 407 | encoded | `replacement`: `s 37 says what must not be read into a repeal, amendment, con...`; `replacement`: `s 37 the thing may be read into what is done` | the grid of what is done by what is read in: 11 cells named by the text, 19 refused |
| s 38 heading | 409 | inert-1 |  | reason 1: a section heading (not operative) |
| s 38 | 410 | encoded | `definitions`: `s 38 speaks only of a notice to be given where no newspaper i...`; `definitions`: `s 38 says that publication in the nearest British Columbia ne...`; `definitions`: `s 38 publication in the nearest British Columbia newspaper ma...` |  |
| s 39 heading | 412 | inert-1 |  | reason 1: a section heading (not operative) |
| s 39 | 413 | encoded | `reading`: `s 39 speaks only of an enactment relating to legal proceedings`; `reading`: `s 39 the definitions section of the Supreme Court Act extends...` |  |
| s 40 heading | 415 | inert-1 |  | reason 1: a section heading (not operative) |
| s 40(1) | 416 | encoded | `reading`: `s 40 speaks only of an enactment relating to municipal and re...`; `reading`: `s 40 the definition applies to the term in the enactment` |  |
| s 40(1)(a) | 417 | encoded | `reading`: `s 40 speaks only of an enactment relating to municipal and re...`; `reading`: `s 40 the definition applies to the term in the enactment` |  |
| s 40(1)(b) | 418 | encoded | `reading`: `s 40 speaks only of an enactment relating to municipal and re...`; `reading`: `s 40 the definition applies to the term in the enactment` |  |
| s 40(2) | 419 | fork | `reading`: `s 40 speaks only of an enactment relating to municipal and re...`; `reading`: `s 40 the definition applies to the term in the enactment` | F-municipality: whether the exception also takes the Local Government Act's "municipality" out |
| s 41 heading | 421 | inert-1 |  | reason 1: a section heading (not operative) |
| s 41(1) | 422 | fork | `powers`: `s 41(1) speaks only of an enactment that provides that the Li...`; `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list: "empowering ... to" lists what a power to make regulations is construed as empowering |
| s 41(1)(a) | 423 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1)(a) speaks only of regulations that are considered nec...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list, and F-limit-or-scope: "considered necessary and advisable ... ancillary ... not inconsistent" describes the regulations the paragraph speaks of; others are a refusal |
| s 41(1)(b) | 424 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list: "empowering ... to" lists what a power to make regulations is construed as empowering |
| s 41(1)(c) | 425 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list: "empowering ... to" lists what a power to make regulations is construed as empowering |
| s 41(1)(d) | 426 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list: "empowering ... to" lists what a power to make regulations is construed as empowering |
| s 41(1)(e) | 427 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1)(e) speaks only of a regulation made by or with the ap...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list, and F-limit-or-scope: "made by or with the approval of the Lieutenant Governor in Council" is the scope of the paragraph; a minister's regulation without approval is a refusal |
| s 41(1)(f) | 428 | fork | `powers`: `s 41(1) lists what a power to make regulations is construed a...`; `powers`: `s 41(1) the power to make regulations is construed as empowering` | F-open-list, and F-limit-or-scope: a ceiling ("not greater than") is a limit stated in the words; a penalty above it is FALSE |
| s 41(2) | 429 | encoded | `powers`: `s 41(2) speaks only of a regulation made under the authority ...`; `powers`: `s 41(2) the regulation has the force of law` |  |
| s 42 heading | 431 | inert-1 |  | reason 1: a section heading (not operative) |
| s 42(1) | 432 | encoded | `reading`: `s 42(1) the place of a subdivision in the descending order`; `reading`: `s 42(1) the subdivision next below` |  |
| s 42(2) | 433 | encoded | `definitions`: `s 42(2) the subdivision a reference means` |  |
| s 42(2)(a) | 434 | encoded | `definitions`: `s 42(2) the subdivision a reference means` |  |
| s 42(2)(b) | 435 | encoded | `definitions`: `s 42(2) the subdivision a reference means` |  |
| s 42(2)(c) | 436 | encoded | `definitions`: `s 42(2) the subdivision a reference means` |  |
| s 43 heading | 438 | inert-1 |  | reason 1: a section heading (not operative) |
| s 43 | 439 | fork | `reading`: `s 43 says only how an Act may be cited; it does not say that ...`; `reading`: `s 43 an Act of this kind may be cited this way` | F-open-list: "may be cited as follows" does not forbid another way |
| s 43(a) | 440 | fork | `reading`: `s 43 says only how an Act may be cited; it does not say that ...`; `reading`: `s 43 an Act of this kind may be cited this way` | F-open-list: "may be cited as follows" does not forbid another way |
| s 43(b) | 441 | fork | `reading`: `s 43 says only how an Act may be cited; it does not say that ...`; `reading`: `s 43 an Act of this kind may be cited this way` | F-open-list: "may be cited as follows" does not forbid another way |
| s 43(c) | 442 | fork | `reading`: `s 43 says only how an Act may be cited; it does not say that ...`; `reading`: `s 43 an Act of this kind may be cited this way` | F-open-list: "may be cited as follows" does not forbid another way |
| s 43(d) | 443 | fork | `reading`: `s 43 says only how an Act may be cited; it does not say that ...`; `reading`: `s 43 an Act of this kind may be cited this way` | F-open-list: "may be cited as follows" does not forbid another way |
| s 44 heading | 445 | inert-1 |  | reason 1: a section heading (not operative) |
| s 44 | 446 | encoded | `reading`: `s 44 speaks only of an enactment that provides that another e...`; `reading`: `s 44 the other enactment applies`; `reading`: `s 44 the other enactment applies with this change` |  |
| Schedule | 448 | inert-1 |  | reason 1: the heading of the Schedule |
| Schedule paragraph | 449 | encoded | `terms`: `the legs of the Schedule` | the Schedule as data, in legs; the limit (no point-in-line test) is finding 7 |


## 2. Fork register

Each fork: the readings seen, the one taken, the text that licenses each, and where it is tested.
"Rival n" is a numbered section of `bc-tests-alt-readings-expected-fail.l4`, where the rival reading is written as an expectation that is meant to fail (16 assertions in all).
Where I looked and found nothing is said under "Where I looked", after the forks.
Four entries are notes and not forks, because the text settles the point and no second reading was seen: F-asymmetry, F-25.5, F-language and F-target.
They were entries of pass 1's register and are kept as they were; no row of the coverage table cites them, and no module or test names them.

### Counting

**F-count. Does a period "from" a day count that day, and is the last day inside it?**
- Reading A (taken): the reference day is not counted, the last day is inside. 30 days from 2026-01-01 end on 2026-01-31.
- Reading B: the reference day is day 1. 30 days from 2026-01-01 end on 2026-01-30.
- Licence for A: s 25.2(2)(a), "by counting forward from and including the day after the reference day"; (b), "by counting backward from and including the day before the reference day". The words "and including" put the first counted day inside the period.
- Tested: `bc-tests-time-periods.l4` (days and weeks, spans, inside). Rival 1 (3 assertions).

**F-position. What do "from", "after", "within N days of" and "before" mean?**
The text names two positions only: the reference day is before the period, or after it (s 25.2(2)(a) and (b), and the same limbs in ss 25.3(1), 25.4(1)). It gives no list of words that fall in each.
Taken: the position is an input (`Position of the reference day`). The four named wrappers (`the last day of a period of days counted from a day` and its three siblings) fix it as "before" and the period as not "clear".
The text does not distinguish "from" from "after": both are a reference day before the period, and the reference day is not counted (F-count).
Not tested as a fork: nothing in the text to test.

**F-asymmetry. Days and weeks are counted; months and years go to a corresponding date.**
This is the text, not a choice: s 25.2 counts days and excludes the reference day; ss 25.3(1) and 25.4(1) go "to and including the date numerically corresponding to the reference day".
So 30 days from 2026-01-01 end on 2026-01-31, and one month from 2026-01-01 ends on 2026-02-01.

**F-month. How does s 29 "month" fit s 25.3?**
- s 29: "month means a period calculated from a day in one month to a day numerically corresponding to that day in the following month, less one day". Read alone, a month that begins 2026-01-01 ends 2026-01-31.
- s 25.3(1)(a): one month from the reference day 2026-01-01 ends on 2026-02-01.
- Taken: the two agree if the period begins on the day AFTER the reference day (2026-01-02 to 2026-02-02, less one day, is 2026-02-01). The text does not say on what day a month period begins; the spans in this module take the day next to the reference day as the near end of all four units, as s 25.2(2) says for days.
- Tested: `bc-tests-time-periods.l4` (months, spans), `bc-tests-time-words.l4` (s 29 "month"). Rival 3.

**F-unit. Calendar months and years, or fixed lengths?**
Calendar, on the text: s 29 "month" is by "a day numerically corresponding", "year means any period of 12 consecutive months", and ss 25.3 and 25.4 go to the corresponding date. A month is not 30 days and a year is not 365.
Tested: leap-day cases in `bc-tests-time-periods.l4`. Rival 2.

**F-start-day. A start on the 31st, on 29 February, and a month that lacks the start day's number.**
- s 25.3(3): a date that does not occur in the month becomes the last day of that month. One month from 2025-01-31 ends 2025-02-28; from 2024-01-31 ends 2024-02-29.
- s 25.4(3): 29 February in a year without one becomes 28 February. One year from 2024-02-29 ends 2025-02-28; four years from it end 2028-02-29, which exists.
- Two years from 2024-02-28 end 2026-02-28: the leap day 2024-02-29 lies inside the period and is not the reference day, so s 25.4(3) is not engaged.
- Tested: `bc-tests-time-periods.l4`, worked cases in section 4.1.

**F-clear. "Clear", "at least", "not less than": which order do the shifts and the date rule apply in?**
- ss 25.3(2) and 25.4(2) shift the date found under (1) by one day (later going forward, earlier going back). ss 25.3(3) and 25.4(3) then say the date "determined under subsection (1) or subsections (1) and (2), as applicable" is replaced if it "would fall on a date that does not occur in the calendar month in which the period begins or ends" (25.3(3)) or "would be February 29 and February 29 does not occur in the year in which the period begins or ends" (25.4(3)).
- Where the date of (1) occurs, the shift is plain arithmetic, and the module does it: 1 clear month from 2026-01-28 ends 2026-03-01 (28 February plus a day); 1 clear year from 2025-07-16 ends 2026-07-17; 1 clear year from 2024-02-28 ends 2025-03-01.
- The month case (ss 25.3(2) and (3)): "at least one month" after 31 January 2025. (1)(a) gives 31 February 2025, which does not occur.
  - Reading M1: (3) is applied to the result of (1) and (2) together. "One day later than 31 February" does not name a day either, so the period ends on the last day of February, 28 February 2025.
  - Reading M2: (3) is applied to the result of (1) alone, and (2) then adds its day: 28 February, then 1 March 2025.
  - Licence for M1: (3) tests the date "determined under subsection (1) or subsections (1) and (2), as applicable": one date, determined once, after (2) where (2) applies.
  - Licence for M2: (2) shifts the end "as determined under subsection (1)(a)", and what (1)(a) determined, once (3) has been applied to it, is 28 February.
- The year case (ss 25.4(2) and (3)): "at least one year" after 29 February 2024. (1)(a) gives 29 February 2025, which does not occur.
  - Reading Y1: (3) is applied to the date that (1) and (2) are aiming at, which "would be February 29", and replaces it: the period ends on 28 February 2025.
  - Reading Y2: the period ends on 1 March 2025, reached either by applying (3) to (1) alone and then adding the day, or by shifting first, since the shifted day, 1 March, is not 29 February and (3) is not engaged.
  - Licence for Y1: (3) speaks of a date that "would be February 29", which is the date (1) names. Licence for Y2: (3) is stated for "(1) or (1) and (2), as applicable", and after (2) the date is 1 March.
- Taken for both cases (the month case and the year case): **REFUSE**, by name (`s 25.3 does not say how to shift a clear month by a day when the day numerically corresponding to the reference day does not occur`; `s 25.4 does not say how to shift a clear year by a day when the reference day is 29 February and the year has none`).
- Tested: `bc-tests-time-periods.l4`, the refused assertions under "clear". Rival 4 covers the reading that "clear" adds nothing, for days. Which end moves for clear days is the fork F-clear-ends.

**F-whole. A count of nought, a negative count, a fraction.**
ss 25.2(2), 25.3(1) and 25.4(1) speak of "one day or consecutive days", "one month or consecutive months", "one year or consecutive years". Nought, a negative or a fractional count is not such a period, and the text says nothing about it.
Taken: **REFUSE** (`ss 25.2 to 25.4 count a whole number of one or more days, weeks, months or years`). A week count is turned into days first, so half a week (3.5 days) is refused too.
Tested: `bc-tests-time-periods.l4`, last section.

### Holidays and closed offices

**F-holiday-scope. Does the holiday rule reach months and years, or only days?**
- s 25(3) names "section 25.2, 25.3 or 25.4", so on its words it reaches days, weeks, months and years.
- It applies only to "a period for doing an act". The text does not define that phrase. A period that is not for doing an act (for example, how long a thing lasts) is not moved.
- Taken: the module offers both forms. The plain functions never move a day. The functions named `... for doing an act` take the caller's calendar and move the ends. Which form a period needs is for the caller to decide, and is an open question (section 6).
- Tested: `bc-tests-time-holidays.l4`, the section on days, weeks, months and years. Rival 5.

**F-near-end. Does the day next to the reference day move off a holiday too?**
- s 25(3) speaks of a period that is determined "to begin or end on a holiday", and says it "begins or ends" on the next (or previous) day that is not a holiday.
- Reading A (taken): both ends move. One day from Saturday 2026-04-04, counting starts on Sunday 2026-04-05, a holiday, so the period begins on the first day after it that is not a holiday.
- Reading B: only the end that ss 25.2 to 25.4 count out to moves.
- Licence for A: the words "begins or ends". For months and years the text does not determine the near end at all (F-month), so for them the near end is the day next to the reference day by the same reading.
- Tested: `bc-tests-time-holidays.l4`, the section on "begins or ends". Rival 11.

**F-consecutive. Several holidays in a row.**
The text says "the next day that is not a holiday" (reference day before the period) and "the previous day that is not a holiday" (after). So the end skips every holiday in a row: with Sunday 2026-04-05 and a supplied Monday 2026-04-06, a period ending on the Sunday ends on Tuesday 2026-04-07. Three in a row (a supplied Friday 25 December, Saturday 26 December, Sunday 27 December) end on Monday 28 December, or Thursday 24 December going backward.
The walk gives up after 366 days with a named refusal, so a calendar that says every day is a holiday cannot loop.
Tested: `bc-tests-time-holidays.l4`.

**F-saturday. Is Saturday a holiday?**
s 29 "holiday includes" Sunday, Christmas Day, Good Friday, Easter Monday, a list of named days, 26 December and days set or appointed by the Parliament of Canada, the Legislature or a proclamation. Saturday is not listed. "Includes" does not make the list closed, so a caller may add Saturday to its own calendar; the module does not.
The named holidays have no dates in the text, so they are input. Only Sunday and 26 December are dated by the text, and `s 29 a day is a holiday` supplies those two.
Tested: Saturday 2026-01-31 is not moved (`bc-tests-time-holidays.l4`). Rival 6.
- Whether the holiday list is open: "holiday includes" followed by (a) to (d).
  - Reading A (taken): the list is open. A day it does not name is not decided by the text, so `s 29 a day is a holiday` takes Sunday and 26 December from the text and the rest of the calendar from the caller, and the catalogue answers a question about an unnamed day, such as Saturday, with a refusal (F-open-list).
  - Reading B: the list is closed. Only the named days are holidays, and a caller may not add Saturday or a local day.
  - Licence for A: the verb is "includes", and the Act writes "means" where it closes a list (F-means-closed). Licence for B: paragraph (d) already lets a day be added ("a day set by the Parliament of Canada or by the Legislature, or appointed by proclamation ... as a public holiday"), which a reader may take as the Act's own way of extending the list and so as leaving no room for others.
  - Tested: `bc-tests-terms-rules.l4` ("holiday" and "Saturday" is a refusal), `bc-tests-time-holidays.l4`.

**F-office. A day the office is closed (s 25(4)) against a holiday (s 25(3)).**
- s 25(4)(a): next day the office is open. (b): the previous day it is open, but only if BOTH the office is regularly closed on the day the period is determined to begin or end AND the reference day is after the period.
- So an office shut on a Friday for a reason that is not its regular closing moves forward even when the reference day is after the period. s 25(3)(b) looks back whenever the reference day is after.
- Taken: as written. Tested: `bc-tests-time-holidays.l4`. Rival 7 and Rival 10.
- The module has the boundary function for s 25(4); it has no span function for it (spans are given for holidays only).

**F-25.5. A day specified for doing an act.**
s 25.5(1): a holiday moves to the next day that is not a holiday. (2): a day the office is not open moves to the next day it is. Neither has a backward limb and neither mentions the reference day.
Tested: `bc-tests-time-holidays.l4`.

### Commencement and moments

**F-moment. From what moment on its commencement day does an enactment bind?**
s 4(1): "an enactment must be construed as commencing at the beginning of the day on which it comes into force". s 26(1) and (2): a reference to time in British Columbia is a reference to Pacific Time, "7 hours behind Coordinated Universal Time".
So an Act with no other date, assented to on 2026-03-10, binds from 2026-03-10 00:00 Pacific Time, which is 2026-03-10 07:00 UTC.
The text answers this directly; there is no fork on the moment itself. The next two rows are the nearby forks.

**F-offset. Pacific Time all year.**
s 26(1) says 7 hours and has no exception and no mention of daylight saving time. Taken: 7 hours on every day of the year, so the beginning of 2026-01-15 is 07:00 UTC.
Whether the Act intends something else is a question for a domain expert (section 6). Rival 8 puts the offset at 8 hours in winter (the figure 8 is not from the text).

**F-assent. "Passed", "published" and "assent".**
The brief's case says the Act is "passed or published" on 2026-03-10. ss 3(2) and 3(1) speak of the DATE OF ASSENT; no provision of the text says that the day an Act is passed or published is its date of assent.
Taken: the module takes the date of assent (`How an Act received assent`). A caller that has only a "passed" or "published" day gets the named refusal `s 3 does not say that the day an Act was passed or published is its date of assent`.
For an Act reserved for the Governor General the date of assent is the date of the signification (s 3(1)); until then it has no date of assent and the answers are `NOTHING`.

**F-fixed-later. An Act that comes into force on a day to be fixed.**
s 3(2) puts only a portion "for which no other date of commencement is provided in the Act" on the date of assent. A portion that the Act says comes into force on proclamation or by regulation therefore commences on the day fixed (2026-06-01 in the brief's case), at the beginning of that day; the text takes this for granted in s 3(3) and s 3(3.1) and does not state it in so many words. The provision that says so, and the title, are deemed in force on the date of assent (s 3(3)).
Until the day is fixed, there is no day and no moment: `NOTHING`, not a refusal, because the text answers (the portion is not in force) and it is the caller's input that is missing.

**F-retroactive. A stated day earlier than assent (s 3(3.1)).**
The portion comes into force "in accordance with the terms of the provision" on the earlier day, and is retroactive. The module returns that day as the commencement and says so with `s 3(3.1) a portion comes into force on a day earlier than the date of assent, and is retroactive`. How far the retroactivity reaches ("to the extent necessary to give it force and effect") is not computable here.

**F-regulation-silent. A regulation that says nothing about commencement.**
- s 3(5) covers "every regulation of a class that is exempted from the application of the Regulations Act or to which that Act does not apply and that is not expressed to come into force on a particular day": it comes into force the day it was enacted. s 3(2) cannot cover a regulation, since it speaks of an Act and of assent.
- Taken: an exempt regulation silent on the matter commences on the day it was enacted, at the beginning of that day (s 4(1), and "enactment" includes a regulation, s 1). A regulation of any other class that names no day gets the named refusal `s 3(5) does not say when a regulation of any other class that names no day comes into force`; the Regulations Act is not in this text.
- A regulation of EITHER class that is expressed to come into force on a particular day: the module passes that day through (2026-05-01 in the test). This is not refused, and it is not licensed by a rule in this text either: s 3(5) only presupposes that a regulation can be so expressed, and the Regulations Act, which is not in the text, may add conditions (deposit or publication, say). Refusing it would make the module unable to answer a question whose answer the text's own wording assumes; passing it through is registered here, and listed in section 6, so that it is a reviewed reading and not an unnoticed default.
- A regulation enacted in the middle of a day binds from the beginning of that day. That is what s 3(5) and s 4(1) say together; it is a surprising result, so it is listed in section 6.
- Tested: `bc-tests-time-commencement.l4`.

**F-proclamation. s 16(2).**
A proclamation "may be dated the day its issue was authorized", and the day it so purports to have been issued is deemed the day it takes effect. Taken: if it bears that date, that day; any other case gets a named refusal.

**F-age. s 25.1 and a birth on 29 February.**
A person reaches an age "at the beginning of the relevant anniversary of the person's birth date". The text does not say which day is the anniversary of 29 February in a year without one. Taken: **REFUSE**. In a leap year the anniversary is 29 February. Tested: `bc-tests-time-words.l4`. Rival 9 is about the beginning, not the end, of the day.

**F-month-def. s 29 "month" and "year" with a start on the 29th to 31st.**
The following month may have no day numerically corresponding to the day the month begins on. s 25.3(3) is written for the periods that s 25.3(1) describes, those "expressed in relation to a reference day", not for this definition. Taken: **REFUSE** for a month that begins on the 29th, 30th or 31st when the following month lacks that number, and so for a year (12 consecutive months, computed month by month) that runs into such a month. Tested: `bc-tests-time-words.l4`.

**F-cessation. s 4(2) and (3).**
An enactment repealed and replaced ceases to have effect "at the time the new enactment commences" (the beginning of its commencement day). Any other enactment ceases "at the end of the day on which it expires", which is taken as the beginning of the next day. Tested: `bc-tests-time-commencement.l4`.

**F-appointment. s 20(4)(e) and "unless earlier terminated by the appointee".**
(e): the end is "when the new appointment begins". The text does not say when a resignation by the appointee takes effect, so no rule is written for it; a caller who knows the day uses (a) with it.

### Other rules

**F-deemed-service. Service and receipt of a mailed notice.**
s 29 "deliver ... includes mail to or leave with a person, or deposit in a person's mailbox or receptacle"; "mail refers to the deposit ... in the Canada Post Office at any place in Canada, postage prepaid ... and includes deliver". The text defines when a document is delivered by mailing as the act of depositing it, and has no rule on when it is received or deemed received.
Taken: the day a mailed document is delivered is the day of deposit; a deposit outside Canada or without prepaid postage is not mail in the Act's sense (named refusal); when a mailed document is RECEIVED is a named refusal, "the Act is silent".
- The two entries point at each other: "deliver ... includes mail to or leave with a person" and "mail ... includes deliver".
  - Reading A (taken): each entry is an open list that names the other, and neither narrows the other. No rule in the modules follows the pointer from one entry to the other (`s 29 the definition of a term names a thing` reads only the entry it is given), so there is no loop to run. The catalogue carries "mail" naming "deliver" and "deliver" naming "mail to a person" as data.
  - Reading B: mutual inclusion makes the two co-extensive, so every delivery of a document is a mailing and every mailing a delivery.
  - Licence for A: both verbs are "includes", which adds to the ordinary meaning without defining it. Licence for B: if each includes the other, the two sets are the same.

**F-rendering-order. The order of the words of "regulation", "insurance company" and "final agreement".**
Pass 1 called this fork F-regulation-def, when only "regulation" was affected; `bc-interpretation-definitions.l4` now cites the new name.
In the rendering, the paragraphs of three entries follow the semicolon that ends the entry: "regulation" (a) "in execution of a power conferred under an Act" and (b) "by or under the authority of the Lieutenant Governor in Council" (src:14-16), "insurance company" (a) "an insurance company" and (b) "an extraprovincial insurance corporation" (src:257-259), and "final agreement" (a) "among a first nation, the Province and Canada" and (b) "negotiated by those parties in a process facilitated by the British Columbia Treaty Commission" (src:334-336).
- Reading A (taken): the paragraphs complete the entry. An instrument is a regulation when it is of a listed kind, is enacted (a) in execution of a power under an Act or (b) by or under the authority of the Lieutenant Governor in Council, and is not one of the two excluded orders.
- Reading B: the paragraphs are separate sentences that define nothing.
- Licence for A: the paragraphs have no verb of their own and follow the entry directly. In "regulation" the entry ends "instrument enacted but does not include ..." and the limbs say how it was enacted; in "insurance company" the entry reads "means authorized to carry on insurance business under the Financial Institutions Act;" and has no one to be authorized until the limbs say who. For "final agreement" the limbs describe the agreement (src:335-336); no more is claimed.
- The structure restored for each entry (the reading taken):
  - "regulation": "regulation means a regulation, order, rule, form, tariff of costs or fees, proclamation, letters patent, commission, warrant, bylaw or other instrument enacted (a) in execution of a power conferred under an Act, or (b) by or under the authority of the Lieutenant Governor in Council, but does not include an order of a court made in the course of an action or an order made by a public officer or administrative tribunal in a dispute between 2 or more persons". The limbs go after "enacted" and before "but does not include". `s 1 an instrument is a regulation` encodes this: a listed kind, AND (under an Act OR by the Lieutenant Governor in Council), AND NOT either excluded order.
  - "insurance company": "insurance company means (a) an insurance company, or (b) an extraprovincial insurance corporation, authorized to carry on insurance business under the Financial Institutions Act". The limbs go between "means" and "authorized", because "means authorized to ..." has no subject. The catalogue names the two limbs, closes the list, and carries "authorized to carry on insurance business under the Financial Institutions Act" as the condition and the Act as a pointer.
  - "final agreement": the limbs "(a) among a first nation, the Province and Canada, and (b) negotiated by those parties in a process facilitated by the British Columbia Treaty Commission" describe the agreement. I did not decide whether they attach to the first "means" limb or to both, and no function depends on it. The catalogue carries them, with "except in references to the Nisga'a Final Agreement", as conditions of the entry as a whole, and names nothing.
- The rendering is not the official text; a reviewer should look at the official order of the words.
- Where: `bc-interpretation-definitions.l4` for "regulation"; the other two are entries of the catalogue in `bc-interpretation-terms.l4`.

**F-government. s 14(2) against "specifically provides otherwise" in s 14(1).**
- s 14(1): "Unless it specifically provides otherwise, an enactment is binding on the government." s 14(2): "Despite subsection (1), an enactment that would bind or affect the government in the use or development of land, or in the planning, construction, alteration, servicing, maintenance or use of improvements, as defined in the Assessment Act, does not bind or affect the government."
- The case: an enactment that EXPRESSLY says it binds the government in the use of land.
- Reading A (taken): s 14(2) wins. "Despite subsection (1)" sets aside the whole of (1), including its "unless it specifically provides otherwise", so an express provision does not bring the enactment back.
- Reading B: the express provision wins. (2) speaks of an enactment that "would bind or affect" the government, and one that specifically provides that it binds the government is the Legislature saying so in terms; (2) is then a default for an enactment that is silent.
- Licence for A: "Despite subsection (1)" and "does not bind or affect"; the words give no exception for an express provision. Licence for B: the word "specifically" in (1) shows that the Act expects the Legislature to be able to say so in terms.
- Where: `s 14 an enactment binds the government` in `bc-interpretation-definitions.l4` has no input for "specifically provides that it DOES bind in land use"; when the enactment affects the government in land use the answer is FALSE whatever it says (the first branch).
- Tested in `bc-tests-definitions.l4`. The text does not address the case where the enactment says it binds the government; section 6.

**F-contrary-intention. s 2(1).**
A provision of the Act applies "unless a contrary intention appears in this Act or in the enactment". Taken: the caller decides whether a contrary intention appears, as two booleans; the function does not search the text of the enactment.

**F-language. Which language version has authority.**
The text has no provision on the language of an enactment. The brief says British Columbia enacts and publishes only in English, and `../../SOURCE-LICENSE.md` says the same; neither is a statement in the Act, and no provision of the text is encoded on this. s 17(1)(f) mentions an English and a French form of a corporation's name, which concerns names, not versions of an enactment.

**F-target. The compiler.**
Not a fork in the law: `unstable`, for the reason in section 0.

### Added in pass 2

"Rival n" for the forks above is a numbered section of `bc-tests-alt-readings-expected-fail.l4`.
"Alt-2 rival n" below is a numbered section of `bc-tests-alt-readings-2-expected-fail.l4`, which has 5 assertions, each meant to fail.
A rival can be written to fail only when the module gives a value that the rival contradicts.
Where the module answers with a refusal, an assertion of the rival's value would be refused, not failed, and `check.sh` counts a refused assertion as red; those rivals are described here and the module's refusal is asserted in its own test file (finding 10).

**F-open-list. Does "may do the following", "includes" or "may be cited as follows" close the list?**
- Reading A (taken): the list says what the provision gives and says nothing about what is not on it. A thing not on the list gets a named refusal: the text neither gives it nor takes it away.
- Reading B: the list is closed. A thing not on it is FALSE (not allowed, not included).
- Licence for A: the words are permissive or inclusive. s 10 "may be in the following form", s 17(1) "may do the following", s 22 "include power to do the following", s 23(1) and (3) "include", s 27(4) "includes a power", s 27(6) and (7) "includes", s 28(2) "include", s 33(6) "includes", s 41(1) "empowering ... to", s 43 "may be cited as follows", and the "includes" and "means and includes" entries of s 29. The Act itself uses "means" where it wants a closed list (F-means-closed), which is why B is not taken.
- Where: each module's refusal by name, for example `s 17(1) lists what a corporation may do and does not say it may do nothing else` in `bc-interpretation-powers.l4`; the catalogue's membership rule `s 29 the definition of a term names a thing` in `bc-interpretation-terms.l4`.
- Tested: each module's test file asserts the refusal and its message (`#ASSERT REFUSED ... BECAUSE`); for example `bc-tests-powers.l4` (s 17(1), 22, 23, 27, 41), `bc-tests-reading.l4` (s 10, 33(6), 43), `bc-tests-terms-rules.l4` (the catalogue). Reading B is not in an expected-fail file (above).

**F-means-closed. Does "means" followed by a list close it?**
- Reading A (taken): yes. "reference day means any of the following" (s 25(1)), "appointing instrument means an enactment that appoints a person to an office" (s 20(1)), and the catalogue entries whose "means" is followed by a list (the `the list is closed` flag) give FALSE for a thing that is not on the list.
- Reading B: "means" leaves the list open as "includes" does, so the answer for a thing not on the list is a refusal.
- Licence for A: the Act writes "includes" when it wants an open list (s 29 "land includes ...") and "means" otherwise (s 29 "enactment" is "an Act, a regulation or a portion"); a reader who takes both as open makes the two words say the same.
- Tested: `bc-tests-periods.l4` (s 25(1)), `bc-tests-commencement.l4` (s 20(1)), `bc-tests-terms-rules.l4`. Alt-2 rival 3 (two assertions: s 25(1) and s 20(1)).

**F-adm. Does "authorized by the minister" qualify "an assistant deputy minister" as well as "some other official"? (s 23(2))**
- The text: "an assistant deputy minister, or some other official authorized by the minister, has the powers and must perform the duties of the deputy minister".
- Reading A (taken): the phrase qualifies "some other official" only. An assistant deputy minister steps in whether or not the minister has authorized that assistant deputy minister.
- Reading B: the phrase qualifies both. An assistant deputy minister the minister has not authorized does not step in.
- Licence for A: the phrase stands next to "some other official" and the first limb is set off by commas. Licence for B: the phrase could be read as an adjunct of the whole alternative; nothing in the section says it is not.
- The module does not model several assistant deputy ministers: it answers for one at a time, and the text does not say which of several steps in.
- Where: `s 23(2) the official has the powers and must perform the duties of the deputy minister`, `bc-interpretation-powers.l4`. The assistant deputy minister constructor carries the field `the minister has authorized the assistant deputy minister`, which reading A ignores and reading B would use.
- Tested: `bc-tests-powers.l4`. Alt-2 rival 1.

**F-pleasure. What does "authority to appoint during pleasure" say? (s 20(2))**
- Reading A (taken): the sentence names appointment during pleasure. It does not say the authority is only for that, and it does not say what an appointment during pleasure allows. A fixed-term appointment, and the ending of an appointment at will, are refusals.
- Reading B1: the authority is only for appointment during pleasure, so a fixed term is FALSE.
- Reading B2: "during pleasure" has its common-law meaning, so an appointment may be ended at will, without notice or cause; TRUE.
- Licence for A: s 22(a) says words authorizing the appointment of a public officer include power to "set the public officer's term of office", which a reader of B1 would have to treat as an exception to s 20(2); and the text contains no definition of "pleasure".
- Where: `s 20(2) names appointment during pleasure and does not say the authority is only for that`; `s 20(2) does not say what an appointment during pleasure allows: ending it at will, without notice or without cause`; `bc-interpretation-commencement.l4`.
- Tested: `bc-tests-commencement.l4` (both refusals asserted). Not in an expected-fail file (refusal).

**F-municipality. Does the exception in s 40(2) take "municipality" out of both sources?**
- The text: "(2) As an exception, subsection (1) does not apply in relation to the definition of "municipality" in the Community Charter."
- Reading A (taken): only the Community Charter's definition is excepted. The word in section 1 of the Schedule to the Local Government Act is not.
- Reading B: the word is out of both sources named in s 40(1).
- Licence for A: the exception names the Community Charter and no other Act. Licence for B: s 40(1) lists the two sources together and the exception speaks of "subsection (1)" as a whole.
- Where: `s 40 the definition applies to the term in the enactment`, `bc-interpretation-reading.l4`.
- Tested: `bc-tests-reading.l4` (both sources, both terms). Alt-2 rival 2.

**F-always-speaking. As of what day is an enactment read? (s 7(1))**
- Reading A (taken): "Every enactment must be construed as always speaking" means it is read as of the day it is applied, not the day it was enacted.
- Reading B: the phrase governs tense only (s 7(2)), and the day a provision is read as of remains the day it was enacted.
- Licence for A: the plain words; s 7(2) is introduced by "If a provision ... is expressed in the present tense", which would be redundant if s 7(1) governed tense alone. Licence for B: the section does not mention definitions or dates.
- Where: `s 7(1) the day as of which an enactment is read`, `bc-interpretation-reading.l4`.
- Tested: `bc-tests-reading.l4`. Alt-2 rival 4.

**F-majority. What is "a majority of the members" of a corporation? (s 17(2))**
- Reading A (taken): more than half. With 4 members, 3 are a majority and 2 are not; the text does not say what fewer than a majority may do, so that is a refusal.
- Reading B: at least half.
- Licence for A: s 18(1) applies only where an act is to be done "by more than 2 persons", which treats two persons as having no majority between them. The Act does not define "majority".
- Where: `s 17(2) the members who act may bind the others and the corporation`, `bc-interpretation-powers.l4`.
- Tested: `bc-tests-powers.l4` (3 of 4 is a majority, 2 of 4 is a refusal, 3 of 3 and 1 of 1 are). Not in an expected-fail file (refusal).

### Added after the independent test pass

An author who had not read this file wrote assertions against the modules and reported cases where a reading was not registered.
The entries below are the new forks; the cases that belong to a fork already in the register were added to it (F-clear, F-saturday, F-deemed-service, F-government).
A rival reading is not written as an expected-failure assertion for any of them in this pass.

**F-clear-ends. "Clear" days: does the one-day shift move the beginning as well as the end? (s 25.2(3)(a))**
- The text: "the beginning or end of the period, as determined under subsection (2) (a), is one day later".
- The case: "7 clear days after 1 January 2026". Under (2)(a), counting forward from and including the day after the reference day, 7 days run from 2 January to 8 January.
- Reading A (taken): "the beginning or end" names the end that the expression fixes by counting from the reference day, so only the end the count reaches moves: the span is 2 January to 9 January (`the span of days of a period counted from a reference day` with `clear` TRUE, run in this pass: `Span of days` from 2 January to 9 January).
- Reading B: both the beginning and the end "as determined under subsection (2)(a)" are one day later, so the span is 3 January to 9 January and keeps its length of 7 days.
- Licence for A: in (2) the phrase "the beginning or end of a period ... expressed in relation to a reference day" names whichever of the two the expression fixes from the reference day, and (3) repeats the phrase.
- Licence for B: (2)(a) determines the beginning (the day after the reference day) and the end together by one count, and (3)(a) moves "the beginning or end ... as determined under subsection (2)(a)", which on a plain reading is both.
- Tested: `bc-tests-periods.l4`, the last section (the span for 7 days, not clear, is 2 to 8 January; clear, 2 to 9 January).

**F-affidavit. Does "made under the Evidence Act, or under the Canada Evidence Act" qualify "a statutory declaration" as well as "a solemn declaration"? (s 29 "affidavit or oath")**
- The text: "affidavit or oath includes an affirmation, a statutory declaration, or a solemn declaration made under the Evidence Act, or under the Canada Evidence Act".
- Reading A (taken): the phrase qualifies the last item only. The catalogue names three things: "an affirmation", "a statutory declaration", and "a solemn declaration made under the Evidence Act, or under the Canada Evidence Act".
- Reading B: the phrase qualifies both declarations, so a statutory declaration counts only if made under one of the two Acts.
- Licence for A: the items are separated by commas, "or" stands before the last item, and the phrase follows the last item with no comma before it. Licence for B: the last two items are both declarations, and a modifier at the end of a list is often read back over more than the last item.
- The entry is "includes", so under either reading a thing it does not name is a refusal (F-open-list).
- Where: `s 29 definition of affidavit` in `bc-interpretation-terms.l4`; the generated tests in `bc-tests-terms.l4` assert the names.

**F-established. What is "a corporation established by an enactment"? (s 17(3))**
- The text: "Individual members of a corporation established by an enactment who do not contravene the enactment are exempt from personal liability for the corporation's debts, obligations or acts".
- Reading A (taken): the Act does not say. `the corporation is established by an enactment` is an input that the caller supplies (finding 5), so a company incorporated under a general incorporating statute is classified by the caller, not by the module.
- Reading B: only a corporation created by its own special enactment is "established by an enactment".
- Reading C: a corporation incorporated under a general incorporating statute is established by an enactment too, because it exists by force of that statute.
- Licence for B: the words set such a corporation apart from one created in another way, and the same sentence speaks of "the enactment" that established it, as if there were one. Licence for C: "established by an enactment" does not say a special or private Act.
- Where: `s 17(3) the member is exempt from personal liability for the corporation's debts, obligations or acts` in `bc-interpretation-powers.l4`; tested in `bc-tests-powers.l4` (the input TRUE with no contravention gives TRUE; a corporation not established by an enactment, or a member who contravenes, is a refusal).

**F-means-and-includes. Is a "means and includes" entry open as a whole, or does "means" give a closed core to which "includes" adds? (s 29)**
- The entries: "Act" (s 1), "acquire", "corporation", "dispose", "Governor, Governor of Canada or Governor General", "justice", "Lieutenant Governor", "Provincial Treasurer or Treasurer", and "mail" ("refers to ... and includes deliver").
- Example: "justice means a justice of the peace and includes a judicial justice or a judge of the Provincial Court".
- Reading A (taken): the whole entry is open. The catalogue names what both limbs name, and a thing that neither names is a refusal (F-open-list).
- Reading B: the "means" limb is a closed core and "includes" adds listed extras, so a thing in neither is FALSE (a registrar is not a "justice").
- Licence for A: the entry contains "includes", which never closes a list, and a reader who lets "means" close it is ignoring the second verb. Licence for B: the Act uses "means" to close (F-means-closed), and the "includes" limb names specific additions, which would be pointless if the "means" limb were already open.
- Where: the nine entries are catalogue entries with the `closed` flag FALSE, in `bc-interpretation-terms.l4`; `bc-tests-terms.l4` asserts the refusal for each (message: "'includes' leaves the list open").

**F-limit-or-scope. When the words mark the edge of a rule, is a case outside the edge FALSE or a refusal?**
- The cases:
  - s 41(1)(e), "for a regulation made by or with the approval of the Lieutenant Governor in Council": a minister's regulation made without approval.
  - s 41(1)(f), "a penalty not greater than the penalties provided in the Offence Act": a penalty above the ceiling.
  - s 41(1)(a), "as are considered necessary and advisable, are ancillary to it, and are not inconsistent with it".
  - s 17(1)(d), "property other than land": land.
  - s 24, "unless the context indicates that the document is conclusive evidence": a document that the context makes conclusive.
- Reading A (taken): FALSE where the words state the negative themselves, and a named refusal where they only mark the edge of what the rule speaks of.
  - FALSE: a negative consequence stated in terms ("is not part", "does not apply", "does not authorize", "it is not necessary"); an exception whose content is the negation of what the function asks ("unless a contrary intention appears" in s 2(1): the function asks whether the provision applies, and the exception says it does not; "unless it specifically provides otherwise" in s 14(1); "As an exception, subsection (1) does not apply" in s 40(2)); a limit stated as a limit on a quantity ("not greater than" in s 41(1)(f)).
  - Refusal: a description of the case the rule speaks of ("made by or with the approval of", "considered necessary and advisable"), and an exception whose content is a different fact from what the function asks, so that it takes the case out of the rule without saying what follows: s 24's function asks whether the document is admissible and the exception is a conclusive document, about which s 24 says nothing on admissibility; s 17(1)(d)'s function asks whether the corporation may do the thing and the exception is land, which paragraph (d) does not cover.
  - The test that sorts the two uses of "unless": put the exception beside the question the function asks; if the exception answers that question with "no" (s 2(1)), the function is FALSE; if it answers a different question (s 24), the function refuses.
  - So (f) above its ceiling is FALSE, and (e), (a), s 17(1)(d) and s 24 are refusals.
- Reading B: every edge is a refusal. The ceiling too only says what the paragraph empowers (up to the ceiling) and does not say what a greater penalty is; this aligns (f) to (e).
- Reading C: every edge is FALSE. A minister's regulation without approval is not empowered by (e), land is not within (d), and a conclusive document is not admissible by force of s 24.
- Licence for A: a ceiling compares two numbers and the words themselves put the larger one outside the paragraph; FALSE for "land" would say a corporation may not hold land, which s 17(1) does not say (its "may do the following" is an open list, F-open-list); FALSE for s 24's conclusive document would say it is not admissible, which s 24 does not say, since the exception takes the case out of the rule without saying what follows.
- Licence for B: F-open-list applied evenly. Licence for C: "unless", "other than" and "made by" limit the power as "not greater than" does.
- The line A draws is a judgement. The uneven pair that prompted this fork is s 41(1)(e), a refusal, and s 41(1)(f), FALSE.
- Where: `s 41(1) the power to make regulations is construed as empowering` and `s 17(1) a corporation may do the thing` in `bc-interpretation-powers.l4`; `s 24 the document is admissible in evidence in any proceeding` and `s 24 the fact is deemed to be established` in `bc-interpretation-definitions.l4`.
- Tested: `bc-tests-powers.l4` (s 17(1)(d); s 41(1)(a), (e), (f)); `bc-tests-definitions.l4` and `bc-tests-definitions-refusals.l4` (s 24).

### Where I looked and found nothing

- "Day": the text has no definition of "day" or of "week" outside s 25.2(1) ("week means a period of 7 consecutive days"). s 29 defines "month" and "year" but not "day" or "week". The Act is silent on the meaning of "day" beyond how ss 4(1), 20(3), 20(4) and 25.2 use it (a day has a beginning and an end).
- Deemed receipt of a mailed or delivered document: no rule (above).
- Recess and days of rest other than Sunday: s 29 has "holiday" only; the words "recess" and "rest" do not appear in the text. Searched with `grep -n -i -E 'recess|day of rest' RSBC-1996-c.-238.txt` (no match; re-run in pass 2, exit status 1).
- Revival of a repealed enactment: s 35(1)(a) says a repeal does not revive an enactment or thing not in force; the text has no rule on revival by the repeal of the repealing enactment.
- Which Act or rule governs the commencement of a regulation of a class that is not exempt: the Regulations Act, which is not in the text.

## 3. Findings

Numbered so that a module, a test file or the fork register can cite one.
Each says what was found, and where it was checked.

1. **The unit count is mine, and the text is a rendering.**
   `units.py` counts 416 units from `RSBC-1996-c.-238.txt` (title lines 2, section headings 53, subsections 124, paragraphs 104, defined-term entries 118, cross-reference entries 14, the Schedule paragraph 1).
   An entry that defines several words at once ("bank or chartered bank") is one unit, and a section with no subsections counts once.
   Those are choices, and a different parse of the same text would give a different count.
   The text is a script-made rendering, not the official text, and nothing was compared with the official text.

2. **What TRUE, FALSE and a refusal mean in the modules.**
   A function answers "does this provision give this thing in this case?".
   It returns TRUE when the case is within the provision and the provision gives the thing.
   It returns FALSE where the words of the provision give the negative themselves:
   - a negative consequence stated in terms ("is not part", "does not apply", "does not authorize", "it is not necessary", "has no effect");
   - an exception whose content IS the negation of what the function asks ("unless a contrary intention appears": the function asks whether the provision applies, and a contrary intention means it does not, s 2(1); "unless it specifically provides otherwise": whether the enactment binds the government, s 14(1); "As an exception, subsection (1) does not apply": whether the definition applies, s 40(2));
   - a limit stated as a limit on a quantity ("not greater than");
   - a limit such as "so far as the terms defined can be applied", "so far as it is applicable", "as far as it can be adapted".
   It refuses, by name, in the other cases:
   - the case is outside what the provision speaks of;
   - the provision only permits or includes and the case is not listed (fork F-open-list);
   - the words only describe the case the rule speaks of ("applicable to the enactment and not inconsistent", s 2(3); "made by or with the approval of the Lieutenant Governor in Council", s 41(1)(e)), or an exception whose content is a DIFFERENT fact from what the function asks ("unless the context indicates that the document is conclusive evidence", s 24: the function asks whether the document is admissible, and a document the context makes conclusive is a case about which s 24 says nothing on admissibility; "other than land", s 17(1)(d): the function asks whether the corporation may do the thing, and the exception says what paragraph (d) does not cover, not that a corporation may not hold land);
   - the provision says what a majority, a quorum or a listed case may do and does not say what fewer or an unlisted case may (ss 17(2), 18(1), 18(2)(c) and (d)).
   Fork F-limit-or-scope gives the other two readings of the middle cases.
   A refusal is asserted with `#ASSERT REFUSED ... BECAUSE "<the message>"`, so the message is part of the test.
   *Pass 1 did not use this convention everywhere, and eight pass-1 functions were changed in this pass to follow it, in two rounds.*
   First round: `s 24 the document is admissible in evidence in any proceeding` and `s 24 the fact is deemed to be established` (FALSE when the enactment provides no evidence rule, or when the context indicates the document is conclusive), `s 28(1) the deviation does not invalidate the form used` (FALSE when no form is prescribed, or when the deviation affects substance), and `s 4(4) the enactment is deemed to be repealed for the purposes of this Act` (FALSE when the enactment has not expired).
   Second round, after the independent test pass: `s 18(1) a majority of the persons may do the act` (FALSE for a number that is not a majority), `s 18(2)(c) the act is deemed to have been done by the association` (FALSE with no quorum or no majority of those present), `s 18(2)(d) a vacancy does not impair the right of the members in office to act` (FALSE when fewer than a quorum are in office) and `s 38 publication in the nearest British Columbia newspaper makes the notice sufficiently given` (FALSE when a newspaper is published in the place, or the notice is not published in the nearest one).
   Each now refuses, by name, in those cases.
   Fourteen pass-1 assertions that expected FALSE there were changed in place to `#ASSERT REFUSED ... BECAUSE` (section "Changes to existing modules" lists them; the old text is quoted there).
   The case that stays FALSE is the one the words give: s 24's fact is not deemed established where there is evidence to the contrary.
   Finding 14 lists every boolean function that was read for the same pattern, and what was found.

3. **Section 2(1) is the caller's step, and the pass-2 rules do not take it as an input.**
   Every provision of the Act applies "unless a contrary intention appears in this Act or in the enactment" (s 2(1)).
   `bc-interpretation-definitions.l4` has the rule (`s 2(1) a provision of this Act applies to an enactment`, from two booleans that the caller supplies).
   The pass-2 rules do not repeat the booleans in every signature.
   A caller who skips the s 2(1) step gets an answer that ignores a contrary intention, and no diagnostic says so (this is the silent failure of section 0).
   Section 2(2) is encoded as TRUE for "this Act", and as a refusal that points at s 2(1) for any other enactment (`s 2(2) speaks only of this Act; s 2(1) governs another enactment`).

4. **The catalogue of defined terms is generated from a curated file, and its generated tests do not check the reading.**
   `gen-terms.py` copies from the text, by line number, the words of each entry, the quotation and the line numbers.
   `terms-data.py` holds my reading of each entry: what it names, leaves out, points at, whether its list is closed, the conditions it carries.
   The 585 assertions of `bc-tests-terms.l4` are generated from `terms-data.py`, so they show that the L4 plumbing says what the data says and they do not show that the data is right.
   The 106 assertions of `bc-tests-terms-rules.l4` are written by hand, with values decided from the text, and carry the independent check.
   A spot check in this pass: flipping the `closed` flag of one entry in the generated catalogue made one assertion refuse, so the generated tests do detect a change to the flag.
   Nobody has compared the curated fields with the official text.

5. **A judgment the text hands to the reader is an input.**
   Which of several constructions "best ensures the attainment of [the] objects" (s 8); whether text in square brackets "is or purports to be descriptive of the subject matter" (s 11(2)); whether regulations are "considered necessary and advisable" and "ancillary" (s 41(1)(a)); whether a power is "necessary" to do an act (s 27(2)); whether a construction "abrogates or derogates from" rights (s 8.1(2)); whether a term "can be applied" (ss 39, 40) are booleans the caller supplies.
   Where the text gives the judgment to no one, nothing is guessed.
   Where two constructions both "best ensure" the objects, or none does, s 8 gives no answer, and the function refuses (`bc-tests-reading.l4`).

6. **The preamble of s 29 prints some cross-references backwards.**
   `["Crown, the", see "Her Majesty"]`, `["King, the", ...]`, `["Queen, the", ...]` and `["Sovereign, the", ...]` are entries of the preamble; the headword they point at is "Her Majesty, His Majesty, the Queen, the King, the Crown or the Sovereign".
   The catalogue keeps the cross-reference as printed ("Crown, the") and the headword's own words ("the Crown") apart: a lookup of "Crown, the" finds the cross-reference (`bc-tests-terms-rules.l4`, line 47), and a lookup of "the Crown" finds the definition.

7. **The Schedule is data, in legs, with no test of a point on the line.**
   The Schedule describes the line called "the Cascade Mountains" (s 29) in one paragraph of 51 "thence" legs and a beginning, so 52 legs (`grep -o thence` on line 449 gives 51).
   `the legs of the Schedule` holds them; the tests assert the count, the first leg and the last leg.
   Nothing in this row decides whether a point lies on, east of or west of the line.
   That needs the watersheds, lots and ranges the paragraph names, and none is in the text.

8. **Definitions are scoped, and two terms are defined twice.**
   "regulation" means one thing in s 1 and, "In this section", the meaning it has in the Regulations Act (s 8.1(1)); the catalogue answers by scope and prefers the narrower scope in its own scope.
   "security" is defined in s 29 twice: "security includes a security as defined in the Securities Act" and, in the entry for "sureties", "security means sufficient security"; both are returned, in the order of the text (`bc-tests-terms-rules.l4`, `count ... EQUALS 2`).

9. **"A majority" is read as more than half.**
   The Act does not define the word.
   See fork F-majority.

10. **A rival reading can be written to fail only when the module gives a value.**
    `check.sh` counts a failed assertion against the expected number for its file, and counts a refused assertion as red.
    Where the module refuses and the rival would give TRUE or FALSE, the assertion of the rival's value is refused, not failed.
    So the open-list rivals (F-open-list, F-pleasure, F-majority) are in the fork register and not in an expected-fail file, and their module-side refusals are asserted in the module's own tests.
    `bc-tests-alt-readings-2-expected-fail.l4` holds the 5 rivals that change a value (F-adm, F-municipality, F-means-closed twice, F-always-speaking).

11. **A spot check of the new tests by mutation.**
    Five single-line changes to the pass-2 modules were made in a scratch copy, one at a time, and the matching test file was run against each: the majority test of s 17(2) changed from "more than half" to "at least half"; the penalty ceiling of s 41(1)(f) from "not greater than" to "less than"; the s 40(2) exception removed; the s 37(2) cell of the grid made unnamed; the s 23(5) exception dropped for the deputy minister.
    Each change made at least one assertion fail or refuse.
    This shows that those tests are sensitive to those branches; it does not show that every branch of every rule is tested.

12. **A duty with no named counterparty.**
    s 23(2) says the official "has the powers and must perform the duties" of the deputy minister.
    The powers are tabled in the Hohfeld table; the duty is not, because the text names no one it is owed to.
    The same holds for s 36(1)(a), where the table names "those the office serves", which is the encoder's inference, not a phrase of the text.

13. **Section 42(1) is encoded as an order, not as a rule about people.**
    `s 42(1) the place of a subdivision in the descending order` and `s 42(1) the subdivision next below` answer from the type `Subdivision of a section` (subsection, paragraph, subparagraph, clause).
    The reading of a reference to a clause in an enactment enacted before 1 July 1974 (s 42(2)) is pass 1's `s 42(2) the subdivision a reference means`.

14. **Every function that returns a BOOLEAN was read for a FALSE that the words do not give.**
    The nine modules hold 172 functions that return a BOOLEAN (`grep -c 'GIVETH A BOOLEAN'` per module, summed); 75 are a bare named refusal and 97 have a body.
    I read the body of each of the 97, after the independent test pass found `s 18(1)`, and did not stop at the functions that say "may".
    Changed to refuse (finding 2): the eight listed there.
    Left as they are, because the words give the negative (the reason in brackets):
    - definitions: `s 1 an instrument is a regulation` and `s 1 a thing is an enactment` (definitions by "means", F-means-closed), `s 2(1)` ("unless"), `s 5(1)` ("has no effect until"), `s 14` ("unless it specifically provides otherwise"; "Despite", F-government), `s 24 the fact is deemed to be established` ("in the absence of any evidence to the contrary"), `s 29 a person is a minor` (a definition), `s 33(1)` (a membership test of a number against the first and last of a series: arithmetic, not a permission), `s 35(1)`, `s 36(1)(a)` ("until another is appointed"), `s 36(1)(e)` ("insofar as they are not inconsistent ... until they are repealed");
    - reading: `s 8.1(2)` ("must be construed as upholding and not abrogating or derogating"), `s 11(1)(a)` ("is not part"), `s 12` ("unless a contrary intention appears"), `s 33(4)` (an identity: the reference "is a reference to" the regulations made under the enactment in which it occurs), `s 39` and `s 40` ("so far as the terms defined can be applied"; "As an exception ... does not apply"), `s 44 the other enactment applies with this change` ("with the necessary changes and so far as it is applicable");
    - commencement: `s 16(1)` ("it is not necessary"), `s 16(3)` ("without being specially pleaded"), `s 20(5)` ("does not apply");
    - periods: `s 25(1)` ("means any of the following", F-means-closed), `s 25(2)` ("unless specifically provided otherwise");
    - powers: `s 21` (two functions that return FALSE: "it is not necessary to renew" and "it is not necessary ... to take an oath of allegiance"; the third, continuing in office, returns TRUE), `s 23(1)` (with s 23(5) "does not authorize"), `s 41(1)(f)` (the ceiling, F-limit-or-scope);
    - replacement: `s 36(1)(b)` ("so far as it may be done consistently"), `s 37` ("must not be construed");
    - catalogue: the definitional functions of `bc-interpretation-terms.l4` (`s 1 an instrument is an Act`, `s 29 a body is a corporation`, `s 29 a publication is a newspaper`, `s 29 territory is a rural area`, `s 29 an instrument is a proclamation`, `s 32(1)` domestic and foreign enactments), which answer by the verb "means" (F-means-closed);
    - time: `s 3(3.1)` (a classifier of facts, with no legal consequence), `s 29 a day is a holiday` (the whole-calendar convention, F-saturday), and the comparisons of dates.
    Not changed, and not a FALSE: `s 17(1)(d)`, `s 41(1)(a)`, `s 41(1)(e)` and `s 24` refuse, as F-limit-or-scope says.
    The remaining 42 of the 97 have no FALSE to give away (a search of each body for `FALSE` and `NOT` found only three hits, below):
    - they return TRUE for the case the provision covers and a named refusal for every other case: `s 3(4)`, `s 5(2)(a)` and `(b)`, `s 20(2)`, `s 17(3)` (its `NOT` is in the condition, with a refusal after it), `s 19(1)` and `(2)`, `s 22`, `s 23(2)` and `(3)`, `s 27(2)`, `(4)`, `(5)` and `(7)`, `s 41(2)`, `s 2(2)`, `s 7(2)`, `s 9` (twice, and the two combined with `s 11(1)(a)`), `s 11(1)(b)` and `s 11(2)`, `s 10`, `s 15(1)` and `(2)`, `s 28(2)` and `(4)`, `s 33(6)`, `s 43`, `s 34`;
    - `s 23(4)` is TRUE whichever way the office stands (its `FALSE` is a case pattern of a `CONSIDER`, not a result), and `s 28(3)` is TRUE for both numbers;
    - four pass on a judgement the caller supplies, as finding 5 says, and so can return FALSE only when the caller says so: `s 8.1(3)`, `s 27(1)`, `s 27(6)` and `s 36(1)(c)` ("as far as it can be adapted");
    - `s 20(1)` is a definition by "means", the conjunction of two inputs (F-means-closed);
    - `a definition scope applies everywhere` in the catalogue is FALSE for the scopes whose lead-in says "In this section" (ss 8.1 and 32) or limits the definitions to treaty first nation matters (s 29.1(1)), which the text gives;
    - the three `a day falls inside ...` functions and `s 25.1 a person has reached an age on a day` compare dates.

15. **The quorum is a whole number of members, and the threshold before rounding is a second function.**
    `s 18(2)` says "at least 1/2" of the fixed number, or of the number in office.
    `s 18(2) the number the members present must reach to constitute a quorum` returns the smallest WHOLE number of members that reaches the threshold: 3 for 5 fixed members, 2 for 3 fixed, 4 for 7 in office, 5 for 10 fixed.
    The fraction (2.5, 1.5, 3.5, 5) is `s 18(2) the threshold of one half, before it is rounded up to a whole number of members`, which the first calls and rounds up with `CEILING`.
    Before this change the first returned the fraction (3.5 for 7), which a client reading the exported number would take as a count of members.
    The comparisons of `s 18(2)(c)` and `(d)` are unchanged in meaning, since a count reaches the fraction exactly when it reaches the whole number above it.
    Where the number of members is outside the authorized limits, or the body has fewer than 3 members, both functions refuse, by name, as before.

## 4. Answer table: the worked cases

Every expected value below was decided by reading the section and written here BEFORE any test was written or run.
"Last day" means the last day of the period, counting the day the text says is counted (see fork F-count).
In every row the period is expressed plainly (no "clear", "at least" or "not less than"), the reference day is BEFORE the period ("from", "after"), and no holiday is in play: s 25(3) is a separate step (section 4.3 below).

### 4.1 Periods

| period | counted from | decided answer (last day) | text that decides it |
| --- | --- | --- | --- |
| three years | 2025-07-16 | 2028-07-16 | s 25.4(1)(a): go forward to and including the date numerically corresponding to the reference day (16 July) in the same calendar month (July) in the year in which the period ends (2028). 16 July 2028 exists, so s 25.4(3) does not apply. |
| five years | 2025-01-15 | 2030-01-15 | s 25.4(1)(a), same reasoning (15 January 2030 exists). |
| five years | 2025-09-01 | 2030-09-01 | s 25.4(1)(a), same reasoning (1 September 2030 exists). |
| thirty days | 2026-01-01 | 2026-01-31 | s 25.2(2)(a): count forward from and including the day after the reference day: 2026-01-02 is day 1, so day 30 is 2026-01-31. The reference day is not counted. |
| two years | 2024-02-28 | 2026-02-28 | s 25.4(1)(a): 28 February 2026 exists. (The leap day 29 February 2024 lies inside the period and is not the reference day, so s 25.4(3) is not engaged.) |
| one year | 2024-02-29 | 2025-02-28 | s 25.4(1)(a) would give 29 February 2025, which does not occur in 2025; s 25.4(3): the period ends on 28 February. |
| one month | 2025-01-31 | 2025-02-28 | s 25.3(1)(a) would give "31 February" 2025, which does not occur; s 25.3(3): the period ends on the last day of that month, 28 February 2025. |

The asymmetry between the first and the other rows is the text's, not an error of this encoding: s 25.2 (days, weeks) COUNTS days and excludes the reference day, so 30 days from 1 January ends on 31 January; ss 25.3 and 25.4 (months, years) GO TO the numerically corresponding date, so one month from 1 January ends on 1 February.
Both agree with the definition of "month" in s 29 once the period is taken to begin on the day after the reference day (fork F-month).

### 4.2 Commencement

| case | question | decided answer | text that decides it |
| --- | --- | --- | --- |
| An Act is passed or published on 2026-03-10 and says nothing about when it comes into force | from what day, and what moment of that day, does it bind, on the text? | If 2026-03-10 is the date of assent: it commences on 2026-03-10, at the beginning of that day in Pacific Time, which is 2026-03-10 07:00 UTC. If 2026-03-10 is only the day it was passed or the day it was published: the text does not say that either is the date of assent, so the text does not answer (named refusal). | s 3(2): the date of commencement of an Act for which no other date is provided is the date of assent; s 4(1): commences at the beginning of the day on which it comes into force; s 26(1)-(2): Pacific Time is 7 hours behind UTC. "Passed" and "published" appear nowhere in ss 3 or 4. |
| An Act says it comes into force on a day to be fixed later; the day is fixed as 2026-06-01 | from what day and moment does it bind? | The portion that is to come into force on the fixed day binds from the beginning of 2026-06-01 in Pacific Time (2026-06-01 07:00 UTC). The provision that fixes the day, and the title of the Act, are deemed to have come into force on the date of assent. Any other portion for which the Act provides no other date commences on the date of assent. | s 3(3) (the provision and the title are deemed in force at assent); s 3(2); s 4(1); s 26. |
| Subordinate legislation is made on 2026-03-10 and says nothing about when it comes into force | from what day does it bind, on the text? | If it is a regulation of a class exempted from the Regulations Act, or to which that Act does not apply: from the day it was enacted, 2026-03-10, at the beginning of that day. If it is any other regulation: the Interpretation Act text does not say (the Regulations Act governs and is not in this text): named refusal. | s 3(5) and s 4(1). s 3(2) cannot apply: it speaks of an Act and the date of assent, and a regulation has neither. |

Each row of 4.1 and 4.2 is an assertion in `bc-tests-time-periods.l4` and `bc-tests-time-commencement.l4`; the dates in the table are the dates in the assertions.

### 4.3 Other decided answers used by the tests

Each row was decided from the text before the file that carries it was first run.
The holiday rows use one test calendar: every Sunday and 26 December (from s 29), plus Friday 2026-04-03, Monday 2026-04-06 and Friday 2026-12-25 supplied by the test.
Weekdays, worked out by hand: 2026-01-31 is a Saturday; 2026-04-03 a Friday, 04-05 a Sunday, 04-06 a Monday; 2026-12-25 a Friday, 12-27 a Sunday.
The office rows use an office open Monday to Friday, shut on Friday 2026-04-03 for a reason that is not its regular closing, and regularly closed on Saturday and Sunday.
"Periods" is `bc-tests-time-periods.l4`, "holidays" is `bc-tests-time-holidays.l4`, "commencement" is `bc-tests-time-commencement.l4`, "words" is `bc-tests-time-words.l4`.

| question | decided answer | text that decides it | tests |
| --- | --- | --- | --- |
| 30 clear days from 2026-01-01 | 2026-02-01 | s 25.2(3)(a): one day later than 2026-01-31 | periods |
| 7 clear days before 2026-01-10 | 2026-01-02 | s 25.2(2)(b) gives 2026-01-03; s 25.2(3)(b): one day earlier | periods |
| 1 clear month from 2026-01-28 | 2026-03-01 | s 25.3(1)(a) gives 2026-02-28; s 25.3(2)(a): one day later | periods |
| 1 clear month before 2026-03-15 | 2026-02-14 | s 25.3(1)(b) gives 2026-02-15; s 25.3(2)(b): one day earlier | periods |
| 1 clear year from 2025-07-16 | 2026-07-17 | s 25.4(1)(a), (2)(a) | periods |
| 1 clear year from 2024-02-28 | 2025-03-01 | s 25.4(2)(a): 2025-02-28 plus a day | periods |
| 1 year before 2026-07-16 begins on | 2025-07-16 | s 25.4(1)(b) | periods |
| 1 clear month from 2025-01-31; 1 clear year from 2024-02-29 | refused (fork F-clear) | ss 25.3(2) and (3), 25.4(2) and (3) | periods |
| a count of 0, -1, 1.5 days, months or years | refused (fork F-whole) | ss 25.2(2), 25.3(1), 25.4(1): "one ... or consecutive" | periods |
| period ends Sunday 2026-04-05, reference day before it | Tuesday 2026-04-07 (Sunday and the supplied Monday are holidays in a row) | s 25(3)(a), s 29 "holiday" (a) | holidays |
| the same, reference day after the period | Saturday 2026-04-04 | s 25(3)(b) | holidays |
| period ends Friday 2026-12-25, reference day before it | Monday 2026-12-28 (25, 26, 27 December are holidays) | s 25(3)(a), s 29 (a), (c) | holidays |
| period ends Sunday 2026-12-27, reference day after it | Thursday 2026-12-24 | s 25(3)(b) | holidays |
| period ends Saturday 2026-01-31 | not moved: Saturday is not in the text's list | s 29 "holiday"; fork F-saturday | holidays |
| 30 days from 2026-03-06, for doing an act | counted end Sunday 2026-04-05, moved to Tuesday 2026-04-07 | ss 25.2(2)(a), 25(3)(a) | holidays |
| 4 weeks from Sunday 2026-03-08; 1 month from 2026-03-05; 1 year from 2025-04-05, each for doing an act | counted end Sunday 2026-04-05, moved to Tuesday 2026-04-07 | s 25(3) names ss 25.2, 25.3 and 25.4 | holidays |
| 1 month before 2026-05-06, for doing an act | begins on Saturday 2026-04-04 (the counted 2026-04-06 and the day before it are holidays) | ss 25.3(1)(b), 25(3)(b) | holidays |
| 1 day from Saturday 2026-04-04, for doing an act | the period is 2026-04-07 only; 2026-04-05 and 2026-04-06 are outside | s 25(3) "begins or ends"; fork F-near-end | holidays |
| 3 days before Tuesday 2026-04-07, for doing an act | the period is 2026-04-04 only | ss 25.2(2)(b), 25(3)(b) | holidays |
| office open Mon to Fri; period ends Saturday 2026-04-04, reference day before | Monday 2026-04-06 | s 25(4)(a) | holidays |
| the same, reference day after the period | Thursday 2026-04-02 (Saturday is regularly closed, Friday is shut) | s 25(4)(b)(i) and (ii) | holidays |
| period ends Friday 2026-04-03 (shut, not regularly closed), reference day after | Monday 2026-04-06 | s 25(4)(b)(i) fails, so (a) applies; fork F-office | holidays |
| day specified Sunday 2026-04-05 (holiday); day specified Saturday 2026-04-04 (office shut) | Tuesday 2026-04-07; Monday 2026-04-06 | s 25.5(1); s 25.5(2) | holidays |
| a calendar in which every day is a holiday | refused after 366 days | s 25(3) has no answer for it | holidays |
| Act assented to 2026-03-10; day known only as "passed" or "published" | refused | ss 3(1), 3(2): only the date of assent counts | commencement |
| Act reserved for the Governor General, signified 2026-04-20 | date of assent 2026-04-20; not yet signified: `NOTHING` | s 3(1) | commencement |
| Act says it comes into force on a day to be fixed, not yet fixed | no day and no moment (`NOTHING`); the provision and the title are in force on the date of assent | s 3(2), s 3(3) | commencement |
| Act says it comes into force on 2026-02-01, assent 2026-03-10 | commences 2026-02-01 and is retroactive | s 3(3.1) | commencement |
| 17:00 Pacific Time on 2026-03-10; 16:59; 23:30; 20:00 on 2026-12-31 | 00:00 UTC on 2026-03-11; 23:59 on 2026-03-10; 06:30 on 2026-03-11; 03:00 on 2027-01-01 | s 26(1): 7 hours behind UTC | commencement |
| beginning of 2026-01-15 | 07:00 UTC (7 hours in winter as in summer; fork F-offset) | s 26(1) | commencement |
| regulation exempt from the Regulations Act, silent, enacted 2026-03-10 | day enacted, 00:00 Pacific Time that day | s 3(5), s 4(1) | commencement |
| any other regulation, silent | refused | s 3(5) does not cover it | commencement |
| regulation expressed to come into force on 2026-05-01 (either class) | 2026-05-01, passed through; no rule in the text says in so many words that the stated day governs (fork F-regulation-silent) | s 3(5) presupposes that a regulation can be so expressed | commencement |
| proclamation dated the day its issue was authorized | that day; any other date, refused | s 16(2) | commencement |
| enactment repealed and replaced, new one commences 2026-09-01 | old one ceases 00:00 Pacific Time on 2026-09-01 | s 4(2) | commencement |
| enactment expires 2026-12-31 | ceases 00:00 Pacific Time on 2027-01-01 (the end of 2026-12-31) | s 4(3) | commencement |
| appointment made by an instrument, effective 2026-03-10 | begins 00:00 on 2026-03-10 | s 20(3) | words |
| appointment ends: day specified 2026-06-30; no day specified and last day of term 2026-06-30; enactment terminates with day 2026-05-15; enactment terminates with no day, made 2026-05-20; terminated and replaced by the same enactment | 00:00 on 2026-06-30; 00:00 on 2026-07-01; 00:00 on 2026-05-15; 00:00 on 2026-05-20; when the new appointment begins | s 20(4)(a) to (e) | words |
| born 2000-05-17, age 18 | reaches it 2018-05-17; has not reached it on 2018-05-16 | s 25.1 | words |
| born 2000-02-29, age 20; age 18 | 2020-02-29; refused (2018 has no 29 February) | s 25.1; fork F-age | words |
| a month beginning 2026-01-15; 2026-01-01; 2024-02-01 | ends 2026-02-14; 2026-01-31; 2024-02-29 | s 29 "month" | words |
| a month beginning 2026-01-31 | refused (fork F-month-def) | s 29 "month" | words |
| a year beginning 2026-07-01; 2023-03-01; the calendar year 2026 | ends 2027-06-30; 2024-02-29; 2026-12-31 | s 29 "year" | words |
| a majority: 5 persons, 3 do it; 5 persons, 2 do it; 4 persons, 2 do it; 2 persons | yes; refused (s 18(1) says what a majority may do and not what fewer may); refused (the same); refused (s 18(1) is for more than 2 persons) | s 18(1) | definitions tests |
| quorum figure: a fixed number of 10, 7, 5 and 3; not a fixed number, 8 in office and 7 in office, within the authorized limits | 5, 4, 3 and 2; 4 and 4 (a whole number of members; the threshold before rounding is 5, 3.5, 2.5, 1.5, 4 and 3.5) | s 18(2)(a), (b) | definitions tests |
| a vacancy and a quorum: 4 in office, a quorum of 5; 5 in office; 6 in office | refused (s 18(2)(d) says nothing below a quorum); the vacancy does not impair; the same | s 18(2)(d) | definitions tests |
| a notice by newspaper: no newspaper in the place and the nearest one used; a newspaper in the place; no newspaper in the place and some other newspaper used | sufficiently given; refused (s 38 speaks only of a place with no newspaper); refused (s 38 does not say that publication elsewhere is not sufficient) | s 38 | definitions tests |
| notice mailed in Canada, postage prepaid, on 2026-03-10 | delivered 2026-03-10; when received: refused | s 29 "deliver", "mail"; fork F-deemed-service | definitions tests |
| enacted 1974-06-30, reference to a clause; enacted 1974-07-01 | means a paragraph; means a clause | s 42(2) | definitions tests |
| penalty 1000 under the former enactment, 500 under the new, imposed after the repeal | 500 (1000 where the new penalty is higher) | s 36(1)(d) | repeal tests |

"definitions tests" is `bc-tests-definitions.l4`; "repeal tests" is `bc-tests-repeal.l4`.


### 4.4 Worked cases of pass 2

Each expected value was decided from the section and written in the test file before that file was first run.
"Refused" means a named refusal asserted with its message.

| question | decided answer | text that decides it | tests |
| --- | --- | --- | --- |
| A corporation acquires land | refused | s 17(1)(d) gives "property other than land for its purposes" and does not take land away (fork F-open-list) | powers |
| 3 of 4 members of a corporation act; 2 of 4; 3 of 3 | bind the others; refused; bind | s 17(2) "A majority of the members" (fork F-majority) | powers |
| A member of a corporation established by an enactment contravenes the enactment | refused | s 17(3) exempts a member "who do[es] not contravene" and does not say what follows for one who does | powers |
| After a demise of the Crown, must a commission be renewed; must an oath be taken | no; no | s 21 "not necessary" twice | powers |
| Words naming a minister, an authority to enact a regulation: the minister designated to act; the deputy; the associate deputy | included; not included; not included | s 23(1), s 23(5) | powers |
| The deputy minister is absent; an assistant deputy minister whom the minister has not authorized | steps in (fork F-adm, reading A); refused for "some other official" the minister has not authorized | s 23(2) | powers; alt-2 rival 1 |
| A regulation sets a penalty of 100, 200, 201 where the Offence Act's greatest is 200 | allowed, allowed, not allowed | s 41(1)(f) "not greater than" | powers |
| A regulation not made by or with the approval of the Lieutenant Governor in Council creates an offence | refused | s 41(1)(e) | powers |
| The enacting clause of an Act uses another form | refused | s 10 "may be in the following form" (fork F-open-list) | reading |
| Italicized descriptive text in square brackets after a reference to a provision | not part of the enactment; added editorially | s 11(1)(a), (b), (2) | reading |
| Two constructions both best ensure the objects; none does | refused; refused | s 8 | reading |
| Amendment, and the inference that the law was different before; consolidation and the inference that the enactment was previously in force | must not be read in; refused (not named) | s 37(2); s 37(1) names repeal, repeal and substitution, and amendment only | replacement (all 30 cells) |
| Exception for "municipality": the Community Charter's; the Local Government Act's | excluded; not excluded (fork F-municipality) | s 40(2) | reading; alt-2 rival 2 |
| An Act is cited by its chapter number in the Revised Statutes: a revised statute in a general revision; a limited revision | allowed; refused | s 43(c), (d) | reading |
| "Something else" as a reference day; as an appointing instrument | FALSE; FALSE (fork F-means-closed) | s 25(1), s 20(1) "means" | periods; commencement; alt-2 rival 3 |
| An appointment is for a fixed term; may be ended at will | refused; refused (fork F-pleasure) | s 20(2) | commencement |
| A proceeding commenced under the former enactment; continuing it is not consistent with the new enactment | must be continued; need not be (FALSE) | s 36(1)(b) "so far as it may be done consistently" | replacement |
| An enactment is read as of | the day it is applied (fork F-always-speaking) | s 7(1) | reading; alt-2 rival 4 |
| A metric expression the Weights and Measures Act (Canada) gives a meaning, and the International System of Units gives another | the Weights and Measures Act's | s 30 "and if not mentioned there" | reading |
| A provision in a private Act, and the Act mentions the right; does not | affects the right only as mentioned; does not affect it | s 6 | reading |
| A term the Act does not define (the test uses "frobnicate") | no definition; membership of a thing in it is refused | s 29 has no such entry | terms-rules |


## Jural relations

One row per provision (units that carry the same relation are grouped), for the whole text.
The table is printed by `python3 -I coverage.py ../../registers/source-bundle/RSBC-1996-c.-238.txt jural` from `jural.tsv`; the command fails if any unit other than a title line or a section heading has no row, or if a row matches no unit.

How to read it.
Kinds are Hohfeld's four pairs: right/duty, privilege/no-right, power/liability, immunity/disability.
The kind names the pair; the relation is stated once, from the holder's side, as a relation between the two parties in the "between" column (holder first, then the other).
It is never written again from the other side.
`none` is for a definition, a rule of reading, a counting or timing rule, or a scope rule: a provision that fixes what other provisions mean and puts no two parties in relation.
The classification is the encoder's reading, not a statement of the text.
The two least certain are s 10 and s 43, which are permissions ("may be in the following form", "may be cited as follows") and are tabled as privileges.
s 11(3), s 29.1(3) and s 29.1(4) are tabled as powers although they are inert (reason 2) in the coverage table: a provision can create a relation and still be machinery for coverage.

| provisions | kind | between | the relation, stated once | note |
| --- | --- | --- | --- | --- |
| Schedule paragraph | none |  |  | a boundary description |
| s 1 | none |  |  | lead-in of definitions |
| s 1 "Act" ... s 1 "repeal" (8 units) | none |  |  | a definition |
| s 2(1) ... s 2(3) (3 units) | none |  |  | says how this Act applies; no party |
| s 3(1) ... s 3(5) (8 units) | none |  |  | a timing rule: the day of commencement |
| s 4(1) ... s 4(4) (4 units) | none |  |  | a timing rule: the moment of commencement or cessation |
| s 5(1) | power/liability | the holder of a power conferred by an enactment that is not yet in force; the person the regulation or thing will affect once it is in force | power to exercise the power before commencement, with no effect until commencement |  |
| s 5(2) ... s 5(2)(b) (3 units) | power/liability | the Lieutenant Governor in Council; the persons subject to the enactment | power to bring provisions into force or repeal them separately and at different times |  |
| s 6 | immunity/disability | a person with rights; the maker of a private Act | immunity of the person's rights from a provision in a private Act, except as the Act refers to or mentions them |  |
| s 7(1) ... s 7(2) (2 units) | none |  |  | a rule of reading |
| s 8 | none |  |  | a rule of reading |
| s 8.1(1) | none |  |  | lead-in of definitions |
| s 8.1(1) "Declaration" ... s 8.1(1) "regulation" (3 units) | none |  |  | a definition |
| s 8.1(2) | none |  |  | a rule of reading |
| s 8.1(3) | none |  |  | a rule of reading |
| s 9 | none |  |  | a rule of reading |
| s 10 | privilege/no-right | the Legislature; everyone | privilege to put the enacting clause of an Act in this form | a permission: nothing in the text gives anyone a right to stop it |
| s 11(1) ... s 11(1)(b) (3 units) | none |  |  | a rule of reading |
| s 11(2) | none |  |  | a rule of reading |
| s 11(3) | power/liability | the Lieutenant Governor in Council; the persons subject to the enactment amended | power to amend an enactment so that a reference to a minister or ministry names the one currently responsible | machinery (inert-2) |
| s 12 | none |  |  | a rule of reading |
| s 13 | none |  |  | a rule of reading |
| s 14(1) | right/duty | those an enactment protects or benefits; the government | duty of the government to comply with an enactment, unless the enactment specifically provides otherwise |  |
| s 14(2) | immunity/disability | the government; the enactment | immunity of the government from an enactment in the use or development of land or improvements | "Despite subsection (1)" |
| s 15(1) ... s 15(2) (2 units) | power/liability | the Legislature; a person granted a power, privilege or advantage by an Act | power to repeal or amend an Act, and to revoke, restrict or modify what it grants, in the same or a later session | s 15(2) is the same power in the same session |
| s 16(1) | privilege/no-right | the issuer of a proclamation; everyone | privilege to omit the mention that it is issued under an order of the Lieutenant Governor in Council | "not necessary" |
| s 16(2) | none |  |  | a deeming rule: the day a proclamation takes effect |
| s 16(3) | right/duty | a party relying on a proclamation; the court | duty of the court to take judicial notice of the issue of the proclamation without pleading |  |
| s 17(1) ... s 17(1)(f) (7 units) | power/liability | a corporation; those who deal with it | power to sue and be sued, to contract, to hold a seal, to hold property other than land, to regulate itself, and to use its name in both forms | capacities |
| s 17(2) | power/liability | a majority of the members of a corporation; the other members and the corporation | power to bind them by its acts |  |
| s 17(3) | immunity/disability | a member of a corporation established by an enactment, who does not contravene the enactment; those with claims on the corporation | immunity of the member from personal liability for the corporation's debts, obligations or acts |  |
| s 18(1) | power/liability | a majority of more than 2 persons who must or may do an act; the others | power to do the act |  |
| s 18(2) | none |  |  | lead-in of the rules for a board |
| s 18(2)(a) | none |  |  | a counting rule: the quorum |
| s 18(2)(b) | none |  |  | a counting rule: the quorum |
| s 18(2)(c) | power/liability | the members present at a meeting, if they are a quorum; the association | power to act for the association by a majority |  |
| s 18(2)(d) | immunity/disability | the members in office; the vacancy | immunity of their right to act from a vacancy, while they are not fewer than a quorum |  |
| s 19(1) | none |  |  | a capacity rule: the office in which a judge or officer exercises a power |
| s 19(2) | power/liability | a person aggrieved by a decision of a court or judge; the decision | power to appeal as in any other proceeding in that court |  |
| s 20(1) | none |  |  | a definition |
| s 20(2) | power/liability | the authority to appoint a public officer; the officer | power to appoint during pleasure | F-pleasure: what "during pleasure" allows is not said |
| s 20(3) | none |  |  | a timing rule |
| s 20(4) ... s 20(4)(e) (6 units) | none |  |  | a timing rule |
| s 20(5) | none |  |  | says where s 4 does not apply |
| s 21 | immunity/disability | a person who held an office or profession under the late Sovereign; the demise of the Crown | immunity of the person's office from a demise of the Crown, with no renewal and no new oath |  |
| s 22 ... s 22(f) (7 units) | power/liability | the authority to appoint a public officer; the officer | power to set the term, terminate, remove or suspend, reappoint, set the remuneration, appoint another or a deputy | an open list |
| s 23(1) | power/liability | a designated minister, or the deputy or associate deputy of a minister; the persons the minister's powers affect | power to do what the words give the minister |  |
| s 23(2) | power/liability | an assistant deputy minister or an authorized official; the persons the deputy minister's powers affect | power to exercise the deputy minister's powers while the deputy minister is absent or unable to act | also a duty to perform the deputy minister's duties; the text names no one it is owed to |
| s 23(3) | power/liability | a person acting for a public officer, or the officer's deputy; the persons the officer's powers affect | power to do what the words give the officer |  |
| s 23(4) | none |  |  | a scope rule: vacancy makes no difference |
| s 23(5) | immunity/disability | a minister's authority to enact a regulation; the minister's deputy or associate deputy | the deputy and the associate deputy lack the authority | a disability |
| s 24 | right/duty | a party relying on a document that an enactment makes evidence or proof of a fact; the court | duty of the court to admit the document and treat the fact as established, absent contrary evidence |  |
| s 25(1) ... s 25(4)(b)(ii) (13 units) | none |  |  | a counting rule |
| s 25.1 ... s 25.5(2) (24 units) | none |  |  | a counting rule |
| s 26(1) ... s 26(2) (2 units) | none |  |  | a counting rule |
| s 27(1) | power/liability | a judge, justice, coroner or public officer; the persons before whom or by whom the thing is done | power to act only where the official's jurisdiction or powers extend |  |
| s 27(2) | power/liability | a person given a power; those the act or thing affects | power to do what is necessary to do or enforce the act or thing |  |
| s 27(3) | none |  |  | a timing rule |
| s 27(4) | power/liability | the maker of regulations; the persons subject to them | power to repeal or amend the regulations and make others |  |
| s 27(5) | power/liability | the Lieutenant Governor in Council or a public officer; those the dependent act affects | power to do the act on which an authorized act depends |  |
| s 27(6) | power/liability | the person with whom an agreement is to be made; the person given the power | power to enter into the agreement and carry out its terms, subject to the conditions that apply to that person |  |
| s 27(7) | power/liability | the person given power to inspect or require records; the holder of the records | power to make copies or extracts |  |
| s 28(1) | immunity/disability | a person who used a prescribed form with deviations that do not affect the substance or mislead; anyone who would challenge its validity | immunity of the form used from invalidity |  |
| s 28(2) | none |  |  | a rule of reading |
| s 28(3) | none |  |  | a rule of reading |
| s 28(4) | none |  |  | a rule of reading |
| s 29 | none |  |  | lead-in of definitions |
| s 29 see calendar year ... s 29 see Treasury (14 units) | none |  |  | a cross-reference |
| s 29 "acquire" ... s 29 "youth custody centre" (108 units) | none |  |  | a definition |
| s 29.1(1) | none |  |  | lead-in of definitions |
| s 29.1(1) "final agreement, except in references to the Nisg̱a'a Final Agreement" ... s 29.1(1) "treaty lands, in relation to a treaty fi" (14 units) | none |  |  | a definition |
| s 29.1(2) | none |  |  | repealed |
| s 29.1(3) | power/liability | the Lieutenant Governor in Council; the treaty first nation and those affected by the definition of its treaty lands | power to make regulations defining treaty lands | machinery (inert-2) |
| s 29.1(4) | power/liability | the Lieutenant Governor in Council; the treaty first nation and those affected | power to define treaty lands by reference to provisions that permit additions or subtractions | machinery (inert-2); the same relation as s 29.1(3) |
| s 29.2(1) | none |  |  | lead-in of definitions |
| s 29.2(1) Nisg̱a'a child ... s 29.2(1) Nisg̱a'a Village Government (9 units) | none |  |  | a definition |
| s 29.2(2) | none |  |  | a definition |
| s 29.2(2) Nisg̱a'a Final Agreement | none |  |  | a definition |
| s 30 | none |  |  | a rule of reading |
| s 31 | none |  |  | a rule of reading |
| s 32(1) | none |  |  | lead-in of definitions |
| s 32(1) "amended, in respect of a domestic enactment" ... s 32(1) "foreign enactment" (5 units) | none |  |  | a definition |
| s 32(2) | none |  |  | a rule of reading |
| s 32(3) | none |  |  | a rule of reading |
| s 32(4) | none |  |  | a rule of reading |
| s 32(5) | none |  |  | a rule of reading |
| s 33(1) ... s 33(6) (6 units) | none |  |  | a rule of reading |
| s 34 | none |  |  | a rule of reading |
| s 35(1) ... s 35(1)(e) (6 units) | immunity/disability | a person holding or owing a right, obligation, penalty, forfeiture or punishment acquired, accrued or incurred under the repealed enactment; the repeal | immunity of those rights and liabilities, and of the previous operation of the enactment, from the repeal | (a) and (b) are the same relation seen at the previous operation |
| s 35(2) | power/liability | the person entitled to institute, continue or enforce an investigation, proceeding or remedy; the person it is brought against | power to proceed as if the enactment had not been repealed | subject to s 36(1) |
| s 36(1) | none |  |  | lead-in of the rules for repeal and replacement |
| s 36(1)(a) | right/duty | those the office serves; a person acting under the former enactment | duty to continue to act as if appointed or elected under the new enactment until another is appointed or elected |  |
| s 36(1)(b) | none |  |  | a continuity rule for proceedings |
| s 36(1)(c) | none |  |  | a procedure rule |
| s 36(1)(d) | right/duty | a person liable to a penalty, forfeiture or punishment that the new enactment reduces; the court | duty of the court to reduce or mitigate it accordingly |  |
| s 36(1)(e) | none |  |  | a continuity rule for regulations |
| s 36(1)(f) | none |  |  | repealed |
| s 36(2) | none |  |  | repealed |
| s 37(1) ... s 37(3) (3 units) | none |  |  | a rule of reading |
| s 38 | power/liability | the person giving the notice; the person to be notified | power to give the notice sufficiently by publication in the nearest British Columbia newspaper |  |
| s 39 | none |  |  | a rule of reading |
| s 40(1) ... s 40(2) (4 units) | none |  |  | a rule of reading |
| s 41(1) ... s 41(1)(f) (7 units) | power/liability | the Lieutenant Governor in Council or any other person who may make regulations; the persons subject to the regulations | power to make the regulations the paragraphs list, including to create an offence and set a penalty | an open list |
| s 41(2) | none |  |  | a status rule: a regulation has the force of law |
| s 42(1) ... s 42(2)(c) (5 units) | none |  |  | a definition of the order of the subdivisions, and a timing rule for references |
| s 43 ... s 43(d) (5 units) | privilege/no-right | anyone citing an Act; everyone | privilege to cite an Act in the ways listed | a permission |
| s 44 | none |  |  | a rule of reading |

## Changes to existing modules

**Four pass-1 files were edited in pass 2, in two rounds, each edit to fix a defect shown against the text, and no module and no test was deleted.**
The defect is the one of finding 2: eight functions answered FALSE where the provision is silent.
The brief lets an existing file change only to fix a defect shown against the text, and says to log it here.
Each function below now refuses, by name, in the cases where it used to answer FALSE; the TRUE cases and the FALSE cases that the words of the provision give are unchanged.
The old lines are quoted here, because the deposit keeps no copy of the files as they were.

First round (before the independent test pass):

| file | function | before | after |
| --- | --- | --- | --- |
| `bc-interpretation-definitions.l4` | `s 24 the document is admissible in evidence in any proceeding` | `providesDocumentIsEvidence AND NOT contextIndicatesConclusive` | a `BRANCH`: refuses `s 24 speaks only of an enactment that provides that a document is evidence or proof of a fact` when the enactment provides no such rule, refuses `s 24 does not say what follows where the context indicates the document is conclusive evidence` when it does, TRUE otherwise |
| `bc-interpretation-definitions.l4` | `s 24 the fact is deemed to be established` | the same two conditions and `AND NOT thereIsEvidenceToTheContrary` | the same two refusals, and otherwise `NOT thereIsEvidenceToTheContrary` (still FALSE where there is evidence to the contrary, which s 24 itself says) |
| `bc-interpretation-definitions.l4` | `s 28(1) the deviation does not invalidate the form used` | `aFormIsPrescribed AND NOT deviationAffectsSubstance AND NOT deviationCalculatedToMislead` | a `BRANCH`: refuses `s 28(1) speaks only of a form prescribed under an enactment` when no form is prescribed, refuses `s 28(1) does not say what follows for a deviation that affects the substance or is calculated to mislead` when it does, TRUE otherwise |
| `bc-interpretation-repeal.l4` | `s 4(4) the enactment is deemed to be repealed for the purposes of this Act` | the condition alone (FALSE when the enactment has not expired) | `IF` the condition `THEN TRUE ELSE` a refusal, `s 4(4) speaks only of an enactment that has expired or otherwise ceased to have effect` |
| `bc-tests-definitions.l4` | six assertions | `#ASSERT NOT (...)` for the cases above | `#ASSERT REFUSED ... BECAUSE "<the message>"` for the same six cases, in the same place |
| `bc-tests-repeal.l4` | one assertion | `#ASSERT NOT (...)` for the unexpired enactment | `#ASSERT REFUSED ... BECAUSE` the message of s 4(4); the file still holds 26 assertions |

Second round (after the independent test pass; the list of what was read is finding 14):

| file | function | before | after |
| --- | --- | --- | --- |
| `bc-interpretation-definitions.l4` | `s 18(1) a majority of the persons may do the act` | for more than 2 persons, `the number of those persons who do it ABOVE (the number of persons DIVIDED BY 2)`, so FALSE for a number that is not a majority | a `BRANCH`: refuses `s 18(1) applies only where more than 2 persons are to do the act` as before, TRUE above half, and otherwise refuses `s 18(1) says what a majority of them may do and does not say what fewer may do` (the same shape as `s 17(2)`) |
| `bc-interpretation-definitions.l4` | `s 18(2) the number the members present must reach to constitute a quorum` | returned the threshold, a fraction (3.5 for 7 members) | returns `CEILING` of `s 18(2) the threshold of one half, before it is rounded up to a whole number of members`, a new function with the old body; the refusals are unchanged (finding 15) |
| `bc-interpretation-definitions.l4` | `s 18(2)(c) the act is deemed to have been done by the association` | `present AT LEAST quorum AND doing ABOVE (present DIVIDED BY 2)` | a `BRANCH`: refuses `s 18(2)(c) speaks only of an act or thing done at a meeting at which the members present constitute a quorum` below a quorum, TRUE with a majority of those present, and otherwise refuses `s 18(2)(c) says what a majority of the members present may do and does not say what fewer may do` |
| `bc-interpretation-definitions.l4` | `s 18(2)(d) a vacancy does not impair the right of the members in office to act` | `in office AT LEAST quorum` | TRUE at or above a quorum, and otherwise refuses `s 18(2)(d) speaks only of a vacancy where the number of members in office is not less than a quorum` |
| `bc-interpretation-definitions.l4` | `s 38 publication in the nearest British Columbia newspaper makes the notice sufficiently given` | `NOT a newspaper is published in the place AND the notice is published in the nearest British Columbia newspaper` | a `BRANCH`: refuses `s 38 speaks only of a notice to be given where no newspaper is published in the particular place at the time` when a newspaper is published there, refuses `s 38 says that publication in the nearest British Columbia newspaper is sufficient and does not say that publication elsewhere is not` when the nearest was not used, TRUE otherwise |
| `bc-tests-definitions.l4` | seven assertions | `#ASSERT NOT (...)` for 2 of 5 and 2 of 4 persons (s 18(1)), no majority and no quorum (s 18(2)(c)), 4 in office against a quorum of 5 (s 18(2)(d)), and the two negative cases of s 38 | `#ASSERT REFUSED ... BECAUSE "<the message>"` for the same cases, in the same place |
| `bc-tests-definitions.l4` | one expected value | a fixed number of 7 members: `EQUALS 3.5` | `EQUALS 4` |
| `bc-tests-definitions.l4` | nine assertions added | | the quorum as a whole number for 5, 3 and 7 in office (3, 2, 4); the threshold before rounding for 5, 3, 7 in office and 10 fixed (2.5, 1.5, 3.5, 5); a meeting below a quorum with a majority of those present; a newspaper in the place and the notice not in the nearest. The file now holds 82 assertions (73 before); the six pass-1 test files that gave 376 satisfied now give 385 |

Four single-line changes to `bc-interpretation-definitions.l4` were made in a scratch copy, one at a time, and `bc-tests-definitions.l4` run against each: the quorum not rounded up, the majority of s 18(1) read as "at least half", the s 18(2)(d) comparison made strict, and the s 38 test of a newspaper in the place switched off.
Each made at least one assertion fail or refuse; the scratch copy was then restored.

The other six files of the baseline (`bc-interpretation-time.l4`, the four `bc-tests-time-*.l4`, `bc-tests-alt-readings-expected-fail.l4`) were not edited: they carry the modification time of the day the deposit was set up (2026-10-29 15:06), earlier than every file written in this pass (the earliest, `units.py`, 15:27); `srcrefs.py` and `BRIEF-pass1.md` too.
`bc-tests-alt-readings-expected-fail.l4` still fails exactly 16 times.

One comment in `bc-interpretation-definitions.l4` named the fork of "regulation" by its pass-1 name, F-regulation-def, which no longer has an entry; it now says F-rendering-order (no code changed).

The new file `bc-tests-definitions-refusals.l4` (4 assertions) asserts the refusals of the two s 24 functions for an enactment that provides no evidence rule, the cases `bc-tests-definitions.l4` did not test.

Other existing files that changed:

| file | change |
| --- | --- |
| `check.sh` | one line added to `expected_failed`: `bc-tests-alt-readings-2-expected-fail.l4` expects 5. Nothing else in the script changed |
| `encoding.json` | version `0.1.0` to `0.2.0`; `scope`, `modules`, `tests`, `files`, `checks`, `l4_bin` rewritten; `not_encoded` removed; `expected_red` unchanged, `expected_red_2` added for the second rival file |
| `SOURCE-LICENSE.md` | rewritten to point at `../../SOURCE-LICENSE.md` and not repeat it (the brief asks for that) |
| `NOTES.md` | rewritten; pass 1's copy is frozen as `NOTES-pass1.md`. After the independent test pass the sections edited were: the module table in section 0, section 1 (counts and table), section 2 (F-clear, F-government, F-saturday, F-deemed-service, F-rendering-order, and the new section "Added after the independent test pass"), section 3 (finding 2 rewritten, findings 14 and 15 added), section 4 (two rows changed, two added), section 5, section 6 (item 3 and "Known limits"), section 7 and this section |
| `PROGRESS.md` | rewritten for pass 2, then updated after the independent test pass |
| `bc-interpretation-terms.l4` | pass 2. The membership rule `s 29 the definition of a term names a thing` refuses with a message chosen by the verb of the entry (three messages; two new named refusals), so a "means" entry is no longer told that "includes" leaves the list open |
| `gen-terms.py`, `bc-tests-terms.l4` | the generator writes the refusal message by the verb of the entry; the 106 generated refusal assertions are 33 for "includes" and "means and includes", 54 for "means", and 19 for the other verbs; the file still holds 585 assertions |
| `bc-tests-terms-rules.l4` | one `BECAUSE` message ("Great Seal", a "means" entry) changed to the message for "means" |
| `bc-tests-periods.l4` | imports `bc-interpretation-time`; two assertions added for the span of 7 days, not clear (2 to 8 January 2026) and clear (2 to 9 January 2026), which pin fork F-clear-ends; the file holds 19 assertions (17 before) |
| `coverage.py`, `coverage-dispositions.tsv` | the fork note of "means and includes" entries names F-means-and-includes; rows moved from encoded to fork for s 17(3) (F-established) and s 24 (F-limit-or-scope); explicit fork rows for s 17(1)(d), s 41(1)(a), (e), (f) and s 29 "affidavit or oath"; the notes of s 25.2(3), s 25.3(3), s 25.4(3), "deliver" and "mail" name the forks added to them |

## 5. What check.sh prints

Run from this directory, with the pinned binary (sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`, computed again just before this run):

```
L4=/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528 L4_TARGET=unstable ./check.sh
```

On stderr:

```
check.sh: the target is unstable, so the main check was skipped.
```

On stdout:

```
module                                    errors satisfied  failed  refused  expected
bc-interpretation-commencement.l4              0         0       0        0         0
bc-interpretation-definitions.l4               0         0       0        0         0
bc-interpretation-periods.l4                   0         0       0        0         0
bc-interpretation-powers.l4                    0         0       0        0         0
bc-interpretation-reading.l4                   0         0       0        0         0
bc-interpretation-repeal.l4                    0         0       0        0         0
bc-interpretation-replacement.l4               0         0       0        0         0
bc-interpretation-terms.l4                     0         0       0        0         0
bc-interpretation-time.l4                      0         0       0        0         0
bc-tests-alt-readings-2-expected-fail.l4       5         0       5        0         5
bc-tests-alt-readings-expected-fail.l4        16         0      16        0        16
bc-tests-commencement.l4                       0        30       0        0         0
bc-tests-definitions-refusals.l4               0         4       0        0         0
bc-tests-definitions.l4                        0        82       0        0         0
bc-tests-periods.l4                            0        19       0        0         0
bc-tests-powers.l4                             0       118       0        0         0
bc-tests-reading.l4                            0       147       0        0         0
bc-tests-repeal.l4                             0        26       0        0         0
bc-tests-replacement.l4                        0        45       0        0         0
bc-tests-terms-rules.l4                        0       106       0        0         0
bc-tests-terms.l4                              0       585       0        0         0
bc-tests-time-commencement.l4                  0        45       0        0         0
bc-tests-time-holidays.l4                      0        81       0        0         0
bc-tests-time-periods.l4                       0       118       0        0         0
bc-tests-time-words.l4                         0        33       0        0         0
TOTAL (25 modules)                            21      1439      21        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit status: 0.

How to read it.
The columns are, per module: error diagnostics, assertions satisfied, assertions failed, assertions refused, and the number of failed assertions `check.sh` expects (`expected_failed`).
Two modules have a non-zero expectation: `bc-tests-alt-readings-expected-fail.l4` (16, pass 1) and `bc-tests-alt-readings-2-expected-fail.l4` (5, pass 2).
Their assertions are rival readings that fail by design, and a failed assertion is also an error, so they show 16 and 5 errors, failed and expected.
Every other module shows 0 errors, 0 failed and 0 refused.
The nine modules (`bc-interpretation-*.l4`) hold no assertions of their own.

**The baseline of pass 1 still holds, and pass 2 adds to it.**
Before any change, `check.sh` with the pass-2 binary printed, for the ten files of pass 1: 376 assertions satisfied (118 periods, 81 holidays, 45 commencement, 33 words, 73 definitions, 26 repeal), 16 failed by design, 0 refused and 0 other errors.
Four of those ten files were edited in this pass (section "Changes to existing modules"): in the first round seven assertions turned from `NOT (...)` into `REFUSED ... BECAUSE` with no change of count, and in the second round seven more did, one expected value changed and nine assertions were added to `bc-tests-definitions.l4`, which now holds 82 (73 before).
So the six pass-1 test files that gave 376 satisfied now give 385, and the 16 failures by design are the same 16.
Pass 2 adds 15 files with 1054 satisfied assertions in all, and 5 failures by design: the total is 1439 satisfied, 21 failed (16 + 5, all by design), 0 refused, in 25 modules.

| test file | what it covers | assertions |
| --- | --- | --- |
| `bc-tests-terms.l4` | one block per catalogue entry, generated from `terms-data.py` (finding 4) | 585 |
| `bc-tests-terms-rules.l4` | the lookup rules, scopes, open and closed lists, the computable definitions, the Schedule | 106 |
| `bc-tests-reading.l4` | ss 2(2), 2(3), 6, 7, 8, 8.1(2), 8.1(3), 9, 10, 11, 12, 13, 15, 28(2) to (4), 30, 31, 33(2) to (6), 39, 40, 42(1), 43, 44 | 147 |
| `bc-tests-powers.l4` | ss 17, 19, 21, 22, 23, 27, 41 | 118 |
| `bc-tests-commencement.l4` | ss 3(4), 5(2), 16(1), 16(3), 20(1), 20(2), 20(5) | 30 |
| `bc-tests-periods.l4` | ss 25(1), 25(2), and the span of 7 clear days (fork F-clear-ends) | 19 |
| `bc-tests-replacement.l4` | ss 34, 36(1)(b), 36(1)(c), 37 (all 30 cells of the grid) | 45 |
| `bc-tests-definitions-refusals.l4` | the refusals of the two s 24 functions for an enactment that provides no evidence rule (finding 2) | 4 |
| `bc-tests-alt-readings-2-expected-fail.l4` | rival readings that change a value, written to fail | 5 |
| (pass 1) `bc-tests-time-periods.l4`, `-holidays.l4`, `-commencement.l4`, `-words.l4`, `bc-tests-definitions.l4`, `bc-tests-repeal.l4`, `bc-tests-alt-readings-expected-fail.l4` | as in pass 1, except that fourteen assertions of the definitions and repeal files now assert a refusal, and `bc-tests-definitions.l4` has nine more | 118, 81, 45, 33, 82, 26, 16 |

Also run, and clean: `python3 -I srcrefs.py check --strict ../../registers/source-bundle/RSBC-1996-c.-238.txt bc-interpretation-*.l4`, which printed `srcrefs check: 581 src: lines, 364 runs, 408 locators, 0 problems`.
The same command with `--refs` in place of `--strict` printed the same line, and both options over `bc-tests-*.l4` print `srcrefs check: 0 src: lines, 0 runs, 0 locators, 0 problems` (the test files carry no quotations).
And `python3 -I coverage.py ../../registers/source-bundle/RSBC-1996-c.-238.txt check` (no unit without a disposition; every `encoded` or `fork` unit's line cited by an `@ref`) and `... jural` (no unit without a row), both with exit status 0.

What this does not show: that the modules read on `main` (target `unstable`), that any answer is what a court would hold, that the quotations match the official text, or that the curated fields of the catalogue are right (finding 4).

## 6. What must be done before relying on this

Nothing here has been put to anyone.
In order of how much it matters:

1. **A domain expert must read the encoding against the official text.** The text used is a script-made rendering, so every quotation, every line number and every entry of the catalogue is the rendering's, and the three entries whose paragraphs the rendering prints after the semicolon (F-rendering-order) are the first to check.
2. **Rule on the forks.** The ones that change an answer most are F-open-list (does an unlisted thing get FALSE or no answer?), F-means-closed, F-adm, F-pleasure, F-municipality, F-majority, F-always-speaking, and the pass-1 forks F-clear, F-assent, F-regulation-silent and F-holiday-scope. Each has its readings and its licensing text in section 2.
3. **Confirm the FALSE / refusal convention.** Finding 2 states it, and F-limit-or-scope gives the readings on either side of the line it draws: FALSE only where the words of the provision give the negative, a named refusal where the text is silent. Eight pass-1 functions were changed to follow it (section "Changes to existing modules"); a reader who prefers FALSE for those cases changes eight functions and fourteen assertions back.
4. **Check the catalogue's curated fields.** The names, leaves, closed flags, conditions and pointers of the 121 entries are my reading (finding 4); the generated tests do not check them.
5. **Apply s 2(1) first.** A caller who does not gets answers that ignore a contrary intention (finding 3).
6. **Run the modules on `main`.** None was; they use `REFUSE`, `YMD` and `#ASSERT REFUSED`, which `main` rejects.
7. **Decide the licence question.** Whether an encoding that quotes the text is within clause 2.2 of the King's Printer Licence is a human decision that `../../SOURCE-LICENSE.md` says must be recorded before an encoding quotes the text; it is undetermined here.
8. **Bring in what the text borrows.** The Regulations Act (which governs the commencement of a regulation that is not exempt), the Evidence Act, the Offence Act (the penalty ceiling of s 41(1)(f) is an input), the Community Charter and Local Government Act schedules, and the other Acts the catalogue points at are not in the text; a borrowed term is asked as a fact.
9. **The Schedule has no geometry** (finding 7).

### Known limits

An independent author, who had not read this file, wrote assertions against the modules and reported 45 gaps: things it wished to ask and could not.
I was given the classes it named, not the 45 one by one.
Each class below was checked against the modules in this pass, and each is a limit of this encoding, not a defect in the text.

- **No "in effect at a moment" predicate.** `the moment from which a portion of an Act binds` and the repeal moment of s 4(2) to (3) are encoded, and nothing combines commencement and repeal to answer "is this enactment in force at moment M" (`grep -n 'in force at' bc-interpretation-time.l4` finds nothing). A caller compares the moments itself.
- **The regulation-making powers of the Lieutenant Governor in Council are not machinery of the encoding.** s 11(3), s 29.1(3) and s 29.1(4) are rows with disposition inert, reason 2 (they authorize the making of regulations and have no condition a function can compute).
- **The calendar names of movable holidays are inputs.** The text names Good Friday, Easter Monday, Victoria Day, Labour Day and others without dates; only Sunday and 26 December are dated (F-saturday). A caller supplies the calendar, and the calendar it passes is the whole calendar (section 0).
- **UTC to Pacific Time is missing.** `s 26 the UTC moment of a Pacific Time moment` converts one way, by adding 7 hours; there is no function from a UTC moment to Pacific Time (`grep -n 'UTC moment' bc-interpretation-time.l4` finds the declaration of the type and this one function).
- **Repealed limbs are not modelled.** s 29 "savings institution" (e), s 29.1(2), s 36(1)(f) and s 36(2) are rows with disposition "repealed or blank in this text"; they are shown in the rendering as "[Repealed ...]" and nothing in the modules refers to them.
- **The Schedule has no coordinates.** It is data in legs; there is no test of a point against the line (finding 7).

### Questions pass 1 raised (unchanged)

Question 12 below is about the paragraphs of "regulation"; with the other two entries it is fork F-rendering-order.

Nothing below has been put to anyone. Each is a place where the text, as rendered, leaves a reading open.

1. **"A period for doing an act" (s 25(3), s 25(4)).** The text does not define the phrase. Which periods in British Columbia law are "for doing an act", so that the holiday rule applies? The module offers both forms and leaves the choice to the caller (fork F-holiday-scope).
2. **Both ends or one (s 25(3) "begins or ends").** Does a holiday on the day next to the reference day move the beginning of a period for doing an act? The module says yes, on the words (fork F-near-end; rival 11 is the other reading).
3. **"Clear" periods that meet a missing date (ss 25.3(2)-(3), 25.4(2)-(3)).** In which order are the one-day shift and the last-day rule applied? The module refuses rather than choose (fork F-clear).
4. **Passed, published, assented (s 3).** Is there a rule elsewhere that a published or passed Act is taken to have received assent on a given day? The text does not have one (fork F-assent).
5. **Pacific Time and daylight saving time (s 26(1)).** The text says 7 hours behind UTC and never mentions daylight saving time. Is a fixed offset what the Act intends for the time of day at which an enactment commences? The module applies 7 hours all year (fork F-offset).
6. **A regulation made part-way through a day (s 3(5) with s 4(1)).** It binds from the beginning of that day, so from a moment before it was made. Is that the intended reading?
7. **A regulation of a class that is not exempt.** Silent on commencement: the Act sends the reader to the Regulations Act, which is not in this text, and the module refuses. Expressing a day: the module passes the stated day through for both classes, with no rule in this text that says the stated day governs (fork F-regulation-silent). Does the Regulations Act add a condition?
8. **Which days are holidays.** The text names most holidays without dates, and lists Saturday nowhere. The caller supplies the calendar (fork F-saturday). Is there a published list a caller should be told to use?
9. **"Month" and "year" that begin on the 29th to 31st (s 29).** The text has no rule for a following month that lacks the number (fork F-month-def). The module refuses.
10. **Receipt of a mailed document (s 29 "mail", "deliver").** The Act has no rule on when a mailed document is received or deemed received. Is the day of deposit the right answer to "when is it delivered"?
11. **s 14(2) against an enactment that says it binds the government.** The module lets s 14(2) win. The text does not say what happens when the enactment says in terms that it binds the government in land use (fork F-government).
12. **The paragraphs of "regulation" (s 1).** The rendering prints the two enacting limbs after the definition. What is the order of the words in the official text, and do (a) and (b) qualify "enacted"? (fork F-rendering-order).
13. **Age of majority (s 29 "minor").** The text uses "the age of majority" and does not give it. The caller supplies it.
14. **Counts of nought, negative or fractional (fork F-whole).** Does any provision outside this text give a meaning to a period of nought days?
15. **"From" and "after" (fork F-position).** Does the case law or practice distinguish them? The text does not, and the module follows the text.
16. **The text itself.** This was written from a script-made plain-text rendering, not from the official consolidation. A reviewer should read the sections quoted in `bc-interpretation-time.l4` against the official text before relying on any answer in it.

## 7. Every refusal in the modules

The cases the text does not answer, each a named `REFUSE` (`grep -n 'REFUSE "' bc-interpretation-*.l4`, taken in this pass).

| module | refusal message |
| --- | --- |
| `commencement` | s 3(4) speaks only of the date of assent and the date of signification |
| `commencement` | s 5(2) speaks only of an enactment to come into force or be repealed on proclamation or by regulation of the Lieutenant Governor in Council |
| `commencement` | s 16(1) speaks only of a proclamation |
| `commencement` | s 16(3) speaks only of an enactment expressed to come into force on proclamation |
| `commencement` | s 20(2) speaks only of an authority under an enactment to appoint a public officer |
| `commencement` | s 20(2) names appointment during pleasure and does not say the authority is only for that |
| `commencement` | s 20(2) does not say what an appointment during pleasure allows: ending it at will, without notice or without cause |
| `commencement` | s 20(5) says where section 4 does not apply and does not say it applies everywhere else |
| `definitions` | s 18(1) applies only where more than 2 persons are to do the act |
| `definitions` | s 18(1) says what a majority of them may do and does not say what fewer may do |
| `definitions` | s 18(2) applies only to a body of 3 or more members |
| `definitions` | s 18(2)(b) does not say what constitutes a quorum when the number of members is outside the authorized maximum or minimum |
| `definitions` | s 18(2)(c) speaks only of an act or thing done at a meeting at which the members present constitute a quorum |
| `definitions` | s 18(2)(c) says what a majority of the members present may do and does not say what fewer may do |
| `definitions` | s 18(2)(d) speaks only of a vacancy where the number of members in office is not less than a quorum |
| `definitions` | s 24 speaks only of an enactment that provides that a document is evidence or proof of a fact |
| `definitions` | s 24 does not say what follows where the context indicates the document is conclusive evidence |
| `definitions` | s 28(1) speaks only of a form prescribed under an enactment |
| `definitions` | s 28(1) does not say what follows for a deviation that affects the substance or is calculated to mislead |
| `definitions` | s 29 does not make a deposit that is outside Canada or without prepaid postage a mailing |
| `definitions` | s 29 does not say when a mailed notice or other document is received |
| `definitions` | s 38 speaks only of a notice to be given where no newspaper is published in the particular place at the time |
| `definitions` | s 38 says that publication in the nearest British Columbia newspaper is sufficient and does not say that publication elsewhere is not |
| `periods` | s 25(1) defines reference day for sections 25.2 to 25.4 only |
| `periods` | s 25(1) names three kinds of reference day and no others |
| `periods` | s 25(2) speaks only of a deed, conveyance or other legal instrument |
| `powers` | s 17(1) lists what a corporation may do and does not say it may do nothing else |
| `powers` | s 17(2) says what a majority of the members may do and does not say what fewer may do |
| `powers` | s 17(2) is not given a number acting that is more than the number of members |
| `powers` | s 17(3) speaks only of a member who does not contravene the enactment that established the corporation |
| `powers` | s 19(1) speaks only of judicial or quasi judicial powers given by an enactment to a judge or officer of a court |
| `powers` | s 19(2) speaks only of an appeal given under an enactment from a person, board, commission or other body to a court or judge |
| `powers` | s 21 speaks only of a person who held or exercised an office or profession in British Columbia during the previous reign, on a demise of the Crown |
| `powers` | s 22 speaks only of words in an enactment authorizing the appointment of a public officer |
| `powers` | s 22 lists the powers such words include and does not say they include no others |
| `powers` | s 23(1) lists whom words naming a minister include and does not say they include no one else |
| `powers` | s 23(2) speaks only of a deputy minister who is absent or unable to act |
| `powers` | s 23(2) names an assistant deputy minister or an official authorized by the minister and no one else |
| `powers` | s 23(3) lists whom words naming a public officer include and does not say they include no one else |
| `powers` | s 27(1) speaks only of a thing that an enactment requires or authorizes to be done by or before a judge, justice, coroner or public officer |
| `powers` | s 27(2) speaks only of the powers necessary to enable the person to do or enforce the doing of the act or thing |
| `powers` | s 27(3) speaks only of a power conferred or a duty imposed |
| `powers` | s 27(4) speaks only of an enactment that confers a power to make regulations |
| `powers` | s 27(4) lists what a power to make regulations includes and does not say it includes nothing else |
| `powers` | s 27(5) speaks only of an act of the Lieutenant Governor in Council or of a public officer on which an authorized act depends |
| `powers` | s 27(6) speaks only of the person given the power to enter into an agreement and the person with whom it is to be made |
| `powers` | s 27(7) speaks only of a power to inspect or to require the production of records |
| `powers` | s 27(7) lists what such a power includes and does not say it includes nothing else |
| `powers` | s 41(1) speaks only of an enactment that provides that the Lieutenant Governor in Council or any other person may make regulations |
| `powers` | s 41(1) lists what a power to make regulations is construed as empowering and does not say it empowers nothing else |
| `powers` | s 41(1)(a) speaks only of regulations that are considered necessary and advisable, ancillary to the enactment and not inconsistent with it |
| `powers` | s 41(1)(e) speaks only of a regulation made by or with the approval of the Lieutenant Governor in Council |
| `powers` | s 41(2) speaks only of a regulation made under the authority of an enactment |
| `reading` | s 2(2) speaks only of this Act; s 2(1) governs another enactment |
| `reading` | s 2(3) speaks only of a rule of construction that is applicable to the enactment and not inconsistent with this Act |
| `reading` | s 6 speaks only of a provision in a private Act |
| `reading` | s 7(2) speaks only of a provision expressed in the present tense |
| `reading` | s 7(2) does not say whether a provision applies to a circumstance that arises while the enactment is not in force |
| `reading` | s 8 names no construction when none is said to best ensure the attainment of the objects |
| `reading` | s 8 does not choose between constructions that equally best ensure the attainment of the objects |
| `reading` | s 8.1(3) speaks only of an Act and a regulation |
| `reading` | s 9 speaks only of the title and the preamble |
| `reading` | s 11(2) speaks only of italicized text in square brackets, after a reference to a provision, that is or purports to be descriptive of the subject matter of the provision |
| `reading` | s 11(1) speaks only of a head note, a reference after the end of a section or division, and text in square brackets |
| `reading` | s 10 says only that the enacting clause of an Act may be in the form given; it does not say that another form is not allowed |
| `reading` | s 12 speaks only of the enactment that contains the definition or interpretation provision |
| `reading` | s 15(2) speaks only of an Act passed in the same session of the Legislature; s 15(1) reserves the power generally |
| `reading` | s 28(2) speaks only of persons of any gender and corporations |
| `reading` | s 28(4) speaks only of another part of speech or grammatical form of a word or expression defined in the enactment |
| `reading` | s 30 gives no meaning to a metric expression that neither the Weights and Measures Act (Canada) nor the International System of Units gives a meaning to |
| `reading` | s 33(2) speaks only of a Part, division, section, schedule, appendix or form |
| `reading` | s 33(3) speaks only of a subsection, paragraph, subparagraph or clause |
| `reading` | s 33(6) says an Act in that reference includes regulations enacted under the authority of that Act; it does not say what else it includes or leaves out |
| `reading` | s 39 speaks only of an enactment relating to legal proceedings |
| `reading` | s 40 speaks only of an enactment relating to municipal and regional district matters |
| `reading` | s 43 says only how an Act may be cited; it does not say that another way is not allowed |
| `reading` | s 44 speaks only of an enactment that provides that another enactment applies |
| `repeal` | s 4(4) speaks only of an enactment that has expired or otherwise ceased to have effect |
| `repeal` | s 36(1) applies only where another enactment is substituted for the repealed one |
| `replacement` | s 34 speaks only of an amending enactment |
| `replacement` | s 36(1)(b) speaks only of a proceeding commenced under the former enactment |
| `replacement` | s 36(1)(c) names three situations in which the procedure of the new enactment is followed and no others |
| `replacement` | s 37 says what must not be read into a repeal, amendment, consolidation, re-enactment or revision and does not say what may |
| `terms` | the Interpretation Act defines no such term in that scope |
| `terms` | the definition does not list the thing: 'includes' leaves the list open, and a meaning given in words is not tested here against a thing |
| `terms` | the definition says what the word means in words and does not list the thing |
| `terms` | the definition gives the meaning in words or by pointing to another enactment, agreement or entry, and does not list the thing |
| `terms` | s 29 defines newspaper only in a provision requiring publication in a newspaper |
| `time` | ss 25.2 to 25.4 count a whole number of one or more days, weeks, months or years |
| `time` | s 25.3 does not say how to shift a clear month by a day when the day numerically corresponding to the reference day does not occur |
| `time` | s 25.4 does not say how to shift a clear year by a day when the reference day is 29 February and the year has none |
| `time` | the holiday calendar supplied has no day free of holidays within a year |
| `time` | the office calendar supplied has no open day within a year |
| `time` | s 29 month: the following month has no day numerically corresponding to the day the month begins on |
| `time` | s 25.1 does not say which day is the anniversary of a birth on 29 February in a year that has none |
| `time` | s 16(2) does not say when a proclamation takes effect if it is not dated the day its issue was authorized |
| `time` | s 3(5) does not say when a regulation of any other class that names no day comes into force |
| `time` | s 3 does not say that the day an Act was passed or published is its date of assent |
| `time` | s 3(5) does not say when a regulation of any other class that names no day comes into force, so no moment can be given |

99 refusals in all.
98 of them are asserted in a test with `#ASSERT REFUSED ... BECAUSE` and their message (checked by matching each message against the `BECAUSE` strings of the `bc-tests-*.l4` files).
The other one, "s 3(5) does not say when a regulation of any other class that names no day comes into force, so no moment can be given" (`bc-interpretation-time.l4`), is asserted as refused without its message (`bc-tests-time-commencement.l4`, line 121, in the section "Regulations (s 3(5))"); it is the only refusal whose message no test pins. Pass 1 wrote that test, and it was left as it was.

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage-dispositions.tsv`, `coverage.py`, `gen-terms.py`, `jural.tsv`, `terms-data.py`, `units.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 549 scenarios, then 27 edge probes (550 to 576) that it wrote after reading the module source, 576 in all.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (532 assertions: 531 scenarios asserted once, and scenario 467 in two parts), ten of them `#ASSERT REFUSED` as written, and ran it against the pass-2 encoding with the pinned unstable binary.
`ANSWERS.md` is not kept in this folder; the scenario numbers in the `-- N [s ..., l.N]` comments of `tests-independent.l4` refer to it, and each assertion carries its provision.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 532 | 501 | 4 | 27 |
| after the repairs below and the reconciliation | 532 | 532 | 0 | 0 |

The 45 scenarios the encoding has no function for are listed in the GAP register at the end of the test file (30 `-- GAP` lines naming 45 scenarios), each with its reason.
All 27 edge probes passed in the first run.
NOTES carries the forks and the repairs: "Added after the independent test pass", "Known limits" and "Changes to existing modules".

**What the 31 first-run disagreements, and six that the repair created, turned out to be.**

- **Three led to a repair (122, 124, 126).**
  `s 18(2) the number the members present must reach to constitute a quorum` returned the raw half (2.5, 1.5, 3.5).
  It now returns a whole number (3, 2, 4), and the raw threshold is a second function.
- **Twenty-one were the author's expectation, not the encoding (27, 57, 79, 99, 101, 114, 115, 117, 137, 160, 164, 167, 313, 316, 318, 319, 340, 407, 447, 509, 517).**
  Each asked what follows outside a provision's stated condition, or whether an "includes" list excludes what it does not name; the section does not say, so the encoding refuses.
- **Seven are genuine forks, registered and kept as the encoding answers:** 235 (a clear month after 31 January; the author's ambiguity A), 374 ("justice" in s 29; ambiguity I), 209 (the first day of "7 clear days", answered 2025-01-02; ambiguity D), 106, 177 and 527 (F-limit-or-scope: when the words mark the edge of a rule, a case outside the edge is a refusal, not `FALSE`) and 112 (`s 17(2)` refused for a minority while `s 18(1)` answered `FALSE` for the same shape).
  The author's own triage called each of these a fork, and said of 177 that the refusal is "the safer answer".
- **Six passed in the first run and refuse now (118, 130, 131, 132, 134, 515), because of the 112 inconsistency.**
  The encoder resolved it toward refusal, as the author's triage suggested was the likelier fix, and its audit found the same shape in `s 18(2)(c)`, `s 18(2)(d)` and `s 38`.
  They now refuse by name: the section says what a majority, a quorum or a listed case may do and does not say what fewer may do (for s 38: "if no newspaper is published ... in the particular place" does not say what follows where one is).
  The author's `N` for these reads "a majority may" as "only a majority may", which the text does not say.

Thirty-four assertions are rewritten in place (`#ASSERT REFUSED`, or the encoding's value for 209) with a `-- RECONCILED` comment above each that quotes the author's original and gives the reason; none is deleted.
The five forks that are new in NOTES (F-clear-ends, F-affidavit, F-established, F-means-and-includes, F-limit-or-scope) and the extensions to F-clear, F-government, F-saturday and F-deemed-service are the encoder's registration of the author's ambiguities A to J.
Separately, the encoder added `bc-tests-alt-readings-2-expected-fail.l4`, five rival readings that change a value and are meant to fail (21 expected failures in all, 16 + 5), and a reason for the new `expected_failed` entry is in NOTES.

**Independence caveat.** At 09:37Z, after the test author's `ANSWERS.md` was last changed (09:33Z) and after it first wrote `tests-independent.l4` (09:27Z), the harness delivered into its session the contents of a backlog file and the paths of four other rows' triage files (AU, CA, SG, UK).
Its tool calls show no read of any of them.

**Check.** `check.sh` with `tests-independent.l4` in the folder, run with `L4_TARGET=unstable` (so not compared with a main build) and the pinned binary `l4-unstable-0528`: 26 modules, 1971 satisfied, 21 failed (the expected 21), 0 refused, run on 2026-10-29.
