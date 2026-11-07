# Restraints of Trade Act 1976 (NSW) -- baseline encoding, the person subject to a restraint of trade

> **Warning.** The text encoded here is taken from the Open Australian Legal Corpus, collected on 10 March 2025 (corpus
> document dated 8 January 2015). It is unofficial and may be out of date: amendments after that version are missing.
> Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05 (`JUST FALSE` where the text says no in its own
words; `NOTHING`, with a `NOTHING-kind` comment, where it does not answer). One regulative rule (the restraint itself,
as far as the Act leaves it valid: a SHANT with the binding days as its WITHIN), run by `EVALTRACE` inside an exported
question that takes only plain facts. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. No pipeline,
no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Act is short (four sections), and the whole
operative Act is encoded.

## Edition

- **Act:** Restraints of Trade Act 1976 No 67, corpus document `nsw_legislation:2015-01-08/act-1976-067` (in force
  8 January 2015), deposited at `../../registers/source-bundle/act-1976-067.txt` (sha256 b52829a2...674620 as
  committed), taken from the Open Australian Legal Corpus (collected 10 March 2025) because legislation.nsw.gov.au
  returned a bot challenge. Not the authorised text.
- **Not deposited:** the Industrial Relations Act 1996 s 304 and the Co-operatives National Law (NSW) s 125 (s 3(3)),
  and the date of assent of the Act (s 3(1)). What they decide is asked as a fact.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read
(and a deliberately wrong assertion, in a scratch copy, was confirmed to be reported as failed).

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `rta-restraints.l4` | 0 | 0 | 0 | 0 |
| `rta-cases.l4` | 0 | 0 | 79 | 79 |

Every expected value was worked by hand from the text, with the edges: the first and last day of a restraint read down
from 12 months to six, the day before it begins and the day after it ends; the court's last day earlier than, equal to
and one day after the written one; an order taking effect on the day it is made, later, and one day earlier (barred); a
breach the day before an order takes effect and on that day (s 4(5)); an order that tries to leave more valid than
s 4(1) allows (capped); each s 3(3) enactment; each failure in s 4(3), with the s 4(4) deeming and outside it.

## Seat

**The person subject to the restraint**: an employee or former employee bound by a non-compete or non-solicitation
clause, a person who sold a business and promised not to compete, or a member of an association whose rules restrain
them. Every exported question is one that person would ask ("Does the Act apply to my restraint?", "How far is it
valid?", "Until what day does it bind me?", "Can I apply to the Supreme Court?", "Can the Court make an order, and what
may it order?", "From what day does the order work?", "Does it wipe out a claim the other side already had against
me?", "Would doing it on this day break my restraint?"). The party who imposed the restraint (the employer, the buyer,
the association) meets the same rules from the other side; a seat for them could be added. The Supreme Court gets no
seat: its power is encoded as what it means for the person bound.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The Act sets no numbers, no time limits and no
  notice steps, and there is no regulation.
- **The actors the text names.** Followed: the person subject to the restraint (the applicant), the person who created
  or joined in creating it, the association, the Supreme Court.
- **Judgments answered conditionally.** Followed: how much of the restraint is against public policy, the last day it
  could run without being against public policy, whether an activity falls within the valid part, whether there was a
  manifest failure to attempt to make it reasonable and whether the problem is partly because of it, and what an order
  says, are all inputs (the court's). The encoding never decides reasonableness.
- **The Act's definitions worked out; borrowed terms asked.** s 2(1), (2) ("association", "public policy", "rules",
  "restraint of trade") are worked into the nouns; "restraint of trade" itself, and invalidity "by reason of any matter
  other than public policy", are the general law's and are asked.
- **One case.** One restraint, as it applies to one person.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:** s 2 (definitions); s 3 (application: restraints created before assent, stipulations to the contrary, other
enactments); s 4(1) (valid to the extent not against public policy, severable or not); s 4(2) (other invalidity
unaffected); s 4(3) (the Supreme Court's order: who may apply, when the power arises, its limit, its effective date);
s 4(4) (associations deemed creators); s 4(5) (rights accrued before the order).

**Out, and why:** s 1 (name): machinery. s 2(3) and the note to s 3 (notes are not part of the Act). The content of
"public policy in respect of restraint of trade" (the common law's reasonableness test) and how a court reads a clause
down: case law, asked as inputs. Industrial Relations Act 1996 s 304, the Co-operatives National Law and the
Commonwealth competition law: separate subjects. The reading down of area or activities is not computed (no measure of
them in the Act); it enters as a yes/no input about the activity asked about.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 3(3) "does not affect the operation of" -- `Does the Act apply to my restraint` -- the Act still applies and
  the other enactment operates beside it -- the other enactment displaces the Act where the two overlap.
- **F2** s 4(2) "does not affect the invalidity ... by reason of any matter other than public policy" -- `Would doing it
  on this day break my restraint` -- a restraint invalid for another reason binds on no day, so `JUST FALSE` -- `NOTHING`,
  since what follows from the other invalidity is the general law's, not the Act's.
- **F3** s 4(4) -- `the failure is by a person who created or joined in creating the restraint`, `Can the Supreme Court
  make an order about my restraint` -- a manifest failure by an association where the restraint is not under its rules on
  a member: s 4(4) does not deem, whether the association in fact created it is not asked, `NOTHING` -- ask it, or
  `JUST FALSE`.
- **F4** s 4(3) "(not being a date earlier than the date on which the order was made)" -- `From what day does the
  Court's order take effect`, `Does the Court's order take away a right already accrued against me`, `Would doing it on
  this day break my restraint` -- an order naming an earlier date: `NOTHING` (the bar is clear, its consequence is not)
  -- the order takes effect from the day it was made.
- **F5** s 4(3) "a person who created or joined in creating the restraint" -- `the failure is by a person who created or
  joined in creating the restraint` -- the input names any creator, the applicant included (an employee who signed the
  contract "joined in creating" it) -- only the party who sought the restraint counts (finding 3).
- **F6** s 4(1) "valid to the extent to which it is not against public policy" -- `Until what day does my restraint bind
  me`, `Would doing it on this day break my restraint` -- read down in time to the earlier of the written last day and
  the court's last day, both days included; area and activity read down through a yes/no input -- the court reads down
  only by striking out words (blue pencil), which s 4(1) "whether it is in severable terms or not" excludes.
- **F7** s 4(3) "may, on such terms as the Court thinks fit" -- `Can the Supreme Court make an order about my
  restraint`, `What may the Court order about my restraint` -- the answer is whether the power arises and its limit, not
  whether the Court will use it -- none (stated so the answer is not read as a promise).
- **F8** s 4(3) with s 4(1) -- `Would doing it on this day break my restraint` -- an order "valid to such extent only"
  that names a later day than s 4(1) allows is capped at the s 4(1) day ("not exceeding the extent to which the
  restraint is not against public policy") -- the order, as made, governs until set aside.

## Jural relations

| Provision | Bearer | Kind | Encoded as |
|---|---|---|---|
| contract or rules (not the Act) | the person subject to the restraint | duty not to do what it forbids, while it binds | SHANT rule, WITHIN the binding days |
| s 4(1), (2) | the person subject to the restraint | immunity from the part against public policy | `How far is my restraint valid`, `Until what day does my restraint bind me` |
| s 4(3) | the person subject to the restraint | power to apply | `Can I apply to the Supreme Court about my restraint` |
| s 4(3), (4) | the Supreme Court | power to order, limited | `Can the Supreme Court make an order about my restraint`, `What may the Court order about my restraint` |
| s 4(5) | the other party | right accrued before the order, preserved | `Does the Court's order take away a right already accrued against me` |

## What the Act turns out to say

1. **The date of assent is not in the text.** s 3(1) excludes restraints "created before the date of assent to this
   Act", but the deposited text does not give that date (the Act is No 67 of 1976). It is asked as a yes/no fact. Any
   restraint a person meets today was created long after it.
2. **No numbers, no time limits.** The Act fixes no period for applying to the Supreme Court, no notice step and no
   amount. A person reading it alone learns how far a restraint stands, not by when to act.
3. **"A person who created or joined in creating the restraint" includes the person bound.** An employee who signed the
   contract joined in creating the restraint. Read literally, the employee's own failure to try to make it reasonable
   would open s 4(3); the purpose suggests only the party who sought the restraint is meant. Fork F5; the encoding does
   not distinguish.
4. **"Public policy" is defined only by itself.** s 2(1) "public policy means public policy in respect of restraint of
   trade": the whole test is handed to the general law. The encoding therefore asks the court's view at every step.
5. **s 4(3) bars a retrospective order but says nothing of one made anyway.** Fork F4; asserted (`NOTHING`).
6. **s 4(5) mostly confirms what s 4(3) already does.** An order cannot take effect before it is made, so rights accrued
   before it are untouched in any case; s 4(5) makes it explicit, and also covers the gap between making an order and a
   later effective date. Asserted: a breach the day before the order takes effect stays a breach.
7. **The s 4(3) order is personal.** It operates "as regards its application to the applicant"; s 4(1) operates for
   everyone. Two people under the same association rule can end up bound to different extents.
8. **A stale note.** The note to s 3 refers to "the Trade Practices Act 1974 of the Commonwealth", renamed the
   Competition and Consumer Act 2010 in 2011, and to the Competition Code of New South Wales. Notes are not part of the
   Act (s 2(3)); the encoding ignores it. s 3(3)(b) is shown as repealed.

## Questions (exported)

`rta-restraints.l4` (9), in the Act's order: `Does the Act apply to my restraint` (ss 2(2), 3), `How far is my
restraint valid` (ss 3(1), 4(1), 4(2)), `Until what day does my restraint bind me` (ss 3(1), 4(1), 4(2)), `Can I apply
to the Supreme Court about my restraint` (ss 3(1), 4(3)), `Can the Supreme Court make an order about my restraint`
(ss 3(1), 4(3), 4(4)), `What may the Court order about my restraint` (s 4(3)), `From what day does the Court's order
take effect` (s 4(3)), `Does the Court's order take away a right already accrued against me` (s 4(5)), `Would doing it
on this day break my restraint` (ss 3(1), 4(1)-(3), 4(5), with the SHANT rule).

## Before relying on it

- Replace the corpus text with the current official text from legislation.nsw.gov.au and re-check every quotation.
- Find the date of assent (finding 1).
- Have a lawyer review the forks, especially F5 (who "joined in creating"), F6 (reading down in time) and F2.
- Link to the Industrial Relations Act 1996 s 304 and the Fair Work and competition law encodings where they exist.
- An independent test pass and the human gates.

Based on content from the New South Wales Legislation website (CC BY 4.0), as collected by the Open Australian Legal
Corpus; see SOURCE-LICENSE.md.
