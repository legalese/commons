# NOTES: the Employment Relations Act 2000 (New Zealand), dismissal and personal grievances, row `legalese-aswathy`

**Draft. No New Zealand employment lawyer has reviewed this encoding against the Act.**

## What is encoded

The computable rules of the Employment Relations Act 2000 (version as at 10 July 2026, from the text converted from the PCO XML) on whether a dismissed employee may bring a personal grievance, its time limits, and the limits on remedies. They sit under one top-level goal, `the grievance position for` (`era-goal.l4`). For an employment, a grievance and the remedy facts, it answers whether a trial provision or the high-earner threshold bars the grievance, whether it was raised in time, the last days to raise it and to commence proceedings, whether reinstatement and compensation are available, and the reimbursement the Authority must order. Three goals sit under it:

1. **Trial periods and high earners** (`era-access.l4`): ss 67A-67B, 67I-67J, 113A-113B.
2. **Raising a grievance and time limits** (`era-grievance.l4`, `era-dates.l4`): ss 114, 120, 142, with the Legislation Act 2019 working day and ss 55-56.
3. **Remedies** (`era-grievance.l4`): ss 123B-124, 128.

Modules: `era-types.l4` (nouns only), `era-dates.l4`, `era-access.l4`, `era-grievance.l4`, `era-goal.l4`; tests in `era-tests.l4` (encoder) and `tests-independent.l4` (independent author).

**Not encoded.** The test of justification (s 103A) and the size of compensation, which are for the Authority; good faith, bargaining, collective agreements, strikes, the employment standards and enforcement Parts, and the rest of the Act.

**Lost in conversion.** The s 67I(4) annual remuneration formula, read as remuneration × 364 ÷ days held. The s 113B(3) increase formula, read as (given − last) ÷ last. The paragraph letters of s 103(1): the encoding uses the inserted letters (da) and (ja).

## Coverage

| provision | heading | disposition |
| --- | --- | --- |
| s 67 | probation | inert: it does not affect unjustifiable dismissal law |
| s 67A | trial provisions | encoded |
| s 67B | effect of a trial provision | encoded: (1)-(3); (4)-(5) good-faith modifications not |
| s 67I | high earners: annual remuneration | encoded: (4); (2)-(3) good-faith modifications not |
| s 67J | opting out | encoded |
| s 103(1) | grounds | encoded (an input) |
| s 103A | test of justification | out of scope: the Authority's judgement |
| s 113A | high earners may not bring a dismissal grievance | encoded |
| s 113B | threshold and its increase | encoded |
| s 114 | raising a grievance | encoded: (1), (3)-(4), (6)-(7) |
| s 115 | exceptional circumstances | an input (leave) |
| s 120 | statement of reasons | encoded |
| s 123 | remedies | inert (their limits are encoded) |
| ss 123B-123C | contributing behaviour | encoded |
| s 124 | reduction for contribution | encoded |
| s 128 | reimbursement | encoded: (2); (3) discretion not |
| s 142 | other actions: 6 years | encoded |

## Fork register

| fork | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 67I(4) | The formula lost in conversion | Remuneration × 364 ÷ days held | Its items; a full year gives the remuneration itself |
| F2 | s 113B(3)-(4) | The formula lost; rounding | Threshold × given ÷ last; halves round up | Its items; ordinary rounding (changed after the independent pass from half-to-even) |
| F3 | ss 114, 120, 142 | Does Legislation Act s 55 extend a period ending on a non-working day? | Yes: to the next working day | s 55 applies to anything to be done within a period; the independent author agreed |
| F4 | s 114(7) | When do 90 days and 12 months "beginning with" a day end? | 90 days: the 89th day after; 12 months: Legislation Act s 56 | s 56 (changed after the independent pass for 29 February) |
| F5 | s 67B(1) | "Before the end of the trial period" | Notice on or before the trial's last day | The period includes its last day; s 55 does not extend it |
| F6 | ss 67B(3)(b), 113A(3)(b) | Which grounds does "(c) to (k)" save? | All grounds after (b), using the inserted letters (da), (ja) | The usual practice for inserted paragraphs; the independent author's positional reading differs (3 assertions fail) |
| F7 | s 124(2) | A reduction above 100% or below 0 | Refused | "by up to 100%" (changed after the independent pass) |

## Results

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-16:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `era-tests.l4` (encoder) | 0 | 38 | 0 |
| `tests-independent.l4` | 3 | 102 | 3 |
| the 5 rule modules | 0 | 0 | 0 |
| **total** | 3 | 140 | 3 |

**3 failures are expected**, which is why `check.sh` exits non-zero: they are the independent author's reading of the s 103(1) letters (fork F6).

The independent pass (`INDEPENDENT-TEST-REPORT.md`) also found two real errors, both fixed: rounding to even under s 113B, and the end of a 12-month period that begins on 29 February. It also led to a reduction over 100% being refused rather than clamped. **The encoder's test that encoded the clamp was removed** and marked.

**Known limits.** Matariki Observance Days are an input. The grounds, findings and remuneration figures are inputs. A trial provision is assumed to start with the employment.

## Open questions for a New Zealand employment lawyer

1. F6: what are the PCO letters of the s 103(1) grounds for remuneration disclosure and whistleblower retaliation? Does "(c) to (k)" in ss 67B(3) and 113A(3) cover them?
2. F1 and F2: what are the s 67I(4) and s 113B(3) formulas? The converted text lost them.
