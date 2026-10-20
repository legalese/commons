# Age Discrimination Act 2004 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. There was no first-pass encoding of this Act to replace.

## Edition

- **The Act:** Compilation No. 57, compilation date 1 July 2026 ("Includes
  amendments: Act No. 17, 2025"; register id C2026C00266). Deposited at
  `../../registers/source-bundle/C2004A01302.txt` (retrieved 2026-10-13).
- **Australian Human Rights Commission Act 1986**, ss 3(1), 46P, 46PH and 46PO only
  (complaints of "unlawful discrimination", which the Act sends there): Compilation
  No. 58, compilation date 18 September 2026 ("Includes amendments: Act No. 87,
  2026"; register id C2026C00416). Deposited at
  `subjects/au/australian-human-rights-commission-act-1986/registers/source-bundle/C2004A03366.txt`.
- No regulations set a number this encoding needs. The plan names none.
- The Fair Work Act 2009 (Compilation No. 73) was read at ss 351 and 772 only, to
  place this encoding beside the Fair Work Act baseline. Nothing from it is encoded.

## Checks

- One module (`ada-work.l4`) and one case file (`ada-cases-work.l4`).
- **39 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98. `l4 run ada-work.l4` also shows no errors or warnings.
- The case file is built by `gen_age-discrimination-act-2004_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.
- One assertion was deliberately changed in a scratch copy. The runner reported it
  as failing (38 of 39), so the runner does catch a wrong expectation.

Facts the life does not state are **assumptions**, labelled in the case file:

- that Jarrah Legal Technologies Pty Ltd, Chloe's employer, is a trading
  corporation, so the Act reaches it (s 10(8));
- that the forced-retirement fixtures are counterfactuals: the life says she
  retires by choice.

## Seat

**The older worker**: the employee or job applicant to whom the Act is applied. In
the lives this is Chloe at 63. Her question is: "Can I be made to retire at an age?"
Around it are the questions an older worker meets next:

- was I treated worse because of my age?
- does an exemption let them do it?
- may they ask my age?
- am I protected if I complain?
- where and by when do I complain?

The Act speaks to employers ("It is unlawful for an employer ..."). The encoding
turns that into what it means for the worker: whether what was done to them is
unlawful, or which exemption covers it.

The 2026-10-18 defaults:

- **The Act alone, plus instruments that set its numbers.** Followed, with one
  addition. No instrument sets a number. The Act sends complaints to the AHRC Act
  (s 4 outline; AHRC Act s 3(1) "unlawful discrimination"). The worker's question
  "where do I complain, and by when?" is answered only there, so ss 46P, 46PH(1)(b)
  and 46PO(2) of that Act are brought in. Nothing else from it is.
- **The actors the text names.** Followed: the employer, the aggrieved person, a
  religious body, the Commission, the President, and a trade union lodging for
  the worker.
- **Judgments handed to someone else are answered conditionally.** Followed. These
  are inputs:
  - whether a court would find the worker unable to carry out the inherent
    requirements (s 18(4), with the s 18(5) factors in the input's description);
  - whether the employer has shown a condition reasonable (s 15(2));
  - whether an act is consistent with the purposes of the Act (s 33);
  - whether a Commission exemption covers it (ss 44, 47);
  - whether a complaint is reasonably arguable (AHRC Act s 46P(1A)).
- **The Act's own definitions are worked out; borrowed terms are asked.** Followed.
  These are worked out from facts:
  - direct and indirect discrimination (ss 14, 15);
  - the two-or-more-reasons rule (s 16);
  - the s 6 carve-out for disability;
  - "youth wages" (under 21);
  - victimisation (s 47A).

  These are asked as facts:
  - the s 10 constitutional reach;
  - "fair work instrument";
  - which Acts Schedules 1 and 2 cover;
  - the State law under s 12(4).
- **One case is the text's natural unit.** Followed: one act of an employer
  towards one worker.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. Out are:
  - the Commission's functions and the Commissioner (Parts 6, 6A);
  - delegation, and protection from civil actions;
  - the other areas of Part 4, which an older worker's employment does not reach.

## The lives

- **Chloe, c092 (14 March 2066, age 63):** "Retires at 63; starts an account-based
  pension". The life cites the Act for "no compulsory retirement age". The decision
  is `Can I be made to retire at an age`.
  - On the facts of the life (she chooses to go) the answer is "nobody is making me:
    retiring by choice is not discrimination".
  - Counterfactual: Jarrah requires her to retire at 63. Then the answer is "no:
    making me retire because of my age is unlawful dismissal on the ground of age
    (s 18(2)(c))".
  - The same case is asserted through the general s 18 decision,
    `What does the Act say about what was done to me at work`.
  - Further cases show when the answer turns to yes: inherent requirements, an
    enterprise agreement term, a Commission exemption. One shows an employer the
    Act does not reach.

The tax question in c092 (Division 301 of ITAA 1997) belongs to that Act's
encoding.

## Why this scope

The one event asks one question, and the Act answers it through s 18(2)(c) read
with s 14. It contains no section on retirement. An older worker who is pushed
out next asks the questions listed under Seat, so the encoding covers:

- whether an exemption lets the employer do it (ss 18(3)-(4), 25, 33, 35, 38-40, 47);
- whether the employer may ask their age (s 32);
- whether they are protected if they complain (s 47A);
- whether a job advertisement aimed at younger people is an offence (s 50);
- whether, where and by when they can complain (s 12(4); AHRC Act ss 46P, 46PH,
  46PO).

The exemptions that do not bear on employment are left out: charities, voluntary
bodies, actuarial data, pensions, Commonwealth employment programs, health,
migration. So are the other areas of Part 4.

**Fair Work Act consistency.** The Fair Work Act baseline leaves the general
protections (Part 3-1) out of scope. Its s 351(1) forbids adverse action because of
age, and its s 772(1)(f) forbids termination for age. They are a parallel route for
the same worker, and they lean on this Act. Under s 351(2)(a), s 351(1) does not
apply to action "not unlawful under any anti-discrimination law in force in the
place where the action is taken", and s 351(3)(aa) names this Act as one. s 772(2)(a)
keeps a reason "based on the inherent requirements of the particular position". This
encoding does not encode either section, so the two baselines agree: neither answers
the general protections question.

## What the Act turns out to say

1. **There is no compulsory retirement age, and no section on retirement.** Being
   made to retire because of reaching an age is dismissal on the ground of age
   (ss 14, 18(2)(c)), unlawful unless an exemption applies. That reading is an
   inference from ss 14 and 18; the Act does not use the word "retirement" in s 18.
   Retiring by choice involves no act of the employer. Asserted.
2. **The inherent requirements exemption is narrow.** It covers only the hiring
   arrangements, the hiring decision, and dismissal (s 18(4): paragraphs (1)(a),
   (1)(b), (2)(c)). It does not cover the terms of an offer, terms of employment,
   access to promotion or training, or other detriment. So a worker a court finds
   unable to do the job may still not be refused training because of age.
   Asserted.
3. **The domestic duties exemption covers hiring only** (s 18(3): (1)(a) and (b)).
   Dismissing a live-in housekeeper because of age is still unlawful. Asserted.
4. **Age need only be one reason.** It need not be the dominant or a substantial
   one (s 16). An assumption about people of one's age counts as well as age itself
   (s 14(b)(ii), (iii)). Asserted.
5. **Indirect discrimination puts the burden on the employer** to show the
   condition is reasonable (s 15(2)). A requirement the employer has not shown
   reasonable is discrimination; the same requirement shown reasonable is not.
   Asserted.
6. **Direct compliance with a fair work instrument, or with a minimum wage order, is
   not unlawful under this Act** (s 39(8)). This covers an enterprise agreement term
   requiring retirement, but only if the term has effect (the s 39(8) note). Whether
   it has effect is a Fair Work Act question, not encoded. Asserted (on the input
   that it has effect).
7. **s 33's own example is about older workers:** "additional notice entitlements for
   older workers" reduce a disadvantage and are not unlawful. A younger worker kept
   out of an over-55s scheme meant to reduce a disadvantage has no claim. Asserted.
8. **Youth wages (under 21) are exempt** in offering work and paying for it (s 25).
   Asserted.
9. **Going to the WA Equal Opportunity Commission first closes the federal door.** A
   complaint or proceeding under a State discrimination law about the same act
   means the worker "is not entitled to make a complaint" under the AHRC Act
   (s 12(4)). Asserted.
10. **The 24 months is a discretion, not a bar.** The President "may terminate" a
    complaint lodged more than 24 months after the act (AHRC Act s 46PH(1)(b)).
    Lodging exactly 24 months later is not "more than". Asserted.
11. **After termination the worker has 60 days from the notice's date of issue** to
    apply to the Federal Court or the Federal Circuit and Family Court (Division 2),
    or longer if the court allows (AHRC Act s 46PO(2)). Asserted.
12. **Victimisation is unlawful and an offence.** It is unlawful under s 47A, and an
    offence under s 51 punishable by 6 months' imprisonment. A threat counts without
    proof that the worker was afraid (s 47A(5)). The s 51 offence is excluded from
    the AHRC Act's "unlawful discrimination", but s 47A puts victimisation in Part 4,
    so it can still be complained of. Asserted.
13. **A job advertisement indicating an intention to discriminate unlawfully** is an
    offence of 10 penalty units, with strict liability on whether it indicates that
    intention (s 50). It can also be complained of (AHRC Act s 3(1)(ca)). Asserted.
14. **The Act does not reach every employer.** Divisions 2 and 3 have effect only as
    s 10 provides: Commonwealth employment, corporations, banking, insurance,
    interstate trade, the Territories. Section 10(7) also gives effect to the ILO
    Discrimination (Employment and Occupation) Convention. That may well reach most
    employment, but this is an inference, and the reach is an input. Asserted (an
    employer the Act does not reach).

## What would need doing before this is worth anything

- A coverage table over Part 4, and an independent test pass.
- The s 10 heads worked out from facts, and an answer on how far s 10(7) reaches.
- Schedules 1 and 2 (which Commonwealth laws are exempt under s 39(1), (1A)), and
  the regulations under s 39(5) (State laws not exempt).
- The remaining exemptions: ss 34, 36, 37, 41, 41A, 42, 43.
- Remedies the court may order, conciliation, and the President's other termination
  grounds (AHRC Act s 46PH(1), (1B), (1C)).
- The Fair Work Act general protections (ss 351, 772), together with the Fair Work
  Act baseline, so a worker can compare routes. Also when an enterprise agreement's
  retirement term "has effect" for s 39(8).
- The WA Equal Opportunity Act 1984 age provisions, for the State route s 12(4)
  makes the worker choose between.
- No case law or Commission guidance was retrieved. "Inherent requirements" and
  "reasonable in the circumstances" are judicial questions left as inputs.
