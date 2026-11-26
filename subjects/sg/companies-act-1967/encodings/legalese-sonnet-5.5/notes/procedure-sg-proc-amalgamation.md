## Procedure layer: amalgamation of companies (Companies Act 1967 ss 215A to 215H, with the short form of s 215D)

Module `sg-proc-amalgamation.l4`, tests `sg-proc-amalgamation-tests.l4`, both in this folder.
The module is a regulative layer over the Boolean encoding in `sgd-amalgamation.l4`: it imports it and calls its gate functions, and it restates none of them.
It writes the whole procedure again from the text and does not call the DEONTIC rules that `sgd-amalgamation.l4` already has.
Every DEONTIC has the type `DEONTIC Party `amalgamation chain act``, and the parties are the corpus's own `Party` (`Board of directors`, `Director`, `Member`, `Company`, `Creditor`, `Registrar`, `Court`).

### The seat of each DEONTIC, and its TIMELINE line

Every deadline in this procedure is a backward count from a date the caller supplies (the general meeting, or the date of effect), or has no number in the text.
So day 0 of every trace is the start day of the trace, a DATE input, and each DATE input must agree with the day of the trace on which that event happens.

- `s 215C chain: the duties before the general meeting`
  - Seat: s 215C(2) (src:21175-21185), (3) (src:21190-21199), (4) (src:21201-21217) and (5) (src:21219-21244).
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting="before the general meeting mentioned in subsection (1)(a)" for the board's resolution and the two solvency statements (last day is the day before the meeting) and "not less than 21 days before the general meeting" for the copy to every member, the copy to every secured creditor and the published notice (last day is the meeting day less 21); the director's declaration (s 215C(3)) has no day in the text, so the found period `the period of all convenient speed, as found` sets it.
- `s 215D chain: the duties before the general meeting`
  - Seat: s 215D(3) (src:21326-21334), (5) (src:21340-21344) and (6) (src:21348-21355).
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting="not less than 21 days before the general meeting" for the written notice to every secured creditor (last day is the meeting day less 21) and "before the commencement of the general meeting" for the solvency statement (last day is the meeting day itself); the director's declaration (s 215D(6)) has no day in the text, so the found period `the period of all convenient speed, as found` sets it.
- `s 215F chain: the removal from the register and the certificate of confirmation`, `s 215F chain: the notice of amalgamation` and `s 215E chain: the filing with the Registrar, then the Registrar's notice`
  - Seat: s 215E(1) (src:21365-21368), s 215F(1) (src:21421-21435), (3) (src:21445-21447), (4) (src:21449-21452) and s 215G (src:21458-21460).
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting: the documents "must be filed" with no day and no named bearer, so no clock is encoded for the filing; the Registrar's notice ("upon the receipt", s 215F(1)(a)) and the certificate ("upon the application", s 215F(4)) take the found period of all convenient speed, running from the filing and from the application; the removal ("as soon as practicable after the effective date", s 215F(3)) takes the found period of the standard of time, running from the Registrar's notice; each step is reached by HENCE from the one before it.
- `s 215H chain: the application to the Court, then the order`
  - Seat: s 215H(1) (src:21491-21508) and (2) (src:21510-21511).
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting="at any time before the date on which the amalgamation becomes effective" (last day is the day before the date of effect); the text names no day on which the window opens, so it is open from day 0; the Court's power has no limit of time.
- `s 215 chain: the members' resolution, the filing, the Registrar's steps and the Court's power`
  - Seat: s 215C(1) (src:21161-21171) and s 215D(1) (src:21251-21259), with the steps of the three rules above.
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting=silent for the resolution ("by special resolution at a general meeting", no last day); the steps after it are as above.
- `s 215 chain: the whole amalgamation`
  - Seat: ss 215A to 215H (src:21068-21511).
  - TIMELINE: unit=calendar day; day 0=the start day of the trace; counting=as the rules above state, each deadline measured back from the DATE input of the meeting or of the date of effect.

### The clocks, and the gates that choose between them

The helpers `s 215 chain: the days from the start day to ...` turn each deadline into a number of days from the start day, using `sg-periods` (`period: the latest day for an act a period before`).
The module calls four existing gates: `s 215D(1)` and `s 215D(2)` (the caller passes the answer to `s 215 chain: the whole amalgamation`; JUST TRUE selects the short form, anything else the long form), `s 215E(1)` (whether the documents filed are those the subsection requires), and `s 215H(1) the Court may make an order in relation to the amalgamation proposal` (whether the Court has power to order).
The existing gates `s 215D(1)` and `s 215D(2)` fold in a Boolean that the members "resolved to approve" on the terms.
In this chain the resolution is a step, so the caller reads that Boolean as the terms of the resolution proposed.

### Forks

The `FORK` lines in the module are the register.
In short:
- "not less than 21 days before" (ss 215C(4), (5), 215D(3)) is read with the last day as the meeting day less 21, an act on that day being in time, as the existing functions read it; the clear-days reading, which the corpus records elsewhere (sg-periods P5), would give the day before it;
- before the meeting, an act on the meeting day is not "before the general meeting" (s 215C(2)), but is "before the commencement" (s 215D(5)) because a date cannot say at what hour the meeting began;
- the duties before the meeting (s 215C(2)) are owed from day 0 on the assumption that the proposal goes to the general meeting, so a board that decides against the amalgamation and never calls the meeting is shown in breach on the day before the meeting date the caller supplies (SG-amalgamation-1, independent review: assumed here, not gated);
- the director's declaration (ss 215C(3), 215D(6)) has no number of days in the text, and takes the found period of the section module (sgd-amalgamation.l4:1197-1203, 1333-1339), although s 215C(4)(b) implies the declarations exist 21 days before the meeting;
- "the directors ... must" (ss 215C(5), 215D(3)) is the duty of one named director per rule;
- the approval "by any other person" (s 215C(1)(b)) is not encoded, because the text names no person;
- the short-form resolution leads to the filing as the long-form one does (s 215D(4));
- the choice between the short and long forms is made on the caller's gate answer, and the Boolean that the members "resolved to approve" the terms is the caller's reading of the terms proposed;
- the members' resolution is a power with no limit, and the filing opens only after it;
- the filing is the amalgamating company's duty, and a filing that lacks what s 215E(1) requires leaves the duty to file open (a second filing is assumed to be complete); the filing has no clock and no LEST, because the text names no one who must file;
- the Registrar's removal (s 215F(3)) takes the found period from the Registrar's notice, not from the effective date, because the rule is reached by HENCE from the notice and does not know the effective date;
- the notice with the notice of incorporation (s 215F(1)(b)) has no clock, as the existing rule has none; the (a) form takes the found period;
- the application for the certificate (s 215F(4)) is a power of the amalgamated company with no last day, and the Registrar's duty follows it;
- the Court route is open from day 0 and closes the day before the date of effect; where the Court is not satisfied, or the applicant is not of the three kinds, or the application is late, the Court has no power to order; the Court's own power has no limit, and the Court's four alternatives are one ROR; an order does not stop or change the filing or the Registrar's steps;
- the date of effect is a DATE input (s 215B(2) or the date shown in the notice under s 215G), not computed from the Registrar's step.

### What the text leaves silent

- No number of days for the director's declaration (ss 215C(3), 215D(6)): the found period of all convenient speed sets it, so a missed declaration is a breach by the director once the period runs out; the offences of ss 215C(6) and 215D(7) have no step of their own to attach to.
- No number of days for the filing (s 215E(1)), which is left without a clock; for the Registrar's notice (s 215F(1)(a)), certificate (s 215F(4)) and removal (s 215F(3)), which take the found periods (see below); for the notice of s 215F(1)(b), which is left without a clock; or for the application for the certificate.
- No day on which the window to apply to the Court opens (s 215H(1)), and no limit on the Court's decision.
- What an order under s 215H(1)(a), (b) or (c) does to the filing and the Registrar's steps: none stops or changes them here.

### Differences from the existing DEONTIC

The existing rules are in `sgd-amalgamation.l4` at lines 1139, 1158, 1177, 1197, 1222, 1252, 1281, 1298, 1315, 1333, 1355, 1374 and 1388 (lines 1409, 1431 and 1447 are s 215K, outside this unit), counted on `unstable-20261126-90eed8e`'s tree after the Interpretation Act pass.
They were read once, before the module was written, and not called.

- s 215D(5), the solvency statement (src:21340-21344, "before the commencement of the general meeting"): the existing rule at :1315 is due within the days to the day before the meeting; this module allows the meeting day itself.
  An act on the meeting day, before it starts, is in time here and a breach there.
- s 215C(3) and s 215D(6), the declarations (src:21190-21199, 21348-21355): the existing rules at :1197 and :1333 have `WITHIN` the found period of all convenient speed and a `LEST BREACH`; this module has the same input and the same breach, so the two layers answer alike (since the independent review; before it the layer's declarations had no clock).
- s 215F(1), (3) and (4) (src:21421-21452): the existing rules at :1355, :1374 and :1388 are free-standing duties of the Registrar with a found period and a `LEST BREACH` (the (b) form of s 215F(1) has no LEST, class "other" in `notes/lest-without-deadline.md`), and with no step before them; here the Registrar's notice follows the company's filing (HENCE), the removal and the certificate follow the notice, and the certificate follows an application by the amalgamated company (src:21449-21450, "Upon the application of the amalgamated company"); the found periods run from those earlier steps.
- s 215E(1), the filing (src:21365-21368): no existing DEONTIC; this module adds the company's duty to file, gated on the existing documents function, with no clock (see "Duties left without a clock").
- ss 215C(1)(a), 215D(1) and 215D(4), the members' resolution (src:21161-21165, 21251-21259): no existing DEONTIC; this module adds it, and makes it the trigger of the filing.
- s 215H(1), the application to the Court (src:21491-21508): no existing DEONTIC; this module adds a power with a last day (the day before the date of effect) and the Court's four alternatives.
- The ss 215C(2)(a) to (c), 215C(4), 215C(5)(a) and (b), and 215D(3) rules (src:21175-21185, 21201-21217, 21219-21244, 21326-21334): the same party, the same act, the same last day and the same breach as the existing rules at :1139, :1158, :1177, :1222, :1252, :1281 and :1298.
  The only difference in form is that this module names the board with the core's `Board of directors` where the existing module declared a `s 215C party` of its own.
- Whole chain: the existing rules stand alone, one function each, with no trigger and no gate; this module runs them as one chain from the day the board begins to the end of the Court window, and chooses the form by the gate answer.

### What was not encoded, and why

- s 215A (src:21068-21072) and s 215B (src:21076-21157): a permission and the required contents of a proposal; no step has a time or a party, so the Boolean functions stand.
- s 215C(1)(b) (src:21167-21171): approval "by any other person" where the proposal would require it; the text names no person.
- ss 215C(6) and 215D(7): the offences for a director who contravenes the declaration duty; the duty has no last day, so no step is the contravention.
- s 215E(2) and s 215F(2): the deeming for a new company and the date the notice is expressed to take effect; they limit what a notice says and set no clock.
- s 215G: the effects (src:21458-21487) are consequences that happen on the date, not duties; the date is the DATE input that ends the Court window.
- s 215H(2): the terms or conditions of an order; the text leaves them to the Court.
- ss 215I and 215J, the solvency statements themselves, and s 215K: outside this unit.

### Which binary verified the traces

The unstable builds `unstable-20261125-a50cbd0` (first build checked, 35 traces) and `unstable-20261126-90eed8e` (after the independent review, 42 traces) ran the module and the tests with no error and no warning from these two files, all 6 `#ASSERT` lines satisfied, and all 42 `#TRACE` lines matched their `-- EXPECT` (`expect_check.py` on `unstable-20261126-90eed8e`).
The main build (the stable build 112) ran both files with no error and no warning, all 6 `#ASSERT` lines satisfied, and 36 of the 42 traces matched.
A sensitivity check on a scratch copy before the independent review (21 days changed to 20 and the day before the meeting changed to the meeting day, then deleted) made 8 traces mismatch.

### READS-DIFFERENTLY-ON-MAIN

Six traces read differently on main, all the same way: in each, nobody applies to the Court and the last day for applying passes.
Unstable reads the lapse of the unused power as the end of the matter (FULFILLED); main shows the Court's four alternatives as still open (RESIDUAL).
The six, by test-file line:

- test-file line 190: expected FULFILLED, MAIN prints RESIDUAL: Nobody applies to the Court, and the window closed on day 89, before the last step.
- test-file line 315: expected FULFILLED, MAIN prints RESIDUAL: The amalgamated company is a new company: the Registrar issues the notice with the notice of incorporation (paragraph (b)).
- test-file line 356: expected FULFILLED, MAIN prints RESIDUAL: The short form: the members resolve under section 215D(1) on day 59, and the chain runs as above; the Court is not applied to and the window closes on
- test-file line 368: expected FULFILLED, MAIN prints RESIDUAL: The existing gate of section 215D(2), all six conditions met: the short form applies. Every step in time, the amalgamation then runs to its end.
- test-file line 381: expected FULFILLED, MAIN prints RESIDUAL: The gate of section 215D(2) fails on one condition (the constitution): the long form applies. Every step in time.
- test-file line 460: expected FULFILLED, MAIN prints RESIDUAL: The Registrar issues the notice on day 90, the last day of the found 30 days after the filing on day 60; the removal follows on day 120 and the certif

The list is at the end of `sg-proc-amalgamation-tests.l4`.

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST or branch, and here.
This unit has one, which was FULFILLED already: the power to apply to the Court under s 215H(1) lapses on the day of effect, with nothing owed (src:21491-21508).
No trace moved from BREACH to FULFILLED after the independent review.
The BREACHes that stay are duties laid on a named party: the board's resolution and statements, the director's declarations, the sending and publication, the notices, and the Registrar's notice, removal and certificate.

### Do-once duties and the found period

Decided by Claude on 2026-11-27 (assumed, not ruled), to align the layer with the section modules (`notes/lest-without-deadline.md`): a duty to do a thing once with no number of days in the text takes a rule-level input of days, and a late act is a BREACH by the bearer.

| duty | class | input | twin in the section module |
| ---- | ----- | ----- | ---- |
| s 215C(3): a director who votes in favour must sign the declaration | no time stated, Interpretation Act 1965 s 52 | `the period of all convenient speed, as found` | `sgd-amalgamation.l4:1197-1203` |
| s 215D(6): the same, for the short form | s 52 | the same | `sgd-amalgamation.l4:1333-1339` |
| s 215F(1)(a): the Registrar must "upon the receipt" issue the notice | s 52 | the same | `sgd-amalgamation.l4:1355-1366` |
| s 215F(3): the Registrar must "as soon as practicable after the effective date" remove the companies | the section's own standard | `the period the standard of time allows, as found` | `sgd-amalgamation.l4:1374-1380` |
| s 215F(4): the Registrar must "upon the application" issue the certificate | s 52 | `the period of all convenient speed, as found` | `sgd-amalgamation.l4:1388-1394` |

The inputs are passed down the chain as plain arguments; the tests pass 30 and 30.

### Duties left without a clock

- s 215E(1), the filing: the text says "must be filed" and names no one who must file, so a `LEST BREACH BY` the amalgamating company would put a breach on a party the text does not name (this unit's own fork says the company is only the party the module chose); decided, assumed, not ruled, and the section module has no rule for it either.
- s 215F(1)(b), the notice with the notice of incorporation: the existing rule carries no LEST and is class "other" in `notes/lest-without-deadline.md` (`sgd-amalgamation.l4:1356-1360`), so this layer does the same.
- The Court's steps under s 215H(1) and the application for the certificate (a power): no time in the text, and a power or a Court's discretion is not a do-once duty of a named party.
