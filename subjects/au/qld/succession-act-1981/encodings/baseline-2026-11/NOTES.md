# Succession Act 1981 (Qld) -- baseline encoding, the claimant on an estate

UNOFFICIAL. Based on content from the Queensland Legislation website at 6 November 2026; (c) The State of Queensland,
licensed under CC BY 4.0 (see SOURCE-LICENSE.md). Not the authorised version.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in a small module (`qsa-dates.l4`,
built-in date functions only, no daydate), the rules in `qsa-rules.l4`, and the claimant's questions in `qsa-seat.l4`,
which imports the rules and restates none. The cases are in `qsa-cases.l4`. The shape follows the Limitation of Actions
Act 1974 (Qld) baseline beside it in `subjects/au/qld/`.

Focus: the provisions a claimant on a deceased person's estate meets -- wills and family provision work.

## Edition

- **Act:** Succession Act 1981 (Qld), Act No. 69 of 1981, the version in force from 28 April 2026 (current on 6 November
  2026), as deposited at `../../registers/source-bundle/act-1981-069.txt` (text sha256 cfe325d8...19b11e8 per the
  `.meta.json`; a Windows checkout with CRLF line endings hashes differently), converted from the Queensland Legislation
  HTML view, retrieved 6 November 2026.
- **Numbers set elsewhere:** none. The Act fixes its own amounts and periods ($150,000 in schedule 2; 30 days; 3, 6 and 9
  months; 2 years) and has no regulation that sets them.
- **Borrowed terms asked as facts:** "de facto partner" and "lived together as a couple on a genuine domestic basis"
  (Acts Interpretation Act 1954 s 32DA); "civil partner" and termination (Civil Partnerships Act 2011); "divorce" and
  "annulment" (Family Law Act 1975 (Cth)); "dust-related condition" (Civil Liability Act 2003 schedule 2); "adopted
  child"; "donatio mortis causa"; "general power of appointment"; "properly made"; "contrary intention"; the declaration
  of paternity (Status of Children Act 1978).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; one
deliberately wrong assertion was run once in a scratch file (deleted) to confirm that a failure shows as
`DiagnosticSeverity_Error`, "assertion failed". Satisfied assertions were counted by distinct source range.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `qsa-dates.l4` | 0 | 0 | 0 | 0 |
| `qsa-rules.l4` | 0 | 0 | 0 | 0 |
| `qsa-seat.l4` | 0 | 0 | 0 | 0 |
| `qsa-cases.l4` | 0 | 0 | 231 | 231 |

Every expected value was worked by hand from the text, with the edges: every exported question at least once and most
several times; months after the 31st into a shorter month (31 August + 6 months = 28 February; 31 May + 9 months = 28
February; 30 November + 3 months = 29 February in a leap year); the last day and the day after for rectification (s 33),
family provision (s 41(8)) and the shared-home election (s 39A), with the s 39B(6) one-month extension on both sides of the
3 months; the 30-day survival rule on the 30th and 31st day (ss 5A, 33B, 35(2)); the s 44 protection on the day before
and on the 6-month and 9-month days; the intestacy shares below, at and $3 over the $150,000, with one line of issue (1/2)
and more (1/3), by representation through a child, a brother and an uncle, and bona vacantia; s 65 combined with s 33B.

## Seat

**The claimant on a deceased person's estate** (`qsa-seat.l4`): the individual with a claim on, or in, the estate -- the
surviving spouse or partner, a child or stepchild, a dependant, a relative entitled on intestacy, a beneficiary under the
will, a person who may ask to see the will, and the family member or beneficiary concerned with a claim that survives the
death (s 66), including a beneficiary sued on such a claim. "Am I the spouse?", "Is this document the will?", "Does my
gift stand?", "What is my share?", "May I buy our home?", "Can I apply for family provision, and by when?", "Could the
court order provision for me?", "Can I still sue the personal representative over a distribution?", "What can the
estate recover?", "What is the most I can be made to pay?". No seat for the court, the personal representative, the
registrar, the public trustee or the Crown: the court's judgments and orders, and what the personal representative has
done, are asked as facts. A personal-representative seat could be added later as `qsa-seat-representative.l4`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Act sets its own numbers.
- **The actors the text names.** Followed: the testator or intestate, the spouse, child, stepchild, dependant, issue,
  next of kin, beneficiary, witness, interpreter, personal representative, the court.
- **Judgments answered conditionally.** Followed: "satisfied" (ss 11, 12, 18, 41(1A)), "adequate provision" and "proper
  maintenance and support" (s 41(1)), "character or conduct" (s 41(2)(c)), "appropriate" (s 33(3)), "otherwise directs"
  (s 41(8)), "properly made" (s 44) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: spouse of a deceased person (s 5AA), the unborn
  child (s 5A), dependant (s 40), stepchild (s 40A), household chattels (s 34A), entitled person (s 33Z), next of kin
  (s 35(1A)), residuary estate shares (schedule 2, ss 36A, 37), the estate for Part 4 (ss 5B, 41(12)).
- **One case.** One estate, one claimant, one document, one gift, one distribution.
- **The Act's terms with plain glosses.** Followed, in each `@desc` ("will-maker" for testator, "personal
  representative" glossed as executor or administrator).
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 5AA; s 5A; s 5B (with s 41(12)); s 9; s 10(2)-(4), (7), (8), (10), (13); s 11; s 12; s 14(1)-(3) except (2)(c);
s 14A(1)-(3) except (2)(c); ss 15, 15A, 15B (as one question); s 33(2), (3); s 33B; s 33Z(1), (2), (4) (entitled person);
s 34(2) (half blood, in the descriptions); s 34A; s 35(1), (1A), (2); s 36(1)(c), (3) (equal division between spouses);
s 36A; s 37; s 39A(1)-(3); s 39B(1), (2), (4), (6); s 40 (child, dependant); s 40A; s 41(1), (1A), (2)(c), (8), (9), (12) (with s 41(6) in the descriptions);
s 44(1)-(4); s 65; s 66(1), (2)(a), (b), (d), (2A), (2B), (6), (9); schedule 2, parts 1 and 2.

**Regulative rule:** one. The time limits ("may only be made within", s 33(2); "no application shall be heard ...
unless ... instituted within", s 41(8); "must be made within", s 39A(3)) as what the person in the seat must do to keep
the step open: `PARTY the person in the seat MUST take the step WITHIN` the days to the last day, `LEST BREACH ...
BECAUSE` the time has run out. Run by EVALTRACE inside the three "on this day" questions, which take only plain dates and
facts.

**Out, and why:**
- ss 1-4, 6, 68-72, Part 7: title, application, jurisdiction, commission, the registrar, practice, service and
  transitional provisions (machinery). The encoding assumes a death, will, marriage and divorce after the 2006
  amendments (s 76 keeps the old ss 16-18 for earlier events; their text is not deposited).
- s 7, s 8: application of Part 2 and what property a will may dispose of; general, not a claimant's question.
- ss 13, 16, 17: how a will is revoked by the will-maker, altered or revived; turn on the physical state of the
  document and the will-maker's intention, left to the court and to s 18.
- ss 19-32: court-authorised wills for minors and persons without capacity; applications made for the will-maker, not
  by a claimant on the estate. A s 21 will answers "not answered by this encoding" in the will question.
- s 33(1), (4), (5), s 33A: the grounds and machinery of rectification and the protection of the personal
  representative (the same 6/9-month pattern as s 44, which is encoded).
- ss 33C-33S: rules for construing a will (evidence, lapse, class gifts, s 33N gifts to issue who die first); general
  construction, not a claimant's entitlement question. A gift to a beneficiary who died before the will-maker answers
  "not answered" for that reason.
- ss 33T-33YE: foreign and international wills.
- s 33Z(3): production in court.
- s 34(1) definitions are used; ss 34B, 39C, 39D: transfer value and the mechanics of acquiring the shared home (the
  descriptions mention transfer value; s 39D's bar on disposal is not asked).
- s 36(1)(a), (b), (4)-(12): agreements and court orders between spouses (a court's just and equitable division is
  not computable; only the equal division is).
- ss 38, 39: partial intestacy trusts and construction of "heir".
- s 41(2)(a), (b), (3)-(5), (7), (10), (11), s 42: the form and incidence of orders, applications on behalf of a person
  under incapacity (in the descriptions only), variation of orders.
- s 41(6): an application filed for one person is, "so far as regards the question of limitation", deemed an
  application on behalf of all who might apply. It bears on the s 41(8) time limit but turns on another person's filing;
  it is stated in the descriptions of the two s 41(8) questions (answer as of the day that application was filed), not
  computed.
- s 44(5): a saving clause (s 44(4) does not prevent a later application within any other period the Part allows); it
  changes no answer here, since the s 41(8) questions already carry the court's direction to hear a late application.
- s 43: computing duties as if the order were part of the will (Queensland levies no death duty).
- Part 5 (administration, debts, insolvent estates) and Part 5A (testamentary guardians): the seat of the personal
  representative and of guardians.
- s 66(2)(c), (3), (4), (5), (7), (8): breach of promise to marry, the deemed cause of action, the Civil Proceedings Act
  link (in the description), pre-commencement actions, contribution and equitable defences (in the description).

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** "within N months after" (ss 33(2), 39A(3), 39B(4), (6), 41(8)), "3 months have passed" (s 36(1)(c)), "N months
  after the deceased's death" (s 44(3)) -- `the day ... months after` -- the same day of the month N months on, or the
  last day of that month if shorter; the day itself excluded -- the Acts Interpretation Act 1954 (Qld) (not deposited)
  governs the reckoning; a reading ending on the 1st of the following month for a 31st.
- **F2** s 39A(3)(b) before the personal representative has given the notice -- `s 39A(3) -- an election on ... is in
  time under` -- NOTHING (the 3 months have not started; the text is silent on an earlier election) -- JUST TRUE.
- **F3** s 5A "remains alive for a period of 30 days", s 33B "dies within 30 days after the testator's death", s 35(2)
  "does not survive ... for a period of 30 days" -- `s 5A ...`, `ss 33B, 35(2) ...` -- alive throughout the 30 days after
  the day of birth or death, so a death on the 30th day after fails and one on the 31st succeeds -- the 30th day
  succeeds under s 35(2) and s 5A (finding 3).
- **F4** s 9(1) with s 18 -- `ss 9, 10, 18 -- the document is the deceased's will` -- a minor's will is not saved by s 18
  (JUST FALSE) -- s 18 can make a minor's informal document a will.
- **F5** s 15(1)(a) "a will in existence when the divorce ... happens", applied also to (b) and (c) -- `ss 15, 15A, 15B
  -- my gift survives the end of our relationship` -- a will made after the ending is untouched (JUST TRUE) -- (b), (c)
  reach any will.
- **F6** s 36A(7)(b), s 37(2) "taken by representation" -- `the share by representation of` -- the asker states how many
  shares the parent's portion divides into; a further generation is not worked out -- a full recursive computation.
- **F7** s 36(1)(c)(i) "3 months have passed since the last of the notices was given" -- `s 36(1)(c) -- the personal
  representative may divide our entitlement equally` -- the distribution falls after the day 3 months after the notice --
  on that day.
- **F8** s 39B(6) "extended until 1 month after the order is made" -- `ss 39A(3), 39B(4), (6) -- my time to elect` --
  the later of the 3-month day and the day 1 month after the order -- the order day + 1 month even if earlier.
- **F9** s 40A(1)(a) "the child of a spouse of the deceased" with s 5AA(2) ("a spouse of a deceased person only if, on
  the deceased's death ...") -- `s 40A -- I am a stepchild of the deceased` -- s 40A(3)(a) is followed: a child whose
  parent died first while still with the deceased is a stepchild -- s 5AA(2) excludes that child (finding 2).
- **F10** s 41(1) "on application by or on behalf of the said spouse, child or dependant" -- `s 41(1) -- I may apply for
  family provision`, `s 41 -- the court may order provision for me` -- NOTHING for anyone else (a grant limited in its
  own wording) -- JUST FALSE.
- **F11** s 41(1A) "in respect of a dependant" -- `s 41 -- the court may order provision for me` -- applied only to an
  applicant who is a dependant and neither a spouse nor a child -- applied to every applicant who is also a dependant.
- **F12** s 44(3) "not earlier than 6 [9] months after the deceased's death" -- `s 44 -- I can sue the personal
  representative over the distribution` -- on or after the day N months after the death; where no limb protects, NOTHING
  (the section protects, it does not give an action) -- JUST TRUE where unprotected.
- **F13** s 65 for two persons born on the same day -- `s 65 -- who is taken to have survived` -- "not answered" --
  seniority by time of birth (not asked).
- **F14** s 66(1) "with the exception of causes of action for defamation or seduction" -- `s 66 -- the estate can
  recover` -- JUST FALSE (the cause of action does not survive) -- NOTHING (the exception only withdraws the grant).
- **F15** s 66(1), (2) for damages the subsection does not exclude -- `s 66 -- the estate can recover` -- JUST TRUE (the
  cause of action survives and the exclusions do not reach them; the amount is for the general law) -- NOTHING.
- **F16** ss 14, 14A for a marriage or civil partnership before the will was made -- `ss 14, 14A -- my gift survives the
  testator's later union` -- JUST TRUE (the marriage cannot revoke a later will) -- NOTHING (the text is silent).
- **F17** s 34A household chattels and the value asked in the share question -- `s 35, schedule 2 -- my share of the
  residuary estate` -- the money share leaves the chattels out (the spouse takes them in kind; with no spouse they are
  shared like the rest) -- valuing the chattels into the residue.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries `NOTHING-kind` tags. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Applied here: "only if" (s 5AA(2), s 39B(2)), "means" (ss 34A, 40, 33Z(4)), "if" (ss 18(2), 36(1)(c), 39A(1), 40A(1)), "is
not valid" (s 9(1)), "must be" (s 10), "is void" (ss 11, 12), "is revoked" and "revokes" (ss 14, 15-15B), "provided"
(s 5A), "may only be made within" (s 33(2)), "shall not be heard ... unless" and "shall not be proceeded with until"
(s 41(8), (9)), "shall not make an order ... unless" (s 41(1A)), "No action shall lie" (s 44), "shall not include"
(s 66(2)) give `JUST FALSE`. `NOTHING` (16 tagged sites): a grant limited in its own wording (ss 41(1), 66(6)), silence
(s 18 for a document stating no testamentary intention, s 39A(3)(b) before the notice, s 44 where no limb protects, s 66(2)(d)
where the act did not cause the death), a pointer outside the text (a gift to a beneficiary who died before the
will-maker: lapse and s 33N), facts that do not fit, s 36's agreement or order, the s 21 statutory will, a child born
after the death whose 30 days have not run.

## What the Act turns out to say

1. **s 5AA(2)(c)(ii) reads "the deceased's dependant former husband or wife or civil partner.a"**, and the term the
   section defines in (4) is "dependent former husband or wife or civil partner". The deposit has a stray "a" (probably a
   note marker lost in conversion) and the two spellings differ; the (4) definition is applied. Worth checking against
   the authorised PDF.
2. **s 40A(3)(a) and s 5AA(2) pull against each other.** s 40A(1)(a) makes a stepchild "the child of a spouse of the
   deceased person"; s 5AA(2) says a person is a spouse of a deceased person "only if, on the deceased's death" they were
   married, partnered or a 2-year de facto partner. A parent who died before the deceased was not a spouse on the
   deceased's death, yet s 40A(3)(a) declares that the step-relationship does not stop merely because the parent died
   first. The encoding follows s 40A(3)(a), which states the purpose expressly (F9). Asserted.
3. **Three wordings of the 30-day rule.** s 5A ("remains alive for a period of 30 days"), s 33B ("dies within 30 days
   after"), s 35(2) ("does not survive ... for a period of 30 days"). Read alike: alive on the 31st day after (F3).
   Asserted on the 30th and 31st days.
4. **Definitions elided in the deposit.** s 5 "de facto spouse ..." and "property ...", s 34(1) "matrimonial home ...",
   and s 40 "spouse ..." appear with their text replaced by "..." in the converted deposit (likely omitted or relocated
   definitions in the HTML view). "Property" is read in its ordinary sense and "spouse" by s 5AA. Worth checking against
   the authorised PDF.
5. **s 36(2) restates the obvious, or something else.** It says that under an equal division by the personal
   representative, where there is issue, the "$150,000 must be distributed in equal shares" -- but s 36(1)(c) already
   divides the whole entitlement "in equal shares". Read as making the cash amount equal whatever is done with the
   household chattels; it does not change the shares asked here.
6. **The practical family-provision deadline is 6 months, not 9.** s 41(8) gives 9 months to start proceedings, but
   s 44(3)(a) protects a personal representative who distributes properly from 6 months after the death without signed
   written notice of any application or intended application on the estate ("any": notice given by another claimant
   counts as well as the asker's own). A claimant who wants the estate kept intact must give that notice within 6
   months, then start (or serve) within 9. Asserted (the 9 July / 10 July and 9 / 10 October cases).
7. **s 39A(3)(b) has no outer limit if the notice is never given.** The spouse who is not a personal representative has 3
   months from the personal representative's notice; until it is given the time does not run, and s 39D(2)(a) stops a
   sale while the time "has not ended". Asserted (NOTHING before the notice).
8. **s 66(2)(c) (breach of promise to marry)** appears spent: actions for breach of promise of marriage were abolished by
   Commonwealth law (Marriage Act 1961 s 111A, not deposited). Left out.
9. **Schedule 2 counts lines, not heads.** The spouse's 1/2 applies where there is "only 1 child of the intestate who
   survived, or who did not survive but left issue who survived": one line of issue, however many grandchildren are in
   it. Asserted (one dead child leaving two grandchildren: the spouse takes 1/2 of the remainder).

## Before relying on it

- Check findings 1 and 4 against the authorised PDF; obtain the Acts Interpretation Act 1954 (Qld) to settle F1.
- An independent test pass and the human gates; a coverage table for Part 2 divisions 3-5 and Part 5.
- Questions not asked: rectification grounds (s 33(1)), construction of wills (ss 33C-33S), court divisions between
  spouses (s 36(7)-(10)), variation of orders (s 42), the personal representative's own seat.
- Deploying is done by a person with Legalese Cloud access; nothing here is deployed.
