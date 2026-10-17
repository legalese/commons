# Parental Leave and Employment Protection Act 1987 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_1987_129.txt`, the PCO's version as at 1 July 2026, converted from its XML on 2026-10-13 (sha256 `e1f5f5ce…`; `act_public_1987_129.meta.json` beside it).

## 1. What is encoded

**The whole Act**: ss 1-77, Schedule 1AA and Schedule 1. Repealed sections (2AB, 18, 19A-19B, 24, 25, 30, Part 3B, 39A, 60-63, 67, 69, 71H, 71LA, 71OA, 71V, 73A, 75) have no text in this version.

**What the converted text lacks.** Paragraph labels are gone; a label in a comment or a name is read from the provision's place in its list.

**Inputs.** These are taken as given rather than worked out:
- who is an employee (ERA s 6), a self-employed person, a spouse or partner, and the s 7 facts (whether permanent primary responsibility was taken, the child's age then, the nomination under s 7(2));
- the average weekly hours with the same employer over the 6 and 12 months (s 72A decides which hours count; Schedule 1 which employers count as the same), and each week's hours and earnings over the 52 weeks;
- ordinary weekly pay (Holidays Act 2003, s 8), net income from self-employment, and the weeks not worked under s 71CB(2);
- **the maximum weekly rate in force**, since s 71N adjusts it each 1 July and s 71O may raise it; the text's own figure, $811.05, is `the maximum weekly rate stated in s 71M`; and the minimum wage, for the self-employed minimum (s 71N(4));
- the day the 36th week of gestation would have ended;
- agreements, consents, employer decisions and defences, Labour Inspector determinations, and relief for irregularities (ss 68, 71IA).

**Earlier children.** Schedule 1AA cl 5 applies this version to a child due or born on or after 1 July 2020, or taken into care on or after that day. Earlier children fall under the Act as it stood before the 2017 amendments (22 weeks, and earlier figures), which the text does not carry; the encoding refuses them.

### The top-level goal

`the parental leave position for` a `Parental leave case` (`pl-goal.l4`, `@export default`) answers: *for this person and this child, which employment test do they meet; are they the primary carer; may they take primary carer leave (26 weeks), partner's leave (1 or 2 weeks), and how much extended leave is left; may they request negotiated carer leave; and are they entitled to parental leave payments, at what weekly rate, for how many weeks, with how many weeks of preterm baby payment, and by when must they apply?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Eligibility | `the primary carer kind of` (`@export`), `the employment test met by … before` (`@export`), `meets the parental leave payment threshold test` (`@export`), `this version applies to`, `s 6 bars leave…` | ss 2, 2BA, 4, 6, 7; Schedule 1AA cl 5 | `pl-eligibility.l4` |
| 2 | Leave | `may take primary carer leave…`, `may take partner's leave…`, `the extended leave remaining…` (`@export`), `the last day of extended leave for…`, `the last day to request or give notice, for` | Parts 1-3A | `pl-leave.l4` |
| 3 | Notices, the position, protection | `the termination contravenes s 49(1)…` (`@export`), `the last day to make a parental leave complaint…` (`@export`), `extended leave may start on…`, `the grounds the employer may prove…` | Parts 4-7 | `pl-protection.l4` |
| 4 | Payments | `entitled to parental leave payments` (`@export`), `the weekly rate of parental leave payment` (`@export`), `the weeks of preterm baby payment for…` (`@export`), `treated as having returned to work…` (`@export`), `the last day to apply for payments…` (`@export`), `the day parental leave payments begin…`, `…end…` | Part 7A, ss 72B-72C | `pl-payments.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-1B, 2, 2A-2AD, 2B, 2C, 3 | carried as text (s 2's 26-of-52-weeks extension of "employee" is applied through the threshold test) |
| s 2BA | Goal 1 |
| s 4 | Goal 1 |
| s 5 | carried as text |
| s 6 | Goals 1, 2 |
| s 6A | carried as text |
| s 7 | Goal 1 |
| ss 8, 9, 11, 15 | Goal 2 |
| ss 10, 12-14, 16 | carried as text |
| ss 17, 19, 21 | Goal 2 |
| ss 20, 22 | carried as text |
| ss 23, 26-28 | Goal 2 |
| s 29 | carried as text |
| ss 30B, 30D, 30E, 30I, 30J | Goal 2 |
| ss 30A, 30C, 30F-30H | carried as text |
| ss 31(3), 33(b) | Goal 2 (`the last day to request or give notice, for`) |
| ss 34-39 | Goal 3 (s 34(1), s 36(3)-(4) carried as text) |
| ss 40-42 | Goal 3 |
| ss 43, 44 | carried as text |
| ss 45-47 | Goal 3 |
| s 48 | carried as text |
| s 49-52 | Goal 3 (the s 51, 52 defences are an input) |
| ss 53, 54 | carried as text (s 54 is the "substantial reason" constructor) |
| ss 55, 56 | Goal 3 |
| ss 57-59, 64-68, 70-71 | carried as text |
| s 70C | Goal 3 |
| ss 71A-71C, 71CC, 71CD | carried as text |
| ss 71CA-71CBA, 71CE, 71D-71G, 71I, 71J-71N | Goal 4 |
| ss 71O-71W, 71ZA | carried as text |
| ss 71X-71ZB, 72B, 72C | Goal 4 |
| ss 72, 72A, 72D-77 | carried as text |
| Schedule 1AA cl 5 | Goal 1 (cls 1-4 are superseded for any child cl 5 reaches) |
| Schedule 1 | input (which employers are the same employer) |

`provisions carried as text` in `pl-protection.l4` lists the text-only provisions.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 26(3), 28(1) | Whose primary carer leave reduces whose extended leave? | The person's own s 26(1) amount is reduced by their own primary carer leave; the pool shared under s 26(2) by both people's | s 26(3) reduces "the period of extended leave to which the employee and his or her spouse or partner are entitled"; s 1B describes a 6-month employee as having an "extension to 26 weeks" in total |
| F2 | s 27(3) | Which end date applies when one partner meets the 12-month test and the other the 6-month test? | The 12-month date | (a) and (b) both apply on the words; the later date gives effect to the 52-week combined entitlement in s 26(2)(c) |
| F3 | ss 30B(3)(c), 33(b), 37, 39(2) | "at least 14 days" / "not less than 21 days' notice" | Clear days (14 or 21 whole days between) | The Legislation Act 2019's rule for "at least" or "not less than" a number of days between 2 events, as in the Holidays Act encoding. The independent author read the Act alone and counted by date difference; 2 of its assertions stay failing on this |
| F4 | ss 6, 71F(a) | When are the 6 months after the last leave or payment period for another child measured to? | To the day the new leave or payments start: the birth (before it, the due date), or the date of becoming the primary carer | Leave begins on the date of confinement (s 10) and payments on the earlier of leave and confinement (s 71K); changed after the independent pass, which measured to the start (S46b, S166b) |
| F5 | s 71M(1B) | The rate for a person eligible both as an employee and as self-employed | The two rates added together, up to the maximum | (1B) only caps the total; the two kinds of work are counted separately (s 2AD) |
| F6 | s 71DA(2) | Does a part week count as a week of preterm baby payment? | As its fraction: the exact weeks between the two dates | s 71DA(4)(a) ends the payment on the day the 36th week would have ended; changed after the independent pass (S204), from rounding up |
| F7 | s 2BA(4) | What does "employed as an employee for at least an average of 10 hours a week for any 26 of the 52 weeks" require? | Employment in at least 26 of the 52 weeks, and 26 of those weeks averaging 10 hours; a week with no hours is a week not employed | s 2 para (b) of "employee" is "a person who was an employee for any 26 of the 52 weeks"; adopted after the independent pass (S36, S41) |

Also read, without a fork: s 7(2) asks for a nomination only where 2 or more persons meet s 7(1)(c); s 6 bars all parental leave (primary carer, partner's and extended); s 54 keeps a dismissal for a substantial reason unrelated to the pregnancy, the child or the employee's rights outside s 49; a (b)(i) or (b)(ii) carer is not barred by s 71D(2); and "26 weeks after" a date (ss 49(1)(c), 56(2), 71L(1)(a)) is the 182nd day after it; s 71I's "before the earliest of" makes the day before the last day to apply; s 9(2) counts the weeks from the start of leave to the expected date of delivery as a fraction; the parental leave payment threshold test is met when the 26 busiest weeks total at least 260 hours; where the 12-month and 6-month tests are both met, the 12-month test is reported.

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `pl-tests.l4` (encoder) | 0 | 217 | 0 |
| `tests-independent.l4` | 2 | 262 | 2 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 2 | 479 | 2 |

**2 failures are expected**, which is why `check.sh` exits non-zero: the independent author's notice deadlines counted by date difference against fork F3's clear days (§3). Neither side's expected value has been changed.

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 12 other disagreements, all now resolved in the author's favour: s 7(2) for a sole carer; the threshold test's 26 weeks of employment (F7); s 6 applied to partner's and extended leave; s 6 and s 71F measured to the start of the leave or payments (F4); the s 71D(2)(b) transfer exception; s 54 dismissals; and fractional preterm weeks (F6). **The encoder's own tests that had encoded the rejected readings were changed** to the new readings, each marked in `pl-tests.l4` ("changed after the independent pass").

**Known limits** (answered through inputs or separate functions): s 4 is not in the top-level goal; s 9(2) is not in the goal's 26 weeks; ss 2A-2AC, 2B, 5, 6A, 72A and Schedule 1 are inputs; ss 10, 12-14 start dates; s 15's conditions; ss 27(4)(b), 31(4), 33(a), (c), 36(3), 45(4)(c); the elements of the ss 51-52 defences; ss 55(2), 68(4), 70A-70G, 71I(3), 71IA; the s 71J(1)(b) split; s 71DB(4)(c).

## 5. Open questions for a New Zealand employment lawyer

1. F1: does a 6-month employee who takes 26 weeks of primary carer leave have any extended leave left if their partner meets the 12-month test?
2. F5: how is the rate set for a person eligible both as an employee and as a self-employed person?
3. F6: are preterm baby payments made for part weeks, or for whole weeks only?
4. F7: does the payment threshold test require 26 weeks of employment, or only 260 hours across the busiest 26 weeks?
5. F3: are "at least 14 days" and "not less than 21 days' notice" counted in clear days?
6. Preterm baby payments (s 71DA) carry no transitional provision in Schedule 1AA; from which children do they apply?

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the deadlines to decide or challenge a flexible-leave request (ss 30D, 30I), to apply for parental leave payments (s 71I), to file a charge (s 71Z), to apply for a review (s 71ZB), to act within n days after an event (ss 34, 36, 38), to apply for an interim order (s 55), to complain (s 70) and to object (s 70C) — not deadlines counted back from an event. The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `pl-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 478 satisfied (220 encoder, 258 independent), 6 failed (the 2 clear-days assertions under fork F3, and 4 written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
