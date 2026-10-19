# Communications Act 2003 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the end-user position for` (`ca03-goal.l4`). It answers:

- **Ending a contract early:**
  - the most I can be made to pay;
  - whether the rights cover a whole bundle;
  - whether I may end the whole bundle for one element's failure.
- **TV licensing:**
  - whether using a receiver would be an offence;
  - whether I meet a concession's age, and whether that age is allowed;
  - the last day a search warrant can be used.
- **Misuse of a network:**
  - whether conduct is an offence under s 127, the last day to prosecute, and whether the prosecution is in time;
  - on a notification of persistent misuse: the shortest representation period, whether the period given is long enough, and whether Ofcom may act on the day;
  - whether a penalty is within £2,000,000.

All three goals sit in `ca03-rules.l4`:

1. **Ending a contract early:** ss 51(8)-(9), 124U(1)-(4) and 124V.
2. **TV licensing:** ss 363(1)-(3), (5)-(6), 365A(2), 366(4) and 368(3).
3. **Misuse of a network:** ss 127(1)-(2), (4)-(5), 128(3)-(4), 129(1), 130(1) and (4).

The source is the revised text at 6 April 2026. Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the individual end-user**: the phone or broadband customer, the television viewer, and the person accused of misusing a network. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "If I end my phone or broadband contract early, what can I be made to pay, and does it cover the whole bundle? Do I need a TV licence; do I meet the age for a concession; until when can a search warrant be used? If I am accused of misusing a network: is it an offence, can I still be prosecuted, how long must Ofcom give me to answer, and what is the most it can fine me?"

The facts it asks for are ones that person can state, or findings made about them, such as Ofcom's view that a case is urgent and the prosecutor's certificate of the evidence date.

## Coverage

| Provision | Disposition |
|---|---|
| Part 1 (ss 1-31) | out of scope: Ofcom |
| ss 32-51(7) | out of scope: the regime of conditions |
| s 51(8)-(9) | encoded: "bundled contract" is an input; "qualifying end-user" is the kind of end-user |
| ss 52-124T | out of scope |
| s 124U | (1)-(4) encoded (goal 1) |
| s 124V | encoded (goal 1) |
| ss 124W-126 | out of scope |
| s 127 | (1)-(2), (4)-(5) encoded (goal 3); (6) (Scotland) has the same limits; (7) makes the evidence date an input |
| s 128 | (3)-(4) encoded (goal 3); persistent misuse itself ((1), (5)-(7)) is Ofcom's determination |
| s 129 | (1) encoded (goal 3) |
| s 130 | (1), (4) encoded (goal 3) |
| ss 131-362 | out of scope: spectrum, broadcasting, competition |
| s 363 | (1)-(3), (5)-(6) encoded (goal 2) |
| ss 364-365 | out of scope: licence terms and fees, which are set by the BBC and regulations |
| s 365A | (2) encoded (goal 2) |
| s 366 | (4) encoded (goal 2) |
| s 368 | (3) is folded into the input |
| Part 4A onwards | out of scope |

## Forks (readings taken)

- **F1, s 124U(2)(b).** The proportion of the agreed equipment value is the unexpired months ÷ the agreed months. No other compensation is due, so the answer is 0 if the equipment is not kept.
- **F2, s 124U(3).** For a machine-to-machine service, s 124U applies only to a qualifying end-user under s 51(9)(a)-(c).
- **F3, s 124U(4).** The bundle rights can be waived only by a business or not-for-profit body with no more than 10 workers. An individual's rights cannot be waived.
- **F4, s 365A(2).** Age is judged on the last day of the month of issue. A person attains an age on the anniversary of birth; for a 29 February birthday, that is 28 February in a common year.
- **F5, s 366(4).** A warrant may be used up to and including the corresponding date one month after it was granted.
- **F6, s 127(5).** The last day is the earlier of the end of the 3 years beginning with the offence and the end of the 6 months beginning with the evidence date. Each ends on the day before the corresponding date.
- **F7, s 128(3).** "Not less than ... seven days" means the period ends on or after the notification day + 7. "One month" means it ends on or after the corresponding date one month on. This is the Gas Act 1986 reading (notice day + N), not clear days.
- **F8, ss 129(1)(c), 130(1)(c).** Ofcom may act only on a day after the period's last day, and only if the period was long enough.
- **Known limits (from the independent pass).**
  - s 363(3) (possession with intent) is not encoded.
  - One input stands for both "installed or used" (s 363(1)) and the s 368(3) meaning of use.
  - "Bundled contract" (s 51(8)) is an input.
  - The s 124U(2)(b) share is not guarded against nil agreed months or unexpired months above the agreed months.
  - s 124V reuses the general right-to-terminate input.
  - The Scottish rule in s 127(6) is not separately modelled, and an information laid before the offence is not checked.
  - For the warrant, only the last day is given.
  - s 365(5A)-(5B) are out of scope.
  - Urgency under s 128(4) is one input.
  - A negative penalty is not checked.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 5 modules: 161 assertions satisfied, 0 failed, 0 other errors — 66 the encoder's (`ca03-tests.l4`), 95 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F7:** must Ofcom's period be counted in clear days?
- **F1:** does the unexpired proportion run in days or in months?
