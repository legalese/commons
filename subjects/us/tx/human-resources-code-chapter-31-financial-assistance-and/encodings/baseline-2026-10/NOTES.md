# Texas TANF (Tex. Hum. Res. Code ch. 31) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE: a child in foster care (s 31.002(b)) answers `not covered`, asserted. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

There was no earlier encoding. No requirement ledger exists for US states.

## Edition

Tex. Hum. Res. Code ch. 31 as deposited at `../../registers/source-bundle/tex-hum-res-code-ch31.txt`: the Texas Legislative Council's chapter file dated 2026-09-01, retrieved 2026-10-19 UTC. The grant table (Texas Works Handbook Appendix C-110) is indexed but not deposited (`../texas-works-handbook-appendix-c-110-tanf-budgetary-allowances/`, waiting on a ruling on HHSC's "unaltered" condition), so no amount is computed.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tx-tanf.l4` | `tx-tanf-cases.l4` | 46 written, 46 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). One `#TRACE` checks the immunization breach with an `-- expect:` comment; it gave the expected breach. Every expected value was worked by hand from the text.

## Seat

**The applicant for or recipient of TANF**: the parent or relative applying for a dependent child. Questions: "Is my child a dependent child?", "How much of our resources and income count?", "Is my new spouse's income left out?", "How many months can I get, and from when?", "Do I meet the work requirement?", "What happens if I am found not cooperating, and do I have good cause?", "By when must I prove immunization or ask for a hearing?", "Do I keep TANF if I leave Texas?", "Can I get the grandparent payment?".

The Health and Human Services Commission's and the Texas Workforce Commission's duties are encoded for what they mean to the applicant: what they must leave out, how long a sanction lasts, when the clock starts.

Defaults followed:
- **The chapter alone.** The indexed vehicle exclusion (s 31.032(d)(2)) and the federal poverty level (ss 31.0038, 31.0041) are inputs; the resource limit and the need standard are in rules, not deposited, and are asked as facts where needed (s 31.002(a)(4), s 31.0041(a)(5)).
- **The actors the text names:** the applicant or recipient, the commission, the Title IV-D agency.
- **Judgments left to others answered conditionally:** non-cooperation and good cause findings, the commission's approval of a temporary absence, the functional educational level from the needs assessment.
- **Definitions worked out from facts:** "dependent child" (s 31.002(a)), "caretaker of a child" (s 31.012(f), in the input's wording), "severance"-style exclusions are not involved.
- **One case:** one family's application or case.
- **Machinery out:** ss 31.006 to 31.0129 and 31.015 to 31.018 (programmes and interagency plans), payment administration (ss 31.035 to 31.045 except s 31.036), budget limits (ss 31.051 to 31.053).

## Scope

**In:** ss 31.002(a), 31.0031(d) (listed in comments), 31.0032(a), (a-1), 31.0033(a), (e), 31.00331, 31.0036, 31.0038, 31.0039 (as an input's wording), 31.0041(a), (b), (e), 31.0065(b)-(e), 31.012(a), (c), 31.031(d), (e), 31.032(d), 31.033(e), 31.036.

**Out:** the amount of assistance (s 31.003 leaves it to rules); the foster-care branch (s 31.002(b), `not covered`); hardship exemptions (ss 31.0065(a), 31.0066: by rule); family violence waivers (s 31.0322) except as an input to good cause; protective payees (s 31.0324); transitional child care (s 31.0035); appeals (s 31.034, which sets no time).

## Regulative rules

Three `DEONTIC` rules, in days: proof of immunization by the 180th day after eligibility is determined (s 31.031(e)); notifying the commission "immediately" of more income or resources (s 31.033(e)); the permission to request a good cause hearing by the 13th day after the notice is sent (s 31.0033(a)). The two deadlines with fixed days are also exported as date questions.

## What the chapter turns out to say

1. **Texas keeps the old "deprivation" test.** Section 31.002(a)(3) still requires that the child "has been deprived of parental support or care because of the death, continued absence from home, or physical or mental incapacity of a parent". A child living with both able parents is not a "dependent child" on the text. Asserted. (South Carolina's s 43-5-1195 removed this test; Texas's chapter did not.)
2. **The time-limit tiers overlap at 18 months of work.** Tier (1) applies to "recent work experience of 18 months or more"; tier (2) to work "of not less than six or more than 18 months", which includes exactly 18. The tiers are tried in order, so 18 months gives 12 months of assistance. Asserted. Tier (3) needs both less than three years of high school and less than six months' work.
3. **The work requirement is one or the other, not a total.** Section 31.012(a): "work not less than 30 hours a week; or ... participate for not less than 20 hours a week" in a programme activity. Twenty-five hours of work and ten of activity meet neither. Asserted. The single-caretaker exemption runs until "the caretaker's youngest child at the time the caretaker first became eligible for assistance reaches the age of one", so a later baby does not restart it.
4. **The vehicle exclusion is for "a motor vehicle".** Section 31.032(d)(2) excludes the value of "the applicant's ownership interest in a motor vehicle", up to $5,000 as indexed. Read as one vehicle, the most valuable; any other vehicle counts in full. Asserted.
5. **"Immediately" has no number.** Section 31.033(e) requires notice "immediately" of income or resources above what was reported. The regulative rule models it as within one day; the encoding does not export a date for it.
6. **The chapter gives few consequences of its own.** The immunization proof deadline and the reporting duty carry no stated sanction in the chapter; sanctions for failing the responsibility agreement are by rule (s 31.0031(c)) and the termination rule of s 31.0032. Each breach is named with its reason only.
7. **A good cause hearing request within 13 days stops the sanction until decided.** Section 31.0033(a): "the commission may not withhold or reduce the payment of financial assistance until the commission determines whether the person had good cause". Two consecutive months of non-cooperation make the family ineligible (s 31.00331) whatever the hearing position; the encoding checks that first. Asserted.

## Before relying on it

- A ruling on depositing the Texas Works Handbook Appendix C-110 grant table, then encode the amount.
- Deposit the Texas Administrative Code TANF rules (1 TAC ch. 372) for the resource limit and need standard, if the TAC viewer can be read.
- An independent test pass.
