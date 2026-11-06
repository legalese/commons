# Fair Work Regulations 2009 — baseline-2026-11: the regulations a person bringing an employment claim meets

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. Checked with the
stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test
pass, no human gate. Not for public use as advice.

This is the first encoding of the Regulations. The Fair Work Act 2009's encodings (`../../../fair-work-act-2009/encodings/`)
already use regs 2.13, 3.01 and 3.06 inside the Act's questions; they are unchanged. The stable `l4` resolves IMPORT
only within a folder, so the two subjects cannot call each other: where a regulation feeds an Act question here
(s 382(b)(iii), s 333F(1)(e)), the Act's comparison is written here in one line with the Act's section cited, and
everything else the Act decides is asked as an input.

Five modules. `fwr-common.l4` holds the regulations' three rounding rules and the day counting, and is the only one that
imports `daydate`. The four question modules import it:

| Module | Covers |
|---|---|
| `fwr-pay.l4` | regs 2.12A (what a deduction authorisation must say), 2.12 (reasonable and unreasonable deductions), 3.45, 3.46 (what a pay slip must show), 3.47, 3.48 (family and domestic violence leave kept off pay slips) |
| `fwr-threshold.l4` | reg 2.13 (the high income threshold: 2009-10 and each later year), reg 3.05 (piece rates and non-money benefits added to earnings), s 382(b)(iii) of the Act (the comparison), reg 3.06 (leave without pay in the compensation cap) |
| `fwr-fixed-term.l4` | reg 2.14 (the threshold for a part-time or part-year fixed term contract) with s 333F(1)(e) of the Act, reg 2.15 (the sport, international event, charity and medical research contracts outside the fixed term limits) |
| `fwr-claims.l4` | regs 3.01, 6.04 (illness or injury that protects an absence); the application fees, hardship waiver and refund of regs 3.02, 3.03, 3.07, 3A.03, 3A.05, 6.05, 6.07A (the FWC's repayment duty as a regulative rule); reg 3.29A (defence members and stop sexual harassment orders); reg 4.01 (asking for the small claims procedure; representation); regs 6.01A, 6.01B (other proceedings) |

Every question is published with `@export` and a description, and every input carries an `@desc` worded from the seat.
Situations a person may not be in (dismissal, discontinuing an application, defence service, a small claim, a
deactivation) are marked in the `§` headings.

## Edition

- **The Regulations:** Fair Work Regulations 2009 (F2009L02356), Compilation No. 57, compilation date 1 October 2026
  (register id F2026C00996, includes amendments up to F2026L01184), as deposited at
  `../../registers/source-bundle/F2009L02356.txt` (retrieved 19 October 2026).
- **The Act, for the sections the regulations are made for:** Fair Work Act 2009, Compilation No. 73 (C2026C00355), as
  deposited at `../../../fair-work-act-2009/registers/source-bundle/C2009A00028.txt`: ss 333F(1)(e), (2) and s 382(b)(iii)
  are each written as one comparison; s 527F(3) is the bar reg 3.29A lifts.
- **Not deposited, so inputs:** the Australian Statistician's AWOTE figures and CPI index numbers; the high income
  threshold figure for a year (published yearly; reg 2.13 gives the method); the fee figure for a year; modern awards and
  enterprise agreements (hours, notice terms); rules of court; State law on representation in magistrates courts; the
  Defence Regulations 2026.

## Checks

With the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset (7 November 2026):

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `fwr-pay-cases.l4` | 31 | 31 | 0 | 0 |
| `fwr-threshold-cases.l4` | 23 | 23 | 0 | 0 |
| `fwr-fixed-term-cases.l4` | 35 | 35 | 0 | 0 |
| `fwr-claims-cases.l4` | 68 | 68 | 0 | 0 |
| **Total** | **157** | **157** | 0 | 0 |

`l4 run` on each module (`fwr-common.l4`, `fwr-pay.l4`, `fwr-threshold.l4`, `fwr-fixed-term.l4`, `fwr-claims.l4`) gives
0 errors and 0 warnings. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A negative control
(three expected values in the threshold cases altered) gave three failures. Expected values were worked by hand from the
text, with the regulation cited beside each; edges include a ratio whose fourth decimal place is 5, a result that is an
exact multiple of $50, a fee ending in 5 cents, 24 hours exactly, an absence of exactly 3 months (and a month-end one),
earnings exactly at the threshold, the 6 December 2023, 1 November 2024 and 1 November 2026 days, revenue exactly at
each limit, and a discontinuance two and three days before a listing. One `#TRACE` (repaying less than the fee) is shown,
not asserted: the stable `l4` cannot compare a residual obligation.

## Seat

**The individual bringing or weighing a claim** under the Fair Work Act 2009: the employee checking a deduction or a
pay slip for an underpayment claim, the dismissed employee working out whether they are under the high income threshold
or what the compensation cap counts, the employee on a fixed term contract asking whether the limits protect them, the
employee dismissed while off sick or injured, the applicant to the Fair Work Commission paying (or excused from, or
getting back) a fee, the defence member harassed at work, the employee suing for unpaid amounts in a small claim, and
the regulated worker deactivated or terminated. Every question is worded as that person asks it, and every input is a
fact they can state.

Provisions that address only the Fair Work Commission (the hardship waiver, the refund, the benefit valuation) are
encoded for what they mean to the claimant: what they pay, what they get back, what is counted. The Commission's
satisfaction is always an input, answered conditionally ("if the FWC is satisfied that ..."), never decided.

## Defaults followed

- **The instrument alone,** with the Act's sections it is made for cited, and no figure the regulations leave to a
  publication (AWOTE, CPI, the yearly threshold and fees): those are inputs.
- **The text's own actors:** the employee, the employer, the FWC, the court, the applicant.
- **Judgments as inputs:** "such longer period as is reasonable in the circumstances" (regs 3.01, 6.04), the FWC's
  satisfaction (regs 3.05(6), the fee regulations (7)), "substantially the same" (reg 2.15(7)(e), (9)(f)), "evidence ...
  that would satisfy a reasonable person" (reg 2.15(7A), (9A)), leave of the court (reg 4.01).
- **Definitions:** the regulations' own (performance support professional, high performance sport, the listings that
  count) worked out; borrowed terms (philanthropic entity, defence member, workplace instrument, annual rate of earnings,
  chosen and stapled fund) asked as facts.
- **One case:** one deduction, one pay slip, one dismissal, one contract, one application.
- **Machinery out:** the Act's application to States and Territories, bargaining and ballots, right of entry, the
  Ombudsman's and inspectors' powers, the Commission's administration, the forms.

## Scope

**In:** regs 2.12A, 2.12, 2.13, 2.14, 2.15 (subregs (1)-(4), (7)-(9A); there are no (5) and (6)), 3.01, 3.02, 3.03,
3.05, 3.06, 3.07, 3.29A, 3.45-3.48, 3A.03, 3A.05, 4.01, 6.01A, 6.01B, 6.04, 6.05, 6.07A.

**Out, and why:**
- **Schedule 3.1 and regs 3.04, 3.08, 3A.04, 6.06 (the schedule of costs):** a bill-of-costs tariff for lawyers'
  items, item by item; it caps what the FWC may award, but the claimant's question ("can I be ordered to pay costs") is
  answered by the Act (ss 570, 611), not by the schedule. A later layer could encode the item caps.
- **Regs 3.31-3.44 (employee records):** the employer's record-keeping duties; the employee meets them only as evidence. A
  later layer.
- **Reg 3.48's grace period (reg 7.06) and the other Chapter 7 transitional rules.**
- **Part 1-2 definitions and Part 1-3 (application of the Act):** read where needed; the borrowed terms are inputs.
- **Part 2-2 (parental leave extension), Part 2-4 (bargaining), Part 3-3 (industrial action and ballots), Part 3-4
  (right of entry), Chapters 3A-3B minimum standards orders, Part 4-1 Division 4 (infringement notices), Chapter 5
  (administration), Part 6-2 (model dispute term), Part 6-3, Part 6-3A, Parts 6-4C to 6-4DA:** not provisions a claimant
  meets in bringing or answering a claim, or machinery.
- **Regs 3.30, 6.07 (forms of notice to Centrelink):** an employer's form.
- **The CPI indexation formula (subregulation (4) of each fee regulation) and reg 3.05(4)(b), (5):** lost from the
  deposited text (finding 1); their results are inputs.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** reg 2.14(4)(c) "38 hours per week" against (2)(b)'s hours "in that year" -- `the full-time hours for reg 2.14`
  -- 38 x 52 = 1,976 hours -- 38 x 52 1/7 (1,981.43 hours), or the weeks of the contract year.
- **F2** reg 2.14(2)(c) -- `What is my fixed term contract's high income threshold` -- the product is not rounded --
  rounded to $100 as reg 2.13's threshold is.
- **F3** the fee regulations (8)(c)(ii) "at least 2 days before that date" -- `the refund conditions are met` -- two
  clear days between the discontinuance and the listed date (the listed date 3 or more days later) -- 2 days later is
  enough.
- **F4** reg 3.07(8) "a circumstance in which the FWC must refund" -- `the refund conditions are met` -- the circumstance
  not met: NOTHING (the list is not closed) -- JUST FALSE, as for the other fee regulations' "must repay ... if".
- **F5** regs 3.02(8), 3.03(8), 6.05(8) "listed for conducting a conference" -- `a listing that counts was made` -- only
  a conference listing counts, so an application listed only for a hearing still gets its refund -- any listing counts.
- **F6** regs 3.01(2), 6.04(2) "within ... 24 hours after the commencement of the absence" -- the certificate route --
  24 hours exactly is in time -- in time only before the 24th hour ends (the same here, as the input is in hours).
- **F7** regs 3.01(5)(a)(i), 6.04(4)(a)(i) "extends for more than 3 months" -- `lasts more than` -- later than the same
  day of the month three months on (clamped at a month end) -- counted in days (for example 91 or 92).
- **F8** regs 3.01(5)(b), 6.04(4)(b) "not on paid personal/carer's leave ... for the duration of the absence" read with
  (6)/(5) -- `the long-absence exclusion applies` -- any workers compensation during the absence takes it outside
  paid leave for the duration -- only the compensated part is taken out, and the rest still counts.
- **F9** reg 3.05(2)-(5) when no qualifying piece rates are paid -- `What piece rates are counted` -- 0 (nothing is
  counted) -- NOTHING (the subregulations do not apply).
- **F10** reg 2.12 (circumstances, not a closed list) -- `Is the deduction reasonable under the regulations` -- none of
  (1)-(3) met: NOTHING -- JUST FALSE.
- **F11** reg 3.29A with s 527F(3) -- `Can I apply for a stop sexual harassment order as a defence member` -- no
  circumstance: JUST FALSE (the Act's flat "cannot, except as provided by the regulations") -- NOTHING.
- **F12** regs 6.05(3)(c), (5) "if the result is 5 cents", "if the result is 0.0005" -- `What is this year's application
  fee` -- read as "ends in", as in the other fee regulations (finding 2) -- read literally, a result that is not exactly
  5 cents or 0.0005 is rounded to the nearest without a tie rule.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` answers. The rulings it follows:

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "unless expressly prohibited" (s 5), "is not liable" (ss 12, 12A), "shall not exceed" (s 23), "shall not
be made so as to affect prejudicially" (s 31(1)(a)), "no consent shall be required" and "shall not be necessary" (s 31(8),
(9)), "shall not apply" (ss 37(5), 63A(4)), "only if" (ss 16(3), 37(3)), "unless" (ss 15, 31(5), (6), 38(5), 63A(1)
proviso), the "if", "where" and "whenever" conditions of ss 11(2), 12A, 12D, 12E, 14, 16, 41(1), 41(6), 44, 48, 51(2)(i),
55, 63, 67, 68, and the periods "during the minority", "on attaining the age of eighteen years ... thenceforth" (s 37),
"at the expiration of the time fixed" (s 33(3)) and "after two-fifths ... has been paid" (s 17(4)) give `JUST FALSE`.
`NOTHING` is answered where ss 6(1), 6(3), 38 defer to the instrument or the Court (*points outside the text*), where

Applied here: "must also include" (reg 2.12A), "is not reasonable" (reg 2.12(3)), "is not a prescribed kind ... if"
(regs 3.01(5), 6.04(4)), the "if" conditions of regs 2.15, 3.29A (through s 527F(3)'s "cannot"), 4.01(3), (4), 6.01A,
6.01B and the fee regulations' (8), the "is" of reg 4.01(1), and the periods "on or after 6 December 2023", "on or after
1 November 2024 ... before 1 November 2026" give `JUST FALSE` (or a plain FALSE where the function answers a BOOLEAN).
`NOTHING` is answered where reg 2.12A does not apply to a saved authorisation (reg 2.12A(3)), where reg 4.01(1) yields to
rules of court (reg 4.01(2)), where reg 3.29A does not arise (the aggrieved person was not a defence member), where the
routes of regs 3.01, 6.04 ("exists if") are not met, where none of reg 2.12's circumstances holds, and where reg 3.07(8)'s
circumstance is not met (*limited by its own wording*, *silent*: none of these is closed with "only").

## What the Regulations turn out to say

1. **Formulas are lost from the deposited text.** Subregulation (4) of each fee regulation (3.02, 3.03, 3.07, 3A.03,
   3A.05, 6.05, 6.07A) says the indexation factor "is worked out using the following formula" and goes straight to
   "where:"; reg 3.05(4)(b) and (5) do the same. The formulas were images in the Word download and did not survive
   conversion. The definitions that follow (index number, most recent March year, previous March year) suggest a ratio
   of CPI sums over two March years, but that is not encoded: the factor and the formula amounts are inputs. A
   `F2009L02356.formulas.md` sidecar transcribed from the authorised rendering would let them be encoded.
2. **Reg 6.05 words its rounding differently.** Regs 3.02, 3.03, 3.07, 3A.03, 3A.05, 6.07A round to 10 cents "rounding
   up if the result ends in 5 cents" and the factor "rounding up if the result ends in 0.0005"; reg 6.05(3)(c) and (5)
   say "if the result is 5 cents" and "if the result is 0.0005". Read literally, reg 6.05's tie rule applies only to a
   result of exactly 5 cents; it looks like a drafting slip. The "ends in" reading is applied (F12). Nothing in any fee
   regulation stops the fee falling if the CPI falls (unlike reg 2.13, whose ratio "becomes 1"). Asserted.
3. **The refund rules are not the same across the fee regulations.** Regs 3.02, 3.03, 6.05 count only a listing "for
   conducting a conference", so an application listed only for a hearing is still refunded however late it is
   discontinued (F5; asserted); regs 3.07, 3A.03, 3A.05 count a conciliation, conference or hearing; reg 6.07A (stop
   bullying) counts a conference or hearing and has no two-day rule at all, so once a bullying application is listed no
   refund is due (asserted). Reg 3.07(8) alone frames the test as "a circumstance in which the FWC must refund", which
   leaves room for other circumstances (F4). Likewise reg 6.04 (unlawful termination, s 772) has no counterpart to reg
   3.01(4): evidence given for paid personal leave makes an illness or injury prescribed for s 352 but not for s 772
   (asserted).
4. **Reg 2.14(4)(c) gives a weekly figure for a yearly calculation.** (2)(b) needs the hours a full-time employee "would
   work in that year"; (4)(c) supplies "38 hours per week" without saying how many weeks (F1).
5. **Reg 2.14 does not round its result.** Reg 2.13 rounds the threshold to $100; reg 2.14(2)(c) multiplies it by a
   ratio rounded to 3 places and stops, so a part-time or part-year threshold can be in cents (F2; asserted: 96,310.60).
6. **"At least 2 days before"** (the fee regulations (8)(c)(ii)) does not say whether the days are clear. Two clear days
   are taken (F3), the cautious reading for an applicant deciding when to discontinue.
7. **Reg 2.15 has no subregulations (5) and (6)**; they appear to have been repealed or never made. The charity and
   medical research exceptions (7), (9) apply only to contracts entered into before 1 November 2026, so as at this
   compilation (and today, 7 November 2026) no new contract can use them (asserted on 1 November 2026).

## Before this is worth relying on

- Transcribe the lost formulas (finding 1) into a sidecar from the authorised rendering, and encode the CPI factor and
  reg 3.05(4)(b), (5).
- Deposit the published high income threshold and fee figures for each year (or the AWOTE and CPI series), so that the
  yearly chain can be run from 2009 rather than asked year by year.
- A lawyer's view on F1, F3, F5 and F8.
- An independent test pass, and the human gates.
- A seat for the employer (deductions, pay slips, fixed term contracts) beside this one, if wanted.
