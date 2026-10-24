# TAFDC financial eligibility (106 CMR 704.000) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `tafdc.l4`: the regulation's own terms (filing unit, assistance unit, Need Standard, Payment Standard, work-related-expense deduction, dependent care deduction, the 50% and 100% earned income disregards, the Step 7 grant) and, under `§§ Questions for the applicant or client`, the exported questions, each calling those rules. The one duty with a deadline, reporting a change in deemed income within ten days (704.235(B)(1)), is a regulative rule. One case file, `tafdc-cases.l4`; expected values worked out by hand.

There was no earlier encoding; this is the first Massachusetts subject in Commons.

## Edition

- 106 CMR 704.000 as posted by the Department of Transitional Assistance on Mass.gov on 24 October 2026 (PDF pages dated 5/10/24), at `../../registers/source-bundle/106-cmr-704-transitional-cash-assistance-financial-eligibility.txt`.
- The TAFDC Table of Need and Payment Standards that 704.410 and 704.420 say "are posted" (Mass.gov, retrieved 24 October 2026), at `../../registers/source-bundle/tafdc-table-of-need-and-payment-standards-704410-704420.txt`. The page gives no effective date for its figures; it carries the September 2026 clothing allowance note, so it was current in 2026.

**Inputs, not deposited:** which income is countable (704.210, 704.250), membership of the filing and assistance units (704.300 to 704.330), the rent allowance (106 CMR 705.910), good cause (106 CMR 701.380), a timely report (106 CMR 701.420), and the Federal Poverty Limit.

**The statute is not deposited.** M.G.L. c. 118 (and c. 18 s 10, the regulation's stated authority) is published only on malegislature.gov, which did not answer the fetcher on 2026-10-24. The encoding therefore rests on the regulation alone.

## Checks

- `tafdc-cases.l4`: 22 assertions written, 22 satisfied, 0 errors, 0 warnings. One `#TRACE` (no report by day 11) prints `BREACH` by the person whose income is deemed, as its `-- expect:` comment says.
- `tafdc.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The applicant or client**: the parent or caretaker who applies for, or receives, TAFDC for the family, and works or does not. "Does my family's income pass the test? How much TAFDC will we get this month? How much child care can I deduct?"

Defaults:

- **The instrument and the figures it brings in.** The regulation with the posted standards; the statute could not be deposited.
- **The actors the text names.** The applicant, the client, the filing unit, the assistance unit, the Department; for 704.235, the person whose income is deemed.
- **Judgments left to someone else.** Good cause (701.380) asked as a fact.
- **Definitions from facts; borrowed terms as facts.** The deductions, disregards and the Step 7 result are worked out; countable income, unit membership, the rent allowance and the poverty limit are asked.
- **One case is one family in one month.**
- **Departure.** One earner. Where more than one member of the assistance unit works, 704.500(A) Step 2 applies the disregards member by member; here the other members' countable earnings are one input.

## Scope

In: 704.260, 704.270, 704.275, 704.280, 704.281, 704.410, 704.420 (with the posted figures), 704.500(A), 704.235(B)(1) (the reporting duty only).

Out: EAEDC (704.285, 704.286, 704.430 to 704.440, 704.500(B)); assets, the EAEDC asset limit and transfers (704.110 to 704.135); deeming amounts (704.230 to 704.236); lump sums (704.240); retroactive Social Security for EAEDC (704.245); verification and averaging of income (704.290); self-employment.

## Links

TAFDC is Massachusetts's programme under Title IV-A of the Social Security Act (`subjects/us/social-security-act/`, 42 U.S.C. 601-619). SSI counts as noncountable income under 704.250 (asked as part of "countable unearned income").

## What the regulation turns out to say

1. **Step 7 states no grant for a family with no countable income.** 704.500(A) Step 7 pays "the result, if $10 or greater, but less than the applicable Payment Standard", and pays the Payment Standard where the result is "less than or equal to the applicable Need Standard, but greater than the applicable Payment Standard". The posted table gives one figure as the "Need and Payment Standard" for each size, so the second branch can never apply, and a family with no countable income gets a result exactly equal to the Payment Standard, which neither branch covers. The obvious intent is the full Payment Standard, but the text does not say so; the encoding answers `not covered`. Asserted.
2. **The income test points to sections that do not exist.** 704.260(A) compares income with "the applicable Need Standard for the exempt or nonexempt assistance unit found at 106 CMR 704.400 and 106 CMR 704.405". The chapter has no 704.400 or 704.405 (its table of contents runs 704.340, 704.410, 704.420); Step 7 cites "704.410 and 704.415", and 704.415 and 704.425 do not exist either. The posted table makes no exempt/nonexempt distinction. The encoding uses the 704.410 figures for both.
3. **The posted table has one irregular entry.** For every size the "with rent allowance" figure is $40 above the "no rent allowance" figure, except size 9: $1,738 and $1,788 ($50). The table also gives an increment of $153 for each person above 10, while the steps between sizes 1 and 10 are $142 to $151. Encoded as posted; asserted.
4. **The address for the figures is dead.** 704.410 and 704.420 say the figures "are posted at www.mass.gov/dta/TAFDCPayments"; that address answered HTTP 404 on 2026-10-24. The figures were taken from the Department's page titled "TAFDC Table of Need and Payment Standards 704.410-704.420".
5. **A cross-reference would remove the dependent care deduction from every working client.** 704.275(B)(1) denies the deduction to one who "meets the applicable provisions of 106 CMR 704.280(A) or (B) or 106 CMR 704.281(A) or (B)". 704.281(A) and (B) are the 100% and the 50% disregards themselves, so read literally no working client could deduct dependent care, contradicting 704.275(A) ("the dependent care deduction is made after the 50% disregard") and Step 3. The encoding follows 704.275(A) and Step 3 and reads the reference as meant for the disqualifying conditions (704.280(A), (B) and their counterparts in 704.281(C)(1), (2)).
6. **The work-related expense and the disqualifying conditions.** 704.270(B)(1) withholds the $200 from one who "meets the provisions of 106 CMR 704.280(A) or (B)", which are written for applicants. For a client's grant the encoding applies the same facts (reduced or left work, or late report, without good cause), since 704.281(C)(1), (2) state them again for clients.
7. **The 50% disregard at application needs recent TAFDC.** 704.280 gives it only to "an applicant who has received TAFDC within the last four calendar months"; a first-time applicant's earnings count in full after the $200 and dependent care. Asserted.

## Before relying on it

- Deposit M.G.L. c. 118 when malegislature.gov answers, and 106 CMR 701, 703 and 705 (good cause, timely reports, the rent allowance).
- Several earners; the EAEDC half of the chapter.
- An independent test pass, and a person's check of findings 1, 2 and 5 with the Department.
