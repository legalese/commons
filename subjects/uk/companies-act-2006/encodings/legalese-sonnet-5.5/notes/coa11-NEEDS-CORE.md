# NEEDS-CORE (coa11)

The core (`coa-core.l4`) lacks the following; this part declared a small type of its own under its own prefix and records here what the lead could hoist at the merge.

1. **A constructor for the audit committee in `Party`.**
   Wanted: `Audit committee` (and, if the lead wants it, `Scottish Ministers` and `Competent authority` is already there).
   Sections: s 485A(3) (the audit committee must make a recommendation to the directors before an appointment) and s 489A(3), the same for a public company; s 494ZA(2) to (4) name "the competent authority" (the core has `Competent authority`), and s 483 names "the Scottish Ministers" (not a regulative rule here: it is a power, encoded as a decision function).
   Declared locally instead: `s 485A party` (`s 485A the audit committee`, `s 485A the directors`), `s 489A party`, `s 485B party`, `s 489B party`, each with its own action type (`s 485A act` and so on), because the core's `Party` has `Director` but no audit committee.
2. **Used from the core where it fitted:** `Party` (`Company`, for the four "give notice to the Secretary of State" duties of ss 486(2), 486A(4), 490(2), 490A(4)), `Penalty` and `Fine limit` (the offence penalties of ss 486(4), 486A(6), 490(4), 490A(6): `a fine not exceeding a level on the standard scale` with level 3 and fraction 1 or 0.1), `Mode of conviction` (`on summary conviction`), `Form of document` (s 488(3)(a)).
3. **A type for "a list of financial years of a company"** is declared locally (`s 494ZA financial year`: first day, last day, whether the auditor was appointed for it following a qualifying selection procedure); another part that needs the company's financial years (Part 15, coa8 and coa9) may want the same record in the core.
