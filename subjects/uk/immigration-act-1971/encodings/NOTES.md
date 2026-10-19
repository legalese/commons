# Immigration Act 1971 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the immigration position for` (`ia71-goal.l4`). For one person it answers:

- whether they have the right of abode, and whether they require leave to enter;
- whether limited leave is extended by s 3C on a given day;
- for an offence under s 24 or s 24B: the maximum imprisonment on indictment and on summary conviction, and the last day to lay an information on the s 28 extended time limits.

Three goals sit under it:

1. **Right of abode and the need for leave** (`ia71-status.l4`): ss 1(1)-(3), 2(1), 3(1) and 3ZA.
2. **Continuation of leave** (`ia71-status.l4`): s 3C(1)-(3).
3. **Offences** (`ia71-offences.l4`): ss 24(A1)-(G1), (1)(b), (c), (h), (3)-(3A), 24B(3)-(4), and 28(1)(a), (1A)(a).

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the person seeking to enter or remain**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Do I have the right of abode or need leave; is my leave still running while my application is decided; and if I am accused of an immigration offence, what is the maximum sentence and by when must I be prosecuted?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 3ZA | encoded (goal 1); s 2(2) is out of scope |
| ss 3-3B, 3D-4 | out of scope: leave and conditions |
| s 3C(1)-(3) | encoded (goal 2); (3A)-(7) are out of scope |
| ss 5-23 | out of scope: deportation, exemptions, the CTA, ETAs, appeals |
| s 24 | encoded (goal 3); the offences are an input category |
| s 24A | out of scope |
| s 24B | encoded (goal 3) as to sentence; whether the offence is committed is an input |
| ss 25-27 | out of scope |
| s 28(1)(a), (1A)(a) | encoded (goal 3); Scotland and Northern Ireland are out of scope |
| ss 28A onwards, Schedules | out of scope |

## Forks (readings taken)

- **F1, s 1(3) and s 3ZA(5).** A local journey within the common travel area needs no leave, except for an Irish citizen who is deported or excluded.
- **F2, s 3C(1)(b): "made before the leave expires".** An application made on the last day of leave counts.
- **F3, s 3C(1)(c), (2).** The application must be undecided when the leave expires. The leave is then extended on each later day while the application is undecided, or up to and including the last day of in-country appeal or review rights. It is not extended on or after the day of departure.
- **F4, s 24(F1)(a), (G1).** The "general limit in a magistrates' court" is an input. Whether the offence came before it applied is an input, because the Act refers to a commencement date it does not print.
- **F5, s 24B(4).** The 51 weeks in England and Wales apply unless the offence was committed before s 281(5) CJA 2003 came into force (an input).
- **F6, s 28(1)(a).** The last day is the later of two dates: the corresponding date six months after the offence; and the earlier of three years after it and two months after the certified evidence date.
- **F7, s 28(1A)(a).** For a bail condition breach, the last day is the later of the end of the six months beginning with the offence and the end of the three months beginning with the first arrest.
- **F8.** Overstaying, failing to observe a condition, and illegal working have no extended limit under s 24(3), so the answer is NOTHING.
- **Known limits (from the independent pass).**
  - **Whether an offence is committed is not encoded:** the offence is an input. The elements of ss 24 and 24B (knowledge, requiring leave, limited leave, the (E1A) journey limbs, s 24(1A), s 24B(2)) are not applied.
  - s 3ZA(2)-(4) is one input.
  - Only leave to enter is answered, not leave to remain.
  - s 3C's pending appeals and reviews are one end date.
  - The transitional readings in s 24(G1) and s 24B(4) are inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 6 modules: 138 assertions satisfied, 0 failed, 0 other errors — 40 the encoder's (`ia71-tests.l4`), 98 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F3:** is leave extended on the day the application is decided, when no appeal right follows?
