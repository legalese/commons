## Procedure layer: compulsory acquisition of shares after a take-over offer (Companies Act 1967 ss 215 and 215AA)

This note covers `sg-proc-compulsory-acquisition.l4` and its tests `sg-proc-compulsory-acquisition-tests.l4`, written from the text of the Act (source lines 20595-21010 of `CoA1967.txt`) as the procedure the Act lays down.
The module is a regulative layer over the Boolean encoding in `sgd-acquisition.l4`: the gates are that file's section functions, called and not restated, and the parties are `Party` from `sg-core.l4`.
The existing regulative rules in `sgd-acquisition.l4` are not called and not edited.

### The seat of each DEONTIC, its TIMELINE line, and its forks

Where a step is a power with a time limit (MAY ... WITHIN), a missed limit is not a breach, because the text states no consequence except that the power is gone: the LEST is FULFILLED.
Where a step is a duty with no last day in the text, it has no WITHIN and no LEST.
Each month or year period becomes a number of days from DATE inputs through `sg-periods`, because a TRACE has no calendar; each DATE input must agree with the day of the trace on which that event happens.

#### `s 215(4) chain: the transferee must transmit the notice and pay, but only once a notice has been given and the Court has not ordered to the contrary`

Seat: `s 215(4) the transferee's duties after the notice (src:20741-20761)`.

TIMELINE line: unit=calendar day; day 0=the first day on which the transferee must act, which is the day after the end of the later of the one month after the notice and the 14 days after the statement, or the day after the Court disposes of a pending application (the existing function `s 215(4) the first day on which the transferee must act` gives the date); counting="after the expiration of one month after the date on which the notice has been given or, after 14 days after a statement has been supplied ... or if an application to the Court by the dissenting shareholder is then pending, after that application has been disposed of" (the text sets the earliest day and no last day, so no clock is encoded and nothing here can be breached by delay).

- FORK: s 215(4) | (a) the copy of the notice with the instrument of transfer, and (b) the payment, are joined by "and" and not put in an order, so each is a MUST open from day 0, in either order (RAND) | (a) before (b)
- FORK: s 215(4) | the earliest day is not a prohibition: a transmission or payment made before the one month or the 14 days is not a breach, because the text says the transferee "must, after" and states no bar before it; the chain below reaches this rule only after the dissenter's window has ended or the Court has disposed of the application | an early payment as a breach
- FORK: s 215(4) | "or if an application ... is then pending, after that application has been disposed of" is read as the later of the end of the window and the disposal, as the existing function does (F-215-14 in sgd-acquisition.l4) | the disposal alone, even where it comes before the end of the window

#### `s 215(1) chain: the approval within 4 months, the notice within 2 months, the application to the Court, then the payment`

Seat: `s 215(1) the offer approved by 90%, the notice, the application to the Court (src:20595-20618)`.

TIMELINE line: unit=calendar day; day 0=the day the transferee makes the offer; counting="within 4 months after the making of the offer" for the approval (the window opens the day after the offer, sg-periods P2; the last day is the offer day plus 4 months, from the DATE input of the offer day); each later step is chained by HENCE, so its clock restarts on the day the step before it is done: "within 2 months, after the offer has been so approved" runs from the approval day (a DATE input that must equal the trace day on which the approval happens); "within one month from the date on which the notice was given or within 14 days of a statement being supplied ... (whichever is the later)" runs from the notice day and the statement day (two DATE inputs that must equal the trace days); the payment duty is the rule above, reached only through the notice.

- FORK: s 215(1) | the approval by the holders is a MAY of the holders with a limit of 4 months, and a lapse ends the chain with nothing owed (FULFILLED) | the approval as something that happens outside the rule, supplied as a Boolean
- FORK: s 215(1) | a notice outside the 2 months, or a notice to a shareholder who is not dissenting, or a notice not in the prescribed manner, is no notice under subsection (1): the existing gate does not answer JUST TRUE and the chain ends with nothing owed | a late or irregular notice as a breach by the transferee
- FORK: s 215(1) | "supplied" is read as the day the statement is posted (subsection (2)), as the existing function does (F-215-5 in sgd-acquisition.l4) | the day the statement is received
- FORK: s 215(1) | the Court's order is a MAY of the Court with no time limit (the text has none): to order otherwise ends the chain, and to dispose of the application without ordering otherwise sends the transferee to its duties in subsection (4) | the Court's silence as a refusal

#### `s 215(1A) chain: the dissenting shareholder may elect between the alternative terms within the later of the one month and the 14 days`

Seat: `s 215(1A) the election between alternative terms (src:20622-20631)`.

TIMELINE line: unit=calendar day; day 0=the day the transferee gave the notice under subsection (1); counting="not later than the end of one month after the date on which the notice is given under subsection (1), or 14 days after a statement is supplied under subsection (2), whichever is the later" (the same window as the application to the Court, from the notice day and the statement day, two DATE inputs).

- FORK: s 215(1A) | the election is a MAY of the dissenting shareholder, and a missed window is not a breach: the shareholder's election is lost, and the terms stated under (1B) apply | the election as a duty

#### `s 215(1B) chain: the transferee must state which of the alternative terms is to apply on a failure to elect`

Seat: `s 215(1B) the statement of the terms that apply on a failure to elect (src:20635-20639)`.

TIMELINE line: unit=calendar day; day 0=the day the transferee makes the offer; counting=silent ("In offering alternative terms", with no number of days, so no clock is encoded and the duty has no breach path of its own).

- FORK: s 215(1B) | the statement is a duty of the transferee open from the offer, with no limit, because the text puts it "in offering" the terms and names no day | a breach on the day the offer is made without the statement

#### `s 215(2) chain: the dissenting shareholder may demand the statement within one month and the transferor company must supply it`

Seat: `s 215(2) the demand for the statement of names and addresses (src:20688-20698)`.

TIMELINE line: unit=calendar day; day 0=the day the transferee gave notice to the dissenting shareholder under subsection (1); counting="within one month from the date on which the notice was given" for the demand (the last day is the notice day plus one month, from the DATE input of the notice day); the company's duty to supply the statement has no day in the text, so its period is the input `the period of all convenient speed, as found` (Interpretation Act 1965 s 52), counted from the demand, and the 14 days after the posting, until which the transferee is not entitled or bound to acquire, are carried by the application window of the chain above.

- FORK: s 215(2) | the demand is a MAY of the dissenting shareholder and the statement a MUST of the transferor company WITHIN the found period of s 52 from the demand, a BREACH of the company if late (the section module takes the same input, decided by Claude on 2026-11-27, assumed, not ruled); a missed month ends the demand and nothing is owed (FULFILLED) | the company's statement as a duty with no clock, which was this module's first reading

#### `s 215(3) chain: the notice of the 90% within one month, the holder's requirement within 3 months, and the acquisition`

Seat: `s 215(3) the sell-out leg (src:20702-20730)`.

TIMELINE line: unit=calendar day; day 0=the day of the transfer that takes the transferee's holding to 90%; counting="within one month from the date of the transfer" for the transferee's notice (the last day is the transfer day plus one month, from the DATE input of the transfer day); the holder's requirement runs "within 3 months from the giving of the notice to such holder", chained by HENCE from the day the notice is given (a DATE input that must equal the trace day of the notice); the transferee's acquisition has no day in the text (silent).

- FORK: s 215(3)(a) | a notice not given within the month is a BREACH by the transferee and ends the rule, so the holder's 3 months never start in the trace | the late notice as a breach that still lets the 3 months run from the late notice
- FORK: s 215(3)(a) | "(unless on a previous transfer ... it has already complied with this requirement)": where it has, no duty arises on this transfer and the rule is FULFILLED at once; the holder's 3 months then run from the earlier notice, under the rule of that transfer | the duty renewed on every transfer
- FORK: s 215(3)(b) | a holder who has assented is outside "any such holder", so no requirement step is offered to that holder | the step open to every holder
- FORK: s 215(3) | the acquisition is a MUST of the transferee with no clock of its own and no breach path: "entitled and bound to acquire" (src:20722) states the status that follows the holder's notice, and the acts that carry the acquisition out are laid out in s 215(4) (transmit the notice and the instrument, pay the price, and the transferor company registers "thereupon", src:20741-20760), whose rules below have their clocks, so the duty of s 215(3) has no clock of its own; the lead-in of s 215(4) names a notice "under subsection (1)" (src:20741-20742), so that its steps also carry out an acquisition on a holder's requirement is a reading and not a statement of the text (decided by Claude 2026-11-27, assumed, not ruled) | a clock of its own for the acquisition, borrowed from subsection (4) or the found period of s 52

#### `s 215(4) and (5) chain: the transferor company must register the transferee, bank the sums and hold them in trust once it has received them`

Seat: `s 215(4), (5) registration, bank account and trust (src:20760-20769)`.

TIMELINE line: unit=calendar day; day 0=the day the transferor company receives the copy of the notice, the instrument of transfer and the price from the transferee; counting="thereupon" for the registration (the input `the period the standard of time allows, as found`) and silent for subsection (5), where the bank account takes the input `the period of all convenient speed, as found` and the holding in trust, a duty that holds throughout, takes no clock.

- FORK: s 215(4), (5) | registration and the two duties of subsection (5) are three MUSTs of the transferor company open together from the day it receives (RAND) | registration first, then the bank account, then the trust
- FORK: s 215(5) | the duty to pay into a separate bank account is owed only for "sums" (money); where only other consideration was received, only registration and the trust are owed | the bank account for any consideration

#### `s 215(6) and (7) chain: the company may transfer after 2 years and must before 10 years, then the Official Receiver deals with it`

Seat: `s 215(6), (7) the transfer to the Official Receiver and what the Official Receiver does (src:20773-20798)`.

TIMELINE line: unit=calendar day; day 0=the day the money or other consideration was received by the company holding it; counting="after the expiration of 2 years and must before the expiration of 10 years from the date on which the money or other consideration was received": the 2 years end on the day received plus 2 years and the 10 years on the day received plus 10 years (sg-periods P1, P4, from the DATE input of the day received), the second window being chained by HENCE from the end of the first (so its length is the 10 years less the 2 years); the Official Receiver's duties have no day in the text, so their period is the input `the period of all convenient speed, as found`, counted from the transfer.

- FORK: s 215(6) | a transfer on or before the last day of the 2 years is outside the permission and does not count: it is not a breach, because the text lays no bar before it and states no consequence (the fork at s 215(4) reads "must, after" the same way); the company still holds in trust and the 10-year MUST is still owed (decided after the independent review, assumed, not ruled) | a transfer on or before the last day of the 2 years a BREACH by the company, which was this module's first reading
- FORK: s 215(6) | "before the expiration of 10 years" is read as up to and including the last day of the 10 years (the existing function does the same, and so does section 210(10A)) | the day before the last day
- FORK: s 215(6) | "received by the person" is read as received by the company holding it, as the existing function does (finding 3 in NOTES.md) | the day the person became entitled
- FORK: s 215(7) | the Official Receiver's two duties are alternatives chosen by what was received (money, or other consideration), each a MUST WITHIN the found period of s 52 from the transfer, a BREACH of the Official Receiver if late (the section module takes the same input, decided by Claude on 2026-11-27, assumed, not ruled) | both owed on every transfer, or each with no clock, which was this module's first reading

#### `s 215AA(6) chain: the joint transferees must make the notice together`

Seat: `s 215AA(1), (6) the joint notice (src:20949-21004)`.

TIMELINE line: unit=calendar day; day 0=the day the joint transferees give a notice under section 215(1) or (3); counting=silent (the text gives subsection (6) no day of its own; the days of the notices are those of the rules above).

- FORK: s 215AA(6) | the rule is written for two joint transferees, each a MUST joined by RAND, and the duty is gated by the existing test of section 215AA(1) (an offer for all the shares by 2 or more persons jointly); a third needs a third branch | one MUST of "all of the joint transferees" as a single party

The "s 215(1) chain" rule is the chain; the "s 215(4) chain" rule is its last step, written as its own rule so that it carries its own gate and can be run alone.
The chain calls the "s 215(4) chain" rule twice: after the Court disposes of an application without ordering to the contrary, and where no application is made in time.

### What the text leaves silent (no clock encoded, no consequence invented)

- the last day for the transferee to transmit the copy of the notice with the instrument of transfer and to pay (s 215(4)): the text gives only the earliest day, so the last day is the found period of s 52 (`the period of all convenient speed, as found`, an input), counted from the earliest day, with a LEST BREACH BY the transferee (decided by Claude on 2026-11-27, assumed, not ruled; see "Do-once duties and the found period");
- the day by which the transferor company supplies the statement of names and addresses (s 215(2)), registers the transferee (s 215(4)), pays sums into a separate bank account and holds in trust (s 215(5));
- any day for the Court to decide an application (s 215(1)) or to fix terms (s 215(3));
- the day by which the transferee acquires the shares a holder requires it to acquire (s 215(3)), and any payment machinery for that route (subsection (4) is for notices under subsection (1));
- any consequence of an approval after the 4 months, a notice after the 2 months, or a transfer to the Official Receiver before the 2 years have ended (the text states only the power);
- any day for the Official Receiver's duties (s 215(7));
- any day for the statement of the terms that apply on a failure to elect, beyond "In offering alternative terms" (s 215(1B));
- how a month, a year or "within" is counted: the Interpretation Act 1965 is not a source, so the counting is sg-periods conventions P1, P2 and P4 (assumed, not ruled by a lawyer).

### Which binary verified the traces

- Unstable `unstable-20261125-a50cbd0` (the first run, 44 traces) and `unstable-20261126-90eed8e` (the run after the independent review, 56 traces): both files run with no `DiagnosticSeverity_Error` and no warning of their own (the import-resolution warnings about two differing copies of `prelude` and `daydate`, the embedded library against the XDG data directory, are about the machine); all 9 `#ASSERT`s are satisfied; all 56 traces match their `-- EXPECT` lines on `unstable-20261126-90eed8e` (each EXPECT was written from the text before the first run; the three changed after the review were decided from the statute line, and the 12 added traces from the text first).
- Stable the stable build 112: both files run with no error and no warning of their own; 45 of 56 traces match, and the 11 that differ are listed below (7 of them were the first run's 7, shifted by the added traces; 4 are new traces on the same two known behaviours).
- Two altered copies of the module (not left in the folder) show the tests can fail: shortening the 2-year window of subsection (6) to 1 year fails 2 traces, and replacing the payment duty that follows a missed application window by FULFILLED fails 1 trace.
- The 4-month and 2-month windows are also checked by the existing gates the rules call, so a change of either window alone was not tried.
- `srcrefs.py check --refs` reports 0 problems for both files.

### READS-DIFFERENTLY-ON-MAIN

- READS-DIFFERENTLY-ON-MAIN: the traces whose class differs on the stable binary (the stable build 112) from the unstable one (20261126, 90eed8e) that all 56 traces matched on (the line is the #TRACE line; the first run, 44 traces on 20261125, a50cbd0, had 7):
     line 64: Approval on 1 March (day 59), notice on 11 March (day 69), no application by the last day (11 April, day 100): the transferee's duties of subsectio... | unstable and the text: FULFILLED; main: RESIDUAL
     line 264: Notice on day 31, and the holder does not require within the 3 months: the holder's right has lapsed and nothing more is owed. | unstable and the text: FULFILLED; main: RESIDUAL
     line 335: Money received on 1 January 2026 = day 0. A transfer on day 731 (the first day after the 2 years, 730) is permitted; the Official Receiver deals wi... | unstable and the text: FULFILLED; main: RESIDUAL
     line 348: A transfer on the last day of the 10 years (day 3652) is in time. | unstable and the text: FULFILLED; main: RESIDUAL
     line 354: A transfer on day 3653, one day after the 10 years: late. | unstable and the text: BREACH; main: RESIDUAL
     line 359: No transfer by day 3653: the company has not transferred before the expiration of the 10 years. | unstable and the text: BREACH; main: RESIDUAL
     line 364: Other consideration, not money: transferred on day 800; the Official Receiver sells or disposes of it on day 810. | unstable and the text: FULFILLED; main: RESIDUAL
     line 375: An early transfer on day 100 does not count: the company still holds the money in trust and nothing is transferred by day 3653, so the duty to tran... | unstable and the text: BREACH; main: RESIDUAL
     line 381: An early transfer on day 100 does not count, and the company transfers on day 800, after the 2 years: that transfer counts, and the Official Receiv... | unstable and the text: FULFILLED; main: RESIDUAL
     line 388: The company transfers on day 800 and the Official Receiver deals with the moneys on day 830, the last day of the period of 30 days after the transfer. | unstable and the text: FULFILLED; main: RESIDUAL
     line 394: The company transfers on day 800 and the Official Receiver deals with the moneys on day 831, one day after the period of all convenient speed: late. | unstable and the text: BREACH; main: RESIDUAL
  Why, by what each trace does (the stable binary's reading is the known one, and the encoding is not changed to suit it):
     a MAY that runs out (lines 64 and 264: the dissenting shareholder's application, the holder's 3 months): on main the trace ends in the HENCE step of that MAY (the Court's order; the transferee's acquisition), where unstable takes the LEST (nothing owed; the transferee's duties of subsection (4) follow).
     the transfer to the Official Receiver (lines 335 to 394: the wait of the first 2 years is a MAY that runs out, then the company's MUST to transfer, with the Official Receiver's MUST after it): on main the trace ends with the company's MUST to transfer still open, with no BREACH and the transfer event not taken as done.
     Observed end states only: this file does not say why main reads these differently, and the module is not changed to suit it.

### What was not encoded, and why

- Sections 215(1C) to (1E), (3A), (8) to (8C) and (9) to (12), and section 215AA(1) to (3): these say which shares count, who is a dissenting shareholder and when the conditions of the rights are met; they are not steps with a day, and they stay in the Boolean layer that the gates call.
- The terms on which the shares are acquired (subsections (1), (1A), (1B) and (3)) and the Court's power to fix other terms on the application of either side (src:20729-20730): the Boolean layer answers which terms apply, and the text puts no day on the Court.
- Section 215AA(4) (joint rights and joint and several obligations) and (5) (a notice to any one of the joint transferees is enough, subject to (6)): neither is a step with a day; the rule for the joint notice is written for two joint transferees.
- The prescribed manner of a notice: an input (a Boolean), because the manner is prescribed outside the Act.
- What section 197 of the Insolvency, Restructuring and Dissolution Act 2018 requires of the Official Receiver: it is not a source, so the Official Receiver's two duties are the steps the text names.
- The 14 days after the posting of the statement, until which the transferee is not entitled or bound to acquire (s 215(2)): carried by the application window of the chain, which ends on the later of the month and the 14 days; a payment made earlier is not a breach (fork at s 215(4)).
- The sell-out leg of subsection (3) is not chained into the chain of subsection (1): it starts from a transfer that brings the transferee to 90%, not from the approval of the offer, so it is a rule of its own with its own day 0.
- Section 215AB (the impossibility of communicating or accepting an offer) is outside this unit.

### Differences from the existing DEONTIC

The existing regulative rules are in `sgd-acquisition.l4` lines 1250-1425.
Each of them stands alone (none is chained to another), has no gate, and takes a caller-supplied number of days where it has a deadline.
The section module `sgd-acquisition.l4` carries a found period (`WITHIN` at `:1280`, `:1327`, `:1333`, `:1346`, `:1363`, `:1412`, `:1422`) for the duties of s 215(2), (4)(a), (4)(b), (4), (5) bank account, (7)(a) and (7)(b), and `-- no LEST:` comments at `:1263` (s 215(1B)), `:1374` (s 215(5) trust) and `:1438` (s 215AA(6)); `l4 run` on `unstable-20261126-90eed8e` reports no `lint/lest-without-deadline` in it or in the new files.
None of the rules below has to change for the new module to work; the warnings are the existing module's own.

- s 215(1B) (sgd-acquisition.l4:1258-1263): The existing rule makes any party MUST state the terms, with no gate; the new rule is owed only where alternative terms were offered (src:20635 "In offering alternative terms"). Both have no clock; the existing rule's LEST is a `-- no LEST:` comment at line 1263 (class OTHER), and the new rule has no LEST.
- s 215(2) (sgd-acquisition.l4:1275-1280): The existing rule makes the company MUST supply the statement, with no gate, no demand and no limit on the demand; the new rule is gated on the notice having been given (src:20688 "Where a transferee has given notice"), makes the dissenting shareholder's demand a MAY within one month of the notice (src:20690-20693), and owes the statement only after a demand. On the existing rule a statement is owed whether or not anyone demanded one; on the new rule a missed month ends the demand and nothing is owed.
- s 215(3)(a) (sgd-acquisition.l4:1293-1299): The existing rule is MUST WITHIN a number of days the caller supplies, with no 90% gate and no "unless ... it has already complied" gate (src:20702-20707, 20709-20712), and nothing after it; the new rule is gated on both, computes the month from the transfer day, and goes on to the holder's MAY within 3 months of the notice (src:20717-20719) and the transferee's MUST to acquire (src:20721-20723). Both give BREACH for a notice after the month.
- s 215(4) (sgd-acquisition.l4:1320-1330): The existing rule makes any party MUST transmit and MUST pay with no gate and no earliest day (the gate "a notice has been given ... and the Court has not ... ordered to the contrary", src:20741-20743, sits in a Boolean function the rule does not call); the new rule calls that function as its gate and is reached only through the chain, after the dissenting shareholder's window has ended or the Court has disposed of the application. The two LESTs of the existing rule (lines 1325, 1330) can never be reached; the new rule has none.
- s 215(4) registration (sgd-acquisition.l4:1336-1341): The existing rule owes registration unconditionally; the new rule owes it once the company has received the copy, the instrument and the price (src:20760 "thereupon"), together with the duties of subsection (5). Line 1341 LEST can never be reached.
- s 215(5) bank account and trust (sgd-acquisition.l4:1351-1365): The existing rules are unconditional; the new rule owes both only once the company has received, and owes the bank account only where money was received (src:20765 "sums"), the trust for sums and other consideration (src:20766-20768). Lines 1356 and 1365 LEST can never be reached.
- s 215(6) (sgd-acquisition.l4:1377-1383): The existing rule is MUST WITHIN a caller-supplied number of days to the last day of the 10 years, with no trust gate (src:20773-20774) and no limb for the 2 years, so an early transfer is simply in time; the new rule is gated on the money or consideration being held in trust, opens with a wait of 2 years (a MAY whose act nobody takes, so a transfer made inside it matches no step and does not count; the company still holds in trust and the 10-year MUST is still owed), then makes the transfer a MUST for the rest of the 10 years, with a BREACH when it is late (src:20773-20776).
- s 215(7)(a) and (b) (sgd-acquisition.l4:1398-1411): The existing rules are two unchained MUSTs of the Official Receiver with no gate; the new rule chains the one that fits what was received after the transfer under subsection (6) (src:20781-20782, 20788-20798). Lines 1403 and 1411 LEST can never be reached; the new rule has none.
- s 215AA(6) (sgd-acquisition.l4:1420-1425): The existing rule is one MUST of a single party with no gate; the new rule is gated on the joint-offer test of section 215AA(1) and makes each of two joint transferees a MUST, joined by RAND (src:21001-21003 "must be made by all of the joint transferees"). Line 1425 LEST can never be reached.
- Steps with no existing rule: the approval within 4 months after the offer (src:20598-20601), the notice within 2 months after the approval (src:20605-20608), the dissenting shareholder's application within the later of one month from the notice and 14 days from the statement, and the Court's order or disposal (src:20609-20613), the election between alternative terms (src:20622-20631), and the dissenting shareholder's demand (src:20690-20693).

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST or branch.
This unit has one change, after the independent review (SG-compulsory-acquisition-1): the transfer of the money or other consideration to the Official Receiver inside the first 2 years.
The text gives only a power "after the expiration of 2 years" (src:20775) and lays no bar before it, so the early transfer is not a breach and does not count: the company still holds the money in trust, and the duty to transfer before the expiration of 10 years (src:20776) is still owed.
The trace "a transfer on day 730" moved from BREACH to RESIDUAL (`-- EXPECT changed after independent review`), and two traces were added to show the 10-year duty still owed after an early transfer (BREACH when nothing follows, FULFILLED when a transfer after the 2 years does).
The BREACHes that stay are laid on a named party: the transferee's notice within a month (s 215(3)(a), "must within one month", src:20709), the transfer before the expiration of 10 years (s 215(6)), and the found-period duties below.
The lapses of the approval, the application, the election, the demand and the holder's 3 months end `FULFILLED`, as before.

### Do-once duties and the found period

Decided by Claude on 2026-11-27 after the independent review (SG-ALL-1), assumed, not ruled: the layer is aligned with the section module `sgd-acquisition.l4`, which carries a found period for a duty to do a thing once (`notes/lest-without-deadline.md`).

| duty | class | input | section module's twin |
| ---- | ----- | ----- | --------------------- |
| s 215(2) the transferor company supplies the statement, counted from the demand | ACHIEVEMENT, s 52 | `the period of all convenient speed, as found` | `sgd-acquisition.l4:1279-1280` |
| s 215(4)(a) the transferee transmits the copy of the notice and the instrument of transfer | ACHIEVEMENT, s 52 | the same input | `sgd-acquisition.l4:1326-1327` |
| s 215(4)(b) the transferee pays, allots or transfers the price | ACHIEVEMENT, s 52 | the same input | `sgd-acquisition.l4:1332-1333` |
| s 215(4) the transferor company registers the transferee "thereupon" | ACHIEVEMENT, text's own standard | `the period the standard of time allows, as found` | `sgd-acquisition.l4:1345-1346` |
| s 215(5) the transferor company pays the sums into a separate bank account | ACHIEVEMENT, s 52 | `the period of all convenient speed, as found` | `sgd-acquisition.l4:1362-1363` |
| s 215(7)(a) the Official Receiver deals with the moneys | ACHIEVEMENT, s 52 | `the period of all convenient speed, as found` | `sgd-acquisition.l4:1411-1412` |
| s 215(7)(b) the Official Receiver sells or disposes of the other consideration | ACHIEVEMENT, s 52 | the same input | `sgd-acquisition.l4:1421-1422` |

In the traces the period is 30 days, and 10 days for "thereupon".
The input is a rule-level `GIVEN` of each chain rule and is passed down to the s 215(4) rule as a plain argument from the s 215(1) chain (the tests' `case:` wrapper passes it); the rule of s 215(4) and (5) takes both inputs.
The nested clock of each step counts from the day the step before it is done (the demand, the transfer, the receipt), which is the trigger the text names.
Traces added: s 215(4) transmission and payment on day 30 FULFILLED, payment on day 31 BREACH; s 215(2) supply on day 40 FULFILLED, day 41 BREACH; registration on day 10 FULFILLED, day 11 BREACH; the bank account on day 31 BREACH; the Official Receiver on day 830 FULFILLED, day 831 BREACH.
Two EXPECTs changed for this reason, both from RESIDUAL to BREACH: the s 215(4) chain with nothing done by day 400, and the s 215(4) and (5) chain with nothing done by day 30.

### Limits of the wait device

The wait act `s 215(6) the 2 years from the receipt run out before the company may transfer` is a device: the text names no act there, only the lapse of the 2 years, and the module carries it as a step nobody takes (a `MAY` whose `HENCE` and `LEST` both call the helper rule), so that the helper starts when the 2 years have run out.
The wait act is a device; a trace must not name it; if it is named, the helper starts on that day.
Measured on unstable-20261126-90eed8e with the act named on day 100 (money received on day 0): a transfer on day 200 and the Official Receiver's dealing on day 210 read `FULFILLED`, so a transfer inside the first 2 years counts; a transfer on day 3100 reads `BREACH` and a transfer on day 3022 reads `FULFILLED`, so the 10-year deadline has moved to day 100 plus the 10 years less the 2 years, which is day 3022, and not day 3652.
No trace in the tests names the act; the same device, and the same limit, are in `sg-proc-derivative-action.l4` for the 14 days' notice of s 216A(3)(a).

### Duties left without a clock

- s 215(1B), the statement of which alternative terms apply: tied to the offer ("In offering alternative terms", src:20635), class OTHER in `notes/lest-without-deadline.md` and a `-- no LEST:` comment at `sgd-acquisition.l4:1263`; the module's fork says the same, so the two layers agree.
- s 215(3), the transferee's acquisition: "entitled and bound to acquire" (src:20722) states the status that follows the holder's notice, and the acts that carry the acquisition out are the s 215(4) steps (transmit the notice and the instrument, pay the price, the transferor company registers "thereupon", src:20741-20760), which have their clocks in this module; so the duty of s 215(3) has no clock of its own (decided by Claude 2026-11-27, assumed, not ruled).
  The lead-in of s 215(4) names a notice "under subsection (1)" (src:20741-20742), so that its steps also carry out an acquisition on a holder's requirement under s 215(3) is a reading and not a statement of the text.
  The section module has no rule for the acquisition, so there is no twin to disagree with, and the module's fork keeps it a `MUST` with no limit.
- s 215(5), holding the sums in trust: a duty that holds throughout (class MAINTENANCE, `sgd-acquisition.l4:1374`).
- s 215AA(6), the joint notice: a requirement on the document's content, class OTHER (`sgd-acquisition.l4:1438`); it is met when the notice is made.
- s 215(3)(a), the notice of the 90%: already has its clock, one month, and a BREACH.

### The late notice under s 215(3)(a) (SG-compulsory-acquisition-2)

A notice under s 215(3)(a) given late ends the rule in BREACH, so the holder's 3 months "from the giving of the notice to such holder" (src:20717-20718) never start in the rule, although the text would still start them on a late notice.
This is a limit of a terminal BREACH, and the module's fork says so (decided by Claude, assumed, not ruled; the other reading encodes a late notice that still lets the 3 months run).
A trace was added to show the position: the notice on day 40 and the holder's requirement on day 60 read BREACH, the rule having ended on day 32 with nothing about the holder.

