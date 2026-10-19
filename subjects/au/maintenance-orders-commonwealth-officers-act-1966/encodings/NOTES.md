# Maintenance Orders (Commonwealth Officers) Act 1966 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the amounts paid under each order for` (`moco-rules.l4`), answering the question below. The scope is set out in BRIEF.md.

## Seat

The encoding is written from the seat of **the person whose Commonwealth pay is subject to a maintenance order**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can my Commonwealth pay be attached to enforce a maintenance order; and if there are several orders, how is my pay split between them?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope |
| s 5 | encoded |
| s 6 | (1), (3) encoded; (2) applied |
| s 7 | (1), (3) encoded; (2) (Matrimonial Causes Act orders) is out of scope |
| s 8 | out of scope |

## Forks (readings taken)

- **F1, s 7(1).** Orders are applied from the earliest in force; each takes what it requires from what is left, and nothing once the earnings run out.
- **F2, s 7(3).** A varied order keeps its first date, which is the input.
- **F3.** How much each order requires on an occasion is set by the State or Territory law. It is an input.

- **Known limits (from the independent pass).** The s 7(3) date is the caller's to supply. All orders are against the one person. Orders that came into force on the same day are taken in list order; the Act is silent.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 16 assertions satisfied, 0 failed, 0 other errors — 5 the encoder's (`moco-tests.l4`), 11 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
