# Code of Alabama 1975, Title 25, Chapter 4 (unemployment compensation benefits) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the unemployed worker (the claimant), with the design defaults ruled on 2026-10-18.
The core rules use the Code's own actors and terms; the worker's questions (`@export`, `@desc`, under `§ Questions for the unemployed worker`) are derived from them.
Duties with times (the weekly work search, the appeal window, repaying disputed benefits) are regulative rules with the party as a parameter.
There is no REFUSE; a benefit year before 2020 answers `not covered`, and a test asserts it.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not advice.**

Why unemployment insurance for Alabama's benefits half: of the Alabama benefits texts deposited, this is the one whose amounts are all in the statute. The Family Assistance (TANF) grant is "the appropriate payment standard ... minus the rounded total net available income" (Ala. Admin. Code r 660-2-2-.10), and the payment standard is not in any deposited rule or statute (the attachment that held it was repealed in 2018). The TANF eligibility rules are encoded separately, beside this one: `../../../code-of-alabama-1975-title-38-chapters-1-and-4-public-assistance/encodings/baseline-2026-10/`.

## Edition

The Code of Alabama 1975 as ALISON served it on 2026-10-20 (no "current through" date published), deposited at `../../registers/source-bundle/ala-code-25-4-art4.txt` (Article 4, ss 25-4-70 to 25-4-78) and `ala-code-25-4-art5.txt` (Article 5, ss 25-4-90 to 25-4-97). Definitions (Article 1, `ala-code-25-4-art1.txt`) are used as glosses: "base period" is "the first four of the last five completed calendar quarters immediately preceding the first day of an individual benefit year" (s 25-4-1).

No annual figure is needed: the $275 maximum is in s 25-4-72(b)(5). The one published figure the Code relies on, "the state's average unemployment rate" (s 25-4-74(d)), is an input.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `al-unemployment.l4` | `al-unemployment-cases.l4` | 49 written, 49 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s carry `-- expect:` comments that matched.
Every expected value was worked out by hand from the text. One hand calculation was wrong on the first run (a quarter of $13,001 is more than 14 × $231, so the lesser is $3,234, not $3,250); the case was replaced by a fresh hand-worked one ($12,001), not by the encoding's output.

## Seat

**The unemployed worker who claims benefits.** Questions: "How much a week?", "Have I earned enough?", "What is the most I can get?", "What will I be paid for a week with some earnings?", "Am I eligible this week?", "Does the way my job ended disqualify me?", "How much must I earn to requalify?", "Can I turn down this job?", "Does my pension reduce my benefit?", "How long do I have to appeal?".

The 2026-10-18 defaults, all followed:

- **The Act alone.** Articles 4 and 5 of Chapter 4.
- **The actors the text names:** the claimant (the individual), the last employing unit, the secretary, the appeals tribunal.
- **Judgments left to the secretary** are asked as facts: good cause for a quit, which kind of misconduct, whether a quit exception applies, the number of weekly amounts deducted (3 to 9), approval of training, suitability of work beyond the three statutory bars.
- **Definitions:** the weekly benefit amount, the base-period test and the maximum are worked out; wages for insured work are stated by the worker.
- **One case:** one claimant, one benefit year.
- **Machinery out:** the appeals tribunal and board (ss 25-4-92 to 25-4-97), employer charging (s 25-4-54), Reed Act appropriations (s 25-4-72(e)).

## Scope

**In:** s 25-4-72(b)(1), (2), (5); s 25-4-73(a), (c); s 25-4-74(a), (d); s 25-4-77(a)(1)-(6), (b)(1)-(2); s 25-4-78(2) (with a.1, c, d as one fact), (3)a-c, (5) (the bars of (5)b), (8)b, c; s 25-4-91(d)(1), (d)(1)a.

**Out:** benefit years before 2020 (`not covered`); maritime workers (s 25-4-76); extended benefits (s 25-4-75) and the training weeks of s 25-4-74(f); s 25-4-78(1) (labour disputes), (4), (6), (7), (9)-(13) and the subdivisions after (13); s 25-4-78(3)d (suspension); s 25-4-77(a)(7) (reemployment services); the period of a (5) disqualification (1 to 5 weeks, the secretary's choice: noted, not computed).

## Read with

- the federal frame: FUTA, 26 U.S.C. 3304, and SSA Title III, deposited in `subjects/us/internal-revenue-code-of-1986/` and `subjects/us/social-security-act/`; extended benefits in `subjects/us/federal-state-extended-unemployment-compensation-act-of-1970/`;
- the tax side: benefits are federal gross income (26 U.S.C. 85); Alabama exempts up to $50,000 of severance and unemployment compensation after an administrative downsizing (s 40-18-19.1), encoded in `../../../code-of-alabama-1975-title-40-chapter-18-income-taxes/encodings/baseline-2026-10/`.

## What the Code turns out to say

1. **Section 25-4-91(a) still points to "subdivision (a)(5) of Section 25-4-77" for the base-period wages.** Act 2022-301 inserted the work search as s 25-4-77(a)(5); the wage test is now (a)(6). The cross-reference is stale; the encoding follows the wage test where it now is.
2. **The weekly benefit amount is one twenty-sixth of the average of the two highest quarters**, with fractions over 50 cents rounded up and 50 cents or less dropped; $44.50 or less gives no weekly benefit amount; above $274.50, $275. Asserted at $44.50, $250.50 and $274.50.
3. **"Computed to the nearest multiple of one dollar" in ss 25-4-73 and 25-4-74 is given s 25-4-72(1)'s tie rule** (exactly 50 cents goes down). The two sections do not say how a tie goes.
4. **The maximum is the lesser of 14 to 20 weekly amounts and a quarter of base-period wages.** One more weekly amount for "each 0.5 percent increase" above 6.5%: read as each complete 0.5% (7.4% gives 15). Asserted.
5. **Earnings up to a third of the weekly benefit amount are disregarded** (s 25-4-73(a)). The first compensable week is a waiting week with nothing paid (s 25-4-73(c)). Asserted.
6. **The work search needs three prospective employers a week**, excused only by a jury summons (s 25-4-77(a)(5)). The rule that later proofs may not repeat an employer unless it has said it is hiring is not modelled. Approved training answers availability ((b)), not the work search. Asserted.
7. **A worker who drew benefits last benefit year must earn eight times the old weekly amount before a new benefit year** (s 25-4-77(a)(6) proviso). Asserted.
8. **A quit without good cause and repeated misconduct have the same effect**: no benefits until re-employed with wages of ten times the weekly amount and separated for a non-disqualifying reason, and the total reduced by three to nine weekly amounts (ss 25-4-78(2)b, (3)b). The worst misconduct ((3)a) adds that wages from that employer never count. Other misconduct ((3)c) costs the week of discharge and one to four more weeks, and the same number of weekly amounts off the total. Asserted.
9. **Three things make offered work unsuitable whatever else is true**: a vacancy caused by a labour dispute, substantially worse conditions than prevail locally, or a union condition (s 25-4-78(5)b). These are also FUTA's conditions (26 U.S.C. 3304(a)(5)). Asserted.
10. **Social Security and Railroad Retirement never reduce benefits; an employer pension does only if the base-period employer alone paid for the plan** (s 25-4-78(8)b, c). Asserted.
11. **The appeal window is short: 7 calendar days after delivery, 15 after mailing** (s 25-4-91(d)(1)); then the determination is final. Benefits paid while an appeal is pending, and not payable under the final decision, must be repaid ((d)(1)a), with no time stated. Asserted and traced.

## Before relying on it

- The secretary's rules on claims (s 25-4-90) and on the work-search proof are not deposited.
- Add labour disputes (s 25-4-78(1)), suspensions, and the remaining disqualifications.
- An independent test pass.
