# NOTES: the Income Tax Act 2007 (New Zealand), personal income tax, row `legalese-aswathy`

**Draft. No New Zealand lawyer or tax adviser has reviewed this encoding against the Act.**

## What is encoded

The personal income tax calculation for a natural person under the Income Tax Act 2007 (version as at 4 September 2026, from the text converted from the PCO XML). It sits under one top-level goal, `the tax position for` (`it-goal.l4`). For a person and a tax year it answers: whether they are resident, their annual gross income, net income or net loss, taxable income, income tax liability, independent earner tax credit, and how their credits are used (terminal tax, refund, credits extinguished or left over). Four goals sit under it:

1. **Residence** (`it-residence.l4`): ss YD 1 and YD 1B(2).
2. **Taxable income and liability** (`it-liability.l4`): ss BC 1-BC 7 and Schedule 1, part A, clause 1.
3. **Credits, terminal tax and refunds** (`it-credits.l4`): ss BC 8, LA 2-LA 7, LC 13-LC 15.
4. **Secondary tax codes** (`it-codes.l4`): Schedule 2, part A, clauses 1-9.

Modules: `it-types.l4` (nouns only), `it-residence.l4`, `it-liability.l4`, `it-credits.l4`, `it-codes.l4`, `it-goal.l4`; tests in `it-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** Everything else in the Act's roughly 38,000 lines: what counts as income or a deduction (Parts C-E), timing, tax losses (Part I), entities (Part H), PIEs, FBT, RWT and NRWT, ESCT, Working for Families (Part M), imputation (Part O), the PAYE rules themselves (Part R) and Schedules 3 onwards. The amounts they produce are inputs. So are the Commissioner's PAYE tables for the M and ME codes.

**Lost in conversion.** Schedule 1, part A, table 1 (the brackets), which is an input; the tests use the 2026-27 table built from the thresholds the Act quotes elsewhere. The LC 13-LC 15 formula. The Schedule 1 clause 1 formula.

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| YD 1(2) | permanent place of abode | encoded |
| YD 1(3)-(4) | 183 days | encoded (the day count and its first day are inputs) |
| YD 1(5)-(6) | 325 days | encoded (likewise) |
| YD 1(7) | Government service | encoded |
| YD 1(8) | part days | inert: applied in counting the input days |
| YD 1(9) | seasonal workers | encoded |
| YD 1(10) | trustees | inert |
| YD 1(11)-(12) | non-resident visitors | encoded: (11); (12)'s later start is not |
| YD 1B(2) | non-resident visitor | encoded ((f)-(h) added after the independent pass); YD 1B(3)-(5) not |
| BC 1 | non-filing and filing taxpayers | encoded |
| BC 2 | annual gross income | encoded |
| BC 3 | annual total deduction | encoded (an input) |
| BC 4 | net income and net loss | encoded |
| BC 5 | taxable income | encoded |
| BC 6 | liability of a filing taxpayer | encoded |
| BC 7 | schedular income | encoded: (1)-(2) with the schedular liability as an input; (4)-(5) PIEs not |
| BC 8 | satisfaction by credits | encoded |
| LA 2-LA 4 | using credits | encoded (the R&D credits in LA 4(1)(d)-(e) are not) |
| LA 5 | remaining credits | encoded: extinguishing (2) and refunding (6); (3)-(5) shown as remaining amounts |
| LA 6-LA 7 | refundable credits | encoded: the refund before any set-off against other years |
| LD 1(5) | donation credits outside LA 2-LA 6 | encoded: refunded whole (added after the independent pass) |
| LA 8-LA 10 | NRWT, life insurers, definitions | out of scope |
| LC 13 | independent earner tax credit | encoded |
| LC 14-LC 15 | the 2024-25 split | encoded |
| Schedule 1, part A, cl 1 | basic rate: natural persons | encoded, with table 1 as an input |
| Schedule 1, part A, cls 2-17 | other persons | out of scope: not natural persons' basic rate |
| Schedule 2, part A, cls 1-9 | PAYE for tax codes | encoded (cls 1-2 refused: the Commissioner's tables) |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | Schedule 1, part A, cl 1 | Are cents of taxable income taxed? | No: only whole dollars | "taxable income means the number of dollars in the person's taxable income"; table 1 applies "for each dollar" |
| F2 | ss LC 13(2), LC 14-LC 15 | The formulas lost in conversion | (credit − abatement) × whole months ÷ 12; for 2024-25, each part × whole days ÷ 365 | The items each section defines; 2024-25 has 365 days |
| F3 | s BC 5 | Can a tax loss take taxable income below zero? | No | Part I subtracts a loss from net income only so far as it extends (s IA 4) |
| F4 | s BC 7 | How is the non-schedular liability found? | Table 1 applied to taxable income less schedular income | "the amount that would be their income tax liability for the year if they had no schedular income" |
| F5 | ss LC 13-LC 15 | A tax year before 2024-25 | Refused | The text as at 4 September 2026 states only the 2024-25 and later rules |
| F6 | s LA 5(3)-(4) | Supplementary dividend and imputation credits left over | Reported as remaining amounts | Their use (LP 3, LE 2-LE 3) is out of scope |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `it-tests.l4` (encoder) | 0 | 63 | 0 |
| `tests-independent.l4` | 0 | 120 | 0 |
| the 6 rule modules | 0 | 0 | 0 |
| **total** | 0 | 183 | 0 |

The independent pass (`INDEPENDENT-TEST-REPORT.md`) failed no assertion but found two gaps, both fixed: YD 1B(2)(f)-(h) were missing from the non-resident visitor test, and donation credits were being used against the liability despite s LD 1(5). No encoder test had encoded either point; tests for both were added.

**Known limits.** Day counts for residence, all income, deduction, loss and credit amounts, and table 1 are inputs. The Schedule 1 rates for persons other than natural persons are text only. Refunds are shown before any LA 6(2) set-off against other years.

## Open questions for a New Zealand tax adviser

1. F2: what are the LC 13-LC 15 formulas? The converted text lost them.
2. F1: does Schedule 1 tax only whole dollars, ignoring cents?
