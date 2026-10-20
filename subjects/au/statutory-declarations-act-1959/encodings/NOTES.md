# Statutory Declarations Act 1959 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the declaration position for` (`sd-rules.l4`). It answers:

- whether my declaration is validly made;
- whether this Act authorises the use I want;
- whether I commit an offence under s 11;
- the maximum imprisonment.

The encoded provisions are ss 6, 7A, 8, 9, 9A(1) and 11. The source is the compilation of 1 January 2024.

## Seat

The encoding is written from the seat of **the declarant**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is my statutory declaration validly made; can it be used for what I want; what if a statement in it is false?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5A | out of scope: machinery |
| s 6 | encoded |
| s 7 | out of scope: references in other laws |
| s 7A | encoded |
| s 8 | encoded |
| s 9 | encoded |
| s 9A | (1) encoded; (2)-(3) are folded into the inputs |
| s 9B | out of scope: platform obligations |
| s 10 | out of scope: declarations under other laws |
| s 11 | encoded |
| ss 12-16 | out of scope |

## Forks (readings taken)

- **F1, s 8.** A declaration is validly made only if it is in the approved form, signed by a method that satisfies s 7A, and made under either s 9 or s 9A.
- **F2, s 9(c)(ii).** Signing a true copy suffices only where the observation was by video link.
- **F3, s 6 (changed after the independent pass).** A declaration not validly made is not one the Act authorises the use of. Use as evidence in a judicial proceeding is not authorised (s 6(3)), though not prevented: FALSE. Other uses are outside s 6(2): FALSE.
- **F4, s 11.** The offence needs an intentionally false statement; the penalty is imprisonment for 4 years.
- **Known limits (from the independent pass).**
  - How the declaration was signed is not checked against how it was made (a platform declaration signed by hand is accepted).
  - The two limbs of s 7A(2)(b) are one input.
  - Whether s 11 reaches a declaration not validly made is untested.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 40 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`sd-tests.l4`), 25 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
