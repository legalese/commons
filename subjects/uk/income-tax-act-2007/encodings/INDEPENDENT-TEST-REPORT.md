# Independent test report: Income Tax Act 2007 (UK)

Method: expectations were written from BRIEF.md and the source text (ss 6-16, 23-25, 35, 55A-55C, 58, 414-415, plus ss 27-29 and 56 because 55B/55C refer to them) and saved in `independent-expectations.md` before any `.l4` file was opened. Each figure was checked by hand, and against a small calculator of my own that does not use the encoding. `tests-independent.l4` then asserts those values. No expected value was changed to fit the code.

## Counts

`L4=~/.local/bin/l4 ./check.sh`:

| module | errors | satisfied | failed |
|---|---|---|---|
| tests-independent.l4 | 4 | 81 | 4 |
| ita-tests.l4 (author's) | 0 | 42 | 0 |

There are 85 independent assertions: 81 pass and 4 fail. All 4 errors are the failed assertions, so there are no syntax or type errors.

## Failing assertions

### 1-2. Order in which the personal allowance comes off savings and dividends (T34, T36)

| Scenario | My expected value | Code |
|---|---|---|
| T34: savings 5,000, dividends 20,000, no other income | 744.975 | 1,282.475 |
| T36: savings 3,000, dividends 15,000, no other income | 207.475 | 529.975 |

Source: s 25(2): "At Steps 2 and 3, deduct the reliefs and allowances in the way which will result in the greatest reduction in the taxpayer's liability to income tax." s 25(3A) makes (2) "subject to a requirement that the reliefs and allowances ... must be deducted from components of income other than property income, savings income or dividend income (so far as it would otherwise be possible to do so) before they are deducted from property income, savings income or dividend income."

The code follows the brief and takes the allowance off non-savings income, then savings, then dividends. But (3A) only puts non-savings income first. It puts savings and dividends in the same group and does not order them. Between those two, (2) applies, and the allowance goes wherever it saves the most tax. When savings fit inside the £5,000 starting-rate band, setting the allowance against dividends gives less tax. In T34 the savings stay at the 0% starting rate and only 6,930 of dividends is taxed at 10.75%. The code's order uses the allowance up on savings that would have been taxed at 0% anyway.

**My view: the Act's reading is right, and the brief's convention is wrong for these cases.** HMRC's own calculations also allocate the allowance in the most beneficial way. To fix it, `my taxable savings income` and `my taxable dividend income` would need to compare the two orders, or better, the possible splits of the leftover allowance, and pick the lowest tax.

### 3-4. Gaining party whose income above the basic rate limit is all savings at the savings nil rate (M8)

Scenario M8: the gaining party (spouse has elected) has wages 50,170 and savings 400. Taxable non-savings income is 37,600 and total taxable income is 38,000, which is 300 above the basic rate limit. The savings allowance is £500, so all 400 of the savings are charged at the savings nil rate.

| Assertion | My expected value | Code |
|---|---|---|
| marriage allowance reduction | 252 | 0 |
| income tax liability | 7,268 | 7,520 |

Source: s 55B(2)(b): "the individual is not, for the tax year, liable to tax at a rate other than the basic rate, ... the savings basic rate, the dividend nil rate, ... the dividend ordinary rate, the savings nil rate or the starting rate for savings". s 55B(2)(ba) adds a "but for s 13A" test for the dividend nil rate only: "if ... liable to tax at the dividend nil rate, the individual would ... neither be liable to tax at the dividend upper rate, nor ... the dividend additional rate, if section 13A ... were omitted".

The code tests "taxable income at most the basic rate limit" (`I pay no more than the basic rate`). That is right for non-savings income, and for dividends because of (ba). But there is no matching "but for s 12A" limb for savings. A person whose only income above the limit is savings charged at the savings nil rate is liable only at permitted rates, so on the words of the Act they are entitled. The same point applies to the relinquishing party under s 55C(1)(c)/(ca).

**My view: the Act's words favour entitlement.** This is a narrow edge, and HMRC practice may be stricter. Either way, the encoding should handle it on purpose and record it in NOTES.md. At present the code silently applies a test that the Act does not state.

## Points where the code agrees with my reading of the Act, not with the brief

- **s 55C(2), the net-income test, is not a condition for a UK resident.** It applies only via s 55C(1)(d) to claimants who meet s 56 through s 56(3). The code says this in a comment and does not apply the test. M11 (wages 49,000) and M13 (wages 12,570) both pass: may elect = TRUE. The brief's Goal 3 wording ("my net income is below my personal allowance") is wrong for the seat and should be corrected.
- M12 passes: wages 49,100 are pushed above the basic rate limit by the reduced allowance, so the person may not elect.

## Reading points that pass but are worth recording

- **s 12B(8) does not list the savings higher and additional rates.** Read literally, savings income charged at the savings higher rate (s 11D) is not "higher-rate income". I read it purposively, as income in the higher band. The code does the same (`my savings allowance` compares total taxable income with the limits). T17, T19 and T22 pass on that basis. The literal reading would give a £1,000 or £500 allowance in those cases, and NOTES.md should mention this.
- **Tax is not rounded.** Values such as 20.425 and 744.975 are exact, and the code does not round either.

## Gaps noticed in the encoding

1. The allowance is allocated between savings and dividends in a fixed order instead of by the s 25(2) greatest-reduction rule (failures 1-2 above).
2. `I pay no more than the basic rate` treats savings above the basic rate limit at the savings nil rate as disqualifying (failures 3-4 above).
3. `my personal allowance` reduces the relinquishing party's allowance whenever they have elected. Under s 55B(6) it is reduced only "if an individual is entitled to a tax reduction under subsection (1) by reference to an election", that is, only if the spouse is in fact entitled. The two-person dependency cannot be expressed from a single taxpayer's inputs. The encoding should state this assumption, or `REFUSE` where the spouse's entitlement is unknown. None of my tests depend on it.
4. `I may elect to transfer my allowance` does not use the marriage/civil partnership condition (s 55C(1)(a)) or the s 45/46 married couple's allowance exclusion (s 55B(2)(d)). These are reasonable as implicit inputs, but they are not stated.
5. `my savings at the starting rate` and the band slicing assume the starting rate band starts at nil taxable income. That is correct. The s 12A(1)(a) Step 3 income > £5,000 condition is not encoded explicitly, but it gives the same results because the nil-rate slice is empty when no savings sit above £5,000.
6. Gift Aid gross-up uses the basic rate input (`100 / (100 - basic rate)`), which follows s 415. There are no input guards: negative incomes or donations are accepted.

## Change after the pass (encoder)

- **Order of the allowance between savings and dividends (s 25(2)).** Accepted. Both orders are computed and the one giving less tax is taken. Both assertions pass.
- **Gaining party with savings at the savings nil rate above the limit (s 55B(2)(b)).** Accepted. The basic-rate test now allows savings above the basic rate limit at the starting or savings nil rate, but no dividends above it. Both assertions pass.
- **s 55C(2).** The brief's Goal 3 wording was corrected.
- The remaining gaps are recorded in NOTES.md (F5, F9 and known limits).
