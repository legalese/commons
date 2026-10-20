# Federal Proceedings (Costs) Act 1981 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the costs position for` (`fpc-rules.l4`). It answers:

- whether the court may grant me a certificate;
- the most the Attorney-General may pay;
- whether my certificate is vacated;
- whether the Attorney-General may pay now.

The encoded provisions are ss 6-10A (as routes), 14, 15, 16(2), 17(1)-(2), 18 and the Schedule. The source is the compilation of 10 June 2025.

## Seat

The encoding is written from the seat of **the litigant who seeks a costs certificate**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can the court give me a costs certificate; what is the most the Attorney-General can pay me; can my certificate be vacated; can I be paid now?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | out of scope: machinery; definitions folded into the inputs |
| ss 6-10A | the route is an input; the conditions of each are folded into it |
| ss 11-13 | out of scope |
| s 14 | encoded |
| s 15 | encoded |
| s 16 | (2) encoded; (1) is noted |
| s 17 | (1)-(2) encoded; (3)-(4) (repayment) are out of scope |
| s 18 | encoded |
| ss 19-22 | out of scope |
| Schedule | encoded |

## Forks (readings taken)

- **F1, ss 6-10A.** The court's grant is discretionary ("may"); the encoding answers whether it may, not whether it will.
- **F2, s 18(2).** The cap does not apply to certificates under s 10(2)-(3) (abortive or discontinued proceedings); the payment is then limited only by the costs (s 16(2)).
- **F3, s 17(2).** For a certificate that can be vacated, the Attorney-General may pay only where the other side has not appealed or sought leave and a notice of no intended appeal has been given.
- **F5, s 15(1), 17(2): disagreement from the independent pass, left open.** For a s 6 certificate, s 15(1) vacates it when the holder (the respondent to whom it was granted) appeals further and succeeds; ss 15(2)-(3) turn on the other side. The encoding has a single input for "the other side appealed further and succeeded", so it applies the (2)-(3) test to s 6 certificates too. The tester's assertion (`tests-independent.l4` line 91) is left failing; fixing it needs a separate input for the holder's own further appeal.
- **F4, s 18(1).** A higher amount prescribed by regulation replaces the Schedule's figure.
- **Known limits (from the independent pass).**
  - The "satisfied" limb of s 17(1) is not modelled, so a vacatable certificate is never paid without a notice.
  - Routes are not checked against the forum (s 9, s 10(1), s 10A).

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 54 assertions satisfied, 1 failed, 0 other errors — 17 the encoder's (`fpc-tests.l4`), 38 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 91) is expected to fail: it applies s 15(1) to the holder's own further appeal (F5).

## Open questions for an Australian lawyer

- None of substance.
