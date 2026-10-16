# New Zealand Superannuation and Retirement Income Act 2001 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_2001_84.txt`, the PCO's version as at 10 July 2026, converted from its XML on 2026-10-13.

## 1. What is encoded

**Part 1 (entitlement)** is encoded as rules, with the computable parts of Part 2 (the Fund's contributions and withdrawals, s 71 reviews) and s 16 (the bounds on the rates). The rest of Part 2 (the Guardians' constitution, investment, reporting), Part 3 (political commitment, transitional) and Part 4 (the Retirement Commissioner) set up bodies and duties, and are carried as text.

**What the converted text lacks — and it matters here.** The conversion dropped every table and formula:
- **the s 8(4) table** of total time requirements by date of birth. The requirement is an input (`total time requirement from the s 8(4) table, in years`). The surviving example (a person born 30 June 1967 needs 14 years) is used in the tests as stated.
- **the Schedule 1 rates.** The rates in force are an input (`Rates in force`); they change each 1 April under s 15 in any case.
- **the s 32(1)(b) formula**, read as *base rate × whole years ÷ 20* (fork F3).
- **the s 43 formula**, read as *percentage × GDP − net cost* (fork F4).
These readings should be checked against the official print (open question 1).

**Inputs.** Besides those: periods resident and present (and the periods ss 9-10A treat as residence, which the chief executive decides); relationship status and household; long-term care, hospital weeks and funded care; absences, intentions and the chief executive's decisions; GDP, net cost and the contribution percentage.

### The top-level goal

`the superannuation position for` a `Superannuation case` (`nzs-goal.l4`, `@export default`) answers: *for this person on this date, are they entitled to New Zealand superannuation, from when, in which rate category, and at what weekly rate before tax?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Entitlement and rate | `is entitled to New Zealand superannuation … on …` (`@export`), `meets the residential qualification`, `the total time requirement in years for`, `the day New Zealand superannuation commences for`, `the rate category for` (`@export`), `is living alone` | ss 4A, 7-12, 17-19; Schedule 1 | `nzs-entitlement.l4` |
| 2 | Absence and payment overseas | `is payable during the temporary absence` (`@export`), `the proportion payable overseas for` (`@export`), `the Pacific rate for…` (`@export`), `the chief executive may pay during an absence of…` | ss 21-35 | `nzs-overseas.l4` |
| 3 | Rates and the Fund | `the rates meet s 16…` (`@export`), `the required annual capital contribution…`, `the most that may be withdrawn from the Fund…`, `the Minister must explain a lesser contribution…`, `the latest the next performance review may be…` | ss 15-16, 43-47, 71 | `nzs-fund.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-6 | carried as text (s 4A in Goal 1) |
| ss 7, 8, 8A, 11, 12 | Goal 1 |
| ss 9, 10, 10A | input (periods treated as residence) |
| ss 13, 14, 20 | no text in this version |
| s 15 | carried as text (rates are an input) |
| s 16 | Goal 3 |
| ss 17-19 | Goal 1 (ss 17(2)(b)-(c), (3); 19(5), (7)-(10) carried as text) |
| ss 21-24 | Goal 2 |
| ss 25, 27, 28, 30, 30A, 31, 33(1)-(1A), 34, 35, 35A | carried as text |
| s 26, 26A | Goal 2 |
| s 26B | carried as text |
| ss 29(2), 33(2) | Goal 2 |
| s 32 | Goal 2 |
| ss 36-42, 45, 46, 48-70 | carried as text |
| ss 43, 44, 47, 71(3) | Goal 3 |
| Part 3, Part 4 | carried as text |
| Schedule 1AA | carried as text (cl 7's saved non-standard couple rate is not modelled) |
| Schedule 1 | input (amounts lost) |
| Schedules 2-6 | carried as text |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 8A(3)(a) | The period "calculated in days" from the relevant date to the 65th birthday, against a requirement in years | Whole calendar years, plus any remaining days divided by 365.25 | The two must be compared in one unit; an exact anniversary should give whole years (the Act's own example gives 15); changed after the independent pass |
| F2 | s 26A | Can the proportion exceed 1? | No: capped at 1 | 540 months is the 45 years from 20 to 65, so a person cannot exceed it except through rounding of additional days |
| F3 | s 32(1)(b) | The formula (lost) | base rate × whole years since 20 ÷ 20 | The items' definitions; the base rate is reached at 20 years |
| F4 | s 43 | The formula (lost) | contribution percentage × projected GDP − expected net cost | The items' definitions |
| F5 | s 19(4) | "on and after the commencement of the 14th week" | The hospital rate applies once more than 13 weeks have passed | The text |
| F6 | s 7 | When does a person born on 29 February attain 65 in a common year? | On 28 February (the date library's year addition) | The Act is silent; the independent author read 1 March, and 1 of its assertions stays failing on this |
| F7 | s 11(1) | When does entitlement begin if residence is met after 65? | On the day the residential qualification is first met (an input) | The s 8 example meets it at 69; added after the independent pass |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `nzs-tests.l4` (encoder) | 0 | 78 | 0 |
| `tests-independent.l4` | 1 | 115 | 1 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 1 | 193 | 1 |

**1 failure is expected**, which is why `check.sh` exits non-zero: the independent author's 29 February birthday case (fork F6).

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found 3 other disagreements, all resolved in its favour: the Pacific rate below 10 years now refuses; commencement waits for the residential qualification (F7); and the refugee period counts calendar years (F1). **The encoder's tests that encoded the rejected readings were changed** and marked in `nzs-tests.l4`.

**Known limits.** The limbs of s 4A, ss 17(2)(b)-(c), 19(5), (7)-(9), 22-26 conditions, 31, 32(1)(c), 33 and 15 are inputs or text; the top-level goal does not include absence (Goal 2 answers it separately).

## 5. Open questions for a New Zealand social security lawyer

1. Confirm the s 8(4) table, the s 32(1)(b) and s 43 formulas, and the Schedule 1 rates against the official print.
2. F1: how is the s 8A(3)(a) period in days compared with a requirement in years?
3. F6: when does a person born on 29 February attain 65?
