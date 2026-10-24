# Human Services Code, Article IV (Pennsylvania public assistance: cash) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, with the design defaults ruled on 2026-10-18.
The core, `pa-hsc.l4`, uses Article IV's own actors and terms and takes no seat.
- **Regulative rules.** Two duties carry a deadline and are written as `PARTY … MUST … WITHIN … LEST BREACH`. One is to meet the work requirements once a disability exemption ends (s 405.1(a.4)(1)): immediately, or within eight weeks. The other is to report changes within the period the department specifies (s 432.14(b)). The right to ask for a fair hearing within the timely notice period (s 423(a)) is a `MAY`.
- **Functions.** The tests (classes, bars, resources, income, work requirement, disqualification, notice) are functions.
- **The seat layer.** `pa-hsc-seat.l4` asks the applicant's and recipient's questions, each with `@export` and a `@desc` on every input. It calls the core and restates no rule.

There is no REFUSE. No question reaches anything outside the encoding. The grant amount is not asked at all (see Scope).

Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

## Edition

The Human Services Code (Act of Jun. 13, 1967, P.L. 31, No. 21; it was called the Public Welfare Code until 2014), as served by the Pennsylvania General Assembly at palegis.us on 24 October 2026. It is deposited whole at `../../registers/source-bundle/pa-1967-act-21-human-services-code.txt`, and Article IV, Public Assistance, is at lines 1299–5284. The site gives no "current through" date.

Nothing else is brought in:
- The payment standards (family size allowances) are set in the department's regulations, 55 Pa. Code ch. 175, which are not deposited.
- The combined SSI-and-supplement amount (s 432(2)(ii)) is fixed by the department under s 432(2)(iii), so it is an input.
- The maximum payments in Pennsylvania and in the person's previous state are also inputs.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `pa-hsc.l4`, `pa-hsc-seat.l4` | `pa-hsc-cases.l4` | 56 written, 56 satisfied |

`l4 run` on all three files gives 0 errors and 0 warnings (2026-10-24). Two `#TRACE` breach checks (a change reported late, and failing to comply at once when an exemption ends in month 10) were read as `BREACH` by the applicant or recipient, as their `-- expect:` comments say. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was worked by hand from the text.

## Seat

**The applicant for, or recipient of, cash assistance.** This is a parent or caretaker relative applying for TANF cash assistance ("aid to families with dependent children" in the Code), an aged, blind or disabled person asking about the State supplement to SSI, or a single adult asking about general assistance. Questions:
- "Can I get general assistance cash?"
- "Am I eligible for the State supplement?"
- "Is anything barring me?"
- "How much of our property counts?"
- "Does this member's income count?"
- "How much of our income counts?"
- "What is the most we can get in our first year here?"
- "What work must I do?"
- "If I fail it, how long am I disqualified, and is it just me?"
- "When can it end?"
- "How long do I have once my exemption ends?"
- "When can a cut take effect?"
- "Does my assistance continue if I appeal?"

Provisions addressed to the department, such as notice (s 432.17) and hearings (s 423), are encoded as what they mean for the person: the earliest day a cut can take effect, and whether assistance continues pending the hearing.

Defaults:
- **The Act alone.** Article IV only. No regulation is deposited, so figures the department sets are inputs.
- **The actors the text names:** the applicant or recipient, the assistance group, the department, the county assistance office.
- **Judgments left to others are asked as facts:**
  - whether federal financial participation is available (s 432(1));
  - the department's exception for a minor parent (s 432(10));
  - a "verified" disability (s 405.1(a.3)(1));
  - "good cause" (s 432.3), which is assumed absent in the disqualification question;
  - the reporting period the department specified (s 432.14(b)).
- **Definitions worked out from facts:** whose income counts (s 432.12(a)), the available resource (s 432.5(c)), and "satisfied the penalty" (s 432(9)). **Borrowed terms asked as facts:** "aged, blind and disabled, as defined in Title XVI", income "pursuant to the standards and income disregards of Title XVI", and when federal law "specifically" requires assistance to a non-citizen.
- **One case:** one applicant or recipient and their assistance group. Whose income counts is asked once per member.
- **Terms:** the Act's own, glossed. "Aid to families with dependent children" is kept, with the gloss that it is today's TANF cash assistance.
- **Machinery out:** county boards, the department's powers, fiscal provisions, information-sharing and verification systems.

## Read with

`subjects/us/social-security-act/` (federal Title IV-A, 42 U.S.C. 601–619, TANF; and Title XVI, SSI). Section 432(1) makes the class depend on whether "Federal financial participation is available". That depends on the federal limits, such as the 60-month limit in 42 U.S.C. 608(a)(7), so it is an input here. Cross-folder IMPORT is not possible in the stable `l4`, so the link is recorded here, not in code.

## Scope

**In:** s 403.2(a), (b); s 405.1(a.2)(1)–(3), (6), (a.3), (a.4)(1), (b); s 423(a) (continued assistance pending a fair hearing); s 432(1), (2)(i)–(ii), (4), (5)(i)–(ii), (6), (9), (10); s 432.3(a); s 432.5(b), (c); s 432.12(a); s 432.14(b); s 432.17; s 432.22.

**Out:**
- the amount of the grant: payment standards are in 55 Pa. Code ch. 175, not deposited, and Article IV does not state how the TANF grant is computed from need and income;
- medical assistance (ss 441–460.1);
- school attendance (ss 461–469);
- drug-felony and sex-offender eligibility (ss 432.24–432.26);
- income averaging and recoupment (ss 432.13, 432.16);
- verification (ss 432.19, 432.23);
- federal benefits as primary sources (s 432.21);
- special allowances (s 405.1A);
- lottery winnings as a resource (s 432.5(g)), whose 12-month proration the text leaves undefined;
- the identification requirements (s 432.4);
- the general assistance classes of s 432(3), because cash ceased in 2019 (finding 1).

## What the Act turns out to say

1. **General assistance cash no longer exists.** Section 432(3) still lists the people eligible for general assistance, but s 403.2(a) says "notwithstanding any other provision of law, the general assistance cash assistance program shall cease August 1, 2019". Only the medical assistance tied to general assistance continues (s 403.2(b)). A single adult without children has no state cash programme under Article IV. Asserted.
2. **The State supplement to SSI follows SSI.** Anyone receiving SSI gets it (s 432(2)(i)). So does an aged, blind or disabled person whose income under the SSI rules is less than SSI plus the supplement (s 432(2)(ii)). The test is "less than", so an income equal to the combined amount fails. The amounts are the department's to set, and once set they are not reduced by federal cost-of-living increases (s 432(2)(v)). Asserted.
3. **One $500 gift in two years bars assistance, except for the State supplement.** Disposing of property "of the value of five hundred dollars ($500), or more, without fair consideration, within two years immediately preceding the date of application" bars assistance "unless he is eligible for State supplemental assistance" (s 432(4)(i)). The Code gives no proportionate penalty period. The bar is absolute. Asserted.
4. **An unsatisfied sentence bars assistance, but parole or probation with a payment plan does not.** "Satisfied the penalty" means both the custody and all fines, costs and restitution. Even so, a person "paroled ... or ... in compliance with all terms of probation" who has paid in full "or is in compliance with an approved payment plan" is not excluded (s 432(9)). A person who has served their time but owes restitution, and is on neither parole nor probation, is barred. Asserted.
5. **An unmarried parent under 18 must live with an adult, unless an exception applies.** The exception is the department's determination, or evidence of one of five grounds about the adult (s 432(10)). At 18 the bar does not apply. Asserted.
6. **The resource allowance is small, and a vehicle is excluded only if its equity is under $40,000.** Other property over $250 for one person, or $1,000 for a larger group, is an available resource (s 432.5(c)). One vehicle is excluded when its market value less the amount owed "is less than forty thousand dollars", so $40,000 of equity exactly is not excluded. The Code does not say at what value a non-excluded vehicle counts. The encoding counts its equity, the only value the text names. Asserted.
7. **Students aged 14 to 21 who are not employed full time have their income ignored.** "Between the ages of fourteen and twenty-one" is read as inclusive of 21. A 21-year-old part-time student's earnings are not considered, and a 22-year-old's are. Children under 14 never count (s 432.12(a)). Asserted, as a reading.
8. **The 50 per cent earned income disregard is stated for recipients only.** "Fifty percent of gross earned income shall be disregarded when determining eligibility for recipients" (s 432.12(a)). The text gives applicants no disregard, so $1,000 of earnings counts in full for a family applying, and as $500 for one already receiving. The department's regulations may say otherwise. They are not deposited. Asserted.
9. **A family new to Pennsylvania gets the lower of two maximums for its first twelve months.** This is the lesser of its previous state's maximum and Pennsylvania's (s 432(5)(ii)). Asserted. This kind of durational cap was held unconstitutional for California in *Saenz v. Roe*, 526 U.S. 489 (1999) (general knowledge, unverified against a deposited source), so it may not be enforced. That needs checking before anyone relies on it.
10. **Disqualification for failing the work rules escalates, and after 24 months it hits the whole family.** The disqualification is at least 30 days, then at least 60 days, then permanent, each "continuing thereafter until such time as he or she is willing to comply". If the reason occurs in "the first twenty-four months" of assistance, only the individual is disqualified. After "more than twenty-four months" the whole assistance group is (s 432.3(a)). Month 24 counts as within the first 24. Asserted.
11. **The work rule tightens at 24 months.** Before then, a non-exempt person must seek, accept and keep work, and anyone working under 20 hours a week must take part in a work-related activity, starting with up to eight weeks of independent job search (s 405.1(a.2)(1)–(3)). After 24 months they must work, or do a listed activity, for an average of 20 hours a week (s 405.1(a.2)(6)). Asserted.
12. **The 2012 amendments were struck down, and the text shows the restored version.** The amendments of ss 405.1(a.2)(3), 432.2(b) and 432.3(a) by Act 80 of 2012 were "declared unconstitutional" in *Washington v. Commonwealth* (Pa. 2018). The deposited text carries notes saying the Legislative Reference Bureau "effectuated" that ruling. The encoding follows the text as printed.
13. **A cut needs ten days' notice, and an appeal in that time keeps assistance going.** Timely notice is "mailed ten days before the intended change would be effective" (s 432.17). A recipient who asks for a fair hearing within that period keeps their assistance until the decision, unless the sole issue is law or policy (s 423(a)). Asserted.

## Before relying on it

- Deposit 55 Pa. Code chs. 175, 177, 178 and 183 (payment standards, income and resources), so that the grant itself can be computed. They could not be fetched on 2026-10-24. The Pennsylvania Code & Bulletin site (pacodeandbulletin.gov) has a robots.txt with `User-agent: *` / `Disallow: /`. Its terms ("No part of the information on this website may be reproduced for profit or sold for profit") would otherwise allow non-commercial use. A human could ask the Legislative Reference Bureau, or save the chapters by hand. Then check findings 6 and 8 against the regulations.
- Check finding 9 against *Saenz v. Roe*.
- An independent test pass.
