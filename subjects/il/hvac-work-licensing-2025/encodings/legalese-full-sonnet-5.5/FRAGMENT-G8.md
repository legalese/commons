# FRAGMENT-G8: the Fees Regulations in three vintages and the SimpLEX test table

Status: draft, written by the G8 encoder on 2026-10-13; no domain expert has read it against the sources.
Every claim below was checked against the modules in `deposit/` on the day it was written, by the commands named in section 10.
Nothing here is ruled by the owner: each reading below is the encoder's, marked "assumed, not ruled", and each has a callable alternative unless it says why not.
The INTEGRATOR merges this file into `NOTES.md`.

Scope: Fees Regulations regs 1 to 5 (as made, Kovetz HaTakanot 11951, 9 July 2025), the amending regulations (Kovetz HaTakanot 12383, 4 May 2026), regs 1 and 2 of the SimpLEX draft (Figure 4, screenshot only), and the four SimpLEX test rows 5 to 8 with the worked example.
Module prefix `g8-`.
The modules import each other (see section 5, "Module order"); they import nothing from another group.

How the encoding is organised, in four lines.
The vintage is an input of every lookup (`Vintage of the Fees Regulations`), and a vintage silent on a head of section 59 answers NOTHING, never a figure from another vintage.
Regulation 3 (update of fees) is a chain of rounded updates over index readings that the caller supplies, and without them the answer is a named refusal.
Regulation 4 is two typed prohibitions (the Registrar; the Training Division) with a boolean test that G1 and G2 consume.
The SimpLEX table is run as three separate claims per case (the outcome, the amount, the cited provision) against each vintage; the claims the text does not meet are in `g8-tests-red.l4`, counted.

## 1. Coverage

34 rows, in the Fees Regulations' own numbering (`R` = regulation, `AM` = the amending regulations, `D` = the SimpLEX draft, `DT`/`DX` = the test table).
31 `encoded`, 3 `inert`, 0 `refused`, 0 `out-of-scope`, 0 `deferred`.
No disposition was changed from `slice-G8.md`.
The modules differ from the slice's plan in three ways: `g8-fees-nouns.l4` was added (the shared nouns of the group, DECLARE only); regulations 3 to 5 of the text as made live in `g8-fees-as-made.l4`, because the amended vintage reuses them and cannot import `g8-fees.l4`; and `g8-fees.l4` holds the vintage-keyed layer.
The Hebrew column is the surveyor's script-copied excerpt from `phase1/coverage.tsv`; none is typed here.

| id | provision | Hebrew (script-copied by the surveyor) | disposition | module | rule or rules |
| --- | --- | --- | --- | --- | --- |
| Rpre | preamble | בתוקף סמכותי לפי סעיפים 59 ו־60 לחוק הסדרת … | inert | g8-fees-as-made | `the sections of the Law under which the Fees Regulations are made` carries the quotation of the preamble; no rule turns on the two approvals |
| R1 | regulation 1 | בתקנות אלה, | inert | g8-fees-as-made | the lead-in is quoted above regulation 1 (src:fees:17); the definitions have their own rows |
| R1/def1 | regulation 1, definition 1 | ”בחינה מעשית“ – בחינה להערכת הידע והמיומנויות המעשיות … | encoded | g8-fees-as-made, g8-fees-as-amended, g8-fees-draft | `as made, regulation 1 — the exam is a practical exam`; `as amended, regulation 1 — the exam is a practical exam`; `the SimpLEX draft, regulation 1 — the exam is a practical exam` |
| R1/def2 | regulation 1, definition 2 | ”בחינה עיונית“ – בחינה להערכת הידע וההבנה העמוקה … | encoded | g8-fees-as-amended, g8-fees-as-made, g8-fees-draft | `as amended, regulation 1 — the exam is a theoretical exam`; as made: the named refusal `the Fees Regulations as made define no theoretical exam`; `the SimpLEX draft, regulation 1 — the exam is a theoretical exam` |
| R2 | regulation 2 | אגרות | encoded | g8-fees-as-made, g8-fees-as-amended, g8-fees | `the Fees Regulations as made state, for the service`; `the Fees Regulations as amended state, for the service`; `the Fees Regulations state in` v `, for the service` s; exports `the amount the Fees Regulations state in` v `for the service` s and `the fee under the Fees Regulations in the vintage for the service on the day` |
| R2(a) | regulation 2(א) | בעד בחינה מעשית, ישלם הנבחן אגרה בסכום של … | encoded | g8-fees-as-made | `as made, regulation 2(a) — the fee for a practical exam` (NIS 194, payer the examinee) |
| R2(a1) | regulation 2(א1) | בעד בחינה עיונית, ישלם הנבחן אגרה בסכום של … | encoded | g8-fees-as-amended | `as amended, regulation 2(a1) — the fee for a theoretical exam` (NIS 158) |
| R2(b) | regulation 2(ב) | הוגשה השגה על ציון הבחינה העיונית, ישלם מגיש … | encoded | g8-fees-as-made, g8-fees-as-amended, g8-fees | `as made, regulation 2(b) — the charge for an objection to the score of the exam`; `as amended, regulation 2(b) — the charge for an objection to the score of the theoretical exam` (and its alternative); `the amount due, reading the objection charge as` r `, in` v `for the objection` s `, the number of objections` n `, the fees being` f |
| R2(c) | regulation 2(ג) | בעד קבלת רישיון או חידושו לפי סעיף 5 … | encoded | g8-fees-as-made | `as made, regulation 2(c) — the fee for receiving a licence or renewing it` (NIS 284); alternative `the Fees Regulations as made state, reading regulation 2(c) as a fee on the application under section 5, for the service` s |
| R2(d) | regulation 2(ד) | בעד בקשה לקבלת רישיון זמני למומחה זר או … | encoded | g8-fees-as-made | `as made, regulation 2(d) — the fee for an application for a foreign expert's temporary licence or its renewal` (NIS 398) |
| R3 | regulation 3 | עדכון אגרות | encoded | g8-fees-as-made, g8-fees | regulation 3 as a set of rules in g8-fees-as-made (called under both vintages) and `the fee payable in` v `for the service` s `on the day` d `, under` ctx in g8-fees |
| R3(a) | regulation 3(א) | סכומי האגרות המפורטים בתקנה 2 יעודכנו ב־1 בינואר … | encoded | g8-fees-as-made | `regulation 3(a) — the update day of the year`; `... — the first update day after the commencement day`; `... — the year of the first update day after the commencement day`; `... — the calendar month before the month of`; `... — the readings published in`; `... — the rate of change on the update day of the year`; `... — rounded to the nearest whole new shekel, a half shekel being treated by`; `... — the year of the first update day that applies to the stated fee`; `regulation 3 — the update of the year` y `binds on` d; `regulation 3(a) — the amount of the stated fee` |
| R3(a)/def1 | regulation 3(א), definition 1 | ”המדד החדש“ – המדד שפורסם בחודש נובמבר שקדם … | encoded | g8-fees-as-made | `regulation 3(a) — the new index of the update day of the year` |
| R3(a)/def2 | regulation 3(א), definition 2 | ”המדד היסודי“ – המדד שפורסם בחודש נובמבר שקדם … | encoded | g8-fees-as-made | `regulation 3(a) — the base index of the update day of the year` (first update day: the month before the commencement; later: the November before the previous update day) |
| R3(a)/def3 | regulation 3(א), definition 3 | ”מדד“ – מדד המחירים לצרכן שמפרסמת הלשכה המרכזית … | encoded | g8-fees-as-made | the index is an input, domain `Price index reading`; `regulation 3(a) — the value of the one reading in` |
| R3(b) | regulation 3(ב) | המנהל הכללי של משרד העבודה יפרסם בהודעה ברשומות … | encoded | g8-fees-as-made | `regulation 3(b) — the Director General publishes the text of regulation 2 as changed` (MUST, no WITHIN: the text gives no time) |
| R4 | regulation 4 | הרשם לא ייתן רישיון שנקבעה בעדו אגרה לפי … | encoded | g8-fees-as-made, g8-fees | `regulation 4 — the bar applies to the service`; the four SHANT rules `regulation 4 — the Registrar and giving the licence`, `... and renewing the licence`, `regulation 4 — the Training Division and allowing the exam`, `... and allowing the objection`; in g8-fees `the service whose fee regulation 4 looks at, reading regulation 4 as` ..., `a fee is fixed under the Fees Regulations in` ..., `regulation 4 bars the service, reading regulation 4 as` ..., and the exports `regulation 4 does not bar the service in the vintage`, `regulation 4 leaves the Registrar free to give or renew the licence in the vintage`, `regulation 4 leaves the Training Division free to allow the exam or the objection in the vintage` |
| R5 | regulation 5 | תחילתן של תקנות אלה 7 ימים מיום פרסומן … | encoded | g8-fees-as-made, g8-fees | `the Fees Regulations as made were published on`; `the Fees Regulations as made came into force on` (and two alternatives); `the Fees Regulations as made begin to bind at`; export `the Fees Regulations made under section 59 came into force on` (IP13) |
| AM1 | amending regulations (12383), reg.1 | (amending regulations: the Hebrew is only in the bidi-scrambled gazette text layer, not quoted) | encoded | g8-fees-as-amended | `as amended, regulation 1 — the exam is a theoretical exam` |
| AM2(1) | amending regulations (12383), reg.2(1) | (amending regulations: the Hebrew is only in the bidi-scrambled gazette text layer, not quoted) | encoded | g8-fees-as-amended | `as amended, regulation 2(a1) — the fee for a theoretical exam` |
| AM2(2) | amending regulations (12383), reg.2(2) | (amending regulations: the Hebrew is only in the bidi-scrambled gazette text layer, not quoted) | encoded | g8-fees-as-amended | `as amended, regulation 2(b) — the charge for an objection to the score of the theoretical exam`; the lookup answers silence for an objection to a practical exam |
| AMc | amending regulations (12383), no commencement clause | (amending regulations: the Hebrew is only in the bidi-scrambled gazette text layer, not quoted) | encoded | g8-fees-as-amended | `the 2026 amendment of the Fees Regulations was published on`; `... came into force on` (Interpretation Ordinance s 17); `... begins to bind at` (Interpretation Law s 21) |
| D1 | SimpLEX draft, reg.1 | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 1 — the exam is a practical exam` and `... a theoretical exam` |
| D2(a) | SimpLEX draft, reg.2(a) | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 2(a) — the fee for a theoretical exam` (NIS 273) |
| D2(b) | SimpLEX draft, reg.2(b) | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 2(b) — the fee for a practical exam` (NIS 194) |
| D2(c) | SimpLEX draft, reg.2(c) | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 2(c) — the charge for an appeal on the exam` (NIS 40) |
| D2(d) | SimpLEX draft, reg.2(d) | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 2(d) — the fee for an application for a licence or its renewal` (NIS 284) |
| D2(e) | SimpLEX draft, reg.2(e) | (screenshot only; the Hebrew is not scripted) | encoded | g8-fees-draft | `the SimpLEX draft, regulation 2(e) — the fee for an application for a foreign expert's temporary licence or its renewal` (NIS 398) |
| DT5 | SimpLEX test table, row 5 | (screenshot only; the Hebrew is not scripted) | encoded | g8-simplex-table | `SimpLEX row 5`, run by `the vintage reproduces the outcome of the SimpLEX case` and its two siblings |
| DT6 | SimpLEX test table, row 6 | (screenshot only; the Hebrew is not scripted) | encoded | g8-simplex-table | `SimpLEX row 6` |
| DT7 | SimpLEX test table, row 7 | (screenshot only; the Hebrew is not scripted) | encoded | g8-simplex-table | `SimpLEX row 7, an appeal on the theoretical exam`; `SimpLEX row 7, an appeal on the practical exam` |
| DT8 | SimpLEX test table, row 8 | (screenshot only; the Hebrew is not scripted) | encoded | g8-simplex-table | `SimpLEX row 8, a practical exam`; `SimpLEX row 8, a theoretical exam` |
| DX | SimpLEX worked example | (screenshot only; the Hebrew is not scripted) | encoded | g8-simplex-table | `the SimpLEX worked example`; its Law premise: `the premise of the worked example holds in the enacted Law` (a named refusal) |
| DT-fees | SimpLEX second panel | (screenshot only; the Hebrew is not scripted) | inert | g8-simplex-table | no row of the second panel is visible in the screenshot; the header comment of g8-simplex-table says so |

## 2. Forks

Every fork names its kind of period where it is about time, the readings with the text that licenses each, the reading taken, and the callable alternative with its test.
"Assumed, not ruled" means the encoder chose it where the text does not settle it.
"IL s.10(c)" is the Interpretation Law's rule on days of rest; the Law's own s.10(c) is not meant anywhere here.
Tests named below are modules in `deposit/`: `fees` is `g8-tests-fees.l4`, `reg3` is `g8-tests-reg3.l4`, `reg4` is `g8-tests-reg4.l4`, `dates` is `g8-tests-dates.l4`, `simplex` is `g8-tests-simplex.l4`, `red` is `g8-tests-red.l4`.

| id | fork | readings and the text that licenses each | taken (assumed, not ruled) | callable alternative and its test |
| --- | --- | --- | --- | --- |
| F1 | vintage silence (T38) | as made prices no theoretical exam; as amended prices no objection to a practical score; the draft shows no regulations 3 to 5; s.59 lists nine heads of fee and each vintage prices some | silence is NOTHING (a head) or a named refusal (a regulation not visible); no figure crosses vintages | none: the brief forbids borrowing; the silence is asserted for every head of every vintage in `fees` (146 assertions) |
| F2 | "in addition to the payment of the fee as stated in sub-regulation (a)" (T33) | (I) the objection charge alone, NIS 40 per objection: the objector is not the examinee and the exam fee was paid when the exam was taken; (II) the exam's own fee, then 40 per objection: "added to the payment" can mean a fresh payment; (II-literal) the fee of whichever sub-regulation (a) is | I, which is what SimpLEX row 7 expects | `the amount due, reading the objection charge as` r `...` with r = the other two readings; `reg3` section "Regulation 2(b)"; `simplex` section "an objection costs the exam fee as well" |
| F3 | "the exam" in regulation 2(b) as made | the one exam the regulations define (the practical exam; (a) is its fee) or any exam | the practical exam only | `the Fees Regulations as made state, reading "the exam" in regulation 2(b) as` `the exam is any exam` `...`; `reg3`, last section |
| F4 | whether the wiki's "(adjusted to 2025)" and "(adjusted to 2026)" notes are law | the notes are the wiki editor's (the gazette pages carry none); so the printed figures are the figures of the gazette | the printed figures take effect on the day their provision commenced and are updated from the first 1 January after it (reg.3(a)) | `the amount the Fees Regulations state in` v `for the service` s (the printed figure, never updated) against `the fee payable in`; `reg3` first sections show 194 and 196 |
| F5 | reg.3(a) "the base index" of the first update day: "the index published in the month before the commencement" | the reading PUBLISHED in June 2025 (the text says "published in the month"); or the reading RELATING to June 2025 | published in the month (T37) | `the reading of regulation 3 that takes the index relating to the month before the commencement`; `reg3` section "Alternative readings" |
| F6 | reg.3(a) "rounded to the nearest whole new shekel" at an exact half | up; to the even shekel; down | up | `the reading of regulation 3 that rounds a half shekel to the even shekel`, `... down`; `reg3` (40 x 1.0125 = 40.5: 41, 40, 40) |
| F7 | when the rounding is done | after every update day (each year's amount is a text the Director General republishes under (b)); or once after the last | after every update day | `the reading of regulation 3 that rounds once, after the last update day`; `reg3` (194 on 1.1.2027: 198 against 199) |
| F8 | the first update day of an amount that took effect after the regulations commenced (158, and the narrowed 2(b)) | the first 1 January after the amount took effect; or the principal regulations' first update day | after the amount took effect | `the reading of regulation 3 that updates a later amount from the first update day of the regulations`; `as amended, regulation 2(b) ..., taken as a new provision from the day of the amendment`; `reg3` |
| F9 | from when an update binds (reg.3(a) "shall be updated on 1 January", (b) "shall publish") | its update day; or the day of the Director General's notice | the update day | `the reading of regulation 3 that lets an update bind from the Director General's notice`; `reg3` (194 until 19.2.2026, 196 from 20.2.2026) |
| F10 | is the objection charge "a fee" that reg.3(a) updates (T36) | reg.2(b) says "an amount of NIS 40", where (a), (c), (d) say "a fee of"; reg.3(a) updates "the amounts of the fees specified in reg.2" | updated like the rest | `the reading of regulation 3 that leaves the objection charge as printed`; `reg3` (40 on 1.1.2026: 41 against 40) |
| F11 | reg.3(a) "the commencement day of these regulations" in the amended text | the principal regulations (16.7.2025); or the amending regulations (4.5.2026) | the principal regulations | an `Inputs of regulation 3` whose commencement is `the 2026 amendment of the Fees Regulations came into force on`; `reg3` last open-question section (158 on 1.1.2027: 160 against 162) |
| F12 | reg.4 where the vintage fixes no fee for the service (the discriminator of T34) | the bar speaks of a service "for which a fee was fixed": none was, so it is not engaged; or the answer is a refusal | not engaged | `the reading of regulation 4 that refuses where no fee is fixed`; `reg4` section "A service for which no fee is fixed" |
| F13 | reg.4 first limb and a temporary licence (repaired after the independent test author's finding DIS-4) | the fee 2(d) is fixed for the APPLICATION; the bar speaks of "a licence for which a fee was fixed"; s.59 prices the grant of a temporary licence separately and no vintage does | the fee fixed for the application binds the grant, whether the Registrar is asked about the application or about the grant itself (the first version answered "free" when asked about the grant) | `the reading of regulation 4 that binds a temporary licence only by a fee fixed for the licence`; `reg4` section "A temporary licence" (the grant: nothing paid, 397, 398, 400, as made and as amended; the mapping `the service whose fee regulation 4 looks at, reading regulation 4 as` r `, the service` s; the alternative leaves the grant free) |
| F14 | reg.4 "paid the fee in full" | at least the fee; or exactly the fee | at least | `the reading of regulation 4 that wants exactly the fee`; `reg4` (194 / 193 / 400) |
| F15 | SimpLEX rows 5 and 6 say nothing about payment | paid in full; or unpaid | paid in full ("approved" is not reachable otherwise) | `the SimpLEX reading that takes rows 5 and 6 as unpaid`; `simplex` section "rows 5 and 6 ... unpaid" |
| F16 | the draft's regulation 4 is not visible | a named refusal; or the text of regulation 4 as made (the table itself says regulation 4 "prohibits registration without payment") | refusal | `the SimpLEX reading that takes the draft's regulation 4 as regulation 4 as made`; `simplex` section "the draft's regulation 4 is the text of regulation 4 as made" (the draft then reproduces every outcome: 7 assertions, and 3 reg.4 references) |
| F17 | what the table's outcome words mean | "registration approved" and "the appeal is examined": regulation 4 does not bar; "suspension of service" and "registration rejected, payment must be completed": regulation 4 bars | as stated | no alternative needed; `simplex` asserts the four mappings and that row 8 and the worked example name one effect with two words |
| F18 | kind C, regulation 5: seven days from publication, IL s.10(c) | the last day of the seven days (16.7.2025), which IL s.10(a) gives and the wiki notes state; the day after (17.7.2025); IL s.10(c) applied | the last day, IL s.10(c) not applied (the fleet default for C) | `the Fees Regulations as made came into force on, taking the day after the seven days have run`; `... applying IL s 10(c) under` a `Calendar of rest days`; `dates` |
| F19 | kind C, the amending regulations: no commencement clause | Ordinance s.17: the day of publication, 4.5.2026; no period is counted, so IL s.10(c) has nothing to apply to; Law s.21 then binds from 00:01 | the day of publication; 00:01 | `Ordinance s 17 ...` with another provision supplied (`dates`); the moment-level function `the vintage of the Fees Regulations in force at the moment` |
| F20 | kind R, the update day: 1 January each year | a recurring calendar date: IL s.10 speaks of periods and not of a recurring date | outside IL s.10 | none needed: `regulation 3(a) — the update day of the year`, tested in `dates` |
| F21 | kind B, "the month before their commencement" | counted backwards: IL s.10 does not cover it; the calendar month before the month of the commencement, on year and month numbers (IL s.3: month is the Gregorian calendar month) | June 2025 | none needed: `regulation 3(a) — the calendar month before the month of`, tested in `dates` (July: June; January: the December before) |
| F22 | kinds D, V and W | none is met: reg.4 sets no time for paying; no figure has a period of validity of its own (the interval in which a vintage is in force is delimited by two commencement dates, and is not counted); no window for an application or a request is opened | none | none |
| F23 | which day fixes the vintage and the update level for a service | the day of the application, of the payment, of the exam, of the objection, or of the grant: the sources do not say | the caller supplies the day; `the vintage of the Fees Regulations in force on` maps a day to a vintage | any other day is another call |
| F24 | the draft's regulation 1 speaks of "the student" where the enacted text speaks of "a learner in a vocational training course" | the same learner; or a wider student | the same four limbs for both | none: no computed answer turns on it (regulation 1 feeds no fee); an open question |
| F25 | reg.4 "paid the fee in full" where the payer paid nothing and the fee needs an index update | a fee fixed at a positive figure is not paid in full by a payment of nothing, whatever the update gives; or the updated figure is consulted for everyone, so that without readings the answer is a refusal | nothing paid is not in full, with no index reading needed (assumed: the printed figures are positive and the guard of regulation 3 demands positive readings); anyone who paid something needs the updated figure | `the reading of regulation 4 that needs the updated figure even where nothing was paid`; `reg4` section "Nothing paid" |

## 3. Answer table

Figures below are new shekels.
Section 3.1 and 3.3 and 3.4 follow the gazette and the SimpLEX image; section 3.2 uses ILLUSTRATIVE index readings (the sources contain none).

### 3.1 What each vintage prints, by head of section 59 (reg.2; the provision in that vintage's own numbering)

| head | draft | as made | as amended |
| --- | --- | --- | --- |
| filing an application for a licence or its renewal (s.5) | 284 [2(d)] | silent | silent |
| receiving a licence or its renewal (s.5) | silent | 284 [2(c)] | 284 [2(c)] |
| filing an application for a foreign expert's temporary licence or its renewal (s.9) | 398 [2(e)] | 398 [2(d)] | 398 [2(d)] |
| being granted a foreign expert's temporary licence | silent | silent | silent |
| sitting a practical exam | 194 [2(b)] | 194 [2(a)] | 194 [2(a)] |
| sitting a theoretical exam | 273 [2(a)] | silent | 158 [2(a1)] |
| objecting to the score of a practical exam | 40 [2(c)] | 40 [2(b)] | silent |
| objecting to the score of a theoretical exam | 40 [2(c)] | silent (F3) | 40 [2(b)] |
| attending a continuing training course (s.17) | silent | silent | silent |

Payers: as made and as amended, the examinee (exams), the objector (objections), the licence applicant (licences and temporary-licence applications); the draft names none.
Source: gazette page images of Kovetz HaTakanot 11951 p. 2116 and 12383 p. 2062 (figures 194, 40, 284, 398 and 158), and the 400 dpi crop of the SimpLEX screenshot (figures 273, 194, 40, 284, 398).
Test: `g8-tests-fees.l4`.

### 3.2 Reg.3: the fee on a day (illustrative readings: published 15.6.2025 value 100; 15.7.2025 value 100.5; 15.11.2025 value 101.25; 15.11.2026 value 102.515625)

| service | as made 31.12.2025 | 1.1.2026 | 1.1.2027 (round at every update) | 1.1.2027 (round once) |
| --- | --- | --- | --- | --- |
| practical exam | 194 | 196 | 198 | 199 |
| licence | 284 | 288 | 292 | 291 |
| temporary licence application | 398 | 403 | 408 | 408 |
| objection to a practical score | 40 | 41 | 42 | 41 |

As amended: a theoretical exam 158 on 4.5.2026, 160 on 1.1.2027 (the update of 1.1.2026 came before the sub-regulation existed); the other figures as above from 4.5.2026.
Without the readings the answer from 1.1.2026 is a named refusal, and the draft's answer is a refusal on every day (it was never in force).
Test: `g8-tests-reg3.l4`.

### 3.3 Dates and which text is in force

| fact | answer | section |
| --- | --- | --- |
| the Fees Regulations as made were published | 9.7.2025 | gazette issue date, KT 11951 |
| they came into force | 16.7.2025 (a Wednesday) | reg.5; IL s.10(a) |
| the amending regulations were published, and came into force | 4.5.2026 (a Monday), no commencement clause | KT 12383; Ordinance s.17 |
| the moment each binds | 00:01 on those days | Interpretation Law s.21 |
| the first update day | 1.1.2026 | reg.3(a) |
| the text in force | none before 16.7.2025; as made to 3.5.2026; as amended from 4.5.2026 | reg.5; AMc |

Test: `g8-tests-dates.l4`.

### 3.4 Regulation 4 and the SimpLEX table

Regulation 4: a fee fixed and not paid in full bars the Registrar (giving or renewing a licence) and the Training Division (allowing an exam or an objection); a fee paid in full or no fee fixed does not bar.
Examples as made, before the first update day: a practical exam paid 194 or 400 is not barred; paid 193 or 0 is barred; a theoretical exam is not barred whatever was paid, as no fee is fixed (F12).
As amended: a theoretical exam paid 157 is barred and paid 158 is not.
The grant of a foreign expert's temporary licence, as made: paid 397 is barred and 398 is not; as amended, nothing paid is barred with no index reading, and with readings 402 is barred and 403 is not.
Test: `g8-tests-reg4.l4`.

The SimpLEX table, 7 cases (rows 5, 6, 7 twice, 8 twice, the worked example) in three claims each against three vintages: 28 claims hold, 10 are asserted refused (the draft's regulation 4 is not visible), 16 fail and are in `g8-tests-red.l4`.
The 16 by vintage: as made 10 (row 5: the amount and the reference; row 6: the reference; row 7, theoretical appeal: the amount and the reference; row 7, practical appeal: the reference; row 8, theoretical exam: the outcome and the reference; the worked example: the outcome and the reference); as amended 6 (row 5: the amount and the reference; row 6: the reference; row 7, theoretical appeal: the reference; row 7, practical appeal: the amount and the reference).
The draft has no failing claim: its fees are the ones the table was written against.

## 4. Nouns requests for the INTEGRATOR

Types the INTEGRATOR should consider moving into `domain.l4`, because consumers outside G8 must name them:
`Vintage of the Fees Regulations` and `Service under the Fees Regulations` (G1 and G2 pass a service to the fee-paid test of IP11; the nine constructors are the heads of s.59).
Types that stay G8-internal: `Fee stated in a vintage`, `Payer under the Fees Regulations`, `Exam in a vocational training course`, `Calendar month under regulation 3`, `Inputs of regulation 3` and the reading records and enumerations, `Fee update notice`, `Act under the Fees Regulations`, `Facts regulation 4 asks about`, and the SimpLEX nouns in `g8-simplex-table.l4`.
`domain.l4`'s `Party` has `the Registrar`, `the Training Division` and `the Director General of the Ministry of Labour`, which G8 uses; it has no `the examinee` and no `the objector`, so `Payer under the Fees Regulations` stands in for them.
`Price index reading` (domain) carries `published on`, `year of the index` and `month of the index`; regulation 3(a) is read off `published on`, and a note in the domain comment that the index "published in a month" is found by that field would save G6 a rediscovery.

## 5. Standard inputs consumed and functions exported

### Inputs

| IP | what G8 takes | exact input |
| --- | --- | --- |
| IP12 | the consumer price index readings, with their publication days | `readings IS A LIST OF` `Price index reading` (domain) on every export that can update a figure |
| IP15 | days of rest, recess or holiday | `calendar IS A` `Calendar of rest days` (domain) on `the Fees Regulations as made came into force on, applying IL s 10(c) under` only; no other function counts a period against a calendar |
| IP6 | not consumed | the fee is by service, not by route; the INTEGRATOR composes G2's route with `the service of sitting a practical exam` and `the service of sitting a theoretical exam` |

### Exports (all in `g8-fees.l4`, all `@export`)

| function (exact name) | GIVEN, in order | returns |
| --- | --- | --- |
| `the amount the Fees Regulations state in` v `for the service` s | `vintage`, `service` | MAYBE NUMBER: the printed figure; NOTHING if silent |
| `the fee under the Fees Regulations in the vintage for the service on the day` | `vintage`, `service`, `day`, `readings` | MAYBE NUMBER: the figure after regulation 3; NOTHING if silent or not yet in force; a named refusal if a reading is missing or the vintage is the draft |
| `regulation 4 does not bar the service in the vintage` | `vintage`, `service`, `paid`, `day`, `readings` | BOOLEAN |
| `regulation 4 leaves the Registrar free to give or renew the licence in the vintage` | the same five | BOOLEAN; a named refusal if the service is not a licence service |
| `regulation 4 leaves the Training Division free to allow the exam or the objection in the vintage` | the same five | BOOLEAN; a named refusal if the service is neither an exam nor an objection |
| `the Fees Regulations made under section 59 came into force on` | none | DATE 16.7.2025 (IP13) |
| `the vintage of the Fees Regulations in force on` | `day` | MAYBE `Vintage of the Fees Regulations` |

The first two take a vintage and a service as constructors of the enumerations in `g8-fees-nouns.l4`.
Everything else in `g8-fees.l4` is callable from L4 and not exported.

The constructors a JSON row carries are these strings, exactly.

| `vintage` | the text |
| --- | --- |
| `the SimpLEX draft of the Fees Regulations` | Figure 4, screenshot only; never in force |
| `the Fees Regulations as made` | Kovetz HaTakanot 11951, in force from 16.7.2025 |
| `the Fees Regulations as amended` | Kovetz HaTakanot 12383, in force from 4.5.2026 |

| `service` | s.59 head | prices it (as made / as amended) |
| --- | --- | --- |
| `the service of filing an application for a licence or its renewal` | submitting a licence application | silent / silent (the draft prices it: 284) |
| `the service of receiving a licence or its renewal` | giving a licence or renewing it | 284 / 284 |
| `the service of filing an application for a foreign expert's temporary licence or its renewal` | the application for a temporary licence | 398 / 398 |
| `the service of being granted a foreign expert's temporary licence` | the grant of a temporary licence | silent / silent |
| `the service of sitting a practical exam` | exams required for a final certificate | 194 / 194 |
| `the service of sitting a theoretical exam` | the same | silent / 158 |
| `the service of objecting to the score of a practical exam` | an objection to exams | 40 / silent |
| `the service of objecting to the score of a theoretical exam` | the same | silent / 40 |
| `the service of attending a continuing training course` | s.17 courses | silent / silent |

Which service each IP11 consumer passes, in the Law's own terms:
G1's s.5 application step passes `the service of filing an application for a licence or its renewal`, which as made and as amended is silent, so regulation 4 leaves it free;
the s.6 grant or renewal passes `the service of receiving a licence or its renewal` to the Registrar's test;
the s.9 temporary licence passes either `the service of being granted a foreign expert's temporary licence` or `the service of filing an application for a foreign expert's temporary licence or its renewal` to the Registrar's test, with the same answer (the taken reading of F13);
the Training Division passes the exam or objection service to its own test.

IP11, the fee-paid test.
G1 and G2 take `the fee was paid in full` as a BOOLEAN input; wire it to `regulation 4 does not bar the service in the vintage` (or to the Registrar's or the Training Division's variant).
The semantic difference matters: that function is TRUE both when the fee is paid in full and when no fee is fixed for the service.
Example: as made, a theoretical exam with nothing paid answers TRUE (no fee is fixed, F12), where "the fee was paid in full" would be FALSE.
Where the consumer needs "a fee was fixed and was paid", ask `the amount the Fees Regulations state in` v `for the service` s first.

IP13.
`the Fees Regulations made under section 59 came into force on` is 16.7.2025.
4.5.2026 is the commencement of the amending regulations (`the 2026 amendment of the Fees Regulations came into force on`), not a date for s.63 purposes.
A note for G7: s.63(a)(1) reads "three months from its publication or the day the regulations enter into force, whichever is later"; that can be read as the later of two dates (14.4.2025 against 16.7.2025: 16.7.2025) or as three months from the later date (16.10.2025).
G8 exports the regulations' date and decides neither.

### The `srcrefs` layout, and how to reproduce the check

Quote lines in the modules are generated from the raw files by `work/g8/build.py` (a script that reads the files; no Hebrew is typed): the bidirectional format characters of the gazette text layers become spaces, and whitespace is squeezed.
The check runs with the Law as RAW and three other raw files beside it under the names the `src:` lines use:
```
mkdir raw && cd raw
ln -s <inputs>/law.wiki law.txt                                  # RAW; bare src:N lines
ln -s <inputs>/regulations-fees.wiki fees.txt                    # src:fees:N
ln -s <inputs>/kovetz-hatakanot-11951-p2116.txt kt11951.txt      # src:kt11951:N
ln -s <inputs>/takanot-12383.txt kt12383.txt                     # src:kt12383:N
python3 -I srcrefs.py check --strict raw/law.txt <deposit>/g8-*.l4
```
Run directly as `srcrefs.py check inputs/law.wiki g8-*.l4`, every `src:fees:`, `src:kt11951:` and `src:kt12383:` line fails with `names no raw file fees.txt` (and the same for the other two): measured on `g8-fees-as-made.l4`, 18 problems.
The three IDs must sit beside the RAW file under those names.
The gate checks that quotations and locators agree with the raw lines; it does not check that a locator names the right provision.

### Module order, and the `l4 batch` finding

The g8 modules import each other in this order: `g8-fees-nouns`; then `g8-fees-draft` and `g8-fees-as-made`; then `g8-fees-as-amended` (imports as-made); then `g8-fees` (imports all four); then `g8-simplex-table` (imports `g8-fees`); the test modules import what they test.
All sit in one directory, with `domain.l4` and `il-interpretation-time.l4`; a one-directory run of `check.sh` works.

FINDING, `l4 batch`.
`l4 batch` re-prints the importing module and fails when that module calls a mixfix of three arguments that is defined in an imported module (two runs measured: two arguments pass, three fail; more than three arguments were not tested).
Minimal reproduction, in `work/g8/probe/`: `batchprobe-a.l4` defines `the total of` x `taken on the day` y `under the rule` z; `batchprobe-b.l4` imports it and exports a function calling it; `l4 batch batchprobe-b.l4 --inputs batchprobe-rows.json --entrypoint "add them all"` answers `status: error`, with `Expected keyword taken on the day but found b / In expression involving: the total of / Check that keywords are in the correct order`.
The same mixfix defined in the same module (`batchprobe-c.l4`) runs and gives 6, and a mixfix of two arguments (`the sum of` x `and also` y) defined in an imported module also runs.
On g8 the same failure reads `Expected keyword on the day but found day / In expression involving: regulation 3(a) — the amount of the stated fee`.
The diagnostic is a check error in the RE-PRINTED module body (`g8-fees.l4.batch1.l4`, line 106), so the whole of `g8-fees.l4` fails to typecheck under `l4 batch` and no entrypoint in it is reachable, whichever is named.
Measured: the 0-argument export `the Fees Regulations made under section 59 came into force on` fails with the same error as the others.
Consequence: every `@export` of `g8-fees.l4` runs under `l4 run` and `#ASSERT` (tested), and none runs under `l4 batch` as written.
This is consistent with the l4-ide `CLAUDE.md` (section 3.2.2), which says that only mixfixes defined in the printed module get their surface form re-emitted; it does not mention the three-argument case of an imported mixfix.
Nothing was restructured to avoid it.
Whether `jl4-service` goes through the same printer was not tested: only the `l4` binary was available.

### What the INTEGRATOR's check.sh must expect from G8

`g8-tests-red.l4` fails exactly 16 assertions, on purpose: set `expected_failed` for it to 16 and name it in `encoding.json` `expected_red`.
Every other g8 module must show 0 errors, 0 failed, 0 refused and 0 warnings.
The count of satisfied assertions per module is in section 10.
`work/g8/check.sh` is the skill's `check.sh` restricted to `g8-*.l4`, with a warning count and three extra checks (the `@lang en` line and ASCII filenames, stray `@ref` warnings, and the `srcrefs` gate).

### What check.sh does not count

The nine `#TRACE` directives in `g8-tests-reg4.l4` (the four prohibitions with the fee unpaid, the Registrar's giving with the fee paid, the standing prohibition with no event, the case where no fee is fixed, and regulation 3(b) twice) print results and assert nothing.
Their expected results are written in the comment above each, before the run, and were verified by reading the `Result:` blocks: a breach for each act done while the fee is unpaid; FULFILLED where the fee is paid or none is fixed; the standing prohibition printed back with no event; regulation 3(b) FULFILLED when published at day 40 (no deadline) and the duty printed back otherwise.

## 6. Contradictions in the source

Found by a separate pass after encoding: regulations 1 to 5, the amendment and the draft crop re-read against the modules, candidates listed first, then each checked.
Each gives the provisions, the discriminating case, and where both readings are callable.

1. Law s.2 "final certificate" and s.59 against regulations 1 and 2 as made.
   s.2 (src:64 in `domain.l4`) makes a Training Division exam that "includes a theoretical exam and a practical exam" part of the final certificate, and s.59 lets the Minister fix fees for "exams required to receive a final certificate"; as made, regulation 1 defines and regulation 2 prices the practical exam only.
   So a required exam has no fee fixed and regulation 4 does not reach it: this is the engine of T34.
   Case: a theoretical exam, unpaid, as made.
   Reading A (taken): not barred.
   Reading B: a refusal.
   Both callable (F12); the amendment of 2026 closes the gap for the theoretical exam.
2. Regulation 2(c) as made says "for RECEIVING a licence or renewing it, under section 5", and section 5 is the section on APPLYING (`Law s.5`, src:78-79 in the law file).
   The draft priced the application.
   Case: an application that is refused: is NIS 284 owed?
   Taken: the fee is on the receipt.
   Alternative: on the application.
   Both callable: `the Fees Regulations as made state, reading regulation 2(c) as a fee on the application under section 5, for the service` (`g8-tests-fees.l4`, last section).
3. Regulation 4 first limb ("a licence for which a fee was fixed") against regulation 2(d), which fixes the fee for the APPLICATION for a temporary licence, and against s.59, which prices the grant of a temporary licence separately (and no vintage prices it).
   Case: a foreign expert whose application fee is unpaid, and the Registrar grants the licence.
   Taken: barred, whether the Registrar is asked about the application or about the grant (F13; the first version missed the grant, DIS-4).
   Alternative: not barred (F13).
   Both callable.
4. Regulation 2(b) says "an amount of NIS 40" where (a), (c) and (d) say "a fee of", and regulation 3(a) updates "the amounts of the fees specified in regulation 2".
   Case: the NIS 40 on 1.1.2026: 41 or 40 (F10).
   Both callable.
5. The consolidated text states 158 "(adjusted to 2026)" and 194, 40, 284 and 398 "(adjusted to 2025)" side by side after 1.1.2026, while regulation 3(a) updates all of regulation 2's amounts on each 1 January and regulation 3(b)'s notice is not in the sources.
   The gazette carries neither note.
   Case: a practical exam on 4.5.2026: 194 (printed) or the updated figure (F4, F8).
   Both callable.
6. The SimpLEX draft's regulation 2(c) adds NIS 40 per appeal "to the payment of the fee as stated in sub-section (a)", where (a) is the THEORETICAL fee, for an appeal on "the exam, theoretical or practical"; its word is appeal where the enacted word is objection.
   Case: a practical-exam appeal in the draft: 40 alone, 194 + 40 (the exam's own fee), or 273 + 40 (literal).
   All three callable (F2; `reg3`: 40, 234, 313).
7. The SimpLEX draft's regulation 2(e) cites section 8 of the Law for the temporary licence (in the enacted Law section 8 is validity and the temporary licence is section 9), its preamble prints "section 139" of the Budget Principles Law where the enacted text says 39B, and the worked example cites "Law section 9(a): requires passing an exam", which no enacted section says (T35).
   The first two are kept as comments; the third is the named refusal `the premise of the worked example holds in the enacted Law`, asserted in `simplex`.
8. The table's row 8 and its worked example give two outcome words, "suspension of service" and "registration rejected, payment must be completed", for the same effect of regulation 4 (barred); regulation 4's own word is "shall not allow".
   Asserted in `simplex` (F17).
9. The table's references (regulations 2(a), 2(b), 2(c) and 4) match the draft's numbering only: as made the numbering is (a) practical, (b) objection, (c) licence, (d) temporary licence; as amended (a), (a1), (b), (c), (d) (T34).
   The 16 failing claims of `g8-tests-red.l4`.
10. Regulation 4 names the payer as "the applicant for the licence or the service", where regulation 2 names three payers (the examinee, the objector, the licence applicant) and no regulation defines "the service".
    Not computable; the payers are carried as data and regulation 4 is tested on the fee paid, whoever paid it.
11. Regulation 1's marginal heading is singular ("definition") as made, exact for one definition, and stays singular after the amendment adds a second; the wiki marks it as a slip.
    No legal effect is taken from a heading.
12. s.63(a)(1) can be read as the later of two dates or as three months from the later date (note for G7, section 5).
Checked and found consistent: the figures of the draft's regulation 2(b), (d) and (e) with the gazette's 194, 284 and 398; the wiki's note on regulation 5 (9.7.2025, 16.7.2025) with the gazette date plus seven days; the wiki's note under s.63(a)(1) with regulation 5.

## 7. Open questions for a domain expert

1. Which index readings and which Director General notices exist for 1.1.2026, and what are the amounts now payable?
   None is in the sources.
2. Is the NIS 40 objection charge a fee that regulation 3(a) updates (F10)?
3. Does the amended text's "these regulations" in regulation 3(a) mean the principal regulations or the amending regulations (F11)?
4. Is regulation 2(c) a fee on the application or on the receipt of the licence (contradiction 2), and does regulation 4 bar the grant of a temporary licence whose application fee is unpaid (contradiction 3)?
5. Does "in addition to the payment of the fee in (a)" make an objector pay the exam fee again (F2)?
6. Does an exact half shekel round up, and is each update rounded before the next (F6, F7)?
7. Which day fixes the figure for an exam or objection that straddles 1 January or 4 May 2026 (F23)?
8. Did the 2026 amendment intend an objection to a practical-exam score to carry no charge, or is that an omission?
9. Is a theoretical exam under the text as made a "required exam" that regulation 4 failed to reach (contradiction 1)?
10. What did the SimpLEX draft's regulations 3 to 5 say, and what did the second panel's fee-update scenarios assert?

## 8. What the sources do not answer

Each is an input or a named refusal in the encoding; none gets a default.
The consumer price index readings and the Director General's notices under regulation 3(b), so no figure from 1.1.2026 is answerable without the caller's readings.
The text of the SimpLEX draft beyond regulations 1 and 2(a) to (e), and the fee-update test rows hidden below the visible part of the screenshot; rows 1 to 4 of the test table.
Which day fixes the vintage and the update level for a service that straddles a commencement.
What payment the SimpLEX rows 5 and 6 assume.
Whether a payment above the fee is payment in full.
Any transitional provision for exams or objections begun before 4.5.2026.
The rules for the objection itself (who may lodge it, when, with whom): the Fees Regulations price it and the Law's s.60(1)(b) empowers rules on it; none is in the sources.
The calendar of days of rest for any year (an input to the one function that applies IL s.10(c)).
The Fees Regulations after revision 3011135 of the wiki (2026-05-04), and the Law after revision 2947808.

## 9. Repairs since the first deposit

DIS-4, found by the independent test author (ind-c): the Registrar's test answered "free" when asked about the GRANT of a foreign expert's temporary licence, because no vintage prices the grant, while it barred an unpaid application.
Reg.4 bars the grant of "a licence for which a fee was fixed" and 2(d) fixes NIS 398 for the licence's application, so the taken reading (F13) must bind the grant itself.
Repair: `the service whose fee regulation 4 looks at, reading regulation 4 as` r `, the service` s maps the grant to the application's service under the taken reading (and to itself under the alternative); the facts regulation 4 asks about read the fee of that service.
No exported name or signature changed.
Two assertions of `g8-tests-reg4.l4` were wrong under the first version and were replaced from the text of reg.4 and 2(d), not from the code: the grant with nothing paid is not free (it had asserted free), and the "no fee is fixed" section no longer lists the grant.
One new assertion of mine was mis-written (it asked the exported test, which always takes the reading the encoding takes, to answer the alternative) and was corrected to ask `regulation 4 bars the service, reading regulation 4 as` with the alternative reading.
The independent author's three assertions of DIS-4 pass against the repaired modules.

The same repair needed a second decision (F25): the independent author's third assertion asks about the amended text with no index readings, where the amended figure has been updated on 1.1.2026.
A payer who paid nothing has not paid in full a fee fixed at a positive figure, so the bar is decided without the updated figure; anyone who paid something still needs the readings and gets a named refusal without them.
The alternative reading, which consults the updated figure for everyone, is callable and tested.

The ordinary licence (284, reg.2(c)) was checked for the same hole and has none: as made and as amended price the RECEIPT of the licence, which is the grant, so `the service of receiving a licence or its renewal` is bound by its own fee (tested: 0 and 283 barred, 284 free), and `the service of filing an application for a licence or its renewal` is silent and not mentioned by reg.4, so it is free (tested).
The hole could recur under two callable alternatives that are NOT composed with the regulation 4 layer: the reading of 2(c) as a fee on the application (contradiction 2), and the draft, which prices the application only (its reg.4 is a refusal).
Were either composed, the same mapping rule would be needed for the ordinary licence; it is not encoded because nothing computes under either today.

## 10. Verification record

All commands were run from `work/g8/` against the binary `L4_BIN` (sha256 2e3d6bd3a154e6b4080a445af6cc189dbc4ac087d8221682d09509212f1ce187) with `JL4_LIBRARY_PATH` unset.

`check.sh` printed:

```
module                              errors satisfied  failed  refused  expected warnings
g8-fees-as-amended.l4                    0         0       0        0         0        0
g8-fees-as-made.l4                       0         0       0        0         0        0
g8-fees-draft.l4                         0         0       0        0         0        0
g8-fees-nouns.l4                         0         0       0        0         0        0
g8-fees.l4                               0         0       0        0         0        0
g8-simplex-table.l4                      0         0       0        0         0        0
g8-tests-dates.l4                        0        47       0        0         0        0
g8-tests-fees.l4                         0       146       0        0         0        0
g8-tests-red.l4                         16         0      16        0        16        0
g8-tests-reg3.l4                         0       113       0        0         0        0
g8-tests-reg4.l4                         0        76       0        0         0        0
g8-tests-simplex.l4                      0        64       0        0         0        0
TOTAL (12 modules)                      16       446      16        0                  0
(a failed assertion is also an error; any other error, any refused assertion or any warning makes the run red)

extra checks
  all g8 modules start with '@lang en' and have ASCII filenames
  l4 check: no stray @ref warnings
  srcrefs (strict): srcrefs check: 43 src: lines, 26 runs, 60 locators, 0 problems
```

The mutation check (`work/g8/mutate.py`): a textual mutation is applied to a scratch copy of the modules, all six test modules are run, and the count of newly failing assertions is printed ("red.l4 -n" means n of the sixteen expected failures stopped failing).
Every one of the 27 mutations was caught by at least one test module.
Provenance: the full run of 24 was made on the module text before the `BRANCH` rewrite of the two three-arm `IF` chains in `g8-fees-as-made.l4` and before the `s 10 — the first day of a period counted from or after an event on` call replaced a `PLUS 1` on a date; M04 and M14 were rerun after their anchors were repaired, M05 and M17 after the rewrite; the counts of `check.sh` are identical before and after.
After the repair of DIS-4 (section 9) M06, M07, M11, M15, M22 and M23 were rerun and M25 to M27 were added; the other lines were run before it, so their `reg4.l4` counts predate the 24 assertions added to that module (their status, caught, is unchanged by the repair, which touched only the regulation 4 layer of `g8-fees.l4`, the nouns and `g8-tests-reg4.l4`).
A full rerun of the first 13 mutations after the process kills of 2026-10-13 gave identical lines.

```
M01 as made 2(a): 194 -> 195                                           fees.l4 +3, reg3.l4 +29, reg4.l4 +5, simplex.l4 +2
M02 reg.5: 7 days -> 6 days                                            dates.l4 +10, reg3.l4 +2
M03 rounding: half up -> truncation                                    reg3.l4 +27, reg4.l4 +1
M04 later base index: November y-2 -> y-1                              reg3.l4 +19
M05 first update day: year + 1 -> year + 0                             dates.l4 +4, reg3.l4 +64, reg4.l4 +27
M06 reg.4 bar: fixed AND NOT paid -> fixed AND paid                    reg4.l4 +43, simplex.l4 +30
M07 payment in full: AT LEAST -> GREATER THAN                          reg4.l4 +12
M08 as amended 2(a1): 158 -> 159                                       fees.l4 +1, reg3.l4 +10, reg4.l4 +1
M09 as amended: practical objection leaks 40                           fees.l4 +5, reg3.l4 +3, reg4.l4 +1, red.l4 -1
M10 draft 2(a): 273 -> 274                                             fees.l4 +1, reg3.l4 +3, simplex.l4 +1
M11 vintage in force: amendment day AT LEAST -> GREATER THAN           dates.l4 +1
M12 draft borrows a figure for receiving a licence                     fees.l4 +4
M13 rate of change over new instead of base                            reg3.l4 +11, reg4.l4 +1
M14 first update year of a later amount ignores its effective day      reg3.l4 +7, reg4.l4 +1
M15 reg.4 officials: temporary licence not bound                       reg4.l4 +5
M16 objection reading I: charge x n -> charge                          reg3.l4 +6
M17 once-rounding reads the chain                                      reg3.l4 +3
M18 SimpLEX: bars-means-approved swapped                               simplex.l4 +11
M19 objection charge treated as not updated although the reading says it is reg3.l4 +63, reg4.l4 +4
M20 first base index: published read as relating                       reg3.l4 +49, reg4.l4 +4
M21 update day is 2 January                                            dates.l4 +6, reg3.l4 +53, reg4.l4 +3
M22 not yet in force: LESS THAN -> AT MOST                             reg3.l4 +9, reg4.l4 +4
M23 reg.4 binds the Registrar for a practical exam                     reg4.l4 +4
M24 payer of the as-made practical exam is the objector                fees.l4 +2
M25 grant of a temporary licence looks at its own (unpriced) fee again reg4.l4 +9
M26 a payer who paid nothing is in full                                reg4.l4 +11
M27 a fee is fixed even before the vintage is in force                 reg4.l4 +1
```

Numbers re-read against the sources: `work/g8/recheck_numbers.py` finds every figure and date of the as-made and as-amended modules (194, 40, 284, 398, 158, 7 days, 9.7.2025, 4.5.2026) in the gazette text layers on the lines of the provision that carries it.
The five figures of the draft (273, 194, 40, 284, 398) and the 40 of row 7 were read by eye from the 400 dpi crop (`draft-bottom.png`, `panel-left-top.png`); there is no text layer to script from.
Where the Wikisource text and the gazette were compared (`work/g8/cmp_asmade.py`), the words of regulations 1 (definition), 2(a), 2(c), 2(d), 3, 4 and 5 as made are the wiki's words, and regulation 2(b) differs exactly as the amendment says.

`peeked`: nothing that the brief forbids.
The `~/.claude/` memory index in my context mentions this subject; I did not follow it.
One `cp -r` of the shared deposit directory into `work/g8/`, a listing of it, and two later listings of the deposit directory itself showed filenames of other groups' files (`FRAGMENT-G7.md`, `g1-adverse-action.l4`); the copy was deleted at once.
The mutation script copied other groups' modules into a scratch directory in its first run, and was changed to copy only `g8-*.l4` and the two read-only modules; those copies were deleted.
A name-clash check read other groups' modules by `grep` for my names and printed no other group's text: no name of G8 appears in any module deposited so far.
