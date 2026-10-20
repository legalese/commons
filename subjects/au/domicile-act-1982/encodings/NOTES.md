# Domicile Act 1982 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the domicile position for` (`dom-rules.l4`). It answers, at a given time:

- whether I can have a domicile of my own (s 8);
- as a child, whose domicile I take (s 9(1)-(3), (5));
- whether I keep that domicile after ceasing to be a child (s 9(4));
- whether I have acquired a domicile of choice in a country (s 10);
- that my domicile does not follow my husband's (s 6), and that my domicile of origin does not revive (s 7).

The encoded provisions are ss 4(1) (child), 5(1)-(2) and 6-10. The source is the compilation of 25 January 2019; the Act commenced on 1 July 1982.

## Seat

The encoding is written from the seat of **the person whose domicile is in question**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can I have a domicile of my own; as a child, whose domicile do I take; do I keep it when I grow up; have I acquired a domicile of choice in this country?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery; commencement on 1 July 1982 is applied |
| s 3 | out of scope: that the question arises under Commonwealth or applicable Territory law is assumed |
| s 4 | (1) child encoded; adopted, country and union are folded into the inputs; (2) applied (parents need not be married) |
| s 5 | (1)-(2) encoded: before 1 July 1982 the answer is NOTHING; (3) out of scope |
| s 6 | encoded |
| s 7 | encoded |
| s 8 | encoded |
| s 9 | encoded |
| s 10 | encoded, with residence asked as a fact |
| s 11 | out of scope: the closest connection is a finding |
| s 12 | out of scope: evidence |
| s 13 | out of scope: regulations |

## Forks (readings taken)

- **F1, s 5.** The commencement day itself (1 July 1982) is governed by the Act.
- **F2, s 8(2).** For a person mentally incapable under the common law, the Act does not say whether they can have an independent domicile: NOTHING.
- **F3, s 9 order (changed after the independent pass).** Rescission (s 9(5)) is taken first, then s 9(2)(b) (a sole adoptive parent), then s 9(1) (which applies to adoptive parents as to any parents), then s 9(2)(a). Where none applies (for example, parents living together and not adopted), the common law governs: NOTHING.
- **F4, s 9(1), (2)(b) death.** Where the parent whose domicile I follow has died, the answer is that parent's domicile at death.
- **F5, s 10.** A domicile of choice needs capacity (s 8), residence (the common law's other limb, asked as a fact) and the s 10 intention.
- **F7, s 9(4) (changed after the independent pass).** A person who had no s 9 domicile on ceasing to be a child does not keep one under s 9(4): FALSE.
- **F6, age.** 18 is attained on the 18th anniversary of birth; 29 February falls on 28 February in a common year.
- **Known limits (from the independent pass).**
  - A 29 February birthday and separated adoptive parents are not tested.
  - s 9(3) is read from present facts, not a change over time.
  - The content of a rescission order (s 9(5)) is not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 50 assertions satisfied, 0 failed, 0 other errors — 21 the encoder's (`dom-tests.l4`), 29 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** where a child has 2 adoptive parents who live apart, does s 9(1) apply, or s 9(2)(a) (which leads to the same place)?
