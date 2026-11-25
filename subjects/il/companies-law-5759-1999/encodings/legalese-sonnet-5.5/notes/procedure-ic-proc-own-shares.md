## Procedure layer: a distribution and the company's purchase of its own shares (sections 301 to 311)

This layer adds nine DEONTICs over the Boolean encoding in `ic3-part7-ch2-distributions.l4`, in `ic-proc-own-shares.l4`, tested in `ic-proc-own-shares-tests.l4`.
It adds no definition to an existing module, and calls the existing gates instead of restating them: `חלוקה` (section 1), `סעיף 302(א)` (both tests), `סעיף 302(ב)` (profits), `סעיף 303(א)` and `303(ד)` (the court's power and the creditors' hearing), `סעיף 308(א)` and `308(ב)`, `סעיף 309(א)`, `309(ג)` and `309(ד)`, `סעיף 310(א)` and `310(ב)`, `סעיף 311`.

### A purchase of its own shares is a distribution

Section 1 (source line 209) defines "חלוקה" as giving a dividend or undertaking to give one, "וכן רכישה", and defines "רכישה" for this purpose as the purchase of the company's shares, or of securities convertible into or exercisable for them, by the company, its subsidiary or another corporation it controls, "ובלבד שהמוכר אינו החברה עצמה או תאגיד אחר בבעלותה המלאה".
So the company's purchase of its own shares from a shareholder goes through sections 302 and 303 like a dividend, and a purchase from the company itself or from a wholly owned corporation does not.
The core's `חלוקה` already answers that, and the first DEONTIC calls it: two `#ASSERT` lines in the tests check it on a purchase from a shareholder (a distribution) and a purchase from a wholly owned corporation (not one), and two traces run the same two facts through the procedure.

### Where each DEONTIC sits, and whose seat it is

All nine sit in `ic-proc-own-shares.l4`, under the heading for the section they carry.
None is wired into `ic3-seat.l4`, because that would edit an existing module.
Chained: the application to the court, then the notice to creditors, then the court's decision, which opens the company's own distribution.
Chained: the subsidiary's board's determination, then the acquiring corporation's purchase.
Separate, each run on its own once a forbidden distribution has been made (`בוצעה חלוקה אסורה` is an input): the shareholder's return (section 310) and the directors' deemed breach (section 311).

- `סעיפים 301 עד 303 - הליך החלוקה`: the company holds the power to distribute when both tests are met, or to apply to the court when the profit test is not met; it calls the next three.
- `סעיף 303(ב) - ההודעה לנושים על הבקשה`: the company bears the duty to notify its creditors of the application, in the manner the Minister sets.
- `סעיף 303(ג) - התנגדות נושה ואחריה החלטת בית המשפט`: a creditor holds the power to object; the court may decide with or without an objection.
- `סעיף 303(ד) - החלטת בית המשפט בבקשה`: the court holds the power to approve in whole or in part, to approve on conditions, or to refuse; an approval opens the company's distribution.
- `סעיף 308(א) - ביטול מניה שנרכשה`: the company holds the power to cancel a share it bought.
- `סעיף 308(ב) - ניירות ערך שנרכשו`: the company holds the power to cancel securities it bought, to sell them again, or to convert or exercise them into shares (alternatives).
- `סעיף 309(א) - רכישה בידי חברה בת או תאגיד רוכש`: the subsidiary's board or the acquiring corporation's managers hold the power to determine that the purchase would have been a permitted distribution; the acquiring corporation then holds the power to buy.
- `סעיף 310(א) - השבת חלוקה אסורה`: the shareholder bears the duty to return what he received (to the company, or to the subsidiary or acquiring corporation under section 309(ג)).
- `סעיף 311 - אחריות הדירקטורים לחלוקה אסורה`: the director is regarded as having breached his duties; the party is the company's director, the subsidiary's director or the acquiring corporation's manager, or the parent's director, as section 309(ג) allocates it.

### The DEONTICs and their timelines

No step in sections 301 to 311 has a time limit, so none of the nine has a clock.
The one period in these sections is the six months of section 302(ב), a look-back from the distribution to the date the financial statements are made up to; it is a gate worked out from two DATE inputs (`סעיף 302(ב) - מספר החודשים שבין מועד הדוחות למועד החלוקה, מעוגל כלפי מעלה`), and the existing profits rule applies "at most 6" to it.
The count rounds up, so six months to the day is in time (31 December to 30 June, and 15 January to 15 July) and a day more is not (1 July, 16 July).

1. `סעיפים 301 עד 303 - הליך החלוקה`:
   `-- TIMELINE: unit=none stated; day 0=the day the company's right to distribute, or to apply to the court, arises; counting="silent"`
2. `סעיף 303(ב) - ההודעה לנושים על הבקשה`:
   `-- TIMELINE: unit=none stated; day 0=the day the company's application is filed; counting="silent"`
3. `סעיף 303(ג) - התנגדות נושה ואחריה החלטת בית המשפט`:
   `-- TIMELINE: unit=none stated; day 0=the day the company's application is filed; counting="silent"`
4. `סעיף 303(ד) - החלטת בית המשפט בבקשה`:
   `-- TIMELINE: unit=none stated; day 0=the day the company's application is filed; counting="silent"`
5. `סעיף 308(א) - ביטול מניה שנרכשה`:
   `-- TIMELINE: unit=none stated; day 0=the day the company bought the share; counting="silent"`
6. `סעיף 308(ב) - ניירות ערך שנרכשו`:
   `-- TIMELINE: unit=none stated; day 0=the day the company bought the securities; counting="silent"`
7. `סעיף 309(א) - רכישה בידי חברה בת או תאגיד רוכש`:
   `-- TIMELINE: unit=none stated; day 0=the day the subsidiary's board takes up the question; counting="silent"`
8. `סעיף 310(א) - השבת חלוקה אסורה`:
   `-- TIMELINE: unit=none stated; day 0=the day the forbidden distribution was made; counting="silent"`
9. `סעיף 311 - אחריות הדירקטורים לחלוקה אסורה`:
   `-- TIMELINE: unit=none stated; day 0=the day of the distribution; counting="silent"`

Because there is no clock, the tests have no "in time", "last day" or "after the period" trace for a step; the six-month boundary is tested instead, at the day, through the procedure (statements made up to 31 December 2025: a distribution on 30 June 2026 passes the profit test, one on 1 July 2026 does not) and through `#ASSERT` lines on the month count.

### Forks

- `סעיפים 302 ו־303`: the company's distribution is a MAY with no time limit; the other reading is a MUST.
- `סעיף 302(ב)`: six months to the day is in time, and a month shorter than the statements' day counts as complete at its last day; the other reading makes the sixth month incomplete until the same day of the month.
- `סעיף 302(ב)`: the six months are measured back from the distribution date (src:2009 "ממועד החלוקה"), so statements to 30 June are in time for a distribution on 31 December; the other reading counts forward from the statements' date and rounds up, which gives seven and fails the profit test.
- `סעיף 303`: the court's decision follows the notice to creditors (src:2017, 2019 and 2020 presuppose it), so an approval given before any notice does not count and the duty to notify stays open; the other reading runs the two side by side (a RAND), the reading before the independent review.
- `סעיף 303(א)`: the company may apply whenever the profit test is not met, whatever the solvency position; the other reading limits the application to a company whose solvency test is met.
- `סעיף 303(ב)`: a notice not in the manner the Minister sets does not discharge the duty; the other reading lets any notice discharge it.
- `סעיף 303(ד)`: the hearing of the objecting creditors is a condition of all three of the court's decisions; the other reading attaches it to approval only.
- `סעיף 303(ד)`: approval in whole or in part is one act; the other reading splits it into two.
- `סעיף 303`: a refusal is an act of the court and the DEONTIC then ends FULFILLED (no step remains, not that the distribution was approved); the other reading leaves the route open.
- `סעיף 301(א)`: the company's own undertaking in its articles or by contract is not an input; the other reading takes it and its additional limits as inputs.
- `סעיף 308(א)`: cancelling is a MAY with no time limit, and non-cancellation is a status (dormancy), not a duty; the other reading is a MUST to cancel or hold the share dormant.
- `סעיף 308(ב)`: cancelling, selling again and converting are alternatives; the other reading lets the company do part of each.
- `סעיף 309(א)`: the board's determination is a MAY that opens the permission to buy; the other reading is a MUST before any purchase.
- `סעיף 309(ד)`: for a part-owned subsidiary the amount set against the parent's capacity is the purchase times the parent's share; the other reading sets the whole purchase against it.
- `סעיף 309(א)`: the parent's capacity to distribute is an input; the other reading computes it here from the parent's profits.
- `סעיף 309(ג)`: the return to the subsidiary or the acquiring corporation is a different act from the return to the company, and the wrong one does not discharge the duty; the other reading is one act of returning.
- `סעיף 310(א)`: the return is a MUST with no time limit; the other reading is a MAY.
- `סעיף 310(א)`: the duty arises only for a shareholder who received something; the other reading arises for every shareholder.
- `סעיף 311`: the deemed breach is a BREACH BY the director, reached with no event and no clock; the other reading has no DEONTIC and leaves the deeming in the Boolean gate.
- `סעיף 311`: "unless he proves" is an input that the proof was made; the other reading makes the proof an act in the trace.

### What the text leaves silent

- Any time within which the company must distribute, apply to the court, or notify its creditors: none is encoded, so the notice, once the application is made, stays open however long it waits and is never a breach.
- Any time within which a creditor may object, or the court must decide, or the court's conditions must be met: none is encoded.
- Any consequence of a missed notice: the text states none, so the notice duty carries no breach and no effect on the court's power.
- Any time for cancelling a share or securities the company bought, or for selling or converting the securities.
- Any time within which the subsidiary's board must make its determination, or the acquiring corporation must buy.
- Any time within which a shareholder must return what he received.
- What the court's conditions are, and how much of an application it approves "in part": the court's decision, not computed.
- The manner of the notice to creditors: it is fixed by regulations (2001) that are not among the sources, so it is a plain input.
- Section 311 gives no time for the director's proof and no step beyond the deemed breach of the duties in sections 252 to 254, which are another part of the Act.

### How the traces were verified

There are 44 traces in `ic-proc-own-shares-tests.l4` and 18 `#ASSERT` lines (the month count, the profit test from dates, the amount counted against the parent's capacity, and section 1's definition), every EXPECT written from the text before the trace was run.
All 44 traces match on the unstable binary (`l4-unstable-20261125-a50cbd0`), and all 18 assertions are satisfied.
Both binaries give zero error diagnostics and no warning of their own on the module and its tests (`l4 check` prints an import-resolution warning about two copies of `daydate` or `prelude` on this machine, which is a machine effect).
Each prints two import-resolution notices (the machine's own copies of `prelude` and `daydate` differ from the embedded ones); they are not diagnostics of these files.
The stable binary is the stable build 112: all 44 traces match on it as well, and all 18 assertions are satisfied.
How a trace is classed: FULFILLED is exactly `FULFILLED`; BREACH is a `DEONTIC BREACHED`; RESIDUAL is any obligation or permission still open.
An act whose proviso fails does not count and the step stays open, so a refusal without a hearing, an approval without the court's satisfaction on solvency, a conditional distribution before the conditions are met, a purchase before the determination, and a notice in the wrong manner each end RESIDUAL.

Two mutated scratch copies were run on the unstable binary and deleted.
The first changed the six-month limit in a Boolean helper (since removed, because the profits rule already carries the limit) and made the notice and the court's decision an alternative instead of side by side: five traces failed, all from the second change, so the joining was tested (the layer has since chained the decision after the notice, see below).
The second dropped the notice's manner proviso and set 309(ד) aside: one trace failed (the part-owned subsidiary at exactly the parent's capacity), and it showed that the notice-manner trace had no teeth, since it ended RESIDUAL either way.
After that run the manner trace was extended to include the court's refusal, and the trace for an approval when the court is not satisfied on solvency was extended to include the company's distribution; both were re-run against the real module (they match) but not against a new mutant.

### READS-DIFFERENTLY-ON-MAIN

None: all 44 traces class the same on the stable binary as on the unstable one.
The known differences need a lapsed MAY, a LEST clock, a RAND of two breaches, or an event after a wait device, and no step in these sections carries a clock or a LEST.
The test file ends with the same statement.

### Differences from the existing DEONTIC

There is none: the encoding had no DEONTIC for these provisions, so there is nothing to compare.

### What I did not encode, and why

- Section 301(א), second limb: the company's own undertaking in its articles or by contract not to distribute under further limits. It is a limit the company took on itself, already answered by `סעיף 301(א)`; the MAY states what the Act permits.
- Section 301(ב): a forbidden distribution is an input to the separate DEONTICs for sections 310 and 311, not computed from the tests there; running the procedure and then those two is the caller's step.
- Section 302(ג) and the 2012 regulations on surpluses: the Minister's presumptions and exemptions are not among the sources.
- Section 304 (shares issued below par), section 305 (regulations), sections 306 and 307 (the shareholder's right to a dividend and who decides on it) and section 312 (redeemable securities): not among the provisions this layer carries; the Boolean gates stand and none has a time limit.
- Section 308: the dormant state of a share or of shares converted from securities is a status, not a step; `סעיף 308(א) - המניה היא מניה רדומה` and `סעיף 308(ב) - המניות שהומרו או מומשו הן מניות רדומות` carry it. The sale or cancellation of shares once converted is not in the text.
- Section 309(ב): that a share of the parent bought by a subsidiary carries no voting rights is a status (`סעיף 309(ב) - המניה קונה זכויות הצבעה`).
- Section 309א: the part of a purchase of convertible securities that is not a distribution, up to the liability shown in the last adjusted statements, is an amount, answered by `סעיף 309א - החלק ברכישה שנחשב חלוקה`; the DEONTIC takes the purchase amount as given.
- Section 310(ב): the presumption that a public company's ordinary shareholder did not know is evidence, not an act; it is called through `סעיף 310(ב)` and decides whether the duty in section 310(א) arises.
- Section 311: the director's proof of one of the three defences is not a step; it is an input.
- A purchase by the subsidiary or the acquiring corporation is itself the parent's distribution (section 1); the parent's own run of the procedure is how its capacity (`היקף החלוקה שהחברה האם רשאית לבצע`) is established, and it is an input to section 309(א).

### Closed routes (not breaches)

The convention for the whole procedure layer is assumed, not ruled: BREACH is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and listed below.
A step the Court is bound by may keep a BREACH BY the court; this unit has none.

- 303(ד): a refusal by the court ends the route with FULFILLED (no step remains, not that the distribution was approved).
- 302(א) and 303(א): where the profit test is met but the solvency test is not, the Act gives no route and the DEONTIC ends FULFILLED.
- 308 and 309: cancelling, re-selling, converting and buying are powers with no clock and no breach.
- 311 is a deemed breach laid on directors by name, so it stays a BREACH BY the director.

### Changes after the independent review

- `סעיף 302(ב)` (IL-own-shares-1, answer changed for month-end statements): the six months are now measured back from the distribution date; the helper caps the count at six when the statements' date is on or after the date six calendar months before the distribution and gives at least seven otherwise; three assertions were added (30 June to 31 December is six, 30 September to 31 March is six, 29 June to 31 December is seven); no trace EXPECT changed.
- `srcrefs --strict` (IL-own-shares-2): the six problems were fixed by quoting src:2007 above its `@ref`, narrowing the 301 to 303 locator to src:2002-2016, quoting src:2051-2053 and widening the 309 locator to src:2049-2053, and adding src:2052 to the 310 locator; the result is 0 problems.
- `סעיף 303` (IL-own-shares-3): the court's decision now follows the notice, so an approval before any notice does not count; no EXPECT changed (the trace that approves before any notice already ended RESIDUAL), and its scenario comment now says why.
