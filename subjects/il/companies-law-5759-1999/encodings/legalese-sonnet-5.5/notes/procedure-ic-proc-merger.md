## Procedure layer: the merger (sections 316 to 323)

This layer adds eight DEONTIC functions over the Boolean encoding in `ic4-part8-merger.l4`, in `ic-proc-merger.l4`, tested in `ic-proc-merger-tests.l4` (43 traces).
It adds no definition to an existing module, and calls the existing gates instead of restating them: `סעיף 316` (both boards approved), `סעיף 320(א)` (the general meeting's approval is needed), `סעיף 319` (the court may order a delay), `סעיף 321(א)` and `סעיף 321(ב)` (who may apply, when the court may declare the approval), `סעיף 323` (the thirty and fifty days) and `סעיף 322 - אסור לבצע את המיזוג` (the bar while a prevention or delay stands).
The existing functions that answer a duty's status (`סעיף 317(א)`, `317(ב)`, `318`, `322` with `מצב קיום חובה`) return a status value and not a Boolean, so they are not gates and are not called.

### Where each DEONTIC sits, and whose seat it is

All eight sit in `ic-proc-merger.l4`, under the heading for the section they carry.
None is wired into `ic4-seat.l4`, because that would edit an existing module.
Every DEONTIC is one merging company's run: the text speaks of "a merging company" ("חברה מתמזגת"), so a merger of two companies runs each once.
The chained steps are separate DEONTICs only where the text starts a new clock from a new event.

- `סעיפים 316 עד 318(א) - הצעת המיזוג, המצאתה לרשם ושליחתה לנושים המובטחים`: the boards bear the duty to draw up and sign the proposal (no clock); the company holds the power to convene the general meeting (no clock) and bears two three-day duties, delivery to the registrar and sending to the secured creditors.
- `סעיף 317(ב) - הודעה לרשם על החלטת האסיפה הכללית`: the general meeting holds the power to decide (no clock); the company bears the three-day duty to tell the registrar. It arises only where section 320(א) requires the meeting's approval.
- `סעיפים 317(ב) ו־318(ב) - הודעה לנושים הלא מובטחים והודעה לרשם על מתן ההודעות`: two duties of the company, neither with a clock.
- `סעיף 317(ב) - המצאת עותק מהחלטת בית המשפט לרשם`: the company bears the three-day duty. It is the step the two court DEONTICs chain into; it is not run alone.
- `סעיף 319 - התנגדות הנושה והחלטת בית המשפט`: a creditor holds the power to apply (no clock); the court holds the power to order a delay or prevention, or to refuse (no clock); then the chained copy duty.
- `סעיף 321 - בקשת בעלי המניות והחלטת בית המשפט`: the shareholders holding at least a quarter of the voting rights hold the power to apply (no clock); the court holds the power to declare the approval, or to refuse (no clock); then the chained copy duty.
- `סעיף 322 - הודעה לרשם על הודעת הממונה על התחרות`: the Commissioner's notice is the event; the company bears the three-day duty to tell the registrar.
- `סעיפים 322 ו־323 - ביצוע המיזוג בידי הרשם`: the registrar bears three duties (steps (3), (4) and (5) of section 323), none with a clock, which arise only when section 323's conditions hold and section 322's bar does not.

### The DEONTICs and their timelines

1. `סעיפים 316 עד 318(א) - הצעת המיזוג, המצאתה לרשם ושליחתה לנושים המובטחים`:
   `-- TIMELINE: unit=calendar day; day 0=the day the general meeting is convened (first clock, section 317(א)) and the day the merger proposal is delivered to the registrar (second clock, section 318(א)); counting="בתוך שלושה ימים ממועד זימון האסיפה הכללית" and "לא יאוחר משלושה ימים ממועד ההמצאה של הצעת המיזוג לרשם החברות"`
2. `סעיף 317(ב) - הודעה לרשם על החלטת האסיפה הכללית`:
   `-- TIMELINE: unit=calendar day; day 0=the day the general meeting decides on the merger; counting="בתוך שלושה ימים ממועד קבלת ההחלטה"`
3. `סעיפים 317(ב) ו־318(ב) - הודעה לנושים הלא מובטחים והודעה לרשם על מתן ההודעות`:
   `-- TIMELINE: unit=none stated; day 0=none; counting="silent"`
4. `סעיף 317(ב) - המצאת עותק מהחלטת בית המשפט לרשם`:
   `-- TIMELINE: unit=calendar day; day 0=the day the court gives its decision under section 319 or 321; counting="בתוך שלושה ימים ממועד מתן החלטה כאמור"`
5. `סעיף 319 - התנגדות הנושה והחלטת בית המשפט`:
   `-- TIMELINE: unit=calendar day (for the copy to the registrar, the application and the court's decision state none); day 0=the day the court gives its decision under section 319; counting="silent" for the application and the decision, then "בתוך שלושה ימים ממועד מתן החלטה כאמור" for the copy`
6. `סעיף 321 - בקשת בעלי המניות והחלטת בית המשפט`:
   `-- TIMELINE: unit=calendar day (for the copy to the registrar, the application and the court's decision state none); day 0=the day the court gives its decision under section 321; counting="silent" for the application and the decision, then "בתוך שלושה ימים ממועד מתן החלטה כאמור" for the copy`
7. `סעיף 322 - הודעה לרשם על הודעת הממונה על התחרות`:
   `-- TIMELINE: unit=calendar day; day 0=the day the company receives the Commissioner's notice; counting="בתוך שלושה ימים ממועד קבלת ההודעה"`
8. `סעיפים 322 ו־323 - ביצוע המיזוג בידי הרשם`:
   `-- TIMELINE: unit=calendar day (for the gate's inputs only); day 0=the day the general meeting decided, in each merging company, and the day the proposals were delivered to the registrar; counting="וחלפו שלושים ימים ממועד קבלת החלטת האסיפה הכללית בכל אחת מן החברות המתמזגות וחמישים ימים מהמועד שבו הומצאו הצעות המיזוג לרשם החברות" (the registrar's steps carry no clock: silent)`

Every period in sections 316 to 323 is a number of days ("שלושה ימים", "שלושים ימים", "חמישים ימים"), so no DATE input is needed and no length is computed.
The text does not say whether "days" are calendar days or working days; the clocks count calendar days and no working-day calendar is used.

### Forks

Each is also a `-- FORK:` line above its DEONTIC.

- `סעיף 316`: the boards' duty to draw up and sign is a MUST with no clock; the other reading is that the sentence states no duty.
- `סעיף 317(א)`: the day of convening is day 0 and the third day is in time (fork F1 of `NOTES-ic4.md`); the other reading makes the day of convening day 1.
- `סעיף 318(א)`: the day of delivery to the registrar is day 0 and "לא יאוחר משלושה ימים" includes the third day; the other reading makes the third day late.
- `סעיפים 317(א), 318(א)`: the convening is a MAY with no clock, present only to stamp the day the count starts; the other reading is a duty to convene, which these sections do not state.
- `סעיף 318(א)`: a missed three-day duty is a terminal BREACH, and the sending to the secured creditors follows only a timely delivery to the registrar; the other reading chains the duty to send after a late delivery as well, so that it survives the breach.
- `סעיף 317(ב)` (decision): "החלטת האסיפה הכללית" is any decision of the general meeting on the merger; the other reading is an approving decision only.
- `סעיפים 320(א), 317(ב)`: a company that needs no general meeting's approval (section 320(א1)) has no decision, so no notice is owed; the other reading owes the notice whenever a meeting is held.
- `סעיף 317(ב)` (creditor notices): the notice to the registrar that the creditors were told has no clock of its own; the other reading extends the first three days to it.
- `סעיפים 317(ב), 318`: that notice is owed once the unsecured creditors were told; the other reading waits for both the secured and the unsecured.
- `סעיף 317(ב)` (court copy): "החלטת בית המשפט לפי סעיפים 319 או 321" is any decision the court gives, a refusal as much as an order; the other reading is an order or determination in the applicant's favour only.
- `סעיף 319`: the creditor's application and the court's order or refusal are MAYs with no deadline, and the court's finding of a reasonable fear is a BOOLEAN input; the other reading binds the court to order once the fear is found.
- `סעיף 319`: where the fear was not found, the only act left to the court is the refusal, and an order is not a permitted act; the other reading lets the order stand.
- `סעיף 321(א)`: "לפחות עשרים וחמישה אחוזים" includes exactly a quarter; the other reading needs more than a quarter.
- `סעיף 321(ב)`: "לא יאשר ... אלא אם כן שוכנע" is a bar, and the court MAY (not MUST) declare the approval once convinced; the other reading is a MUST.
- `סעיף 322`: the Commissioner's notice, an event under another Act, is put in the trace as the Commissioner's MAY act stamped on the day the company receives it; the other reading takes the day as an input.
- `סעיף 322`: the duty arises on any notice from the Commissioner; the other reading limits it to a notice that bears on the merger.
- `סעיף 323`: the thirty and fifty days are a gate on the registrar's duties and the elapsed days are inputs, one per company, with an exact thirty and an exact fifty enough (fork F6 of `NOTES-ic4.md`); the other reading is a prohibition that lasts until a computed day.
- `סעיפים 322, 323`: while notice of a prevention or delay stands at the registrar, the registrar's duties under 323 do not arise; the other reading lets the bar forbid only the companies and leaves the registrar's steps due.
- `סעיף 323(3)-(5)`: the registrar's three steps are three MUSTs due together in any order (a RAND); the other reading chains one after another.

### What the text leaves silent

No clock is encoded where the text sets none, and each such step stays open however long it waits (most of the tests wait 400 days to show it):
the boards' drawing up and signing (316); the convening of the general meeting; the general meeting's decision (320); the notice to the unsecured creditors and the notice to the registrar that creditors were told (317(ב), 318(ב)); a creditor's application and the court's decision under 319; the shareholders' application and the court's decision under 321; the Commissioner's notice reaching the company; the registrar's three steps under 323.
Section 317(ב) and 322 each give a three-day clock for the company; section 323 gives thirty and fifty days, but as a bar on carrying out the merger and not as a time within which anyone must act.
Sections 324 to 327 state no clock.

### Differences from the existing DEONTIC

None: the encoding had no DEONTIC for these sections, so there is nothing to compare.
Two readings differ from the Boolean encoding's own comments and are worth the next reader's eye: the Boolean encoding gives the court's directions securing creditors' rights its own function (fork F3 there), where here the court's decision, whether an order, a direction or a refusal, is one act that starts the registrar's three days; and its 321 gate is split here into the application (321(א)) and the court's reply (321(ב)), each tested alone.

### Which binary verified the traces

Both. With the unstable build `l4-unstable-20261125-a50cbd0` and with the stable build 112, run from this folder with `JL4_LIBRARY_PATH` unset: `ic-proc-merger.l4` and `ic-proc-merger-tests.l4` print no error and no warning of their own, and `expect_check.py` matches 43 of 43 traces on each.
(The one message the binaries print, about two copies of `prelude` in the embedded library and the XDG data directory, comes from the machine and is the same for every module in the folder.)
There is no new Boolean helper, so the tests carry no `#ASSERT`.
Two mutated copies, since deleted, were run as a sensitivity check: widening the delivery clock of 317(א) from three days to four failed two traces, and dropping the section 322 bar from the registrar's gate failed one.

### Reads differently on main

No trace reads differently.
The module has no MAY with a LEST, no RAND of two breaches and no act after a wait device, which are the places the two binaries are known to part; its RANDs join three MUSTs that have no clock.

### What was not encoded, and why

- Paragraphs (1) and (2) of section 323 (the assets and liabilities pass; the absorbing company stands in the target's place in proceedings) and the second half of paragraph (4) (the target "תחוסל": is wound up) take effect by operation of law, and nobody acts.
- The court's second power under 319, to give directions securing creditors' rights, is not a separate act (see the fork above); the Boolean function for it is not called.
- Whether the merger has secured creditors at all: the sending to the secured creditors (318(א)) is owed whenever the proposal was delivered, as the text states it, and the case of no secured creditors is not a separate branch.
- Section 320(ג) to (ו) (the special vote where shares are held by the other merging company or a holder of a quarter of its control) and the class meetings of 320(ב): these set the majority needed, not a step or a clock; they are inputs to the general meeting's decision and stay in the Boolean encoding.
- Sections 324 (freedom to contract), 325 and 327(ב) (floating charges), 326 (regulations) and 327(א) (a transitional majority): no step with a clock; sections 324 to 327 state none.
- Section 315 (the board's duty to weigh the absorbing company's ability to pay creditors) lies before section 316 and outside the units here.

### Closed routes (not breaches)

The convention for the whole procedure layer is assumed, not ruled: BREACH is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and listed below.
A step the Court is bound by may keep a BREACH BY the court; this unit has none.

No power in this unit ends in a breach: the creditor's application (319), the shareholders' application (321(ב)) and the court's own steps are MAYs with no clock.
The three-day duties of 317(א), 318(א), 317(ב) (both the general meeting's decision and the court's) and 322 are laid on the merging company by name, so a lapse stays a BREACH BY the company.
No step has a BREACH BY the court.

### Changes after the independent review

- The forks F1 and F6 are cited as forks of `NOTES-ic4.md`, where they are, and no longer as forks of `NOTES.md`, which has neither.
- Not encoded: a step whose clock the text does not state. The delivery duty of 317(א) opens only after the MAY of convening a general meeting, so a merging company whose merger needs no approval of its general meeting (src:2109, the target company wholly owned and controlled by the absorbing company) has no route to deliver its proposal in this layer, although src:2128 counts the fifty days "מהמועד שבו הומצאו הצעות המיזוג לרשם" for every merging company; the text names no starting event for that delivery, so none is encoded.
- The verification line says "no warning of their own" where it said "zero warnings".
