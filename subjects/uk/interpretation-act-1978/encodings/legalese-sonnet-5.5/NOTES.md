# NOTES: Interpretation Act 1978 (1978 c. 30), row `legalese-sonnet-5.5`

Status: draft. Written by a single Sonnet 5.5 agent working alone from `BRIEF.md`; no domain expert has read it against the statute (see `encoding.json`, `not_reviewed`).

## The source is a converter rendering, not the official text

The only source is `../../registers/source-bundle/ukpga-1978-30.txt`: a plain-text rendering made by a converter script from https://www.legislation.gov.uk/ukpga/1978/30/data.xml (version of 2026-01-01).
It is not the official text and it is not marked up.
Nothing here is claimed to be "verified against the official text".
The `.meta.json` beside it, `../../registers/source-bundle/ukpga-1978-30.meta.json`, records its hashes: text sha256 `e6d0e2422aca474ecf24aa71ed164ed40e73a02e2ad8fe834749f00f1936e64b`, which I re-computed with `shasum -a 256` and found equal.
Quotations in the `.l4` files are `-- src:N | ...` lines produced by `srcrefs.py quote` from that file, and `python3 -I srcrefs.py check --refs` reads them back against it.
The licence note is `SOURCE-LICENSE.md`, which points at `../../SOURCE-LICENSE.md` (Open Government Licence v3.0).

## The target compiler is `unstable`, and why

The brief mandates `@lang en` on every module, `REFUSE` for what the source does not answer, and `#ASSERT REFUSED ... BECAUSE` for testing a refusal.
The `main` compiler rejects each of these (`references/dialects.md` of the writing-l4-rules skill: probe 01 `@lang` is rejected with `unexpected '@'`; probe 02 `REFUSE` with `I could not find a definition for the identifier REFUSE`; probe 03 `REFUSED`; probe 04 `BECAUSE` with `unexpected BECAUSE`; probe 05, `YMD`, which `daydate` users need for a bounds-checked date, is rejected too).
So the target is `unstable`, and `check.sh` is run as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`.
`check.sh` then skips its comparison with a main build, and says so on stderr; no main build was compared.
The binary is `/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4`, sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7` (re-computed); its `--version` prints `dev`, and it behaves as unstable.
`JL4_LIBRARY_PATH` was unset for every run (`env -u JL4_LIBRARY_PATH`).

A conflict between the brief and the skill, noted rather than resolved silently: the writing-l4-rules skill says never to write `@lang en`, and the compiler agrees with a Hint (`A module that declares nothing is English; this line can go.`) on every module.
The brief says every module starts with `@lang en`, so every module does, and every module carries that one Hint and no other diagnostic.

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
| `uk-interpretation-time.l4` (imports only `prelude` and `daydate`) | s 4 commencement (day and moment); s 4(a), 4(b) reach; s 9 time standard; s 13 anticipatory exercise; s 26 and the commencement day; Sch 1 "Month", "Financial year", "Commencement"; named refusals for the six time-computation items | `tests-time.l4` |
| `uk-interpretation-service.l4` | s 7 deemed service by post, and the deemed time | `tests-service.l4` |
| `uk-interpretation-repeals.l4` | ss 2, 15, 16, 17 | `tests-repeals.l4` |
| `uk-interpretation-construction.l4` | ss 3, 6, 8, 10, 11, 12, 14, 14A, 18, 19, 20(1), 20(2), 21 | `tests-construction.l4` |
| `uk-interpretation-application.l4` | ss 5, 22, 23, 25 and Sch 2 (Parts I and II), with Sch 1's year and date marks as Sch 2 para 4 reads them | `tests-application.l4` |
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

## What is not encoded

See the coverage table; the inert rows carry the reasons.
In short: the devolution and withdrawal provisions (ss 20(2A) to 20A, 23ZA, 23A, 23B, 23C, 24) turn on Acts that are not among the sources and on dates the text points at without giving; Schedule 1's definitions are cross-references or institutions; s 1 and s 27 give nothing to decide; Schedule 3 shows no rows in this text.

## Coverage table

One row per section and per schedule, and one per definition of Schedule 1, built from the text by a script that checks that every non-blank line of the text falls in some row.
Dispositions: `encoded`, `inert` (with a reason), `repealed or blank in this text` (what the text shows), `not applicable` (none were needed).

Legend for the Schedule 1 codes: A, defined by pointing at another Act or instrument that is not among the sources; B, names an institution, court or office; C, names a territory or a legislature; D, a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code); E, EU-withdrawal vocabulary that depends on texts not among the sources.
A definition's year or date mark (for example "[1889]") is applied by the generic functions on Sch 2 para 4, not row by row.

| row | text lines | heading or term | disposition | where it is encoded, or why not |
| --- | --- | --- | --- | --- |
| Preliminary | 1-5 | Title, chapter, long title, date of enactment | inert | The title, chapter number, long title and "[20th July 1978]" are not provisions. The date is used as a fixture (tests-time.l4: the Act is passed on 1978-07-20 and commences on 1979-01-01 under s 26). |
| s 1 | 6-7 | Words of enactment | inert | States a drafting form: that every section of an Act takes effect as a substantive enactment without introductory words. There is no input from which an answer would differ, and the brief says canons need not be forced into code. Sch 2 para 2 (Acts passed after 1850) is encoded, so the reach of s 1 is answerable (application module, `section 1`). |
| s 2 | 8-9 | Amendment or repeal in same Session | encoded | uk-interpretation-repeals.l4: `section 2 permits amendment or repeal in`. The Session of passing returns TRUE; any other Session is a named REFUSE, because the section speaks only of the Session of passing. |
| s 3 | 10-11 | Judicial notice | encoded | uk-interpretation-construction.l4: `section 3 provides that the Act is a public Act to be judicially noticed as such`. |
| s 4 | 12-16 | Time of commencement | encoded | uk-interpretation-time.l4: `section 4 — when the enactment comes into force`, `section 4(a) applies to`, `section 4(b) applies to`. Day and moment ("at the beginning of that day"). |
| s 5 | 17-18 | Definitions | encoded | uk-interpretation-application.l4: `section 5 provides that the word is to be construed according to Schedule 1` (the contrary intention); the Schedule 1 words that are time words are in uk-interpretation-time.l4. |
| s 6 | 19-23 | Gender and number | encoded | uk-interpretation-construction.l4: `section 6(a)`, `6(b)`, `6(c)`. Encoded over four abstract word forms, although the brief says canons need not be forced into code; the reach of each paragraph (Sch 2 paras 1, 2) is in uk-interpretation-application.l4. |
| s 7 | 24-25 | References to service by post | encoded | uk-interpretation-service.l4: `section 7 applies to`, `section 7 deems service to be effected by posting`, `section 7 — the time at which service is deemed to be effected`. |
| s 8 | 26-27 | References to distance | encoded | uk-interpretation-construction.l4: `section 8 — the way a distance is measured`. |
| s 9 | 28-29 | References to time of day | encoded | uk-interpretation-time.l4: `section 9 — the time standard of an expression of time in an Act`, `section 4 read with section 9 — the clock reading of the moment`. Summer time is a named REFUSE. |
| s 10 | 30-31 | References to the Sovereign | encoded | uk-interpretation-construction.l4: `section 10 — the Sovereign a reference is to be construed as`. |
| s 11 | 32-34 | Construction of subordinate legislation | encoded | uk-interpretation-construction.l4: `section 11 provides that an expression used in the subordinate legislation has the meaning which it bears in the Act`. |
| s 12 | 35-37 | Continuity of powers and duties | encoded | uk-interpretation-construction.l4: `section 12(1) ...`, `section 12(2) ...`. |
| s 13 | 38-41 | Anticipatory exercise of powers | encoded | uk-interpretation-time.l4: `the conditions of section 13 are met by`, `section 13 permits an instrument made under the Act to come into force at`, `section 13 permits the power to be exercised on`. |
| s 14 | 42-46 | Implied power to amend | encoded | uk-interpretation-construction.l4: `section 14 provides a power to revoke, amend or re-enact any instrument made under the power`. |
| s 14A | 47-59 | Power to include sunset and review provisions in subordinate legislation | encoded | uk-interpretation-construction.l4: `section 14A applies to the power or duty`, `section 14A permits subordinate legislation to include`. Subsection (6), the definition of "specified", is not given a function (it is one word). |
| s 15 | 60-61 | Repeal of repeal | encoded | uk-interpretation-repeals.l4: `section 15 provides that the repeal of a repealing enactment does not revive the enactment previously repealed`. |
| s 16 | 62-70 | General savings | encoded | uk-interpretation-repeals.l4: `section 16(1) provides that the repeal ... does not revive or affect`, `section 16(1) provides that it may be instituted, continued, enforced or imposed ...`, `section 16 treats the way the enactment ceases as a repeal by an Act`. |
| s 17 | 71-76 | Repeal and re-enactment | encoded | uk-interpretation-repeals.l4: `section 17(1) provides that the repealed enactment remains in force on`, `section 17(2)(a) ...`, `section 17(2)(b) ...`. |
| s 18 | 77-78 | Duplicated offences | encoded | uk-interpretation-construction.l4: `section 18 provides that the offender is liable to be prosecuted ...`, `section 18 provides that the offender is not liable to be punished more than once ...`. |
| s 19 | 79-84 | Citation of other Acts | encoded | uk-interpretation-construction.l4: `section 19(1) — the edition a citation is read as referring to`, `section 19(2) provides that the Act may continue to be cited by the short title ...`. |
| s 20 | 85-95 | References to other enactments etc | encoded | uk-interpretation-construction.l4: `section 20(1) provides that the portion described or cited includes` and `section 20(2) provides that the reference is a reference to the enactment as amended, extended or applied`. Subsections (2A) to (6), about EU material, are not encoded: they turn on "IP completion day", on the European Union (Withdrawal) Act 2018 and on the Direct Payments to Farmers (Legislative Continuity) Act 2020, none of which is among the sources, and the text does not give the date. |
| s 20A | 96-98 | References to certain EU instruments | inert | Applies to Acts passed after the commencement "of this section", and the text does not give the date on which s 20A commenced; it also turns on "EU instrument" (Sch 1) and on how an instrument is "amended, extended or applied" by another, which needs the text of those instruments. Nothing here is computable from the sources. |
| s 21 | 99-101 | Interpretation etc | encoded | uk-interpretation-construction.l4: `section 21(1) counts the instrument as an Act`, `section 21(1) counts the instrument as subordinate legislation`, `section 21(2) provides that the Interpretation Act 1978 binds the Crown`. The dates "IP completion day" and "exit day" are inputs (fork F13). |
| s 22 | 102-105 | Application to Acts and Measures | encoded | uk-interpretation-application.l4: (1) `section 22(1) provides that the Interpretation Act 1978 applies to itself`, `the extent to which the provision applies to an Act passed on`; (3) `section 22(3) applies the Act to the Church measure as it applies to Acts`. Subsection (2) ("a reference to an Act is a reference to an Act to which that provision applies") is not a function of its own: it is what the `Extent of application` result means, and so is realised by the structure of the module rather than by a rule. |
| s 23 | 106-110 | Application to other instruments | encoded | uk-interpretation-application.l4: (1) `the extent to which the provision applies to subordinate legislation made on`, `section 23(1) excepts the provision`; (3) `section 23(3) — the extent to which the provision applies to a deed or other instrument or document made on`; (4) `section 23(4) provides that subsections (1) and (2) do not apply`. Subsection (2) (references to an enactment include subordinate legislation) is carried by the module's one `An enactment` type, which takes either kind, and has no function of its own. |
| s 23ZA | 111-134 | Assimilated direct legislation | inert | Assimilated direct legislation: applies the Act to it "as they apply to an Act passed at the corresponding time", where "corresponding time" is the time of the amending Act, subordinate legislation or devolution legislation. The encoding has no taxonomy of devolution legislation or of assimilated direct legislation, and the terms are defined by the European Union (Withdrawal) Act 2018 and the Direct Payments to Farmers (Legislative Continuity) Act 2020, which are not among the sources. The rule that would compose with this encoding (apply the Act at the corresponding time) is the `the extent to which the provision applies to an Act passed on` function, given the corresponding day by the caller. |
| s 23A | 135-143 | Acts of the Scottish Parliament etc | inert | Acts of the Scottish Parliament: applies only ss 15 to 18 and parts of s 20, to Acts of that Parliament and instruments made under them. It needs a kind of enactment the encoding does not have, and the references to "the Scottish Parliament" turn on the Scotland Act 1998, not among the sources. |
| s 23B | 144-162 | Application of this Act to Welsh legislation | inert | Welsh legislation: turns on 1 January 2020 and on "devolved Welsh authority", "Welsh zone" and "Wales" as the Government of Wales Act 2006 defines them, and on the Legislation (Wales) Act 2019, neither of which is among the sources. The dates are in the text, but the kinds of instrument (Measure, Act of the Assembly, instruments of Welsh Ministers made with or without others) would need a taxonomy this encoding does not build. |
| s 23C | 163-179 | Interpretation of this Act in relation to Welsh legislation | inert | Interpretation of "enactment", "statutory instrument", "Acts" and "another Act" for Welsh legislation, all by pointing at the Legislation (Wales) Act 2019, which is not among the sources. |
| s 24 | 180-211 | Application to Northern Ireland | inert | Northern Ireland: (1) extends the Act to Northern Ireland so far as it applies to Acts or subordinate legislation that so extend; (2) to (3A) extend "enactment", the Order in Council terminology and s 14 and s 20A to Northern Ireland legislation; (4) lists the Schedule 1 definitions that apply to it (line 186 is a line of dots where an entry stood); (5) defines "Northern Ireland legislation" by seven kinds of instrument. It needs a Northern Ireland kind of enactment and the Statutory Rules (Northern Ireland) Order 1979 and other texts not among the sources; nothing in it is a rule about time that the encoding can compute. |
| s 25 | 212-215 | Repeals and savings | encoded | uk-interpretation-application.l4: (2) `section 25(2) provides that the reference is to be construed as referring to the Interpretation Act 1978`, (3) `section 25(3) — the day that decides which provisions apply to the enactment`. Subsection (1) repeals the enactments in Schedule 3, which this text does not show (see the Schedule 3 row); the "corresponding provision" mapping of (2) needs that table, so it is not encoded. |
| s 26 | 216-217 | Commencement | encoded | uk-interpretation-time.l4: `the day on which the Interpretation Act 1978 comes into force` (1 January 1979), used by every "after the commencement" test. |
| s 27 | 218-219 | Short title | inert | The short title, "This Act may be cited as the Interpretation Act 1978": a citation label; nothing to compute. |
| Sch 1 heading | 220-224 | SCHEDULES; Schedule 1 — Words and Expressions Defined; Section 5; the note on years and dates; Definitions | inert | Headings, the cross-reference to s 5 and the note that the years and dates after some entries are relevant to Sch 2 para 4. The note is what the mark logic in the application module implements; the heading itself computes nothing. |
| Sch 1 “Act” | 225 | “Act” | encoded | uk-interpretation-construction.l4: `section 21(1) counts the instrument as an Act` takes "an Act of Parliament" as an input. |
| Sch 1 “Associated state” | 226 | “Associated state” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Bank of England” | 227 | “Bank of England” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Bank of Ireland” | 228 | “Bank of Ireland” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “British Islands” | 229 | “British Islands” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “British overseas territory” | 230 | “British overseas territory” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “British possession” | 231 | “British possession” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 line 232 | 232 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 “Building regulations” | 233 | “Building regulations” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Central funds” | 234 | “Central funds” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Charity Commission” | 235 | “Charity Commission” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Church Commissioners” | 236 | “Church Commissioners” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Civil partnership” | 237 | “Civil partnership” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Colonial legislature” | 238 | “Colonial legislature”, and “legislature” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Colony” | 239-243 | “Colony” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Commencement” | 244 | “Commencement” | encoded | uk-interpretation-time.l4: `Schedule 1 — the commencement of the enactment` (the time when the enactment comes into force, by s 4). |
| Sch 1 “Committed for trial” | 245-247 | “Committed for trial” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 line 248 | 248 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 “Comptroller and Auditor General” | 249 | “Comptroller and Auditor General” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Consular officer” | 250 | “Consular officer” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “The Corporation Tax Acts” | 251 | “The Corporation Tax Acts” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “County court” | 252-254 | “County court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Court of Appeal” | 255-257 | “Court of Appeal” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Court of Judicature” | 258 | “Court of Judicature” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Court of summary jurisdiction” | 259 | “Court of summary jurisdiction” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Crown Court” | 260-262 | “Crown Court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Crown Estate Commissioners” | 263 | “Crown Estate Commissioners” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 line 264 | 264 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 line 265 | 265 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 “Enactment” | 266 | “Enactment” | inert | a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code). Code D in the legend below. |
| Sch 1 “England” | 267 | “England” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Financial year” | 268 | “Financial year” | encoded | uk-interpretation-time.l4: `Schedule 1 — the financial year` (and the time-word function). The twelve months ending with 31 March, limited to the stated matters; the [1889] mark is applied. |
| Sch 1 “Governor-General” | 269 | “Governor-General” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Her Majesty’s Revenue and Customs” | 270 | “Her Majesty’s Revenue and Customs” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “High Court” | 271-273 | “High Court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “The Immigration Acts” | 274 | “The Immigration Acts” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “The Income Tax Acts” | 275 | “The Income Tax Acts” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Land” | 276 | “Land” | inert | a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code). Code D in the legend below. |
| Sch 1 “Lands Clauses Acts” | 277-280 | “Lands Clauses Acts” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Local land charges register” | 281 | “Local land charges register” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Local policing body” | 282 | “Local policing body” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “London borough” | 283 | “London borough” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Lord Chancellor” | 284 | “Lord Chancellor” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Magistrates’ court” | 285-287 | “Magistrates’ court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Month” | 288 | “Month” | encoded | uk-interpretation-time.l4: `Schedule 1 — the meaning of month in`, `Schedule 1 defines month as a calendar month for`, `Schedule 1 — the meaning of the time word, in the text's own words`. The definition is "calendar month", and nothing says how a period of calendar months is counted (named REFUSE). |
| Sch 1 “National Debt Commissioners” | 289 | “National Debt Commissioners” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Northern Ireland legislation” | 290 | “Northern Ireland legislation” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Oath” | 291 | “Oath” and “affidavit” | inert | a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code). Code D in the legend below. |
| Sch 1 “Officer of a provider of probation services” | 292 | “Officer of a provider of probation services” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Officer of Revenue and Customs” | 293 | “Officer of Revenue and Customs” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Ordnance Map” | 294 | “Ordnance Map” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Parliamentary Election” | 295 | “Parliamentary Election” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “PAYE income” | 296 | “PAYE income” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “PAYE regulations” | 297 | “PAYE regulations” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Person” | 298 | “Person” | inert | a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code). Code D in the legend below. |
| Sch 1 “Police and crime commissioner” | 299 | “Police and crime commissioner” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Police area” | 300-302 | “Police area” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 line 303 | 303 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 “Police Service of Northern Ireland” | 304 | “Police Service of Northern Ireland” and “Police Service of Northern Ireland Reserve” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “The Privy Council” | 305 | “The Privy Council” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Provider of probation services” | 306 | “Provider of probation services” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Registered” | 307 | “Registered” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Registered medical practitioner” | 308 | “Registered medical practitioner” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Registered provider of social housing” | 309 | “Registered provider of social housing” and “private registered provider of social housing” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Rules of Court” | 310 | “Rules of Court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Secretary of State” | 311 | “Secretary of State” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Senior Courts” | 312 | “Senior Courts” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Sent for trial” | 313 | “Sent for trial” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “The Sentencing Code” | 314 | “The Sentencing Code” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Sewerage undertaker” | 315 | “Sewerage undertaker” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Sheriff” | 316 | “Sheriff” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “The standard scale” | 317-320 | “The standard scale” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Statutory declaration” | 321 | “Statutory declaration” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Statutory maximum” | 322-325 | “Statutory maximum” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Supreme Court” | 326 | “Supreme Court” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “The Tax Acts” | 327 | “The Tax Acts” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “The Treasury” | 328 | “The Treasury” | inert | names an institution, court or office; there is no input from which an answer would differ. Code B in the legend below. |
| Sch 1 “Trust of land” | 329 | “Trust of land” and “trustees of land” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “United Kingdom” | 330 | “United Kingdom” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Wales” | 331 | “Wales” | inert | names a territory or a legislature; there is no map or boundary in the sources, and nothing is computable here. Code C in the legend below. |
| Sch 1 “Water undertaker” | 332 | “Water undertaker” | inert | defined by pointing at another Act or instrument that is not among the sources; encoding it would need that text, and nothing is computable here. Code A in the legend below. |
| Sch 1 “Writing” | 333 | “Writing” | inert | a general word with an open-textured meaning (an interpretive canon the brief says need not be forced into code). Code D in the legend below. |
| Sch 1 line 334 | 334 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 line 335 | 335 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 paragraph group | 336-343 | Construction of certain expressions relating to offences | inert | Defines "indictable offence", "summary offence" and "offence triable either way" for England and Wales by the mode of trial, and "general limit in a magistrates' court" by a section of the Sentencing Code (not among the sources). Substantive classification of offences; there is no time computation and no input from which an answer would differ. |
| Sch 1 paragraph group | 344-349 | Construction of certain references to relationships | inert | Construes relationship references for England and Wales "in accordance with section 1 of the Family Law Reform Act 1987", which is not among the sources, with a mark "[The date of the coming into force of that section]" that the text does not give. |
| Sch 1 paragraph group | 350-356 | Construction of certain expressions relating to the police: Scotland | inert | Equates the Police Service of Scotland with the police force, chief officer, authority and area; names institutions, and nothing is computable. It is one of the Part II para 6 expressions ("in relation to Scotland, expressions relating to the police"), whose reach is encoded in the application module. |
| Sch 1 group 357 | 357-357 | Definitions relating to the EU and the United Kingdom's withdrawal | inert | Heading only: its entries have their own rows. |
| Sch 1 “Assimilated law” | 358 | “Assimilated law” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Assimilated obligation” | 359-362 | “Assimilated obligation” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “The Communities” | 363 | “The Communities” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “E.C.S.C. Treaty” | 364 | “E.C.S.C. Treaty” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “EEA agreement” | 365 | “EEA agreement” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “EEA state” | 366-368 | “EEA state” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “E.E.C. Treaty” | 369 | “E.E.C. Treaty” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Entry date” | 370 | “Entry date” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “The EU” | 371 | “The EU” or “the European Union” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “EU institution” | 372 | “EU institution” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “EU instrument” | 373 | “EU instrument” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Euratom” | 374 | “Euratom” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Euratom Treaty” | 375 | “Euratom Treaty” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “European Court” | 376 | “European Court” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “EU withdrawal agreement” | 377 | “EU withdrawal agreement” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Exit day” | 378 | “Exit day” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “IP completion day” | 379 | “IP completion day” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 “Member” | 380 | “Member” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 1 line 381 | 381 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 line 382 | 382 | a line of dots | repealed or blank in this text | The text shows a line of dots where a definition stood; it is a repeal mark in the converter output, and nothing else is on the line. |
| Sch 1 “The Treaties” | 383 | “The Treaties” or “the EU Treaties” | inert | EU-withdrawal vocabulary: it depends on EU and UK texts that are not among the sources, and any date it uses ("exit day", "IP completion day") is given by those texts. Code E in the legend below. |
| Sch 2 Part I heading | 386 | Part I — Acts | encoded | uk-interpretation-application.l4: the heading; see paras 1 to 5. |
| Sch 2 heading | 384-385 | Application of Act to Existing Enactments (Sections 22, 23) | encoded | uk-interpretation-application.l4: the heading and cross-reference; the content is in the rows below. |
| Sch 2 Part I para 1 | 387-394 | Provisions that apply to Acts whenever passed | encoded | uk-interpretation-application.l4: `Part I of Schedule 2 — the extent to which the provision applies to an Act passed before the commencement` (ss 9, 10, 14A, 18, 19(2) in whole; s 6(a) and (c) so far as offences; s 11 so far as subordinate legislation made after 1889). |
| Sch 2 Part I para 2 | 395-401 | Provisions that apply to Acts passed after the year 1850 | encoded | uk-interpretation-application.l4: same function (ss 1, 2, 3, 15, 17(1) and the rest of s 6(a) and (c)). |
| Sch 2 Part I para 3 | 402-412 | Provisions that apply to Acts passed after the year 1889 | encoded | uk-interpretation-application.l4: same function (ss 4, 7, 8, 12, 13, 14 so far as rules, regulations or byelaws, 16(1), 17(2)(a), 19(1), 20(1)). |
| Sch 2 Part I para 4(1) | 413-415 | Schedule 1 paragraphs and their year or date marks | encoded | uk-interpretation-application.l4: `Schedule 2 para 4(1) — a Schedule 1 paragraph with the mark applies to an Act passed before the commencement, on`, `a Schedule 1 paragraph with the mark applies to the enactment`. |
| Sch 2 Part I para 4(2) | 416 | "British Islands" and the Irish Free State | inert | Turns on "the establishment of the Irish Free State", whose date the text does not give, and the substance is a territorial extension (the Republic of Ireland). The generic mark logic of para 4(1) applies; this exception is not computable from the sources. |
| Sch 2 Part I para 4(3) | 417-420 | "colony" for Acts passed before the commencement | inert | A substantive extension of "colony" by reference to the Interpretation Act 1889 s 18(3) (not among the sources) and to countries that ceased to be Her Majesty's dominions; nothing is computable. |
| Sch 2 Part I para 4(4) | 421 | "Lord Chancellor" before 1 October 1921 in relation to Ireland only | encoded | uk-interpretation-application.l4: `Schedule 2 para 4(4) provides that the definition of Lord Chancellor does not apply to the Act`. |
| Sch 2 Part I para 4(5) | 422 | "person" includes bodies corporate for offences | inert | A substantive extension of the meaning of "person" to bodies corporate for provisions relating to an offence punishable on indictment or on summary conviction, for any date; no time rule and nothing to compute beyond a yes for that class. |
| Sch 2 Part I para 4(6) | 423 | Water Act 1973 treated as passed after 1 April 1974 | inert | Treats the Water Act 1973 as passed after 1 April 1974 for this paragraph; the opening words are "This paragraph applies to . . . the Water Act 1973", with dots where the text elides, so the enactments the paragraph covers are not all shown. A single-enactment exception. |
| Sch 2 Part I para 5 | 424-427 | Definitions treated as included in Schedule 1 | inert | Three substantive additions for earlier Acts: England includes Berwick upon Tweed and Monmouthshire (Acts before 1 April 1974); "land" includes messuages and so on (Acts before the commencement and after 1850); "Summary Jurisdiction (Scotland) Acts" means Part II of the Criminal Procedure (Scotland) Act 1975 (not among the sources). Each is a change to the meaning of a word, with no time rule beyond the dates stated. |
| Sch 2 Part II heading | 428 | Subordinate Legislation | encoded | uk-interpretation-application.l4: the heading; see paras 6 to 8. |
| Sch 2 Part II para 6 | 429-436 | ss 4(a), 9, 19(1) and named Schedule 1 definitions apply to earlier subordinate legislation | encoded | uk-interpretation-application.l4: `Part II of Schedule 2 — the extent to which the provision applies to subordinate legislation made before the commencement` and `Schedule 2 Part II — the definition applies to subordinate legislation made before the commencement, on`. Line 430 is a line of dots (the text elides one or more expressions there). |
| Sch 2 Part II para 7 | 437 | "county court" for Orders in Council after the year 1846 | encoded | uk-interpretation-application.l4: `Schedule 2 Part II — the definition applies ...` (`county court, in relation to England and Wales`). |
| Sch 2 Part II para 8 | 438 | "enactment" in so far as it relates to assimilated direct legislation | encoded | uk-interpretation-application.l4: `Schedule 2 Part II — the definition applies ...` (`enactment, in so far as it relates to assimilated direct legislation`). |
| Sch 3 | 439-440 | Enactments Repealed (Section 25) | repealed or blank in this text | The text shows only the heading "SCHEDULE 3 — ENACTMENTS REPEALED" and the reference "Section 25."; it shows no rows. SOURCES.md says the converter keeps table rows, so the absence suggests that the source carries none; the converted XML was not checked here. |

Counts: 40 encoded, 111 inert, 10 repealed or blank in this text, 0 not applicable (161 rows).
Among the preliminary row and the 33 sections, 25 sections are encoded and 8 sections and the preliminary row are inert; the lines of dots in Schedule 1 and the empty Schedule 3 are the `repealed or blank` rows.


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

Run as `cd <this directory> && env -u JL4_LIBRARY_PATH L4=/Users/mengwong/.cabal/store/ghc-9.10.3-fe9c/jl4-0.1-9afd0288/bin/l4 L4_TARGET=unstable ./check.sh`; it exited 0.
Standard output:

```
module                                    errors satisfied  failed  refused  expected
tests-application.l4                           0       545       0        0         0
tests-construction.l4                          0       155       0        0         0
tests-red.l4                                   7         0       7        0         7
tests-repeals.l4                               0        42       0        0         0
tests-service.l4                               0        22       0        0         0
tests-time.l4                                  0       141       0        0         0
uk-interpretation-application.l4               0         0       0        0         0
uk-interpretation-construction.l4              0         0       0        0         0
uk-interpretation-repeals.l4                   0         0       0        0         0
uk-interpretation-service.l4                   0         0       0        0         0
uk-interpretation-time.l4                      0         0       0        0         0
TOTAL (11 modules)                             7       905       7        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Standard error, one line: `check.sh: the target is unstable, so the main check was skipped.`

How to read it.
The numbers are error diagnostics, assertions satisfied, assertions failed, assertions refused, and the failures the file is expected to have.
`tests-red.l4` has 7 failed assertions, all expected (`expected_failed` in `check.sh` and `expected_red` in `encoding.json`), so its 7 errors are the same 7.
There are **0 refused assertions**: a plain `#ASSERT` over an expression that refuses would print `assertion refused` and count there, and none does.
The refusals that the tests mean are written `#ASSERT REFUSED ... BECAUSE "<reason>"`, which pins the reason as well; there are 76 of them across the test files (56 of the 141 satisfied assertions in `tests-time.l4`).
No other diagnostic exists: each module prints the one `@lang en` Hint described above and nothing else.
The counts are a point-in-time record from the `l4` build named above (sha256 `2d912dd2...cd607d7`); canon has no CI that re-runs them.

## Mutation check

The assertions were tested against 24 hand-made mutations of the modules (one change each: an operator, a boundary year, a deleted condition, a refusal turned into a value, a refusal that no longer refuses).
Each mutation was applied to a copy and the module's own test file run; **all 24 were caught** (at least one assertion failed or refused).
The mutated lines include: s 4(b) reaching subordinate legislation; the 1889 bar moved to 1888; the financial year starting a day early; a period function that computes a date; the rest-day function that returns its input; s 9 ignoring summer time; s 7 dropping the pre-paid condition; s 17(1) in force through the commencement day; s 20(1) excluding the first part; s 23(1) no longer excepting s 4(b); the England mark date moved a day; the Church Assembly bar read as on or after.
The mutation script is not shipped (it holds scratch paths); the list above is the record.

## Open questions for a domain expert

1. Does anything outside this Act, in the law the reader works under, supply the counting rule and the rest-day rule that the six refused cases need? The Act does not, and this encoding has no source for them. If one is found, it belongs in its own module with its own `@ref`s, beside this one.
2. s 9 and s 4 (F6): does "the beginning of that day" count as "an expression of time" in an Act, so that Greenwich mean time governs it?
3. s 9 is subject to s 3 of the Summer Time Act 1972, whose text is not among the sources. What does it say, and should the summer-time refusal become a rule?
4. Schedule 3 shows no rows in this text. Does the official text have a table of enactments repealed there? s 25(2)'s mapping to "the corresponding provision" needs it.
5. F14: is it right that the years and dates after Schedule 1 entries bar a definition only for Acts passed before the commencement?
6. s 7 (F11): what time governs once the contrary is proved?
7. The dates "IP completion day" and "exit day" (s 21(1), s 20(2A) to (3), s 23ZA) are given by other Acts. Which dates, and should `section 21(1)` take them as constants?
8. The devolved provisions (ss 23A, 23B, 23C, 24) are inert: a decision is needed on whether an encoding of the Interpretation Act should build the taxonomy of Scottish, Welsh and Northern Irish legislation, or leave that to the encodings of those jurisdictions' statutes.
9. s 13 (F8): is an instrument that comes into force at the beginning of the day of the Royal Assent "after the passing of the Act"?
