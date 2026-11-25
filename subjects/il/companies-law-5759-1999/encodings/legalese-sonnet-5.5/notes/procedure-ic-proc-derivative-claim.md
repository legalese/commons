## Procedure layer: the derivative claim (sections 194 to 198)

This layer adds three DEONTICs over the Boolean encoding in `ic2-p5c3-derivative-claim.l4`, in `ic-proc-derivative-claim.l4`, tested in `ic-proc-derivative-claim-tests.l4`.
It adds no definition to an existing module, and calls the existing gates instead of restating them: `סעיף 194(א)`, `סעיף 194(ב)-(ג)`, `סעיף 194(ד)`, `סעיף 195`, `סעיף 196` (the 45 days and the content of the answer), `סעיף 197` (the five limbs and the 75 days), `סעיף 198(א)` and `סעיף 198(ב)`.

### Where each DEONTIC sits, and whose seat it is

All three sit in `ic-proc-derivative-claim.l4`, under the heading for the section they carry.
None is wired into `ic2-seat.l4`, because that would edit an existing module.
The three are chained: the answer calls the 75-day step and the court route, and the 75-day step calls the court route when it lapses.
The consequence of a missed 45-day answer (section 197(4)) is not chained: it is the third DEONTIC run on its own with `החברה לא השיבה` true, because the answer's LEST is a terminal BREACH.

- `סעיף 196 - הדרישה והמענה של החברה`: the plaintiff (a shareholder or director) holds the power to deliver the demand; the company bears the duty to answer within 45 days.
- `סעיף 197(3) - הגשת התביעה בידי החברה בתוך שבעים וחמישה ימים`: the company holds the power to file within 75 days; when it lapses the plaintiff's route opens.
- `סעיפים 197 ו־198 - בקשת התובע לאישור בית המשפט`: the plaintiff holds the power to ask the court; the court bears the duty to approve once convinced (and holds the power to approve an early-filed claim under 198(ב)).

### The DEONTICs and their timelines

1. `סעיף 196 - הדרישה והמענה של החברה` (sections 194 to 196: the plaintiff's written demand, the company's answer, and what follows the way the company took):
   `-- TIMELINE: unit=calendar day; day 0=the day the company received the demand (the day the plaintiff's act of delivering it is stamped); counting="בתוך ארבעים וחמישה ימים מיום קבלת הדרישה"`
2. `סעיף 197(3) - הגשת התביעה בידי החברה בתוך שבעים וחמישה ימים` (section 197(3): the company that told the plaintiff it decided to file):
   `-- TIMELINE: unit=calendar day; day 0=the day of the company's notice to the plaintiff that it decided to file a claim; counting="בתוך שבעים וחמישה ימים מיום ההודעה"`
3. `סעיפים 197 ו־198 - בקשת התובע לאישור בית המשפט` (sections 197 and 198: the plaintiff's request, the court's approval, and the early-filing route of 198(ב)):
   `-- TIMELINE: unit=none stated; day 0=the day the plaintiff's right to ask the court arises; counting="silent"`

### Forks

- `סעיף 194(ב)`: the plaintiff's delivery of a compliant demand is a MAY with no time limit; the other reading is a MUST ("יפנה").
- `סעיף 196`: the day of receipt is day 0 and the forty-fifth day is in time (fork F1 of `NOTES-ic4.md`, borrowed here); the other reading makes the day of receipt day 1.
- `סעיף 196`: an answer that is not a section 195 way (a rejection without reasons) or lacks what section 196 requires does not count, so the 45 days run on; the other reading lets it discharge the duty.
- `סעיף 196`: a missed answer is a terminal BREACH BY the company, and the plaintiff's route is the third DEONTIC on its own; the other reading chains the breach into the route and so hides it.
- `סעיף 197(3)`: the company's filing within 75 days is a MAY whose lapse opens the plaintiff's route; the other reading is a MUST with the route as the consequence of its breach.
- `סעיף 197(3)`: the 75th day is in time and the route opens on the 76th; the other reading opens it on the 75th.
- `סעיף 198(א)`: once the court is convinced of both limbs it MUST approve; the other reading is a MAY.
- `סעיף 198(ב)`: for a claim filed early the court MAY approve on a finding of prescription, and conviction under 198(א) is still needed; the other reading drops the conviction.
- `סעיף 198`: where the court is not convinced the DEONTIC ends FULFILLED, which means no step remains and not that the claim was approved; the other reading makes the refusal an act of the court.

### What the text leaves silent

- Any time within which the plaintiff must make the demand: none is encoded, so a demand never made stays open without breach.
- Any time within which the plaintiff may ask the court, and any time within which the court decides: none is encoded.
- Any consequence of a missed 45-day answer beyond the plaintiff's route under 197(4): the text states none, so the BREACH carries no further step.
- Whether the company is bound to file within 75 days of saying it will: the text states no duty (see the fork above).

### How the traces were verified

There are 68 traces in `ic-proc-derivative-claim-tests.l4`, every EXPECT written from the text before the trace was run.
All 68 match on the unstable binary (`l4-unstable-20261125-a50cbd0`).
Both binaries give zero error diagnostics and no warning of their own on the module and its tests (`l4 check` prints an import-resolution warning about two copies of `daydate` or `prelude` on this machine, which is a machine effect).
The stable binary is the stable build 112: 62 of the 68 match on it and 6 differ.
The match counts come from a small script that reads the `-- EXPECT` line above each `#TRACE`, runs `l4 run` and compares the printed class (FULFILLED, BREACH, or RESIDUAL for anything still open); the script is not in this repository, so a reader without it can read each trace's `Result:` block by hand.
The module's source quotations and `@ref` locators pass `srcrefs.py check --refs --strict` against the Wikisource text.

READS-DIFFERENTLY-ON-MAIN: the six traces below differ, all with one cause: the stable binary ignores a LEST after a MAY, so the 75-day MAY that lapses ends FULFILLED on it, where the unstable binary opens the plaintiff's route (RESIDUAL).

- Decided to file; notice on day 20; filing on day 96 is late (the answer's chain).
- Decided to file; notice on day 20; no filing by day 200 (the answer's chain).
- Decided to file, no filing; the plaintiff asks the court on day 210 (the answer's chain).
- The seventy-sixth day is late (the 75-day step alone).
- No filing by day 200 (the 75-day step alone).
- No filing; the plaintiff asks on day 100 (the 75-day step alone).

Five more traces match on the stable binary for a different reason, so the 62 overstate what main was shown to do: the court approving on day 220 and on day 120, the court not convinced after a lapse (twice), and the 75-day step's gate-fails trace come after the lapse, where main is already FULFILLED and never reaches the court step or its gate.
Nothing shows a difference in the 45-day duty, which is a MUST and counts the same on both.
A mutation check was run on the unstable binary: removing the `PLUS 1` that turns 75 into 76, dropping the section 195 gate from the answer's guard, and dropping the 198(ב) conjunct on section 194(א) each made at least one trace fail (the last was found by a trace added for it).

### What was not encoded

- Section 194(ד) as its own DEONTIC: the exemption from a demand is the existing Boolean gate, used inside the court route (limb 5 of section 197) and passed through the answer.
- The court's power to make its approval conditional on meeting the conditions of the sub-chapter (198(ב), end): the text states no standard, so there is nothing to test.
- Section 198א (the request for disclosure of documents) and sections 199 to 206 (fee, costs, settlement, derivative defence): outside the units named, and already covered by Boolean gates.
- The plaintiff's own opinion in limb (1) is an input, not guessed; so are the court's convictions and its finding of prescription.

### Differences from the existing DEONTIC

There is none to compare: the encoding has no DEONTIC for these sections before this layer.

### Closed routes (not breaches)

The convention for the whole procedure layer is assumed, not ruled: BREACH is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end FULFILLED, with the reason in a comment beside the branch and listed below.
A step the Court is bound by may keep a BREACH BY the court; this unit has none.

- 197(3): the company's seventy-five days to file are a power; when they lapse unused the LEST opens the plaintiff's route (197(4)), and that is no breach.
- 198: the plaintiff's request to the court, and the court's approval or refusal, are powers; none ends in a breach.
- The forty-five days of 196 are a duty on the company by name, so a missed answer stays a BREACH BY the company.

### Changes after the independent review

- The counting rule ("within N days" includes the Nth day) is the fork F1 of `NOTES-ic4.md`, scoped there to the Part 8 sections and borrowed here for sections 196 and 197(3); the module and these notes no longer cite a fork F1 of `NOTES.md`, which has none.
- A new fork: the day the plaintiff delivers the demand is the day the company receives it, because the text counts from receipt (src:1372) and delivery equals receipt only by convention; no answer changed.
- The verification line says "no warning of their own" instead of "zero warnings".
