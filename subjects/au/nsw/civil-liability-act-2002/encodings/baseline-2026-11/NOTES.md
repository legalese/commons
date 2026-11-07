# Civil Liability Act 2002 (NSW) -- baseline encoding, the injured person and the person abused as a child

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 16 June 2022). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05. In short, as section 5 of the encoding guide
puts it: "a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means"
definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as
"while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may
not")." Everywhere else the answer is `NOTHING`, with a `NOTHING-kind` comment. Judgments the Act leaves to the court
("if the court is satisfied", "just and reasonable", "reasonable precautions") are asked as the court's finding, with
"the court has not decided" leaving the answer open.

Most questions about a bar are asked as "Does section X stop me ...?": `JUST TRUE` means the bar holds, `JUST FALSE`
that this section does not bar the claim on these facts (it never means the claim succeeds).

One regulative rule (s 6N(4), the organisation's 28-day duty to identify its associated trusts) is run by `EVALTRACE`
inside an exported question that takes only plain facts and dates. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in
`LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Civil Liability Act 2002 No 22, corpus document `nsw_legislation:2022-06-16/act-2002-022` (in force 16 June
  2022), deposited at `../../registers/source-bundle/act-2002-022.txt` (text sha256 ce6d10ec...6bd04 as recorded in its
  `.meta.json`), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited, so asked as inputs:** the commencement dates of ss 6F and 6H and of Part 1B (Civil Liability
  Amendment (Organisational Child Abuse Liability) Act 2018) and of s 6A of the Limitation Act 1969; the Minister's s 17
  orders indexing the s 16 maximum (the maximum in force is an input; $350,000 is the s 16(2) figure, and the indexed
  figure is much higher); the Australian Statistician's average weekly earnings (ss 12, 15, 15A, 15B); any regulation
  under ss 3B(3), 6E(1)(c), 6F(4)(h), 6G(4), 12(3)(b), 14(2)(a), 15(4)(b), 18(3)(a); the minimum superannuation
  guarantee percentage (s 15C, Commonwealth law). The case files use illustrative dates and figures, said to be such.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Exported questions | Assertions written | Satisfied |
|---|---|---|---|---|---|
| `cla-core.l4` | 0 | 0 | 1 | 0 | 0 |
| `cla-child-abuse.l4` | 0 | 0 | 16 | 0 | 0 |
| `cla-damages.l4` | 0 | 0 | 12 | 0 | 0 |
| `cla-liability.l4` | 0 | 0 | 9 | 0 | 0 |
| `cla-cases-child-abuse.l4` | 0 | 0 | 0 | 119 | 119 |
| `cla-cases-damages.l4` (s 3B and Part 2) | 0 | 0 | 0 | 132 | 132 |
| `cla-cases-liability.l4` | 0 | 0 | 0 | 89 | 89 |

Every expected value was worked by hand from the text, with the edges: age 17 and 18 (s 6A); abuse on the commencement
day and the day before (Sch 1 cll 43, 44); the 120th and 121st day after service (s 6N(1)), across months; the 28th and
29th day after an application, across 29 February (s 6N(4)); an agreement made on the day s 6A or Part 1B commenced and
the day before (s 7C); 5 and 6 hours a week, 5 and 6 months (ss 15, 15B); 39 and 40 hours (s 15(4), (5)); earnings at
and just over three times average weekly earnings (s 12); severity 14%, 15%, every changing step of the Table, 33%, 34%,
100%, a fraction, over 100% (s 16), with amounts that land on $250 and $750 (rounded up) and others rounded down;
$100,000 and $100,001 of future loss (s 23); a 5-month and a 6-month maximum prison term (ss 54, 54A); each s 3B
category against the provisions it keeps and drops (Part 1C included, through s 7C); a failed condition meeting an open
one; each of the court's s 54(1) findings left undecided.

## Seat

**The individual claimant**: the injured person bringing a claim for personal injury damages (Parts 1A, 2, 3, 6, 7),
and, for Parts 1B and 1C, the person who was abused as a child, suing an organisation or seeking to set aside an earlier
settlement. Every exported question is one that person would ask ("Did the organisation owe me the duty, and is it
presumed to have breached it?", "Can I sue the unincorporated organisation in its own name?", "How much can I get for
pain and suffering?", "Does section 50 cut my damages because I was drunk?"). The court, the organisation, its trustees,
insurers and the Minister get no seat; what the Act lets them do is encoded as what it means for the claimant. No second
seat is written: the defendant meets the same rules from the other side, and a defendant seat can be layered on these
modules later.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; none of those instruments is deposited, so
  their figures and dates are inputs (see Edition).
- **The actors the text names.** Followed: the claimant (plaintiff, applicant), the defendant, the organisation, its
  management members, proper defendants and trustees, the court, the victim (Part 3).
- **Judgments answered conditionally.** Followed: reasonable precautions (s 6F), the occasion supplied by the role
  (s 6H), just and reasonable (ss 7C(1)(c), 7D), the court's satisfaction (ss 15, 15B, 50, 54(1)), what the claimant's
  conduct was "on the balance of probabilities" and whether it contributed materially (ss 54(1), 54A(1)), reasonable
  response (s 52) are the court's findings, with "not decided" answering `NOTHING` or a "not settled" value.
- **The Act's definitions worked out; borrowed terms asked.** Followed: child, organisation, responsible, associated,
  akin to an employee, child abuse, associated trust, suitable proper defendant, affected agreement, close member of the
  family, serious offence, intoxicated, dangerous recreational activity are worked out; "recognised psychiatric
  illness", "obvious" (a reasonable-person test), "employee", "public sector body" membership, the s 6A Limitation Act
  cause of action are asked.
- **One case.** One claim by one claimant against one defendant (one act of abuse for the Part 1B timing questions).
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

The Act is large (Parts 1 to 12, with Part 2A on offenders in custody alone running to some 300 lines). The focus is Part
1B; around it are encoded the gateway (s 3B) and the provisions a personal injury claimant meets most.

**In:**

- s 3B (which provisions apply to which kind of claim) with s 3B(2) (motor accidents): `cla-core.l4`.
- **Part 1B**, every provision with a question for the claimant: s 6A (definitions), s 6C (successor organisations),
  ss 6D-6E (responsibility, association), s 6F (duty and reverse onus) with Sch 1 cl 43, ss 6G-6H (vicarious liability)
  with Sch 1 cl 44, and in Division 4 (unincorporated organisations and proper defendants, with Sch 1 cl 45) ss 6J,
  6K(1), 6L, 6M, 6N, 6O and 6P(2), (6): `cla-child-abuse.l4`. The rest of Part 1B is out, listed below.
- **Part 1C, whole** (ss 7A-7F, setting aside child abuse settlements), gated by s 3B (finding 2): `cla-child-abuse.l4`.
- **Part 2** (personal injury damages): ss 11, 11A (by way of the s 3B gate), 12 (earnings cap), 14 (discount rate),
  15, 15A (gratuitous attendant care: threshold and caps), 15B (lost capacity to provide domestic services: threshold,
  s 15B(6) and cap), 15C (superannuation cap), 16 with s 17(3) (non-economic loss: threshold, Table, rounding), 18(1)
  (no interest), 21 (no exemplary damages in negligence), 23 and 25 (structured settlements): `cla-damages.l4`.
- **Part 1A** ss 5F, 5H, 5I (obvious and inherent risks) and ss 5J-5L (dangerous recreational activities); **Part 3**
  ss 27, 28, 30, 31, 33 (mental harm); **Part 6** ss 47, 48, 50 (intoxication); **Part 7 Division 1** ss 51-54A (self-defence,
  criminals): `cla-liability.l4`.

**Out, and why:**

- ss 1, 2, 4 (name, commencement, Crown, regulations, notes), s 3A (contracting out: no question for the claimant
  alone), s 3C (folded into fork F1), s 6I (objects), s 6Q (rules of court), s 6K(2)-(4) (management members may exercise the
  organisation's functions; the court's orders and directions for Division 4: addressed to the organisation and the
  court, and a discretion), s 6P(1), (3)-(5) (trustees' powers and indemnity, Corporations Act displacement):
  machinery or addressed to others with no question for the claimant.
- s 6B(1) (nothing in s 5Q, Part 2A or Part 5 protects against or limits Part 1B liability): none of s 5Q, Part 2A or
  Part 5 is encoded here, so there is nothing in these modules for it to switch off; a later layer that encodes any of
  them must carve Part 1B liability out.
- s 6B(2) (an award under Division 2 or 3 must take into account an award under the other): a direction about
  assessment, not a computable rule; noted.
- Part 1A s 5G (the presumption that the injured person was aware of an obvious risk): a rule of proof that matters to
  a defence of voluntary assumption of risk, which this baseline does not encode; no encoded question turns on
  awareness (s 5L(2) says it does not matter). Part 1A ss 5B-5E (breach and causation: judgments left wholly to the court), s 5M (risk warnings, 11 subsections),
  s 5N (contract waivers for recreation services), ss 5O-5P (professional standard of care: peer opinion is a judgment),
  s 5Q, ss 5R-5T (contributory negligence: the court's percentage; s 5S allows 100%): not encoded in this baseline; s 5M
  is the first candidate for a later layer.
- Part 2: s 13 (the court's assumptions), s 15B(3), (7)-(11) (assisted-care disregard is folded into the inputs; Lifetime
  Care, Motor Accidents Compensation Act and s 15 overlaps out), s 17 (the indexation mechanism: the result is an input),
  s 17A, s 18(2)-(5) (the interest rate: regulations and Reserve Bank rate not deposited), s 19 (contribution between
  defendants), ss 22, 24, 26.
- Part 2A (offenders in custody) and Part 7 Division 2: separate claimant groups with their own machinery; a later
  encoding.
- Part 3 s 32 (duty of care for mental harm: a foreseeability judgment), s 29 (no question beyond "shock is no bar").
- Part 4 (proportionate liability: claims for economic loss or property damage, not personal injury), Part 5 (public
  authorities: resources and policy judgments), Parts 8, 8A, 9, 10, 11, 12, s 49 (duty and standard of care: no
  computable rule), Schedules 1 (except cll 43-45) and 2.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3B(1)(a) "civil liability of a person in respect of an intentional act that is done by the person", with
  s 3C -- `Does this part of the Act apply to my claim` and every gated question -- for liability for someone else's
  intentional or sexual act (vicarious liability), the answer is settled where (a) would make no difference and
  `NOTHING` where it would -- (a) reaches only the doer's own liability, so the whole Act applies to the organisation;
  or s 3C carries the exclusion to the vicariously liable person.
- **F2** Sch 1 cll 43, 44 "perpetrated after the commencement of that section" -- `What does section 6F mean for my
  claim`, `Is the organisation vicariously liable under section 6H` -- abuse on the commencement day counts as after it
  -- the commencement day is excluded.
- **F3** s 6L(3) "the State is taken to be appointed as the proper defendant" -- `Can I apply for the trustees to be
  appointed` -- for a public sector body the answer is no, the State being taken as a suitable proper defendant -- s 6N
  still applies if the State is not "suitable" under s 6M.
- **F4** s 6N(1)(a) "by the end of 120 days after ... served" -- `By when must a proper defendant be appointed`, `Can I
  apply for the trustees to be appointed` -- the day of service is day 0, an appointment on day 120 is in time, and the
  earliest application is day 121 -- the period ends at the start of day 120.
- **F5** s 16(3) Table, whole percentages, "34%-100% respectively" -- `How much for non-economic loss` -- a severity that
  is not a whole percentage is not settled -- interpolate between the Table's lines, or round the severity.
- **F6** s 23(2) "exceeding $100,000", s 25 "a plaintiff who proposes to negotiate" (a duty whose condition is unmet) --
  `Must the court tell us the proposed award first`, `Must my lawyer advise me about structured settlements` --
  `JUST FALSE` (this section does not require it) -- `NOTHING`.
- **F7** s 6K for an incorporated organisation (a scope limit with no "only") -- `Can I sue the unincorporated
  organisation in its own name` -- `NOTHING` -- `JUST FALSE`.
- **F8** s 7F(3) where nothing has been set aside -- `Must I repay what I received under the settlement` -- `NOTHING`
  (the section is silent) -- `JUST TRUE` (the agreement stands, so its terms govern).
- **F9** s 50(5) "where the court is satisfied that the intoxication was not self-induced", undecided -- `What does
  section 50 do to my claim` -- not settled -- s 50 applies until the court is so satisfied.
- **F10** "unless" bars once met (ss 15(2), (3), 30(2), 31, 33, 15B(2)) -- the "Does section X stop ..." questions --
  `JUST FALSE` (this section does not bar the claim) -- `NOTHING` (the bar lifted grants nothing).
- **F11** s 6N(4) "within 28 days after the application is made" -- `By when must the organisation identify its trusts`,
  `Has the organisation identified its trusts in time` -- day of application is day 0, the 28th day is the last (an
  identification on it is in time) -- the 28th day is excluded.
- **F12** s 21 where the cause was not negligence, and every claim outside Part 2 -- `Can I get exemplary or aggravated
  damages` -- `NOTHING` (the Act is silent) -- `JUST TRUE`.
- **F13** s 6F where the abuser's association is open (s 6E "without limitation includes") and the court found reasonable
  precautions -- `What does section 6F mean for my claim` -- "the Act does not settle it" -- "the presumption is
  rebutted", since every route ends without a s 6F breach.
- **F14** s 5L, s 30, s 33 and the other Part 1A and Part 3 questions where the claim is not in negligence (s 5A, s 28(1))
  -- the gated questions -- `JUST FALSE` (this section does not bar) -- `NOTHING` (outside the Part's scope).

## What the Act turns out to say

1. **The vicarious liability gap in s 3B(1)(a).** The intentional-act exclusion speaks of the liability of "a person in
   respect of an intentional act that is done by the person". A claim against an organisation for its employee's sexual
   abuse is liability for someone else's act, so on the words the whole Act (Part 2's caps included) applies to it,
   while the abuser's own liability escapes Part 2. s 3C (exclusions and limits carry over to vicarious liability) pulls
   the other way. Fork F1; asserted `NOTHING` where it matters.
2. **Part 1C is not among the s 3B(1)(a) exceptions.** s 3B(1)(a) keeps Part 1B (and ss 15B, 18(1)(c), Part 2A, Part 7)
   for intentional and sexual torts, but not Part 1C. Read literally, Part 1C (setting aside child abuse settlements)
   does not apply "to or in respect of" the abuser's own liability for sexual assault, nor (by (f)) to work injury
   damages; it still applies to the organisation's liability in negligence. The likelier intent is that Part 1C operates
   on agreements whatever the liability. Asserted on the literal words (`JUST FALSE`), both through the s 3B question and
   through the Part 1C questions themselves (ss 7C, 7D take the kind of claim settled).
3. **Two meanings of child abuse in Part 1B.** ss 6F(5) and 6H(4) confine "child abuse" to sexual or physical abuse that
   was unlawful at the time; s 6J "child abuse proceedings" covers any "abuse (including sexual abuse) against a child",
   under Part 1B or the common law. So the Division 4 machinery (suing an unincorporated organisation, proper defendants,
   trustees) reaches claims for emotional abuse or neglect that ss 6F and 6H do not. Asserted.
4. **Divisions 2 and 3 are prospective, Division 4 is not.** Sch 1 cll 43 and 44 confine ss 6F and 6H to abuse after
   their commencement; cl 45 extends Division 4 to earlier abuse. Asserted.
5. **A late appointment does not stop s 6N.** s 6N(1)(a) asks whether a suitable proper defendant was appointed "by the
   end of 120 days" after service. If one is appointed on day 121, the condition is met and the plaintiff may still apply
   to have trust trustees appointed, though a suitable defendant now exists. Asserted.
6. **s 54(2) and s 54A(4) differ.** s 54 is displaced only where the defendant's conduct "constitutes an offence"; s 54A
   is displaced also where it would have been an offence but for the defendant's impairment. So a claimant who committed
   a serious offence is barred under s 54 even against an impaired defendant whose conduct would otherwise have been an
   offence. Asserted.
7. **s 18(1)(c) applies to motor accidents under the 2017 Act although s 15B does not.** s 3B(2)(a1) withholds s 15B
   from Motor Accident Injuries Act 2017 accidents, while s 3B(2)(c1) keeps the bar on interest for s 15B-type loss for
   all motor accidents. Harmless, but the interest bar then attaches to damages the Act does not award. Asserted.
8. **The s 16 Table is whole-percentage only.** It gives 15% to 33% line by line and then "34%-100% respectively", with
   no rule for 15.5% or 27.25%. Fork F5; asserted not settled.
9. **The s 15 note relies on s 3B(1)(b)** to send dust disease claims to s 15A; s 15A(1) says so in its own words, but
   notes are not part of the Act (s 4(3)). No effect on the answers.
10. **The real maximum for non-economic loss is not $350,000.** s 17(3) displaces the s 16(2) figure with the amount in
    the Minister's latest order; none is deposited, so the maximum is an input.

## Questions (exported)

`cla-core.l4` (1): `Does this part of the Act apply to my claim` (s 3B).

`cla-child-abuse.l4` (16), in the Act's order: `Is the successor the same organisation under Part 1B` (s 6C), `What
does section 6F mean for my claim` (ss 6A, 6D-6F; Sch 1 cl 43),
`Is the organisation vicariously liable under section 6H` (ss 6G, 6H; cl 44), `Can I sue the unincorporated organisation
in its own name` (ss 6J, 6K; cl 45), `Is the entity a suitable proper defendant` (s 6M), `Is it an associated trust`
(s 6N(3)), `By when must a proper defendant be appointed` (s 6N(1)), `Can I apply for the trustees to be appointed`
(ss 6L, 6N), `By when must the organisation identify its trusts` (s 6N(4)), `Has the organisation identified its trusts
in time` (s 6N(4), the regulative rule), `Does the proper defendant stand in for the organisation` (s 6O), `The most I
can recover from the trustees` (s 6P), `Is my settlement an affected agreement` (ss 3B, 7C), `Can the court set aside my
settlement` (ss 3B, 7D), `Can the court also set aside this thing` (s 7E),
`Must I repay what I received under the settlement` (s 7F).

`cla-damages.l4` (12): `What weekly earnings can the court count` (s 12), `What discount rate applies` (s 14), `Does
section 15 stop my claim for gratuitous care`, `What is the most per week for gratuitous care` (ss 15, 15A), `Does section
15B stop my claim for lost capacity to care for dependants`, `What is the most per week for lost capacity to care for
dependants` (s 15B), `What is the most for lost superannuation` (s 15C), `How much for non-economic loss` (ss 16, 17),
`Does section 18 stop interest on this part of my damages` (s 18), `Can I get exemplary or aggravated damages` (s 21),
`Must the court tell us the proposed award first` (s 23), `Must my lawyer advise me about structured settlements` (s 25).

`cla-liability.l4` (9): `Does section 5H remove the duty to warn me`, `Does section 5I stop my claim`, `Does section 5L
stop my claim`, `Do sections 30 and 31 stop my claim for pure mental harm`, `My damages for pure mental harm after the
victim's reduction` (s 30(3)), `Does section 33 stop my economic loss claim for consequential mental harm`, `What does
section 50 do to my claim`, `Can the defendant rely on self-defence` (ss 52, 53), `What does my own offence mean for my
claim` (ss 54, 54A).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation
  (amendments after 16 June 2022 are missing).
- Deposit the commencement instruments, the s 17 orders and the Civil Liability Regulation, and replace the date and
  figure inputs with them.
- Have a lawyer review the forks, especially F1 (s 3B and vicarious liability), F2 and F4 (day counting) and finding 2
  (Part 1C and s 3B).
- Encode s 5M (risk warnings), Part 2A (offenders in custody) and the contributory negligence provisions as further
  layers.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
