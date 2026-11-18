# NEEDS-CORE (sgd): constructors and types this part wanted in the core

The core's `Party` (`sg-core.l4`, line 26) cannot be extended from another module, so this part declared small types of its own under its `s ...` prefix and uses them.
Each item below says what is wanted, what this part has instead, and where it is used, so that the lead can hoist it and this part can drop its own.

1. **A `Party` constructor `Official Receiver`, with no name.**
   The Official Receiver is an office of the State, like `Registrar` and `Court`, which the core already carries without a name.
   Instead: ``DECLARE `s 210(10B) party` IS ONE OF `s 210(10B) the Official Receiver` `` in `sgd-compromise.l4`.
   Used by the six rules `s 210(10B)(a)`, `s 210(10B)(b)` (`sgd-compromise.l4`), `s 215(7)(a)`, `s 215(7)(b)` (`sgd-acquisition.l4`), `s 215K(2)(a)` and `s 215K(2)(b)` (`sgd-amalgamation.l4`).

2. **A `Party` constructor `Board of directors`, `HAS` the name of the company.**
   Several provisions put a duty on "the board of directors of each amalgamating company" as a body, distinct from "a director" (which is the core's `Director`).
   Instead: ``DECLARE `s 215C party` IS ONE OF `s 215C the board of directors of an amalgamating company` HAS `s 215C the name of the amalgamating company` IS A STRING`` in `sgd-amalgamation.l4`.
   Used by the seven rules `s 215C(2)(a)`, `s 215C(2)(b)`, `s 215C(2)(c)`, `s 215C(4)`, `s 215D(5)`, `s 215I(4)(a)` and `s 215J(3)(a)`.

3. **A record `Penalty` for an offence provision's penalty**, so that every part's penalty functions share one shape.
   Instead: ``DECLARE `s 210(9) penalty` HAS`` four fields, in `sgd-compromise.l4`: the highest fine in Singapore dollars, the longest imprisonment in months, whether the text allows both the fine and the imprisonment, and whether the person is also liable to a default penalty.
   Used by the five functions `the most the person may be sentenced to on conviction` of ss 210(9), 211(5), 212(3), 215I(6) and 215J(5).
   The default-penalty flag is a flag only: its amount is not encoded (PLAN section 4 gives `s 4(1) "default penalty"` to a later wave).
   Sections 215C(6) and 215D(7) state no penalty (finding 6 in `NOTES.md`), so they do not use it.
