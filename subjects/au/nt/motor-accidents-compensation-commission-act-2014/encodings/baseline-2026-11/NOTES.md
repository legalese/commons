# Motor Accidents (Compensation) Commission Act 2014 (NT) -- baseline encoding, a person with a claim on the Commission

UNOFFICIAL. Copyright in Northern Territory legislation is owned by the Northern Territory. This encoding quotes the Act
under the NT copyright policy of 8 October 1996 and the licence ruling of 24 October 2026 (`SOURCE-LICENSE.md`); it is
not an official version of the Act.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The one date (the commencement) is in a small
module (`ntmaccc-dates.l4`, built-in date functions only, no daydate), the rules and the 10 exported questions in
`ntmaccc-claims.l4`, and the worked cases in `ntmaccc-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act constitutes the body that runs the Northern Territory's
no-fault motor accident scheme and keeps its Fund; the claimant's entitlements themselves are in the Motor Accidents
(Compensation) Act 1979 (`subjects/au/nt/motor-accidents-compensation-act-1979/`, encoded separately). Most of this Act
is machinery (finding 1). What a claimant meets here is: who may act on the Commission's behalf (ss 5, 9, 11), whom
they can hold liable (s 5(2)(c), s 15), whether the Territory stands behind what is owed (s 27), what the Fund may pay
for (ss 16, 17), the reimbursement of public hospital costs for MAC claimants (s 18), the confidentiality of their
information (s 28), documents under seal (s 12(3)), and, for those who dealt with the Territory Insurance Office, the
carrying over of earlier steps (s 5(1), s 43) and who deals with an old policy or deposit (ss 30, 33, 34). The one rule
laid on others for the claimant's protection, the s 28 prohibition on disclosure, is a regulative rule (`SHANT`) run by
EVALTRACE inside an exported question.

## Edition

- **Act:** Motor Accidents (Compensation) Commission Act 2014 (NT), Act No. 42 of 2014, assented 28 November 2014,
  commenced 00:01 on 1 January 2015. The deposited text is reprint REPM059, as in force at 1 July 2021 (the last
  amendment recorded being the Health Service Act 2021), retrieved from the Northern Territory Legislation website on
  6 November 2026: `../../registers/source-bundle/Motor-Accidents-Compensation-Commission-Act-2014-NT-current-reprint-REPM059.txt`.
  The register showed the Act in force, reprint REPM059 current, on that day.
- **Numbers set elsewhere:** the value of a penalty unit (Penalty Units Act 2009 (NT), not deposited) is asked. No
  regulations under s 29 are recorded in the reprint, and none sets a number the claimant questions need.
- **Not deposited:** the Territory Insurance Office (Sale) Act 2014 (the sale, the s 9 contract, the sale dates), the
  Government Owned Corporations Act 2001 (s 26), the Criminal Code (Part IIAA, s 43BE), the Health Service Act 2021
  (NT Regional Health Services), the Penalty Units Act 2009. Each is asked as a fact where a question needs it.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (the s 28 rule asked to be kept by a disclosure outside s 28(3)) was run once in a scratch
copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ntmaccc-dates.l4` | 0 | 0 | 0 | 0 |
| `ntmaccc-claims.l4` | 0 | 0 | 0 | 0 |
| `ntmaccc-cases.l4` | 0 | 0 | 88 | 88 |

Every exported question has cases, with the edges: each kind of handler, an approved and an unapproved business name,
the s 9(5) sale contract with and without the other approvals, each of the three s 9(1)(d), (2), (3) conditions failing
in turn, a sub-delegate with and without permission and under a defective delegation; each of the three defendants, s
15(1) in and out of good faith, s 15(2) both ways (finding 2); each kind of liability for s 27; every paragraph of s
17(2) and a purpose outside it; each limb of the s 18(3) definitions failing; each element and each exception of s 28,
an exception and a justification together, the regulative rule alone on each combination; the fine at three penalty
unit values; s 12(3) all four ways; s 43 on 31 December 2014 (the last day before commencement), on 1 January 2015 and
after, with and without ongoing effect; ss 30 and 33 sold and not sold.

**No mirror cases.** One seat.

## Seat

**A person with a claim on the Commission** (`ntmaccc-claims.l4`): usually the person injured in a motor accident in
the Territory, or a dependant after a death, claiming under the MAC scheme; also a former Territory Insurance Office
customer whose policy or deposit stayed with the Commission. "Is the company handling my claim acting for the
Commission?", "Can I hold the Commission, the Commissioner or the Territory liable?", "Does the Territory guarantee what
I am owed?", "Can my benefits be paid out of the Fund?", "Is my public hospital treatment reimbursed from the Fund?",
"Was it an offence to disclose information about me?", "What is the most they can be fined?", "Is a sealed document
taken as the Commission's?", "Does what I did with TIO still count?", "Who deals with my old TIO policy or deposit?".

The Act speaks almost entirely to the Commission, the Minister and the Treasurer. They get no seat: what they approve,
determine or are satisfied of is asked as a fact. No second seat was written; the only other party the text puts a
duty on that is not an official is a person who obtains information in administering the Act (s 28), whose questions
are the same ones from the other side.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument is deposited that sets a number
  a claimant meets; the penalty unit value is asked.
- **The actors the text names.** Followed: the Commission, the Commissioner and Associate Commissioners, the Minister,
  the Treasurer, the Chief Executive Officer, a public sector employee, a statutory corporation, a non-government
  delegate, the Territory, the Central Holding Authority, NT Regional Health Services, TIO.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: the Minister's approvals (s 9, s
  11), good faith (s 15(1)), evidence to the contrary (s 12(3)), "of ongoing effect" (s 43), a disclosure justified or
  excused by law (Criminal Code s 43BE), what was included in the sale.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "MAC claimant" and "public health
  services" (s 18(3)), "non-government delegate" (s 9(1)(d)), "MAC business" (s 3, in the answer lists), "residual
  insurance business" and "residual deposit" (in the answers). Asked: entitlement under s 18 of the MAC Act 1979,
  NT Regional Health Services, a contract under s 9 of the TIO (Sale) Act 2014, what the sale included.
- **One case is the text's natural unit.** Followed: one claim (one handler, one act, one disclosure, one document, one
  TIO matter).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 3 (MAC business, MAC scheme, Fund), s 5 (continuation of TIO; may sue and be sued; constitution), s 7(a) and
s 8 (in the answers), s 9 (delegation, including s 9(4)(a) and s 9(5)), s 11, s 12(3), s 15, s 16(2), (3) (in the
answers), s 17(2), s 18, s 27, s 28, s 30, s 31 (definitions, in the answers), s 33, s 34 (in the answers), s 43.

**Out, and why.**
- s 1, s 2, s 29: short title, commencement, regulation-making.
- s 4 (Part IIAA of the Criminal Code applies to offences): mentioned in no answer beyond s 28(2); the Criminal Code is
  not deposited.
- s 6, s 10, s 12(1), (2), s 13, s 14: appointment, ministerial direction, the seal's custody, proceedings, staff. s 10
  means the Minister may direct the Commission, which the MAC Act 1979 s 32 confirms; a claimant can state no fact that
  changes an answer, so no question was written (finding 8).
- s 7(b)-(d), s 16(1), s 17(1), ss 19-25: the Fund's income, the prudential fee, surplus, records, reports, audit,
  information to the Minister, Treasurer's determinations: the Commission's own management.
- s 26: applies ss 52 and 53 (other than s 52(1)(d)) of the Government Owned Corporations Act 2001 (assumptions a person
  dealing with the Commission may make); that Act is not deposited, so the assumptions cannot be stated. A candidate
  for a later layer.
- s 9(4)(b) (a delegate contracting as the Commission's agent): folded into "acting for the Commission"; a sub-delegate's
  own sub-delegation (barred by s 9(4)(a)'s "other than this power") is not offered as a choice.
- s 32, s 36-42: the banking business before the sale, reports, determinations, the Corporations Act exclusion, the
  references in other Acts (s 39), first annual report: spent or not reaching a claimant. s 35 expired (endnote 4).
- No requirement ledger exists for the Northern Territory, and none was raised: no scenario life has reached this Act.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 9(1)(d) "with the approval of the Minister", s 9(2) "must be made by written contract" -- `s 5, s 9, s 11 -- is
  the one handling my claim acting for the Commission` -- without the approval or the written contract, the text's no
  (not a non-government delegate) -- NOTHING-kind (a bare "must" not done; the delegation may still be effective). One
  of the six site-by-site questions of 2026-11-05.
- **F2** s 11 -- the same question -- a name the Minister has not approved: NOTHING-kind (the grant's own limit) -- the
  text's no.
- **F3** s 27 "liabilities ... in relation to the MAC business" -- `s 27 -- does the Territory guarantee what the
  Commission owes me` -- the residual insurance and banking business and anything else: NOTHING-kind (a scope limit
  without "only") -- the text's no (no guarantee).
- **F4** s 15(2) "a function under this Act" -- `s 5(2)(c), s 15 -- can I hold them liable` -- the Commission's acts in
  administering the MAC scheme count, since administering it is the Commission's function under s 7(a) of this Act --
  the powers used to decide claims are conferred by the MAC Act 1979, so s 15(2) would not reach them.
- **F5** s 28(1)(a) "functions connected with the administration of this Act" -- `s 28 -- was disclosing my information
  an offence` -- asked as a fact, with the @desc saying that work on the MAC scheme or the Fund counts (s 7(a), (b)) --
  only work on this Act's own machinery counts, leaving claim information to the MAC Act (which has no secrecy
  provision of its own in the deposited text).
- **F6** the note to s 28(3) (Criminal Code s 43BE) -- the same question -- answered conditionally ("not criminally
  responsible if ... justified or excused"), after the s 28(3) exceptions -- leaving the note out as not operative.
- **F7** s 12(3) "in the absence of evidence to the contrary" -- `s 12(3) -- is the sealed document taken as the
  Commission's` -- with such evidence, NOTHING-kind (the presumption gives way; execution is a question of fact) -- the
  text's no. One of the six site-by-site questions ("unless" once met).
- **F8** s 43(1) "that is of ongoing effect" -- `s 5(1), s 43 -- does what was done with TIO still count` -- not of
  ongoing effect: NOTHING-kind -- the text's no.
- **F9** commencement at 00:01 on 1 January 2015 -- the same question -- days are the unit, so anything on 1 January
  2015 is after commencement -- separating the first minute of that day.
- **F10** s 9(1)(b), (c) -- `s 5, s 9, s 11 -- is the one handling my claim acting for the Commission` -- a public servant
  or statutory corporation without a delegation: NOTHING-kind -- the text's no.
- **F11** s 5(3)(a) -- the same question -- the Commissioner or an Associate Commissioner is "yes" without asking about
  a delegation, since they constitute the Commission -- one member acting alone needs a delegation under s 9(1)(a)
  where there are two or more (s 13).
- **F12** s 18 -- `s 18 -- is my public treatment reimbursed from the Fund` -- whether the claimant is charged:
  NOTHING-kind ("this Act does not say") -- reading s 18 as implying public treatment is not charged to the claimant.
- **F13** ss 30, 33 -- `s 30, s 33 -- who deals with my old TIO matter` -- a policy or deposit included in the sale:
  NOTHING-kind (the TIO (Sale) Act governs) -- the text's no.

Sites decided without a fork line: s 9(3) is an "unless" (the text's no); s 9(4)(a) and s 28(1) are "if" conditions;
s 17(2) is a list closed with "only"; s 15(1) and (2) are flat negatives ("is not ... liable"); s 18(3)'s definitions
are "means" definitions; s 43's "before the commencement" is a period the text fixes (ruling (a) of 2026-11-05).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding answers with a choice from a list rather than a MAYBE BOOLEAN: the answers marked "NOTHING-kind" are the
NOTHING answers, and the answers marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.


The s 28 prohibition is the regulative rule (`SHANT` disclose, with an excepted disclosure not matching the action,
`LEST BREACH`), run by EVALTRACE inside the question; outside s 28(1)(a) and on an s 28(3) exception the answer is the
text's no (its "if" and "does not apply if").

## What the Act turns out to say

1. **Almost all of the Act is machinery.** It continues the Territory Insurance Office as the Commission, keeps the
   Fund, and governs the Commission's finances, reports and the wind-up of TIO's old businesses. A claimant's
   entitlements, time limits and reviews are all in the Motor Accidents (Compensation) Act 1979; this Act gives a
   claimant no right to a benefit of its own. The encoding is correspondingly small (10 questions).
2. **s 15(2) protects the Commissioner without a good-faith condition.** s 15(1) protects the Commissioner or an
   Associate Commissioner for their own acts "in good faith"; s 15(2) adds that "the person" is not liable for an act of
   the Commission, with no such words. A bad-faith act of the Commission therefore leaves the Commissioner protected
   under s 15(2) though the same act done by the Commissioner personally would not be under s 15(1). Encoded as written.
   Asserted.
3. **s 18(2) says "the fee".** s 18(1) has the Minister determine "the amount (if any)" to reimburse the Territory;
   s 18(2) then has the Commission pay "the fee" -- a word that belongs to s 19 (the prudential supervision fee), from
   which s 18(2) appears to have been copied. Read as the amount determined under s 18(1).
4. **s 17(2)(a) misnames the MAC Act.** It speaks of benefits under the "Motor Accident (Compensation) Act 1979"; the
   Act's title, and this Act's own s 3, has "Motor Accidents". Read as that Act. Asserted (s 17(2)(a) gives "yes").
5. **s 31 "full banking business", paragraph (a), says "the TIO insurance business".** The Division is about the
   banking business, and paragraph (b) and the other definitions speak of banking; "insurance" looks like an error for
   "banking". Paragraph (b) also ends with a stray ")". No question turns on it.
6. **s 28 sets no period.** The prohibition runs for as long as the person holds the information. The regulative rule
   needs a window to end its trace; it is given one of 1 time unit, around the one disclosure asked about, as a
   modelling device. It says nothing about when the duty ends.
7. **"MAC claimant" in s 18 is narrower than "claimant".** It means a person entitled to compensation under s 18 of the
   MAC Act 1979 (medical and rehabilitation expenses) only. In the deposited text the definition of "NT Regional Health
   Services" (inserted in 2021) sits unindented between the two other definitions; a conversion artefact, not a
   change of meaning.
8. **The Minister may direct the Commission (s 10(1)), including in deciding claims.** The MAC Act 1979 s 32 says the
   same from the other side ("not subject to the direction of anyone other than the Minister"). Directions must be
   reported in the annual report (s 10(2)), but nothing requires a claimant to be told. No question was written.
9. **s 15 does not protect a delegate.** The protection is for the Commissioner and Associate Commissioners only; a
   non-government delegate handling claims under a delegation contract (s 9(1)(d)) gets none from this Act. The
   encoding does not ask about a delegate's liability (the Act is silent).
10. **The s 27 guarantee reaches only the MAC business.** TIO's residual insurance and banking business are not
   covered by it; for the banking business, s 34 makes the moneys the Territory's property, which is not a guarantee
   of a deposit. Asserted (fork F3).

## Before this is worth relying on

- The Territory Insurance Office (Sale) Act 2014 (the sale contract under its s 9, what each sale included and the sale
  dates), so that ss 9(5), 30, 31 and 33 can be worked out rather than asked.
- The Government Owned Corporations Act 2001 ss 52 and 53, to encode s 26 (what a person dealing with the Commission may
  assume).
- The Penalty Units Act 2009, for the value of a penalty unit on a given day.
- A check of findings 2 to 5 against an authorised print, a lawyer's view on forks F1, F4, F5, F7 and F11, an
  independent test pass and a human gate.
