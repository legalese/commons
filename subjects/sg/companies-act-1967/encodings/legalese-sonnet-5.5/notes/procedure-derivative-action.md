## Procedure layer: the statutory derivative action (Companies Act 1967 s 216A and s 216B)

Module `sg-proc-derivative-action.l4`, tests `sg-proc-derivative-action-tests.l4`.
It adds a regulative layer over the Boolean encodings in `sgf-s216a.l4` and `sgf-s216b.l4`, and edits neither.
The parties are the corpus's own `Party` (`sg-core.l4`): the complainant is any `Party`, and the Court is `Court`.
The acts are the new enum `derivative action act`, and `s 216A(5) the order in question` picks one of the three named orders.
Every rule is gated by the existing section function: where the gate does not answer `JUST TRUE`, nothing is owed and the rule is `FULFILLED` at once.
There is no existing DEONTIC for s 216A or s 216B (`sgf-s216a.l4` and `sgf-s216b.l4` are Boolean only), so there is nothing to compare.

### The seat of each DEONTIC

- `s 216A(3)(a) the complainant may give the directors notice of the intention to apply to the Court`: the complainant MAY give the notice; no gate.
- `s 216A(2) the complainant may apply to the Court for permission and the Court decides`: the complainant MAY apply, HENCE the Court decides.
  Gate for the application: `s 216A(2) the complainant may apply to the Court for permission`.
  The decision is chosen by `s 216A(3) the bar on bringing the action or arbitration, or making the intervention, applies`: where the bar does not apply (`JUST FALSE`) the Court MAY grant permission or MAY refuse; where it applies and `s 216A(4) the Court may make an interim order pending the complainant giving notice` holds, the Court MAY make the interim order, HENCE the complainant MAY give the notice the order awaits, or the Court MAY refuse; otherwise the Court MAY only refuse.
  The "or" of the Court's two options is `ROR`.
- `s 216A(5) the Court may make the order in granting permission`: a separate DEONTIC, one MAY of the Court for each of (a), (b) and (c), each gated by its own function (`s 216A(5)(a)`, `(b)` and `(c) the Court may make an order ...`).
- `s 216B(1) the Court must not stay or dismiss by reason only of the members' approval`: the Court SHANT stay or dismiss on that ground, LEST BREACH BY the Court; gate `s 216B(1) the stay or dismissal is barred where the only reason is the members' approval of the alleged breach`.
- `s 216B(2) the Court may approve the stay, discontinuance, settlement or dismissal and order notice to the complainant`: the Court MAY approve, HENCE MAY order a party to give notice to the complainant where it has determined that the complainant's interest may be substantially affected.
  Gates: `s 216B(2) the Court may give its approval upon such terms as it thinks fit` and `s 216B(2) the Court may order a party to give notice to the complainant`.
- `s 216B(3) the Court may at any time order the company to pay the complainant interim costs`: the Court MAY order; gate `s 216B(3) the Court may order the company to pay the complainant interim costs`.

### The TIMELINE lines

- s 216A(3)(a), the notice: unit=calendar day; day 0=the day the complainant gives the directors the notice; counting="14 days' notice", read as notice given not less than 14 days before the application (sg-periods P5: the clear-days reading is the other, fork F-216A-3 in `sgf-s216a.l4`); the 14 days are the earliest day for the application, not a last day for anything, so no clock is encoded for the notice and the next rule tests the day from two DATE inputs.
- s 216A(2) to (4), the application and the decision: unit=calendar day; day 0=the day the complainant gave the directors the notice (where the interim order of subsection (4) is the route, the day the application is made); counting="14 days' notice" as above, so notice on 1 March allows an application from 15 March, which is day 14; the Court's decision and the notice that follows an interim order have no time limit in the text ("silent"); the DATE inputs are the notice day and the application day and must agree with the days of the trace.
- s 216A(5), the orders: unit=calendar day; day 0=the day the Court grants permission; counting=silent (the text puts no time limit on the orders).
- s 216B(1): unit=calendar day; day 0=the day the application is made or the action is brought or intervened in under section 216A; counting=silent (a standing bar with no time limit).
- s 216B(2): unit=calendar day; day 0=the day the Court is asked to approve the stay, discontinuance, settlement or dismissal; counting=silent (the text puts no time limit on the approval or on the notice).
- s 216B(3): unit=calendar day; day 0=the day the application is made or the action is brought or intervened in under section 216A; counting="at any time" (the Court may order the interim costs on any day, so no clock is encoded).

### The forks

- s 216A(3)(a): the notice is a step the complainant MAY take, with no time limit, because the text makes it a condition of the Court's satisfaction and never a duty (the other reading: a MUST with no deadline).
- s 216A(3): the Court's refusal is an act the Court MAY do, open at every outcome of the application (the other reading: the text names no refusal, only "unless the Court is satisfied", so the refusal could be left out and the Court's silence read as refusal).
- s 216A(3): the Court being satisfied is a necessary condition and not a sufficient one, so where it holds the Court may grant or may refuse (the other reading: the Court must grant where it is satisfied).
- s 216A(4): after an interim order the complainant MAY give the notice, with no time limit, because the text says "pending the complainant giving notice as required" and states no duty or time (the other reading: a duty with a deadline set by the Court).
- s 216A(3): where the bar applies and subsection (4) does not, the Court may only refuse (the other reading: the application lapses with nothing further owed).
- s 216A(5): the orders are a separate DEONTIC, because "In granting permission" ties them to the grant and says nothing of an order that comes after it (the other reading: the orders as the next step after the grant).
- s 216B(1): the bearer of "must not be stayed or dismissed" is the Court (the other reading: no bearer, because the text is in the passive and names none).
- s 216B(1): a stay or dismissal by reason only of the members' approval is a BREACH by the Court, although the text states no consequence (the other reading: no breach, the bar only making the order liable to be set aside).
- s 216B(2): the bar on a stay, discontinuance, settlement or dismissal without the Court's approval has no bearer in the text and is not encoded as a duty of anyone; the Court's approval and the notice order are MAY acts of the Court (the other reading: the party who seeks the stay as the bearer of a SHANT until the Court approves).

### What the text leaves silent

- No time limit on the Court at any step, no last day for the complainant to give the notice or to apply, and no time for the notice that an interim order awaits.
- No consequence stated for a stay or dismissal in breach of s 216B(1).
- No bearer for the passive bars in s 216B(1) and (2).
- The list of orders in s 216A(5) is open ("including (but not limited to)"): only (a), (b) and (c) are encoded.

### Which binary verified the traces

Both builds were run from inside the encoding folder with `JL4_LIBRARY_PATH` unset.
The unstable build is `l4-unstable-20261125-a50cbd0-darwin-arm64`, and the stable build is the cache entry 112.
All 37 traces matched their `-- EXPECT` on both (`expect_check.py`).
There are no `#ASSERT`s, because this module defines no new Boolean helper.
Neither file gives an error or a warning on either build.
The expected outcomes were written from the text before the first run.
A copy of the module with the bar test inverted failed seven traces, so the traces can fail.

### READS-DIFFERENTLY-ON-MAIN

None by outcome class: every trace gives the same class on the stable build as on the unstable build.
The only difference is in print: a still-open MAY is laid out on one line by the unstable build and on three lines by the stable build.

### What was not encoded

- s 216A(1), who is a complainant: it is an input here (`the person is a complainant`), because calling `s 216A(1) the person is a complainant` would add six inputs that the procedure does not use.
- s 216A(6), that the application is made in a District Court where the action is in the State Courts: it says where, and neither when nor by whom, so it is not a step.
- s 216B(1), "evidence of approval by the members may be taken into account": a liberty with no step.
- s 216B(3), "the complainant may be accountable for such interim costs upon final disposition": a liability with no stated act or time.
- Any order outside the three in s 216A(5), because the list is open and the text names no others.
