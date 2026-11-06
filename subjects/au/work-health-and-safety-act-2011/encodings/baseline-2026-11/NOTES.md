# Work Health and Safety Act 2011 (Cth) -- baseline encoding, the claimant

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

The focus asked for is **the provisions a person bringing or answering a claim meets**. The Act gives an individual one
civil claim of its own (Part 6, s 112) and says so (s 267); the rest of what a claimant meets is machinery around a
death, injury or dangerous incident: asking for a prosecution and the time to bring one (ss 231, 232), review of an
inspector's or Comcare's decision (Part 12), compensation for an inspector's use of power (s 184), void contract terms
(s 272) and charging workers for safety (s 273). Part 6 and Part 12 are encoded whole, less the exceptions under Scope.

**This encoding is a new layer beside `../baseline-2026-10/`, which is untouched.** That encoding (worker and PCBU seats,
the duties, notifiable incidents, stopping unsafe work, the Regulations and indexed penalties) already answers the
short form of ss 104 to 106, 112, 113(1) and 115(a) in its worker seat. This folder encodes Part 6 whole, with coercion,
misrepresentation, the orders, the presumptions, the defence and the criminal side. The stable `l4` resolves IMPORT only
within a folder, so nothing here imports the older modules and nothing is restated from them by editing; where both
answer the same facts (a dismissal for raising safety, inside a year, with no other claim) they agree.

Files: the rules in `whs-claims-rules.l4` (the only module that imports `daydate`), the questions in
`whs-claims-seat.l4` (imports the rules, restates none), the cases in `whs-claims-cases.l4`.

## Edition

Compilation No. 16, compilation date 1 July 2024, includes amendments up to Act No. 120, 2023 (register id
**C2024C00243**, Federal Register of Legislation, retrieved 13 October 2026), as deposited at
`../../registers/source-bundle/C2011A00137.txt`. Schedule 4's tier A and tier F amounts are the printed figures, before
the annual indexation of cl 4 (`../baseline-2026-10/whs-penalty-indexation.l4` indexes them; it cannot be imported here).
No regulation sets a number these provisions use, except item 13 of the s 223 table (decisions the Regulations make
reviewable) and the courts a regulation may add under s 273A(1)(d), both left out; the Work Health and Safety
Regulations 2011 are deposited at `subjects/au/work-health-and-safety-regulations-2011/` but were not needed.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read;
two deliberately wrong assertions were run once in a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `whs-claims-rules.l4` | 0 | 0 | 0 | 0 |
| `whs-claims-seat.l4` (26 questions) | 0 | 0 | 0 | 0 |
| `whs-claims-cases.l4` | 0 | 0 | 140 | 140 |

Every expected value was worked by hand from the text before the run. Every exported question has cases, with the
edges: each limb and each defeater of ss 108 and 109; s 106(h) inside and outside its list; the last day and the day
after under s 113(1) and s 231(1B), at a month end and from 29 February; the s 231(2) duty answered on the last day and
the day after, and not answered as at either; each period of s 232 winning in turn, industrial manslaughter, and the
fresh-evidence exception for Category 1 and not Category 2; each eligible-person head of s 223 and a person outside it;
the improvement notice's compliance period under, over and at 14 days; s 226 with and without a request for
information, answered and not, and a request giving fewer than 7 days; each branch of s 228, and Comcare's own decisions
(items 5, 6, 12), which s 228 does not reach; each period of s 229(2); for s 104, each element, with and without the
s 110(1) case.

## Seat

**The claimant** (`whs-claims-seat.l4`): the individual the law is applied to, asking in their own words. In Part 6, the
worker, prospective worker or other person (in a commercial arrangement) who was dismissed, disadvantaged, pressured or
misled for a safety reason: "Is what was done to me discriminatory conduct?", "Was it done for a prohibited reason?",
"Was I coerced or induced?", "Was I misled about my rights?", "Can I start a court proceeding?", "By what day must I
start?", "What orders can the court make for me?", "What orders can a criminal court make for me?", "Can they be
convicted for discriminating against me?", "What is the most they can be fined for it?". After a death, serious injury
or dangerous incident, the injured worker or a family member: "May I ask for a prosecution?", "Between which days may I
ask?", "By what day must Comcare answer me?", "Is Comcare late in answering me?", "By what day must Comcare refer my
matter?", "Until when can they be prosecuted?". The worker affected by a notice or decision: "Can I have the decision
reviewed?", "By what day must I ask for internal review?", "When is the decision taken to be confirmed?", "Is the
decision on hold during review?", "By what day must I go to the Fair Work Commission?". And: "Can I get compensation for
what an inspector did?", "Does the Act give me a right to sue?", "Is the contract term void?", "Did the business break
the rule against charging me for safety?", "What is the most the business can be fined for charging me?".

No seat for Comcare, an inspector, the Director of Public Prosecutions, the Fair Work Commission or a court; their duties
appear as what the person is owed and by when (s 231(2) as a regulative rule on Comcare). No seat for the person
accused of discriminating or for the business: the PCBU seat in `../baseline-2026-10/` covers the business's duties.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. Schedule 4's printed amounts; no regulation
  sets a number used here.
- **The actors the text names.** Followed: the worker and prospective worker, the person in a commercial arrangement,
  the person conducting a business or undertaking, the eligible person and their representative, Comcare (the
  regulator, s 4), inspectors, the internal reviewer, the Director of Public Prosecutions, the Fair Work Commission, the
  court.
- **Judgments answered conditionally.** Followed: "reasonably considers" (s 231), "reasonable in the circumstances"
  (s 113(3)), "would not be expected to rely on it" (s 109(2)), "a reasonable direction" (s 108(3)), "just" (s 184(3)),
  the court's satisfaction about fresh evidence (s 232(2)), and the burdens the Act puts on the other side (ss 110(2),
  113(2), (3)) are inputs, worded "has the other side proved" where the burden is theirs.
- **The Act's definitions worked out; borrowed terms asked.** Followed: discriminatory conduct (s 105), prohibited
  reason (s 106), eligible person (s 112(6)), reviewable decision and eligible person (s 223), prescribed time
  (s 224(3)) are worked out; "employee", "commercial arrangement", "official inquiry" (glossed in the input), "WHS
  undertaking" and "workers' compensation" are asked.
- **One case.** One course of conduct against one person; one offence; one decision.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** Part 6 whole: ss 104 (with (2) and (3)), 105, 106, 107 (as s 112(2)(b) and the tier A penalty), 108, 109, 110, 111, 112,
113, 114, 115; s 184; Part 12: s 223 (items 1 to 12), 224, 226, 228, 229(1), (2); Part 13: ss 231(1), (1A), (1B), (2)(a),
(3)(b), 232, 267; Part 14: ss 272, 273, and 273A(1) (named in the answer); Schedule 4 cl 2 items 1 and 6 (tier A and
tier F, before indexation).

**Regulative rules:** two. s 231(2) as Comcare's obligation (`MUST ... WITHIN ... LEST BREACH ... BECAUSE`), counted in
days to the day 3 months after it receives the request, run by EVALTRACE inside "Is Comcare late in answering me?"; and
s 273 as a prohibition (`SHANT`) on the business, run by EVALTRACE inside "Did the business break the rule against
charging me for safety?". Both questions take only plain facts.

**Out, and why:**
- s 107(2) (fault element under the Criminal Code): the s 107 offence is not asked as a question; its conviction is an
  input to the s 111 orders. (s 104(3)'s intention is an input to "Can they be convicted for discriminating against
  me?", and so is the prosecution's s 110(1) case, which raises the presumption.)
- s 113(4), 110(3) (legal burden): reflected in the "has the other side proved" wording.
- s 223 item 13 (decisions the Regulations make reviewable): answers "not answered here".
- s 225, 227 (who reviews, written reasons), 228(6) (how long a stay lasts), 229(3) (what the Commission may do):
  machinery or the tribunal's powers; the person's questions are the ones above.
- s 231(2)(b), (2A), (4) to (7) (advising the accused, three-monthly updates, the DPP's advice and notices): duties
  owed to the person, but with no date the person can check except (2A)'s "at least every 3 months", which needs the
  advice day; left for a later layer.
- s 230 (who may prosecute) and s 233 (charging multiple contraventions): not met by the claimant.
- Part 13 Division 2 (ss 234 to 242, the court's sentencing orders: adverse publicity, restoration, project and training
  orders, court-ordered undertakings, injunctions; the Part 6 sentencing order, s 111, is in Part 6 Division 2 and is
  in): orders made in the prosecution, not claims the person brings. Division 7 (civil penalty proceedings, only by
  Comcare or an inspector, s 260): not open to the claimant; s 267 says so in "Does the Act give me a right to sue?".
- Part 13 Division 3 (s 243, infringement notices), Division 4 (s 244, offences by bodies corporate: who is liable for
  the offence), Division 5 (ss 245 to 248, the Commonwealth as a duty holder) and Division 6 (ss 249 to 253, public
  authorities): who is prosecuted and how, not a claim, time or step the claimant meets.
- ss 182, 183 (inspector's notice of damage): the s 184 claim is in; the notice is a duty without a period.
- s 272A, 272B (no insurance against penalties): duties on the duty holder and insurer, not a claim.
- Part 7 (entry permits, and its civil penalty provisions): the union's and the business's, not the individual's.
- The rest of `../baseline-2026-10/`'s scope (duties, consultation, ceasing work, notifiable incidents, penalties of
  Schedule 4 cl 1, the Regulations, indexation): not repeated here. The overlap on ss 105, 106, 112, 113(1) and 115(a) is
  deliberate: Part 6 is encoded whole here (see Method), and the two agree on the same facts.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule.

How they fall here:
- `JUST FALSE`: s 105 and s 106 ("engages in discriminatory conduct if", "for a prohibited reason if"); s 104(2) ("only
  if"); s 108 and s 109 (flat negatives, with closed lists of what they are about; s 109(2) "does not apply if"); s 231
  ("applies if", "may only be made"); s 223 (the table closes who is eligible); s 184(1) ("if"), (3) ("only if"); s 267
  ("nothing in this Act is to be construed as conferring").
- `NOTHING`: s 223 for a decision outside items 1 to 12; s 231(3)(b) when its "if" fails (no day to give); s 272 for a
  term that neither excludes, limits, modifies nor transfers (the section is silent).

### Forks

- **F1** s 105(2), `s 105 -- it is discriminatory conduct`: organising or threatening is folded into each head; other
  reading: none, the answer is the same.
- **F2** s 106(h), `s 106 -- it was for a prohibited reason`: raising a concern only with someone outside (h)(i) to
  (viii), such as the media, answers JUST FALSE for (h); other reading: it may fall under (j) ("taking action ... to seek
  compliance"), which the person would choose instead.
- **F3** ss 112, 113(1), 115, `ss 112, 113(1), 115(a), (c) -- whether I can start`: the first failing condition is
  reported, in the order reach, eligibility, time, other claims; other reading: report every bar.
- **F4** "1 year after", "6 months after", "3 months after", "1 month of" (ss 113(1), 231, 232), `months after` and
  `years after`: a day that does not exist in the later month is taken as that month's last day (29 February 2024 + 1
  year = 28 February 2025; 31 August + 6 months = 28 February); other reading: roll forward to 1 March.
- **F5** s 231(1B)(b), `s 231(1B) -- the window`: "within 6 months after the report is made" is read to include the day
  of the report; other reading: from the next day.
- **F6** s 224(3)(a), `s 224 -- the last day to apply for internal review`: the improvement notice states a day
  (s 192(1)(d)), not a period; the compliance period is read as the days from issue to that day, then compared with 14
  and counted from the day the notice came to the person's notice; other reading: the earlier of the compliance day and
  14 days after the notice came to the person's notice.
- **F7** s 226(4), `s 226 -- the day the decision is taken to be confirmed`: a request giving fewer than 7 days is read
  as giving 7; other reading: the request is defective and the 14-day period never stopped.
- **F8** s 229(2)(c), `s 229(2) -- the last day to apply to the Fair Work Commission`: when the Commission requires
  reasons, (c)'s 14 days after the statement replace (a) or (b); other reading: whichever of the periods ends later.
- **F9** s 228(1), (2), `s 228 -- the decision is stayed`: for a prohibition or non-disturbance notice with no stay
  granted or deemed, JUST FALSE ("other than" read as excluding the automatic stay); other reading: NOTHING. For
  Comcare's own decisions (items 5, 6, 12), which have no internal review (s 224(1)), and a decision outside the table,
  NOTHING: s 228 speaks only of "an application for an internal review".
- **F10** s 273, `s 273 -- the business must not charge me for safety`: the prohibition has no period; `WITHIN 1` stands
  for the one period the question asks about, so a trace with no charge ends FULFILLED.
- **F11** s 231(2), `s 231(2) -- the duty was kept, or can still be`: "late" is computed as "an answer on the day asked
  about would not keep the duty"; the deadline day itself is in time.
- **F12** s 267, `s 267 -- the Act gives me a right of action`: Part 7 and Division 7 are excepted from s 267, but
  Division 7 proceedings may be brought only by Comcare or an inspector (s 260), so for the individual the answer is JUST
  FALSE; other reading: NOTHING for Part 7 (s 267 does not itself say no for the excepted Parts).
- **F13** s 112(3), (4), s 113(3), s 114(3), `s 112(3) -- the orders the court may make`: once the other side proves the
  reason was not substantial, or proves the defence, or a s 111 order was made, no s 112 order is listed, not even
  "any other order" under (3)(d); other reading: (3)(d) and s 112(5) leave the court other orders.
- **F14** s 115(b), same function: received compensation removes only the compensation order, and the proceeding and
  the other orders remain; other reading: none, (b) speaks only of recovering compensation.
- **F15** s 232(1)(c), `s 232 -- how long they can be prosecuted`: the three events of (c) are given as one day, the
  latest; other reading: none, "within 6 months after" each, and the latest period wins.

## What the Act turns out to say

1. **Misrepresentation gives no civil claim.** s 112(2) reaches discriminatory conduct (a), procuring it (b) and s 108
   coercion (c), but not s 109. A worker misled about their rights can only report it; it is a tier A offence.
   Asserted.
2. **Coercion gets a thinner remedy than discrimination.** For s 108, s 112(3) allows an injunction or "any other order"
   but not compensation ((3)(b) is limited to (2)(a) and (b)) or reinstatement ((3)(c) to (2)(a)); and neither the
   presumption (s 113(2)) nor the defence (s 113(3)) applies to it. Asserted.
3. **Two thresholds for the same reason.** The civil claim needs the safety reason to be "a substantial reason"
   (s 112(4)); the offence needs it to be "the dominant reason" (s 104(2)). Both are presumed, and the other side must
   disprove them on the balance of probabilities (ss 110(2), 113(2)). Asserted.
4. **Reinstatement against the person who did it only.** s 112(3)(c) is for (2)(a) conduct, so a person who procured
   the dismissal (2)(b) can be ordered to pay compensation but not to reinstate. Asserted.
5. **Civil and criminal compensation exclude each other, but not the prosecution.** A s 112 order bars a s 111 order for
   the same conduct (s 114(2)) and the reverse (s 114(3)), yet a prosecution may follow a civil order (s 114(1)).
   Asserted (the bars).
6. **Losing a workers' compensation claim does not bar the Part 6 claim; losing any other claim does** (s 115(c)), and
   a live claim elsewhere bars starting one (s 115(a)). Compensation received elsewhere bars only compensation
   (s 115(b)). Asserted.
7. **The Act gives no right to sue for an injury.** s 267 says nothing in the Act confers a civil right of action for a
   contravention, except in Part 6, Part 7 and Division 7 of Part 13; Division 7 proceedings may be brought only by
   Comcare or an inspector (s 260). An injured worker's claim lies in negligence or workers' compensation, outside this
   Act. Asserted.
8. **A request for a prosecution cannot be made early, and the window is measured from a different day than the
   limitation period.** s 231(1B)(a) opens 6 months after the act and closes 18 months after it; s 232(1)(a) runs 2 years
   from when the offence first came to Comcare's notice. If Comcare learns of it late, the limitation period can outlast
   the request window; if it learned of it on the day it happened, a request made at 18 months leaves 6 months before
   the limitation period ends (s 231(2) gives Comcare 3 of them to answer). Asserted (each
   window's edges).
9. **Category 3 offences cannot be the subject of a request** (s 231(1)); industrial manslaughter has no time limit
   (s 232(2A)); a Category 1 offence can be prosecuted late on fresh evidence (s 232(2)), but not Category 2. Asserted.
10. **The internal review can be confirmed earlier than 14 days.** If the reviewer asks for information and the person
    does not answer in time, the decision "is taken to have been confirmed ... at the end of that time" (s 226(5)),
    which can fall before the 14 days would have ended. Asserted (22 March against 24 March).
11. **A forfeiture notice and the review section count from different days.** s 179(6)(b) requires the notice to say
    the person "may apply within 28 days after the date of the notice"; s 229(2)(a) allows 28 days "after the day on
    which the decision first came to the applicant's notice". s 179(6)(d) also promises a stay on review, but forfeiture
    is Comcare's own decision and goes straight to the Fair Work Commission (s 229(1)(a)), and the only stay provision is
    s 228, for internal review. Not asserted (a drafting finding); the encoding follows s 229.
12. **The improvement notice states a day, but s 224(3)(a) speaks of a period.** See fork F6. Asserted on the reading
    taken.
13. **A worker cannot seek review of an inspector's decision on HSR training** (s 223 item 2 lists only the PCBU and "A
    health and safety representative whose interests are affected by the decision", the representative's own
    interests, not those of the workers it represents, as items 1, 3, 4 and 7 to 12 word it), nor of a forfeiture or
    return decision unless entitled to the thing (items 5, 6). Item 1 alone adds the worker's representative appointed
    for the s 52(1)(b) negotiations. Asserted.

## What would need doing before this is worth relying on

- An independent test pass, and a lawyer's look at the forks, especially F4 (month ends), F6 and F12.
- The indexed tier A and tier F amounts for the year asked (cl 4), and the CPI numbers; the printed figures are not the
  ones in force from 1 July 2024.
- s 231(2A) updates and s 231(4) to (6), and s 228(6)'s end of a stay, if a case asks.
- s 223 item 13 from the Regulations, if any regulation makes a decision reviewable.
- The common-law and workers' compensation claims an injured worker actually brings are in other Acts (the Safety,
  Rehabilitation and Compensation Act 1988 for Commonwealth workers) and are not here.
- Wider sources: no Comcare guidance, Fair Work Commission or court decision was read.
