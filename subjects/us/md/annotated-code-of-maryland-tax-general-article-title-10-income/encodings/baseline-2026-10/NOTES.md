# Maryland income tax (Tax-General Title 10) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `mdit.l4`, holds the seat-neutral rules in the statute's own terms (resident, Maryland adjusted gross income, exemptions, Maryland taxable income, State income tax, county income tax, the credits) and, under `§§ Questions for the taxpayer` and the filing headings, the exported questions with `@export` and `@desc`, each calling the rules rather than restating them. The filing duty of ss 10-805 and 10-820 is also written as a regulative rule (`DEONTIC`), with the resident as the party. One case file, `mdit-cases.l4`; its expected values were worked out by hand from the text, with the arithmetic in a comment beside each case.

There was no earlier encoding of this subject.

## Edition

The Annotated Code of Maryland as served by the General Assembly at mgaleg.maryland.gov with "Include enactments of the last session: Yes", i.e. **the Code as in effect on 1 October 2026**, after the 2026 Regular Session:

- `../../registers/source-bundle/tax-general-title-10-subtitles-1-2-rates-and-maryland-taxable-income.txt` (ss 10-101 to 10-223, deposited 2026-10-20);
- `../../registers/source-bundle/tax-general-title-10-subtitle-7-individual-credits.txt` (ss 10-701 to 10-758 selected, deposited 2026-10-20);
- `../../registers/source-bundle/tax-general-title-10-subtitle-8-returns.txt` (ss 10-804 to 10-823, **deposited 2026-10-24 for this encoding**).

The rate schedule in s 10-105(a), the flat standard deduction in s 10-217(b), the exemption limits in s 10-211(c) and the 2% addition on net capital gain in s 10-105(a)(3) are the text as served; the register prints no applicability dates for them. The encoding applies them to taxable years beginning in 2025 and 2026 and answers `not covered` for any other year: whether they also governed 2024 is not visible in the deposited text.

**Figures set outside the deposited text, taken as inputs:**

- the Comptroller's cost-of-living adjustment for the standard deduction for 2026 (s 10-217(c)); none is deposited;
- each county's income tax rate (s 10-106: the county sets it by ordinance or resolution, between 2.25% and 3.30%);
- the federal figures: federal adjusted gross income, the federal earned income credit (IRC s 32), the IRC s 6012(a) filing amounts, and the HHS poverty guideline used by s 10-709.

## Checks

- `mdit-cases.l4`: 60 assertions written, 60 satisfied, 0 errors, 0 warnings. One `#TRACE` (the filing duty with no return by day 106) prints `BREACH` by the resident, as its `-- expect:` comment says; a breached trace cannot be asserted in the stable l4.
- `mdit.l4`: 0 errors, 0 warnings.
- Both run with the stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset (`l4 run <file>`; the exit code is 0 even on failure, so the diagnostics were read).

## Seat

**The individual Maryland resident**, or the married couple on a joint return, who asks: "Am I a resident? Must I file, and by when? What State and county income tax do I owe, and what earned income, poverty-level and child tax credits do I get back?"

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The rates, exemption amounts, standard deduction, credit percentages and the child tax credit are statutory. The instruments that set the remaining numbers (county ordinances, the Comptroller's adjustment, federal figures) are not deposited; those numbers are inputs.
- **The actors the text names.** Followed: the resident (the "individual" and "taxpayer"), the county, the Comptroller.
- **A judgment handed to someone else, answered conditionally.** Followed for s 10-807(b)(4) ("the Comptroller determines circumstances warrant"), asked as a fact.
- **Definitions worked out from facts; borrowed terms asked as facts.** "Resident" (s 10-101(k)(1)(i)), Maryland adjusted gross income, Maryland taxable income, the exemptions and the "eligible low income taxpayer" (s 10-709(a)(3)) are worked out. Federal terms (federal AGI, the s 32 credit, s 152 dependant, s 2 filing status, s 6012(a)) are asked.
- **One case is one return** for one taxable year.
- **The Act's own terms**, each with a plain gloss in the comments.
- **Machinery out**: the Comptroller's reports (s 10-108(b)), distribution (s 10-106.1(c)), county procedure for setting rates (s 10-106(a)(3), (b)).

**Departure:** where the person may elect between the standard deduction and itemizing (s 10-217(a)(1), s 10-218(a)), the encoding takes the larger allowed deduction rather than asking which was elected, since that is the election that lowers the tax. A person who elects otherwise would get a different answer.

## Scope

In: ss 10-101(i), (k), 10-102, 10-103(a)(1), 10-105(a)(1)-(4), (c), 10-106(a)(1), 10-201, 10-203, 10-207(a), (j), 10-211, 10-217, 10-218, 10-704(b)-(d), 10-706(c), 10-709(a)-(d), 10-751, 10-805(a), (b), 10-807, 10-820(a)(1), (3).

Out: nonresidents and part-year residents (ss 10-101(k)(2), 10-105(d), 10-219, 10-704(e), 10-709(e)); fiduciaries; an individual claimed as an exemption on another's return; counties that tax on a bracket basis (s 10-106(c)); s 10-106.1 (the tax on a resident not subject to a county tax); the additions of s 10-204 and the subtractions of ss 10-207 to 10-210 other than s 10-207(j) (asked as totals); the other credits of Subtitle 7, including withholding (s 10-701) and taxes paid to other states (s 10-703); estimated tax and withholding returns (ss 10-815 to 10-822); the extension of s 10-823; interest and penalties (Title 13, not deposited).

## Link to the federal encoding

Maryland starts from federal adjusted gross income "as determined under the Internal Revenue Code" (s 10-101(e)) and keys its earned income credit to IRC s 32, its poverty-level credit to IRC s 32(c)(2), its dependants to IRC s 152 and its filing duty to IRC s 6012(a). Those come from `subjects/us/internal-revenue-code-of-1986/` (being encoded on 24 October 2026). Cross-folder IMPORT does not work in the stable l4, so they are inputs here.

## What the Act turns out to say

1. **The child tax credit's phase-out cannot operate.** s 10-751(b) allows the credit to a resident "and has federal adjusted gross income lower than the threshold amount of $15,000"; (c) reduces it "by $50 for each $1,000, or fraction thereof, by which the taxpayer's federal adjusted gross income exceeds the threshold amount". Under (b) no claimant's income exceeds the threshold, so (c) never reduces anything and the credit stops dead at $15,000 (a family at $14,999 gets $500 per child, at $15,000 nothing). The reduction is encoded as written; asserted at $14,999 and $15,000.
2. **The 2% capital-gain addition turns on federal AGI, not Maryland income.** s 10-105(a)(4) applies (a)(3) only to individuals "with a federal adjusted gross income in excess of $350,000", so a resident whose Maryland subtractions bring Maryland income far below that still pays it, and one at exactly $350,000 does not. Asserted.
3. **Joint-return exemptions.** s 10-211(a) gives an exemption for "(1) the taxpayer" and "(2) the spouse" only where "a joint return is not made". The text does not say in so many words that a joint return carries two "taxpayer" exemptions; the encoding counts each spouse on a joint return as a taxpayer (2 exemptions), the reading that makes (a)(2)(i) meaningful. Likewise the additional $1,000 for age 65 and blindness ((b)(3), (4)) is counted per spouse.
4. **A wrong cross-reference in the poverty-level credit.** s 10-709(a)(3)(iv) requires that "the credit allowed under s 10-704(a)(1) of this subtitle is less than the State income tax". s 10-704(a)(1) is the definitions lead-in ("In this section the following words have the meanings indicated"); the credit against the State tax is s 10-704(b)(1), which s 10-709(c)(1) itself cites. Encoded as s 10-704(b)(1). Consequence, asserted in case C: a low-income parent whose State earned income credit already wipes out the State tax gets no poverty-level credit against the *county* tax either, because (iv) is a condition of being an "eligible low income taxpayer" for both.
5. **"Total tax otherwise payable".** For an individual without a qualifying child, s 10-704(c)(3)(iv) refunds the excess of the 100% credit over "the total tax otherwise payable", where (c)(3)(ii) makes it a credit "against the State income tax". The encoding reads "total tax" as the State income tax, since the county credit has its own rule in (d). If "total tax" meant State plus county tax, the refund would be smaller.
6. **No poverty guideline in the Code.** s 10-709 takes "the most recent poverty income guideline published by the United States Department of Health and Human Services, available as of July 1 of the taxable year" for the number of s 10-211(b)(1) exemptions. It is an input.
7. **The filing threshold leaves out Social Security.** s 10-805(a) tests the federal filing duty "after exclusion of Social Security and railroad retirement benefits", matching the full subtraction of those benefits in s 10-207(j); a retiree living on Social Security alone need not file. The s 6012(a) amounts themselves are federal inputs.

## Before relying on it

- Encode the federal inputs (AGI, the s 32 credit) from the IRC encoding and check them against these cases.
- Deposit and encode the county rate ordinances (or the Comptroller's published county rate table) and the 2026 cost-of-living adjustment.
- Add the additions and subtractions (ss 10-204 to 10-210), especially the pension exclusion (s 10-209), part-year residents, bracket-basis counties, s 10-106.1, and the other individual credits.
- An independent test pass, and a person's check of findings 3 to 5.
