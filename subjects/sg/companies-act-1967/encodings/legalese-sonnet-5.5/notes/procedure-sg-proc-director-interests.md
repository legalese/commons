## Procedure layer: a director's declaration of interest (Companies Act 1967 s 156) and loans and other restricted transactions in favour of a director (s 162)

Module `sg-proc-director-interests.l4`, tests `sg-proc-director-interests-tests.l4`.
It adds a regulative layer over the Boolean encodings in `sgb1-s156-interests.l4` and `sgb2-s162-loans-to-directors.l4`, and edits neither.
The parties are the corpus's own `Party` (`sg-core.l4`): a declarant, the company, the secretary and a director are each any `Party` the caller passes.
There is no constructor for a chief executive officer in `sg-core.l4`, so a chief executive officer who is not a director is passed as an `Officer` (fork on s 156(1)).
The acts are two new enums, `s 156 declaration act` and `s 162 loan act`.
Every rule is gated by the existing section function: where the gate does not answer `JUST TRUE` (or, for s 162(7), `JUST FALSE`), nothing is owed and the rule is `FULFILLED` at once.
Five new Boolean or numeric helpers sit in the module and are asserted in the tests (18 `#ASSERT` lines).

### The seat of each DEONTIC

- `s 156(1) the director or chief executive officer must declare the interest or send a written notice, and the company and the secretary follow`: the declarant MUST declare the interest at a meeting of the directors, HENCE the secretary MUST minute it (s 156(11)); or (`ROR`) the declarant MUST send a written notice, HENCE the company MUST send a copy to the directors (s 156(9)) and (`RAND`) the secretary MUST minute it in the next meeting after the notice, because s 156(10) deems the notice part of that meeting and s 156(10)(b) applies the minutes provision as if the declaration had been made there.
  Gate: `s 156(1) the director or chief executive officer must declare the nature of the interest or send a written notice`, which already takes in s 156(3) and (4).
- `s 156(6) the director or chief executive officer must declare the conflict, at the first meeting if by declaration`: the declarant MUST declare the conflict at a meeting, WITHIN the days from the day the person commenced to hold the office or property (or became a director) to the first meeting of the directors after it; or (`ROR`) MUST send a written notice (s 156(6)(b), (8)), which has no day.
  If the first meeting passes, the declaration route lapses into the written-notice duty.
  Gates: `s 156(6) the director or chief executive officer must declare the conflict or send a written notice`; the first meeting is `s 156(7) the meeting of the directors at which the declaration under subsection (6)(a) must be made`; day 0 is `s 156(8) the date after which the written notice under subsection (6)(b) must be given as soon as practicable`.
- `s 156(15) a director or chief executive officer must not fail to comply with a provision of section 156`: the declarant SHANT fail to comply, LEST BREACH BY the declarant, the BECAUSE text naming the offence and its penalty.
  Gate: `s 156(15) the person is guilty of the offence this subsection creates`.
- `s 162(2) the company must not make the restricted transaction unless it is exempt or an exception or an approval takes it outside the bar`: the company SHANT make it, LEST BREACH BY the company.
  Gate: an exempt private company, or a transaction within section 163A or 163B or (3)(c) or (d), or `s 162(3) and (4) the transaction is within paragraph (a) or (b) and subsection (4) authorises it` (a helper built on `s 162(4) subsection (3)(a) or (b) authorises the making of the restricted transaction` and `s 162(10) the approval counts as prior approval`).
- `s 162(4)(b) the amount must be repaid or the liability discharged within 6 months from the conclusion of the next annual general meeting`: the relevant director MUST repay or discharge WITHIN the days from the day of the transaction to the last day of the six months, LEST BREACH BY the company.
  The last day is `s 162(4)(b) the last day on which the amount or liability must be repaid or discharged`.
- `s 162(5) the directors who authorised the transaction must indemnify the company against the loss`: the authorising director MUST indemnify the company; gate `s 162(5) the directors who authorised the transaction are jointly and severally liable to indemnify the company against any loss`.
- `s 162(6) where the company contravenes section 162 a director must not authorise the making of the restricted transaction`: the director SHANT authorise it, LEST BREACH BY the director, the BECAUSE text naming the offence and its penalty; gate `s 162(6) the director is guilty of the offence`.
- `s 162(7) the company may recover the amount of a dealing made contrary to section 162`: the company MAY recover the amount; gate `s 162(7) section 162 operates to prevent the company from recovering the amount`, which must answer `JUST FALSE`.

### The TIMELINE lines

Copied from the module, in the order of the rules.

- s 156(1), (9), (10), (11): unit=calendar day; day 0=the day the relevant facts come to the director's or chief executive officer's knowledge; counting="as soon as is practicable after the relevant facts have come to his or her knowledge" (not a number of days, so no clock is encoded; for the written notice the same words run from the dates in subsection (2), and for the copy and the minutes the text sets no day at all)
- s 156(6) to (8): unit=calendar day; day 0=the day the person commenced to hold the office or to possess the property if already a director or chief executive officer, otherwise the day the person became one (s 156(7)(a), (b), s 156(8)); counting="at the first meeting of the directors of the company held" after that day for a declaration under (6)(a), the first meeting being day n, the days from day 0 to the date of that meeting, computed from the DATE inputs by DATE_SERIAL; "as soon as is practicable after" that day for a written notice under (6)(b) (no number, so no clock)
- s 156(15): unit=calendar day; day 0=the day the person fails to comply with a provision of section 156; counting=silent (the text puts no day on the offence, and "as soon as is practicable" gives the duties above no day on which a failure is certain, so the failure is an event the trace supplies)
- s 162(2): unit=calendar day; day 0=the day the company makes the restricted transaction; counting=silent (the bar has no time limit; the day of the transaction decides only whether an approval came before it, from the DATE inputs)
- s 162(4)(b): unit=calendar day; day 0=the day the company makes the restricted transaction; counting="within 6 months from the conclusion of that meeting", the meeting being the next following annual general meeting: the last day is that meeting's conclusion plus 6 months (sg-periods P1, P4, the existing function s 162(4)(b)), and n is the days from day 0 to that last day, computed from the two DATE inputs by DATE_SERIAL
- s 162(5): unit=calendar day; day 0=the conclusion of the next following annual general meeting without the prior approval; counting=silent ("jointly and severally liable to indemnify the company against any loss arising therefrom" has no day, so no clock is encoded)
- s 162(6): unit=calendar day; day 0=the day the company makes the restricted transaction; counting=silent (no time limit)
- s 162(7): unit=calendar day; day 0=the day the company makes the dealing contrary to section 162; counting=silent (the text gives no day for the recovery, and only says nothing in the section prevents it)

### The forks

Each is a `-- FORK:` line in the module, above the rule it governs.

- s 156(1): the two routes are alternatives with no clock; the declarant is any `Party`; a chief executive officer who is not a director is an `Officer`.
- s 156(10): the deeming is encoded as a step the secretary owes after the notice.
- s 156(9) and (10): the copy and the minute are owed together (`RAND`).
- s 156(11): the minute has no day, so no breach path.
- s 156(7): a first meeting that passes without a declaration is not a breach by itself; where no meeting has yet been held, there is no clock.
- s 156(15): the offence is a separate DEONTIC whose forbidden act is the failure itself.
- s 162(10): an approval given on the day of the transaction counts, because it is not "after" the transaction.
- s 162(4)(b) with (10): s 162(10) governs every reference to prior approval in the section, (4)(b) included.
  The text reads "a reference to prior approval does not include any approval of the company that is given after the restricted transaction has been made" (src:13563-13566), and (4)(b) speaks of "the prior approval of the company".
  So an approval given at the next following annual general meeting, after the transaction, does not meet the condition, and the six months run unless the approval came before the transaction.
  The other reading lets an approval at or before that meeting count for (4)(b) although it comes after the transaction, so that the condition has something to do; it is in the module's FORK line as the other reading.
  A mutated copy that takes the other reading fails 2 of the traces (the approval-at-the-meeting traces for the repayment rule and for the indemnity), so the tests do pin the choice.
- s 162(2): the making of a transaction on the condition of (4)(b) is not a breach.
- s 162(4)(b): the bearer of the repayment is the relevant director, and a failure is charged to the company as its contravention; the six months run unless the approval of (4)(a) was given before the transaction.
- s 162(5): one rule for one authorising director ("jointly and severally" cannot be said of a single party); the indemnity is owed once the meeting has passed without an approval given before the transaction.
- s 162(6): the offence is a separate DEONTIC gated on the company's contravention.
- s 162(7): "Nothing ... operates to prevent" is a liberty of the company, a MAY with no clock.

### What the text leaves silent

- No day for "as soon as is practicable" in s 156(1), (2), (8) and (9): nothing lapses, so these duties have no breach path of their own, and the module carries no `LEST` on them (the unstable build warns that a `LEST` on a rule with no deadline can never be reached).
- No day for the secretary's minute (s 156(11)), for the indemnity (s 162(5)), for the recovery (s 162(7)) or for the offences (s 156(15), s 162(6)).
- Whether both the fine and the imprisonment may be imposed: both offences say "or", and the BECAUSE texts say "or".
- Whether s 162(10) governs the reference to prior approval in (4)(b) (the fork above).

### Verification

- Both modules check with the unstable build 20261125 (a50cbd0) and with the stable build (cache entry 112): zero errors and zero warnings from the two new files, all 18 `#ASSERT` lines satisfied.
  The unstable build reports 3 `lint/lest-without-deadline` warnings, all in the existing `sgb1-s156-interests.l4`, and none in the new files.
- All 45 traces match their `-- EXPECT` comments on both builds (`expect_check.py`).
  The expected outcomes were written from the text before the module was run; after a change of reading on s 162(4)(b) and (10) the expectations that depend on it were changed with it, each for the reason in its comment.
- Two mutated copies, deleted afterwards, were run as a sensitivity check: taking the other reading of (4)(b) and (10) changes 2 traces, and dropping the s 162(10) test from prior approval changes 3.
- `srcrefs.py check --refs` over the module reports 176 quoted lines, 19 locators and 0 problems.
- None of the 28 names the module defines (constructors, enum types and rule or helper names) occurs in `sgb1-s156-interests.l4`, `sgb2-s162-loans-to-directors.l4`, `sg-core.l4`, `sg-periods.l4` or `sg-groups.l4`.

### READS-DIFFERENTLY-ON-MAIN

None by outcome class: every trace gives the same class on the stable build as on the unstable build.
The layout of a still-open result was not compared.
In the `ROR` rules the unstable build prints a still-open result that lists the other route as well as the open step; the class is `RESIDUAL` either way.

### Differences from the existing DEONTIC

The existing DEONTICs are in `sgb1-s156-interests.l4` (s 156(1), (7), (11), (12)) and `sgb2-s162-loans-to-directors.l4` (s 162(2)).
The module does not call them.

- s 156(1): the existing rule has no gate and one act ("declare ... or send a written notice"), so it applies to every director whatever the interest; the new rule is gated by `s 156(1) the director or chief executive officer must declare ...`, so s 156(3) (a member or creditor of an interested corporation, not material) and s 156(4) (a guarantee or a directorship of a related corporation, by reason only) end the duty (src:12938-12949, src:12969-12981, src:12983-13003).
  The new rule has two acts in `ROR` and the steps that follow each (the company's copy, the secretary's minute), where the existing one stops at the act (src:13092-13102, src:13104-13116, src:13118-13121).
- s 156(1), (7) and (11): the existing rules carry a `LEST BREACH` on a `MUST` with no `WITHIN`.
  The unstable build reports each as a `lint/lest-without-deadline` warning (`sgb1-s156-interests.l4` lines 471, 504 and 518), and the stable build does not.
  The new rules carry none.
- s 156(7): the existing rule is a `MUST ... WITHIN` with the number of days to the first meeting as an input, and a lapse is a breach; there is no written-notice route.
  The new rule takes the dates and the meeting list, finds the first meeting through the existing function, and counts the days itself.
  At a lapse it is not a breach: the written notice of (6)(b) and (8) has no day and is still owed (src:13046-13058, src:13060-13070, src:13074-13090).
  Where no meeting has been held after the date, there is no first meeting, and the new rule has no clock.
- The parties: the existing s 156 rules bind only `Director <name>`, while the text says "every director or chief executive officer" (src:12938-12939); the new rules take any `Party`, so a chief executive officer who is not a director can be the declarant.
- Gates not called: the existing `s 156(9) the persons to whom the company must send a copy of the notice` and `s 156(10)(a) the declaration is deemed to form part of the proceedings ...` are not called.
  The act of s 156(9) is one act whose name covers both sets of recipients, so no choice between them is left to make.
  The s 156(10) steps are owed after any written notice under the new rule, so the deeming needs no separate gate there.
  A rule that needs either distinction would call them.
- s 156(12): not in the new module.
- s 156(15): the existing module has the offence as a Boolean and a penalty only; the new module adds a DEONTIC whose act is the failure (src:13163-13168).
- s 162(2): the existing rule takes "the transaction is within an exception" as one fact.
  The new rule builds it from the facts of (3)(a) or (b) (the expenditure, the home, a second home transaction outstanding), the prior approval of (4)(a) with its day tested against the day of the transaction by s 162(10), and the condition of (4)(b) (src:13463-13502, src:13506-13519, src:13563-13566).
  Read side by side, the two give the same answer where the same facts are passed as one Boolean; this was not run.
- s 162(4)(b), (5), (6), (7): the existing module has Boolean functions only.
  The new module adds the repayment rule with its six-month clock, the indemnity, the offence and the recovery (src:13506-13519, src:13526-13530, src:13534-13537, src:13541-13545).

### What was not encoded, and why

- s 156(12): no day, no step after it, and the existing module has the DEONTIC.
- The second limb of s 156(11): the records of "written resolution duly signed and returned": the section nowhere else speaks of a written resolution, so there is no act to name.
- s 156(14): a saving of other law, no act.
- s 156(5) (a standing declaration): it says when a declaration is treated as sufficient, and the Boolean function already answers it; the new rules take the declaration as given.
- s 162(1), (8), (9): definitions, left to the Boolean encoding.
- s 162(3)(c) and (d), and sections 163A and 163B: taken as one fact, `the transaction is within section 163A or 163B or section 162(3)(c) or (d)`.
- The loss the indemnity covers, and whether the amount was in fact repaid in part: no figures are tested.
