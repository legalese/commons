# Privy Council (Limitation of Appeals) Act 1968 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `may I ask for leave from` (`pcla-rules.l4`). It answers whether this Act bars a litigant from asking Her Majesty in Council for leave to appeal from a decision. The whole operative Act is encoded: ss 3-4.

The source is the compilation prepared on 7 November 2000 (C2004C00594).

## Seat

The encoding is written from the seat of **the litigant**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "May I ask the Privy Council for leave to appeal from this decision?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery (the commencement date is fixed by Proclamation and is an input) |
| s 3 | encoded |
| s 4 | encoded |

## Forks (readings taken)

- **F1.** The Act only limits. Where it does not bar asking, the answer is "this Act does not bar it", not a right to appeal. That includes decisions of courts the Act does not mention, such as a State Supreme Court; this was changed after the independent pass.
- **F2, s 3(2).** A proceeding begun in a court before the Act commenced is untouched by s 3(1), whatever its subject. Section 4 has no such saving and is applied to every case.
- **F3.** The later Privy Council (Appeals from the High Court) Act 1975 narrowed s 3 further. It is its own subject, and this encoding answers for this Act alone.
- **Known limits (from the independent pass).**
  - The three items in s 3(1)(b), and s 3(1)(a), are each one input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 19 assertions satisfied, 0 failed, 0 other errors — 7 the encoder's (`pcla-tests.l4`), 12 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F2:** does s 4 apply to proceedings begun before the Act commenced?
