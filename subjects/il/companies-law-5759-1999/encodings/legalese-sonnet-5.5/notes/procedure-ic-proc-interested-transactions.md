## Procedure layer: a personal interest in a transaction (sections 269 to 272, 278, 280 and 283)

This layer adds three DEONTICs over the Boolean encoding in `ic3-part6-ch5-interested-transactions.l4`, in `ic-proc-interested-transactions.l4`, tested in `ic-proc-interested-transactions-tests.l4`.
It adds no definition to an existing module, and calls the existing gates instead of restating them: `סעיף 269(א)` (who must disclose), `סעיף 269(ב)` (when the duty does not apply), `סעיף 270` (the transaction is for the company's benefit), `סעיף 271`, `סעיף 272(א) ו־(ב)` and `סעיף 272(ד)` (the approvals each kind of transaction needs), `סעיף 278(ג)` (the general meeting's approval when most directors are interested), `סעיף 277` (joining the approvals), `סעיף 278` (who may be present and who may vote) and `סעיף 283(א)` (what a missed disclosure is).
One new helper is added, a NUMBER function, `סעיף 269(א) - מספר הימים עד ישיבת הדירקטוריון`, which turns two dates into the number of days the disclosure clock runs; the tests file has seven `#ASSERT`s, four on the helper's numbers and three tying it to the Boolean gate `סעיף 269(א) - הגילוי נעשה במועד`.

### Where each DEONTIC sits, and whose seat it is

All three sit in `ic-proc-interested-transactions.l4`, under the heading for the sections they carry.
None is wired into `ic3-seat.l4`, because that would edit an existing module.
They are separate, not chained: the Act joins the disclosure, the approvals and the abstention by no step of its own.

- `סעיפים 269 ו־283(א) - הליך: גילוי הענין האישי`: the person who has the personal interest (an office holder, or a controlling shareholder of a public company or a private bond company) bears the duty to disclose; a missed disclosure ends in a terminal BREACH BY that person whose reason names the duty breached (loyalty for an office holder, fairness for a controlling shareholder), which is the consequence section 283(א) gives.
- `סעיפים 270 עד 272 ו־278(ג) - הליך: אישורי העסקה`: the audit committee, the board and the general meeting each hold the power to approve; which of them the transaction needs is read from the existing gates, not restated.
- `סעיף 278 - הליך: הימנעות מהדיון ומההצבעה`: the person with a personal interest in approving the transaction bears the two prohibitions, to be absent from the discussion and not to vote, each a SHANT, joined by RAND when both bind.

### The DEONTICs and their timelines

1. `סעיפים 269 ו־283(א) - הליך: גילוי הענין האישי`:
   `-- TIMELINE: unit=calendar day; day 0=the day the person comes to know of the personal interest in the existing or proposed transaction; counting="בלא דיחוי, ולא יאוחר מישיבת הדירקטוריון שבה נדונה העסקה לראשונה" (the days from day 0 to the day of that meeting, from two DATE inputs; the meeting day itself is in time)`
2. `סעיפים 270 עד 272 ו־278(ג) - הליך: אישורי העסקה`:
   `-- TIMELINE: unit=none stated; day 0=the day the transaction is brought for approval; counting="silent"`
3. `סעיף 278 - הליך: הימנעות מהדיון ומההצבעה`:
   `-- TIMELINE: unit=none stated; day 0=the day the transaction is brought to the audit committee or the board; counting="silent"`

### The shape of the approvals DEONTIC

The record of approvals the transaction needs is built by joining the answers of sections 271, 272(א) and (ב), 272(ד) and 278(ג) with section 277's joiner, and the DEONTIC then walks it.
Where the audit committee is needed its approval comes first (272(א): "ולאחר מכן").
Then, where the board and the general meeting are both needed, they are joined by RAND, because the text states no order between them (272(ב), 278(ג)); where one is needed it stands alone; where neither is needed the DEONTIC ends FULFILLED.
Each approval is a MAY with no clock: the text says the transaction "needs" the approval (טעונה אישור), not that any body must give it.
A board approval given before the committee's does not count, and the board's step opens only once the committee has approved (the traces at lines 253 and 260 of the tests file show it: board on day 3 and committee on day 5 stays open; board again on day 9 completes it).

How a trace ends says only what this layer lists.
FULFILLED means every approval the layer lists has been given, or that the layer lays down none; it does not certify that the transaction is valid, because 280(א) also denies force for a material defect in the approval process or a material departure from the approval.
RESIDUAL means an approval is still missing, and section 280 may then deny the transaction force: 280(א) reaches a transaction with the office holder himself or one under 270(4) or (4א), and 280(ב) reaches another person who knew of the interest and knew or should have known of the missing approval.
Which of those applies to a given transaction is answered by the existing gates `סעיף 280(א)` and `סעיף 280(ב)`, not here; the Act names no act or duty for that state, so nothing more is encoded.

### Forks

- `סעיף 269(א)`: the disclosure is a MUST whose clock is the number of days from the day the person comes to know of the interest to the day of the board meeting, that day included, and a meeting already past leaves 0 days; the other reading starts the clock from some other event, or leaves no day in time after a past meeting, which is what the Boolean gate answers (see Differences below).
- `סעיף 269(א)`: "בלא דיחוי" (without delay) is a plain input about the disclosure, and a delayed disclosure does not count, so the duty stays open to the meeting day and then lapses; the other reading lets a delayed disclosure made before the meeting discharge the duty.
- `סעיף 269(א)`: the day of the meeting at which the transaction is first discussed is a plain input (a date) and not an event the trace can move; the other reading makes the meeting an event.
- `סעיף 283(א)`: the missed disclosure is a terminal BREACH BY the interested person, and a person who is both an office holder and a controlling shareholder is breached once, as an office holder; the other reading is two breaches, or fairness first.
- `סעיפים 271 ו־272`: each approval is a MAY and no clock is encoded, so a missing approval is never a breach; the other reading is a MUST on each body.
- `סעיף 272(א)`: the committee's approval must come before the board's and an earlier board approval does not count; the other reading takes an approval in any order.
- `סעיף 272(ב)`: with no audit committee, the board and the general meeting (for a director) are joined by RAND; the other reading puts the board first, as in 272(א).
- `סעיף 278(ג)`: where the general meeting's approval is added because most directors are interested, the committee (if needed) still comes first and the board and the meeting follow in either order; the other reading puts the meeting before the board.
- `סעיף 270`: "ובלבד שהעסקה היא לטובת החברה" limits what may be approved, so a transaction not for the company's benefit gets no approval route here; the other reading makes it a condition only on the validity of an approval already given.
- `סעיף 280`: no act or consequence is encoded, since the text says a transaction not approved has no force in the cases it names, which is a state and not a step; the other reading adds an act such as "the company performs the transaction", with the lack of force as its consequence.
- `סעיף 278(א)`: each prohibition is a SHANT with a BREACH BY the interested person at the first act of attending or voting, and the text does not say what follows the breach; whether it makes the approval defective under 280(א) is left to that section.
- `סעיף 278(א)`: presence and vote are one DEONTIC and cover the audit committee and the board alike (the text says "בוועדת הביקורת ובדירקטוריון"); the other reading is one DEONTIC for each body.

### What the text leaves silent

- Any time within which any body must approve the transaction: none is encoded, so an approval never given leaves the DEONTIC open without breach.
- The order of the general meeting against the audit committee when all three are needed (278(ג) together with 272(א)).
- What follows a breach of 278(א) for the validity of the approval, and what follows a breach of 269(א) for the transaction itself; section 283(א) gives only the characterisation (a breach of the duty of loyalty or of fairness).
- When "without delay" ends: the text sets no calendar for it, so it is a plain input and not a number of days.
- How long a prohibition of 278(א) lasts: the text names the discussion and the vote and sets no end, so no trace ends FULFILLED while the person is barred.

### Verification

Traces: 43 (13 for the disclosure, 21 for the approvals, 9 for the abstention), each with an `-- EXPECT` written from the text before it was run.
Checked with the unstable binary `l4-unstable-20261125-a50cbd0-darwin-arm64`: both modules type-check with no error and no warning of their own (the two import-resolution warnings about `prelude` and `daydate` come from the local environment, not these files), all seven `#ASSERT`s are satisfied, and `expect_check.py` matched 43 of 43.
Checked again with the stable binary (`~/.cache/l4-main/112/l4`): the same, 43 of 43.
Two scratch mutations were run and deleted, on the 41-trace version that preceded the 272(ד) traces: one shortened the disclosure clock by a day (the day-10 trace and the past-meeting trace then failed), and one made the board and the general meeting sequential instead of RAND (the two general-meeting-first traces then failed).
`srcrefs.py check --refs` reports 22 `src:` lines, 11 locators and 0 problems for the module.

### READS-DIFFERENTLY-ON-MAIN

None: all 43 traces class the same on main as on the unstable binary.
The places the two are known to part are not in these traces: the one clock is a MUST whose LEST is a terminal BREACH, the approval steps are MAYs with no clock and no LEST, no event follows a wait, and the RAND in the abstention DEONTIC joins two SHANTs of which no trace breaches both.

### Differences from the existing DEONTIC

The encoding had no DEONTIC for these provisions, so there is nothing to compare.
Where the layer reads the Boolean gates, one difference and two agreements:

- **Difference, a meeting already past.** The Boolean gate `סעיף 269(א) - הגילוי נעשה במועד` answers FALSE for any disclosure after the meeting day, so when the meeting at which the transaction was first discussed is already past by the time the person comes to know of the interest, no disclosure day is in time under it.
  The DEONTIC gives that case an allowance of 0 days, so disclosure on day 0 is in time and day 1 is a breach (two traces).
  The reason is that "בלא דיחוי" still governs and the second limb ("no later than the meeting") cannot be met; the other reading is the gate's.
  Three `#ASSERT`s record the gate's answers (last day TRUE, next day FALSE, past meeting FALSE).
- Agreement: the gate and the DEONTIC both put the board-meeting day inside the time ("no later than the meeting"), and both treat "without delay" as a plain input.
- Agreement: the gate for 272(ב) gives the general meeting's approval only where the other side is a director (the existing fork F7 reads (ב) as applying to the transactions of (א) in a private company that is not a bond company and has no audit committee), so a non-director office holder needs the board alone, which the traces check.

### What was not encoded, and why

- Section 280 as an act: the text lays down no act and no duty, only that a transaction not approved as the chapter requires has no force in the cases it names; it shows only in how an approvals trace ends (see the fork on 280).
- Sections 272(ג) and (ג1), and 272(ד) for a public company or a private bond company: they need the compensation committee and conditions on the compensation policy (267ב, 267א and the Schedule 1A conditions), and this layer declares no compensation committee and none of those conditions.
  A transaction that reaches the approvals DEONTIC under those limbs ends FULFILLED, which means the layer lays down no step, not that no approval is needed.
  The same holds for sections 273 to 275, which are outside the unit.
- Section 269(ג) (the duty of an "interested party" in a material private offer to disclose, with no outer limit but "without delay") and the damages claim of 283(ב): outside the subsections the unit names; the gates `סעיף 269(ג)` and `סעיף 283(ב)` exist in the Boolean encoding.
- Sections 270(3) to (5), 276, 279, 281 and 282: they concern directors' terms, private offers, shareholders' own disclosure, the audit committee's composition and the effect against another person, which are outside the unit.
- The approval of an ordinary transaction by a method the articles lay down (271): the approvals DEONTIC ends FULFILLED, as the Act leaves the steps to the articles.
- A refusal by any body: the text names no act of refusing, so a refusal is the same as no approval and the trace stays open.
