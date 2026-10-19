# Trade Union and Labour Relations (Consolidation) Act 1992 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the worker position for` (`tulrca-goal.l4`). It answers:

- **Union membership and activities:**
  - whether a detriment or dismissal on union grounds is protected;
  - whether the qualifying period is disapplied;
  - the last day to complain of a detriment;
  - the last day for interim relief, and whether the application is in time;
  - the basic award before reductions, with the £9,157 minimum.
- **Collective redundancies:**
  - whether consultation was required, the last day for it to begin, and whether it began in time;
  - the protected period and my remuneration under a protective award;
  - the last days for the complaint of failure to consult and for the complaint of non-payment.
- **Protected industrial action:** whether the dismissal is unfair, and the last day to complain.

Three goals sit under it:

1. **Union membership and activities** (`tulrca-union.l4`): ss 146(1)-(3), (5A), 147(1)(a), (4), 152(1)-(3), 153, 154, 156(1) and 161(1)-(3).
2. **Collective redundancies** (`tulrca-redundancy.l4`): ss 188(A1), (1A), 189(4)-(5A), 190(2), 192(2)-(2A) and 195A.
3. **Protected industrial action** (`tulrca-redundancy.l4`): ss 238(5), 238A(1)-(2) and 239(1)-(2).

The s 292A extension for early conciliation is in `tulrca-periods.l4`.

The source is the revised text at 25 August 2026. It runs together some wording from before and after the Employment Rights Act 2025, such as s 188(A1) and (1) and the cap of 180 days in s 189(4). The amended version is encoded. Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the worker or employee**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "I was treated badly, or dismissed, because of my union membership or activities, or for not joining. Am I protected; by when must I complain; can I get interim relief, and by when; what is the least basic award? My employer is making collective redundancies: when should consultation have begun, what protective award can I get, and by when must the complaints be made? I was dismissed for taking part in official industrial action: is that unfair, and by when must I complain?"

The facts it asks for are ones that person can state, or findings made about them: the reason the tribunal finds, whether others were kept on, and the period the tribunal fixes.

## Coverage

| Provision | Disposition |
|---|---|
| Parts I-II (ss 1-136) | out of scope: unions, elections, political funds, members' rights against the union |
| ss 137-145F | out of scope: refusal of employment, refusal to deal, inducements (whether an offer contravened s 145A or 145B is an input) |
| s 146 | (1)-(3), (5A) encoded (goal 1); (2A)-(2D), (4) are folded into the reason input |
| s 147 | (1)(a), (4) encoded (goal 1); (1)(b) (late complaint) and (2)-(3) (when an act is done) are inputs |
| ss 148-151 | out of scope: consideration and remedies |
| s 152 | (1)-(3) encoded (goal 1); (4)-(5) are folded into the reason input |
| ss 153-154 | encoded (goal 1) |
| s 155 | out of scope: contributory fault |
| s 156 | (1) encoded (goal 1) |
| ss 159-160 | out of scope |
| s 161 | (1)-(3) encoded (goal 1); (6) affects only the certificate's content |
| ss 162-167 | out of scope: the hearing and orders |
| ss 168-187 | out of scope: time off, disclosure of information |
| s 188 | (A1), (1A) encoded (goal 2); (1B)-(8) (representatives and content) are out of scope |
| ss 188A-188B | out of scope |
| s 189 | (4)-(5A) encoded (goal 2); (1)-(3), (6) are inputs (that a protective award was made) |
| s 190 | (2) encoded (goal 2); (4)-(6) are folded into the days not payable |
| s 191 | folded into the days not payable |
| s 192 | (2)-(2A) encoded (goal 2) |
| ss 193-194 | out of scope: notifying the Secretary of State |
| s 195A | the threshold number is an input |
| ss 196-237 | out of scope |
| s 238 | (5) encoded (goal 3); the rest is out of scope |
| s 238A | (1)-(2) encoded (goal 3); whether the action is protected (s 219) is an input |
| s 239 | (1)-(2) encoded (goal 3); (3)-(4) are out of scope |
| s 292A | encoded |
| the rest of the Act | out of scope |

## Forks (readings taken)

- **F1, "N months beginning with" a day.** The period ends on the day before the corresponding date, or on the last day of the month where there is none.
- **F2, s 292A(3).** Only the days from the later of the day after Day A and the first day of the period, to Day B, are not counted. If Day A falls after the limit, (3) adds nothing. This is the reading the Employment Rights Act 1996 encoding took after its independent pass (s 207B).
- **F3, s 161(2), "before the end of the period of seven days immediately following the effective date of termination".** The application is in time by that date + 7. It may also be presented before the date of termination.
- **F4, s 188(1A)(a), "100 or more employees as mentioned in subsection (A1)" (changed after the independent pass).** This means 100 or more proposed to be dismissed as redundant within the 90 days, counted across the employer, whichever route of (A1) triggers the duty.
- **F5, s 188(1A), "at least 45 days ... before".** Consultation must begin on or before the first dismissal day − 45 (or − 30).
- **F6, s 189(4).** The protected period's last day is its first day + (days − 1), with at most 180 days. Remuneration is a week's pay × payable days ÷ 7.
- **F7, s 239(2).** This Act does not apply s 292A to s 239(2), so no extension for early conciliation is made.
- **F9, s 146(5A) (changed after the independent pass).** A worker who is not an employee keeps s 146, and the s 147 time limit, when the engagement is ended for a union reason. Only an employee's dismissal falls to ss 152-154 and 161.
- **F8, s 156(1).** The minimum applies wherever the dismissal is protected under s 152(1) or 153. A dismissal for refusing payments in lieu of membership counts, since s 152(3) treats it as within (1)(c).
- **Known limits (from the independent pass).**
  - s 161(6), the date of dismissal for the certificate, is not modelled.
  - A threshold number below 20 (s 195A(3)) is accepted, not refused.
  - s 189(5)(a): only the last day is given; a complaint before the last dismissal is in time.
  - The "not reasonably practicable" extensions are inputs left to the tribunal and are not computed.
  - s 156(2) is out of scope.
  - Where the employee resigns on notice, s 238(5)(a) does not apply; the effective date of termination is used.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 7 modules: 183 assertions satisfied, 0 failed, 0 other errors — 80 the encoder's (`tulrca-tests.l4`), 103 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F7:** does ERA 1996 s 207B, or anything else, extend the s 239(2) time limit for early conciliation?
- **F4:** is the 100 for the 45-day period counted across the employer, or at the establishment where only (A1)(b) applies?
