# Water Industry Act 1991 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the water customer position for` (`wia-goal.l4`). It answers:

- **Connections:**
  - whether the duty to connect has arisen, and the last day for the connection;
  - the interest on a deposit;
  - the last day the sewerage undertaker may refuse a drain, and whether a refusal was in time.
- **Disconnection for non-payment:**
  - whether the premises are protected by Schedule 4A;
  - the earliest day the water can be cut off, and whether it may be cut off on a given day;
  - whether a limiting device would be an offence.
- **Charges:**
  - the last day I can be charged for after leaving, or after a s 62 notice;
  - whether I may require a meter, and whether the undertaker must provide one;
  - the last day to revoke a meter;
  - whether the undertaker may impose one.

Three goals sit under it:

1. **Connections** (`wia-connection.l4`): ss 45(1)-(2), 47(1)-(3), 48(1), 51(1)-(3), (6) and 106(1), (3)-(4).
2. **Disconnection for non-payment** (`wia-disconnection.l4`): ss 61(1), (1ZA), (1A), (2)-(3), 63(3)(a), 63A(1) and Schedule 4A.
3. **Charges** (`wia-charges.l4`): ss 144(2)-(7), 144A(1)-(3), (5)-(7) and 144B(1)-(3).

Working days (s 144(7)) are in `wia-days.l4`. Good Friday is computed from Easter, Christmas Day is fixed, and the bank holidays in England and Wales are an input list.

The source is the revised text at 30 July 2026.

## Seat

The encoding is written from the seat of **the water customer**: the owner or occupier who wants a connection, is supplied and charged, or faces disconnection. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Must the water company connect my premises to its main, by when, and what conditions can it impose; what interest is due on my deposit; can the sewerage company still refuse my drain? Can my water be cut off for non-payment, from when; can a limiting device be used on my home? When I move out, until when am I liable for charges; can I insist on a meter, revoke it, or be put on one against my will?"

The facts it asks for are ones that person can state, or findings made about them, such as whether metering is reasonably practicable under s 144A(3).

## Coverage

| Provision | Disposition |
|---|---|
| Parts I-II | out of scope: the regulators, appointments, licences, enforcement |
| ss 37-44 | out of scope: supply duties, bulk supplies, requisitions |
| s 45 | (1)-(2) encoded (goal 1); (3)-(8) are out of scope (information, actions, charges) |
| s 46 | out of scope: ancillary works |
| s 47 | (1)-(3) encoded (goal 1): whether conditions were imposed in time, and when they were met; which conditions may be imposed is an input |
| s 48 | (1) encoded (goal 1) |
| ss 49-50 | out of scope |
| s 51 | (1)-(3), (6) encoded (goal 1); (5) (delay for missing information) is out of scope |
| ss 51A-60 | out of scope |
| s 61 | (1), (1ZA), (1A), (2)-(3) encoded (goal 2); the licensee route (1ZB)-(1ZC), (2A), and (4)-(6) are out of scope |
| s 62 | the notice is an input to s 144(5)-(6) |
| s 63 | (3)(a) encoded (goal 2); (1)-(2) (notice to the local authority within 48 hours) are out of scope |
| s 63A | (1) encoded (goal 2) |
| ss 63AA-105 | out of scope: licensees, constancy, quality, fluoridation, sewerage generally |
| s 106 | (1), (3)-(4) encoded (goal 1); the grounds of refusal are not tested |
| ss 106A-141 | out of scope |
| ss 142-143E | out of scope: charges schemes and rules |
| s 144 | (2)-(7) encoded (goal 3) |
| ss 144ZA-144ZF | out of scope |
| s 144A | (1)-(3), (5)-(7) encoded (goal 3); the period under (2), and the prescribed conditions under (5)(b), are not computed |
| s 144B | (1)-(3) encoded (goal 3); the prescribed conditions under (1)(c) are not computed |
| ss 144C onwards | out of scope |
| Schedule 4A | encoded as kinds of premises (goal 2) |
| other Schedules | out of scope |

## Forks (readings taken)

- **F1, s 45(2)(b) and s 47(3).** Only conditions imposed by a counter-notice within the 14 days beginning with the day after the connection notice count. Once such conditions are imposed, the duty arises only when they are satisfied.
- **F2, s 51(1)-(2).** A pipe already laid must be connected by the relevant day + 13. Otherwise the 21-day presumption gives the relevant day + 20. The presumption can be rebutted; that is not modelled.
- **F3, s 48(1).** Interest is paid for whole 50p sums and whole periods of three months.
- **F4, s 61(1ZA)(b).**
  - Payment by the notice day + 7 is in time, and the power arises on the notice day + 8.
  - A later payment does not end the power. This matches the reading of the Gas Act 1986 (D3) and the Electricity Act 1989.
  - To bar the power, the counter-notice must be served within the seven days beginning with the day after service: from the notice day + 1 to the notice day + 7. A counter-notice on the day of service is not within them; this was changed after the independent pass.
  - **Disagreement from the independent pass, left open.** The tester reads s 61(1ZA)(a)'s "is liable ... to pay charges due" as present: once paid, nothing is due, and the power ends. That assertion (`tests-independent.l4` line 124) is left failing. The tester's confidence is low.
- **F5, "two working days" (s 144(3), (6), (7)); changed after the independent pass.** The Act counts 48 hours, ignoring time on excluded days. Counted in days:
  - Informing on a working day is in time if the day of leaving is on or after the second working day after it.
  - Informing on an excluded day starts the 48 hours at the next working day, so leaving must be after the second working day: Saturday 17 October 2026 needs Wednesday 21 October.
  - The end of "two working days beginning with the service" is the second working day after the day of service.
- **F6, s 144(4).** The first relevant day is the earliest of the events that occur after the person leaves. A new occupier's notice given before then is ignored.
- **F7, s 144A(5).** The revocation period of 12 months ends on the day before the corresponding date, or on the last day of the month where there is none. The prescribed conditions of (5)(b) are assumed to be met.
- **Known limits (from the independent pass).**
  - s 51(3): whether the customer's part of the service pipe is laid is not an input; the pipe-laid notice date stands for it.
  - s 63A(1): the intention of enforcing payment is assumed.
  - s 61(2): continued occupation after a counter-notice is not checked.
  - s 144(4)(b): the meter reading day is taken as the next one after leaving; a reading before leaving is not filtered out.
  - s 144(5)(b) and the proviso for a demand made since the notice are not modelled.
  - The prescribed conditions of ss 144A(5)(b) and 144B(1)(c) are treated as met.
  - s 144B(2)(a) "not revoked" and (3) are folded into the inputs.
  - The date conditions were satisfied has no "as at" date.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 8 modules: 193 assertions satisfied, 1 failed, 0 other errors — 82 the encoder's (`wia-tests.l4`), 112 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 124) is expected to fail: it reads a late payment as ending the s 61 power (F4).

## Open questions for a UK lawyer

- **F5:** how is "48 hours ... disregarding" to be applied where informing or service is part-way through a day?
- **F4:** does a payment after the seven days but before the cut-off end the s 61 power?
