# Texas Unemployment Compensation Act (Tex. Lab. Code Title 4, Subtitle A), benefits — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

There was no earlier encoding. No requirement ledger exists for US states.

## Edition

Tex. Lab. Code ch. 201 (definitions) and ch. 207 (benefits) as deposited at `../../registers/source-bundle/tex-lab-code-ch201-general-provisions.txt` and `tex-lab-code-ch207-benefits.txt`: the Texas Legislative Council's chapter files dated 2026-05-14 (latest credit 89th Leg., R.S., 2025), retrieved 2026-10-19 UTC. Changes from the 2025 called sessions may be missing (state README).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tx-ui.l4` | `tx-ui-cases.l4` | 35 written, 35 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The unemployed individual claiming benefits.** Questions: "How much a week?", "How much in total this benefit year?", "How much for a week I earned a little?", "Am I eligible?", "Am I disqualified for how I left?", "What about severance, workers' compensation or a pension?".

The Texas Workforce Commission's determinations (misconduct, good cause, suitable work, reasonable cause, the profiling referral) are asked as facts. The commission's annual maximum and minimum weekly benefit amounts (s 207.002(b)-(d): 47.6% and 7.6% of the state average weekly wage, rounded, capped at $14 and $1 increases) are not in the deposited text and are inputs; every figure used in the cases is HYPOTHETICAL.

Defaults followed: the Act's chapters 201 and 207 only; the actors named (the individual, the commission); one case is one claim (one benefit year, one benefit period where weekly); machinery out (ch. 208 claims and appeals, employer taxes and chargebacks).

## Scope

**In:** s 201.011(1)(A) (base period, in the input's wording), s 201.091 (total and partial unemployment), ss 207.002(a), (a-2), 207.003, 207.004 (benefit wage credits as base-period wages), 207.005, 207.006, 207.021(a), 207.0211, 207.044, 207.045(a)-(d), (f), 207.047, 207.049(a), (b), 207.050(a)-(c).

**Out:** ch. 208; s 201.011(1)(B) (the injury or illness base period: the person enters the quarters the commission uses); ss 207.022, 207.023 (training); 207.026 (drug testing); 207.041 to 207.043; 207.045(e), (g)-(j) (asked through the "s 207.045(d) or s 207.046" choice only); 207.046 except as a choice; 207.048 (labor disputes); 207.051, 207.053; ss 207.071 to 207.114.

## Regulative rules

None. Chapter 207's operative provisions are conditions of eligibility and disqualification, not duties with deadlines; the claimant's duties to register, report and claim are in ch. 208 and the commission's rules, not deposited. Stated so the reader does not look for them here.

## What the Act turns out to say

1. **The weekly amount is 1/25 of the best quarter, then bounded, then rounded up.** Section 207.002(a) gives "1/25 of the wages ... during that quarter in the individual's base period in which wages were highest"; (a-2) bounds it by the maximum and minimum; s 207.006 raises any benefit rate "to the next multiple of $1". Rounding is applied before bounding, which only matters if the bounds are not whole dollars (s 207.002(c) makes them whole). Asserted ($6,010 quarter: $241).
2. **Total benefits are capped twice.** "The lesser of: (1) 26 times the individual's benefit amount; or (2) 27 percent of the individual's benefit wage credits" (s 207.005). For a worker whose wages are spread unevenly across the base period the 27% cap binds well before 26 weeks. Asserted ($25,000 base-period wages: $6,750, about 17 weeks at $400).
3. **The partial-week rule and the definition of unemployment use the same allowance.** A week is "totally unemployed" where wages do not exceed the greater of $5 or 25% of the benefit amount (s 201.091(a)); a partially unemployed week pays the benefit amount plus that allowance, less wages (s 207.003(b)). Partial unemployment needs "less than full-time work" (s 201.091(b)). Asserted.
4. **Two thresholds in s 207.021(a)(6) and (7) are "not less than".** Base-period wages of exactly 37 times the benefit amount, and wages since the last benefit year of exactly six times, qualify. Asserted (6 x 400 = 2,400).
5. **A permanently disabled part-time worker on SSDI is treated as able and available.** Section 207.0211 needs all four facts, including receipt of "disability insurance benefits under 42 U.S.C. Section 423". The federal Social Security Act is at `subjects/us/social-security-act/`. Asserted.
6. **The usual disqualifications end on re-employment, not after a fixed time.** Misconduct, quitting without good cause and refusing suitable work each continue "until the individual has returned to employment and: (1) worked for six weeks; or (2) earned wages equal to six times the individual's benefit amount" (ss 207.044(b), 207.045(b), 207.047(b)). Leaving to move with a spouse is the exception: "not less than six benefit periods and not more than 25 benefit periods", as the commission decides (s 207.045(c)). Asserted.
7. **A Social Security payment never reduces the weekly benefit; any other work pension reduces it pound for pound.** Section 207.050(b), (c). A pension equal to or more than the benefit leaves nothing (the reduction in (c) applies only where the remuneration is "less than the benefits"). Asserted. Severance pay, wages in lieu of notice and workers' compensation disability benefits disqualify for the week outright (s 207.049(a)), but a settlement of an employment claim is not "severance pay" (s 207.049(b)).

## Before relying on it

- Deposit the commission's current maximum and minimum weekly benefit amounts if an official publication can be deposited (www.twc.texas.gov answered 403 on 2026-10-20).
- Deposit ch. 208 and encode the claim and appeal deadlines as regulative rules.
- An independent test pass.
