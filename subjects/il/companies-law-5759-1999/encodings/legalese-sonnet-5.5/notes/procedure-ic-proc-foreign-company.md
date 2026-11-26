## Procedure layer: a foreign company's place of business in Israel (sections 346 to 349א)

This layer adds six DEONTICs over the Boolean encoding in `ic6-foreign-company.l4`, in `ic-proc-foreign-company.l4`, tested in `ic-proc-foreign-company-tests.l4`.
It adds six Boolean or number helpers, and the helper DEONTIC `סעיף 348 - דין וחשבון שנתי אחד` (one yearly report) and changes no existing module.
It calls the existing rules `חברת חוץ` (the core definition), `סעיף 346(א) - חברת חוץ רשאית לקיים בישראל מקום עסקים`, `סעיף 346(ב) - צורפו לבקשה כל המסמכים הנדרשים`, `סעיף 346(ג1) - הרשם צריך לרשום את המען הדיגיטלי`, `סעיף 349 - חברת חוץ הפרה את סעיף 346(א)`, `סעיף 349 - החברה חבה בקנס לפי סעיף 61(א)(2) לחוק העונשין`, `סעיף 349 - נושא משרה או שלוח של חברת החוץ חב בקנס` and `סעיף 349א(א) - המועד שממנו חברת החוץ פטורה מחובותיה לפי הפרק`.
The source is the Hebrew Wikisource text, lines 2958 to 2985.

### Differences from the existing DEONTIC

There is no earlier DEONTIC for these sections, so there is nothing to compare.
The places where the layer reads the text differently from the Boolean rules are listed under "Where the layer departs from the Boolean rules" below.

### Where each DEONTIC sits, and whose seat it is

All six sit in `ic-proc-foreign-company.l4`, under the heading for the section they carry.
None is wired into `ic6-seat.l4`, because that would edit an existing module.
The parties are the foreign company, an office-holder or agent of it who took part in a violation (section 349), and the Registrar of Companies.

| DEONTIC | section | seat |
| --- | --- | --- |
| `סעיף 346(ב) - הגשת הבקשה לרישום בתוך חודש` | 346(ב), with (ד) in the documents | the company MUST apply, with every required document, within a month |
| `סעיף 346(ג) - ההודעה לרשם על שינוי בתוך ארבעה עשר ימים` | 346(ג), (ד) | the company MUST tell the Registrar of a change within fourteen days |
| `סעיף 346(ג1) - רישום המען הדיגיטלי בידי הרשם` | 346(ג1) | the Registrar MUST enter the digital address, no clock |
| `סעיף 348 - הדין וחשבון השנתי של חברת חוץ` | 348 | the company MUST file a yearly report within a year (the first from registration, each next from the one before), three in a row, then a permission to file the next |
| `סעיפים 346(א) ו־349 - האיסור לקיים מקום עסקים ללא רישום והקנס` | 346(א), 349 | the company SHANT keep a place of business unless registered and paid; keeping one is a BREACH BY the company (and by an office-holder or agent who took part), the fine being named in the reason |
| `סעיף 349א - ההודעה על הפסקת מקום העסקים והמען האחר` | 349א | the company MAY tell the Registrar it has stopped, then MAY give another address for service |

### The TIMELINE lines

- 346(ב): unit=calendar day; day 0=the day the place of business is set up in Israel; counting="בתוך חודש לאחר הקמת מקום העסקים".
  The month is turned into days from the date: the days between the start day and the same day of the next month (the library's `add months`), which is 28 for a start on 31 January 2026 and 31 for a start on 15 January 2026.
  The helper `סעיף 346(ב) - מספר הימים להגשת הבקשה לרישום` does the sum, and an `#ASSERT` pair agrees with the Boolean rule of `ic6-foreign-company.l4` on both sides of the last day.
- 346(ג): unit=calendar day; day 0=the day of the change; counting="בתוך ארבעה עשר ימים ממועד השינוי".
- 346(ג1): unit=none stated; day 0=the day both conditions are met; counting="silent".
- 348: unit=calendar day; day 0=the day the company registers under 346 (assumed, not ruled); counting="אחת לשנה": the first year by `add years` from the registration day, each later year 365 days from the previous report.
- 346(א), 349: unit=none stated; day 0=the day the ban applies to the company; counting="silent".
- 349א: unit=none stated; day 0=the day the company stopped keeping a place of business; counting="silent".

### The forks

- 346(ב): the month starts on the day of setting up (day 0), and the same day of the next month is the last day in time; the other reading starts the month on the next day.
- 346(ב): a missed application is a terminal BREACH BY the company with no further step; the text names no consequence for it, and the fine of section 349 is for breaking 346(א).
- 346(ב): an application lacking a required document does not count, so the duty stays open and the month runs on; the other reading lets an incomplete application discharge the duty.
- 346(ב): a company that stopped and told the Registrar on or before the last day owes no application; the other reading says the exemption does not reach a duty already running.
- 346(ב) and 346(ג), the 349א(ב) override: the exit of 349א(א) lifts the whole duty, although src:2981 ("על אף הוראות סעיף קטן (א)") keeps a company that gave the notice bound by 346(ב)(3), the authorised person in Israel for service, until it gives another address.
  The DEONTICs do not call `סעיף 349א(ב) - חברת חוץ נשארה חייבת בחובה שבסעיף 346(ב)(3)`, and the change trigger of 346(ג) is not split to show a change in the (3) person's details.
  The other reading keeps the duty for those details unless the company has given another address.
- 346(ג): the day of the change is day 0 and the fourteenth day is the last in time; the other reading makes the day of the change day 1.
- 346(ג): one trigger covers a change in a document, the directors, or the details of the persons of paragraphs (3) and (4), and a change in a document the Minister added under (ד) is a second; the other reading makes separate duties for each kind.
- 346(ג): any notice on or before the fourteenth day discharges the duty, since the text states no form.
- 346(ג1): the Registrar's entry is a MUST that arises once both conditions hold, and it is a separate DEONTIC from the application and the notice; the other reading chains it after them.
- 346(ג1): before both conditions hold the DEONTIC ends FULFILLED, which means only that the Act lays down no step for those facts.
- 348: the year runs from the day the company registers under 346 (the text names no start day: assumed, not ruled), then from each report to the next; the other reading is no clock on the first report, as the Boolean rule answers NOTHING until a previous report exists.
- 348: a report missed within its year is a terminal BREACH BY the company ("תגיש" lays the duty on the company by name, and "אחת לשנה" fixes the cadence); the other reading leaves the timing to the Minister and makes a late report no breach.
- 348: the first year is `add years` from the registration day and each later year is 365 days from the previous report, since that report's date is not known when the clock is set; the other reading is `add years` for every year.
- 348: three yearly reports are encoded and the rule then stays open on a permission to file the next, which stands for the later years not encoded here; the other reading is an unbounded chain.
- 348: the duty binds every foreign company until it has stopped and told the Registrar; the other reading limits it to a company registered under 346 and not yet exempt.
- 348: a report not in the Minister's form does not count; the other reading lets it discharge the duty.
- 348: a report not in the Minister's form does not count, so its year runs on to a BREACH.
- 346(א): the ban has no grace period, and the month of 346(ב) is the time for the application only; the other reading makes that month a grace period in which the ban is not broken.
- 349: keeping the place of business while unregistered is a BREACH BY the company and, in addition (a RAND), BY an office-holder or agent who took part; the fine is named in the reason, because the text makes it the punishment a court imposes (src:2977) and paying it does not undo the breach; the other reading is the duty to pay the fine, the reading before the independent review.
- 349: registration and payment are taken as they stood when the company kept the place of business; the other reading ends the ban the day the company registers and pays.
- 349א(א): the notice is a MAY with no time limit, and the exemption starts the day it is given; the other reading is a MUST whose lapse is a breach.
- 349א(ב): giving another address is a MAY after the notice, with no time limit; the continuing duty of 346(ב)(3) is not encoded as a step.

### What the text leaves silent

- The time within which the Registrar must enter the digital address (346(ג1)); no clock is encoded, and the duty is never a breach.
- The day from which the yearly clock of 348 runs: the text names none, so the layer starts it on the registration day (a fork, assumed, not ruled); the report's content and form are the Minister's ("כפי שיקבע השר").
- The time within which the company may give notice that it has stopped, and the time for the further address (349א); no clock is encoded for either.
- The amount of the fine and when it falls due (349); those are the Penal Law's and a court's, so the fine is named in the reason of the breach and is not a step.
- Who registers the company and when (346(א) says "נרשמה"); no duty of the Registrar to register on an application is stated, so none is encoded.
- Any consequence of a late application under 346(ב); section 349 punishes only a breach of 346(א).

### Which binary verified the traces

Both.
All 50 traces match their EXPECT on the unstable binary (`l4-unstable-20261125-a50cbd0`) and on the stable one (main, the stable build 112).
All 21 `#ASSERT` lines are satisfied on both.
The only warnings printed are the two `Import Resolution` ones about a shadowed copy of `prelude` and `daydate` in the XDG data directory; they come from the machine, not from these files, and the existing `ic-proc-register-access.l4` prints the same two.
Two mutated scratch copies were run as a sensitivity check and then deleted: changing the fourteen days to fifteen made three traces fail (the day-15 notice, the day-15 notice for a further document, and the notice of cessation on day 15), and removing the two `PROVIDED` guards (the application's documents, the report's form) made two traces fail.

### The READS-DIFFERENTLY-ON-MAIN list

None.
No trace in this layer lapses a MAY that has a LEST after it, and the RAND of 349 ends in the same class on both binaries whichever side has paid.

### Where the layer departs from the Boolean rules

- Section 348 here counts the first year from the registration day, where the Boolean rule answers NOTHING until a previous report exists, and counts each later year as 365 days from the previous report, where the Boolean rule uses `add years`.
- A change in a document the Minister added under 346(ד) triggers the notice duty here (`סעיף 346(ג) ו־(ד) - חלה חובה להודיע לרשם על שינוי`, a new helper).
  The Boolean rule `סעיף 346(ג) ו־(ד) - החברה עמדה בחובת ההודעה על שינוי` now agrees: it takes a second change input, for a further document the Minister required, and applies the same fourteen days to it (assumed, not ruled; see `NOTES-ic6.md`).

### What was not encoded, and why

- Section 347 (deemed service on a registered foreign company): it states what the law treats as done, not a step anyone must or may take, and the Boolean rule `סעיף 347 - יראו את כתב בי־דין או ההודעה כאילו הומצאו כדין לחברת חוץ` already answers it.
- The further fine of section 61(ג) of the Penal Law for each day a continuing violation goes on, and the Registrar's notice that starts the count (349): it is a count of days, which the rule `סעיף 349 - מספר הימים שבגינם נוסף קנס יומי` returns, and the text names no act to be done on any day.
- The status of 349א(ב) that no court permission is needed to serve a company that gave an address outside Israel: it is a state of the law, held by `סעיף 349א(ב) - אין צורך בהיתר בית משפט להמצאת כתבי בי־דין לחברת חוץ`.
- The Minister's earlier day of exemption from the fee (349א(א)): it concerns the fee only, and no DEONTIC here is about the fee.
- The Minister's power to require further documents (346(ד)): it is a power of the Minister, not a step in the procedure; its effect on the duties is in the document record and the change helper.
- The fees themselves (346(א)): the Minister fixes them, and payment is a plain fact.
- The digital-address conditions of section 3ב of the Digital Communication with Public Bodies Law: another Law's, taken as a plain fact.

### Closed routes (not breaches)

The convention for the whole procedure layer is assumed, not ruled: BREACH is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and listed below.
A step the Court is bound by may keep a BREACH BY the court; this unit has none.

- 349א(א): the exemption from the day the Registrar is told is a route closed: the duties of 346(ב) and 348 end FULFILLED for a company that has stopped and told the Registrar.
- 349א: the notice of cessation and the further address are permissions with no clock and never lapse.
- 346(ב), 346(ג), 348 and the ban of 346(א) with 349 are duties and a prohibition laid on named parties, so they keep their BREACH.

### Changes after the independent review

- `סעיף 348` (IL-foreign-company-1, answer changed): a yearly clock replaces the open duty. The first report is due within `add years` 1 from the registration day (assumed, not ruled: the text names no start), each later one 365 days after the one before it, three in a row, and after the third a permission to file the next stays open; a missed report is a BREACH BY the company. Four existing traces changed class (no report for 5,000 days, a report on day 400, a report not in the Minister's form, and a company that stopped but did not tell the Registrar, each from open or FULFILLED to BREACH) and four were added.
- `סעיפים 346(א) ו־349` (IL-foreign-company-2, answer changed): keeping the place of business while unregistered is now a BREACH BY the company and, where the gate holds, BY the office-holder or agent who took part, with the fine named in the reason; paying the fine no longer ends it. Seven traces changed class, from open or FULFILLED to BREACH.
- The module's `-- FORK:` lines for 348 and 349 and the TIMELINE line for 348 were rewritten; the first observation of the NOTES.md section now cites `ic6-foreign-company.l4:74-81`.
