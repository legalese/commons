# Human Rights (Sexual Conduct) Act 1994 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the sexual conduct position for` (`hrsc-rules.l4`). It answers:

- whether everyone involved is an adult;
- whether the conduct is protected by s 4(1);
- whether an interference with it under a law of the Commonwealth, a State or a Territory is barred.

The operative s 4 is encoded, with s 3 (external Territories) assumed. The source is the compilation prepared on 5 August 2009 (C2009C00395).

## Seat

The encoding is written from the seat of **the adult whose private sexual conduct is in question**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is my conduct protected by s 4, and may a law interfere with it?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | assumed: the Act extends to every external Territory |
| s 4 | encoded |

## Forks (readings taken)

- **F1, s 4(2).** A person is 18 from the eighteenth anniversary of birth. A 29 February birthday falls on 28 February in a common year.
- **F2, s 4(1), "arbitrary interference ... within the meaning of Article 17".** Whether an interference is arbitrary is a judgment for the courts, and it is an input. The answer is conditional on it.
- **F3 (changed after the independent pass).** Section 4 does not reach an interference under any other law, so it does not bar it: the answer is FALSE.
- **F4 (changed after the independent pass).** Conduct must involve at least one person; an empty list is not protected.
- **Known limits (from the independent pass).** The 28 February rule for 29 February birthdays comes from the brief, not the Act. Conduct before the Act commenced (Royal Assent, not in the text) is not handled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 34 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`hrsc-tests.l4`), 25 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
