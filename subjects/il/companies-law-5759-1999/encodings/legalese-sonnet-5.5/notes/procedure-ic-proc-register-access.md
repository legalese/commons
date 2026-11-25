## Procedure layer: documents kept at the registered office, the registers, copies (sections 124 to 129)

This layer adds three DEONTICs over the Boolean encoding in `ic2-p4c1-registered-office.l4` and `ic2-p4c2-registers.l4`, in `ic-proc-register-access.l4`, tested in `ic-proc-register-access-tests.l4`.
It adds one Boolean helper and no change to an existing module.
It calls the existing gates: `סעיף 124`, `סעיף 126(א)`, `סעיף 126` (the payment limit), `סעיף 127`, `סעיף 128` and `סעיף 129`.

### Where each DEONTIC sits, and whose seat it is

All three sit in `ic-proc-register-access.l4`, under the heading for the section they carry.
None is wired into `ic2-seat.l4`, because that would edit an existing module.
The two parties are the company and "the person who asks" (any person for a register, one entitled to inspect for a copy).

- `סעיף 124 - חובת השמירה במשרד הרשום`: the company bears the duty to keep the document.
- `סעיף 129 - עיון במרשם`: any person holds the power to ask to inspect; the company bears the duty to let him.
- `סעיף 126 - מתן העתק`: the person entitled to inspect holds the power to ask for a copy; the company bears the duty to give it for a payment within the limit.

### The DEONTICs and their timelines

1. `סעיף 124 - חובת השמירה במשרד הרשום` (the company keeps the listed document at its registered office):
   `-- TIMELINE: unit=none stated; day 0=the day the duty is entered (the text names no starting event); counting="silent"`
2. `סעיף 129 - עיון במרשם` (any person may ask to inspect the register of shareholders, or in a public company the register of material shareholders, and the company must let him):
   `-- TIMELINE: unit=none stated; day 0=the day the person's right to ask arises (the text names no starting event); counting="silent"`
3. `סעיף 126 - מתן העתק` (one entitled to inspect the section 124 documents may ask for a copy, and the company must give it for a payment within its cost and the Minister's maximum if set):
   `-- TIMELINE: unit=none stated; day 0=the day the person's right to a copy arises (the text names no starting event); counting="silent"`

The new Boolean helper is `הליך העיון - המרשם חובה לנהלו והוא פתוח לעיון`: the register is one the company must keep (section 127, or 128 for a public company's material register) and is open to any person (section 129).
It has six assertions in the test file, three true and three false, covering both registers, a private company, and a body that is not a company of this Law; all are satisfied.

### Forks

- `סעיף 124`: the duty to keep is a MUST with no WITHIN, so waiting never turns it into a breach; the other reading is a standing duty whose breach is the absence of the document at any moment.
- `סעיף 129`: "open to inspection" is a power of any person to ask (a MAY) after which the company must let him inspect; the other reading is a standing prohibition on refusing, with no request step.
- `סעיף 126(א)`: the entitlement to a copy is the company's MUST to give the copy once asked; the other reading is a bare cap on the price.
- `סעיף 126(א)`: a copy given for a payment above the permitted one does not discharge the duty, which stays open; the other reading makes the excessive charge a breach.
- `סעיף 126(א)`: for the two registers listed in section 124(7), whether the person is entitled to inspect stays an input although section 129 gives every person that right, so a caller asking for a copy of a register passes TRUE; the other reading derives the entitlement from section 129 for those two documents.

### What the text leaves silent

The text of sections 124 to 129 states no request procedure (how a person asks to inspect or to be given a copy) and no time limit (for keeping, for opening the register, or for giving a copy).
So no clock is encoded in any of the three DEONTICs, and no trace has an "in time", "last day" or "late" case.
Every step stays open however long the trace waits, and none ever reaches BREACH.
The tests instead cover: done; never done after a long wait (still open); and the gate failing (no step arises).

### How the traces were verified

There are 25 traces and 6 assertions in `ic-proc-register-access-tests.l4`, every EXPECT written from the text before the trace was run.
All 25 traces match on the unstable binary (`l4-unstable-20261125-a50cbd0`) and on the stable binary at `~/.cache/l4-main/112/l4`, and all 6 assertions are satisfied on both.
Both binaries give zero error diagnostics and zero warnings on the module and its tests.
The match counts come from a small script that reads the `-- EXPECT` line above each `#TRACE`, runs `l4 run` and compares the printed class; the script is not in this repository, so a reader without it can read each trace's `Result:` block by hand.
The module's source quotations and `@ref` locators pass `srcrefs.py check --refs --strict` against the Wikisource text.
A mutation check on the unstable binary, making the payment guard always true, made two traces fail.

READS-DIFFERENTLY-ON-MAIN: none.
This module has no MAY with a LEST and no clock, so none of the known differences between the two binaries arises.

### What was not encoded

- Section 125 (keeping the documents by electronic means, provided those entitled to inspect can get copies) is not a DEONTIC: it is a permission whose only condition is the existing Boolean gate, and the company's duty to give a copy under section 126 is the duty that condition protects.
- Section 126(ב) (the Minister's maximum sums) enters only as the optional maximum the existing payment gate takes.
- The registers' contents (sections 130 onward) and the right to inspect other documents (sections 184, 224, 241 and others) are outside the sections named.
- Who is "entitled to inspect" the section 124 documents is an input, because those rights are given in other sections.

### Differences from the existing DEONTIC

There is none to compare: the encoding has no DEONTIC for these sections before this layer.
