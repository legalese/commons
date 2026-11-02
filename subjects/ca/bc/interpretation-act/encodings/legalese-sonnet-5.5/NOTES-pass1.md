# NOTES: the Interpretation Act (British Columbia), RSBC 1996, c. 238, in L4

Row: `legalese-sonnet-5.5`. A single Sonnet 5.5 agent, working alone from `BRIEF.md`, with no subagents and no other encoding to copy from.
Status: **draft**. No domain expert has read it against the statute.

## 0. What this is, and the status of the source

**What it is.**
An English L4 encoding of the Interpretation Act (British Columbia), RSBC 1996, c. 238, written to be reused.
An encoding of any other British Columbia enactment can `IMPORT` `bc-interpretation-time` and ask when a period ends, whether a day falls inside it, what a holiday does to it, and from what day and moment an enactment binds.
It encodes every provision of the text that has a condition a function can compute, and section 1 says why each other provision is left inert.

**The source.**
`RSBC-1996-c.-238.txt` (consolidation current to 2026-10-13; text sha256 `2d0b9b39ee02996f119a4fd91d42f1e1fc3f2446f8482bd6ad90b9ae4a2ce862`, the value `../../registers/source-bundle/RSBC-1996-c.-238.meta.json` records).
It is a plain-text rendering made by a converter script from the King's Printer consolidation.
**It is not the official text, and nothing here is verified against the official text.**
Quotations in the modules are copied from that file by `srcrefs.py` (`-- src:N | ...` lines, `N` a line of the file); `python3 -I srcrefs.py check --strict <the .txt> <module>` confirms that every `@ref` locator spans the lines its quotations come from.
The terms the quoted text carries are in `SOURCE-LICENSE.md`, which points at `../../SOURCE-LICENSE.md`.

One rendering oddity, which appears three times and matters only for the first: the paragraphs (a) and (b) of the definition of "regulation" are printed after the semicolon that ends the definition (src:14-16), and the same happens to "insurance company" (src:257-259) and "final agreement" (src:334-336); see fork F-regulation-def.

**Target compiler: `unstable`.**
The brief mandates `REFUSE` for what the text does not answer, and `main` build 98 rejects `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` and `YMD` (`dialects.md` of the writing-l4-rules skill, rows at lines 168-171).
The brief does not name a target, so this is an inference from that mandate.
`check.sh` defaults to `unstable` here and says so on stderr.
**No run against a `main` build was made**, so nothing here claims these modules read on `main`.

**Pinned binary.**
`/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (checked with `shasum -a 256` before the final run).
`JL4_LIBRARY_PATH` was left unset throughout.
`l4` has no `--version`.

### Modules (reading order; each starts `@lang en`)

| file | imports | what it holds |
| --- | --- | --- |
| `bc-interpretation-time.l4` | `prelude`, `daydate` | the reusable module: counting periods (ss 25.2 to 25.4), what holidays and closed offices do (ss 25(3), 25(4), 25.5, 29 "holiday"), whether a day is inside a period, the moment of commencement in Pacific Time (ss 3, 4, 26), regulations (s 3(5)), proclamations (s 16(2)), appointments (s 20), age (s 25.1), the time words of s 29 |
| `bc-interpretation-definitions.l4` | `prelude`, `daydate` | the definitions and rules that are not about time: ss 1, 2(1), 5(1), 14, 18, 24, 28(1), 29 (deliver, mail, minor), 33(1), 38, 42(2) |
| `bc-interpretation-repeal.l4` | `prelude`, `daydate` | what a repeal does: ss 4(4), 32, 35, 36(1)(a), (d), (e) |

There is no nouns module: each module declares the few types it needs, so that `bc-interpretation-time.l4` stays self-contained.

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

I ran that snippet before writing it here; the three results are the ones in the comments.

**Two things to know before calling it, sorted by how they fail.**
*Loud:* a count that is not one or more whole units, a month or year that cannot be counted as the text says, and every case the text does not answer, return a named `REFUSE` (a warning, and a refused assertion in a test).
*Silent:* the holiday function you pass is used as the whole calendar. It is not topped up with Sundays, so a calendar that omits `s 29 a day is a holiday` leaves a Sunday end alone and returns a plausible, wrong date with no diagnostic (test: `bc-tests-time-holidays.l4`, section "The calendar passed in is the whole calendar").

## 1. Coverage table

Built from the text itself: one row per section and the Schedule, then one row for each repealed sub-provision.
Line numbers are lines of `RSBC-1996-c.-238.txt` as deposited in `../../registers/source-bundle/`; the first line is the line of the section's number and the last is its last non-blank line.
Dispositions are `encoded`, `inert` (with a reason), `repealed or blank in this text` and `not applicable`.
"Encoded" means the part of the section that has a condition a function can compute; the "where / why" column says what is left inert inside it.

Rows: 57 (52 sections and the Schedule, and 4 repealed sub-provisions that sit inside sections already counted). Encoded 25 (some in part: the "where / why" column says which parts are inert); inert 28; repealed or blank in this text 4; not applicable 0.

Items the brief asks for where **the Act is silent**: the meaning of "day" and of "week" outside s 25.2(1); when a mailed or delivered document is received or deemed received; which language version has authority; whether the day an Act is passed or published is its date of assent; what a period of nought or a fractional number of units is; when a regulation of a class that is not exempt, and that names no day, comes into force (the Regulations Act governs); when a resignation by an appointee takes effect.
Each is a named refusal in the code or is said in the fork register; none is defaulted.

| s | heading | lines | disposition | where / why |
| --- | --- | --- | --- | --- |
| 1 | Definitions | 9-17 | encoded | `bc-interpretation-definitions.l4`: "regulation" (the kinds of instrument, the two enacting limbs, the two excluded orders) and "enactment" (Act, regulation, or a portion of either). The other definitions ("Act", "enact", "public officer", "repeal") only widen the words and compute nothing: inert. |
| 2 | Application | 20-22 | encoded | `bc-interpretation-definitions.l4`: s 2(1), a provision applies unless a contrary intention appears in the Act or in the enactment. Inert: s 2(2) (this Act applies to itself) and s 2(3) (rules of construction are not excluded) state scope and conserve other law; neither has a condition to compute. |
| 3 | Date of commencement | 25-32 | encoded | `bc-interpretation-time.l4`: s 3(1) the date of assent (including an Act reserved for the Governor General), s 3(2) the date of commencement, s 3(3) the provision that fixes a later day and the title, s 3(3.1) the retroactive case, s 3(5) a regulation. Inert: s 3(4), "the date of assent or signification is part of the Act", which is a statement about the text of an Act. |
| 4 | Time of commencement or repeal | 35-38 | encoded | `bc-interpretation-time.l4`: s 4(1) the beginning of the day, s 4(2) cessation on repeal and replacement, s 4(3) cessation otherwise. `bc-interpretation-repeal.l4`: s 4(4) an expired enactment is deemed repealed. |
| 5 | Preliminary proceedings and staggered commencement | 41-44 | encoded | `bc-interpretation-definitions.l4`: s 5(1), whether a thing done before commencement has effect on a day. Inert: s 5(2), that a proclamation or regulation may bring provisions into force separately and at different times; the encoding shows that by giving each portion of an Act its own value of "what it says about when it comes into force", and the subsection has no condition of its own. |
| 6 | Effect of private Acts | 47-47 | inert | The text says a provision in a private Act affects no person's rights except as the Act refers to them. That is a rule about what an Act's words reach, not a condition on facts that can be tested by a function with no knowledge of the Act. |
| 7 | Enactment always speaking | 50-51 | inert | A canon of construction: an enactment is "always speaking" and a present-tense provision applies to circumstances as they arise. No condition to compute. |
| 8 | Enactment remedial | 54-54 | inert | A canon of construction: fair, large and liberal interpretation. No condition to compute. |
| 8.1 | Section 35 of Constitution Act, 1982 and Declaration | 57-62 | inert | A canon (construe consistently with section 35 of the Constitution Act, 1982 and with the Declaration), and definitions that point to other Acts that are not in this text. |
| 9 | Title and preamble | 65-65 | inert | A rule that the title and preamble are part of an enactment and assist in explaining it: a canon, with no condition to compute. |
| 10 | Enacting clause | 68-68 | inert | The permitted wording of the enacting clause of an Act. A drafting form, "may be", with no condition to compute. |
| 11 | Reference aids and clarifications | 71-75 | inert | Head notes, references after the end of a section and italicized descriptive text are not part of the enactment (a canon about what counts as text), and a power of the Lieutenant Governor in Council to amend references to a minister or ministry. |
| 12 | Definitions and interpretation provisions | 78-78 | inert | Definitions and interpretation provisions apply to the whole enactment unless a contrary intention appears: a canon of scope. |
| 13 | Application of expressions in enactments to regulations | 81-81 | inert | An expression in a regulation has the meaning it has in the enabling enactment: a canon, with no condition to compute. |
| 14 | Government bound by enactments; exception | 84-85 | encoded | `bc-interpretation-definitions.l4`: s 14(1) and (2), whether an enactment binds the government. The caller says whether the enactment specifically provides otherwise and whether it would bind or affect the government in the use or development of land or of improvements. |
| 15 | Power of repeal and amendment | 88-89 | inert | Every Act is construed as reserving to the Legislature the power to repeal or amend it, and an Act may be amended or repealed in the same session: statements of legislative capacity. |
| 16 | Proclamation | 92-94 | encoded | `bc-interpretation-time.l4`: s 16(2), a proclamation dated the day its issue was authorized takes effect on that day. Inert: s 16(1), that a proclamation need not mention the order, and s 16(3), that judicial notice is taken of the issue of a proclamation (an evidence rule). |
| 17 | Corporate rights and powers | 97-105 | inert | The list of things a corporation may do, and that a majority of its members may bind the others. A statement of capacities, no condition on facts to compute; the second limb is the majority rule of s 18 and is not repeated. |
| 18 | Majority and quorum | 108-113 | encoded | `bc-interpretation-definitions.l4`: s 18(1) a majority of more than 2 persons; s 18(2)(a) and (b) the quorum figure; (c) the act of a majority of those present, if they are a quorum; (d) a vacancy does not impair the right to act while the members in office are not fewer than a quorum. |
| 19 | Powers to judges and court officers | 116-117 | inert | A judge or court officer who exercises judicial powers does so in an official capacity representing the court, and appeals lie as in other proceedings: statements of capacity and of procedure with no condition to compute. |
| 20 | Appointments of officers | 120-129 | encoded | `bc-interpretation-time.l4`: s 20(3) when an appointment begins, s 20(4)(a) to (e) when it ends. Inert: s 20(1) the definition of "appointing instrument", and s 20(2), authority to appoint a public officer is authority to appoint during pleasure. s 20(5), that s 4 does not apply to an appointing instrument or to the enactments in s 20(4)(c) to (e), is respected in meaning and not by call structure: s 20(3) and (4) state their own moments, and they share with s 4(1) only the helper that turns a day into its beginning (00:00 Pacific Time). No function applies the s 4 rule that an enactment commences at the beginning of its day to an appointing instrument. |
| 21 | Demise of Crown | 132-132 | inert | On a demise of the Crown, commissions and appointments continue without renewal and no new oath is needed: a savings rule with no condition to compute. |
| 22 | Included powers | 135-141 | inert | Words that authorize the appointment of a public officer include six listed powers: a rule about what words include. |
| 23 | Powers to act for ministers, deputy ministers and public officers | 144-148 | inert | A minister, deputy minister or public officer includes the person acting for them: a rule about what words include, which depends on facts about offices and not on a computation. |
| 24 | Documentary evidence | 151-151 | encoded | `bc-interpretation-definitions.l4`: s 24, whether a document that an enactment makes evidence or proof of a fact is admissible, and whether the fact is deemed established. |
| 25 | General rules for determining beginning or end of periods of time | 154-166 | encoded | `bc-interpretation-time.l4`: s 25(1) the three kinds of reference day (the caller supplies the reference day and says whether it is before or after the period); s 25(3) the holiday rule for a period for doing an act; s 25(4) the closed-office rule. Inert: s 25(2), that ss 25 to 25.5 also apply to a deed, conveyance or other legal instrument unless it provides otherwise, which is a statement of scope: the functions do not look at what instrument the period comes from. |
| 25.1 | Calculation of age | 169-169 | encoded | `bc-interpretation-time.l4`: the day a person reaches an age expressed in years, and whether a person has reached an age on a day. A birth on 29 February in a year without one is refused. |
| 25.2 | Determining the beginning or end of periods of days or weeks | 172-178 | encoded | `bc-interpretation-time.l4`: periods of days and weeks, plain and "clear"; the week is 7 consecutive days (s 25.2(1)). |
| 25.3 | Determining the beginning or end of periods of months | 181-187 | encoded | `bc-interpretation-time.l4`: periods of months, plain and "clear", including the date that does not occur in the month (s 25.3(3)). |
| 25.4 | Determining the beginning or end of periods of years | 190-196 | encoded | `bc-interpretation-time.l4`: periods of years, plain and "clear", including 29 February (s 25.4(3)). |
| 25.5 | If day specified is holiday or office closed | 199-200 | encoded | `bc-interpretation-time.l4`: s 25.5(1) a day specified for doing an act that is a holiday, s 25.5(2) the same for a day on which a business office is not open. |
| 26 | Pacific Time | 203-204 | encoded | `bc-interpretation-time.l4`: Pacific Time as 7 hours behind UTC (s 26(1)), and the conversion from a Pacific Time moment to a UTC moment; s 26(2) is the reason the moment of commencement is read in Pacific Time. |
| 27 | Ancillary powers | 207-213 | inert | Ancillary powers: powers needed to do the thing, powers exercised from time to time, powers to amend regulations. Rules about what a grant of power includes; no condition to compute. |
| 28 | Use of forms and words | 216-219 | encoded | `bc-interpretation-definitions.l4`: s 28(1), whether a deviation from a prescribed form invalidates the form used. Inert: s 28(2) to (4), gender, singular and plural and other grammatical forms, which are canons about words. |
| 29 | Expressions defined | 222-330 | encoded | `bc-interpretation-time.l4` and `bc-interpretation-definitions.l4`: "commencement", "now", "month", "year" (and the calendar year), "holiday" (Sunday, 26 December and the caller's other holidays), "deliver", "mail", "minor". Inert: all the other definitions (the rest of the section): they point to other Acts, to offices, or to the meaning of an ordinary word ("land", "person", "record", "writing"), and none has a condition that a function could compute. "Registered mail includes certified mail" and "shall is to be construed as imperative" are examples. The caller supplies the age of majority, which this text does not give. |
| 29.1 | Definitions in relation to treaty first nations | 333-350 | inert | Definitions for treaty first nation matters: each points to another Act, to an agreement or to a regulation, or is "prescribed". Nothing to compute. s 29.1(2) is repealed (see the last rows of this table). |
| 29.2 | Definitions in relation to Nisg̱a'a Final Agreement | 353-354 | inert | Nisg̱a'a definitions that take their meaning from the Nisg̱a'a Final Agreement or its Act: a cross-reference, with nothing to compute. |
| 30 | Metric expressions | 357-357 | inert | Metric expressions have the meaning given in the Weights and Measures Act (Canada) or the International System of Units: a cross-reference to law outside this text. |
| 31 | Common names | 360-360 | inert | The name commonly applied to a body or thing means that body or thing: a canon about names. |
| 32 | References to enactments | 363-372 | encoded | `bc-interpretation-repeal.l4`: which day's text of a named enactment a reference is to: an amended domestic enactment (the text as amended, for a subsequent transaction), a domestic enactment repealed and not replaced (as it read immediately before its repeal), a foreign enactment (as it read on the day the British Columbia enactment was enacted). |
| 33 | References in enactments | 375-380 | encoded | `bc-interpretation-definitions.l4`: s 33(1), a series referred to by its first and last numbers or letters includes both. Inert: s 33(2) to (6), which say which Part, section or regulation a reference points to; they resolve names, and need the enactment itself. |
| 34 | Amending enactment part of enactment amended | 383-383 | inert | An amending enactment is part of the enactment it amends: a rule about how to read a text. |
| 35 | Repeal | 386-392 | encoded | `bc-interpretation-repeal.l4`: s 35(1)(a) to (e), what a repeal does not do, and s 35(2), on what basis an investigation, proceeding or remedy goes on. |
| 36 | Repeal and replacement | 395-402 | encoded | `bc-interpretation-repeal.l4`: s 36(1)(a), (d) and (e). Inert: s 36(1)(b) and (c), that proceedings go on under the new enactment "so far as it may be done consistently with the new enactment" and that the new procedure is followed "as far as it can be adapted": each turns on a judgment of consistency or adaptability that a function with no knowledge of the two enactments cannot make. s 36(1)(f) and s 36(2) are repealed (see the last rows). |
| 37 | No implications from repeal, amendment, etc. | 405-407 | inert | A repeal, substitution or amendment is not a declaration about the previous state of the law, and does not adopt a judicial construction: a canon about inferences. |
| 38 | Notice by newspaper | 410-410 | encoded | `bc-interpretation-definitions.l4`: s 38, when notice by publication in a newspaper of the particular place may be given by publication in the nearest British Columbia newspaper. |
| 39 | Application of definitions in Supreme Court Act to other enactments | 413-413 | inert | The definitions section of the Supreme Court Act extends to enactments about legal proceedings: a cross-reference to another Act. |
| 40 | Definitions in Community Charter and Local Government Act apply to other enactments | 416-419 | inert | Definitions in the Community Charter and the Local Government Act apply to enactments about municipal and regional district matters: a cross-reference to other Acts. |
| 41 | Powers to make regulations | 422-429 | inert | What an enactment that lets regulations be made empowers the maker to do (six listed powers) and that a regulation has the force of law: rules about what a grant of power includes. |
| 42 | Subdivisions of Act | 432-436 | encoded | `bc-interpretation-definitions.l4`: s 42(2), what a reference to a clause, paragraph or subparagraph means in an enactment enacted before 1 July 1974. s 42(1), the order of the subdivisions, is a list of names that the type `Subdivision of a section` spells out. |
| 43 | Citation of Acts | 439-443 | inert | The ways in which an Act may be cited: a rule about citation with no condition to compute. |
| 44 | Mutatis mutandis | 446-446 | inert | Where an enactment provides that another applies, it applies with the necessary changes and so far as applicable: a canon. |
| Schedule | Schedule | 448-449 | inert | The legal description of the line called "the Cascade Mountains" in s 29: a boundary traced by watersheds, lots and ranges. It can be quoted but not computed on; it is not a time rule and nothing in this encoding asks where the line runs. |
| 29.1(2) | Definitions in relation to treaty first nations (sub-provision) | 348-348 | repealed or blank in this text | The text shows "(2) [Repealed 2011-11-42.]". Nothing to encode. |
| 29 "savings institution" (e) | Expressions defined (sub-provision) | 316-316 | repealed or blank in this text | The text shows "(e) [Repealed 2004-23-21.]". Nothing to encode; the list still has items (a) to (d). |
| 36(1)(f) | Repeal and replacement (sub-provision) | 401-401 | repealed or blank in this text | The text shows "(f) [Repealed 2018-5-6.]". Nothing to encode. |
| 36(2) | Repeal and replacement (sub-provision) | 402-402 | repealed or blank in this text | The text shows "(2) [Repealed 2018-5-6.]". Nothing to encode. |

## 2. Fork register

Each fork: the readings seen, the one taken, the text that licenses each, and where it is tested.
"Rival n" is a numbered section of `bc-tests-alt-readings-expected-fail.l4`, where the rival reading is written as an expectation that is meant to fail (16 assertions in all).
Where I looked and found nothing is said under "Where I looked", after the forks.

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
- Tested: `bc-tests-time-periods.l4`, worked cases in section 3.1.

**F-clear. "Clear", "at least", "not less than": which order do the shifts and the date rule apply in?**
- ss 25.3(2) and 25.4(2) shift the date found under (1) by one day (later going forward, earlier going back). ss 25.3(3) and 25.4(3) then say the date "determined under subsection (1) or subsections (1) and (2), as applicable" is replaced if it "would fall on a date that does not occur".
- Where the date of (1) occurs, the shift is plain arithmetic, and the module does it: 1 clear month from 2026-01-28 ends 2026-03-01 (28 February plus a day); 1 clear year from 2025-07-16 ends 2026-07-17; 1 clear year from 2024-02-28 ends 2025-03-01.
- Where the date of (1) does not occur, there are two readings that differ. (i) Replace the date by the last day of the month, then shift: 1 clear month from 2025-01-31 ends 2025-03-01. (ii) Shift first and test the result: "one day later than 31 February" does not name a day, and the text gives no way to say whether it is the last day of February or the day after it. The text does not choose between the readings.
- Taken: **REFUSE**, by name (`s 25.3 does not say how to shift a clear month by a day when the day numerically corresponding to the reference day does not occur`; the year version names 29 February).
- Tested: `bc-tests-time-periods.l4`, the refused assertions under "clear". Rival 4 covers the reading that "clear" adds nothing, for days.

**F-whole. A count of nought, a negative count, a fraction.**
ss 25.2(2), 25.3(1) and 25.4(1) speak of "one day or consecutive days", "one month or consecutive months", "one year or consecutive years". Nought, a negative or a fractional count is not such a period, and the text says nothing about it.
Taken: **REFUSE** (`ss 25.2 to 25.4 count a whole number of one or more days, weeks, months or years`). A week count is turned into days first, so half a week (3.5 days) is refused too.
Tested: `bc-tests-time-periods.l4`, last section.

### Holidays and closed offices

**F-holiday-scope. Does the holiday rule reach months and years, or only days?**
- s 25(3) names "section 25.2, 25.3 or 25.4", so on its words it reaches days, weeks, months and years.
- It applies only to "a period for doing an act". The text does not define that phrase. A period that is not for doing an act (for example, how long a thing lasts) is not moved.
- Taken: the module offers both forms. The plain functions never move a day. The functions named `... for doing an act` take the caller's calendar and move the ends. Which form a period needs is for the caller to decide, and is an open question (section 5).
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
Whether the Act intends something else is a question for a domain expert (section 5). Rival 8 puts the offset at 8 hours in winter (the figure 8 is not from the text).

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
- A regulation of EITHER class that is expressed to come into force on a particular day: the module passes that day through (2026-05-01 in the test). This is not refused, and it is not licensed by a rule in this text either: s 3(5) only presupposes that a regulation can be so expressed, and the Regulations Act, which is not in the text, may add conditions (deposit or publication, say). Refusing it would make the module unable to answer a question whose answer the text's own wording assumes; passing it through is registered here, and listed in section 5, so that it is a reviewed reading and not an unnoticed default.
- A regulation enacted in the middle of a day binds from the beginning of that day. That is what s 3(5) and s 4(1) say together; it is a surprising result, so it is listed in section 5.
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

**F-regulation-def. The order of the words of "regulation".**
In the rendering, paragraphs (a) "in execution of a power conferred under an Act" and (b) "by or under the authority of the Lieutenant Governor in Council" follow the semicolon (src:14-16). On its face they qualify "enacted". The encoding reads them so: an instrument is a regulation when it is of a listed kind, is enacted (a) in execution of a power under an Act or (b) by or under the authority of the Lieutenant Governor in Council, and is not one of the two excluded orders. The rendering is not the official text; a reviewer should look at the official order of the words.

**F-government. s 14(2) against "specifically provides otherwise" in s 14(1).**
s 14(2) opens "Despite subsection (1)", and an enactment that would bind or affect the government in the use or development of land does not bind it. Taken: s 14(2) wins over an enactment's own provision that it binds the government; there is no input for "specifically provides that it DOES bind in land use". Tested in `bc-tests-definitions.l4`. The text does not address the case where the enactment says it does; section 5.

**F-contrary-intention. s 2(1).**
A provision of the Act applies "unless a contrary intention appears in this Act or in the enactment". Taken: the caller decides whether a contrary intention appears, as two booleans; the function does not search the text of the enactment.

**F-language. Which language version has authority.**
The text has no provision on the language of an enactment. The brief says British Columbia enacts and publishes only in English, and `../../SOURCE-LICENSE.md` says the same; neither is a statement in the Act, and no provision of the text is encoded on this. s 17(1)(f) mentions an English and a French form of a corporation's name, which concerns names, not versions of an enactment.

**F-target. The compiler.**
Not a fork in the law: `unstable`, for the reason in section 0.

### Where I looked and found nothing

- "Day": the text has no definition of "day" or of "week" outside s 25.2(1) ("week means a period of 7 consecutive days"). s 29 defines "month" and "year" but not "day" or "week". The Act is silent on the meaning of "day" beyond how ss 4(1), 20(3), 20(4) and 25.2 use it (a day has a beginning and an end).
- Deemed receipt of a mailed or delivered document: no rule (above).
- Recess and days of rest other than Sunday: s 29 has "holiday" only; the words "recess" and "rest" do not appear in the text. Searched with `grep -n -i -E 'recess|day of rest' RSBC-1996-c.-238.txt` (no match; checked just before this table was written).
- Revival of a repealed enactment: s 35(1)(a) says a repeal does not revive an enactment or thing not in force; the text has no rule on revival by the repeal of the repealing enactment.
- Which Act or rule governs the commencement of a regulation of a class that is not exempt: the Regulations Act, which is not in the text.

## 3. Answer table: the worked cases

Every expected value below was decided by reading the section and written here BEFORE any test was written or run.
"Last day" means the last day of the period, counting the day the text says is counted (see fork F-count).
In every row the period is expressed plainly (no "clear", "at least" or "not less than"), the reference day is BEFORE the period ("from", "after"), and no holiday is in play: s 25(3) is a separate step (section 3.3 below).

### 3.1 Periods

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

### 3.2 Commencement

| case | question | decided answer | text that decides it |
| --- | --- | --- | --- |
| An Act is passed or published on 2026-03-10 and says nothing about when it comes into force | from what day, and what moment of that day, does it bind, on the text? | If 2026-03-10 is the date of assent: it commences on 2026-03-10, at the beginning of that day in Pacific Time, which is 2026-03-10 07:00 UTC. If 2026-03-10 is only the day it was passed or the day it was published: the text does not say that either is the date of assent, so the text does not answer (named refusal). | s 3(2): the date of commencement of an Act for which no other date is provided is the date of assent; s 4(1): commences at the beginning of the day on which it comes into force; s 26(1)-(2): Pacific Time is 7 hours behind UTC. "Passed" and "published" appear nowhere in ss 3 or 4. |
| An Act says it comes into force on a day to be fixed later; the day is fixed as 2026-06-01 | from what day and moment does it bind? | The portion that is to come into force on the fixed day binds from the beginning of 2026-06-01 in Pacific Time (2026-06-01 07:00 UTC). The provision that fixes the day, and the title of the Act, are deemed to have come into force on the date of assent. Any other portion for which the Act provides no other date commences on the date of assent. | s 3(3) (the provision and the title are deemed in force at assent); s 3(2); s 4(1); s 26. |
| Subordinate legislation is made on 2026-03-10 and says nothing about when it comes into force | from what day does it bind, on the text? | If it is a regulation of a class exempted from the Regulations Act, or to which that Act does not apply: from the day it was enacted, 2026-03-10, at the beginning of that day. If it is any other regulation: the Interpretation Act text does not say (the Regulations Act governs and is not in this text): named refusal. | s 3(5) and s 4(1). s 3(2) cannot apply: it speaks of an Act and the date of assent, and a regulation has neither. |

Each row of 3.1 and 3.2 is an assertion in `bc-tests-time-periods.l4` and `bc-tests-time-commencement.l4`; the dates in the table are the dates in the assertions.

### 3.3 Other decided answers used by the tests

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
| a majority: 5 persons, 3 do it; 4 persons, 2 do it; 2 persons | yes; no; refused (s 18(1) is for more than 2 persons) | s 18(1) | definitions tests |
| quorum figure: a fixed number of 10; a fixed number of 7; not a fixed number, 8 in office, within the authorized limits | 5; 3.5 (so 4 members present are a quorum and 3 are not); 4 | s 18(2)(a), (b) | definitions tests |
| notice mailed in Canada, postage prepaid, on 2026-03-10 | delivered 2026-03-10; when received: refused | s 29 "deliver", "mail"; fork F-deemed-service | definitions tests |
| enacted 1974-06-30, reference to a clause; enacted 1974-07-01 | means a paragraph; means a clause | s 42(2) | definitions tests |
| penalty 1000 under the former enactment, 500 under the new, imposed after the repeal | 500 (1000 where the new penalty is higher) | s 36(1)(d) | repeal tests |

"definitions tests" is `bc-tests-definitions.l4`; "repeal tests" is `bc-tests-repeal.l4`.

## 4. What check.sh prints

Run from this directory, with the pinned binary (sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`, computed again just before this run):

```
L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 ./check.sh
```

On stderr:

```
check.sh: the target is unstable, so the main check was skipped.
```

On stdout:

```
module                                    errors satisfied  failed  refused  expected
bc-interpretation-definitions.l4               0         0       0        0         0
bc-interpretation-repeal.l4                    0         0       0        0         0
bc-interpretation-time.l4                      0         0       0        0         0
bc-tests-alt-readings-expected-fail.l4        16         0      16        0        16
bc-tests-definitions.l4                        0        73       0        0         0
bc-tests-repeal.l4                             0        26       0        0         0
bc-tests-time-commencement.l4                  0        45       0        0         0
bc-tests-time-holidays.l4                      0        81       0        0         0
bc-tests-time-periods.l4                       0       118       0        0         0
bc-tests-time-words.l4                         0        33       0        0         0
TOTAL (10 modules)                            16       376      16        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Exit status: 0.

How to read it.
The columns are, per module: error diagnostics, assertions satisfied, assertions failed, assertions refused, and the number of failed assertions `check.sh` expects (`expected_failed`).
The only module with a non-zero expectation is `bc-tests-alt-readings-expected-fail.l4`: its 16 assertions are rival readings that fail by design, and a failed assertion is also an error, so it shows 16 errors, 16 failed and 16 expected.
Every other module shows 0 errors, 0 failed and 0 refused.
Satisfied assertions per file are 118 (periods), 81 (holidays), 45 (commencement), 33 (words), 73 (definitions) and 26 (repeal), 376 in all.
The three modules (`bc-interpretation-*.l4`) hold no assertions of their own.

| test file | what it covers | assertions |
| --- | --- | --- |
| `bc-tests-time-periods.l4` | the counting rules of ss 25.2 to 25.4, the four named wrappers, spans, inside and outside, and counts that are not whole | 118 |
| `bc-tests-time-holidays.l4` | ss 25(3), 25(4), 25.5, s 29 "holiday", holidays in a row, near and far ends, a calendar with no free day, and the whole-calendar convention | 81 |
| `bc-tests-time-commencement.l4` | ss 3, 4, 16(2), 26, regulations, the moment of commencement | 45 |
| `bc-tests-time-words.l4` | s 29 "month" and "year", s 25.1 age, s 20 appointments | 33 |
| `bc-tests-definitions.l4` | ss 1, 2(1), 5(1), 14, 18, 24, 28(1), 29 deliver/mail/minor, 33(1), 38, 42(2) | 73 |
| `bc-tests-repeal.l4` | ss 4(4), 32, 35, 36 | 26 |
| `bc-tests-alt-readings-expected-fail.l4` | rival readings, written as expectations that are meant to fail | 16 |

Also run, and clean: `python3 -I srcrefs.py check --strict ../../../../../registers/source-bundle/RSBC-1996-c.-238.txt <module>` on each of the three modules (every quotation block's `@ref` locators span the lines it quotes); the paths there are those of the working directory of the run, which is not part of the deposit.

What this does not show: that the modules read on `main` (target `unstable`), that any answer is what a court would hold, or that the quotations match the official text.

## 5. Open questions for a domain expert

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
12. **The paragraphs of "regulation" (s 1).** The rendering prints the two enacting limbs after the definition. What is the order of the words in the official text, and do (a) and (b) qualify "enacted"? (fork F-regulation-def).
13. **Age of majority (s 29 "minor").** The text uses "the age of majority" and does not give it. The caller supplies it.
14. **Counts of nought, negative or fractional (fork F-whole).** Does any provision outside this text give a meaning to a period of nought days?
15. **"From" and "after" (fork F-position).** Does the case law or practice distinguish them? The text does not, and the module follows the text.
16. **The text itself.** This was written from a script-made plain-text rendering, not from the official consolidation. A reviewer should read the sections quoted in `bc-interpretation-time.l4` against the official text before relying on any answer in it.
