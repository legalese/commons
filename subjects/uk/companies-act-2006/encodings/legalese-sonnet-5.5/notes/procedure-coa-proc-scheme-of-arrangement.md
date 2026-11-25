## Procedure layer: schemes of arrangement (Companies Act 2006, Part 26, ss 895 to 901)

Module: `coa-proc-scheme-of-arrangement.l4`, tests: `coa-proc-scheme-of-arrangement-tests.l4`.
Source lines 12205 to 12331 of `ukpga-2006-46.txt`.
The module is a regulative layer over the Boolean encoding in `coa20-part26.l4`, which it imports and does not change.
Where a gate fails, a rule answers `FULFILLED`: nothing is owed.
Where the Act gives no time, no clock is encoded, and an unexercised duty or power stays open (`RESIDUAL`).
The only period the Act fixes in Part 26 is the seven days of s 900(6).

### The twelve rules, their seats and their clocks

1. `s 896(1) the court's power to order a meeting`: seat s 896(1) and (2) (src:12216-12222). The court MAY order the meeting once the Part applies, an application is made and the applicant is one s 896(2) lists. TIMELINE: unit=none; day 0=not applicable; counting=silent.
2. `s 897(1) the company's duty to send the statement with the notice or make it available`: seat s 897(1) (src:12225-12230). The company MUST send each notice with the statement, or, for an advertisement, include the statement or say where and how copies may be had (ROR). TIMELINE: unit=none; day 0=not applicable; counting=silent.
3. `s 897(4) the company's duty to provide a copy of the statement free of charge`: seat s 897(4) (src:12237). The creditor or member MAY apply, and the next step is the company's MUST to provide the copy. TIMELINE: unit=none; day 0=not applicable; counting=silent.
4. `s 897(5) the company and every officer in default`: seat s 897(5) to (7) (src:12238-12245). Two prohibitions side by side (RAND), the company's and the officer's, each closed by the s 897(7) defence when that person shows it. TIMELINE: unit=none; day 0=not applicable; counting=silent.
5. `s 898(1) the duty of a director or trustee to give the company notice`: seat s 898(1) (src:12249-12253). TIMELINE: unit=none; day 0=not applicable; counting=silent.
6. `s 898(2) the director's or trustee's duty not to make default`: seat s 898(2) (src:12254-12255), the offence as the next consequence of the duty above, written as its own rule. TIMELINE: unit=none; day 0=not applicable; counting=silent.
7. `s 899(1) the court's power to sanction the compromise or arrangement`: seat s 899(1) and (2) (src:12257-12263). The court MAY sanction, gated by the existing majority function (a majority in number representing 75% in value of those present and voting), by who may apply, and by s 899A(5) not barring it. TIMELINE: unit=none; day 0=not applicable; counting=silent.
8. `s 899(4) the company's delivery of a copy of the order to the registrar`: seat s 899(4) (src:12269). The company MAY deliver, because the text says only that the order "has no effect until" delivery. TIMELINE: unit=none; day 0=not applicable; counting=silent.
9. `s 900(6) the duty of a company to see that a copy of the order reaches the registrar`: seat s 900(1) and (6) (src:12292-12295, 12310). TIMELINE: unit=calendar day; day 0=the day the order under section 900 is made; counting="within seven days after its making" (the day of the order is day 0 and the seventh day after it, day 7, is the last day).
10. `s 900(7) the company and every officer in default`: seat s 900(7) (src:12311-12313). The company's duty above with its breach laid on the company, beside the same duty with the breach laid on the officer in default (RAND). TIMELINE: unit=calendar day; day 0=the day the order under section 900 is made; counting="within seven days after its making" (the day of the order is day 0 and the seventh day after it, day 7, is the last day; the default is the missed seventh day). The officer's limb is gated by the existing s 900(7) function.
11. `s 901(2) the company's duty to deliver the amended articles with the copy of the order`: seat s 901(1) and (2) (src:12316-12323). TIMELINE: unit=calendar day; day 0=the day the copy of the order is delivered to the registrar; counting="must be accompanied" (the amended documents are due on the day of delivery: `WITHIN 0`).
12. `s 901(3) the company's duty to accompany each copy of the articles with a copy of the order`: seat s 901(3) and (5) (src:12324, 12328-12330), a prohibition on issuing a copy of the articles alone, gated by the existing s 901(3) function asked about a copy issued after the order and not accompanied by it. TIMELINE: unit=none; day 0=not applicable; counting=silent.

### Forks taken

- s 896(1) "may": the court's order is a power (MAY); the other reading is that the court is bound to order the meeting once asked.
- s 897(1)(b) "either (i) or (ii)": the two ways of advertising are alternatives (ROR); the other reading is that the company must do both.
- s 897(1) trigger: that a meeting is summoned is an input, and the existing s 897(1) function is not the gate because it answers whether the duty was met.
- s 897(4) "entitled, on making application": the application is a MAY and the company's copy is the next step; the gate is the existing function asked with the application assumed made.
- s 897(5) "makes default": the offence is a prohibition on the event of default, not a deadline.
- s 897(5)(b) "every officer in default": a second prohibition beside the company's, with a person treated as an officer by s 897(6) counted as an officer.
- s 897(7) "if he shows": each person's defence is its own input and removes only that person's prohibition.
- s 898(1) "such matters relating to himself as may be necessary": whether a matter is necessary is an input.
- s 898(2) "makes default": a prohibition on the event of default, under the same gate as the duty.
- s 899(1) "may": a power of the court; the other reading is that the court must sanction once the majority is shown.
- s 899A(5): a sanction the existing function answers `JUST FALSE` to closes the gate; `NOTHING` (s 899A does not apply) leaves it open.
- s 899(4) the delivery: a MAY of the company (a condition of effect, not a stated duty); the other reading is a MUST with no time.
- s 900(6) "within seven days after its making": the last day is day 7; the other reading counts the day of the order as day 1 and ends on day 6.
- s 900(6) "every company in relation to which an order is made": each such company has its own duty, so the rule is run once per company with its own day 0; the other reading is that one company delivers for all.
- s 900(7)(b): the officer's liability is the same duty with the breach laid on the officer; the other reading is a second prohibition no time limit drives.
- s 901(2) "must be accompanied": due on the day of delivery (`WITHIN 0`); the other reading allows a short time after delivery.
- s 901(3) "must be accompanied": a prohibition on issuing a copy alone; the other reading is a duty to accompany each copy.

### What the text leaves silent

The Act gives no time for the court to order a meeting (s 896), for the statement to be sent (s 897(1)), for a copy to be provided on application (s 897(4)), for a director or trustee to give notice (s 898(1)), for the court to sanction (s 899), or for a copy of the sanctioning order to reach the registrar (s 899(4) says only that the order "has no effect until" delivery).
It names no day on which a "default" is made under s 897(5), s 898(2) or s 901(5).
No clock is encoded for any of these.
The seven days of s 900(6) run only for an order under s 900; they do not run for a sanction under s 899.

### Differences from the existing DEONTIC

The existing rule is `s 900(6) the company's duty to deliver a copy of the order` at `coa20-part26.l4:678-689`; it was read, and not called.

- Gate: the existing rule has no gate and owes the delivery for any order; this module's rule 9 owes it only where s 900 applies (an application under s 899, a scheme of reconstruction or amalgamation, and a transfer under the scheme; src:12293-12295) and an order is made under s 900 (src:12310).
- Party: not a difference in behaviour, since both rules name one company as the party; this module's reading that rule 9 is run once for each company in relation to which the order is made (src:12310 "Every company") is a fork, recorded above.
- Offence: the existing rule stops at the company's breach; this module adds the officer in default as a second breach (src:12311-12313), through rule 10.
- Penalty: neither rule encodes the fine or the daily default fine of s 900(8) (src:12314); it stays Boolean in `coa20-part26.l4`.
- Limit and counting: the same, seven days with day 0 the day of the order (src:12310); the existing file states this in a comment on its Boolean function and this module states it in a TIMELINE line.
- Articles: the existing rule says nothing of s 901(2), the amended articles that go with the copy (src:12320-12323); this module adds it as rule 11.

### Which binary verified the traces

All 47 traces match their `EXPECT` on the unstable build (a50cbd0) and on main (112), and both builds print no error and no warning for either file.
The class (`FULFILLED`, `BREACH`, `RESIDUAL`) is the same on both for every trace.
The officer's limb of rule 10 shares the company's act and deadline, so it never changes a trace's class and `expect_check.py` cannot see it.
Its evidence is the unstable print: it names the officer in the breach of the day-8 trace and leaves the officer out of the trace in which the officer is not in default, and main prints no officer limb at all.
The print differs on main in four traces: unstable prints both breaches of a RAND (the `s 897(5)` trace with the company and the officer both in default, and the `s 900(7)` trace delivered on day 8 with the officer in default) where main prints only the company's, and unstable prints the open prohibition's LEST with its BREACH in parentheses (the `s 897(5)` trace with no default yet and the `s 901(3)` trace with no unaccompanied copy yet) where main does not.
That list is also the `READS-DIFFERENTLY-ON-MAIN` block at the end of the tests file.
The source quotations and locators check clean (`srcrefs.py check --refs` on the module: 56 quotation lines, 12 runs, 12 locators, 0 problems).
The module was altered in place twice as a sensitivity check and restored byte for byte (compared with `cmp`): the seven days changed to six (two traces failed, the day-7 traces of rules 9 and 10), and the s 899A(5) gate dropped (one trace failed, the barred sanction).

### What was not encoded, and why

- s 895(2) and (3), s 896(3) and (4), s 899(1A): definitions and signposts that decide no act; they stay Boolean.
- s 897(2) and (3): what the statement must contain; the trace says whether a statement was sent, and the contents stay a Boolean question.
- s 897(8), s 898(3), s 900(8), s 901(6): penalties, which are consequences and not acts; they stay Boolean.
- s 899(3): that the arrangement binds is an effect, not an act.
- s 899A(1) to (4) and (6): the twelve weeks and the relevant creditors condition when the section applies and who takes part in the meeting; the twelve weeks is a gate inside the Boolean layer and not a duty, so no clock is encoded. Only s 899A(5) is called, as a bar on the sanction.
- s 900(2) to (5): what the court may provide in the order and how property vests; these are powers and effects that change no duty and no time limit.
- s 901(4): an interpretation clause.
- s 901(5)(b): the officer in default of s 901; the module lays the company's offence on the company only, and the officer's follows the pattern of rules 4 and 10.
- s 899(5): the text shows only dots, so there is nothing to encode.
- No new Boolean helper was written, so the tests carry no `#ASSERT`.
