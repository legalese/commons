# Wages Protection Act 1983 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (ss 1-19 and the Schedule), as in the PCO's version 25 as at 27 November 2025. It is encoded from the PDF the user supplied; the text is deposited and the PDF is not.

**Inputs.** These are taken as given rather than worked out:
- who is a worker and who is an employer (s 2: ERA ss 5 and 6), and who is "involved" (ss 11A(5), 13(3): ERA s 142W);
- whether a deduction is for a lawful purpose (s 5(1)) or unreasonable (s 5A), whether a consent was obtained by duress (s 11(1)(a)(ii)), and whether the worker was consulted (s 5(1A));
- whether another Act, a collective agreement or an order authorises a deduction or a manner of payment (ss 15, 16), and whether a pre-1964 bearer-cheque contract applies (s 17);
- the count of working days for s 6(3)(ba)(i);
- for s 5(2) and s 9(2), whether it was practicable to act on a withdrawal within 2 weeks, and if not, the earliest practicable day.

**Conduct before 1 April 2016.** The 2016 Act replaced or amended ss 5(1), 5(1A), 5A, 11, 11A, 12A(1) and 13, and Schedule cl 2(2) keeps those amendments off earlier conduct. The sections as they stood before are not carried, so the encoding refuses a question about a deduction, or a penalty, before that date. A s 11 action on such a deduction is now out of time anyway (s 11(2): 6 years, so by 1 April 2022), and the encoding says 0 in that case rather than refusing.

### The top-level goal

`the wage protection position for` a `Wage payment case` (`wpa-goal.l4`, `@export default`) answers: *for this payment of wages, how much was deducted and how much of it lawfully; were the wages paid in a lawful manner; did the employer contravene ss 4, 5, 5A or 7; and what may the worker, or a Labour Inspector, recover from the employer under s 11 in an action brought on the given day?*

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Was the deduction lawful? May the overpayment be recovered? | `the deduction was lawful` (`@export`), `the lawful part of the deduction`, `the employer may recover the overpayment under s 6` (`@export`), `the consent or request still covers what is done on`, `the last day for notice of the overpayment` | ss 4, 5, 5A, 6, 15, 16 | `wpa-deductions.l4` |
| 2 | Were the wages paid in a lawful manner? | `the wages were paid in a lawful manner` (`@export`) | ss 7-10, 15-17 | `wpa-payment.l4` |
| 3 | What may be recovered under s 11, and is the action in time? What from a person involved? | `the deduction is within s 11(1)(a)`, `an action under s 11 is in time…`, `the amount recoverable under s 11(1)(a) for…`, `the arrears recoverable under s 11A by … on` (`@export`) | ss 11, 11A(1)-(2), (5) | `wpa-enforcement.l4` |
| 4 | Premiums, spending, penalties | `s 12A(1) is breached`, `the premium recoverable from the employer under s 12A(2) by…`, `the premium recoverable from a person involved under s 11A(3) by…`, `s 12 is breached`, `liable to a penalty under s 13` (`@export`), `may recover a penalty under s 13` | ss 11A(3)-(4), 12, 12A, 13 | `wpa-enforcement.l4` |

The top-level answer also reports `wages neither paid nor deducted`: wages payable less the amount paid and all deductions. That shortfall is not recoverable under s 11 (which reaches deductions and payment otherwise than in money); it is for an action for arrears under the Employment Relations Act 2000.

## 2. Coverage table

| provision | disposition |
| --- | --- |
| s 1 (title, commencement 1 February 1984) | carried as text; the date is used by s 11(3) |
| s 2 interpretation | read into the facts |
| ss 2A, 3 | carried as text |
| s 4 | Goal 1 |
| s 5(1), (1A), (2) | Goal 1 |
| s 5A | Goal 1 |
| s 6(1)-(3) | Goal 1 |
| s 6(4)(a) | Goal 1 (`the notice identifies the overpayment`) |
| s 6(4)(b) | carried as text (a group notice is valid for the worker given it) |
| s 6(3)(ba) (second), 6(5) | repealed |
| s 7 | Goals 2, 3 |
| ss 8, 9, 10 | Goal 2 |
| s 11(1)-(3) | Goal 3 |
| s 11A(1)-(2), (5) | Goal 3 |
| s 11A(3)-(4) | Goal 4 |
| s 12 | Goal 4 |
| s 12A(1)-(2) | Goal 4 |
| s 12A(3) | carried as text |
| s 13 | Goal 4 |
| s 14, s 18(2) | repealed |
| ss 15, 16 | Goals 1-3 (as inputs on a deduction or a payment) |
| s 17 | Goal 2 (as an input) |
| s 18(1), s 19 | carried as text |
| Schedule cls 1-2 | Goals 1, 3, 4 (`the 2016 amendments apply to conduct on`) |

`provisions carried as text` in `wpa-enforcement.l4` lists the text-only provisions.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | ss 5(2), 9(2) | Up to which day does a withdrawn consent still cover a deduction or a manner of payment? | Up to and including the last day the employer has to act: 14 days after receiving the notice if practicable, else the earliest practicable day | The employer "shall ... within 2 weeks ... cease"; until then it is not in breach |
| F2 | s 6(3)(b) | Is notice given on the day of recovery given "before recovering"? | Yes | A notice can precede the payroll run on the same day |
| F3 | s 11(1)(a)(iii)-(iv) | Do the grounds inserted on 27 November 2025 reach earlier deductions? | No: only deductions on or after 27 November 2025 | The Statutes Amendment Act 2025 states no transitional rule, and legislation does not have retrospective effect |
| F4 | s 11(1)(a) "otherwise than pursuant to section 6" | A deduction that relies on s 6 but does not meet s 6(3) | Not "pursuant to section 6", and not consented to: within ground (i) | s 6(3) "No employer shall recover an overpayment under subsection (2) unless ..." |
| F5 | ss 5(2), 11(1)(a)(i) | A deduction after a withdrawal has taken effect | Not consented to: ground (i) | The consent no longer exists |
| F6 | ss 15, 16, 11(1)(a) | Can a deduction another Act or a collective agreement authorises be recovered under ground (i)? | No | s 15 reads the Act subject to other Acts; s 16 says nothing in it derogates from a collective agreement or order |
| F7 | s 11(2) "after the expiration of 6 years from the date on which the cause of action concerned arose" | Last day to bring an action | The sixth anniversary of the date the cause arose | The period runs from that date; it expires at the end of the anniversary |
| F8 | s 11(1)(a) | A consented deduction not for a lawful purpose (s 5(1)) | Unlawful (s 4), but not within grounds (i)-(iv) | (i)-(iv) do not name it; it can still found a penalty (s 13) and an ERA arrears claim |
| F9 | s 11(1)(b) | How much is recoverable for wages paid otherwise than in money? | The whole amount paid in the unlawful manner | "an amount equal to any wages required by section 7 to be paid to that worker in money" |
| F11 | s 6(2) "recover the amount of that overpayment" | A s 6 deduction larger than the overpayment | Lawful up to the overpayment; the excess is a deduction s 4 forbids, recoverable under s 11(1)(a)(i) | The subsection authorises recovery of that amount only. Raised by the independent test author |
| F10 | ss 5(1), 5A, 11, 11A, 13; Schedule cl 2 | Deductions and penalties for conduct before 1 April 2016 | `REFUSE`, except that a s 11 action already out of time gives 0 | The pre-2016 text is not carried |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15 (l4-ide unstable at 7768812fa): **7 modules, 0 errors, 284 assertions satisfied, 0 failed, 0 warnings** (140 in `wpa-tests.l4`, 144 in `tests-independent.l4`). No assertion is expected to fail. A full run takes about two minutes.

`wpa-tests.l4` (140 assertions) is written from the Act.

**The independent test pass** (`tests-independent.l4`, `independent-expectations.md`, `INDEPENDENT-TEST-REPORT.md`): a fresh session wrote expectations from the brief and the Act before reading the encoding. Of 144 assertions, 143 passed first time. The one failure was a real error: a deduction to recover an overpayment was treated as lawful in full even where it exceeded the overpayment (s 6(2), fork F11). The encoding now has `the lawful part of the deduction`, and the excess counts as unlawful and recoverable. The author also found that s 11A(3) (premiums from a person involved) lacked the 2016 date gate; it now has one. The s 11A(3) calls in the independent file were ported to the new date input (marked `[Ported …]`); no expected value was changed.

Remarks not acted on, kept as limits of the model:
- s 12A(2): the claimant who may recover a premium is "the person who paid the premium or from whose wages it was deducted"; a caller who picks `the worker` gets 0 even if the premium came from the worker's wages.
- ss 5(2), 9(2): a notice that *varies* a consent is modelled only as ending it for the deduction or manner of payment in question.
- For a s 6 deduction, the deduction's date and the overpayment's recovery date are separate inputs; the encoding does not check that they agree.
- s 13 refuses for conduct before 1 April 2016 even for the employer, whose liability predates 2016, because the pre-2016 text is not carried.

## 5. Open questions for a New Zealand employment lawyer

1. F3: do s 11(1)(a)(iii)-(iv) reach deductions made before 27 November 2025?
2. F8: is a consented deduction for an unlawful purpose recoverable under s 11, or only through the Employment Relations Act?
3. s 5(1A): what does "consulting" require? The encoding takes it as a yes/no input.
4. s 6(3)(ba)(i): the "working days" for a specified pay deduction are an input; which definition applies (ERA s 5)?
