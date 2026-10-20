# National Rental Affordability Scheme Act 2008 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the dwelling position for` (`nras-rules.l4`). It answers:

- whether it is a rental dwelling;
- the last day of the incentive period;
- whether the newness condition is met;
- whether this year's rent condition is met;
- whether this year's tenant or vacancy condition is met;
- the first and last days of the NRAS year containing the day asked about.

The encoded provisions are s 4 (rental dwelling, incentive period, NRAS year) and s 7(2), (3), (5). The source is the compilation of 5 December 2025.

## Seat

The encoding is written from the seat of **the investor who owns a dwelling under the Scheme**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is it a rental dwelling; does it meet the Act's conditions this year; when does the incentive period end, and which NRAS year am I in?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3A | out of scope: machinery, object, severability |
| s 4 | encoded: rental dwelling, incentive period, NRAS year; the other definitions are folded into the inputs |
| ss 5-6 | out of scope: the Scheme is made by regulations |
| s 7 | (2), (3), (5) encoded; (1), (4), (6)-(7) are out of scope |
| ss 8-12 | out of scope |

## Forks (readings taken)

- **F1, s 4 incentive period (changed after the independent pass).** "A 10 year period" that starts on a day ends on the day before its tenth anniversary; a period starting on 29 February ends on 28 February ten years on.
- **F2, s 7(2)(b)(ii).** "At least 20% less than the market value rent" means each charge is no more than 80% of the market value rent for the same period.
- **F3, s 7(2)(b)-(c).** In a year when the dwelling is rented for part of the time, both the tenant condition and the vacancy limit apply.
- **F4, s 4 NRAS year.** The first ran from 1 July 2008 to 30 April 2009; each later year runs from 1 May to 30 April.
- **Known limits (from the independent pass).**
  - No output says whether the start date is a valid incentive period start, or whether the tested year falls within the period.
  - There is no single conditions-met output.
  - Market value rent is one figure for the year.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 55 assertions satisfied, 0 failed, 0 other errors — 19 the encoder's (`nras-tests.l4`), 36 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
