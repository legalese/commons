# Asbestos-related Claims (Management of Commonwealth Liabilities) Act 2005 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the asbestos position for` (`arc-rules.l4`). It answers:

- whether mine is an asbestos-related claim;
- whether I may claim against Comcare;
- who is liable to me;
- the day the liability passed to Comcare.

The encoded provisions are ss 3(1), 5 and 6(1)-(2). The source is the compilation of 1 July 2014; Part 2 commenced on 26 October 2005.

## Seat

The encoding is written from the seat of **the person with an asbestos-related condition who claims compensation or damages**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is mine an asbestos-related claim; may I claim against Comcare; who is liable to me now?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery; Part 2 commenced on 26 October 2005 |
| s 3 | (1) encoded: asbestos-related claim, condition, liability; the authority definition is folded into the inputs; (2) is out of scope |
| s 4 | out of scope: declarations, folded into the inputs |
| s 5 | encoded |
| s 6 | (1)-(2) encoded; (3)-(6) are out of scope |
| ss 7-16 | out of scope |

## Forks (readings taken)

- **F1, s 5(1) (changed after the independent pass).** A claim made against the Commonwealth or an authority on or before 26 October 2005 passes to Comcare on that day; a claim made against Comcare before then does not.
- **F2, s 5(2)-(3).** A later claim, against the Commonwealth, an authority or Comcare, passes when made. Until a claim is made, the Commonwealth or authority remains liable.
- **F3, s 6.** Only a liability that was an authority's can be transferred back, to the authority or its successor.
- **F5, s 5(3)(a) (changed after the independent pass).** Anyone who could make an asbestos-related claim may claim against Comcare, even where the liability is one the Act does not transfer.
- **F4, s 3(1) liability.** A liability under an insurance contract, an unstayed judgment not under appeal at commencement, or a written settlement made before commencement is outside the Act.
- **Known limits (from the independent pass).**
  - The "subject to appeal" boundary, s 6(1)(b) successors and when a s 6 declaration takes effect are not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 58 assertions satisfied, 0 failed, 0 other errors — 13 the encoder's (`arc-tests.l4`), 45 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
