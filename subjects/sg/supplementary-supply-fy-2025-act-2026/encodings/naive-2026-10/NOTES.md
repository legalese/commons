# Supplementary Supply (FY 2025) Act 2026 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill conventions and nothing else. No pipeline, no coverage table, no independent
test pass, no human gate. NOT for public use.

**Edition:** informal consolidation, "version in force from 20/3/2026", deposited at
`../../registers/source-bundle/SSFY2025A2026.txt` (SSO: "Current version as at 01 Oct
2026"). No amendment is annotated and no historical version is listed.

**Checks:** one case file, 44 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

**Requirement REQ-0221** in `subjects/sg/requirements.jsonl`: Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to. No scenario has asked
a sharper question yet.

The Act is four sections and a Schedule, so the whole of it is encoded except s 1
(short title): the meaning of FY 2025 (s 2), the two ceilings (ss 3, 4) and the
eleven Heads of Expenditure in the Schedule. Not encoded: the Supply Act 2025 it
supplements, the Constitution's provisions on supply and the Financial Procedure
Act. None of them was read.

## What the Act turns out to say

### 1. It decides nothing for a person or business

The answer to REQ-0221's question is: nothing directly. The Act authorises the
Government to issue further sums and says for which Heads. It creates no right,
duty, fee, deadline, offence or remedy for anyone outside government. What a person
might meet is a programme funded under one of these Heads, and the Act does not
name any programme.

### 2. $3.25 billion more, in force eleven days before the year ends

s 3(1) authorises up to **$1,087,355,800** from the Consolidated Fund and s 4(1) up to
**$2,161,019,900** from the Development Fund, both "not otherwise provided for by the
Supply Act 2025". The Schedule's grand total is **$3,248,375,700**. The version in
force runs from 20 March 2026, eleven days before FY 2025 ends on 31 March 2026
(s 2). Both 1 April 2025 and 31 March 2026 are inside FY 2025. Asserted.

### 3. Two thirds is development money, and most of it goes to two Ministries

The Development Fund sum is roughly twice the Consolidated Fund sum. On the order
matching (finding 5), the Ministry of Transport takes $1,137,286,200 and the
Ministry of National Development $909,322,000 from the Development Fund: together
about 95% of it. The largest Consolidated Fund items are Home Affairs ($472,103,300)
and Manpower ($346,483,200). Asserted, figure by figure.

### 4. The Schedule adds up exactly to the sections

Computed from the eleven rows, the Consolidated Fund column is exactly the s 3(1)
ceiling, the Development Fund column exactly the s 4(1) ceiling, and their sum the
printed total. The three Heads drawing on both funds (L, S, W) have row totals equal
to their printed totals. Asserted.

### 5. The Schedule is a column-shifted table; Heads were matched by order

In the PDF and its text the figures sit one line out of step with the Head names
(the Ministry of Sustainability and the Environment's total is on its own line, its
two components on the Home Affairs line). The eleven rows of figures were matched to
the eleven Heads **by order**. This is an inference. It is consistent with every row
adding up and the columns matching ss 3 and 4, but those sums would also hold under
other labellings, so they do not prove which Head carries which figure. One reading
detail is decided by arithmetic: the Attorney-General's Chambers' $364,800 is
Development Fund money. Read as Consolidated Fund, the column would overshoot the
s 3(1) ceiling by exactly $364,800.

### 6. Spending under a Head is capped by its column (inference)

The Act appropriates the sums "for the Heads of Expenditure ... specified in the
Schedule". The encoding infers that a Head can be charged only up to its figure in
the column for that fund, and not at all from a fund whose column shows "..." or
under a Head the Schedule does not name. The Act does not say this in terms.
Asserted as an inference.

## What would need doing before this is worth anything

- Check the Head-to-figure matching against the SSO HTML table or the Supplementary
  Estimates paper, which would settle finding 5.
- Read the Supply Act 2025, the Constitution's supply provisions and the Financial
  Procedure Act, which give the Act its legal effect (virement, lapse at year end,
  what "issued" means).
- Find which programmes the sums fund. Only then does the Act connect to anything a
  person would meet.
