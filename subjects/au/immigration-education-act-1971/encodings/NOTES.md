# Immigration (Education) Act 1971 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the English position for` (`ie-rules.l4`). It answers:

- whether I am eligible;
- whether the Minister must provide me tuition;
- the last day to register, the last day to start a course, and the last day of eligibility.

The encoded provisions are ss 3 (visa commencement day), 4A, 4B(1), 4C and 4D. The source is the compilation of 19 April 2021.

## Seat

The encoding is written from the seat of **the migrant seeking English tuition**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I eligible for free English tuition; must it be given to me; by when must I register and start, and when does my eligibility end?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | visa commencement day is an input; vocational English is an input |
| s 4 | out of scope: the power to provide courses |
| s 4A | encoded; the specified temporary visas are an input |
| s 4B | (1) encoded; (3) is noted |
| s 4C | (1)-(2) encoded; extensions (3)-(6) are an input in days |
| s 4D | (1)-(2) encoded; extensions (3)-(6) are an input in days |
| ss 4E-13 | out of scope |

## Forks (readings taken)

- **F1, ss 4C(2), 4D(2).** "The period of N months (5 years) starting on" the visa commencement day ends on the day before the corresponding day, or the month's last day where there is none.
- **F2, s 4C(2)(a).** The 6-month or 12-month limit follows the age on the visa commencement day; 18 is reached on the 18th birthday.
- **F3, ss 4C(1A), 4D(1A).** A visa commencement day on or before 1 October 2020 takes the person outside the time limits. The limits reach only persons who ever held a permanent or specified temporary visa, which the encoding takes as the first three statuses.
- **F4, s 4C(2).** A person who has not yet registered or started stays eligible until the last day passes; registering or starting late ends eligibility.
- **F5, s 4B(1)(b).** The person must have been 18 on the first day in Australia after the permanent visa came into effect, taken as the visa commencement day.
- **Known limits (from the independent pass).**
  - s 4B(1)(b) age is taken on the visa commencement day, which differs only if a specified temporary visa came first.
  - Status is one value, so a child of a permanent resident who also held a visa cannot be expressed.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 61 assertions satisfied, 0 failed, 0 other errors — 17 the encoder's (`ie-tests.l4`), 44 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** does a child with a permanent-resident parent, who never held a visa, fall under ss 4C-4D?
