# Independent expectations: Privy Council (Limitation of Appeals) Act 1968

Written from BRIEF.md and C1968A00036.txt only, before opening any .l4 file.

Question: "May I ask the Privy Council for leave to appeal from this decision?"
Answers below are in three values: **BARRED** (this Act says leave shall not / may not be asked),
**NOT BARRED** (this Act does not bar asking; it confers no right), **NOTHING** (the source does not answer).

| # | Facts | Expected | The Act's words |
|---|-------|----------|-----------------|
| 1 | High Court; on appeal from a State Supreme Court in non-federal jurisdiction; no Constitution / Cth law / instrument involved; proceeding began after commencement | NOT BARRED | s 3(1): "may be asked only in a matter in which ... (a) was given on appeal from a decision of the Supreme Court of a State given otherwise than in the exercise of federal jurisdiction; and (b) did not involve ..." — both limbs met |
| 2 | High Court; appeal from State SC non-federal; involved interpreting the Constitution; after commencement | BARRED | s 3(1)(b)(i) "did not involve the application or interpretation of: (i) the Constitution" fails |
| 3 | High Court; appeal from State SC non-federal; involved applying a Commonwealth Act; after commencement | BARRED | s 3(1)(b)(ii) "a law made by the Parliament" |
| 4 | High Court; appeal from State SC non-federal; involved only a regulation/by-law made under a Commonwealth Act; after commencement | BARRED | s 3(1)(b)(iii) "an instrument (including an ordinance, rule, regulation or by-law) made under a law made by the Parliament" |
| 5 | High Court; original jurisdiction (not on appeal from a State SC); no federal law; after commencement | BARRED | s 3(1)(a) not met: "only in a matter in which ... was given on appeal from a decision of the Supreme Court of a State" |
| 6 | High Court; on appeal from a State SC exercising federal jurisdiction; no federal law involved; after commencement | BARRED | s 3(1)(a) "otherwise than in the exercise of federal jurisdiction" not met |
| 7 | High Court; involved Cth law, not on appeal from State SC; proceeding commenced in a court before commencement | NOT BARRED | s 3(2): "(1) does not apply in respect of a decision of the High Court given in a proceeding that was commenced in a court before the commencement of this Act" |
| 8 | Federal Court of Australia (not HC); proceeding began before commencement | BARRED | s 4: "shall not be asked from a decision of a Federal Court (not being the High Court)". s 4 has NO transitional saving like s 3(2), so pre-commencement does not help |
| 9 | Supreme Court of a Territory; after commencement | BARRED | s 4 "or of the Supreme Court of a Territory" — "whether special leave or otherwise" |
| 10 | Some other court (e.g. a State Supreme Court, appeal direct to the Privy Council); any facts | NOT BARRED | The Act addresses only HC (s 3) and Federal/Territory courts (s 4). Brief: "Where it does not bar asking, the answer is that this Act does not bar it." |
| 11 | Federal court, with HC-only inputs set favourably (appeal from State SC non-federal, no federal law) | BARRED | s 4 — HC-only facts are irrelevant |

## Points where my reading may differ from the brief

- The brief lists "whether it involved applying or interpreting the Constitution, a Commonwealth law or an instrument" as one input. Fine; the Act treats the three as alternatives under (b), any one of which defeats (b).
- Scenario 10: one could argue the Act "does not answer" (NOTHING) for other courts. I read the brief's rule "Where it does not bar asking, the answer is that this Act does not bar it" as covering this: NOT BARRED. If the encoding returns NOTHING there, I treat that as a defensible alternative, but flag it.
- s 4 has no pre-commencement saving (scenario 8). An encoding that applies s 3(2) to s 4 would be wrong.
- Neither section creates a right to appeal; NOT BARRED is not "may appeal".
