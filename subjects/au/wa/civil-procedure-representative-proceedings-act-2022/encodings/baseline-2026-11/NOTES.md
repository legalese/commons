# Civil Procedure (Representative Proceedings) Act 2022 (WA) -- baseline encoding, the claimant in a class action

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Act is short (37 sections) and is taken whole:
every operative section is either encoded or listed below as out, with the reason. Its shape follows Part IVA of the
Federal Court of Australia Act 1976, whose baseline (`subjects/au/federal-court-of-australia-act-1976/encodings/baseline-2026-11/`)
was read for layout; nothing is imported from it (the stable `l4` cannot import across subjects), and the differences
the WA text makes are recorded as findings.

Modules:
- `crp-dates.l4` -- the date arithmetic, with Interpretation Act 1984 ss 61 and 62; the only module that imports `daydate`;
- `crp-rules.l4` -- the rules, by section, and the one regulative rule;
- `crp-seat.l4` -- the claimant's questions, each `@export` with `@desc` inputs, importing the rules and restating none;
- `crp-cases.l4` -- the cases.

## Edition

- **Act:** Civil Procedure (Representative Proceedings) Act 2022 (WA), No. 30 of 2022, deposited at
  `../../registers/source-bundle/mrdoc_45801.txt`, a plain-text conversion of the Word file from the Western Australian
  Legislation website (mrdoc 45801), retrieved 7 September 2026. The compilation table lists no amending Act. Part 1
  came into operation on 14 September 2022, the rest on 25 March 2023 (s 2, SL 2023/21 cl. 2). Amendments after
  retrieval are not in the text.
- **Rules that fill in its steps:** Rules of the Supreme Court 1971, version 09-am0-00 (currency from 11 December 2025),
  deposited at `subjects/au/wa/rules-of-the-supreme-court-1971/registers/source-bundle/mrdoc_49048.txt` (retrieved 6
  November 2026). Used: O. 18A r. 2 (a representative proceeding only by a legal practitioner), r. 4 (consent by Form
  10A, filed and served), r. 5 (opt out by filing Form 10B). Hand-worked into the rules here, with the rule number.
- **Interpretation:** Interpretation Act 1984 (WA), deposited at
  `subjects/au/wa/interpretation-act-1984/registers/source-bundle/mrdoc_49111.txt`. Used: s 61(1)(b), (c), (e) and
  s 62(3) (counting days and months).
- **Not deposited and not applied:** the court rules fixing the time for instituting an appeal (s 30(3) is worked from
  the representative party's last day, an input), and the limitation laws whose periods s 32 suspends (the old last
  day is an input; the WA Limitation Act 2005 has its own baseline encoding beside this subject).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, at most two
processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `crp-dates.l4` | 0 | 0 | 0 | 0 |
| `crp-rules.l4` | 0 | 0 | 0 | 0 |
| `crp-seat.l4` | 0 | 0 | 0 | 0 |
| `crp-cases.l4` | 0 | 0 | 168 | 168 |

The cases file also runs one `#TRACE` of the s 28(3)(c) rule (a claim on day 212 of 212: FULFILLED). Every exported
question has cases, with the edges: the day Part 2 came into operation and the day before, and before Part 1; 6 and 7
claimants and each s 6(1) limb and s 10; standing without an interest of one's own and without a lawyer; each kind of
person in s 8(2) with and without consent; opt-out notices the day before, on and after the opt-out date, not a Form
10B, and in an appeal; a hearing on and the day before the opt-out date; later claims on the commencement day, the day
after, and on and the day before the Court's cut-off; s 32 with each outcome, an expired period, and a class action
begun on the old last day; every notice subject with dispensing, damages and orders; 6, 7 and 100 likely group members
and each s 15 and s 16 limb; every cell of the costs matrix; s 33 at, under and just over the damages; the earliest end
of the distribution period across month ends and a leap year; a fund claim on the last day, one day late, and before
the order; the group member's appeal window's first and last days and a last day falling on a weekend; s 36 on the day
it came into operation and the day before.

## Seat

**The claimant in a class action** (`crp-seat.l4`): a group member, or a person with a claim who starts and runs the
class action as representative party (or subgroup representative). "Can my claim be brought in a class action?", "Can I
start the class action as representative party?", "Can I keep running the class action without a claim of my own?",
"Am I a group member?", "Must I consent to be a group member?", "Do I need a next friend?", "Can I opt out of the class
action?", "By when must I opt out?", "Can the hearing start before my opt-out date?", "Can the group be widened to
include my later claim?", "What happens to my time limit?", "Must I be given notice of this?", "Can the Court order
personal notice to each of us?", "Does missing a notice affect the class action?", "Can the representative party be
replaced on my application?", "Can the representative party withdraw?", "Can the class action be stopped?", "Can I go
on with my own claim after the class action stops?", "Can I be ordered to pay costs?", "How much of the damages can go
to the representative's costs?", "Can the class action be settled?", "Can damages be awarded as a lump sum?", "Can my
award be held back?", "Will the judgment bind me?", "What is the earliest end of the distribution period?", "Can I
claim from the fund?", "By when can I appeal for the group?", "Can I appeal for the group?", "Can I be sued for
maintenance or champerty?" (29 questions).

No seat for the Court or the Minister. No respondent seat was written; one would ask several of the same rules (ss 15,
16, 22, 28(5)) from the other side.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: Rules of the Supreme Court O. 18A supplies the
  forms and the lawyer requirement; the Interpretation Act supplies the counting of days and months. The appeal rules
  and limitation laws are not deposited, so the dates they give are asked.
- **The actors the text names.** Followed: group member, representative party, subgroup member, subgroup representative
  party, respondent, the Court.
- **Judgments answered conditionally.** Followed: a substantial common issue (s 6(1)(c)), sufficient interest (s 7), the
  Court's view of the likely number of group members (s 14), excessive distribution cost (s 15), the interests of
  justice (ss 16, 21), adequacy of representation (s 21), notice in sufficient time (s 24(4)), "just" (ss 25(4), 28(4)),
  practicable and not unduly expensive (s 26(4)), a reasonably accurate assessment (s 27(3)), reasonable and recoverable
  costs (s 33) are inputs worded "if the Court ...". A yes about a power of the Court means it can act, not that it will.
- **The Act's definitions worked out; borrowed terms asked.** Followed: group member (s 3 with s 8) and the distribution
  period (s 28(3)) are worked out; "person under disability" (s 9(1) points to the rules of the Court), "limitation
  period", cross-vesting jurisdiction, "monetary relief" and "want of prosecution" are asked.
- **One case.** One class action and one claimant in it.
- **The Act's terms with plain glosses.** Followed: "class action" glosses "representative proceeding"; "time limit"
  glosses "limitation period"; "litigation representative" glosses "next friend".
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** ss 3, 4(1), 6(1) (with (3), (4) and s 7(2) noted: they remove requirements, so nothing is asked), 7(1), (3), 8,
9, 10, 12(2), (4), 13(2), 14, 15(2), (3), 16(1), 17, 18(3), 19(2), 21(1), (2), 22, 23(1), 24(2), (4), 25(1)-(5), 26(4),
(7), 27(1)(f), (3), 28(3)(c), (4), 29, 30(3), (4), 31, 32, 33(1), (2), 36; Rules of the Supreme Court 1971 O. 18A rr. 2,
4, 5; Interpretation Act 1984 ss 61(1)(b), (c), (e), 62(3).

**Regulative rule:** one. s 28(3)(c), the distribution period "within which group members may make a claim for payment
out of the fund", as a bare `DO ... WITHIN` the days from the fund order to the end of the period (`HENCE FULFILLED`,
`LEST BREACH ... BECAUSE` naming s 28(4)). The text says "may", so neither MUST nor MAY fits: a MAY never breaches and
cannot tell a claim in time from none, and the claimant owes no duty to claim. `DO` is the neutral action. It is run by
EVALTRACE inside "Can I claim from the fund?", which takes only plain dates. The opt-out (s 12(2)) and the group
member's appeal (s 30(3)) are permissions with periods, computed as dates and periods rather than run as traces.

**Out, and why:**
- s 1, s 2 (except the commencement dates, used), s 5 (binds the Crown), s 35 (rules of court), s 37 (review): machinery.
- s 4(2) (other representative actions under the rules): saves another procedure; nothing to compute.
- s 11 (contents of the originating process; (2) names need not be given): the representative party's drafting.
- s 12(1), (3), s 13(1), (3), (4): the Court fixing and extending dates and giving leave; the dates are inputs.
- s 15(2)(b) (stay of the monetary relief) is folded into "Can the class action be stopped?"; s 16(2), (3) (no further
  application by the respondent): the respondent's side.
- s 18(1), (2), s 19(1), s 20 (directions, subgroups, separate proceedings): the Court's case management; the costs
  consequences in ss 18(3) and 19(2) are in.
- s 21(3), s 24(1), (3), (5): the Court's further orders and the representative's own settlement; the preconditions in
  s 24(4) are in.
- s 23(2), s 25(6), s 26(1)-(3), (5), (6), s 27(1)(a)-(e), (g), (2), (4), s 28(1), (2), (3)(a), (b), (d), (5): the
  Court's powers over notices, judgment and distribution; what the claimant meets (notice, the lump-sum bar, the
  distribution period, late claims) is in. s 25(6) ("as soon as practicable") is stated in the notice question's text.
- s 30(1), (2), (5), (6): who the parties to an appeal are, and notice of it; the group member's own appeal right in
  (3) and the no-opt-out rule in (4) are in.
- s 34 (general power): nothing to compute; noted in the stopping question (other powers are not answered).
- s 36(2)(b) (contracts contrary to public policy): left to the general law; the export's text says so.
- Litigation funding, common fund orders and contingency fees: the Act says nothing about them beyond s 36; they are for
  case law and the Legal Profession Uniform Law.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: s 6(1) "if" (a)-(c); s 10 "cannot"; O. 18A r. 2 "cannot ... except"; s 3 "means"; s 8(2) "unless";
  s 9(2) "not necessary", s 9(3) "unless the Court otherwise orders"; s 12(2) outside the period; s 30(4) "cannot opt
  out"; s 12(4) "must not"; ss 14, 15, 16 "if"/"only"/"where"; s 17 "where"; s 31 "must not ... other than", and "and not
  the representative party" (ss 18(3), 19(2)); s 21 "if" and "may only"; s 24(4) "must be satisfied"; s 22 "where";
  s 23(1) "cannot"; s 25(4) "unless ... must not"; s 26(4) "must not ... unless"; s 26(7) "does not affect"; s 27(3) "not
  ... unless"; s 28(3)(c) outside the period, s 28(4) "if"; s 29 "other than"; s 30(3) "if" and its period; s 33(2)
  "cannot ... unless"; s 36(1) "abolished".
- `NOTHING`: s 4(1) before 14 September 2022 (scope), and before Part 2 came into operation (silent, fork F1); s 7(1)
  without a sufficient interest (silent); s 7(3) for a person who did not commence it (scope, fork F2); s 9 for a person
  not under disability (scope); s 12(2) without a filed Form 10B (grant's wording, fork F3); s 13 outside (a) or (b)
  (grant's wording, fork F5); s 24 for a representative not settling (grant's wording); s 25(5) without an order
  (silent); s 26(7) without a missed notice (scope); s 29 for a person the judgment does not describe (scope); s 30(3)
  for a non-member (scope); s 36 for a cause accruing before 25 March 2023 (points outside the sources).

### Forks

- **F1** ss 2, 4, `ss 2, 4 -- Part 2 reaches a proceeding commenced that day`: a proceeding commenced from 14 September
  2022 to 24 March 2023 answers NOTHING (s 4 was in operation, s 6 was not); other reading: JUST FALSE (no power to
  commence a representative proceeding existed).
- **F2** s 7(3), `s 7(3) -- I keep my standing without a claim`: a representative party who did not commence the
  proceeding (one substituted under s 21 or s 24(3)) answers NOTHING; other reading: JUST FALSE, as the Federal Court
  baseline reads s 33D(2)'s "Where" (here there is no "where", only "A person who has commenced").
- **F3** s 12(2), `s 12(2) -- I can opt out`: a written notice in time that was not filed as a Form 10B answers NOTHING
  (O. 18A r. 5 says a member "may" opt out by filing a Form 10B; the Court may accept another written notice); other
  reading: JUST FALSE ("by written notice given under the rules of the Court").
- **F4** s 12(2), `s 12(2) -- the last day to opt out`: the day before the fixed date, with no roll-over where that day
  is a weekend (Interpretation Act s 61(1)(e) speaks of a time "limited" by a written law; the date is the Court's);
  other reading: s 61(1)(h) or (e) moves a weekend last day, which can only move it onto the fixed date itself.
- **F5** s 13, `s 13 -- the group can be altered to include me`: a claim accruing on the commencement day, or on or
  after the Court's cut-off, answers NOTHING; other reading: JUST FALSE ("after", "before" as periods under ruling (a)).
- **F6** ss 18(3), 31, `s 31 -- costs can be awarded against me`: a subgroup representative party is read as a subgroup
  member, so s 31 shields them from all but the subgroup's costs (JUST FALSE for the rest); s 18(2) lets the Court
  appoint "a person", who might not be a group member, and s 31 would not then protect them. And the representative
  party is never liable for subgroup costs, which s 18(3) says only "Where the Court appoints a person other than the
  representative party".
- **F7** s 33(1), `s 33 -- the most paid to the representative out of the damages`: the most is the excess, capped at
  the damages awarded; the text does not state the cap, but the money must come "out of damages awarded".
- **F8** s 27(3), `s 27(3) -- damages can be awarded as a lump sum`: when approving a settlement, JUST TRUE (the power
  in s 27(1)(f) stands once (3) is out of the way); other reading: NOTHING (the exception says no more), as the Federal
  Court baseline reads s 33Z(3)'s "Subject to section 33V".
- **F9** s 25(4), `s 25 -- I must be given notice`: the bar on deciding a settlement without notice is read as a duty to
  give notice unless the Court is satisfied; other reading: no duty, only a bar on deciding (NOTHING).
- **F10** s 28(3)(c), `s 28(3)(c) -- the earliest end of the distribution period`: "6 months after the day on which the
  order is made" is a period of 6 months beginning the next day (s 61(1)(b)), ending on the corresponding date less one
  or the month's last day (s 62(3)); other reading: the date 6 months on from the order day. The two mostly agree, but
  an order on 30 November 2026 gives 31 May 2027 here and 30 May 2027 on the other reading. Asserted.
- **F11** s 30(3), `s 30(3) -- my last day to appeal for the group`: a last day on a Saturday or Sunday moves to the
  Monday (s 61(1)(e)); public holidays, also excluded days under s 61(2), are not computed, so a last day on a public
  holiday is given unmoved. The representative party's last day is an input taken as the rules give it, already moved.
- **F12** s 29(b) "other than", `s 29 -- the judgment binds me`: an opted-out person answers JUST FALSE ("(other than
  X)" has no ruled convention); other reading: NOTHING.
- **F13** s 32, `s 32 -- my limitation period`: the days left are counted from the day after the class action began to
  the old last day, and added to the day the period runs again; a class action begun on the old last day leaves that
  later day only; other reading: the day of commencement counts as a day left, adding one day.

## What the Act turns out to say

1. **A gap of six months in 2022-23.** s 4(1) applies the Act to proceedings commenced on or after the day s 4 came into
   operation (14 September 2022, with Part 1), but s 6, which allows a representative proceeding, came into operation
   only on 25 March 2023 (fork F1). A proceeding begun in between was within s 4 with no Part 2 to use. Asserted.
2. **No cut-off for old causes of action.** Unlike s 33B of the Federal Court Act (causes of action after 4 March 1992),
   s 4(1) reaches a cause of action accrued "before, on or after" commencement; only the day the proceeding is commenced
   matters, so the seat question asks that day, not the day the claim arose. Asserted.
3. **The opt-out date itself is too late.** s 12(2) requires notice "before the date so fixed"; Interpretation Act
   s 61(1)(c) confirms the day is excluded. A group member reading "opt out by 30 June" may miss it. Asserted.
4. **Costs protection is in the Act itself, and wider than the Federal Court's.** s 31 bars costs against "a group member
   or subgroup member" except the three named awards, so a subgroup representative party who is a subgroup member is
   shielded from the group's general costs (fork F6); the Federal Court's s 43(1A) is silent on that. Asserted.
5. **Late fund claims turn on the state of the fund at the end of the period.** s 28(4) asks whether the fund "has not
   been fully distributed before the end of the distribution period", not (as the Federal Court's s 33ZA(4)) whether it
   has "already" been fully distributed when the late claim is made. Read literally, a fund emptied after the period
   ended still allows a late claim to be considered; a fund emptied before the end never does. Asserted.
6. **s 25(4) is a bar, not a duty** (fork F9), as in the Federal Court Act.
7. **No opt-out from an appeal, though the time limit stays suspended through it.** s 30(4) bars opting out of an
   appeal; s 32(2) keeps the limitation period suspended until "any appeals" are determined. Asserted.
8. **The torts of maintenance and champerty are gone for causes accruing from 25 March 2023** (s 36), the day Part 6
   came into operation; s 36(2)(b) keeps the rule that a funding contract may be contrary to public policy, which the
   Act does not settle. Asserted.
9. **"Next friend" only.** s 9 speaks only of a next friend and defers the definition of a person under disability to
   the rules of the Court; the Federal Court Act adds "committee". The encoding asks the rules' answer as a fact.

## Before relying on it

- Check for amendments after 7 September 2026 (a later compilation of the Act) and to RSC O. 18A after 11 December 2025.
- Deposit the Supreme Court (Court of Appeal) Rules 2005 and compute the representative's appeal time (s 30(3)) rather
  than ask it; compute WA public holidays for fork F11.
- An independent test pass and a human gate; a lawyer's view on forks F1, F3, F6, F8 and F10.
- A respondent seat (ss 15, 16, 22, 28(5)).
