# War Gratuity Act 1945 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the gratuity position for` (`wg-rules.l4`). It answers:

- the months at the overseas rate and at the general rate;
- the war gratuity in dollars;
- that it is a free gift, which may be withheld or deferred.

The encoded provisions are ss 2 (month), 4, 6, 8, 12, 13, 14(1), 15 (as an input) and 16. The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the Second World War member, or their dependants**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "How much war gratuity is to be credited for my service?"

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | out of scope |
| s 2 | month (30 days) encoded; the other definitions are folded into the inputs |
| s 3 | applied |
| s 4 | encoded |
| s 6 | applied: a free gift (reported) |
| s 7 | the days of overseas qualifying service are an input |
| s 8 | encoded |
| ss 9-11 | the days of general qualifying service are an input |
| s 12 | encoded |
| s 13 | encoded |
| s 14 | (1) encoded; (2)-(3) (who receives the increase) are out of scope |
| s 15 | the disqualification is an input; the provisos are discretionary |
| s 16 | encoded as one debt figure |
| ss 17 onwards | out of scope |
| Schedule | an input |

## Forks (readings taken)

- **F1, ss 2, 12.** Days are converted to 30-day months, with any fraction counting as a whole month.
- **F2, ss 8, 12(2).** The deemed 12 months of overseas service are deducted from the general months too.
- **F3, s 14.** The minimum is 36 months at $7.50 ($270), including any s 13 addition.
- **F4, s 15.** A disqualified member's gratuity is nil; the prescribed authority's discretion to credit dependants or allow it is not modelled.
- **F5, s 16.** Debts are deducted after the s 14 minimum, not below nil.
- **Known limits (from the independent pass).**
  - s 8's three return reasons are one input.
  - s 14's total dependency and death before 1 July 1947 are one input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 32 assertions satisfied, 0 failed, 0 other errors — 14 the encoder's (`wg-tests.l4`), 18 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F2:** are the months deemed by s 8 deducted from the general months under s 12(2)?
