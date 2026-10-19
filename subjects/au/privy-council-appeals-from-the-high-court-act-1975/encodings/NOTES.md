# Privy Council (Appeals from the High Court) Act 1975 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `may I still ask for special leave from` (`pcah-rules.l4`). It answers whether a litigant may still ask for special leave to appeal from a High Court decision to Her Majesty in Council. The operative s 3 is encoded.

The source is the Act as made (No. 33 of 1975).

## Seat

The encoding is written from the seat of **the litigant**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "May I still ask for special leave to appeal from this High Court decision?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery (the commencement date is fixed by Proclamation and is an input) |
| s 3 | encoded |

## Forks (readings taken)

- **F1.** Section 3 applies only where special leave "could, but for this Act, have been asked" under s 3 of the 1968 Act. Whether it could is an input, and the 1968 Act is its own subject. Where it could not, this Act does not decide the question, and the answer is NOTHING.
- **F2.** Where special leave was open under the 1968 Act, it remains open only for a proceeding begun in a court before this Act commenced.
- **Known limits (from the independent pass).**
  - The module does not import the 1968 Act's encoding; whether special leave was open under it is a bare input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 10 assertions satisfied, 0 failed, 0 other errors — 4 the encoder's (`pcah-tests.l4`), 6 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
