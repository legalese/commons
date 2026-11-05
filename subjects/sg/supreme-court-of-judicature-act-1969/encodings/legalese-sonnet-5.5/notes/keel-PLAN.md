# PLAN.md: how the three parts divide the Supreme Court of Judicature Act 1969 (Singapore), and what they share

Status (checked 2026-11-05 on main build 1.6.109 and main build 1.6.108): `scja-core.l4` (297 lines) and `scja-core-tests.l4` (23 assertions) compile with no error or warning on both builds; `check.sh` prints the same four counts on both (NOTES.md has the table). Everything below about the SECTIONS, SEAMS and READING ORDER was read from `SCJA1969.txt` by the keel and is a plan, not a ruling: a part that finds a seam wrong says so in its own NOTES.md.
The source is a plain-text rendering of the 2020 Revised Edition, informal consolidation "version in force from 1/7/2024" (line 16). It is not the official text; no file in this row claims to have been checked against the official text.

## What the keel wrote, and what it did not

| file | what |
| --- | --- |
| `scja-core.l4` | The shared nouns: DECLARE and the Act's own figures and dates. No rule. Imports `prelude` and `daydate` only. Read-only for every part. |
| `scja-core-tests.l4` | 23 assertions on the core's figures, dates and record shapes, expected values written from the text. |
| `PLAN.md`, `NOTES.md`, `PROGRESS.md` | This plan; the keel's notes (coverage of lines 1-45, fork register, jural relations); the keel's log. |
| `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` | Descriptor, the subject's licence note, and the scripts. |

**No `scja-definitions.l4` was written, on purpose.** The keel's range (lines 1-45) holds the cover page, the consolidation banner, the running title and the first 24 lines of the Arrangement of Sections; it holds no definition. Section 2 (Interpretation, lines 378-433) lies in `scja1`'s range, so `scja1` encodes it, with the function names `s 2 ...` that the naming rule below gives it. A keel module that also encoded section 2 would define the same names twice. Every other definition in the Act is also in a part's range (list under each part).

## Naming rules every part follows (verbatim from the brief)

- A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name. Every top-level name (function, constant, type constructor not in the core) a part defines **begins with the section label it implements, in the form `s 4(2)(a) ...`** (the Act's own numbering: `s 2014(d) a household with an elderly member`, `sch 3 para 2 the amount is reduced`; parentheses inside a backtick name parse fine on your main binary). Types and constructors shared across parts live only in the core.
- A part may not edit the core and never waits for it. If a part needs a type or constructor the core lacks, it defines it in its own module under its own prefix, records it in `NEEDS-CORE.md` in its sandbox, and the lead hoists it into the core at the merge.
- File names: every module of part `X` begins with `X-` (the part's id), and every module of yours begins with `scja-`.

Two additions the keel makes, both measured:

1. **Schedule labels.** Write a Schedule's names as `sch 3 para 1(a) ...` (a Schedule number, then `para`), the form the brief gives. The core's own names begin with `the Act's ...` or are type names, so they cannot collide with a section-label name.
2. **Names that a part must not define because a module it may copy already does.** `inputs/DEPENDENCIES/sg-interpretation-act/sgia-interpretation-time.l4` and `sgia-p1-definitions.l4` define these types and constructors, and the core avoids all of them (checked: the core, `sgia-interpretation-time` and `sgia-p1-definitions` import together in one file with no "multiple definitions" error): `Moment`; `Period unit` with `Days`, `Weeks`, `Months`, `Years`; `Counting word` with `From`, `After`; `Reach of section 50(b)` with `every period`, `periods of days only`; `How the day of commencement is fixed` with its three constructors; `Provision and its day`; `Time for doing a thing` with its one constructor; `Kind of definition` with `Means`, `Includes`, `Means and includes`, `Has the meaning given by another law`, `Depends on where it is made`, `Rule of reading`; `Definition`. A part that copies either module (see "Periods" below) must not declare any of these.

## The core, name by name

| core name | what it holds | who is expected to use it |
| --- | --- | --- |
| `Court` | GD, SICC, Family Division, AD, CA, District, Magistrate's, Family, Youth, Syariah, other subordinate body | all three |
| `Manner of hearing` | open court, private, video / television / audio-only link, asynchronous written, without oral arguments | scja1 (ss 8, 8A, 17B, 22A), scja2 (ss 37, 55) |
| `Jurisdiction exercised`, `Nature of the proceeding` | original / appellate / supervisory; civil / quasi-criminal / criminal | scja1 (ss 15-29E), scja2 (ss 35, 53, 60D), scja3 (Schedules 3-6, 9) |
| `Kind of Judge`, `Judge`, `Bench`, `Split of opinion`, `Hearing` | who sits, in what office, since when; how they divided; the facts ss 8A(3), 10, 17B, 18H, 22A, 32, 36, 37, 50, 54, 55 turn on | scja1, scja2 |
| `Smaller panel` | a single Judge; a single Judge or 2 Judges; 2 Judges | scja2 (ss 36(1), 54(1), 60E(1)), scja3 (Seventh and Tenth Schedules) |
| `Role`, `Person` | claimant ... assessor; a person with roles, Muslim status, citizenship | scja1 (ss 8(5), 13, 15, 17A, 18M, 22), scja2, scja3 (ss 73A-74) |
| `Officer of the Supreme Court` | Registrar ... other officer | scja2 (Part 6), scja3 (ss 73, 75-79), scja1 (s 2 "Registrar") |
| `Subject of the case` | divorce, admiralty, bankruptcy, ... , patents, elections, `any other civil matter` | scja1 (ss 17, 17A, 18D, 28A, 29D), scja3 (Fifth and Sixth Schedules) |
| `Subject of an order or application`, `Way an order went`, `Order`, `Decision` | what a decision is about, how it went, and the facts ss 21, 29, 29A, 29B, 46, 47 and the Third, Fourth, Fifth, Seventh and Ninth Schedules turn on | scja1, scja2, scja3 |
| `the Act's figure for s 21(1)(a)` (60000), `... s 29A(1)(b)` (250000), `the Act's number of days for s 29B(2)(b)` (15), `... ss 41(10)(b) and 59(10)(b)` (7), `the Act's number of years for ss 73C(4)(a) and 73D(4)(a)` (2) | the Act's own printed figures | scja1, scja2, scja3 |
| `the day the Act was brought into operation` (9 Jan 1970), `the day the text is in force from` (1 Jul 2024), `the day before which a registered Muslim divorce counts under s 17A(3A)` (1 Mar 2009), `the day before which the Companies Act 1967 is read under s 18D(2)(c)` (30 Jul 2020) | the Act's own printed dates | scja1, scja3 (s 80(2A)(c)(ii)) |

Things the core deliberately does not hold: any answer to "does permission lie", "which court hears it", "may the court do X". Those are rules and live in the parts. Figures the Minister or President may replace by order (`s 21(3)`, `s 29A(3)`, `s 83`) are the Act's printed figures only; a part asks the substituted figure as an input and records that a substitution changes its answers.

A decision with no amount or value in dispute carries `NOTHING` in the amount field of `Decision`: the Act does not say what an unvalued case counts as for `s 21(1)(a)` or `s 29A(1)(b)`, so a part answers `NOTHING` there, not `FALSE`.

## Part 1: `scja1`

Range, copied unchanged from `inputs/PARTS.md`: **lines 46-2309** (11403 words). Files begin `scja1-`.

Covers: the rest of the Arrangement of Sections (lines 46-371, inert: headings) and the long title and enactment date (lines 365-370, inert: not operative; the date is a core constant); Part 1 (ss 1-2); Part 2 (ss 3-8A); Part 3, Divisions 1-9 (ss 9-29E). Section start lines: 1@375, 2@378, 3@448, 4@456, 5@481, 5A@498, 6@506, 7@514, 8@521, 8A@691, 9@767, 10@771, 10A@852, 10B@885, 11@905, 12@914, 13@923, 14@956, 15@994, 16@1029, 17@1056, 17A@1109, 17B@1236, 17C@1263, 18@1295, 18A@1317 ... 18M@1656, 19@1675, 20@1702, 21@1719, 22@1759, 22A@1821, 22B@1853, 23@1886, 24@1903, 25@1913, 26@1923, 27@1930, 28@1973, 28A@1988, 28B@2033, 29@2042, 29A@2064, 29B@2122, 29C@2186, 29D@2206, 29E@2262.
Repealed in this text (disposition `repealed or blank in this text`): ss 9 (line 767), 12 (914), 18E (1479), 28B (2033).
**Definitions that sit in this range and are this part's to encode** (the keel encodes none): s 2 "Appellate Division", "court", "Family Division of the High Court", "Family Justice Rules", "General Division", "Judge" (limbs (a)-(c)), "Registrar", "Rules of Court", "seal", "subordinate court", "Supreme Court Judge" (lines 378-433); s 8(7) "broadcasting service", "newspaper"; s 17(2); s 17A(9) and (3A); s 17C(3); s 18J(4); s 22B(3). Section 2 opens "unless the context otherwise requires": record that as a fork (phrasebook 1.5).
Core names to expect: `Court`, `Manner of hearing`, `Jurisdiction exercised`, `Nature of the proceeding`, `Kind of Judge`, `Judge`, `Bench`, `Split of opinion`, `Hearing`, `Role`, `Person`, `Subject of the case`, `Subject of an order or application`, `Way an order went`, `Order`, `Decision`, `Officer of the Supreme Court` (s 2 "Registrar"), the figures for ss 21(1)(a), 29A(1)(b), 29B(2)(b), and the dates for ss 17A(3A) and 18D(2)(c).

## Part 2: `scja2`

Range, copied unchanged: **lines 2310-4320** (10212 words). Files begin `scja2-`.

Covers: Part 4, the Appellate Division (ss 30-47); Part 5, the Court of Appeal, Divisions 1-4 (ss 48-60M: general, civil, criminal, and the post-appeal application in a capital case); Part 6, officers and offices (ss 61-72). Section start lines: 30@2318 ... 47@2819, 48@2880 ... 60E@3424, 60F@3462, 60G@3605, 60H@3751, 60I@3827, 60J@3869, 60K@3924, 60L@3931, 60M@3940, 61@4065 ... 72@4300.
Definitions in this range: s 60F (a whole definitions section: "application for PACC permission", "application for review permission", "counsel", "Judge of the Court of Appeal", "PACP", "post-appeal application in a capital case", "President's order", "relevant application", "relevant date", "review application", with its Examples); the "(called in this section ...)" definitions in ss 40(1), 58(1), 60I(1) and 60J(1).
Core names to expect: `Court`, `Bench`, `Hearing`, `Judge`, `Kind of Judge`, `Split of opinion`, `Smaller panel`, `Manner of hearing`, `Decision`, `Order`, `Subject of an order or application`, `Role`, `Person`, `Officer of the Supreme Court`, the number of days for ss 41(10)(b) and 59(10)(b).
The seat is civil; Part 5 Divisions 3 and 4 (criminal and capital) are in range and are covered like every other row: encode them for the accused or prisoner as the individual the court acts on, with no seat export.

## Part 3: `scja3`

Range, copied unchanged: **lines 4321-7314** (15628 words). Files begin `scja3-`.

Covers: Part 7 (ss 73-83); the First to Tenth Schedules (lines 5462-6585; the Eighth is repealed, line 6485); the Legislative History (lines 6587-7314), which says of itself "It is not part of the Act" (line 6592): `inert`, reason 1. Section start lines: 73@4330, 73A@4382, 73B@4500, 73C@4581, 73D@4674, 74@4772, 75@4841, 76@4876, 77@4885, 78@4891, 79@4940, 80@5022, 81@5345, 82@5376, 83@5435. Schedule start lines: First 5462, Second 5716, Third 5784, Fourth 5830, Fifth 5956, Sixth 6172, Seventh 6270, Eighth 6483, Ninth 6487, Tenth 6542.
Definitions in this range: s 74(5) "legal proceedings"; Fifth Schedule para 1 "appellate court"; First Schedule paras 21(2) "family support programme or activity" and 23(2) "amicable resolution"; s 80(3) (the Rules Committee is constituted by the list there).
The Schedules are data (phrasebook 1.10: one named item per paragraph, gathered into a `LIST`, then the operative test as a membership test). Several Schedules are "listed in Schedule N" lookups: the brief's question QC governs how a failed membership answers, decided case by case.
Core names to expect: `Court`, `Decision`, `Order`, `Subject of an order or application`, `Way an order went`, `Subject of the case`, `Smaller panel`, `Jurisdiction exercised`, `Nature of the proceeding`, `Role`, `Person`, `Officer of the Supreme Court`, the number of years for ss 73C(4)(a), 73D(4)(a), and the figures for ss 21(1)(a) and 29A(1)(b) (the Third and Fifth Schedules repeat the cases those sections send to them).

## Seams

A part cannot import another part, so each seam below is an INPUT of the asking function, named for the section that answers it. **Every seam whose answering section can say `NOTHING` is typed `MAYBE ...`, and the asking function passes `NOTHING` through: a caller never turns `NOTHING` into `FALSE` (rule of 2026-10-29).** The names are the exact `GIVEN` names the asking function uses; the lead connects each to the answering function at the merge.
Verified recipe (main 1.6.109, 4 assertions satisfied, run in a scratch copy of the core):

```
GIVEN `sch 3 the decision is a case specified in the Third Schedule` IS A MAYBE BOOLEAN
GIVETH A MAYBE BOOLEAN
`s 21(1) permission is needed` MEANS
    CONSIDER `sch 3 the decision is a case specified in the Third Schedule`
    WHEN JUST TRUE THEN JUST TRUE
    WHEN JUST FALSE THEN NOTHING     -- which side is NOTHING or JUST FALSE is the part's judgment call, not this recipe's
    WHEN NOTHING THEN NOTHING
```
Parenthesise a call that is compared: `#ASSERT (f NOTHING (JUST TRUE)) EQUALS JUST TRUE` (without the brackets the type-checker reports a `MAYBE` where a `BOOLEAN` was expected).

| # | asking section (part) | answering section (part) | input name | type |
| --- | --- | --- | --- | --- |
| 1 | s 18(2) (scja1) | First Schedule, paras 1-23 (scja3) | `sch 1 the power is one set out in the First Schedule` | MAYBE BOOLEAN |
| 2 | s 18I(1)(a) (scja1) | First Schedule para 1 (scja3) | `sch 1 para 1 the power is the power under paragraph 1` | MAYBE BOOLEAN |
| 3 | s 21(1)(b) (scja1) | Third Schedule (scja3) | `sch 3 the decision is a case specified in the Third Schedule` | MAYBE BOOLEAN |
| 4 | s 29(b) (scja1) | Fourth Schedule, with its exceptions (scja3) | `sch 4 the Fourth Schedule says no appeal can be brought` | MAYBE BOOLEAN |
| 5 | s 29A(1)(b) (scja1) | Fifth Schedule, paras 2(2) and 4(2) (scja3) | `sch 5 an exception in the Fifth Schedule takes the case out of s 29A(1)(b)` | MAYBE BOOLEAN |
| 6 | s 29A(1)(c) (scja1) | Fifth Schedule, paras 3, 4(1), 5(1) and their exceptions (scja3) | `sch 5 the case is one specified in paragraph 3, 4(1) or 5(1) of the Fifth Schedule and no exception applies` | MAYBE BOOLEAN |
| 7 | s 29A(2)(b) (scja1) | Fifth Schedule, para 1 (scja3) | `sch 5 the court from which permission must be obtained` | MAYBE `Court` |
| 8 | s 29C(2) (scja1) | Sixth Schedule, para 1 (scja3) | `sch 6 the appeal is to be made to the Court of Appeal` | MAYBE BOOLEAN |
| 9 | Fifth Schedule para 1; ss 73A(9), 73B(5), 73C(6), 73D(6), 74(2A) (scja3) | s 29C (scja1) | `s 29C the court to which the appeal is to be made` | MAYBE `Court` |
| 10 | Fifth Schedule para 2(1) (scja3) | s 29A(1)(b) (scja1) | `s 29A(1)(b) the amount in dispute or value of the subject matter does not exceed the sum` | MAYBE BOOLEAN |
| 11 | s 8A(6) (scja1) | ss 34(1)(a), 52(1)(a) (scja2); s 11(1) (scja1) | `s 34(1)(a) or s 52(1)(a) the place is one the Chief Justice appointed` | MAYBE BOOLEAN |
| 12 | ss 30(3)(a), 48(2)(a) (scja2) | s 4 (scja1) | `s 4 the most senior Supreme Court Judge among those sitting` | MAYBE `Judge` |
| 13 | ss 32(3), 50(3) (scja2) | s 10A (scja1) | `s 10A the court may summon assessors` (scja1 writes s 10A with `the court` as an input of type `Court`, so the lead can call it with `Appellate Division` and `Court of Appeal`) | MAYBE BOOLEAN |
| 14 | ss 36(1), 54(1) (scja2) | Seventh Schedule (scja3) | `sch 7 the smaller panel the Seventh Schedule allows` | MAYBE `Smaller panel` |
| 15 | s 46 (scja2) | Ninth Schedule (scja3) | `sch 9 the Appellate Division decision is a case specified in the Ninth Schedule` | MAYBE BOOLEAN |
| 16 | s 60E(1) (scja2) | Tenth Schedule (scja3) | `sch 10 the smaller panel the Tenth Schedule allows` | MAYBE `Smaller panel` |
| 17 | s 65A(2) (scja2) | s 79(2) (scja3) | `s 79(2) the officer is not liable to be sued` | MAYBE BOOLEAN |
| 18 | s 69(1) (scja2) | Second Schedule (scja3) | `sch 2 the oath taken is the appropriate oath of office set out in the Second Schedule` | MAYBE BOOLEAN |
| 19 | s 47(4)(b)(i), (ii) (scja2) | ss 29E(1), 29D(1) (scja1) | `s 29E(1) the appeal was transferred to the Appellate Division`, `s 29D(1) the Court of Appeal declined to transfer the appeal to itself` (facts a party can state) | BOOLEAN each |
| 20 | ss 35(2)(b), 53(2)(c) (scja2) | ss 29D(1), 29E(1) (scja1) | `s 29D(1) the appeal was transferred to the Court of Appeal`, `s 29E(1) the appeal was transferred to the Appellate Division` (facts) | BOOLEAN each |

Not seams, and why (so no part spends time looking for them):

- Rule-making and prescribing powers ("as prescribed by Rules of Court", "the Family Justice Rules", "the Criminal Procedure Rules", ss 8A(1), 8A(3)(c), 10A, 16, 17B, 17C(1)(b), 18D to 18M, 22A, 22B, 29D(3), 37, 38, 47(3), 55, 56, 60G(3)-(5), 80(2)-(2B)): each is machinery (reason 2) or an outside fact, asked as a plain input such as `the matter is prescribed by the Rules of Court`. Section 18C's "Subject to sections 18D to 18M and 80(2A)" points at rule-making powers and adds no seam.
- Other Acts (Administration of Muslim Law Act 1966 in s 17A, Criminal Procedure Code 2010 in Part 5, Legal Profession Act 1966, Mediation Act 2017, Land Acquisition Act 1966, Protection from Online Falsehoods and Manipulation Act 2019 in the Fifth and Sixth Schedules): not staged; take the borrowed fact as an input citing the section.
- Seventh, Ninth and Tenth Schedules name ss 32(1), 40(1), 50(1), 58(1), 29D and 29E: the fact "this is an application under s 40(1) or 58(1)" is the core constructor `an incidental direction or interim order under section 40(1) or 58(1)` of `Subject of an order or application`; the Schedules' "despite section 32(1)" is a statement scja3 encodes on its own and scja2 encodes the section it modifies.
- Fourth Schedule para 4(1)(g) names Fifth Schedule para 3(i): both are scja3, no seam.

## Twins: the Act says the same thing more than once

Encode each section's answer on its own (ruling E1, option C), with the wording kept alike so the lead can compare them. Each pair is a duplication the keel did not remove:
oral hearing not needed: ss 17B (GD, original), 22A (GD, appellate), 37 (AD), 55 (CA); summary dismissal: ss 17C, 22B, 38, 56; rehearing and further evidence: ss 22, 41, 59; new trial: ss 43, 60A; immaterial errors: ss 44, 60B; no stay: ss 45, 60C; costs: ss 42, 60; applications: ss 39, 57; incidental directions and interim orders: ss 40, 58; composition, decisions and sittings: ss 32-34 and 50-52; jurisdiction and presidents: ss 30-31 and 48-49; the three civil restraint orders: ss 73B, 73C, 73D; permission to appeal after a restraint order: ss 73B(5)-(6), 73C(6)-(7), 73D(6)-(7).
The power to refer or transfer an appeal appears in s 29D(2)(b) (scja1) and Seventh Schedule para 1(2)(a) (scja3), and in s 29D(1) / 29E(1) and Seventh Schedule para 3(2): same power, stated from the panel's side in the Schedule.

## Difficulties the parts will meet

1. **"General Division" and the Singapore International Commercial Court.** The SICC is "a division of the General Division" (s 18A, line 1317); the Act applies to it "as they apply to proceedings in the General Division exercising its original civil jurisdiction" (s 18C); and s 18J(4) says "'General Division' does not include the Singapore International Commercial Court" for that section. The core keeps the SICC as its own `Court` constructor so a fact can say which court made a decision; each section that says "General Division" is a fork for its part (does the SICC count?), recorded with the text that licenses each reading. The Family Division of the High Court is likewise its own constructor (Fourth Schedule para 2, Fifth Schedule paras 2(2)(b), 4, 5).
2. **The Act sets almost no time limit that a party can count.** The time for a notice of appeal is in the Rules of Court (outside the sources); s 29B(4)(b) only says when that time "begins". The periods the Act itself sets are: s 7 vacations "must not exceed 2 months in any year" (line 515); s 29B(2)(b) "the 15th day after the date on which the decision is made" (line 2139); ss 41(10)(b) and 59(10)(b) "the expiration of 7 days after the date on which the decision ... is made" (lines 2714, 3283); ss 73C(4)(a) and 73D(4)(a) "not exceeding 2 years", ss 73C(5)(b) and 73D(5)(b) "must not extend that period for more than 2 years on any given occasion"; s 10B(1) the General Division sits every day except Saturdays, Sundays and public holidays. `inputs/DEPENDENCIES.md` stages the Interpretation Act time module for these. **Periods:** copy `sgia-interpretation-time.l4` UNCHANGED from `inputs/DEPENDENCIES/sg-interpretation-act/` into your sandbox only when a provision of yours counts a period or a day (ss 10B, 29B, 41, 59, 72, 73C, 73D), `IMPORT` it by name, and do not declare any name in the reserved list above. Its `the last day of a period` answers `NOTHING` for the counting word `After` and for weeks, months and years, because the Interpretation Act has no counting rule for them (read at lines 223-232 of the staged module); ss 41(10)(b) and 59(10)(b) say "7 days after the date" and s 29B(2)(b) says "the 15th day after the date", so read what the module gives for each before relying on it, and say in the fork register what you took (rulings of 2026-11-05: a period the text fixes in its own words answers `JUST FALSE` outside it; a result that is a date and cannot carry `JUST FALSE` gets a yes/no twin). The Rules of Court count their own periods, but they are not among the sources.
3. **Most provisions leave a judgment to a court, a Judge, the Chief Justice, the Registrar, the Minister or the Rules of Court.** "If it thinks fit", "if satisfied", "as the court thinks fit", "for other sufficient reason", "extremely urgent" (ss 8(2), 10A(1), 10B(2)(b), 17C(1), 22B(1), 27(2), 28A(1), 29B(2), 38, 56, 73A to 74): take the judgment as a plain input ("X, if the court is satisfied that ...", phrasebook 8.4 and 8.5), never guess it.
4. **Powers of the General Division in the First Schedule** (23 paragraphs) are a list of powers, not duties on an individual: encode what each means for the person (what may be ordered against them), per the seat rule, and use the core nouns `Order` and `Subject of an order or application` where a paragraph names an order the Third to Ninth Schedules also mention.
5. **Page furniture.** Lines such as `Informal Consolidation – version in force from 1/7/2024`, `Supreme Court of`, `2020 Ed. Judicature Act 1969 14`, and amendment tags (`[40/2019]`, `[Act 25 of 2021 wef 01/04/2022]`) sit between provisions and inside them; they are not provisions. The tags do not change the text, which is the consolidation in force from 1 July 2024: no part has two vintages to merge.
6. **A letter in a section number** (`5A`, `10A`, `18A`-`18M`, `22A`, `28A`, `29A`-`29E`, `60A`-`60M`, `65A`, `73A`-`73D`) is the Act's own label; use it as printed in `s 29A(1)(b) ...`.
7. **One shared fact the core does not hold:** "every issue in the appeal has already been decided ... in an earlier matter in which the appellant was involved, and the appeal therefore has no merit" is a ground in ss 17C(1)(a) (scja1), 22B(1)(b) (scja1), 38(1)(b) (scja2) and 56(1)(b) (scja2). Each part takes it as a plain `BOOLEAN` input whose name begins with its own section label (for example `s 38(1)(b) every issue was already decided in an earlier matter involving the appellant`), and records it in `NEEDS-CORE.md`; the lead may hoist one shared field into `Hearing` at the merge. Its courts differ (ss 17C, 22B: the General Division, the Appellate Division or the Court of Appeal; s 38: the Appellate Division or the Court of Appeal; s 56: the Court of Appeal), so one input per section is the safe shape.
8. **Run each part's own `check.sh`** with `L4=<L4_BIN> L4_MAIN=<the 108 build> ./check.sh` and `python3 -I srcrefs.py check --refs <SCJA1969.txt> <your .l4 files>`; the core and its tests are the keel's and are not in a part's count.

## What the lead does at the merge

Hoist what each `NEEDS-CORE.md` lists into `scja-core.l4` (keeping to the reserved-name list), connect the 20 seams above to the answering functions, copy the staged Interpretation Act modules once, and merge the three `NOTES.md` files with the four ruling bullets (E1, N2, periods, delegated definitions) once. The keel's own `NOTES.md` carries those bullets word for word.
