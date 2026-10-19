# Electricity Act 1989 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the electricity customer position for` (`ea89-goal.l4`). It answers:

- **Connection:**
  - whether the distributor must connect the premises, or maintain the connection;
  - the earliest day it may disconnect a maintained connection under s 17(1)(c);
  - the last day to refer a connection dispute to Ofgem;
  - the interest on a security deposit.
- **Non-payment:**
  - from when the supplier may fit a pre-payment meter or disconnect for unpaid charges, and whether it may on the day;
  - whether its officer may enter;
  - whether restoring the connection oneself is an offence.
- **Redress and resale:**
  - whether a consumer redress order can be made for the supplier's contravention;
  - whether the order's compliance date is lawful, the supplier's last day to appeal, and from when interest runs on unpaid compensation;
  - the most compensation in all;
  - what can be recovered on electricity resold above the maximum price.

Three goals sit under it:

1. **Connection** (`ea89-connection.l4`): ss 16(1), (4), 16A(1)-(2), 17, 20(1A), (3), 22(2) and 23(1C).
2. **Non-payment, and entry** (`ea89-nonpayment.l4`): Schedule 6 paras 2, 5, 7(4)-(5), 8(3)(a), (4) and 10(4).
3. **Redress and resale** (`ea89-redress.l4`): ss 27G(1), (5), 27K, 27M(2), (5), 27N(1)-(2), (4), 27O(2)-(4) and 44(2)(b), (4).

Working days (s 64(1)) are in `ea89-days.l4`. Good Friday is computed from Easter, Christmas Day is fixed, and the bank holidays are an input list.

The source is the revised text at 24 July 2026. Dates are computed as the Act words them.

## Seat

The encoding is written from the seat of **the electricity customer**: the owner or occupier who wants a connection, is supplied, or was affected by the supplier's breach. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Must the distributor connect my premises, or keep them connected; when can it disconnect me; what interest is due on my security; until when can I refer a dispute? Can my supplier fit a pre-payment meter or disconnect me for unpaid charges, from when; may its officer enter; can I restore the connection myself? And if Ofgem acts on my supplier's breach, can a redress order still be made, by when must I be paid, and what can I recover on electricity resold to me?"

The facts it asks for are ones that person can state, or findings made about them: the distributor's circumstances under s 17, and the Authority's view under s 27N(2).

The redress-order provisions address the Authority and the supplier. The encoding gives what they mean for the customer: whether an order can still be made, when payment is due, and when interest runs.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-15A | out of scope: the regulators, licensing, licence modification |
| s 16 | (1)(a), (4) encoded (goal 1); (1)(b) (distributor-to-distributor) and (2A) are out of scope |
| s 16A | (1)-(2) encoded (goal 1); the offer of terms, (3)-(6), is not computed |
| s 17 | encoded (goal 1) |
| s 19 | out of scope: the expenses "reasonable in all the circumstances" are not computed |
| s 20 | (1A), (3) encoded (goal 1) |
| s 21 | out of scope: the additional terms |
| s 22 | (2) encoded (goal 1) |
| s 23 | (1C) encoded (goal 1); the determination is not |
| ss 24-27F | out of scope: enforcement orders (an input) and penalties (only the amount enters, through s 27O(4)) |
| ss 27G-27O | encoded as for the Gas Act 1986 ss 30G-30O (goal 3) |
| ss 28-43B | out of scope: information powers, safety, the renewables obligation, consents, standards of performance |
| s 44 | (2)(b), (4) encoded (goal 3) |
| ss 44B onwards | out of scope |
| s 64(1) "working day" | encoded |
| Schedule 6 para 2 | encoded (goal 2) |
| Schedule 6 para 5 | encoded (goal 2): whether there is consent |
| Schedule 6 paras 7(4)-(5), 8(3)(a), (4), 10(4) | encoded (goal 2) |
| Schedule 6 other paragraphs | out of scope |
| Schedule 7 and the other Schedules | out of scope |

## Forks (readings taken)

- **F1, s 17(1)(c) and (3).** For a new connection, s 17(1)(c) is an exception like the others. For a maintained connection, s 17(1)(c) allows disconnection only after the notice. Other s 17 grounds need no notice.
- **F2, "not less than seven working days' notice" (s 17(3), Sch 6 para 2(2)(b)) and "at least two working days' notice" (paras 7(5), 8(4)).** The act may be done on or after the seventh (or second) working day after the day of the notice; the notice day itself is not counted. The Gas Act 1986 encoding counts "not less than 7 days' notice" the same way (notice day + 7).
  - **Disagreement from the independent pass, left open.** The tester reads these as clear working days: neither the notice day nor the act day counts, and the act falls on the next working day. Notice on Monday 30 March 2026 then gives Monday 13 April, where the encoding gives Friday 10 April. Notice on Thursday 2 April gives entry from Thursday 9 April, not Wednesday 8 April.
  - The tester cites *Re Railway Sleepers Supply Co* (1885) and *R v Turner* [1910] for the clear-days rule.
  - The tester's two assertions are left failing (`tests-independent.l4` lines 142 and 201). Its other assertions on these periods follow the brief's reading and pass.
- **F3, s 20(3).** Interest is paid for every whole 50p and every whole three months, at the rate fixed per 50p per three months.
- **F4, s 23(1C), "12 months beginning with".** The period ends on the day before the corresponding date, or on the last day of the month where there is none.
- **F5, Sch 6 para 2(1).** Once the 28 days have passed unpaid, a later payment does not end the power. This follows the Gas Act 1986 independent pass (D3).
- **F6, Sch 6 para 2(2)(b).**
  - The notice may be given at any time on or after the demand, so it can run during the 28 days.
  - The earliest day to act is the later of the day after the 28 days and the seventh working day after the notice.
  - The Gas Act's para 7(3) reads "after giving ... notice" in a sub-paragraph that applies only once the time has passed. Para 2(2)(b) is a bare restriction on exercise.
- **F7, entry.** The entry is taken to be on the day of the action. Entry needs the power to act on that day, a reasonable time, the two working days' notice and the document (para 10(4)).
- **F8, ss 27G-27O and 44.** These are read as for the Gas Act 1986 ss 30G-30O and 37, including 5 years "from" as the corresponding date and an appeal within 42 days suspending compliance.
- **Known limits (from the independent pass).**
  - Para 5: the exception for disconnections under s 29 regulations is not modelled, and the offence answer turns only on consent.
  - s 17(1)(b) and s 17(2) are each one input.
  - Para 2(2)(a): a genuine dispute bars the whole debt, and a s 39 dispute must be left out by the caller.
  - A notice of intention given before the demand gives no power.
  - A maintained connection with a s 17(1)(c) finding still reports "must maintain"; the disconnection goal gives the earliest day.
  - s 27N(1) gives the day interest starts, not its amount.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 8 modules: 198 assertions satisfied, 2 failed, 0 other errors — 101 the encoder's (`ea89-tests.l4`), 99 independent (`tests-independent.l4`). Two assertions in `tests-independent.l4` (lines 142 and 201) are expected to fail: they take the clear-days reading of working days' notice (F2).

## Open questions for a UK lawyer

- **F2:** are "not less than seven working days' notice" and "at least two working days' notice" clear working days? If so, the earliest day moves one working day later, and the Gas Act 1986 encoding's "not less than 7 days' notice" should be read the same way.

- **F6:** may the para 2(2)(b) notice be given before the 28 days have passed?
