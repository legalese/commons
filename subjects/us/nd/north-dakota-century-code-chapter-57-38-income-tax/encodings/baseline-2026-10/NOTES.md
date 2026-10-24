# North Dakota Century Code chapter 57-38 (individual income tax) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A part-year resident or nonresident answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the statute's own terms in `nd-pit.l4`. The taxpayer's questions are in `nd-pit-seat.l4`, which IMPORTs the core and calls its rules. Each question has `@export` and every input a `@desc`. There was no earlier encoding of this chapter to keep.

## Edition

N.D.C.C. ch. 57-38, the Legislative Council's 07/01/25 update (all changes approved by the 69th Legislative Assembly, 2025 session), deposited on 2026-10-20 at `../../registers/source-bundle/ndcc-t57c38.txt` (from the chapter PDF; see its `.meta.json`). The rate schedules are deposited as `| a | b |` rows, and were read from those rows.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `nd-pit.l4`, `nd-pit-seat.l4` | `nd-pit-cases.l4` | 31 written, 31 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. One `#TRACE` shows a breach (a federal change reported on day 100), with its expected result in an `-- expect:` comment. Every expected value was worked by hand from the text.

## Seat

**The individual taxpayer**: "Am I a North Dakota resident? Must I file? By when? How much North Dakota tax do I pay? Do we get the marriage penalty credit?"

The Tax Commissioner's duties are encoded as what they mean for that person. The indexed schedules and the indexed maximum credit the commissioner prescribes are inputs the person reads off the commissioner's forms.

The 2026-10-18 defaults:

- **The Act alone.** Chapter 57-38 only.
- **The actors the text names:** the taxpayer, the tax commissioner.
- **Judgments left to others:** none needed in the encoded sections. The commissioner's prescribed schedules are facts (inputs).
- **The Act's own definitions are worked out from facts:** resident (s 57-38-01(11)), North Dakota taxable income (s 57-38-30.3(2)), qualifying income of the lesser-earning spouse (s 57-38-01.28(4)). **Borrowed federal terms are asked as facts:** federal taxable income, filing status, the IRC s 86 amount, the IRC s 151(d) and s 63(c)(2)(A) amounts, the federal filing requirement.
- **One case:** one return for one year.
- **The Act's own terms**, quoted in the comments.
- **Machinery out:** forms, the optional simplified method ((1)(h)), the tax tables ((10)), administration.

## Regulative rules

Two, in `nd-pit.l4`:

1. `my duty to file and pay` (ss 57-38-34(2), 57-38-35): the taxpayer MUST file the return, and MUST pay the tax computed on it, each WITHIN the days from 31 December to 15 April, joined by RAND, each with `LEST BREACH ... BECAUSE`.
2. `my duty to report a federal change` (s 57-38-34.4): after an IRS change becomes final, the taxpayer MUST report it by an amended state return WITHIN 90 days (subsection 1). After filing an amended federal return, the taxpayer MUST file an amended state return with a copy WITHIN 90 days (subsection 2).

## Scope

**In:** s 57-38-01(11); s 57-38-31(1); s 57-38-34(2); s 57-38-35; s 57-38-34.4; s 57-38-30.3(1)(a)-(d) and (g), (2)(a), (d), (e), (g), (r), (s) with the other (2) adjustments as inputs, (3); s 57-38-01.28.

**Out:** part-year residents and nonresidents ((1)(f), `not covered`); estates and trusts ((1)(e)); the credit for tax paid to another state ((4)); farm income averaging ((9)); every other credit listed in s 57-38-30.3(7); the 30%-of-all-dividends alternative in (2)(d)(2); corporate income tax; withholding, estimated tax, interest and penalties.

Read with the federal Internal Revenue Code encoding, `subjects/us/internal-revenue-code-of-1986/` (being encoded by another session on 2026-10-24). North Dakota starts from federal *taxable* income, so the federal standard deduction and exemptions come through it. Cross-folder IMPORT is not possible in the stable `l4`.

## What the chapter turns out to say

1. **North Dakota starts from federal taxable income, not AGI** (s 57-38-30.3(2)), and has no standard deduction or personal exemption of its own. The federal deduction comes through federal taxable income. The filing status must be the federal one ((3); s 57-38-31(2)). Asserted.
2. **Federally taxable social security is fully excluded** ((2)(s)), and so are military retirement benefits ((2)(r)) and active-duty, guard and reserve pay ((2)(g)). Asserted.
3. **The printed rate schedules are not the ones a taxpayer uses.** Subdivision (1)(g) says "The tax commissioner shall prescribe new rate schedules that apply in lieu of the schedules set forth in subdivisions a through e", indexed each year by the federal s 1(f) cost-of-living adjustment, with the rates unchanged. The text does not say which year the printed figures belong to. The encoding therefore offers both: the tax on the printed schedule, and the tax on a schedule whose two thresholds the person reads from the commissioner's forms. The 2026 thresholds are not deposited. Asserted (both questions; the printed figures given as inputs reproduce the printed schedule).
4. **The printed top-row bases are rounded to the cent.** For example, $3,534.38 for single is 1.95% of $181,250, which is $3,534.375. The encoding computes from the rates, so its answer above the second threshold can differ from the printed row by half a cent. Asserted ($300,000 single = $5,385.00).
5. **The first bracket taxes at 0.00%.** Below $44,725 (single), $74,750 (joint), $37,375 (separate) and $59,950 (head of household) of North Dakota taxable income, there is no tax. A filing duty still arises under s 57-38-31 for anyone required to file federally, or with North Dakota-source income. Asserted.
6. **The marriage penalty credit's citations are partly obsolete.** The lesser-earning spouse's income is reduced by "the amount for one exemption under section 151(d)" (zero since 2018: unverified (general knowledge); the IRC deposit should confirm it) and "one-half of the amount of the standard deduction under section 63(c)(2)(A) (4)". "(4)" has no evident meaning after "(A)"; it is read as s 63(c)(2)(A), the joint-return basic standard deduction. Both amounts are inputs. The credit compares "the rates and income levels in subdivision b" and "subdivision a"; the seat uses the printed schedules, because (1)(g) speaks of schedules applying "in lieu of" (a) to (e) for the tax, not for this credit. Interpretive. Asserted as encoded (including the cap at the maximum).
7. **Residence turns on months, not days**: a person with a permanent place of abode is a resident after "more than seven months" in the state (s 57-38-01(11)). Asserted.
8. **North Dakota has no earned income credit or child credit in chapter 57-38.** No section of the deposited chapter refers to an earned income or child tax credit; the personal credits in s 57-38-30.3(7) are the family care credit, the marriage penalty credit and business and investment credits. Not asserted (a finding about the chapter's content).
9. **A federal change must be reported within 90 days**, counted from the final determination, or from the filing of an amended federal return (s 57-38-34.4). Asserted.

## What would need doing before this is worth relying on

- **The commissioner's indexed schedules** and maximum marriage penalty credit for the year, from a deposited Office of State Tax Commissioner publication.
- **Part-year residents and nonresidents** ((1)(f)) and the credit for tax paid to another state ((4)).
- **The family care credit** (s 57-38-01.20), the remaining personal credit.
- **The federal inputs** from the IRC encoding.
- **An independent test pass**, and a check of finding 6 against the commissioner's forms.
