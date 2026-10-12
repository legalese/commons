# Supply Act 2026 — naive encoding

**Method: naive.** Straight from the deposited text, following the conventions of
the `writing-l4-rules` skill as shown in the finished naive rows (the skill itself
was not loadable in this session). No pipeline, no coverage table, no independent
test pass, no human gate.

**Edition:** Act 6 of 2026, informal consolidation, "version in force from
1/4/2026", retrieved 1 October 2026 ("Current version as at 01 Oct 2026"). The
deposit annotates no amendment. The Schedule's figures were read from the deposited
PDF (`SA2026.pdf`), not the deposited `.txt`; see finding 2.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is **REQ-0223** in the requirement ledger: Tier 3 of the remaining Singapore
Acts, ordered by everyday-life relevance. The requirement asks what the Act decides
for a person or business it applies to; no scenario has asked a sharper question
yet. The Act is three sections and a two-page Schedule, so the row takes all of it:
commencement (s 1), the ceilings on issue from the Consolidated Fund and the
Development Fund (ss 2, 3) and the sum appropriated to each of the 23 Heads of
Expenditure. Nothing outside the deposit is encoded: not the Constitution, the
Financial Procedure Act, the Development Fund Act, the Estimates or the subheads
beneath each Head.

## What the Act turns out to say

### 1. It decides nothing for a person or business

The answer to REQ-0223 is that the Act confers no right, duty, entitlement, offence
or remedy on any private person. Every operative verb is addressed to the
Government's Funds: a sum "is authorised to be issued" and "is appropriated for the
Heads of Expenditure". A person's interest in it is indirect, through what the
Ministries then spend under other law. Asserted.

### 2. The deposited text scrambles the Schedule; the PDF reconciles exactly

In `SA2026.txt` the Schedule's figures drift between rows and columns (for example,
Judicature appears with no Consolidated Fund figure and Cabinet Office with a
Development Fund figure). Read from the deposited PDF with `pdftotext -table`, every
Head's two appropriations add to its printed total, the Consolidated Fund column adds
to the $158,962,520,000 in s 2(1), the Development Fund column to the $49,014,559,600
in s 3(1), and the grand total is $207,977,079,600. All four checks are computed by
the encoding, not copied. Asserted.

### 3. Three Ministries get more from the Development Fund than the Consolidated Fund

National Development ($13,613,535,500 against $8,640,058,800), Trade and Industry
($10,705,745,500 against $1,861,722,800) and Transport ($13,306,280,300 against
$3,109,174,200). Health and Defence draw mainly on the Consolidated Fund. Asserted.

### 4. The largest Head is not a Ministry

Head Z, Financial Transfers, takes $55,395,577,200, all from the Consolidated Fund,
more than Defence ($23,343,497,600) or Health ($20,035,377,700). The Act does not say
what the transfers are. The figure is asserted; the comparison is not separately.

### 5. The authority is bounded by the financial year, and by "not more than"

The Act comes into operation on 1 April 2026 (s 1), and both sums are authorised
"for the period starting 1 April 2026 and ending 31 March 2027". An issue dated
1 April 2027, or one that takes the period's issues past the ceiling by a dollar, is
outside ss 2(1) and 3(1). Asserted.

### 6. Two readings are inferences, and are labelled so

The Schedule prints "..." for the Development Fund under Cabinet Office, the
Presidential Councils and Financial Transfers; it is read as nil because the totals
add up only on that reading. And the Act does not say in terms that issue for a Head
is capped at that Head's sum; the per-Head rule is encoded as an inference. The
lettering runs B to Z with no A, H or Y; the text gives no reason. The per-Head cases
are asserted against the inference.

## What would need doing before this is worth anything

- The Act's machinery lives elsewhere: the Constitution's supply provisions, the
  Financial Procedure Act and the Development Fund Act would need encoding before
  the per-Head reading in finding 6 could be confirmed or rejected.
- Any Supplementary Supply Act for FY2026 would change the figures; none was looked
  for.
- The column-scrambled `.txt` in the source bundle should be flagged for whoever
  maintains the deposits.
