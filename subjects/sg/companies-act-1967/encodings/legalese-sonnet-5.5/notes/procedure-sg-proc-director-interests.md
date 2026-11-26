## Procedure layer: a director's declaration of interest (Companies Act 1967 s 156) and loans and other restricted transactions in favour of a director (s 162)

Module `sg-proc-director-interests.l4`, tests `sg-proc-director-interests-tests.l4`.
It adds a regulative layer over the Boolean encodings in `sgb1-s156-interests.l4` and `sgb2-s162-loans-to-directors.l4`, and edits neither.
The parties are the corpus's own `Party` (`sg-core.l4`): a declarant, the company, the secretary and a director are each any `Party` the caller passes.
There is no constructor for a chief executive officer in `sg-core.l4`, so a chief executive officer who is not a director is passed as an `Officer` (fork on s 156(1)).
The acts are two new enums, `s 156 declaration act` and `s 162 loan act`.
Every rule is gated by the existing section function: where the gate does not answer `JUST TRUE` (or, for s 162(7), `JUST FALSE`), nothing is owed and the rule is `FULFILLED` at once.
Five new Boolean or numeric helpers sit in the module and are asserted in the tests (18 `#ASSERT` lines).

### The seat of each DEONTIC

- `s 156(1) the director or chief executive officer must declare the interest or send a written notice, and the company and the secretary follow`: the declarant MUST declare the interest at a meeting of the directors WITHIN `the period the standard of time allows, as found`, LEST BREACH BY the declarant, HENCE the secretary MUST minute it (s 156(11), no clock); or (`ROR`) the declarant MUST send a written notice WITHIN the same period, LEST BREACH BY the declarant, HENCE the company MUST send a copy to the directors (s 156(9)) WITHIN the same period from the receipt, LEST BREACH BY the company, and (`RAND`) the secretary MUST minute it in the next meeting after the notice (no clock), because s 156(10) deems the notice part of that meeting and s 156(10)(b) applies the minutes provision as if the declaration had been made there.
  Gate: `s 156(1) the director or chief executive officer must declare the nature of the interest or send a written notice`, which already takes in s 156(3) and (4).
- `s 156(6) the director or chief executive officer must declare the conflict, at the first meeting if by declaration`: the declarant MUST declare the conflict at a meeting, WITHIN the days from the day the person commenced to hold the office or property (or became a director) to the first meeting of the directors after it; or (`ROR`) MUST send a written notice (s 156(6)(b), (8)), which has no clock (see "Duties left without a clock").
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

- s 156(1), (9), (10), (11): unit=calendar day; day 0=the day the relevant facts come to the director's or chief executive officer's knowledge; counting="as soon as is practicable after the relevant facts have come to his or her knowledge", which is not a number of days, so the period is the input `the period the standard of time allows, as found` (the section's own standard of time, so Interpretation Act 1965 s 52 does not supply it); the copy of s 156(9) runs the same period from the day the company receives the notice, which is the day the notice is sent; for the minutes the text sets no day at all
- s 156(6) to (8): unit=calendar day; day 0=the day the person commenced to hold the office or to possess the property if already a director or chief executive officer, otherwise the day the person became one (s 156(7)(a), (b), s 156(8)); counting="at the first meeting of the directors of the company held" after that day for a declaration under (6)(a), the first meeting being day n, the days from day 0 to the date of that meeting, computed from the DATE inputs by DATE_SERIAL; "as soon as is practicable after" that day for a written notice under (6)(b) (no number, so no clock)
- s 156(15): unit=calendar day; day 0=the day the person fails to comply with a provision of section 156; counting=silent (the text puts no day on the offence, and the duties above that have no clock give no day on which a failure is certain, so the failure is an event the trace supplies)
- s 162(2): unit=calendar day; day 0=the day the company makes the restricted transaction; counting=silent (the bar has no time limit; the day of the transaction decides only whether an approval came before it, from the DATE inputs)
- s 162(4)(b): unit=calendar day; day 0=the day the company makes the restricted transaction; counting="within 6 months from the conclusion of that meeting", the meeting being the next following annual general meeting: the last day is that meeting's conclusion plus 6 months (sg-periods P1, P4, the existing function s 162(4)(b)), and n is the days from day 0 to that last day, computed from the two DATE inputs by DATE_SERIAL
- s 162(5): unit=calendar day; day 0=the conclusion of the next following annual general meeting without the prior approval; counting=silent ("jointly and severally liable to indemnify the company against any loss arising therefrom" has no day, so no clock is encoded)
- s 162(6): unit=calendar day; day 0=the day the company makes the restricted transaction; counting=silent (no time limit)
- s 162(7): unit=calendar day; day 0=the day the company makes the dealing contrary to section 162; counting=silent (the text gives no day for the recovery, and only says nothing in the section prevents it)

### The forks

Each is a `-- FORK:` line in the module, above the rule it governs.

- s 156(1): the two routes are alternatives (`ROR`), each open from day 0 and each WITHIN the found period, so a director who does neither within it is in BREACH (the other reading: each route open with no clock, which was this module's first reading); the declarant is any `Party`; a chief executive officer who is not a director is an `Officer`.
- s 156(9): the company's copy runs the same found period from the receipt of the notice, and a copy after it is a BREACH of the company; the section module has no rule for this duty, so the class is chosen by the same test (the text's own standard, "as soon as practicable"), decided by Claude on 2026-11-27, assumed, not ruled (the other reading: the copy with no clock).
- s 156(8): the written notice of (6)(b) has no found period of its own, because it is the alternative to a declaration at the first meeting and a period counted from day 0 would put the director in BREACH on a day when the declaration at the first meeting is still open (the other reading: the notice WITHIN the found period, as the s 156(1) rule takes for its two routes).
- s 156(10): the deeming is encoded as a step the secretary owes after the notice.
- s 156(9) and (10): the copy and the minute are owed together (`RAND`).
- s 156(11): the minute has no day, so no breach path; its time is the minutes' own time under s 188(1)(a), which this layer does not encode, and the section module leaves it without a clock too.
- s 156(7): a first meeting that passes without a declaration is not a breach by itself; where no meeting has yet been held, there is no clock.
- s 156(15): the offence is a separate DEONTIC whose forbidden act is the failure itself, because it covers every provision of section 156 and several of the duties above (s 156(6)(b), (10), (11)) carry no clock to lapse on.
- s 162(10): an approval given on the day of the transaction counts, because it is not "after" the transaction.
- s 162(4)(b) with (10): s 162(10) governs every reference to prior approval in the section, (4)(b) included.
  The text reads "a reference to prior approval does not include any approval of the company that is given after the restricted transaction has been made" (src:13563-13566), and (4)(b) speaks of "the prior approval of the company".
  So an approval given at the next following annual general meeting, after the transaction, does not meet the condition, and the six months run unless the approval came before the transaction.
  The other reading lets an approval at or before that meeting count for (4)(b) although it comes after the transaction, so that the condition has something to do; it is in the module's FORK line as the other reading.
  A mutated copy that takes the other reading fails 2 of the traces (the approval-at-the-meeting traces for the repayment rule and for the indemnity), so the tests do pin the choice.
- s 162(2): the making of a transaction on the condition of (4)(b) is not a breach.
- s 162(2): the one `Party` the bar binds is the company named; the exception and the exemption are facts the caller supplies (the other reading: none; SG-director-interests-2 found this fork in the module and not in these notes).
- s 162(4)(b): the bearer of the repayment is the relevant director, and a failure is charged to the company as its contravention; the six months run unless the approval of (4)(a) was given before the transaction.
- s 162(5): one rule for one authorising director ("jointly and severally" cannot be said of a single party); the indemnity is owed once the meeting has passed without an approval given before the transaction.
- s 162(5): the indemnity is a liability that arises with the transaction, not an act that falls due, so it takes no found period (class OTHER in `notes/lest-without-deadline.md`, as the liabilities of s 25C(4)(a) and (b) are); the section module has no rule for it (the other reading: the indemnity WITHIN the period of all convenient speed, as found, with a LEST BREACH).
- s 162(6): the offence is a separate DEONTIC gated on the company's contravention.
- s 162(7): "Nothing ... operates to prevent" is a liberty of the company, a MAY with no clock.

### What the text leaves silent

- No number of days for "as soon as is practicable" in s 156(1), (2), (8) and (9): for s 156(1) and (9) the layer takes the found period of the section's own standard as an input; for (6)(b) and (8) it takes none (see "Duties left without a clock").
- No day for the secretary's minute (s 156(10)(b), (11)), for the indemnity (s 162(5)), for the recovery (s 162(7)) or for the offences (s 156(15), s 162(6)); the module carries no `LEST` on a `MUST` with no `WITHIN`, because the unstable build warns that such a `LEST` can never be reached.
- Whether both the fine and the imprisonment may be imposed: both offences say "or", and the BECAUSE texts say "or".
- Whether s 162(10) governs the reference to prior approval in (4)(b) (the fork above).

### Verification

- Both modules check with the unstable builds `unstable-20261125-a50cbd0` (first run) and `unstable-20261126-90eed8e` (after the independent review) and with the stable build (cache entry 112): zero errors and zero warnings of their own from the two new files, all 18 `#ASSERT` lines satisfied.
  The only warnings printed are the import-resolution warnings about two differing copies of `prelude` and `daydate` (the embedded library and the XDG data directory); the `lint/lest-without-deadline` warnings that `sgb1-s156-interests.l4` gave at the first run are gone from the section modules since the s 52 pass.
- All 51 traces match their `-- EXPECT` comments on `unstable-20261126-90eed8e` and on the stable build 112 (`expect_check.py`); the first run's 45 matched on `unstable-20261125-a50cbd0`.
  The expected outcomes were written from the text before the module was run; after a change of reading on s 162(4)(b) and (10) the expectations that depend on it were changed with it, each for the reason in its comment; one EXPECT changed after the independent review (below), and six traces were added, decided from the text first.
- Two mutated copies were run as a sensitivity check at the first run, and not re-run in the fix pass: taking the other reading of (4)(b) and (10) changes 2 traces, and dropping the s 162(10) test from prior approval changes 3.
  The two traces that flip under the other reading of (4)(b) and (10), the repayment owed after an approval at the meeting itself and the indemnity owed after the same approval, carry a comment line in the tests naming the reading (SG-director-interests-1).
- `srcrefs.py check --refs` and `check --strict` over the module report 176 quoted lines, 19 locators and 0 problems each.
- None of the 28 names the module defines (constructors, enum types and rule or helper names) occurs in `sgb1-s156-interests.l4`, `sgb2-s162-loans-to-directors.l4`, `sg-core.l4`, `sg-periods.l4` or `sg-groups.l4` (checked at the first run, not re-run).

### The s 162(4)(b) and (10) reading, flagged for a ruling

The module reads s 162(10) into s 162(4)(b), so an approval given at the next following annual general meeting never meets the condition, and the six months run unless the approval came before the transaction.
That leaves the words "if the prior approval of the company is not given as aforesaid at or before the next following annual general meeting" (src:13514-13516) with no case of their own, since an approval before the transaction is already the case of (4)(a).
The text of s 162(10) (src:13563-13566) supports the literal reading, and the other reading is in the module's fork, so the encoding is not wrong; but the two subsections may be a drafting defect that needs a ruling.
The traces that flip under the other reading are the approval at the meeting itself for the repayment rule (`-- EXPECT BREACH`, tests line 257) and the indemnity owed after the same approval (tests line 291), which tell a director to repay, and the company that it contravened, on a contested reading; an approval after the meeting is a BREACH on both readings.

### READS-DIFFERENTLY-ON-MAIN

None by outcome class: every one of the 51 traces gives the same class on the stable build 112 as on the unstable build `unstable-20261126-90eed8e`.
The layout of a still-open result was not compared.
In the `ROR` rules the unstable build prints a still-open result that lists the other route as well as the open step; the class is `RESIDUAL` either way.

### Differences from the existing DEONTIC

The existing DEONTICs are in `sgb1-s156-interests.l4` (s 156(1), (7), (11), (12)) and `sgb2-s162-loans-to-directors.l4` (s 162(2)).
The module does not call them.

- s 156(1): the existing rule has no gate and one act ("declare ... or send a written notice"), so it applies to every director whatever the interest; the new rule is gated by `s 156(1) the director or chief executive officer must declare ...`, so s 156(3) (a member or creditor of an interested corporation, not material) and s 156(4) (a guarantee or a directorship of a related corporation, by reason only) end the duty (src:12938-12949, src:12969-12981, src:12983-13003).
  The new rule has two acts in `ROR` and the steps that follow each (the company's copy, the secretary's minute), where the existing one stops at the act (src:13092-13102, src:13104-13116, src:13118-13121).
- s 156(1), (7) and (11): the existing s 156(1) rule takes the found period of the section's own standard (`WITHIN` at `sgb1-s156-interests.l4:471`, `LEST BREACH` at `:473`) and the new rule takes the same input, with the same `WITHIN` and a `LEST BREACH` on each of its two routes, so the two layers answer alike once the gate holds.
  The existing s 156(11) rule has no clock (a `-- no LEST:` comment at `sgb1-s156-interests.l4:506`, class OTHER), and the new rules leave the minutes without one too.
  The existing module has no rule for s 156(8), (9) or (10)(b) as duties; the new rules take (9) by the same test (own standard) and leave (8) and (10)(b) without a clock.
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

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST or branch.
This unit has no route to change: its BREACHes are the declarant's duty to declare or send a notice (s 156(1), "must", src:12941), the company's duty to send the copy (s 156(9), src:13092), the director's duty to repay (s 162(4)(b), whose breach is charged to the company as a contravention), the prohibitions of s 156(15), s 162(2) and s 162(6) ("must not", "shall be guilty"), each laid on a named party.
The lapse of the declaration route at the first meeting (s 156(7)) is not a breach, and was already a closed route that leaves the written notice owed.

### Do-once duties and the found period

Decided by Claude on 2026-11-27 after the independent review (SG-ALL-1), assumed, not ruled: the layer is aligned with the section modules of the same folder, which carry a found period for a duty to do a thing once (`notes/lest-without-deadline.md`).

| duty | class | input | section module's twin |
| ---- | ----- | ----- | --------------------- |
| s 156(1)(a) declare at a meeting "as soon as is practicable" | ACHIEVEMENT, text's own standard | `the period the standard of time allows, as found` (10 days in the traces) | `sgb1-s156-interests.l4:470-473` |
| s 156(1)(b) send a written notice "as soon as is practicable" | ACHIEVEMENT, text's own standard | the same input | `sgb1-s156-interests.l4:470-473` (one rule for "declare ... or send") |
| s 156(9) the company's copy "as soon as practicable after the receipt of the written notice" | ACHIEVEMENT, text's own standard (no twin; chosen by the same test, decided by Claude on 2026-11-27, assumed, not ruled) | the same input, counted from the receipt | none |

The one input is passed down the chain as a plain argument to the s 156(9) step, which sits inside the s 156(1)(b) route.
Traces: a declaration on day 10 FULFILLED, day 11 BREACH; a written notice on day 11 BREACH; the copy on day 15 (the 10th day after the notice on day 5) FULFILLED, day 16 BREACH; the notice and no copy by day 30 BREACH; nothing by day 400 BREACH (it read RESIDUAL before, `-- EXPECT changed after independent review`).

### Duties left without a clock

- s 156(6)(b) and (8), the written notice of a conflict "as soon as is practicable": left without a clock, because it is the alternative to a declaration at the first meeting (s 156(6)(a), (7)); a period counted from day 0 would put the director in BREACH on a day when the declaration at the first meeting is still open, and the layer has no combined clock for the two routes (the later of the first meeting and the period).
  The section module has no DEONTIC for (6)(b), so the two layers do not give different answers.
  The other reading is in the module's fork on s 156(8).
- s 156(10)(b) and (11), the secretary's minutes: the time is that of the minutes, s 188(1)(a) ("within one month"), which this layer does not encode; class OTHER in `notes/lest-without-deadline.md` (row `sgb1-s156-interests.l4:506`), and the section module has no clock for (11) either.
- s 156(12): not in this module (the section module has it, class OTHER).
- s 162(5), the indemnity: a liability that arises with the transaction, not an act that falls due; class OTHER (the liabilities of s 25C(4)(a) and (b) are the same class in the notes); the section module has no rule for it.
- s 162(4)(b): already has its clock, the six months from the conclusion of the meeting.
- s 156(15), s 162(2) and (6): prohibitions ("must not", "shall be guilty"), no act to do.
- s 162(7): a liberty of the company.
