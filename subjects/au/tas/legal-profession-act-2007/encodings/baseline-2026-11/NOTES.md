# Legal Profession Act 2007 (Tas), Part 3.3 -- baseline encoding, the client (costs agreements)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module
(`lpatas-dates.l4`, the only module that imports `daydate`), the rules and the 38 exported questions in
`lpatas-costs.l4`, and the worked cases in `lpatas-cases.l4`.

The focus asked for is **costs agreements**: what a person who retains a law practice for a claim (an injury,
compensation, insurance or employment claim, often on a no-win no-fee agreement) meets about the lawyers' own costs.
The Act is large (Chapters 1 to 8, 812 provisions), so only **Part 3.3 (Costs Disclosure and Assessment, ss 282 to 341)**
is encoded: Division 5 (costs agreements) nearly whole, and the machinery around it that the client meets -- disclosure
and the effect of failing to disclose, the basis of recovery and interest, bills and when the client can be sued, and
costs assessment with its time limits. The rest of the Act regulates admission, practising certificates, trust money,
indemnity insurance, the guarantee fund, complaints and discipline, and is out (see Scope).

## Edition

- **Act:** Legal Profession Act 2007 (Tas), No. 24 of 2007, the consolidated version published 2026-05-05 and current on
  the Tasmanian Legislation website on 6 November 2026, retrieved by its Chapters and Schedules on 2026-11-06:
  `../../registers/source-bundle/act-2007-024.txt` (how it was joined is in the `.meta.json`). The latest amendment in
  Part 3.3 is s 331(6) (inserted by No. 29 of 2017, the 4% fee).
- **Numbers set elsewhere:** the Legal Profession Regulations are not deposited. They may prescribe a disclosure
  threshold higher than $1,500 (s 295(1)(a)), further exemptions from disclosure (s 295(1)(f)), the maximum interest rate
  (s 305(4)), matters excluded from conditional costs agreements (s 307(2)), the forms of s 291(5) and s 315(3), and the
  rules on substantial connection (s 289). Each is asked as a fact. The statutory holidays of the Statutory Holidays Act
  2000 (business days, s 283) are not deposited either: the person states how many fall on a weekday in the period (fork
  F4). Penalties (100 penalty units for ss 308, 309) are not converted to dollars.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Two
deliberately wrong assertions (a cooling-off notice on the sixth business day asserted in time; proceedings on the 29th
day after the bill asserted allowed) were run once in a scratch copy, since deleted, and showed as "assertion failed"
(187 satisfied, 2 failed). After the verification fixes of 2026-11-07 (below) the cases file has 195
assertions, all satisfied.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpatas-dates.l4` | 0 | 0 | 0 | 0 |
| `lpatas-costs.l4` (38 questions) | 0 | 0 | 0 | 0 |
| `lpatas-cases.l4` | 0 | 0 | 195 | 195 |

Every expected value was worked by hand from the text before the run, and all held on the first run. Every exported
question has cases, with the edges: the $1,500 threshold at $1,500 and $1,500.01, and a higher prescribed amount at and
above it; each exception to disclosure, two at once; each disclosure item, two missing at once; the s 286(4) notice on
the 28th and 29th day; the 30-day interest start on day 29 and 30, a rate at and above the maximum; each excluded matter
for a conditional agreement; 4 and 5 cooling-off days; the cooling-off end from a Monday and a Friday, with a holiday, and
across the new year (three weekday holidays: 25 and 28 December 2026 and 1 January 2027, so the end is Monday 4 January,
with the undercount that lands on New Year's Day shown too); a notice on the last business day and the day after, and before the agreement; the uplift fee at
exactly 25% and one cent over, outside litigation, and outside a conditional agreement; each s 311 ground and three at
once; each repayment rule, capped by the agreement and by the scale; the itemised bill on day 21 and 22; suing on day 29
and 30 after the bill, after an itemised bill, with a court order on a lump sum and on an itemised bill; the 60-day
assessment limit on day 60 and 61, from payment, for a sophisticated client; a 15% reduction exactly and $1 short; the
14-day review limit with a longer and a shorter time allowed.

**No mirror cases.** One seat.

## Seat

**The client** (`lpatas-costs.l4`): the person for whom a law practice provides legal services, asking in their own
words -- "Must I be told the costs?", "Can my claim be no-win no-fee?", "Is the uplift fee allowed?", "Is my costs
agreement void, and what must be repaid?", "By what day can I cool off?", "Can the law practice sue me yet?", "By what
day must I apply for a costs assessment?". Where the Act gives the client's rights to an **associated third party
payer** (a person who owes the law practice the client's costs: ss 284, 300, 302, 306(6), 319), the questions say so and
accept that person. The law practice, the costs assessor, the Supreme Court, the Board and the Law Society get no seat;
their duties and powers appear as what the client is owed, what may be done to the client, and by when. A seat for the
law practice (a business with duties: disclosure, billing, the cooling-off period) would be a further layer.

**Defaults followed.** The Act alone (the regulations not deposited, their numbers asked); the actors the text names; the
costs assessor's and the Supreme Court's judgments ("if satisfied", "just and fair", "unless the costs assessor
otherwise orders") answered conditionally or taken as inputs, never decided; the Act's own definitions in L4 (third
party payer, sophisticated client, uplift fee, litigious matter, business day so far as the weekends go); one case is
one matter and one costs agreement; the Act's terms with plain glosses ("no-win no-fee" glosses a conditional costs
agreement); the operative provisions in, the machinery out. **One departure:** the statutory holidays in a business-day
count are asked as a number, not worked out (fork F4).

## Scope

**In** (Part 3.3):
- Division 1: s 283 (sophisticated client, uplift fee, litigious matter, business day), s 284 (third party payers).
- Division 2: ss 285, 286 (including the 28 days of s 286(4)), 287(1), (2).
- Division 3: ss 291(1), (4) and 292 (as a checklist), 294(1), (2) (in the disclosure question's gloss), 295(1), (2), (5)
  (exceptions, the $1,500 threshold), 296 (settlement), 297 (uplift), 300(1), (2), (3) (a further ground to apply to set
  the agreement aside, in the s 312 question), (5), 301(1), (2) (reports and what they cost).
- Division 4: s 303 (basis of recovery), s 305 (interest).
- Division 5: ss 306(2) to (5), 307 (excluded matters, formal requirements, cooling-off, what may be recovered after
  cooling off), 308 (uplift fees, the 25% cap), 309 (contingency fees), 311 (void agreements and repayment), 312(1),
  (5), (6), (12) with s 306(6) (setting aside).
- Division 6: s 313(1) to (3) (no suit for 30 days, the court order, the stay), s 314(1) (bill forms, in the glosses),
  s 316(1), (2), (4), (5) (itemised bills, 21 days, 30 days). Regulative: s 316(2) (MUST within 21 days) and ss 313(1), 316(4), (5) (SHANT
  for 30 days), run by EVALTRACE inside the questions.
- Division 7: s 319(1), (2), (5), (6), s 321(4), s 323(b), s 328(1), s 331(2), (3), (6), ss 333(1), 334(1), (2), s 338.

**Out**, and why:
- s 282 (purposes), s 288 (where instructions are received: in the glosses only), s 289 (regulation-making), s 290
  (matters moving between jurisdictions: a two-period split, rare for a single claim; fork F1), s 287(3).
- ss 291(2), (3), (5) to (7), 293 (disclosure where another law practice is retained: the client sees it through the
  s 296 and s 300(5) questions), 294(3), 295(3), (4), 298 (plain language, oral disclosure), 299 (ongoing disclosure:
  "as soon as is reasonably practicable" has no countable deadline), 300(4), (6), (7) (the assessor's discretion and
  professional conduct), 301(3), (4) (a law practice retained by another: the client's reports come from the practice
  the client retained), 302 (disclosure to associated payers, beyond what the questions accept).
- s 304 (security for costs: the law practice "may take reasonable security", a judgment with no countable rule).
- s 306(1) (who may make a costs agreement, inter-practice agreements), s 310 (enforced like any contract), s 312(2) to
  (4), (7) to (11) (the assessor's considerations, orders and procedure).
- s 313(4) (costs agreement or not: the questions do not turn on it), ss 314(2) to (7), 315, 316(6) (how a bill is signed
  and given, and the rights statement: taken as the fact "a bill has been given"), s 316(3) (a request by a person liable
  for part of the costs reaches only that part: the extent of a request, not whether or when it may be made), s 317
  (interim bills).
- s 321(1) to (3) (which costs the law practice itself may put to assessment: the question asks only from what day it
  may apply), s 323(a) (no payment into court), s 328(2) (what the assessor need not examine), s 331(1), (4), (5) (the
  assessor fixing the costs of assessment, costs of delay, referral to the Supreme Court: the assessor's and the Court's
  discretion).
- ss 318, 319(3), (4), (7) to (10), 320 (applications by a retaining law practice), 322 (form of application; the fee
  waiver on serious hardship is the assessor's judgment), 324 to 327, 329, 330, 332, 333(2) to (6), 334(3), (4), 335 to
  337, 339 to 341: procedure, the assessor's powers and criteria, certificates, enforcement, referral for discipline,
  regulations and imputation.
- Every other Chapter and Part of the Act (admission, practising certificates, trust money, professional indemnity
  insurance, the Solicitors' Guarantee Fund, incorporated practices, foreign lawyers, complaints and discipline, the
  Board and Tribunal): not costs agreements, and not met by a client bringing a claim.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they fall here (questions the text always answers return a plain BOOLEAN or a choice; the others a MAYBE):
- No (FALSE / JUST FALSE): s 284 and s 283 ("is ... if", "means"); ss 285 to 287 ("applies if", "has no effect if");
  s 296, s 297 ("If"); s 300(1) once the costs are assessed ("unless they have been assessed"); s 305 ("must not ...
  unless", "may not"); s 307(2) ("except"); s 307(3), s 306 and s 308 ("must"); the cooling-off period (a period the text
  fixes); s 309 ("must not"); s 316(1) ("If"); s 319(6) for a sophisticated client ("otherwise than by"); s 328 ("if ...
  unless"); s 334 ("A party who objects", a period the text fixes).
- `NOTHING`: s 300(1) where nothing required went undisclosed, or the s 300(5) exception applies (s 300 does not answer
  whether payment can be held back); s 307(6) where the client did not end the agreement in the cooling-off period (the
  agreement governs); s 308(4) outside a litigious matter (the Act sets no cap); ss 313, 316 while an itemised bill the
  client asked for is outstanding (no day can yet be named).

### Forks

Each line: the provision, the function, the answer taken, the other reading.

- **F1** ss 287(3), 290, `ss 285 to 287 -- does Part 3.3 apply to my matter`: a later agreement or notice bringing the
  Part back after displacement, and the split of costs between periods, are not modelled; other reading: model s 287(3)
  as a further input.
- **F2** ss 291, 292, 295, `ss 291, 292 -- was I told everything` and `s 295 -- must the law practice give me costs
  disclosure`: the first missing item, and the first exception that applies, in the Act's order are reported; other
  reading: report all.
- **F3** s 300(1), `s 300(1) -- may I hold off paying until the costs are assessed`: once the costs are assessed, JUST
  FALSE (the "unless" is met and s 300 no longer excuses payment); other reading: NOTHING (the Act then leaves payment to
  the certificate, s 336).
- **F4** s 283 "business day", s 307(3)(e), `s 307(3)(e) -- by what day can I cool off`: Saturdays and Sundays are
  worked out; the statutory holidays falling on a weekday in the period are a number the person gives, each pushing the
  end one weekday on, and they are counted to the end of the period as the holidays extend it (a Monday on which a
  weekend holiday is observed counts); "clear" days start the day after the agreement is made; other reading: count from
  the day after the client receives the signed agreement.
- **F5** s 306(3), (4), `s 306 -- the agreement is properly made`: the s 306(4) statements are required of every
  agreement made by accepting a written offer, whether accepted in writing or by conduct; other reading: only where
  acceptance is by conduct.
- **F6** s 307(3)(e), (6), `s 307(3)(e) -- by what day can I cool off`: where the agreement gives fewer than 5 business
  days (and is void for that, s 311), the 5 days are used; other reading: the agreement's shorter period, or no cooling-off
  rule at all for a void agreement.
- **F7** ss 283, 308(1), `s 308 -- the uplift fee is allowed`: an uplift fee is allowed only in a conditional costs
  agreement (s 308(1)), and s 307 applies to the whole of a conditional agreement that carries one, despite the s 283
  definition (finding 2); other reading: a non-conditional uplift fee falls outside s 308 and is left to s 309 and the
  general law.
- **F8** s 311, `s 311 -- is my costs agreement void`: where several provisions are broken, the one with the heaviest
  consequence is reported (s 309, then s 308, then s 307, then s 306); other reading: report each.
- **F9** s 311(3), (4), `s 311 -- how much must the law practice repay me`: under s 308 the uplift paid is repaid, and
  the rest is capped at the lesser of the scale or fair value and the agreement without the uplift; under another
  contravention, at the lesser of the scale or fair value and the whole agreement; the s 303 figure is the person's (an
  assessment); other reading: under s 308 only the uplift is repaid.
- **F10** s 316(1), `s 316(1) -- can I ask for an itemised bill`: "any person who is entitled to apply for an assessment"
  is read as the client or a third party payer liable for the costs, without testing the s 319(5) 60 days; other
  reading: once the 60 days have passed (and no extension is given), the right to an itemised bill goes too.
- **F11** s 313(2), `ss 300, 313, 316, 323 -- can the law practice sue me for costs`: a court order lifts only the
  s 313(1) bar; for a lump sum bill, s 316(4) and (5) still bar suit for 30 days (finding 3); other reading: the order
  authorises suit despite s 316 too.
- **F12** s 321(4), `s 321(4) -- from what day can the law practice apply for assessment`: (a), (b) and (c) are
  alternatives, so the earliest day any allows (another person's application can come first, finding 5); other reading:
  30 days must also have passed since another person's application.
- **F13** periods: "within 60 days after", "within 21 days after", "within 14 days after", "within 28 days" let the last
  day be the day plus the number; "at least 30 days after" and "unpaid 30 days or more after" first allow the day plus
  30; other reading: the Acts Interpretation Act 1931 (Tas), not deposited, may count differently when the last day is a
  weekend or holiday.

## What the Act turns out to say

1. **A note points at the wrong subsection.** The note to s 312(1) says "Section 300(2) (Effect of failure to disclose)
   also enables a client to make an application under this section"; it is s 300(3) that does so (s 300(2) bars the
   law practice from suing). Notes are not part of the Act, so nothing turns on it. Not encoded.
2. **A conditional costs agreement with an uplift fee is, by definition, partly not one.** s 283 defines a conditional
   costs agreement as one making payment conditional on success "but does not include a costs agreement to the extent to
   which section 308 ... or section 309 ... applies", while s 308(1) says "A conditional costs agreement may provide for
   the payment of an uplift fee". Read literally, the uplift part of a no-win no-fee agreement escapes s 307 (cooling-off,
   signature, independent advice statement). Encoded as applying s 307 to the whole agreement (fork F7).
3. **A court order to sue a departing client early does not reach a lump sum bill.** s 313(2) lets a court authorise
   proceedings "sooner" than s 313(1) allows, if the person is about to leave Tasmania; but s 316(4) separately bars
   proceedings on a lump sum bill until 30 days after it is given (and s 316(5), after a requested itemised bill), and
   s 313(2) does not mention s 316. Asserted (an order lets suit proceed on day 4 on an itemised bill, not on a lump sum
   bill; fork F11).
4. **The disclosure promises a 30-day limit that the billing Division does not state.** s 291(1)(b)(iii) says the client
   must be told of the right to "request an itemised bill within 30 days after receipt of a lump sum bill", but s 316(1)
   sets no time for the request: anyone entitled to apply for assessment may ask. Encoded per s 316 (fork F10).
5. **The law practice's own assessment start can be brought forward by another person's application.** s 321(4) lets
   the law practice apply once 30 days have passed since (a) the bill, (b) payment, or (c) "an application has been made
   under this Division by another person". s 321(1) requires a bill only for the law practice's own application; a client
   or third party payer may apply before any bill, for costs paid without one (s 319(1), (4)), so (c) can come before (a)
   and, read as an alternative, bring the day forward. Asserted (an application on 15 June leaves the day at 1 July after
   a bill on 1 June; an application on 5 May, before a bill on 1 June, brings it to 4 June). Corrected on 2026-11-07: the
   first version said (c) could only fall after (a) and never came first; the code already took the earliest day.
6. **The uplift fee cap is 25% only in litigation.** s 308(4)(b) caps the uplift at 25% of the legal costs (excluding
   disbursements) otherwise payable "If a conditional costs agreement relates to a litigious matter"; elsewhere the Act
   sets no cap, only disclosure (s 297) and an estimate (s 308(3)). A litigious matter includes one "likely to involve"
   proceedings, which covers most injury claims before they are filed. Asserted (25% exactly and one cent over).
7. **Sharing in the payout is prohibited outright, and costs the law practice everything.** s 309 bars any fee
   calculated by reference to the award, settlement or property recovered (except by adopting a scale), and s 311(5) then
   denies the law practice any amount for its services in the matter, with repayment recoverable as a debt (s 311(6)).
   Asserted.
8. **The $1,500 disclosure threshold excludes disbursements and GST, and is a floor.** s 295(1)(a): the higher of $1,500
   and any prescribed amount; costs exactly at the threshold need no disclosure, and s 295(2) revives the duty once the
   costs become likely to exceed it. Asserted.
9. **The Supreme Court alone can let a late assessment application proceed, and never for a sophisticated client.**
   s 319(6) and its note. Asserted (day 60 and 61).
10. **A client who was not told the costs cannot be sued until they are assessed.** s 300(2) (with s 323 while an
    assessment is under way) blocks proceedings even after the 30 days of s 313. Asserted.
11. **The costs of the assessment follow a 15% reduction.** s 331(2): a cut of 15% or more, or a disclosure failure, puts
    the costs of the assessment on the law practice unless the assessor orders otherwise; s 331(6) (2017) adds a Court fee
    of up to 4% of the amount allowed. Asserted (15% exactly, and $1 short).

## Before this is worth relying on

- The Legal Profession Regulations (Tas), deposited, for the prescribed disclosure threshold, exemptions, the maximum
  interest rate, excluded matters, the prescribed forms and the substantial-connection rules.
- The Statutory Holidays Act 2000 (Tas), for business days (fork F4), and the Acts Interpretation Act 1931 (Tas) for
  counting periods (fork F13).
- The Legal Profession (Conduct) rules and any scale of costs (the Supreme Court scale), for s 303(b) and s 329.
- An independent test pass, and a lawyer's look at the forks, especially F3, F7, F9 and F11, and at findings 2 and 3.
- The claims themselves (injury, compensation, limitation) are in other Acts and are not here; nor are a court's costs
  orders between the parties, which this Part does not govern.
- Wider sources: no guidance from the Law Society of Tasmania or the Legal Profession Board and no court decision was read.
