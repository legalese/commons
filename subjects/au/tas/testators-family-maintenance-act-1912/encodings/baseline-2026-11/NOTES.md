# Testator's Family Maintenance Act 1912 (Tas) -- baseline encoding, the claimant and the beneficiary

UNOFFICIAL. Based on material from the Tasmanian Legislation website at 6 November 2026; (c) State of Tasmania, licensed
under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The one date helper is in a small module
(`tfm-dates.l4`, built-in date functions only, no daydate), the rules in `tfm-rules.l4`, the claimant's questions in
`tfm-seat.l4` and the beneficiary's in `tfm-seat-beneficiary.l4`, both importing the rules and restating none. The cases
are in `tfm-cases.l4` (claimant) and `tfm-beneficiary-cases.l4` (beneficiary, with mirror cases). The shape follows the
Fatal Accidents Act 1934 (Tas) baseline in `subjects/au/tas/fatal-accidents-act-1934/encodings/baseline-2026-11/`.

## Edition

- **Act:** Testator's Family Maintenance Act 1912 (Tas), No. 7 of 1912, consolidated version published 2021-11-11 and
  current at point in time 2026-11-06, as deposited at `../../registers/source-bundle/act-1912-007.txt` (text sha256
  4523ceb7...1b33), retrieved from legislation.tas.gov.au on 6 November 2026. It includes the 2003 significant-relationship
  amendments (No. 45 of 2003), the 2012 surrogate child (No. 31 of 2012), the 2015 stepchild definition (No. 38 of 2015)
  and No. 18 of 2021 (s 8A(1A), the Tribunal).
- **Numbers set elsewhere:** none. The Act fixes its one number (three months, s 11(1)) and has no regulations.
- **Borrowed terms asked as facts:** "significant relationship" (Relationships Act 2003, not deposited); "spouse" beyond
  its inclusion, "child", adoption under the adoption law, surrogate child status (Surrogacy Act 2012); "maintenance"
  received or due; "full age or mental capacity"; "final distribution"; the Court's findings (adequate provision, the
  opinion under s 8(1), the extension, the s 3(4) order, exoneration).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `tfm-dates.l4` | 0 | 0 | 0 | 0 |
| `tfm-rules.l4` | 0 | 0 | 0 | 0 |
| `tfm-seat.l4` | 0 | 0 | 0 | 0 |
| `tfm-seat-beneficiary.l4` | 0 | 0 | 0 | 0 |
| `tfm-cases.l4` | 0 | 0 | 70 | 70 |
| `tfm-beneficiary-cases.l4` | 0 | 0 | 23 | 23 |

Every expected value was worked by hand from the text, with the edges: every exported question at least twice; every
relationship s 3A and s 2 name, a parent with and without a surviving spouse or child, a former spouse or partner with
and without maintenance; a stepchild whose step-parent died on 13 October 2015 (the commencement) and on 12 October 2015;
the last day of the three months and the day after (15 / 16 April 2026 for a grant on 15 January 2026; 28 February / 1
March 2026 for a grant on 30 November 2025; 29 February / 1 March 2024 for a grant on 30 November 2023; across the year
end, 31 January / 1 February 2026 for a grant on 31 October 2025); a summons on the day of the grant and before it; an
extension's last day and the day after; the net estate at exactly nil and $1 above; the ratable share of a payment.

## Seats

**The claimant** (`tfm-seat.l4`): the person who applies, or for whom an application is made, for provision out of the
estate of a person who has died -- the spouse or partner in a significant relationship, a child (adopted, step- and
surrogate children included), a parent where no spouse or child was left, or a former spouse or partner who was
receiving or entitled to maintenance. "Can I claim?", "Can the executor apply for me?", "By when must I take out my
summons?", "Will the Court hear me if I file on this day?", "Can I still ask for more time?", "Can the Court order
provision for me?", "Can it refuse me for my conduct?", "What estate does it look at?", "Can my provision be a house?",
"Does it continue if I remarry?", "Must I be told if someone applies to change the order?".

**The beneficiary** (`tfm-seat-beneficiary.l4`): a person who takes under the will or the intestacy and whose share
bears the provision -- the person answering the claim. "Must the summons be served on me?", "How much falls on my
share?", "Can what I have already received be disturbed?", "Can I apply to change the order?". The beneficiary may also
be the executor or administrator; the inputs ask.

No seat for the executor or administrator as such (they act for the estate), the Court or the judge: their findings are
asked as facts. The two seats keep their own names and draw on the same rules, so they cannot disagree about the law;
`tfm-beneficiary-cases.l4` has mirror cases.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own number.
- **The actors the text names.** Followed: the applicant, the persons in s 3A, the executor or administrator, the
  trustee of a class fund (s 10, out), the beneficiary, the Court or a judge.
- **Judgments answered conditionally.** Followed: "left without adequate provision for his proper maintenance and
  support", the s 8(1) opinion, the s 9(4) direction, the s 11(2) extension, the s 3(4) order, s 10A exoneration or a
  contrary order are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "stepchild" (a "means" definition) is worked out
  from the relationship and, under s 2(2), the date of death; "child" and "spouse" ("includes") are taken with their
  inclusions; "significant relationship" is asked.
- **One case.** One death, one claimant (or one beneficiary).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 2(1), 2(2) (who may apply, through the definitions), 3(1), 3(2), 3(3) (in the form question), 3(4) (in the
time question), 3(5), 3A, 4(2), 7(a), 8(1), 9(4), 9(5), 9(5A), 9(6), 10A(1), 10A(2) (exoneration), 11(1)-(4).

**Regulative rule:** one, run by EVALTRACE inside exported questions that take only plain facts.
- s 11(1): from the grant of probate or letters of administration, `PARTY the applicant MUST take out the summons WITHIN`
  the days to the corresponding day three months later `HENCE FULFILLED LEST BREACH ... BECAUSE` the Court has no
  jurisdiction unless it extends the time; run in `Can the Court hear my application if I take out the summons on this
  day` and `Can the Court order provision for me out of the estate`. A summons on the last day is in time (a step at
  exactly the WITHIN bound is FULFILLED on the stable l4, checked).

**Out, and why:**
- s 1 (short title): machinery. ss 2(3)-(5), 5, 8(3) are repealed or omitted.
- s 4(1), (3) (the summons in chambers, its title, adjournment into Court), s 6 (the Court's inquiry), s 8A (evidence
  of the deceased's reasons), s 9(1), (2) (contents and endorsement of the order): procedure addressed to the Court,
  giving the claimant no question of his or her own beyond those encoded. s 8A is a finding below.
- s 7(b) (the claimant's independent means): a matter the Court has regard to, with no rule to compute; noted in the
  `@export` text of the net estate question.
- s 8(2) (conditions on provision), s 9(3) (provision takes effect as a codicil or a modification of the Intestacy Act
  2010), s 9(7) (the estate held subject to the order), s 10 (class fund), s 10A(3) (commutation), s 10B (apportioning
  duty): effects of an order and the Court's powers in framing it, with no fact the claimant could state that changes an
  answer; s 10B refers to estate duty, which no deposited source imposes.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 11(1) "not later than three months after the date of grant" -- `the corresponding day`, `s 11(1) -- the last
  day for the summons` -- the three months end on the same day of the month three months later (or that month's last
  day if it is shorter), and a summons on that day is in time -- the period ending the day before the corresponding day
  (the Acts Interpretation Act 1931 (Tas), not deposited, governs).
- **F2** s 2(2) "the commencement of that Act" -- `s 2(2) -- the day the stepchild definition commenced` -- 13 October
  2015, from the history note "Applied:13 Oct 2015" -- another commencement date, if the 2015 Act commenced in parts.
- **F3** s 3A "may be made by or on behalf of all or any of the following persons" -- `s 3A -- I may apply for
  provision` -- a person the list does not name (a grandchild, sibling, other dependant), and a former spouse or partner
  without maintenance, get NOTHING (a list not closed with "only"; a limit in the text's own wording) -- JUST FALSE, s 3A
  read as the whole class of applicants (s 3(1) speaks of "any person by whom ... application ... may be made under this
  Act").
- **F4** s 3(2) "In addition to, and without prejudice to, any other powers" -- `s 3(2) -- the provision may take this
  form` -- another form (periodic payments, a charge, a transfer of other property) gets NOTHING -- JUST TRUE under s
  3(1)'s "such provision as ... thinks proper".
- **F5** s 7(a) "the net value only ... as ascertained by deducting" -- `s 7(a) -- the net value of the estate` -- never
  below nothing -- a negative net value (an insolvent estate) reported as such.
- **F6** s 9(4) "may ... direct that that provision shall operate ... notwithstanding that he or she may ... remarry" --
  `s 9(4) -- my provision continues if I remarry` -- without the direction, NOTHING (the Act is silent; the order's terms
  decide) -- JUST FALSE, reading s 9(4) as implying that a spouse's provision otherwise ends on remarriage.
- **F7** s 10A(1) "fall ratably upon the whole estate" -- `s 10A -- the part of the payment falling on my part of the
  estate` -- in proportion to the value of each part -- ratably in proportion to the benefits taken under the will or
  intestacy, or applied in a statutory order of abatement.
- **F8** s 10A(1) "unless the Court or a judge otherwise orders" (an "unless" once it is met, decided case by case) --
  same -- NOTHING: the Court's order decides -- the ratable share still answered, as a default the order departs from.
- **F9** ss 11(4), 9(5A) -- `ss 11(4), 9(5A) -- the distribution to me may be disturbed` -- for a claim taken out in time,
  and for a distribution after the application, NOTHING (the text is silent) -- JUST TRUE, reading the two protections
  as implying that other distributions may be followed.
- **F10** s 11(4) "shall be made before the final distribution" -- `s 11(2)-(4) -- I may apply for an extension of time`
  -- JUST FALSE after the final distribution (a period the text fixes in its own words) -- NOTHING (a bare "shall" not
  done, the Court's power under s 11(3) read widely).
- **F11** s 3(4) "for the purposes of section eleven, be treated as an application made by all of those persons" --
  `s 11 -- the Court has jurisdiction to hear my application` -- my summons is in time whenever another person's in-time
  application has been so ordered, whatever the day of mine -- the order protecting only the application it names, with
  a late separate summons still needing an extension.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: the "means" definition of stepchild, the "if" of s 3A(c), s 3(1) and s 8(1), the "unless" of s 11(1) ("shall
have no jurisdiction ... unless"), the period of s 11(4) ("before the final distribution"), and the flat negatives of s
9(5A) ("shall not ... disturb") and s 11(4) ("no distribution ... shall be disturbed") give `JUST FALSE`. `NOTHING` is
answered for a person s 3A does not name and a former spouse or partner without maintenance (a list not closed; a limit in
the text's own words, F3), a stepchild of a death before 13 October 2015 (points outside the sources), another form of
provision (F4), a spouse's order without a s 9(4) direction (silent, F6), s 3(5) for a person of full age and capacity, s
4(2), s 9(5) and s 9(6) for persons outside their lists (silent or limited in the text's own words), s 10A where the
Court has otherwise ordered (F8), and distributions the Act does not protect (F9).

## What the Act turns out to say

1. **A narrow class of claimants.** s 3A names the spouse (with a partner in a significant relationship at the death), the
   children (adopted, step- and surrogate children), the parents only where no spouse or child survives, and former
   spouses or partners only if they were receiving or entitled to maintenance. Grandchildren, brothers and sisters, and
   other dependants are not named. Asserted as NOTHING (F3).
2. **A parent's claim turns on whether a spouse or child was left, not on whether they claim or need anything.** A
   parent is shut out by a surviving child who is well provided for. Asserted.
3. **The stepchild definition depends on the date of death.** s 2(2) keeps the 2015 definition away from estates of
   persons who died before its commencement; the earlier definition is not in the consolidation (the history notes
   show paragraph (b) of "child" amended by No. 31 of 2012 from 1 May 2013, but not its earlier wording). Asserted at 12 and 13 October 2015 (F2).
4. **The time runs from the grant, not the death, and a summons may be taken out before any grant.** Three months is
   short, but s 11(3) lets the Court extend even after it has expired; the only bar is the final distribution (s 11(4)),
   and an extension cannot disturb what was distributed before it was sought. Asserted.
5. **"before or not later than three months after"** leaves no question that a summons before the grant is good; the
   encoding answers JUST TRUE for one taken out before any grant, with no lower bound at the death.
6. **The definition of "spouse" uses "his or her death" ambiguously.** "the person with whom a person is, or was at the
   time of his or her death, in a significant relationship" -- read here as the deceased's death, which is what s 3A(a)
   needs; asked as a fact ("partner in a significant relationship at the death").
7. **s 7's heading speaks of "widow or child"** though the text speaks of "any person who is entitled to make an
   application": the heading is a survival from 1912 and is not encoded.
8. **s 9(4) protects only the spouse.** The Court may direct that a spouse's provision survive remarriage or a new
   significant relationship; the Act says nothing of what happens without the direction, or of a child or former spouse
   (F6).
9. **s 9(5A) protects only distributions "lawfully made"; s 11(4) protects any distribution made before the extension
   application.** The two protections are worded differently. Asserted (F9).
10. **s 8A lets the Court hear the deceased's reasons "whether that evidence would otherwise be admissible ... or not"**,
    and for a statutory will made by the Tribunal or the Court under the Wills Act 2008, the records of that body: an
    evidential rule for the hearing, not encoded.
11. **The Act has no cap, no formula and no regulation.** What provision is "proper" is wholly the Court's discretion,
    guided only by s 7 and s 8A; the encoding answers whether the Court may order, never how much.

## Before this is worth relying on

- Check the text against the authorised version on legislation.tas.gov.au.
- The Acts Interpretation Act 1931 (Tas) rule for reckoning "three months after" (F1), the commencement of the Justice
  and Related Legislation (Miscellaneous Amendments) Act 2015 (F2), and the Relationships Act 2003 (Tas) for
  "significant relationship", if deposited.
- A lawyer's view on forks F3, F6, F7, F9 and F11 and findings 1, 5 and 6; an independent test pass and a human gate.
