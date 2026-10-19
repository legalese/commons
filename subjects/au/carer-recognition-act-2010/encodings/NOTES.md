# Carer Recognition Act 2010 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the carer position for` (`carer-rules.l4`). It answers:

- whether I am a carer;
- whether the body I deal with must make its staff aware of the Statement for Australia's Carers;
- whether it must reflect the Statement's principles in care supports;
- whether it must consult carers on care supports;
- that none of this is enforceable, nor a ground to challenge a decision.

The operative provisions are encoded: ss 4-5 and 7-10. The source is the Act as made (No. 123, 2010).

## Seat

The encoding is written from the seat of **the carer**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I a carer under this Act? Must the government agency dealing with me have regard to the Statement for Australia's Carers, and consult carers about care supports? Can I enforce any of this, or challenge a decision because the agency did not comply?"

The facts it asks for are ones that person can state: the care they give, why it is needed, on what basis, and who they are dealing with.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery and the object |
| s 4 | the kinds of body are an input; whether an agency is a "public service care agency" or a provider an "associated provider" is the caller's |
| s 5 | encoded |
| s 6, Schedule 1 | inert: the Statement's principles |
| s 7 | (1) encoded; (2) (internal human resources policies) is out of scope |
| s 8 | (1)-(2) encoded; (3)-(4) (annual reports) are out of scope |
| s 9 | encoded |
| s 10 | (1)-(2) encoded; (3) is inert |
| ss 11-12 | out of scope |

## Forks (readings taken)

- **F1, s 5(1).** "Personal care, support and assistance" is one input, and the need must be one of the four in s 5(1)(a)-(d).
- **F2, s 5(2)-(3).** Care given informally is the only basis that qualifies. Being a relative, guardian or housemate does not count without the care itself.
- **F3, s 7(1) and s 9(a).** Every public service agency (care or not), and every associated provider, must take practicable measures for its staff's awareness of the Statement.
- **F4, s 10.** No obligation is enforceable, and non-compliance affects no decision. The answers say so for every case.
- **Known limits (from the independent pass).**
  - "Frail and aged" is one choice; the user decides that both hold.
  - The s 4 definitions (public service care agency, associated provider, including subcontractors, the State and Territory exclusion, and contracts for care supports) are an input, not worked out.
  - s 7(2) (internal human resources policies) and s 10(3) are not encoded.
  - The s 8(2) duty to consult carries no limit to "when developing or evaluating care supports".
  - One basis of care per case: mixed paid and unpaid care cannot be entered.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 4 modules: 54 assertions satisfied, 0 failed, 0 other errors — 20 the encoder's (`carer-tests.l4`), 34 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
