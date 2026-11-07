# Legal Profession Act 2006 (ACT), Part 3.2 (costs agreements) -- baseline encoding, the client

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for was costs agreements: what a person bringing a claim (a personal injury, workers compensation, will or
discrimination claim) meets when a lawyer acts for them on a costs agreement, including a no-win no-fee one. Division 3.2.5
(costs agreements) is encoded apart from s 286 (enforcement and mediation), with the claims machinery around it in Part 3.2: whether the Part applies, the duty to
disclose costs and what follows a failure, the basis of charging, interest, itemised bills, when the lawyer may sue for
costs, the time to apply for a costs assessment, and what follows an assessment.

No encoding of this Act existed; this is the first, so nothing was extended or touched. The dates are in one small module
(`lpact-dates.l4`, built-in date functions only, no daydate), the rules and the 29 exported questions in `lpact-costs.l4`,
and the worked cases in `lpact-cases.l4`.

Two duties with deadlines are regulative rules run by EVALTRACE inside exported questions that take only plain facts:
the law practice's bar on starting a proceeding to recover costs (`SHANT ... WITHIN`, s 289 (1), s 292 (6) and (7)), and
the client's 12 months to apply for a costs assessment (`MUST ... WITHIN ... LEST BREACH`, s 294A (5)).

## Edition

- **Act:** Legal Profession Act 2006 (ACT), A2006-25, Republication No 45 (R45), effective 16 May 2026, as deposited at
  `../../registers/source-bundle/A2006-25.txt` (converted from the register's DOCX, which the register marks as an
  unauthorised version; the authorised text is the register's PDF). Retrieved 6 November 2026.
- **Numbers set elsewhere:** the interest cap of s 281 (4) (b) is "the rate applying under the Court Procedures Rules 2006,
  schedule 2, part 2.2 (Interest after judgment)". That instrument is deposited
  (`subjects/au/act/court-procedures-rules-2006/registers/source-bundle/SL2006-29.txt`, same licence): items 2.3 and 2.4
  set, for any half-year after 30 June 2010, 6% above the cash rate the Reserve Bank last published before the half-year
  began, for both the Supreme and the Magistrates Court. The cash rate is the client's input.
- **Regulations not deposited:** the Legal Profession Regulation 2007 may prescribe a higher threshold than $1 500 (s 272
  (1) (a), s 292 (10)), an interest rate (s 281 (4) (a)), further exceptions to disclosure (s 272 (1) (f)) and the rules for
  "substantial connection" (s 267). It is not deposited. The Act's own figures are used, as the encoding guide directs; a
  prescribed figure would change the answers.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 284 (4) (b) cap on $20 000 asserted as $5 000.01) was run once in a scratch copy, since
deleted, and showed as "assertion failed" (154 satisfied, 1 failed). After the independent verification the cases were
corrected and extended (2026-11-07, below) and all files re-run.

**Fixes after the independent verification (2026-11-07).**
- s 281: the interest question refused all interest where a costs agreement provided for interest but the bill did not
  say it was payable under the agreement. s 281 (2) is an additional route ("may also"), and s 281 (3) (c) is asked only
  of agreement interest, so the s 281 (1) route is still open on (3) (a) and (b). The question now falls through to
  s 281 (1); the wrong case was corrected and two added.
- Fork F5 now takes the clear-days reading of "until at least N days after the day": all N days must have passed, so the
  earliest day is day N + 1 (1 August after a 1 July bill, not 31 July). The bar and the earliest-day question share one
  definition of the barred days and named lengths (`the s 289 (1) days`, `the s 292 (6) days`, `the s 292 (7) days`), so
  the deadline lives in one place.
- The out list now names s 283 (4), s 289 (3), s 292 (5) and (9); s 281 (5) is taken in through the bill-day input; s 286
  is listed once (out).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpact-dates.l4` | 0 | 0 | 0 | 0 |
| `lpact-costs.l4` | 0 | 0 | 0 | 0 |
| `lpact-cases.l4` | 0 | 0 | 156 | 156 |

Every exported question has cases, with the edges: s 264 (4) notification on day 28 and day 29 after being told; disclosure
at exactly $1 500 and at $1 500.01; each s 272 exception; each s 282 and s 283 requirement failing in turn, and the
sophisticated client's exemptions (and what they do not reach); a cooling-off notice on the last day and the day after; an
uplift fee of exactly 25% and one cent over, and outside a litigious matter; each kind of void agreement, with fair value
below, between and above the agreement figures; the s 281 example's own dates (bill 1 May 2008; 31 May and 1 June); an
itemised bill asked for on day 90 and day 91, at $1 500 and $1 500.01; s 281 (1) interest where the bill fails s 281 (3) (c);
suing on day 30 and day 31 after a bill, day 90 and day 91 after a lump sum bill, day 30 and day 31 after an itemised bill,
before the bill, and with leave to sue sooner; an
assessment application on the last day of the 12 months and the day after, before time began, and from 29 February 2024;
costs cut by exactly 15% and by 14.99%.

**No mirror cases.** One seat.

## Seat

**The client** (`lpact-costs.l4`): the person who retains a lawyer (a "law practice") for a matter and pays, or is asked to
pay, the legal costs: "Does Part 3.2 apply to my matter?", "Must my lawyer tell me what it will cost?", "Is my no-win no-fee
agreement valid?", "Can I still cool off?", "Is the uplift fee allowed, and what is the most it can be?", "Is this a
prohibited contingency fee?", "What can my lawyer recover if the agreement is void, and what must they repay?", "Can I have
the agreement set aside?", "May my lawyer charge interest, and at what rate?", "Can I ask for an itemised bill, and by
when?", "When can my lawyer sue me?", "Am I in time to have the bill assessed?", "Who pays for the assessment?".

The Part puts its duties on the law practice ("must disclose", "must not enter into", "must not start a proceeding"); the
encoding turns them into what they mean for the client. No law practice seat was written: the brief asks for the claimant's
seat, and the practice's offences (ss 284 (6), (7), 285 (3), (4)) are out (below). The Supreme Court, the law society
council and the ACAT get no seat.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed: the Court Procedures Rules' judgment rate for
  s 281 (4) (b). The Legal Profession Regulation is not deposited (above).
- **The actors the text names.** Followed: the client, the law practice (and through s 307 its principals), the Supreme
  Court, the law society council (s 304), an associate (s 307A). Third party payers are left out (below).
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the matter has a "substantial
  connection" with the ACT (s 264, regulation-set); whether a principal decided "on reasonable grounds" (s 272 (1) (b));
  "clear plain language" (s 283 (3) (c) (ii)); the law practice's "reasonable belief" (s 284 (4) (a)); whether the Supreme
  Court is satisfied the agreement is not fair or reasonable (s 288); the fair and reasonable value or scale amount (s 279,
  s 287 (2)); whether the court is satisfied of a disclosure failure (s 302 (2) (b)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "sophisticated client" (s 261, from
  s 272 (1) (c), (d)), "litigious matter" (s 261, from whether proceedings are started or likely), "threshold amount"
  (s 292 (10)), "conditional costs agreement" and "uplift fee" (s 261, as the facts asked). Asked: "scale of costs",
  "business day", "corresponding law", the Corporations Act categories of s 272 (1) (c) (one yes/no).
- **One case is the text's natural unit.** Followed: one matter, one law practice, one bill.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts ("uplift fee (success fee)",
  "conditional (no-win no-fee) costs agreement").
- **Operative sections in; machinery out.** Followed.

## Scope

**In.** s 261 (the definitions used); ss 263, 264, 265 (application and displacement), with s 268 (2) in an answer; s 269
with ss 271, 272 and 275 (the duty to disclose, when and how, its exceptions); s 274 (uplift disclosure); s 277 (effect of
failure to disclose); s 278 (1), (2) (progress reports); s 279 (basis of recovery); s 281 (interest; (5) through the bill-day input); **Division 3.2.5**
apart from s 286 (s 282 making costs agreements, s 283 conditional costs agreements and cooling off, s 284 uplift fees,
s 285 contingency fees, s 287 void agreements, s 288 setting aside); s 289 (1), (2), (4) (no proceeding until 30 days after
a bill); s 292 (1) to (4), (6) to (8), (10) (itemised bills and the 90-day bar); s 294A (1), (3) to (7) (the client's application and its time limit);
s 298 (b); s 300C; s 302; s 304; s 304A; s 307A (claim farming).

**Out, and why.**
- ss 266 to 268 apart from s 268 (2), s 270 (disclosure where another law practice is retained), s 273 (settlement
  estimates), s 276 (ongoing disclosure), s 278 (3), (4): duties between law practices or details that add no question
  the client asks beyond "was everything disclosed?", which s 277 takes as one fact.
- s 278A, s 261A, s 282 (1) (d), (6), s 294A (2), (8) to (10) (third party payers): another person, not the client.
- s 280 (security for costs), s 286 (enforcement as a contract, mediation), s 293 (interim bills), s 299 to s 300B
  (assessment procedure and criteria), s 301 (bound by a lump sum bill), s 303 (referral to ACAT): the Supreme Court's
  procedure and discretions, with nothing the client can be told on plain facts beyond what is encoded.
- s 290 and s 291 (form and giving of a bill, statement of rights): asked as one fact ("a bill complying with ss 290 and
  291") in the suing questions.
- s 295, s 296 (law practices' own applications for assessment), s 297 (form of application).
- s 283 (4) (conditional costs agreements between law practices, under s 282 (1) (c)): not the client's agreement.
- s 289 (3) (a court must stay a proceeding brought too early): the court's procedure; the suing questions already say
  the proceeding may not be started.
- s 292 (5) (a person liable for only part of the costs asks only about that part): one case is the client liable for the
  whole bill; s 292 (9) (ss 290 (2) and (5) applied to an itemised bill): the form of a bill, taken with ss 290 and 291 as
  one fact.
- ss 284 (6), (7) and 285 (3), (4) (offences, 50 penalty units each): they bind the law practice and its principals, not
  the client; the client's consequences (void agreement, repayment) are encoded through s 287.
- ss 262, 305 to 307 (purposes, regulation-making, imputation, principals' liability): machinery.
- The Civil Law (Wrongs) Act 2002 parts 14.1 and 14.2 (costs caps in personal injury claims, referred to in the notes to
  ss 283, 284 and 300) and part 15.4A (claim farming): another Act; the conviction is asked as a fact.
- No requirement ledger exists for the ACT, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 264 (1) (a) "this part does not currently apply" and s 265 (3) -- `ss 263 to 265 -- does Part 3.2 apply to my
  matter` -- read as "the client did not first instruct the law practice in the ACT"; displacement under s 265 is final
  within the one question -- a later s 264 agreement or notification re-applying the Part (s 265 (3)) as a further answer.
- **F2** s 284 (1) "A conditional costs agreement may provide for the payment of an uplift fee" -- `s 284 -- is my uplift
  fee allowed` -- an uplift fee in an agreement that is not a conditional costs agreement meeting s 283 contravenes s 284
  (so s 287 (4) applies) -- it contravenes only s 283 (void under s 287 (1), but s 287 (4) not engaged).
- **F3** s 282 (5) against s 304A -- `s 282 -- is my costs agreement in the required form` -- a sophisticated client's
  term excluding assessment is a valid contracting out, not a contravention of s 282 (5) -- s 282 (5) voids it whatever the
  client (s 304A then working only by a separate agreement).
- **F4** s 281 (1) "unpaid for 30 days or longer after the day the practice gave a bill" -- `s 281 -- may my lawyer charge
  me interest` -- interest may be charged once the costs are still unpaid after the 30th day after the bill day (paid on
  day 30: no interest; unpaid on day 31: interest from the day after the bill, as the example says) -- unpaid at any time on
  day 30 being enough.
- **F5** s 289 (1), s 292 (6), (7) "until at least N days after the day" -- the suing questions and the regulative rule --
  all N days must have passed (the clear-days reading of "at least N days"), so the earliest day is day N + 1 after the
  bill day (1 August after 1 July) -- day N (31 July). Changed to this reading after the independent verification; the
  ACT Legislation Act 2001, which could settle it, is not deposited.
- **F6** s 289 (2) (a court may authorise a proceeding "sooner") -- the suing questions -- lifts the s 289 (1) bar only,
  not the s 292 (6) or (7) bars -- lifts every bar in Division 3.2.6.
- **F7** s 287 (3) and (4) together, under a void agreement that contravened s 284 -- `the most recoverable under s 287` --
  the cap is the agreement amount less the uplift fee, and the scale or fair value if lower -- the cap is the full agreement
  amount, (4) striking only amounts labelled as the uplift fee.
- **F8** s 288 (1) "a client who is a party to a costs agreement" -- `s 288 -- can I have my costs agreement set aside` --
  a client who is not a party: NOTHING-kind (a scope limit with no "only"; s 277 (3) and s 282 (6) widen it) -- the text's
  no.
- **F9** s 294A (5) "12 months after the day" -- `12 months after`, `s 294A -- am I in time ...` -- the same date a year
  later; from 29 February to a year without one, 28 February -- 1 March (the date rolled forward).
- **F10** s 292 (7) "However, if the person asks for an itemised bill" -- the suing questions -- once an itemised bill is
  asked for, the 30 days after it replace the 90 days of s 292 (6) -- both bars apply (the later of the two days).
- **F11** s 272 (1), several exceptions at once -- `s 272 -- must my lawyer disclose the costs to me` -- the first in the
  Act's order is reported (the answer "no" is the same) -- report all.
- **F12** s 283 (3) (e) "during which the client may ... terminate" -- `s 283 (6) -- can I still cool off` -- the period's
  last day is the client's fact (business days are not counted here); notice on the last day is in time -- the encoding
  counting 5 business days from the agreement, with ACT public holidays (Holidays Act 1958, deposited) as a further input.
- **F13** s 277 "anything required by this division" -- `s 277 -- what follows ...`, the suing questions -- one yes/no fact
  for the whole of Division 3.2.3 -- one question per disclosure item.
- **F14** ss 263 and 264, both failing -- `ss 263 to 265 ...` -- the text's no ("This part applies to a matter if ...":
  an "if" condition), with a corresponding law of another jurisdiction presumably applying (not said) -- NOTHING.
- **F15** s 292 (1) and (2), "any person who is entitled to apply for an assessment" -- `s 292 -- can I ask for an itemised
  bill` -- the client is taken to be entitled (s 294A (1)), even out of the s 294A time -- the request barred once no
  assessment can be applied for.

Sites decided without a fork line: the "means" definitions of s 261 answer FALSE when an element fails; "must not",
"may not" and "is not entitled" (ss 278 (2), 281 (3), 284, 285, 287, 289, 292, 298, 307A) are flat negatives answered as
the text's no; the 12-month, 90-day, 28-day and cooling-off periods are periods the text fixes, so outside them the answer
is the text's no (ruling (a) of 2026-11-05), except where s 294A (6) itself gives the court a way in.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding answers mostly with choices from a list rather than MAYBE BOOLEAN: the answers marked "(the text's no)" are
the JUST FALSE answers; the answer marked "NOTHING-kind" (s 288, F8) and the questions that return NOTHING (the s 284 (4)
(b) cap outside a litigious matter; s 287 for an agreement that is not void; s 307A without a conviction; the last day to
ask for an itemised bill where s 292 does not apply; the earliest day to sue while suing is barred outright) are the
NOTHING answers. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **The note to s 282 (3) cites the wrong paragraph.** It says acceptance by other conduct is not permitted for
   conditional costs agreements "(see s 283 (3) (c) (i))". Paragraph (c) (i) is "in writing", which a written offer accepted
   by conduct satisfies; the requirement that excludes acceptance by conduct is (c) (iii), "signed by the client". The
   encoding follows (c) (iii), which also explains why a sophisticated client, exempt from (c) (iii) by s 283 (5), can accept
   by conduct. Asserted (the s 282 cases with and without a sophisticated client).
2. **The uplift cap applies only in litigious matters.** s 284 (4) caps the uplift fee at 25% of the legal costs otherwise
   payable (excluding disbursements) only "If a conditional costs agreement relates to a litigious matter"; outside one the
   Act sets no cap, though "litigious matter" reaches any matter where proceedings are merely likely. Asserted (a $9 000
   uplift on $20 000 outside a litigious matter is allowed; the cap question answers no figure).
3. **A contingency fee forfeits everything; a bad uplift forfeits only the uplift.** s 287 (5) leaves the law practice
   nothing for its services under an agreement contravening s 285; s 287 (4) takes only the uplift fee where s 284 is
   contravened; any other contravention leaves the scale or fair value, capped at the agreement. Asserted.
4. **s 287 (3) and (4) leave open what cap applies after a s 284 contravention** (fork F7).
5. **s 292 (6) and (7) leave open whether the 90-day bar survives a request for an itemised bill** (fork F10). On the
   reading taken, an itemised bill given early can let the law practice sue before day 91 (asserted: 15 September after a
   1 July bill, itemised bill on 15 August).
6. **s 281 (1)'s example confirms interest runs back to the day after the bill**, not from day 31, once the 30 days have
   passed; the boundary day itself is not settled by the example (fork F4). The cap is the judgment rate (cash rate plus 6
   points) unless a regulation prescribes one.
7. **s 281 (4) (b) and s 300C (3) (b) point to "schedule 2, part 2.2" of the Court Procedures Rules, which has separate
   Supreme Court and Magistrates Court tables.** For any period after 30 June 2010 they agree (6% above the cash rate), so
   the encoding does not ask which court; for earlier periods they differ, and the Act does not say which applies.
8. **Disclosure thresholds are drafted two ways for one figure.** s 272 (1) (a): "$1 500 (exclusive of GST)" of "total legal
   costs ..., excluding disbursements"; s 292 (10): "$1 500 (exclusive of GST and disbursements)". They come to the same,
   but s 272 (1) (a) asks whether costs are "likely" to exceed it and s 292 (1) whether a bill "exceed[s]" it: $1 500 exactly
   is under both. Asserted.
9. **Small drafting slips**, not affecting the encoding: s 284 (7) lacks the full stop after "commits an offence"; s 277 (5)
   (b) ends with a semicolon; s 274 (2) cites "section 269 (Disclosure of costs to client)" where the heading reads "clients";
   s 288's heading ("Setting aside costs agreements or provisions of costs agreements") differs from the short title cited in
   ss 269, 277, 282, 291 and 300A ("Setting aside costs agreements").
10. **The claimant's caps are elsewhere.** The notes to ss 283, 284 and 300 point to the Civil Law (Wrongs) Act 2002 parts
    14.1 and 14.2 (maximum costs for certain personal injury damages claims; no reasonable prospects of success). A personal
    injury claimant's costs may be limited by those parts beyond anything this Part says; they are not encoded here.

## Before this is worth relying on

- The Legal Profession Regulation 2007 (ACT), for any higher threshold, prescribed interest rate, further disclosure
  exceptions and the "substantial connection" rules; not deposited.
- The Civil Law (Wrongs) Act 2002 parts 14.1, 14.2 and 15.4A, for the personal injury costs caps and claim farming.
- A lawyer's view on forks F2, F3, F5, F7 and F10 and findings 1, 4 and 5; an independent test pass and a human gate.
