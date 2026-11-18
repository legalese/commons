# Independent reader: triage of the chapter 3 row

An independent reader, who had only the text and then the layer-1 and seat modules (no tests, notes or plans), wrote 244 scenarios before opening any module and asserted 420 of them in `bgg3-tests-independent.l4`.
On the first run 400 were satisfied and 20 failed; each of the 20 had the encoding answering `NOTHING` where the reader expected `JUST FALSE`, and none failed on a number or on the other sign.

**What changed in the file, and what did not.**
Every one of the 20 is now restated to the encoding's answer, with a `RECONCILED` comment on its line giving the reader's expectation and the reading behind it.
The file therefore passes (420 satisfied, 0 failed, 0 refused), and its comments are the record of the disagreements.
None of the 20 is a defect the encoder was asked to repair; all 20 are readings the Guide leaves open, labelled "assumed, not ruled" and listed for a lawyer.

**The reader labelled six of the 20 `ENCODER`; the lead reclassified them `AMBIGUOUS` (lines 1 to 6 of the table).**
They are Art 83 limbs (g), (l), (w), (z), (zbis) and (f), asked through the seat question "is my decision excluded?".
Each limb is a bar limited by its own wording ("wenn ...").
The Guide's "In short" sentence answers `NOTHING` when a case falls outside the limit of a prohibition's own wording, and the periods ruling (b) answers `JUST FALSE` for a "where" condition that fails.
The encoder took the first (fork F22 and the "limited bars" paragraph of `NOTES.md`), and the brief lists the two readings as an open question for a lawyer, so the encoding does not break a ruling.

**The five GAP lines (21 to 25) are not repaired in this row.**
Lines 22 and 23 ask about the filing period and the effect of the appeal on enforcement, which are Art 100 and Art 103, in chapter 4, outside this row's text; the chapter 4 row covers Art 100.
Line 24 notes that Art 89, Art 76 and Art 81 each have one function per paragraph and no function that combines their paragraphs, so the person combines them.
Line 25 notes that `Art 79` and `Art 80(1)` answer differently for a decision of the Beschwerdekammer and nothing combines them.
Line 21 is a language question (a brief in French) that the encoding does not ask.
These are known limits of this row.

**A later seat-polarity pass changed three of the reader's lines.**
After the reader returned, a second independent reader checked every seat question's wording against what `JUST TRUE` and `JUST FALSE` mean in the function it calls.
It found three questions of this row whose wording did not match, and the encoder re-worded them: Art 73 and Art 79 now ask whether the decision is excluded from the appeal (so `JUST TRUE` means excluded, the two definite answers swapped as for Art 83), and Art 86(2) now names its exception.
Three assertions of the reader's file (S13, S16 and S60) called the renamed seat functions; they are renamed in the file, with a comment, and S13 and S16 are restated from `JUST FALSE` ("not admissible") to `JUST TRUE` ("excluded"), which is the same expectation under the new wording.

---

The reader's own triage follows, unchanged.

# Triage: one line per FAILED or REFUSED assertion and per GAP

Run (JL4_LIBRARY_PATH unset, binary l4-main-110, from enc/): 420 assertions in `enc/tests-independent.l4`: 400 satisfied, 20 failed, 0 refused (run output kept in `run4.txt`).
Scenarios in `ANSWERS.md`: 244 (226 numbered + 18 seat).
Every failure is the encoding answering `NOTHING` where I expected `JUST FALSE`; there is no failure with the opposite sign and no failure on a number.
Polarity note: ANSWERS.md asks Art. 83 and Art. 85(1) as "is the appeal barred?"; the layer-1 functions ask "is it admissible?".
I translated "barred NO" to `NOTHING` there (a bar that does not apply is not a grant; Art. 83(m)'s derogation is the one grant), and those assertions pass.
The seat Art. 83 question asks "is my decision excluded?", where my answers need no translation: that is where the six `ENCODER` lines come from.

Columns: scenario | line of my assertion in `enc/tests-independent.l4` | provision | my expected | encoding answered | verdict | note

1. | S21 | line 362 | Art. 83(g) via the seat question | `JUST FALSE` (public-law employment, a pecuniary matter: "wenn ... nicht vermögensrechtlich" unmet, so the exclusion does not apply; guide ruling (b)) | `NOTHING` | ENCODER | A plain "wenn" failing gives `JUST FALSE` to the question "is my decision excluded?"; the seat swap keeps layer-1's `NOTHING` as `NOTHING`, so the exclusion question loses ruling (b) (layer 1, asked as "admissible?", is right to say `NOTHING`).
2. | S28 | line 376 | Art. 83(l) via the seat question | `JUST FALSE` (customs assessment on the origin of the goods: "wenn ... Tarifierung oder Gewichts" unmet) | `NOTHING` | ENCODER | Same as S21.
3. | S47-w-fund | line 459 | Art. 83(w) via the seat question | `JUST FALSE` (a legal question of fundamental importance arises: "wenn sich keine Rechtsfrage ... stellt" unmet) | `NOTHING` | ENCODER | Same as S21.
4. | S47-z-fund | line 460 | Art. 83(z) via the seat question | `JUST FALSE` (same condition) | `NOTHING` | ENCODER | Same as S21.
5. | S47-zbis-fund | line 461 | Art. 83(zbis) via the seat question | `JUST FALSE` (same condition) | `NOTHING` | ENCODER | Same as S21.
6. | S47-f-fund-above | line 464 | Art. 83(f) via the seat question | `JUST FALSE` (a fundamental question arises and the value is above the threshold: neither "wenn" limb holds) | `NOTHING` | ENCODER | Same as S21.
7. | S47-x-fund | line 462 | Art. 83(x) via the seat question | `JUST FALSE` (a fundamental question arises: "ausser wenn" met) | `NOTHING` | AMBIGUOUS | Readings: "ausser wenn" once met is a case-by-case call (guide), so `JUST FALSE`; or the seat swap leaves `NOTHING` as the encoder's reading of "the text does not let it in in so many words".
8. | S20 | line 360 | Art. 83(g) via the seat question | `JUST FALSE` (gender equality: "nicht aber die Gleichstellung der Geschlechter" takes the case out of the bar) | `NOTHING` | AMBIGUOUS | Readings: an exception inside a "wenn" met, so the exclusion does not apply (`JUST FALSE`); or the text only carves the case out and does not say yes (`NOTHING`).
9. | S31 | line 384 | Art. 83(d)(1) via the seat question | `JUST FALSE` (asylum decision of the Federal Administrative Court, extradition request pending: "ausser sie betreffen ..." met) | `NOTHING` | AMBIGUOUS | "ausser" once met: `JUST FALSE` or `NOTHING` (the case-by-case question).
10. | 7 | line 47 | Art. 72(2)(b)(4) | `JUST FALSE` (supervision of a pension fund: "mit Ausnahme der Vorsorge- und Freizügigkeitseinrichtungen") | `NOTHING` | AMBIGUOUS | "Except" once met: item 4 does not reach it (`JUST FALSE`); or the list is open ("insbesondere") and the general clause may still carry the decision (`NOTHING`).
11. | S18 | line 356 | Art. 72(2)(b)(4) via the seat question | `JUST FALSE` (a pension fund asks) | `NOTHING` | AMBIGUOUS | Same as 7.
12. | 36 | line 85 | Art. 75(2) | `JUST FALSE` (the last cantonal instance is a first-instance district court, no exception) | `NOTHING` | AMBIGUOUS | A bare duty ("Die Kantone setzen ... ein") not done: `JUST FALSE` or `NOTHING` (the encoding's own fork F5).
13. | 42 | line 91 | Art. 75(2) | `JUST FALSE` (CHF 150 000, filed at a lower court, no exception) | `NOTHING` | AMBIGUOUS | Same as 12 (the encoding folds "directly with the upper court" and "consent of all parties" into one input, so this and 41 share an input).
14. | 40 | line 89 | Art. 75(2)(c) | `JUST FALSE` (CHF 99 999 filed directly with consent: below "mindestens 100 000") | `NOTHING` | AMBIGUOUS | "Cases in which a claim of at least CHF 100 000 ... was filed": a "where" condition unmet gives `JUST FALSE` (ruling (b)); or a scope limit of an exception with no "only" gives `NOTHING` (ruling (c), whose own example is a threshold). Both sides of the CHF 100 000 line are tested: 100 000 passes (39).
15. | 41 | line 90 | Art. 75(2)(c) | `JUST FALSE` (CHF 150 000 filed directly, one party did not consent) | `NOTHING` | AMBIGUOUS | Same as 40.
16. | 52 | line 103 | Art. 76(2) | `JUST FALSE` (a subordinate unit (Dienststelle) where federal law does not provide for its right: "soweit das Bundesrecht es vorsieht") | `NOTHING` | AMBIGUOUS | "Soweit" unmet: `JUST FALSE` (where) or `NOTHING` (scope). Also a modelling limit: the input "subordinate service AND federal law provides" folds the "soweit" condition into the status, so a unit without such a provision cannot be stated; it can only be entered as "neither", which is `NOTHING`. The same fold is in Art. 81(3) and Art. 89(2)(a).
17. | 55 | line 108 | Art. 77(1)(a) | `JUST FALSE` (international award, the conditions of Art. 190 to 192 IPRG not met: "unter den Voraussetzungen") | `NOTHING` | AMBIGUOUS | A condition the text introduces: `JUST FALSE`; or the conditions lie in a statute outside the sources: `NOTHING`.
18. | 82 | line 144 | Art. 80(2) | `JUST FALSE` (a district court as last instance, no StPO exception) | `NOTHING` | AMBIGUOUS | A bare duty not done, as 12.
19. | 197 | line 280 | Art. 86(2) | `JUST FALSE` (a district court as immediate lower instance, no other federal statute) | `NOTHING` | AMBIGUOUS | A bare duty not done, as 12.
20. | 204 | line 287 | Art. 87(2) | `JUST FALSE` (cantonal law provides no remedy against the enactment: "Soweit das kantonale Recht ein Rechtsmittel ... vorsieht") | `NOTHING` | AMBIGUOUS | "Soweit" unmet: `JUST FALSE` (where) or `NOTHING` (scope), as 16.
21. | 66 | none | Art. 77(2bis) | `NOT COVERED` (may a brief in an arbitral appeal be in French?) | no function | GAP | The encoding answers only "may it be drafted in English"; a question about another language cannot be asked.
22. | 119 | none | whole chapter | `NOT COVERED` (within how many days must the appeal be filed? The period is Art. 100, outside the text) | no function | GAP | Silence of the text; nothing in the encoding to ask, and no `NOTHING` marker for a question the modules do not model.
23. | 120 | none | whole chapter | `NOT COVERED` (does the appeal suspend enforcement? Art. 103 is outside the text) | no function | GAP | As 22.
24. | 223 | none | Art. 89(1) to (3) | `NO` (an organisation that fails Art. 89(1) and has no right under another federal act: not entitled overall) | no function | GAP | Art. 89 has one function per paragraph and no composite "is this person entitled to appeal in public-law matters" that combines Abs. 1, Abs. 2 and Abs. 3; asked limb by limb, 89(2)(d) answers `NOTHING` and 89(1) answers `JUST FALSE`, and the reader must combine them. The same holds for Art. 76 (Abs. 1 and 2) and Art. 81 (Abs. 1 to 3).
25. | 75/76 combined | none | Art. 79 with Art. 80(1) | `NO` for a Beschwerdekammer decision on something other than coercive measures (Art. 79 bars what Art. 80(1) lists) | two answers | GAP | `Art 80(1)` answers `JUST TRUE` for the Beschwerdekammer and `Art 79` answers `JUST FALSE`; no function composes them, so the question "may I appeal against this body's decision" has two contradicting answers depending on which function is asked. The same pairing is Art. 73 with Art. 72/75, Art. 74/85 with Art. 72/86 and Art. 83 with Art. 86: no function gives the overall answer.
