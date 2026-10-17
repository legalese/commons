# KiwiSaver Act 2006 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_2006_40.txt`, the PCO's version as at 1 April 2026, converted from its XML on 2026-10-13 (`act_public_2006_40.meta.json` beside it).

## 1. What is encoded

**Parts 1-3 and Schedule 1** — who the Act applies to, membership, contributions, and the scheme rules on withdrawals — are encoded as rules. **Parts 4 and 5** (governance of schemes, default providers, complying superannuation funds, exempt employers, administration) set duties on providers, the FMA and the Commissioner rather than answers for a member or an employer; they are carried as text, with the periods in Part 3 that touch them (the 62-day holding period, s 75).

**What the converted text lacks.** Paragraph labels are gone. **Formulas** in ss 86, 87, 101D, 101T and Schedule 4 have lost their symbols. The compulsory employer contribution formula (s 101D(1)) is read as *gross salary or wages × CEC rate − other contributions − hybrid schemes amount*, never below 0 ("a positive amount"); that reading should be checked against the official print (open question 1). The interest formulas (ss 86, 87) are not encoded.

**Inputs.**
- residence, citizenship, date of birth, and the New Zealand superannuation qualification age (set by the New Zealand Superannuation and Retirement Income Act 2001; 65 in the tests);
- the kind of employment, and whether the employer is exempt, the employee a secondee, the job on the same payroll or business, or excluded by s 14(1);
- each pay's gross salary or wages and date; the rate the employee chose; rate reductions, savings suspensions and non-deduction notices; other employer contributions and any hybrid schemes amount; grace periods (s 101FB);
- the member's accumulation and its Crown contribution and Australian parts; whether the manager or supervisor is satisfied of a hardship, illness or congenital condition, and whether alternatives are exhausted.

### The top-level goal

`the KiwiSaver position for` a `KiwiSaver case` (`ks-goal.l4`, `@export default`) answers: *for this person, this employment and this pay, does automatic enrolment apply and what is the opt-out window; what is the contribution rate and the deduction; what is the compulsory employer contribution; and, if a withdrawal is sought, the most that may be withdrawn?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Membership | `automatic enrolment applies to…` (`@export`), `the opt-out is in time…` (`@export`), `the first/last day to opt out…`, `the day the opt-out takes effect…`, `who may opt in…` | ss 6, 10-21, 33-35, 42, 51 | `ks-membership.l4` |
| 2 | Contributions | `the contribution rate for` (`@export`), `the deduction from the pay` (`@export`), `the compulsory employer contribution for … and …` (`@export`), `a rate reduction must be granted…`, `may apply for a savings suspension…`, `the days of savings suspension granted…` | ss 62-66, 101A-101FC, 101L-112B | `ks-contributions.l4` |
| 3 | Withdrawals | `the most the member may withdraw, facts … , account …` (`@export`), `may make a first home withdrawal` | Schedule 1 cls 4-14C | `ks-withdrawals.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-5, 6A-9 | carried as text |
| s 6 | Goal 1 (s 6(2)-(3) employers: carried as text) |
| ss 10-12, 14 | Goal 1 |
| s 13 | no text in this version |
| s 15 | carried as text |
| ss 16-18 | Goal 1 |
| ss 19-23A | carried as text |
| ss 24-32 | no text in this version (exempt employers, repealed) |
| ss 33-35 | Goal 1 |
| ss 36-41, 43-50, 52-59D | carried as text |
| s 42 | Goal 1 |
| s 51 | Goal 1 |
| ss 60-63B | carried as text (s 62 in the deduction) |
| ss 64, 66 | Goal 2 |
| ss 65, 66A, 67-74, 76-101AA | carried as text (ss 86, 87 formulas lost) |
| s 75 | Goal 1 (62 days) |
| ss 101A-101FC | Goal 2 |
| ss 101G-101K | carried as text |
| ss 101L, 101M, 101S(2) | Goal 2 |
| ss 101N-101R, 101T | carried as text |
| ss 102, 104, 108, 112B(3) | Goal 2 |
| ss 103, 105-107, 109-112, 113, 114 | carried as text |
| Part 4, Part 5 | carried as text |
| Schedule 1AA | carried as text |
| Schedule 1 cls 1-3, 4A, 5-7, 13, 15-17 | carried as text |
| Schedule 1 cls 4, 4B, 8, 9, 10, 12, 12B, 14, 14C | Goal 3 |
| Schedule 1 cl 14B | carried as text (a transfer of the whole accumulation to Australia) |
| Schedules 2-4 | carried as text |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 10(c), 12(2)(b), 16 | A 28-day contract | Only one that continues to the 28th day becomes new employment; age and the opt-out window are taken from that day | s 12(2) "(as if the employee then started new employment)"; the opt-out window and the ended-contract case changed after the independent pass |
| F2 | s 104(3)(b)(i) | "1 year" as a number of days | 365 | The application states a period |
| F3 | s 101D(1) | The formula (symbols lost) | gross × CEC rate − other contributions − hybrid schemes amount, at least 0 | The items' definitions, in order; "a positive amount" |
| F4 | ss 16, 18(2) | The late opt-out window | Accepted only if the s 18(1)(b) ground applies, the Commissioner accepts, and the notice is received within 92 days after the first contribution (if any) | s 18(2) |
| F5 | cl 14C | The amount | The lesser of the liability and the accumulation less Crown contributions; the terminal-tax cap (cl 14C(2)(a)(ii)) is folded into the liability input | The text |
| F6 | s 101L(3) | Is the ending date of a rate reduction its last day? | Yes: both the first and the last day count towards the 92 days and the 1 year | s 101N "the date on which the rate reduction will end"; adopted after the independent pass |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `ks-tests.l4` (encoder) | 0 | 119 | 0 |
| `tests-independent.l4` | 0 | 167 | 0 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 0 | 286 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 7 disagreements, all resolved in its favour: 28-day contracts that end (F1), the Oranga Tamariki guardian in s 35(3), rate-reduction days (F6), a notice naming an unlisted rate, and the s 64(1)(a)(ii)-(iii) rates. **The encoder's tests that encoded the rejected readings were changed** and marked in `ks-tests.l4`.

**Known limits.** s 112B(3)'s "within 92 days" shares the s 64(4) test; Schedule 1 cl 17 (no tax-credit Crown contribution without a residence declaration) is not applied; s 6(2)-(3), s 12(2)(a), s 62(a), (c), the s 101FB periods, s 101E, the eligibility in ss 101L(1), 112B(1), s 48, cl 14C's terminal-tax cap and 24-month window, and cls 14(2), 14B are inputs or text.

## 5. Open questions for a New Zealand superannuation lawyer

1. s 101D(1): confirm the formula against the official print.
2. F1: is age taken at the start of a short contract or when it becomes new employment?
3. F6: is the ending date of a rate reduction its last day?
4. s 112B(3): may a non-deduction notice be revoked on the 92nd day?

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the deadlines to opt out (s 16), to give the information pack (s 42(1)(a)) and to pay a complying fund (s 101F(2)). The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `ks-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 285 satisfied (123 encoder, 162 independent), 5 failed (5 independent assertions written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
