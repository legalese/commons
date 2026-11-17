# NOTES.md -- ccc17: the Criminal Code of Canada (R.S.C., 1985, c. C-46), sections 487.05 to 490.019

Part agent `ccc17` of the 32-part parallel encoding of the Criminal Code (Canada) into L4.
My range is lines 9544-10274 of `inputs/R.S.C.-1985-c.-C-46.txt`: sections 487.05 to 490.019 (43 section headings), inside Part XV.
It holds the DNA warrants, orders and samples (ss 487.05 to 487.0911), other warrants and their execution (ss 487.092 to 488), journalists' warrants and the sealing of documents (ss 488.01 and 488.02), solicitor-client privilege in a seizure (s 488.1), seizure and detention of things (ss 489 to 490.01) and the first sections of the sex offender information registration orders (ss 490.011 to 490.019).

## Status, and how each claim below was checked

- Every claim in this file was checked on 2026-11-16 against the files in this folder, not against my notes: the counts are printed by `check.sh`, `srcrefs.py` and the scripts named in each section.
- Binary: `l4` 1.6.110 (main, e51181d), sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`; second build for the "reads differently on main" check: 1.6.109 (main, 4c887e0), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`. `JL4_LIBRARY_PATH` was unset throughout.
- `check.sh` (target `main`): 19 modules, 0 errors, 1,257 assertions satisfied, 0 failed, 0 refused, the same four counts on both builds (the full output is at the end of this file).
- `srcrefs.py check --refs` and `--strict` over all 16 `ccc17-*` files: 665 `-- src:` lines, 208 runs, 255 locators, 0 problems, in both modes.
- The two `#TRACE` runs of each tests file that has them (`ccc17-tests-dna-orders.l4`, `ccc17-tests-sor.l4`) were compared across the two builds with `JL4_LIBRARY_PATH` unset on both sides: both printed their evaluations, the whole output of each file is identical on the two builds, and the two traces read the same in both files (FULFILLED when the date is set on day 90, a BREACH BY `the court` on day 91).
- `work/lint.py` (not shipped): every `JUST FALSE` carries a `FALSE-kind` quote that is a verbatim slice of lines 9544-10274, every `NOTHING` carries one of the six `NOTHING-kind` reasons, every function name begins with its section label and is named in a test; it also checks the five `CONSIDER` wrappers of the seat file that answer `JUST FALSE` and the seven that answer `NOTHING`.

## About this text, and what is not claimed

- The text is a plain-text rendering made by a converter script from the Justice Laws Website consolidation, under the Open Government Licence - Canada (`inputs/STUB-SOURCE-LICENSE.md`).
- It is not the official text. **Nothing in this encoding is verified against the official text.**
- The French version is equally authoritative and is not among the sources; the French equivalents printed after a defined term are not encoded.
- Every quoted word in a `-- src:` line was copied by a script from that file (`work/build.py`), never typed.

## Where this file departs from PLAN.md

Where `inputs/PLAN.md` and the brief differ, the brief governs. The differences I acted on:

1. PLAN.md section 1 says a part receives only `ccc-core.l4`. This sandbox also holds `ccc-definitions.l4` and `ccc-interpretation.l4`, and the brief says layer 1 IMPORTs `ccc-core.l4` and `ccc-definitions.l4`. `ccc17-warrants.l4` imports both and calls `s 2 day` and `s 2 night` for section 488; the other modules import the core only.
2. Every other answer from section 2 (`peace officer`, `public officer`) and every answer from another part is an input named `s <label> <what is asked>`, `MAYBE BOOLEAN`, as PLAN.md section 4 says (see "Seams" below). The merged seat layer can replace each input by a call.
3. PLAN.md says periods keep the text's units and use the core's `Length of time`. The periods of this range are written in days (10, 14, 90 and 180 days, and the clear days of notice) and in years (one, five, ten, twenty). Days are added with `PLUS`; years are added with the standard library's `add years` (assumed, not ruled: the core's `Length of time` has no function that adds it to a date, so I did not use it here; fork F5 records how a year is counted).
4. The Hohfeld table is generated from `-- jural:` comments above each rule, one row per provision that creates a relation.

## The seat

The seat is the brief's: **a person who is, or may be, accused of an offence under the Criminal Code (the accused), asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction.**
(Assumed, not ruled: Singapore's Penal Code is the model, as the maintainer instructed on 2026-11-09, but this is a plain seat layer; no charge-generator contract.)
Provisions that address only an official (for example the Attorney General's review in s 487.0911, the sheriff's custody in s 488.1(2)(b)) are encoded in layer 1 for what they decide, and appear in layer 2 only where they mean something to the person; there is no seat for an official.

## Files

- Layer 1: `ccc17-dna-orders.l4` (ss 487.05 to 487.0552), `ccc17-dna-samples.l4` (ss 487.056 to 487.0911), `ccc17-warrants.l4` (ss 487.092 to 488), `ccc17-journalists.l4` (ss 488.01 to 488.02), `ccc17-privilege.l4` (s 488.1), `ccc17-seizure.l4` (ss 489 to 490.01), `ccc17-sor.l4` (ss 490.011 to 490.019).
- Tests, one per module: `ccc17-tests-dna-orders.l4` (174 assertions), `-dna-samples` (146), `-warrants` (138), `-journalists` (84), `-privilege` (73), `-seizure` (129), `-sor` (366): 1,110 in all.
- Layer 2: `ccc17-seat.l4` (52 questions) and `ccc17-cases-seat.l4` (147 assertions).
- `NOTES.md` (this file) and `PROGRESS.md`. There is no `NEEDS-CORE.md`: no type or constructor of the core was lacking; every constructor I needed is declared under its section label in my own modules.
- The keel's `ccc-core.l4`, `ccc-definitions.l4`, `ccc-interpretation.l4`, `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are untouched.

## Coverage (ccc17)

Lines 9544-10274 of the text (`R.S.C.-1985-c.-C-46.txt`). Built by `work/units.py` (the units, from the text) and `work/coverage.py` (the dispositions, from the `-- covers:` comments in the layer-1 modules); neither is shipped.
Every unit has exactly one disposition: `encoded` (a rule, definition or table in layer 1 with a test, citing the provision with `@ref`), `fork` (encoded under a reading chosen in the fork register), `inert` (reason 1, 2 or 3 of the brief), or `repealed or blank in this text`. There is no `out-of-scope` and no `deferred` row.
The names are given as the index entries `N1`... of the table at the end of this section (the full L4 name of each rule). A row's marginal note (its heading) is inside its line range; an unnumbered closing paragraph of a subsection has its own row (`... closing words`).

### Audit counts

- text units counted by the script: **524** rows in 43 sections (every subsection, paragraph, subparagraph, defined term, closing paragraph, group heading and one-subsection section of the range); the 726 non-blank lines of the range are each in exactly one row (726 of 726 checked). A section's marginal note is inside the line range of its first row; the section table below sums the rows of each section.
- rows in the table before: 524 (each starts as a `deferred` placeholder, as the skill's step 3 has it); after: 524, none `deferred` and none `UNCOVERED` (0).
- dispositions of the 524 rows: encoded 405, fork 107, inert 4, repealed or blank in this text 8.

### Sections

| section | lines | encoded | fork | inert | repealed |
| --- | --- | --- | --- | --- | --- |
| 487.05 | 9544-9563 | 3 | 7 | 0 | 1 |
| 487.051 | 9564-9574 | 0 | 7 | 0 | 0 |
| 487.052 | 9575-9575 | 0 | 0 | 0 | 1 |
| 487.053 | 9576-9582 | 3 | 2 | 0 | 0 |
| 487.054 | 9583-9584 | 1 | 0 | 0 | 0 |
| 487.055 | 9585-9627 | 25 | 8 | 0 | 2 |
| 487.0551 | 9628-9631 | 1 | 1 | 0 | 0 |
| 487.0552 | 9632-9637 | 3 | 1 | 0 | 0 |
| 487.056 | 9638-9655 | 11 | 1 | 0 | 0 |
| 487.057 | 9656-9665 | 7 | 0 | 0 | 0 |
| 487.058 | 9666-9667 | 1 | 0 | 0 | 0 |
| 487.06 | 9668-9676 | 6 | 0 | 0 | 0 |
| 487.07 | 9677-9701 | 17 | 0 | 0 | 1 |
| 487.071 | 9702-9711 | 7 | 0 | 0 | 0 |
| 487.08 | 9712-9726 | 9 | 0 | 0 | 1 |
| 487.09 | 9727-9739 | 1 | 6 | 0 | 0 |
| 487.091 | 9740-9747 | 2 | 3 | 0 | 0 |
| 487.0911 | 9748-9757 | 6 | 0 | 0 | 0 |
| 487.092 | 9758-9766 | 1 | 4 | 0 | 1 |
| 487.093 | 9769-9777 | 5 | 0 | 0 | 0 |
| 487.1 | 9778-9833 | 44 | 1 | 0 | 0 |
| 487.11 | 9834-9835 | 0 | 1 | 0 | 0 |
| 487.2 | 9836-9840 | 4 | 0 | 0 | 0 |
| 487.3 | 9841-9857 | 4 | 4 | 0 | 0 |
| 488 | 9858-9862 | 4 | 0 | 0 | 0 |
| 488.01 | 9863-9895 | 17 | 6 | 0 | 0 |
| 488.02 | 9896-9913 | 9 | 2 | 0 | 0 |
| 488.1 | 9914-9954 | 17 | 9 | 0 | 0 |
| 489 | 9955-9964 | 8 | 0 | 0 | 0 |
| 489.1 | 9965-9978 | 8 | 0 | 0 | 0 |
| 490 | 9979-10048 | 29 | 21 | 0 | 0 |
| 490.01 | 10049-10054 | 0 | 3 | 0 | 0 |
| 490.011 | 10058-10152 | 92 | 0 | 0 | 0 |
| 490.012 | 10155-10178 | 12 | 7 | 0 | 0 |
| 490.013 | 10179-10198 | 9 | 4 | 0 | 1 |
| 490.0131 | 10199-10202 | 3 | 0 | 0 | 0 |
| 490.0132 | 10203-10208 | 3 | 2 | 0 | 0 |
| 490.014 | 10209-10212 | 3 | 0 | 0 | 0 |
| 490.015 | 10213-10231 | 4 | 7 | 0 | 0 |
| 490.016 | 10232-10248 | 13 | 0 | 0 | 0 |
| 490.017 | 10249-10252 | 2 | 0 | 0 | 0 |
| 490.018 | 10253-10270 | 10 | 0 | 0 | 0 |
| 490.019 | 10273-10274 | 1 | 0 | 0 | 0 |

### Rows

| unit | lines | text | disposition | L4 name (index) or note | fork |
| --- | --- | --- | --- | --- | --- |
| 487.05(1) | 9544-9545 | 487.05 (1) A provincial court judge who on ex parte applic | fork | N1 | F1 |
| 487.05(1)(a) | 9546-9546 | (a) that a designated offence has been committed, | fork | N1 | F1 |
| 487.05(1)(b) | 9547-9551 | (b) that a bodily substance has been found or obtained | fork | N1 | F1 |
| 487.05(1)(c) | 9552-9552 | (c) that a person was a party to the offence, and | fork | N1 | F1 |
| 487.05(1)(d) | 9553-9553 | (d) that forensic DNA analysis of a bodily substance from  | fork | N1 | F1 |
| 487.05(1) closing words | 9554-9554 | and who is satisfied that it is in the best interests of t | fork | N1 | F1 |
| 487.05(2) | 9555-9556 | (2) In considering whether to issue the warrant, the provi | encoded | N2 |  |
| 487.05(2)(a) | 9557-9557 | (a) the nature of the designated offence and the circumsta | encoded | N2 |  |
| 487.05(2)(b) | 9558-9560 | (b) whether there is | encoded | N2 |  |
| 487.05(3) | 9561-9561 | (3) [Repealed, 2022, c. 17, s. 20] | repealed or blank in this text | the text shows: (3) [Repealed, 2022, c. 17, s. 20] |  |
| 487.05(4) | 9562-9563 | (4) A warrant issued under subsection (1) may be executed  | fork | N3 | F14 |
| 487.051(1) | 9564-9565 | 487.051 (1) The court shall make an order in Form 5.03 aut | fork | N4 | F2 |
| 487.051(2) | 9566-9567 | (2) The court shall make such an order in Form 5.03 in rel | fork | N5 | F2 |
| 487.051(3) | 9568-9569 | (3) The court may, on application by the prosecutor and if | fork | N6 | F1 |
| 487.051(3)(a) | 9570-9570 | (a) a person who is found not criminally responsible on ac | fork | N6 | F1 |
| 487.051(3)(b) | 9571-9571 | (b) a person who is convicted, discharged under section 73 | fork | N6 | F1 |
| 487.051(3) closing words | 9572-9572 | In deciding whether to make the order, the court shall con | fork | N6, N7 | F1 |
| 487.051(4) | 9573-9574 | (4) When the court makes an order authorizing the taking o | fork | N9 | G1 |
| 487.052 | 9575-9575 | 487.052 [Repealed, 2007, c. 22, s. 3] | repealed or blank in this text | the text shows: 487.052 [Repealed, 2007, c. 22, s. 3] |  |
| 487.053(1) | 9576-9577 | 487.053 (1) The court may make an order under section 487. | fork | N10 | G1 |
| 487.053(2) | 9578-9579 | (2) If the court does not consider the matter at that time | encoded | N11 |  |
| 487.053(2)(a) | 9580-9580 | (a) shall, within 90 days after the day on which it impose | encoded | N11 |  |
| 487.053(2)(b) | 9581-9581 | (b) retains jurisdiction over the matter; and | encoded | N12 |  |
| 487.053(2)(c) | 9582-9582 | (c) may require the person to appear by closed-circuit tel | fork | N13 | F1, G1 |
| 487.054 | 9583-9584 | 487.054 The offender or the prosecutor may appeal from a d | encoded | N17 |  |
| 487.055(1) | 9585-9586 | 487.055 (1) A provincial court judge may, on ex parte appl | fork | N23 | F1 |
| 487.055(1)(a) | 9587-9587 | (a) had been declared a dangerous offender under Part XXIV | fork | N23 | F1 |
| 487.055(1)(b) | 9588-9588 | (b) had been declared a dangerous offender or a dangerous  | fork | N23 | F1 |
| 487.055(1)(c) | 9589-9589 | (c) had been convicted of murder; | fork | N23 | F1 |
| 487.055(1)(c.1) | 9590-9590 | (c.1) had been convicted of attempted murder or conspiracy | fork | N23 | F1 |
| 487.055(1)(d) | 9591-9591 | (d) had been convicted of a sexual offence within the mean | fork | N23 | F1 |
| 487.055(1)(e) | 9592-9592 | (e) had been convicted of manslaughter and, on the date of | fork | N23 | F1 |
| 487.055(2) | 9593-9594 | (2) The application shall be accompanied by a certificate  | encoded | N24 |  |
| 487.055(3) | 9595-9596 | (3) For the purposes of subsection (1), sexual offence mea | encoded | N21 |  |
| 487.055(3)(a) | 9597-9597 | (a) an offence under any of the following provisions, name | encoded | N18 |  |
| 487.055(3)(a)(i) | 9598-9598 | (i) section 151 (sexual interference), | encoded | N18 |  |
| 487.055(3)(a)(ii) | 9599-9599 | (ii) section 152 (invitation to sexual touching or exposur | encoded | N18 |  |
| 487.055(3)(a)(iii) | 9600-9600 | (iii) section 153 (sexual exploitation), | encoded | N18 |  |
| 487.055(3)(a)(iv) | 9601-9601 | (iv) section 155 (incest), | encoded | N18 |  |
| 487.055(3)(a)(v) | 9602-9602 | (v) subsection 212(4) (offence in relation to juvenile pro | encoded | N18 |  |
| 487.055(3)(a)(vi) | 9603-9603 | (vi) section 271 (sexual assault), | encoded | N18 |  |
| 487.055(3)(a)(vii) | 9604-9604 | (vii) section 272 (sexual assault with a weapon, threats t | encoded | N18 |  |
| 487.055(3)(a)(viii) | 9605-9605 | (viii) section 273 (aggravated sexual assault); | encoded | N18 |  |
| 487.055(3)(a.1) | 9606-9606 | (a.1) an offence under subsection 348(1) if the indictable | encoded | N21 |  |
| 487.055(3)(b) | 9607-9607 | (b) an offence under any of the following provisions of th | encoded | N19 |  |
| 487.055(3)(b)(i) | 9608-9608 | (i) section 144 (rape), | encoded | N19 |  |
| 487.055(3)(b)(ii) | 9609-9609 | (ii) section 146 (sexual intercourse with female under fou | encoded | N19 |  |
| 487.055(3)(b)(iii) | 9610-9610 | (iii) section 148 (sexual intercourse with feeble-minded,  | encoded | N19 |  |
| 487.055(3)(b)(iv) | 9611-9611 | (iv) section 149 (indecent assault on female), | encoded | N19 |  |
| 487.055(3)(b)(v) | 9612-9612 | (v) section 156 (indecent assault on male), or | encoded | N19 |  |
| 487.055(3)(b)(vi) | 9613-9613 | (vi) section 157 (acts of gross indecency); | encoded | N19 |  |
| 487.055(3)(c) | 9614-9614 | (c) an offence under paragraph 153(1)(a) (sexual intercour | encoded | N20 |  |
| 487.055(3)(d) | 9615-9615 | (d) an attempt to commit an offence referred to in any of  | encoded | N21 |  |
| 487.055(3.01) | 9616-9617 | (3.01) The court may require a person who is given notice  | fork | N26 | F1, G1 |
| 487.055(3.1) | 9618-9619 | (3.1) In deciding whether to grant an authorization under  | encoded | N27 |  |
| 487.055(3.11) | 9620-9621 | (3.11) If the court authorizes the taking of samples of bo | encoded | N29 |  |
| 487.055(4) | 9622-9623 | (4) However, if a person who is on conditional release has | encoded | N30 |  |
| 487.055(5) | 9624-9625 | (5) The summons shall be accompanied by a copy of the auth | encoded | N31 |  |
| 487.055(6) | 9626-9626 | (6) [Repealed, 2008, c. 18, s. 13] | repealed or blank in this text | the text shows: (6) [Repealed, 2008, c. 18, s. 13] |  |
| 487.055(7) | 9627-9627 | (7) to (10) [Repealed, 2007, c. 22, s. 11] | repealed or blank in this text | the text shows: (7) to (10) [Repealed, 2007, c. 22, s. 11] |  |
| 487.0551(1) | 9628-9629 | 487.0551 (1) If a person fails to appear at the place, day | fork | N32 | F1 |
| 487.0551(2) | 9630-9631 | (2) The warrant may be executed anywhere in Canada by a pe | encoded | N33 |  |
| 487.0552(1) | 9632-9633 | 487.0552 (1) Every person who, without reasonable excuse,  | encoded | N35 |  |
| 487.0552(1)(a) | 9634-9634 | (a) an indictable offence and liable to imprisonment for a | encoded | N35 |  |
| 487.0552(1)(b) | 9635-9635 | (b) an offence punishable on summary conviction. | encoded | N35 |  |
| 487.0552(2) | 9636-9637 | (2) For greater certainty, a lawful command that prevents  | fork | N37 | F3 |
| 487.056(1) | 9638-9639 | 487.056 (1) Samples of bodily substances shall be taken as | encoded | N38 |  |
| 487.056(1)(a) | 9640-9640 | (a) at the place, day and time set out in an order made un | encoded | N38 |  |
| 487.056(1)(b) | 9641-9641 | (b) in any other case, on the day on which the order autho | encoded | N38 |  |
| 487.056(2) | 9642-9643 | (2) Samples of bodily substances shall be taken as authori | encoded | N39 |  |
| 487.056(2)(a) | 9644-9644 | (a) at the place, day and time set out in an order made un | encoded | N39 |  |
| 487.056(2)(b) | 9645-9645 | (b) in any other case, as soon as feasible after the autho | encoded | N39 |  |
| 487.056(3) | 9646-9647 | (3) If a person fails to appear as required by an order ma | encoded | N40 |  |
| 487.056(3)(a) | 9648-9648 | (a) when the person is arrested under a warrant issued und | encoded | N40 |  |
| 487.056(3)(b) | 9649-9649 | (b) as soon as feasible after the person appears at the pl | encoded | N40 |  |
| 487.056(4) | 9650-9651 | (4) Subsections (1) to (3) apply even if the order or auth | encoded | N41 |  |
| 487.056(5) | 9652-9653 | (5) A peace officer who is authorized under section 487.05 | encoded | N42 |  |
| 487.056(6) | 9654-9655 | (6) The samples shall be taken by a peace officer who has  | fork | N43 | F4 |
| 487.057(1) | 9656-9657 | 487.057 (1) A peace officer who takes samples of bodily su | encoded | N44 |  |
| 487.057(1)(a) | 9658-9658 | (a) the provincial court judge who issued the warrant unde | encoded | N44 |  |
| 487.057(1)(b) | 9659-9659 | (b) the court that made the order under section 487.051. | encoded | N44 |  |
| 487.057(2) | 9660-9661 | (2) The report shall include | encoded | N46 |  |
| 487.057(2)(a) | 9662-9662 | (a) a statement of the time and date the samples were take | encoded | N46 |  |
| 487.057(2)(b) | 9663-9663 | (b) a description of the bodily substances that were taken | encoded | N46 |  |
| 487.057(3) | 9664-9665 | (3) A peace officer who takes the samples or causes the sa | encoded | N47 |  |
| 487.058 | 9666-9667 | 487.058 No peace officer, and no person acting under a pea | encoded | N48 |  |
| 487.06(1) | 9668-9669 | 487.06 (1) A peace officer or a person acting under a peac | encoded | N49 |  |
| 487.06(1)(a) | 9670-9670 | (a) the plucking of individual hairs from the person, incl | encoded | N49 |  |
| 487.06(1)(b) | 9671-9671 | (b) the taking of buccal swabs by swabbing the lips, tongu | encoded | N49 |  |
| 487.06(1)(c) | 9672-9672 | (c) the taking of blood by pricking the skin surface with  | encoded | N49 |  |
| 487.06(2) | 9673-9674 | (2) The warrant, order or authorization shall include any  | encoded | N50 |  |
| 487.06(3) | 9675-9676 | (3) A peace officer who is authorized to take samples of b | encoded | N51 |  |
| 487.07(1) | 9677-9678 | 487.07 (1) Before taking samples of bodily substances from | encoded | N52 |  |
| 487.07(1)(a) | 9679-9679 | (a) the contents of the warrant, order or authorization; | encoded | N52 |  |
| 487.07(1)(b) | 9680-9680 | (b) the nature of the investigative procedures by means of | encoded | N52 |  |
| 487.07(1)(c) | 9681-9681 | (c) the purpose of taking the samples; | encoded | N52 |  |
| 487.07(1)(d) | 9682-9682 | (d) the authority of the peace officer and any other perso | encoded | N52 |  |
| 487.07(1)(d.1) | 9683-9683 | (d.1) [Repealed, 2000, c. 10, s. 20] | repealed or blank in this text | the text shows: (d.1) [Repealed, 2000, c. 10, s. 20] |  |
| 487.07(1)(e) | 9684-9686 | (e) in the case of samples of bodily substances taken in e | encoded | N52 |  |
| 487.07(2) | 9687-9688 | (2) A person from whom samples of bodily substances are to | encoded | N53 |  |
| 487.07(2)(a) | 9689-9689 | (a) be detained for that purpose for a period that is reas | encoded | N53 |  |
| 487.07(2)(b) | 9690-9690 | (b) be required to accompany a peace officer for that purp | encoded | N54 |  |
| 487.07(3) | 9691-9692 | (3) A peace officer who takes samples of bodily substances | encoded | N55 |  |
| 487.07(4) | 9693-9694 | (4) A young person against whom a warrant is executed has, | encoded | N56 |  |
| 487.07(4)(a) | 9695-9695 | (a) the right to a reasonable opportunity to consult with, | encoded | N56 |  |
| 487.07(4)(b) | 9696-9696 | (b) the right to have the warrant executed in the presence | encoded | N56 |  |
| 487.07(4) closing words | 9697-9697 | counsel and a parent or, in the absence of a parent, an ad | encoded | N56 |  |
| 487.07(5) | 9698-9699 | (5) A young person may waive his or her rights under subse | encoded | N58 |  |
| 487.07(5)(a) | 9700-9700 | (a) must be recorded on audio tape or video tape or otherw | encoded | N58 |  |
| 487.07(5)(b) | 9701-9701 | (b) must be made in writing and contain a statement signed | encoded | N58 |  |
| 487.071(1) | 9702-9703 | 487.071 (1) Before taking samples of bodily substances fro | encoded | N59 |  |
| 487.071(2) | 9704-9705 | (2) If the person’s DNA profile is in the convicted offend | encoded | N60 |  |
| 487.071(2)(a) | 9706-9706 | (a) confirm in writing on the order or authorization that  | encoded | N60 |  |
| 487.071(2)(b) | 9707-9707 | (b) transmit a copy of the order or authorization containi | encoded | N60 |  |
| 487.071(3) | 9708-9709 | (3) If the person’s DNA profile is not in the convicted of | encoded | N62 |  |
| 487.071(3)(a) | 9710-9710 | (a) any bodily substances taken; and | encoded | N62 |  |
| 487.071(3)(b) | 9711-9711 | (b) a copy of the order or authorization and any other inf | encoded | N62 |  |
| 487.08(1) | 9712-9713 | 487.08 (1) No person shall use bodily substances that are  | encoded | N63 |  |
| 487.08(1.1) | 9714-9715 | (1.1) No person shall use bodily substances that are taken | encoded | N64 |  |
| 487.08(2) | 9716-9717 | (2) No person shall use the results of forensic DNA analys | encoded | N65 |  |
| 487.08(2)(a) | 9718-9718 | (a) in the course of an investigation of the designated of | encoded | N65 |  |
| 487.08(2)(b) | 9719-9719 | (b) in any proceeding for such an offence. | encoded | N65 |  |
| 487.08(2.1) | 9720-9720 | (2.1) [Repealed, 2005, c. 25, s. 9] | repealed or blank in this text | the text shows: (2.1) [Repealed, 2005, c. 25, s. 9] |  |
| 487.08(3) | 9721-9722 | (3) Every person who contravenes subsection (1) or (2) is  | encoded | N66 |  |
| 487.08(4) | 9723-9724 | (4) Every person who contravenes subsection (1.1) | encoded | N68 |  |
| 487.08(4)(a) | 9725-9725 | (a) is guilty of an indictable offence and liable to impri | encoded | N68 |  |
| 487.08(4)(b) | 9726-9726 | (b) is guilty of an offence punishable on summary convicti | encoded | N68 |  |
| 487.09(1) | 9727-9728 | 487.09 (1) Subject to subsection (2), bodily substances th | fork | N70 | F5 |
| 487.09(1)(a) | 9729-9729 | (a) the results of that analysis establish that the bodily | fork | N70 | F5 |
| 487.09(1)(b) | 9730-9730 | (b) the person is finally acquitted of the designated offe | fork | N70 | F5 |
| 487.09(1)(c) | 9731-9734 | (c) the expiration of one year after | fork | N70 | F5 |
| 487.09(1) closing words | 9735-9735 | unless during that year a new information is laid or an in | fork | N70 | F5 |
| 487.09(2) | 9736-9737 | (2) A provincial court judge may order that the bodily sub | fork | N73 | F1 |
| 487.09(3) | 9738-9739 | (3) Bodily substances that are provided voluntarily by a p | encoded | N74 |  |
| 487.091(1) | 9740-9741 | 487.091 (1) A provincial court judge may, on ex parte appl | fork | N75 | F1 |
| 487.091(1)(a) | 9742-9742 | (a) a DNA profile cannot be derived from the bodily substa | fork | N75 | F1 |
| 487.091(1)(b) | 9743-9743 | (b) the information or bodily substances required by regul | fork | N75 | F1 |
| 487.091(2) | 9744-9745 | (2) The application shall state the reasons why a DNA prof | encoded | N76 |  |
| 487.091(3) | 9746-9747 | (3) If the court authorizes the taking of samples of bodil | encoded | N77 |  |
| 487.0911(1) | 9748-9749 | 487.0911 (1) On receipt of a notice from the Commissioner  | encoded | N79 |  |
| 487.0911(2) | 9750-9751 | (2) If the Attorney General is of the opinion that the def | encoded | N80 |  |
| 487.0911(2)(a) | 9752-9752 | (a) apply, ex parte, to the judge who made the order or au | encoded | N80 |  |
| 487.0911(2)(b) | 9753-9753 | (b) transmit a copy of the corrected order or authorizatio | encoded | N80 |  |
| 487.0911(3) | 9754-9755 | (3) If the Attorney General is of the opinion that the off | encoded | N82 |  |
| 487.0911(4) | 9756-9757 | (4) If the Attorney General is of the opinion that the off | encoded | N83 |  |
| 487.092(1) | 9758-9759 | 487.092 (1) A justice may issue a warrant in writing autho | fork | N234 | F1 |
| 487.092(1)(a) | 9760-9760 | (a) by information on oath in writing that there are reaso | fork | N234 | F1 |
| 487.092(1)(b) | 9761-9761 | (b) that it is in the best interests of the administration | fork | N234 | F1 |
| 487.092(2) | 9762-9763 | (2) A warrant issued under subsection (1) shall contain su | encoded | N235 |  |
| 487.092(3) | 9764-9765 | (3) A warrant issued under subsection (1) may be executed  | fork | N236 | F14 |
| 487.092(4) | 9766-9766 | (4) [Repealed, 2022, c. 17, s. 21] | repealed or blank in this text | the text shows: (4) [Repealed, 2022, c. 17, s. 21] |  |
| group heading: Other Provisions Respecting Warrants and Orders | 9768-9768 | Other Provisions Respecting Warrants and Orders | inert | reason 1 (a heading of a group of sections) |  |
| 487.093(1) | 9769-9770 | 487.093 (1) A person who executes a warrant issued under s | encoded | N237, N238 |  |
| 487.093(1)(a) | 9771-9773 | (a) give the following to any person who is present and os | encoded | N238 |  |
| 487.093(1)(b) | 9774-9774 | (b) affix the copy and the notice in a prominent location  | encoded | N238 |  |
| 487.093(1)(c) | 9775-9775 | (c) give the copy and the notice to the person to be searc | encoded | N238 |  |
| 487.093(2) | 9776-9777 | (2) Subsection (1) does not apply if the warrant authorize | encoded | N238 |  |
| 487.1(1) | 9778-9779 | 487.1 (1) Despite anything in this Act, the Attorney Gener | fork | N242 | F1 |
| 487.1(1)(a) | 9780-9780 | (a) a warrant under subsection 83.222(1); | encoded | N240 |  |
| 487.1(1)(b) | 9781-9781 | (b) an order under subsection 83.223(1); | encoded | N240 |  |
| 487.1(1)(b.1) | 9782-9782 | (b.1) a warrant under subsection 110.1(5); | encoded | N240 |  |
| 487.1(1)(b.2) | 9783-9783 | (b.2) a warrant under subsection 117.0101(6); | encoded | N240 |  |
| 487.1(1)(c) | 9784-9784 | (c) a warrant under subsection 117.04(1); | encoded | N240 |  |
| 487.1(1)(d) | 9785-9785 | (d) a warrant under subsection 164(1); | encoded | N240 |  |
| 487.1(1)(e) | 9786-9786 | (e) an order under subsection 164.1(1); | encoded | N240 |  |
| 487.1(1)(f) | 9787-9787 | (f) a warrant under subsection 320(1); | encoded | N240 |  |
| 487.1(1)(g) | 9788-9788 | (g) an order under subsection 320.1(1); | encoded | N240 |  |
| 487.1(1)(h) | 9789-9789 | (h) a warrant under subsection 320.29(1); | encoded | N240 |  |
| 487.1(1)(i) | 9790-9790 | (i) a warrant under subsection 395(1); | encoded | N240 |  |
| 487.1(1)(j) | 9791-9791 | (j) a warrant under subsection 462.32(1); | encoded | N240 |  |
| 487.1(1)(j.1) | 9792-9792 | (j.1) a warrant under subsection 462.321(1); | encoded | N240 |  |
| 487.1(1)(k) | 9793-9793 | (k) an order under subsection 462.33(3); | encoded | N240 |  |
| 487.1(1)(l) | 9794-9794 | (l) a warrant under subsection 487(1); | encoded | N240 |  |
| 487.1(1)(m) | 9795-9795 | (m) a warrant under subsection 487.01(1) that does not aut | encoded | N240 |  |
| 487.1(1)(n) | 9796-9796 | (n) an extension under subsection 487.01(5.2); | encoded | N240 |  |
| 487.1(1)(o) | 9797-9797 | (o) an order under any of sections 487.013 to 487.018; | encoded | N241 |  |
| 487.1(1)(p) | 9798-9798 | (p) an order under subsection 487.019(3); | encoded | N240 |  |
| 487.1(1)(q) | 9799-9799 | (q) an order under subsection 487.0191(1); | encoded | N240 |  |
| 487.1(1)(r) | 9800-9800 | (r) an order under subsection 487.0191(4); | encoded | N240 |  |
| 487.1(1)(s) | 9801-9801 | (s) a warrant under subsection 487.05(1); | encoded | N240 |  |
| 487.1(1)(t) | 9802-9802 | (t) a warrant under subsection 487.092(1); | encoded | N240 |  |
| 487.1(1)(u) | 9803-9803 | (u) an order under subsection 487.3(1); | encoded | N240 |  |
| 487.1(1)(v) | 9804-9804 | (v) an order under subsection 487.3(4); | encoded | N240 |  |
| 487.1(1)(w) | 9805-9805 | (w) a warrant under subsection 492.1(1); | encoded | N240 |  |
| 487.1(1)(x) | 9806-9806 | (x) a warrant under subsection 492.1(2); | encoded | N240 |  |
| 487.1(1)(y) | 9807-9807 | (y) an authorization under subsection 492.1(7); | encoded | N240 |  |
| 487.1(1)(z) | 9808-9808 | (z) a warrant under subsection 492.2(1). | encoded | N240 |  |
| 487.1(2) | 9809-9810 | (2) A person who must swear an oath in connection with an  | encoded | N243 |  |
| 487.1(3) | 9811-9812 | (3) A judicial officer who receives an application submitt | encoded | N244 |  |
| 487.1(4) | 9813-9814 | (4) An application under subsection 487.01(5.2) shall not  | encoded | N245 |  |
| 487.1(5) | 9815-9816 | (5) An applicant may submit their application by a means o | encoded | N246 |  |
| 487.1(6) | 9817-9818 | (6) An application submitted by a means of telecommunicati | encoded | N247 |  |
| 487.1(7) | 9819-9820 | (7) Any oath required in connection with an application su | encoded | N248 |  |
| 487.1(8) | 9821-9822 | (8) A judicial officer who receives an application submitt | encoded | N249 |  |
| 487.1(9) | 9823-9824 | (9) If an application is submitted by a means of telecommu | encoded | N250 |  |
| 487.1(10) | 9825-9826 | (10) A judicial officer who issues the warrant, order, ext | encoded | N251 |  |
| 487.1(10)(a) | 9827-9827 | (a) the judicial officer shall complete and sign the docum | encoded | N251 |  |
| 487.1(10)(b) | 9828-9828 | (b) if the means of telecommunication produces a writing,  | encoded | N251 |  |
| 487.1(10)(c) | 9829-9829 | (c) if the means of telecommunication does not produce a w | encoded | N251 |  |
| 487.1(11) | 9830-9831 | (11) The following definitions apply in this section. | encoded | N252 |  |
| 487.1(11) "judicial officer" | 9832-9832 | judicial officer means a judge or justice who is authorize | encoded | N252 |  |
| 487.1(11) "public officer" | 9833-9833 | public officer means a public officer who is appointed or  | encoded | N253 |  |
| 487.11 | 9834-9835 | 487.11 A peace officer, or a public officer who has been a | fork | N254 | F1 |
| 487.2 | 9836-9837 | 487.2 If a search warrant is issued under section 487 or a | encoded | N255 |  |
| 487.2(a) | 9838-9838 | (a) the location of the place searched or to be searched,  | encoded | N255 |  |
| 487.2(b) | 9839-9839 | (b) the identity of any person who is or appears to occupy | encoded | N255 |  |
| 487.2 closing words | 9840-9840 | without the consent of every person referred to in paragra | encoded | N255 |  |
| 487.3(1) | 9841-9842 | 487.3 (1) On application made at the time an application i | fork | N257 | F1 |
| 487.3(1)(a) | 9843-9843 | (a) the ends of justice would be subverted by the disclosu | fork | N257 | F1 |
| 487.3(1)(b) | 9844-9844 | (b) the reason referred to in paragraph (a) outweighs in i | fork | N257 | F1 |
| 487.3(2) | 9845-9846 | (2) For the purposes of paragraph (1)(a), an order may be  | encoded | N258 |  |
| 487.3(2)(a) | 9847-9852 | (a) if disclosure of the information would | encoded | N258 |  |
| 487.3(2)(b) | 9853-9853 | (b) for any other sufficient reason. | encoded | N258 |  |
| 487.3(3) | 9854-9855 | (3) Where an order is made under subsection (1), all docum | encoded | N259 |  |
| 487.3(4) | 9856-9857 | (4) An application to terminate the order or vary any of i | fork | N260 | F6 |
| 488 | 9858-9859 | 488 A warrant issued under section 487 shall be executed b | encoded | N261 |  |
| 488(a) | 9860-9860 | (a) the justice is satisfied that there are reasonable gro | encoded | N261 |  |
| 488(b) | 9861-9861 | (b) the reasonable grounds are included in the information | encoded | N261 |  |
| 488(c) | 9862-9862 | (c) the warrant authorizes that it be executed by night. | encoded | N261 |  |
| 488.01(1) | 9863-9864 | 488.01 (1) The following definitions apply in this section | encoded | N89 |  |
| 488.01(1) "data" | 9865-9865 | data has the same meaning as in section 487.011. (données) | encoded | N84 |  |
| 488.01(1) "document" | 9866-9866 | document has the same meaning as in section 487.011. (docu | encoded | N85 |  |
| 488.01(1) "journalist" | 9867-9867 | journalist has the same meaning as in subsection 39.1(1) o | encoded | N86 |  |
| 488.01(1) "journalistic source" | 9868-9868 | journalistic source has the same meaning as in subsection  | encoded | N87 |  |
| 488.01(1) "officer" | 9869-9869 | officer means a peace officer or public officer. (fonction | encoded | N88 |  |
| 488.01(2) | 9870-9871 | (2) Despite any other provision of this Act, if an applica | encoded | N90 |  |
| 488.01(3) | 9872-9873 | (3) A judge may issue a warrant, authorization or order un | encoded | N93 |  |
| 488.01(3)(a) | 9874-9874 | (a) there is no other way by which the information can rea | encoded | N93 |  |
| 488.01(3)(b) | 9875-9875 | (b) the public interest in the investigation and prosecuti | encoded | N93 |  |
| 488.01(4) | 9876-9877 | (4) The judge to whom the application for the warrant, aut | encoded | N94 |  |
| 488.01(5) | 9878-9879 | (5) Subsections (3) and (4) do not apply in respect of an  | encoded | N95 |  |
| 488.01(6) | 9880-9881 | (6) If a warrant, authorization or order referred to in su | fork | N96 | F1 |
| 488.01(7) | 9882-9883 | (7) The warrant, authorization or order referred to in sub | encoded | N97 |  |
| 488.01(8) | 9884-9885 | (8) The judge who rules on the application for the warrant | encoded | N98 |  |
| 488.01(9) | 9886-9887 | (9) If an officer, acting under a warrant, authorization o | encoded | N99 |  |
| 488.01(9)(a) | 9888-9888 | (a) refrain from examining or reproducing, in whole or in  | encoded | N99 |  |
| 488.01(9)(b) | 9889-9889 | (b) place any document obtained pursuant to the warrant, a | encoded | N99 |  |
| 488.01(10) | 9890-9891 | (10) On an application under subsection (9), the judge may | fork | N101 | F1 |
| 488.01(10)(a) | 9892-9892 | (a) confirm the warrant, authorization or order if the jud | fork | N101 | F1 |
| 488.01(10)(b) | 9893-9893 | (b) vary the warrant, authorization or order to impose any | fork | N101 | F1 |
| 488.01(10)(c) | 9894-9894 | (c) if the judge considers it necessary to protect the con | fork | N101 | F1 |
| 488.01(10)(d) | 9895-9895 | (d) revoke the warrant, authorization or order if the judg | fork | N101 | F1 |
| 488.02(1) | 9896-9897 | 488.02 (1) Any document obtained pursuant to a warrant, au | encoded | N102 |  |
| 488.02(2) | 9898-9899 | (2) No officer is to examine or reproduce, in whole or in  | encoded | N103 |  |
| 488.02(3) | 9900-9901 | (3) The journalist or relevant media outlet may, within 10 | fork | N104 | F7, G1 |
| 488.02(4) | 9902-9903 | (4) A document that is subject to an application under sub | encoded | N106 |  |
| 488.02(5) | 9904-9905 | (5) The judge may order the disclosure of a document only  | encoded | N107 |  |
| 488.02(5)(a) | 9906-9906 | (a) there is no other way by which the information can rea | encoded | N107 |  |
| 488.02(5)(b) | 9907-9907 | (b) the public interest in the investigation and prosecuti | encoded | N107 |  |
| 488.02(6) | 9908-9909 | (6) The judge may, if he or she considers it necessary, ex | fork | N108 | F1 |
| 488.02(7) | 9910-9911 | (7) The judge must, | encoded | N109 |  |
| 488.02(7)(a) | 9912-9912 | (a) if he or she is of the opinion that the document shoul | encoded | N109 |  |
| 488.02(7)(b) | 9913-9913 | (b) if he or she is of the opinion that the document shoul | encoded | N109 |  |
| 488.1(1) | 9914-9915 | 488.1 (1) In this section, | encoded | N110 |  |
| 488.1(1) "custodian" | 9916-9916 | custodian means a person in whose custody a package is pla | encoded | N110 |  |
| 488.1(1) "document" | 9917-9917 | document, for the purposes of this section, has the same m | encoded | N111 |  |
| 488.1(1) "judge" | 9918-9918 | judge means a judge of a superior court of criminal jurisd | encoded | N112 |  |
| 488.1(1) "lawyer" | 9919-9919 | lawyer means, in the Province of Quebec, an advocate, lawy | fork | N113 | F8 |
| 488.1(1) "officer" | 9920-9920 | officer means a peace officer or public officer. (fonction | encoded | N114 |  |
| 488.1(2) | 9921-9922 | (2) Where an officer acting under the authority of this or | encoded | N115 |  |
| 488.1(2)(a) | 9923-9923 | (a) seize the document and place it in a package and suita | encoded | N115 |  |
| 488.1(2)(b) | 9924-9924 | (b) place the package in the custody of the sheriff of the | encoded | N115 |  |
| 488.1(3) | 9925-9926 | (3) Where a document has been seized and placed in custody | fork | N117 | F7, G1 |
| 488.1(3)(a) | 9927-9929 | (a) within fourteen days from the day the document was so  | fork | N117 | F7, G1 |
| 488.1(3)(b) | 9930-9930 | (b) serve a copy of the order on all other persons entitle | encoded | N120 |  |
| 488.1(3)(c) | 9931-9931 | (c) if he has proceeded as authorized by paragraph (b), ap | fork | N122 | F1 |
| 488.1(4) | 9932-9933 | (4) On an application under paragraph (3)(c), the judge | fork | N123 | F1 |
| 488.1(4)(a) | 9934-9934 | (a) may, if the judge considers it necessary to determine  | fork | N123 | F1 |
| 488.1(4)(b) | 9935-9935 | (b) where the judge is of the opinion that it would materi | fork | N124 | F1 |
| 488.1(4)(c) | 9936-9936 | (c) shall allow the Attorney General and the person who ob | encoded | N125 |  |
| 488.1(4)(d) | 9937-9939 | (d) shall determine the question summarily and, | encoded | N126 |  |
| 488.1(4) closing words | 9940-9940 | and shall, at the same time, deliver concise reasons for t | encoded | N126 |  |
| 488.1(5) | 9941-9942 | (5) Where the judge determines pursuant to paragraph (4)(d | encoded | N128 |  |
| 488.1(6) | 9943-9944 | (6) Where a document has been seized and placed in custody | encoded | N129 |  |
| 488.1(7) | 9945-9946 | (7) Where the judge to whom an application has been made u | fork | N130 | G1 |
| 488.1(8) | 9947-9948 | (8) No officer shall examine, make copies of or seize any  | encoded | N131 |  |
| 488.1(9) | 9949-9950 | (9) At any time while a document is in the custody of a cu | fork | N132 | F1 |
| 488.1(10) | 9951-9952 | (10) An application under paragraph (3)(c) shall be heard  | encoded | N133 |  |
| 488.1(11) | 9953-9954 | (11) This section does not apply in circumstances where a  | encoded | N134 |  |
| 489(1) | 9955-9956 | 489 (1) Every person who executes a warrant may seize, in  | encoded | N135 |  |
| 489(1)(a) | 9957-9957 | (a) has been obtained by the commission of an offence agai | encoded | N135 |  |
| 489(1)(b) | 9958-9958 | (b) has been used in the commission of an offence against  | encoded | N135 |  |
| 489(1)(c) | 9959-9959 | (c) will afford evidence in respect of an offence against  | encoded | N135 |  |
| 489(2) | 9960-9961 | (2) Every peace officer, and every public officer who has  | encoded | N136 |  |
| 489(2)(a) | 9962-9962 | (a) has been obtained by the commission of an offence agai | encoded | N136 |  |
| 489(2)(b) | 9963-9963 | (b) has been used in the commission of an offence against  | encoded | N136 |  |
| 489(2)(c) | 9964-9964 | (c) will afford evidence in respect of an offence against  | encoded | N136 |  |
| 489.1(1) | 9965-9966 | 489.1 (1) Subject to this or any other Act of Parliament,  | encoded | N137 |  |
| 489.1(1)(a) | 9967-9969 | (a) return the thing seized, on being issued a receipt for | encoded | N137 |  |
| 489.1(1)(b) | 9970-9970 | (b) bring the thing seized before a justice referred to in | encoded | N137 |  |
| 489.1(2) | 9971-9972 | (2) Subject to this or any other Act of Parliament, if a p | encoded | N138 |  |
| 489.1(2)(a) | 9973-9973 | (a) bring the thing before a justice having jurisdiction i | encoded | N138 |  |
| 489.1(2)(b) | 9974-9974 | (b) report to the justice referred to in paragraph (a) tha | encoded | N138 |  |
| 489.1(3) | 9975-9976 | (3) A report to a justice under this section shall be in F | encoded | N139 |  |
| 489.1(4) | 9977-9978 | (4) This section does not apply with respect to computer d | encoded | N140 |  |
| 490(1) | 9979-9980 | 490 (1) Subject to this or any other Act of Parliament, wh | encoded | N141 |  |
| 490(1)(a) | 9981-9981 | (a) where the lawful owner or person who is lawfully entit | encoded | N141 |  |
| 490(1)(b) | 9982-9982 | (b) where the prosecutor, or the peace officer or other pe | encoded | N141 |  |
| 490(2) | 9983-9984 | (2) Nothing shall be detained under the authority of parag | encoded | N142 |  |
| 490(2)(a) | 9985-9985 | (a) a justice, on the making of a summary application to h | encoded | N142 |  |
| 490(2)(b) | 9986-9986 | (b) proceedings are instituted in which the thing detained | encoded | N142 |  |
| 490(3) | 9987-9988 | (3) More than one order for further detention may be made  | encoded | N144 |  |
| 490(3)(a) | 9989-9989 | (a) a judge of a superior court of criminal jurisdiction o | encoded | N144 |  |
| 490(3)(b) | 9990-9990 | (b) proceedings are instituted in which the thing detained | encoded | N144 |  |
| 490(3.1) | 9991-9992 | (3.1) A thing may be detained under paragraph (1)(b) for a | fork | N146 | F1 |
| 490(4) | 9993-9994 | (4) When an accused has been ordered to stand trial, the j | encoded | N147 |  |
| 490(5) | 9995-9996 | (5) Where at any time before the expiration of the periods | encoded | N148 |  |
| 490(5)(a) | 9997-9997 | (a) a judge of a superior court of criminal jurisdiction o | encoded | N148 |  |
| 490(5)(b) | 9998-9998 | (b) a justice, in any other case, | encoded | N148 |  |
| 490(5) closing words | 9999-9999 | who shall, after affording the person from whom the thing  | encoded | N148 |  |
| 490(6) | 10000-10001 | (6) Where the periods of detention provided for or ordered | encoded | N150 |  |
| 490(7) | 10002-10003 | (7) A person from whom anything has been seized may, after | fork | N151 | G1 |
| 490(7)(a) | 10004-10004 | (a) a judge of a superior court of criminal jurisdiction o | fork | N151 | G1 |
| 490(7)(b) | 10005-10005 | (b) a justice, in any other case, | fork | N151 | G1 |
| 490(7) closing words | 10006-10006 | for an order under paragraph (9)(c) that the thing seized  | fork | N151 | G1 |
| 490(8) | 10007-10008 | (8) A judge of a superior court of criminal jurisdiction o | fork | N152 | G1 |
| 490(9) | 10009-10010 | (9) Subject to this or any other Act of Parliament, if | fork | N153 | F9 |
| 490(9)(a) | 10011-10011 | (a) a judge referred to in subsection (7), where a judge o | fork | N153 | F9 |
| 490(9)(b) | 10012-10012 | (b) a justice, in any other case, | fork | N153 | F9 |
| 490(9) closing words | 10013-10013 | is satisfied that the periods of detention provided for or | fork | N153 | F9 |
| 490(9)(c) | 10014-10014 | (c) if possession of it by the person from whom it was sei | fork | N153 | F9 |
| 490(9)(d) | 10015-10015 | (d) if possession of it by the person from whom it was sei | fork | N153 | F9 |
| 490(9) closing words | 10016-10016 | and may, if possession of it by the person from whom it wa | fork | N153 | F9 |
| 490(9.1) | 10017-10018 | (9.1) Notwithstanding subsection (9), a judge or justice r | fork | N155 | F1 |
| 490(9.1)(a) | 10019-10019 | (a) that the continued detention of the thing might reason | fork | N155 | F1 |
| 490(9.1)(b) | 10020-10020 | (b) that it is in the interests of justice to do so. | fork | N155 | F1 |
| 490(10) | 10021-10022 | (10) Subject to this or any other Act of Parliament, a per | fork | N156 | G1 |
| 490(10)(a) | 10023-10023 | (a) a judge referred to in subsection (7), where a judge o | fork | N156 | G1 |
| 490(10)(b) | 10024-10024 | (b) a justice, in any other case, | fork | N156 | G1 |
| 490(10) closing words | 10025-10025 | for an order that the thing detained be returned to the ap | fork | N156 | G1 |
| 490(11) | 10026-10027 | (11) Subject to this or any other Act of Parliament, on an | encoded | N157 |  |
| 490(11)(a) | 10028-10028 | (a) the applicant is the lawful owner or lawfully entitled | encoded | N157 |  |
| 490(11)(b) | 10029-10029 | (b) the periods of detention provided for or ordered under | encoded | N157 |  |
| 490(11) closing words | 10030-10030 | the judge or justice shall order that | encoded | N157 |  |
| 490(11)(c) | 10031-10031 | (c) the thing seized be returned to the applicant, or | encoded | N157 |  |
| 490(11)(d) | 10032-10032 | (d) except as otherwise provided by law, where, pursuant t | encoded | N157 |  |
| 490(12) | 10033-10034 | (12) Notwithstanding anything in this section, nothing sha | encoded | N158 |  |
| 490(13) | 10035-10036 | (13) The Attorney General, the prosecutor or the peace off | encoded | N160 |  |
| 490(14) | 10037-10038 | (14) Every copy made under subsection (13) that is certifi | encoded | N161 |  |
| 490(15) | 10039-10040 | (15) Where anything is detained pursuant to subsections (1 | fork | N163 | G1 |
| 490(16) | 10041-10042 | (16) An order that is made under subsection (15) shall be  | encoded | N164 |  |
| 490(17) | 10043-10044 | (17) A person who feels aggrieved by an order made under s | encoded | N165 |  |
| 490(17)(a) | 10045-10045 | (a) to the court of appeal as defined in section 673 if th | encoded | N165 |  |
| 490(17)(b) | 10046-10046 | (b) to the appeal court as defined in section 812 in any o | encoded | N165 |  |
| 490(18) | 10047-10048 | (18) Any person to whom three days notice must be given un | encoded | N166 |  |
| 490.01 | 10049-10050 | 490.01 Where any thing seized pursuant to this Act is peri | fork | N167 | F1 |
| 490.01(a) | 10051-10051 | (a) may return it to its lawful owner or the person who is | fork | N167 | F1 |
| 490.01(b) | 10052-10054 | (b) where, on ex parte application to a justice, the justi | fork | N168 | F1 |
| group heading: Sex Offender Information | 10056-10056 | Sex Offender Information | inert | reason 1 (a heading of a group of sections) |  |
| 490.011(1) | 10058-10060 | 490.011 (1) The following definitions apply in this sectio | encoded | N180 |  |
| 490.011(1) "crime of a sexual nature" | 10061-10061 | crime of a sexual nature means a crime referred to in subs | encoded | N180 |  |
| 490.011(1) "database" | 10062-10062 | database has the same meaning as in subsection 3(1) of the | encoded | N181 |  |
| 490.011(1) "designated offence" | 10063-10063 | designated offence means a primary offence or a secondary  | encoded | N179 |  |
| 490.011(1) "Ontario Act" | 10064-10064 | Ontario Act means Christopher’s Law (Sex Offender Registry | encoded | N182 |  |
| 490.011(1) "pardon" | 10065-10065 | pardon means a conditional pardon granted under Her Majest | encoded | N183 |  |
| 490.011(1) "primary offence" | 10066-10066 | primary offence means | encoded | N175 |  |
| 490.011(1) "primary offence"(a) | 10067-10067 | (a) an offence under any of the following provisions: | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(i) | 10068-10068 | (i) subsection 7(4.1) (offence in relation to sexual offen | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(ii) | 10069-10069 | (ii) section 151 (sexual interference), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(iii) | 10070-10070 | (iii) section 152 (invitation to sexual touching or exposu | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(iv) | 10071-10071 | (iv) section 153 (sexual exploitation), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(v) | 10072-10072 | (v) section 153.1 (sexual exploitation of person with disa | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(vi) | 10073-10073 | (vi) section 155 (incest), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(vii) | 10074-10074 | (vii) subsection 160(1) (bestiality), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(viii) | 10075-10075 | (viii) subsection 160(2) (compelling the commission of bes | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(ix) | 10076-10076 | (ix) subsection 160(3) (bestiality in presence of or by a  | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(ix.1) | 10077-10077 | (ix.1) subsection 160(3.1) (representation of bestiality), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(x) | 10078-10078 | (x) subsection 162.1(1) (intimate image — publication etc. | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(x.1) | 10079-10079 | (x.1) subsection 162.1(1.1) (intimate image — threat to pu | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xi) | 10080-10080 | (xi) section 163.1 (child sexual abuse and exploitation ma | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xii) | 10081-10081 | (xii) section 170 (parent or guardian procuring sexual act | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xiii) | 10082-10082 | (xiii) section 171.1 (making sexually explicit material av | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xiv) | 10083-10083 | (xiv) section 172.1 (luring a child), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xv) | 10084-10084 | (xv) section 172.2 (agreement or arrangement — sexual offe | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xvi) | 10085-10085 | (xvi) subsection 173(2) (exposure), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xvii) | 10086-10086 | (xvii) section 271 (sexual assault), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xviii) | 10087-10087 | (xviii) section 272 (sexual assault with a weapon, threats | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xix) | 10088-10088 | (xix) section 273 (aggravated sexual assault), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xx) | 10089-10089 | (xx) subsection 273.3(2) (removal of a child from Canada), | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxi) | 10090-10090 | (xxi) section 279.011 (trafficking — person under 18 years | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxii) | 10091-10091 | (xxii) subsection 279.02(2) (material benefit — traffickin | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxiii) | 10092-10092 | (xxiii) subsection 279.03(2) (withholding or destroying do | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxiv) | 10093-10093 | (xxiv) subsection 286.1(2) (obtaining sexual services for  | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxv) | 10094-10094 | (xxv) subsection 286.2(2) (material benefit from sexual se | encoded | N175 |  |
| 490.011(1) "primary offence"(a)(xxvi) | 10095-10095 | (xxvi) subsection 286.3(2) (procuring — person under 18 ye | encoded | N175 |  |
| 490.011(1) "primary offence"(b) | 10096-10096 | (b) an offence under any of the following provisions of th | encoded | N175 |  |
| 490.011(1) "primary offence"(b)(i) | 10097-10097 | (i) section 144 (rape), | encoded | N175 |  |
| 490.011(1) "primary offence"(b)(ii) | 10098-10098 | (ii) section 145 (attempt to commit rape), | encoded | N175 |  |
| 490.011(1) "primary offence"(b)(iii) | 10099-10099 | (iii) section 149 (indecent assault on female), | encoded | N175 |  |
| 490.011(1) "primary offence"(b)(iv) | 10100-10100 | (iv) section 156 (indecent assault on male), and | encoded | N175 |  |
| 490.011(1) "primary offence"(b)(v) | 10101-10101 | (v) subsection 246(1) (assault with intent) if the intent  | encoded | N175 |  |
| 490.011(1) "primary offence"(c) | 10102-10102 | (c) an offence under any of the following provisions of th | encoded | N175 |  |
| 490.011(1) "primary offence"(c)(i) | 10103-10103 | (i) section 246.1 (sexual assault), | encoded | N175 |  |
| 490.011(1) "primary offence"(c)(ii) | 10104-10104 | (ii) section 246.2 (sexual assault with a weapon, threats  | encoded | N175 |  |
| 490.011(1) "primary offence"(c)(iii) | 10105-10105 | (iii) section 246.3 (aggravated sexual assault); | encoded | N175 |  |
| 490.011(1) "primary offence"(d) | 10106-10106 | (d) an offence under any of the following provisions of th | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(i) | 10107-10107 | (i) subsection 146(1) (sexual intercourse with a female un | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(ii) | 10108-10108 | (ii) subsection 146(2) (sexual intercourse with a female b | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(iii) | 10109-10109 | (iii) section 153 (sexual intercourse with step-daughter), | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(iv) | 10110-10110 | (iv) section 157 (gross indecency), | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(v) | 10111-10111 | (v) section 166 (parent or guardian procuring defilement), | encoded | N175 |  |
| 490.011(1) "primary offence"(d)(vi) | 10112-10112 | (vi) section 167 (householder permitting defilement); | encoded | N175 |  |
| 490.011(1) "primary offence"(e) | 10113-10113 | (e) an offence under any of the following provisions of th | encoded | N175 |  |
| 490.011(1) "primary offence"(e)(i) | 10114-10114 | (i) paragraph 212(1)(i) (stupefying or overpowering for th | encoded | N175 |  |
| 490.011(1) "primary offence"(e)(ii) | 10115-10115 | (ii) subsection 212(2) (living on the avails of prostituti | encoded | N175 |  |
| 490.011(1) "primary offence"(e)(iii) | 10116-10116 | (iii) subsection 212(2.1) (aggravated offence in relation  | encoded | N175 |  |
| 490.011(1) "primary offence"(e)(iv) | 10117-10117 | (iv) subsection 212(4) (prostitution of person under 18 ye | encoded | N175 |  |
| 490.011(1) "primary offence"(f) | 10118-10118 | (f) an attempt or conspiracy to commit an offence referred | encoded | N175 |  |
| 490.011(1) "record suspension" | 10119-10119 | record suspension means a record suspension, as defined in | encoded | N184 |  |
| 490.011(1) "registration centre" | 10120-10120 | registration centre has the same meaning as in subsection  | encoded | N185 |  |
| 490.011(1) "Review Board" | 10121-10121 | Review Board means the Review Board established or designa | encoded | N186 |  |
| 490.011(1) "secondary offence" | 10122-10122 | secondary offence means | encoded | N178 |  |
| 490.011(1) "secondary offence"(a) | 10123-10123 | (a) an offence under any of the following provisions: | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(i) | 10124-10124 | (i) section 162 (voyeurism), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(ii) | 10125-10125 | (ii) subsection 173(1) (indecent acts), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(iii) | 10126-10126 | (iii) section 177 (trespassing at night), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(iv) | 10127-10127 | (iv) section 231 (murder), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(v) | 10128-10128 | (v) section 234 (manslaughter), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(vi) | 10129-10129 | (vi) paragraph 245(1)(a) (administering noxious thing with | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(vii) | 10130-10130 | (vii) paragraph 245(1)(b) (administering noxious thing wit | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(viii) | 10131-10131 | (viii) section 246 (overcoming resistance to commission of | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(ix) | 10132-10132 | (ix) section 264 (criminal harassment), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(x) | 10133-10133 | (x) section 279 (kidnapping), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xi) | 10134-10134 | (xi) section 279.01 (trafficking in persons), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xii) | 10135-10135 | (xii) subsection 279.02(1) (material benefit — trafficking | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xiii) | 10136-10136 | (xiii) subsection 279.03(1) (withholding or destroying doc | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xiv) | 10137-10137 | (xiv) section 280 (abduction of a person under age of sixt | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xv) | 10138-10138 | (xv) section 281 (abduction of a person under age of fourt | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xvi) | 10139-10139 | (xvi) subsection 286.1(1) (obtaining sexual services for c | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xvii) | 10140-10140 | (xvii) subsection 286.2(1) (material benefit from sexual s | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xviii) | 10141-10141 | (xviii) subsection 286.3(1) (procuring), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xix) | 10142-10142 | (xix) section 346 (extortion), | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xx) | 10143-10143 | (xx) paragraph 348(1)(d) (breaking and entering a dwelling | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xxi) | 10144-10144 | (xxi) paragraph 348(1)(d) (breaking and entering a dwellin | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xxii) | 10145-10145 | (xxii) paragraph 348(1)(e) (breaking and entering a place  | encoded | N178 |  |
| 490.011(1) "secondary offence"(a)(xxiii) | 10146-10146 | (xxiii) paragraph 348(1)(e) (breaking and entering a place | encoded | N178 |  |
| 490.011(1) "secondary offence"(b) | 10147-10147 | (b) an attempt or conspiracy to commit an offence referred | encoded | N178 |  |
| 490.011(1) "verdict of not criminally responsible on account of mental disorder" | 10148-10148 | verdict of not criminally responsible on account of mental | encoded | N187 |  |
| 490.011(2) | 10149-10150 | (2) For the purpose of this section and sections 490.012 t | encoded | N188 |  |
| 490.011(2)(a) | 10151-10151 | (a) within the meaning of subsection 2(1) of the Youth Cri | encoded | N188 |  |
| 490.011(2)(b) | 10152-10152 | (b) within the meaning of subsection 2(1) of the Young Off | encoded | N188 |  |
| group heading: Order to Comply with the Sex Offender Information Registration Act | 10154-10154 | Order to Comply with the Sex Offender Information Registra | inert | reason 1 (a heading of a group of sections) |  |
| 490.012(1) | 10155-10156 | 490.012 (1) Subject to subsection (5), when a court impose | fork | N190 | F11 |
| 490.012(1)(a) | 10157-10157 | (a) the designated offence was prosecuted by indictment; | fork | N190 | F11 |
| 490.012(1)(b) | 10158-10158 | (b) the sentence for the designated offence is a term of i | fork | N190 | F11 |
| 490.012(1)(c) | 10159-10159 | (c) the victim of the designated offence is under the age  | fork | N190 | F11 |
| 490.012(2) | 10160-10161 | (2) Subject to subsection (5), when a court imposes a sent | encoded | N191 |  |
| 490.012(2)(a) | 10162-10162 | (a) was previously convicted of a primary offence or previ | encoded | N191 |  |
| 490.012(2)(b) | 10163-10163 | (b) is or was, as a result of a conviction, subject to an  | encoded | N191 |  |
| 490.012(3) | 10164-10165 | (3) Subject to subsection (5), when a court imposes a sent | fork | N192 | F12 |
| 490.012(3)(a) | 10166-10166 | (a) there would be no connection between making the order  | fork | N192 | F12 |
| 490.012(3)(b) | 10167-10167 | (b) the impact of the order on the person, including on th | fork | N192 | F12 |
| 490.012(4) | 10168-10169 | (4) In determining whether to make an order under subsecti | encoded | N193 |  |
| 490.012(4)(a) | 10170-10170 | (a) the nature and seriousness of the designated offence; | encoded | N193 |  |
| 490.012(4)(b) | 10171-10171 | (b) the victim’s age and other personal characteristics; | encoded | N193 |  |
| 490.012(4)(c) | 10172-10172 | (c) the nature and circumstances of the relationship betwe | encoded | N193 |  |
| 490.012(4)(d) | 10173-10173 | (d) the personal characteristics and circumstances of the  | encoded | N193 |  |
| 490.012(4)(e) | 10174-10174 | (e) the person’s criminal history, including the age at wh | encoded | N193 |  |
| 490.012(4)(f) | 10175-10175 | (f) the opinions of experts who have examined the person;  | encoded | N193 |  |
| 490.012(4)(g) | 10176-10176 | (g) any other factors that the court considers relevant. | encoded | N193 |  |
| 490.012(5) | 10177-10178 | (5) A court shall make an order under any of subsections ( | encoded | N189 |  |
| 490.013(1) | 10179-10180 | 490.013 (1) An order made under section 490.012 begins on  | encoded | N194 |  |
| 490.013(2) | 10181-10182 | (2) An order made under subsection 490.012(1) or (3) | fork | N195 | F13 |
| 490.013(2)(a) | 10183-10183 | (a) subject to subsections (3) and (5), ends 10 years afte | fork | N195 | F13 |
| 490.013(2)(b) | 10184-10184 | (b) subject to subsections (3) and (5), ends 20 years afte | fork | N195 | F13 |
| 490.013(2)(c) | 10185-10185 | (c) applies for life if the maximum term of imprisonment f | fork | N195 | F13 |
| 490.013(2.1) | 10186-10186 | (2.1) [Repealed, 2023, c. 28, s. 8] | repealed or blank in this text | the text shows: (2.1) [Repealed, 2023, c. 28, s. 8] |  |
| 490.013(3) | 10187-10188 | (3) An order made under subsection 490.012(1) or (3) appli | encoded | N196 |  |
| 490.013(3)(a) | 10189-10189 | (a) in the same proceeding, the person has been convicted  | encoded | N196 |  |
| 490.013(3)(b) | 10190-10190 | (b) the court is satisfied that those offences demonstrate | encoded | N196 |  |
| 490.013(4) | 10191-10192 | (4) If paragraph (3)(a) applies in the circumstances but t | encoded | N197 |  |
| 490.013(5) | 10193-10194 | (5) An order made under subsection 490.012(1) or (3) appli | encoded | N198 |  |
| 490.013(5)(a) | 10195-10195 | (a) was previously convicted of, or previously received a  | encoded | N198 |  |
| 490.013(5)(b) | 10196-10196 | (b) is, or was at any time, the subject of an order or obl | encoded | N198 |  |
| 490.013(6) | 10197-10198 | (6) An order made under subsection 490.012(2) applies for  | encoded | N199 |  |
| 490.0131 | 10199-10200 | 490.0131 The court shall | encoded | N202 |  |
| 490.0131(a) | 10201-10201 | (a) state the designated offence, and the term of imprison | encoded | N202 |  |
| 490.0131(b) | 10202-10202 | (b) give reasons for a decision under subsection 490.012(3 | encoded | N202 |  |
| 490.0132 | 10203-10204 | 490.0132 If the court does not consider the matter under a | encoded | N203 |  |
| 490.0132(a) | 10205-10205 | (a) shall, within 90 days after the day on which it impose | encoded | N203 |  |
| 490.0132(b) | 10206-10206 | (b) retains jurisdiction over the matter; | encoded | N204 |  |
| 490.0132(c) | 10207-10207 | (c) may require the person to appear at the hearing by vid | fork | N205 | F1, G1 |
| 490.0132(d) | 10208-10208 | (d) may issue a summons in Form 6.3 to compel the attendan | fork | N206 | F1 |
| 490.014 | 10209-10210 | 490.014 The prosecutor, or a person who is subject to an o | encoded | N210 |  |
| 490.014(a) | 10211-10211 | (a) dismiss the appeal; or | encoded | N211 |  |
| 490.014(b) | 10212-10212 | (b) allow the appeal and order a new hearing, quash or ame | encoded | N211 |  |
| 490.015(1) | 10213-10214 | 490.015 (1) A person who is subject to an order may apply  | fork | N212 | F10, F5 |
| 490.015(1)(a) | 10215-10215 | (a) if five years have elapsed since the order was made, i | fork | N212 | F10, F5 |
| 490.015(1)(b) | 10216-10216 | (b) if 10 years have elapsed since the order was made, in  | fork | N212 | F10, F5 |
| 490.015(1)(c) | 10217-10217 | (c) if 20 years have elapsed since the order was made, in  | fork | N212 | F10, F5 |
| 490.015(2) | 10218-10219 | (2) A person who is subject to more than one order made un | fork | N214 | F10, F5 |
| 490.015(3) | 10220-10221 | (3) Despite subsections (1) and (2), a person may apply fo | fork | N215 | F1 |
| 490.015(4) | 10222-10223 | (4) The application shall be in relation to every order th | encoded | N216 |  |
| 490.015(5) | 10224-10225 | (5) A person whose application is refused may re-apply if  | fork | N218 | F5 |
| 490.015(6) | 10226-10227 | (6) The application shall be made to | encoded | N219 |  |
| 490.015(6)(a) | 10228-10230 | (a) a superior court of criminal jurisdiction if | encoded | N219 |  |
| 490.015(6)(b) | 10231-10231 | (b) a court of criminal jurisdiction, in any other case in | encoded | N219 |  |
| 490.016(1) | 10232-10233 | 490.016 (1) The court shall make a termination order if it | encoded | N220 |  |
| 490.016(1)(a) | 10234-10234 | (a) there would be no connection between continuing an ord | encoded | N220 |  |
| 490.016(1)(b) | 10235-10235 | (b) the impact on the person of continuing an order or obl | encoded | N220 |  |
| 490.016(1.1) | 10236-10237 | (1.1) In determining whether to make the termination order | encoded | N221 |  |
| 490.016(1.1)(a) | 10238-10238 | (a) the nature and seriousness of the offence that is the  | encoded | N221 |  |
| 490.016(1.1)(b) | 10239-10239 | (b) the victim’s age and other personal characteristics; | encoded | N221 |  |
| 490.016(1.1)(c) | 10240-10240 | (c) the nature and circumstances of the relationship betwe | encoded | N221 |  |
| 490.016(1.1)(d) | 10241-10241 | (d) the personal characteristics and circumstances of the  | encoded | N221 |  |
| 490.016(1.1)(e) | 10242-10242 | (e) the person’s criminal history, including the age at wh | encoded | N221 |  |
| 490.016(1.1)(f) | 10243-10243 | (f) the opinions of experts who have examined the person;  | encoded | N221 |  |
| 490.016(1.1)(g) | 10244-10244 | (g) any other factors that the court considers relevant. | encoded | N221 |  |
| 490.016(2) | 10245-10246 | (2) The court shall give reasons for its decision. | encoded | N222 |  |
| 490.016(3) | 10247-10248 | (3) If the court makes a termination order, it shall cause | encoded | N223 |  |
| 490.017(1) | 10249-10250 | 490.017 (1) The prosecutor or the person who applied for a | encoded | N224 |  |
| 490.017(2) | 10251-10252 | (2) If the appeal court makes an order that may be made un | encoded | N226 |  |
| 490.018(1) | 10253-10254 | 490.018 (1) When a court or appeal court makes an order un | encoded | N227 |  |
| 490.018(1)(a) | 10255-10255 | (a) the order to be read by or to the person who is subjec | encoded | N227 |  |
| 490.018(1)(b) | 10256-10256 | (b) a copy of the order to be given to that person; | encoded | N227 |  |
| 490.018(1)(c) | 10257-10257 | (c) that person to be informed of sections 4 to 7.1 of the | encoded | N227 |  |
| 490.018(1)(d) | 10258-10262 | (d) a copy of the order to be sent to | encoded | N227 |  |
| 490.018(2) | 10263-10264 | (2) After paragraphs (1)(a) to (c) have been complied with | encoded | N228 |  |
| 490.018(3) | 10265-10266 | (3) A Review Board shall cause a copy of the order to be g | encoded | N229 |  |
| 490.018(3)(a) | 10267-10267 | (a) under paragraph 672.54(a), that the person be discharg | encoded | N229 |  |
| 490.018(3)(b) | 10268-10268 | (b) under paragraph 672.54(b), that the person be discharg | encoded | N229 |  |
| 490.018(4) | 10269-10270 | (4) The person in charge of the place in which the person  | encoded | N230 |  |
| group heading: Notice and Obligation to Comply with the Sex Offender Information Registration Act — Convictions Before December 15, 2004 | 10272-10272 | Notice and Obligation to Comply with the Sex Offender Info | inert | reason 1 (a heading of a group of sections) |  |
| 490.019 | 10273-10274 | 490.019 A person who is served with a notice in Form 53 sh | encoded | N232 |  |

### Index of L4 names

| index | L4 name | module |
| --- | --- | --- |
| N1 | `s 487.05(1) the provincial court judge may issue a warrant in Form 5.02` | ccc17-dna-orders.l4 |
| N2 | `s 487.05(2) the provincial court judge shall have regard to the matter` | ccc17-dna-orders.l4 |
| N3 | `s 487.05(4) the warrant may be executed by the peace officer at the place` | ccc17-dna-orders.l4 |
| N4 | `s 487.051(1) the court shall make an order in Form 5.03` | ccc17-dna-orders.l4 |
| N5 | `s 487.051(2) the court shall make an order in Form 5.03` | ccc17-dna-orders.l4 |
| N6 | `s 487.051(3) the court may make an order in Form 5.04` | ccc17-dna-orders.l4 |
| N7 | `s 487.051(3) the court shall consider the matter in deciding whether to make the order` | ccc17-dna-orders.l4 |
| N8 | `s 487.051(3) the court shall give reasons for its decision` | ccc17-dna-orders.l4 |
| N9 | `s 487.051(4) the court may make an order in Form 5.041 requiring the person to report and submit to the taking of the samples` | ccc17-dna-orders.l4 |
| N10 | `s 487.053(1) the court may make an order under section 487.051 at this time` | ccc17-dna-orders.l4 |
| N11 | `s 487.053(2)(a) the court shall set a date for a hearing within 90 days` | ccc17-dna-orders.l4 |
| N12 | `s 487.053(2)(b) the court retains jurisdiction over the matter` | ccc17-dna-orders.l4 |
| N13 | `s 487.053(2)(c) the court may require the person to appear by closed-circuit television or videoconference` | ccc17-dna-orders.l4 |
| N14 | `s 487.053(2)(a) the last day for the court to set a date for the hearing` | ccc17-dna-orders.l4 |
| N15 | `s 487.053(2)(a) the court set the date within 90 days` | ccc17-dna-orders.l4 |
| N16 | `s 487.053(2)(a) the court must set a date for the hearing` | ccc17-dna-orders.l4 |
| N17 | `s 487.054 the person may appeal from the decision of the court` | ccc17-dna-orders.l4 |
| N18 | `s 487.055(3)(a) the provisions` | ccc17-dna-orders.l4 |
| N19 | `s 487.055(3)(b) the provisions` | ccc17-dna-orders.l4 |
| N20 | `s 487.055(3)(c) the provision` | ccc17-dna-orders.l4 |
| N21 | `s 487.055(3) the offence is a sexual offence` | ccc17-dna-orders.l4 |
| N22 | `s 487.055(3) the offence attempted is one referred to in paragraphs (a) to (c)` | ccc17-dna-orders.l4 |
| N23 | `s 487.055(1) the provincial court judge may authorize in Form 5.06 the taking of samples of bodily substances` | ccc17-dna-orders.l4 |
| N24 | `s 487.055(2) the application is accompanied by the certificate` | ccc17-dna-orders.l4 |
| N25 | `s 487.055(2) the certificate may be received in evidence without the notice referred to in subsection 667(4)` | ccc17-dna-orders.l4 |
| N26 | `s 487.055(3.01) the court may require the person to appear by closed-circuit television or videoconference` | ccc17-dna-orders.l4 |
| N27 | `s 487.055(3.1) the court shall consider the matter in deciding whether to grant an authorization` | ccc17-dna-orders.l4 |
| N28 | `s 487.055(3.1) the court shall give reasons for its decision` | ccc17-dna-orders.l4 |
| N29 | `s 487.055(3.11) the court shall make an order in Form 5.041 requiring the person to report and submit to the taking of the samples` | ccc17-dna-orders.l4 |
| N30 | `s 487.055(4) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples` | ccc17-dna-orders.l4 |
| N31 | `s 487.055(5) the summons is served as the subsection requires` | ccc17-dna-orders.l4 |
| N32 | `s 487.0551(1) a justice of the peace may issue a warrant for the arrest of the person in Form 5.062` | ccc17-dna-orders.l4 |
| N33 | `s 487.0551(2) the warrant may be executed by the peace officer at the place` | ccc17-dna-orders.l4 |
| N34 | `s 487.0551(2) the warrant remains in force` | ccc17-dna-orders.l4 |
| N35 | `s 487.0552(1) the person is guilty of an offence` | ccc17-dna-orders.l4 |
| N36 | `s 487.0552(1) the punishments` | ccc17-dna-orders.l4 |
| N37 | `s 487.0552(2) a lawful command that prevents the person from complying is a reasonable excuse` | ccc17-dna-orders.l4 |
| N38 | `s 487.056(1) the time at which the samples shall be taken under section 487.051` | ccc17-dna-samples.l4 |
| N39 | `s 487.056(2) the time at which the samples shall be taken under section 487.055 or 487.091` | ccc17-dna-samples.l4 |
| N40 | `s 487.056(3) the time at which the samples shall be taken when the person fails to appear` | ccc17-dna-samples.l4 |
| N41 | `s 487.056(4) subsections (1) to (3) apply even though the order or authorization is appealed` | ccc17-dna-samples.l4 |
| N42 | `s 487.056(5) the peace officer may cause the samples to be taken in the place` | ccc17-dna-samples.l4 |
| N43 | `s 487.056(6) the samples are taken by a person the subsection permits` | ccc17-dna-samples.l4 |
| N44 | `s 487.057(1) the peace officer shall make a written report in Form 5.07 and cause it to be filed` | ccc17-dna-samples.l4 |
| N45 | `s 487.057(1) with whom the report shall be filed` | ccc17-dna-samples.l4 |
| N46 | `s 487.057(2) the report shall include the matter` | ccc17-dna-samples.l4 |
| N47 | `s 487.057(3) the peace officer shall send a copy of the report to the other peace officer` | ccc17-dna-samples.l4 |
| N48 | `s 487.058 the person incurs no criminal or civil liability for the thing done` | ccc17-dna-samples.l4 |
| N49 | `s 487.06(1) the means is one by which the peace officer is authorized to take samples of bodily substances` | ccc17-dna-samples.l4 |
| N50 | `s 487.06(2) the warrant, order or authorization shall include the term or condition` | ccc17-dna-samples.l4 |
| N51 | `s 487.06(3) the peace officer, or a person acting under their direction, may take fingerprints from the person for the purpose of the DNA Identification Act` | ccc17-dna-samples.l4 |
| N52 | `s 487.07(1) the peace officer shall inform the person of the matter before taking the samples` | ccc17-dna-samples.l4 |
| N53 | `s 487.07(2)(a) the person may be detained for the purpose of taking the samples` | ccc17-dna-samples.l4 |
| N54 | `s 487.07(2)(b) the person may be required to accompany a peace officer for the purpose of taking the samples` | ccc17-dna-samples.l4 |
| N55 | `s 487.07(3) the taker shall ensure that the person’s privacy is respected in a manner that is reasonable in the circumstances` | ccc17-dna-samples.l4 |
| N56 | `s 487.07(4) the young person has the right to consult counsel and an adult and to have the warrant executed in their presence` | ccc17-dna-samples.l4 |
| N57 | `s 487.07(4) the adult with whom the young person may consult and in whose presence the warrant is to be executed` | ccc17-dna-samples.l4 |
| N58 | `s 487.07(5) the young person’s waiver of the rights under subsection (4) is valid` | ccc17-dna-samples.l4 |
| N59 | `s 487.071(1) the peace officer, or the person acting under their direction, shall verify whether the convicted offenders index contains the person’s DNA profile` | ccc17-dna-samples.l4 |
| N60 | `s 487.071(2) the peace officer shall not take any bodily substances from the person` | ccc17-dna-samples.l4 |
| N61 | `s 487.071(2) the peace officer shall confirm in writing on the order or authorization that they have been advised that the profile is in the data bank and transmit a copy to the Commissioner of the Royal Canadian Mounted Police` | ccc17-dna-samples.l4 |
| N62 | `s 487.071(3) the peace officer shall execute the order or authorization and transmit the bodily substances taken and a copy to the Commissioner of the Royal Canadian Mounted Police` | ccc17-dna-samples.l4 |
| N63 | `s 487.08(1) the use of the bodily substances is barred` | ccc17-dna-samples.l4 |
| N64 | `s 487.08(1.1) the use of the bodily substances is barred` | ccc17-dna-samples.l4 |
| N65 | `s 487.08(2) the use of the results of forensic DNA analysis is barred` | ccc17-dna-samples.l4 |
| N66 | `s 487.08(3) the person is guilty of an offence punishable on summary conviction` | ccc17-dna-samples.l4 |
| N67 | `s 487.08(3) the punishments` | ccc17-dna-samples.l4 |
| N68 | `s 487.08(4) the person is guilty of an offence` | ccc17-dna-samples.l4 |
| N69 | `s 487.08(4) the punishments` | ccc17-dna-samples.l4 |
| N70 | `s 487.09(1) the bodily substances and the results of forensic DNA analysis shall be destroyed without delay` | ccc17-dna-samples.l4 |
| N71 | `s 487.09(1)(c) the day on which one year after the event expires` | ccc17-dna-samples.l4 |
| N72 | `s 487.09(1)(c) one year after the event has expired on the day in question` | ccc17-dna-samples.l4 |
| N73 | `s 487.09(2) the provincial court judge may order that the bodily substances and the results not be destroyed during the period considered appropriate` | ccc17-dna-samples.l4 |
| N74 | `s 487.09(3) the voluntarily given bodily substances and the results shall be destroyed without delay` | ccc17-dna-samples.l4 |
| N75 | `s 487.091(1) the provincial court judge may authorize in Form 5.09 the taking of additional samples of bodily substances` | ccc17-dna-samples.l4 |
| N76 | `s 487.091(2) the application states the reasons the subsection requires` | ccc17-dna-samples.l4 |
| N77 | `s 487.091(3) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples` | ccc17-dna-samples.l4 |
| N78 | `s 487.091(3) subsection 487.055(5) applies to the summons with the modifications that the circumstances require` | ccc17-dna-samples.l4 |
| N79 | `s 487.0911(1) the Attorney General shall review the order or authorization and the court record` | ccc17-dna-samples.l4 |
| N80 | `s 487.0911(2) the Attorney General shall apply ex parte to have the order or authorization corrected` | ccc17-dna-samples.l4 |
| N81 | `s 487.0911(2)(b) the Attorney General shall transmit a copy of the corrected order or authorization to the Commissioner` | ccc17-dna-samples.l4 |
| N82 | `s 487.0911(3) the Attorney General shall inform the Commissioner of the opinion that the offence is not a designated offence` | ccc17-dna-samples.l4 |
| N83 | `s 487.0911(4) the Attorney General shall transmit the opinion, with written reasons, to the Commissioner` | ccc17-dna-samples.l4 |
| N84 | `s 488.01(1) data` | ccc17-journalists.l4 |
| N85 | `s 488.01(1) document` | ccc17-journalists.l4 |
| N86 | `s 488.01(1) journalist` | ccc17-journalists.l4 |
| N87 | `s 488.01(1) journalistic source` | ccc17-journalists.l4 |
| N88 | `s 488.01(1) officer` | ccc17-journalists.l4 |
| N89 | `s 488.01(1) the definitions apply in this section and in section 488.02` | ccc17-journalists.l4 |
| N90 | `s 488.01(2) the applicant shall make the application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552` | ccc17-journalists.l4 |
| N91 | `s 488.01(2) the sections named` | ccc17-journalists.l4 |
| N92 | `s 488.01(2) the judge has exclusive jurisdiction to dispose of the application` | ccc17-journalists.l4 |
| N93 | `s 488.01(3) the judge may issue the warrant, authorization or order` | ccc17-journalists.l4 |
| N94 | `s 488.01(4) the judge may request that a special advocate present observations in the interests of freedom of the press concerning the conditions set out in subsection (3)` | ccc17-journalists.l4 |
| N95 | `s 488.01(5) subsections (3) and (4) do not apply` | ccc17-journalists.l4 |
| N96 | `s 488.01(6) the judge may order that some or all documents obtained are to be dealt with in accordance with section 488.02` | ccc17-journalists.l4 |
| N97 | `s 488.01(7) the warrant, authorization or order may contain the condition` | ccc17-journalists.l4 |
| N98 | `s 488.01(8) the judge has the same powers, with the necessary adaptations, as the authority who may issue the warrant, authorization or order` | ccc17-journalists.l4 |
| N99 | `s 488.01(9) the officer shall, as soon as possible, make an ex parte application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552` | ccc17-journalists.l4 |
| N100 | `s 488.01(9) until the judge disposes of the application the officer shall refrain from examining or reproducing any document obtained and shall keep it in a sealed packet` | ccc17-journalists.l4 |
| N101 | `s 488.01(10) the judge may make the order` | ccc17-journalists.l4 |
| N102 | `s 488.02(1) the document shall be placed in a packet and sealed by the court and kept in the custody of the court` | ccc17-journalists.l4 |
| N103 | `s 488.02(2) the officer is barred from examining or reproducing the document` | ccc17-journalists.l4 |
| N104 | `s 488.02(3) the journalist or media outlet may apply to a judge of the court that issued the warrant, authorization or order for an order that the document is not to be disclosed to an officer` | ccc17-journalists.l4 |
| N105 | `s 488.02(3) the last day on which the application may be made` | ccc17-journalists.l4 |
| N106 | `s 488.02(4) the document is not to be disclosed to an officer` | ccc17-journalists.l4 |
| N107 | `s 488.02(5) the judge may order the disclosure of the document` | ccc17-journalists.l4 |
| N108 | `s 488.02(6) the judge may examine the document` | ccc17-journalists.l4 |
| N109 | `s 488.02(7) the order the judge must make` | ccc17-journalists.l4 |
| N110 | `s 488.1(1) custodian` | ccc17-privilege.l4 |
| N111 | `s 488.1(1) document` | ccc17-privilege.l4 |
| N112 | `s 488.1(1) judge` | ccc17-privilege.l4 |
| N113 | `s 488.1(1) lawyer` | ccc17-privilege.l4 |
| N114 | `s 488.1(1) officer` | ccc17-privilege.l4 |
| N115 | `s 488.1(2) the officer shall, without examining or making copies of the document, seize it and place it in a package, suitably sealed and identified` | ccc17-privilege.l4 |
| N116 | `s 488.1(2)(b) the package shall be placed in the custody of` | ccc17-privilege.l4 |
| N117 | `s 488.1(3)(a) the person may apply to a judge for an order appointing a place and a day for the determination of the question and requiring the custodian to produce the document` | ccc17-privilege.l4 |
| N118 | `s 488.1(3)(a) the last day to apply to a judge` | ccc17-privilege.l4 |
| N119 | `s 488.1(3)(a)(i) the latest day that may be appointed for the determination of the question` | ccc17-privilege.l4 |
| N120 | `s 488.1(3)(b) the last day to serve a copy of the order on all other persons entitled to make application and on the custodian` | ccc17-privilege.l4 |
| N121 | `s 488.1(3)(b) the copy of the order is served within six days` | ccc17-privilege.l4 |
| N122 | `s 488.1(3)(c) the person may apply at the appointed time and place for an order determining the question` | ccc17-privilege.l4 |
| N123 | `s 488.1(4)(a) the judge may inspect the document` | ccc17-privilege.l4 |
| N124 | `s 488.1(4)(b) the judge may allow the Attorney General to inspect the document` | ccc17-privilege.l4 |
| N125 | `s 488.1(4)(c) the judge shall allow the Attorney General and the person who objects to the disclosure of the document to make representations` | ccc17-privilege.l4 |
| N126 | `s 488.1(4)(d) the order the judge shall make` | ccc17-privilege.l4 |
| N127 | `s 488.1(4) the judge shall, at the same time, deliver concise reasons for the determination in which the nature of the document is described without divulging the details` | ccc17-privilege.l4 |
| N128 | `s 488.1(5) the document remains privileged and inadmissible as evidence` | ccc17-privilege.l4 |
| N129 | `s 488.1(6) the judge shall order the custodian to deliver the document to the officer who seized it or to some other person designated by the Attorney General` | ccc17-privilege.l4 |
| N130 | `s 488.1(7) subsequent applications under paragraph (3)(c) may be made to another judge` | ccc17-privilege.l4 |
| N131 | `s 488.1(8) the officer is barred from examining, making copies of or seizing the document` | ccc17-privilege.l4 |
| N132 | `s 488.1(9) the judge may authorize the person to examine the document or make a copy of it in the presence of the custodian or the judge` | ccc17-privilege.l4 |
| N133 | `s 488.1(10) the application shall be heard in private` | ccc17-privilege.l4 |
| N134 | `s 488.1(11) this section does not apply` | ccc17-privilege.l4 |
| N135 | `s 489(1) the person who executes a warrant may seize the thing in addition to the things mentioned in the warrant` | ccc17-seizure.l4 |
| N136 | `s 489(2) the officer may, without a warrant, seize the thing` | ccc17-seizure.l4 |
| N137 | `s 489.1(1) what the peace officer shall do as soon as is practicable` | ccc17-seizure.l4 |
| N138 | `s 489.1(2) the person shall, as soon as is practicable, bring the thing before a justice or report to the justice that it has been seized and is being detained` | ccc17-seizure.l4 |
| N139 | `s 489.1(3) the report to a justice shall be in Form 5.2, varied to suit the case` | ccc17-seizure.l4 |
| N140 | `s 489.1(4) section 489.1 does not apply to the thing` | ccc17-seizure.l4 |
| N141 | `s 490(1) the order the justice shall make` | ccc17-seizure.l4 |
| N142 | `s 490(2) the section bars detaining the thing for more than 180 days after the day of the seizure` | ccc17-seizure.l4 |
| N143 | `s 490(2) the last day on which the thing may be detained without a further order` | ccc17-seizure.l4 |
| N144 | `s 490(3) the section bars detaining the thing for more than one year from the day of the seizure` | ccc17-seizure.l4 |
| N145 | `s 490(3) the last day on which the thing may be detained without a judge’s order` | ccc17-seizure.l4 |
| N146 | `s 490(3.1) the thing may be detained for the period` | ccc17-seizure.l4 |
| N147 | `s 490(4) the justice shall forward anything detained to the clerk of the court to which the accused has been ordered to stand trial` | ccc17-seizure.l4 |
| N148 | `s 490(5) the court to which the application is made` | ccc17-seizure.l4 |
| N149 | `s 490(5) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9)` | ccc17-seizure.l4 |
| N150 | `s 490(6) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9) or (9.1)` | ccc17-seizure.l4 |
| N151 | `s 490(7) the person from whom anything has been seized may apply summarily for an order under paragraph (9)(c) that the thing be returned` | ccc17-seizure.l4 |
| N152 | `s 490(8) the judge or justice may allow an application under subsection (7) to be made before the expiration of the periods` | ccc17-seizure.l4 |
| N153 | `s 490(9) the order the judge or justice shall make` | ccc17-seizure.l4 |
| N154 | `s 490(9) the judge or justice may order the thing forfeited to Her Majesty, to be disposed of as the Attorney General directs or otherwise dealt with in accordance with the law` | ccc17-seizure.l4 |
| N155 | `s 490(9.1) the judge or justice may order that the thing continue to be detained for such period as the judge or justice considers necessary` | ccc17-seizure.l4 |
| N156 | `s 490(10) the claimant may at any time apply summarily for an order that the thing detained be returned to the applicant` | ccc17-seizure.l4 |
| N157 | `s 490(11) the order the judge or justice shall make on the application under subsection (10)` | ccc17-seizure.l4 |
| N158 | `s 490(12) nothing shall be returned, forfeited or disposed of` | ccc17-seizure.l4 |
| N159 | `s 490(12) the last day of the thirty days after the order` | ccc17-seizure.l4 |
| N160 | `s 490(13) the person may make, and retain, a copy of the document before bringing it before a justice or complying with an order` | ccc17-seizure.l4 |
| N161 | `s 490(14) the copy is admissible in evidence` | ccc17-seizure.l4 |
| N162 | `s 490(14) the copy has the same probative force as the original document would have if it had been proved in the ordinary way` | ccc17-seizure.l4 |
| N163 | `s 490(15) the judge may order that the person be permitted to examine anything so detained` | ccc17-seizure.l4 |
| N164 | `s 490(16) the order shall be made on terms necessary or desirable to ensure that anything is safeguarded and preserved for any purpose for which it may subsequently be required` | ccc17-seizure.l4 |
| N165 | `s 490(17) the court to which the person aggrieved may appeal` | ccc17-seizure.l4 |
| N166 | `s 490(18) the person may agree that the application be made before the expiration of the three days` | ccc17-seizure.l4 |
| N167 | `s 490.01(a) the person may return the thing to its lawful owner or the person lawfully entitled to possession of it` | ccc17-seizure.l4 |
| N168 | `s 490.01(b) the person may dispose of the thing, or destroy it` | ccc17-seizure.l4 |
| N169 | `s 490.01(b)(i) the proceeds of disposition` | ccc17-seizure.l4 |
| N170 | `s 490.011(1) primary offence (a) the provisions` | ccc17-sor.l4 |
| N171 | `s 490.011(1) primary offence (b) the provisions` | ccc17-sor.l4 |
| N172 | `s 490.011(1) primary offence (c) the provisions` | ccc17-sor.l4 |
| N173 | `s 490.011(1) primary offence (d) the provisions` | ccc17-sor.l4 |
| N174 | `s 490.011(1) primary offence (e) the provisions` | ccc17-sor.l4 |
| N175 | `s 490.011(1) primary offence` | ccc17-sor.l4 |
| N176 | `s 490.011(1) the offence is one referred to in paragraphs (a) to (e) of the definition of primary offence` | ccc17-sor.l4 |
| N177 | `s 490.011(1) secondary offence (a) the provisions` | ccc17-sor.l4 |
| N178 | `s 490.011(1) secondary offence` | ccc17-sor.l4 |
| N179 | `s 490.011(1) designated offence` | ccc17-sor.l4 |
| N180 | `s 490.011(1) crime of a sexual nature` | ccc17-sor.l4 |
| N181 | `s 490.011(1) database` | ccc17-sor.l4 |
| N182 | `s 490.011(1) Ontario Act` | ccc17-sor.l4 |
| N183 | `s 490.011(1) pardon` | ccc17-sor.l4 |
| N184 | `s 490.011(1) record suspension` | ccc17-sor.l4 |
| N185 | `s 490.011(1) registration centre` | ccc17-sor.l4 |
| N186 | `s 490.011(1) Review Board` | ccc17-sor.l4 |
| N187 | `s 490.011(1) verdict of not criminally responsible on account of mental disorder` | ccc17-sor.l4 |
| N188 | `s 490.011(2) the person is not included among those convicted of, or found not criminally responsible for, a designated offence` | ccc17-sor.l4 |
| N189 | `s 490.012(5) the court may make an order in respect of the offence` | ccc17-sor.l4 |
| N190 | `s 490.012(1) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` | ccc17-sor.l4 |
| N191 | `s 490.012(2) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` | ccc17-sor.l4 |
| N192 | `s 490.012(3) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` | ccc17-sor.l4 |
| N193 | `s 490.012(4) the court shall consider the factor in determining whether to make an order under subsection (3)` | ccc17-sor.l4 |
| N194 | `s 490.013(1) the day on which the order begins` | ccc17-sor.l4 |
| N195 | `s 490.013(2) the duration of an order made under subsection 490.012(1) or (3) apart from subsections (3) and (5)` | ccc17-sor.l4 |
| N196 | `s 490.013(3) an order made under subsection 490.012(1) or (3) applies for life` | ccc17-sor.l4 |
| N197 | `s 490.013(4) the duration of the order when the court is not satisfied as set out in paragraph (3)(b)` | ccc17-sor.l4 |
| N198 | `s 490.013(5) an order made under subsection 490.012(1) or (3) applies for life` | ccc17-sor.l4 |
| N199 | `s 490.013(6) an order made under subsection 490.012(2) applies for life` | ccc17-sor.l4 |
| N200 | `s 490.013 the duration of the order` | ccc17-sor.l4 |
| N201 | `s 490.013(2) the day on which the order ends` | ccc17-sor.l4 |
| N202 | `s 490.0131 what the court shall do` | ccc17-sor.l4 |
| N203 | `s 490.0132(a) the court shall set a date for a hearing within 90 days` | ccc17-sor.l4 |
| N204 | `s 490.0132(b) the court retains jurisdiction over the matter` | ccc17-sor.l4 |
| N205 | `s 490.0132(c) the court may require the person to appear at the hearing by videoconference` | ccc17-sor.l4 |
| N206 | `s 490.0132(d) the court may issue a summons in Form 6.3 to compel the attendance of the person at the hearing` | ccc17-sor.l4 |
| N207 | `s 490.0132(a) the last day for the court to set a date for the hearing` | ccc17-sor.l4 |
| N208 | `s 490.0132(a) the court set the date within 90 days` | ccc17-sor.l4 |
| N209 | `s 490.0132(a) the court must set a date for the hearing` | ccc17-sor.l4 |
| N210 | `s 490.014 the person may appeal from the decision of the court` | ccc17-sor.l4 |
| N211 | `s 490.014 the appeal court may make the disposition` | ccc17-sor.l4 |
| N212 | `s 490.015(1) the person may apply for a termination order` | ccc17-sor.l4 |
| N213 | `s 490.015(1) the earliest day on which the person may apply for a termination order` | ccc17-sor.l4 |
| N214 | `s 490.015(2) the person subject to more than one order may apply for a termination order` | ccc17-sor.l4 |
| N215 | `s 490.015(3) the person may apply for a termination order despite subsections (1) and (2)` | ccc17-sor.l4 |
| N216 | `s 490.015(4) the application shall also be in relation to the obligation` | ccc17-sor.l4 |
| N217 | `s 490.015(4) the application shall be in relation to every order that is in effect` | ccc17-sor.l4 |
| N218 | `s 490.015(5) the person may re-apply for a termination order` | ccc17-sor.l4 |
| N219 | `s 490.015(6) the court to which the application shall be made` | ccc17-sor.l4 |
| N220 | `s 490.016(1) the court shall make a termination order` | ccc17-sor.l4 |
| N221 | `s 490.016(1.1) the court shall consider the factor in determining whether to make the termination order` | ccc17-sor.l4 |
| N222 | `s 490.016(2) the court shall give reasons for its decision` | ccc17-sor.l4 |
| N223 | `s 490.016(3) the court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision` | ccc17-sor.l4 |
| N224 | `s 490.017(1) the person may appeal from the decision made under subsection 490.016(1)` | ccc17-sor.l4 |
| N225 | `s 490.017(1) the appeal court may make the disposition` | ccc17-sor.l4 |
| N226 | `s 490.017(2) the appeal court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision` | ccc17-sor.l4 |
| N227 | `s 490.018(1) the court shall cause the thing to be done` | ccc17-sor.l4 |
| N228 | `s 490.018(2) the person who is subject to the order shall endorse the order` | ccc17-sor.l4 |
| N229 | `s 490.018(3) the Review Board shall cause a copy of the order to be given to the person` | ccc17-sor.l4 |
| N230 | `s 490.018(4) the earliest day on which the person in charge shall give the person a copy of the order` | ccc17-sor.l4 |
| N231 | `s 490.018(4) the person in charge shall give the person a copy of the order on the day` | ccc17-sor.l4 |
| N232 | `s 490.019 the person shall comply with the Sex Offender Information Registration Act` | ccc17-sor.l4 |
| N233 | `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force` | ccc17-sor.l4 |
| N234 | `s 487.092(1) the justice may issue a warrant in writing authorizing a peace officer to obtain a print or impression of the body of the person` | ccc17-warrants.l4 |
| N235 | `s 487.092(2) the warrant shall contain the term or condition` | ccc17-warrants.l4 |
| N236 | `s 487.092(3) the warrant may be executed by the peace officer at the place` | ccc17-warrants.l4 |
| N237 | `s 487.093(1) the warrants` | ccc17-warrants.l4 |
| N238 | `s 487.093(1) what the person executing the warrant shall do during the execution` | ccc17-warrants.l4 |
| N239 | `s 487.093(2) subsection (1) does not apply` | ccc17-warrants.l4 |
| N240 | `s 487.1(1) the provisions` | ccc17-warrants.l4 |
| N241 | `s 487.1(1)(o) the order is under one of sections 487.013 to 487.018` | ccc17-warrants.l4 |
| N242 | `s 487.1(1) the application may be submitted by a means of telecommunication` | ccc17-warrants.l4 |
| N243 | `s 487.1(2) the statement is deemed to be a statement made under oath` | ccc17-warrants.l4 |
| N244 | `s 487.1(3) the judicial officer shall certify the application as to time and date of receipt` | ccc17-warrants.l4 |
| N245 | `s 487.1(4) the application shall not be submitted by a means of telecommunication that does not produce a writing` | ccc17-warrants.l4 |
| N246 | `s 487.1(5) the applicant may submit the application by a means of telecommunication that does not produce a writing` | ccc17-warrants.l4 |
| N247 | `s 487.1(6) the application includes the statement of circumstances the subsection requires` | ccc17-warrants.l4 |
| N248 | `s 487.1(7) the oath may be administered by a means of telecommunication` | ccc17-warrants.l4 |
| N249 | `s 487.1(8) the judicial officer shall record the application verbatim and certify the record or a transcription of it as to time, date and contents` | ccc17-warrants.l4 |
| N250 | `s 487.1(9) the judicial officer is barred from issuing the warrant, order, extension or authorization` | ccc17-warrants.l4 |
| N251 | `s 487.1(10) the steps that follow when the judicial officer issues the document by a means of telecommunication` | ccc17-warrants.l4 |
| N252 | `s 487.1(11) judicial officer` | ccc17-warrants.l4 |
| N253 | `s 487.1(11) public officer` | ccc17-warrants.l4 |
| N254 | `s 487.11 the officer may exercise the powers described in subsection 487(1) or 492.1(1) without a warrant` | ccc17-warrants.l4 |
| N255 | `s 487.2 the person is guilty of an offence punishable on summary conviction` | ccc17-warrants.l4 |
| N256 | `s 487.2 the punishments` | ccc17-warrants.l4 |
| N257 | `s 487.3(1) the justice or judge may make an order prohibiting access to, and the disclosure of, any information relating to the warrant, order or authorization` | ccc17-warrants.l4 |
| N258 | `s 487.3(2) the ground is one on which an order under subsection (1) may be made` | ccc17-warrants.l4 |
| N259 | `s 487.3(3) all documents relating to the application shall be placed in a packet, sealed and kept in the custody of the court` | ccc17-warrants.l4 |
| N260 | `s 487.3(4) the application to terminate the order or vary its terms and conditions may be made to the judge` | ccc17-warrants.l4 |
| N261 | `s 488 the warrant shall be executed by day` | ccc17-warrants.l4 |
| N262 | `s 488 the warrant may be executed at the time of day` | ccc17-warrants.l4 |

## Fork register (ccc17)

Every place where the text can be read two or more ways with different outcomes, the reading taken, the other reading, and the text that licenses each.
A coverage row with disposition `fork` points here by its tag (F1 to F14, G1) and at the rule that encodes the reading taken (the index in the Coverage section).
Where the text does not choose, the rule answers `NOTHING` and the row says so.

### The rulings this register applies, word for word

- **A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).
- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

### Forks taken (F1 to F14)

**F1. A grant named "may" that the text makes depend on a stated condition ("if", "where", "once", "on application of", "who ... is satisfied that"): a failed condition answers `NOTHING`.**
27 functions, listed below; every function of the range whose name contains "may", "permitted", "power" or "authoris/authoriz" and that has a `NOTHING` branch was read for this, and each one whose text carries such a conditional word is tagged.
A grant whose only limit is a scope, with no conditional word (who may use it, in what place, over which thing: for example `s 487.0551(2)` "by a peace officer who has jurisdiction in that place or over the person", or `s 489(1)` "any thing that the person believes on reasonable grounds") answers `NOTHING` under the periods ruling (c) and the guide's "In short" sentence with no other reading, so it has no fork line; those branches are in the generated table of marginal readings as "limited by its own wording".
Reading taken: `NOTHING` (ruling of 2026-11-12, limit (1): the guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit").
Other reading: `JUST FALSE`, a failed "if" read as the text's own no (reading (a)); no function of this range answers `JUST FALSE` on such a gate in the files as they stand (the name-test sweep below checked every function named for a grant).
Four members, `s 488.1(4)(b)`, `s 490.01(a)`, `s 490.01(b)` and `s 490.015(3)`, are led by "where" or "once" rather than "if"; the periods ruling (b) and the 2026-11-05 delegated ruling (c) point to `JUST FALSE` for a "where" or "when" that fails, so their other reading is `JUST FALSE` on both counts.
They are not in group G1 below, because G1 lists only the functions that answer `JUST FALSE`.
Three members, `s 487.053(2)(c)`, `s 487.055(3.01)` and `s 490.0132(c)`, also carry a second gate, "as long as", answer `JUST FALSE` when that one fails, and so are in G1 as well.

**F2. The seam names for ss 487.051(1) and (2) are finer than PLAN.md's.**
Subsection (1) turns on paragraphs (a) and (c.02) of the definition of "primary designated offence" in s 487.04; subsection (2) turns on the other paragraphs ((a.1) to (c.01) and (c.03) to (d)); subsection (3) turns on "designated offence when the finding is made" and "secondary designated offence".
Reading taken: one input per paragraph group, each `MAYBE BOOLEAN`, so that `JUST FALSE` from ccc16 reads "not within these paragraphs" and `NOTHING` reads "ccc16 does not say".
Other reading: PLAN.md's single input `s 487.04 the offence is a primary designated offence`, which cannot tell (1) from (2).

**F3. `s 487.0552(2)`, "For greater certainty, a lawful command that prevents a person from complying with an order or summons is a reasonable excuse if, at the time, the person is subject to the Code of Service Discipline".**
Reading taken: `JUST TRUE` when the person is so subject, `JUST FALSE` otherwise (the text's "if", reading (a)); the function is named for the rule, not for a grant or a power.
Other reading: `NOTHING` when not so subject, because "for greater certainty" says that this command IS an excuse and does not say that no other command is.

**F4. `s 487.056(6)`: who must have jurisdiction, and who must be able.**
Text: "a peace officer who has jurisdiction over the person or in the place in which the samples are taken -- or a person acting under their direction -- who is able, by virtue of training or experience, to take them".
Reading taken: the peace officer must have jurisdiction (over the person or in the place), and whoever actually takes the samples (the officer or the person acting under direction) must be able by training or experience; anyone else taking them gives `JUST FALSE` (the text names only these two).
Other reading: both clauses attach to the person actually taking them, so a person acting under direction would also need jurisdiction.

**F5. How a year is counted.**
The text does not say whether the day of the event counts, and the Interpretation Act is not among the sources.
Reading taken: a year after a day is the same date a year later (`add years`); an anniversary that does not exist (29 February) is carried to 28 February by the library function.
Other readings: the day before the anniversary; 1 March (the roll-forward of `Date 29 2 2023`).
Functions: `s 487.09(1)`, `s 487.09(1)(c) the day on which one year after the event expires`, `s 490(3) the last day on which the thing may be detained without a judge's order`, `s 490.013(2) the day on which the order ends`, `s 490.015(1)`, `s 490.015(2)`, `s 490.015(5)`.

**F6. `s 487.3(4)`: who may apply to terminate or vary a non-disclosure order.**
The subsection names the judges to whom the application may be made but not who may apply.
Reading taken: the function answers the forum only (which judge), and asks nothing about the applicant; other reading: the person who sought the order, or any person affected.

**F7. A stated period on a grant: `s 488.02(3)` ("within 10 days of receiving the notice") and `s 488.1(3)(a)` ("within fourteen days from the day the document was so placed in custody", "on two days notice of motion").**
Reading taken: outside the period the answer is `JUST FALSE` (periods ruling of 2026-11-05, (a): a period the text fixes in its own words).
Other reading: `NOTHING`, because the brief's list of what limits a grant "in its own wording" includes "a stated period". Both functions are also rows of group G1 below.

**F8. `s 488.1(1)` "lawyer": the territories.**
Reading taken: the definition answers `JUST TRUE` for an advocate, lawyer or notary in Quebec and a barrister or solicitor in another province, `JUST FALSE` for any other description in a province (the definition says "means"), and `NOTHING` for a territory (Yukon, Northwest Territories, Nunavut): the text names provinces only.
Other reading: `JUST FALSE` for a territory, if "any other province" is read as exhaustive.

**F9. `s 490(9)(c)` and `(d)`: a thing seized when it was not in anyone's possession, with a lawful owner known.**
Reading taken: neither paragraph reaches it; the function answers `NOTHING` (silent).
Other reading: paragraph (d) reaches it as an unlawful-possession case.

**F10. `s 490.015(1)` and `(2)`: a grant gated by "if N years have elapsed".**
Reading taken: before the period has run the answer is `NOTHING` (ruling of 2026-11-12, limit (1): a "may" gated by "if").
Other reading: `JUST FALSE`, a period the text fixes in its own words (periods ruling of 2026-11-05, (a)).

**F11. `s 490.012(1)`: a duty ("shall make an order") gated by "if" (a), (b) and (c).**
Reading taken: `JUST FALSE` when the offence was not prosecuted by indictment, the term is under two years (24 months), or the victim was 18 or over (a failed "if" on a duty: reading (a)); `NOTHING` when the court is not sentencing or the offence is not a designated offence.
Other reading: `NOTHING` on every failed "if" (a duty that does not arise is simply not covered).

**F12. `s 490.012(3)`: whether (1) or (2) applying defeats (3) for a verdict of not criminally responsible.**
Reading taken: for a sentence, (3) applies only when neither (1) nor (2) applies; for a verdict of not criminally responsible, (3) applies whatever (1) and (2) say, because the verdict is a separate limb ("or when the court renders a verdict").
Other reading: (3) never applies when (1) or (2) applies.

**F13. `s 490.013(2)`: a maximum term of imprisonment other than 2, 5, 10, 14 years or life.**
Reading taken: `NOTHING` (silent).
Other reading: the nearest listed term.

**F14. `s 487.05(4)` and `s 487.092(3)`: a grant ("may be executed at any place in Canada") followed by a bare "must".**
Text: "Any peace officer who executes the warrant must have authority to act as a peace officer in the place where it is executed."
Reading taken: `JUST FALSE` where the peace officer lacks that authority (a flat requirement the text states in its own words; kept under test 2 of the name-test sweep), `NOTHING` where the place is not in Canada (the grant does not reach it).
Other reading: `NOTHING` where the officer lacks authority, a limit on a grant in its own wording (reading (b)). The functions are named "may be executed", so this is the one place where the sweep's "named for a grant" test and its "closed by the text" test point in different directions.

The 27 functions of F1 (all answer `NOTHING` on a failed condition in the files as they stand; none was flipped by the sweep of 2026-11-12):

- `s 487.05(1) the provincial court judge may issue a warrant in Form 5.02` (N1, ccc17-dna-orders.l4)
- `s 487.051(3) the court may make an order in Form 5.04` (N6, ccc17-dna-orders.l4)
- `s 487.053(2)(c) the court may require the person to appear by closed-circuit television or videoconference` (N13, ccc17-dna-orders.l4)
- `s 487.055(1) the provincial court judge may authorize in Form 5.06 the taking of samples of bodily substances` (N23, ccc17-dna-orders.l4)
- `s 487.055(3.01) the court may require the person to appear by closed-circuit television or videoconference` (N26, ccc17-dna-orders.l4)
- `s 487.0551(1) a justice of the peace may issue a warrant for the arrest of the person in Form 5.062` (N32, ccc17-dna-orders.l4)
- `s 487.09(2) the provincial court judge may order that the bodily substances and the results not be destroyed during the period considered appropriate` (N73, ccc17-dna-samples.l4)
- `s 487.091(1) the provincial court judge may authorize in Form 5.09 the taking of additional samples of bodily substances` (N75, ccc17-dna-samples.l4)
- `s 488.01(6) the judge may order that some or all documents obtained are to be dealt with in accordance with section 488.02` (N96, ccc17-journalists.l4)
- `s 488.01(10) the judge may make the order` (N101, ccc17-journalists.l4)
- `s 488.02(6) the judge may examine the document` (N108, ccc17-journalists.l4)
- `s 488.1(3)(c) the person may apply at the appointed time and place for an order determining the question` (N122, ccc17-privilege.l4)
- `s 488.1(4)(a) the judge may inspect the document` (N123, ccc17-privilege.l4)
- `s 488.1(4)(b) the judge may allow the Attorney General to inspect the document` (N124, ccc17-privilege.l4)
- `s 488.1(9) the judge may authorize the person to examine the document or make a copy of it in the presence of the custodian or the judge` (N132, ccc17-privilege.l4)
- `s 490(3.1) the thing may be detained for the period` (N146, ccc17-seizure.l4)
- `s 490(9) the judge or justice may order the thing forfeited to Her Majesty, to be disposed of as the Attorney General directs or otherwise dealt with in accordance with the law` (N154, ccc17-seizure.l4)
- `s 490(9.1) the judge or justice may order that the thing continue to be detained for such period as the judge or justice considers necessary` (N155, ccc17-seizure.l4)
- `s 490.01(a) the person may return the thing to its lawful owner or the person lawfully entitled to possession of it` (N167, ccc17-seizure.l4)
- `s 490.01(b) the person may dispose of the thing, or destroy it` (N168, ccc17-seizure.l4)
- `s 490.0132(c) the court may require the person to appear at the hearing by videoconference` (N205, ccc17-sor.l4)
- `s 490.0132(d) the court may issue a summons in Form 6.3 to compel the attendance of the person at the hearing` (N206, ccc17-sor.l4)
- `s 490.015(3) the person may apply for a termination order despite subsections (1) and (2)` (N215, ccc17-sor.l4)
- `s 487.092(1) the justice may issue a warrant in writing authorizing a peace officer to obtain a print or impression of the body of the person` (N234, ccc17-warrants.l4)
- `s 487.1(1) the application may be submitted by a means of telecommunication` (N242, ccc17-warrants.l4)
- `s 487.11 the officer may exercise the powers described in subsection 487(1) or 492.1(1) without a warrant` (N254, ccc17-warrants.l4)
- `s 487.3(1) the justice or judge may make an order prohibiting access to, and the disclosure of, any information relating to the warrant, order or authorization` (N257, ccc17-warrants.l4)

### Group G1: "may" functions gated by "where", "when", "upon" or an equivalent (listed, not decided)

Ruling (b) of the periods paragraph (and (c) of the 2026-11-05 delegated ruling, which makes "when", "upon" and "whenever" count as "where") says `JUST FALSE` when such a gate fails; the guide's line on grants says `NOTHING`.
That is a question for the maintainer or a lawyer, so these functions are LISTED here and left answering `JUST FALSE`, as the brief says (limit (3) of the 2026-11-12 ruling).
Assumed, not ruled: "so long as", "as long as", "while", "after ...", "on ...", a stated period and a stated period of notice are equivalent conditions of that kind and go with the group (`name-test-sweep.md`, test 3(i)).
The other reading of every row is `NOTHING`.
Count: **12** functions.

| # | function (index) | gate | the gate's words | reading taken | other reading |
| --- | --- | --- | --- | --- | --- |
| 1 | `s 487.051(4) the court may make an order in Form 5.041 requiring the person to report and submit to the taking of the samples` (N9) | when | "When the court makes an order authorizing the taking of samples of bodily substances" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 2 | `s 487.053(1) the court may make an order under section 487.051 at this time` (N10) | when | "when it imposes a sentence on a person, finds the person not criminally responsible on account of mental disorder or directs that they be discharged under section 730" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 3 | `s 487.053(2)(c) the court may require the person to appear by closed-circuit television or videoconference` (N13) | as long as | "as long as the person is given the opportunity to communicate privately with counsel if they are represented by counsel" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 4 | `s 487.055(3.01) the court may require the person to appear by closed-circuit television or videoconference` (N26) | as long as | "as long as the person is given the opportunity to communicate privately with counsel if they are represented by counsel" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 5 | `s 490.0132(c) the court may require the person to appear at the hearing by videoconference` (N205) | as long as | "as long as the person is given the opportunity to communicate privately with counsel if they are represented by counsel" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 6 | `s 488.02(3) the journalist or media outlet may apply to a judge of the court that issued the warrant, authorization or order for an order that the document is not to be disclosed to an officer` (N104) | period (also F7) | "may, within 10 days of receiving the notice referred to in subsection (2), apply" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 7 | `s 488.1(3)(a) the person may apply to a judge for an order appointing a place and a day for the determination of the question and requiring the custodian to produce the document` (N117) | period and notice (also F7) | "within fourteen days from the day the document was so placed in custody"; "on two days notice of motion to all other persons entitled to make application" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 8 | `s 488.1(7) subsequent applications under paragraph (3)(c) may be made to another judge` (N130) | where | "Where the judge to whom an application has been made under paragraph (3)(c) cannot act or continue to act under this section for any reason" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 9 | `s 490(7) the person from whom anything has been seized may apply summarily for an order under paragraph (9)(c) that the thing be returned` (N151) | after, and notice | "may, after the expiration of the periods of detention provided for or ordered under subsections (1) to (3)"; "on three clear days notice to the Attorney General" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 10 | `s 490(8) the judge or justice may allow an application under subsection (7) to be made before the expiration of the periods` (N152) | where | "where he is satisfied that hardship will result unless the application is so allowed" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 11 | `s 490(10) the claimant may at any time apply summarily for an order that the thing detained be returned to the applicant` (N156) | notice | "on three clear days notice to the Attorney General and the person from whom the thing was seized" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |
| 12 | `s 490(15) the judge may order that the person be permitted to examine anything so detained` (N163) | where, on, after | "Where anything is detained pursuant to subsections (1) to (3.1)"; "on summary application on behalf of a person who has an interest in what is detained"; "after three clear days notice to the Attorney General" | `JUST FALSE` when the gate fails (periods ruling (b), (c)) | `NOTHING` (limited by its own wording) |

### Group G2: functions named for an "entitled" claim (listed, not decided)

Count: **0**.
The word "entitled" occurs in this range only inside phrases such as "lawfully entitled to possession" (for example in ss 489.1(1), 490(1), 490(9) and 490.01), which are facts asked of the person; no function is named for an entitlement.

### Sites decided case by case (the maintainer, typed 2026-11-05T10:25:24Z)

The ruling leaves six kinds of site to the encoder's judgment and asks for one fork line per site.
Those that occur in this range are generated below, one line per function, from the `FALSE-kind` tags (the tag's quoted words decide the kind): an "unless" or "except" once it is met; a bare "must" or "shall" not done; a duty whose "if" or "where" is unmet; "(other than X)".
The other two kinds ("listed in Schedule N", a missing event in the state ledger) do not occur in this range.
The answer taken at every site is `JUST FALSE` where the text itself introduces the gate or the exception, quoted in the tag; the other reading at every site is `NOTHING`.
A human reviewer may overrule any line.

| # | function (index) | kind of site | the text's words (first branch) | answer taken | other reading |
| --- | --- | --- | --- | --- | --- |
| 1 | `s 487.05(4) the warrant may be executed by the peace officer at the place` (N3) | a bare "must" or "shall" not done | "must have authority to act as a peace officer in the place where it is executed" | `JUST FALSE` | `NOTHING` |
| 2 | `s 487.051(1) the court shall make an order in Form 5.03` (N4) | an "if" unmet | "if that offence is a primary designated offence within the meaning of paragraphs (a) and (..." | `JUST FALSE` | `NOTHING` |
| 3 | `s 487.051(2) the court shall make an order in Form 5.03` (N5) | an "if" unmet | "if that offence is a primary designated offence within the meaning of any of paragraphs (a..." | `JUST FALSE` | `NOTHING` |
| 4 | `s 487.053(2)(a) the court shall set a date for a hearing within 90 days` (N11) | an "if" unmet | "If the court does not consider the matter at that time" | `JUST FALSE` | `NOTHING` |
| 5 | `s 487.053(2)(b) the court retains jurisdiction over the matter` (N12) | an "if" unmet | "If the court does not consider the matter at that time" | `JUST FALSE` | `NOTHING` |
| 6 | `s 487.055(2) the application is accompanied by the certificate` (N24) | a bare "must" or "shall" not done | "The application shall be accompanied by a certificate referred to in paragraph 667(1)(a) t..." | `JUST FALSE` | `NOTHING` |
| 7 | `s 487.055(3.11) the court shall make an order in Form 5.041 requiring the person to report and submit to the taking of the samples` (N29) | an "if" unmet | "If the court authorizes the taking of samples of bodily substances from a person who is on..." | `JUST FALSE` | `NOTHING` |
| 8 | `s 487.055(4) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples` (N30) | an "if" unmet | "if a person who is on conditional release has not appeared at the hearing" | `JUST FALSE` | `NOTHING` |
| 9 | `s 487.055(5) the summons is served as the subsection requires` (N31) | a bare "must" or "shall" not done | "The summons shall be accompanied by a copy of the authorization" | `JUST FALSE` | `NOTHING` |
| 10 | `s 487.055(5) the summons is served as the subsection requires` (N31) | an "if" unmet | "shall either deliver it personally to the person to whom it is directed or, if that person..." | `JUST FALSE` | `NOTHING` |
| 11 | `s 487.0551(2) the warrant remains in force` (N34) | a "where", "when", "until" or period unmet | "The warrant remains in force until it is executed." | `JUST FALSE` | `NOTHING` |
| 12 | `s 487.0552(2) a lawful command that prevents the person from complying is a reasonable excuse` (N37) | an "if" unmet | "is a reasonable excuse if, at the time, the person is subject to the Code of Service Disci..." | `JUST FALSE` | `NOTHING` |
| 13 | `s 487.056(6) the samples are taken by a person the subsection permits` (N43) | a bare "must" or "shall" not done | "The samples shall be taken by a peace officer who has jurisdiction over the person or in t..." | `JUST FALSE` | `NOTHING` |
| 14 | `s 487.057(3) the peace officer shall send a copy of the report to the other peace officer` (N47) | an "unless" or "except" once met | "unless that other peace officer had jurisdiction to take the samples" | `JUST FALSE` | `NOTHING` |
| 15 | `s 487.07(1) the peace officer shall inform the person of the matter before taking the samples` (N52) | an "if" unmet | "if the sample is taken from a young person, the rights of the young person under subsectio..." | `JUST FALSE` | `NOTHING` |
| 16 | `s 487.07(5) the young person’s waiver of the rights under subsection (4) is valid` (N58) | a bare "must" or "shall" not done | "any such waiver (a) must be recorded on audio tape or video tape or otherwise; or (b) must..." | `JUST FALSE` | `NOTHING` |
| 17 | `s 487.071(2) the peace officer shall not take any bodily substances from the person` (N60) | an "if" unmet | "If the person’s DNA profile is in the convicted offenders index of the national DNA data b..." | `JUST FALSE` | `NOTHING` |
| 18 | `s 487.071(2) the peace officer shall confirm in writing on the order or authorization that they have been advised that the profile is in the data bank and transmit a copy to the Commissioner of the Royal Canadian Mounted Police` (N61) | an "if" unmet | "If the person’s DNA profile is in the convicted offenders index of the national DNA data b..." | `JUST FALSE` | `NOTHING` |
| 19 | `s 487.071(3) the peace officer shall execute the order or authorization and transmit the bodily substances taken and a copy to the Commissioner of the Royal Canadian Mounted Police` (N62) | an "if" unmet | "If the person’s DNA profile is not in the convicted offenders index of the national DNA da..." | `JUST FALSE` | `NOTHING` |
| 20 | `s 487.08(1) the use of the bodily substances is barred` (N63) | an "unless" or "except" once met | "except to use them for the purpose of forensic DNA analysis in the course of an investigat..." | `JUST FALSE` | `NOTHING` |
| 21 | `s 487.08(1.1) the use of the bodily substances is barred` (N64) | an "unless" or "except" once met | "except to transmit them to the Commissioner of the Royal Canadian Mounted Police for the p..." | `JUST FALSE` | `NOTHING` |
| 22 | `s 487.08(2) the use of the results of forensic DNA analysis is barred` (N65) | an "unless" or "except" once met | "except (a) in the course of an investigation of the designated offence or any other design..." | `JUST FALSE` | `NOTHING` |
| 23 | `s 487.09(1) the bodily substances and the results of forensic DNA analysis shall be destroyed without delay` (N70) | a "where", "when", "until" or period unmet | "the expiration of one year after" | `JUST FALSE` | `NOTHING` |
| 24 | `s 487.09(1) the bodily substances and the results of forensic DNA analysis shall be destroyed without delay` (N70) | an "unless" or "except" once met | "unless during that year a new information is laid or an indictment is preferred charging t..." | `JUST FALSE` | `NOTHING` |
| 25 | `s 487.09(3) the voluntarily given bodily substances and the results shall be destroyed without delay` (N74) | a "where", "when", "until" or period unmet | "without delay after the results of that analysis establish that the bodily substance refer..." | `JUST FALSE` | `NOTHING` |
| 26 | `s 487.091(2) the application states the reasons the subsection requires` (N76) | a bare "must" or "shall" not done | "The application shall state the reasons why a DNA profile cannot be derived" | `JUST FALSE` | `NOTHING` |
| 27 | `s 487.091(3) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples` (N77) | an "if" unmet | "If the court authorizes the taking of samples of bodily substances from a person who is no..." | `JUST FALSE` | `NOTHING` |
| 28 | `s 487.0911(2) the Attorney General shall apply ex parte to have the order or authorization corrected` (N80) | an "if" unmet | "If the Attorney General is of the opinion that the defect is due to a clerical error" | `JUST FALSE` | `NOTHING` |
| 29 | `s 487.0911(2)(b) the Attorney General shall transmit a copy of the corrected order or authorization to the Commissioner` (N81) | an "if" unmet | "transmit a copy of the corrected order or authorization, if any" | `JUST FALSE` | `NOTHING` |
| 30 | `s 487.0911(3) the Attorney General shall inform the Commissioner of the opinion that the offence is not a designated offence` (N82) | an "if" unmet | "If the Attorney General is of the opinion that the offence referred to in the order or aut..." | `JUST FALSE` | `NOTHING` |
| 31 | `s 487.0911(4) the Attorney General shall transmit the opinion, with written reasons, to the Commissioner` (N83) | an "if" unmet | "If the Attorney General is of the opinion that the offence referred to in the order or aut..." | `JUST FALSE` | `NOTHING` |
| 32 | `s 488.01(2) the applicant shall make the application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552` (N90) | an "if" unmet | "if an applicant for a warrant under section 487.01, 492.1 or 492.2, a search warrant under..." | `JUST FALSE` | `NOTHING` |
| 33 | `s 488.01(9) the officer shall, as soon as possible, make an ex parte application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552` (N99) | an "if" unmet | "If an officer, acting under a warrant, authorization or order referred to in subsection (2..." | `JUST FALSE` | `NOTHING` |
| 34 | `s 488.01(9) until the judge disposes of the application the officer shall refrain from examining or reproducing any document obtained and shall keep it in a sealed packet` (N100) | an "if" unmet | "If an officer, acting under a warrant, authorization or order referred to in subsection (2..." | `JUST FALSE` | `NOTHING` |
| 35 | `s 488.01(9) until the judge disposes of the application the officer shall refrain from examining or reproducing any document obtained and shall keep it in a sealed packet` (N100) | a "where", "when", "until" or period unmet | "until the judge disposes of the application" | `JUST FALSE` | `NOTHING` |
| 36 | `s 488.1(2) the officer shall, without examining or making copies of the document, seize it and place it in a package, suitably sealed and identified` (N115) | a "where", "when", "until" or period unmet | "Where an officer acting under the authority of this or any other Act of Parliament is abou..." | `JUST FALSE` | `NOTHING` |
| 37 | `s 488.1(5) the document remains privileged and inadmissible as evidence` (N128) | an "unless" or "except" once met | "unless the client consents to its admission in evidence or the privilege is otherwise lost" | `JUST FALSE` | `NOTHING` |
| 38 | `s 488.1(6) the judge shall order the custodian to deliver the document to the officer who seized it or to some other person designated by the Attorney General` (N129) | a "where", "when", "until" or period unmet | "Where a document has been seized and placed in custody under subsection (2) and a judge, o..." | `JUST FALSE` | `NOTHING` |
| 39 | `s 489.1(4) section 489.1 does not apply to the thing` (N140) | "(other than X)" | "other than virtual currency or other digital assets" | `JUST FALSE` | `NOTHING` |
| 40 | `s 490(2) the section bars detaining the thing for more than 180 days after the day of the seizure` (N142) | an "unless" or "except" once met | "unless (a) a justice, on the making of a summary application to him after three clear days..." | `JUST FALSE` | `NOTHING` |
| 41 | `s 490(3) the section bars detaining the thing for more than one year from the day of the seizure` (N144) | an "unless" or "except" once met | "unless (a) a judge of a superior court of criminal jurisdiction or a judge as defined in s..." | `JUST FALSE` | `NOTHING` |
| 42 | `s 490(4) the justice shall forward anything detained to the clerk of the court to which the accused has been ordered to stand trial` (N147) | a "where", "when", "until" or period unmet | "When an accused has been ordered to stand trial" | `JUST FALSE` | `NOTHING` |
| 43 | `s 490(5) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9)` (N149) | a "where", "when", "until" or period unmet | "Where at any time before the expiration of the periods of detention provided for or ordere..." | `JUST FALSE` | `NOTHING` |
| 44 | `s 490(6) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9) or (9.1)` (N150) | a "where", "when", "until" or period unmet | "Where the periods of detention provided for or ordered under subsections (1) to (3) in res..." | `JUST FALSE` | `NOTHING` |
| 45 | `s 490(9) the order the judge or justice shall make` (N153) | an "if" unmet | "(d) if possession of it by the person from whom it was seized is unlawful and the lawful o..." | `JUST FALSE` | `NOTHING` |
| 46 | `s 490(11) the order the judge or justice shall make on the application under subsection (10)` (N157) | a "where", "when", "until" or period unmet | "where a judge or justice is satisfied that (a) the applicant is the lawful owner or lawful..." | `JUST FALSE` | `NOTHING` |
| 47 | `s 490.011(2) the person is not included among those convicted of, or found not criminally responsible for, a designated offence` (N188) | an "unless" or "except" once met | "unless they are given an adult sentence within the meaning of that subsection for the offe..." | `JUST FALSE` | `NOTHING` |
| 48 | `s 490.012(1) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` (N190) | an "if" unmet | "A court shall make an order under any of subsections (1) to (3) in respect of a secondary ..." | `JUST FALSE` | `NOTHING` |
| 49 | `s 490.012(2) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` (N191) | an "if" unmet | "A court shall make an order under any of subsections (1) to (3) in respect of a secondary ..." | `JUST FALSE` | `NOTHING` |
| 50 | `s 490.012(3) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` (N192) | an "if" unmet | "A court shall make an order under any of subsections (1) to (3) in respect of a secondary ..." | `JUST FALSE` | `NOTHING` |
| 51 | `s 490.012(3) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` (N192) | an "unless" or "except" once met | "unless the court is satisfied the person has established that" | `JUST FALSE` | `NOTHING` |
| 52 | `s 490.013(3) an order made under subsection 490.012(1) or (3) applies for life` (N196) | an "if" unmet | "applies for life if (a) in the same proceeding, the person has been convicted of" | `JUST FALSE` | `NOTHING` |
| 53 | `s 490.013(5) an order made under subsection 490.012(1) or (3) applies for life` (N198) | an "if" unmet | "applies for life if the person (a) was previously convicted of" | `JUST FALSE` | `NOTHING` |
| 54 | `s 490.0132(a) the court shall set a date for a hearing within 90 days` (N203) | an "if" unmet | "If the court does not consider the matter under any of subsections 490.012(1) to (3) at th..." | `JUST FALSE` | `NOTHING` |
| 55 | `s 490.0132(b) the court retains jurisdiction over the matter` (N204) | an "if" unmet | "If the court does not consider the matter under any of subsections 490.012(1) to (3) at th..." | `JUST FALSE` | `NOTHING` |
| 56 | `s 490.015(4) the application shall also be in relation to the obligation` (N216) | an "if" unmet | "If a person is subject to an obligation under section 490.019 or 490.02901" | `JUST FALSE` | `NOTHING` |
| 57 | `s 490.016(1) the court shall make a termination order` (N220) | an "if" unmet | "The court shall make a termination order if it is satisfied that the person has establishe..." | `JUST FALSE` | `NOTHING` |
| 58 | `s 490.016(3) the court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision` (N223) | an "if" unmet | "If the court makes a termination order, it shall cause the Commissioner of the Royal Canad..." | `JUST FALSE` | `NOTHING` |
| 59 | `s 490.017(2) the appeal court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision` (N226) | an "if" unmet | "If the appeal court makes an order that may be made under subsection 490.016(1)" | `JUST FALSE` | `NOTHING` |
| 60 | `s 490.018(1) the court shall cause the thing to be done` (N227) | an "if" unmet | "the Review Board that is responsible for making a disposition with respect to that person,..." | `JUST FALSE` | `NOTHING` |
| 61 | `s 490.018(2) the person who is subject to the order shall endorse the order` (N228) | a "where", "when", "until" or period unmet | "After paragraphs (1)(a) to (c) have been complied with" | `JUST FALSE` | `NOTHING` |
| 62 | `s 490.018(3) the Review Board shall cause a copy of the order to be given to the person` (N229) | an "unless" or "except" once met | "unless the conditions restrict the person’s liberty in a manner and to an extent that prev..." | `JUST FALSE` | `NOTHING` |
| 63 | `s 490.018(4) the person in charge shall give the person a copy of the order on the day` (N231) | a bare "must" or "shall" not done | "before their release or discharge shall give the person a copy of the order" | `JUST FALSE` | `NOTHING` |
| 64 | `s 490.019 the person shall comply with the Sex Offender Information Registration Act` (N232) | an "unless" or "except" once met | "unless a court makes an exemption order under subsection 490.023(2)" | `JUST FALSE` | `NOTHING` |
| 65 | `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force` (N233) | a "where", "when", "until" or period unmet | "ends 10 years after it was made if the offence in connection with which it was made was pr..." | `JUST FALSE` | `NOTHING` |
| 66 | `s 487.092(3) the warrant may be executed by the peace officer at the place` (N236) | a bare "must" or "shall" not done | "must have authority to act as a peace officer in the place where it is executed" | `JUST FALSE` | `NOTHING` |
| 67 | `s 487.1(6) the application includes the statement of circumstances the subsection requires` (N247) | a bare "must" or "shall" not done | "shall include a statement of the circumstances that make it impracticable" | `JUST FALSE` | `NOTHING` |
| 68 | `s 487.2 the person is guilty of an offence punishable on summary conviction` (N255) | an "unless" or "except" once met | "unless a charge has been laid in respect of any offence in relation to which the warrant w..." | `JUST FALSE` | `NOTHING` |
| 69 | `s 487.3(3) all documents relating to the application shall be placed in a packet, sealed and kept in the custody of the court` (N259) | a "where", "when", "until" or period unmet | "Where an order is made under subsection (1)" | `JUST FALSE` | `NOTHING` |
| 70 | `s 488 the warrant shall be executed by day` (N261) | an "unless" or "except" once met | "shall be executed by day, unless (a) the justice is satisfied that there are reasonable gr..." | `JUST FALSE` | `NOTHING` |
| 71 | `s 488 the warrant may be executed at the time of day` (N262) | an "unless" or "except" once met | "shall be executed by day, unless (a) the justice is satisfied that there are reasonable gr..." | `JUST FALSE` | `NOTHING` |

### Fork tags found in the code (generated)

| fork | count of rules tagged | rules (index) |
| --- | --- | --- |
| F1 | 27 | N1, N6, N13, N23, N26, N32, N73, N75, N96, N101, N108, N122, N123, N124, N132, N146, N154, N155, N167, N168, N205, N206, N215, N234, N242, N254, N257 |
| F10 | 2 | N212, N214 |
| F11 | 1 | N190 |
| F12 | 1 | N192 |
| F13 | 1 | N195 |
| F14 | 2 | N3, N236 |
| F2 | 2 | N4, N5 |
| F3 | 1 | N37 |
| F4 | 1 | N43 |
| F5 | 7 | N70, N71, N145, N201, N212, N214, N218 |
| F6 | 1 | N260 |
| F7 | 2 | N104, N117 |
| F8 | 1 | N113 |
| F9 | 1 | N153 |
| G1 | 12 | N9, N10, N13, N26, N104, N117, N130, N151, N152, N156, N163, N205 |

## Jural relations (ccc17)

One row per provision that creates a relation, from the `-- jural:` comment above each rule (generated by `work/coverage.py`). The first-named party holds the position in the last column (as the L4 rule's comment states it); the second-named party holds the correlative (right-duty, privilege-no-right, power-liability, immunity-disability). Provisions that create no relation (a definition, a counting rule, a table) are listed once as `none` below the table.

| section | first party | second party | first party's position | second party's correlative | L4 rule |
| --- | --- | --- | --- | --- | --- |
| 487.05(1) | a provincial court judge | the person from whom samples would be taken | power | liability | N1 |
| 487.05(2) | the person from whom samples would be taken | a provincial court judge | right | duty | N2 |
| 487.05(4) | a peace officer | the person named in the warrant | power | liability | N3 |
| 487.051(1) | the person convicted, discharged or found guilty | the court | liability | power | N4 |
| 487.051(2) | the person convicted, discharged or found guilty | the court | liability | power | N5 |
| 487.051(3) | the court | the person found not criminally responsible, or convicted of a secondary designated offence | power | liability | N6 |
| 487.051(3) closing words | the person concerned | the court | right | duty | N7 |
| 487.051(4) | the court | the person subject to the order | power | liability | N9 |
| 487.053(1) | the court | the person to be sentenced, found not criminally responsible or discharged | power | liability | N10 |
| 487.053(2) | the person concerned | the court | right | duty | N11 |
| 487.053(2)(b) | the person concerned | the court | right | duty | N12 |
| 487.053(2)(c) | the court | the person concerned | power | liability | N13 |
| 487.054 | the offender or the prosecutor | the court of appeal | power | liability | N17 |
| 487.055(1) | a provincial court judge | a person who, before June 30, 2000, had been declared a dangerous offender or convicted of murder, manslaughter or a sexual offence | power | liability | N23 |
| 487.055(2) | the person concerned | the applicant | right | duty | N24 |
| 487.055(3.01) | the court | the person who wishes to appear at the hearing | power | liability | N26 |
| 487.055(3.1) | the person concerned | the court | right | duty | N27 |
| 487.055(3.11) | the person on conditional release | the court | right | duty | N29 |
| 487.055(4) | the person on conditional release who has not appeared | the court | liability | power | N30 |
| 487.055(5) | the person to be served | a peace officer | right | duty | N31 |
| 487.0551(1) | a justice of the peace | the person who failed to appear | power | liability | N32 |
| 487.0551(2) | a peace officer | the person named in the warrant | power | liability | N33 |
| 487.0552(1) | the state | the person who fails to comply | power | liability | N35 |
| 487.0552(2) | a person subject to the Code of Service Discipline | the court | immunity | disability | N37 |
| 487.056(1) | a peace officer | the person subject to the order | power | liability | N38 |
| 487.056(2) | a peace officer | the person subject to the authorization | power | liability | N39 |
| 487.056(3) | a peace officer | the person who failed to appear | power | liability | N40 |
| 487.056(4) | the person subject to the order | a peace officer | no-right | privilege | N41 |
| 487.056(5) | a peace officer | the person subject to the order or authorization | power | liability | N42 |
| 487.056(6) | the person subject to the order or authorization | the person who takes the samples | right | duty | N43 |
| 487.057(1) | the court that issued the instrument | a peace officer | right | duty | N44 |
| 487.057(2) | the court that receives the report | a peace officer | right | duty | N46 |
| 487.057(3) | a peace officer who requested the taking | a peace officer who took the samples | right | duty | N47 |
| 487.058 | a peace officer or a person acting under a peace officer’s direction | the person from whom the samples were taken | immunity | disability | N48 |
| 487.06(1) | a peace officer | the person from whom the samples are taken | power | liability | N49 |
| 487.06(2) | the person from whom the samples are taken | the provincial court judge or court | right | duty | N50 |
| 487.06(3) | a peace officer | the person from whom the samples are taken | power | liability | N51 |
| 487.07(1) | the person from whom the samples are to be taken | a peace officer | right | duty | N52 |
| 487.07(2) | a peace officer | the person from whom the samples are to be taken | power | liability | N53 |
| 487.07(2)(b) | a peace officer | the person from whom the samples are to be taken | power | liability | N54 |
| 487.07(3) | the person from whom the samples are taken | the person who takes the samples | right | duty | N55 |
| 487.07(4) | a young person against whom a warrant is executed | a peace officer | right | duty | N56 |
| 487.07(5) | a young person | a peace officer | power | liability | N58 |
| 487.071(1) | the person subject to the order or authorization | a peace officer | right | duty | N59 |
| 487.071(2) | the person whose profile is in the data bank | a peace officer | immunity | disability | N60 |
| 487.071(3) | a peace officer | the person subject to the order or authorization | power | liability | N62 |
| 487.08(1) | the person from whom the substances were taken | any person | immunity | disability | N63 |
| 487.08(1.1) | the person from whom the substances were taken | any person | immunity | disability | N64 |
| 487.08(2) | the person from whom the substances were taken | any person | immunity | disability | N65 |
| 487.08(3) | the state | a person who contravenes subsection (1) or (2) | power | liability | N66 |
| 487.08(4) | the state | a person who contravenes subsection (1.1) | power | liability | N68 |
| 487.09(1) | the person from whom the substances were taken | the person who holds them | right | duty | N70 |
| 487.09(2) | a provincial court judge | the person from whom the substances were taken | power | liability | N73 |
| 487.09(3) | the person who provided the substances voluntarily | the person who holds them | right | duty | N74 |
| 487.091(1) | a provincial court judge | the person from whom additional samples are needed | power | liability | N75 |
| 487.091(2) | the court | the applicant | right | duty | N76 |
| 487.091(3) | the person not in custody | the court | liability | power | N77 |
| 487.0911(1) | the person subject to the order | the Attorney General | right | duty | N79 |
| 487.0911(2) | the person subject to the order | the Attorney General | liability | power | N80 |
| 487.0911(3) | the person subject to the order | the Attorney General | liability | power | N82 |
| 487.0911(4) | the person subject to the order | the Attorney General | liability | power | N83 |
| 488.01(2) | a journalist | an applicant for a warrant, authorization or order | immunity | disability | N90 |
| 488.01(3) | a journalist | the judge | immunity | disability | N93 |
| 488.01(4) | the judge | a journalist | power | liability | N94 |
| 488.01(5) | a journalist suspected of an offence | the judge | disability | immunity | N95 |
| 488.01(6) | the judge | a journalist suspected of an offence | power | liability | N96 |
| 488.01(7) | a journalist | the judge | right | duty | N97 |
| 488.01(8) | the judge | the applicant | power | liability | N98 |
| 488.01(9) | a journalist | an officer | right | duty | N99 |
| 488.01(10) | a journalist | the judge | power | liability | N101 |
| 488.02(1) | a journalist | the court | right | duty | N102 |
| 488.02(2) | a journalist and the relevant media outlet | an officer | right | duty | N103 |
| 488.02(3) | a journalist or the relevant media outlet | a judge of the court that issued the warrant, authorization or order | power | liability | N104 |
| 488.02(4) | a journalist | an officer | immunity | disability | N106 |
| 488.02(5) | a journalist | the judge | immunity | disability | N107 |
| 488.02(6) | the judge | a journalist | power | liability | N108 |
| 488.02(7) | a journalist | the judge | right | duty | N109 |
| 488.1(2) | a lawyer and the client claiming privilege | an officer | right | duty | N115 |
| 488.1(3) | the client, the lawyer on behalf of the client, or the Attorney General | a judge | power | liability | N117 |
| 488.1(3)(b) | all other persons entitled to make application, and the custodian | the client, the lawyer or the Attorney General who applied | right | duty | N120 |
| 488.1(3)(c) | the client, the lawyer on behalf of the client, or the Attorney General | a judge | power | liability | N122 |
| 488.1(4) | the Attorney General and the person who objects | a judge | right | duty | N123 |
| 488.1(4)(b) | a judge | the person who objects to the disclosure | power | liability | N124 |
| 488.1(4)(c) | the Attorney General and the person who objects to the disclosure | a judge | right | duty | N125 |
| 488.1(4)(d) | the client | a judge | right | duty | N126 |
| 488.1(5) | the client | any person who would use the document in evidence | immunity | disability | N128 |
| 488.1(6) | the Attorney General | a judge | right | duty | N129 |
| 488.1(7) | a person with an application under paragraph (3)(c) | a judge | power | liability | N130 |
| 488.1(8) | the person claiming privilege | an officer | right | duty | N131 |
| 488.1(9) | the person claiming privilege | a judge | power | liability | N132 |
| 488.1(10) | the person claiming privilege | the public | immunity | disability | N133 |
| 489(1) | a person executing a warrant | the person from whom the thing is seized | power | liability | N135 |
| 489(2) | a peace officer or a public officer | the person from whom the thing is seized | power | liability | N136 |
| 489.1(1) | the person lawfully entitled to possession | a peace officer | right | duty | N137 |
| 489.1(2) | the person lawfully entitled to possession | a person other than a peace officer who has seized the thing | right | duty | N138 |
| 490(1) | the lawful owner or person lawfully entitled to possession | a justice | right | duty | N141 |
| 490(2) | the person from whom the thing was seized | a peace officer or the prosecutor | right | duty | N142 |
| 490(3) | the person from whom the thing was seized | a peace officer or the prosecutor | right | duty | N144 |
| 490(3.1) | the lawful owner | a peace officer or the prosecutor | power | liability | N146 |
| 490(4) | the clerk of the court | a justice | right | duty | N147 |
| 490(5) | the person from whom the thing was seized or who claims to be its owner | the prosecutor, peace officer or other person having custody | right | duty | N148 |
| 490(6) | the person from whom the thing was seized | the prosecutor, peace officer or other person having custody | right | duty | N150 |
| 490(7) | the person from whom anything was seized | a judge or justice | power | liability | N151 |
| 490(8) | the person from whom anything was seized | a judge or justice | power | liability | N152 |
| 490(9) | the person from whom the thing was seized, or the lawful owner | a judge or justice | right | duty | N153 |
| 490(9.1) | the person from whom the thing was seized | a judge or justice | power | liability | N155 |
| 490(10) | a person who claims to be the lawful owner | a judge or justice | power | liability | N156 |
| 490(11) | the claimant | a judge or justice | right | duty | N157 |
| 490(12) | the person from whom the thing was seized, the owner or the person claiming it | a judge or justice, a peace officer and the prosecutor | immunity | disability | N158 |
| 490(13) | a person with custody of a document seized | the person from whom it was seized | power | liability | N160 |
| 490(14) | the person from whom the document was seized | the person who certifies the copy | disability | immunity | N161 |
| 490(15) | a person who has an interest in what is detained | a judge | power | liability | N163 |
| 490(16) | the person who examines the thing | a judge | right | duty | N164 |
| 490(17) | a person aggrieved by the order | a court of appeal | power | liability | N165 |
| 490(18) | a person to whom three days notice must be given | the applicant | power | liability | N166 |
| 490.01 | the lawful owner | the person who seized the thing or has custody of it | right | duty | N167 |
| 490.01(b) | the person who seized the thing or has custody of it | the lawful owner | power | liability | N168 |
| 490.011(2) | a young person | the court | immunity | disability | N188 |
| 490.012(5) | a person convicted of a secondary offence | the court | immunity | disability | N189 |
| 490.012(1) | a person sentenced for a designated offence | the court | liability | power | N190 |
| 490.012(2) | a person previously convicted of a primary offence or subject to an obligation | the court | liability | power | N191 |
| 490.012(3) | a person sentenced for, or found not criminally responsible for, a designated offence | the court | liability | power | N192 |
| 490.012(4) | the person concerned | the court | right | duty | N193 |
| 490.013(1) | the person subject to the order | the court | liability | power | N194 |
| 490.013(2) | the person subject to the order | the court | liability | power | N195 |
| 490.013(3) | the person subject to the order | the court | liability | power | N196 |
| 490.013(4) | the person subject to the order | the court | liability | power | N197 |
| 490.013(5) | the person subject to the order | the court | liability | power | N198 |
| 490.013(6) | the person subject to the order | the court | liability | power | N199 |
| 490.0131 | the person subject to the order | the court | right | duty | N202 |
| 490.0132 | the person concerned | the court | right | duty | N203 |
| 490.0132(b) | the person concerned | the court | right | duty | N204 |
| 490.0132(c) | the court | the person concerned | power | liability | N205 |
| 490.0132(d) | the court | the person concerned | power | liability | N206 |
| 490.014 | the prosecutor or a person subject to an order | the appeal court | power | liability | N210 |
| 490.014(a) | the prosecutor or a person subject to an order | the appeal court | power | liability | N211 |
| 490.015(1) | a person subject to an order | the court | power | liability | N212 |
| 490.015(2) | a person subject to more than one order | the court | power | liability | N214 |
| 490.015(3) | a person who receives a pardon, a record suspension or an absolute discharge | the court | power | liability | N215 |
| 490.015(4) | a person subject to an order | the court | liability | power | N216 |
| 490.015(5) | a person whose application is refused | the court | power | liability | N218 |
| 490.015(6) | a person subject to an order | the court | power | liability | N219 |
| 490.016(1) | a person subject to an order | the court | right | duty | N220 |
| 490.016(1.1) | the person who applied | the court | right | duty | N221 |
| 490.016(2) | the person who applied | the court | right | duty | N222 |
| 490.016(3) | the Commissioner of the Royal Canadian Mounted Police and the Attorney General | the court | right | duty | N223 |
| 490.017(1) | the prosecutor or the person who applied | the appeal court | power | liability | N224 |
| 490.017(2) | the Commissioner of the Royal Canadian Mounted Police and the Attorney General | the appeal court | right | duty | N226 |
| 490.018(1) | the person subject to the order | the court or appeal court | right | duty | N227 |
| 490.018(2) | the court | the person subject to the order | right | duty | N228 |
| 490.018(3) | the person subject to the order | a Review Board | right | duty | N229 |
| 490.018(4) | the person subject to the order | the person in charge of the place of custody | right | duty | N230 |
| 490.019 | the Attorney General or minister of justice | a person served with a notice in Form 53 | power | liability | N232 |
| 487.092(1) | a justice | the person whose print or impression is to be obtained | power | liability | N234 |
| 487.092(2) | the person whose print or impression is to be obtained | a justice | right | duty | N235 |
| 487.092(3) | a peace officer | the person named in the warrant | power | liability | N236 |
| 487.093(1) | the person searched, or in control of the place searched | the person who executes the warrant | right | duty | N238 |
| 487.1(1) | the Attorney General, a peace officer or a public officer | the judge or justice | power | liability | N242 |
| 487.1(2) | a person who must swear an oath | the court | privilege | no-right | N243 |
| 487.1(3) | the applicant | a judicial officer | right | duty | N244 |
| 487.1(4) | the applicant | a judicial officer | disability | immunity | N245 |
| 487.1(5) | the applicant | a judicial officer | privilege | no-right | N246 |
| 487.1(6) | a judicial officer | the applicant | right | duty | N247 |
| 487.1(7) | a judicial officer | the applicant | power | liability | N248 |
| 487.1(8) | the applicant | a judicial officer | right | duty | N249 |
| 487.1(9) | the person subject to the warrant | a judicial officer | immunity | disability | N250 |
| 487.1(10) | the applicant | a judicial officer | power | liability | N251 |
| 487.11 | a peace officer or a public officer | the person searched or whose place is searched | power | liability | N254 |
| 487.2 | the person occupying or suspected in relation to the place searched | any person who publishes | right | duty | N255 |
| 487.3(1) | a justice or a judge | any person who seeks the information | power | liability | N257 |
| 487.3(3) | any person who seeks the information | the justice or judge | disability | immunity | N259 |
| 487.3(4) | a person who applies to terminate or vary the order | the justice or judge | power | liability | N260 |
| 488 | the person whose place is searched | a peace officer | right | duty | N261 |

Provisions that create no relation (`none`): the definitions, tables and counting rules N18, N19, N20, N21, N84, N85, N86, N87, N88, N89, N110, N111, N112, N113, N114, N134, N139, N140, N170, N171, N172, N173, N174, N175, N177, N178, N179, N180, N181, N182, N183, N184, N185, N186, N187, N237, N240, N241, N252, N253, N258 (see the index in the Coverage section); and every repealed row, heading and group heading.

The relation rules were checked once against the convention: where the court or an official holds a power, the person it is exercised on holds the liability; where a duty is imposed on an official for the person, the person holds the right; a bar on an official is the person's immunity.

## Marginal readings for a lawyer (ccc17)

The readings the brief says to take as the status quo and to flag, not decide: **(a)** a failed "if" counts as the text's no, clause by clause within the provision that holds the "if", and flat negatives count as the text saying no (N2 of 2026-11-04 for flat negatives); **(b)** a prohibition or grant limited by its own wording does not count as the text's no, so the answer is `NOTHING` (the other reading of every such branch is `JUST FALSE`, the text's no). The ruling of 2026-11-12 settles the one sub-case of grants named for "may" gated by "if": `NOTHING`.
Two groups are not decided here, as the brief says: **G1**, "may" functions whose gate is "where", "when" or "upon" or an equivalent (answered `JUST FALSE` by the periods ruling (b) and (c) of 2026-11-05; the line on grants points the other way): 12 functions, listed in the fork register; **G2**, functions named for an "entitled" claim: 0.

Below, every layer-1 function that answers `JUST FALSE` or `NOTHING` on any branch, with the kind of each branch (generated by `work/coverage.py` from the comments `-- FALSE-kind (...)` and `-- NOTHING-kind (...)`, which `work/lint.py` checks against the text). `JUST FALSE` branches are listed with the first words of the quoted text and the class the quote falls in; for `NOTHING` the count per reason is given. A branch of class "if", "flat negative", "as long as", "shall/must" or "where/when" rests on reading (a) (or on the periods ruling); a `NOTHING` of reason "limited by its own wording" rests on reading (b).

| function (index) | JUST FALSE branches: class, quoted words (start) | NOTHING branches by reason |
| --- | --- | --- |
| s 487.05(1) the provincial court judge may issue a warrant in Form 5.02 (N1) |  | limited by its own wording x8, points outside the text x1 |
| s 487.05(2) the provincial court judge shall have regard to the matter (N2) |  | includes x1 |
| s 487.05(4) the warrant may be executed by the peace officer at the place (N3) | shall/must: "must have authority to act as a peace officer in the place where it is..." | limited by its own wording x1 |
| s 487.051(1) the court shall make an order in Form 5.03 (N4) | if: "if that offence is a primary designated offence within the meaning of ..." | limited by its own wording x2, points outside the text x1 |
| s 487.051(2) the court shall make an order in Form 5.03 (N5) | if: "if that offence is a primary designated offence within the meaning of ..."; if: "the court is not required to make the order if it is satisfied that th..." | limited by its own wording x2, points outside the text x1 |
| s 487.051(3) the court may make an order in Form 5.04 (N6) |  | limited by its own wording x3 |
| s 487.051(3) the court shall consider the matter in deciding whether to make the order (N7) |  | list not closed x1 |
| s 487.051(3) the court shall give reasons for its decision (N8) |  | limited by its own wording x1 |
| s 487.051(4) the court may make an order in Form 5.041 requiring the person to report and submit to the taking of the samples (N9) | where/when/after/period: "When the court makes an order authorizing the taking of samples of bod..." |  |
| s 487.053(1) the court may make an order under section 487.051 at this time (N10) | where/when/after/period: "when it imposes a sentence on a person, finds the person not criminall..." |  |
| s 487.053(2)(a) the court shall set a date for a hearing within 90 days (N11) | if: "If the court does not consider the matter at that time" |  |
| s 487.053(2)(b) the court retains jurisdiction over the matter (N12) | if: "If the court does not consider the matter at that time" |  |
| s 487.053(2)(c) the court may require the person to appear by closed-circuit television or videoconference (N13) | as long as: "as long as the person is given the opportunity to communicate privatel..." | limited by its own wording x1 |
| s 487.054 the person may appeal from the decision of the court (N17) |  | limited by its own wording x2 |
| s 487.055(3) the offence is a sexual offence (N21) | means: "sexual offence means"; means: "sexual offence means" |  |
| s 487.055(1) the provincial court judge may authorize in Form 5.06 the taking of samples of bodily substances (N23) |  | limited by its own wording x3 |
| s 487.055(2) the application is accompanied by the certificate (N24) | shall/must: "The application shall be accompanied by a certificate referred to in p..." |  |
| s 487.055(2) the certificate may be received in evidence without the notice referred to in subsection 667(4) (N25) |  | limited by its own wording x1 |
| s 487.055(3.01) the court may require the person to appear by closed-circuit television or videoconference (N26) | as long as: "as long as the person is given the opportunity to communicate privatel..." | limited by its own wording x1 |
| s 487.055(3.1) the court shall consider the matter in deciding whether to grant an authorization (N27) |  | list not closed x1 |
| s 487.055(3.1) the court shall give reasons for its decision (N28) |  | limited by its own wording x1 |
| s 487.055(3.11) the court shall make an order in Form 5.041 requiring the person to report and submit to the taking of the samples (N29) | if: "If the court authorizes the taking of samples of bodily substances fro..." |  |
| s 487.055(4) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples (N30) | if: "if a person who is on conditional release has not appeared at the hear..." |  |
| s 487.055(5) the summons is served as the subsection requires (N31) | shall/must: "The summons shall be accompanied by a copy of the authorization"; shall/must: "be served by a peace officer who shall either deliver it personally"; shall/must: "shall either deliver it personally to the person to whom it is directe..." |  |
| s 487.0551(1) a justice of the peace may issue a warrant for the arrest of the person in Form 5.062 (N32) |  | limited by its own wording x2 |
| s 487.0551(2) the warrant may be executed by the peace officer at the place (N33) |  | limited by its own wording x1 |
| s 487.0551(2) the warrant remains in force (N34) | where/when/after/period: "The warrant remains in force until it is executed." |  |
| s 487.0552(1) the person is guilty of an offence (N35) |  | limited by its own wording x3 |
| s 487.0552(2) a lawful command that prevents the person from complying is a reasonable excuse (N37) | if: "is a reasonable excuse if, at the time, the person is subject to the C..." |  |
| s 487.056(1) the time at which the samples shall be taken under section 487.051 (N38) |  | limited by its own wording x1 |
| s 487.056(2) the time at which the samples shall be taken under section 487.055 or 487.091 (N39) |  | limited by its own wording x1 |
| s 487.056(3) the time at which the samples shall be taken when the person fails to appear (N40) |  | limited by its own wording x1 |
| s 487.056(4) subsections (1) to (3) apply even though the order or authorization is appealed (N41) |  | silent x1 |
| s 487.056(5) the peace officer may cause the samples to be taken in the place (N42) |  | limited by its own wording x1 |
| s 487.056(6) the samples are taken by a person the subsection permits (N43) | shall/must: "The samples shall be taken by a peace officer who has jurisdiction ove..."; other, read by hand: "a peace officer who has jurisdiction over the person or in the place i..."; other, read by hand: "who is able, by virtue of training or experience, to take them" |  |
| s 487.057(1) the peace officer shall make a written report in Form 5.07 and cause it to be filed (N44) |  | limited by its own wording x1 |
| s 487.057(1) with whom the report shall be filed (N45) |  | limited by its own wording x1 |
| s 487.057(2) the report shall include the matter (N46) |  | includes x1 |
| s 487.057(3) the peace officer shall send a copy of the report to the other peace officer (N47) | unless/except: "unless that other peace officer had jurisdiction to take the samples" | limited by its own wording x1 |
| s 487.058 the person incurs no criminal or civil liability for the thing done (N48) |  | limited by its own wording x3 |
| s 487.06(1) the means is one by which the peace officer is authorized to take samples of bodily substances (N49) |  | limited by its own wording x1, list not closed x1 |
| s 487.06(2) the warrant, order or authorization shall include the term or condition (N50) |  | limited by its own wording x1 |
| s 487.06(3) the peace officer, or a person acting under their direction, may take fingerprints from the person for the purpose of the DNA Identification Act (N51) |  | silent x1, limited by its own wording x1 |
| s 487.07(1) the peace officer shall inform the person of the matter before taking the samples (N52) | if: "if the sample is taken from a young person, the rights of the young pe..." | limited by its own wording x2 |
| s 487.07(2)(a) the person may be detained for the purpose of taking the samples (N53) |  | limited by its own wording x1 |
| s 487.07(2)(b) the person may be required to accompany a peace officer for the purpose of taking the samples (N54) |  | limited by its own wording x1 |
| s 487.07(3) the taker shall ensure that the person’s privacy is respected in a manner that is reasonable in the circumstances (N55) |  | limited by its own wording x1 |
| s 487.07(4) the young person has the right to consult counsel and an adult and to have the warrant executed in their presence (N56) |  | limited by its own wording x1 |
| s 487.07(4) the adult with whom the young person may consult and in whose presence the warrant is to be executed (N57) |  | limited by its own wording x1 |
| s 487.07(5) the young person’s waiver of the rights under subsection (4) is valid (N58) | shall/must: "any such waiver (a) must be recorded on audio tape or video tape or ot..." | limited by its own wording x1 |
| s 487.071(1) the peace officer, or the person acting under their direction, shall verify whether the convicted offenders index contains the person’s DNA profile (N59) |  | limited by its own wording x1 |
| s 487.071(2) the peace officer shall not take any bodily substances from the person (N60) | if: "If the person’s DNA profile is in the convicted offenders index of the..." | limited by its own wording x1 |
| s 487.071(2) the peace officer shall confirm in writing on the order or authorization that they have been advised that the profile is in the data bank and transmit a copy to the Commissioner of the Royal Canadian Mounted Police (N61) | if: "If the person’s DNA profile is in the convicted offenders index of the..." |  |
| s 487.071(3) the peace officer shall execute the order or authorization and transmit the bodily substances taken and a copy to the Commissioner of the Royal Canadian Mounted Police (N62) | if: "If the person’s DNA profile is not in the convicted offenders index of..." |  |
| s 487.08(1) the use of the bodily substances is barred (N63) | unless/except: "except to use them for the purpose of forensic DNA analysis in the cou..." | limited by its own wording x1 |
| s 487.08(1.1) the use of the bodily substances is barred (N64) | unless/except: "except to transmit them to the Commissioner of the Royal Canadian Moun..." | limited by its own wording x1 |
| s 487.08(2) the use of the results of forensic DNA analysis is barred (N65) | unless/except: "except (a) in the course of an investigation of the designated offence..."; other, read by hand: "or (b) in any proceeding for such an offence" | limited by its own wording x1 |
| s 487.08(3) the person is guilty of an offence punishable on summary conviction (N66) |  | limited by its own wording x2 |
| s 487.08(4) the person is guilty of an offence (N68) |  | limited by its own wording x2 |
| s 487.09(1) the bodily substances and the results of forensic DNA analysis shall be destroyed without delay (N70) | subject to: "Subject to subsection (2)"; where/when/after/period: "the expiration of one year after"; unless/except: "unless during that year a new information is laid or an indictment is ..." | limited by its own wording x1, list not closed x1 |
| s 487.09(2) the provincial court judge may order that the bodily substances and the results not be destroyed during the period considered appropriate (N73) |  | limited by its own wording x1 |
| s 487.09(3) the voluntarily given bodily substances and the results shall be destroyed without delay (N74) | where/when/after/period: "without delay after the results of that analysis establish that the bo..." | limited by its own wording x1 |
| s 487.091(1) the provincial court judge may authorize in Form 5.09 the taking of additional samples of bodily substances (N75) |  | limited by its own wording x2 |
| s 487.091(2) the application states the reasons the subsection requires (N76) | shall/must: "The application shall state the reasons why a DNA profile cannot be de..." |  |
| s 487.091(3) a summons in Form 5.061 shall be directed to the person requiring them to report and submit to the taking of the samples (N77) | if: "If the court authorizes the taking of samples of bodily substances fro..." |  |
| s 487.091(3) subsection 487.055(5) applies to the summons with the modifications that the circumstances require (N78) |  | limited by its own wording x1 |
| s 487.0911(1) the Attorney General shall review the order or authorization and the court record (N79) |  | limited by its own wording x1 |
| s 487.0911(2) the Attorney General shall apply ex parte to have the order or authorization corrected (N80) | if: "If the Attorney General is of the opinion that the defect is due to a ..." |  |
| s 487.0911(2)(b) the Attorney General shall transmit a copy of the corrected order or authorization to the Commissioner (N81) | if: "transmit a copy of the corrected order or authorization, if any" |  |
| s 487.0911(3) the Attorney General shall inform the Commissioner of the opinion that the offence is not a designated offence (N82) | if: "If the Attorney General is of the opinion that the offence referred to..." |  |
| s 487.0911(4) the Attorney General shall transmit the opinion, with written reasons, to the Commissioner (N83) | if: "If the Attorney General is of the opinion that the offence referred to..." |  |
| s 488.01(1) journalist (N86) |  | points outside the text x1 |
| s 488.01(1) journalistic source (N87) |  | points outside the text x1 |
| s 488.01(1) officer (N88) | means: "officer means a peace officer or public officer" | points outside the text x1 |
| s 488.01(2) the applicant shall make the application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552 (N90) | if: "if an applicant for a warrant under section 487.01, 492.1 or 492.2, a ..." | list not closed x1 |
| s 488.01(2) the judge has exclusive jurisdiction to dispose of the application (N92) |  | limited by its own wording x1 |
| s 488.01(3) the judge may issue the warrant, authorization or order (N93) | only if: "A judge may issue a warrant, authorization or order under subsection (..." |  |
| s 488.01(4) the judge may request that a special advocate present observations in the interests of freedom of the press concerning the conditions set out in subsection (3) (N94) |  | limited by its own wording x1 |
| s 488.01(5) subsections (3) and (4) do not apply (N95) |  | silent x1 |
| s 488.01(6) the judge may order that some or all documents obtained are to be dealt with in accordance with section 488.02 (N96) |  | limited by its own wording x1 |
| s 488.01(7) the warrant, authorization or order may contain the condition (N97) |  | limited by its own wording x1 |
| s 488.01(8) the judge has the same powers, with the necessary adaptations, as the authority who may issue the warrant, authorization or order (N98) |  | limited by its own wording x1 |
| s 488.01(9) the officer shall, as soon as possible, make an ex parte application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552 (N99) | if: "If an officer, acting under a warrant, authorization or order referred..." |  |
| s 488.01(9) until the judge disposes of the application the officer shall refrain from examining or reproducing any document obtained and shall keep it in a sealed packet (N100) | if: "If an officer, acting under a warrant, authorization or order referred..."; where/when/after/period: "until the judge disposes of the application" |  |
| s 488.01(10) the judge may make the order (N101) |  | limited by its own wording x2 |
| s 488.02(1) the document shall be placed in a packet and sealed by the court and kept in the custody of the court (N102) |  | limited by its own wording x1 |
| s 488.02(2) the officer is barred from examining or reproducing the document (N103) |  | limited by its own wording x2 |
| s 488.02(3) the journalist or media outlet may apply to a judge of the court that issued the warrant, authorization or order for an order that the document is not to be disclosed to an officer (N104) | where/when/after/period: "may, within 10 days of receiving the notice referred to in subsection ..." | limited by its own wording x2 |
| s 488.02(4) the document is not to be disclosed to an officer (N106) | only if: "is to be disclosed to an officer only following a disclosure order in ..." | limited by its own wording x1 |
| s 488.02(5) the judge may order the disclosure of the document (N107) | only if: "The judge may order the disclosure of a document only if he or she is ..." |  |
| s 488.02(6) the judge may examine the document (N108) |  | limited by its own wording x1 |
| s 488.02(7) the order the judge must make (N109) |  | silent x1 |
| s 488.1(1) custodian (N110) | means: "custodian means a person in whose custody a package is placed pursuant..." |  |
| s 488.1(1) judge (N112) | means: "judge means a judge of a superior court of criminal jurisdiction of th..." |  |
| s 488.1(1) lawyer (N113) | means: "lawyer means, in the Province of Quebec, an advocate, lawyer or notary"; other, read by hand: "in any other province, a barrister or solicitor" | limited by its own wording x1 |
| s 488.1(1) officer (N114) | means: "officer means a peace officer or public officer" | points outside the text x1 |
| s 488.1(2) the officer shall, without examining or making copies of the document, seize it and place it in a package, suitably sealed and identified (N115) | where/when/after/period: "Where an officer acting under the authority of this or any other Act o..." |  |
| s 488.1(2)(b) the package shall be placed in the custody of (N116) |  | limited by its own wording x1 |
| s 488.1(3)(a) the person may apply to a judge for an order appointing a place and a day for the determination of the question and requiring the custodian to produce the document (N117) | where/when/after/period: "within fourteen days from the day the document was so placed in custod..."; where/when/after/period: "on two days notice of motion to all other persons entitled to make app..." | limited by its own wording x2 |
| s 488.1(3)(c) the person may apply at the appointed time and place for an order determining the question (N122) |  | limited by its own wording x2 |
| s 488.1(4)(a) the judge may inspect the document (N123) |  | limited by its own wording x1 |
| s 488.1(4)(b) the judge may allow the Attorney General to inspect the document (N124) |  | limited by its own wording x1 |
| s 488.1(4)(c) the judge shall allow the Attorney General and the person who objects to the disclosure of the document to make representations (N125) | other, read by hand: "On an application under paragraph (3)(c), the judge" |  |
| s 488.1(4)(d) the order the judge shall make (N126) |  | limited by its own wording x1, silent x1 |
| s 488.1(4) the judge shall, at the same time, deliver concise reasons for the determination in which the nature of the document is described without divulging the details (N127) | other, read by hand: "On an application under paragraph (3)(c), the judge" |  |
| s 488.1(5) the document remains privileged and inadmissible as evidence (N128) | unless/except: "unless the client consents to its admission in evidence or the privile..." | limited by its own wording x1 |
| s 488.1(6) the judge shall order the custodian to deliver the document to the officer who seized it or to some other person designated by the Attorney General (N129) | where/when/after/period: "Where a document has been seized and placed in custody under subsectio..." |  |
| s 488.1(7) subsequent applications under paragraph (3)(c) may be made to another judge (N130) | where/when/after/period: "Where the judge to whom an application has been made under paragraph (..." |  |
| s 488.1(8) the officer is barred from examining, making copies of or seizing the document (N131) |  | limited by its own wording x1 |
| s 488.1(9) the judge may authorize the person to examine the document or make a copy of it in the presence of the custodian or the judge (N132) |  | limited by its own wording x1 |
| s 488.1(10) the application shall be heard in private (N133) |  | limited by its own wording x1 |
| s 488.1(11) this section does not apply (N134) | flat negative: "This section does not apply in circumstances where a claim of solicito..." |  |
| s 489(1) the person who executes a warrant may seize the thing in addition to the things mentioned in the warrant (N135) |  | limited by its own wording x1 |
| s 489(2) the officer may, without a warrant, seize the thing (N136) |  | limited by its own wording x3 |
| s 489.1(1) what the peace officer shall do as soon as is practicable (N137) |  | limited by its own wording x1 |
| s 489.1(2) the person shall, as soon as is practicable, bring the thing before a justice or report to the justice that it has been seized and is being detained (N138) |  | limited by its own wording x1 |
| s 489.1(3) the report to a justice shall be in Form 5.2, varied to suit the case (N139) |  | limited by its own wording x1 |
| s 489.1(4) section 489.1 does not apply to the thing (N140) | other than: "other than virtual currency or other digital assets" | limited by its own wording x1 |
| s 490(1) the order the justice shall make (N141) |  | limited by its own wording x1, silent x1 |
| s 490(2) the section bars detaining the thing for more than 180 days after the day of the seizure (N142) | unless/except: "unless (a) a justice, on the making of a summary application to him af..." | limited by its own wording x2 |
| s 490(3) the section bars detaining the thing for more than one year from the day of the seizure (N144) | unless/except: "unless (a) a judge of a superior court of criminal jurisdiction or a j..." | limited by its own wording x2 |
| s 490(3.1) the thing may be detained for the period (N146) |  | limited by its own wording x1 |
| s 490(4) the justice shall forward anything detained to the clerk of the court to which the accused has been ordered to stand trial (N147) | where/when/after/period: "When an accused has been ordered to stand trial" |  |
| s 490(5) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9) (N149) | where/when/after/period: "Where at any time before the expiration of the periods of detention pr..." |  |
| s 490(6) the prosecutor, peace officer or other person shall apply for an order in respect of the property under subsection (9) or (9.1) (N150) | where/when/after/period: "Where the periods of detention provided for or ordered under subsectio..." |  |
| s 490(7) the person from whom anything has been seized may apply summarily for an order under paragraph (9)(c) that the thing be returned (N151) | where/when/after/period: "may, after the expiration of the periods of detention provided for or ..."; where/when/after/period: "on three clear days notice to the Attorney General" |  |
| s 490(8) the judge or justice may allow an application under subsection (7) to be made before the expiration of the periods (N152) | where/when/after/period: "where he is satisfied that hardship will result unless the application..." |  |
| s 490(9) the order the judge or justice shall make (N153) | other, read by hand: "is satisfied that the periods of detention provided for or ordered und..."; if: "(d) if possession of it by the person from whom it was seized is unlaw..." | silent x1 |
| s 490(9) the judge or justice may order the thing forfeited to Her Majesty, to be disposed of as the Attorney General directs or otherwise dealt with in accordance with the law (N154) |  | limited by its own wording x1 |
| s 490(9.1) the judge or justice may order that the thing continue to be detained for such period as the judge or justice considers necessary (N155) |  | limited by its own wording x1 |
| s 490(10) the claimant may at any time apply summarily for an order that the thing detained be returned to the applicant (N156) | where/when/after/period: "on three clear days notice to the Attorney General and the person from..." | limited by its own wording x2 |
| s 490(11) the order the judge or justice shall make on the application under subsection (10) (N157) | where/when/after/period: "where a judge or justice is satisfied that (a) the applicant is the la..." | points outside the text x1 |
| s 490(12) nothing shall be returned, forfeited or disposed of (N158) |  | limited by its own wording x1 |
| s 490(13) the person may make, and retain, a copy of the document before bringing it before a justice or complying with an order (N160) |  | limited by its own wording x2 |
| s 490(14) the copy is admissible in evidence (N161) |  | limited by its own wording x2 |
| s 490(14) the copy has the same probative force as the original document would have if it had been proved in the ordinary way (N162) | other, read by hand: "in the absence of evidence to the contrary, has the same probative for..." | limited by its own wording x2 |
| s 490(15) the judge may order that the person be permitted to examine anything so detained (N163) | where/when/after/period: "Where anything is detained pursuant to subsections (1) to (3.1)"; other, read by hand: "on summary application on behalf of a person who has an interest in wh..."; where/when/after/period: "after three clear days notice to the Attorney General" | limited by its own wording x1 |
| s 490(16) the order shall be made on terms necessary or desirable to ensure that anything is safeguarded and preserved for any purpose for which it may subsequently be required (N164) |  | limited by its own wording x1 |
| s 490(17) the court to which the person aggrieved may appeal (N165) |  | limited by its own wording x2 |
| s 490(18) the person may agree that the application be made before the expiration of the three days (N166) |  | limited by its own wording x1 |
| s 490.01(a) the person may return the thing to its lawful owner or the person lawfully entitled to possession of it (N167) |  | limited by its own wording x1 |
| s 490.01(b) the person may dispose of the thing, or destroy it (N168) |  | limited by its own wording x1 |
| s 490.01(b)(i) the proceeds of disposition (N169) |  | silent x1 |
| s 490.011(1) primary offence (N175) | means: "primary offence means" |  |
| s 490.011(1) secondary offence (N178) | means: "secondary offence means" |  |
| s 490.011(1) designated offence (N179) | means: "designated offence means a primary offence or a secondary offence" |  |
| s 490.011(1) crime of a sexual nature (N180) |  | points outside the text x1 |
| s 490.011(1) database (N181) |  | points outside the text x1 |
| s 490.011(1) Ontario Act (N182) | means: "Ontario Act means Christopher’s Law (Sex Offender Registry), 2000, S.O..." |  |
| s 490.011(1) pardon (N183) | means: "pardon means a conditional pardon granted under Her Majesty’s royal pr..." |  |
| s 490.011(1) record suspension (N184) | means: "record suspension means a record suspension, as defined in subsection ..." |  |
| s 490.011(1) registration centre (N185) |  | points outside the text x1 |
| s 490.011(1) Review Board (N186) | means: "Review Board means the Review Board established or designated for a pr..." |  |
| s 490.011(1) verdict of not criminally responsible on account of mental disorder (N187) | means: "verdict of not criminally responsible on account of mental disorder me..." |  |
| s 490.011(2) the person is not included among those convicted of, or found not criminally responsible for, a designated offence (N188) | unless/except: "unless they are given an adult sentence within the meaning of that sub..."; unless/except: "unless they are convicted of the offence in ordinary court within the ..." | silent x1 |
| s 490.012(5) the court may make an order in respect of the offence (N189) | only if: "only if the prosecutor applies for the order and establishes beyond a ..." | limited by its own wording x1 |
| s 490.012(1) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act (N190) | shall/must: "A court shall make an order under any of subsections (1) to (3) in res..."; if: "if (a) the designated offence was prosecuted by indictment; (b) the se..." | limited by its own wording x2 |
| s 490.012(2) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act (N191) | shall/must: "A court shall make an order under any of subsections (1) to (3) in res..."; if: "if the prosecutor establishes that, before or after the coming into fo..." | limited by its own wording x2 |
| s 490.012(3) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act (N192) | shall/must: "A court shall make an order under any of subsections (1) to (3) in res..."; other, read by hand: "in circumstances in which neither subsection (1) nor (2) applies"; unless/except: "unless the court is satisfied the person has established that" | limited by its own wording x2 |
| s 490.012(4) the court shall consider the factor in determining whether to make an order under subsection (3) (N193) |  | limited by its own wording x1 |
| s 490.013(2) the duration of an order made under subsection 490.012(1) or (3) apart from subsections (3) and (5) (N195) |  | silent x1 |
| s 490.013(3) an order made under subsection 490.012(1) or (3) applies for life (N196) | if: "applies for life if (a) in the same proceeding, the person has been co..." | limited by its own wording x1 |
| s 490.013(4) the duration of the order when the court is not satisfied as set out in paragraph (3)(b) (N197) |  | limited by its own wording x1 |
| s 490.013(5) an order made under subsection 490.012(1) or (3) applies for life (N198) | if: "applies for life if the person (a) was previously convicted of" |  |
| s 490.013(6) an order made under subsection 490.012(2) applies for life (N199) |  | limited by its own wording x1 |
| s 490.013(2) the day on which the order ends (N201) |  | silent x1 |
| s 490.0131 what the court shall do (N202) |  | limited by its own wording x1 |
| s 490.0132(a) the court shall set a date for a hearing within 90 days (N203) | if: "If the court does not consider the matter under any of subsections 490..." |  |
| s 490.0132(b) the court retains jurisdiction over the matter (N204) | if: "If the court does not consider the matter under any of subsections 490..." |  |
| s 490.0132(c) the court may require the person to appear at the hearing by videoconference (N205) | as long as: "as long as the person is given the opportunity to communicate privatel..." | limited by its own wording x1 |
| s 490.0132(d) the court may issue a summons in Form 6.3 to compel the attendance of the person at the hearing (N206) |  | limited by its own wording x1 |
| s 490.014 the person may appeal from the decision of the court (N210) |  | limited by its own wording x3 |
| s 490.014 the appeal court may make the disposition (N211) |  | list not closed x1 |
| s 490.015(1) the person may apply for a termination order (N212) |  | limited by its own wording x2 |
| s 490.015(1) the earliest day on which the person may apply for a termination order (N213) |  | limited by its own wording x1 |
| s 490.015(2) the person subject to more than one order may apply for a termination order (N214) |  | limited by its own wording x1 |
| s 490.015(3) the person may apply for a termination order despite subsections (1) and (2) (N215) |  | limited by its own wording x1 |
| s 490.015(4) the application shall also be in relation to the obligation (N216) | if: "If a person is subject to an obligation under section 490.019 or 490.0..." |  |
| s 490.015(4) the application shall be in relation to every order that is in effect (N217) |  | limited by its own wording x1 |
| s 490.015(5) the person may re-apply for a termination order (N218) | flat negative: "they may not re-apply under this subsection if an order is made with r..." | limited by its own wording x2 |
| s 490.015(6) the court to which the application shall be made (N219) |  | limited by its own wording x1 |
| s 490.016(1) the court shall make a termination order (N220) | shall/must: "The court shall make a termination order if it is satisfied that the p..." |  |
| s 490.016(1.1) the court shall consider the factor in determining whether to make the termination order (N221) |  | limited by its own wording x1 |
| s 490.016(2) the court shall give reasons for its decision (N222) |  | limited by its own wording x1 |
| s 490.016(3) the court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision (N223) | if: "If the court makes a termination order, it shall cause the Commissione..." |  |
| s 490.017(1) the person may appeal from the decision made under subsection 490.016(1) (N224) |  | limited by its own wording x3 |
| s 490.017(1) the appeal court may make the disposition (N225) |  | list not closed x1 |
| s 490.017(2) the appeal court shall cause the Commissioner of the Royal Canadian Mounted Police and the Attorney General of the province, or the minister of justice of the territory, to be notified of the decision (N226) | if: "If the appeal court makes an order that may be made under subsection 4..." |  |
| s 490.018(1) the court shall cause the thing to be done (N227) | if: "the Review Board that is responsible for making a disposition with res..."; if: "or is to be detained in custody as part of a disposition under Part XX..." | limited by its own wording x1 |
| s 490.018(2) the person who is subject to the order shall endorse the order (N228) | where/when/after/period: "After paragraphs (1)(a) to (c) have been complied with" |  |
| s 490.018(3) the Review Board shall cause a copy of the order to be given to the person (N229) | unless/except: "unless the conditions restrict the person’s liberty in a manner and to..." | limited by its own wording x1 |
| s 490.018(4) the person in charge shall give the person a copy of the order on the day (N231) | flat negative: "not earlier than 10 days before their release or discharge"; shall/must: "before their release or discharge shall give the person a copy of the ..." |  |
| s 490.019 the person shall comply with the Sex Offender Information Registration Act (N232) | unless/except: "unless a court makes an exemption order under subsection 490.023(2)"; other, read by hand: "for the applicable period specified in section 490.022" | limited by its own wording x1, points outside the text x1 |
| s 490.012 an order to comply with the Sex Offender Information Registration Act is in force (N233) | other, read by hand: "An order made under section 490.012 begins on the day on which it is m..."; where/when/after/period: "ends 10 years after it was made if the offence in connection with whic..."; where/when/after/period: "ends 20 years after it was made if the maximum term of imprisonment fo..." | silent x3 |
| s 487.092(1) the justice may issue a warrant in writing authorizing a peace officer to obtain a print or impression of the body of the person (N234) |  | limited by its own wording x1 |
| s 487.092(2) the warrant shall contain the term or condition (N235) |  | limited by its own wording x1 |
| s 487.092(3) the warrant may be executed by the peace officer at the place (N236) | shall/must: "must have authority to act as a peace officer in the place where it is..." | limited by its own wording x1 |
| s 487.093(1) what the person executing the warrant shall do during the execution (N238) |  | limited by its own wording x1 |
| s 487.093(2) subsection (1) does not apply (N239) | flat negative: "Subsection (1) does not apply if the warrant authorizes the search of ..." |  |
| s 487.1(1) the application may be submitted by a means of telecommunication (N242) |  | limited by its own wording x3, list not closed x1 |
| s 487.1(2) the statement is deemed to be a statement made under oath (N243) |  | limited by its own wording x1 |
| s 487.1(3) the judicial officer shall certify the application as to time and date of receipt (N244) |  | limited by its own wording x1 |
| s 487.1(4) the application shall not be submitted by a means of telecommunication that does not produce a writing (N245) |  | limited by its own wording x1 |
| s 487.1(5) the applicant may submit the application by a means of telecommunication that does not produce a writing (N246) | means: "An applicant may submit their application by a means of telecommunicat..." |  |
| s 487.1(6) the application includes the statement of circumstances the subsection requires (N247) | shall/must: "shall include a statement of the circumstances that make it impractica..." | limited by its own wording x1 |
| s 487.1(7) the oath may be administered by a means of telecommunication (N248) |  | limited by its own wording x1 |
| s 487.1(8) the judicial officer shall record the application verbatim and certify the record or a transcription of it as to time, date and contents (N249) |  | limited by its own wording x1 |
| s 487.1(9) the judicial officer is barred from issuing the warrant, order, extension or authorization (N250) | flat negative: "shall not issue the warrant, order, extension or authorization unless ..." | limited by its own wording x1 |
| s 487.1(10) the steps that follow when the judicial officer issues the document by a means of telecommunication (N251) |  | limited by its own wording x1 |
| s 487.1(11) judicial officer (N252) | means: "judicial officer means a judge or justice who is authorized, under the..." |  |
| s 487.1(11) public officer (N253) | means: "public officer means a public officer who is appointed or designated t..." |  |
| s 487.11 the officer may exercise the powers described in subsection 487(1) or 492.1(1) without a warrant (N254) |  | limited by its own wording x4 |
| s 487.2 the person is guilty of an offence punishable on summary conviction (N255) | unless/except: "unless a charge has been laid in respect of any offence in relation to..." | limited by its own wording x3 |
| s 487.3(1) the justice or judge may make an order prohibiting access to, and the disclosure of, any information relating to the warrant, order or authorization (N257) |  | limited by its own wording x4 |
| s 487.3(2) the ground is one on which an order under subsection (1) may be made (N258) |  | limited by its own wording x1 |
| s 487.3(3) all documents relating to the application shall be placed in a packet, sealed and kept in the custody of the court (N259) | where/when/after/period: "Where an order is made under subsection (1)" |  |
| s 487.3(4) the application to terminate the order or vary its terms and conditions may be made to the judge (N260) |  | limited by its own wording x1 |
| s 488 the warrant shall be executed by day (N261) | shall/must: "shall be executed by day, unless (a) the justice is satisfied that the..." | limited by its own wording x1 |
| s 488 the warrant may be executed at the time of day (N262) | shall/must: "shall be executed by day, unless (a) the justice is satisfied that the..." | silent x1 |

Totals (a `JUST FALSE` here includes the three answers that are a constructor meaning "the text says no": two in `s 490(9) the order the judge or justice shall make` and one in `s 490(11) the order the judge or justice shall make on the application under subsection (10)`): 133 `JUST FALSE` branches in 107 functions (of the 219 that answer `JUST FALSE` or `NOTHING` on some branch), by class: if 32; where/when/after/period 26; means 18; shall/must 17; unless/except 14; other, read by hand 12; flat negative 5; only if 4; as long as 3; subject to 1; other than 1.
228 `NOTHING` branches, by reason: limited by its own wording 191, silent 15, points outside the text 12, list not closed 8, includes 2.


### Fork lines recorded by the name-test sweep of 2026-11-12

- **F14** (new): `s 487.05(4) the warrant may be executed by the peace officer at the place` and `s 487.092(3) the warrant may be executed by the peace officer at the place`: `JUST FALSE` where the peace officer lacks authority to act as a peace officer in the place of execution (a bare "must" in the text's second sentence); other reading `NOTHING`. Reading (b) is the other reading.
- **F1** (answers `NOTHING`; nothing flipped): the 27 grants named "may" and conditioned by the text ("if", "where", "once", "on application of", "satisfied that"); the other reading is `JUST FALSE` (reading (a)). The list is under F1 in the fork register.
- The 12 functions of group G1 and the 0 of group G2 are listed in the fork register and nowhere else.

### Reading a result: FALSE and NOTHING (ccc17)

Every layer-1 function and every seat question of this part answers `JUST TRUE`, `JUST FALSE` or `NOTHING` (a `MAYBE BOOLEAN`), or a `MAYBE` of a date or a number.
In the subject of this range, which is what the criminal law does to a person whose bodily substances, papers, belongings or registration status are in question:

- **`JUST TRUE`** is "yes, on the text's own words and the facts given": the judge may issue the warrant, the court must make the order, the officer is barred, the person is guilty.
- **`JUST FALSE`** is "no, because the text itself says no in its own words", and only then. Four kinds of own-words no occur here: a definition that says "means" (a provision outside the six limbs of `sexual offence` is not one); a condition the text introduces with "if", "only if", "unless" or "as long as" (for example `s 488.01(3)`: a judge may issue the warrant "only if" two further conditions are met); a period the text fixes ("within 10 days of receiving the notice", "180 days after the day of the seizure"); a flat negative ("shall not", "may not", "does not apply").
  `JUST FALSE` is never "the person is safe" or "the court may not": for a duty it says the section imposes no duty on these facts, and for a bar it says the "unless" has been met, and in each case the text's words are quoted beside the branch.
- **`NOTHING`** is "not covered": the text does not answer on these facts, and nothing may be concluded from that.
  The commonest case in this range is a grant limited by its own wording: "a provincial court judge may issue a warrant" if the listed grounds are met. When they are not met, the section does not authorise the warrant, but it does not forbid one either, so the answer is `NOTHING` and not `JUST FALSE` (ruling of 2026-11-12, limit (1)).
  The other cases are a person the section does not name (for example a person found not criminally responsible asked under `s 487.051(1)`, which names the convicted, the discharged and the young), a list the text does not close, an answer that belongs to another part (`s 487.04`, whether the offence is a designated offence), a silence (the text does not say who may apply to vary an order under `s 487.3(4)`).
- A caller must never turn `NOTHING` into `FALSE`. In particular, `NOTHING` from "may the court make the order?" does not mean "the court may not": it means this part's sources do not say.
- Each `JUST FALSE` branch is tagged `-- FALSE-kind (the text says no in its own words): "<quote>"` and each `NOTHING` branch `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording; `work/lint.py` checks both mechanically.
- The two readings the brief leaves to a lawyer are taken as the status quo and every branch that rests on one is listed under "Marginal readings for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.

## Seams (ccc17)

### Answers this part takes from other parts (inputs)

| input (as the layer-1 function names it) | type | asked by | answered by (PLAN.md section 6) | note |
| --- | --- | --- | --- | --- |
| `s 487.04 the offence is a designated offence` | MAYBE BOOLEAN | `s 487.05(1)` | ccc16 s 487.04 | PLAN.md names this one; used as the plan names it |
| `s 487.04 the offence is a designated offence when the finding is made` | MAYBE BOOLEAN | `s 487.051(3)(a)` | ccc16 s 487.04 | finer than PLAN.md (fork F2) |
| `s 487.04 the offence is a secondary designated offence when the person is sentenced or discharged` | MAYBE BOOLEAN | `s 487.051(3)(b)` | ccc16 s 487.04 | PLAN.md names `s 487.04 the offence is a ... secondary designated offence`; I added the time at which the text asks |
| `s 487.04 the offence is a primary designated offence within paragraph (a) or (c.02) of the definition when the person is sentenced or discharged` | MAYBE BOOLEAN | `s 487.051(1)` | ccc16 s 487.04 | finer than PLAN.md (fork F2): the text of (1) turns on paragraphs (a) and (c.02) |
| `s 487.04 the offence is a primary designated offence within any of paragraphs (a.1) to (c.01) and (c.03) to (d) of the definition when the person is sentenced or discharged` | MAYBE BOOLEAN | `s 487.051(2)` | ccc16 s 487.04 | finer than PLAN.md (fork F2): the text of (2) turns on the other paragraphs |
| `s 321 the thing is a document` | MAYBE BOOLEAN | `s 488.1` | ccc12 s 321 | as PLAN.md names it |
| `s 487.011 document: the thing is a document`, `s 487.011 data: the thing is data` | MAYBE BOOLEAN | `s 488.01(1)` (definitions "document" and "data" "have the same meaning as in section 487.011") | the part that owns s 487.011 | a seam the plan lacks; the definition says only "has the same meaning as in" |
| `s 2 peace officer: the person is one`, `s 2 public officer: the person is one` | MAYBE BOOLEAN | `s 487.11` and `s 489(2)` (`s 2 peace officer` only), and the two definitions `s 488.01(1) officer` and `s 488.1(1) officer` (both inputs) | `ccc-definitions.l4` (the keel) | taken as inputs where my rule turns on them, as PLAN.md section 4 says; `s 2 day` and `s 2 night` are called directly in s 488 |
| `s 490.022 the person is within the applicable period` | MAYBE BOOLEAN | `s 490.019` | ccc18 s 490.022 | PLAN.md does not name it; s 490.019 says "for the applicable period specified in section 490.022" |

### Answers other parts take from this part

| function | type | asked by | note |
| --- | --- | --- | --- |
| `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force` | MAYBE BOOLEAN | ccc18, ss 490.02 to 490.027 and 490.04 (PLAN.md section 6) | the name is exactly the one PLAN.md gives; it takes whether an order was made under s 490.012, the day it was made, the day in question, the duration given by `s 490.013 the duration of the order` and whether a termination order has been made |
| `s 490.011(1) designated offence`, `s 490.011(1) primary offence`, `s 490.011(1) secondary offence` | MAYBE BOOLEAN | ccc18 | PLAN.md section 6 names only s 490.011 among the sections ccc18 asks for, not a function name; these three are the definition functions this part offers for it |
| `s 490.019 the person shall comply with the Sex Offender Information Registration Act` | MAYBE BOOLEAN | ccc18 | PLAN.md section 6 names s 490.019 among the sections ccc18 asks for, not a function name |

### Seams the plan lacks

- `s 488.01(1)` takes two definitions by reference ("document" and "data" have the same meaning as in section 487.011): two inputs, above.
- `s 490.019` reads the "applicable period specified in section 490.022", which sits in ccc18: one input, above.
- `s 487.051(1)` and `(2)` need the paragraph of the definition of "primary designated offence" in `s 487.04`, not only whether the offence is a primary designated offence: two inputs named for the paragraph groups, above (fork F2).

## What the text turns out to say (ccc17)

Numbered findings from reading the range closely; each is checked against the text lines cited.

1. **Eight rows of the range are shown repealed, one of them a whole section.** `487.05(3)` (line 9561), `487.052` (9575, the whole section), `487.055(6)` (9626), `487.055(7) to (10)` (9627, four subsections on one line), `487.07(1)(d.1)` (9683), `487.08(2.1)` (9720), `487.092(4)` (9766) and `490.013(2.1)` (10186) carry only "[Repealed, year, c. n, s. n]". Each is a coverage row `repealed or blank in this text`; none is encoded.
2. **`s 487.091(3)` incorporates a repealed subsection.** Line 9747 says "Subsections 487.055(5) and (6) apply, with any modifications that the circumstances require", but line 9626 shows `487.055(6)` repealed (2008, c. 18, s. 13). The incorporation is encoded for subsection (5) only (`s 487.091(3)`, comment in the module).
3. **Two provisions of the secondary-offence table appear twice.** In `490.011(1) "secondary offence" (a)` (lines 10123 to 10146) paragraphs `348(1)(d)` and `348(1)(e)` each appear twice, once for breaking and entering with intent to commit an indictable offence and once for breaking and entering and committing one (subparagraphs (xx) to (xxiii)). The table keeps all 23 rows; each is tested.
4. **`s 487.056(6)` can be read two ways.** "The samples shall be taken by a peace officer who has jurisdiction over the person or in the place in which the samples are taken -- or a person acting under their direction -- who is able, by virtue of training or experience, to take them." The relative clauses can attach to the peace officer, to the person acting under direction, or to both (fork F4).
5. **`s 487.05(4)` and `s 487.092(3)` are the same two sentences** ("A warrant issued under subsection (1) may be executed at any place in Canada. Any peace officer who executes the warrant must have authority to act as a peace officer in the place where it is executed."); the second sentence is a bare "must", not an "if" (fork F14).
6. **`s 488.1(1)` "lawyer" says nothing for the territories.** "In the Province of Quebec, an advocate, lawyer or notary and, in any other province, a barrister or solicitor": a territory is not a province (fork F8).
7. **`s 490(9)` has a gap.** Paragraph (c) returns the thing to the person from whom it was seized if their possession is lawful; paragraph (d) returns it to the lawful owner if possession is unlawful and the owner is known; a thing seized when it was not in anyone's possession, with a known owner, is reached by neither (fork F9).
8. **`s 490.013(2)` names the maximum terms 2, 5, 10, 14 and life only.** An offence with another maximum term (3, 7 or 12 years, for example) is not placed by paragraphs (a) to (c); the answer is `NOTHING` (fork F13).
9. **Several periods are counted from a day the text does not count.** "one year after", "five years have elapsed", "180 days after the day of the seizure": the text gives no rule for whether the day itself counts, and the Interpretation Act is not among the sources (fork F5).
10. **`s 490.012(1)` to `(3)` and `(5)` interlock.** `(3)` applies "in circumstances in which neither subsection (1) nor (2) applies, or when the court renders a verdict of not criminally responsible"; whether (1) or (2) applying defeats (3) for a verdict of not criminally responsible is not stated (fork F12). Subsection (5) says: "A court shall make an order under any of subsections (1) to (3) in respect of a secondary offence only if the prosecutor applies for the order and establishes beyond a reasonable doubt that the person committed the secondary offence with the intent to commit a primary offence." It is encoded as `s 490.012(5) the court may make an order in respect of the offence`, closed by "only if", and each of (1) to (3) answers `JUST FALSE` when (5) does.
11. **Twelve of the 52 seat questions asked more or less than the function they call answers.** Eleven named a different limb, route, section or premise (a status the body does not require, "to me" for "the person lawfully entitled", the custody limb of s 488.1(2)(b) inside the question for (a)); one used "may" for a "shall" (s 490.018(4)). They were retitled to what the body answers; the old and the new text of each are listed under "Seat questions (ccc17)" below.

## What the stable binary does not accept, and what it does differently (ccc17)

Measured on `l4` 1.6.110 while writing this part; where a skill describes a construct that this binary rejects, the binary governs.
Sorted by how each failure shows up.

**Loud (an error says so; the file does not run):**

- `length` is not a function of the stable prelude: use `count`.
- `WHEN `constructor` WITH t THEN` is a parse error: write `WHEN `constructor` t THEN`.
- A record built with `OF` needs commas between its fields: `rec OF a, b, c`.
- There is no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` (except `LEST BREACH ... BECAUSE`, which is accepted and used in the two regulative rules): "not covered" is `NOTHING` or a constructor.
- A DEONTIC value cannot be compared with `EQUALS`, so a regulative rule cannot be asserted: the two rules (`s 487.053(2)(a) the court must set a date for the hearing`, `s 490.0132(a) the court must set a date for the hearing`) are run with `#TRACE` and read (FULFILLED on day 90, BREACH BY `the court` on day 91, identical on both builds), and each duty is also encoded as a decision function over the same facts whose period boundaries are asserted.
- A continuation line of an `#ASSERT` is rejected: every assertion is on one line (some are 600 characters long).

**Silent (the file runs and returns an answer you might not expect):**

- `NOT a AND b` parses as `NOT (a AND b)`. A test caught this in `s 490.012(3)` (an unparenthesised `NOT x AND (...)`); every `NOT` is now parenthesised.
- `add years d n` clamps: 29 February plus one year is 28 February, where `Date 29 2 2023` rolls forward to 1 March. This is why the counting of a year is fork F5.
- `Date PLUS n` adds days, so a period in days is `PLUS n`; a period in years is `add years`.
- Never define `YMD`: dates are written `Date day month year`.
- `WAIT UNTIL` is spelled `WAITUNTIL` (not used in this range).

## Seat questions (ccc17)

52 questions in `ccc17-seat.l4`, grouped under six `§` headings in the text's order: ss 487.05 to 487.091 (14 questions), 487.092 to 488 (7), 488.01 and 488.02 (4), 488.1 (5), 489 to 490.01 (10), 490.011 to 490.019 (12).
Each begins "Under section N,", takes plain inputs with an `@desc` worded as the person would be asked, carries `@export` and `@desc`, and calls one layer-1 function (or reads one through a `CONSIDER`); it never restates a rule.
`ccc17-cases-seat.l4` has 147 assertions, at least one for every question and an explicit `NOTHING` case for each question that has one.
The first column is the question's number in the file; the second is its `@export` text as it now stands; the third is the layer-1 function it calls.

| # | `@ref` | question (`@export` text) | layer-1 function called |
| --- | --- | --- | --- |
| 1 | s 487.05(1) | Under section 487.05(1), may a provincial court judge issue a warrant to take my bodily substances for forensic DNA analysis? | `s 487.05(1) the provincial court judge may issue a warrant in Form 5.02` |
| 2 | s 487.051(1) | Under section 487.051(1), must the court order me to give samples of my bodily substances for DNA analysis, because my offence is a primary designated offence within paragraph (a) or (c.02) of the definition? | `s 487.051(1) the court shall make an order in Form 5.03` |
| 3 | s 487.051(2) | Under section 487.051(2), must the court order me to give samples of my bodily substances for DNA analysis, because my offence is a primary designated offence within the other paragraphs, unless I show that the order would be grossly disproportionate? | `s 487.051(2) the court shall make an order in Form 5.03` |
| 4 | s 487.051(3) | Under section 487.051(3), may the court order me to give samples of my bodily substances for DNA analysis? | `s 487.051(3) the court may make an order in Form 5.04` |
| 5 | s 487.054 | Under section 487.054, may I, as the offender, appeal from a decision of the court under subsection 487.051(1), (2) or (3)? | `s 487.054 the person may appeal from the decision of the court` |
| 6 | s 487.055(1) | Under section 487.055(1), may a provincial court judge authorize the taking of samples of my bodily substances for DNA analysis because, before June 30, 2000, I had been declared a dangerous offender, convicted of murder, or convicted of another listed offence for which I am serving a sentence? | `s 487.055(1) the provincial court judge may authorize in Form 5.06 the taking of samples of bodily substances` |
| 7 | s 487.0552(1) | Under section 487.0552(1), am I guilty of an offence because I failed, without reasonable excuse, to comply with an order or summons to report and give DNA samples? | `s 487.0552(1) the person is guilty of an offence` |
| 8 | s 487.0552(1) | Under section 487.0552(1), what is the longest term of imprisonment, in years, that I can be given if I am prosecuted by indictment for failing to comply with an order or summons to report and give DNA samples? | `s 487.0552(1) the punishments` |
| 9 | s 487.07(1) | Under section 487.07(1), must the peace officer tell me, before taking my samples, that the results of forensic DNA analysis may be used in evidence? | `s 487.07(1) the peace officer shall inform the person of the matter before taking the samples` |
| 10 | s 487.07(2) | Under section 487.07(2), may I be detained for a reasonable period so that samples of my bodily substances can be taken? | `s 487.07(2)(a) the person may be detained for the purpose of taking the samples` |
| 11 | s 487.071(2) | Under section 487.071(2), is the peace officer barred from taking bodily substances from me because my DNA profile is already in the convicted offenders index of the national DNA data bank? | `s 487.071(2) the peace officer shall not take any bodily substances from the person` |
| 12 | s 487.09(1) | Under section 487.09(1), must my bodily substances, taken under a DNA warrant, and the results of the analysis be destroyed without delay? | `s 487.09(1) the bodily substances and the results of forensic DNA analysis shall be destroyed without delay` |
| 13 | s 487.09(1)(c) | Under section 487.09(1)(c), on what day does the one year end after which my bodily substances must be destroyed, counted from the day I was discharged after a preliminary inquiry, the charge was dismissed or withdrawn, or the proceedings were stayed? | `s 487.09(1)(c) the day on which one year after the event expires` |
| 14 | s 487.091(1) | Under section 487.091(1), may a provincial court judge authorize the taking of additional samples of my bodily substances because a DNA profile could not be derived or the information was lost? | `s 487.091(1) the provincial court judge may authorize in Form 5.09 the taking of additional samples of bodily substances` |
| 15 | s 487.092(1) | Under section 487.092(1), may a justice issue a warrant to obtain a print or impression of my body, such as a fingerprint or footprint? | `s 487.092(1) the justice may issue a warrant in writing authorizing a peace officer to obtain a print or impression of the body of the person` |
| 16 | s 487.093(1) | Under section 487.093(1), must the person executing a search warrant give me a copy of the warrant and a notice in Form 5.1, or leave them in a prominent place? | `s 487.093(1) what the person executing the warrant shall do during the execution` |
| 17 | s 487.1(5) | Under section 487.1(5), may the police submit their application for a warrant to a judge or justice by a means of telecommunication that does not produce a writing, such as a telephone call? | `s 487.1(5) the applicant may submit the application by a means of telecommunication that does not produce a writing` |
| 18 | s 487.11 | Under section 487.11, may a peace officer or public officer search, or seize under section 487(1) or 492.1(1), without a warrant because it is impracticable to obtain one in exigent circumstances? | `s 487.11 the officer may exercise the powers described in subsection 487(1) or 492.1(1) without a warrant` |
| 19 | s 487.2 | Under section 487.2, is it an offence to publish or broadcast the location of the place searched under a search warrant, or the identity of a person who occupies it or is suspected, without the consent of every person referred to in paragraph 487.2(b), before a charge is laid? | `s 487.2 the person is guilty of an offence punishable on summary conviction` |
| 20 | s 487.3(1) | Under section 487.3(1), may a justice or judge order that access to, and disclosure of, information about the warrant, order or authorization be prohibited? | `s 487.3(1) the justice or judge may make an order prohibiting access to, and the disclosure of, any information relating to the warrant, order or authorization` |
| 21 | s 488 | Under section 488, may a search warrant issued under section 487 be executed at this time of day? | `s 488 the warrant may be executed at the time of day` |
| 22 | s 488.01(2) | Under section 488.01(2), must the police apply to a judge of a superior court of criminal jurisdiction (or a judge as defined in section 552) for a warrant, authorization or order that relates to a journalist? | `s 488.01(2) the applicant shall make the application to a judge of a superior court of criminal jurisdiction or a judge as defined in section 552` |
| 23 | s 488.01(3) | Under section 488.01(3), may the judge issue a warrant, authorization or order that relates to my communications as a journalist, only if there is no other reasonable way to get the information and the public interest outweighs my right to privacy? | `s 488.01(3) the judge may issue the warrant, authorization or order` |
| 24 | s 488.02(3) | Under section 488.02(3), may I, as a journalist, still apply within 10 days of receiving the officer's notice for an order that a sealed document not be disclosed to an officer? | `s 488.02(3) the journalist or media outlet may apply to a judge of the court that issued the warrant, authorization or order for an order that the document is not to be disclosed to an officer` |
| 25 | s 488.02(3) | Under section 488.02(3), what is the last day on which I may apply to a judge for an order that a sealed document not be disclosed to an officer, counting 10 days from the day I received the notice? | `s 488.02(3) the last day on which the application may be made` |
| 26 | s 488.1(2) | Under section 488.1(2), must an officer, without examining or copying the document, seize it and place it in a sealed and identified package, because the lawyer claims solicitor-client privilege for it? | `s 488.1(2) the officer shall, without examining or making copies of the document, seize it and place it in a package, suitably sealed and identified` |
| 27 | s 488.1(3)(a) | Under section 488.1(3)(a), may I, as the client (or my lawyer for me), still apply to a judge within 14 days from the day the document was placed in custody, on two days notice of motion? | `s 488.1(3)(a) the person may apply to a judge for an order appointing a place and a day for the determination of the question and requiring the custodian to produce the document` |
| 28 | s 488.1(3)(a) | Under section 488.1(3)(a), what is the last day on which I may apply to a judge, counting 14 days from the day the document was placed in custody? | `s 488.1(3)(a) the last day to apply to a judge` |
| 29 | s 488.1(5) | Under section 488.1(5), does a document that the judge has determined to be privileged remain privileged and inadmissible as evidence? | `s 488.1(5) the document remains privileged and inadmissible as evidence` |
| 30 | s 488.1(8) | Under section 488.1(8), is an officer barred from examining, copying or seizing a document without giving a reasonable opportunity for a claim of solicitor-client privilege to be made? | `s 488.1(8) the officer is barred from examining, making copies of or seizing the document` |
| 31 | s 489(1) | Under section 489(1), may a person executing a search warrant seize things that the warrant does not mention? | `s 489(1) the person who executes a warrant may seize the thing in addition to the things mentioned in the warrant` |
| 32 | s 489.1(1) | Under section 489.1(1), must the peace officer return the thing seized, on being issued a receipt, to the person lawfully entitled to its possession, because there is no dispute about who is entitled to it and it is not needed for any investigation or proceeding? | `s 489.1(1) what the peace officer shall do as soon as is practicable` |
| 33 | s 490(1) | Under section 490(1), must the justice order the thing seized returned to the lawful owner or the person lawfully entitled to possession, unless the prosecutor or the officer satisfies the justice that its detention is required? | `s 490(1) the order the justice shall make` |
| 34 | s 490(2) | Under section 490(2), is the detention of the thing seized from me barred, because more than 180 days have passed since the day of the seizure and no extension has been ordered and no proceedings have been started? | `s 490(2) the section bars detaining the thing for more than 180 days after the day of the seizure` |
| 35 | s 490(2) | Under section 490(2), what is the last day on which the thing seized from me may be detained without a further order, counting 180 days from the day of the seizure? | `s 490(2) the last day on which the thing may be detained without a further order` |
| 36 | s 490(3) | Under section 490(3), is the detention of the thing seized from me barred, because more than one year has passed since the day of the seizure and no judge has ordered further detention and no proceedings have been started? | `s 490(3) the section bars detaining the thing for more than one year from the day of the seizure` |
| 37 | s 490(7) | Under section 490(7), may I, the person from whom the thing was seized, apply summarily to a justice or judge for an order that it be returned to me? | `s 490(7) the person from whom anything has been seized may apply summarily for an order under paragraph (9)(c) that the thing be returned` |
| 38 | s 490(9) | Under section 490(9), must the justice or judge order the thing seized returned to me, the person from whom it was seized, because my possession of it was lawful? | `s 490(9) the order the judge or justice shall make` |
| 39 | s 490(12) | Under section 490(12), must nothing be returned, forfeited or disposed of while an application or appeal is pending or within 30 days after an order is made? | `s 490(12) nothing shall be returned, forfeited or disposed of` |
| 40 | s 490.01 | Under section 490.01(b), may the person who seized a perishable thing of mine dispose of it or destroy it, with a justice's authorization given on an ex parte application? | `s 490.01(b) the person may dispose of the thing, or destroy it` |
| 41 | s 490.011(1) | Under section 490.011(1), is my offence a designated offence (a primary or a secondary offence)? | `s 490.011(1) designated offence` |
| 42 | s 490.012(1) | Under section 490.012(1), must the court, when it sentences me, order me to comply with the Sex Offender Information Registration Act, because I was prosecuted by indictment, sentenced to two years or more, and the victim was under 18? | `s 490.012(1) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` |
| 43 | s 490.012(2) | Under section 490.012(2), must the court, when it sentences me, order me to comply with the Sex Offender Information Registration Act, because the prosecutor establishes that I was previously convicted of a primary offence or was already subject to an order or obligation to comply? | `s 490.012(2) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` |
| 44 | s 490.012(3) | Under section 490.012(3), must the court order me to comply with the Sex Offender Information Registration Act, unless I establish that there would be no connection to the purpose of the Act or that the impact on me would be grossly disproportionate? | `s 490.012(3) the court shall make an order in Form 52 requiring the person to comply with the Sex Offender Information Registration Act` |
| 45 | s 490.013 | Under section 490.013, does the order to comply with the Sex Offender Information Registration Act apply to me for life? | `s 490.013 the duration of the order` |
| 46 | s 490.013(2) | Under section 490.013(2), on what day does my order to comply with the Sex Offender Information Registration Act end, if it lasts 10 or 20 years? | `s 490.013(2) the day on which the order ends` |
| 47 | s 490.014 | Under section 490.014, may I appeal from the court's decision about an order under section 490.012 or 490.013, on a question of law or of mixed law and fact? | `s 490.014 the person may appeal from the decision of the court` |
| 48 | s 490.015(1) | Under section 490.015(1), may I now apply for a termination order, because five, ten or twenty years (according to how long my order lasts) have elapsed since it was made? | `s 490.015(1) the person may apply for a termination order` |
| 49 | s 490.015(1) | Under section 490.015(1), on what day may I first apply for a termination order, counting five, ten or twenty years from the day my order was made? | `s 490.015(1) the earliest day on which the person may apply for a termination order` |
| 50 | s 490.016(1) | Under section 490.016(1), must the court make a termination order, because I have established that continuing my order has no connection to the purpose of the Act or would have a grossly disproportionate impact on me? | `s 490.016(1) the court shall make a termination order` |
| 51 | s 490.018(4) | Under section 490.018(4), on what day is the earliest on which the person in charge of the place where I am held must give me a copy of the order, counting ten days before my release or discharge? | `s 490.018(4) the earliest day on which the person in charge shall give the person a copy of the order` |
| 52 | s 490.019 | Under section 490.019, must I comply with the Sex Offender Information Registration Act because I was served with a notice in Form 53, unless a court has made an exemption order? | `s 490.019 the person shall comply with the Sex Offender Information Registration Act` |

### Seat-question audit (brief's direction audit, and the second pass of 2026-11-12)

The brief asks for a list of every seat question whose name and body differ in direction or in subject, and for each to be fixed; no earlier audit was recorded in this file, so this pass is both the first and the second.
I read each question's `@export` text and its question name (the `DECIDE` name) against the BODY of the layer-1 function it calls, not against its own title: the function's branches, its inputs, what it answers on each branch, and the quoted text.
Retitle only when one of the four tightened criteria holds: (1) a different limb, route or scope; (2) a premise, qualifier or consequence the function does not compute or the text does not say; (3) the polarity or the modal is wrong; (4) the type of answer differs.

**Counts.** Seat questions read: **52**. Mismatched and retitled: **12** (direction: **0** permission-over-bar or bar-over-permission; modal: **1**, question 51; subject, limb, section or premise: **11**). Read and left: **40**. Assertions restated in place (`-- RECONCILED 2026-11-12`): **13** (the five questions whose question name changed: 26, 32, 37, 45 and 51; the other seven retitles changed the `@export` text only and broke no assertion).
Every `JUST FALSE` and `NOTHING` answer in a `CONSIDER` wrapper of the seat file (5 and 7) carries its `FALSE-kind` quote or `NOTHING-kind` reason; `work/lint.py` checked the quotes against the text.

#### Retitled (12), with the old and the new text exactly

- **Question 2** (`@ref s 487.051(1)`): scope (criterion 1): the title names one status, "convicted"; the body answers the five ways the person can stand (convicted, discharged under section 730, found guilty under the Youth Criminal Justice Act or the Young Offenders Act) and gives `NOTHING` for the rest.
  - was `@export`: Under section 487.051(1), must the court order me to give samples of my bodily substances for DNA analysis, because I was convicted of a primary designated offence of the kind in paragraphs (a) and (c.02)?
  - now `@export`: Under section 487.051(1), must the court order me to give samples of my bodily substances for DNA analysis, because my offence is a primary designated offence within paragraph (a) or (c.02) of the definition?
  - question name (unchanged): `Under section 487.051(1), must the court order me to give samples of my bodily substances for DNA analysis because my offence is a primary designated offence within paragraph (a) or (c.02)`
- **Question 3** (`@ref s 487.051(2)`): scope (criterion 1): as question 2, for subsection (2).
  - was `@export`: Under section 487.051(2), must the court order me to give samples of my bodily substances for DNA analysis, because I was convicted of a primary designated offence of the other kinds, unless I show that the order would be grossly disproportionate?
  - now `@export`: Under section 487.051(2), must the court order me to give samples of my bodily substances for DNA analysis, because my offence is a primary designated offence within the other paragraphs, unless I show that the order would be grossly disproportionate?
  - question name (unchanged): `Under section 487.051(2), must the court order me to give samples of my bodily substances for DNA analysis because my offence is a primary designated offence within the other paragraphs`
- **Question 4** (`@ref s 487.051(3)`): scope (criterion 1): the title names "convicted of a secondary designated offence"; paragraph (b) also covers the discharged and the young, and (a) the finding of not criminally responsible on account of mental disorder.
  - was `@export`: Under section 487.051(3), may the court order me to give samples of my bodily substances for DNA analysis, because I was found not criminally responsible for a designated offence or convicted of a secondary designated offence?
  - now `@export`: Under section 487.051(3), may the court order me to give samples of my bodily substances for DNA analysis?
  - question name (unchanged): `Under section 487.051(3), may the court order me to give samples of my bodily substances for DNA analysis`
- **Question 19** (`@ref s 487.2`): premise (criterion 2): "my consent" and "my identity"; the text, and the function, turn on "the consent of every person referred to in paragraph (b)" and on the identity of any person who occupies the place or is suspected.
  - was `@export`: Under section 487.2, is it an offence, without my consent, to publish or broadcast the location of the place searched under a search warrant or my identity as the person who occupies it or is suspected, before any charge is laid?
  - now `@export`: Under section 487.2, is it an offence to publish or broadcast the location of the place searched under a search warrant, or the identity of a person who occupies it or is suspected, without the consent of every person referred to in paragraph 487.2(b), before a charge is laid?
  - question name (unchanged): `Under section 487.2, is it an offence to publish the location of the place searched or the identity of a person without consent before a charge is laid`
- **Question 22** (`@ref s 488.01(2)`): premise (criterion 2): "and to no one else" is the exclusive-jurisdiction rule of a different function (`s 488.01(2) the judge has exclusive jurisdiction to dispose of the application`); this function answers only where the application is made.
  - was `@export`: Under section 488.01(2), must the police apply to a judge of a superior court of criminal jurisdiction (or a judge as defined in section 552), and to no one else, for a warrant, authorization or order that relates to my communications as a journalist?
  - now `@export`: Under section 488.01(2), must the police apply to a judge of a superior court of criminal jurisdiction (or a judge as defined in section 552) for a warrant, authorization or order that relates to a journalist?
  - question name (unchanged): `Under section 488.01(2), must the police apply to a superior court judge for a warrant, authorization or order that relates to a journalist`
- **Question 26** (`@ref s 488.1(2)`): limb (criterion 1): the title adds the custody limb, paragraph (b), which is a different function (`s 488.1(2)(b) the package shall be placed in the custody of`); this function answers paragraph (a), the seizure and sealed package.
  - was `@export`: Under section 488.1(2), must an officer, without examining or copying my document, seize it and place it in a sealed package in the custody of the sheriff or a person agreed in writing, because my lawyer claims solicitor-client privilege for it?
  - now `@export`: Under section 488.1(2), must an officer, without examining or copying the document, seize it and place it in a sealed and identified package, because the lawyer claims solicitor-client privilege for it?
  - was question name: `Under section 488.1(2), must the officer seal the document and place it in custody without examining or copying it when the lawyer claims solicitor-client privilege`
  - now question name: `Under section 488.1(2), must the officer, without examining or copying the document, seize it and place it in a sealed and identified package when the lawyer claims solicitor-client privilege`
- **Question 32** (`@ref s 489.1(1)`): premise (criterion 2): "to me"; the text and the function say "to the person lawfully entitled to its possession", and nothing in the inputs says that is the asker.
  - was `@export`: Under section 489.1(1), must the peace officer return the thing seized to me, on being issued a receipt, because there is no dispute about who is entitled to it and it is not needed for any investigation or proceeding?
  - now `@export`: Under section 489.1(1), must the peace officer return the thing seized, on being issued a receipt, to the person lawfully entitled to its possession, because there is no dispute about who is entitled to it and it is not needed for any investigation or proceeding?
  - was question name: `Under section 489.1(1), must the peace officer return the thing seized to me on being issued a receipt`
  - now question name: `Under section 489.1(1), must the peace officer return the thing seized, on being issued a receipt, to the person lawfully entitled to its possession`
- **Question 33** (`@ref s 490(1)`): premise (criterion 2): "to me, the lawful owner"; the function's paragraph (a) returns the thing to "the lawful owner or the person lawfully entitled to possession".
  - was `@export`: Under section 490(1), must the justice order the thing seized returned to me, the lawful owner, unless the prosecutor or the officer satisfies the justice that its detention is required?
  - now `@export`: Under section 490(1), must the justice order the thing seized returned to the lawful owner or the person lawfully entitled to possession, unless the prosecutor or the officer satisfies the justice that its detention is required?
  - question name (unchanged): `Under section 490(1), must the justice order the thing seized returned to the lawful owner unless detention is shown to be required`
- **Question 37** (`@ref s 490(7)`): route (criterion 1): the title says "now that the periods of detention have expired"; the body also answers `JUST TRUE` on the subsection (8) route (the court has allowed an early application).
  - was `@export`: Under section 490(7), may I, the person from whom the thing was seized, apply to a justice or judge for an order that it be returned to me, now that the periods of detention have expired?
  - now `@export`: Under section 490(7), may I, the person from whom the thing was seized, apply summarily to a justice or judge for an order that it be returned to me?
  - was question name: `Under section 490(7), may I apply for an order that the thing seized from me be returned now that the periods of detention have expired`
  - now question name: `Under section 490(7), may I apply summarily for an order that the thing seized from me be returned`
- **Question 41** (`@ref s 490.011(1)`): premise (criterion 2): "the offence I was convicted of, or found not criminally responsible for"; the definition ("designated offence means a primary offence or a secondary offence") says nothing of conviction or verdict.
  - was `@export`: Under section 490.011(1), is the offence I was convicted of, or found not criminally responsible for, a designated offence (a primary or a secondary offence)?
  - now `@export`: Under section 490.011(1), is my offence a designated offence (a primary or a secondary offence)?
  - question name (unchanged): `Under section 490.011(1), is my offence a designated offence, that is a primary or a secondary offence`
- **Question 45** (`@ref s 490.013`): section (criterion 1): the title names subsection 490.013(2); the body is the whole-section duration function `s 490.013 the duration of the order`, which also reads subsections (3) to (5).
  - was `@export`: Under section 490.013(2), does the order to comply with the Sex Offender Information Registration Act apply to me for life?
  - now `@export`: Under section 490.013, does the order to comply with the Sex Offender Information Registration Act apply to me for life?
  - was question name: `Under section 490.013(2), does the order to comply with the Sex Offender Information Registration Act apply to me for life`
  - now question name: `Under section 490.013, does the order to comply with the Sex Offender Information Registration Act apply to me for life`
- **Question 51** (`@ref s 490.018(4)`): modal (criterion 3): "may give" over a duty; the text says "shall give the person a copy of the order not earlier than 10 days before their release or discharge" and the function is named "shall give".
  - was `@export`: Under section 490.018(4), on what day is the earliest that the person in charge of the place where I am held may give me a copy of the order, ten days before my release or discharge?
  - now `@export`: Under section 490.018(4), on what day is the earliest on which the person in charge of the place where I am held must give me a copy of the order, counting ten days before my release or discharge?
  - was question name: `Under section 490.018(4), on what day is the earliest that I may be given a copy of the order before my release or discharge`
  - now question name: `Under section 490.018(4), on what day is the earliest on which the person in charge must give me a copy of the order before my release or discharge`

#### Read and left (40), one line of reason each

| # | `@ref` | reason |
| --- | --- | --- |
| 1 | s 487.05(1) | title restates the function's own name ("may ... issue a warrant"); the grounds are inputs |
| 5 | s 487.054 | title restates the function's own name; the offender status is its input |
| 6 | s 487.055(1) | "because ..." restates the section's own grounds, which the function tests as inputs; the question name omits them |
| 7 | s 487.0552(1) | title restates the offence's own elements, which the function tests as inputs |
| 8 | s 487.0552(1) | answer type agrees: a number of years; the function returns the years of the longest term on indictment |
| 9 | s 487.07(1) | duty ("must tell") over a duty; the matter asked is paragraph (e)(i) |
| 10 | s 487.07(2) | title restates the text's own limb ("for a period that is reasonable in the circumstances"), tested as an input |
| 11 | s 487.071(2) | bar over a bar; "because ... profile" is the text's own "If", tested as an input |
| 12 | s 487.09(1) | duty over a duty; scope as the function (taken under a DNA warrant) |
| 13 | s 487.09(1)(c) | answer type agrees: a day; "after which ... must be destroyed" identifies the year of paragraph (c) in the text's words |
| 14 | s 487.091(1) | "because ..." restates the two grounds of paragraphs (a) and (b), which the function tests |
| 15 | s 487.092(1) | wording only ("such as a fingerprint" is a gloss) |
| 16 | s 487.093(1) | wording only ("leave them in a prominent place" for "affix them") |
| 17 | s 487.1(5) | wording only ("the police" for "the applicant") |
| 18 | s 487.11 | "because ... exigent circumstances" restates the text's own gate, tested as an input |
| 20 | s 487.3(1) | wording only ("prohibit" for "make an order prohibiting") |
| 21 | s 488 | permission over a permission: the function is named "may be executed" |
| 23 | s 488.01(3) | polarity agrees ("only if"); "my" for "the" is wording |
| 24 | s 488.02(3) | title restates the text's own period and the journalist as the function's applicant input |
| 25 | s 488.02(3) | answer type agrees: a day |
| 27 | s 488.1(3)(a) | title restates the text's own period and notice, tested as inputs |
| 28 | s 488.1(3)(a) | answer type agrees: a day |
| 29 | s 488.1(5) | title restates the text's own gate ("Where the judge determines"), tested as an input |
| 30 | s 488.1(8) | bar over a bar |
| 31 | s 489(1) | grant over a grant |
| 34 | s 490(2) | bar over a bar; "more than 180 days" is the function's own name, and the "unless" limbs are tested as inputs |
| 35 | s 490(2) | answer type agrees: a day; the function's own name |
| 36 | s 490(3) | as question 34, for one year |
| 38 | s 490(9) | title is limb (c) in the text's words ("possession ... lawful"), the limb the function returns `JUST TRUE` for |
| 39 | s 490(12) | bar over a bar |
| 40 | s 490.01 | grant over a grant; the justice's authorization is an input |
| 42 | s 490.012(1) | the three grounds of paragraphs (a) to (c) are the text's own "if", tested as inputs |
| 43 | s 490.012(2) | the two grounds of (a) and (b) are the text's own, tested as inputs |
| 44 | s 490.012(3) | the "unless" is the text's own and the function tests it |
| 46 | s 490.013(2) | answer type agrees: a day; "if it lasts 10 or 20 years" is the function's domain |
| 47 | s 490.014 | grant over a grant |
| 48 | s 490.015(1) | the period gate is the text's own, tested as inputs |
| 49 | s 490.015(1) | answer type agrees: a day |
| 50 | s 490.016(1) | the "if it is satisfied" gate is the text's own; "I have established" for the court's satisfaction is wording |
| 52 | s 490.019 | the notice and the "unless" are the text's own, tested as inputs |

The inputs' `@desc` texts were not changed: none of them carried the mismatched premise.

### Name-test sweep of 2026-11-12

The class: a layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to", "the court may ...") that answers `JUST FALSE` because an "if" gate failed reads as "may not".
I applied the three tests of `name-test-sweep.md` to every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorised/authorized" (I also took the stem "authoris/authoriz", so "authorization" counts): 86 of the 262 layer-1 functions; 25 of them answer `JUST FALSE` on some branch, and the other 61 answer `NOTHING` or a date, a court or a number only, so there was nothing to flip.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 0 | 13 | 12 | 0 |

- **Flipped to `NOTHING` by the sweep: none.** The ruling of 2026-11-12 was part of my brief from the start, so the 27 grants named "may" and conditioned by the text (fork F1, listed in the fork register) answer `NOTHING` on a failed condition (checked on the files as they stand); the sweep changed no answer and no assertion needed restating for it.
- **Kept `JUST FALSE`, gate closed by the text (8 grants and 5 bars or duties, 13 in all):** test 2 ("only if", "only where", "may not ... unless", a flat negative; a bar, a duty, or the provision's own question):
  - `s 487.05(4) the warrant may be executed by the peace officer at the place` -- a bare "must" in the text's second sentence (fork F14)
  - `s 487.092(3) the warrant may be executed by the peace officer at the place` -- a bare "must" in the text's second sentence (fork F14)
  - `s 488.01(3) the judge may issue the warrant, authorization or order` -- "only if"
  - `s 488.02(5) the judge may order the disclosure of the document` -- "only if"
  - `s 487.1(5) the applicant may submit the application by a means of telecommunication that does not produce a writing` -- "only if"
  - `s 488 the warrant may be executed at the time of day` -- "shall be executed by day, unless"
  - `s 490.012(5) the court may make an order in respect of the offence` -- "only if"
  - `s 490.015(5) the person may re-apply for a termination order` -- "they may not re-apply under this subsection if" (a flat negative)
  - and, named with the stem "authorization" but not for a grant, the 5 bars or duties:
    - `s 487.1(9) the judicial officer is barred from issuing the warrant, order, extension or authorization` -- a bar ("shall not issue ... unless")
    - `s 487.071(2) the peace officer shall confirm in writing on the order or authorization that they have been advised that the profile is in the data bank and transmit a copy to the Commissioner of the Royal Canadian Mounted Police` -- a duty
    - `s 487.071(3) the peace officer shall execute the order or authorization and transmit the bodily substances taken and a copy to the Commissioner of the Royal Canadian Mounted Police` -- a duty
    - `s 487.0911(2) the Attorney General shall apply ex parte to have the order or authorization corrected` -- a duty
    - `s 487.0911(2)(b) the Attorney General shall transmit a copy of the corrected order or authorization to the Commissioner` -- a duty
  - The two grants of F14 (`s 487.05(4)`, `s 487.092(3)`) are the closest calls: their second sentence is a bare "must", not an "if" or an "only if", so they carry a fork line (F14, with the other reading `NOTHING`) in the fork register and in the marginal readings below.
- **Listed, not flipped: "may" with a where/when/upon-kind gate (12):** group G1 of the fork register lists each with its gate and the other reading. They answer `JUST FALSE`, as ruling (b) of the periods paragraph says; the guide's line on grants points the other way, so the choice is for the maintainer or a lawyer.
  - `s 487.051(4) the court may make an order in Form 5.041 requiring the person to report and submit to the taking of the samples`
  - `s 487.053(1) the court may make an order under section 487.051 at this time`
  - `s 487.053(2)(c) the court may require the person to appear by closed-circuit television or videoconference`
  - `s 487.055(3.01) the court may require the person to appear by closed-circuit television or videoconference`
  - `s 490.0132(c) the court may require the person to appear at the hearing by videoconference`
  - `s 488.02(3) the journalist or media outlet may apply to a judge of the court that issued the warrant, authorization or order for an order that the document is not to be disclosed to an officer`
  - `s 488.1(3)(a) the person may apply to a judge for an order appointing a place and a day for the determination of the question and requiring the custodian to produce the document`
  - `s 488.1(7) subsequent applications under paragraph (3)(c) may be made to another judge`
  - `s 490(7) the person from whom anything has been seized may apply summarily for an order under paragraph (9)(c) that the thing be returned`
  - `s 490(8) the judge or justice may allow an application under subsection (7) to be made before the expiration of the periods`
  - `s 490(10) the claimant may at any time apply summarily for an order that the thing detained be returned to the applicant`
  - `s 490(15) the judge may order that the person be permitted to examine anything so detained`
- **Listed: "entitled"-named functions: 0.** (Group G2 of the fork register; the word occurs here only inside the phrase "lawfully entitled to possession".)
- **Outside the sweep: named "it is lawful ...": 0.** "it is lawful, scoped" (a name such as "s N makes it lawful ..."): 0; "it is lawful, unscoped and retitled": 0. No function of this part is named "it is lawful"; the only function with "lawful" in its name, `s 487.0552(2) a lawful command that prevents the person from complying is a reasonable excuse`, is a rule about an excuse, not a justification, and keeps its answer (fork F3).
- Assertions restated by the sweep: 0. Callers: the sweep changed no input and no answer.

## What `check.sh` prints

Run from this folder on 2026-11-16 as `L4=<scratchpad>/bin/l4-main-110 L4_MAIN=<scratchpad>/bin/l4-main-109 ./check.sh`.

Baseline, run first on the resumed part before any edit of the day (the deposit as the interrupted run left it): TOTAL (19 modules), 0 errors, 1,257 assertions satisfied, 0 failed, 0 refused, the same on 1.6.110 and 1.6.109.
After the second-pass edits (seat retitles, 13 restated assertions, fork tags) it is the same TOTAL, shown in full below.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc17-cases-seat.l4                            0       147       0        0         0 |      0       147       0        0  same
ccc17-dna-orders.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc17-dna-samples.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc17-journalists.l4                           0         0       0        0         0 |      0         0       0        0  same
ccc17-privilege.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc17-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc17-seizure.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc17-sor.l4                                   0         0       0        0         0 |      0         0       0        0  same
ccc17-tests-dna-orders.l4                      0       174       0        0         0 |      0       174       0        0  same
ccc17-tests-dna-samples.l4                     0       146       0        0         0 |      0       146       0        0  same
ccc17-tests-journalists.l4                     0        84       0        0         0 |      0        84       0        0  same
ccc17-tests-privilege.l4                       0        73       0        0         0 |      0        73       0        0  same
ccc17-tests-seizure.l4                         0       129       0        0         0 |      0       129       0        0  same
ccc17-tests-sor.l4                             0       366       0        0         0 |      0       366       0        0  same
ccc17-tests-warrants.l4                        0       138       0        0         0 |      0       138       0        0  same
ccc17-warrants.l4                              0         0       0        0         0 |      0         0       0        0  same
TOTAL (19 modules)                             0      1257       0        0           |      0      1257       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit=0
```
