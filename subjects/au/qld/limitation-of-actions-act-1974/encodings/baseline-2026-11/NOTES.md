# Limitation of Actions Act 1974 (Qld) -- baseline encoding, the claimant

UNOFFICIAL. Based on content from the Queensland Legislation website at 6 November 2026; (c) The State of Queensland,
licensed under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`qla-dates.l4`,
built-in date functions only, no daydate), the rules in `qla-rules.l4`, and the claimant's questions in `qla-seat.l4`,
which imports the rules and restates none. The cases are in `qla-cases.l4`. The shape follows the Limitation Act 1974
(Tas) and Limitation Act 1981 (NT) baselines in `subjects/au/`.

## Edition

- **Act:** Limitation of Actions Act 1974 (Qld), Act No. 75 of 1974, the version in force from 28 April 2026 (current on
  6 November 2026), as deposited at `../../registers/source-bundle/act-1974-075.txt` (text sha256 6775c366...7d116),
  converted from the Queensland Legislation HTML view, retrieved 6 November 2026. The conversion removed the
  amendment-history notes, so the commencement days of the amending Acts the transitional sections name (2010, 2016,
  2019, 2021, 2023) are not in the deposit; where a rule turns on one, the claimant is asked whether the event came
  after it.
- **Numbers set elsewhere:** none. The Act fixes its own periods and has no regulations.
- **Borrowed terms asked as facts:** when a cause of action "arose" or "accrued" (the general law); "unsound mind";
  "infant" and "child" (read as under 18: F2); "dust-related condition" (Civil Liability Act 2003, schedule 2);
  "sexual abuse", "serious physical abuse" (undefined); "concerns notice" (Defamation Act 2005, s 12A); "associate" and
  "materially different" (s 10AB, a court's judgment); "liquidated pecuniary claim"; "future interest"; whether another
  enactment fixes a period (s 7); whether a tax would have been an overpayment anyway (s 10A(2)).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two
deliberately wrong assertions were run once in a scratch file (deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `qla-dates.l4` | 0 | 0 | 0 | 0 |
| `qla-rules.l4` | 0 | 0 | 0 | 0 |
| `qla-seat.l4` | 0 | 0 | 0 | 0 |
| `qla-cases.l4` | 0 | 0 | 126 | 126 |

Every expected value was worked by hand from the text, with the edges: every exported question at least once and most
several times; the last day and the day after (10 / 11 March 2023 for personal injury, 1 / 2 July 2025 for contract,
1 / 2 March 2025 for defamation, 30 June / 1 July 2026 for tax); periods from 29 February; injury the day before, on and
after the 18th birthday; the s 10AA concerns notice on the last day, at the section's own example (6 days left, 50 more),
at the first day of the 56-day window and the day before it, and the day after expiry; a s 32A order inside and beyond the
3-year cap; the s 31 "last year" on its first day and the day before; a debt acknowledged after it was barred, in signed
writing, orally, by payment to the creditor and to someone else.

## Seat

**The claimant** (`qla-seat.l4`): the individual to whom a right of action accrues and who brings or proposes to bring
the action -- the injured person, the family member or personal representative suing for a death or for the estate, the
survivor of child abuse, the person with a dust-related condition, the person defamed, a party to a contract or deed, a
creditor, a beneficiary of a trust or an estate, a person who paid a tax under an invalid law. "By when must I start my
action?", "Can I still start it on this day?", "Am I under a disability?", "Is there no time limit for my claim?", "Can
the court give me more time?", "Did their acknowledgement or payment restart my time?". Two questions (s 40 contribution,
s 42 counterclaim) are asked by the same individual when answering a claim. No seat for the court, the person sued, an
insurer or the Crown: the court's judgments and orders are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers; none is borrowed.
- **The actors the text names.** Followed: the plaintiff, the defendant, the person liable or accountable, the agent,
  the trustee and beneficiary, the personal representative, the first publisher and associate, the court.
- **Judgments answered conditionally.** Followed: "decisive character" and "means of knowledge" (ss 30-32), "reasonable
  diligence" (s 38), "just and reasonable" (ss 32A, 48), "materially different" (s 10AB), "unsound mind" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: disability (s 5(2), (3)), "abuse" (s 11A(6)),
  "previously settled right of action" (s 48(6)), the accrual of contribution (s 40(2)) and of a later publication
  (s 10AB) are worked out from facts.
- **One case.** One right of action, of one person, against one person liable.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5(1) ("personal injury", "damage"), (2), (3), (7)(d)-(f) (accrual for accounts, judgments, interest); s 7;
s 10(1)-(4), (6) (as "another kind of claim"); ss 10AA, 10AB, 10A, 11, 11A; ss 27(1), (2), (2A), 28; s 29(1), (2)(a),
(c), (3)(a); ss 30, 31, 32, 32A, 33 (in the descriptions); s 35(3), (4) (in the description); s 36; s 38(1); s 40; s 41(3)
(in the description of the day an action starts); s 42; ss 47, 48, 49, 50, 51.

**Regulative rule:** one. The time bar ("shall not be brought after the expiration of", "must not be brought after") as
what the plaintiff must do to keep the action: `PARTY the plaintiff MUST commence the action WITHIN` the days to the last
day, `LEST BREACH ... BECAUSE` the period has expired. Run by EVALTRACE inside the three "Can I still start ... on this
day" questions, which take only plain dates and facts.

**Out, and why:**
- ss 1, 2, 3, 34, 39, 43, 43A, 44, 45, 46 and Parts 6-7: short title, commencement, practice, costs (a matter for the
  court), the equitable savings, characterisation (choice of law; see the Choice of Law (Limitation Periods) Act 1996
  encoding), and transitional provisions for repealed sections or long-past events (s 44 is for the repealed s 30A).
- s 6: the Crown is bound and benefits; s 6(3) concerns actions by the Crown, not the claimant; s 6(4) is land.
- s 8: actions barred or pending before 1 July 1975.
- s 10(5), (5A), s 29(3)(b): penalties and forfeitures (brought by informers or the Crown, not claimants).
- s 12 (successive conversions of goods), ss 13-24, 25, 26, s 29(2)(b), s 35(1), (2), s 37: land, rent, mortgages and the
  effect of acknowledgements on third persons. Land and mortgage law, not claims work; one case is one person liable.
- s 27(3): a beneficiary's share of another's judgment; s 38(2): protects innocent purchasers, not the claimant's time.
- s 41(1), (2), (4)-(6): arbitration machinery; an arbitration is treated as an action, so the same questions apply.
- s 41A: limits what the electronic publication date is used for.
- Defamation published before the 2021 amendment, and deeds made before the 2023 amendment: the earlier wording is not
  deposited; the questions answer "not answered by this encoding". s 38 is not asked in the defamation questions.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "N years from the date" (ss 10, 11, 27, 28, 29), "1 year running from" (s 10AA), "within 1 year after the day"
  (s 10A), "1 year after that date" (ss 31, 32), "running from" (ss 32A, 40) -- `the anniversary` -- the day itself is
  excluded, so the last day is the anniversary; from 29 February into a year without one, 28 February -- the Acts
  Interpretation Act 1954 (Qld) s 38 (not deposited) governs the reckoning; 1 March is the other reading for 29 February.
- **F2** "infant" (s 5(2)), "child" (s 11A) -- `s 29 -- the disability of`, the s 11A question -- under 18, ceasing on the
  18th birthday -- the age of majority is set by another Act, not deposited.
- **F3** s 38(1) "shall not begin to run until" -- `s 38 -- the day the period runs from` -- the period runs from the later
  of the accrual and the discovery, counted like any other period -- a reading that counts it from the day after.
- **F4** s 29(1) for a person who was both an infant and of unsound mind at accrual -- `s 29 -- the disability of` -- the
  disability lasts until both have ended -- the reading that only the disability existing at accrual is followed.
- **F5** s 47(2)(a), (b) "judgment has been given", "settled or discontinued" (without (c)'s "before the commencement")
  -- `s 11(2) -- my dust-related condition claim has no limitation period` -- the exceptions reach only rights that
  accrued before s 47 commenced, since s 47 only extends s 11(2) to those -- the literal reading reaching any judgment or
  settlement.
- **F6** s 11A for abuse of an adult or a claim not for personal injury damages -- `s 11A -- my action may be brought at
  any time` -- NOTHING (a grant limited in its own wording; s 11 governs) -- JUST FALSE.
- **F7** s 31(2)(a), s 32(2)(a) "a date after the commencement of the year last preceding the expiration" -- `ss 31, 32 --
  the court may extend my period` -- the year begins the day after the day one year before the last day, so the fact day
  must be after that day one year before -- a reading that includes that day.
- **F8** s 7 ("Subject to sections 11(2) and 43A") with s 11A(1)(b) ("not subject to a limitation period under an Act") --
  `the time limit for the injury claim` -- s 11A applies even where another Act fixes a period -- the reading that s 7,
  which does not name s 11A, displaces it (finding 1).
- **F9** s 31(2) "the period of limitation for the action" -- `the time limit for the injury claim` -- the period as s 29
  leaves it, and an order never shortens it -- the s 11(1) period alone.
- **F10** s 10AA(2) "within the period of 56 days before the limitation period expires" -- `s 10AA -- the last day after
  any concerns notice` -- a notice from 55 days before the last day to the last day -- 56 days before; the extension is
  nil there either way (finding 2).
- **F11** s 40 before liability is fixed by a judgment, award or agreement -- `s 40 -- the time limit for my contribution
  claim` -- "not answered by this encoding" (accrual left to the general law) -- the s 40(1)(b) day alone.
- **F12** s 29(1) "on the date on which a right of action accrued" -- `s 29 -- the disability of` -- the actual accrual day,
  not a day deemed by s 35(3) or s 27(2A) -- the deemed day.
- **F13** s 36(1) "shall be in writing and signed" with an unwritten acknowledgement -- `ss 35(3), 36 -- the acknowledgement
  or payment restarts my time` -- JUST FALSE (it has no effect) -- NOTHING.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "while" of s 5(2), (3), the "means" definition of abuse (s 11A(6)), "does not include" (s 11(3)), "does
not apply" (s 47(2)), "shall be in writing and signed" (s 36(1)), the "where" of ss 31(2), 35(3), the "if" of s 48(5A)
and "shall not be brought after" (the time bar) give `JUST FALSE`. `NOTHING` is answered for s 11(2) and s 11A where the
facts fall outside the grant and for s 35(3) where the claim is not liquidated (*limited by its own wording*), for s 48
where a claim was settled within time (*limited by its own wording*), where another Act decides (s 7), for an overpayment
(s 10A(2)), an earlier deed (s 51), an earlier defamation (s 50), unfixed contribution (s 40), and a kind of claim outside
the encoding (*points outside the text*).

## What the Act turns out to say

1. **s 7 does not name s 11A.** s 7 makes the Act give way to another enactment's period "Subject to sections 11(2) and
   43A". s 11(2) (dust) and s 11A (child abuse) both say the claim "is not subject to a limitation period under an Act or
   law or rule of law", but only s 11(2) is saved. Read as s 11A prevailing, by its own words (F8). Asserted.
2. **The concerns-notice arithmetic always ends 56 days after the notice.** s 10AA(3) adds "56 days minus any days
   remaining after the notice day"; with the section's own example (7 days before expiry leaves 6 days, so 50 more), the
   period ends on the notice day plus 56. The window's edge (55 or 56 days before) therefore makes no difference.
   Asserted (26 April 2025 for a notice on the last day; 20 April 2025 for the example).
3. **A defamed minor gets more time than a defamed adult by years.** s 29(2)(c) shortens the disability extension to 3
   years only for personal injury and death; s 29(1) applies to "a right of action ... for which a period of limitation
   is prescribed by this Act", which includes s 10AA. A person defamed at 13 may sue until their 24th birthday, against an
   adult's 1 year. Asserted (born 1 June 2010, published 1 March 2024: 1 June 2034).
4. **An acknowledgement or payment revives even a barred debt.** s 35(3) sets the accrual "on and not before the date of
   the acknowledgment or the last payment" with no requirement that it come before the period expires, and s 37(5A), (6A)
   speak of acknowledgements and payments "made after the expiration". Encoded: it restarts time against its maker even
   after expiry. Asserted (a debt barred after 1 July 2021 revived to 10 October 2028).
5. **s 47(2) is uneven.** Paragraph (c) is limited to a refusal "before the commencement of this section"; (a) and (b)
   (judgment given, settled or discontinued) are not. Read as reaching only rights that accrued before s 47 commenced
   (F5). Asserted both ways.
6. **s 48 does not reach a claim settled within time.** A "previously settled right of action" is one settled "after a
   limitation period applying to the right of action had expired"; a survivor who settled within time is outside s 48,
   though the same claim unsettled would now have no limitation period (s 11A). Asserted (NOTHING).
7. **s 32(2)(a) "the deceased person or the applicant".** It is unclear whether the fact must have been outside the
   means of knowledge of both, or of either. Left to the court as an input; noted in the `@desc`.
8. **Dead text.** s 44 is a transitional provision for s 30A, which is repealed; s 5(3)(c) still speaks of an order given
   "in the name of Her Majesty". Not encoded.
9. **Three wordings for one count.** "from the date" (ss 10, 11), "running from the date" (ss 10AA, 32A, 40) and "within 1
   year after the day" (s 10A) are all read as excluding the first day (F1).

## Before this is worth relying on

- Check the text against the authorised PDF on legislation.qld.gov.au.
- Bring in the commencement days of the 2010, 2016, 2019, 2021 and 2023 amending Acts (from the history notes or the
  authorised reprint), so the claimant gives a date rather than a yes/no.
- The Acts Interpretation Act 1954 (Qld) s 38 for reckoning periods (F1) and the Law Reform Act 1995 for the age of
  majority (F2).
- Encode the land, mortgage, rent and penalty provisions if wanted.
- A lawyer's view on findings 1, 3, 5 and 6 and forks F3-F5, F7-F9, F11, F12; an independent test pass and a human gate.
