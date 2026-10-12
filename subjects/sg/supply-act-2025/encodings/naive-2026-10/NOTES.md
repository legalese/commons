# Supply Act 2025 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table, no
independent test pass, no human gate. NOT for public use.

**Edition:** No. 11 of 2025, as deposited at `../../registers/source-bundle/SA2025.txt`.
Every page is marked "Informal Consolidation – version in force from 1/4/2025"; the
retrieval record says "Current version as at 01 Oct 2026". No amendment is annotated.

**Checks:** one case file, 50 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

Requirement **REQ-0222** in `subjects/sg/requirements.jsonl`: tier 3 of the remaining
Singapore Acts, ordered by everyday-life relevance. The requirement asks what the Act
decides for a person or business it applies to; no scenario has asked a sharper
question yet.

It is not scoped: the Act is three sections and a Schedule, and all of it is encoded —
commencement (s 1), the two ceilings and the period (ss 2, 3), and the 23 Heads of
Expenditure with their Consolidated Fund, Development Fund and total figures. Not
encoded: who issues money and how (the Constitution and the Financial Procedure Act,
not read), and the Supplementary Supply (FY 2025) Act 2026, deposited as a separate
subject and not read.

## What the Act turns out to say

### 1. It decides nothing for a person or business

The Act authorises sums "to be issued" from two Funds and appropriates them to Heads of
Expenditure. It confers no right, imposes no duty, creates no offence and names no
person outside government. The answer to REQ-0222's question is "nothing directly":
whatever a citizen receives under a Head is decided by other law. The encoding can only
say whether an issue or charge fits within the figures.

### 2. Two hard ceilings, one financial year

s 2(1): "not more than $139,804,307,900" from the Consolidated Fund; s 3(1): "not more
than $39,236,834,600" from the Development Fund; both "for the period starting 1 April
2025 and ending 31 March 2026". The Act comes into operation on 1 April 2025 (s 1).
Treating the ceiling as cumulative over the period, and treating the Head figures as
caps on charges to each Head, are labelled inferences in the `.l4`. Asserted.

### 3. The Schedule adds up — once it is rebuilt

The deposit's text layer is column-shifted: figures for different Heads share a line,
and totals stand beside the wrong names. Rebuilt by order and arithmetic (each
Consolidated Fund figure paired with the unique Development Fund figure that gives a
printed total), all 23 printed totals are reproduced, the Consolidated Fund column sums
to exactly the s 2(1) figure, the Development Fund column to exactly the s 3(1) figure,
and together they give the printed grand total of $179,041,142,500. Asserted (23 head
totals and both column sums).

### 4. The biggest Head is not a ministry

Head Z, Financial Transfers, takes $42,623,333,500 from the Consolidated Fund and nothing
from the Development Fund — more than Defence ($24,326,073,300 in all) or Health
($20,863,215,900). Asserted (its total and the absence of a development appropriation).

### 5. Some ministries are mostly development

National Development gets $11,140,637,200 from the Development Fund against
$8,344,980,000 from the Consolidated Fund; Transport $12,528,311,800 against
$2,798,018,900. Cabinet Office, Presidential Councils and Financial Transfers have no
development appropriation (the deposit prints "..." or nothing; recorded as 0, an
inference from the printed total). Asserted.

### 6. Gaps in the lettering

The Heads run B to Z without A, H or Y. The text does not say why.

## What would need doing before this is worth anything

- The PDF was not compared with the rebuilt Schedule; the pairing is by arithmetic and
  order only, and a pairing that happens to add up could still be wrong.
- The Supplementary Supply (FY 2025) Act 2026 presumably adds to these figures (an
  inference from its title); it was not read, and nothing here combines the two.
- The Constitution's and the Financial Procedure Act's rules on issue, virement and
  lapse were not read, so the two "within the figure" predicates are readings, not law.
