# Environment Protection and Biodiversity Conservation Act 1999 (Cth): injunctions, judicial review standing and compensation (baseline encoding)

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied. It follows the design defaults
ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

The encoding has three files:

- `epbc-claims-dates.l4`: the one period these provisions count ("the 2 years immediately before"), with the built-in
  date functions, not the daydate library.
- `epbc-claims.l4`: the rules and the 11 exported questions, each with `@export` and a `@desc` on every input.
- `epbc-claims-cases.l4`: the worked cases.

**No regulative rule.** The provisions encoded put no duty with a deadline on the person bringing the claim. The time
limits that do bind such a person are in other Acts: the ADJR Act's period for applying for review, and the limitation
period for recovering the s 500(3) debt. Neither is deposited with this Act, and neither can be imported here (see
"Before this is worth relying on"). No question takes a DEONTIC or an EVENT input.

This is the first encoding of the Act in Commons. Only the Parts a claimant meets are encoded (see Scope).

## Edition

- **The Act:** Compilation No. 70, compilation date 24 August 2026, "includes amendments: Act No. 68, 2025" (register
  id C2026C00369). Deposited at `../../registers/source-bundle/C2004A00485.txt` (retrieved 13 October 2026). Sections
  475 and 476 were amended by Act No. 68, 2025 (endnotes); the text encoded is the compiled text as amended.
- **No regulations are needed.** These provisions use no prescribed number or date.
- **Not deposited here:** the Administrative Decisions (Judicial Review) Act 1977 (its own meaning of "person
  aggrieved" and its time limits) and the Federal Court of Australia Act 1976 (Part IVA representative proceedings).
  Both have subject folders in `subjects/au/`; a cross-encoding link would go in a register, not code.

## Checks

- Stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. Commands: `l4 run epbc-claims-dates.l4`,
  `l4 run epbc-claims.l4`, `l4 run epbc-claims-cases.l4`.
- **73 assertions written, 73 satisfied, 0 errors, 0 warnings** in every file (2026-11-07).
- Every expected value was worked by hand from the text before the file was run; none was copied from the encoding's
  output. All 73 passed on the first run of the cases file.
- In a scratch copy, the s 500 amount for the first case was changed from 14000 to 14001. The run reported one error, so
  the runner catches a wrong expectation.

## Seat

**The individual who brings, or wants to bring, a claim about a contravention of the Act.** That person is:

- an Australian citizen or resident whose interests are affected by conduct that contravenes the Act, or who has been
  working for the protection or conservation of, or research into, the environment (s 475);
- a person acting on behalf of an environmental organisation or group (ss 475(1)(c), 488);
- a landholder bound by a conservation agreement whose co-party breaks it (s 476);
- a person who wants judicial review of a decision under the Act (s 487);
- a person who suffered loss or damage from a contravention (s 500).

The person asks: "Am I an interested person?", "Can I apply for an injunction?", "Can my group, or can I for it?",
"What can the court order?", "Can I enforce my conservation agreement against the other party?", "Can I seek judicial
review?", "Can I recover my loss, how much, and from whom?", "Can I rely on the earlier court finding?".

The Federal Court, the CEO, the Director of National Parks and the Minister get no seat. Their findings and decisions are
asked as facts. The person who contravenes the Act is a party the Act puts liabilities on; no seat was written for them.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed. No instrument sets a number these provisions
  use.
- **The actors the text names.** Followed: the interested person, the organisation, the person acting on behalf of an
  unincorporated organisation, the person bound by a conservation agreement, the person aggrieved, the wrongdoer and the
  affected party, the CEO, the Director, the Minister and the Federal Court.
- **Judgments handed to someone else are answered conditionally.** Followed. Each of these is an input:
  - whether conduct is "an offence or other contravention of this Act or the regulations" (ss 475, 500);
  - whether a person's or organisation's interests "have been, are or would be affected";
  - whether activities are "a series of activities" for the environment;
  - whether conduct contravenes a conservation agreement;
  - whether loss "arises from" the contravention, and which expenses were "reasonably incurred" (s 500(2));
  - for s 499(3), whether the Minister or the CEO acted "unaware of the certainty or likelihood" of damage.
- **The Act's own definitions are worked out; borrowed terms are asked.** Worked out: "interested person" (s 475(6),
  (7)), who is bound by a conservation agreement (s 307), "person aggrieved" as extended (s 487(2), (3)). Asked:
  citizenship and ordinary residence, incorporation, and "person aggrieved" in the ADJR Act's own meaning (left open).
- **One case is the text's natural unit.** Followed: one course of conduct and one application; one decision; one
  contravention and the loss from it.
- **The Act's own terms, each glossed.** Followed, in the comments and the `@desc` texts.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**

- **Part 17 Division 14 (injunctions):** s 475 (all), s 476 with s 307, s 477, s 479; s 480 by its effect (the Court's
  other powers saved).
- **Part 17 Division 14A:** s 480A(5) only by its effect: a remediation order is for the CEO or the Director to seek; the
  applicant's route to repair or mitigation is the s 475(3) order.
- **Part 17 Division 16 (review of administrative decisions):** ss 487, 488.
- **Part 18 (remedying environmental damage):** s 499(3), s 500 (all); s 501 by its effect.

**Out, and why:**

- **The rest of the Act** (Parts 1-16, the approval process, permits, listing, the rest of Part 17, Parts 19-23): the
  duties and procedures of proponents, permit holders and officials. A claimant meets them only as "a contravention",
  which is asked as a fact. Encoding the Part 3 prohibitions or the Part 9 approval process would be separate layers.
- **ss 480A-480N (remediation orders and determinations) apart from s 480A(5):** applied for or made by the CEO or the
  Director; for a claimant they are what the regulator may do, not a claim.
- **Division 15 (civil penalties, ss 481-486D) and Division 15A (ss 486DA, 486DB, undertakings):** the CEO's proceedings.
  A civil penalty finding matters to the claimant only as the s 500(5) evidence, which is encoded.
- **Division 15B (ss 486E-486J, information notices):** duties on a person the CEO believes holds information; not the
  claimant's position.
- **s 499(1), (2), (4):** the Commonwealth's own power to remedy damage, and its recovery under s 500 (the note to
  s 500(2)). The Commonwealth gets no seat.
- **Representative (class) proceedings:** the Act has no class action provision. A group claim under s 475 or s 500 runs
  under Part IVA of the Federal Court of Australia Act 1976 or a State court's rules, which are not encoded here.
- **The ADJR Act's own standing test and time limits:** not in this Act; s 487 answers NOTHING-kind where its extension
  fails.

## Rulings on negatives (2026-11-04 and 2026-11-05), as applied

Answers are marked "(the text's no)" or "NOTHING-kind". The ruling of 2026-10-29, as the guide copies it from section 2
of `docs/design-question-false-or-nothing.md`: a function answers `JUST FALSE` only where the text itself says no to the
case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or
"unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative
("does not", "shall not", "may not"). Everywhere else it answers `NOTHING`: where the text lists without closing the
list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition
in its own wording and the case falls outside the limit.

Rulings N2 (flat negatives count as a no), the periods ruling ((a) a period the text fixes: outside it, `JUST FALSE`;
(b) a "where" condition that fails: `JUST FALSE`; (c) a scope limit with no "only": `NOTHING`) and the case-by-case
ruling of 2026-11-05 are applied site by site below.

| Site | Function | Answer taken | Other reading |
|---|---|---|---|
| s 475(6) "an individual is an interested person if" | `s 475(6) -- am I an interested person` | text's no when it fails (an "if" definition, closed by s 528) | none likely |
| s 475(7) "an organisation ... is an interested person if" | `s 475(7) -- can my organisation apply for an injunction` | text's no | none likely |
| s 475(1) opening "If a person has engaged ... [in a contravention]" | `s 475(1) ...`, `s 475(7) ...`, `ss 475, 479 ...` | text's no when there is no contravention | NOTHING (the Court's other powers, s 480) |
| s 475(1) list of applicants, not closed with "only" | `s 475(1) -- can I apply for an injunction` | NOTHING-kind for a non-interested person | text's no (the list as exhaustive) |
| s 476(1) applicants | `s 476 -- ...` | NOTHING-kind for a person not bound | text's no |
| s 476(1) "If a person bound ..." | `s 476 -- ...` | text's no when the actor is not bound or there is no contravention | none likely |
| s 487(1) "extends (and does not limit)" | `s 487(2) ...`, `ss 487(3), 488 ...` | NOTHING-kind when s 487 fails | none: the text says it does not limit |
| s 500(7) "This section does not apply" | `s 500 -- can I recover my loss` | text's no (flat negative) | none likely |
| s 500(1) no contravention, or loss not arising | `s 500 -- can I recover my loss` | NOTHING-kind (fork F6) | text's no |
| s 500(5) no earlier finding | `s 500(5) ...` | NOTHING-kind (silent) | none likely |

## Forks

- **F1. The 2 years "immediately before".** The window is read as running from the same day of the month 2 years
  earlier, that day included, up to and including the day of the conduct, application or decision. An activity on the
  day of the conduct counts; an activity after it does not. Another reading excludes the anniversary day, or the end day.
- **F2. 29 February.** Two years before 29 February 2028 is read as 28 February 2026.
- **F3. Continuing conduct.** For conduct that continues, the person gives the day of it they rely on. Another reading
  ties the 2 years to the day the conduct began.
- **F4. Past conduct under s 476.** s 476(1) speaks of a person bound who "engages or proposes to engage" in the conduct;
  s 476(2) and (4) also reach one who "has engaged" or "has refused or failed". Conduct that has wholly stopped is read
  as outside (1) and answered NOTHING-kind. Another reading takes (1)'s "engages" to include past engagement, as s 475(1)
  expressly does ("has engaged, engages or proposes to engage").
- **F5. s 475(7)(b), (c): objects and activities together.** (i) and (ii) are read as holding at the same time, at some
  time in the 2 years; the person gives the last day the organisation carried on its activities while its objects
  included the environment. Another reading lets (i) and (ii) hold at different times within the 2 years.
- **F6. s 500 without a contravention or without a causal link.** Answered NOTHING-kind (a scope limit with no "only";
  s 501 saves other rights). Another reading answers the text's no.
- **F7. s 499(3) and the loss.** s 499(3) deems the environmental damage or condition to arise from the s 489
  contravention. The person's own loss must still arise from that damage or condition; that link is an input.

## What the Act turns out to say

1. **The Act has no class action machinery.** Claims by many affected people (for example under s 500) must be brought
   as representative proceedings under other law. s 500(4) makes several wrongdoers jointly and severally liable, and
   s 500(5) lets a court's earlier finding of contravention be used as evidence, which is what such a group claim would
   lean on. Asserted.
2. **s 475(6)(b) does not require the environmental activities to be in Australia; s 487(2)(b) does** ("in Australia or
   an external Territory"). A citizen whose conservation work was all overseas can be an interested person for an
   injunction but is not taken to be a person aggrieved for judicial review. Asserted (the overseas case in s 487(2)).
3. **s 476(1) omits past conduct** that s 476(2), (4) and s 475(1) include (fork F4). Possibly a drafting gap: the
   s 475(1) words "has engaged" were not carried into s 476(1). Asserted as NOTHING-kind.
4. **The organisation tests differ.** s 475(7) asks for environmental objects "at any time during the 2 years" and also
   lets an organisation in through affected interests; s 487(3)(c) asks for environmental objects "at the time of the
   decision" and has no interests limb (the ADJR Act's own meaning covers it). An organisation that adopted
   environmental objects after a decision qualifies for neither under (b)/(c). Asserted for s 487(3).
5. **The 2-year window for proposed conduct runs back from the application, not the conduct** (s 475(6)(b)(ii),
   (7)(c)), so the same last activity can qualify a person for proposed conduct and not for conduct already done, or the
   reverse. Asserted.
6. **s 499(3)(c) is narrower than (b).** (b) speaks of damage to "the environment or to a matter protected by a provision
   of Part 3"; (c) requires that the action "results in damage to the environment or gives rise to a condition relating
   to the environment", without the Part 3 matter. Damage only to a Part 3 matter is not within (c) on its words. Not
   asserted separately (folded into one input).
7. **s 500(7) excludes decisions purportedly under the Act**, so loss from an unlawful approval is not recoverable from
   the decision-maker under s 500; s 499(3) instead deems the damage to arise from the proponent's false information.
   Asserted.
8. **No undertaking as to damages provision.** The former s 478 was repealed by Act No. 165, 2006 (endnotes). Whether an
   applicant must give the usual undertaking is left to the Federal Court's practice; not encoded.
9. **A remediation order (s 480A) is not open to a private applicant**; s 480A(5) names "the CEO personally" or the
   Director. A private applicant's route to repair or mitigation is the s 475(3) order made with a prohibitory injunction.
   Stated in the answer text.

## Before this is worth relying on

- A lawyer's review of forks F1-F7, especially F4 (s 476 past conduct) and F1 (the window's ends).
- The ADJR Act's own "person aggrieved" test and time limits, and the limitation period for the s 500(3) debt, encoded in
  their own subjects and linked from here.
- Part 3 (the matters of national environmental significance) encoded, so that "a contravention" can be worked out
  rather than asked.
- A seat for the person against whom an injunction or s 500 claim is brought, drawing on the same rules.
- An independent test pass.
