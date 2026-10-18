# Third Parties (Rights against Insurers) Act 2010 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the third party position for` (`tprai-goal.l4`). For a third party owed a liability by an insured, it answers:

- whether the insured's rights against its insurer have been transferred;
- whether the third party may enforce them now;
- the amount due from the insurer;
- the amount it may still enforce against the insured;
- the last days to provide information and to serve a list of documents.

Three goals sit under it:

1. **Transfer of rights** (`tprai-transfer.l4`): ss 1(1)-(2), 4-7 (the event is an input, with the limits in ss 4(4), 5(1), 6(5)-(6) and 6A(2)-(3)), 15, 16, and Sch 3 paras 1 and 3.
2. **Recovery and enforcement** (`tprai-recovery.l4`): ss 1(3)-(4), 8, 9(3)-(6), 10, and 14(1), (6)-(7).
3. **Information and disclosure** (`tprai-information.l4`): Sch 1 paras 1-4.

As the user asked, this covers only the sections those goals need.

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Coverage

| Provision | Disposition |
|---|---|
| s 1 | encoded (goals 1-2) |
| ss 2-3 | out of scope: the procedure for declarations; "established" (s 1(4)) is an input |
| ss 4-7 | encoded as an input event, with the limits in ss 4(4), 5(1), 6(5)-(6), 6A(2)-(3); (4)(5), 6(7), 7(2) re-transfer on recall are out of scope |
| s 8 | encoded (goal 2) |
| s 9(3)-(6) | encoded (goal 2); (2) (acts of the third party count) is out of scope |
| s 10 | encoded (goal 2) |
| s 11, Sch 1 paras 1-4 | encoded (goal 3); paras 5-7 are out of scope |
| s 12 | out of scope: limitation defences in proceedings |
| s 13 | out of scope: jurisdiction |
| s 14(1), (6)-(7) | encoded (goal 2); (2)-(3) arrangements are out of scope |
| s 15, s 16 | encoded (goal 1) |
| ss 17-21, Schs A1, 2, 4 | out of scope |
| Sch 3 paras 1, 3 | encoded (goal 1): the 1930 Act case is an input; para 2 (pre-commencement relevant persons) is folded into "an insolvency event" |

## Forks (readings taken)

- **F1, s 1(1)(a) or (b).** If the insured became a relevant person on or before the day the liability was incurred, route (a) applies; otherwise (b) does. This matters only for the "(b) only" events in ss 4(4) and 5(1), which therefore need the liability to come first, strictly.
- **F2, s 6(1) arrangements.** The rights transfer only where the liability stays with the body (s 6(5)) and the arrangement binds the third party (s 6(6)).
- **F3, ss 8 and 10.** The amount due is the lesser of the two liabilities, less set-off, and not below nothing.
- **F4, s 14(6)-(7).** The amount recoverable excludes any shortfall from the insurer's own insolvency and any fund-limit shortfall. Where the third party is eligible for the FSCS, an insolvency shortfall counts only if a claim was made, and only net of what the FSCS paid or owes.
- **F5, s 9.** A notice-of-claim condition is not "information or assistance" (s 9(4)). Prior discharge (pay to be paid) binds only in marine insurance, for liabilities other than death or personal injury.
- **F6, "the period of 28 days beginning with the day of receipt".** It ends on receipt + 27.
- **F7, the paragraph numbers.** The conversion drops the Schedule paragraph numbers. The encoding uses the printed order (paras 1-7).

- **Known limits (from the independent pass).**
  - "The liability is established" (s 1(4)) and the beliefs and conditions in Sch 1 paras 1 and 3 are each one flag.
  - There is no jurisdiction input: Sch 1 paras 3-4 do not apply in Scotland (s 21(4)).
  - Re-transfer on recall of a sequestration (ss 4(5), 6(7), 7(2)) and Sch 3 para 2(7) are not modelled.
  - Under s 9(3), the insured's status is treated as conclusive of "cannot be fulfilled because".

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18:

- 7 modules: 147 assertions satisfied, 0 failed, 0 other errors;
- 50 are the encoder's (`tprai-tests.l4`);
- 97 are independent (`tests-independent.l4`).

No assertion is expected to fail.

## Open questions for a UK lawyer

- **F1:** confirm that a liability incurred on the day the insured becomes a relevant person falls within route (a).
