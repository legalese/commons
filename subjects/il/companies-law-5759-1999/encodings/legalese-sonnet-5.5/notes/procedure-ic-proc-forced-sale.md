## Procedure layer: the forced sale of shares (sections 336 to 341)

This layer adds seven DEONTICs over the Boolean encoding in `ic4-part8-forced-sale.l4`, in `ic-proc-forced-sale.l4`, tested in `ic-proc-forced-sale-tests.l4`.
It adds no definition to an existing module, and calls the existing gates instead of restating them: `סעיף 336(א)`, `סעיף 337` (the acceptance by five percent, two percent and the disinterested offerees), `סעיף 337(ב)`, `סעיף 338`, `סעיף 341(א)`, `סעיף 341(ב)` (twice) and `סעיפים 341(ד) ו־342` (the rate in force).
The one new definition besides the DEONTICs and their party and act enums is a counting rule, `מספר הימים בתקופה שהחוק קובע בחודשים`, which turns a period in calendar months into a number of days from a DATE.

### Where each DEONTIC sits, and whose seat it is

All seven sit in `ic-proc-forced-sale.l4`, under the heading for the section they carry.
None is wired into `ic4-seat.l4`, because that would edit an existing module.
They are run each on its own, not chained to one another, because a month is not a fixed number of days: each month clock takes the date it starts from as an input, and its trace starts AT 0 on that day.
The one chain across DEONTICs is 341(ב) into 341(ג): the month of 341(ב) is also the day the offeror's duty of 341(ג) falls due, so the 341(ב) DEONTIC opens the 341(ג) one when its month lapses or after the court's ruling.
Inside each DEONTIC the next step the text names is chained: the court's step after an application, the sale and purchase after a notice, the company's registration after the offeror's copy.
Section 338א (the same sections apply to each class of security the offer covers) is met by running the DEONTICs once for each class.

1. `סעיף 336(א) - הליך: אסור לרכוש מעל תשעים אחוזים אלא בהצעת רכש מלאה שהתקבלה`: the offeror bears a prohibition (a SHANT) on buying past ninety percent otherwise than by an accepted full offer; a purchase is a BREACH BY the offeror, which is also the breach of statutory duty of section 340(ב).
2. `סעיף 337(ב) - הליך: אסור לרכוש מניצעים שנענו מעל תשעים אחוזים כשההצעה לא התקבלה`: the offeror bears the prohibition (a SHANT) on buying from responding offerees past ninety percent after the offer was not accepted; a purchase is a BREACH BY the offeror.
3. `סעיף 337(א) - הליך: רישום העברת המניות לאחר שהצעת הרכש המלאה התקבלה`: the company that keeps the records bears the duty (a MUST, no clock) to change the ownership records once the offer is accepted.
4. `סעיף 338 - הליך: בקשת הניצע לסעד הערכה בתוך שישה חודשים`: the offeree holds the power (a MAY, six months) to ask the court; the court holds the power (a MAY, no clock) to fix the fair value once it finds the consideration was below it.
5. `סעיף 341(א) - הליך: הודעת המציע לבעל מניה מתנגד`: the offeror holds the power (a MAY, the two months and the month after them) to notify; after the notice the dissenting shareholder bears the duty to sell and the offeror the duty to buy (a RAND of two MUSTs, no clock).
6. `סעיף 341(ב) - הליך: בקשת בעל מניה מתנגד לבית המשפט בתוך חודש ימים`: the dissenting shareholder holds the power (a MAY, one month) to ask the court to decide otherwise; the court holds the power (a MAY, no clock) to decide otherwise or to rule without deciding otherwise; when the month lapses unused, or after the court's ruling, this DEONTIC opens the offeror's duty of 341(ג).
7. `סעיף 341(ג) - הליך: העתק ההודעה והתמורה לחברה`: the offeror bears the duty (a MUST, no clock of its own) to send the copy and the price once the duty has fallen due, and the company the duty (a MUST, no clock) to register him; the DEONTIC for 341(ב) opens it, and it can be run alone for a notice whose month has run out.

### The DEONTICs and their timelines

1. `סעיף 336(א) - הליך: אסור לרכוש מעל תשעים אחוזים אלא בהצעת רכש מלאה שהתקבלה`:
   `-- TIMELINE: unit=none stated; day 0=the day the offeror's holding would pass ninety percent; counting="silent"`
2. `סעיף 337(ב) - הליך: אסור לרכוש מניצעים שנענו מעל תשעים אחוזים כשההצעה לא התקבלה`:
   `-- TIMELINE: unit=none stated; day 0=the day the offeror's purchase from responding offerees would pass ninety percent; counting="silent"`
3. `סעיף 337(א) - הליך: רישום העברת המניות לאחר שהצעת הרכש המלאה התקבלה`:
   `-- TIMELINE: unit=none stated; day 0=the day the full tender offer is accepted; counting="silent"`
4. `סעיף 338 - הליך: בקשת הניצע לסעד הערכה בתוך שישה חודשים`:
   `-- TIMELINE: unit=calendar day (six calendar months turned into days by `add months` from the acceptance date); day 0=the day the full tender offer was accepted; counting="לא יאוחר משישה חודשים ממועד קבלת הצעת הרכש המלאה"`
5. `סעיף 341(א) - הליך: הודעת המציע לבעל מניה מתנגד`:
   `-- TIMELINE: unit=calendar day (the two months turned into days by `add months` from the offer date, then one more month by `add months` from the day the two months end); day 0=the day the offeror made the offer; counting="הסכימו בתוך חודשיים להצעה, רשאי המציע בתוך חודש לאחר תום החודשיים האמורים, להודיע"`
6. `סעיף 341(ב) - הליך: בקשת בעל מניה מתנגד לבית המשפט בתוך חודש ימים`:
   `-- TIMELINE: unit=calendar day (one calendar month turned into days by `add months` from the notice date); day 0=the day of the offeror's notice ("תאריך ההודעה"); counting="בתוך חודש ימים לאחר תאריך ההודעה"; the 341(ג) duty follows it: "בתום חודש ימים מתאריך הודעתו, ואם היתה אותה שעה בקשתו של בעל מניה מתנגד תלויה ועומדת לפני בית המשפט – לאחר שפסק בה בית המשפט"`
7. `סעיף 341(ג) - הליך: העתק ההודעה והתמורה לחברה`:
   `-- TIMELINE: unit=none stated beyond the month the DEONTIC for 341(ב) counts; day 0=the day the duty falls due (the end of a month from the notice, or after the court's ruling on an application then pending); counting="בתום חודש ימים מתאריך הודעתו" (the company's registration: "silent")`

The clock of the six-month and one-month periods is the number of days from the start day to the same day of the month that many calendar months later (the last day of that month if it has no such day), and that last day is inside the period.
The clock of 341(א) now starts when the two months end, so a notice before that day is not a step on this timeline (see the fork on 341(א)).
In 341(ב) and (ג) an early step is not treated as in time: the offeror's duty is not open until the month lapses or the court has ruled, so an early copy and price are ignored and the duty stays open.

### Forks

- `סעיף 336(א)`: the prohibition is a SHANT: the offeror breaches the moment he buys past ninety percent otherwise than by an accepted full offer, and the breach is the statutory-duty breach of section 340(ב); the other reading: a bar that only strips the purchased shares of their rights (340(א), dormant shares) without making the purchase itself a breach.
- `סעיף 336(א)`: whether the full offer was accepted is a fact the caller states when the DEONTIC is run (the Boolean input), so the purchase is judged on the offer's outcome; the other reading: judged only at the moment of the purchase, before the offer's outcome is known.
- `סעיף 337(ב)`: the prohibition is a SHANT with the statutory-duty breach of 340(ב), as for 336(א); the other reading: a bar that only strips the shares of their rights (340(א)).
- `סעיף 337(א)`: the duty to change the ownership records is the company's (it keeps them), with no clock; the other reading: the offeror's duty, or no party's: a pure effect of the Act.
- `סעיף 338(ב)`: the six months run from the day the full tender offer was accepted (the day section 337's test is met), reading "קבלת" with "התקבלה" in 337(א) and 338(א); the other reading: "קבלת" as the offerees' receipt of the offer, which starts the clock earlier: only the start-date input changes.
- `סעיף 338(ב)`: "no later than six months" includes the sixth month's own day, counted in calendar months to the same day of the month (the last day of the month where it has no such day); the other reading: six months of thirty days.
- `סעיף 338(א)`: the court MAY fix the fair value ("רשאי") and does so only if it finds the consideration was below it; the other reading: a MUST once the finding is made.
- `סעיף 338(א)`: where the court finds the consideration was not below fair value, no step remains and the DEONTIC ends FULFILLED, which means the Act lays down nothing further and not that the application succeeded; the other reading: an explicit refusal as an act of the court.
- `סעיף 341(א)`: the notice is a MAY whose window opens when the two months end (day 0) and closes one month later; a notice before the two months end is outside the power and is not a step on this timeline; the other reading: a notice before the two months end counts as in time (the clock holds no lower bound), the reading before the independent review.
- `סעיף 341(א)`: the month after the two months is counted from the day the two months end (the offer day plus two calendar months), the last day inside, so a month-end clamp can apply twice (offer on 30 December 2026: the two months end on 28 February 2027, the last day is 28 March); the other reading: three calendar months from the offer day in one step (30 March), or counted from the day the shareholders' agreement reached the required rate.
- `סעיף 341(ב)`: after the notice the dissenter's duty to sell and the offeror's duty to buy are two duties at once with no clock (a RAND), the court's relief being the other DEONTIC; the other reading: the duties arise only when the offeror's copy and price are sent.
- `סעיף 341(ג)`: "בתום חודש ימים מתאריך הודעתו" is the day the duty falls due, as "לאחר שפסק בה בית המשפט" is for a pending application: the duty opens when the dissenter's month lapses unused or after the court's ruling, and has no last day, so a late copy and price are no breach; the other reading: a last day: a copy and price sent after the month are a breach by the offeror.
- `סעיף 341(ג)`: a copy and price sent before the duty falls due are not the send the subsection asks for and leave the duty open; the other reading: an early send discharges the duty.
- `סעיף 341(ג)`: where the court rules before the month's end, the duty opens at the ruling and not at the month's end (the clock holds no lower bound for the court's step); the other reading: it opens at the month's end in every case.
- `סעיף 341(ב)`: "חודש ימים" is one calendar month from the date of the notice, the last day inside, counted by `add months`; the other reading: thirty days.
- `סעיף 341(ב)`: a court that does not decide otherwise rules on the application as an act (`בית המשפט פוסק בבקשת בעל מניה מתנגד ואינו מחליט אחרת`), because the duty of 341(ג) waits for "after the court has decided it"; the other reading: the ruling is not an act on the trace, so the duty opens at the application.

### Differences from the existing DEONTIC

The Israeli encoding had no DEONTIC for these sections, so there was nothing to read first and nothing to compare line by line.
The places where this layer reads the text differently from the Boolean gate it calls, each with the line that decides it:

- `סעיף 341(ג)` (src:2222, "ישלח המציע, בתום חודש ימים מתאריך הודעתו, ואם היתה אותה שעה בקשתו ... תלויה ועומדת – לאחר שפסק בה בית המשפט"): the Boolean function `סעיף 341(ג) - חובת המציע לשלוח לחברה את ההודעה ולהעביר לה את התמורה` says the duty arises once the month has passed and stands until it is done, with no last day, and the DEONTIC agrees: the month's end, like the court's ruling, is the day the duty falls due, and a late copy or price is no breach. It differs in how it gets there: the month is counted in days as the dissenter's clock in the 341(ב) DEONTIC, the duty opens when that clock lapses (or after the court's ruling), and the Boolean function takes "the month has passed" and "an application is pending" as inputs.
- `סעיף 338` (src:2203, "לא יאוחר משישה חודשים ממועד קבלת הצעת הרכש המלאה"): the Boolean gate takes a number of months elapsed and tests it AT MOST 6, leaving the counting of months to the caller; the DEONTIC counts calendar days from the acceptance date, with the same-day-of-month rule, and passes 0 to the gate's months input so that the clock is not counted twice.
- `סעיף 341(א)` (src:2220, "הסכימו בתוך חודשיים ... רשאי המציע בתוך חודש לאחר תום החודשיים"): the Boolean gate takes the two months and the following month as two numbers of months; the DEONTIC keeps the first (the agreement's months) as the gate's input and makes the second the offeror's clock, counted in days from the day the two months end, passing 0 for it.
- `סעיף 337(א)` (src:2197, "והרישומים של הבעלויות במניות ישונו בהתאם"): the Boolean encoding stops at "the shares pass"; the DEONTIC adds the change of the records as the company's duty (a judgement, the first fork on 337(א)).
- `סעיף 341(ב)` (src:2221): the Boolean encoding gives the dissenters' duty to sell and the offeror's duty to buy as one truth value; the DEONTIC splits them into the two acts and leaves them with no clock.

### What the text leaves silent

- Any period for the prohibitions of 336(א) and 337(ב): none is encoded, so a prohibition nobody has broken stays open and is never a breach.
- Any party and any period for changing the ownership records (337(א)); the shares themselves pass by the Act, with no act of any party.
- Who pays the fair value fixed under 338(א), and by when; and any period for the court's decision (338(א), 341(ב)).
- Any period for the dissenter's sale and the offeror's purchase (341(ב)), and the way the offeror's notice is given ("בדרך שיקבע השר", with the regulations of section 342א, not in the sources).
- Any last day for the offeror's copy and price (341(ג)): the text says when the duty falls due, at the month's end or after the court's ruling, and no day after it; and any period for the company's registration.

### Which binary verified the traces

The unstable binary (`l4-unstable-20261125-a50cbd0-darwin-arm64`) ran both modules with no error diagnostic and 5 of 5 assertions satisfied, and `expect_check.py` matched 44 of 44 traces.
The stable binary (the stable build 112) ran both modules with no error diagnostic and 5 of 5 assertions satisfied, and matched 37 of 44 traces; the seven that class differently are listed in the test file's `-- READS-DIFFERENTLY-ON-MAIN:` block and below.
The only warnings either binary prints for these files are the two import-resolution warnings about the user data directory's copies of `prelude` and `daydate`, which every module in the folder prints, including the existing derivative-claim module.
The `srcrefs.py check --refs` run reports 20 `src:` lines, 12 locators and no problem.
Three mutated copies were run on the unstable binary and deleted.
The last was made from this final text: it ended the 341(ב) month's LEST in FULFILLED (so the 341(ג) duty never opens), made the 341(ב) month two months, and cut the 341(א) count to two months, and it turned 6 traces into mismatches, one for each of those three changes' effects (lines 160, 170, 180 and 212 for the 341(א) clock, line 230 for the 341(ב) month, line 237 for the missing opening).
The first two copies were made on earlier text and turned 6 and 3 traces into mismatches (six months to five in 338, one month to two in 341(ב), `OR` to `AND` in 337(א), among others); they are not re-run on this text, except for the 341(ב) month, which the last copy repeats.
The day counts in the tests (181, 181, 31, 28 and 28 days, and the 90-day count that the other reading of 341(א) would give) were worked out from the calendar with a date library, not from l4.

### READS-DIFFERENTLY-ON-MAIN

Seven traces class as RESIDUAL on the stable binary where the unstable one gives FULFILLED: 338 with an application on day 182 (two traces) and with no application by day 200, 341(א) with a notice on day 32, on day 29 of the 30 December offer, and with no notice by day 40, and 341(ב) with an application on day 29 followed by the offeror's copy and the company's registration.
All seven are a late act or a lapse of a MAY whose HENCE is a further step; the stable result is that further step left open.
One more trace (341(ג), no application by day 100) is RESIDUAL on both, but the open step differs: the offeror's duty on the unstable binary, the court's step on the stable one.
Every in-time trace and every gate-fails trace gives the same class on both binaries.

### What was not encoded, and why

- The prohibition of 336(ב) and (ג) on a holder above ninety percent buying more: it has the shape of the 336(א) SHANT and the existing three-valued gate `סעיף 336(ב) ו־(ג) - רכישת מניות נוספות בידי מי שמחזיק למעלה מתשעים אחוזים` already answers it; its acceptance under 336(ג) is an input of the 337(א) and 338 DEONTICs, as it is of the Boolean 338 gate.
- The making of the full tender offer, and of the offer in a private company: the text gives no power or duty to make them beyond the prohibitions, so no step stands for them.
- Sections 339 (the company becomes private) and 340(א) (dormant shares): each states a status that follows from the facts, with no act and no clock; the Boolean gates carry them.
- Section 340(ב) is not a separate duty: it is the wording of the BREACH of the two prohibitions.
- The count of disinterested offerees and section 276 (337(א)), the exclusion of the offeror's controllers from the 80 percent count (341(א)), and the change of the articles under sections 20 and 350 (341(ד), 342): inputs of the existing gates, outside this unit.
- A step for a notice given before the two months end (341(א)): the window opens when the two months end, so an early notice is not a step on the timeline and no trace shows it.

### Closed routes (not breaches)

The convention for the whole procedure layer is assumed, not ruled: BREACH is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and listed below.
A step the Court is bound by may keep a BREACH BY the court; this unit has none.

- 338(ב): the offeree's six months to apply for a valuation lapse unused: the LEST ends FULFILLED.
- 341(א): the offeror's month to notify lapses unused: FULFILLED (the power is gone).
- 341(ב): the dissenter's month to apply lapses unused: the lapse opens the offeror's 341(ג) duty, and is no breach.
- 336(א) and 337(ב) are prohibitions on the offeror by name, so buying past ninety percent otherwise than as the text allows stays a BREACH BY the offeror (the statutory-duty breach of 340(ב)).

### Changes after the independent review

- `סעיף 341(א)` (IL-forced-sale-1, answer changed): the window opens when the two months end (src:2220 "בתוך חודש לאחר תום החודשיים האמורים"), so day 0 of that DEONTIC is the day the two months end and a notice before it is not a step; the eight 341(א) traces with an event or a wait after day 0 were re-timed (a notice on the last day is now day 31 for the 31 October offer and day 28 for the 30 December offer), and no EXPECT class changed.
- `סעיף 341(ג)` (IL-forced-sale-2, not changed): where the court rules before the month ends the duty still opens at the ruling and not at the later of the month's end and the ruling. The text reads "אותה שעה" as the month's end (src:2222), but the clock of this DEONTIC cannot wait out the rest of the month after an early ruling, because the days left depend on the ruling's date, which is not known when the clock is set; so the reading stays, the fork says so, and the later reading needs a way to hold a step until a day.
- The verification lines give the new day numbers.
