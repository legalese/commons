# Legal Profession Act 2006 (NT) -- baseline encoding, costs agreements, the client

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`lpcnt-dates.l4`,
built-in date functions only, no daydate), the rules and exported questions in `lpcnt-costs.l4`, and the worked cases in
`lpcnt-cases.l4`.

The focus asked for: **costs agreements**. The Act is large (over 700 sections); Part 3.3 (costs disclosure and
assessment) alone runs from s 294 to s 372. The encoding takes **Division 5 of Part 3.3 whole** (ss 317 to 323), with the
definitions and the claims machinery a client meets around it: who is a sophisticated client, the uplift fee disclosure
of s 308, the basis of recovery in s 314 that a void agreement falls back on, the assessment of complying costs
agreements under s 339, contracting out under s 343, and the 28 days to seek review of a set-aside under s 352(2)(a).
Two duties with deadlines are regulative rules run by EVALTRACE inside exported questions that take only plain facts:
the cooling-off period of a conditional costs agreement (s 318(3)(e), (6)(b): the client's written notice within the
period brings in a prohibition on the law practice recovering the uplift fee), and the time to apply for review of a
s 323 determination.

The Act sits in the claims set because a person bringing a personal injury or compensation claim in the Northern
Territory is usually offered a "no win, no fee" conditional costs agreement with an uplift fee; whether that agreement
is valid, and what the client pays if it is not, are the questions encoded.

## Edition

- **Act:** Legal Profession Act 2006 (NT), reprint REPL007, as in force at 1 August 2025, the current reprint on the NT
  Legislation register when retrieved on 6 November 2026:
  `../../registers/source-bundle/Legal-Profession-Act-2006-NT-current-reprint-REPL007.txt`.
- **Numbers set elsewhere:** the Legal Profession Regulations (NT) prescribe the percentage that caps an uplift fee in a
  litigious matter (s 319(4)) and may prescribe proceedings in which no conditional costs agreement may be made
  (s 318(2)(c)). They are **not deposited**, so both are asked as facts (the percentage as a number; whether the
  proceedings are prescribed as a choice). The cases take 25% as the input; that figure is not checked against the
  regulations.
- The Act fixes the only other numbers used: 5 clear business days (s 318(3)(e)) and 28 days (s 352(2)(a)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (a notice the day after the cooling-off period ended asserted to bar the uplift fee) was
run once in a scratch copy and showed as "assertion failed" (129 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lpcnt-dates.l4` | 0 | 0 | 0 | 0 |
| `lpcnt-costs.l4` | 0 | 0 | 0 | 0 |
| `lpcnt-cases.l4` | 0 | 0 | 130 | 130 |

Every exported question has cases, with the edges: each kind of party under s 317(1); each way of making the agreement
and each missing element of a s 317(4) offer; contracting out with and without a sophisticated client; each s 318(2)
exception; each s 318(3) requirement failing alone and all together, with and without a sophisticated client; exactly
5 clear business days and 4; the cooling-off period across a public holiday, across Christmas and New Year, from a
Saturday, and of 10 days; notice on the day the agreement was made, the day before its last day, the last day, the
Saturday after and the Monday after, and before the agreement was made; the regulative rule alone on day 0, the day
before the deadline, the deadline and the day after; each s 318(6)(a) condition failing; s 308 with and without an uplift
fee and for each kind of sophisticated client; the uplift cap at exactly 25% and at 25.01%, and over the cap in a matter
not litigious; each s 319(3) route; s 320 with and without a fixed costs provision; s 322 amounts for each reason a
costs agreement is void, with fair value below, at and above the agreement's amount, and payments below, at and above
what is recoverable; each s 339 limb; each s 323 route; the 28-day review period on the day, the 27th, 28th and 29th
day, across the year end and into 29 February 2028.

**No mirror cases.** One seat.

## Seat

**The client** (`lpcnt-costs.l4`): the person who retains a law practice, or for whom one is retained, and who makes or
is asked to make a costs agreement with it -- typically an injured person or other claimant offered a "no win, no fee"
conditional costs agreement with an uplift fee. "May I make a costs agreement?", "Is it in a form the Act allows?", "May
it be conditional on winning?", "What must it contain?", "By when can I back out, and what do I pay if I do?", "Can my
lawyer take a percentage of what I recover?", "Is my agreement void, and what may be recovered from me or must be repaid
to me?", "Will the costs assessor hold me to its rates?", "Can it be set aside?", "Am I in time to seek review?". An
associated third party payer (someone who owes the law practice the client's costs) is answered where the text names
one (s 317(1)(d), s 317(6)).

The Act's Division 5 speaks mostly to the law practice ("must not enter into", "is not entitled to recover", "must
repay") and to the costs assessor ("may order", "must determine"); the encoding turns that into what it means for the
client. The law practice could have a second seat (its offences under ss 319(6), (7) and 320(3), (4)), but none was
written: every rule here is the same rule seen from the other side. The costs assessor and the reviewer get no seat:
their satisfaction is asked as a fact.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed as far as possible: the Legal Profession
  Regulations (NT) are not deposited, so the uplift cap and the prescribed proceedings are inputs.
- **The actors the text names.** Followed: the client, the law practice, the associated third party payer, the costs
  assessor, the reviewer.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether an estimate of the uplift
  fee was "not reasonably practicable" (s 319(3)); whether the costs assessor is satisfied the agreement is not fair or
  reasonable (s 323(1)) or that a s 339(1)(c) or (d) limb is made out; the fair and reasonable value of the legal
  services (s 314(c), s 323(5)); whether the agreement is "in clear plain language" (s 318(3)(c)(ii)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "conditional costs agreement"
  (s 295, fork F6), "sophisticated client" (s 295 with s 306(1)(c), (d), the list asked as one fact), "associated" and
  "non-associated third party payer" (s 296), "business day" (s 4). Asked: "litigious matter" (s 295, one fact),
  "public holiday" (a list of dates), "fixed costs provision", "criminal proceedings", the Corporations Act terms in
  s 306(1)(c).
- **One case is the text's natural unit.** Followed: one costs agreement in one matter.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

**One departure.** The two s 322 amount questions take the reason the agreement is void as a choice (`it is not void`,
`a contingency fee contrary to s 320`, `its uplift fee contravenes s 319`, `another provision of Division 5`) rather than
all 26 facts again. The client gets that reason from the s 322(1) question; the choice stands for the facts, and the
encoding builds a set of facts void for that reason internally. Where both s 320 and s 319 are contravened, the `@desc`
says to choose s 320 (it takes everything).

## Scope

**In.** Part 3.3 Division 5, whole: s 317 (making costs agreements), s 318 (conditional costs agreements), s 319 (uplift
fees), s 320 (contingency fees prohibited), s 321 (effect: noted in the s 322(1) question), s 322 (void agreements, what
may be recovered and repaid, recovery as a debt), s 323 (setting aside: who may apply, the order, the s 323(6) cap).
Around it: s 4 "business day"; s 295 (definitions used); s 296 (third party payers); s 306(1)(c), (d) (as the test for a
sophisticated client); s 308 (uplift fee disclosure); s 314 (as used by s 322(2)); s 339 (assessment of complying costs
agreements); s 343 (contracting out, as used by s 317(5)); s 352(1)(a), (2)(a) (time for review of a s 323
determination).

**Out, and why.**
- ss 294, 297 to 302 (purposes; when Part 3.3 applies, first instructions, displacement by a corresponding law): the
  encoding assumes Part 3.3 applies to the matter (the client first instructed the law practice in the Territory,
  s 297). A matter governed by another jurisdiction's corresponding law is outside it.
- ss 303 to 307, 309 to 313 (costs disclosure, other than s 308): a separate focus. Their effect on a costs agreement
  reaches the encoding only through s 311(3) (a failure to disclose lets the client apply under s 323, named in the
  s 323 question), s 323(2)(c) and s 339(1)(c) (the assessor's satisfaction, an input).
- ss 315, 316 (security, interest): not about costs agreements beyond s 316(2), whose rate cap is in the regulations.
- ss 319(6), (7), 320(3), (4) (offences, 500 penalty units): the law practice's liability, not the client's question;
  no second seat was written.
- Divisions 6 to 10 (billing, mediation, costs assessment other than s 339 and the s 352 time limit, costs assessors):
  the assessment procedure, the 12-month time limit for a costs assessment application (s 332(5)) and the review
  procedure are a separate focus. s 323(2), (3), (7) to (10) (the matters the assessor may consider, adjournment,
  costs of the application, reasons) are the assessor's, reached only as the "satisfied" input.
- The rest of the Act (admission, practising certificates, trust money, complaints and discipline, the fidelity fund,
  incorporated practices): not the focus.
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 317(3), (4) "The offer must clearly specify" -- `s 317 -- contraventions`, `s 317(2) to (4) -- is my costs
  agreement in a form the Act allows` -- an accepted written offer that does not clearly specify the three things
  contravenes s 317(4), so the agreement is void (s 322(1)) -- the agreement stands anyway, being "evidenced in writing"
  by the offer document (s 317(2)).
- **F2** s 318(2) "may relate to any matter, except" -- `s 318 -- contraventions` -- a conditional costs agreement in an
  excepted matter contravenes s 318 and is void -- the exception only withholds the permission, leaving an ordinary
  (unconditional) agreement or the general law.
- **F3** s 318(3)(c)(i) "in writing" -- `s 318(3)(c)(i) -- in writing` -- a written agreement or an accepted written offer
  is in writing; an oral agreement merely evidenced in writing is not -- "evidenced in writing" (s 317(2)) suffices.
- **F4** s 318(3)(e) "a cooling-off period of not less than 5 clear business days" -- `the business day ... after ...`,
  `s 318(3)(e) -- the last day of my cooling-off period` -- the period runs from the day the agreement was made, that day
  not counted, and ends at the end of the n-th business day after it; the period is the number the agreement gives --
  the period runs from signing or from the client's receipt of a copy; or the client always has at least 5 days whatever
  the agreement says.
- **F5** s 317(1) "may be made: ... " (a list not closed with "only") -- `s 317(1) -- may I make a costs agreement with
  this law practice` -- NOTHING for a non-associated third party payer or anyone else (NOTHING-kind) -- JUST FALSE.
- **F6** s 295 "conditional costs agreement" -- `s 295 -- a conditional costs agreement` -- an agreement with an uplift
  fee is conditional (the uplift is payable only on success), even if the client does not call it "no win, no fee" -- an
  uplift fee in an otherwise unconditional agreement is outside s 318 (and then outside s 319(1), so void anyway).
- **F7** s 322(3), (4) -- `s 322 -- the most the law practice may recover` -- with a s 319 contravention, the cap is the
  agreement's costs without the uplift fee; otherwise the agreement's costs with it -- the s 322(3) cap includes the
  uplift fee in every case, s 322(4) only stopping its recovery "as uplift".
- **F8** s 339(1) "if ... unless the assessor is satisfied" -- `s 339 -- must the costs assessor hold to my agreement's
  amounts or rates` -- FALSE once an "unless" limb is met -- NOTHING (the text then says no more than that s 339 does not
  bind; s 341 governs).
- **F9** s 318(6)(a) "may recover only" -- `s 318(6)(a) -- may the law practice recover its costs for this work` --
  FALSE where a condition fails ("only"); NOTHING where there was no termination within the period -- JUST FALSE for the
  latter too.
- **F10** s 322(2) "recoverable as set out in section 314(b) or (c)" -- `s 322 -- the most the law practice may recover`
  -- the fair and reasonable value (s 314(c)), an input -- s 314(a) (a fixed costs provision) where one applies; s 314(b)
  (a costs agreement under a corresponding law) is taken never to be met by the void agreement itself.
- **F11** s 319(1) "additional legal costs (excluding disbursements)" -- `s 319 -- contraventions` -- an uplift fee that
  includes disbursements contravenes s 319 -- it is only an uplift fee to the extent it excludes them, and the rest is
  an ordinary conditional cost.
- **F12** s 318(3)(e), (6)(b) -- `the cooling-off period` -- written notice on the day the agreement is made (day 0) is
  within the period -- the period starts only the next day, and earlier notice does not count.
- **F13** s 323(1) "may order ... if satisfied" -- `s 323 -- can my costs agreement be set aside` -- no satisfaction:
  the text's no; satisfaction: "may" (the order stays a discretion) -- NOTHING where not satisfied.
- **F14** s 323(1) with s 317(6) and (11) -- the same -- a client is anyone to or for whom legal services are or were
  provided; an associated third party payer only for an agreement it made without the client -- an associated third
  party payer for any agreement that binds it.

Sites decided without a fork line: s 317(2) "must be written or evidenced in writing", s 317(5) "cannot", s 320(1)
"must not", s 308(2) "is not required" and s 322(1) "is void" are the text's own words, answered as its yes or no;
s 352(2)(a) "within 28 days" is a period the text fixes (ruling (a) of 2026-11-05).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries three `NOTHING-kind` answers: s 317(1) for a party the list does not name (F5), s 318(6)(a) where
the agreement was not ended within the cooling-off period (F9), and s 319(4) where the matter is not litigious (no cap
from that subsection). The s 322 amount questions answer NOTHING where the agreement is not void (s 322 does not
apply). The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **No time limit to apply to set a costs agreement aside.** s 323 gives the client an application to the costs
   assessor but fixes no period, and s 332(5)'s 12 months is written for "an application ... for a costs assessment under
   this section" (s 332), not for s 323. Yet s 303(1)(j) requires the law practice to disclose "any time limits that apply"
   to the setting aside of a costs agreement. The only time limit in the set-aside route is the 28 days to seek review of
   the assessor's determination (s 352(2)(a)). Asserted (the review cases); the absence is not encoded as an answer.
2. **"the premium" in s 319(4) is undefined.** Part 3.3 defines "uplift fee" (s 295) and s 319 uses it everywhere else;
   s 319(4) caps "the premium". Read as the uplift fee. A drafting slip, probably carried over from a model provision.
3. **s 323(2)(g) is garbled.** It reads "whether and how billing under the agreement addresses changed circumstances
   affecting the extent and nature of legal services provided under the agreement the time at which the agreement was
   made" -- words such as "since" appear to be missing before "the time". Not encoded (the s 323(2) matters are the
   assessor's); noted as a possible drafting or reprint error.
4. **s 322(2) skips s 314(a).** A void agreement's costs are recoverable "as set out in section 314(b) or (c)", leaving out
   the fixed costs provision of s 314(a), which s 314 puts first. Read as fair and reasonable value (fork F10); whether a
   fixed costs provision still governs is open.
5. **The cooling-off period has no start.** s 318(3)(e) requires "a cooling-off period of not less than 5 clear business
   days" but does not say from when (fork F4). Asserted on the reading taken (from the day the agreement was made, that
   day excluded).
6. **A contingency fee is not a conditional costs agreement "to the extent" s 320(1) applies** (s 295). An agreement can
   therefore be part conditional and part contingency; the encoding lists the s 318 and s 320 contraventions side by side
   and treats any one as voiding the whole agreement under s 322(1). Asserted (the Family Law and contingency case).
7. **Conversion artefacts in s 318(6)(a).** The deposited text reads "the legal service s would b e performed during that
   period ;", stray spaces from the Word reprint; the meaning is clear and the deposited file was not altered.
8. **The uplift cap depends on regulations that are not deposited.** s 319(4) leaves the percentage to the regulations,
   and s 318(2)(c) leaves further excepted proceedings to them. Every uplift and excepted-matter answer depends on an
   input the encoding cannot check.

## Before this is worth relying on

- The Legal Profession Regulations (NT), for the s 319(4) percentage and any s 318(2)(c) proceedings (finding 8), and the
  Interpretation Act 1978 (NT) for counting "within 28 days after" and "clear" days.
- A lawyer's view on forks F1, F2, F4, F6, F7 and F10, and on findings 1, 3 and 4.
- The disclosure provisions (ss 303 to 313) and costs assessment (Division 8) as their own encodings, so that s 311 and
  s 339(1)(c) can be worked out from facts rather than asked.
- An independent test pass and a human gate.
