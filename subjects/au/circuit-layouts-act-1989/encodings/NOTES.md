# Circuit Layouts Act 1989 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the layout position for` (`cla-rules.l4`). It answers:

- whether the layout is protected (an eligible layout);
- the day its protection period ends;
- whether my act infringes;
- whether an action lies against me;
- whether damages may be awarded, rather than only an account of profits;
- the last day I can be sued.

The encoded provisions are ss 5, 6, 7, 10(b), 11, 17, 19-25, 27(2)-(3) and 28. The source is the compilation prepared on 12 October 2012. The Proclamation day for Part II is an input; the deposited text does not give it.

## Seat

The encoding is written from the seat of **the person who copies a circuit layout, makes a chip to it, or commercially exploits it in Australia**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is this layout protected, and until when; does what I do infringe; can damages be awarded against me; until when can I be sued?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope: machinery; the Part II commencement day is an input |
| s 5 | encoded: eligible layout, protection period; eligible person and eligible foreign country are inputs |
| s 6 | applied: folded into whether the maker was an eligible person |
| s 7 | encoded |
| ss 8-9 | applied: commercial exploitation and exclusive right are the kinds of act |
| s 10 | (b) encoded: the layout is made when first fixed; (a) applied |
| s 11 | encoded |
| s 12 | applied: licence is an input |
| s 13 | applied: a substantial part counts as the layout |
| ss 14-15, 18 | applied: folded into whether the maker was an eligible person |
| s 16 | out of scope: ownership |
| s 17 | encoded |
| s 19 | encoded |
| s 20 | encoded |
| s 21 | encoded |
| s 22 | encoded |
| s 23 | (1)(a), (2)(a) encoded; (1)(b)-(d), (2)(b)-(d) (a new original layout) are out of scope: a new original layout is not this layout |
| s 24 | (1) encoded; (2)-(3) (copyright) are out of scope |
| s 25 | (1) encoded as one input; (2)-(7) are out of scope |
| s 26 | out of scope |
| s 27 | (2)-(3) encoded; (1), (4) are out of scope |
| s 28 | encoded |
| ss 29-48 | out of scope: exclusive licensees, evidence, jurisdiction, eligible countries, dealings, groundless threats, regulations |

## Forks (readings taken)

- **F1, s 5 protection period.** "Within 10 calendar years after the calendar year in which the layout was made" is read as a first-exploitation year no later than the making year + 10. Then the period ends on 31 December of the exploitation year + 10; otherwise on 31 December of the making year + 10.
- **F2, s 19(3).** Only commercial exploitation needs knowledge (or that I ought reasonably to know) that I am not licensed; copying and making do not.
- **F3, s 20.** It covers commercial exploitation only. Once I am, or could reasonably be expected to be, aware, the protection continues only if I pay equitable remuneration.
- **F4, ss 21-23.** They excuse copying and making, not commercial exploitation.
- **F5, s 28.** "After the end of 6 years after the day when the infringement took place": the last day to sue is the corresponding day 6 years later, and 28 February for an act on 29 February.
- **F6, s 7.** An infringement before Part II commenced is still reported as infringing, but no action lies for it.
- **Known limits (from the independent pass).**
  - The 29 February limitation case (28 February or 1 March) was left open.
  - s 23(1)(b)-(d), the "authorises" limbs, and ss 6, 13 and 15 are not separate inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 68 assertions satisfied, 0 failed, 0 other errors — 29 the encoder's (`cla-tests.l4`), 39 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F5:** does the 6-year period end on the anniversary of the infringement, or the day before?
