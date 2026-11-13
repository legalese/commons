# NOTES: Companies Act 2006 (United Kingdom), coa20: Parts 26, 26A and 27 (ss 895 to 941), lines 12203-13131 of `ukpga-2006-46.txt`

Status (2026-11-12, written by part agent coa20, model Sonnet 5.5): all modules compile on the stable binary 1.6.110 (main, e51181d, 2026-11-11) and on 1.6.109 (main, 4c887e0, 2026-11-04) with no `DiagnosticSeverity_Error` or `_Warning`; every assertion is satisfied (`check.sh` output below); `srcrefs.py check --refs` and `--strict` report 0 problems over my files. Verified by those runs and by the unit audit in the coverage section; not reviewed by a lawyer.

Files (all in this folder): layer 1 `coa20-part26.l4` (ss 895 to 901), `coa20-part26a.l4` (ss 901A to 901L), `coa20-part27-merger.l4` (ss 902 to 918A), `coa20-part27-division.l4` (ss 919 to 934), `coa20-part27-supp.l4` (ss 935 to 941); their tests `coa20-tests-part26.l4`, `coa20-tests-part26a.l4`, `coa20-tests-part27-merger.l4`, `coa20-tests-part27-division.l4`, `coa20-tests-part27-supp.l4`; layer 2 `coa20-seat.l4` and `coa20-cases-seat.l4`; this file and `PROGRESS.md`. The scratch that built them is in `../../work` (not shipped): `expand.py` (copies quotations from the raw text, and instantiates twin sections from the twin's block), the `src/*.l4.in` sources, `gen_units.py`, `gen_notes.py`, `twin.py` (a word-by-word diff of each pair of twin sections, run before any twin was instantiated).

## Source and what "verified" means here

The only source is `inputs/ukpga-2006-46.txt`, a plain-text rendering of the Act and its Schedules from legislation.gov.uk (Open Government Licence v3.0) made by a converter script; it is not the official text, and nothing here is "verified against the official text". The rendering shows some text that the official text does not (two limbs (c) in s 899(2); stray "i)" in three places; the residue ". . ." of amendments): findings 1 to 6 below. Every `-- src:` quotation in the layer-1 modules was copied from the file by `srcrefs.py quote` (through `work/expand.py`), never retyped; the short quotations inside `-- FALSE-kind` and `-- NOTHING-kind` comments were typed and are not machine-checked (the gate checks `-- src:` lines only).

## Method, and what was not done

One session, no subagents. Steps followed from `encoding-a-subject`: the unit list from the text (step 3), nouns before rules (the keel's core; the enumerations of my own are declared beside the rules that use them), rules against those nouns (step 5), tests from the text (step 6), the self-check loop reading diagnostics and counts (step 7), this file (step 9). Read in full: both `SKILL.md` files, `dialects.md`, `source-locators.md`; read in part: `regulative.md` (the `#TRACE` part), `drafting-patterns.md` (the section on exercising a `DEONTIC`), `builtins.md` (the `daydate` table). Not read: `source-patterns.md` and `source-patterns/01`-`11`, `second-pass.md`, `canon-deposit.md`, `example-brief.md`, `gotchas.md`, `sets.md`, `state-ledger.md`. Not done: the independent test pass of step 8 (a fresh session writing expectations from the text before reading the encoding); the tests are by one author. No `REFUSE`, set, `TYPICALLY`, section `GIVEN`, ledger or `EVERY` is used.

## Seat

The individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one (as a creditor, a debenture trustee, a would-be expert), asking on facts they can state what the Act requires or lets them do about a compromise, arrangement, merger or division, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.) The court, the registrar and the Takeover Panel appear only as the parties the text names; there is no seat for an official. Provisions that address only the court or the registrar (ss 896(1), 900(2), 906(2), 934(1), 939(1), (2), (4), (5)) are encoded in layer 1 for what they decide and have no seat question of their own; the person's questions about them are asked through the rules that give the person something (may I apply, may the court sanction on these votes, was the notice published a month ahead, has the court fixed the date within six months). The seat layer has 66 exported questions, each beginning "Under section N,", grouped under `§` headings in the text's order.

## What is encoded and what is not

Encoded: every provision of s 895 to s 941 (71 sections including the lettered ones), in five layer-1 modules with 334 cited declarations (rules and types that carry an `@ref`; a few bare `DECLARE`s of enumerations sit beside them), each citing its source lines with `@ref` and a quotation. Not encoded as L4, and listed as `inert` reason 2 (machinery): the regulation-making powers and their procedure in s 901B(3), s 901G(6)-(7), s 901I(3)-(8), s 901L and s 936(4); `inert` reason 1: the 33 Part, Chapter and cross-headings; `repealed or blank in this text`: s 899(5) and s 931(5). Everything else has a rule: a "subject to" signpost is a function (fork F21), a definition is a function with a test for each entry, a duty is a decision function and, where it has a deadline or a named performer, also a regulative rule (ss 900(6) and 901J(6); both traced).

Not covered by design: the Insolvency Act 1986 and the Insolvency (Northern Ireland) Order 1989 (borrowed definitions in ss 895(2), 899A(6), 901A(4), 901H(6)), the Pensions Acts and the Financial Services and Markets Act 2000 (ss 901B(2), 901I(9), 910(5), 925(4A)), the regulations of s 936(1)(c), and the amounts a level on the standard scale and the statutory maximum stand for (the penalty functions answer the core's `Penalty` with a level and a fraction, never pounds).

## Differences from PLAN.md

Where PLAN.md and the brief differ the brief governs: (1) the brief says layer 1 imports `coa-definitions`, PLAN.md section 4.1 says parts cannot; every layer-1 module imports both and takes the keel's answers as inputs named as PLAN.md names them (see Seams). (2) PLAN.md section 3 lists the core's `Fine limit` for "a fine not exceeding level 3 on the standard scale"; the penalty functions use it (`a fine not exceeding a level on the standard scale` 3 1), and "one-tenth of level 3" as the same constructor with the fraction 0.1. Nothing the core lacks was needed, so there is no `NEEDS-CORE.md`.

### Reading a result: FALSE and NOTHING (coa20)

The rule of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05 as they read in Parts 26, 26A and 27. A caller must never turn `NOTHING` into `FALSE`.

- `JUST TRUE`: the text says the case is within the rule (a condition is met, a person may apply, a requirement is satisfied, a penalty is the one stated).
- `JUST FALSE` ("a no"): the text says no in its own words: a "means" definition (ss 902(2), 904(2), 915(6), 919(2), 936(3)); a condition introduced with "if", "where" or "only if" that is not met, where the function is not a grant or a power (ss 899A(1), 901C(4), 901G(2), 936(1)); a period the text fixes ("within seven days after its making", "at least one month before": ss 900(6), 906(3)); a flat negative ("may not participate", "is not guilty", "does not apply"). In Parts 26 and 26A a requirement function also answers `JUST FALSE` where its "where" gate fails or its "must" is not done (fork F3, fork F15); in Part 27 the two are kept apart by `s 903(1) status of a requirement`. Each such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- `NOTHING` ("not covered"): the text lists without closing the list ("An application may be made by", "includes"), is silent, leaves a term undefined, points outside the sources (the Insolvency Act 1986, the Pensions Acts, regulations, section 1121), or limits a grant or prohibition in its own wording and the case falls outside the limit ("on an application under this section", "in that case"), including an unmet "if" on a power the text gives ("If a majority ... agree, the court may"; "if the company is being wound up, the liquidator": ss 896(2), 899(1), 899(2), 901C(2), 901F(1), 901F(3), 934(1), 938(2), forks F26 to F33, name-test sweep of 2026-11-12). Each such branch carries `-- NOTHING-kind (<why>)`.
- Part 27 status: `s 903(1) requirement complied with` (the facts the text asks for are in order), `requirement not complied with` (a "must" not done, fork F3), `requirement does not apply` (an excluding section, or a gate such as "in the case of a merger by formation of a new company", says so: a flat negative), `requirement not covered` (an excluding section's answer is not known). `s 903(1) the requirements of this Part do not bar the court from sanctioning` answers `JUST FALSE` when any requirement is not complied with ("must not sanction ... unless"), `NOTHING` when one is not covered, and `JUST TRUE` otherwise (a requirement that does not apply is no bar): it never says the court may sanction.
- Four answers are not `MAYBE BOOLEAN`: the penalty functions answer `MAYBE Penalty` (`NOTHING` where the section is silent about the mode of conviction), `s 940(1)` answers `MAYBE NUMBER` (pounds; `JUST 0` where subsection (2) takes the liability away), `s 908(2A)` answers which statement is required, and `s 918A(3)`/`s 933(4)` answer a date.
- "Until" bars (ss 899(4), 901F(6)) are bars: `JUST TRUE` while the step is not done, `JUST FALSE` after; no function says an order has effect. A defence the person must show (ss 897(7), 901D(7)) answers `JUST FALSE` for "this section gives no defence on these facts".

## Findings: what the text turns out to say

1. s 899(2) prints limb (c) twice (lines 12263-12265): "(c) if the company is being wound up or an administration order is in force in relation it, the liquidator or administrator." and then "(c) if the company is being wound up, the liquidator, or (d) if the company is in administration, the administrator." The rendering carries a pre-amendment and a post-amendment limb together (fork F1). Asserted: `s 899(2) the person may apply for the court's sanction` in `coa20-tests-part26.l4`.
2. s 899(5) and s 931(5) are shown as a row of dots (lines 12270 and 12964): repealed or omitted. Coverage rows `repealed or blank in this text`.
3. The "majority in number" test is in s 899(1), s 907(1), s 922(1) and s 940(2) (lines 12258, 12592, 12844, 13108) and is absent from the Part 26A counterparts s 901F(1) and s 940(2A) (lines 12405, 13109), which say "a number representing 75% in value" (fork F5). Asserted at the boundary in the tests of ss 899(1), 901F(1), 940(2).
4. The penalty is split by country in s 901D(8) (lines 12392-12395: England and Wales, "a fine"; Scotland or Northern Ireland, a fine not exceeding the statutory maximum) but not in s 897(8) (lines 12246-12248: "on summary conviction, to a fine not exceeding the statutory maximum"). Asserted in the tests of ss 897(8) and 901D(8): for s 901D(8) a summary conviction in no named place answers `NOTHING`.
5. The one-month periods are anchored on different dates: s 916(3A) and s 918(2A) on "the date of the first meeting of members ... of the transferor company"; s 917(3A) and s 931(3A) on "the date of the court's order" (lines 12719, 12742, 12767, 12949); s 932(2A) on the first meeting of the transferor's members (line 12975). The twins were instantiated from s 916 with the anchor replaced, and each has its own boundary tests.
6. Typographical residue in the rendering: "i)" before the text of s 918A(1A)(a)(i), s 926A(5)(b)(i) and s 933A(3)(a)(i) (lines 12789, 12920, 13015); ". . ." in s 911(3)(d), s 912(1) and s 926(3)(d) (lines 12648, 12679, 12903); a doubled full stop at the end of s 908(3) (line 12604). None changes a rule; the quotations keep them.
7. A fourth condition that differs between the twins: s 916(5), s 917(5), s 918(4) and s 932(4) require that members holding not less than 5% of the paid-up voting capital "would have been able" to require a meeting and that none did (lines 12735, 12758, 12783, 12991); s 931 has instead (6), a report of material change (line 12965), after the repealed (5). Asserted in the tests of ss 916(5), 931(6).
8. s 923(3) (the report must say whether a report has been made under s 593 and whether it was delivered to the registrar) has no counterpart in s 908: a merger report carries no such statement.
9. s 904(2)(b): in a merger by formation of a new company "the merging companies" are the transferor companies only, so the new transferee company is not one: `JUST FALSE` for the new company. Asserted.
10. s 940(1) makes each transferee company liable for another's defaulted liability "to the extent that the other company has made default", capped by the net value transferred to it (s 940(3)), and s 940(2) and (2A) take the liability away for creditors who agreed by the stated majority; the three together are the one answer of the question "how much may I claim" (`s 940(1) the amount for which the transferee company is liable`).
11. s 899A(1)(a) and s 901H(1)(a): an application made during the moratorium is "before the end of the period of 12 weeks beginning with the day after the end of any moratorium" on a literal reading (fork F14). Asserted: an application 9 days before the moratorium ended is within section 899A.
12. s 902 and s 903 name sections of other Parts by number ("sections 915 to 918A", "sections 931 to 934"); the aggregator `s 903(2)` and `s 903(3)` take the statuses of those requirements as a list, so a requirement section that is left out of the list is silently not counted: the seat layer asks the requirements one by one and the lead's merged seat is where the list is built.
13. s 911(4) and s 926(4) (the requirements of the documents of (3)(b) and (c), and for s 926 also (e), are "subject to" ss 915, 918A, 933, 933A and 934) are wired into the document lists: `s 911(3)` and `s 926(3)` take the answer of subsection (4) and a document it excludes answers `JUST FALSE`; `s 911(1)` and `s 926(1)` take only the whole-section exclusion (s 911(7), s 934(1)(a)). The seat questions on ss 911(1) and 926(1) ask whether the person could inspect the documents the section requires.

## What the stable binary does not accept, and what it does

Measured on 2026-11-12 with `L4_BIN` (1.6.110 main) and `L4_MAIN` (1.6.109 main) by the runs recorded in `work/probe` and by `check.sh`:

- **Loud:** an action written with `WITH` inside a `MUST` (``MUST `Action of a party` WITH performer IS ...``) is a parse error (`unexpected WITH`); the action is written by applying the constructor to its fields positionally (`MUST `Action of a party` Company Registrar "deliver ..."`), which both builds accept. `LIST` of record constructions needs each record in brackets (``LIST (`s 1 class` OF 100, 51), (`s 1 class` OF 10, 6)``): without them the application takes too many arguments.
- **Silent:** `NOT (x) OR y` and `a AND NOT (b) AND c` read as `NOT ((x) OR y)` and `a AND NOT ((b) AND c)`. Found by two failing assertions in this run (s 909(5) and s 915A(6)); every `NOT` that is followed by `AND` or `OR` in a layer-1 file is now bracketed as `((NOT (x)) OR y)`. A `DEONTIC` value cannot be compared with `EQUALS` in an `#ASSERT` (the `drafting-patterns.md` note), so the two regulative rules (`s 900(6)` and `s 901J(6)`) are exercised with `#TRACE` and their decision twins are asserted; the trace outcomes are not counted by `check.sh`. Traces read by hand in this run (three, in `coa20-tests-part26.l4`; the 901J twin repeats them): a copy delivered on day 5 of 7: `FULFILLED`; on day 7, the last day: `FULFILLED`; the clock reaching day 8 with nothing delivered: `DEONTIC BREACHED: BREACH BY Company BECAUSE "a copy of the order was not delivered to the registrar within seven days after its making (s 900(6))"`. The six traces (three each in `coa20-tests-part26.l4` and `coa20-tests-part26a.l4`) give the same outcomes on 1.6.109 and 1.6.110, compared by hand (`check.sh` compares assertion counts, not traces).
- **Accepted although the brief says the stable line does not have them** (the keel measured the same): `REFUSE`, `#ASSERT REFUSED` and `YMD`. None is used here: not-covered answers are `NOTHING` or a constructor, dates are `Date day month year`.
- Used and accepted: `MAYBE` of a record (`MAYBE Penalty`), `MAYBE NUMBER`, `MAYBE DATE`, `all` over a list with a lambda, `elem` over a list of `MAYBE BOOLEAN`, `add months` with a negative count (`add months d (0 MINUS 7)`), `EQUALS` between `MAYBE` values, between enum constructors and between records, `CONSIDER` over `MAYBE` and enum values, a rule and a `GIVEN` input of the same name (the input shadows the rule inside the function, as the seam convention needs), and an `@export` description containing an apostrophe.

## Coverage (coa20)

Units of lines 12203-13131 of `inputs/ukpga-2006-46.txt`, found by `work/gen_units.py` reading the raw text: 828 units (headings 33, sections 71, subsections 343, paragraphs 358, defined terms 23). Rows in this table: 828 (before this agent: 0). Non-blank lines in the range: 929; lines in no row: 0. Rows with no L4 name and no inert or repealed reason: 0.

Dispositions (exactly one per row): encoded 544, fork 227, inert 55, repealed or blank in this text 2. The first column is the unit in the text's own numbering; the L4 names are the rules whose `@ref` locator contains the unit (a section row counts the rules in the section). `fork` rows name their fork-register entries; a row that rests on a register-wide convention (F3, F15, F21) is `encoded`, with the convention named in the register. "(second (c) as printed)" marks the second limb (c) that the text prints in s 899(2).

Reason numbers for `inert` are those of the brief: 1 not operative, 2 machinery, 3 text shown repealed or blank. A paragraph or sub-paragraph that is part of a list encoded by one function is covered by that function, which cites the whole list. The `(i)`, `(ii)` sub-paragraphs are inside their paragraph rows.

| unit | lines | disposition | forks / reason | L4 names or why inert |
| --- | --- | --- | --- | --- |
| Part 26 — Arrangements and reconstructions: general | 12203-12203 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Application of this Part | 12204-12204 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 895 | 12205-12214 | encoded |  | 4 rules, see the rows below |
| s 895(1) | 12206-12208 | encoded |  | `s 895(1) the provisions of Part 26 apply` |
| s 895(1)(a) | 12207-12207 | encoded |  | `s 895(1) the provisions of Part 26 apply` |
| s 895(1)(b) | 12208-12208 | encoded |  | `s 895(1) the provisions of Part 26 apply` |
| s 895(2) | 12209-12213 | encoded |  | `s 895(2) the reorganisation of the share capital is an arrangement`; `s 895(2) the body is a company for the purposes of Part 26` |
| s 895(2) arrangement | 12210-12210 | encoded |  | `s 895(2) the reorganisation of the share capital is an arrangement` |
| s 895(2) company | 12211-12213 | encoded |  | `s 895(2) the body is a company for the purposes of Part 26` |
| s 895(2)(a) | 12212-12212 | encoded |  | `s 895(2) the body is a company for the purposes of Part 26` |
| s 895(2)(b) | 12213-12213 | encoded |  | `s 895(2) the body is a company for the purposes of Part 26` |
| s 895(3) | 12214-12214 | encoded |  | `s 895(3) the provisions of Part 26 have effect subject to Part 27` |
| Meeting of creditors or members | 12215-12215 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 896 | 12216-12224 | encoded | F26 | 4 rules, see the rows below |
| s 896(1) | 12217-12217 | encoded |  | `s 896(1) the court may order a meeting of the creditors, class of creditors, members or class of members` |
| s 896(2) | 12218-12222 | fork | F26 | `s 896(2) the person may apply for an order for a meeting` |
| s 896(2)(a) | 12219-12219 | fork | F26 | `s 896(2) the person may apply for an order for a meeting` |
| s 896(2)(b) | 12220-12220 | fork | F26 | `s 896(2) the person may apply for an order for a meeting` |
| s 896(2)(c) | 12221-12221 | fork | F26 | `s 896(2) the person may apply for an order for a meeting` |
| s 896(2)(d) | 12222-12222 | fork | F26 | `s 896(2) the person may apply for an order for a meeting` |
| s 896(3) | 12223-12223 | encoded |  | `s 896(3) section 323 applies to the meeting` |
| s 896(4) | 12224-12224 | encoded |  | `s 896(4) section 896 is subject to section 899A` |
| s 897 | 12225-12248 | encoded | F16 | 7 rules, see the rows below |
| s 897(1) | 12226-12230 | encoded |  | `s 897(1) the notice summoning the meeting satisfies the requirement` |
| s 897(1)(a) | 12227-12227 | encoded |  | `s 897(1) the notice summoning the meeting satisfies the requirement` |
| s 897(1)(b) | 12228-12230 | encoded |  | `s 897(1) the notice summoning the meeting satisfies the requirement` |
| s 897(2) | 12231-12235 | encoded |  | `s 897(2) the statement complies` |
| s 897(2)(a) | 12232-12232 | encoded |  | `s 897(2) the statement complies` |
| s 897(2)(b) | 12233-12235 | encoded |  | `s 897(2) the statement complies` |
| s 897(3) | 12236-12236 | encoded |  | `s 897(3) the statement complies as respects debenture holders` |
| s 897(4) | 12237-12237 | encoded |  | `s 897(4) the person is entitled to be provided by the company with a copy of the statement free of charge` |
| s 897(5) | 12238-12241 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(5)(a) | 12239-12239 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(5)(b) | 12240-12241 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(6) | 12242-12244 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(6)(a) | 12243-12243 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(6)(b) | 12244-12244 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897` |
| s 897(7) | 12245-12245 | fork | F16 | `s 897(5) the person is guilty of an offence under section 897`; `s 897(7) section 897(7) gives the person a defence on these facts` |
| s 897(8) | 12246-12248 | encoded |  | `s 897(8) the penalty on conviction` |
| s 897(8)(a) | 12247-12247 | encoded |  | `s 897(8) the penalty on conviction` |
| s 897(8)(b) | 12248-12248 | encoded |  | `s 897(8) the penalty on conviction` |
| s 898 | 12249-12255 | encoded |  | 2 rules, see the rows below |
| s 898(1) | 12250-12253 | encoded |  | `s 898(1) the person is under a duty to give the company notice of the matter` |
| s 898(1)(a) | 12251-12251 | encoded |  | `s 898(1) the person is under a duty to give the company notice of the matter` |
| s 898(1)(b) | 12252-12253 | encoded |  | `s 898(1) the person is under a duty to give the company notice of the matter` |
| s 898(2) | 12254-12254 | encoded |  | `s 898(2) the person commits an offence` |
| s 898(3) | 12255-12255 | encoded |  | `s 898(2) the person commits an offence` |
| Court sanction for compromise or arrangement | 12256-12256 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 899 | 12257-12270 | encoded | F1 F17 F2 F27 F28 | 5 rules, see the rows below |
| s 899(1) | 12258-12258 | fork | F2 F27 | `s 899(1) the court may sanction the compromise or arrangement` |
| s 899(1A) | 12259-12259 | encoded |  | `s 899(1A) section 899(1) is subject to section 899A` |
| s 899(2) | 12260-12265 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(2)(a) | 12261-12261 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(2)(b) | 12262-12262 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(2)(c) | 12263-12263 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(2)(c) (the second limb (c) as printed) | 12264-12264 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(2)(d) | 12265-12265 | fork | F1 F28 | `s 899(2) the person may apply for the court's sanction` |
| s 899(3) | 12266-12268 | encoded |  | `s 899(3) the compromise or arrangement is binding on the person` |
| s 899(3)(a) | 12267-12267 | encoded |  | `s 899(3) the compromise or arrangement is binding on the person` |
| s 899(3)(b) | 12268-12268 | encoded |  | `s 899(3) the compromise or arrangement is binding on the person` |
| s 899(4) | 12269-12269 | fork | F17 | `s 899(4) the court's order cannot yet have effect` |
| s 899(5) | 12270-12270 | repealed or blank in this text |  | s 899(5): the text shows only dots (repealed or omitted) |
| Special cases | 12271-12271 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 899A | 12272-12290 | encoded | F14 | 6 rules, see the rows below |
| s 899A(1) | 12273-12275 | fork | F14 | `s 899A(1) this section applies` |
| s 899A(1)(a) | 12274-12274 | fork | F14 | `s 899A(1) this section applies` |
| s 899A(1)(b) | 12275-12275 | fork | F14 | `s 899A(1) this section applies` |
| s 899A(2) | 12276-12278 | encoded |  | `s 899A(2) the creditor is a relevant creditor` |
| s 899A(2)(a) | 12277-12277 | encoded |  | `s 899A(2) the creditor is a relevant creditor` |
| s 899A(2)(b) | 12278-12278 | encoded |  | `s 899A(2) the creditor is a relevant creditor` |
| s 899A(3) | 12279-12279 | encoded |  | `s 899A(3) the relevant creditor may participate in the meeting summoned under section 896` |
| s 899A(4) | 12280-12282 | encoded |  | `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend` |
| s 899A(4)(a) | 12281-12281 | encoded |  | `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend` |
| s 899A(4)(b) | 12282-12282 | encoded |  | `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend` |
| s 899A(5) | 12283-12283 | encoded |  | `s 899A(5) the court may sanction the compromise or arrangement under section 899` |
| s 899A(6) | 12284-12290 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6) moratorium debt | 12285-12287 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6)(a) | 12286-12286 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6)(b) | 12287-12288 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6) priority pre-moratorium debt | 12288-12290 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6)(a) (the second limb (c) as printed) | 12289-12289 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 899A(6)(b) (the second limb (c) as printed) | 12290-12290 | encoded |  | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| Reconstructions and amalgamations | 12291-12291 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 900 | 12292-12314 | encoded | F6 | 9 rules, see the rows below |
| s 900(1) | 12293-12295 | encoded |  | `s 900(1) this section applies` |
| s 900(1)(a) | 12294-12294 | encoded |  | `s 900(1) this section applies` |
| s 900(1)(b) | 12295-12295 | encoded |  | `s 900(1) this section applies` |
| s 900(2) | 12296-12302 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(a) | 12297-12297 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(b) | 12298-12298 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(c) | 12299-12299 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(d) | 12300-12300 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(e) | 12301-12301 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(2)(f) | 12302-12302 | encoded |  | `s 900(2) the court may make provision for the matter` |
| s 900(3) | 12303-12305 | encoded |  | `s 900(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 900(3)(a) | 12304-12304 | encoded |  | `s 900(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 900(3)(b) | 12305-12305 | encoded |  | `s 900(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 900(4) | 12306-12306 | encoded |  | `s 900(4) the property vests freed from the charge` |
| s 900(5) | 12307-12309 | encoded |  | `s 900(5) the thing is property` |
| s 900(5) property | 12308-12308 | encoded |  | `s 900(5) the thing is property` |
| s 900(5) liabilities | 12309-12309 | encoded |  | `s 900(5) the thing is property` |
| s 900(6) | 12310-12310 | fork | F6 | `s 900(6) the company delivered a copy of the order to the registrar in time`; `s 900(6) the company's duty to deliver a copy of the order` |
| s 900(7) | 12311-12313 | encoded |  | `s 900(7) the person is guilty of an offence under section 900(7)` |
| s 900(7)(a) | 12312-12312 | encoded |  | `s 900(7) the person is guilty of an offence under section 900(7)` |
| s 900(7)(b) | 12313-12313 | encoded |  | `s 900(7) the person is guilty of an offence under section 900(7)` |
| s 900(8) | 12314-12314 | encoded |  | `s 900(8) the penalty on conviction` |
| Obligations of company with respect to articles etc | 12315-12315 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901 | 12316-12331 | encoded | F10 | 6 rules, see the rows below |
| s 901(1) | 12317-12319 | encoded |  | `s 901(1) this section applies to the order` |
| s 901(1)(a) | 12318-12318 | encoded |  | `s 901(1) this section applies to the order` |
| s 901(1)(b) | 12319-12319 | encoded |  | `s 901(1) this section applies to the order` |
| s 901(2) | 12320-12323 | encoded |  | `s 901(2) the copy of the order is accompanied as the section requires` |
| s 901(2)(a) | 12321-12321 | encoded |  | `s 901(2) the copy of the order is accompanied as the section requires` |
| s 901(2)(b) | 12322-12323 | encoded |  | `s 901(2) the copy of the order is accompanied as the section requires` |
| s 901(3) | 12324-12324 | fork | F10 | `s 901(3) the copy of the articles is accompanied as the section requires` |
| s 901(4) | 12325-12327 | encoded |  | `s 901(4) the thing is within the reference` |
| s 901(4)(a) | 12326-12326 | encoded |  | `s 901(4) the thing is within the reference` |
| s 901(4)(b) | 12327-12327 | encoded |  | `s 901(4) the thing is within the reference` |
| s 901(5) | 12328-12330 | encoded |  | `s 901(5) the person is guilty of an offence under section 901` |
| s 901(5)(a) | 12329-12329 | encoded |  | `s 901(5) the person is guilty of an offence under section 901` |
| s 901(5)(b) | 12330-12330 | encoded |  | `s 901(5) the person is guilty of an offence under section 901` |
| s 901(6) | 12331-12331 | encoded |  | `s 901(6) the penalty on conviction` |
| PART 26A — Arrangements and reconstructions: companies in fi | 12332-12332 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Application of this Part (the second limb (c) as printed) | 12333-12333 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901A | 12334-12347 | encoded | F25 | 6 rules, see the rows below |
| s 901A(1) | 12335-12335 | encoded |  | `s 901A(1) the provisions of Part 26A apply` |
| s 901A(2) | 12336-12336 | fork | F25 | `s 901A(2) condition A is met` |
| s 901A(3) | 12337-12341 | fork | F25 | `s 901A(3) condition B is met` |
| s 901A(3)(a) | 12338-12340 | fork | F25 | `s 901A(3) condition B is met` |
| s 901A(3)(b) | 12341-12341 | fork | F25 | `s 901A(3) condition B is met` |
| s 901A(4) | 12342-12346 | encoded |  | `s 901A(4) the reorganisation of the share capital is an arrangement`; `s 901A(4) the body is a company for the purposes of Part 26A` |
| s 901A(4) arrangement | 12343-12343 | encoded |  | `s 901A(4) the reorganisation of the share capital is an arrangement` |
| s 901A(4) company | 12344-12346 | encoded |  | `s 901A(4) the body is a company for the purposes of Part 26A` |
| s 901A(4)(a) | 12345-12345 | encoded |  | `s 901A(4) the body is a company for the purposes of Part 26A` |
| s 901A(4)(b) | 12346-12346 | encoded |  | `s 901A(4) the body is a company for the purposes of Part 26A` |
| s 901A(5) | 12347-12347 | encoded |  | `s 901A(5) the provisions of Part 26A have effect subject to Part 27` |
| s 901B | 12348-12357 | encoded |  | 2 rules, see the rows below |
| s 901B(1) | 12349-12353 | encoded |  | `s 901B(1) Part 26A does not apply because of regulations under section 901B` |
| s 901B(1)(a) | 12350-12350 | encoded |  | `s 901B(1) Part 26A does not apply because of regulations under section 901B` |
| s 901B(1)(b) | 12351-12353 | encoded |  | `s 901B(1) Part 26A does not apply because of regulations under section 901B` |
| s 901B(2) | 12354-12356 | encoded |  | `s 901B(2) the person is an authorised person` |
| s 901B(2) authorised person | 12355-12355 | encoded |  | `s 901B(2) the person is an authorised person` |
| s 901B(2) specified | 12356-12356 | encoded |  | `s 901B(2) the person is an authorised person` |
| s 901B(3) | 12357-12357 | inert | reason 2 | s 901B(3): regulations under this section are subject to affirmative resolution procedure (machinery: a regulation-making procedure) |
| Meeting of creditors or members (the second limb (c) as printed) | 12358-12358 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901C | 12359-12370 | encoded | F29 F4 | 7 rules, see the rows below |
| s 901C(1) | 12360-12360 | encoded |  | `s 901C(1) the court may order a meeting of the creditors, class of creditors, members or class of members` |
| s 901C(2) | 12361-12365 | fork | F29 | `s 901C(2) the person may apply to the court` |
| s 901C(2)(a) | 12362-12362 | fork | F29 | `s 901C(2) the person may apply to the court` |
| s 901C(2)(b) | 12363-12363 | fork | F29 | `s 901C(2) the person may apply to the court` |
| s 901C(2)(c) | 12364-12364 | fork | F29 | `s 901C(2) the person may apply to the court` |
| s 901C(2)(d) | 12365-12365 | fork | F29 | `s 901C(2) the person may apply to the court` |
| s 901C(3) | 12366-12366 | encoded |  | `s 901C(3) the person must be permitted to participate in the meeting` |
| s 901C(4) | 12367-12367 | fork | F4 | `s 901C(4) subsection (3) does not apply in relation to the class` |
| s 901C(5) | 12368-12368 | encoded |  | `s 901C(5) the person is the one who is to make the application under subsection (4)` |
| s 901C(6) | 12369-12369 | encoded |  | `s 901C(6) section 323 applies to the meeting` |
| s 901C(7) | 12370-12370 | encoded |  | `s 901C(7) section 901C is subject to section 901H` |
| s 901D | 12371-12395 | encoded | F16 | 7 rules, see the rows below |
| s 901D(1) | 12372-12376 | encoded |  | `s 901D(1) the notice summoning the meeting satisfies the requirement` |
| s 901D(1)(a) | 12373-12373 | encoded |  | `s 901D(1) the notice summoning the meeting satisfies the requirement` |
| s 901D(1)(b) | 12374-12376 | encoded |  | `s 901D(1) the notice summoning the meeting satisfies the requirement` |
| s 901D(2) | 12377-12381 | encoded |  | `s 901D(2) the statement complies` |
| s 901D(2)(a) | 12378-12378 | encoded |  | `s 901D(2) the statement complies` |
| s 901D(2)(b) | 12379-12381 | encoded |  | `s 901D(2) the statement complies` |
| s 901D(3) | 12382-12382 | encoded |  | `s 901D(3) the statement complies as respects debenture holders` |
| s 901D(4) | 12383-12383 | encoded |  | `s 901D(4) the person is entitled to be provided by the company with a copy of the statement free of charge` |
| s 901D(5) | 12384-12387 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(5)(a) | 12385-12385 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(5)(b) | 12386-12387 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(6) | 12388-12390 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(6)(a) | 12389-12389 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(6)(b) | 12390-12390 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D` |
| s 901D(7) | 12391-12391 | fork | F16 | `s 901D(5) the person is guilty of an offence under section 901D`; `s 901D(7) section 901D(7) gives the person a defence on these facts` |
| s 901D(8) | 12392-12395 | encoded |  | `s 901D(8) the penalty on conviction` |
| s 901D(8)(a) | 12393-12393 | encoded |  | `s 901D(8) the penalty on conviction` |
| s 901D(8)(b) | 12394-12394 | encoded |  | `s 901D(8) the penalty on conviction` |
| s 901D(8)(c) | 12395-12395 | encoded |  | `s 901D(8) the penalty on conviction` |
| s 901E | 12396-12402 | encoded |  | 2 rules, see the rows below |
| s 901E(1) | 12397-12400 | encoded |  | `s 901E(1) the person is under a duty to give the company notice of the matter` |
| s 901E(1)(a) | 12398-12398 | encoded |  | `s 901E(1) the person is under a duty to give the company notice of the matter` |
| s 901E(1)(b) | 12399-12400 | encoded |  | `s 901E(1) the person is under a duty to give the company notice of the matter` |
| s 901E(2) | 12401-12401 | encoded |  | `s 901E(2) the person commits an offence` |
| s 901E(3) | 12402-12402 | encoded |  | `s 901E(2) the person commits an offence` |
| Court sanction for compromise or arrangement (the second limb (c) as printed) | 12403-12403 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901F | 12404-12423 | encoded | F17 F30 F31 F5 | 6 rules, see the rows below |
| s 901F(1) | 12405-12405 | fork | F30 F5 | `s 901F(1) the court may sanction the compromise or arrangement` |
| s 901F(2) | 12406-12408 | encoded |  | `s 901F(2) section 901F(1) is subject to sections 901G and 901H` |
| s 901F(2)(a) | 12407-12407 | encoded |  | `s 901F(2) section 901F(1) is subject to sections 901G and 901H` |
| s 901F(2)(b) | 12408-12408 | encoded |  | `s 901F(2) section 901F(1) is subject to sections 901G and 901H` |
| s 901F(3) | 12409-12413 | fork | F31 | `s 901F(3) the person may apply to the court` |
| s 901F(3)(a) | 12410-12410 | fork | F31 | `s 901F(3) the person may apply to the court` |
| s 901F(3)(b) | 12411-12411 | fork | F31 | `s 901F(3) the person may apply to the court` |
| s 901F(3)(c) | 12412-12412 | fork | F31 | `s 901F(3) the person may apply to the court` |
| s 901F(3)(d) | 12413-12413 | fork | F31 | `s 901F(3) the person may apply to the court` |
| s 901F(4) | 12414-12417 | encoded |  | `s 901F(4) the court may by the order make the provision` |
| s 901F(4)(a) | 12415-12415 | encoded |  | `s 901F(4) the court may by the order make the provision` |
| s 901F(4)(b) | 12416-12416 | encoded |  | `s 901F(4) the court may by the order make the provision` |
| s 901F(4)(c) | 12417-12417 | encoded |  | `s 901F(4) the court may by the order make the provision` |
| s 901F(5) | 12418-12420 | encoded |  | `s 901F(5) the compromise or arrangement is binding on the person` |
| s 901F(5)(a) | 12419-12419 | encoded |  | `s 901F(5) the compromise or arrangement is binding on the person` |
| s 901F(5)(b) | 12420-12420 | encoded |  | `s 901F(5) the compromise or arrangement is binding on the person` |
| s 901F(6) | 12421-12423 | fork | F17 | `s 901F(6) the court's order cannot yet have effect` |
| s 901F(6)(a) | 12422-12422 | fork | F17 | `s 901F(6) the court's order cannot yet have effect` |
| s 901F(6)(b) | 12423-12423 | fork | F17 | `s 901F(6) the court's order cannot yet have effect` |
| s 901G | 12424-12433 | encoded | F4 | 5 rules, see the rows below |
| s 901G(1) | 12425-12425 | encoded |  | `s 901G(1) this section applies` |
| s 901G(2) | 12426-12426 | encoded |  | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` |
| s 901G(3) | 12427-12427 | fork | F4 | `s 901G(3) condition A is met` |
| s 901G(4) | 12428-12428 | encoded |  | `s 901G(4) the relevant alternative` |
| s 901G(5) | 12429-12429 | encoded |  | `s 901G(5) condition B is met` |
| s 901G(6) | 12430-12432 | inert | reason 2 | s 901G(6)-(7): the Secretary of State's power to amend the section by regulations, and the affirmative procedure (machinery) |
| s 901G(6)(a) | 12431-12431 | inert | reason 2 | s 901G(6)-(7): the Secretary of State's power to amend the section by regulations, and the affirmative procedure (machinery) |
| s 901G(6)(b) | 12432-12432 | inert | reason 2 | s 901G(6)-(7): the Secretary of State's power to amend the section by regulations, and the affirmative procedure (machinery) |
| s 901G(7) | 12433-12433 | inert | reason 2 | s 901G(6)-(7): the Secretary of State's power to amend the section by regulations, and the affirmative procedure (machinery) |
| Special cases (the second limb (c) as printed) | 12434-12434 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901H | 12435-12453 | encoded | F14 | 6 rules, see the rows below |
| s 901H(1) | 12436-12438 | fork | F14 | `s 901H(1) this section applies` |
| s 901H(1)(a) | 12437-12437 | fork | F14 | `s 901H(1) this section applies` |
| s 901H(1)(b) | 12438-12438 | fork | F14 | `s 901H(1) this section applies` |
| s 901H(2) | 12439-12441 | encoded |  | `s 901H(2) the creditor is a relevant creditor` |
| s 901H(2)(a) | 12440-12440 | encoded |  | `s 901H(2) the creditor is a relevant creditor` |
| s 901H(2)(b) | 12441-12441 | encoded |  | `s 901H(2) the creditor is a relevant creditor` |
| s 901H(3) | 12442-12442 | encoded |  | `s 901H(3) the relevant creditor may participate in the meeting summoned under section 901C` |
| s 901H(4) | 12443-12445 | encoded |  | `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend` |
| s 901H(4)(a) | 12444-12444 | encoded |  | `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend` |
| s 901H(4)(b) | 12445-12445 | encoded |  | `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend` |
| s 901H(5) | 12446-12446 | encoded |  | `s 901H(5) the court may sanction the compromise or arrangement under section 901F` |
| s 901H(6) | 12447-12453 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6) moratorium debt | 12448-12450 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6)(a) | 12449-12449 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6)(b) | 12450-12451 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6) priority pre-moratorium debt | 12451-12453 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6)(a) (the second limb (c) as printed) | 12452-12452 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901H(6)(b) (the second limb (c) as printed) | 12453-12453 | encoded |  | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| s 901I | 12454-12480 | encoded |  | 7 rules, see the rows below |
| s 901I(1) | 12455-12455 | encoded |  | `s 901I(1) the notice or other document has been sent to the Pensions Regulator as the section requires` |
| s 901I(2) | 12456-12456 | encoded |  | `s 901I(2) the notice or other document has been sent to the Board of the Pension Protection Fund as the section requires` |
| s 901I(3) | 12457-12460 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(3)(a) | 12458-12458 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(3)(b) | 12459-12460 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(4) | 12461-12463 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(4)(a) | 12462-12462 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(4)(b) | 12463-12463 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(5) | 12464-12467 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(5)(a) | 12465-12465 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(5)(b) | 12466-12466 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(5)(c) | 12467-12467 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(6) | 12468-12468 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(7) | 12469-12469 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(8) | 12470-12470 | inert | reason 2 | s 901I(3)-(8): the power to make regulations about the Board's exercise of creditors' rights, and their procedure (machinery) |
| s 901I(9) | 12471-12480 | encoded |  | `s 901I(9) the scheme is an eligible scheme`; `s 901I(9) the person is an employer`; `s 901I(9) the scheme is a money purchase scheme` (+2 more) |
| s 901I(9) eligible scheme | 12472-12472 | encoded |  | `s 901I(9) the scheme is an eligible scheme` |
| s 901I(9) employer | 12473-12477 | encoded |  | `s 901I(9) the person is an employer` |
| s 901I(9)(a) | 12474-12474 | encoded |  | `s 901I(9) the person is an employer` |
| s 901I(9)(b) | 12475-12480 | encoded |  | `s 901I(9) the person is an employer`; `s 901I(9) the scheme is a money purchase scheme`; `s 901I(9) the scheme is an occupational pension scheme or a pension scheme` (+1 more) |
| s 901I(9) money purchase scheme | 12478-12478 | encoded |  | `s 901I(9) the scheme is a money purchase scheme` |
| s 901I(9) occupational pension scheme | 12479-12479 | encoded |  | `s 901I(9) the scheme is an occupational pension scheme or a pension scheme` |
| s 901I(9) specified | 12480-12480 | encoded |  | `s 901I(9) the description is specified` |
| Reconstructions and amalgamations (the second limb (c) as printed) | 12481-12481 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901J | 12482-12504 | encoded | F17 F6 | 9 rules, see the rows below |
| s 901J(1) | 12483-12485 | encoded |  | `s 901J(1) this section applies` |
| s 901J(1)(a) | 12484-12484 | encoded |  | `s 901J(1) this section applies` |
| s 901J(1)(b) | 12485-12485 | encoded |  | `s 901J(1) this section applies` |
| s 901J(2) | 12486-12492 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(a) | 12487-12487 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(b) | 12488-12488 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(c) | 12489-12489 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(d) | 12490-12490 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(e) | 12491-12491 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(2)(f) | 12492-12492 | encoded |  | `s 901J(2) the court may make provision for the matter` |
| s 901J(3) | 12493-12495 | encoded |  | `s 901J(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 901J(3)(a) | 12494-12494 | encoded |  | `s 901J(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 901J(3)(b) | 12495-12495 | encoded |  | `s 901J(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| s 901J(4) | 12496-12496 | encoded |  | `s 901J(4) the property vests freed from the charge` |
| s 901J(5) | 12497-12499 | encoded |  | `s 901J(5) the thing is property` |
| s 901J(5) property | 12498-12498 | encoded |  | `s 901J(5) the thing is property` |
| s 901J(5) liabilities | 12499-12499 | encoded |  | `s 901J(5) the thing is property` |
| s 901J(6) | 12500-12500 | fork | F17 F6 | `s 901J(6) the company delivered a copy of the order to the registrar in time`; `s 901J(6) the company's duty to deliver a copy of the order` |
| s 901J(7) | 12501-12503 | encoded |  | `s 901J(7) the person is guilty of an offence under section 901J(7)` |
| s 901J(7)(a) | 12502-12502 | encoded |  | `s 901J(7) the person is guilty of an offence under section 901J(7)` |
| s 901J(7)(b) | 12503-12503 | encoded |  | `s 901J(7) the person is guilty of an offence under section 901J(7)` |
| s 901J(8) | 12504-12504 | encoded |  | `s 901J(8) the penalty on conviction` |
| Obligations of company with respect to articles etc (the second limb (c) as printed) | 12505-12505 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901K | 12506-12523 | encoded | F10 | 6 rules, see the rows below |
| s 901K(1) | 12507-12509 | encoded |  | `s 901K(1) this section applies to the order` |
| s 901K(1)(a) | 12508-12508 | encoded |  | `s 901K(1) this section applies to the order` |
| s 901K(1)(b) | 12509-12509 | encoded |  | `s 901K(1) this section applies to the order` |
| s 901K(2) | 12510-12515 | encoded |  | `s 901K(2) the copy of the order is accompanied as the section requires` |
| s 901K(2)(a) | 12511-12513 | encoded |  | `s 901K(2) the copy of the order is accompanied as the section requires` |
| s 901K(2)(b) | 12514-12515 | encoded |  | `s 901K(2) the copy of the order is accompanied as the section requires` |
| s 901K(3) | 12516-12516 | fork | F10 | `s 901K(3) the copy of the articles is accompanied as the section requires` |
| s 901K(4) | 12517-12519 | encoded |  | `s 901K(4) the thing is within the reference` |
| s 901K(4)(a) | 12518-12518 | encoded |  | `s 901K(4) the thing is within the reference` |
| s 901K(4)(b) | 12519-12519 | encoded |  | `s 901K(4) the thing is within the reference` |
| s 901K(5) | 12520-12522 | encoded |  | `s 901K(5) the person is guilty of an offence under section 901K` |
| s 901K(5)(a) | 12521-12521 | encoded |  | `s 901K(5) the person is guilty of an offence under section 901K` |
| s 901K(5)(b) | 12522-12522 | encoded |  | `s 901K(5) the person is guilty of an offence under section 901K` |
| s 901K(6) | 12523-12523 | encoded |  | `s 901K(6) the penalty on conviction` |
| Power to amend Act | 12524-12524 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 901L | 12525-12527 | inert | reason 2 | s 901L: the power to amend the Act by regulations for the purposes of Part 26A (machinery) |
| s 901L(1) | 12526-12526 | inert | reason 2 | s 901L: the power to amend the Act by regulations for the purposes of Part 26A (machinery) |
| s 901L(2) | 12527-12527 | inert | reason 2 | s 901L: the power to amend the Act by regulations for the purposes of Part 26A (machinery) |
| Part 27 — Mergers and divisions of public companies | 12528-12528 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Chapter 1 — Introductory | 12529-12529 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 902 | 12530-12543 | encoded |  | 3 rules, see the rows below |
| s 902(1) | 12531-12539 | encoded |  | `s 902(1) this Part applies` |
| s 902(1)(a) | 12532-12535 | encoded |  | `s 902(1) this Part applies` |
| s 902(1)(b) | 12536-12538 | encoded |  | `s 902(1) this Part applies` |
| s 902(1)(c) | 12539-12539 | encoded |  | `s 902(1) this Part applies` |
| s 902(2) | 12540-12542 | encoded |  | `s 902(2)(a) the company is a new company` |
| s 902(2)(a) | 12541-12541 | encoded |  | `s 902(2)(a) the company is a new company` |
| s 902(2)(b) | 12542-12542 | encoded |  | `s 902(2)(a) the company is a new company` |
| s 902(3) | 12543-12543 | encoded |  | `s 902(3) the winding up of the company takes the compromise or arrangement out of this Part` |
| s 903 | 12544-12549 | encoded | F23 | 3 rules, see the rows below |
| s 903(1) | 12545-12545 | fork | F23 | `s 903(1) the requirements of this Part do not bar the court from sanctioning` |
| s 903(2) | 12546-12547 | fork | F23 | `s 903(2) the requirements applicable to a merger do not bar the court from sanctioning` |
| s 903(3) | 12548-12549 | fork | F23 | `s 903(3) the requirements applicable to a division do not bar the court from sanctioning` |
| Chapter 2 — Merger | 12550-12550 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Introductory | 12551-12551 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 904 | 12552-12558 | encoded |  | 4 rules, see the rows below |
| s 904(1) | 12553-12555 | encoded |  | `s 904(1) the scheme involves a merger` |
| s 904(1)(a) | 12554-12554 | encoded |  | `s 904(1) the scheme involves a merger`; `s 904(1)(a) the scheme involves a merger by absorption` |
| s 904(1)(b) | 12555-12555 | encoded |  | `s 904(1) the scheme involves a merger`; `s 904(1)(b) the scheme involves a merger by formation of a new company` |
| s 904(2) | 12556-12558 | encoded |  | `s 904(2) the company is one of the merging companies` |
| s 904(2)(a) | 12557-12557 | encoded |  | `s 904(2) the company is one of the merging companies` |
| s 904(2)(b) | 12558-12558 | encoded |  | `s 904(2) the company is one of the merging companies` |
| Requirements applicable to merger | 12559-12559 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 905 | 12560-12576 | encoded | F24 | 3 rules, see the rows below |
| s 905(1) | 12561-12561 | encoded |  | `s 905(1) the draft terms have been drawn up and adopted` |
| s 905(2) | 12562-12575 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(a) | 12563-12566 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(b) | 12567-12567 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(c) | 12568-12568 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(d) | 12569-12569 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(e) | 12570-12570 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(f) | 12571-12571 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(2)(g) | 12572-12575 | fork | F24 | `s 905(2) the draft terms give the particulars required` |
| s 905(3) | 12576-12576 | encoded |  | `s 905(3) the requirements in subsection (2)(b), (c) and (d) are subject to section 915` |
| s 906 | 12577-12581 | encoded | F18 F6 | 4 rules, see the rows below |
| s 906(1) | 12578-12578 | fork | F18 | `s 906(1) the directors have delivered a copy of the draft terms to the registrar` |
| s 906(2) | 12579-12579 | fork | F18 | `s 906(2) the registrar has published notice of receipt of the draft terms in the Gazette` |
| s 906(3) | 12580-12580 | fork | F18 F6 | `s 906(3) the notice was published at least one month before the meeting` |
| s 906(4) | 12581-12581 | fork | F18 | `s 906(4) the requirements in section 906 are subject to section 906A` |
| s 906A | 12582-12590 | encoded | F18 F6 | 6 rules, see the rows below |
| s 906A(1) | 12583-12583 | fork | F18 | `s 906A(1) section 906 does not apply in respect of the company` |
| s 906A(2) | 12584-12586 | fork | F18 | `s 906A(2) the first condition is met` |
| s 906A(2)(a) | 12585-12585 | fork | F18 | `s 906A(2) the first condition is met` |
| s 906A(2)(b) | 12586-12586 | fork | F18 | `s 906A(2) the first condition is met` |
| s 906A(3) | 12587-12587 | fork | F18 | `s 906A(3) the second condition is met` |
| s 906A(4) | 12588-12588 | fork | F18 | `s 906A(4) the third condition is met` |
| s 906A(5) | 12589-12589 | fork | F18 F6 | `s 906A(5) the fourth condition is met` |
| s 906A(6) | 12590-12590 | fork | F18 F6 | `s 906A(6) the fifth condition is met` |
| s 907 | 12591-12593 | encoded | F2 | 2 rules, see the rows below |
| s 907(1) | 12592-12592 | fork | F2 | `s 907(1) the scheme has been approved by the members of the merging company` |
| s 907(2) | 12593-12593 | encoded |  | `s 907(2) the meeting of members is not required` |
| s 908 | 12594-12604 | encoded |  | 4 rules, see the rows below |
| s 908(1) | 12595-12595 | encoded |  | `s 908(1) the directors have drawn up and adopted a report` |
| s 908(2) | 12596-12600 | encoded |  | `s 908(2) the report consists of what the section requires` |
| s 908(2)(a) | 12597-12597 | encoded |  | `s 908(2) the report consists of what the section requires` |
| s 908(2)(b) | 12598-12600 | encoded |  | `s 908(2) the report consists of what the section requires` |
| s 908(2A) | 12601-12603 | encoded |  | `s 908(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 908(2A)(a) | 12602-12602 | encoded |  | `s 908(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 908(2A)(b) | 12603-12603 | encoded |  | `s 908(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 908(3) | 12604-12604 | encoded |  | `s 908(3) the requirement in section 908 is excluded` |
| s 909 | 12605-12623 | encoded | F19 F25 | 6 rules, see the rows below |
| s 909(1) | 12606-12606 | encoded |  | `s 909(1) an expert's report has been drawn up on behalf of the company` |
| s 909(2) | 12607-12607 | encoded |  | `s 909(1) an expert's report has been drawn up on behalf of the company` |
| s 909(3) | 12608-12609 | fork | F19 | `s 909(3) the way the expert's report is drawn up complies` |
| s 909(4) | 12610-12612 | encoded |  | `s 909(4) the person may be the expert` |
| s 909(4)(a) | 12611-12611 | encoded |  | `s 909(4) the person may be the expert` |
| s 909(4)(b) | 12612-12612 | encoded |  | `s 909(4) the person may be the expert` |
| s 909(5) | 12613-12618 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(5)(a) | 12614-12614 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(5)(b) | 12615-12615 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(5)(c) | 12616-12616 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(5)(d) | 12617-12617 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(5)(e) | 12618-12618 | encoded |  | `s 909(5) the expert's report contains what the section requires` |
| s 909(6) | 12619-12622 | fork | F25 | `s 909(6) the expert has the right of access to the document or to require the information` |
| s 909(6)(a) | 12620-12620 | fork | F25 | `s 909(6) the expert has the right of access to the document or to require the information` |
| s 909(6)(b) | 12621-12622 | fork | F25 | `s 909(6) the expert has the right of access to the document or to require the information` |
| s 909(7) | 12623-12623 | encoded |  | `s 909(7) the requirement in section 909 is excluded` |
| s 910 | 12624-12635 | encoded | F20 F25 F6 | 7 rules, see the rows below |
| s 910(1) | 12625-12627 | fork | F25 F6 | `s 910(1) this section applies` |
| s 910(1)(a) | 12626-12626 | fork | F25 F6 | `s 910(1) this section applies` |
| s 910(1)(b) | 12627-12627 | fork | F25 F6 | `s 910(1) this section applies` |
| s 910(1A) | 12628-12628 | encoded |  | `s 910(1A) the directors have prepared a supplementary accounting statement` |
| s 910(2) | 12629-12631 | fork | F20 F6 | `s 910(2) the statement consists of what the section requires` |
| s 910(2)(a) | 12630-12630 | fork | F20 F6 | `s 910(2) the statement consists of what the section requires` |
| s 910(2)(b) | 12631-12631 | fork | F20 F6 | `s 910(2) the statement consists of what the section requires` |
| s 910(3) | 12632-12632 | encoded |  | `s 910(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` |
| s 910(4) | 12633-12633 | encoded |  | `s 910(4) the balance sheet has been approved and signed as section 414 provides` |
| s 910(5) | 12634-12634 | encoded |  | `s 910(5) the report is a half-yearly financial report` |
| s 910(6) | 12635-12635 | encoded |  | `s 910(6) the requirement in section 910 is excluded` |
| s 911 | 12636-12655 | encoded | F6 | 8 rules, see the rows below |
| s 911(1) | 12637-12639 | encoded |  | `s 911(1) the members could inspect the documents and obtain copies` |
| s 911(1)(a) | 12638-12638 | encoded |  | `s 911(1) the members could inspect the documents and obtain copies` |
| s 911(1)(b) | 12639-12639 | encoded |  | `s 911(1) the members could inspect the documents and obtain copies` |
| s 911(2) | 12640-12643 | fork | F6 | `s 911(2) the members could inspect and obtain copies throughout the period` |
| s 911(2)(a) | 12641-12641 | fork | F6 | `s 911(2) the members could inspect and obtain copies throughout the period` |
| s 911(2)(b) | 12642-12643 | fork | F6 | `s 911(2) the members could inspect and obtain copies throughout the period` |
| s 911(3) | 12644-12650 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(a) | 12645-12645 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(b) | 12646-12646 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(c) | 12647-12647 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(d) | 12648-12648 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(e) | 12649-12649 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3)(f) | 12650-12650 | encoded |  | `s 911(3) the document is one the members must be able to inspect` |
| s 911(3A) | 12651-12651 | encoded |  | `s 911(3A) the requirement in section 911(1)(a) is subject to section 911A(1)` |
| s 911(4) | 12652-12652 | encoded |  | `s 911(4) the requirements of subsection (3)(b) and (c) are excluded` |
| s 911(5) | 12653-12653 | encoded |  | `s 911(5) section 1145 does not apply to the document` |
| s 911(6) | 12654-12654 | encoded |  | `s 911(6) Part 4 of Schedule 5 does not apply` |
| s 911(7) | 12655-12655 | encoded |  | `s 911(7) the requirements in section 911 are excluded` |
| s 911A | 12656-12668 | encoded | F6 | 6 rules, see the rows below |
| s 911A(1) | 12657-12657 | encoded |  | `s 911A(1) section 911(1)(a) does not apply to the document` |
| s 911A(2) | 12658-12660 | encoded |  | `s 911A(2) the first condition is met` |
| s 911A(2)(a) | 12659-12659 | encoded |  | `s 911A(2) the first condition is met` |
| s 911A(2)(b) | 12660-12660 | encoded |  | `s 911A(2) the first condition is met` |
| s 911A(3) | 12661-12661 | encoded |  | `s 911A(3) the second condition is met` |
| s 911A(4) | 12662-12662 | fork | F6 | `s 911A(4) the third condition is met` |
| s 911A(5) | 12663-12667 | encoded |  | `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| s 911A(5)(a) | 12664-12664 | encoded |  | `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| s 911A(5)(b) | 12665-12667 | encoded |  | `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| s 911A(6) | 12668-12668 | encoded |  | `s 911A(6) members can obtain copies only as mentioned in subsection (5)` |
| s 911B | 12669-12677 | encoded |  | 3 rules, see the rows below |
| s 911B(1) | 12670-12673 | encoded |  | `s 911B(1) the directors have reported material changes in property and liabilities` |
| s 911B(1)(a) | 12671-12671 | encoded |  | `s 911B(1) the directors have reported material changes in property and liabilities` |
| s 911B(1)(b) | 12672-12673 | encoded |  | `s 911B(1) the directors have reported material changes in property and liabilities` |
| s 911B(2) | 12674-12676 | encoded |  | `s 911B(2) the directors of the other merging companies have reported those matters in turn` |
| s 911B(2)(a) | 12675-12675 | encoded |  | `s 911B(2) the directors of the other merging companies have reported those matters in turn` |
| s 911B(2)(b) | 12676-12676 | encoded |  | `s 911B(2) the directors of the other merging companies have reported those matters in turn` |
| s 911B(3) | 12677-12677 | encoded |  | `s 911B(3) the requirement in section 911B is excluded` |
| s 912 | 12678-12680 | encoded |  | 1 rules, see the rows below |
| s 912(1) | 12679-12679 | encoded |  | `s 912(1) the articles of the transferee company have been approved by ordinary resolution` |
| s 912(2) | 12680-12680 | encoded |  | `s 912(1) the articles of the transferee company have been approved by ordinary resolution` |
| s 913 | 12681-12685 | encoded |  | 1 rules, see the rows below |
| s 913(1) | 12682-12682 | encoded |  | `s 913(1) the scheme protects the holder of securities to which special rights are attached` |
| s 913(2) | 12683-12685 | encoded |  | `s 913(1) the scheme protects the holder of securities to which special rights are attached` |
| s 913(2)(a) | 12684-12684 | encoded |  | `s 913(1) the scheme protects the holder of securities to which special rights are attached` |
| s 913(2)(b) | 12685-12685 | encoded |  | `s 913(1) the scheme protects the holder of securities to which special rights are attached` |
| s 914 | 12686-12689 | encoded |  | 1 rules, see the rows below |
| s 914(a) | 12688-12688 | encoded |  | `s 914 the scheme does not provide for the allotment of shares the section forbids` |
| s 914(b) | 12689-12689 | encoded |  | `s 914 the scheme does not provide for the allotment of shares the section forbids` |
| Exceptions where shares of transferor company held by transf | 12690-12690 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 915 | 12691-12700 | encoded |  | 7 rules, see the rows below |
| s 915(1) | 12692-12692 | encoded |  | `s 915(1) this section applies` |
| s 915(2) | 12693-12693 | encoded |  | `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)` |
| s 915(3) | 12694-12694 | encoded |  | `s 915(3) section 897 does not apply` |
| s 915(3A) | 12695-12695 | encoded |  | `s 915(3A) section 901D does not apply` |
| s 915(4) | 12696-12698 | encoded |  | `s 915(4) the requirements of sections 908 and 909 do not apply` |
| s 915(5) | 12699-12699 | encoded |  | `s 915(5) the requirements of section 911 so far as relating to a document required to be drawn up under sections 908 and 909 do not apply` |
| s 915(6) | 12700-12700 | encoded |  | `s 915(6) the securities are relevant securities` |
| s 915A | 12701-12714 | encoded | F7 F8 | 6 rules, see the rows below |
| s 915A(1) | 12702-12702 | fork | F7 | `s 915A(1) this section applies` |
| s 915A(2) | 12703-12708 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(2)(a) | 12704-12704 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(2)(b) | 12705-12705 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(2)(c) | 12706-12706 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(2)(d) | 12707-12707 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(2)(e) | 12708-12708 | encoded |  | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| s 915A(3) | 12709-12709 | encoded |  | `s 915A(3) the first condition is met` |
| s 915A(4) | 12710-12710 | fork | F8 | `s 915A(4) the second condition is met` |
| s 915A(5) | 12711-12711 | encoded |  | `s 915A(5) the court may determine, or make provision for the determination of, the consideration` |
| s 915A(6) | 12712-12714 | encoded |  | `s 915A(6) the person is an other holder` |
| s 915A(6)  other holder  | 12713-12713 | encoded |  | `s 915A(6) the person is an other holder` |
| s 915A(6)  relevant securities  | 12714-12714 | encoded |  | `s 915A(6) the person is an other holder` |
| s 916 | 12715-12737 | encoded | F18 F4 F6 F7 | 12 rules, see the rows below |
| s 916(1) | 12716-12716 | fork | F7 | `s 916(1) this section applies` |
| s 916(2) | 12717-12717 | fork | F4 | `s 916(2) the meeting of members of the transferee company is not required` |
| s 916(3) | 12718-12718 | encoded |  | `s 916(3) the first condition is met` |
| s 916(3A) | 12719-12719 | fork | F18 F6 | `s 916(3A) subsection (3A) is satisfied` |
| s 916(3B) | 12720-12723 | fork | F6 | `s 916(3B) subsection (3B) is satisfied` |
| s 916(3B)(a) | 12721-12721 | fork | F6 | `s 916(3B) subsection (3B) is satisfied` |
| s 916(3B)(b) | 12722-12722 | fork | F6 | `s 916(3B) subsection (3B) is satisfied` |
| s 916(3B)(c) | 12723-12723 | fork | F6 | `s 916(3B) subsection (3B) is satisfied` |
| s 916(4) | 12724-12724 | encoded |  | `s 916(4) the second condition is met` |
| s 916(4A) | 12725-12725 | fork | F6 | `s 916(4A) subsection (4A) is satisfied for the document` |
| s 916(4B) | 12726-12729 | fork | F6 | `s 916(4B) subsection (4B) is satisfied for the document` |
| s 916(4B)(a) | 12727-12727 | fork | F6 | `s 916(4B) subsection (4B) is satisfied for the document` |
| s 916(4B)(b) | 12728-12728 | fork | F6 | `s 916(4B) subsection (4B) is satisfied for the document` |
| s 916(4B)(c) | 12729-12729 | fork | F6 | `s 916(4B) subsection (4B) is satisfied for the document` |
| s 916(4C) | 12730-12730 | fork | F6 | `s 916(4C) the third condition is met` |
| s 916(4D) | 12731-12733 | encoded |  | `s 916(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 916(4D)(a) | 12732-12732 | encoded |  | `s 916(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 916(4D)(b) | 12733-12733 | encoded |  | `s 916(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 916(5) | 12734-12736 | encoded |  | `s 916(5) the fourth condition is met` |
| s 916(5)(a) | 12735-12735 | encoded |  | `s 916(5) the fourth condition is met` |
| s 916(5)(b) | 12736-12736 | encoded |  | `s 916(5) the fourth condition is met` |
| s 916(6) | 12737-12737 | encoded |  | `s 916(6) the securities are relevant securities` |
| s 917 | 12738-12760 | encoded | F18 F4 F6 | 12 rules, see the rows below |
| s 917(1) | 12739-12739 | encoded |  | `s 917(1) this section applies` |
| s 917(2) | 12740-12740 | fork | F4 | `s 917(2) the meeting of members of any of the merging companies is not required` |
| s 917(3) | 12741-12741 | encoded |  | `s 917(3) the first condition is met` |
| s 917(3A) | 12742-12742 | fork | F18 F6 | `s 917(3A) subsection (3A) is satisfied` |
| s 917(3B) | 12743-12746 | fork | F6 | `s 917(3B) subsection (3B) is satisfied` |
| s 917(3B)(a) | 12744-12744 | fork | F6 | `s 917(3B) subsection (3B) is satisfied` |
| s 917(3B)(b) | 12745-12745 | fork | F6 | `s 917(3B) subsection (3B) is satisfied` |
| s 917(3B)(c) | 12746-12746 | fork | F6 | `s 917(3B) subsection (3B) is satisfied` |
| s 917(4) | 12747-12747 | encoded |  | `s 917(4) the second condition is met` |
| s 917(4A) | 12748-12748 | fork | F6 | `s 917(4A) subsection (4A) is satisfied for the document` |
| s 917(4B) | 12749-12752 | fork | F6 | `s 917(4B) subsection (4B) is satisfied for the document` |
| s 917(4B)(a) | 12750-12750 | fork | F6 | `s 917(4B) subsection (4B) is satisfied for the document` |
| s 917(4B)(b) | 12751-12751 | fork | F6 | `s 917(4B) subsection (4B) is satisfied for the document` |
| s 917(4B)(c) | 12752-12752 | fork | F6 | `s 917(4B) subsection (4B) is satisfied for the document` |
| s 917(4C) | 12753-12753 | fork | F6 | `s 917(4C) the third condition is met` |
| s 917(4D) | 12754-12756 | encoded |  | `s 917(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 917(4D)(a) | 12755-12755 | encoded |  | `s 917(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 917(4D)(b) | 12756-12756 | encoded |  | `s 917(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 917(5) | 12757-12759 | encoded |  | `s 917(5) the fourth condition is met` |
| s 917(5)(a) | 12758-12758 | encoded |  | `s 917(5) the fourth condition is met` |
| s 917(5)(b) | 12759-12759 | encoded |  | `s 917(5) the fourth condition is met` |
| s 917(6) | 12760-12760 | encoded |  | `s 917(6) the securities are relevant securities` |
| Other exceptions | 12761-12761 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 917A | 12762-12763 | encoded |  | 1 rules, see the rows below |
| s 918 | 12764-12784 | encoded | F18 F4 F6 | 10 rules, see the rows below |
| s 918(1) | 12765-12765 | fork | F4 | `s 918(1) the meeting of members of the transferee company is not required` |
| s 918(2) | 12766-12766 | encoded |  | `s 918(2) the first condition is met` |
| s 918(2A) | 12767-12767 | fork | F18 F6 | `s 918(2A) subsection (2A) is satisfied` |
| s 918(2B) | 12768-12771 | fork | F6 | `s 918(2B) subsection (2B) is satisfied` |
| s 918(2B)(a) | 12769-12769 | fork | F6 | `s 918(2B) subsection (2B) is satisfied` |
| s 918(2B)(b) | 12770-12770 | fork | F6 | `s 918(2B) subsection (2B) is satisfied` |
| s 918(2B)(c) | 12771-12771 | fork | F6 | `s 918(2B) subsection (2B) is satisfied` |
| s 918(3) | 12772-12772 | encoded |  | `s 918(3) the second condition is met` |
| s 918(3A) | 12773-12773 | fork | F6 | `s 918(3A) subsection (3A) is satisfied for the document` |
| s 918(3B) | 12774-12777 | fork | F6 | `s 918(3B) subsection (3B) is satisfied for the document` |
| s 918(3B)(a) | 12775-12775 | fork | F6 | `s 918(3B) subsection (3B) is satisfied for the document` |
| s 918(3B)(b) | 12776-12776 | fork | F6 | `s 918(3B) subsection (3B) is satisfied for the document` |
| s 918(3B)(c) | 12777-12777 | fork | F6 | `s 918(3B) subsection (3B) is satisfied for the document` |
| s 918(3C) | 12778-12778 | fork | F6 | `s 918(3C) the third condition is met` |
| s 918(3D) | 12779-12781 | encoded |  | `s 918(3D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 918(3D)(a) | 12780-12780 | encoded |  | `s 918(3D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 918(3D)(b) | 12781-12781 | encoded |  | `s 918(3D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 918(4) | 12782-12784 | encoded |  | `s 918(4) the fourth condition is met` |
| s 918(4)(a) | 12783-12783 | encoded |  | `s 918(4) the fourth condition is met` |
| s 918(4)(b) | 12784-12784 | encoded |  | `s 918(4) the fourth condition is met` |
| s 918A | 12785-12800 | encoded |  | 4 rules, see the rows below |
| s 918A(1) | 12786-12786 | encoded |  | `s 918A(1) the requirements are dispensed with by agreement` |
| s 918A(1A) | 12787-12793 | encoded |  | `s 918A(1A) the requirement is one that may be dispensed with under section 918A` |
| s 918A(1A)(a) | 12788-12792 | encoded |  | `s 918A(1A) the requirement is one that may be dispensed with under section 918A` |
| s 918A(1A)(b) | 12793-12793 | encoded |  | `s 918A(1A) the requirement is one that may be dispensed with under section 918A` |
| s 918A(2) | 12794-12797 | encoded |  | `s 918A(2) the holding counts for the purposes of section 918A` |
| s 918A(2)(a) | 12795-12795 | encoded |  | `s 918A(2) the holding counts for the purposes of section 918A` |
| s 918A(2)(b) | 12796-12797 | encoded |  | `s 918A(2) the holding counts for the purposes of section 918A` |
| s 918A(3) | 12798-12800 | encoded |  | `s 918A(3) the date of the relevant application` |
| s 918A(3)(a) | 12799-12799 | encoded |  | `s 918A(3) the date of the relevant application` |
| s 918A(3)(b) | 12800-12800 | encoded |  | `s 918A(3) the date of the relevant application` |
| Chapter 3 — Division | 12801-12801 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Introductory (the second limb (c) as printed) | 12802-12802 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 919 | 12803-12807 | encoded |  | 2 rules, see the rows below |
| s 919(1) | 12804-12806 | encoded |  | `s 919(1) the scheme involves a division` |
| s 919(1)(a) | 12805-12805 | encoded |  | `s 919(1) the scheme involves a division` |
| s 919(1)(b) | 12806-12806 | encoded |  | `s 919(1) the scheme involves a division` |
| s 919(2) | 12807-12807 | encoded |  | `s 919(2) the company is one of the companies involved in the division` |
| Requirements to be complied with in case of division | 12808-12808 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 920 | 12809-12828 | encoded | F24 | 3 rules, see the rows below |
| s 920(1) | 12810-12810 | encoded |  | `s 920(1) the draft terms have been drawn up and adopted` |
| s 920(2) | 12811-12824 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(a) | 12812-12815 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(b) | 12816-12816 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(c) | 12817-12817 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(d) | 12818-12818 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(e) | 12819-12819 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(f) | 12820-12820 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(2)(g) | 12821-12824 | fork | F24 | `s 920(2) the draft terms give the particulars required` |
| s 920(3) | 12825-12828 | encoded |  | `s 920(3) the draft terms also do what the section requires` |
| s 920(3)(a) | 12826-12826 | encoded |  | `s 920(3) the draft terms also do what the section requires` |
| s 920(3)(b) | 12827-12827 | encoded |  | `s 920(3) the draft terms also do what the section requires` |
| s 920(3)(c) | 12828-12828 | encoded |  | `s 920(3) the draft terms also do what the section requires` |
| s 921 | 12829-12833 | encoded | F6 F9 | 4 rules, see the rows below |
| s 921(1) | 12830-12830 | encoded |  | `s 921(1) the directors have delivered a copy of the draft terms to the registrar` |
| s 921(2) | 12831-12831 | encoded |  | `s 921(2) the registrar has published notice of receipt of the draft terms in the Gazette` |
| s 921(3) | 12832-12832 | fork | F6 | `s 921(3) the notice was published at least one month before the meeting` |
| s 921(4) | 12833-12833 | fork | F9 | `s 921(4) the requirements in section 921 are excluded` |
| s 921A | 12834-12842 | encoded | F6 | 6 rules, see the rows below |
| s 921A(1) | 12835-12835 | encoded |  | `s 921A(1) section 921 does not apply in respect of the company` |
| s 921A(2) | 12836-12838 | encoded |  | `s 921A(2) the first condition is met` |
| s 921A(2)(a) | 12837-12837 | encoded |  | `s 921A(2) the first condition is met` |
| s 921A(2)(b) | 12838-12838 | encoded |  | `s 921A(2) the first condition is met` |
| s 921A(3) | 12839-12839 | encoded |  | `s 921A(3) the second condition is met` |
| s 921A(4) | 12840-12840 | encoded |  | `s 921A(4) the third condition is met` |
| s 921A(5) | 12841-12841 | fork | F6 | `s 921A(5) the fourth condition is met` |
| s 921A(6) | 12842-12842 | fork | F6 | `s 921A(6) the fifth condition is met` |
| s 922 | 12843-12845 | encoded | F2 | 2 rules, see the rows below |
| s 922(1) | 12844-12844 | fork | F2 | `s 922(1) the scheme has been approved by the members of a company involved in the division` |
| s 922(2) | 12845-12845 | encoded |  | `s 922(2) the meeting of members is not required` |
| s 923 | 12846-12859 | encoded |  | 5 rules, see the rows below |
| s 923(1) | 12847-12847 | encoded |  | `s 923(1) the directors have drawn up and adopted a report` |
| s 923(2) | 12848-12852 | encoded |  | `s 923(2) the report consists of what the section requires` |
| s 923(2)(a) | 12849-12849 | encoded |  | `s 923(2) the report consists of what the section requires` |
| s 923(2)(b) | 12850-12852 | encoded |  | `s 923(2) the report consists of what the section requires` |
| s 923(2A) | 12853-12855 | encoded |  | `s 923(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 923(2A)(a) | 12854-12854 | encoded |  | `s 923(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 923(2A)(b) | 12855-12855 | encoded |  | `s 923(2A) the required statement explaining the effect of the compromise or arrangement` |
| s 923(3) | 12856-12858 | encoded |  | `s 923(3) the report states what the section requires` |
| s 923(3)(a) | 12857-12857 | encoded |  | `s 923(3) the report states what the section requires` |
| s 923(3)(b) | 12858-12858 | encoded |  | `s 923(3) the report states what the section requires` |
| s 923(4) | 12859-12859 | encoded |  | `s 923(4) the requirement in section 923 is excluded` |
| s 924 | 12860-12878 | encoded | F19 | 6 rules, see the rows below |
| s 924(1) | 12861-12861 | encoded |  | `s 924(1) an expert's report has been drawn up on behalf of the company` |
| s 924(2) | 12862-12862 | encoded |  | `s 924(1) an expert's report has been drawn up on behalf of the company` |
| s 924(3) | 12863-12864 | fork | F19 | `s 924(3) the way the expert's report is drawn up complies` |
| s 924(4) | 12865-12867 | encoded |  | `s 924(4) the person may be the expert` |
| s 924(4)(a) | 12866-12866 | encoded |  | `s 924(4) the person may be the expert` |
| s 924(4)(b) | 12867-12867 | encoded |  | `s 924(4) the person may be the expert` |
| s 924(5) | 12868-12873 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(5)(a) | 12869-12869 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(5)(b) | 12870-12870 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(5)(c) | 12871-12871 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(5)(d) | 12872-12872 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(5)(e) | 12873-12873 | encoded |  | `s 924(5) the expert's report contains what the section requires` |
| s 924(6) | 12874-12877 | encoded |  | `s 924(6) the expert has the right of access to the document or to require the information` |
| s 924(6)(a) | 12875-12875 | encoded |  | `s 924(6) the expert has the right of access to the document or to require the information` |
| s 924(6)(b) | 12876-12877 | encoded |  | `s 924(6) the expert has the right of access to the document or to require the information` |
| s 924(7) | 12878-12878 | encoded |  | `s 924(7) the requirement in section 924 is excluded` |
| s 925 | 12879-12890 | encoded | F20 F6 | 7 rules, see the rows below |
| s 925(1) | 12880-12882 | fork | F6 | `s 925(1) this section applies` |
| s 925(1)(a) | 12881-12881 | fork | F6 | `s 925(1) this section applies` |
| s 925(1)(b) | 12882-12882 | fork | F6 | `s 925(1) this section applies` |
| s 925(1A) | 12883-12883 | encoded |  | `s 925(1A) the directors have prepared a supplementary accounting statement` |
| s 925(2) | 12884-12886 | fork | F20 F6 | `s 925(2) the statement consists of what the section requires` |
| s 925(2)(a) | 12885-12885 | fork | F20 F6 | `s 925(2) the statement consists of what the section requires` |
| s 925(2)(b) | 12886-12886 | fork | F20 F6 | `s 925(2) the statement consists of what the section requires` |
| s 925(3) | 12887-12887 | encoded |  | `s 925(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` |
| s 925(4) | 12888-12888 | encoded |  | `s 925(4) the balance sheet has been approved and signed as section 414 provides` |
| s 925(4A) | 12889-12889 | encoded |  | `s 925(4A) the report is a half-yearly financial report` |
| s 925(5) | 12890-12890 | encoded |  | `s 925(5) the requirement in section 925 is excluded` |
| s 926 | 12891-12909 | encoded | F6 F9 | 7 rules, see the rows below |
| s 926(1) | 12892-12894 | encoded |  | `s 926(1) the members could inspect the documents and obtain copies` |
| s 926(1)(a) | 12893-12893 | encoded |  | `s 926(1) the members could inspect the documents and obtain copies` |
| s 926(1)(b) | 12894-12894 | encoded |  | `s 926(1) the members could inspect the documents and obtain copies` |
| s 926(2) | 12895-12898 | fork | F6 | `s 926(2) the members could inspect and obtain copies throughout the period` |
| s 926(2)(a) | 12896-12896 | fork | F6 | `s 926(2) the members could inspect and obtain copies throughout the period` |
| s 926(2)(b) | 12897-12898 | fork | F6 | `s 926(2) the members could inspect and obtain copies throughout the period` |
| s 926(3) | 12899-12905 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(a) | 12900-12900 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(b) | 12901-12901 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(c) | 12902-12902 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(d) | 12903-12903 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(e) | 12904-12904 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3)(f) | 12905-12905 | encoded |  | `s 926(3) the document is one the members must be able to inspect` |
| s 926(3A) | 12906-12906 | encoded |  | `s 926(3A) the requirement in section 926(1)(a) is subject to section 926A(1)` |
| s 926(4) | 12907-12907 | fork | F9 | `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded` |
| s 926(5) | 12908-12908 | encoded |  | `s 926(5) section 1145 does not apply to the document` |
| s 926(6) | 12909-12909 | encoded |  | `s 926(6) Part 4 of Schedule 5 does not apply` |
| s 926A | 12910-12922 | encoded | F6 | 6 rules, see the rows below |
| s 926A(1) | 12911-12911 | encoded |  | `s 926A(1) section 926(1)(a) does not apply to the document` |
| s 926A(2) | 12912-12914 | encoded |  | `s 926A(2) the first condition is met` |
| s 926A(2)(a) | 12913-12913 | encoded |  | `s 926A(2) the first condition is met` |
| s 926A(2)(b) | 12914-12914 | encoded |  | `s 926A(2) the first condition is met` |
| s 926A(3) | 12915-12915 | encoded |  | `s 926A(3) the second condition is met` |
| s 926A(4) | 12916-12916 | fork | F6 | `s 926A(4) the third condition is met` |
| s 926A(5) | 12917-12921 | encoded |  | `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| s 926A(5)(a) | 12918-12918 | encoded |  | `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| s 926A(5)(b) | 12919-12921 | encoded |  | `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| s 926A(6) | 12922-12922 | encoded |  | `s 926A(6) members can obtain copies only as mentioned in subsection (5)` |
| s 927 | 12923-12931 | encoded |  | 3 rules, see the rows below |
| s 927(1) | 12924-12927 | encoded |  | `s 927(1) the directors have reported material changes in property and liabilities` |
| s 927(1)(a) | 12925-12925 | encoded |  | `s 927(1) the directors have reported material changes in property and liabilities` |
| s 927(1)(b) | 12926-12927 | encoded |  | `s 927(1) the directors have reported material changes in property and liabilities` |
| s 927(2) | 12928-12930 | encoded |  | `s 927(2) the directors of each existing transferee company have reported those matters in turn` |
| s 927(2)(a) | 12929-12929 | encoded |  | `s 927(2) the directors of each existing transferee company have reported those matters in turn` |
| s 927(2)(b) | 12930-12930 | encoded |  | `s 927(2) the directors of each existing transferee company have reported those matters in turn` |
| s 927(3) | 12931-12931 | encoded |  | `s 927(3) the requirement in section 927 is excluded` |
| s 928 | 12932-12934 | encoded |  | 1 rules, see the rows below |
| s 928(1) | 12933-12933 | encoded |  | `s 928(1) the articles of every new transferee company have been approved by ordinary resolution of the transferor company` |
| s 928(2) | 12934-12934 | encoded |  | `s 928(1) the articles of every new transferee company have been approved by ordinary resolution of the transferor company` |
| s 929 | 12935-12939 | encoded |  | 1 rules, see the rows below |
| s 929(1) | 12936-12936 | encoded |  | `s 929(1) the scheme protects the holder of securities to which special rights are attached` |
| s 929(2) | 12937-12939 | encoded |  | `s 929(1) the scheme protects the holder of securities to which special rights are attached` |
| s 929(2)(a) | 12938-12938 | encoded |  | `s 929(1) the scheme protects the holder of securities to which special rights are attached` |
| s 929(2)(b) | 12939-12939 | encoded |  | `s 929(1) the scheme protects the holder of securities to which special rights are attached` |
| s 930 | 12940-12943 | encoded |  | 1 rules, see the rows below |
| s 930(a) | 12942-12942 | encoded |  | `s 930 the scheme does not provide for the allotment of shares the section forbids` |
| s 930(b) | 12943-12943 | encoded |  | `s 930 the scheme does not provide for the allotment of shares the section forbids` |
| Exceptions where shares of transferor company held by transf (the second limb (c) as printed) | 12944-12944 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 931 | 12945-12968 | encoded | F18 F4 F6 | 11 rules, see the rows below |
| s 931(1) | 12946-12946 | encoded |  | `s 931(1) this section applies` |
| s 931(2) | 12947-12947 | fork | F4 | `s 931(2) the meeting of members of the transferor company is not required` |
| s 931(3) | 12948-12948 | encoded |  | `s 931(3) the first condition is met` |
| s 931(3A) | 12949-12949 | fork | F18 F6 | `s 931(3A) subsection (3A) is satisfied` |
| s 931(3B) | 12950-12953 | fork | F6 | `s 931(3B) subsection (3B) is satisfied` |
| s 931(3B)(a) | 12951-12951 | fork | F6 | `s 931(3B) subsection (3B) is satisfied` |
| s 931(3B)(b) | 12952-12952 | fork | F6 | `s 931(3B) subsection (3B) is satisfied` |
| s 931(3B)(c) | 12953-12953 | fork | F6 | `s 931(3B) subsection (3B) is satisfied` |
| s 931(4) | 12954-12954 | encoded |  | `s 931(4) the second condition is met` |
| s 931(4A) | 12955-12955 | fork | F6 | `s 931(4A) subsection (4A) is satisfied for the document` |
| s 931(4B) | 12956-12959 | fork | F6 | `s 931(4B) subsection (4B) is satisfied for the document` |
| s 931(4B)(a) | 12957-12957 | fork | F6 | `s 931(4B) subsection (4B) is satisfied for the document` |
| s 931(4B)(b) | 12958-12958 | fork | F6 | `s 931(4B) subsection (4B) is satisfied for the document` |
| s 931(4B)(c) | 12959-12959 | fork | F6 | `s 931(4B) subsection (4B) is satisfied for the document` |
| s 931(4C) | 12960-12960 | fork | F6 | `s 931(4C) the third condition is met` |
| s 931(4D) | 12961-12963 | encoded |  | `s 931(4D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 931(4D)(a) | 12962-12962 | encoded |  | `s 931(4D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 931(4D)(b) | 12963-12963 | encoded |  | `s 931(4D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 931(5) | 12964-12964 | repealed or blank in this text |  | s 931(5): the text shows only dots (repealed or omitted) |
| s 931(6) | 12965-12968 | fork | F6 | `s 931(6) the fourth condition is met` |
| s 931(6)(a) | 12966-12966 | fork | F6 | `s 931(6) the fourth condition is met` |
| s 931(6)(b) | 12967-12968 | fork | F6 | `s 931(6) the fourth condition is met` |
| Other exceptions (the second limb (c) as printed) | 12969-12969 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 931A | 12970-12971 | encoded |  | 1 rules, see the rows below |
| s 932 | 12972-12993 | encoded | F18 F4 F6 F9 | 11 rules, see the rows below |
| s 932(1) | 12973-12973 | fork | F4 | `s 932(1) the meeting of members of the transferee company is not required` |
| s 932(2) | 12974-12974 | encoded |  | `s 932(2) the first condition is met` |
| s 932(2A) | 12975-12975 | fork | F18 F6 | `s 932(2A) subsection (2A) is satisfied` |
| s 932(2B) | 12976-12979 | fork | F6 | `s 932(2B) subsection (2B) is satisfied` |
| s 932(2B)(a) | 12977-12977 | fork | F6 | `s 932(2B) subsection (2B) is satisfied` |
| s 932(2B)(b) | 12978-12978 | fork | F6 | `s 932(2B) subsection (2B) is satisfied` |
| s 932(2B)(c) | 12979-12979 | fork | F6 | `s 932(2B) subsection (2B) is satisfied` |
| s 932(3) | 12980-12980 | encoded |  | `s 932(3) the second condition is met` |
| s 932(3A) | 12981-12981 | fork | F6 | `s 932(3A) subsection (3A) is satisfied for the document` |
| s 932(3B) | 12982-12985 | fork | F6 | `s 932(3B) subsection (3B) is satisfied for the document` |
| s 932(3B)(a) | 12983-12983 | fork | F6 | `s 932(3B) subsection (3B) is satisfied for the document` |
| s 932(3B)(b) | 12984-12984 | fork | F6 | `s 932(3B) subsection (3B) is satisfied for the document` |
| s 932(3B)(c) | 12985-12985 | fork | F6 | `s 932(3B) subsection (3B) is satisfied for the document` |
| s 932(3C) | 12986-12986 | fork | F6 | `s 932(3C) the third condition is met` |
| s 932(3D) | 12987-12989 | encoded |  | `s 932(3D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 932(3D)(a) | 12988-12988 | encoded |  | `s 932(3D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 932(3D)(b) | 12989-12989 | encoded |  | `s 932(3D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| s 932(4) | 12990-12992 | encoded |  | `s 932(4) the fourth condition is met` |
| s 932(4)(a) | 12991-12991 | encoded |  | `s 932(4) the fourth condition is met` |
| s 932(4)(b) | 12992-12992 | encoded |  | `s 932(4) the fourth condition is met` |
| s 932(5) | 12993-12993 | fork | F9 | `s 932(5) the first, second and third conditions are subject to section 934` |
| s 933 | 12994-13009 | encoded |  | 4 rules, see the rows below |
| s 933(1) | 12995-12995 | encoded |  | `s 933(1) the requirements are dispensed with by agreement` |
| s 933(2) | 12996-13002 | encoded |  | `s 933(2) the requirement is one that may be dispensed with under section 933` |
| s 933(2)(a) | 12997-13001 | encoded |  | `s 933(2) the requirement is one that may be dispensed with under section 933` |
| s 933(2)(b) | 13002-13002 | encoded |  | `s 933(2) the requirement is one that may be dispensed with under section 933` |
| s 933(3) | 13003-13006 | encoded |  | `s 933(3) the holding counts for the purposes of section 933` |
| s 933(3)(a) | 13004-13004 | encoded |  | `s 933(3) the holding counts for the purposes of section 933` |
| s 933(3)(b) | 13005-13006 | encoded |  | `s 933(3) the holding counts for the purposes of section 933` |
| s 933(4) | 13007-13009 | encoded |  | `s 933(4) the date of the relevant application` |
| s 933(4)(a) | 13008-13008 | encoded |  | `s 933(4) the date of the relevant application` |
| s 933(4)(b) | 13009-13009 | encoded |  | `s 933(4) the date of the relevant application` |
| s 933A | 13010-13019 | encoded |  | 3 rules, see the rows below |
| s 933A(1) | 13011-13011 | encoded |  | `s 933A(1) this section applies` |
| s 933A(2) | 13012-13012 | encoded |  | `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` |
| s 933A(3) | 13013-13019 | encoded |  | `s 933A(3) the requirement is one that does not apply under section 933A` |
| s 933A(3)(a) | 13014-13018 | encoded |  | `s 933A(3) the requirement is one that does not apply under section 933A` |
| s 933A(3)(b) | 13019-13019 | encoded |  | `s 933A(3) the requirement is one that does not apply under section 933A` |
| s 934 | 13020-13034 | encoded | F32 F4 F9 | 6 rules, see the rows below |
| s 934(1) | 13021-13027 | fork | F32 F4 F9 | `s 934(1) the court may by order direct that the requirements do not apply`; `s 934(1)(a) the court has directed that sections 921 and 926 do not apply`; `s 934(1)(b) section 932 has effect without its first, second and third conditions` |
| s 934(1)(a) | 13022-13025 | fork | F32 F4 F9 | `s 934(1) the court may by order direct that the requirements do not apply`; `s 934(1)(a) the court has directed that sections 921 and 926 do not apply`; `s 934(1)(b) section 932 has effect without its first, second and third conditions` |
| s 934(1)(b) | 13026-13027 | fork | F32 F4 F9 | `s 934(1) the court may by order direct that the requirements do not apply`; `s 934(1)(a) the court has directed that sections 921 and 926 do not apply`; `s 934(1)(b) section 932 has effect without its first, second and third conditions` |
| s 934(2) | 13028-13030 | encoded |  | `s 934(2) the first condition is met` |
| s 934(2)(a) | 13029-13029 | encoded |  | `s 934(2) the first condition is met` |
| s 934(2)(b) | 13030-13030 | encoded |  | `s 934(2) the first condition is met` |
| s 934(3) | 13031-13033 | encoded |  | `s 934(3) the second condition is met` |
| s 934(3)(a) | 13032-13032 | encoded |  | `s 934(3) the second condition is met` |
| s 934(3)(b) | 13033-13033 | encoded |  | `s 934(3) the second condition is met` |
| s 934(4) | 13034-13034 | encoded |  | `s 934(4) the third condition is met` |
| Chapter 4 — Supplementary provisions | 13035-13035 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| Expert's report and related matters | 13036-13036 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 935 | 13037-13046 | encoded | F25 | 2 rules, see the rows below |
| s 935(1) | 13038-13043 | fork | F25 | `s 935(1) the expert may arrange for or accept the valuation` |
| s 935(1)(a) | 13039-13039 | fork | F25 | `s 935(1) the expert may arrange for or accept the valuation` |
| s 935(1)(b) | 13040-13043 | fork | F25 | `s 935(1) the expert may arrange for or accept the valuation` |
| s 935(2) | 13044-13046 | encoded |  | `s 935(2) the expert's report states what the section requires` |
| s 935(2)(a) | 13045-13045 | encoded |  | `s 935(2) the expert's report states what the section requires` |
| s 935(2)(b) | 13046-13046 | encoded |  | `s 935(2) the expert's report states what the section requires` |
| s 936 | 13047-13066 | encoded | F22 | 5 rules, see the rows below |
| s 936(1) | 13048-13058 | encoded |  | `s 936(1) the person meets the independence requirement` |
| s 936(1)(a) | 13049-13051 | encoded |  | `s 936(1) the person meets the independence requirement` |
| s 936(1)(b) | 13052-13054 | encoded |  | `s 936(1) the person meets the independence requirement` |
| s 936(1)(c) | 13055-13058 | encoded |  | `s 936(1) the person meets the independence requirement` |
| s 936(2) | 13059-13059 | fork | F22 | `s 936(2) the person is regarded as an officer or employee of the company for the purposes of section 936` |
| s 936(3) | 13060-13065 | encoded |  | `s 936(3)(a) the company is a company concerned in the scheme`; `s 936(3)(b) the undertaking is an associated undertaking of the company`; `s 936(3)(c) the person is an associate` |
| s 936(3)(a) | 13061-13061 | encoded |  | `s 936(3)(a) the company is a company concerned in the scheme` |
| s 936(3)(b) | 13062-13064 | encoded |  | `s 936(3)(b) the undertaking is an associated undertaking of the company` |
| s 936(3)(c) | 13065-13065 | encoded |  | `s 936(3)(c) the person is an associate` |
| s 936(4) | 13066-13066 | inert | reason 2 | s 936(4): regulations under this section are subject to negative resolution procedure (machinery) |
| s 937 | 13067-13082 | encoded | F11 | 2 rules, see the rows below |
| s 937(1) | 13068-13068 | encoded |  | `s 937(1) the definition applies` |
| s 937(2) | 13069-13072 | fork | F11 | `s 937 the person is an associate` |
| s 937(2)(a) | 13070-13070 | fork | F11 | `s 937 the person is an associate` |
| s 937(2)(b) | 13071-13071 | fork | F11 | `s 937 the person is an associate` |
| s 937(2)(c) | 13072-13072 | fork | F11 | `s 937 the person is an associate` |
| s 937(3) | 13073-13076 | fork | F11 | `s 937 the person is an associate` |
| s 937(3)(a) | 13074-13074 | fork | F11 | `s 937 the person is an associate` |
| s 937(3)(b) | 13075-13075 | fork | F11 | `s 937 the person is an associate` |
| s 937(3)(c) | 13076-13076 | fork | F11 | `s 937 the person is an associate` |
| s 937(4) | 13077-13080 | fork | F11 | `s 937 the person is an associate` |
| s 937(4)(a) | 13078-13078 | fork | F11 | `s 937 the person is an associate` |
| s 937(4)(b) | 13079-13079 | fork | F11 | `s 937 the person is an associate` |
| s 937(4)(c) | 13080-13080 | fork | F11 | `s 937 the person is an associate` |
| s 937(5) | 13081-13081 | fork | F11 | `s 937 the person is an associate` |
| s 937(6) | 13082-13082 | fork | F11 | `s 937 the person is an associate` |
| Powers of the court | 13083-13083 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 938 | 13084-13094 | encoded | F33 | 3 rules, see the rows below |
| s 938(1) | 13085-13088 | encoded |  | `s 938(1) the court may order a meeting of the members or creditors of the company` |
| s 938(1)(a) | 13086-13086 | encoded |  | `s 938(1) the court may order a meeting of the members or creditors of the company` |
| s 938(1)(b) | 13087-13088 | encoded |  | `s 938(1) the court may order a meeting of the members or creditors of the company` |
| s 938(2) | 13089-13093 | fork | F33 | `s 938(2) the person may apply to the court` |
| s 938(2)(a) | 13090-13090 | fork | F33 | `s 938(2) the person may apply to the court` |
| s 938(2)(b) | 13091-13091 | fork | F33 | `s 938(2) the person may apply to the court` |
| s 938(2)(c) | 13092-13092 | fork | F33 | `s 938(2) the person may apply to the court` |
| s 938(2)(d) | 13093-13093 | fork | F33 | `s 938(2) the person may apply to the court` |
| s 938(3) | 13094-13094 | encoded |  | `s 938(3) section 323 applies to the meeting` |
| s 939 | 13095-13103 | encoded | F6 | 5 rules, see the rows below |
| s 939(1) | 13096-13099 | encoded |  | `s 939(1) the court has fixed a date for the transfer` |
| s 939(1)(a) | 13097-13097 | encoded |  | `s 939(1) the court has fixed a date for the transfer` |
| s 939(1)(b) | 13098-13099 | encoded |  | `s 939(1) the court has fixed a date for the transfer` |
| s 939(2) | 13100-13100 | encoded |  | `s 939(2) the order fixes the same date for the dissolution` |
| s 939(3) | 13101-13101 | fork | F6 | `s 939(3) the court has fixed a date for the steps within six months` |
| s 939(4) | 13102-13102 | encoded |  | `s 939(4) the court may postpone the dissolution of the transferor company until that date` |
| s 939(5) | 13103-13103 | encoded |  | `s 939(5) the court may postpone or further postpone the date` |
| Liability of transferee companies | 13104-13104 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 940 | 13105-13111 | encoded | F12 F2 F5 | 3 rules, see the rows below |
| s 940(1) | 13106-13107 | fork | F12 | `s 940(1) the amount for which the transferee company is liable` |
| s 940(2) | 13108-13108 | fork | F2 F5 | `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` |
| s 940(2A) | 13109-13109 | fork | F2 F5 | `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` |
| s 940(3) | 13110-13111 | fork | F12 | `s 940(3) the net value transferred` |
| Disruption of websites | 13112-13112 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 940A | 13113-13126 | encoded | F13 | 2 rules, see the rows below |
| s 940A(1) | 13114-13116 | encoded |  | `s 940A(1) the failure is to be disregarded` |
| s 940A(1)(a) | 13115-13115 | encoded |  | `s 940A(1) the failure is to be disregarded` |
| s 940A(1)(b) | 13116-13116 | encoded |  | `s 940A(1) the failure is to be disregarded` |
| s 940A(2) | 13117-13126 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(a) | 13118-13118 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(b) | 13119-13119 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(c) | 13120-13120 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(d) | 13121-13121 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(e) | 13122-13122 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(f) | 13123-13123 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(g) | 13124-13124 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| s 940A(2)(h) | 13125-13126 | fork | F13 | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| Interpretation | 13127-13127 | inert | reason 1 | a Part, Chapter or cross-heading: not operative |
| s 941 | 13128-13131 | encoded |  | 2 rules, see the rows below |
| s 941 liabilities | 13130-13130 | encoded |  | `s 941 the thing is a liability` |
| s 941 property | 13131-13131 | encoded |  | `s 941 the thing is property` |

## Fork register (coa20)

Each entry: the provision, the function(s), the reading taken, the other reading, and the text that licenses it. Sites that the 2026-11-05 ruling leaves to the encoder carry one line here. F3, F15 and F21 are register-wide conventions that no single row names. F34 to F38 are rows the name-test sweep of 2026-11-12 listed instead of flipping; no coverage row or marginal-readings row names them.

The rulings that govern the `NOTHING-kind` tags in this subject, word for word from the brief (the keel and the other parts carry the same text):

- **E1** (bench `commons-negation-1030`): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04.
- **N2** (bench `commons-negation-1030`): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04.
- **Periods, "where" and scope limits** (2026-11-05): (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c."
- **Delegated definitions, defences and "until" bars** (2026-11-05): (a) a definition the text hands to a list: when no head holds, `JUST FALSE`; a bare list still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts"; (c) "when", "upon" and "whenever" count as "where"; (d) "the property does not pass until X": encode the bar (`JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed.
- **Questions with no convention: decide case by case (2026-11-05)**: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger: each gets one fork line for the human reviewer to overrule.

- **F1**: s 899(2): the text shows two versions of limb (c) (lines 12263-12265: 'if the company is being wound up or an administration order is in force in relation it, the liquidator or administrator' and, below it, 'if the company is being wound up, the liquidator, or (d) if the company is in administration, the administrator'). Taken: the union: the liquidator of a company being wound up may apply; the administrator of a company in administration or in relation to which an administration order is in force may apply. **Other reading:** Only the first (c), which would let a liquidator or administrator apply whenever either the winding up or the administration order is in force (a liquidator of a company in administration, say). **Licence:** Both limbs are printed in the rendering; they agree on every case except that. Functions: `s 899(2) the person may apply for the court's sanction`.
- **F2**: 'a majority in number representing 75% in value ... present and voting': two tests, each on those present and voting: more than half in number, and at least 75% in value (the text's '75%' is read as 'not less than'). Exactly half in number fails; exactly 75% in value passes. **Other reading:** A single test (a majority in number, which must also carry 75% in value of the whole class, not only of those voting); or 'more than 75%' in value. **Licence:** s 899(1), s 907(1), s 922(1), s 940(2): 'a majority in number representing 75% in value ... present and voting either in person or by proxy'. Functions: `s 899(1) the court may sanction the compromise or arrangement`, `s 907(1) the scheme has been approved by the members of the merging company`, `s 922(1) the scheme has been approved by the members of a company involved in the division`, `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors`.
- **F3**: A bare 'must' not done (the 2026-11-05 ruling leaves it to the encoder): the requirement function answers JUST FALSE (Part 26 and 26A) or `s 903(1) requirement not complied with` (Part 27). The answer is the text's own 'must', so it is not NOTHING. **Other reading:** NOTHING: 'must' alone does not say that a breach is the answer to 'is it satisfied?'. **Licence:** Every 'must' of ss 897, 898, 901, 901D, 901E, 901I, 901K, 905 to 914, 920 to 930, 935, 939.
- **F4**: 'if the court is satisfied ...': the court's satisfaction is a judgment the text hands to the court, so it is a conditional input (a plain BOOLEAN 'the court is satisfied'); where the text also lists conditions of fact, those are separate functions of the facts and the exemption needs both. One fork line for ss 901C(4), 901G(3), 916(2), 917(2), 918(1), 931(2), 932(1), 934(1). **Other reading:** The function answers only 'the conditions hold on these facts' and the court's satisfaction is left to the person's wording. **Licence:** 'it is not necessary for the scheme to be approved ... if the court is satisfied that the following conditions have been complied with' (ss 916(2), 917(2), 918(1), 931(2), 932(1)). Functions: `s 901C(4) subsection (3) does not apply in relation to the class`, `s 901G(3) condition A is met`, `s 916(2) the meeting of members of the transferee company is not required`, `s 917(2) the meeting of members of any of the merging companies is not required`, `s 918(1) the meeting of members of the transferee company is not required`, `s 931(2) the meeting of members of the transferor company is not required` (+2 more).
- **F5**: s 901F(1) and s 940(2A): 'a number representing 75% in value': no test of the number of persons voting (Part 26A drops the 'majority in number' of s 899(1) and s 940(2)). The encoding applies 75% in value only for Part 26A. **Other reading:** The headcount test of Part 26 is implied. **Licence:** Compare ss 899(1) and 901F(1), and ss 940(2) and 940(2A): the words 'a majority in number' are absent from the 26A texts. Functions: `s 901F(1) the court may sanction the compromise or arrangement`, `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors`.
- **F6**: Counting a month: 'one month before the date of a meeting' is the library's calendar month taken backwards from the meeting date (`add months` clamps the day: one month before 31 March is 28 February); 'at least one month before' means on or before that date; 'the period beginning one month before, and ending on, the date' includes both ends; 'seven months', 'six months', 'three months' before are counted the same way; 'not later than six months after' (s 939(3)) is counted forward and includes the last day; 'seven days after its making' (ss 900(6), 901J(6)) includes the seventh day. **Other reading:** Counting forward from the earlier date (31 January plus one month is 28 February, but 31 March minus one month and 28 February plus one month differ), or the 'corresponding date' rule of the Interpretation Act 1978, which is outside the sources. **Licence:** The Act does not say how a month is counted; the Interpretation Act 1978 is not among the sources. Functions: `s 900(6) the company delivered a copy of the order to the registrar in time`, `s 901J(6) the company delivered a copy of the order to the registrar in time`, `s 906(3) the notice was published at least one month before the meeting`, `s 906A(5) the fourth condition is met`, `s 906A(6) the fifth condition is met`, `s 910(1) this section applies` (+37 more).
- **F7**: '90% or more (but not all)' of the relevant securities of the transferor company 'or, if there is more than one, of each of them': each transferor company's holding is at least 90% and below 100%. **Other reading:** 'but not all' attaches to the transferor companies together, so one company may be wholly held if another is at least 90% held. **Licence:** s 915A(1), s 916(1). Functions: `s 915A(1) this section applies`, `s 916(1) this section applies`.
- **F8**: s 915A(4): 'if a holder of securities exercises that right, the consideration to be given for those securities is fair and reasonable': read as a forward-looking condition on the consideration that would be given; the function is true if that consideration is fair and reasonable, whether or not a holder has yet exercised the right. **Other reading:** Vacuously satisfied (or not covered) until a holder exercises the right. **Licence:** s 915A(4). Functions: `s 915A(4) the second condition is met`.
- **F9**: s 934(1): 'the court may by order direct that ... do not apply': where no order is made, the section excludes nothing, so the exclusion input is JUST FALSE (not NOTHING). **Other reading:** NOTHING: a grant ('may') limited by its own wording and not exercised. **Licence:** s 934(1). Functions: `s 921(4) the requirements in section 921 are excluded`, `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded`, `s 932(5) the first, second and third conditions are subject to section 934`, `s 934(1)(a) the court has directed that sections 921 and 926 do not apply`, `s 934(1)(b) section 932 has effect without its first, second and third conditions`.
- **F10**: An 'unless' once met (2026-11-05 case-by-case): 'every copy of the articles ... must be accompanied by a copy of the order, unless the effect of the order has been incorporated into the articles by amendment': once the effect is incorporated, nothing more is required, so 'the copy is accompanied as the section requires' is JUST TRUE. **Other reading:** JUST FALSE ('no accompanying copy is required'), which would give one answer to two different situations. **Licence:** s 901(3), s 901K(3). Functions: `s 901(3) the copy of the articles is accompanied as the section requires`, `s 901K(3) the copy of the articles is accompanied as the section requires`.
- **F11**: s 937(6): 'in relation to a limited liability partnership, for "director" read "member"': read as applying wherever the body corporate in the relationship is a limited liability partnership: the relationship 'a body corporate of which the other is a director (for a limited liability partnership, a member)' covers both. **Other reading:** Applies only where the person in relation to whom 'associate' is defined is itself a limited liability partnership. **Licence:** s 937(6). Functions: `s 937 the person is an associate`.
- **F12**: s 940(3): the 'net value transferred' is the value of the property less the liabilities transferred; a negative result is read as nil (a company is not liable for more than nothing). **Other reading:** A negative cap, which the text does not contemplate. **Licence:** s 940(3). Functions: `s 940(1) the amount for which the transferee company is liable`, `s 940(3) the net value transferred`.
- **F13**: s 940A(2): 'The provisions referred to above are' (a list): read as closed, so a provision not listed answers JUST FALSE. **Other reading:** NOTHING: the list is not closed with 'only'. **Licence:** s 940A(2). Functions: `s 940A(2) the provision is one of those to which section 940A(1) applies`.
- **F14**: s 899A(1)(a) and s 901H(1)(a): 'an application ... is made before the end of the period of 12 weeks beginning with the day after the end of any moratorium': the period is the 84 days from the day after the moratorium ends; an application on or before the 84th day is within it, and an application made during the moratorium is also 'before the end of the period' (literal reading). **Other reading:** Only an application made after the moratorium has ended counts; or an application on the 84th day is not 'before the end'. **Licence:** s 899A(1)(a), s 901H(1)(a). Functions: `s 899A(1) this section applies`, `s 901H(1) this section applies`.
- **F15**: In Parts 26 and 26A a requirement whose 'where' or 'if' gate is not met answers JUST FALSE (the 2026-11-05 ruling on 'where'), the same word as 'the requirement is not complied with'; the questions say which. In Part 27 the two are separate (`requirement does not apply` and `requirement not complied with`). **Other reading:** NOTHING for a failed gate (the requirement does not arise), keeping JUST FALSE for non-compliance. **Licence:** ss 897(1), 897(5), 901D(1), 901D(5), 901I(1), 901I(2).
- **F16**: A defence 'if he shows ...' (ruling of 2026-11-05 (b)): when it is not shown, the answer is JUST FALSE for that provision's defence ('this section gives no defence on these facts'), never 'no defence at all'. **Other reading:** NOTHING. **Licence:** s 897(7), s 901D(7). Functions: `s 897(5) the person is guilty of an offence under section 897`, `s 897(7) section 897(7) gives the person a defence on these facts`, `s 901D(5) the person is guilty of an offence under section 901D`, `s 901D(7) section 901D(7) gives the person a defence on these facts`.
- **F17**: 'has no effect until a copy ... has been delivered': encoded as the bar (ruling of 2026-11-05 (d)): JUST TRUE while no copy has been delivered; JUST FALSE once the step is done; the encoding never says the order has effect. **Other reading:** An 'effect' function answering JUST TRUE after delivery. **Licence:** s 899(4), s 901F(6). Functions: `s 899(4) the court's order cannot yet have effect`, `s 901F(6) the court's order cannot yet have effect`, `s 901J(6) the company delivered a copy of the order to the registrar in time`, `s 901J(6) the company's duty to deliver a copy of the order`.
- **F18**: Several meetings or companies: 'any meeting' and 'the first meeting', and 'in respect of all the merging companies', are each taken as one date (the first meeting; the latest publication date) supplied by the person. **Other reading:** A list of dates, one per company. **Licence:** ss 906(3), 906A(5), 916(3A), 917(3A), 918(2A), 931(3A), 932(2A). Functions: `s 906(1) the directors have delivered a copy of the draft terms to the registrar`, `s 906(2) the registrar has published notice of receipt of the draft terms in the Gazette`, `s 906(3) the notice was published at least one month before the meeting`, `s 906(4) the requirements in section 906 are subject to section 906A`, `s 906A(1) section 906 does not apply in respect of the company`, `s 906A(2) the first condition is met` (+9 more).
- **F19**: A joint expert approved by the court and a separate report as well: NOTHING (the text allows the joint expert and says only that, with no appointment, there must be separate reports). **Other reading:** JUST FALSE. **Licence:** s 909(3), s 924(3). Functions: `s 909(3) the way the expert's report is drawn up complies`, `s 924(3) the way the expert's report is drawn up complies`.
- **F20**: A balance sheet dated after the day the draft terms were adopted: NOTHING (the text speaks of a date 'not more than three months before' adoption). **Other reading:** JUST TRUE (it is not more than three months before). **Licence:** s 910(2)(a), s 925(2)(a). Functions: `s 910(2) the statement consists of what the section requires`, `s 925(2) the statement consists of what the section requires`.
- **F21**: A subsection that only says another provision applies or yields ('subject to section 899A', 'subject to Part 27') is not inert: it is a function answering JUST TRUE where the other provision applies and NOTHING where it does not (silent). Seven 'means'-style definitions answer JUST FALSE outside the definition; 'includes' definitions answer NOTHING outside it. **Other reading:** Inert (reason 1, a signpost that creates no rule of its own), as the keel treated its signposts (keel fork F7). **Licence:** The brief lists three reasons for inert and a signpost is none of them read literally.
- **F22**: s 936(2): an auditor is not regarded as an officer or employee: JUST FALSE for an auditor; NOTHING for anyone else (the subsection says nothing of them). **Other reading:** JUST TRUE for a non-auditor who is an officer. **Licence:** s 936(2). Functions: `s 936(2) the person is regarded as an officer or employee of the company for the purposes of section 936`.
- **F23**: s 903(1): a requirement that 'does not apply' is no bar; the court is barred only by a requirement that is not complied with; a requirement not covered gives NOTHING. **Other reading:** Only requirements 'complied with' lift the bar. **Licence:** s 903(1): 'unless the relevant requirements of this Part have been complied with'; ss 915 to 918A and 931 to 934 'modify or exclude' requirements. Functions: `s 903(1) the requirements of this Part do not bar the court from sanctioning`, `s 903(2) the requirements applicable to a merger do not bar the court from sanctioning`, `s 903(3) the requirements applicable to a division do not bar the court from sanctioning`.
- **F24**: s 905(2)(a), s 920(2)(a): particulars 'in respect of each transferor company and the transferee company' are taken as one BOOLEAN each (given for every one of them). **Other reading:** A list of BOOLEANs, one per company. **Licence:** s 905(2)(a), s 920(2)(a). Functions: `s 905(2) the draft terms give the particulars required`, `s 920(2) the draft terms give the particulars required`.
- **F25**: Open-textured judgments the text hands to someone ('financial difficulties that are affecting ... its ability to carry on business as a going concern', 'it appears to an expert', 'as he thinks necessary', 'reasonable') are plain BOOLEAN inputs. **Other reading:** None; the text names no test. **Licence:** ss 901A(2), 935(1), 909(6). Functions: `s 901A(2) condition A is met`, `s 901A(3) condition B is met`, `s 909(6) the expert has the right of access to the document or to require the information`, `s 910(1) this section applies`, `s 935(1) the expert may arrange for or accept the valuation`.
- **F26**: s 896(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'. **Licence:** s 896(2)(c) and (d). Functions: `s 896(2) the person may apply for an order for a meeting`.
- **F27**: s 899(1): 'If a majority in number representing 75% in value ... agree a compromise or arrangement, the court may ... sanction': when the votes fall short of that test the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The count test itself is fork F2. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar). **Licence:** s 899(1). Functions: `s 899(1) the court may sanction the compromise or arrangement`.
- **F28**: s 899(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). The two printed versions of limb (c) are fork F1. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'. **Licence:** s 899(2)(c) and (d). Functions: `s 899(2) the person may apply for the court's sanction`.
- **F29**: s 901C(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'. **Licence:** s 901C(2)(c) and (d). Functions: `s 901C(2) the person may apply to the court`.
- **F30**: s 901F(1): 'If a number representing 75% in value ... agree a compromise or arrangement, the court may ... sanction': when the value falls short of 75% the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The absence of a headcount test is fork F5. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar). **Licence:** s 901F(1). Functions: `s 901F(1) the court may sanction the compromise or arrangement`.
- **F31**: s 901F(3): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'. **Licence:** s 901F(3)(c) and (d). Functions: `s 901F(3) the person may apply to the court`.
- **F32**: s 934(1): 'the court may by order direct that ... if the court is satisfied that the following conditions will be fulfilled in relation to that company': when the court is not satisfied, or a condition of s 934(2) to (4) fails, the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The court's satisfaction as a conditional input is fork F4. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar). **Licence:** s 934(1). Functions: `s 934(1) the court may by order direct that the requirements do not apply`.
- **F33**: s 938(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'. **Licence:** s 938(2)(c) and (d). Functions: `s 938(2) the person may apply to the court`.
- **F34**: LISTED, NOT FLIPPED (name-test sweep of 2026-11-12); no coverage row or marginal-readings row names it. `s 900(2) the court may make provision for the matter` is named for a power and answers JUST FALSE where s 900(1) 'This section applies where ...' is not met. ASSUMED, NOT RULED, that a 'where' gate goes with this listed group: ruling (b) of 'Periods, where and scope limits' and ruling (c) of the 2026-11-05 delegated ruling say JUST FALSE, and the Guide's line on grants says NOTHING, so it is kept as JUST FALSE for the maintainer or a lawyer to decide. **Other reading:** NOTHING: a grant limited by its own wording, the case falling outside the limit (the Guide's line on grants). **Licence:** s 900(1)-(2): 'This section applies where ...'.
- **F35**: LISTED, NOT FLIPPED (name-test sweep of 2026-11-12); no coverage row or marginal-readings row names it. `s 901J(2) the court may make provision for the matter` is named for a power and answers JUST FALSE where s 901J(1) 'This section applies where ...' is not met. ASSUMED, NOT RULED, that a 'where' gate goes with this listed group: ruling (b) of 'Periods, where and scope limits' and ruling (c) of the 2026-11-05 delegated ruling say JUST FALSE, and the Guide's line on grants says NOTHING, so it is kept as JUST FALSE for the maintainer or a lawyer to decide. **Other reading:** NOTHING: a grant limited by its own wording, the case falling outside the limit (the Guide's line on grants). **Licence:** s 901J(1)-(2): 'This section applies where ...'.
- **F36**: LISTED, NOT FLIPPED (name-test sweep of 2026-11-12); no coverage row or marginal-readings row names it. `s 935(1) the expert may arrange for or accept the valuation` is named for a power and answers JUST FALSE where s 935(1) 'Where it appears to an expert ...' is not met (a valuation is reasonably necessary, it is reasonable for another person to make it, that person has the knowledge and meets the independence requirement). ASSUMED, NOT RULED, that a 'where' gate goes with this listed group: ruling (b) of 'Periods, where and scope limits' and ruling (c) of the 2026-11-05 delegated ruling say JUST FALSE, and the Guide's line on grants says NOTHING, so it is kept as JUST FALSE for the maintainer or a lawyer to decide. **Other reading:** NOTHING: a grant limited by its own wording, the case falling outside the limit (the Guide's line on grants). **Licence:** s 935(1): 'Where it appears to an expert ... he may arrange for or accept such a valuation'.
- **F37**: LISTED, NOT FLIPPED (name-test sweep of 2026-11-12); no coverage row or marginal-readings row names it. `s 897(4) the person is entitled to be provided by the company with a copy of the statement free of charge` is named 'entitled' and already answers NOTHING outside its conditions (an earlier answer, kept). An entitlement is a claim, not a power, and the Guide does not settle it, so it is a question for the maintainer or a lawyer. **Other reading:** JUST FALSE: the unmet 'where ... on making application' read as the text's own no (ruling (b) of 'Periods, where and scope limits'). **Licence:** s 897(4): 'Where a notice given by advertisement states ... every such creditor or member is entitled, on making application ...'.
- **F38**: LISTED, NOT FLIPPED (name-test sweep of 2026-11-12); no coverage row or marginal-readings row names it. `s 901D(4) the person is entitled to be provided by the company with a copy of the statement free of charge` is named 'entitled' and already answers NOTHING outside its conditions (an earlier answer, kept). An entitlement is a claim, not a power, and the Guide does not settle it, so it is a question for the maintainer or a lawyer. **Other reading:** JUST FALSE: the unmet 'where ... on making application' read as the text's own no (ruling (b) of 'Periods, where and scope limits'). **Licence:** s 901D(4): 'Where a notice given by advertisement states ... every such creditor or member is entitled, on making application ...'.

### Name-test sweep of 2026-11-12

Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" was read against its text: 32 functions (the same test over `coa20-part26.l4`, `coa20-part26a.l4`, `coa20-part27-merger.l4`, `coa20-part27-division.l4` and `coa20-part27-supp.l4`, cross-checked by `work/gen_notes.py`).
A function named for a grant or a power that answered `JUST FALSE` because an "if" gate failed now answers `NOTHING`, one fork line each (F26 to F33, also in the coverage rows and under the marginal readings); a bar, a duty, a qualification the text closes with "must be a person who", and a provision's own question keep `JUST FALSE`; a power gated by "where" and the "entitled" functions are listed, not flipped (F34 to F38), as assumed, not ruled.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 8 | 6 | 3 | 2 |

Not in any of the four columns: 8 functions that already answered `NOTHING` where their gate failed (no `JUST FALSE` to flip), and 5 that are not a grant at a gate (a definition, a rule of reading, or a list of what may be dispensed with) and never answer `JUST FALSE` of their own.

**Flipped to `NOTHING`:**

- F26: `s 896(2) the person may apply for an order for a meeting`
- F27: `s 899(1) the court may sanction the compromise or arrangement`
- F28: `s 899(2) the person may apply for the court's sanction`
- F29: `s 901C(2) the person may apply to the court`
- F30: `s 901F(1) the court may sanction the compromise or arrangement`
- F31: `s 901F(3) the person may apply to the court`
- F32: `s 934(1) the court may by order direct that the requirements do not apply`
- F33: `s 938(2) the person may apply to the court`

**Kept `JUST FALSE`:**

- `s 899A(3) the relevant creditor may participate in the meeting summoned under section 896`: a bar: "may not participate"
- `s 899A(5) the court may sanction the compromise or arrangement under section 899`: a bar: "may not sanction ... if it includes provision ... who has not agreed"
- `s 901H(3) the relevant creditor may participate in the meeting summoned under section 901C`: a bar: "may not participate"
- `s 901H(5) the court may sanction the compromise or arrangement under section 901F`: a bar: "may not sanction ... if it includes provision ... who has not agreed"
- `s 909(4) the person may be the expert`: the text says "must be a person who", which closes the condition
- `s 924(4) the person may be the expert`: the text says "must be a person who", which closes the condition

**Listed: "may" with where, when or upon (not flipped):**

- F34: `s 900(2) the court may make provision for the matter`
- F35: `s 901J(2) the court may make provision for the matter`
- F36: `s 935(1) the expert may arrange for or accept the valuation`

**Listed: "entitled" (not flipped):**

- F37: `s 897(4) the person is entitled to be provided by the company with a copy of the statement free of charge`
- F38: `s 901D(4) the person is entitled to be provided by the company with a copy of the statement free of charge`

**Already `NOTHING` at the gate, unchanged:**

- `s 896(1) the court may order a meeting of the creditors, class of creditors, members or class of members`
- `s 901C(1) the court may order a meeting of the creditors, class of creditors, members or class of members`
- `s 901C(3) the person must be permitted to participate in the meeting`
- `s 901F(4) the court may by the order make the provision`
- `s 915A(5) the court may determine, or make provision for the determination of, the consideration`
- `s 938(1) the court may order a meeting of the members or creditors of the company`
- `s 939(4) the court may postpone the dissolution of the transferor company until that date`
- `s 939(5) the court may postpone or further postpone the date`

**Not a grant at a gate, unchanged:**

- `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend`
- `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend`
- `s 901B(2) the person is an authorised person`
- `s 918A(1A) the requirement is one that may be dispensed with under section 918A`
- `s 933(2) the requirement is one that may be dispensed with under section 933`

## Jural relations (coa20)

Hohfeld's correlatives, stated once per provision as a relation between two parties, named neutrally (the holder of the right, privilege, power or immunity; the bearer of the correlative duty, no-right, liability or disability). The tags are written beside each rule in the layer-1 modules (`-- JURAL holder: kind | bearer: kind`) and this table is generated from them; a rule with no relation is listed once as `none`. A court, a registrar or an official is named only as the party the text names; there is no seat for an official. Where a rule has two relations they are separated by a semicolon. Rows marked "(by the kind of rule)" (174 assigned by pattern; a further 8 are listed as `none (a condition, a computation or a rule of reading)` by default, of 334 rules) carry no explicit tag in the source: the relation was assigned by the kind of rule (a penalty, a power to apply, a report or inspection duty, an exclusion) by patterns in `work/gen_notes.py`, and they are the weaker rows for a lawyer to check; the others were written beside the rule.

| provision (the locator of the rule) | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | section | L4 rule |
| --- | --- | --- | --- | --- |
| src:12206-12208 | none (a rule fixing the scope of the Part) | none | s 895 | `s 895(1) the provisions of Part 26 apply` |
| src:12209-12210 | none (a definition) | none | s 895 | `s 895(2) the reorganisation of the share capital is an arrangement` |
| src:12211-12213 | none (a definition) | none | s 895 | `s 895(2) the body is a company for the purposes of Part 26` |
| src:12214-12214 | none (a rule of precedence between Parts) | none | s 895 | `s 895(3) the provisions of Part 26 have effect subject to Part 27` |
| src:12217-12217 | the creditors or members concerned: liability to be summoned to a meeting ; the applicant: power to apply | the court: power (s 896(1)) ; the court: liability to hear it (s 896(2)) | s 896 | `s 896(1) the court may order a meeting of the creditors, class of creditors, members or class of members` |
| src:12218-12222 | the person named (the company, a creditor or member, the liquidator, the administrator): power to apply to the court (by the kind of rule) | the court: liability to hear the application | s 896 | `s 896(2) the person may apply for an order for a meeting` |
| src:12223-12223 | the company (a corporation that is a creditor): power to appoint a representative | the meeting: liability to receive that representative (s 323 is outside this range) | s 896 | `s 896(3) section 323 applies to the meeting` |
| src:12224-12224 | none (a signpost whose effect is s 899A) | none | s 896 | `s 896(4) section 896 is subject to section 899A` |
| src:12226-12230 | the creditor or member: claim to the statement | the company: duty to send it (s 897(1)(a)) | s 897 | `s 897(1) the notice summoning the meeting satisfies the requirement` |
| src:12231-12235 | the company: duty to explain ; interests of directors: duty of disclosure | the creditors and members: claim to the explanation (s 897(2)) ; the company (s 897(2)(b)) | s 897 | `s 897(2) the statement complies` |
| src:12236-12236 | the trustees for debenture holders: claim to the like explanation (by the kind of rule) | the company: duty to give it in the statement | s 897 | `s 897(3) the statement complies as respects debenture holders` |
| src:12237-12237 | the creditor or member entitled to attend: claim to a free copy | the company: duty to provide it | s 897 | `s 897(4) the person is entitled to be provided by the company with a copy of the statement free of charge` |
| src:12238-12245 | the State (a prosecuting power) | the company and every officer in default: liability to conviction | s 897 | `s 897(5) the person is guilty of an offence under section 897` |
| src:12245-12245 | the person who shows the refusal: immunity from conviction (by the kind of rule) | the State: disability to convict | s 897 | `s 897(7) section 897(7) gives the person a defence on these facts` |
| src:12246-12248 | the State (a power to prosecute and the court's power to sentence) | the person guilty: liability to the penalty | s 897 | `s 897(8) the penalty on conviction` |
| src:12250-12253 | the company: claim to notice of a director's or trustee's matters | any director of the company and any trustee for its debenture holders: duty to give it | s 898 | `s 898(1) the person is under a duty to give the company notice of the matter` |
| src:12254-12255 | the State | any person who makes default in complying with section 898: liability to conviction (s 898(2)) | s 898 | `s 898(2) the person commits an offence` |
| src:12258-12258 | the company, any creditor or member: power to apply ; the court: power to sanction | the court: liability to hear ; those bound: liability (s 899(1)) | s 899 | `s 899(1) the court may sanction the compromise or arrangement` |
| src:12259-12259 | none (a signpost whose effect is s 899A) | none | s 899 | `s 899(1A) section 899(1) is subject to section 899A` |
| src:12260-12265 | the person named (the company, a creditor or member, the liquidator, the administrator): power to apply to the court (by the kind of rule) | the court: liability to hear the application | s 899 | `s 899(2) the person may apply for the court's sanction` |
| src:12266-12268 | the company, the creditors and members concerned: (the court's sanction is a power over them) | those bound: liability to be bound | s 899 | `s 899(3) the compromise or arrangement is binding on the person` |
| src:12269-12269 | the registrar (receipt) | the company: duty to deliver | s 899 | `s 899(4) the court's order cannot yet have effect` |
| src:12273-12275 | none (a rule fixing when the section applies) | none | s 899A | `s 899A(1) this section applies` |
| src:12276-12278 | none (a definition or a rule of reading) (by the kind of rule) | none | s 899A | `s 899A(2) the creditor is a relevant creditor` |
| src:12279-12279 | the relevant creditor: disability (it may not participate) | the meeting | s 899A | `s 899A(3) the relevant creditor may participate in the meeting summoned under section 896` |
| src:12280-12282 | the relevant creditor: claim to a statement | the company: duty to send it (s 899A(4)(a)) | s 899A | `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend` |
| src:12283-12283 | the creditor (a relevant creditor that has not agreed): immunity from provision in the arrangement | the court: disability to sanction | s 899A | `s 899A(5) the court may sanction the compromise or arrangement under section 899` |
| src:12284-12290 | none (a definition or a rule of reading) (by the kind of rule) | none | s 899A | `s 899A(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| src:12293-12295 | none (a rule fixing when the section applies) | none | s 900 | `s 900(1) this section applies` |
| src:12296-12302 | the court: power to make the provision | the companies, creditors and members concerned: liability to it | s 900 | `s 900(2) the court may make provision for the matter` |
| src:12303-12305 | the transferee company: right to the property and the burden of the liabilities | the transferor company: disability (the property passes without further act) | s 900 | `s 900(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| src:12306-12306 | the transferee company: right to the property free of the charge (by the kind of rule) | the holder of the charge: liability (the charge ceases to have effect) | s 900 | `s 900(4) the property vests freed from the charge` |
| src:12307-12309 | none (a definition or a rule of reading) (by the kind of rule) | none | s 900 | `s 900(5) the thing is property` |
| src:12310-12310 | the registrar (receipt) | every company in relation to which an order is made: duty to cause a copy to be delivered within seven days | s 900 | `s 900(6) the company delivered a copy of the order to the registrar in time` |
| src:12310-12310 | the registrar: claim to a copy of the order within seven days (by the kind of rule) | the company: duty to cause it to be delivered | s 900 | `s 900(6) the company's duty to deliver a copy of the order` |
| src:12311-12313 | the State | the company and every officer in default: liability to conviction | s 900 | `s 900(7) the person is guilty of an offence under section 900(7)` |
| src:12314-12314 | the State: power to prosecute and the court's power to sentence (by the kind of rule) | the person convicted: liability to the penalty | s 900 | `s 900(8) the penalty on conviction` |
| src:12317-12319 | none (a rule fixing when the section applies) | none | s 901 | `s 901(1) this section applies to the order` |
| src:12320-12323 | the registrar (receipt) | the company: duty to accompany the copy of the order with the amended articles, resolution or agreement | s 901 | `s 901(2) the copy of the order is accompanied as the section requires` |
| src:12324-12324 | anyone to whom the company issues a copy of its articles: claim to a copy of the order | the company: duty to accompany each copy of the articles | s 901 | `s 901(3) the copy of the articles is accompanied as the section requires` |
| src:12325-12327 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901 | `s 901(4) the thing is within the reference` |
| src:12328-12330 | the State | the company and every officer in default: liability to conviction (s 901(5)) | s 901 | `s 901(5) the person is guilty of an offence under section 901` |
| src:12331-12331 | the State: power to prosecute and the court's power to sentence (by the kind of rule) | the person convicted: liability to the penalty | s 901 | `s 901(6) the penalty on conviction` |
| src:12335-12335 | none (a rule fixing the scope of the Part) | none | s 901A | `s 901A(1) the provisions of Part 26A apply` |
| src:12336-12336 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901A | `s 901A(2) condition A is met` |
| src:12337-12341 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901A | `s 901A(3) condition B is met` |
| src:12342-12343 | none (a definition) | none | s 901A | `s 901A(4) the reorganisation of the share capital is an arrangement` |
| src:12344-12346 | none (a definition) | none | s 901A | `s 901A(4) the body is a company for the purposes of Part 26A` |
| src:12347-12347 | none (a rule of precedence between Parts) | none | s 901A | `s 901A(5) the provisions of Part 26A have effect subject to Part 27` |
| src:12349-12353 | the company or creditors the regulations name: immunity from Part 26A | whoever proposes the compromise or arrangement: disability | s 901B | `s 901B(1) Part 26A does not apply because of regulations under section 901B` |
| src:12354-12356 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901B | `s 901B(2) the person is an authorised person` |
| src:12360-12360 | the creditors or members concerned: liability to be summoned | the court: power | s 901C | `s 901C(1) the court may order a meeting of the creditors, class of creditors, members or class of members` |
| src:12361-12365 | the company, any creditor or member: power to apply | the court: liability to hear it | s 901C | `s 901C(2) the person may apply to the court` |
| src:12366-12366 | the creditor or member whose rights are affected: claim to participate | the company and the court: duty to permit it | s 901C | `s 901C(3) the person must be permitted to participate in the meeting` |
| src:12367-12367 | the class of creditors or members: immunity from the right in (3) if the court so finds | the creditors and members: disability to insist on participation | s 901C | `s 901C(4) subsection (3) does not apply in relation to the class` |
| src:12368-12368 | none (a condition, a computation or a rule of reading) | none | s 901C | `s 901C(5) the person is the one who is to make the application under subsection (4)` |
| src:12369-12369 | the corporation that is a creditor: power to appoint a representative (by the kind of rule) | the meeting: liability to receive that representative | s 901C | `s 901C(6) section 323 applies to the meeting` |
| src:12370-12370 | none (a signpost whose effect is s 901H) | none | s 901C | `s 901C(7) section 901C is subject to section 901H` |
| src:12372-12376 | the creditor or member: claim to the statement | the company: duty to send it (s 901D(1)(a)) | s 901D | `s 901D(1) the notice summoning the meeting satisfies the requirement` |
| src:12377-12381 | the company: duty to explain ; interests of directors: duty of disclosure | the creditors and members: claim to the explanation (s 901D(2)) ; the company (s 901D(2)(b)) | s 901D | `s 901D(2) the statement complies` |
| src:12382-12382 | the trustees for debenture holders: claim to the like explanation (by the kind of rule) | the company: duty to give it in the statement | s 901D | `s 901D(3) the statement complies as respects debenture holders` |
| src:12383-12383 | the creditor or member entitled to attend: claim to a free copy | the company: duty to provide it | s 901D | `s 901D(4) the person is entitled to be provided by the company with a copy of the statement free of charge` |
| src:12384-12391 | the State (a prosecuting power) | the company and every officer in default: liability to conviction | s 901D | `s 901D(5) the person is guilty of an offence under section 901D` |
| src:12391-12391 | the person who shows the refusal: immunity from conviction (by the kind of rule) | the State: disability to convict | s 901D | `s 901D(7) section 901D(7) gives the person a defence on these facts` |
| src:12392-12395 | the State | the person guilty: liability to the penalty | s 901D | `s 901D(8) the penalty on conviction` |
| src:12397-12400 | the company: claim to notice of a director's or trustee's matters | any director of the company and any trustee for its debenture holders: duty to give it | s 901E | `s 901E(1) the person is under a duty to give the company notice of the matter` |
| src:12401-12402 | the State | any person who makes default in complying with section 901E: liability to conviction (s 901E(2)) | s 901E | `s 901E(2) the person commits an offence` |
| src:12405-12405 | the company, any creditor or member: power to apply | the court: power to sanction | those bound: liability | s 901F | `s 901F(1) the court may sanction the compromise or arrangement` |
| src:12406-12408 | none (a signpost whose effect is ss 901G and 901H) | none | s 901F | `s 901F(2) section 901F(1) is subject to sections 901G and 901H` |
| src:12409-12413 | the company, any creditor or member: power to apply | the court: liability to hear it | s 901F | `s 901F(3) the person may apply to the court` |
| src:12414-12417 | the court: power over the administration or winding up | the administrator or liquidator: liability to its terms | s 901F | `s 901F(4) the court may by the order make the provision` |
| src:12418-12420 | the company, the creditors or class, the members or class, the liquidator and contributories: liability to be bound | none | s 901F | `s 901F(5) the compromise or arrangement is binding on the person` |
| src:12421-12423 | the registrar or the Gazette (receipt) | the company: duty to deliver or publish | s 901F | `s 901F(6) the court's order cannot yet have effect` |
| src:12425-12425 | none (a rule fixing when the section applies) | none | s 901G | `s 901G(1) this section applies` |
| src:12426-12426 | the dissenting class: immunity from being outvoted only if conditions A and B are not met | the court: power to sanction despite the dissent | s 901G | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` |
| src:12427-12427 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901G | `s 901G(3) condition A is met` |
| src:12428-12428 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901G | `s 901G(4) the relevant alternative` |
| src:12429-12429 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901G | `s 901G(5) condition B is met` |
| src:12436-12438 | none (a rule fixing when the section applies) | none | s 901H | `s 901H(1) this section applies` |
| src:12439-12441 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901H | `s 901H(2) the creditor is a relevant creditor` |
| src:12442-12442 | the relevant creditor: disability (it may not participate) | the meeting | s 901H | `s 901H(3) the relevant creditor may participate in the meeting summoned under section 901C` |
| src:12443-12445 | the relevant creditor: claim to a statement | the company: duty to send it (s 901H(4)(a)) | s 901H | `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend` |
| src:12446-12446 | the creditor (a relevant creditor that has not agreed): immunity from provision in the arrangement | the court: disability to sanction | s 901H | `s 901H(5) the court may sanction the compromise or arrangement under section 901F` |
| src:12447-12453 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901H | `s 901H(6) the debt is a moratorium debt or a priority pre-moratorium debt` |
| src:12455-12455 | the Pensions Regulator: claim to a copy of every notice or document sent to a creditor | the company: duty to send it | s 901I | `s 901I(1) the notice or other document has been sent to the Pensions Regulator as the section requires` |
| src:12456-12456 | the Board of the Pension Protection Fund: claim to a copy | the company: duty to send it | s 901I | `s 901I(2) the notice or other document has been sent to the Board of the Pension Protection Fund as the section requires` |
| src:12471-12472 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901I | `s 901I(9) the scheme is an eligible scheme` |
| src:12473-12477 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901I | `s 901I(9) the person is an employer` |
| src:12478-12478 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901I | `s 901I(9) the scheme is a money purchase scheme` |
| src:12479-12479 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901I | `s 901I(9) the scheme is an occupational pension scheme or a pension scheme` |
| src:12480-12480 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901I | `s 901I(9) the description is specified` |
| src:12483-12485 | none (a rule fixing when the section applies) | none | s 901J | `s 901J(1) this section applies` |
| src:12486-12492 | the court: power to make the provision | the companies, creditors and members concerned: liability to it | s 901J | `s 901J(2) the court may make provision for the matter` |
| src:12493-12495 | the transferee company: right to the property and the burden of the liabilities | the transferor company: disability (the property passes without further act) | s 901J | `s 901J(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` |
| src:12496-12496 | the transferee company: right to the property free of the charge (by the kind of rule) | the holder of the charge: liability (the charge ceases to have effect) | s 901J | `s 901J(4) the property vests freed from the charge` |
| src:12497-12499 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901J | `s 901J(5) the thing is property` |
| src:12500-12500 | the registrar (receipt) | every company in relation to which an order is made: duty to cause a copy to be delivered within seven days | s 901J | `s 901J(6) the company delivered a copy of the order to the registrar in time` |
| src:12500-12500 | the registrar: claim to a copy of the order within seven days (by the kind of rule) | the company: duty to cause it to be delivered | s 901J | `s 901J(6) the company's duty to deliver a copy of the order` |
| src:12501-12503 | the State | the company and every officer in default: liability to conviction | s 901J | `s 901J(7) the person is guilty of an offence under section 901J(7)` |
| src:12504-12504 | the State: power to prosecute and the court's power to sentence (by the kind of rule) | the person convicted: liability to the penalty | s 901J | `s 901J(8) the penalty on conviction` |
| src:12507-12509 | none (a rule fixing when the section applies) | none | s 901K | `s 901K(1) this section applies to the order` |
| src:12516-12516 | anyone to whom the company issues a copy of its articles: claim to a copy of the order | the company: duty to accompany each copy of the articles | s 901K | `s 901K(3) the copy of the articles is accompanied as the section requires` |
| src:12517-12519 | none (a definition or a rule of reading) (by the kind of rule) | none | s 901K | `s 901K(4) the thing is within the reference` |
| src:12520-12522 | the State | the company and every officer in default: liability to conviction (s 901K(5)) | s 901K | `s 901K(5) the person is guilty of an offence under section 901K` |
| src:12523-12523 | the State: power to prosecute and the court's power to sentence (by the kind of rule) | the person convicted: liability to the penalty | s 901K | `s 901K(6) the penalty on conviction` |
| src:12510-12515 | the registrar (receipt) | the company: duty to accompany the copy of the order with the amended articles, resolution or agreement | s 901K | `s 901K(2) the copy of the order is accompanied as the section requires` |
| src:12531-12539 | none (a rule fixing the scope of the Part) | none | s 902 | `s 902(1) this Part applies` |
| src:12540-12542 | none (a definition or a rule of reading) (by the kind of rule) | none | s 902 | `s 902(2)(a) the company is a new company` |
| src:12543-12543 | the members and creditors of the company being wound up: immunity from Part 27 | whoever proposes the scheme: disability | s 902 | `s 902(3) the winding up of the company takes the compromise or arrangement out of this Part` |
| src:12545-12545 | the members and creditors of the companies: claim that the court not sanction until the requirements are complied with | the court: disability to sanction | s 903 | `s 903(1) the requirements of this Part do not bar the court from sanctioning` |
| src:12546-12547 | none (a condition, a computation or a rule of reading) | none | s 903 | `s 903(2) the requirements applicable to a merger do not bar the court from sanctioning` |
| src:12548-12549 | none (a condition, a computation or a rule of reading) | none | s 903 | `s 903(3) the requirements applicable to a division do not bar the court from sanctioning` |
| src:12553-12555 | none (a definition) | none | s 904 | `s 904(1) the scheme involves a merger` |
| src:12553-12554 | none (a definition or a rule of reading) (by the kind of rule) | none | s 904 | `s 904(1)(a) the scheme involves a merger by absorption` |
| src:12555-12555 | none (a definition or a rule of reading) (by the kind of rule) | none | s 904 | `s 904(1)(b) the scheme involves a merger by formation of a new company` |
| src:12556-12558 | none (a definition or a rule of reading) (by the kind of rule) | none | s 904 | `s 904(2) the company is one of the merging companies` |
| src:12561-12561 | the members and creditors: claim to draft terms | the directors of the merging companies: duty to draw them up and adopt them | s 905 | `s 905(1) the draft terms have been drawn up and adopted` |
| src:12562-12575 | the members: claim to the particulars | the directors of the merging companies: duty to give them | s 905 | `s 905(2) the draft terms give the particulars required` |
| src:12576-12576 | none (a signpost whose effect is section 915) | none | s 905 | `s 905(3) the requirements in subsection (2)(b), (c) and (d) are subject to section 915` |
| src:12578-12578 | the registrar (receipt of the draft terms): none | the directors of each merging company: duty to deliver a copy | s 906 | `s 906(1) the directors have delivered a copy of the draft terms to the registrar` |
| src:12579-12579 | the members and creditors: claim to publication of notice of receipt | the registrar: duty to publish (an official: no seat) | s 906 | `s 906(2) the registrar has published notice of receipt of the draft terms in the Gazette` |
| src:12580-12580 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 906 | `s 906(3) the notice was published at least one month before the meeting` |
| src:12581-12581 | none (a signpost whose effect is section 906A) | none | s 906 | `s 906(4) the requirements in section 906 are subject to section 906A` |
| src:12584-12586 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 906A | `s 906A(2) the first condition is met` |
| src:12587-12587 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 906A | `s 906A(3) the second condition is met` |
| src:12588-12588 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 906A | `s 906A(4) the third condition is met` |
| src:12589-12589 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 906A | `s 906A(5) the fourth condition is met` |
| src:12590-12590 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 906A | `s 906A(6) the fifth condition is met` |
| src:12583-12583 | the company: immunity from section 906 | the registrar: disability to require delivery and publication | s 906A | `s 906A(1) section 906 does not apply in respect of the company` |
| src:12592-12592 | the members of each merging company: right to vote on the scheme | the directors and the company: duty to put it to them | s 907 | `s 907(1) the scheme has been approved by the members of the merging company` |
| src:12593-12593 | the members: immunity from being called to a meeting (by the kind of rule) | whoever proposes the scheme: no duty to put it to them | s 907 | `s 907(2) the meeting of members is not required` |
| src:12595-12595 | the members: claim to the report | the directors of each merging company: duty to draw it up and adopt it | s 908 | `s 908(1) the directors have drawn up and adopted a report` |
| src:12596-12600 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 908 | `s 908(2) the report consists of what the section requires` |
| src:12601-12603 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 908 | `s 908(2A) the required statement explaining the effect of the compromise or arrangement` |
| src:12604-12604 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 908 | `s 908(3) the requirement in section 908 is excluded` |
| src:12606-12607 | the members: claim to an expert's report | each merging company: duty to have one drawn up | s 909 | `s 909(1) an expert's report has been drawn up on behalf of the company` |
| src:12608-12609 | the merging companies (jointly): power to apply for a joint expert | the court: liability to hear it | s 909 | `s 909(3) the way the expert's report is drawn up complies` |
| src:12610-12612 | none (a rule fixing who may be the expert) | none | s 909 | `s 909(4) the person may be the expert` |
| src:12613-12618 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 909 | `s 909(5) the expert's report contains what the section requires` |
| src:12619-12622 | the expert: claim of access to documents and to information from the officers | the merging companies and their officers: duty to give them | s 909 | `s 909(6) the expert has the right of access to the document or to require the information` |
| src:12623-12623 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 909 | `s 909(7) the requirement in section 909 is excluded` |
| src:12625-12627 | none (a condition, a computation or a rule of reading) | none | s 910 | `s 910(1) this section applies` |
| src:12628-12628 | the members: claim to a supplementary accounting statement | the directors: duty to prepare it | s 910 | `s 910(1A) the directors have prepared a supplementary accounting statement` |
| src:12629-12631 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 910 | `s 910(2) the statement consists of what the section requires` |
| src:12632-12632 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 910 | `s 910(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` |
| src:12633-12633 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 910 | `s 910(4) the balance sheet has been approved and signed as section 414 provides` |
| src:12634-12634 | none (a definition or a rule of reading) (by the kind of rule) | none | s 910 | `s 910(5) the report is a half-yearly financial report` |
| src:12635-12635 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 910 | `s 910(6) the requirement in section 910 is excluded` |
| src:12640-12643 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 911 | `s 911(2) the members could inspect and obtain copies throughout the period` |
| src:12637-12639 | the members of each merging company: claim to inspect the documents and to have copies free of charge | each merging company: duty to allow it | s 911 | `s 911(1) the members could inspect the documents and obtain copies` |
| src:12644-12650 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911 | `s 911(3) the document is one the members must be able to inspect` |
| src:12651-12651 | none (a signpost whose effect is section 911A(1) | none | s 911 | `s 911(3A) the requirement in section 911(1)(a) is subject to section 911A(1)` |
| src:12652-12652 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911 | `s 911(4) the requirements of subsection (3)(b) and (c) are excluded` |
| src:12653-12653 | the member (who consented to electronic communication): immunity from the right to hard copy | the company: disability under section 1145 | s 911 | `s 911(5) section 1145 does not apply to the document` |
| src:12654-12654 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911 | `s 911(6) Part 4 of Schedule 5 does not apply` |
| src:12655-12655 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911 | `s 911(7) the requirements in section 911 are excluded` |
| src:12658-12660 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911A | `s 911A(2) the first condition is met` |
| src:12661-12661 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911A | `s 911A(3) the second condition is met` |
| src:12662-12662 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911A | `s 911A(4) the third condition is met` |
| src:12657-12657 | the member: claim to inspect at the registered office (unless the website conditions are met) | the company: duty to allow inspection or to meet the conditions | s 911A | `s 911A(1) section 911(1)(a) does not apply to the document` |
| src:12663-12667 | the person: claim to a copy he can retain and print | the company: duty to keep the document on the website so that he can | s 911A | `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| src:12668-12668 | none (a condition, a computation or a rule of reading) | none | s 911A | `s 911A(6) members can obtain copies only as mentioned in subsection (5)` |
| src:12670-12673 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 911B | `s 911B(1) the directors have reported material changes in property and liabilities` |
| src:12674-12676 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 911B | `s 911B(2) the directors of the other merging companies have reported those matters in turn` |
| src:12677-12677 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 911B | `s 911B(3) the requirement in section 911B is excluded` |
| src:12679-12680 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 912 | `s 912(1) the articles of the transferee company have been approved by ordinary resolution` |
| src:12682-12685 | the holder of the securities: claim to rights of equivalent value in the transferee company | the scheme (and the transferee company): duty to provide them | s 913 | `s 913(1) the scheme protects the holder of securities to which special rights are attached` |
| src:12687-12689 | the members of the transferor companies: immunity from dilution by allotments to a company holding its own shares | the scheme: disability to provide for them | s 914 | `s 914 the scheme does not provide for the allotment of shares the section forbids` |
| src:12700-12700 | none (a definition or a rule of reading) (by the kind of rule) | none | s 915 | `s 915(6) the securities are relevant securities` |
| src:12692-12692 | none (a rule fixing when the section applies) | none | s 915 | `s 915(1) this section applies` |
| src:12693-12693 | the directors of the merging companies: immunity from the duty to give the particulars | the members: no-right to them | s 915 | `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)` |
| src:12694-12694 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 915 | `s 915(3) section 897 does not apply` |
| src:12695-12695 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 915 | `s 915(3A) section 901D does not apply` |
| src:12696-12698 | the directors of the merging companies: immunity from the duties to report and to obtain an expert's report | the members: no-right to the reports | s 915 | `s 915(4) the requirements of sections 908 and 909 do not apply` |
| src:12699-12699 | the merging companies: immunity from the duty to make those documents available for inspection | the members: no-right to inspect them | s 915 | `s 915(5) the requirements of section 911 so far as relating to a document required to be drawn up under sections 908 and 909 do not apply` |
| src:12702-12702 | none (a rule fixing when the section applies) | none | s 915A | `s 915A(1) this section applies` |
| src:12703-12708 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 915A | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| src:12709-12709 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 915A | `s 915A(3) the first condition is met` |
| src:12710-12710 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 915A | `s 915A(4) the second condition is met` |
| src:12711-12711 | the transferee company and the holders: liability to the court's determination of the consideration | the court: power | s 915A | `s 915A(5) the court may determine, or make provision for the determination of, the consideration` |
| src:12712-12714 | none (a definition or a rule of reading) (by the kind of rule) | none | s 915A | `s 915A(6) the person is an other holder` |
| src:12716-12716 | none (a rule fixing when the section applies) | none | s 916 | `s 916(1) this section applies` |
| src:12719-12719 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(3A) subsection (3A) is satisfied` |
| src:12720-12723 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(3B) subsection (3B) is satisfied` |
| src:12718-12718 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(3) the first condition is met` |
| src:12725-12725 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(4A) subsection (4A) is satisfied for the document` |
| src:12726-12729 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(4B) subsection (4B) is satisfied for the document` |
| src:12724-12724 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(4) the second condition is met` |
| src:12730-12730 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(4C) the third condition is met` |
| src:12731-12733 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| src:12734-12736 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 916 | `s 916(5) the fourth condition is met` |
| src:12737-12737 | none (a definition or a rule of reading) (by the kind of rule) | none | s 916 | `s 916(6) the securities are relevant securities` |
| src:12717-12717 | the members of the transferee company: immunity from being called to a meeting | the court: power to excuse the meeting on being satisfied | s 916 | `s 916(2) the meeting of members of the transferee company is not required` |
| src:12742-12742 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(3A) subsection (3A) is satisfied` |
| src:12743-12746 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(3B) subsection (3B) is satisfied` |
| src:12741-12741 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(3) the first condition is met` |
| src:12748-12748 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(4A) subsection (4A) is satisfied for the document` |
| src:12749-12752 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(4B) subsection (4B) is satisfied for the document` |
| src:12747-12747 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(4) the second condition is met` |
| src:12753-12753 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(4C) the third condition is met` |
| src:12754-12756 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| src:12757-12759 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 917 | `s 917(5) the fourth condition is met` |
| src:12760-12760 | none (a definition or a rule of reading) (by the kind of rule) | none | s 917 | `s 917(6) the securities are relevant securities` |
| src:12740-12740 | the members of the transferee company: immunity from being called to a meeting | the court: power to excuse the meeting on being satisfied | s 917 | `s 917(2) the meeting of members of any of the merging companies is not required` |
| src:12739-12739 | none (a rule fixing when the section applies) | none | s 917 | `s 917(1) this section applies` |
| src:12763-12763 | the members of the transferor company: immunity from being called to a meeting | whoever proposes the scheme: no duty to put it to them | s 917A | `s 917A(1) the meeting of members of the transferor company is not required` |
| src:12767-12767 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(2A) subsection (2A) is satisfied` |
| src:12768-12771 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(2B) subsection (2B) is satisfied` |
| src:12766-12766 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(2) the first condition is met` |
| src:12773-12773 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(3A) subsection (3A) is satisfied for the document` |
| src:12774-12777 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(3B) subsection (3B) is satisfied for the document` |
| src:12772-12772 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(3) the second condition is met` |
| src:12778-12778 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(3C) the third condition is met` |
| src:12779-12781 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(3D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` |
| src:12782-12784 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 918 | `s 918(4) the fourth condition is met` |
| src:12765-12765 | the members of the transferee company: immunity from being called to a meeting | the court: power to excuse the meeting on being satisfied | s 918 | `s 918(1) the meeting of members of the transferee company is not required` |
| src:12786-12786 | the merging companies and their directors: immunity from the listed requirements | the members and holders of voting securities: power to dispense by agreement (all of them) | s 918A | `s 918A(1) the requirements are dispensed with by agreement` |
| src:12787-12793 | none (a definition or a rule of reading) (by the kind of rule) | none | s 918A | `s 918A(1A) the requirement is one that may be dispensed with under section 918A` |
| src:12798-12800 | none (a definition or a rule of reading) (by the kind of rule) | none | s 918A | `s 918A(3) the date of the relevant application` |
| src:12794-12797 | none (a definition or a rule of reading) (by the kind of rule) | none | s 918A | `s 918A(2) the holding counts for the purposes of section 918A` |
| src:12804-12806 | none (a definition) | none | s 919 | `s 919(1) the scheme involves a division` |
| src:12807-12807 | none (a definition or a rule of reading) (by the kind of rule) | none | s 919 | `s 919(2) the company is one of the companies involved in the division` |
| src:12810-12810 | the members and creditors: claim to draft terms | the directors of each company involved in the division: duty to draw them up and adopt them | s 920 | `s 920(1) the draft terms have been drawn up and adopted` |
| src:12811-12824 | the members: claim to the particulars | the directors of the companies involved in the division: duty to give them | s 920 | `s 920(2) the draft terms give the particulars required` |
| src:12825-12828 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 920 | `s 920(3) the draft terms also do what the section requires` |
| src:12830-12830 | the registrar (receipt of the draft terms): none | the directors of each company involved in the division: duty to deliver a copy | s 921 | `s 921(1) the directors have delivered a copy of the draft terms to the registrar` |
| src:12831-12831 | the members and creditors: claim to publication of notice of receipt | the registrar: duty to publish (an official: no seat) | s 921 | `s 921(2) the registrar has published notice of receipt of the draft terms in the Gazette` |
| src:12832-12832 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 921 | `s 921(3) the notice was published at least one month before the meeting` |
| src:12833-12833 | none (a signpost whose effect is ss 921A and 934) | none | s 921 | `s 921(4) the requirements in section 921 are excluded` |
| src:12836-12838 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 921A | `s 921A(2) the first condition is met` |
| src:12839-12839 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 921A | `s 921A(3) the second condition is met` |
| src:12840-12840 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 921A | `s 921A(4) the third condition is met` |
| src:12841-12841 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 921A | `s 921A(5) the fourth condition is met` |
| src:12842-12842 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 921A | `s 921A(6) the fifth condition is met` |
| src:12835-12835 | the company: immunity from section 921 | the registrar: disability to require delivery and publication | s 921A | `s 921A(1) section 921 does not apply in respect of the company` |
| src:12844-12844 | the members of each merging company: right to vote on the scheme | the directors and the company: duty to put it to them | s 922 | `s 922(1) the scheme has been approved by the members of a company involved in the division` |
| src:12845-12845 | the members: immunity from being called to a meeting (by the kind of rule) | whoever proposes the scheme: no duty to put it to them | s 922 | `s 922(2) the meeting of members is not required` |
| src:12847-12847 | the members: claim to the report | the directors of each merging company: duty to draw it up and adopt it | s 923 | `s 923(1) the directors have drawn up and adopted a report` |
| src:12848-12852 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 923 | `s 923(2) the report consists of what the section requires` |
| src:12853-12855 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 923 | `s 923(2A) the required statement explaining the effect of the compromise or arrangement` |
| src:12856-12858 | the members: claim to a statement whether a section 593 valuation report was made and delivered | the directors: duty to state it | s 923 | `s 923(3) the report states what the section requires` |
| src:12859-12859 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 923 | `s 923(4) the requirement in section 923 is excluded` |
| src:12861-12862 | the members: claim to an expert's report | each company involved in the division: duty to have one drawn up | s 924 | `s 924(1) an expert's report has been drawn up on behalf of the company` |
| src:12863-12864 | the companies involved in the division (jointly): power to apply for a joint expert | the court: liability to hear it | s 924 | `s 924(3) the way the expert's report is drawn up complies` |
| src:12865-12867 | none (a rule fixing who may be the expert) | none | s 924 | `s 924(4) the person may be the expert` |
| src:12868-12873 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 924 | `s 924(5) the expert's report contains what the section requires` |
| src:12874-12877 | the expert: claim of access to documents and to information from the officers | the companies involved in the division and their officers: duty to give them | s 924 | `s 924(6) the expert has the right of access to the document or to require the information` |
| src:12878-12878 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 924 | `s 924(7) the requirement in section 924 is excluded` |
| src:12880-12882 | none (a condition, a computation or a rule of reading) | none | s 925 | `s 925(1) this section applies` |
| src:12883-12883 | the members: claim to a supplementary accounting statement | the directors: duty to prepare it | s 925 | `s 925(1A) the directors have prepared a supplementary accounting statement` |
| src:12884-12886 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 925 | `s 925(2) the statement consists of what the section requires` |
| src:12887-12887 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 925 | `s 925(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` |
| src:12888-12888 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 925 | `s 925(4) the balance sheet has been approved and signed as section 414 provides` |
| src:12889-12889 | none (a definition or a rule of reading) (by the kind of rule) | none | s 925 | `s 925(4A) the report is a half-yearly financial report` |
| src:12890-12890 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 925 | `s 925(5) the requirement in section 925 is excluded` |
| src:12895-12898 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 926 | `s 926(2) the members could inspect and obtain copies throughout the period` |
| src:12892-12894 | the members of each company involved in the division: claim to inspect the documents and to have copies free of charge | each company involved in the division: duty to allow it | s 926 | `s 926(1) the members could inspect the documents and obtain copies` |
| src:12906-12906 | none (a signpost whose effect is section 926A(1) | none | s 926 | `s 926(3A) the requirement in section 926(1)(a) is subject to section 926A(1)` |
| src:12908-12908 | the member (who consented to electronic communication): immunity from the right to hard copy | the company: disability under section 1145 | s 926 | `s 926(5) section 1145 does not apply to the document` |
| src:12909-12909 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926 | `s 926(6) Part 4 of Schedule 5 does not apply` |
| src:12899-12905 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926 | `s 926(3) the document is one the members must be able to inspect` |
| src:12907-12907 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926 | `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded` |
| src:12912-12914 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926A | `s 926A(2) the first condition is met` |
| src:12915-12915 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926A | `s 926A(3) the second condition is met` |
| src:12916-12916 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 926A | `s 926A(4) the third condition is met` |
| src:12911-12911 | the member: claim to inspect at the registered office (unless the website conditions are met) | the company: duty to allow inspection or to meet the conditions | s 926A | `s 926A(1) section 926(1)(a) does not apply to the document` |
| src:12917-12921 | the person: claim to a copy he can retain and print | the company: duty to keep the document on the website so that he can | s 926A | `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| src:12922-12922 | none (a condition, a computation or a rule of reading) | none | s 926A | `s 926A(6) members can obtain copies only as mentioned in subsection (5)` |
| src:12924-12927 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 927 | `s 927(1) the directors have reported material changes in property and liabilities` |
| src:12928-12930 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 927 | `s 927(2) the directors of each existing transferee company have reported those matters in turn` |
| src:12931-12931 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 927 | `s 927(3) the requirement in section 927 is excluded` |
| src:12933-12934 | the transferor company's members: right to approve the articles of each new transferee company by ordinary resolution | the directors: duty to put them to the members | s 928 | `s 928(1) the articles of every new transferee company have been approved by ordinary resolution of the transferor company` |
| src:12936-12939 | the holder of the securities: claim to rights of equivalent value in a transferee company | the scheme (and a transferee company): duty to provide them | s 929 | `s 929(1) the scheme protects the holder of securities to which special rights are attached` |
| src:12941-12943 | the members of the transferor companies: immunity from dilution by allotments to a company holding its own shares | the scheme: disability to provide for them | s 930 | `s 930 the scheme does not provide for the allotment of shares the section forbids` |
| src:12946-12946 | none (a rule fixing when the section applies) | none | s 931 | `s 931(1) this section applies` |
| src:12949-12949 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(3A) subsection (3A) is satisfied` |
| src:12950-12953 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(3B) subsection (3B) is satisfied` |
| src:12948-12948 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(3) the first condition is met` |
| src:12955-12955 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(4A) subsection (4A) is satisfied for the document` |
| src:12956-12959 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(4B) subsection (4B) is satisfied for the document` |
| src:12954-12954 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(4) the second condition is met` |
| src:12960-12960 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(4C) the third condition is met` |
| src:12961-12963 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 931 | `s 931(4D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| src:12947-12947 | the members of every company involved in the division: immunity from being called to a meeting | the court: power to excuse the meeting on being satisfied | s 931 | `s 931(2) the meeting of members of the transferor company is not required` |
| src:12965-12968 | the members and the directors of the existing transferee companies: claim to a report of material change | the directors of the transferor company: duty to send it | s 931 | `s 931(6) the fourth condition is met` |
| src:12971-12971 | the members of the transferor company: immunity from being called to a meeting | whoever proposes the scheme: no duty to put it to them | s 931A | `s 931A(1) the meeting of members of the transferor company is not required` |
| src:12975-12975 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(2A) subsection (2A) is satisfied` |
| src:12976-12979 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(2B) subsection (2B) is satisfied` |
| src:12974-12974 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(2) the first condition is met` |
| src:12981-12981 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(3A) subsection (3A) is satisfied for the document` |
| src:12982-12985 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(3B) subsection (3B) is satisfied for the document` |
| src:12980-12980 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(3) the second condition is met` |
| src:12986-12986 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(3C) the third condition is met` |
| src:12987-12989 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(3D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` |
| src:12990-12992 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 932 | `s 932(4) the fourth condition is met` |
| src:12973-12973 | the members of the transferee company: immunity from being called to a meeting | the court: power to excuse the meeting on being satisfied | s 932 | `s 932(1) the meeting of members of the transferee company is not required` |
| src:12993-12993 | none (a condition, a computation or a rule of reading) | none | s 932 | `s 932(5) the first, second and third conditions are subject to section 934` |
| src:12995-12995 | the companies involved in the division and their directors: immunity from the listed requirements | the members and holders of voting securities: power to dispense by agreement (all of them) | s 933 | `s 933(1) the requirements are dispensed with by agreement` |
| src:12996-13002 | none (a definition or a rule of reading) (by the kind of rule) | none | s 933 | `s 933(2) the requirement is one that may be dispensed with under section 933` |
| src:13007-13009 | none (a definition or a rule of reading) (by the kind of rule) | none | s 933 | `s 933(4) the date of the relevant application` |
| src:13003-13006 | none (a definition or a rule of reading) (by the kind of rule) | none | s 933 | `s 933(3) the holding counts for the purposes of section 933` |
| src:13011-13011 | none (a rule fixing when the section applies) | none | s 933A | `s 933A(1) this section applies` |
| src:13012-13012 | the transferee companies' directors and the transferor company: immunity from the listed requirements | the members: no-right to the reports where they receive proportional shares | s 933A | `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` |
| src:13013-13019 | none (a definition or a rule of reading) (by the kind of rule) | none | s 933A | `s 933A(3) the requirement is one that does not apply under section 933A` |
| src:13028-13030 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 934 | `s 934(2) the first condition is met` |
| src:13031-13033 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 934 | `s 934(3) the second condition is met` |
| src:13034-13034 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 934 | `s 934(4) the third condition is met` |
| src:13021-13027 | the company: power to ask for the direction | the court: power to direct | s 934 | `s 934(1) the court may by order direct that the requirements do not apply` |
| src:13021-13027 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 934 | `s 934(1)(a) the court has directed that sections 921 and 926 do not apply` |
| src:13021-13027 | the company and its directors (or the court's order): immunity from the requirement, where the exclusion holds (by the kind of rule) | the members and creditors: no-right to the requirement | s 934 | `s 934(1)(b) section 932 has effect without its first, second and third conditions` |
| src:13038-13043 | the expert: power to arrange for or accept another person's valuation | the other person and the merging companies: liability | s 935 | `s 935(1) the expert may arrange for or accept the valuation` |
| src:13044-13046 | the members: claim to an expert's report that names the valuer and describes the valuation | the expert: duty to state it | s 935 | `s 935(2) the expert's report states what the section requires` |
| src:13048-13058 | the members and creditors: claim to an independent expert | the expert and valuer: disability to act unless independent | s 936 | `s 936(1) the person meets the independence requirement` |
| src:13059-13059 | the auditor of a company: immunity from being treated as an officer or employee for this purpose | the merging companies: no-right to treat the auditor as disqualified | s 936 | `s 936(2) the person is regarded as an officer or employee of the company for the purposes of section 936` |
| src:13061-13061 | none (a definition or a rule of reading) (by the kind of rule) | none | s 936 | `s 936(3)(a) the company is a company concerned in the scheme` |
| src:13062-13064 | none (a definition or a rule of reading) (by the kind of rule) | none | s 936 | `s 936(3)(b) the undertaking is an associated undertaking of the company` |
| src:13065-13065 | none (a definition or a rule of reading) (by the kind of rule) | none | s 936 | `s 936(3)(c) the person is an associate` |
| src:13068-13068 | none (a signpost: the section defines a term for section 936) | none | s 937 | `s 937(1) the definition applies` |
| src:13069-13082 | none (a definition) | none | s 937 | `s 937 the person is an associate` |
| src:13085-13088 | the members or creditors of the existing transferee company: liability to be summoned | the court: power | s 938 | `s 938(1) the court may order a meeting of the members or creditors of the company` |
| src:13089-13093 | the company, a member or creditor: power to apply | the court: liability to hear it | s 938 | `s 938(2) the person may apply to the court` |
| src:13094-13094 | the corporation that is a creditor: power to appoint a representative (by the kind of rule) | the meeting: liability to receive that representative | s 938 | `s 938(3) section 323 applies to the meeting` |
| src:13096-13099 | the members and creditors, the transferor and the transferee companies: claim that the court fix the date | the court: duty to fix it | s 939 | `s 939(1) the court has fixed a date for the transfer` |
| src:13100-13100 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 939 | `s 939(2) the order fixes the same date for the dissolution` |
| src:13101-13101 | the transferor company: duty to take the steps by the date | the court: duty to fix the date | s 939 | `s 939(3) the court has fixed a date for the steps within six months` |
| src:13102-13102 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 939 | `s 939(4) the court may postpone the dissolution of the transferor company until that date` |
| src:13103-13103 | the members and creditors: claim to the document, report or notice (by the kind of rule) | the directors, the company or the registrar: duty to provide or publish it | s 939 | `s 939(5) the court may postpone or further postpone the date` |
| src:13108-13109 | the creditors who so agree: no claim against the other transferee companies | the creditors: disability | s 940 | `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` |
| src:13110-13111 | the creditor: claim limited by the net value (by the kind of rule) | the transferee company: liability limited to the net value | s 940 | `s 940(3) the net value transferred` |
| src:13106-13107 | the creditor: claim against each transferee company, jointly and severally | each transferee company: liability for the others' defaults | s 940 | `s 940(1) the amount for which the transferee company is liable` |
| src:13117-13126 | none (a definition or a rule of reading) (by the kind of rule) | none | s 940A | `s 940A(2) the provision is one of those to which section 940A(1) applies` |
| src:13114-13116 | the company: immunity from the consequences of the website failure (by the kind of rule) | the members: no-right to the availability throughout the period | s 940A | `s 940A(1) the failure is to be disregarded` |
| src:13129-13130 | none (a definition or a rule of reading) (by the kind of rule) | none | s 941 | `s 941 the thing is a liability` |
| src:13131-13131 | none (a definition or a rule of reading) (by the kind of rule) | none | s 941 | `s 941 the thing is property` |
| headings, the repealed s 899(5) and s 931(5), and the machinery subsections listed as inert in the coverage table | none | none | | (inert) |

## Marginal readings for a lawyer (coa20)

Every branch below rests on one of the two readings the brief marks "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and a flat negative counts as the text saying no; (b) a prohibition or grant limited by its own wording does not (the case outside the limit answers `NOTHING`). Listed per function: the number of branches on each reading and the first such branch's quoted words. The other reading is `NOTHING` for (a) and `JUST FALSE` for (b). Reading (a) is counted for every `FALSE-kind` branch except those that rest on a plain "means" definition, an "only" list or condition, or a bare "must" (fork F3): a failed "if", "where", "satisfied if", "until" or period, and a flat negative ("does not apply", "may not", "is not guilty"), are all counted. The count is therefore generous: the rulings of 2026-11-05 already settle the "where" and period cases, which are listed because the brief marks them "for a lawyer".

| function | (a) unmet "if", "where" or flat negative | (b) limited by its own wording | first quoted words |
| --- | --- | --- | --- |
| `s 895(1) the provisions of Part 26 apply` | 1 | 0 | The provisions of this Part apply where a compromise or arrangement is proposed between a company and |
| `s 895(3) the provisions of Part 26 have effect subject to Part 27` | 1 | 0 | subject to Part 27 (mergers and divisions of public companies) where that Part applies |
| `s 896(1) the court may order a meeting of the creditors, class of creditors, members or class of members` | 0 | 1 | on an application under this section |
| `s 896(2) the person may apply for an order for a meeting` | 0 | 2 | if the company is being wound up, the liquidator |
| `s 896(3) section 323 applies to the meeting` | 0 | 1 | applies to a meeting of creditors under this section |
| `s 897(1) the notice summoning the meeting satisfies the requirement` | 2 | 0 | Where a meeting is summoned under section 896 |
| `s 897(2) the statement complies` | 1 | 0 | The statement must— (a) explain the effect of the compromise or arrangement, and (b) in particular, state |
| `s 897(3) the statement complies as respects debenture holders` | 1 | 1 | Where the compromise or arrangement affects the rights of debenture holders |
| `s 897(4) the person is entitled to be provided by the company with a copy of the statement free of charge` | 0 | 1 | Where a notice given by advertisement states ... every such creditor or member is entitled, on making applicat |
| `s 897(5) the person is guilty of an offence under section 897` | 2 | 0 | If a company makes default in complying with any requirement of this section, an offence is committed by |
| `s 897(7) section 897(7) gives the person a defence on these facts` | 1 | 0 | if he shows that the default was due to the refusal |
| `s 898(1) the person is under a duty to give the company notice of the matter` | 0 | 1 | any director of the company, and any trustee for its debenture holders, to give notice to the company of such  |
| `s 898(2) the person commits an offence` | 1 | 0 | Any person who makes default in complying with this section commits an offence |
| `s 899(1) the court may sanction the compromise or arrangement` | 0 | 2 | the court may, on an application under this section, sanction |
| `s 899(2) the person may apply for the court's sanction` | 0 | 2 | if the company is being wound up, the liquidator |
| `s 899(3) the compromise or arrangement is binding on the person` | 0 | 1 | A compromise or arrangement sanctioned by the court is binding on |
| `s 899(4) the court's order cannot yet have effect` | 1 | 0 | has no effect until a copy of it has been delivered to the registrar |
| `s 899A(1) this section applies` | 1 | 0 | This section applies where |
| `s 899A(3) the relevant creditor may participate in the meeting summoned under section 896` | 1 | 1 | where |
| `s 899A(4) the relevant creditor is within section 897 as a creditor entitled to be sent the statement and to attend` | 0 | 1 | For the purposes of section 897 |
| `s 899A(5) the court may sanction the compromise or arrangement under section 899` | 1 | 2 | where |
| `s 900(1) this section applies` | 1 | 0 | This section applies where application is made to the court under section 899 to sanction a compromise or arra |
| `s 900(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` | 1 | 0 | If an order under this section provides for the transfer of property or liabilities |
| `s 900(4) the property vests freed from the charge` | 1 | 0 | The property (if the order so directs) vests freed from any charge that is by virtue of the compromise or arra |
| `s 900(6) the company delivered a copy of the order to the registrar in time` | 2 | 0 | within seven days after its making |
| `s 900(7) the person is guilty of an offence under section 900(7)` | 1 | 0 | If default is made in complying with subsection (6) an offence is committed by |
| `s 901(1) this section applies to the order` | 0 | 1 | This section applies— (a) to any order under section 899 ..., and (b) to any order under section 900 ... that  |
| `s 901(2) the copy of the order is accompanied as the section requires` | 0 | 2 | If the order amends |
| `s 901(3) the copy of the articles is accompanied as the section requires` | 0 | 2 | Every copy of the company's articles issued by the company after the order is made |
| `s 901(4) the thing is within the reference` | 1 | 0 | references to the effect of the order include the effect of the compromise or arrangement |
| `s 901(5) the person is guilty of an offence under section 901` | 1 | 0 | If a company makes default in complying with this section an offence is committed by |
| `s 901A(1) the provisions of Part 26A apply` | 1 | 0 | The provisions of this Part apply where conditions A and B are met in relation to a company |
| `s 901A(2) condition A is met` | 1 | 0 | Condition A is that the company has encountered, or is likely to encounter, financial difficulties that are af |
| `s 901A(3) condition B is met` | 1 | 0 | Condition B is that— (a) a compromise or arrangement is proposed between the company and ..., and (b) the purp |
| `s 901A(5) the provisions of Part 26A have effect subject to Part 27` | 1 | 0 | subject to Part 27 (mergers and divisions of public companies) where that Part applies |
| `s 901C(1) the court may order a meeting of the creditors, class of creditors, members or class of members` | 0 | 1 | on an application under this subsection |
| `s 901C(2) the person may apply to the court` | 0 | 2 | if the company is being wound up, the liquidator |
| `s 901C(3) the person must be permitted to participate in the meeting` | 0 | 1 | Every creditor or member of the company whose rights are affected by the compromise or arrangement must be per |
| `s 901C(4) subsection (3) does not apply in relation to the class` | 1 | 0 | subsection (3) does not apply in relation to a class of creditors or members of the company if, on an applicat |
| `s 901C(5) the person is the one who is to make the application under subsection (4)` | 1 | 0 | An application under subsection (4) is to be made by the person who made the application under subsection (1) |
| `s 901C(6) section 323 applies to the meeting` | 0 | 1 | applies to a meeting of creditors under this section |
| `s 901D(1) the notice summoning the meeting satisfies the requirement` | 2 | 0 | Where a meeting is summoned under section 901C |
| `s 901D(2) the statement complies` | 1 | 0 | The statement must— (a) explain the effect of the compromise or arrangement, and (b) in particular, state |
| `s 901D(3) the statement complies as respects debenture holders` | 1 | 1 | Where the compromise or arrangement affects the rights of debenture holders |
| `s 901D(4) the person is entitled to be provided by the company with a copy of the statement free of charge` | 0 | 1 | Where a notice given by advertisement states ... every such creditor or member is entitled, on making applicat |
| `s 901D(5) the person is guilty of an offence under section 901D` | 2 | 0 | If a company makes default in complying with any requirement of this section, an offence is committed by |
| `s 901D(7) section 901D(7) gives the person a defence on these facts` | 1 | 0 | if the person shows that the default was due to the refusal |
| `s 901E(1) the person is under a duty to give the company notice of the matter` | 0 | 1 | any director of the company, and any trustee for its debenture holders, to give notice to the company of such  |
| `s 901E(2) the person commits an offence` | 1 | 0 | Any person who makes default in complying with this section commits an offence |
| `s 901F(1) the court may sanction the compromise or arrangement` | 0 | 2 | the court may, on an application under this section, sanction |
| `s 901F(3) the person may apply to the court` | 0 | 2 | if the company is being wound up, the liquidator |
| `s 901F(4) the court may by the order make the provision` | 0 | 1 | Where the court makes an order under this section in relation to a company that is in administration or is bei |
| `s 901F(5) the compromise or arrangement is binding on the person` | 0 | 1 | A compromise or arrangement sanctioned by the court is binding |
| `s 901F(6) the court's order cannot yet have effect` | 2 | 0 | has no effect until a copy of it has been— (a) in the case of an overseas company ..., published in the Gazett |
| `s 901G(1) this section applies` | 1 | 0 | This section applies if the compromise or arrangement is not agreed by a number representing at least 75% in v |
| `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` | 1 | 1 | This section applies if the compromise or arrangement is not agreed by |
| `s 901G(3) condition A is met` | 1 | 0 | Condition A is that the court is satisfied that, if the compromise or arrangement were to be sanctioned under  |
| `s 901G(5) condition B is met` | 1 | 0 | Condition B is that the compromise or arrangement has been agreed by a number representing 75% in value of a c |
| `s 901H(1) this section applies` | 1 | 0 | This section applies where |
| `s 901H(3) the relevant creditor may participate in the meeting summoned under section 901C` | 1 | 1 | where |
| `s 901H(4) the relevant creditor is within section 901D as a creditor entitled to be sent the statement and to attend` | 0 | 1 | For the purposes of section 901D |
| `s 901H(5) the court may sanction the compromise or arrangement under section 901F` | 1 | 2 | where |
| `s 901I(1) the notice or other document has been sent to the Pensions Regulator as the section requires` | 1 | 0 | In a case where the company ... is or has been an employer in respect of an occupational pension scheme that i |
| `s 901I(2) the notice or other document has been sent to the Board of the Pension Protection Fund as the section requires` | 1 | 0 | In a case where the company ... is an employer in respect of an eligible scheme, any notice or other document  |
| `s 901J(1) this section applies` | 1 | 0 | This section applies where application is made to the court under section 901F to sanction a compromise or arr |
| `s 901J(3) the property vests in, and the liabilities become liabilities of, the transferee company by virtue of the order` | 1 | 0 | If an order under this section provides for the transfer of property or liabilities |
| `s 901J(4) the property vests freed from the charge` | 1 | 0 | The property (if the order so directs) vests freed from any charge that is by virtue of the compromise or arra |
| `s 901J(6) the company delivered a copy of the order to the registrar in time` | 2 | 0 | within seven days after its making |
| `s 901J(7) the person is guilty of an offence under section 901J(7)` | 1 | 0 | If default is made in complying with subsection (6) an offence is committed by |
| `s 901K(1) this section applies to the order` | 0 | 1 | This section applies— (a) to any order under section 901F ..., and (b) to any order under section 901J ... tha |
| `s 901K(3) the copy of the articles is accompanied as the section requires` | 0 | 2 | Every copy of the company's articles issued by the company after the order is made |
| `s 901K(4) the thing is within the reference` | 1 | 0 | references to the effect of the order include the effect of the compromise or arrangement |
| `s 901K(5) the person is guilty of an offence under section 901K` | 1 | 0 | If a company makes default in complying with this section an offence is committed by |
| `s 901K(2) the copy of the order is accompanied as the section requires` | 0 | 2 | If— (a) the order amends ... and (b) a copy of the order is required to be delivered to the registrar by the c |
| `s 902(1) this Part applies` | 1 | 0 | This Part applies where— (a) a compromise or arrangement is proposed between a public company and ..., (b) ... |
| `s 902(3) the winding up of the company takes the compromise or arrangement out of this Part` | 0 | 1 | This Part does not apply where the company ... is being wound up |
| `s 903(1) the requirements of this Part do not bar the court from sanctioning` | 1 | 0 | The court must not sanction the compromise or arrangement under Part 26 ... or Part 26A ... unless the relevan |
| `s 904(1)(a) the scheme involves a merger by absorption` | 1 | 0 | The scheme involves a merger where under the scheme— (a) the undertaking, property and liabilities of one or m |
| `s 904(1)(b) the scheme involves a merger by formation of a new company` | 1 | 0 | (b) the undertaking, property and liabilities of two or more public companies ... are to be transferred to a n |
| `s 904(2) the company is one of the merging companies` | 2 | 0 | References in this Part to “the merging companies” are— (a) in relation to a merger by absorption, to the tran |
| `s 906(2) the registrar has published notice of receipt of the draft terms in the Gazette` | 0 | 1 | notice of receipt by him from that company of a copy of the draft terms |
| `s 906(3) the notice was published at least one month before the meeting` | 1 | 1 | before the date of any meeting of that company summoned for the purpose of approving the scheme |
| `s 906A(2) the first condition is met` | 1 | 0 | The first condition is that the draft terms are made available on a website which— (a) is maintained by or on  |
| `s 906A(3) the second condition is met` | 1 | 0 | The second condition is that neither access to the draft terms on the website nor the supply of a hard copy of |
| `s 906A(4) the third condition is met` | 1 | 0 | The third condition is that the directors of the company deliver to the registrar a notice giving details of t |
| `s 906A(5) the fourth condition is met` | 1 | 0 | The fourth condition is that the registrar publishes the notice in the Gazette at least one month before the d |
| `s 906A(6) the fifth condition is met` | 1 | 0 | The fifth condition is that the draft terms remain available on the website throughout the period beginning on |
| `s 906A(1) section 906 does not apply in respect of the company` | 1 | 0 | Section 906 does not apply in respect of a company if the conditions in subsections (2) to (6) are met |
| `s 908(2A) the required statement explaining the effect of the compromise or arrangement` | 0 | 1 | in a case where a meeting is summoned under section 896 ...; in a case where a meeting is summoned under secti |
| `s 909(3) the way the expert's report is drawn up complies` | 1 | 0 | If no such appointment is made, there must be a separate expert's report to the members of each merging compan |
| `s 909(4) the person may be the expert` | 1 | 0 | The expert must be a person who— (a) is eligible for appointment as a statutory auditor ..., and (b) meets the |
| `s 909(6) the expert has the right of access to the document or to require the information` | 0 | 1 | The expert (or each of them) has ... all such documents ... as he thinks necessary for the purposes of making  |
| `s 910(1) this section applies` | 2 | 0 | This section applies if the last annual accounts of any of the merging companies relate to a financial year en |
| `s 910(1A) the directors have prepared a supplementary accounting statement` | 2 | 0 | This section applies if |
| `s 910(2) the statement consists of what the section requires` | 2 | 0 | not more than three months before the draft terms were adopted |
| `s 910(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` | 0 | 1 | apply to the balance sheet required for an accounting statement under this section |
| `s 910(4) the balance sheet has been approved and signed as section 414 provides` | 0 | 1 | apply to the balance sheet required for an accounting statement under this section |
| `s 911(3) the document is one the members must be able to inspect` | 4 | 0 | The requirements of subsection (3)(b) and (c) are subject to section 915 ... and section 918A |
| `s 911(5) section 1145 does not apply to the document` | 0 | 1 | does not apply to a document sent or supplied in accordance with subsection (1)(b) to a member who has consent |
| `s 911(6) Part 4 of Schedule 5 does not apply` | 0 | 1 | does not apply for the purposes of subsection (1)(b) (but see section 911A(5)) |
| `s 911A(2) the first condition is met` | 1 | 0 | The first condition is that the document is made available on a website which— (a) is maintained by or on beha |
| `s 911A(3) the second condition is met` | 1 | 0 | The second condition is that access to the document on the website is not conditional on payment of a fee or o |
| `s 911A(4) the third condition is met` | 1 | 0 | The third condition is that the document remains available on the website throughout the period beginning one  |
| `s 911A(1) section 911(1)(a) does not apply to the document` | 1 | 0 | Where members of a company are able to obtain copies of a document only as mentioned in subsection (5), sectio |
| `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` | 2 | 0 | A person is able to obtain a copy of a document as required by section 911(1)(b) if— (a) the conditions in sub |
| `s 911A(6) members can obtain copies only as mentioned in subsection (5)` | 0 | 1 | Where members of a company are able to obtain copies of a document only as mentioned in subsection (5) |
| `s 912(1) the articles of the transferee company have been approved by ordinary resolution` | 2 | 0 | In the case of a merger by formation of a new company |
| `s 913(1) the scheme protects the holder of securities to which special rights are attached` | 2 | 0 | where any securities of a transferor company (other than shares) to which special rights are attached are held |
| `s 914 the scheme does not provide for the allotment of shares the section forbids` | 1 | 0 | The scheme must not provide for any shares in the transferee company to be allotted to |
| `s 915(1) this section applies` | 1 | 0 | This section applies in the case of a merger by absorption where all of the relevant securities of the transfe |
| `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)` | 1 | 0 | The draft terms of the scheme need not give the particulars mentioned in section 905(2)(b), (c) or (d) |
| `s 915(3) section 897 does not apply` | 1 | 0 | In a case where a meeting has been summoned under section 896 in relation to the compromise or arrangement, se |
| `s 915(3A) section 901D does not apply` | 1 | 0 | In a case where a meeting has been summoned under section 901C in relation to the compromise or arrangement, s |
| `s 915(4) the requirements of sections 908 and 909 do not apply` | 1 | 0 | The requirements of the following sections do not apply— section 908 (directors' explanatory report), section  |
| `s 915(5) the requirements of section 911 so far as relating to a document required to be drawn up under sections 908 and 909 do not apply` | 1 | 0 | The requirements of section 911 (inspection of documents) so far as relating to any document required to be dr |
| `s 915A(1) this section applies` | 1 | 0 | This section applies in the case of a merger by absorption where 90% or more (but not all) of the relevant sec |
| `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` | 1 | 0 | If the conditions in subsections (3) and (4) are met, the requirements of the following sections do not apply |
| `s 915A(3) the first condition is met` | 1 | 0 | The first condition is that the scheme provides that every other holder of relevant securities has the right t |
| `s 915A(4) the second condition is met` | 1 | 0 | The second condition is that, if a holder of securities exercises that right, the consideration to be given fo |
| `s 915A(5) the court may determine, or make provision for the determination of, the consideration` | 0 | 1 | the power to determine ... the consideration to be given for securities acquired under this section |
| `s 916(1) this section applies` | 1 | 0 | This section applies in the case of a merger by absorption where 90% or more (but not all) of the relevant sec |
| `s 916(3A) subsection (3A) is satisfied` | 1 | 0 | This subsection is satisfied if publication of notice of receipt of the draft terms by the registrar took plac |
| `s 916(3B) subsection (3B) is satisfied` | 3 | 0 | (a) the conditions in section 906A(2) to (4) are met in respect of the transferee company |
| `s 916(3) the first condition is met` | 1 | 0 | The first condition is that either subsection (3A) or subsection (3B) is satisfied |
| `s 916(4A) subsection (4A) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if the members of the transferee company were able during the peri |
| `s 916(4B) subsection (4B) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if— (a) the document is made available on a website which is maint |
| `s 916(4) the second condition is met` | 1 | 0 | The second condition is that subsection (4A) or (4B) is satisfied for each of the documents listed in the appl |
| `s 916(4C) the third condition is met` | 1 | 0 | The third condition is that the members of the transferee company were able to obtain copies of the documents  |
| `s 916(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` | 0 | 1 | For the purposes of subsection (4C) |
| `s 916(5) the fourth condition is met` | 1 | 0 | The fourth condition is that— (a) one or more members of the transferee company, who together held not less th |
| `s 916(2) the meeting of members of the transferee company is not required` | 3 | 0 | This section applies in the case of a merger by absorption where |
| `s 917(3A) subsection (3A) is satisfied` | 1 | 0 | This subsection is satisfied if publication of notice of receipt of the draft terms by the registrar took plac |
| `s 917(3B) subsection (3B) is satisfied` | 3 | 0 | (a) the conditions in section 906A(2) to (4) are met in respect of all the merging companies |
| `s 917(3) the first condition is met` | 1 | 0 | The first condition is that either subsection (3A) or subsection (3B) is satisfied |
| `s 917(4A) subsection (4A) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if the members of the transferee company were able during the peri |
| `s 917(4B) subsection (4B) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if— (a) the document is made available on a website which is maint |
| `s 917(4) the second condition is met` | 1 | 0 | The second condition is that subsection (4A) or (4B) is satisfied for each of the documents listed in the appl |
| `s 917(4C) the third condition is met` | 1 | 0 | The third condition is that the members of the transferee company were able to obtain copies of the documents  |
| `s 917(4D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` | 0 | 1 | For the purposes of subsection (4C) |
| `s 917(5) the fourth condition is met` | 1 | 0 | The fourth condition is that— (a) one or more members of the transferee company, who together held not less th |
| `s 917(2) the meeting of members of any of the merging companies is not required` | 3 | 0 | This section applies in the case of a merger by absorption where |
| `s 917(1) this section applies` | 1 | 0 | This section applies in the case of a merger by absorption where all of the relevant securities of the transfe |
| `s 917A(1) the meeting of members of the transferor company is not required` | 1 | 0 | In the case of a compromise or arrangement to be sanctioned under Part 26A, it is not necessary |
| `s 918(2A) subsection (2A) is satisfied` | 1 | 0 | This subsection is satisfied if publication of notice of receipt of the draft terms by the registrar took plac |
| `s 918(2B) subsection (2B) is satisfied` | 3 | 0 | (a) the conditions in section 906A(2) to (4) are met in respect of the transferee company |
| `s 918(2) the first condition is met` | 1 | 0 | The first condition is that either subsection (2A) or subsection (2B) is satisfied |
| `s 918(3A) subsection (3A) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if the members of the transferee company were able during the peri |
| `s 918(3B) subsection (3B) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if— (a) the document is made available on a website which is maint |
| `s 918(3) the second condition is met` | 1 | 0 | The second condition is that subsection (3A) or (4B) is satisfied for each of the documents listed in the appl |
| `s 918(3C) the third condition is met` | 1 | 0 | The third condition is that the members of the transferee company were able to obtain copies of the documents  |
| `s 918(3D) section 911A(5) applies and Part 4 of Schedule 5 does not apply` | 0 | 1 | For the purposes of subsection (3C) |
| `s 918(4) the fourth condition is met` | 1 | 0 | The fourth condition is that— (a) one or more members of the transferee company, who together held not less th |
| `s 918(1) the meeting of members of the transferee company is not required` | 3 | 0 | In the case of any merger by absorption |
| `s 918A(1) the requirements are dispensed with by agreement` | 1 | 0 | If all members holding shares in, and all persons holding other securities of, the merging companies ... so ag |
| `s 918A(2) the holding counts for the purposes of section 918A` | 1 | 0 | are determined as at the date of the relevant application |
| `s 919(1) the scheme involves a division` | 1 | 0 | The scheme involves a division where under the scheme the undertaking, property and liabilities of the company |
| `s 919(2) the company is one of the companies involved in the division` | 1 | 0 | References in this Part to the companies involved in the division are to the transferor company and any existi |
| `s 921(2) the registrar has published notice of receipt of the draft terms in the Gazette` | 0 | 1 | notice of receipt by him from that company of a copy of the draft terms |
| `s 921(3) the notice was published at least one month before the meeting` | 1 | 1 | before the date of any meeting of that company summoned for the purpose of approving the scheme |
| `s 921A(2) the first condition is met` | 1 | 0 | The first condition is that the draft terms are made available on a website which— (a) is maintained by or on  |
| `s 921A(3) the second condition is met` | 1 | 0 | The second condition is that neither access to the draft terms on the website nor the supply of a hard copy of |
| `s 921A(4) the third condition is met` | 1 | 0 | The third condition is that the directors of the company deliver to the registrar a notice giving details of t |
| `s 921A(5) the fourth condition is met` | 1 | 0 | The fourth condition is that the registrar publishes the notice in the Gazette at least one month before the d |
| `s 921A(6) the fifth condition is met` | 1 | 0 | The fifth condition is that the draft terms remain available on the website throughout the period beginning on |
| `s 921A(1) section 921 does not apply in respect of the company` | 1 | 0 | Section 921 does not apply in respect of a company if the conditions in subsections (2) to (6) are met |
| `s 923(2A) the required statement explaining the effect of the compromise or arrangement` | 0 | 1 | in a case where a meeting is summoned under section 896 ...; in a case where a meeting is summoned under secti |
| `s 924(3) the way the expert's report is drawn up complies` | 1 | 0 | If no such appointment is made, there must be a separate expert's report to the members of each company involv |
| `s 924(4) the person may be the expert` | 1 | 0 | The expert must be a person who— (a) is eligible for appointment as a statutory auditor ..., and (b) meets the |
| `s 924(6) the expert has the right of access to the document or to require the information` | 0 | 1 | The expert (or each of them) has ... all such documents ... as he thinks necessary for the purposes of making  |
| `s 925(1) this section applies` | 2 | 0 | This section applies if the last annual accounts of a company involved in the division relate to a financial y |
| `s 925(1A) the directors have prepared a supplementary accounting statement` | 2 | 0 | This section applies if |
| `s 925(2) the statement consists of what the section requires` | 2 | 0 | not more than three months before the draft terms were adopted |
| `s 925(3) the requirements as to the balance sheet of annual accounts apply to the balance sheet` | 0 | 1 | apply to the balance sheet required for an accounting statement under this section |
| `s 925(4) the balance sheet has been approved and signed as section 414 provides` | 0 | 1 | apply to the balance sheet required for an accounting statement under this section |
| `s 926(5) section 1145 does not apply to the document` | 0 | 1 | does not apply to a document sent or supplied in accordance with subsection (1)(b) to a member who has consent |
| `s 926(6) Part 4 of Schedule 5 does not apply` | 0 | 1 | does not apply for the purposes of subsection (1)(b) (but see section 926A(5)) |
| `s 926(3) the document is one the members must be able to inspect` | 5 | 0 | The requirements in subsection (3)(b), (c) and (e) are subject to section 933 ..., section 933A ... and sectio |
| `s 926A(2) the first condition is met` | 1 | 0 | The first condition is that the document is made available on a website which— (a) is maintained by or on beha |
| `s 926A(3) the second condition is met` | 1 | 0 | The second condition is that access to the document on the website is not conditional on payment of a fee or o |
| `s 926A(4) the third condition is met` | 1 | 0 | The third condition is that the document remains available on the website throughout the period beginning one  |
| `s 926A(1) section 926(1)(a) does not apply to the document` | 1 | 0 | Where members of a company are able to obtain copies of a document only as mentioned in subsection (5), sectio |
| `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` | 2 | 0 | A person is able to obtain a copy of a document as required by section 926(1)(b) if— (a) the conditions in sub |
| `s 926A(6) members can obtain copies only as mentioned in subsection (5)` | 0 | 1 | Where members of a company are able to obtain copies of a document only as mentioned in subsection (5) |
| `s 928(1) the articles of every new transferee company have been approved by ordinary resolution of the transferor company` | 1 | 0 | Subsection (1) does not apply in the case of a compromise or arrangement to be sanctioned under Part 26A |
| `s 929(1) the scheme protects the holder of securities to which special rights are attached` | 2 | 0 | where any securities of a transferor company (other than shares) to which special rights are attached are held |
| `s 930 the scheme does not provide for the allotment of shares the section forbids` | 1 | 0 | The scheme must not provide for any shares in a transferee company to be allotted to |
| `s 931(1) this section applies` | 1 | 0 | This section applies in the case of a division where all of the shares or other securities of the transferor c |
| `s 931(3A) subsection (3A) is satisfied` | 1 | 0 | This subsection is satisfied if publication of notice of receipt of the draft terms by the registrar took plac |
| `s 931(3B) subsection (3B) is satisfied` | 3 | 0 | (a) the conditions in section 906A(2) to (4) are met in respect of all the companies involved in the division |
| `s 931(3) the first condition is met` | 1 | 0 | The first condition is that either subsection (3A) or subsection (3B) is satisfied |
| `s 931(4A) subsection (4A) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if the members of every company involved in the division were able |
| `s 931(4B) subsection (4B) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if— (a) the document is made available on a website which is maint |
| `s 931(4) the second condition is met` | 1 | 0 | The second condition is that subsection (4A) or (4B) is satisfied for each of the documents listed in the appl |
| `s 931(4C) the third condition is met` | 1 | 0 | The third condition is that the members of every company involved in the division were able to obtain copies o |
| `s 931(4D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` | 0 | 1 | For the purposes of subsection (4C) |
| `s 931(2) the meeting of members of the transferor company is not required` | 3 | 0 | This section applies in the case of a division where |
| `s 931(6) the fourth condition is met` | 1 | 0 | The fourth condition is that the directors of the transferor company have sent— (a) to every member ..., and ( |
| `s 931A(1) the meeting of members of the transferor company is not required` | 1 | 0 | In the case of a compromise or arrangement to be sanctioned under Part 26A, it is not necessary |
| `s 932(2A) subsection (2A) is satisfied` | 1 | 0 | This subsection is satisfied if publication of notice of receipt of the draft terms by the registrar took plac |
| `s 932(2B) subsection (2B) is satisfied` | 3 | 0 | (a) the conditions in section 906A(2) to (4) are met in respect of the transferee company |
| `s 932(2) the first condition is met` | 1 | 0 | The first condition is that either subsection (2A) or subsection (2B) is satisfied |
| `s 932(3A) subsection (3A) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if the members of the transferee company were able during the peri |
| `s 932(3B) subsection (3B) is satisfied for the document` | 1 | 0 | This subsection is satisfied for a document if— (a) the document is made available on a website which is maint |
| `s 932(3) the second condition is met` | 1 | 0 | The second condition is that subsection (3A) or (4B) is satisfied for each of the documents listed in the appl |
| `s 932(3C) the third condition is met` | 1 | 0 | The third condition is that the members of the transferee company were able to obtain copies of the documents  |
| `s 932(3D) section 926A(5) applies and Part 4 of Schedule 5 does not apply` | 0 | 1 | For the purposes of subsection (3C) |
| `s 932(4) the fourth condition is met` | 1 | 0 | The fourth condition is that— (a) one or more members of the transferee company, who together held not less th |
| `s 932(1) the meeting of members of the transferee company is not required` | 3 | 0 | In the case of a division |
| `s 933(1) the requirements are dispensed with by agreement` | 1 | 0 | If all members holding shares in, and all persons holding other securities of, the companies involved in the d |
| `s 933(3) the holding counts for the purposes of section 933` | 1 | 0 | are determined as at the date of the relevant application |
| `s 933A(1) this section applies` | 1 | 0 | This section applies in the case of a division where each of the transferee companies is a new company |
| `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` | 2 | 0 | This section applies in the case of a division where each of the transferee companies is a new company |
| `s 934(2) the first condition is met` | 1 | 0 | The first condition is that the members of that company will have received, or will have been able to obtain f |
| `s 934(3) the second condition is met` | 1 | 0 | The second condition is that the creditors of that company will have received or will have been able to obtain |
| `s 934(4) the third condition is met` | 1 | 0 | The third condition is that no prejudice would be caused to the members or creditors of the transferor company |
| `s 934(1) the court may by order direct that the requirements do not apply` | 0 | 2 | if the court is satisfied that the following conditions will be fulfilled in relation to that company |
| `s 934(1)(a) the court has directed that sections 921 and 926 do not apply` | 1 | 0 | the court may by order direct that ... the requirements of— (i) section 921 ..., and (ii) section 926 ..., do  |
| `s 934(1)(b) section 932 has effect without its first, second and third conditions` | 1 | 0 | in relation to an existing transferee company, section 932 ... has effect with the omission of the first, seco |
| `s 935(1) the expert may arrange for or accept the valuation` | 2 | 0 | Where it appears to an expert— (a) that a valuation is reasonably necessary ..., and (b) that it is reasonable |
| `s 935(2) the expert's report states what the section requires` | 1 | 0 | Where any valuation is made by a person other than the expert himself |
| `s 936(1) the person meets the independence requirement` | 2 | 0 | A person meets the independence requirement ... only if— (a) he is not— (i) an officer or employee of any of t |
| `s 936(2) the person is regarded as an officer or employee of the company for the purposes of section 936` | 1 | 0 | An auditor of a company is not regarded as an officer or employee of the company for this purpose |
| `s 937(1) the definition applies` | 0 | 1 | defines “associate” for the purposes of section 936 |
| `s 938(1) the court may order a meeting of the members or creditors of the company` | 0 | 1 | The court may order a meeting of— (a) the members of an existing transferee company, ..., or (b) the creditors |
| `s 938(2) the person may apply to the court` | 0 | 2 | if the company is being wound up, the liquidator |
| `s 938(3) section 323 applies to the meeting` | 0 | 1 | applies to a meeting of creditors under this section |
| `s 939(1) the court has fixed a date for the transfer` | 1 | 0 | Where the court sanctions the compromise or arrangement |
| `s 939(2) the order fixes the same date for the dissolution` | 1 | 0 | Any such order that provides for the dissolution of the transferor company |
| `s 939(3) the court has fixed a date for the steps within six months` | 1 | 0 | If it is necessary for the transferor company to take steps to ensure that the undertaking, property and liabi |
| `s 939(4) the court may postpone the dissolution of the transferor company until that date` | 0 | 1 | In that case, the court may postpone the dissolution |
| `s 939(5) the court may postpone or further postpone the date` | 0 | 1 | if it is satisfied that the steps mentioned cannot be completed by the date (or latest date) fixed under that  |
| `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` | 2 | 0 | If, in the case of a compromise or arrangement to be sanctioned under Part 26, a majority in number representi |
| `s 940(1) the amount for which the transferee company is liable` | 1 | 1 | In the case of a division, each transferee company is jointly and severally liable for any liability transferr |
| `s 940A(2) the provision is one of those to which section 940A(1) applies` | 1 | 0 | The provisions referred to above are |
| `s 940A(1) the failure is to be disregarded` | 1 | 0 | is to be disregarded if— (a) it is made available on the website for part of that period, and (b) the failure  |

Fork lines of the name-test sweep of 2026-11-12 (the flipped functions above carry a `NOTHING-kind (limited by its own wording)` branch for the unmet "if"; each line names the other reading):

- **F26** `s 896(2) the person may apply for an order for a meeting`: s 896(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'.
- **F27** `s 899(1) the court may sanction the compromise or arrangement`: s 899(1): 'If a majority in number representing 75% in value ... agree a compromise or arrangement, the court may ... sanction': when the votes fall short of that test the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The count test itself is fork F2. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar).
- **F28** `s 899(2) the person may apply for the court's sanction`: s 899(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). The two printed versions of limb (c) are fork F1. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'.
- **F29** `s 901C(2) the person may apply to the court`: s 901C(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'.
- **F30** `s 901F(1) the court may sanction the compromise or arrangement`: s 901F(1): 'If a number representing 75% in value ... agree a compromise or arrangement, the court may ... sanction': when the value falls short of 75% the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The absence of a headcount test is fork F5. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar).
- **F31** `s 901F(3) the person may apply to the court`: s 901F(3): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'.
- **F32** `s 934(1) the court may by order direct that the requirements do not apply`: s 934(1): 'the court may by order direct that ... if the court is satisfied that the following conditions will be fulfilled in relation to that company': when the court is not satisfied, or a condition of s 934(2) to (4) fails, the court is not covered (NOTHING): the text gives the court the power on an 'if' and says nothing of the court outside it, and it does not say 'only if' (name-test sweep of 2026-11-12). The court's satisfaction as a conditional input is fork F4. **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar).
- **F33** `s 938(2) the person may apply to the court`: s 938(2): 'if the company is being wound up, the liquidator' and 'if the company is in administration, the administrator': a liquidator of a company that is not being wound up, or an administrator of a company that is not in administration, is not covered (NOTHING): the text gives the power to them on a condition and says nothing of them outside it, and its list does not say 'only' (the Guide's line on a grant limited by its own wording; name-test sweep of 2026-11-12). **Other reading:** JUST FALSE: the unmet 'if' read as the text's own no (a failed 'if' as a bar), as the 2026-11-05 ruling reads a failed 'where'.

## Seams (coa20)

Each seam input is named for the answering section (PLAN.md section 4). The lead wires the answering part's function to the input at the merge: `JUST TRUE`, `JUST FALSE` or `NOTHING` passes straight through. Two lists: the seams to other parts (answers my ranges take as inputs), and the seams inside my own ranges (one of my rules takes another of my rules' answer; the seat layer wires them).

PLAN.md and the brief differ on one point, and the brief governs: the brief says layer 1 imports the keel's `coa-core.l4` and `coa-definitions.l4`; PLAN.md section 4.1 says parts cannot import the keel's definitions module and take its answers as inputs. Every layer-1 module imports both (measured: three modules, two importing `coa-definitions` and one importing both, check clean, so the merged import is safe), but the rules take the keel's answers as inputs named as PLAN.md names them, so that the lead's wiring does not depend on the import. The tests import `coa-definitions` and nothing in them uses it.

### Seams to other parts (answers taken as inputs)

| input (named for the answering section) | taken by |
| --- | --- |
| `s 1(1) the body is a company` | `s 895(2) the body is a company for the purposes of Part 26`, `s 901A(4) the body is a company for the purposes of Part 26A` |
| `s 1121 the officer is in default` | `s 897(5) the person is guilty of an offence under section 897`, `s 900(7) the person is guilty of an offence under section 900(7)`, `s 901(5) the person is guilty of an offence under section 901`, `s 901D(5) the person is guilty of an offence under section 901D` (+2 more) |
| `s 4(2) the company is a public company` | `s 902(1) this Part applies` |
| `s 1212 the person is eligible for appointment as a statutory auditor` | `s 909(4) the person may be the expert`, `s 924(4) the person may be the expert` |
| `s 399 the company would be required to prepare group accounts if that date were the last day of a financial year` | `s 910(2) the statement consists of what the section requires`, `s 925(2) the statement consists of what the section requires` |
| `s 414 the balance sheet has been approved and signed as that section provides` | `s 910(4) the balance sheet has been approved and signed as section 414 provides`, `s 925(4) the balance sheet has been approved and signed as section 414 provides` |
| `s 282 the resolution approving the articles or a draft of them is an ordinary resolution of the transferor company` | `s 912(1) the articles of the transferee company have been approved by ordinary resolution`, `s 928(1) the articles of every new transferee company have been approved by ordinary resolution of the transferor company` |
| `s 1162(2) the undertaking is a parent undertaking or subsidiary undertaking of the company` | `s 936(3)(b) the undertaking is an associated undertaking of the company` |
| `s 1162(4) the undertaking is a subsidiary undertaking of a parent undertaking of the company` | `s 936(3)(b) the undertaking is an associated undertaking of the company` |

Seams the PLAN lacks, found in my ranges: `s 1046` (whether an overseas company is required to register particulars: s 901F(6)(a), taken as a plain fact, not a function: it is coa23's), `s 593` (the report on a valuation of non-cash consideration, s 923(3): taken as a fact "a report has been made", not an answer), the Insolvency Act 1986 and Insolvency (Northern Ireland) Order 1989 (ss 895(2), 899A(6), 901A(4), 901H(6): borrowed definitions taken as inputs, as the keel does for borrowed terms), the Pensions Acts 2004 and 1993 and the 2005 Order (s 901I(9)), the Financial Services and Markets Act 2000 (ss 901B(2), 910(5), 925(4A)). The "regulations specified" connection of s 936(1)(c) is a plain input (the regulations are not among the sources).

### Seams inside my own ranges (wired by the seat layer)

| input | answered by (the rule of that name) | taken by |
| --- | --- | --- |
| `s 902(1) this Part applies` | `s 902(1) this Part applies` | `s 895(3) the provisions of Part 26 have effect subject to Part 27`, `s 901A(5) the provisions of Part 26A have effect subject to Part 27` |
| `s 899A(1) this section applies` | `s 899A(1) this section applies` | `s 896(4) section 896 is subject to section 899A`, `s 899(1A) section 899(1) is subject to section 899A`, `s 899A(3) the relevant creditor may participate in the meeting summoned under section 896` (+2 more) |
| `s 900(1) this section applies` | `s 900(1) this section applies` | `s 900(2) the court may make provision for the matter` |
| `s 901(1) this section applies to the order` | `s 901(1) this section applies to the order` | `s 901(2) the copy of the order is accompanied as the section requires`, `s 901(3) the copy of the articles is accompanied as the section requires` |
| `s 901H(1) this section applies` | `s 901H(1) this section applies` | `s 901C(7) section 901C is subject to section 901H`, `s 901F(2) section 901F(1) is subject to sections 901G and 901H`, `s 901H(3) the relevant creditor may participate in the meeting summoned under section 901C` (+2 more) |
| `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` | `s 901F(2) section 901F(1) is subject to sections 901G and 901H` |
| `s 901G(1) this section applies` | `s 901G(1) this section applies` | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` |
| `s 901G(3) condition A is met` | `s 901G(3) condition A is met` | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` |
| `s 901G(5) condition B is met` | `s 901G(5) condition B is met` | `s 901G(2) the dissent of the dissenting class does not prevent the court from sanctioning under section 901F` |
| `s 901J(1) this section applies` | `s 901J(1) this section applies` | `s 901J(2) the court may make provision for the matter` |
| `s 901K(1) this section applies to the order` | `s 901K(1) this section applies to the order` | `s 901K(2) the copy of the order is accompanied as the section requires`, `s 901K(3) the copy of the articles is accompanied as the section requires` |
| `s 904(1) the scheme involves a merger` | `s 904(1) the scheme involves a merger` | `s 902(1) this Part applies` |
| `s 919(1) the scheme involves a division` | `s 919(1) the scheme involves a division` | `s 902(1) this Part applies` |
| `s 904(1)(a) the scheme involves a merger by absorption` | `s 904(1)(a) the scheme involves a merger by absorption` | `s 904(1) the scheme involves a merger` |
| `s 904(1)(b) the scheme involves a merger by formation of a new company` | `s 904(1)(b) the scheme involves a merger by formation of a new company` | `s 904(1) the scheme involves a merger` |
| `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)` | `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)` | `s 905(2) the draft terms give the particulars required` |
| `s 915(1) this section applies` | `s 915(1) this section applies` | `s 905(3) the requirements in subsection (2)(b), (c) and (d) are subject to section 915`, `s 915(2) the draft terms need not give the particulars in section 905(2)(b), (c) and (d)`, `s 915(3) section 897 does not apply` (+3 more) |
| `s 906A(1) section 906 does not apply in respect of the company` | `s 906A(1) section 906 does not apply in respect of the company` | `s 906(1) the directors have delivered a copy of the draft terms to the registrar`, `s 906(4) the requirements in section 906 are subject to section 906A` |
| `s 940A(1) the failure to make the draft terms available throughout the period is to be disregarded` | (a fact, not a rule: asked of the person) | `s 906A(6) the fifth condition is met`, `s 921A(6) the fifth condition is met` |
| `s 906A(2) the first condition is met` | `s 906A(2) the first condition is met` | `s 906A(1) section 906 does not apply in respect of the company`, `s 916(3B) subsection (3B) is satisfied`, `s 917(3B) subsection (3B) is satisfied` (+1 more) |
| `s 906A(3) the second condition is met` | `s 906A(3) the second condition is met` | `s 906A(1) section 906 does not apply in respect of the company`, `s 916(3B) subsection (3B) is satisfied`, `s 917(3B) subsection (3B) is satisfied` (+1 more) |
| `s 906A(4) the third condition is met` | `s 906A(4) the third condition is met` | `s 906A(1) section 906 does not apply in respect of the company`, `s 916(3B) subsection (3B) is satisfied`, `s 917(3B) subsection (3B) is satisfied` (+1 more) |
| `s 906A(5) the fourth condition is met` | `s 906A(5) the fourth condition is met` | `s 906A(1) section 906 does not apply in respect of the company` |
| `s 906A(6) the fifth condition is met` | `s 906A(6) the fifth condition is met` | `s 906A(1) section 906 does not apply in respect of the company` |
| `s 907(2) the meeting of members is not required` | `s 907(2) the meeting of members is not required` | `s 907(1) the scheme has been approved by the members of the merging company` |
| `s 916(2) the meeting of members of the transferee company is not required` | `s 916(2) the meeting of members of the transferee company is not required` | `s 907(2) the meeting of members is not required` |
| `s 917(2) the meeting of members of any of the merging companies is not required` | `s 917(2) the meeting of members of any of the merging companies is not required` | `s 907(2) the meeting of members is not required` |
| `s 917A(1) the meeting of members of the transferor company is not required` | `s 917A(1) the meeting of members of the transferor company is not required` | `s 907(2) the meeting of members is not required` |
| `s 918(1) the meeting of members of the transferee company is not required` | `s 918(1) the meeting of members of the transferee company is not required` | `s 907(2) the meeting of members is not required` |
| `s 908(3) the requirement in section 908 is excluded` | `s 908(3) the requirement in section 908 is excluded` | `s 908(1) the directors have drawn up and adopted a report` |
| `s 915(4) the requirements of sections 908 and 909 do not apply` | `s 915(4) the requirements of sections 908 and 909 do not apply` | `s 908(3) the requirement in section 908 is excluded`, `s 909(7) the requirement in section 909 is excluded` |
| `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` | `s 908(3) the requirement in section 908 is excluded`, `s 909(7) the requirement in section 909 is excluded`, `s 910(6) the requirement in section 910 is excluded` (+2 more) |
| `s 918A(1) the requirements are dispensed with by agreement` | `s 918A(1) the requirements are dispensed with by agreement` | `s 908(3) the requirement in section 908 is excluded`, `s 909(7) the requirement in section 909 is excluded`, `s 910(6) the requirement in section 910 is excluded` (+2 more) |
| `s 909(7) the requirement in section 909 is excluded` | `s 909(7) the requirement in section 909 is excluded` | `s 909(1) an expert's report has been drawn up on behalf of the company` |
| `s 936(1) the person meets the independence requirement` | `s 936(1) the person meets the independence requirement` | `s 909(4) the person may be the expert`, `s 924(4) the person may be the expert`, `s 935(1) the expert may arrange for or accept the valuation` |
| `s 910(1) this section applies` | `s 910(1) this section applies` | `s 910(1A) the directors have prepared a supplementary accounting statement` |
| `s 910(6) the requirement in section 910 is excluded` | `s 910(6) the requirement in section 910 is excluded` | `s 910(1A) the directors have prepared a supplementary accounting statement` |
| `s 911(7) the requirements in section 911 are excluded` | `s 911(7) the requirements in section 911 are excluded` | `s 911(1) the members could inspect the documents and obtain copies` |
| `s 911(4) the requirements of subsection (3)(b) and (c) are excluded` | `s 911(4) the requirements of subsection (3)(b) and (c) are excluded` | `s 911(3) the document is one the members must be able to inspect` |
| `s 911A(1) section 911(1)(a) does not apply to the document` | `s 911A(1) section 911(1)(a) does not apply to the document` | `s 911(3A) the requirement in section 911(1)(a) is subject to section 911A(1)` |
| `s 915(5) the requirements of section 911 so far as relating to a document required to be drawn up under sections 908 and 909 do not apply` | `s 915(5) the requirements of section 911 so far as relating to a document required to be drawn up under sections 908 and 909 do not apply` | `s 911(4) the requirements of subsection (3)(b) and (c) are excluded` |
| `s 940A(1) the failure to make the document available throughout the period is to be disregarded` | (a fact, not a rule: asked of the person) | `s 911A(4) the third condition is met`, `s 926A(4) the third condition is met` |
| `s 911A(2) the first condition is met` | `s 911A(2) the first condition is met` | `s 911A(1) section 911(1)(a) does not apply to the document`, `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| `s 911A(3) the second condition is met` | `s 911A(3) the second condition is met` | `s 911A(1) section 911(1)(a) does not apply to the document`, `s 911A(5) the person is able to obtain a copy as section 911(1)(b) requires` |
| `s 911A(4) the third condition is met` | `s 911A(4) the third condition is met` | `s 911A(1) section 911(1)(a) does not apply to the document` |
| `s 911A(6) members can obtain copies only as mentioned in subsection (5)` | `s 911A(6) members can obtain copies only as mentioned in subsection (5)` | `s 911A(1) section 911(1)(a) does not apply to the document` |
| `s 911B(3) the requirement in section 911B is excluded` | `s 911B(3) the requirement in section 911B is excluded` | `s 911B(1) the directors have reported material changes in property and liabilities`, `s 911B(2) the directors of the other merging companies have reported those matters in turn` |
| `s 915A(1) this section applies` | `s 915A(1) this section applies` | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| `s 915A(3) the first condition is met` | `s 915A(3) the first condition is met` | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| `s 915A(4) the second condition is met` | `s 915A(4) the second condition is met` | `s 915A(2) the requirements of sections 908, 909, 910, 911 and 911B do not apply` |
| `s 916(3A) subsection (3A) is satisfied` | `s 916(3A) subsection (3A) is satisfied` | `s 916(3) the first condition is met` |
| `s 916(3B) subsection (3B) is satisfied` | `s 916(3B) subsection (3B) is satisfied` | `s 916(3) the first condition is met` |
| `s 916(1) this section applies` | `s 916(1) this section applies` | `s 916(2) the meeting of members of the transferee company is not required` |
| `s 916(3) the first condition is met` | `s 916(3) the first condition is met` | `s 916(2) the meeting of members of the transferee company is not required` |
| `s 916(4) the second condition is met` | `s 916(4) the second condition is met` | `s 916(2) the meeting of members of the transferee company is not required` |
| `s 916(4C) the third condition is met` | `s 916(4C) the third condition is met` | `s 916(2) the meeting of members of the transferee company is not required` |
| `s 916(5) the fourth condition is met` | `s 916(5) the fourth condition is met` | `s 916(2) the meeting of members of the transferee company is not required` |
| `s 917(3A) subsection (3A) is satisfied` | `s 917(3A) subsection (3A) is satisfied` | `s 917(3) the first condition is met` |
| `s 917(3B) subsection (3B) is satisfied` | `s 917(3B) subsection (3B) is satisfied` | `s 917(3) the first condition is met` |
| `s 917(1) this section applies` | `s 917(1) this section applies` | `s 917(2) the meeting of members of any of the merging companies is not required` |
| `s 917(3) the first condition is met` | `s 917(3) the first condition is met` | `s 917(2) the meeting of members of any of the merging companies is not required` |
| `s 917(4) the second condition is met` | `s 917(4) the second condition is met` | `s 917(2) the meeting of members of any of the merging companies is not required` |
| `s 917(4C) the third condition is met` | `s 917(4C) the third condition is met` | `s 917(2) the meeting of members of any of the merging companies is not required` |
| `s 917(5) the fourth condition is met` | `s 917(5) the fourth condition is met` | `s 917(2) the meeting of members of any of the merging companies is not required` |
| `s 918(2A) subsection (2A) is satisfied` | `s 918(2A) subsection (2A) is satisfied` | `s 918(2) the first condition is met` |
| `s 918(2B) subsection (2B) is satisfied` | `s 918(2B) subsection (2B) is satisfied` | `s 918(2) the first condition is met` |
| `s 918 the scheme is a merger by absorption` | (a fact, not a rule: asked of the person) | `s 918(1) the meeting of members of the transferee company is not required` |
| `s 918(2) the first condition is met` | `s 918(2) the first condition is met` | `s 918(1) the meeting of members of the transferee company is not required` |
| `s 918(3) the second condition is met` | `s 918(3) the second condition is met` | `s 918(1) the meeting of members of the transferee company is not required` |
| `s 918(3C) the third condition is met` | `s 918(3C) the third condition is met` | `s 918(1) the meeting of members of the transferee company is not required` |
| `s 918(4) the fourth condition is met` | `s 918(4) the fourth condition is met` | `s 918(1) the meeting of members of the transferee company is not required` |
| `s 921(4) the requirements in section 921 are excluded` | `s 921(4) the requirements in section 921 are excluded` | `s 921(1) the directors have delivered a copy of the draft terms to the registrar` |
| `s 921A(1) section 921 does not apply in respect of the company` | `s 921A(1) section 921 does not apply in respect of the company` | `s 921(4) the requirements in section 921 are excluded` |
| `s 934(1)(a) the court has directed that sections 921 and 926 do not apply` | `s 934(1)(a) the court has directed that sections 921 and 926 do not apply` | `s 921(4) the requirements in section 921 are excluded`, `s 926(1) the members could inspect the documents and obtain copies`, `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded` |
| `s 921A(2) the first condition is met` | `s 921A(2) the first condition is met` | `s 921A(1) section 921 does not apply in respect of the company`, `s 931(3B) subsection (3B) is satisfied`, `s 932(2B) subsection (2B) is satisfied` |
| `s 921A(3) the second condition is met` | `s 921A(3) the second condition is met` | `s 921A(1) section 921 does not apply in respect of the company`, `s 931(3B) subsection (3B) is satisfied`, `s 932(2B) subsection (2B) is satisfied` |
| `s 921A(4) the third condition is met` | `s 921A(4) the third condition is met` | `s 921A(1) section 921 does not apply in respect of the company`, `s 931(3B) subsection (3B) is satisfied`, `s 932(2B) subsection (2B) is satisfied` |
| `s 921A(5) the fourth condition is met` | `s 921A(5) the fourth condition is met` | `s 921A(1) section 921 does not apply in respect of the company` |
| `s 921A(6) the fifth condition is met` | `s 921A(6) the fifth condition is met` | `s 921A(1) section 921 does not apply in respect of the company` |
| `s 922(2) the meeting of members is not required` | `s 922(2) the meeting of members is not required` | `s 922(1) the scheme has been approved by the members of a company involved in the division` |
| `s 931(2) the meeting of members of the transferor company is not required` | `s 931(2) the meeting of members of the transferor company is not required` | `s 922(2) the meeting of members is not required` |
| `s 931A(1) the meeting of members of the transferor company is not required` | `s 931A(1) the meeting of members of the transferor company is not required` | `s 922(2) the meeting of members is not required` |
| `s 932(1) the meeting of members of the transferee company is not required` | `s 932(1) the meeting of members of the transferee company is not required` | `s 922(2) the meeting of members is not required` |
| `s 923(4) the requirement in section 923 is excluded` | `s 923(4) the requirement in section 923 is excluded` | `s 923(1) the directors have drawn up and adopted a report` |
| `s 933(1) the requirements are dispensed with by agreement` | `s 933(1) the requirements are dispensed with by agreement` | `s 923(4) the requirement in section 923 is excluded`, `s 924(7) the requirement in section 924 is excluded`, `s 925(5) the requirement in section 925 is excluded` (+2 more) |
| `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` | `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` | `s 923(4) the requirement in section 923 is excluded`, `s 924(7) the requirement in section 924 is excluded`, `s 925(5) the requirement in section 925 is excluded` (+2 more) |
| `s 924(7) the requirement in section 924 is excluded` | `s 924(7) the requirement in section 924 is excluded` | `s 924(1) an expert's report has been drawn up on behalf of the company` |
| `s 925(1) this section applies` | `s 925(1) this section applies` | `s 925(1A) the directors have prepared a supplementary accounting statement` |
| `s 925(5) the requirement in section 925 is excluded` | `s 925(5) the requirement in section 925 is excluded` | `s 925(1A) the directors have prepared a supplementary accounting statement` |
| `s 926A(1) section 926(1)(a) does not apply to the document` | `s 926A(1) section 926(1)(a) does not apply to the document` | `s 926(3A) the requirement in section 926(1)(a) is subject to section 926A(1)` |
| `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded` | `s 926(4) the requirements of subsection (3)(b), (c) and (e) are excluded` | `s 926(3) the document is one the members must be able to inspect` |
| `s 926A(2) the first condition is met` | `s 926A(2) the first condition is met` | `s 926A(1) section 926(1)(a) does not apply to the document`, `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| `s 926A(3) the second condition is met` | `s 926A(3) the second condition is met` | `s 926A(1) section 926(1)(a) does not apply to the document`, `s 926A(5) the person is able to obtain a copy as section 926(1)(b) requires` |
| `s 926A(4) the third condition is met` | `s 926A(4) the third condition is met` | `s 926A(1) section 926(1)(a) does not apply to the document` |
| `s 926A(6) members can obtain copies only as mentioned in subsection (5)` | `s 926A(6) members can obtain copies only as mentioned in subsection (5)` | `s 926A(1) section 926(1)(a) does not apply to the document` |
| `s 927(3) the requirement in section 927 is excluded` | `s 927(3) the requirement in section 927 is excluded` | `s 927(1) the directors have reported material changes in property and liabilities`, `s 927(2) the directors of each existing transferee company have reported those matters in turn` |
| `s 931(3A) subsection (3A) is satisfied` | `s 931(3A) subsection (3A) is satisfied` | `s 931(3) the first condition is met` |
| `s 931(3B) subsection (3B) is satisfied` | `s 931(3B) subsection (3B) is satisfied` | `s 931(3) the first condition is met` |
| `s 931(1) this section applies` | `s 931(1) this section applies` | `s 931(2) the meeting of members of the transferor company is not required` |
| `s 931(3) the first condition is met` | `s 931(3) the first condition is met` | `s 931(2) the meeting of members of the transferor company is not required` |
| `s 931(4) the second condition is met` | `s 931(4) the second condition is met` | `s 931(2) the meeting of members of the transferor company is not required` |
| `s 931(4C) the third condition is met` | `s 931(4C) the third condition is met` | `s 931(2) the meeting of members of the transferor company is not required` |
| `s 931(6) the fourth condition is met` | `s 931(6) the fourth condition is met` | `s 931(2) the meeting of members of the transferor company is not required` |
| `s 932(2A) subsection (2A) is satisfied` | `s 932(2A) subsection (2A) is satisfied` | `s 932(2) the first condition is met` |
| `s 932(2B) subsection (2B) is satisfied` | `s 932(2B) subsection (2B) is satisfied` | `s 932(2) the first condition is met` |
| `s 932 the scheme is a division` | (a fact, not a rule: asked of the person) | `s 932(1) the meeting of members of the transferee company is not required` |
| `s 932(2) the first condition is met` | `s 932(2) the first condition is met` | `s 932(1) the meeting of members of the transferee company is not required` |
| `s 932(3) the second condition is met` | `s 932(3) the second condition is met` | `s 932(1) the meeting of members of the transferee company is not required` |
| `s 932(3C) the third condition is met` | `s 932(3C) the third condition is met` | `s 932(1) the meeting of members of the transferee company is not required` |
| `s 932(4) the fourth condition is met` | `s 932(4) the fourth condition is met` | `s 932(1) the meeting of members of the transferee company is not required` |
| `s 934(1)(b) section 932 has effect without its first, second and third conditions` | `s 934(1)(b) section 932 has effect without its first, second and third conditions` | `s 932(5) the first, second and third conditions are subject to section 934` |
| `s 933A(1) this section applies` | `s 933A(1) this section applies` | `s 933A(2) the requirements of sections 923, 924, 925 and 927 do not apply` |
| `s 934(2) the first condition is met` | `s 934(2) the first condition is met` | `s 934(1) the court may by order direct that the requirements do not apply` |
| `s 934(3) the second condition is met` | `s 934(3) the second condition is met` | `s 934(1) the court may by order direct that the requirements do not apply` |
| `s 934(4) the third condition is met` | `s 934(4) the third condition is met` | `s 934(1) the court may by order direct that the requirements do not apply` |
| `s 937 the person is an associate` | `s 937 the person is an associate` | `s 936(3)(c) the person is an associate` |
| `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` | `s 940(2) subsection (1) does not apply in relation to the liabilities owed to those creditors` | `s 940(1) the amount for which the transferee company is liable` |
| `s 940(3) the net value transferred` | `s 940(3) the net value transferred` | `s 940(1) the amount for which the transferee company is liable` |
| `s 940A(2) the provision is one of those to which section 940A(1) applies` | `s 940A(2) the provision is one of those to which section 940A(1) applies` | `s 940A(1) the failure is to be disregarded` |

## Seat questions

66 exported questions, in the text's order. Each takes plain inputs with an `@desc` worded as the person would be asked, builds the layer-1 inputs from them and calls the layer-1 rule; the person states the answer of another part's section as a fact (s 1121, s 4(2), s 282, s 399, s 414, s 1212), which the lead replaces with the answering part's function at the merge.

| question | sections |
| --- | --- |
| Under section 895(1), does Part 26 (arrangements and reconstructions) apply to the compromise or arrangement that is proposed? | s 895(1) |
| Under section 896(2), may I apply to the court for an order that a meeting of the creditors or members be summoned? | s 896(2) |
| Under section 897(1), does the notice summoning the creditors' or members' meeting satisfy the requirement to give or offer the explanatory statement? | s 897(1) |
| Under section 897(2), does the explanatory statement say what the section requires: the effect of the compromise or arrangement and the directors' interests? | s 897(2) |
| Under section 897(4), am I entitled to be given a copy of the explanatory statement free of charge? | s 897(4) |
| Under section 897(5), am I guilty of an offence because the company made default in complying with the explanatory statement requirements? | ss 897(5)-(7) |
| Under section 897(8), what is the most I can be fined for an offence under section 897? | s 897(8) |
| Under section 898(1), must I, as a director or a debenture trustee, give the company notice of matters relating to myself? | s 898(1) |
| Under section 898(2), do I commit an offence if I make default in giving the company that notice? | ss 898(2)-(3) |
| Under section 898(3), what is the most I can be fined for that offence? | s 898(3) |
| Under section 899(1), may the court sanction the compromise or arrangement on the votes cast at the meeting? | s 899(1) |
| Under section 899(3), is a sanctioned compromise or arrangement binding on me? | s 899(3) |
| Under section 899(4), is the court's order still without effect because no copy has yet been delivered to the registrar? | s 899(4) |
| Under section 899A(3), may I take part in the creditors' meeting if I am a creditor in respect of a moratorium debt or priority pre-moratorium debt? | ss 899A(1)-(3) |
| Under section 899A(5), may the court sanction a compromise or arrangement that makes provision for a relevant creditor who has not agreed to it? | ss 899A(1), (5) |
| Under section 900(6), did the company deliver a copy of the order to the registrar within seven days after it was made? | s 900(6) |
| Under section 900(7), am I guilty of an offence because the company did not deliver the copy of the order in time? | s 900(7) |
| Under section 900(8), what is the most I can be fined for that offence, and what is the daily default fine? | s 900(8) |
| Under section 901(2), is the copy of the order delivered to the registrar accompanied by a copy of the amended articles, resolution or agreement as the section requires? | ss 901(1)-(2) |
| Under section 901(3), is each copy of the company's articles issued after the order is made accompanied by a copy of the order as the section requires? | ss 901(1), (3) |
| Under section 901A(1), does Part 26A (companies in financial difficulty) apply to the compromise or arrangement that is proposed? | s 901A(1)-(3) |
| Under section 901C(3), must I be permitted to take part in the meeting of creditors or members? | s 901C(3) |
| Under section 901C(4), does section 901C(3) not apply to my class because the court is satisfied that none of its members has a genuine economic interest in the company? | s 901C(4) |
| Under section 901D(1), does the notice summoning the creditors' or members' meeting satisfy the requirement to give or offer the explanatory statement? | s 901D(1) |
| Under section 901D(5), am I guilty of an offence because the company made default in complying with the explanatory statement requirements? | ss 901D(5)-(7) |
| Under section 901D(8), what is the most I can be fined for an offence under section 901D? | s 901D(8) |
| Under section 901E(1), must I, as a director or a debenture trustee, give the company notice of matters relating to myself for the explanatory statement? | s 901E(1) |
| Under section 901F(1), may the court sanction the compromise or arrangement on the votes cast at the meeting (75% in value)? | s 901F(1) |
| Under section 901G(2), can the court sanction the compromise or arrangement although one class has not agreed it? | ss 901G(1)-(5) |
| Under section 901F(6), is the court's order still without effect because the copy has not yet been published or delivered as required? | s 901F(6) |
| Under section 901I(1), has the notice or document sent to a creditor also been sent to the Pensions Regulator as the section requires? | s 901I(1) |
| Under section 901I(2), has the notice or document sent to a creditor also been sent to the Board of the Pension Protection Fund as the section requires? | s 901I(2) |
| Under section 901J(6), did the company deliver a copy of the order to the registrar within seven days after it was made? | s 901J(6) |
| Under section 901K(3), is each copy of the company's articles issued after the order is made accompanied by a copy of the order as the section requires? | ss 901K(1), (3) |
| Under section 902(1), does Part 27 (mergers and divisions of public companies) apply to the scheme that is proposed? | ss 902-904, 919 |
| Under section 905(2), do the draft terms of the merger scheme give the particulars the section requires? | ss 905(2), 915(2) |
| Under section 906(3), was the registrar's notice of receipt of the draft terms published in the Gazette at least one month before the members' meeting? | s 906(3) |
| Under section 907(1), has the merger scheme been approved by the members at the meeting (a majority in number representing 75% in value of each class)? | ss 907(1)-(2) |
| Under section 908(1), must the directors of each merging company draw up and adopt an explanatory report, and have they? | ss 908(1)-(3) |
| Under section 909(1), must an expert's report be drawn up on behalf of each merging company, and has it been? | ss 909(1)-(7) |
| Under section 909(4), may I act as the expert for a merging company: am I eligible as a statutory auditor and independent of the companies? | ss 909(4), 936(1) |
| Under section 910(1), must the directors prepare a supplementary accounting statement, and have they? | ss 910(1)-(6) |
| Under section 911(1), can the members of each merging company inspect the listed documents at the registered office and obtain copies free of charge throughout the month before the first meeting? | ss 911(1)-(2) |
| Under section 911B(1), must the directors report material changes in the company's property and liabilities to the members' meeting and to the other merging companies' directors, and have they? | s 911B(1) |
| Under section 912, must the articles of the new transferee company be approved by ordinary resolution of each transferor company, and have they been? | s 912 |
| Under section 913, must the merger scheme give me rights of equivalent value in the transferee company if I hold securities of a transferor company with special rights, and does it? | s 913 |
| Under section 914, does the merger scheme comply with the ban on allotting shares in the transferee company to a transferor company or its nominee in respect of its own shares? | s 914 |
| Under section 915A(1), are the conditions met for the reports and inspection requirements to be dropped where the transferee company holds 90% or more (but not all) of a transferor company's voting securities? | ss 915A(1)-(4) |
| Under section 916(2), is the meeting of the transferee company's members excused, on the court being satisfied the four conditions have been complied with? | ss 916(1)-(5) |
| Under section 918A(1), have all the members and holders of voting securities of the merging companies agreed to dispense with the reports and the inspection requirements? | s 918A(1) |
| Under section 920(2), do the draft terms of the division scheme give the particulars the section requires? | s 920(2) |
| Under section 922(1), has the division scheme been approved by the members of the company at the meeting (a majority in number representing 75% in value of each class)? | ss 922(1)-(2) |
| Under section 923(3), does the directors' report on the division say whether a report was made under section 593 and whether it was delivered to the registrar? | s 923(3) |
| Under section 926(1), can the members of each company involved in the division inspect the listed documents at the registered office and obtain copies free of charge throughout the month before the first meeting? | ss 926(1)-(2) |
| Under section 928, must the articles of each new transferee company be approved by ordinary resolution of the transferor company, and have they been? | s 928 |
| Under section 931(6), is the fourth condition for excusing the transferor's members' meeting met: has the board sent the report of material changes to every member and to the directors of every existing transferee company, covering changes up to a date no earlier than one month before the court's order? | s 931(6) |
| Under section 933A(2), do the reports and accounts requirements fall away because each transferee company is new and its shares are allotted to the transferor company's members in proportion to their rights? | ss 933A(1)-(2) |
| Under section 934(1), may the court direct that the publication and inspection requirements do not apply, or that the transferee company's meeting conditions are omitted? | ss 934(1)-(4) |
| Under section 935(1), may I, as the expert, arrange for or accept a valuation made by another person? | s 935(1) |
| Under section 936(1), do I meet the independence requirement to act as an expert or valuer for the companies concerned in the scheme? | s 936(1) |
| Under section 937, am I an associate of a person, for the purposes of the independence requirement? | s 937 |
| Under section 938(2), may I apply to the court for an order that a meeting of the members or creditors of an existing transferee company be summoned? | ss 938(1)-(2) |
| Under section 939(3), is the date the court fixed for the steps needed to complete the transfer within six months after the transfer date? | s 939(3) |
| Under section 940(1), how much may I claim, as a creditor of the transferor company in a division, from another transferee company for a liability that was transferred to a defaulting transferee company? | ss 940(1)-(3) |
| Under section 940(2), did the creditors agree to the scheme by the majority that takes away their claim against the other transferee companies? | ss 940(2), (2A) |
| Under section 940A(1), is the failure to keep the draft terms or document on the website throughout the period to be disregarded? | ss 940A(1)-(2) |

### Seat audit of 2026-11-12

Every one of the 66 seat questions was read, its name and its `@export` text, against the layer-1 function its body calls and against that function's body; the `@desc` texts were read in the same pass and none needed changing.
Direction mismatches (a question titled as a permission that returns the bar, or the reverse): none.
Every name points the same way as its function: the "may", "can", "is excused", "fall away" and "does not apply" questions call functions of the same sense.
ss 899A(3) and 899A(5) are bars in the text ("may not"), asked as permissions and answered by the permission-form functions, so they answer `JUST FALSE` or `NOTHING` and can never answer `JUST TRUE`.
Names that asked more or less than the function answers: two, ss 901I(1) and 901I(2), repaired earlier on 2026-11-12 (they were titled "must a notice ... also be sent" and answer "has it been sent as the section requires"); no name was changed in the rest of the audit.
`@export` texts that asked two questions where the name and the body answer one: six, repaired by cutting the text to the question the name and the body answer, with the names unchanged.
s 901(2) asked "must ... and was it".
s 901C(3) added "and can the company exclude my class", which is the separate question on s 901C(4).
s 902(1) added "and does the court need these requirements met", which is s 903(1) and is not computed there.
s 931(6) asked only whether the report was sent, where the body also tests how far the report reaches.
s 939(3) asked whether the court has fixed a date, where the body takes the date as given and tests it against six months.
s 940(1) asked "am I entitled ... and how much", where the body returns the amount: `JUST 0` when the creditors' agreement displaces the liability, `NOTHING` when it is not a division or the agreement is not known.
Left as they are, by decision: ss 911B(1), 912, 913 and 928, whose `@export` text still reads "must ... and have they" or "does it".
Their functions return `s 903(1) status of a requirement`, in which "does not apply" answers "must" and "complied with" or "not complied with" answers "have they", so the compound text asks what the status answers; ss 908(1), 909(1) and 910(1) carry the compound form in their names for the same reason.
A silent point for readers of Parts 26 and 26A: there `JUST FALSE` can mean that the section's conditions are not met (nothing arises) or that the requirement is not complied with (fork F15); in Part 27 the status says which.
Assertions restated by this audit: none, because no name changed (the four restated earlier today are the ones on ss 901I(1) and 901I(2)).

## What `check.sh` printed

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (target `main`: every module is also run with 1.6.109 and the counts compared). Before this agent's files the folder held `coa-core.l4` and `coa-definitions.l4` (2 modules, 0 assertions). `expected_failed` is empty: no assertion is meant to fail.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa20-cases-seat.l4                            0       168       0        0         0 |      0       168       0        0  same
coa20-part26.l4                                0         0       0        0         0 |      0         0       0        0  same
coa20-part26a.l4                               0         0       0        0         0 |      0         0       0        0  same
coa20-part27-division.l4                       0         0       0        0         0 |      0         0       0        0  same
coa20-part27-merger.l4                         0         0       0        0         0 |      0         0       0        0  same
coa20-part27-supp.l4                           0         0       0        0         0 |      0         0       0        0  same
coa20-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa20-tests-part26.l4                          0       196       0        0         0 |      0       196       0        0  same
coa20-tests-part26a.l4                         0       249       0        0         0 |      0       249       0        0  same
coa20-tests-part27-division.l4                 0       329       0        0         0 |      0       329       0        0  same
coa20-tests-part27-merger.l4                   0       408       0        0         0 |      0       408       0        0  same
coa20-tests-part27-supp.l4                     0       112       0        0         0 |      0       112       0        0  same
TOTAL (14 modules)                             0      1462       0        0           |      0      1462       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)

```

The numbers per file: the five test files satisfy 196 (s 895 to 901), 249 (s 901A to 901L), 408 (s 902 to 918A), 329 (s 919 to 934) and 112 (s 935 to 941) assertions, and the seat cases satisfy 168; 1462 in all, none failed, none refused. The test files written by hand contain expectations written from the text before the run; the tests of a cloned twin are the twin's tests renamed by `work/gen_tests26a.py`, `gen_tests27m.py` and `gen_tests27d.py` (the expected values were re-read against the twin's own text, finding 5 being the difference that matters). Two assertions failed on the first run (s 909(5), s 915A(6)) and one more when the first design of `s 901G(2)` was run; each was a code fault (the `NOT` precedence, and a three-valued conjunction that turned an unknown condition into a no), and no expected value was edited to match the code. One expectation was changed together with its code by design, not to match a result: `s 901(3)` and its twin `s 901K(3)` first answered `JUST FALSE` where the effect of the order is already in the articles, and were changed to `JUST TRUE` (the "unless" exception is met, so nothing more is required) when the seat question showed that one word was carrying two meanings (fork F10); the test beside it says so.

## Open questions for a domain expert

- Is a failed "if" or "where" a no in each place the marginal-readings table lists (reading (a)), and is "limited by its own wording" a not-covered (reading (b))?
- s 901G(2): when condition A or B is not met, is the dissent merely "not prevented from preventing" the court (so NOTHING), or does it prevent (so JUST FALSE as encoded)?
- Forks F34 to F38 (listed, not flipped by the name-test sweep): for a function named for a power and gated by "where" (ss 900(2), 901J(2), 935(1)), does the ruling on "where" (`JUST FALSE`) or the Guide's line on grants (`NOTHING`) govern; and is an "entitled" claim (ss 897(4), 901D(4)) a power?
- Fork F6: how is a month counted ("one month before" a meeting date)? The Interpretation Act 1978 is outside the sources.
- Fork F4: should the court's satisfaction be a conjunct of the exemption (as encoded), or left to the person's wording?
- s 903(1): does a requirement that "does not apply" count as no bar (as encoded)?

## Copied modules

None.

## peeked

Nothing outside `INPUTS_DIR`, the two skills and their references, the Commons guide copies in `inputs/`, my own deposit and scratch, and the supplied binaries was opened. No existing encoding of any Act, no directory under `runs/` other than `dst-coa20/`, and nothing under `<local tool>` was read.
