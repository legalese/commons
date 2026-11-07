# Civil Liability Act 2002 (Tas) — baseline-2026-11: the provisions a claimant meets

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the
individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the rulings on negatives of
2026-11-04/05. No `REFUSE`. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No
pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; no longer encoding exists, so this is a baseline rather than a seat layer.
Every question is published with `@export` and a plain-words description, and every input carries an `@desc`.

Modules: `clatas-dates.l4` (the only module that imports daydate), `clatas-common.l4` (ss 3B and 4, which every Part
uses), `clatas-damages.l4`, `clatas-liability.l4`, `clatas-abuse.l4`. Cases: one file for each of the last three.

## Edition

- **The Act:** the Civil Liability Act 2002 (No. 54 of 2002), consolidated version published 21 October 2024 and
  current on Tasmanian Legislation Online at 6 November 2026, deposited at
  `../../registers/source-bundle/act-2002-054.txt` (retrieved 6 November 2026). The two s 27 formulas appear on the site
  only as images; the deposit transcribes them (`Amount awarded = 1.25 x (amount assessed minus Amount A)`;
  `A = Ao x C / D`), and this encoding uses those transcriptions.
- **No regulations.** None is deposited. A discount rate prescribed under s 28A(b), classes excluded under s 3B(5),
  bodies prescribed under ss 37 and 49G, and amounts prescribed under s 45(2)(b) are asked as facts.
- **Figures set outside the Act** are inputs: adult average weekly earnings (s 3, ABS catalogue 6302.0), the Hobart CPI
  (s 27(8)), the superannuation guarantee percentage (s 25(2)), the maximum penalty of an offence (s 6(3)). The Gazette
  notice of Amounts A and B is "for public information only" (s 27(7)); the amounts are worked from the formula.

## Checks

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `clatas-damages-cases.l4` | 134 | 134 | 0 | 0 |
| `clatas-liability-cases.l4` | 141 | 141 | 0 | 0 |
| `clatas-abuse-cases.l4` | 57 | 57 | 0 | 0 |

`l4 run` on each module succeeds with no diagnostics. `l4 run` exits 0 even when an assertion fails, so the diagnostics
were read. A negative control (three expected values altered in a copy of `clatas-damages-cases.l4`, one of them shared
by two assertions) gave four "assertion failed". Expected values were worked by hand from the text, with the edges:
each start date and the day before; 6 and 7 months' imprisonment; 6 hours a week and 6 months; Amount A, Amount B and a
dollar over each; the $250 rounding point; the 3 x and 1/40 adult average weekly earnings caps; age 17 and 18; the 60th
day after service and the next; the 28th and 29th day after an application.

## Seat

**The individual bringing the claim:** the injured person ("By how much will my damages be reduced?", "How much will I
be awarded for non-economic loss?", "Can I hold the volunteer liable?"); for s 26, also a dependant claiming under the
Fatal Accidents Act 1934; the person with mental harm (Part 8); the guest whose property was lost (Part 10A); the person
abused as a child who sues an organisation (Part 10C, s 7AA). Part 10B speaks to an employee who is sued ("Must my
employer indemnify me?"); that is the same individual answering a claim.

The provisions speak mostly to the court ("is not to award", "may award", "must not award") or protect a defendant ("is
not liable", "does not owe a duty"). Each is encoded as what it means for the claimant. No seat for the court, the
Minister, the organisation, the authority, the insurer or any other defendant.

Each 2026-10-18 default:

- **The Act alone, plus the instruments that set its numbers.** Followed; none is deposited (see Edition).
- **The actors the text names.** Followed: the plaintiff, the defendant, the court, the medical practitioner and the
  professional, the good samaritan, the food donor, the public or other authority, the concurrent wrongdoer, the
  volunteer and the community organisation, the accommodation provider, the employer and employee, the organisation, the
  individual associated with it, the unincorporated organisation, the proper defendant, the trustees.
- **Judgments handed to others, asked as inputs.** Followed: what the court is "satisfied" of (ss 5, 6), whether a risk
  is "obvious" (s 15), "not insignificant" or one a "reasonable person" would guard against (s 11), "scope of liability"
  (s 13), whether peer opinion is "irrational" (s 22), normal fortitude (s 34), "good faith" (ss 35B, 47), the share the
  court "considers just" (s 43B), "reasonable precautions" (s 49H), the s 49P(2)(b) findings. Every "may" of the court
  is answered "can", never "will".
- **The Act's own definitions worked out from facts.** Followed for "intoxicated" (s 5(5), (6)), "serious offence"
  (s 6(3)), "structured settlement" (s 8(2)), "dust-related disease" (s 8B(2)), "dangerous recreational activity"
  (s 19), "close member of the family" and "spouse" (s 32(3)), "good samaritan" (s 35B(1)), "volunteer" (s 45),
  "guest" (s 49A(1)), "child" and "organisation" (s 49C), "responsible for a child" (s 49F), "associated" (s 49G),
  "child abuse" (ss 49H(5), 49J(3), 49L), "akin to an employee" (s 49I), "associated trust" (s 49P(3)), "suitable
  proper defendant" (s 49O). Borrowed or open terms asked as facts: "recreational activity" (an open "includes"),
  "public or other authority" (s 37, partly prescribed), "community organisation" and "community work" (s 44),
  "sexual abuse", "physical abuse", "recognised psychiatric illness", Part III of the Motor Accidents (Liabilities and
  Compensation) Act 1973 and the other Acts s 3B names.
- **One case is the text's natural unit.** One claim against one defendant; one concurrent wrongdoer at a time
  (s 43B); one trust (s 49P).
- **The Act's terms, each with a plain gloss.** In the comments and the `@desc` lines.
- **Operative sections in, machinery out.** Followed; see Scope.

No exported question takes a DEONTIC or EVENT input. The one duty with a deadline a claimant meets, s 49P(4) (the
unincorporated organisation must identify its associated trusts within 28 days after the plaintiff's application), is a
regulative rule (`PARTY ... MUST ... WITHIN 28 ... LEST BREACH ... BECAUSE`) run by `EVALTRACE` inside a question that
takes dates and a yes/no. The 28 days are held once (`the s 49P(4) period, in days`), and both the rule's `WITHIN` and
the deadline question read them from there.

## Scope

In (the whole Act so far as a claimant meets it):

- ss 3, 3B, 4: which Parts reach which claims and from what dates (`clatas-common.l4`).
- Part 2 (s 5, intoxication); Part 3 (s 6, recovery by criminals); Part 5 (s 8, structured settlements); Part 5A
  (s 8B, provisional damages for dust-related diseases, with s 4(2A)-(2B)); Part 7 (ss 25-28E: superannuation, the
  earnings cap, non-economic loss thresholds, the discount rate, gratuitous services, loss of capacity to care, motor
  accident claims, consortium, abolished actions) (`clatas-damages.l4`).
- Part 4 (ss 6B, 7); Part 6 (ss 11, 13, 15-17, 19-22); Part 8 (ss 29, 32-35); Part 8A (ss 35B, 35C); Part 8B (s 35F);
  Part 9 (ss 39-42); Part 9A (ss 43A, 43B, 43E); Part 10 (ss 45, 47, 48); Part 10A (s 49A); Part 10B (s 49B)
  (`clatas-liability.l4`).
- Part 10C (ss 49C, 49F-49J, 49L-49P, 49R(2), (6)) and ss 7AA, 7AB (`clatas-abuse.l4`).

Out, and why:

- Machinery: s 1, s 2, s 4AA, s 3B(5)-(6) (regulation-making; no regulation deposited), s 49S (rules of court),
  Part 11 (regulations), s 49R(5) (a Corporations Act s 5G declaration), s 49M(2)-(4) (management members may exercise
  the organisation's functions; the court's orders and directions to them).
- Definitions and glosses taken into an input's `@desc` rather than encoded as a rule: s 37 ("public or other
  authority": the Crown, councils, statutory authorities and the rest, partly by prescription; asked as a fact), s 49E
  (an organisation and its successor are the same organisation; the claimant names the organisation as the court will
  treat it).
- s 46: (1) Part 10 "applies to civil liability for a thing done by a volunteer after the commencement of this Part";
  the encoding dates Part 10 by the accrual of the cause of action under s 4(3) instead (fork F15). (2) Part 10 "does
  not limit the protection from liability given by another written law": other written laws are outside this Act.
- s 4(3C): the 2013 amendment of s 28C (which added the loss of capacity to provide gratuitous services) does not reach
  a cause of action accrued before 1 March 2014. Not a separate rule: the only question that turns on that limb of
  s 28C is the s 28BA question, which s 4(3B) already confines to causes of action accrued from 1 March 2014.
- Principles with no fact of the claimant's to turn: s 3A, s 3C, s 12, s 13(3) (how a court decides what the plaintiff
  would have done), s 14 (onus on causation), s 15(2)-(5) (glosses on "obvious", folded into the input's `@desc`),
  s 23 (the standard for contributory negligence under the Wrongs Act 1954), s 28 (earlier awards as tariffs), s 31,
  s 34(2)-(4) (circumstances the court considers), s 38 (resources of authorities), s 43, s 49H(4) (matters the court
  may consider), s 49K (objects).
- Provisions that bind other parties among themselves: ss 43C, 43D (costs order against a defendant: a court's
  discretion with no amount), 43F, 43G, s 49 (indemnities between volunteer and organisation), s 49Q (conduct of the
  proceedings by the proper defendant), s 49R(1), (3), (4) (the trustees' powers and indemnity).
- s 49D: Part 9 does not limit Part 10C liability (no Part 9 question touches Part 10C), and an award under Division 2
  or 3 "must take into account" one already made under the other (no rule for how much; not a number).
- s 7AA(2) (who should make the apology and what it may include): guidance with no consequence, since s 7AA(4)(d) keeps
  the protection for an apology that does not meet it.
- **Limitation periods** for these claims are in the Limitation Act 1974, not this Act.

## Rulings on negatives and legal effects (2026-11-04/05), as applied here

`JUST FALSE` only where the text says no in its own words; `NOTHING` where it is silent, does not apply, or the case is
outside its scope. As applied:

- "means" definitions (ss 8B(2), 32(3), 49H(5)/49J(3)): `JUST FALSE` outside them.
- "is not to award" (s 6), "may not recover ... unless" (s 28B(2)), "only if" (s 28BA(2)), "is not to include"
  (s 28C), "is not liable" (ss 28D, 20, 42, 35B, 47), "abolished" (s 28E), "not entitled ... unless" (s 32(2)), "There
  is no liability ... unless" (s 33), "cannot make an award ... unless" (s 35), "does not owe a duty" (ss 17, 39),
  "does not constitute ... unless" (s 40), "is not liable ... except as provided" (s 49A(2)): `JUST FALSE`.
- "does not apply" (ss 3B, 4, 5(4), 7(3), 21(2), 22(5), 49B(3), 7AA(3), 7AB): `NOTHING`, the general law decides.
- "If ... the court may" with no "only if" (ss 8, 8B(1)): `JUST TRUE` where the condition is met, `NOTHING` where it is
  not; the Act gives the power and says nothing of other cases.
- Where a defence or limit does not arise, the Act is silent and the answer is `NOTHING`, never `TRUE`: the claimant
  still has to make out the claim at common law.

### Fork register (questions with no convention, decided case by case)

- **F1** ss 4(3A), (3B), (4), (5), (6), (7), (8), 4(2A): the commencement days of the amending Acts are read from the
  editorial history notes on the sections they inserted (15 December 2005; 1 March 2014; 1 June 2005; 22 October 2008;
  30 May 2012; 1 May 2020). Other reading: the commencement days must come from the proclamations, which are not
  deposited.
- **F2** s 4(6) "accrued after the commencement", s 4(7), (8) "perpetrated after the commencement": a cause of action
  accrued, or abuse perpetrated, on the day of commencement counts as after it. Other reading: only from the next day.
- **F3** ss 11, 13, `Do breach and causation stand in my way`: when every limb is met the answer is "ss 11 and 13 do not
  stand in the way", not "breach is established" (the limbs are prerequisites). Other reading: s 11(1)(c) met is a
  finding of breach.
- **F4** s 49P(1)(a): "by the end of the period of 60 days after" service excludes the day of service; s 49P applies
  from the 61st day. Other reading: the day of service is day 1, a day earlier.
- **F5** s 16, `Am I taken to have known of the risk`: a plaintiff who proves they were unaware answers `JUST FALSE`
  (the "unless" met). Other reading: `NOTHING`, s 16 then being silent.
- **F6** s 49G: "includes, but is not limited to": an abuser outside the list is asked as "otherwise associated".
- **F7** s 21, `Did my doctor breach the duty to warn`: a failure to give the s 21(1)(a) or (b) information answers
  `JUST TRUE` (breach of the duty to warn). Other reading: `NOTHING`, s 21 only saying when there is no breach.
- **F8** s 22: where it is not established that the professional acted as peers widely accept, the answer is `NOTHING`
  (s 22 gives no defence; the common law decides), not `JUST TRUE`.
- **F9** s 39(9) "to the extent that the warning was contradicted": read as all or nothing. Other reading: the
  authority may rely on the uncontradicted part of a warning.
- **F10** s 28E: it has no start date in s 4, but sits in Part 7, which s 4(3) keeps from causes of action accrued
  before 4 July 2003. Other reading: s 4(3) speaks of Part 7 as enacted in 2003, and the abolition reaches every cause
  of action.
- **F11** s 49J: where it does not make the organisation liable, the answer is `NOTHING`, because s 49J(2) keeps the
  common law of vicarious liability.
- **F12** s 49P(4): where the organisation has not identified its trusts, an identification on the day asked about
  stands for "had it done so that day"; if that would not keep the duty, it is late.
- **F13** Part 10A takes no s 3B class: every s 3B exclusion concerns personal injury, intent or a scheme, not a guest's
  property. Part 10B does take one (s 49B): the claim against the employee is classed under s 3B like any other, so a
  Part III motor accident injury, an intentional act, child abuse or a workers compensation Division 2 injury gives
  "s 49B does not apply". Asserted.
- **F14** s 7AB: in proceedings begun or determined before the Justice Miscellaneous (Commission of Inquiry) Act 2024
  received the Royal Assent, s 7 stands as it was before that Act (with the earlier s 7(3), and without s 6B). That
  earlier text is not deposited, so the s 7 question answers `NOTHING` for those proceedings, as the s 7AA question
  does.
- **F15** s 46(1): Part 10 reaches "a thing done by a volunteer after the commencement of this Part"; the encoding uses
  the s 4(3) accrual date (4 July 2003) instead. They differ only where the volunteer acted before 4 July 2003 and the
  cause of action accrued on or after it. Other reading: ask the day of the volunteer's act.

## What the Act turns out to say

1. **No cliff at Amount B.** Between Amount A and Amount B the award is 1.25 x (assessed - A); at B that is
   1.25 x 4A = 5A = B, so the award climbs from nothing at A to the full assessment at B with no jump. Asserted
   ($37 500 assessed gives $37 500; $37 501 gives $37 501).
2. **s 27 does not say which financial year's Amount A applies to a claim**: the year of the injury, of the assessment
   or of the award. The financial year is an input. Not asserted.
3. **The s 27 rounding rounds $250 up**: 4 000 x 145 / 80 = 7 250 becomes $7 500; 7 249.50 becomes $7 000. Asserted.
4. **A motor accident claim under Part III of the Motor Accidents (Liabilities and Compensation) Act 1973 loses Parts 4,
   6 Divisions 5-6, 8A, 8B, 9, 9A and 10** (s 3B(2)). So in a road crash claim a road authority has no s 42 protection,
   a doctor no s 21 and a professional no s 22, and the dangerous recreational activity defence is gone; Part 7's caps
   still apply, and s 28C removes gratuitous services. Asserted.
5. **Intentional child abuse keeps Parts 4 and 10C only** (s 3B(1A)), so Part 7's thresholds and caps, Part 8's mental
   harm limits and the rest do not reach it. Asserted for Parts 4, 7 and 10C.
6. **s 28E is dated by s 4(3).** It was inserted in 2006 with no start date of its own, so through s 4(3) it reaches
   causes of action accrued from 4 July 2003 (fork F10). Asserted.
7. **The Act's own commencement day is not in it** (s 2: "a day to be proclaimed"), yet s 4(1) keeps Parts 2, 3 and 4
   from causes of action accrued before it. Asked as a fact.
8. **The aftermath of mere peril does not count.** s 32(2)(a) lets a witness at the scene recover for seeing the victim
   "killed, injured or put in peril", but for the aftermath only "of the victim being killed or injured". Asserted.
9. **An individual's apology for child abuse has no s 7 protection** (s 7(3), substituted in 2024), and an
   organisation's apology made by the alleged perpetrator has none under s 7AA(3). Both hold only in proceedings begun
   after the 2024 Act received the Royal Assent (s 7AB, fork F14). Asserted.
10. **Exactly 6 hours a week, or exactly 6 months, fails** ss 28B(2) and 28BA(2) ("more than"); so does an offence
    punishable by exactly 6 months' imprisonment for s 6 ("greater than"). Asserted.
11. **ss 49H and 49J reach only abuse after 1 May 2020**, but Division 4 (suing an unincorporated organisation and its
    associated trusts) reaches abuse at any time (s 4(7)-(9)). Asserted.
12. **The State is not an "organisation"** for Part 10C (s 49C), so ss 49H and 49J do not reach it; its agencies,
    government businesses, councils and statutory authorities are. Yet s 49N(3) makes the State the proper defendant for
    an unincorporated Government department. Asserted for ss 49H, 49J and 49N(3).
13. **s 26 uses the earnings figure at the award**, "as last published ... before damages are awarded", not at the
    injury. Built into the input.
14. **Proportionate liability never reaches a personal injury claim** (s 43A(1)(a)). Asserted.

## What would need doing before this is worth relying on

- Encode the Limitation Act 1974 (time limits, including the child abuse provisions) and the Wrongs Act 1954 s 4
  (apportionment for contributory negligence), which these questions assume.
- Search for regulations under ss 3B(5), 28A, 37, 44, 45 and 49G, and fill the published Amounts A and B, adult average
  weekly earnings and the Hobart CPI series into worked examples.
- Confirm the commencement days in fork F1 against the proclamations, and the Act's own commencement day.
- A lawyer's reading of forks F2-F15 and findings 2, 5, 6 and 12.
- Check the deposited text against the authorised version: it was retrieved on 6 November 2026.
