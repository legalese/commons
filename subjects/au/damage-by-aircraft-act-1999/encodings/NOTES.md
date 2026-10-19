# Damage by Aircraft Act 1999 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the aircraft harm position for` (`dba-rules.l4`). For a person on the ground harmed by an aircraft, it answers:

- whether the Act applies;
- who is jointly and severally liable;
- whether damages are recoverable without proof of fault;
- the damages after any reduction for the person's own negligence.

The operative provisions are encoded: ss 4-7, 9, 10, 11 and 11A, with the application provisions in endnote 3. The source is the compilation in force on 31 March 2013 (C2013C00130).

## Seat

The encoding is written from the seat of **the person on the ground**: the person who suffered injury, loss or damage, or whose property did. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Does the Act apply to what happened to me; who is liable to me; can I recover without proving negligence; and by how much are my damages reduced if I was partly to blame?"

The facts it asks for are ones that person can state, or that come out in evidence or as findings of the court.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery and the object |
| s 4 | "aircraft" excluding model aircraft is applied; the other definitions are folded into the inputs |
| ss 5-7 | "in flight", "operator" and employees' use are folded into the cause and people inputs |
| s 8 | inert |
| s 9 | encoded: (2)-(4); (1) (external Territories) is folded into "within Australian territory" |
| s 10 | encoded |
| s 11 | encoded |
| s 11A | encoded |
| s 11B | out of scope: contribution between those liable |
| s 12 | out of scope |
| Endnote 3 (Act No. 191, 2012, Sch 1 item 7(3)-(4)) | applied: s 10(1A) and s 11A from 31 March 2013 |

## Forks (readings taken)

- **F1, endnote 3.** Item 5 (s 10(1A)) applies to mental injury suffered on or after 31 March 2013. Item 6 is taken to be s 11A (contributory negligence), applying to harm suffered on or after that date. Before it, the Act makes no reduction, and the answer is NOTHING.
- **F2, s 11A(3).** "Reduced to the extent the court thinks just and equitable having regard to the share of the sufferer in the responsibility" is taken as a reduction by the share the court assesses, as a percentage.
- **F3, s 10(2)(a).** The operator is always liable when s 10 applies. Who the operator is (ss 6-7) is the caller's input.
- **F4, s 10(2A).** The owner escapes only if it had no active role, and someone else had the exclusive right to use the aircraft under a lease or arrangement, or with the owner providing financial accommodation.
- **Known limits (from the independent pass).**
  - An owner who also authorised the use: s 10(2A) ("Subsection (2) does not apply to a person") should also take a passive, leasing owner out of s 10(2)(c). The encoding treats owner and authoriser as separate people, with no input to say they are the same.
  - s 9(4), and "more than 14 consecutive days", are single inputs.
  - s 11A(1) needs a defendant to prove the sufferer's negligence; a 0% share stands for "not proved".
  - A share outside 0-100 is clamped; the Act is silent.
  - ss 5-7 (in flight, operator, employees) are left to the caller's inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 4 modules: 66 assertions satisfied, 0 failed, 0 other errors — 26 the encoder's (`dba-tests.l4`), 40 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** confirm that item 6 of Act No. 191, 2012, Schedule 1 inserted s 11A (and s 11B).
