# Washington capital gains tax (chapter 82.87 RCW) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual who sells long-term capital assets, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding to keep; the text was first deposited on 2026-10-24 (commit `3266cda0d`).

## Edition

Chapter 82.87 RCW as printed on the full-chapter page of app.leg.wa.gov/RCW, retrieved 2026-10-24T02:52Z, deposited at `../../registers/source-bundle/rcw-82-87.txt` (unofficial; 18 sections; history to 2026 c 191 and 2026 c 268).

**Annual amounts.** The Department of Revenue adjusts the standard deduction, the charitable floor and cap, and the family-business revenue ceiling each October and publishes them on its website (RCW 82.87.150). That publication is not deposited, so these are **inputs**; each `@desc` names the printed figure. The cases use the printed figures, except one hypothetical adjusted deduction.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wa-capital-gains.l4` | `wa-capital-gains-cases.l4` | 37 written, 37 satisfied |

Plus six `#TRACE`s of the three regulative rules with `-- expect:` comments (three FULFILLED, three breaches by the taxpayer, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The individual seller** (or a married couple or registered domestic partners) of stocks, bonds or other long-term capital assets. Questions: "Does Washington tax my wages?", "Am I a resident?", "Is this sale exempt?", "Is the gain allocated to Washington?", "How much do I owe?", "Must I file, jointly?", "What is the late-filing penalty?", and, as rules with deadlines, filing, payment and amendment.

Defaults (2026-10-18):
- **The Act alone**: chapter 82.87; the Department's annual figures would be brought in if deposited (inputs).
- **Actors**: the taxpayer and the Department of Revenue.
- **Judgments left to others**: the Department's satisfaction with evidence of a federal extension (82.87.110(5)) and the penalty waivers (82.87.110(6)(b)) are asked as facts.
- **Definitions**: resident, exemption, allocation, adjusted capital gain and Washington capital gains are worked out from facts; federal net long-term capital gain is borrowed and asked.
- **One case**: one return for one taxable year.
- **Machinery out**: distribution of revenue, the treasurer's transfers, brokers' reporting, criminal penalties.

## Washington has no wage income tax

None of the deposited Washington text imposes a tax on wages or ordinary income, and the README's index check found no such statute. Chapter 82.87 is an **excise** "on the sale or exchange of long-term capital assets" that "Only individuals are subject to" (82.87.040(1)(a)); it is the one tax on an individual's income. The encoding answers "Does Washington tax my wages?" with no, as a finding of the deposited law, not of the constitution or case law (the Washington constitutional history is general knowledge, unverified, and not relied on).

## Read with the federal encodings

The starting point is federal net long-term capital gain, "determined as if Title 26 U.S.C. Secs. 55 through 59, 164, 1256, 1400Z-1, and 1400Z-2 ... did not exist" (82.87.020(3)), under the Internal Revenue Code "as of July 25, 2021, or such subsequent date as the department may provide by rule" (82.87.020(6)). It is an input; the federal text is in `subjects/us/internal-revenue-code-of-1986/`.

## Scope

**In:** 82.87.020(1), (3), (11), (16); 82.87.040(1), (3); 82.87.050 (as a list); 82.87.060; 82.87.070 (as an amount); 82.87.080; 82.87.100; 82.87.110(1), (3), (5), (6)(a)-(b), (8) (rules for filing, payment, amendment); 82.87.120(1)-(2), (4) (the share of the standard deduction); 82.87.160 (the B&O credit).

**Out:** 82.87.010, 030, 090, 115, 130, 140, 150 (except as the source of the inputs), 170; 82.87.040(4); 82.87.050(2) valuation; 82.87.070 qualification tests; 82.87.110(2), (4), (7), (9); chapter 82.32 RCW (interest and late-payment penalties, not deposited).

## What the chapter turns out to say

1. **No wage income tax; a 7 percent excise on long-term capital gains, plus 2.9 percent on Washington capital gains above $1,000,000 from 2025** (82.87.040(1)). $1,500,000 of gains: $94,750 in 2026, $87,500 in 2024. Asserted.
2. **One standard deduction for a couple.** "In the case of spouses or domestic partners, their combined standard deduction is limited to $250,000, regardless of whether they file joint or separate returns" (82.87.060(1)), and their assets are combined "as if they were one individual" for every threshold (82.87.120(4)(a)). Spouses filing separately share it. Asserted (half each).
3. **The $1,000,000 threshold is not indexed, though the deductions are.** RCW 82.87.150(2)(a) lists the "applicable amounts" adjusted each October (the distribution amount, the standard deduction, the family-business revenue ceiling, the charitable floor and cap); the $1,000,000 in 82.87.040(1)(b) is not among them. As the standard deduction rises, the 2.9 percent band therefore starts at a fixed figure.
4. **A cross-reference in RCW 82.87.150 points at a definition, not a deduction.** It names "The standard deduction amount in RCW 82.87.020(16) and 82.87.060(1)". RCW 82.87.020(16) is the definition of "Washington capital gains", which contains no amount. The reference is harmless (the amount is in 82.87.060(1)) but wrong.
5. **The charitable deduction is a band.** Only donations to organisations "principally directed and managed within the state of Washington" above the floor ($250,000 printed) count, up to the cap ($100,000 printed), with no carry-over (82.87.080). Giving $400,000 deducts $100,000; giving $300,000 deducts $50,000. Asserted.
6. **Gains on intangibles follow domicile; gains on tangible property follow its location** (82.87.100(1)). A painting moved out of the state before sale is still allocated to Washington if it was there during the year or the year before, the seller is a resident, and no other jurisdiction taxes the gain. Asserted.
7. **Filing follows the federal extension; payment does not.** The return is due on the federal due date, or the federal extension date if evidence of it is given by the due date (82.87.110(1), (5)); the tax is due by the original date "regardless of any filing extension" (82.87.110(3)). A late return costs 5 percent of the tax a month, up to 25 percent, unless waived (82.87.110(6)). A final federal change must be reflected in an amended return within 90 days (82.87.110(8)). Traced and asserted.
8. **Only taxpayers who owe tax must file** (82.87.110(1)(a): "taxpayers owing tax under this chapter must file"). A seller whose gains are within the standard deduction has no return to file. Asserted.

## Before relying on it

- Deposit the Department of Revenue's published annual amounts and test with them.
- Deposit chapter 82.32 RCW for interest and late-payment penalties.
- Encode the 82.87.050(2) valuation and the 82.87.070 qualification tests.
- An independent test pass.
