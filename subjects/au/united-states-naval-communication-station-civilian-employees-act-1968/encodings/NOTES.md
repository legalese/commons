# United States Naval Communication Station (Civilian Employees) Act 1968 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the station position for` (`usnc-rules.l4`). It answers:

- whether the Act applies;
- that the compensation Act then applies;
- whether damages are recoverable from the Commonwealth.

The encoded provisions are ss 3(2), 4, 5(1) and 6(1)-(2).

## Seat

The encoding is written from the seat of **the civilian employee at the Station**, or a dependant. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does this Act apply to me; am I covered by the Commonwealth Employees' Compensation Act; and can I recover damages from the Commonwealth?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | applied: an instrumentality counts as the US Government (s 3(2)) |
| s 4 | encoded |
| s 5 | (1) encoded; (2) and the Schedule (modifications of the compensation Act) are out of scope |
| s 6 | (1)-(2) encoded; (3)-(4) are out of scope |

## Forks (readings taken)

- **F1, s 6(1)-(2).** Injury, disease or death on or after 29 August 1966 is covered: s 6(2) before commencement, s 6(1) after. The hypothetical entitlement to damages is an input.

- **Known limits (from the independent pass).** Several inputs are combined: the US Government with its instrumentalities, citizen with national, and the two kinds of agreeing body (an association recognised by the Fair Work (Registered Organisations) Act is included in "an Australian union"). Who recovers (worker or dependant), and which subsection grounds the claim, are not reported. The s 6(2) hypothesis reuses the s 6(1) inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 29 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`usnc-tests.l4`), 20 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
