## Procedure layer: the financial statements of a foreign company (Companies Act 1967 s 373(1), (3), (7) and (9))

Module `sg-proc-foreign-company-accounts.l4`, tests `sg-proc-foreign-company-accounts-tests.l4`, both in this folder.
The module is a regulative layer over the Boolean encoding in `sgg-returns.l4`: it imports it and calls its gate functions, and it restates none of them.
It writes the duties again from the text and does not call the DEONTIC rule that `sgg-returns.l4` already has for s 373(7).
Every DEONTIC has the type `DEONTIC Party `foreign company accounts act``, and the party is the corpus's own `Foreign company`.

### The seat of each DEONTIC, and its TIMELINE line

- `s 373(1) chain: the foreign company must lodge the financial statements, the declaration and the auditor's name within the time in subsection (3)`
  - Seat: s 373(1) (src:24188-24194), s 373(3) (src:24235-24248) and the offence in s 373(18) (src:24463-24473).
  - TIMELINE: unit=calendar day; day 0=the day the annual general meeting is held where the law of the place of incorporation requires the statements to be tabled at one, and otherwise the day the last financial year ended; counting="within 60 days after the date on which its annual general meeting is held" (last day is the meeting day plus 60; an act on that day is in time) or "within such period as the directors ... would have been required to lodge its financial statements if the company were a public company incorporated under this Act which does not keep a branch register outside Singapore" (a last day supplied from outside the section).
- `s 373(7) chain: the foreign company must lodge the documents of subsection (7), or the unaudited ones where it is dormant, within the time in subsection (3)`, with `s 373(7) chain: the three documents of subsection (7)` and `s 373(9) chain: the two unaudited documents of subsection (9)`
  - Seat: s 373(7) (src:24286-24304) and s 373(9) (src:24335-24343).
  - TIMELINE: unit=calendar day; day 0=as above; counting="within the time specified in subsection (3)", the same last day as the financial statements.

### The clocks, and the gates

The helper `s 373 accounts: the days from the day the count starts to the last day for lodging` calls the existing `s 373(3) the last day for lodging the financial statements` and subtracts the day the count starts, so the number of days is computed from DATE inputs and not supplied.
For a company whose law requires the statements to be tabled at an annual general meeting the count is 60 days from the meeting.
For any other the text gives no number of days: the last day is the DATE the caller supplies for "the period a public company incorporated under this Act ... would have had", and day 0 is the day the last financial year ended, which is a choice of origin only.
The module calls two more existing gates: `s 365 this Division applies to the foreign company` (the caller passes its answer; only JUST TRUE makes the duties arise) and `s 373(9) the foreign company may lodge unaudited documents in lieu of subsection (7)` (only JUST TRUE opens the dormant alternative).

### Forks

The `FORK` lines in the module are the register.
In short:
- the statements, the declaration and the statement of the auditor's name are three lodgings, each due by the same last day, and the last is owed only where the statements are audited;
- the audited statement, the audited profit and loss account and the statement of the auditor's name under subsection (7) are three lodgings;
- subsection (9) is an alternative to subsection (7), a choice (ROR) between the two groups, on the same last day;
- the dormant alternative is open only where the existing gate answers JUST TRUE;
- day 0 for a company with no meeting is the end of the last financial year;
- "within 60 days after" is read with the last day as the meeting day plus 60;
- the duties arise only on the caller's JUST TRUE answer from s 365.

### What the text leaves silent

- No time before which the statements may not be lodged, so an early lodging is not a breach.
- No number of days of its own for a company that does not table its statements at a meeting (s 373(3)(b) points to other sections).
- No time for subsection (9) of its own: "in lieu of satisfying the requirements of subsection (7)" is read to carry subsection (7)'s time.
- The extended time after the Registrar acts under s 373(10): the text leaves it to the Registrar.

### Differences from the existing DEONTIC

The existing rule is `s 373(7) the foreign company must lodge ... within the time in subsection (3)` in `sgg-returns.l4` at line 403 (the lines 95, 118 and 190 named in the request are the s 372 rules, and the s 373 rules are at 368 and 403).
It was read once, before the module was written, and not called.

- Clock (src:24286-24289, "within the time specified in subsection (3)"): the existing rule takes the number of days as a plain input; this module computes it from the DATE inputs by calling the existing `s 373(3)` function, so a 60-day limit after a meeting and a supplied date for any other company both come out of the rule's own inputs.
- Acts (src:24291-24304): the existing rule is one act for all three lodgings (the audited statement, the audited profit and loss account and the auditor's name); this module has three acts, so one lodging missing is a breach and one lodged leaves the others open.
- Gates: the existing rule has none; this module is gated on the s 365 answer, and offers the dormant alternative of subsection (9) (src:24335-24343) where the existing gate allows it.
- Party: the existing rule uses the module's own `s 365 the foreign company`; this module uses the core's `Foreign company`.
- The breach reason: this module's text says the company is guilty of an offence under s 373(18) (src:24463-24473); the existing text does not mention it.
- s 373(1) (src:24188-24194), the lodging of the financial statements, the declaration and the auditor's name: no existing DEONTIC; this module adds it.

### What was not encoded, and why

- s 373(2): which statements are meant; a definition, with no step.
- s 373(4) to (6): the Registrar's notice and the company's duty to comply with it; the notice sets its own time, and the existing rule at line 368 covers it.
- s 373(7A) and (8): the true and fair view and the apportionments; standards, not steps with a time.
- s 373(10), (12), (13), (13A) to (17): the Registrar's powers to extend, waive, relieve and the Minister's exemptions; each is a power with no time of its own in the text.
- s 373(18): the offence is carried in the breach reason of each duty; the separate liability of a director or authorised representative who "knowingly and wilfully authorises or permits the default" depends on a state of mind, and the text names no step a trace could show.
- s 373(18A) and (19): outside this unit.

### Which binary verified the traces

The unstable build `l4-unstable-20261125-a50cbd0-darwin-arm64` ran the module and the tests with no error and no warning from these two files, all 3 `#ASSERT` lines satisfied, and all 22 `#TRACE` lines matched their `-- EXPECT` (`expect_check.py`).
The main build (`~/.cache/l4-main/112/l4`) gave the same result: no error and no warning, 3 assertions satisfied, 22 of 22 traces matched.
A sensitivity check on a scratch copy (the origin for a company with no meeting changed to the meeting day, then deleted) made 2 traces mismatch.

### READS-DIFFERENTLY-ON-MAIN

None.
No trace uses a lapsed power, a `LEST` clock on a power, or an event after a wait; every step is a duty with a limit.
