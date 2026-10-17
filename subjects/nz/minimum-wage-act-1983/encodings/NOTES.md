# Minimum Wage Act 1983 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (ss 1-14, Schedules 1AA and 1), as in the PCO's version 38 as at 20 December 2023, and the two transitional provisions reprinted with it (Minimum Wage Amendment Act 2007 s 6; Minimum Wage (Starting-out Wage) Amendment Act 2013 s 7). It is encoded from the PDF the user supplied; the text is deposited and the PDF is not.

**The Act prescribes no rate.** Sections 4, 4A and 4B give the Governor-General power to prescribe rates by Order in Council, and limit that power. The rates (and, for s 4A, the classes) are therefore an input: a `Minimum Wage Order`. The encoding checks the Order's classes and rates against the limits in ss 4A and 4B, and refuses when a class that applies to the worker is outside them, because the Act does not say what rate follows.

**Other inputs.** These are taken as given rather than worked out:
- whether a person is a "worker" (s 2: an employee under s 6 of the Employment Relations Act 2000);
- whether a person is "involved" in a default or non-compliance (ss 10(4), 11AA(3): s 142W of that Act);
- the first day of each period of continuous employment (with any employer, with any employer since the benefit run, with the current employer), and the months of continuous benefit payments, on the definitions in s 4A(5)-(6). The encoding works out from the first day when the s 4A(3)(a)(i) period is completed;
- a Labour Inspector's satisfaction under s 8(1) and (5), and a permit's terms;
- the cash value of board and lodging where an Act, determination or agreement fixes it (s 7(1)).

### The top-level goal

`the minimum wage position for` a `Wage case` (`mwa-goal.l4`, `@export default`) answers: *for this worker and this pay period, does the Act apply; which minimum rate governs and what is it per hour; what is the minimum for the period; what board and lodging deductions count; how much is owed; and may it be recovered under s 11?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Does the Act apply; which rate governs; is the Order's rate within the power? | `the Act applies to`, `the rate that governs … under … on` (`@export`), `the starting-out rate for … under`, `the training rate for … under`, `the class and its rate are within s 4A`, `the permit is in force on` | ss 2, 4, 4A, 4B, 6(1), 8(3)-(5), 9 | `mwa-rates.l4` |
| 2 | What is the minimum for the period, what may be deducted, what is owed? | `the hours the minimum applies to`, `the minimum wages at … for hours`, `the most that may be deducted for board/lodging under`, `the arrears at … for … in` (`@export`) | ss 6, 7, 9(e), 11(1) | `mwa-payment.l4` |
| 3 | Who is liable to a penalty; who may recover what, from whom? | `liable to a penalty under s 10` (`@export`), `may recover a penalty under s 10`, `s 11 applies`, `may recover the wages under s 11`, `the wages recoverable under s 11AA by … on` (`@export`), `may commence compliance order proceedings under s 11A` | ss 10, 11, 11AA, 11A; Sch 1AA | `mwa-enforcement.l4` |
| 4 | Does the hours clause comply with s 11B? | `the hours clause complies with s 11B` (`@export`), `the parties must endeavour to fix a week of not more than 5 days` | s 11B | `mwa-enforcement.l4` |
| 5 | Permits, the annual review, the 2013 transition | `a Labour Inspector may issue an exemption permit` (`@export`), `a Labour Inspector may revoke the permit`, `the review for the year must be done by`, `the rate for a new entrant under the 2013 transition` | ss 5, 8(1), (5); 2013 Act s 7 | `mwa-enforcement.l4` |

How the rate is chosen (`the rate that governs`):
1. The Act does not apply (not a worker, or s 9(b) or (d)) → no rate.
2. An exemption permit in force on the day → the permit's rate (s 8(4) "is taken to be the minimum rate of wages prescribed under this Act for the worker").
3. A starting-out class of the Order applies → the highest such rate (s 4A(4)).
4. The worker is in a training class allowed by s 4B and the Order has a training rate → the training rate.
5. Aged 16 or older → the adult rate (s 4(1)).
6. Otherwise (under 16) → no minimum rate is prescribed (s 6(1) reaches only a worker "who belongs to a class of workers in respect of whom a minimum rate of wages has been prescribed").

## 2. Coverage table

| provision | disposition |
| --- | --- |
| s 1 (title, commencement 2 September 1985) | carried as text |
| s 2 interpretation | read into the facts; `worker` is an input |
| s 2A, s 3 | carried as text |
| s 4(1)-(2) adult rate | Goal 1 (`the rate that governs`) |
| s 4(3), 4A(7), 4B(3), 12(2) secondary legislation | carried as text |
| s 4A(1)-(4) starting-out rates | Goal 1 |
| s 4A(5)-(6) continuity, definitions | Goal 1 (`a specified social security benefit`, `the continuous social assistance period in months`); the rest read into the month-count inputs |
| s 4B(1)-(2) training rate | Goal 1 |
| s 5 annual review | Goal 5 |
| s 6(1) entitlement | Goals 1-2 |
| s 6(2)-(3) | repealed |
| s 7(1) board and lodging | Goal 2 |
| s 7(2) time lost | Goal 2 |
| s 8(1), (5) issue and revoke a permit | Goal 5 |
| s 8(2) | carried as text |
| s 8(3)-(4) a permit in force and its rate | Goal 1 |
| s 8(6) "disability" | read into the s 8(1)(a) input |
| ss 8A-8D, 9(a), 9(c) | repealed |
| s 9(b), (d), (e) | Goals 1 and 2 |
| s 10 penalties | Goal 3 |
| s 11 recovery | Goals 2-3 |
| s 11AA recovery from a person involved | Goal 3 |
| s 11A compliance orders | Goal 3 |
| s 11B hours | Goal 4 |
| s 12 regulations | carried as text |
| s 13 saving | carried as text |
| s 14, Schedule 1 repeals | carried as text |
| Schedule 1AA | Goal 3 (`the 2016 amendments apply to conduct on`) |
| 2007 Act s 6 | carried as text (an old permit is entered as a `Permit`) |
| 2013 Act s 7 | Goal 5 |

`provisions carried as text` in `mwa-enforcement.l4` lists the text-only provisions.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 4A(1)(c)(i), (6) | A run of benefit payments that includes a payment not on the s 4A(6) list: is it a "continuous social assistance period"? | No: its length counts as 0 | (1)(c)(i) speaks of being "continuously paid 1 or more specified social security benefits" |
| F2 | s 4A(3)(a)(i) | A class defined by factor (i) only: whose employment ends the rate, "any employer or the worker's current employer (as the case requires)"? | Any employer, counting only employment since the benefit run | By analogy with (1)(c)(ii)(A), which excludes employment before the continuous social assistance period when the class uses factor (i) |
| F3 | s 8(3), (5) | Is a permit in force on the last day of its stated period, and on the day its revocation takes effect? | In force on the last day; not in force from the revocation date | "remains in force for the period stated"; revocation ends it |
| F4 | s 7(1) | Board and lodging both provided: one ceiling or two? | Two, added: 15% for board and 5% for lodging, or each fixed cash value | The subsection gives each its own figure ("15% for board or ... 5% for lodging") |
| F5 | s 7(1) | What does a deduction above the ceiling count for? | Only up to the ceiling; the excess is not credited against the minimum | The deduction "shall not exceed" the ceiling |
| F6 | s 7(2) | Which hours does s 7(2) reach? | The hours the worker was engaged for in the period; time lost for any reason other than (a) default or (b) illness or accident is still paid at the minimum | The text bars any other deduction "in respect of time lost". The caller decides which hours the worker was "engaged" for |
| F7 | ss 4A(2), 4B(2) | An Order's rate below 80%, or a class outside s 4A(1) or (3), that applies to the worker | `REFUSE` | The Act limits the power but does not say what rate the worker gets if the limit is broken |
| F8 | s 4A(2) | A rate prescribed as a percentage: rounded to the cent? | Not rounded | The Act says nothing of rounding |
| F9 | s 10, Schedule 1AA cl 2 | Penalty liability for conduct before 1 April 2016 | `REFUSE`: the section as it stood before then is not carried | Schedule 1AA cl 2 keeps the 2016 amendments off earlier conduct |
| F10 | s 11AA, Schedule 1AA cl 2 | Recovery from a person involved, for conduct before 1 April 2016 | 0: s 11AA did not exist before the 2016 Act and does not reach earlier conduct. (Contrast ss 10 and 11, which replaced earlier sections: those refuse) | Schedule 1AA cl 2 |
| F11 | s 4A(3)(a)(i) | "only until ... the date on which the worker has completed 6 months' continuous employment": may the rate be paid on that date? | Yes: "until" includes the date. A period beginning on the first day of work is completed on the day before the same date N months later | Limb (ii) says "the day before the date on which the worker ceases to satisfy" the criteria, which only makes sense if "until" includes the date it names. Raised by the independent test author |
| F12 | s 4A(3)(a)(ii) | The day before the worker's 20th birthday | Age is an input in whole years, tested on the day asked, so the rate stops on the birthday | The caller gives the age on the day |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15 (l4-ide unstable at 7768812fa): **7 modules, 0 errors, 257 assertions satisfied, 0 failed, 0 warnings** (131 in `mwa-tests.l4`, 126 in `tests-independent.l4`). No assertion is expected to fail.

`mwa-tests.l4` (131 assertions) is written from the Act. The Order it uses is invented: an adult rate of $23.15, three starting-out classes at 80% (16-17 by employment with the current employer; 18-19 by 6 months on a benefit and employment since; 16-19 on a training contract) and a training rate of 80%.

**The independent test pass** (`tests-independent.l4`, `independent-expectations.md`, `INDEPENDENT-TEST-REPORT.md`): a fresh session wrote expectations from the brief and the Act before reading the encoding, with its own Order (adult $25; classes at $20, 85% and $21; a training rate of $20). Of 126 assertions, 125 passed first time. The one failure was the day the worker completes 6 months (F11): the encoding took month counts and stopped the rate on that day. The encoding now takes the first day of work and works out the completion date, and pays the starting-out rate on it. The author's other remarks led to two more changes: s 11, like s 10, now refuses for conduct before 1 April 2016; and the top-level goal now reports a board or lodging deduction above the s 7(1) ceiling. When the inputs changed from month counts to dates, the independent file's helpers were ported (each change is marked `[ported …]`); no expected value was changed.

## 5. Open questions for a New Zealand employment lawyer

1. F2: for a factor (i) class, whose employment ends the starting-out rate under s 4A(3)(a)(i)?
2. F6: does s 7(2) reach a worker paid only for hours actually worked?
3. F7: if an Order's starting-out or training rate is below 80% of the adult rate, is the rate void (so the adult rate applies), or does the Order stand until set aside?
4. s 8(4): does a permit's rate govern a worker under 16, for whom no rate is otherwise prescribed?

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the Minister's annual review (s 5(1)), which read literally may then be done on the first working day of the following January. The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `mwa-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 258 satisfied (134 encoder, 124 independent), 2 failed (2 independent assertions written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.

**Open question (s 55).** Does Legislation Act s 55 really let the s 5(1) review "in each year ending on 31 December" be done in the following January? Read literally it does, since 31 December is never a working day; the encoding applies it at the user's direction.
