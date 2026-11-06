# Law Reform (Miscellaneous Provisions) Act 1941 (WA) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The dates are in one small module (`lrmp-dates.l4`,
built-in date functions only, no daydate), the rules and the 14 exported questions in `lrmp-claims.l4`, and the worked
cases in `lrmp-cases.l4`.

The focus asked for: the provisions a claimant meets (survival of causes of action; the dust-disease provisions). The Act
is five sections long, so the whole operative Act is encoded: survival of causes of action for and against a dead
person's estate (s 4(1), (4)), what the estate can and cannot recover (s 4(2)), the asbestos and silica exceptions that
let an estate keep damages for pain and suffering (s 4(2a), (3)), the estate's claim beside the dependants' claim
(s 4(5)), the discount rate for lump-sum future loss in injury and death awards (s 5), and the spousal capacity
provisions (s 2, s 3). The Act imposes no duty with a deadline on anyone, so there is no regulative rule.

## Edition

- **Act:** Law Reform (Miscellaneous Provisions) Act 1941 (WA), Act No. 29 of 1941, in operation from 24 October 1942.
  The deposited text is the compilation on the Western Australian Legislation website when retrieved on 7 September 2026,
  the last amendment recorded being the Civil Liability Amendment (Provisional Damages for Dust Diseases) Act 2024 Part 3
  (in force 1 December 2024): `../../registers/source-bundle/mrdoc_47978.txt`.
- **Numbers set elsewhere:** the s 5(1)(d) discount rate, if the Governor has fixed one by Order. No Order is deposited:
  whether one is in force, and its percentage, are asked; without one the Act's 6% applies (s 5(1)(e)).
- **Dates used** (from the compilation table): the Act, 24 October 1942; the Law Reform (Miscellaneous Provisions
  (Asbestos Diseases)) Act 2002, 21 March 2002; the Civil Liability Amendment (Provisional Damages for Dust Diseases) Act
  2024 Part 3, 1 December 2024; the Limitation Legislation Amendment and Repeal Act 2005, 15 November 2005.
- **Not deposited:** the Limitation Act 2005; the Civil Liability Act 2002 Part 2 Division 5 (initial and subsequent
  actions, borrowed by s 4(1A)); the Fatal Accidents Act 1959; the text of s 4 as it stood before 15 November 2005.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
deliberately wrong assertion (an Order rate of 3% asserted to give 6%) was run once in a scratch copy and showed as
"assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lrmp-dates.l4` | 0 | 0 | 0 | 0 |
| `lrmp-claims.l4` | 0 | 0 | 0 | 0 |
| `lrmp-cases.l4` | 0 | 0 | 64 | 64 |

Every exported question has cases, with the edges: a death on 24 and 25 October 1942; a cause of action accrued on
14 and 15 November 2005; an asbestos death on 21 and 22 March 2002; a silica death on 1 and 2 December 2024; an asbestos
death on 1 December 2024 (still within s 4(2a)); each condition of s 4(2a) and (3) failing in turn; each excepted kind of
claim; a claim out of time; the s 4(4) deeming with the wrongdoer dying before, with, and after the damage; each limb of
s 5(1) and each failure (not a lump sum, another kind of loss, not personal injury or death); an Order in force and not.

**No mirror cases.** One seat.

## Seat

**The claimant** (`lrmp-claims.l4`). Mostly the person pursuing, for a dead person's estate, a claim the dead person had
(the executor or administrator, or a family member acting for the estate): "Does my late father's claim survive his
death?", "Can his estate still get damages for his pain and suffering from mesothelioma?", "Can the estate claim exemplary
damages, the lost years' earnings, funeral expenses?", "Does the estate's claim cut down our own claim as dependants?".
Also the injured person claiming against someone who has died ("Can I still claim against his estate?"), the injured
person or dependants whose lump-sum damages for future loss are discounted ("What discount rate applies?"), and a married
person ("Is my legal personality separate from my spouse's?"). The courts, the Governor and the Attorney General get no
seat. No second seat was written: the estate of a wrongdoer that answers a surviving claim would ask the same s 4(1)
questions with the same answers.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No s 5(1)(d) Order is deposited: asked.
- **The actors the text names.** Followed: the deceased person, the estate, the dependants, the Governor (s 5), the
  Attorney General (s 5(2)).
- **Judgments handed to someone else are answered conditionally.** Followed. Whether a claim is out of time under the
  Limitation Act 2005, whether an injury is "latent", whether the death resulted from it, whether the death was caused by
  the act or omission, and when the cause of action accrued are asked as facts.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "personal injury" (s 5(3), an
  "includes" definition: injury, disease, impairment). Asked: "proceedings" in its s 4(1A) extension (initial and
  subsequent actions under the Civil Liability Act 2002), "latent injury", accrual.
- **One case is the text's natural unit.** Followed: one cause of action of one deceased person (s 4); one part of one
  award (s 5); one married person (s 3).
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (below).

## Scope

**In.** s 2, s 3, s 4 ((1A), (1) and its proviso, (2)(a)-(e), (2a), (3), (4), (5)), s 5(1), (3).

**Out, and why.**
- The long title and s 1 (short title and commencement): no rule; the commencement date is used as the s 4(1) gate.
- s 5(2) (the Governor may fix a rate by Order on the Attorney General's recommendation): machinery; its result is asked.
- The s 4 that the Limitation Legislation Amendment and Repeal Act 2005 s 15(4) keeps for causes of action accrued before
  15 November 2005: not deposited, so every s 4 question answers NOTHING for such a cause of action (finding 4).
- How the present value is computed at the s 5 rate (single sum, annuity, tables): the Act says only "by adopting a
  discount rate"; no calculator is offered (finding 6).
- No requirement-ledger entry exists for this Act in `subjects/au/wa/requirements.jsonl`, and none was raised: no
  scenario life has reached it.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 4(1) "Subject to ... the Limitation Act 2005" -- `survives the death under s 4(1)` and every question built on
  it -- a claim already out of time answers NOTHING (the answer lies outside the sources) -- JUST FALSE (the claim cannot
  survive as an enforceable claim). The proviso's flat negative is answered before this point.
- **F2** s 4(2)(b) "in the case of a breach of promise to marry" -- `s 4(2)(b) -- is the estate's claim for breach of
  promise to marry limited to damage to the estate` -- read as a "where" condition, so another kind of claim is JUST FALSE
  -- NOTHING (a scope limit with no "only").
- **F3** s 4(2)(c) "except that a sum in respect of funeral expenses may be included" -- `s 4(2)(c) -- can the estate's
  damages include funeral expenses` -- where the death was not caused by the act or omission, NOTHING (the paragraph is
  silent) -- JUST FALSE.
- **F4** s 4(5) "the Imperial Act 9th and 10th Victoria, Chapter 93" -- `s 4(5) -- does the estate's claim cut down the
  dependants' claim` -- read as reaching the dependants' claim that replaced the repealed Imperial Act (the Fatal
  Accidents Act 1959), JUST FALSE -- NOTHING for a death after the repeal, the reference being to a repealed Act
  (finding 3).
- **F5** s 4(4) "Where damage has been suffered ... if that person had not died before or at the same time as the damage
  was suffered" -- `s 4(4) -- is a claim deemed to have existed against the person before they died` -- a death after the
  damage is JUST FALSE for this narrow question (the "where" fails; the claim existed anyway and survives under s 4(1)) --
  NOTHING (deeming not needed).

Sites decided without a fork line: the proviso to s 4(1) and s 4(2)(a), (d), (e) are flat negatives ("shall not apply",
"shall not include"): JUST TRUE to "does the law stop ...", and s 4(2a), (3) ("does not apply") the text's no to the bar;
s 4(2)(c) and s 5(1) fail on "where" (ruling (b) of 2026-11-05); s 4(1) "after the commencement" is a scope limit
(NOTHING, ruling (c)); s 4(5) "not in derogation" is a flat negative; s 3(2) "the same legal capacity" is the text's no
to any loss of capacity.

## Rulings on negatives (copied word for word from docs/ENCODING-GUIDE.md section 5)

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## What the Act turns out to say

1. **A death on the commencement day itself falls outside both dust-disease exceptions.** s 4(2a)(a) and s 4(3)(a) both
   require the death to occur "after the day on" which the amending law comes into operation. An asbestos death on
   21 March 2002, or a silica death on 1 December 2024, leaves the s 4(2)(d) bar in place. Asserted.
2. **The exceptions turn on the dead person's own proceedings.** Both require proceedings instituted by the person before
   death and pending at death (s 4(2a)(c), s 4(3)(c)). An estate whose person died before suing, or whose proceedings had
   ended, cannot recover damages for pain and suffering, harm or shortened life, however clear the disease. Asserted.
   The two paragraphs differ in wording: asbestos injury "attributable to" the inhalation, silica injury "resulted from"
   it; "proceedings ... had been instituted by that person" against "that person had instituted proceedings". The
   encoding treats each pair as one fact; a court might not. A latent injury from another dust (coal, for example)
   meets neither exception. Asserted.
3. **s 4(5) still names a repealed Act.** The rights of dependants are those "conferred ... by the Imperial Act 9th and
   10th Victoria, Chapter 93", which note 1 of the compilation records as repealed for Western Australia by the Fatal
   Accidents Act 1959 s 2. The text was never updated to name the 1959 Act. Fork F4 reads it as reaching the dependants'
   claim that replaced it.
4. **For a cause of action that accrued before 15 November 2005, a different s 4 applies, and it is not deposited.** The
   savings provision printed in note 2 (Limitation Legislation Amendment and Repeal Act 2005 s 15(4)) keeps s 4 "as it
   was immediately before commencement day" for such causes of action. The encoding takes "commencement day" as
   15 November 2005 (the amending Act's commencement in the compilation table; the defining provision is not
   deposited) and answers NOTHING for every s 4 question about an earlier cause of action. For dust diseases with long
   latency, whose causes of action can accrue long after exposure, the accrual date matters. Asserted.
5. **The long title promises more than the Act holds.** It still speaks of "proceedings against, and contributions
   between, tortfeasors"; no section of the compilation deals with them.
6. **s 5 fixes a rate but not a method.** The present value "shall be quantified by adopting" the rate; the Act does not
   say whether it is applied as a single compound discount, an annuity, or through tables. The encoding gives the rate
   only. Whether a Governor's Order is in force could not be checked from the deposited sources; without one the rate
   is 6%. Asserted.
7. **s 4(2)(d) is barred by default and unbarred only by (2a) or (3).** The paragraph's own words ("shall not, unless
   because of subsection (2a) or (3) this paragraph does not apply, include ...") mean the exceptions lift the bar; they
   do not themselves grant damages. The question is therefore phrased "does the law stop the estate recovering ...",
   and JUST FALSE means only that this Act does not stop it.

## Before relying on it

- Deposit the Limitation Act 2005, the Fatal Accidents Act 1959 and the Civil Liability Act 2002 Part 2 Division 5, and
  link the questions that now ask "out of time", accrual and "proceedings" as facts.
- Deposit the pre-2005 s 4 (the 2002 reprint) so that causes of action accrued before 15 November 2005 get answers.
- Check whether a Governor's Order under s 5(1)(d) has ever been made.
- An independent test pass and the human gates.
