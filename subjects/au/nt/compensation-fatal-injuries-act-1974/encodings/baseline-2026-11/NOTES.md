# Compensation (Fatal Injuries) Act 1974 (NT) -- baseline encoding, a member of the deceased person's family

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`
(none is used). No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The calendar arithmetic is in one small module
(`cfi-dates.l4`, built-in date functions only, no daydate), the rules and exported questions in `cfi-claims.l4`, and the
worked cases in `cfi-cases.l4`.

The focus asked for: the provisions a claimant meets. The Act is short (twelve operative sections), so the whole operative
Act is encoded: whether it covers the death (s 5, with s 2(2)), who is a member of the family (s 4), when the wrongdoer is
liable (s 7), who brings the one action and when a family member may bring it (ss 8, 13, 14), what the damages may
include and what does not reduce them (s 10), the reduction for the deceased's own fault (s 11), the division after
unrecovered costs (s 10(2)), money paid into court (s 12) and omitted names (s 15). The one step with a deadline -- the
personal representative's 6 months after the death, after which a member of the family may commence the action -- is a
regulative rule run by EVALTRACE inside an exported question.

## Edition

- **Act:** Compensation (Fatal Injuries) Act 1974 (NT), first made as the Compensation (Fatal Injuries) Ordinance 1974
  (Act No. 36, 1974), assented and commenced 23 September 1974. The deposited text is reprint REPC010, "as in force at
  28 November 2022" (the last amendment: Burial and Cremation Act 2022), the current reprint on the NT Legislation
  register when retrieved on 6 November 2026:
  `../../registers/source-bundle/Compensation-Fatal-Injuries-Act-1974-NT-current-reprint-REPC010.txt`.
- **Numbers set elsewhere:** none. The Act fixes two periods itself (6 months in s 10(5) and s 13(1)) and one age (18 in
  s 10(3)(e)(i)); no regulation sets a number. Its commencement date is from the endnotes' list of legislation.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (a widow bringing the action herself on the last day of the 6 months) was run once in a
scratch copy, since deleted, and showed as "assertion failed" (104 satisfied, 1 failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `cfi-dates.l4` | 0 | 0 | 0 | 0 |
| `cfi-claims.l4` | 0 | 0 | 0 | 0 |
| `cfi-cases.l4` | 0 | 0 | 105 | 105 |

Every exported question has cases, with the edges: a death on the commencement day and the day before; a motor-accident
death with an action precluded and not; every relationship in s 4; each element of s 7 failing; the regulative rule alone
on day 0, the last day of the 6 months and the day after; a family member on the last day of the 6 months and the next
day, after a 31 August death (the 6 months end on 28 February), with an action already brought, with no damage, with an
unnamed relationship; every head of damages on and off; a child turning 18 on the day of the death and the day after,
born after the death, born on 29 February; every paragraph of s 10(4); the deceased's own settlement on the last day of
the 6 months after the wrongful act and the day after; unrecovered costs equal to the damages, above them, and $1 below;
each branch of s 12 and s 15.

**No mirror cases.** One seat.

## Seat

**A member of the deceased person's family who sustained damage because of the death** (`cfi-claims.l4`): the person
for whose benefit the action is brought (s 8(2)), and who may bring it in his or her own name if the personal
representative has not commenced it within 6 months (s 13). "Does this Act cover the death?", "Am I a member of the
family?", "Is the wrongdoer liable?", "Who brings the claim, and can I bring it myself?", "From what day?", "What can the
damages include?", "Until when can a carer for my child be claimed?", "Is my award reduced by the insurance I received?",
"How much do I get?", "Can I get the money paid into court?", "My name was left off: can I still share?".

The personal representative is an actor in the s 13 rule, not a seat: the questions are the family member's. The court
and the jury get no seat: their findings (wrongful act, the reduction for the deceased's fault, the shares, whether a name
should have been included) are asked as facts, and their discretions are reported as discretions. No second seat was
written: the defendant (the wrongdoer, who may be the Crown, s 6) would ask the s 7, s 10(4) and s 12 questions from the
other side with the same answers; a defendant's layer can be added beside this one.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number.
- **The actors the text names.** Followed: the deceased, the members of the family, the personal representative, the
  defendant ("the person who would have been liable"), the court and the jury.
- **Judgments handed to someone else are answered conditionally.** Followed. Inputs: whether the death was caused by a
  wrongful act, neglect or default and the deceased could have sued (s 7); the reduction for the deceased's own fault (s 11,
  under the Law Reform (Miscellaneous Provisions) Act 1956); the shares (s 10(2)); whether the court is satisfied a name
  should have been included (s 15). Never decided: the amount of damages (s 10(1)), what is "reasonable" (s 10(3)), whether
  the court makes a s 15 order.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "child", "parent", "member of a
  deceased person's family", the s 4(3) deeming rules. Asked: "spouse", "de facto partner", "in loco parentis", "infant"
  (read as under 18), "accident" and "precluded" under the Motor Accidents (Compensation) Act 1979, "wrong" and the estate's
  reduction under the Law Reform (Miscellaneous Provisions) Act 1956, "burial" and "disposal" (Burial and Cremation Act
  2022).
- **One case is the text's natural unit.** Followed: one death, one wrongdoer (s 8(1) allows one action against each).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts ("solatium": money for grief and
  suffering; "personal representative": executor or administrator).
- **Operative sections in; machinery out.** Followed: s 1 (short title), s 2(1) (repeal), s 15(3) and (4) (procedural
  orders; powers not limited) out. s 6 (binds the Crown) is stated in the s 7 question; s 16 (the jury stands in for the
  court in s 10) is noted in comments.

## Scope

**In.** s 2(2), ss 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15(1) and (2), 16: the whole operative Act.

**Out, and why.**
- s 1 (short title), s 2(1) (repeal of the 1938 and 1970 Ordinances), s 15(3) and (4): machinery.
- **The time limit for the action.** s 9 (the old limitation section) was repealed by the Limitation Act 1981 (No. 87,
  1981, s 3). The deadline for commencing the action is that Act's (deposited at `subjects/au/nt/limitation-act-1981`), not
  this one's, and is not encoded here (finding 1).
- The Motor Accidents (Compensation) Act 1979 (whether a death is from an "accident" within it, and whether it precludes
  an action, s 5(2)) and Part II and Part V of the Law Reform (Miscellaneous Provisions) Act 1956 (the reduction for the
  deceased's own wrong, s 11): other Acts, asked as facts.
- The Compensation (Fatal Injuries) Ordinance 1938, which s 2(2) keeps for deaths before 23 September 1974: not deposited;
  the s 5 question names it and stops.
- No requirement ledger exists for the Northern Territory, and no ledger entry names this Act; none was raised.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 5(2) "except in those circumstances in which an action ... is not precluded by that Act" -- `s 5 -- does this
  Act cover the death` -- an "except" once met (decided case by case under the 2026-11-05 ruling): where the Motor
  Accidents (Compensation) Act leaves an action open, this Act applies -- the "except" only lifts s 5(2) and leaves the
  question open (NOTHING).
- **F2** s 4(2) list of members of the family, and "child" and "parent" defined by "includes" -- `s 4 -- am I a member of
  the family` -- any other relationship (aunt, cousin, step-sibling, fiance) is NOTHING-kind, since the list is not closed
  with "only" -- an exhaustive list, so JUST FALSE ("not a member of the family").
- **F3** s 13(1) and s 10(5) "within 6 months after" -- `the last day of 6 months after` (cfi-dates.l4) -- the period ends
  on the same day of the month 6 months later, or that month's last day where it is shorter; the next day is outside it --
  the Interpretation Act 1978 (NT)'s rule, not deposited, which could count differently.
- **F4** s 10(3)(e) "infant" -- `s 10(3)(e) -- until when can carer expenses for my child be claimed` -- under 18 at the
  death; a child whose 18th birthday is the day of the death is not an infant -- "infant" read by the Age of Majority Act
  (not deposited), or the birthday counted the other way.
- **F5** s 10(5), a settlement, release or judgment the deceased made more than 6 months after the wrongful act --
  `s 10(4) and (5) -- is my award reduced by it` -- the Act does not say (NOTHING-kind) -- the negative implication of
  s 10(5) (not taken into account, JUST FALSE), or s 10(4)(g) (no reduction for "any other gain or benefits").
- **F6** s 10(2) "after deducting the costs not recovered from the defendant" -- `s 10(2) and s 11 -- how much do I
  receive` -- where the unrecovered costs exceed the damages recovered, nothing is left to divide (0) -- the text gives no
  rule for a shortfall.
- **F7** s 8(2) "for the benefit of those members ... who sustained damage because of his or her death" -- `s 8 and s 13 --
  who brings the action, and can I bring it myself` -- a member who sustained no damage gets the text's no (a restrictive
  clause read as a condition) -- NOTHING (a limit in the section's own wording).
- **F8** s 8(1) "against any one person" -- the same function -- the input asks whether an action has already been brought
  against this wrongdoer; a second wrongdoer can be sued separately -- one action for the death, whoever the defendants.
- **F9** s 13(1), the family member's day counted from the death -- the same function -- a "today" before the death is
  counted as day 0 (not yet) -- an error.
- **F10** s 10(3)(c) "if the deceased person is survived by a spouse or de facto partner" -- `s 10 -- what can the damages
  include` -- a former spouse or partner (a member of the family by s 4(2)(g)) does not open the consortium head -- "spouse"
  read to include a former spouse.
- **F11** s 10(3) "may include" -- the same function -- the heads whose "if" is met are listed; a head the text does not
  name is neither listed nor excluded, and s 10(1) damages and solatium are always listed -- solatium only for some
  members (the Act does not limit it).

Sites decided without a fork line: s 5(1) "applies only where a death occurs on or after the commencement" (a condition
closed by "only": the text's no); s 7(1) "Where ..." (ruling (b): the text's no); s 10(4) "no reduction must be made" (a
flat negative); s 12(2) "no portion ... must be paid out ... except under an order" (a flat negative); s 10(3)(e) "if ...
an infant" (ruling (b) with "if": the text's no); s 12 and s 15 "Where ..." (ruling (b)).

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

This encoding carries three `NOTHING-kind` tags (s 4 and its use in s 8, F2; s 10(5), F5). The questions answer with a
choice from a list rather than a MAYBE BOOLEAN: the answers marked "NOTHING-kind" are the NOTHING answers, and the answers
marked "the text's no" are JUST FALSE. The rulings it follows:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The 6 months of s 13(1) are the regulative rule (`PARTY the personal representative DO commence the action WITHIN` the
days to the last day of the 6 months, `LEST PARTY a member of the family MAY commence the action`), run by EVALTRACE
inside the question; within the period the family member's answer is "not yet".

## What the Act turns out to say

1. **The Act sets no time limit for the action.** s 9 was repealed by the Limitation Act 1981 (No. 87, 1981); the
   deadline is in that Act. The only periods here are the personal representative's 6 months (s 13(1)) and the 6 months
   for the deceased's own settlement (s 10(5)). Not asserted (out of scope).
2. **s 4(3) has paragraphs (b) and (d) only.** Paragraphs (a) and (c) have gone without renumbering. The list of
   amendments records seven amendments of s 4 (from the Status of Children Act 1978 to the Burial and Cremation Act 2022)
   and does not say which removed them. Noted only.
3. **s 10(5) has a word missing:** "the wrongful act, neglect or default causing his or death"; s 7(2) has "causing his or
   her death". Read as "his or her". Possible drafting error; no effect on the encoding.
4. **s 10(3)(e) reads "a child of his or her who is an infant"** ("his or hers"), and (e)(i) says "a person on whose behalf
   the action is brought" where every other provision says "for whose benefit". Read as the same persons. Noted only.
5. **A settlement the deceased made more than 6 months after the wrongful act is not dealt with.** s 7(2) keeps the
   wrongdoer's liability despite any settlement, and s 10(5) takes into account only a payment under one made within
   6 months. On the words, a later settlement neither defeats the action nor is taken into account (fork F5). Asserted
   (the day after the 6 months answers NOTHING-kind).
6. **A former spouse or de facto partner is a member of the family** (s 4(2)(g)), and s 10(4)(h) bars any reduction for
   their remarriage prospects; but the consortium head (s 10(3)(c)) is only for a surviving spouse or de facto partner.
   Asserted (s 4 and s 10 cases; fork F10).
7. **Step-siblings are not named,** though step-parents ("parent") and stepchildren ("child") are; nor are aunts, uncles,
   nieces, nephews or cousins. Asserted as NOTHING-kind (fork F2).
8. **The 6 months are the personal representative's alone.** Within them a family member cannot bring the action even if
   no personal representative has been appointed (s 13's heading names that case, the text does not shorten the period).
   Asserted (a widow on the last day of the 6 months: "not yet").
9. **Motor accident deaths are largely outside the Act** (s 5(2)): it applies to them only where the Motor Accidents
   (Compensation) Act 1979 does not preclude an action. Asserted, with that Act's answer as a fact.
10. **s 10(3)(c) assesses consortium "as ... by a husband"** for any surviving spouse or partner, and s 11(1) still says
    "for the benefit of his estate": wording older than the Act's gender-neutral amendments. Noted only.
11. **The commencement date comes from the Ordinance.** The Act began as the Compensation (Fatal Injuries) Ordinance 1974,
    commenced 23 September 1974 (endnotes, list of legislation); s 5(1)'s "commencement of this Act" is read as that day.
    Asserted (a death on 23 September 1974 is covered, on 22 September it is not).

## Before this is worth relying on

- The Limitation Act 1981 (NT) for the time limit (finding 1), and the Interpretation Act 1978 (NT) for counting months
  (fork F3), neither encoded here.
- The Motor Accidents (Compensation) Act 1979 answer for s 5(2), and the Law Reform (Miscellaneous Provisions) Act 1956
  for s 11, wired to their own encodings when cross-folder links are possible.
- A lawyer's view on forks F2, F5, F7 and F10 and findings 5 and 8; an independent test pass and a human gate.
