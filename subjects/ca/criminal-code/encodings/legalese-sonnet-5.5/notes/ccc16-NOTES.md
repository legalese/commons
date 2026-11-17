# NOTES.md -- ccc16: the Criminal Code (Canada), R.S.C., 1985, c. C-46, lines 8719-9543 (ss 483 to 487.04, Part XV opening)

Part agent ccc16, run `dst-ccc16`, Sonnet 5.5, on the stable binary 1.6.110 (cross-checked on 1.6.109 by `check.sh`).
Layer 1 is seven modules `ccc16-*.l4` with tests `ccc16-tests-*.l4`; layer 2 is `ccc16-seat.l4` with `ccc16-cases-seat.l4`; they sit beside the keel's `ccc-core.l4`, `ccc-definitions.l4` and `ccc-interpretation.l4`, which are untouched.

## About the text, the seat and the brief

- **The text.** The source is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation current to 2026-09-30 (Open Government Licence - Canada). It is not the official text, and nothing here is claimed verified against the official text. The French equivalents in parentheses after a defined term are not encoded.
- **The seat.** A person who is, or may be, accused of an offence under the Criminal Code. Assumed, not ruled: Singapore's Penal Code is the model (the maintainer, 2026-11-09), but this is a plain seat layer with no charge-generator contract. There is never a seat for an official: provisions that address only a judge, justice, prosecutor or peace officer are asked for what they mean to the accused (what may be done to them, what they must be given, and when).
- **Brief over PLAN.** Where `PLAN.md` and the brief differ, the brief governs. The differences met: the brief's ruling of 2026-11-12 (a power named for a grant answers NOTHING on a failed "if" gate, three limits) is later than the plan; the brief's seat-question naming ("Under section N,") and its direction rule; and the plan's seam row for s 487.04 names functions "that agree with the input name", where this part's functions take the record `s 487.04 facts of the offence` (see Seams).
- **What this range holds.** Opening of Part XV: ss 483 to 485.2 (powers of officials, procedural irregularities, the summons under the Identification of Criminals Act), ss 486 to 486.71 (exclusion of the public, support persons and animals, testimony outside the court room, the accused not to cross-examine, publication bans, security of witnesses), ss 487 to 487.02 (search warrant, general warrant, preservation and production orders, assistance order) and s 487.04 (the definitions of the DNA designated offences, with long lists of offences by section).

### Reading a result: FALSE and NOTHING (ccc16)

- `JUST TRUE`: the text's own words cover the case (a power exists, a duty arises, a bar applies, an offence is made out).
- `JUST FALSE` is the text saying no in its own words, and only that: a definition that says "means"; a condition introduced with "if", "only if", "unless", "until", "where"; a period or maximum the text states; a list closed with "only"; a flat negative ("shall not", "is not required", "No adverse inference may be drawn"). In this row a `JUST FALSE` on a power reads "the section gives no such power on these facts", on a duty "the duty does not arise on these facts", and on a bar "the bar does not apply"; it never reads "unlawful".
- `NOTHING` is "not covered": a power whose "if" gate fails (ruling of 2026-11-12), a limit the text puts on a grant and the case falls outside it, a term left to another section, silence, a list not closed, a meaning left to the Youth Criminal Justice Act or another Act that is not among the sources. A caller never turns `NOTHING` into `FALSE`.
- Every branch that answers a "no" carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` (`work/lint.py` checks both, and that every quoted fragment occurs in the text).
- `REFUSE` does not exist on the stable binary; "not covered" is `NOTHING` or a constructor, asserted.

## Rulings applied (copied word for word from the brief)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Coverage (ccc16)

One row per unit of lines 8719-9543: 623 rows over 823 non-blank lines (`work/units.py`, `work/mkcov.py`; every non-blank line falls in some row, and the lines in no row number 0). Dispositions: encoded 420, fork 187, repealed or blank in this text 13, inert 3 (the Part heading, reason 1; s 487.021(1) and (2), reason 2: a parliamentary review of the Act's provisions that affects no one now), `out-of-scope` 0, `deferred` 0.
The audit count before the table was built from the text was 622 rows (the Part heading was in the first section row); the final count is 623 because the Part heading is its own row. The last column is the number of `#ASSERT`s that name the rule in the tests. Seventeen paragraph-head rows of s 487.04 show 0: their tests name the rows below them (one assertion per list row, `ccc16-tests-dna-rows.l4`) or the caller `s 487.04 the offence is a primary designated offence` / `a secondary designated offence` (the attempt and conspiracy limbs, 13 assertions in `ccc16-tests-dna-definitions.l4`); no other `encoded` or `fork` row lacks an assertion that names it. A `fork` row names its fork id(s) from the register below.

| unit | lines | disposition | L4 name | asserts |
| --- | --- | --- | --- | --- |
| PART XV; General Powers of Certain Officials | 8719-8721 | inert (reason 1: headings) | - | 0 |
| 483 | 8722-8723 | encoded | `s 483 the judge or provincial court judge may do alone what two or more justices are authorized to do` | 4 |
| 484 | 8724-8725 | encoded | `s 484 the judge or provincial court judge has the same power and authority to preserve order as the superior court of criminal jurisdiction` | 3 |
| 485(1) | 8726-8727 | encoded | `s 485(1) jurisdiction over the offence is lost by reason of the failure` | 3 |
| 485(1.1) | 8728-8729 | encoded | `s 485(1.1) jurisdiction over the accused is lost by reason of the failure to appear personally or in person` | 3 |
| 485(2) | 8730-8731 | fork (F1, F2, F3) | `s 485(2) the court, judge, provincial court judge or justice may issue a summons`; `s 485(2) the court, judge, provincial court judge or justice may issue a warrant for the arrest` | 7 |
| 485(3) | 8732-8733 | fork (F3) | `s 485(3) the proceedings are deemed to be dismissed for want of prosecution`; `s 485(3) the proceedings may be recommenced` | 9 |
| 485(4) | 8734-8735 | fork (F2) | `s 485(4) the court, judge, provincial court judge or justice may adjourn the proceeding and make an order` | 3 |
| 485(5) | 8736-8737 | encoded | `s 485(5) the provisions of Part XVI apply with such modifications as the circumstances require` | 2 |
| 485.1 | 8738-8739 | fork (F6) | `s 485.1 a new information or a new indictment in respect of the same transaction is barred` | 7 |
| 485.1(a) | 8740-8740 | fork (F6) | `s 485.1 a new information or a new indictment in respect of the same transaction is barred` | 7 |
| 485.1(b) | 8741-8741 | fork (F6) | `s 485.1 a new information or a new indictment in respect of the same transaction is barred` | 7 |
| 485.2(1) | 8742-8743 | fork (F1) | `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` | 5 |
| 485.2(1)(a) | 8744-8744 | fork (F1) | `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` | 5 |
| 485.2(1)(b) | 8745-8745 | fork (F1) | `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` | 5 |
| 485.2(1)(c) | 8746-8746 | fork (F1) | `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` | 5 |
| 485.2(2) | 8747-8748 | encoded | `s 485.2(2) subsection (1) applies in respect of the offender` | 4 |
| 485.2(3) | 8749-8750 | fork (F7) | `s 485.2(3) the application states the reasons required` | 2 |
| 485.2(4) | 8751-8752 | encoded | `s 485.2(4) the justice or judge may proceed ex parte to determine the application` | 2 |
| 485.2(5) | 8753-8754 | encoded | `s 485.2(5) the application may be made by the means of telecommunication` | 2 |
| 485.2(6) | 8755-8756 | encoded | `s 485.2(6) the person may make a statement in writing instead of swearing an oath`; `s 485.2(6) the statement is deemed to be a statement made under oath` | 5 |
| 485.2(7) | 8757-8758 | fork (F7) | `s 485.2(7) the summons has the contents required` | 4 |
| 485.2(7)(a) | 8759-8759 | fork (F7) | `s 485.2(7) the summons has the contents required` | 4 |
| 485.2(7)(b) | 8760-8760 | fork (F7) | `s 485.2(7) the summons has the contents required` | 4 |
| 485.2(7)(c) | 8761-8761 | fork (F7) | `s 485.2(7) the summons has the contents required` | 4 |
| 485.2(8) | 8762-8763 | fork (F7) | `s 485.2(8) the summons was served as required` | 6 |
| 486(1) | 8764-8765 | fork (F1, F8) | `s 486(1) the presiding judge or justice may order the exclusion of the public or that the witness testify behind a screen`; `s 486(1) the proceedings against the accused are held in open court` | 9 |
| 486(1.1) | 8766-8767 | encoded | `s 486(1.1) the application may be made to the judge or justice`; `s 486(1.1) when the application is made` | 8 |
| 486(2) | 8768-8769 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(a) | 8770-8770 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(b) | 8771-8771 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(c) | 8772-8772 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(d) | 8773-8773 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(e) | 8774-8774 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(f) | 8775-8775 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(g) | 8776-8776 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(2)(h) | 8777-8777 | encoded | `s 486(2) factor`; `s 486(2) the judge or justice must consider the factor` | 10 |
| 486(3) | 8778-8779 | fork (F8, F9) | `s 486(3) the judge or justice must state the reason for not making an order`; `s 486(3) the listed offences` | 11 |
| 486(4) | 8780-8781 | encoded | `s 486(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | 2 |
| 486.1(1) | 8782-8783 | fork (F5, F8, F9) | `s 486.1(1) the judge or justice must order that a support person or a support animal be permitted` | 7 |
| 486.1(1.1) | 8784-8785 | fork (F5, F8, F9) | `s 486.1(1.1) the judge or justice must order that a support person or a support animal be permitted for a victim`; `s 486.1(1.1) the proceedings are in respect of one of the offences the subsection names` | 12 |
| 486.1(1.2) | 8786-8787 | encoded | `s 486.1(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | 2 |
| 486.1(2) | 8788-8789 | fork (F1, F8) | `s 486.1(2) the judge or justice may order that a support person or a support animal be permitted for another witness` | 5 |
| 486.1(2.1) | 8790-8791 | encoded | `s 486.1(2.1) the application may be made to the judge or justice` | 8 |
| 486.1(3) | 8792-8793 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(a) | 8794-8794 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(b) | 8795-8795 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(c) | 8796-8796 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(d) | 8797-8797 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(e) | 8798-8798 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(f) | 8799-8799 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(3)(g) | 8800-8800 | encoded | `s 486.1(3) factor`; `s 486.1(3) the judge or justice must consider the factor` | 9 |
| 486.1(4) | 8801-8802 | fork (F5) | `s 486.1(4) the judge or justice is barred from permitting a witness to be a support person` | 3 |
| 486.1(5) | 8803-8804 | encoded | `s 486.1(5) the judge or justice may order that the support person and the witness not communicate with each other while the witness testifies` | 3 |
| 486.1(6) | 8805-8806 | encoded | `s 486.1(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | 2 |
| 486.1(7) | 8807-8808 | encoded | `s 486.1(7) the judge or justice must include the reasons for their decision, in writing, in the record` | 2 |
| 486.2(1) | 8809-8810 | fork (F5, F8, F9) | `s 486.2(1) the judge or justice must order that the witness testify outside the court room or behind a screen, at the option of the witness` | 5 |
| 486.2(1.1) | 8811-8812 | fork (F5, F8, F9) | `s 486.2(1.1) the judge or justice must order that the victim testify outside the court room or behind a screen, at the option of the witness` | 5 |
| 486.2(1.2) | 8813-8814 | encoded | `s 486.2(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | 2 |
| 486.2(2) | 8815-8816 | fork (F1, F8) | `s 486.2(2) the judge or justice may order that another witness testify outside the court room or behind a screen, at the option of the witness` | 4 |
| 486.2(2.1) | 8817-8818 | encoded | `s 486.2(2.1) the application may be made to the judge or justice` | 8 |
| 486.2(3) | 8819-8820 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(a) | 8821-8821 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(b) | 8822-8822 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(c) | 8823-8823 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(d) | 8824-8824 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(e) | 8825-8825 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(f) | 8826-8826 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(f.1) | 8827-8827 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(g) | 8828-8828 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(3)(h) | 8829-8829 | encoded | `s 486.2(3) factor`; `s 486.2(3) the judge or justice must consider the factor` | 11 |
| 486.2(4) | 8830-8831 | encoded | `s 486.2(4) the judge or justice must order that the witness testify in accordance with subsection (2)` | 2 |
| 486.2(5) | 8832-8833 | fork (F13, F5) | `s 486.2(5) the witness is barred from testifying outside the court room in accordance with the order` | 5 |
| 486.2(6) | 8834-8835 | encoded | `s 486.2(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | 2 |
| 486.2(7) | 8836-8837 | encoded | `s 486.2(7) the judge or justice must include the reasons for their decision, in writing, in the record` | 2 |
| 486.3(1) | 8838-8839 | fork (F5, F8, F9) | `s 486.3(1) the judge or justice must appoint counsel to conduct the cross-examination`; `s 486.3(1) the judge or justice must order that the accused not personally cross-examine the witness under 18` | 7 |
| 486.3(2) | 8840-8841 | fork (F5, F8, F9) | `s 486.3(2) the judge or justice must appoint counsel to conduct the cross-examination`; `s 486.3(2) the judge or justice must order that the accused not personally cross-examine the victim` | 6 |
| 486.3(2.1) | 8842-8843 | encoded | `s 486.3(2.1) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | 2 |
| 486.3(3) | 8844-8845 | fork (F1, F8) | `s 486.3(3) the judge or justice may order that the accused not personally cross-examine another witness`; `s 486.3(3) the judge or justice must appoint counsel to conduct the cross-examination` | 7 |
| 486.3(4) | 8846-8847 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(a) | 8848-8848 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(b) | 8849-8849 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(c) | 8850-8850 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(d) | 8851-8851 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(e) | 8852-8852 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(f) | 8853-8853 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4)(g) | 8854-8854 | encoded | `s 486.3(4) factor`; `s 486.3(4) the judge or justice must consider the factor` | 9 |
| 486.3(4.1) | 8855-8856 | encoded | `s 486.3(4.1) the application may be made to the judge or justice` | 8 |
| 486.3(5) | 8857-8858 | encoded | `s 486.3(5) an adverse inference may be drawn from the fact that counsel is, or is not, appointed under this section` | 2 |
| 486.3(6) | 8859-8860 | encoded | `s 486.3(6) the judge or justice must include the reasons for their decision, in writing, in the record` | 2 |
| 486.31(1) | 8861-8862 | fork (F1, F8) | `s 486.31(1) the judge or justice may order that information that could identify the witness not be disclosed in the course of the proceedings` | 5 |
| 486.31(2) | 8863-8864 | encoded | `s 486.31(2) the judge or justice may hold a hearing, and the hearing may be in private` | 2 |
| 486.31(3) | 8865-8866 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(a) | 8867-8867 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(b) | 8868-8868 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(c) | 8869-8869 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(d) | 8870-8870 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(e) | 8871-8871 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(e.1) | 8872-8872 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(f) | 8873-8873 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(g) | 8874-8874 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(h) | 8875-8875 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(i) | 8876-8876 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(3)(j) | 8877-8877 | encoded | `s 486.31(3) factor`; `s 486.31(3) the judge or justice must consider the factor` | 13 |
| 486.31(4) | 8878-8879 | encoded | `s 486.31(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | 2 |
| 486.4(1) | 8880-8881 | encoded | `s 486.4(1) the presiding judge or justice may make an order directing that information that could identify the victim or a witness not be published` | 2 |
| 486.4(1)(a) | 8882-8882 | encoded | `s 486.4(1)(a) the offence is one referred to in paragraph (a)`; `s 486.4(1)(a)(i) the listed offences` | 10 |
| 486.4(1)(i) | 8883-8883 | encoded | `s 486.4(1)(a) the offence is one referred to in paragraph (a)`; `s 486.4(1)(a)(i) the listed offences` | 10 |
| 486.4(1)(ii) | 8884-8884 | encoded | `s 486.4(1)(a) the offence is one referred to in paragraph (a)`; `s 486.4(1)(a)(i) the listed offences` | 10 |
| 486.4(1)(b) | 8885-8885 | encoded | `s 486.4(1)(b) two or more offences are dealt with in the same proceeding, at least one of which is an offence referred to in paragraph (a)` | 3 |
| 486.4(2) | 8886-8887 | fork (F12, F8) | `s 486.4(2)(a) the presiding judge or justice must inform the person of the right to make an application for the order`; `s 486.4(2)(b) the presiding judge or justice must make the order` (+1) | 11 |
| 486.4(2)(a) | 8888-8888 | fork (F12, F8) | `s 486.4(2)(a) the presiding judge or justice must inform the person of the right to make an application for the order` | 3 |
| 486.4(2)(b) | 8889-8889 | fork (F12, F8) | `s 486.4(2)(b) the presiding judge or justice must make the order` | 6 |
| 486.4(2)(c) | 8890-8890 | fork (F12, F8) | `s 486.4(2)(c) the presiding judge or justice must inform the witnesses and the victim of the order's existence and of their right to apply to revoke or vary it` | 2 |
| 486.4(2.1) | 8891-8892 | fork (F1, F9) | `s 486.4(2.1) the presiding judge or justice may make an order directing that information that could identify the victim not be published` | 3 |
| 486.4(2.2) | 8893-8894 | fork (F12, F8, F9) | `s 486.4(2.2) the subsection applies to the proceedings`; `s 486.4(2.2)(a) the presiding judge or justice must inform the victim of their right to make an application for the order` (+2) | 10 |
| 486.4(2.2)(a) | 8895-8895 | fork (F12, F8, F9) | `s 486.4(2.2)(a) the presiding judge or justice must inform the victim of their right to make an application for the order` | 2 |
| 486.4(2.2)(b) | 8896-8896 | fork (F12, F8, F9) | `s 486.4(2.2)(b) the presiding judge or justice must make the order` | 4 |
| 486.4(2.2)(c) | 8897-8897 | fork (F12, F8, F9) | `s 486.4(2.2)(c) the presiding judge or justice must inform the victim of the existence of the order and of their right to apply to revoke or vary it` | 2 |
| 486.4(3) | 8898-8899 | fork (F9) | `s 486.4(3) the judge or justice must make an order directing that information that could identify the person not be published` | 5 |
| 486.4(3.1) | 8900-8901 | encoded | `s 486.4(3.1)(a), (b) the presiding judge or justice must inquire`; `s 486.4(3.1)(c) the presiding judge or justice must advise the prosecutor of their duty under subsection (3.2)` | 5 |
| 486.4(3.1)(a) | 8902-8902 | encoded | `s 486.4(3.1)(a), (b) the presiding judge or justice must inquire` | 3 |
| 486.4(3.1)(b) | 8903-8903 | encoded | `s 486.4(3.1)(a), (b) the presiding judge or justice must inquire` | 3 |
| 486.4(3.1)(c) | 8904-8904 | encoded | `s 486.4(3.1)(c) the presiding judge or justice must advise the prosecutor of their duty under subsection (3.2)` | 2 |
| 486.4(3.2) | 8905-8906 | fork (F12) | `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.4(3.2) what the prosecutor informs the judge or justice of is complete` | 6 |
| 486.4(3.2)(a) | 8907-8907 | fork (F12) | `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.4(3.2) what the prosecutor informs the judge or justice of is complete` | 6 |
| 486.4(3.2)(b) | 8908-8908 | fork (F12) | `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.4(3.2) what the prosecutor informs the judge or justice of is complete` | 6 |
| 486.4(3.2)(c) | 8909-8909 | fork (F12) | `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.4(3.2) what the prosecutor informs the judge or justice of is complete` | 6 |
| 486.4(4) | 8910-8911 | encoded | `s 486.4(4) the order applies to the disclosure of information` | 5 |
| 486.4(4)(a) | 8912-8912 | encoded | `s 486.4(4) the order applies to the disclosure of information` | 5 |
| 486.4(4)(b) | 8913-8913 | encoded | `s 486.4(4) the order applies to the disclosure of information` | 5 |
| 486.4(5) | 8914-8915 | fork (F19) | `s 486.4(5) the order applies to the disclosure of information by the victim or witness` | 4 |
| 486.5(1) | 8916-8917 | fork (F1, F5, F8) | `s 486.5(1) the judge or justice may make an order directing that information that could identify the victim or witness not be published` | 7 |
| 486.5(2) | 8918-8919 | fork (F1, F8) | `s 486.5(2) the judge or justice may make an order directing that information that could identify the justice system participant not be published` | 6 |
| 486.5(2.1) | 8920-8921 | fork (F18) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)`; `s 486.5(2.1)(a) the listed offences` | 18 |
| 486.5(2.1)(a) | 8922-8922 | fork (F18) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)`; `s 486.5(2.1)(a) the listed offences` | 18 |
| 486.5(2.1)(b) | 8923-8923 | fork (F18) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)` | 18 |
| 486.5(2.1)(c) | 8924-8924 | fork (F18) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)`; `s 486.5(2.1)(c) the listed provisions of the Foreign Interference and Security of Information Act` | 18 |
| 486.5(2.1)(d) | 8925-8925 | fork (F18) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)`; `s 486.5(2.1)(c) the listed provisions of the Foreign Interference and Security of Information Act` | 18 |
| 486.5(3) | 8926-8927 | encoded | `s 486.5(3) the order applies to the disclosure of information` | 3 |
| 486.5(3)(a) | 8928-8928 | encoded | `s 486.5(3) the order applies to the disclosure of information` | 3 |
| 486.5(3)(b) | 8929-8929 | encoded | `s 486.5(3) the order applies to the disclosure of information` | 3 |
| 486.5(3.1) | 8930-8931 | fork (F19) | `s 486.5(3.1) the order applies to the disclosure of information by the victim, witness or justice system participant` | 4 |
| 486.5(4) | 8932-8933 | encoded | `s 486.5(4)(a) the applicant has applied as required`; `s 486.5(4)(b) the applicant has provided notice of the application` | 10 |
| 486.5(4)(a) | 8934-8934 | encoded | `s 486.5(4)(a) the applicant has applied as required` | 6 |
| 486.5(4)(b) | 8935-8935 | encoded | `s 486.5(4)(b) the applicant has provided notice of the application` | 4 |
| 486.5(5) | 8936-8937 | encoded | `s 486.5(5) the applicant has set out the grounds` | 2 |
| 486.5(5.1) | 8938-8939 | encoded | `s 486.5(5.1)(a), (b) the judge or justice must inquire`; `s 486.5(5.1)(c) the judge or justice must advise the prosecutor of their duty under subsection (8.2)` | 5 |
| 486.5(5.1)(a) | 8940-8940 | encoded | `s 486.5(5.1)(a), (b) the judge or justice must inquire` | 3 |
| 486.5(5.1)(b) | 8941-8941 | encoded | `s 486.5(5.1)(a), (b) the judge or justice must inquire` | 3 |
| 486.5(5.1)(c) | 8942-8942 | encoded | `s 486.5(5.1)(a), (b) the judge or justice must inquire`; `s 486.5(5.1)(c) the judge or justice must advise the prosecutor of their duty under subsection (8.2)` | 5 |
| 486.5(6) | 8943-8944 | encoded | `s 486.5(6) the judge or justice may hold a hearing, and the hearing may be in private` | 2 |
| 486.5(7) | 8945-8946 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(a) | 8947-8947 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(b) | 8948-8948 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(c) | 8949-8949 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(d) | 8950-8950 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(e) | 8951-8951 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(f) | 8952-8952 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(g) | 8953-8953 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(7)(h) | 8954-8954 | encoded | `s 486.5(7) factor`; `s 486.5(7) the judge or justice must consider the factor` | 10 |
| 486.5(8) | 8955-8956 | encoded | `s 486.5(8) the order may be subject to the condition` | 2 |
| 486.5(8.1) | 8957-8958 | fork (F12) | `s 486.5(8.1) the judge or justice must inform the victims, witnesses and justice system participants of the order's existence and of their right to apply to revoke or vary it` | 2 |
| 486.5(8.2) | 8959-8960 | fork (F12) | `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.5(8.2) what the prosecutor informs the judge or justice of is complete` | 5 |
| 486.5(8.2)(a) | 8961-8961 | fork (F12) | `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.5(8.2) what the prosecutor informs the judge or justice of is complete` | 5 |
| 486.5(8.2)(b) | 8962-8962 | fork (F12) | `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.5(8.2) what the prosecutor informs the judge or justice of is complete` | 5 |
| 486.5(8.2)(c) | 8963-8963 | fork (F12) | `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.5(8.2) what the prosecutor informs the judge or justice of is complete` | 5 |
| 486.5(9) | 8964-8965 | fork (F5) | `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` | 5 |
| 486.5(9)(a) | 8966-8966 | fork (F5) | `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` | 5 |
| 486.5(9)(b) | 8967-8967 | fork (F5) | `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` | 5 |
| 486.5(9)(c) | 8968-8968 | fork (F5) | `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` | 5 |
| 486.51(1) | 8969-8970 | encoded | `s 486.51(1) the prosecutor must make an application to vary or revoke the order on the person's behalf` | 3 |
| 486.51(2) | 8971-8972 | fork (F5) | `s 486.51(2) the court must vary or revoke the order without holding a hearing` | 3 |
| 486.51(3) | 8973-8974 | encoded | `s 486.51(3) the court must hold a hearing to determine whether the order should be varied or revoked` | 2 |
| 486.51(4) | 8975-8976 | encoded | `s 486.51(4) the court must take into account whether it is possible to vary the order in a manner that protects the privacy interests of any other person` | 2 |
| 486.51(5) | 8977-8978 | fork (F21) | `s 486.51(5) the applicant is required to provide notice of the application to vary or revoke the order to the accused` | 2 |
| 486.51(6) | 8979-8980 | fork (F21) | `s 486.51(6) the accused is permitted to make submissions in relation to the application` | 2 |
| 486.51(7) | 8981-8982 | encoded | `s 486.51(7) the prosecutor must notify the accused` | 2 |
| 486.6(1) | 8983-8984 | encoded | `s 486.6(1) the order is one made under any of subsections 486.4(1) to (3) or subsection 486.5(1) or (2)`; `s 486.6(1) the person is guilty of an offence punishable on summary conviction` (+1) | 17 |
| 486.6(1.1) | 8985-8986 | fork (F5) | `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` | 5 |
| 486.6(1.1)(a) | 8987-8987 | fork (F5) | `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` | 5 |
| 486.6(1.1)(b) | 8988-8988 | fork (F5) | `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` | 5 |
| 486.6(1.1)(c) | 8989-8989 | fork (F5) | `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` | 5 |
| 486.6(2) | 8990-8991 | encoded | `s 486.6(2) the order applies to prohibit the publication of information that could identify a victim, witness or justice system participant in those proceedings` | 2 |
| 486.7(1) | 8992-8993 | fork (F1, F10, F8) | `s 486.7(1) the presiding judge or justice may make an order to protect the security of a witness` | 7 |
| 486.7(2) | 8994-8995 | encoded | `s 486.7(2) the application may be made to the judge or justice` | 8 |
| 486.7(3) | 8996-8997 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(a) | 8998-8998 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(b) | 8999-8999 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(c) | 9000-9000 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(d) | 9001-9001 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(e) | 9002-9002 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(f) | 9003-9003 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(g) | 9004-9004 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(h) | 9005-9005 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(i) | 9006-9006 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(j) | 9007-9007 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(3)(k) | 9008-9008 | encoded | `s 486.7(3) factor`; `s 486.7(3) the judge or justice must consider the factor` | 13 |
| 486.7(4) | 9009-9010 | encoded | `s 486.7(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | 2 |
| 486.71 | 9011-9012 | fork (F21) | `s 486.71 the judge or justice is prohibited from making more than one order regarding the same witness` | 2 |
| 487(1) | 9013-9014 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | 7 |
| 487(1)(a) | 9015-9015 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | 7 |
| 487(1)(b) | 9016-9016 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | 7 |
| 487(1)(c) | 9017-9017 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | 7 |
| 487(1)(c.1) | 9018-9018 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | 7 |
| 487(1)(d) | 9019-9020 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place`; `s 487(1) the warrant may authorize the act` | 10 |
| 487(1)(e) | 9021-9021 | fork (F1) | `s 487(1) the justice may issue a warrant to search the building, receptacle or place`; `s 487(1) the warrant may authorize the act` | 10 |
| 487(2) | 9022-9023 | fork (F7) | `s 487(2) the officer who executes the warrant has the authority required`; `s 487(2) the warrant may be executed at the place` | 5 |
| 487(2.1) | 9024-9025 | encoded | `s 487(2.1) the person may do the act` | 6 |
| 487(2.1)(a) | 9026-9026 | encoded | `s 487(2.1) the person may do the act` | 6 |
| 487(2.1)(b) | 9027-9027 | encoded | `s 487(2.1) the person may do the act` | 6 |
| 487(2.1)(c) | 9028-9028 | encoded | `s 487(2.1) the person may do the act` | 6 |
| 487(2.1)(d) | 9029-9029 | encoded | `s 487(2.1) the person may do the act` | 6 |
| 487(2.2) | 9030-9031 | encoded | `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` | 6 |
| 487(2.2)(a) | 9032-9032 | encoded | `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` | 6 |
| 487(2.2)(b) | 9033-9033 | encoded | `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` | 6 |
| 487(2.2)(c) | 9034-9034 | encoded | `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` | 6 |
| 487(3) | 9035-9036 | encoded | `s 487(3) the search warrant may be in the form set out as Form 5` | 2 |
| 487(4) | 9037-9037 | repealed or blank in this text: the text shows `[Repealed, 2019, c. 25, s. 191]` | - | 0 |
| 487.01(1) | 9038-9039 | fork (F1) | `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` | 8 |
| 487.01(1)(a) | 9040-9040 | fork (F1) | `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` | 8 |
| 487.01(1)(b) | 9041-9041 | fork (F1) | `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` | 8 |
| 487.01(1)(c) | 9042-9042 | fork (F1) | `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` | 8 |
| 487.01(2) | 9043-9044 | encoded | `s 487.01(2) subsection (1) permits the act` | 2 |
| 487.01(3) | 9045-9046 | fork (F7) | `s 487.01(3) the warrant contains the terms and conditions required` | 3 |
| 487.01(4) | 9047-9048 | fork (F7) | `s 487.01(4) the warrant contains the privacy terms and conditions required` | 3 |
| 487.01(5) | 9049-9050 | encoded | `s 487.01(5) the provision applies, with such modifications as the circumstances require, to the warrant` | 18 |
| 487.01(5.1) | 9051-9052 | fork (F7) | `s 487.01(5.1) the warrant requires notice of the covert entry and search as required` | 3 |
| 487.01(5.2) | 9053-9054 | fork (F17, F2) | `s 487.01(5.2) the extension does not exceed three years`; `s 487.01(5.2) the judge may grant an extension of the period for giving notice` | 11 |
| 487.01(6) | 9055-9056 | fork (F7) | `s 487.01(6) the general warrant may be executed at the place`; `s 487.01(6) the peace officer who executes the general warrant has the authority required` | 5 |
| 487.01(7) | 9057-9057 | repealed or blank in this text: the text shows `[Repealed, 2022, c. 17, s. 17]` | - | 0 |
| 487.011 | 9058-9059 | encoded | `s 487.011 the definitions apply in the section` | 8 |
| 487.011 "computer data" | 9060-9060 | encoded | `s 487.011 computer data` | 3 |
| 487.011 "data" | 9061-9061 | encoded | `s 487.011 data` | 3 |
| 487.011 "document" | 9062-9062 | encoded | `s 487.011 document` | 3 |
| 487.011 "judge" | 9063-9063 | encoded | `s 487.011 judge` | 3 |
| 487.011 "public officer" | 9064-9064 | encoded | `s 487.011 public officer` | 5 |
| 487.011 "tracking data" | 9065-9065 | encoded | `s 487.011 tracking data` | 4 |
| 487.011 "transmission data" | 9066-9066 | encoded | `s 487.011 transmission data` | 7 |
| 487.011 transmission data (a) | 9067-9067 | encoded | `s 487.011 transmission data` | 7 |
| 487.011 transmission data (b) | 9068-9068 | encoded | `s 487.011 transmission data` | 7 |
| 487.011 transmission data (c) | 9069-9069 | encoded | `s 487.011 transmission data` | 7 |
| 487.012(1) | 9070-9071 | encoded | `s 487.012(1) the peace officer or public officer may make a demand to preserve computer data` | 4 |
| 487.012(2) | 9072-9073 | fork (F20) | `s 487.012(2) the peace officer or public officer may make the demand` | 5 |
| 487.012(2)(a) | 9074-9074 | fork (F20) | `s 487.012(2) the peace officer or public officer may make the demand` | 5 |
| 487.012(2)(b) | 9075-9075 | fork (F20) | `s 487.012(2) the peace officer or public officer may make the demand` | 5 |
| 487.012(2)(c) | 9076-9076 | fork (F20) | `s 487.012(2) the peace officer or public officer may make the demand` | 5 |
| 487.012(3) | 9077-9078 | fork (F21) | `s 487.012(3) the demand is barred against the person under investigation for the offence` | 2 |
| 487.012(4) | 9079-9080 | fork (F4) | `s 487.012(4) the demand expires on the day`; `s 487.012(4) the demand is in effect on the day` (+1) | 11 |
| 487.012(4)(a) | 9081-9081 | fork (F4) | `s 487.012(4) the demand expires on the day`; `s 487.012(4) the demand is in effect on the day` (+1) | 11 |
| 487.012(4)(b) | 9082-9082 | fork (F4) | `s 487.012(4) the demand expires on the day`; `s 487.012(4) the demand is in effect on the day` (+1) | 11 |
| 487.012(5) | 9083-9084 | encoded | `s 487.012(5) the officer may revoke the condition at any time`; `s 487.012(5) the officer who makes the demand may impose the condition in the demand` | 4 |
| 487.012(6) | 9085-9086 | fork (F21) | `s 487.012(6) another demand to preserve the same computer data in connection with the investigation is barred` | 2 |
| 487.013(1) | 9087-9088 | encoded | `s 487.013(1) the justice or judge may order the person to preserve computer data` | 3 |
| 487.013(2) | 9089-9090 | encoded | `s 487.013(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.013(2)(a) | 9091-9091 | encoded | `s 487.013(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.013(2)(b) | 9092-9092 | encoded | `s 487.013(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.013(3) | 9093-9094 | encoded | `s 487.013(3) the justice or judge has the further satisfaction required for an offence against a law of a foreign state` | 3 |
| 487.013(4) | 9095-9096 | encoded | `s 487.013(4) the order is in Form 5.003` | 2 |
| 487.013(5) | 9097-9098 | fork (F21) | `s 487.013(5) the order is barred against the person under investigation for the offence` | 2 |
| 487.013(6) | 9099-9100 | fork (F4) | `s 487.013(6) the order expires on the day`; `s 487.013(6) the order is in effect on the day` | 6 |
| 487.0131(1) | 9101-9102 | fork (F5) | `s 487.0131(1) the justice or judge may order the person to keep the account open or active`; `s 487.0131(1) the person must keep the account open or active` | 5 |
| 487.0131(2) | 9103-9104 | encoded | `s 487.0131(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0131(2)(a) | 9105-9105 | encoded | `s 487.0131(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0131(2)(b) | 9106-9106 | encoded | `s 487.0131(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0131(3) | 9107-9108 | encoded | `s 487.0131(3) the order is in Form 5.0032` | 2 |
| 487.0131(4) | 9109-9110 | encoded | `s 487.0131(4) the order contains the notification requirement` | 2 |
| 487.0131(5) | 9111-9112 | fork (F21) | `s 487.0131(5) the order is barred against the person under investigation for the offence` | 2 |
| 487.0131(6) | 9113-9114 | fork (F4) | `s 487.0131(6) the order expires on the day`; `s 487.0131(6) the order is in effect on the day` | 6 |
| 487.0131(7) | 9115-9116 | fork (F17) | `s 487.0131(7) the justice or judge may renew the order for the period` | 4 |
| 487.0131(8) | 9117-9118 | encoded | `s 487.0131(8) the justice or judge has the satisfaction required before renewing the order` | 2 |
| 487.014(1) | 9119-9120 | fork (F10) | `s 487.014(1) the justice or judge may order the person to produce a document or to prepare and produce a document` | 4 |
| 487.014(2) | 9121-9122 | encoded | `s 487.014(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.014(2)(a) | 9123-9123 | encoded | `s 487.014(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.014(2)(b) | 9124-9124 | encoded | `s 487.014(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.014(3) | 9125-9126 | encoded | `s 487.014(3) the order is in Form 5.005` | 2 |
| 487.014(4) | 9127-9128 | fork (F21) | `s 487.014(4) the order is barred against the person under investigation for the offence` | 2 |
| 487.0141(1) | 9129-9130 | encoded | `s 487.0141(1) the justice or judge may order the person to produce a document on any of the dates specified in the order` | 3 |
| 487.0141(2) | 9131-9132 | encoded | `s 487.0141(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0141(2)(a) | 9133-9133 | encoded | `s 487.0141(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0141(2)(b) | 9134-9134 | encoded | `s 487.0141(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.0141(3) | 9135-9136 | encoded | `s 487.0141(3) the order is in Form 5.0051` | 2 |
| 487.0141(4) | 9137-9138 | fork (F17, F3) | `s 487.0141(4) the order may specify the dates` | 6 |
| 487.0141(5) | 9139-9140 | fork (F1) | `s 487.0141(5) the order may require the person to produce a copy of the reports` | 3 |
| 487.0141(6) | 9141-9142 | fork (F17) | `s 487.0141(6)(a) the person may be required to produce documents again`; `s 487.0141(6)(b) the person may be required to produce a copy of a document that was in their possession or control before the day on which the order is made` (+1) | 8 |
| 487.0141(6)(a) | 9143-9143 | fork (F17) | `s 487.0141(6)(a) the person may be required to produce documents again` | 4 |
| 487.0141(6)(b) | 9144-9144 | fork (F17) | `s 487.0141(6)(b) the person may be required to produce a copy of a document that was in their possession or control before the day on which the order is made` | 2 |
| 487.0141(6)(c) | 9145-9145 | fork (F17) | `s 487.0141(6)(c) the person may be required to prepare and produce a document that contains data that was in their possession or control before the day on which the order is made` | 2 |
| 487.0141(7) | 9146-9147 | fork (F21) | `s 487.0141(7) the order is barred against the person under investigation for the offence` | 2 |
| 487.0141(8) | 9148-9149 | fork (F4) | `s 487.0141(8) the order expires on the day`; `s 487.0141(8) the order is in effect on the day` | 6 |
| 487.0141(9) | 9150-9151 | fork (F17) | `s 487.0141(9) the justice or judge may renew the order for the period` | 4 |
| 487.0141(10) | 9152-9153 | encoded | `s 487.0141(10) the justice or judge has the satisfaction required before renewing the order` | 2 |
| 487.0141(11) | 9154-9155 | fork (F17, F3) | `s 487.0141(11) the renewed order may specify the dates` | 4 |
| 487.015(1) | 9156-9157 | encoded | `s 487.015(1) the justice or judge may order the person to prepare and produce a document containing transmission data` | 3 |
| 487.015(2) | 9158-9159 | encoded | `s 487.015(2) the justice or judge has the satisfaction required before making the order` | 5 |
| 487.015(2)(a) | 9160-9160 | encoded | `s 487.015(2) the justice or judge has the satisfaction required before making the order` | 5 |
| 487.015(2)(b) | 9161-9161 | encoded | `s 487.015(2) the justice or judge has the satisfaction required before making the order` | 5 |
| 487.015(2)(c) | 9162-9162 | encoded | `s 487.015(2) the justice or judge has the satisfaction required before making the order` | 5 |
| 487.015(3) | 9163-9164 | encoded | `s 487.015(3) the order is in Form 5.006` | 2 |
| 487.015(4) | 9165-9166 | fork (F22, F3) | `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` | 12 |
| 487.015(4)(a) | 9167-9167 | fork (F22, F3) | `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` | 12 |
| 487.015(4)(b) | 9168-9168 | fork (F22, F3) | `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` | 12 |
| 487.015(5) | 9169-9170 | fork (F21) | `s 487.015(5) the order is barred against the person under investigation for the offence` | 2 |
| 487.015(6) | 9171-9172 | fork (F12) | `s 487.015(6) the day from which the report is due as soon as feasible`; `s 487.015(6) the report states what is required` | 8 |
| 487.016(1) | 9173-9174 | encoded | `s 487.016(1) the justice or judge may order the person to prepare and produce a document containing transmission data` | 3 |
| 487.016(2) | 9175-9176 | encoded | `s 487.016(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.016(2)(a) | 9177-9177 | encoded | `s 487.016(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.016(2)(b) | 9178-9178 | encoded | `s 487.016(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.016(3) | 9179-9180 | encoded | `s 487.016(3) the order is in Form 5.007` | 2 |
| 487.016(4) | 9181-9182 | fork (F21) | `s 487.016(4) the order is barred against the person under investigation for the offence` | 2 |
| 487.017(1) | 9183-9184 | encoded | `s 487.017(1) the justice or judge may order the person to prepare and produce a document containing tracking data` | 3 |
| 487.017(2) | 9185-9186 | encoded | `s 487.017(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.017(2)(a) | 9187-9187 | encoded | `s 487.017(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.017(2)(b) | 9188-9188 | encoded | `s 487.017(2) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.017(3) | 9189-9190 | encoded | `s 487.017(3) the order is in Form 5.007` | 2 |
| 487.017(4) | 9191-9192 | fork (F21) | `s 487.017(4) the order is barred against the person under investigation for the offence` | 2 |
| 487.018(1) | 9193-9194 | encoded | `s 487.018(1) the justice or judge may order the document to set out the data` | 7 |
| 487.018(1)(a) | 9195-9195 | encoded | `s 487.018(1) the justice or judge may order the document to set out the data` | 7 |
| 487.018(1)(b) | 9196-9196 | encoded | `s 487.018(1) the justice or judge may order the document to set out the data` | 7 |
| 487.018(1)(c) | 9197-9197 | encoded | `s 487.018(1) the justice or judge may order the document to set out the data` | 7 |
| 487.018(1)(d) | 9198-9198 | encoded | `s 487.018(1) the justice or judge may order the document to set out the data` | 7 |
| 487.018(2) | 9199-9200 | encoded | `s 487.018(2) the order may also require the document to set out the identifying data` | 5 |
| 487.018(2)(a) | 9201-9201 | encoded | `s 487.018(2) the order may also require the document to set out the identifying data` | 5 |
| 487.018(2)(b) | 9202-9202 | encoded | `s 487.018(2) the order may also require the document to set out the identifying data` | 5 |
| 487.018(2)(c) | 9203-9203 | encoded | `s 487.018(2) the order may also require the document to set out the identifying data` | 5 |
| 487.018(3) | 9204-9205 | encoded | `s 487.018(3) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.018(3)(a) | 9206-9206 | encoded | `s 487.018(3) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.018(3)(b) | 9207-9207 | encoded | `s 487.018(3) the justice or judge has the satisfaction required before making the order` | 4 |
| 487.018(4) | 9208-9209 | encoded | `s 487.018(4) the order is in Form 5.008` | 2 |
| 487.018(5) | 9210-9211 | fork (F21) | `s 487.018(5) the order is barred against the person under investigation for the offence` | 2 |
| 487.019(1) | 9212-9213 | encoded | `s 487.019(1) the order may contain the condition`; `s 487.019(1) the order may contain the condition to protect a privileged communication` | 9 |
| 487.019(2) | 9214-9215 | encoded | `s 487.019(2) the order has effect at the place` | 2 |
| 487.019(3) | 9216-9217 | fork (F12) | `s 487.019(3) the justice or judge may revoke or vary the order`; `s 487.019(3) the peace officer or public officer must give notice of the revocation or variation to the person who is subject to the order` | 6 |
| 487.0191(1) | 9218-9219 | encoded | `s 487.0191(1) the justice or judge may make an order prohibiting the person from disclosing the existence or contents of the demand or order` | 3 |
| 487.0191(2) | 9220-9221 | encoded | `s 487.0191(2) the justice or judge has the satisfaction required before making the order` | 3 |
| 487.0191(3) | 9222-9223 | encoded | `s 487.0191(3) the order is in Form 5.0091` | 2 |
| 487.0191(4) | 9224-9225 | encoded | `s 487.0191(4) the applicant may apply to revoke or vary the order` | 5 |
| 487.0192(1) | 9226-9227 | fork (F7) | `s 487.0192(1) the order contains the particulars required` | 5 |
| 487.0192(2) | 9228-9229 | fork (F7) | `s 487.0192(2) the order made under section 487.015 contains the particulars required` | 3 |
| 487.0192(3) | 9230-9231 | encoded | `s 487.0192(3) the order may specify that a document may be produced on or through an electro-magnetic medium` | 2 |
| 487.0192(4) | 9232-9233 | encoded | `s 487.0192(4) the provision applies to the document` | 4 |
| 487.0192(5) | 9234-9235 | encoded | `s 487.0192(5) the copy is admissible in evidence` | 3 |
| 487.0192(6) | 9236-9237 | encoded | `s 487.0192(6) the document is considered to be original for the purposes of the Canada Evidence Act` | 2 |
| 487.01921(1) | 9238-9239 | encoded | `s 487.01921(1) the person may apply to revoke or vary the order` | 3 |
| 487.01921(2) | 9240-9241 | encoded | `s 487.01921(2) the person may make the application` | 3 |
| 487.01921(3) | 9242-9243 | fork (F11, F5) | `s 487.01921(3) the person must comply with the order pending the decision` | 2 |
| 487.01921(4) | 9244-9245 | fork (F3) | `s 487.01921(4) the hearing must be commenced`; `s 487.01921(4) the hearing of the application is commenced as required` | 4 |
| 487.01921(5) | 9246-9247 | fork (F1) | `s 487.01921(5) the justice or judge may revoke or vary the order` | 2 |
| 487.0193(1) | 9248-9249 | encoded | `s 487.0193(1) the person, financial institution or entity may apply to revoke or vary the order` | 5 |
| 487.0193(2) | 9250-9251 | fork (F3) | `s 487.0193(2) the notice may be given`; `s 487.0193(2) the person, institution or entity may make the application` | 4 |
| 487.0193(3) | 9252-9253 | fork (F11) | `s 487.0193(3) the person, institution or entity is required to prepare or produce the document` | 3 |
| 487.0193(4) | 9254-9255 | fork (F1) | `s 487.0193(4) the justice or judge may revoke or vary the order` | 3 |
| 487.0193(4)(a) | 9256-9256 | fork (F1) | `s 487.0193(4) the justice or judge may revoke or vary the order` | 3 |
| 487.0193(4)(b) | 9257-9257 | fork (F1) | `s 487.0193(4) the justice or judge may revoke or vary the order` | 3 |
| 487.0194(1) | 9258-9259 | fork (F12, F5) | `s 487.0194(1) the person to whom a preservation demand is made must destroy it` | 5 |
| 487.0194(2) | 9260-9261 | fork (F12, F5) | `s 487.0194(2) the person subject to a preservation order must destroy it` | 4 |
| 487.0194(3) | 9262-9263 | encoded | `s 487.0194(3) the earlier day after which the person must destroy the computer data as soon as feasible` | 5 |
| 487.0194(3)(a) | 9264-9264 | encoded | `s 487.0194(3) the earlier day after which the person must destroy the computer data as soon as feasible` | 5 |
| 487.0194(3)(b) | 9265-9265 | encoded | `s 487.0194(3) the earlier day after which the person must destroy the computer data as soon as feasible` | 5 |
| 487.0194(4) | 9266-9267 | encoded | `s 487.0194(4) the person must destroy the computer data when the document is obtained under a warrant` | 3 |
| 487.0195(1) | 9268-9269 | encoded | `s 487.0195(1) a preservation demand, preservation order, keep account open or active order or production order is necessary for the officer to ask` | 5 |
| 487.0195(2) | 9270-9271 | fork (F21) | `s 487.0195(2) the person incurs criminal or civil liability for doing so` | 2 |
| 487.0196 | 9272-9273 | fork (F10, F21, F23) | `s 487.0196 the document the individual was required to prepare may be used or received in evidence against them`; `s 487.0196 the person is excused from complying with the order` | 7 |
| 487.0197 | 9274-9275 | fork (F17, F6) | `s 487.0197 the fine is within the maximum`; `s 487.0197 the person is guilty of an offence punishable on summary conviction` (+1) | 9 |
| 487.0198 | 9276-9277 | fork (F17, F6) | `s 487.0198 the person, financial institution or entity is guilty of an offence punishable on summary conviction`; `s 487.0198 the punishment is within the maximum` (+1) | 11 |
| 487.0199 | 9278-9279 | fork (F6) | `s 487.0199 the person is guilty of an offence punishable on summary conviction`; `s 487.0199 the punishment the section states` | 5 |
| 487.02(1) | 9280-9281 | fork (F1) | `s 487.02(1) the assistance order has effect at the place`; `s 487.02(1) the judge or justice may order the person to provide assistance` | 6 |
| 487.02(2) | 9282-9283 | encoded | `s 487.02(2) the order to provide assistance may be issued by a means of telecommunication` | 2 |
| 487.021(1) | 9284-9285 | inert (reason 2: machinery, a parliamentary review of the Act's provisions that affects no one now) | - | 0 |
| 487.021(2) | 9286-9287 | inert (reason 2: machinery, a parliamentary review of the Act's provisions that affects no one now) | - | 0 |
| 487.03 | 9288-9289 | repealed or blank in this text: the text shows `[Repealed, 2019, c. 25, s. 196]` | - | 0 |
| 487.04 | 9290-9292 | encoded | `s 487.04 the definitions apply in the section` | 7 |
| 487.04 "adult" | 9293-9293 | encoded | `s 487.04 adult` | 3 |
| 487.04 "designated offence" | 9294-9294 | encoded | `s 487.04 the offence is a designated offence` | 5 |
| 487.04 "DNA" | 9295-9295 | encoded | `s 487.04 DNA` | 2 |
| 487.04 "forensic DNA analysis" | 9296-9296 | encoded | `s 487.04 forensic DNA analysis` | 6 |
| 487.04 forensic DNA analysis (a) | 9297-9297 | encoded | `s 487.04 forensic DNA analysis` | 6 |
| 487.04 forensic DNA analysis (b) | 9298-9298 | encoded | `s 487.04 forensic DNA analysis` | 6 |
| 487.04 "primary designated offence" | 9299-9299 | encoded | `s 487.04 primary designated offence paragraph (c.1) lists the provision`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` (+1) | 199 |
| 487.04 primary designated offence (a) | 9300-9300 | encoded | `s 487.04 primary designated offence (a) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (a)(i) | 9301-9301 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(i.1) | 9302-9302 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(i.2) | 9303-9303 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.3) | 9304-9304 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(i.4) | 9305-9305 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.5) | 9306-9306 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.6) | 9307-9307 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(i.7) | 9308-9308 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(i.8) | 9309-9309 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.9) | 9310-9310 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.901) | 9311-9311 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.91) | 9312-9312 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.911) | 9313-9313 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(i.92) | 9314-9314 | encoded | `s 487.04 primary designated offence (a) provisions` | 3 |
| 487.04 primary designated offence (a)(i.93) | 9315-9315 | repealed or blank in this text: the text shows `[Repealed, 2014, c. 25, s. 23]` | `s 487.04 primary designated offence (a) provisions` | 0 |
| 487.04 primary designated offence (a)(ii) | 9316-9316 | encoded | `s 487.04 primary designated offence (a) provisions` | 10 |
| 487.04 primary designated offence (a)(iii) | 9317-9317 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(iv) | 9318-9318 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(v) | 9319-9319 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(vi) | 9320-9320 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(vi.1) | 9321-9321 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(vii) | 9322-9322 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(viii) | 9323-9323 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(ix) | 9324-9324 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(x) | 9325-9325 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xi) | 9326-9326 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xi.1) | 9327-9327 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xi.2) | 9328-9328 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xi.3) | 9329-9329 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xii) | 9330-9330 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiii) | 9331-9331 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiii.1) | 9332-9332 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(xiv) | 9333-9333 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiv.1) | 9334-9334 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiv.2) | 9335-9335 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a)(xiv.3) | 9336-9336 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiv.4) | 9337-9337 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiv.5) | 9338-9338 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xiv.6) | 9339-9339 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xv) | 9340-9340 | encoded | `s 487.04 primary designated offence (a) provisions` | 1 |
| 487.04 primary designated offence (a)(xvi) | 9341-9341 | encoded | `s 487.04 primary designated offence (a) provisions` | 2 |
| 487.04 primary designated offence (a.1) | 9342-9342 | encoded | `s 487.04 primary designated offence (a.1) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (a.1)(i) | 9343-9343 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(i.01) | 9344-9344 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.02) | 9345-9345 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.03) | 9346-9346 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.04) | 9347-9347 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.041) | 9348-9348 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.042) | 9349-9349 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.043) | 9350-9350 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.044) | 9351-9351 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.05) | 9352-9352 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(i.051) | 9353-9353 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(i.06) | 9354-9354 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.061) | 9355-9355 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.07) | 9356-9356 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.071) | 9357-9357 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.072) | 9358-9358 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.08) | 9359-9359 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.09) | 9360-9360 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.091) | 9361-9361 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(i.1) | 9362-9362 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(i.11) | 9363-9363 | repealed or blank in this text: the text shows `[Repealed, 2010, c. 17, s. 3]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(iv) | 9364-9364 | repealed or blank in this text: the text shows `[Repealed, 2014, c. 25, s. 23]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(iv.1) | 9365-9365 | repealed or blank in this text: the text shows `[Repealed, 2010, c. 17, s. 3]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(v) | 9366-9366 | repealed or blank in this text: the text shows `[Repealed, 2014, c. 25, s. 23]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(v.1) | 9367-9367 | repealed or blank in this text: the text shows `[Repealed, 2010, c. 17, s. 3]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(vi) | 9368-9368 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(vii) | 9369-9369 | repealed or blank in this text: the text shows `[Repealed, 2010, c. 17, s. 3]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (a.1)(vii.1) | 9370-9370 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(vii.11) | 9371-9371 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(vii.12) | 9372-9372 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(viii) | 9373-9373 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(viii.1) | 9374-9374 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(viii.2) | 9375-9375 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(viii.3) | 9376-9376 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(viii.4) | 9377-9377 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(ix) | 9378-9378 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(x) | 9379-9379 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(xi) | 9380-9380 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(xii) | 9381-9381 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(xiii) | 9382-9382 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 1 |
| 487.04 primary designated offence (a.1)(xiii.1) | 9383-9383 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(xiv) | 9384-9384 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(xiv.1) | 9385-9385 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(xv) | 9386-9386 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(xvi) | 9387-9387 | encoded | `s 487.04 primary designated offence (a.1) provisions` | 2 |
| 487.04 primary designated offence (a.1)(xvi.1) | 9388-9388 | repealed or blank in this text: the text shows `[Repealed, 2005, c. 25, s. 1]` | `s 487.04 primary designated offence (a.1) provisions` | 0 |
| 487.04 primary designated offence (b) | 9389-9389 | fork (F14) | `s 487.04 primary designated offence (b) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (b)(i) | 9390-9390 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 6 |
| 487.04 primary designated offence (b)(i.1) | 9391-9391 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 2 |
| 487.04 primary designated offence (b)(ii) | 9392-9392 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 2 |
| 487.04 primary designated offence (b)(iii) | 9393-9393 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 2 |
| 487.04 primary designated offence (b)(iv) | 9394-9394 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 1 |
| 487.04 primary designated offence (b)(v) | 9395-9395 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 1 |
| 487.04 primary designated offence (b)(vi) | 9396-9396 | fork (F14) | `s 487.04 primary designated offence (b) provisions` | 3 |
| 487.04 primary designated offence (b)(vii) | 9397-9397 | fork (F14) | `s 487.04 primary designated offence (b) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 1 |
| 487.04 primary designated offence (c) | 9398-9398 | fork (F14) | `s 487.04 primary designated offence (c) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (c)(i) | 9399-9399 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 2 |
| 487.04 primary designated offence (c)(ii) | 9400-9400 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 2 |
| 487.04 primary designated offence (c)(iii) | 9401-9401 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 2 |
| 487.04 primary designated offence (c)(iv) | 9402-9402 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 3 |
| 487.04 primary designated offence (c)(v) | 9403-9403 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 1 |
| 487.04 primary designated offence (c)(vi) | 9404-9404 | fork (F14) | `s 487.04 primary designated offence (c) provisions` | 2 |
| 487.04 primary designated offence (c.01) | 9405-9405 | fork (F14) | `s 487.04 primary designated offence (c.01) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (c.01)(i) | 9406-9406 | fork (F14) | `s 487.04 primary designated offence (c.01) provisions` | 2 |
| 487.04 primary designated offence (c.01)(ii) | 9407-9407 | fork (F14) | `s 487.04 primary designated offence (c.01) provisions` | 1 |
| 487.04 primary designated offence (c.01)(iii) | 9408-9408 | fork (F14) | `s 487.04 primary designated offence (c.01) provisions` | 2 |
| 487.04 primary designated offence (c.02) | 9409-9409 | fork (F14) | `s 487.04 primary designated offence (c.02) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (c.02)(i) | 9410-9410 | fork (F14) | `s 487.04 primary designated offence (c.02) provisions` | 2 |
| 487.04 primary designated offence (c.02)(ii) | 9411-9411 | fork (F14) | `s 487.04 primary designated offence (c.02) provisions` | 2 |
| 487.04 primary designated offence (c.02)(iii) | 9412-9412 | fork (F14) | `s 487.04 primary designated offence (c.02) provisions` | 2 |
| 487.04 primary designated offence (c.02)(iv) | 9413-9413 | fork (F14) | `s 487.04 primary designated offence (c.02) provisions` | 2 |
| 487.04 primary designated offence (c.03) | 9414-9414 | fork (F14) | `s 487.04 primary designated offence (c.03) provisions`; `s 487.04 primary designated offence paragraphs (a) to (c.03) list the provision` | 0 |
| 487.04 primary designated offence (c.1) | 9415-9415 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions`; `s 487.04 primary designated offence paragraph (c.1) lists the provision` | 0 |
| 487.04 primary designated offence (c.1)(i) | 9416-9416 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 5 |
| 487.04 primary designated offence (c.1)(ii) | 9417-9417 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 2 |
| 487.04 primary designated offence (c.1)(ii.1) | 9418-9418 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 1 |
| 487.04 primary designated offence (c.1)(ii.2) | 9419-9419 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 1 |
| 487.04 primary designated offence (c.1)(ii.3) | 9420-9420 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 1 |
| 487.04 primary designated offence (c.1)(ii.4) | 9421-9421 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 2 |
| 487.04 primary designated offence (c.1)(iii) | 9422-9422 | fork (F14, F16) | `s 487.04 primary designated offence (c.1) provisions` | 2 |
| 487.04 primary designated offence (d) | 9423-9423 | fork (F16) | `s 487.04 the offence is a primary designated offence` | 199 |
| 487.04 "provincial court judge" | 9424-9424 | encoded | `s 487.04 provincial court judge, in relation to a young person, includes a youth justice court judge` | 3 |
| 487.04 "secondary designated offence" | 9425-9425 | fork (F15) | `s 487.04 the offence is a secondary designated offence` | 158 |
| 487.04 secondary designated offence (a) | 9426-9426 | fork (F15, F17) | `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)`; `s 487.04 the maximum punishment is imprisonment for five years or more` (+1) | 5 |
| 487.04 secondary designated offence (a.1) | 9427-9427 | encoded | `s 487.04 secondary designated offence (a.1) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (a.1)(i) | 9428-9428 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 4 |
| 487.04 secondary designated offence (a.1)(ii) | 9429-9429 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 1 |
| 487.04 secondary designated offence (a.1)(iii) | 9430-9430 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 1 |
| 487.04 secondary designated offence (a.1)(iv) | 9431-9431 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 1 |
| 487.04 secondary designated offence (a.1)(v) | 9432-9432 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 1 |
| 487.04 secondary designated offence (a.1)(vi) | 9433-9433 | encoded | `s 487.04 secondary designated offence (a.1) provisions` | 2 |
| 487.04 secondary designated offence (b) | 9434-9434 | encoded | `s 487.04 secondary designated offence (b) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (b)(i) | 9435-9435 | encoded | `s 487.04 secondary designated offence (b) provisions` | 3 |
| 487.04 secondary designated offence (b)(ii) | 9436-9436 | encoded | `s 487.04 secondary designated offence (b) provisions` | 5 |
| 487.04 secondary designated offence (b)(iii) | 9437-9437 | encoded | `s 487.04 secondary designated offence (b) provisions` | 2 |
| 487.04 secondary designated offence (c) | 9438-9438 | encoded | `s 487.04 secondary designated offence (c) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (c)(i) | 9439-9439 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(i.0001) | 9440-9440 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(i.0002) | 9441-9441 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.001) | 9442-9442 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.002) | 9443-9443 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.003) | 9444-9444 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.004) | 9445-9445 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.005) | 9446-9446 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.006) | 9447-9447 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.007) | 9448-9448 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.008) | 9449-9449 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.009) | 9450-9450 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.01) | 9451-9451 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.011) | 9452-9452 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.012) | 9453-9453 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.013) | 9454-9454 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.014) | 9455-9455 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.015) | 9456-9456 | encoded | `s 487.04 secondary designated offence (c) provisions` | 6 |
| 487.04 secondary designated offence (c)(i.016) | 9457-9457 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(i.1) | 9458-9458 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(i.2) | 9459-9459 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(i.3) | 9460-9460 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(i.4) | 9461-9461 | repealed or blank in this text: the text shows `[Repealed, 2010, c. 17, s. 3]` | `s 487.04 secondary designated offence (c) provisions` | 0 |
| 487.04 secondary designated offence (c)(iii) | 9462-9462 | encoded | `s 487.04 secondary designated offence (c) provisions` | 3 |
| 487.04 secondary designated offence (c)(iv) | 9463-9463 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.1) | 9464-9464 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.2) | 9465-9465 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.3) | 9466-9466 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.4) | 9467-9467 | repealed or blank in this text: the text shows `[Repealed, 2022, c. 17, s. 19]` | `s 487.04 secondary designated offence (c) provisions` | 0 |
| 487.04 secondary designated offence (c)(iv.5) | 9468-9468 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.6) | 9469-9469 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.7) | 9470-9470 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.8) | 9471-9471 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(iv.9) | 9472-9472 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(v) | 9473-9473 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(vi) | 9474-9474 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(vii) | 9475-9475 | encoded | `s 487.04 secondary designated offence (c) provisions` | 7 |
| 487.04 secondary designated offence (c)(viii) | 9476-9476 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.01) | 9477-9477 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.02) | 9478-9478 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.1) | 9479-9479 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.11) | 9480-9480 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.12) | 9481-9481 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.13) | 9482-9482 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.14) | 9483-9483 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.15) | 9484-9484 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.16) | 9485-9485 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.17) | 9486-9486 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.2) | 9487-9487 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.201) | 9488-9488 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(viii.202) | 9489-9489 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.203) | 9490-9490 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.21) | 9491-9491 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(viii.22) | 9492-9492 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.23) | 9493-9493 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(viii.24) | 9494-9494 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(ix) | 9495-9495 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (c)(x) | 9496-9496 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.1) | 9497-9497 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.11) | 9498-9498 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.12) | 9499-9499 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.13) | 9500-9500 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.14) | 9501-9501 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.15) | 9502-9502 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.16) | 9503-9503 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.17) | 9504-9504 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.18) | 9505-9505 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.19) | 9506-9506 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.2) | 9507-9507 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.21) | 9508-9508 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.22) | 9509-9509 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.23) | 9510-9510 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.24) | 9511-9511 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.25) | 9512-9512 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.26) | 9513-9513 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.27) | 9514-9514 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.28) | 9515-9515 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(x.29) | 9516-9516 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi) | 9517-9517 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.01) | 9518-9518 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.02) | 9519-9519 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.1) | 9520-9520 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.11) | 9521-9521 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.12) | 9522-9522 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.13) | 9523-9523 | encoded | `s 487.04 secondary designated offence (c) provisions` | 3 |
| 487.04 secondary designated offence (c)(xi.14) | 9524-9524 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.15) | 9525-9525 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.16) | 9526-9526 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.17) | 9527-9527 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.18) | 9528-9528 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.19) | 9529-9529 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.2) | 9530-9530 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.21) | 9531-9531 | encoded | `s 487.04 secondary designated offence (c) provisions` | 1 |
| 487.04 secondary designated offence (c)(xi.22) | 9532-9532 | encoded | `s 487.04 secondary designated offence (c) provisions` | 4 |
| 487.04 secondary designated offence (c)(xi.23) | 9533-9533 | encoded | `s 487.04 secondary designated offence (c) provisions` | 2 |
| 487.04 secondary designated offence (d) | 9534-9534 | fork (F14) | `s 487.04 secondary designated offence (d) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (d)(i) | 9535-9535 | fork (F14) | `s 487.04 secondary designated offence (d) provisions` | 2 |
| 487.04 secondary designated offence (d)(ii) | 9536-9536 | fork (F14) | `s 487.04 secondary designated offence (d) provisions` | 2 |
| 487.04 secondary designated offence (d.1) | 9537-9537 | fork (F14) | `s 487.04 secondary designated offence (d.1) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (d.2) | 9538-9538 | fork (F14) | `s 487.04 secondary designated offence (d.2) provisions`; `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | 0 |
| 487.04 secondary designated offence (e) | 9539-9539 | fork (F16) | `s 487.04 secondary designated offence (e) an attempt or a conspiracy` | 0 |
| 487.04 secondary designated offence (e)(i) | 9540-9540 | fork (F16) | `s 487.04 secondary designated offence (e) an attempt or a conspiracy` | 0 |
| 487.04 secondary designated offence (e)(ii) | 9541-9541 | fork (F16) | `s 487.04 secondary designated offence (e) an attempt or a conspiracy` | 0 |
| 487.04 "Young Offenders Act" | 9542-9542 | encoded | `s 487.04 Young Offenders Act` | 2 |
| 487.04 "young person" | 9543-9543 | encoded | `s 487.04 young person` | 6 |

## Fork register (ccc16)

Every ambiguity, the reading taken (assumed, not ruled, unless a ruling is cited), the other reading, and the text that licenses each. The members of a fork are the coverage rows that name it. F-EXP (cited in `ccc16-preservation.l4` and `ccc16-production-orders.l4`) is F4, and F-72 (cited in `ccc16-production-orders.l4`) is the last sentence of F17.

### F1

- **The fork:** A power named "may" whose "if" gate fails (a justice or judge "satisfied", "of the opinion", "considers") answers NOTHING, not JUST FALSE (ruling of 2026-11-12, three limits).
- **Reading taken:** NOTHING (limited by its own wording): the failed "if" is not the text's no; the power is simply not shown to exist on those facts.
- **Other reading:** JUST FALSE: a failed "if" is the text's own no, clause by clause (reading (a) of the brief); the grant then reads as "may not".
- **Licensing text:** "if the judge or justice is of the opinion that"; "may revoke or vary the order if satisfied that"
- **Members (31 coverage rows):** 485(2), 485.2(1), 485.2(1)(a), 485.2(1)(b), 485.2(1)(c), 486(1), 486.1(2), 486.2(2), 486.3(3), 486.31(1), 486.4(2.1), 486.5(1), 486.5(2), 486.7(1), 487(1), 487(1)(a), 487(1)(b), 487(1)(c), 487(1)(c.1), 487(1)(d), 487(1)(e), 487.01(1), 487.01(1)(a), 487.01(1)(b), 487.01(1)(c), 487.0141(5), 487.01921(5), 487.0193(4), 487.0193(4)(a), 487.0193(4)(b), 487.02(1)

### F2

- **The fork:** A literal "Where" gate on a power (s 485(2): jurisdiction lost and not regained; s 485(4): an accused who appears has been misled or prejudiced; s 487.01(5.2): an affidavit and the interests of justice) answers JUST FALSE. Listed, not flipped (name-test class (i)).
- **Reading taken:** JUST FALSE: ruling (b) of 2026-11-05 says a failed "where" condition is the text's no.
- **Other reading:** NOTHING: the guide's line that a grant limited by its own wording is not a bar (a question for the maintainer or a lawyer).
- **Licensing text:** "Where jurisdiction over an accused or a defendant is lost and has not been regained"; "Where, in the opinion of the court, judge, provincial court judge or justice, an accused or a defendant who appears at a proceeding has been misled or prejudiced"
- **Members (3 coverage rows):** 485(2), 485(4), 487.01(5.2)

### F3

- **The fork:** A period the text fixes in its own words: outside it the answer is JUST FALSE (ruling (a) of 2026-11-05). The three months of s 485(2) and (3), the 60 days of s 487.015(4), the 30 days of s 487.0193(2), the 14 days of s 487.01921(4).
- **Reading taken:** JUST FALSE outside the period; inside it JUST TRUE (or the duty or power arises).
- **Other reading:** NOTHING: the brief's other line, that a stated period limits a grant and the case outside it is not covered.
- **Licensing text:** "within three months after the loss of jurisdiction"; "within 30 days after the day on which the order is made"
- **Members (9 coverage rows):** 485(2), 485(3), 487.0141(4), 487.0141(11), 487.015(4), 487.015(4)(a), 487.015(4)(b), 487.01921(4), 487.0193(2)

### F4

- **The fork:** F-EXP. The day a demand or order expires: "expires 60 days after the day on which it is made" (s 487.0131(6), s 487.0141(8); 90 days in s 487.013(6); 21 days or 90 days in s 487.012(4)): a boundary reading of the last day.
- **Reading taken:** In effect on the days before the made day plus N; it expires on the made day plus N (that day is the first on which it is not in effect).
- **Other reading:** In effect through the made day plus N.
- **Licensing text:** "it expires 60 days after the day on which it is made"; "21 days after the day on which it is made"
- **Members (6 coverage rows):** 487.012(4), 487.012(4)(a), 487.012(4)(b), 487.013(6), 487.0131(6), 487.0141(8)

### F5

- **The fork:** A duty ("shall", "must") whose trigger ("on application", "If ... is not made") is unmet, or whose "unless" is met, answers JUST FALSE (case by case, the maintainer 2026-11-05: the brief's list of six open questions includes a duty whose "if" or "where" is unmet).
- **Reading taken:** JUST FALSE: the duty does not arise on these facts.
- **Other reading:** NOTHING: the section is silent about the case where the trigger is not met.
- **Licensing text:** "unless the judge or justice is of the opinion that the order would interfere with the proper administration of justice"
- **Members (22 coverage rows):** 486.1(1), 486.1(1.1), 486.1(4), 486.2(1), 486.2(1.1), 486.2(5), 486.3(1), 486.3(2), 486.5(1), 486.5(9), 486.5(9)(a), 486.5(9)(b), 486.5(9)(c), 486.51(2), 486.6(1.1), 486.6(1.1)(a), 486.6(1.1)(b), 486.6(1.1)(c), 487.0131(1), 487.01921(3), 487.0194(1), 487.0194(2)

### F6

- **The fork:** An exception that is MET on a bar or an offence (s 485.1: "without (a) the personal consent in writing of the Attorney General or Deputy Attorney General"; ss 487.0197 to 487.0199: "without lawful excuse") answers NOTHING.
- **Reading taken:** NOTHING (limited by its own wording; ruling of 2026-10-29, marginal reading (b)): the section does not say what follows once the exception is met.
- **Other reading:** JUST FALSE: a met "unless" is the text's own no to the bar or the offence.
- **Licensing text:** "without lawful excuse"; "personal consent in writing"
- **Members (6 coverage rows):** 485.1, 485.1(a), 485.1(b), 487.0197, 487.0198, 487.0199

### F7

- **The fork:** A requirement on the content of an instrument or on how it is served (s 485.2(3), (7), (8); s 487(2); s 487.01(3), (4), (5.1), (6); s 487.0192(1), (2)) that is not met answers JUST FALSE.
- **Reading taken:** JUST FALSE: the summons, order or warrant does not meet the section.
- **Other reading:** NOTHING: the section states the requirement and no consequence.
- **Licensing text:** "set out briefly the offence"
- **Members (13 coverage rows):** 485.2(3), 485.2(7), 485.2(7)(a), 485.2(7)(b), 485.2(7)(c), 485.2(8), 487(2), 487.01(3), 487.01(4), 487.01(5.1), 487.01(6), 487.0192(1), 487.0192(2)

### F8

- **The fork:** Who applies. The text names the applicant (the prosecutor, a witness, the judge on their own motion; the accused only in s 486(3)). Another applicant answers NOTHING for a power (a named complement) and JUST FALSE for a duty whose trigger is the named applicant's application.
- **Reading taken:** As stated: the named applicant is a limit of the grant, or the trigger of the duty.
- **Other reading:** For a power, JUST FALSE under ruling (c) of 2026-11-05, which counts "on" and "upon" as "where" (see the name-test sweep below: 26 sites).
- **Licensing text:** "on application of the prosecutor in respect of a witness, or on application of a witness"
- **Members (23 coverage rows):** 486(1), 486(3), 486.1(1), 486.1(1.1), 486.1(2), 486.2(1), 486.2(1.1), 486.2(2), 486.3(1), 486.3(2), 486.3(3), 486.31(1), 486.4(2), 486.4(2)(a), 486.4(2)(b), 486.4(2)(c), 486.4(2.2), 486.4(2.2)(a), 486.4(2.2)(b), 486.4(2.2)(c), 486.5(1), 486.5(2), 486.7(1)

### F9

- **The fork:** A class with no "only" (a witness under 18, a victim of a listed offence, a proceeding for a listed offence): a case outside the class answers NOTHING (ruling (c) of 2026-11-05, a scope limit with no "only").
- **Reading taken:** NOTHING.
- **Other reading:** JUST FALSE.
- **Licensing text:** "who is under the age of 18 years or who has a mental or physical disability"
- **Members (13 coverage rows):** 486(3), 486.1(1), 486.1(1.1), 486.2(1), 486.2(1.1), 486.3(1), 486.3(2), 486.4(2.1), 486.4(2.2), 486.4(2.2)(a), 486.4(2.2)(b), 486.4(2.2)(c), 486.4(3)

### F10

- **The fork:** An exclusion ("other than", "Subject to"; the the "other than" site site is one of the brief's six case-by-case questions): s 486.7(1) answers JUST FALSE for an order that may be made under ss 486 to 486.5 (an the "other than" site site, decided case by case, the maintainer 2026-11-05); s 487.014(1) answers NOTHING for an order that ss 487.015 to 487.018 provide; s 487.0196 answers NOTHING in a prosecution for ss 132, 136 or 137.
- **Reading taken:** As stated, site by site.
- **Other reading:** For s 486.7(1): NOTHING (ruling (c)). For the other two: JUST FALSE.
- **Licensing text:** "other than one that may be made under any of sections 486 to 486.5"; "Subject to sections 487.015 to 487.018"
- **Members (3 coverage rows):** 486.7(1), 487.014(1), 487.0196

### F11

- **The fork:** An "until" in a duty or a bar (ruling (d) of 2026-11-05): s 487.01921(3) "must comply with the order until a decision is made"; s 487.0193(3) "is not required to prepare or produce the document until a final decision is made".
- **Reading taken:** s 487.01921(3): JUST TRUE before the decision, JUST FALSE after it (the text's "until"). s 487.0193(3): the bar, JUST FALSE before the decision, NOTHING after it (never read as a grant: after the decision the section is silent).
- **Other reading:** s 487.01921(3): NOTHING after the decision. s 487.0193(3): JUST TRUE (required) after the decision.
- **Licensing text:** "The person must comply with the order until a decision is made with respect to the application"; "is not required to prepare or produce the document until a final decision is made with respect to the application"
- **Members (2 coverage rows):** 487.01921(3), 487.0193(3)

### F12

- **The fork:** A duty to inform or to report "as soon as feasible" or "as soon as practicable": the text states no number, so none is invented; the function answers whether the duty has arisen.
- **Reading taken:** The function is the duty's trigger, not a deadline.
- **Other reading:** A fixed number of days (not chosen: it would be invented).
- **Licensing text:** "as soon as feasible"
- **Members (21 coverage rows):** 486.4(2), 486.4(2)(a), 486.4(2)(b), 486.4(2)(c), 486.4(2.2), 486.4(2.2)(a), 486.4(2.2)(b), 486.4(2.2)(c), 486.4(3.2), 486.4(3.2)(a), 486.4(3.2)(b), 486.4(3.2)(c), 486.5(8.1), 486.5(8.2), 486.5(8.2)(a), 486.5(8.2)(b), 486.5(8.2)(c), 487.015(6), 487.019(3), 487.0194(1), 487.0194(2)

### F13

- **The fork:** s 486.2(5): "unless arrangements are made ... and the accused is permitted to communicate with counsel": two conditions joined by "and".
- **Reading taken:** The bar is lifted (JUST FALSE) only when both are met.
- **Other reading:** The bar is lifted when either is met.
- **Licensing text:** "unless arrangements are made for the accused, the judge or justice and the jury to watch the testimony of the witness by means of closed-circuit television or videoconference and the accused is permitted to communicate with counsel while watching the testimony"
- **Members (1 coverage rows):** 486.2(5)

### F14

- **The fork:** The lists of s 487.04 that name another text (the Criminal Code, chapter C-34 of the Revised Statutes of Canada, 1970; the Act as it read before July 1, 1990; before the conveyances amendment; the Foreign Interference and Security of Information Act; the Cannabis Act; the Controlled Drugs and Substances Act): the instrument and vintage where the provision is found is an input.
- **Reading taken:** A second fact of the offence (`where that provision is found`); the text of those other instruments is not among the sources.
- **Other reading:** Encode only the Act as it reads now.
- **Licensing text:** "as they read from time to time before July 1, 1990"
- **Members (39 coverage rows):** 487.04 primary designated offence (b), 487.04 primary designated offence (b)(i), 487.04 primary designated offence (b)(i.1), 487.04 primary designated offence (b)(ii), 487.04 primary designated offence (b)(iii), 487.04 primary designated offence (b)(iv), 487.04 primary designated offence (b)(v), 487.04 primary designated offence (b)(vi), 487.04 primary designated offence (b)(vii), 487.04 primary designated offence (c), 487.04 primary designated offence (c)(i), 487.04 primary designated offence (c)(ii), 487.04 primary designated offence (c)(iii), 487.04 primary designated offence (c)(iv), 487.04 primary designated offence (c)(v), 487.04 primary designated offence (c)(vi), 487.04 primary designated offence (c.01), 487.04 primary designated offence (c.01)(i), 487.04 primary designated offence (c.01)(ii), 487.04 primary designated offence (c.01)(iii), 487.04 primary designated offence (c.02), 487.04 primary designated offence (c.02)(i), 487.04 primary designated offence (c.02)(ii), 487.04 primary designated offence (c.02)(iii), 487.04 primary designated offence (c.02)(iv), 487.04 primary designated offence (c.03), 487.04 primary designated offence (c.1), 487.04 primary designated offence (c.1)(i), 487.04 primary designated offence (c.1)(ii), 487.04 primary designated offence (c.1)(ii.1), 487.04 primary designated offence (c.1)(ii.2), 487.04 primary designated offence (c.1)(ii.3), 487.04 primary designated offence (c.1)(ii.4), 487.04 primary designated offence (c.1)(iii), 487.04 secondary designated offence (d), 487.04 secondary designated offence (d)(i), 487.04 secondary designated offence (d)(ii), 487.04 secondary designated offence (d.1), 487.04 secondary designated offence (d.2)

### F15

- **The fork:** "that may be prosecuted by indictment — or, for section 487.051 to apply, is prosecuted by indictment" (paragraphs (a), (a.1), (b) of "secondary designated offence").
- **Reading taken:** For the purposes of s 487.051 the offence must be prosecuted by indictment; for every other purpose it is enough that it may be.
- **Other reading:** In every case the offence must be prosecuted by indictment.
- **Licensing text:** "may be prosecuted by indictment — or, for section 487.051 to apply, is prosecuted by indictment"
- **Members (2 coverage rows):** 487.04 "secondary designated offence", 487.04 secondary designated offence (a)

### F16

- **The fork:** Findings on the reach of the cross-references in s 487.04 (see Findings 1 and 2): paragraph (d) of "primary designated offence" names paragraphs (a) to (c.03), not (c.1); paragraph (e)(i) of "secondary designated offence" names paragraphs (a) or (b), not (a.1).
- **Reading taken:** The text as written: an attempt or a conspiracy to commit a (c.1) offence is not within (d), and one to commit an (a.1) Cannabis Act offence is not within (e)(i).
- **Other reading:** The same reach as for the principal offence.
- **Licensing text:** "(d) an attempt to commit or, other than for the purposes of subsection 487.05(1), a conspiracy to commit an offence referred to in any of paragraphs (a) to (c.03)"; "(i) an offence referred to in paragraph (a) or (b) — which, for section 487.051 to apply, is prosecuted by indictment, or"
- **Members (12 coverage rows):** 487.04 primary designated offence (c.1), 487.04 primary designated offence (c.1)(i), 487.04 primary designated offence (c.1)(ii), 487.04 primary designated offence (c.1)(ii.1), 487.04 primary designated offence (c.1)(ii.2), 487.04 primary designated offence (c.1)(ii.3), 487.04 primary designated offence (c.1)(ii.4), 487.04 primary designated offence (c.1)(iii), 487.04 primary designated offence (d), 487.04 secondary designated offence (e), 487.04 secondary designated offence (e)(i), 487.04 secondary designated offence (e)(ii)

### F17

- **The fork:** A maximum the text states in its own words ("up to 10 dates", "not more than 60 days", "no extension may exceed three years", "more than once in any 72-hour period", the fines and terms of ss 487.0197 and 487.0198): above it the answer is JUST FALSE. F-72: two requirements less than 72 hours apart fall in one 72-hour period.
- **Reading taken:** JUST FALSE above the maximum (a flat negative); F-72 as stated.
- **Other reading:** NOTHING above the maximum; F-72: the period runs from the first requirement to the 72nd hour inclusive.
- **Licensing text:** "but no extension may exceed three years"; "produce documents more than once in any 72-hour period"
- **Members (12 coverage rows):** 487.01(5.2), 487.0131(7), 487.0141(4), 487.0141(6), 487.0141(6)(a), 487.0141(6)(b), 487.0141(6)(c), 487.0141(9), 487.0141(11), 487.0197, 487.0198, 487.04 secondary designated offence (a)

### F18

- **The fork:** s 486.5(2.1): the offences for the purposes of subsection (2) include "a serious offence committed for the benefit of, at the direction of, or in association with, a criminal organization" and a terrorism offence, terms of section 2.
- **Reading taken:** Asked as `s 2 criminal organization offence` and `s 2 terrorism offence` (MAYBE BOOLEAN inputs); the section 2 answer is not computed here.
- **Other reading:** Encode the section 2 meaning here.
- **Licensing text:** "a serious offence committed for the benefit of, at the direction of, or in association with, a criminal organization"
- **Members (5 coverage rows):** 486.5(2.1), 486.5(2.1)(a), 486.5(2.1)(b), 486.5(2.1)(c), 486.5(2.1)(d)

### F19

- **The fork:** s 486.4(5), s 486.5(3.1): the ban "does not apply in respect of the disclosure ... when it is not the purpose of the disclosure to make the information known to the public".
- **Reading taken:** JUST FALSE (the order does not apply) where the stated exception is met; NOTHING otherwise.
- **Other reading:** JUST TRUE otherwise (the order applies to every other disclosure).
- **Licensing text:** "when it is not the purpose of the disclosure to make the information known to the public"
- **Members (2 coverage rows):** 486.4(5), 486.5(3.1)

### F20

- **The fork:** s 487.012(2): "may make the demand only if they have reasonable grounds to suspect that" three things, joined by "and", of which paragraph (b) begins "in the case of an offence committed under a law of a foreign state".
- **Reading taken:** (b) applies only to an offence under a law of a foreign state; "only if" closes the gate, so the answer is JUST FALSE when it fails.
- **Other reading:** (b) is a condition of every demand.
- **Licensing text:** "The peace officer or public officer may make the demand only if they have reasonable grounds to suspect that"
- **Members (4 coverage rows):** 487.012(2), 487.012(2)(a), 487.012(2)(b), 487.012(2)(c)

### F21

- **The fork:** A bar or flat negative addressed to an official, asked for the person it protects ("A demand may not be made to a person who is under investigation"; "No one is excused"; "is not required"): N2 of 2026-11-04.
- **Reading taken:** JUST TRUE where the bar applies to the person asking (the bar is the answer); NOTHING where the facts for it are absent.
- **Other reading:** JUST FALSE where the facts for the bar are absent.
- **Licensing text:** "A demand may not be made to a person who is under investigation for the offence referred to in paragraph (2)(a)"
- **Members (15 coverage rows):** 486.51(5), 486.51(6), 486.71, 487.012(3), 487.012(6), 487.013(5), 487.0131(5), 487.014(4), 487.0141(7), 487.015(5), 487.016(4), 487.017(4), 487.018(5), 487.0195(2), 487.0196

### F22

- **The fork:** s 487.015(4): the order may be served within 60 days after the day on which it is made, or within one year after that day for the offences named (ss 467.11 to 467.13, an offence for the benefit of a criminal organization, a terrorism offence).
- **Reading taken:** JUST FALSE for a service day before the order is made or more than a year after it; JUST TRUE within 60 days; between 60 days and a year, JUST TRUE for the offences named (the section 2 terms are MAYBE inputs: NOTHING if section 2 does not answer), JUST FALSE for any other offence.
- **Other reading:** NOTHING outside the two periods (a period limits a grant).
- **Licensing text:** "within 60 days after the day on which the order is made"; "within one year after the day on which the order is made"
- **Members (3 coverage rows):** 487.015(4), 487.015(4)(a), 487.015(4)(b)

### F23

- **The fork:** s 487.0196 self-incrimination: "No one is excused from complying ... on the ground that", and the bar on use of a document an individual was required to prepare, other than in a prosecution under sections 132, 136 or 137.
- **Reading taken:** JUST FALSE for "excused" on that ground under ss 487.014 to 487.018, and JUST FALSE for use of the prepared document in a later criminal proceeding; NOTHING in a prosecution under ss 132, 136 or 137 (a carve-out from a bar is not a grant).
- **Other reading:** JUST TRUE (the document may be used) in a prosecution under ss 132, 136 or 137.
- **Licensing text:** "No one is excused from complying with an order made under any of sections 487.014 to 487.018 on the ground that"
- **Members (1 coverage rows):** 487.0196

Rows citing no fork rest only on the conventions of "Reading a result: FALSE and NOTHING" above; the functions with a branch that rests on reading (a) or (b) are listed in "Marginal readings for a lawyer". The repeated conventions are F1, F5, F8 and F9.

### Name-test sweep of 2026-11-12

The class: every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorized" (regex `may|permitted|power|entitled|authori[sz]ed|authori[sz]es|authori[sz]ing|lawful`, `work/nametest_table.py`): 90 functions, of which 2 are outside the class and 88 are swept. The ruling was in force from the first pass, so no answer was changed in this sweep: 0 flipped; 33 grant-named functions answer NOTHING on a failed "if" gate or a limit in their own wording (written so from the start).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon: literal "Where" (JUST FALSE) | listed: "may" with where/when/upon: on-application / when kind (NOTHING kept) | listed: "entitled" |
| --- | --- | --- | --- | --- |
| 0 (already NOTHING from the first pass: 33) | 27 | 4 | 24 | 0 |

**Assumed, not ruled, and flagged for the lead:** the sweep file counts "on such an application" and "on ..." with the where/when/upon group, whose answer under ruling (b) is JUST FALSE. This part's first pass kept NOTHING for another applicant ("On application of the prosecutor", "On ex parte application made by a peace officer or public officer") and for another recipient or time ("during the proceedings", "before the proceedings begin", "Before they are required"), reading the named applicant, recipient or time as a limit of the grant (the brief's "a named complement"). The 24 functions of the third list below answer NOTHING, and two more counted under "kept" (`s 486.5(1)`, `s 486.7(1)`) also carry an on-application branch that answers NOTHING: 26 sites. The other reading is JUST FALSE for a failed on-application or when gate. To change them would touch these functions, their tests and their seat cases. The question was sent to team-lead (with a count of 18, which this list corrects); no answer had arrived when this file was written.

**Name-test class (i) listed, a literal "Where" gate (answer JUST FALSE, the guide's own; not flipped):**

- `s 485(2) the court, judge, provincial court judge or justice may issue a summons` (officials): "Where jurisdiction over an accused or a defendant is lost and has not been regained"
- `s 485(2) the court, judge, provincial court judge or justice may issue a warrant for the arrest` (officials): "Where jurisdiction over an accused or a defendant is lost and has not been regained"
- `s 485(4) the court, judge, provincial court judge or justice may adjourn the proceeding and make an order` (officials): "Where, in the opinion of the court, judge, provincial court judge or justice, an accused or a defendant who appears at a proceeding has been misled or prejudiced"
- `s 487.01(5.2) the judge may grant an extension of the period for giving notice` (search-warrants): "Where the judge who issues a warrant under subsection (1) or any other judge having jurisdiction to issue such a warrant is, on the basis of an affidavit submitted in support of an application to vary the period, satisfied that the interests of justice warrant the granting of the application"

**Name-test class (i) listed, on-application / when kind (answer NOTHING kept, first-pass reading; other reading JUST FALSE):**

- `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` (officials): "on application in writing and on oath in Form 6.1"
- `s 486(1) the presiding judge or justice may order the exclusion of the public or that the witness testify behind a screen` (open-court): "on application of the prosecutor or a witness or on his or her own motion"
- `s 486(1.1) the application may be made to the judge or justice` (open-court): "during the proceedings / before the proceedings begin, to the judge or justice named"
- `s 486.1(2) the judge or justice may order that a support person or a support animal be permitted for another witness` (open-court): "on application of the prosecutor in respect of a witness, or on application of a witness"
- `s 486.1(2.1) the application may be made to the judge or justice` (open-court): "during the proceedings / before the proceedings begin, to the judge or justice named"
- `s 486.2(2) the judge or justice may order that another witness testify outside the court room or behind a screen, at the option of the witness` (open-court): "on application of the prosecutor in respect of a witness, or on application of a witness"
- `s 486.2(2.1) the application may be made to the judge or justice` (open-court): "during the proceedings / before the proceedings begin, to the judge or justice named"
- `s 486.3(3) the judge or justice may order that the accused not personally cross-examine another witness` (open-court): "on application of the prosecutor in respect of a witness who is not entitled to make an application"
- `s 486.3(4.1) the application may be made to the judge or justice` (open-court): "during the proceedings / before the proceedings begin, to the judge or justice named"
- `s 486.31(1) the judge or justice may order that information that could identify the witness not be disclosed in the course of the proceedings` (open-court): "on application of the prosecutor in respect of a witness, or on application of a witness"
- `s 486.7(2) the application may be made to the judge or justice` (open-court): "during the proceedings / before the proceedings begin, to the judge or justice named"
- `s 487.013(1) the justice or judge may order the person to preserve computer data` (preservation): "On ex parte application made by a peace officer or public officer"
- `s 487.0131(1) the justice or judge may order the person to keep the account open or active` (preservation): "On ex parte application made by a peace officer or public officer"
- `s 487.014(1) the justice or judge may order the person to produce a document or to prepare and produce a document` (production-orders): "on ex parte application made by a peace officer or public officer"
- `s 487.0141(1) the justice or judge may order the person to produce a document on any of the dates specified in the order` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.015(1) the justice or judge may order the person to prepare and produce a document containing transmission data` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.016(1) the justice or judge may order the person to prepare and produce a document containing transmission data` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.017(1) the justice or judge may order the person to prepare and produce a document containing tracking data` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.018(1) the justice or judge may order the document to set out the data` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.019(1) the order may contain the condition to protect a privileged communication` (production-orders): "in the case of an order made under section 487.014 or 487.0141"
- `s 487.019(3) the justice or judge may revoke or vary the order` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.0191(1) the justice or judge may make an order prohibiting the person from disclosing the existence or contents of the demand or order` (production-orders): "On ex parte application made by a peace officer or public officer"
- `s 487.0193(1) the person, financial institution or entity may apply to revoke or vary the order` (production-orders): "Before they are required by an order ... to produce a document"
- `s 486.5(2) the judge or justice may make an order directing that information that could identify the justice system participant not be published` (publication-bans): "On application of the prosecutor in respect of a justice system participant"

**Name-test class (ii) listed, "entitled"-named functions:** none (no function name of this part contains "entitled").

**Kept JUST FALSE because the text closes the gate itself, or the function is a bar or a duty (test 2):**

- `s 485(3) the proceedings may be recommenced` (officials): shall not be recommenced except in accordance with section 485.1: a flat negative
- `s 486(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 486.1(1) the judge or justice must order that a support person or a support animal be permitted` (open-court): a duty (shall order), not a grant; 'unless' closes the gate
- `s 486.1(1.1) the judge or justice must order that a support person or a support animal be permitted for a victim` (open-court): a duty (shall order), not a grant; 'unless' closes the gate
- `s 486.1(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` (open-court): a duty (shall inquire), not a grant
- `s 486.1(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 486.2(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` (open-court): a duty (shall inquire), not a grant
- `s 486.2(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 486.3(2.1) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` (open-court): a duty (shall inquire), not a grant
- `s 486.3(5) an adverse inference may be drawn from the fact that counsel is, or is not, appointed under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 486.31(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 486.7(1) the presiding judge or justice may make an order to protect the security of a witness` (open-court): OWN FORK LINE: JUST FALSE for 'any order, other than one that may be made under any of sections 486 to 486.5' (an '(other than X)' site, decided case by case, the maintainer 2026-11-05); not an 'if' gate; the other reading is NOTHING (ruling (c): a scope limit with no 'only')
- `s 486.7(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` (open-court): No adverse inference may be drawn: a flat negative
- `s 487.012(2) the peace officer or public officer may make the demand` (preservation): 'only if they have reasonable grounds to suspect': the text closes the gate with 'only if'
- `s 487.0131(7) the justice or judge may renew the order for the period` (preservation): 'for a period of not more than 60 days': a maximum in the text's own words (ruling (a))
- `s 487.0141(4) the order may specify the dates` (production-orders): 'up to 10 dates' within 'the 60-day period': a maximum and a period in the text's own words (ruling (a))
- `s 487.0141(6)(a) the person may be required to produce documents again` (production-orders): The person must not be required to: a flat negative
- `s 487.0141(6)(b) the person may be required to produce a copy of a document that was in their possession or control before the day on which the order is made` (production-orders): The person must not be required to: a flat negative
- `s 487.0141(6)(c) the person may be required to prepare and produce a document that contains data that was in their possession or control before the day on which the order is made` (production-orders): The person must not be required to: a flat negative
- `s 487.0141(9) the justice or judge may renew the order for the period` (production-orders): 'for a period of not more than 60 days': a maximum in the text's own words (ruling (a))
- `s 487.0141(11) the renewed order may specify the dates` (production-orders): 'up to 10 dates during the period for which it is renewed': a maximum and a period in the text's own words (ruling (a))
- `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` (production-orders): 'within 60 days' / 'within one year after the day on which the order is made': periods in the text's own words (ruling (a))
- `s 487.01921(2) the person may make the application` (production-orders): 'only if they give at least three days' notice': the text closes the gate with 'only if'
- `s 487.0193(2) the person, institution or entity may make the application` (production-orders): 'only if they give notice ... within 30 days': the text closes the gate with 'only if'
- `s 487.0196 the document the individual was required to prepare may be used or received in evidence against them` (production-orders): no document ... may be used or received in evidence: a flat negative
- `s 486.5(1) the judge or justice may make an order directing that information that could identify the victim or witness not be published` (publication-bans): 'Unless an order is made under section 486.4': the text closes the gate with 'unless'
- `s 486.51(6) the accused is permitted to make submissions in relation to the application` (publication-bans): The accused shall not be permitted: a flat negative

**Outside the class:** `s 487.0193(2) the notice may be given` (a regulative MAY rule) and the Boolean helper `s 487.04 the offence may be prosecuted by indictment or, for section 487.051 to apply, is prosecuted by indictment`. "It is lawful" functions outside the sweep: scoped 0, unscoped and retitled 0 (no function of this part is named "it is lawful ...").

**Answer NOTHING on a failed "if" gate or a limit in their own wording, from the first pass (33; the test-1 class, none needed flipping):**

- `s 483 the judge or provincial court judge may do alone what two or more justices are authorized to do` (officials)
- `s 484 the judge or provincial court judge has the same power and authority to preserve order as the superior court of criminal jurisdiction` (officials)
- `s 485.2(4) the justice or judge may proceed ex parte to determine the application` (officials)
- `s 485.2(5) the application may be made by the means of telecommunication` (officials)
- `s 485.2(6) the person may make a statement in writing instead of swearing an oath` (officials)
- `s 486.1(5) the judge or justice may order that the support person and the witness not communicate with each other while the witness testifies` (open-court)
- `s 486.31(2) the judge or justice may hold a hearing, and the hearing may be in private` (open-court)
- `s 487.012(1) the peace officer or public officer may make a demand to preserve computer data` (preservation)
- `s 487.012(4) the peace officer or public officer may revoke the demand` (preservation)
- `s 487.012(5) the officer who makes the demand may impose the condition in the demand` (preservation)
- `s 487.012(5) the officer may revoke the condition at any time` (preservation)
- `s 487.0141(5) the order may require the person to produce a copy of the reports` (production-orders)
- `s 487.018(2) the order may also require the document to set out the identifying data` (production-orders)
- `s 487.019(1) the order may contain the condition` (production-orders)
- `s 487.0191(4) the applicant may apply to revoke or vary the order` (production-orders)
- `s 487.0192(3) the order may specify that a document may be produced on or through an electro-magnetic medium` (production-orders)
- `s 487.01921(1) the person may apply to revoke or vary the order` (production-orders)
- `s 487.01921(5) the justice or judge may revoke or vary the order` (production-orders)
- `s 487.0193(4) the justice or judge may revoke or vary the order` (production-orders)
- `s 487.02(1) the judge or justice may order the person to provide assistance` (production-orders)
- `s 487.02(2) the order to provide assistance may be issued by a means of telecommunication` (production-orders)
- `s 486.4(1) the presiding judge or justice may make an order directing that information that could identify the victim or a witness not be published` (publication-bans)
- `s 486.4(2.1) the presiding judge or justice may make an order directing that information that could identify the victim not be published` (publication-bans)
- `s 486.5(6) the judge or justice may hold a hearing, and the hearing may be in private` (publication-bans)
- `s 486.5(8) the order may be subject to the condition` (publication-bans)
- `s 487(1) the justice may issue a warrant to search the building, receptacle or place` (search-warrants)
- `s 487(1) the warrant may authorize the person` (search-warrants)
- `s 487(1) the warrant may authorize the act` (search-warrants)
- `s 487(2) the warrant may be executed at the place` (search-warrants)
- `s 487(2.1) the person may do the act` (search-warrants)
- `s 487(3) the search warrant may be in the form set out as Form 5` (search-warrants)
- `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` (search-warrants)
- `s 487.01(6) the general warrant may be executed at the place` (search-warrants)

## Jural relations (ccc16)

Hohfeld's correlatives, each relation stated once, neutrally. A provision that creates no relation (a definition, a form, a counting or application rule, machinery) is listed once as `none`. Every section and subsection of the range is in a row (the generator checks it).

| provisions | held by (right, privilege, power or immunity) | borne by (duty, no-right, liability or disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| 483 | a judge or provincial court judge authorized by the law of the province | anyone affected by what the judge does alone | power / liability | `s 483 the judge or provincial court judge may do alone what two or more justices are authorized to do` |
| 484 | the presiding judge or provincial court judge | anyone in the court | power / liability | `s 484 the judge or provincial court judge has the same power and authority to preserve order as the superior court of criminal jurisdiction` |
| 485(1), 485(1.1) | the court (it keeps jurisdiction over the offence and over the accused) | the accused (stays subject to it despite a failure to act in time, a missed adjournment rule, or an allowed non-appearance) | power / liability | `s 485(1) jurisdiction over the offence is lost by reason of the failure`; `s 485(1.1) jurisdiction over the accused is lost by reason of the failure to appear personally or in person` |
| 485(2) | the court, judge, provincial court judge or justice (summons or warrant within three months) | the accused or defendant | power / liability | `s 485(2) the court, judge, provincial court judge or justice may issue a summons` |
| 485(3) | the accused (the proceedings are deemed dismissed for want of prosecution) | the prosecutor (no recommencement except under s 485.1) | immunity / disability | `s 485(3) the proceedings are deemed to be dismissed for want of prosecution` |
| 485(4) | the court, judge, provincial court judge or justice (adjourn and make an order) | the parties, among them an accused who has been misled or prejudiced | power / liability | `s 485(4) the court, judge, provincial court judge or justice may adjourn the proceeding and make an order` |
| 485(5) | - | - | none (a rule of application: Part XVI applies with the necessary changes) | `s 485(5) the provisions of Part XVI apply with such modifications as the circumstances require` |
| 485.1 | the accused | the prosecutor (no new information or indictment on the same transaction without the Attorney General's personal consent or a judge's order) | immunity / disability | `s 485.1 a new information or a new indictment in respect of the same transaction is barred` |
| 485.2(1) | a justice or judge (summons under the Identification of Criminals Act) | the accused or offender | power / liability | `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` |
| 485.2(2) | the offender (no summons unless proceedings are ongoing and sentencing has not concluded) | the justice or judge | immunity / disability | `s 485.2(2) subsection (1) applies in respect of the offender` |
| 485.2(3) | the justice or judge (reasons for the application) | the applicant | claim / duty | `s 485.2(3) the application states the reasons required` |
| 485.2(4) | the justice or judge (proceed ex parte) | the accused or offender | power / liability | `s 485.2(4) the justice or judge may proceed ex parte to determine the application` |
| 485.2(5), 485.2(6) | the applicant (telecommunication) and the person who makes a statement in writing instead of swearing an oath | the justice or judge (cannot require an oath or an application in person) | privilege / no-right | `s 485.2(5) the application may be made by the means of telecommunication`; `s 485.2(6) the person may make a statement in writing instead of swearing an oath` |
| 485.2(7) | the accused or offender (a summons with the required contents) | the justice or judge who issues it | claim / duty | `s 485.2(7) the summons has the contents required` |
| 485.2(8) | the accused or offender (service by a peace officer in the way the subsection allows) | the peace officer who serves it | claim / duty | `s 485.2(8) the summons was served as required` |
| 486(1) | the presiding judge or justice (exclude the public, or a screen for the witness) | the public and the witness | power / liability | `s 486(1) the presiding judge or justice may order the exclusion of the public or that the witness testify behind a screen` |
| 486(1) | the accused and the public (proceedings in open court) | the court | claim / duty | `s 486(1) the proceedings against the accused are held in open court` |
| 486(1.1), 486.1(2.1), 486.2(2.1), 486.3(4.1), 486.7(2) | the prosecutor, the witness or the other person who may apply (to apply during the proceedings or before they begin) | the judge or justice named (liable to hear it) | power / liability | `s 486(1.1) the application may be made to the judge or justice`; `s 486.1(2.1) the application may be made to the judge or justice`; `s 486.2(2.1) the application may be made to the judge or justice`; `s 486.3(4.1) the application may be made to the judge or justice`; `s 486.7(2) the application may be made to the judge or justice` |
| 486(2), 486.1(3), 486.2(3), 486.2(4), 486.3(4), 486.31(3), 486.5(5), 486.5(7), 486.7(3) | the accused, the prosecutor and the witness (that the factors are weighed) | the judge or justice | claim / duty | `s 486(2) factor`; `s 486.1(3) factor`; `s 486.2(3) factor`; `s 486.2(4) the judge or justice must order that the witness testify in accordance with subsection (2)`; `s 486.3(4) factor`; `s 486.31(3) factor` (+3 more) |
| 486(3), 486.1(7), 486.2(7), 486.3(6) | the accused and the prosecutor (reasons stated or put in writing) | the judge or justice | claim / duty | `s 486(3) the judge or justice must state the reason for not making an order`; `s 486.1(7) the judge or justice must include the reasons for their decision, in writing, in the record`; `s 486.2(7) the judge or justice must include the reasons for their decision, in writing, in the record`; `s 486.3(6) the judge or justice must include the reasons for their decision, in writing, in the record` |
| 486(4), 486.1(6), 486.2(6), 486.3(5), 486.31(4), 486.7(4) | the accused (and the witness): no adverse inference from the making or not making of an order | the judge, justice or jury who would draw it | immunity / disability | `s 486(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section`; `s 486.1(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section`; `s 486.2(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section`; `s 486.3(5) an adverse inference may be drawn from the fact that counsel is, or is not, appointed under this section`; `s 486.31(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section`; `s 486.7(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` |
| 486.1(1), 486.1(1.1), 486.2(1), 486.2(1.1) | the witness under 18, with a disability, or the victim of a listed offence (support person or animal; testimony outside the court room or behind a screen) | the judge or justice | claim / duty | `s 486.1(1) the judge or justice must order that a support person or a support animal be permitted`; `s 486.1(1.1) the judge or justice must order that a support person or a support animal be permitted for a victim`; `s 486.2(1) the judge or justice must order that the witness testify outside the court room or behind a screen, at the option of the witness`; `s 486.2(1.1) the judge or justice must order that the victim testify outside the court room or behind a screen, at the option of the witness` |
| 486.3(1), 486.3(2) | the witness under 18, or the victim of a listed offence (not to be cross-examined personally by the accused) | the judge or justice (who must also appoint counsel); the accused is under a disability to cross-examine personally | claim / duty | `s 486.3(1) the judge or justice must appoint counsel to conduct the cross-examination`; `s 486.3(2) the judge or justice must appoint counsel to conduct the cross-examination` |
| 486.1(1.2), 486.2(1.2), 486.3(2.1), 486.4(3.1) | the witness or victim (to be informed that an application may be made) | the judge or justice (inquiry of the prosecutor) | claim / duty | `s 486.1(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made`; `s 486.2(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made`; `s 486.3(2.1) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made`; `s 486.4(3.1)(a), (b) the presiding judge or justice must inquire` |
| 486.1(2), 486.2(2), 486.3(3) | the judge or justice (order for another witness) | the witness and the accused | power / liability | `s 486.1(2) the judge or justice may order that a support person or a support animal be permitted for another witness`; `s 486.2(2) the judge or justice may order that another witness testify outside the court room or behind a screen, at the option of the witness`; `s 486.3(3) the judge or justice may order that the accused not personally cross-examine another witness` |
| 486.1(4) | the accused and the witness (a witness is not to be the support person) | the judge or justice (barred, unless necessary for the proper administration of justice) | immunity / disability | `s 486.1(4) the judge or justice is barred from permitting a witness to be a support person` |
| 486.1(5) | the judge or justice (no communication between the support person and the witness while the witness testifies) | the support person and the witness | power / liability | `s 486.1(5) the judge or justice may order that the support person and the witness not communicate with each other while the witness testifies` |
| 486.2(5) | the accused (no testimony outside the court room unless arrangements for watching and for communicating with counsel are made) | the court and the witness | immunity / disability | `s 486.2(5) the witness is barred from testifying outside the court room in accordance with the order` |
| 486.31(1), 486.31(2) | the judge or justice (non-disclosure of the witness's identity; a hearing, in private) | everyone in the proceedings | power / liability | `s 486.31(1) the judge or justice may order that information that could identify the witness not be disclosed in the course of the proceedings`; `s 486.31(2) the judge or justice may hold a hearing, and the hearing may be in private` |
| 486.4(1) | the presiding judge or justice (ban on publishing identifying information) | anyone who would publish, broadcast or transmit it | power / liability | `s 486.4(1) the presiding judge or justice may make an order directing that information that could identify the victim or a witness not be published` |
| 486.4(2), 486.4(2.2), 486.4(3) | the victim, the prosecutor and the witness under 18 (a mandatory order on application; to be informed of the right to apply and of the order) | the presiding judge or justice | claim / duty | `s 486.4(2)(a) the presiding judge or justice must inform the person of the right to make an application for the order`; `s 486.4(2.2) the subsection applies to the proceedings`; `s 486.4(3) the judge or justice must make an order directing that information that could identify the person not be published` |
| 486.4(2.1) | the presiding judge or justice (victim under 18, other offences) | anyone who would publish | power / liability | `s 486.4(2.1) the presiding judge or justice may make an order directing that information that could identify the victim not be published` |
| 486.4(3.2), 486.5(8.2) | the judge or justice (to be told what the prosecutor has done to inform) | the prosecutor | claim / duty | `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done`; `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done` |
| 486.4(4), 486.4(5), 486.5(3), 486.5(3.1) | the person who discloses information in the administration of justice, or who discloses their own information to a person in a relationship of trust | -: the order does not reach the disclosure (the ban's beneficiaries have no right against it) | privilege / no-right | `s 486.4(4) the order applies to the disclosure of information`; `s 486.4(5) the order applies to the disclosure of information by the victim or witness`; `s 486.5(3) the order applies to the disclosure of information`; `s 486.5(3.1) the order applies to the disclosure of information by the victim, witness or justice system participant` |
| 486.5(1), 486.5(2) | the judge or justice (ban for victims, witnesses, justice system participants) | anyone who would publish | power / liability | `s 486.5(1) the judge or justice may make an order directing that information that could identify the victim or witness not be published`; `s 486.5(2) the judge or justice may make an order directing that information that could identify the justice system participant not be published` |
| 486.5(2.1) | - | - | none (a list of offences for the purposes of 486.5(2)) | `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)` |
| 486.5(4) | the prosecutor, the accused and others affected (notice of the application) | the applicant | claim / duty | `s 486.5(4)(a) the applicant has applied as required` |
| 486.5(5.1), 486.5(8.1) | the victim, witnesses and justice system participants (to be informed of the order and of the right to apply) | the judge or justice | claim / duty | `s 486.5(5.1)(a), (b) the judge or justice must inquire`; `s 486.5(8.1) the judge or justice must inform the victims, witnesses and justice system participants of the order's existence and of their right to apply to revoke or vary it` |
| 486.5(6), 486.51(3) | the judge or justice (a hearing, which may be in private) | the parties | power / liability | `s 486.5(6) the judge or justice may hold a hearing, and the hearing may be in private`; `s 486.51(3) the court must hold a hearing to determine whether the order should be varied or revoked` |
| 486.5(8) | the judge or justice (conditions on the order) | the person subject to the order | power / liability | `s 486.5(8) the order may be subject to the condition` |
| 486.5(9) | the victim, witness or participant protected by the order | everyone: no one may publish, broadcast or transmit what the order covers | claim / duty | `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` |
| 486.51(1), 486.51(2) | the person who is the subject of the order (to have the prosecutor apply; to have the order varied or revoked without a hearing) | the prosecutor and the court | claim / duty | `s 486.51(1) the prosecutor must make an application to vary or revoke the order on the person's behalf`; `s 486.51(2) the court must vary or revoke the order without holding a hearing` |
| 486.51(4) | any other person who is the subject of a publication ban (their privacy interests are weighed on an application to vary) | the court | claim / duty | `s 486.51(4) the court must take into account whether it is possible to vary the order in a manner that protects the privacy interests of any other person` |
| 486.51(5) | the applicant (no notice to the accused) | the accused (no claim to notice) | privilege / no-right | `s 486.51(5) the applicant is required to provide notice of the application to vary or revoke the order to the accused` |
| 486.51(6) | the court (no submissions from the accused on the application) | the accused (disabled from making them) | immunity / disability | `s 486.51(6) the accused is permitted to make submissions in relation to the application` |
| 486.51(7) | the accused (to be notified when the order is varied or revoked) | the prosecutor | claim / duty | `s 486.51(7) the prosecutor must notify the accused` |
| 486.6(1) | the Crown (an offence punishable on summary conviction) | anyone who fails to comply with a ban | power / liability | `s 486.6(1) the order is one made under any of subsections 486.4(1) to (3) or subsection 486.5(1) or (2)` |
| 486.6(1.1) | the person who is the subject of the order (no prosecution for failing to comply, save in the prosecutor's opinion) | the prosecutor | immunity / disability | `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` |
| 486.6(2) | - | - | none (the order applies to the disclosure; a rule of application) | `s 486.6(2) the order applies to prohibit the publication of information that could identify a victim, witness or justice system participant in those proceedings` |
| 486.7(1) | the presiding judge or justice (order to protect a witness's security) | the accused and the witness | power / liability | `s 486.7(1) the presiding judge or justice may make an order to protect the security of a witness` |
| 486.71 | the witness (one order only regarding the same witness) | the judge or justice (prohibited from making more than one) | immunity / disability | `s 486.71 the judge or justice is prohibited from making more than one order regarding the same witness` |
| 487(1) | a justice (search warrant) | the occupier or person in possession of the building, receptacle or place | power / liability | `s 487(1) the justice may issue a warrant to search the building, receptacle or place` |
| 487(2) | the peace officer or public officer named in the warrant (execute anywhere in Canada) | the occupier | power / liability | `s 487(2) the officer who executes the warrant has the authority required` |
| 487(2.1) | the person carrying out the search (use a computer system, make a hard copy, copy) | the person in possession or control | privilege / no-right | `s 487(2.1) the person may do the act` |
| 487(2.2) | the person carrying out the search | the person in possession or control (must permit it once the warrant is presented) | claim / duty | `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` |
| 487(3), 487(4) | - | - | none (487(3) the form of the warrant; 487(4) repealed) | `s 487(3) the search warrant may be in the form set out as Form 5` |
| 487.01(1) | a judge (general warrant) | the person whose property or privacy the technique reaches | power / liability | `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` |
| 487.01(2) | the person searched (nothing in the general warrant permits interference with their bodily integrity) | the judge and the officers | immunity / disability | `s 487.01(2) subsection (1) permits the act` |
| 487.01(3), 487.01(4) | the person searched, and the person observed by a television camera or similar device (terms in the warrant to keep the search reasonable and the observed person's privacy respected) | the judge who issues the warrant (it must contain them) | claim / duty | `s 487.01(3) the warrant contains the terms and conditions required`; `s 487.01(4) the warrant contains the privacy terms and conditions required` |
| 487.01(5), 487.01(7) | - | - | none (487.01(5) the interception provisions apply to a video-surveillance warrant: a rule of application; (7) repealed) | `s 487.01(5) the provision applies, with such modifications as the circumstances require, to the warrant` |
| 487.01(5.1) | the person whose place was entered covertly (notice of the entry and search) | the judge (the warrant must require it) and the officer | claim / duty | `s 487.01(5.1) the warrant requires notice of the covert entry and search as required` |
| 487.01(5.2) | the judge (extend the period for giving notice) | the person to be notified | power / liability | `s 487.01(5.2) the extension does not exceed three years` |
| 487.01(6) | the officer (execute anywhere in Canada) | the occupier | power / liability | `s 487.01(6) the general warrant may be executed at the place` |
| 487.011 | - | - | none (definitions for sections 487.012 to 487.0199) | `s 487.011 the definitions apply in the section` |
| 487.012(1), 487.012(5) | the peace officer or public officer (a demand to preserve computer data, with conditions) | the person to whom it is made | power / liability | `s 487.012(1) the peace officer or public officer may make a demand to preserve computer data`; `s 487.012(5) the officer may revoke the condition at any time` |
| 487.012(2), 487.012(3), 487.012(6) | the person (no demand without the grounds; none to a person under investigation; no further demand for the same data) | the peace officer or public officer | immunity / disability | `s 487.012(2) the peace officer or public officer may make the demand`; `s 487.012(3) the demand is barred against the person under investigation for the offence`; `s 487.012(6) another demand to preserve the same computer data in connection with the investigation is barred` |
| 487.012(4) | the peace officer or public officer (revoke the demand); the person (the demand expires) | the person to whom it is made | power / liability | `s 487.012(4) the demand expires on the day` |
| 487.013(1), 487.0131(1) | the justice or judge (preservation order; keep-account-open order) | the person ordered | power / liability | `s 487.013(1) the justice or judge may order the person to preserve computer data`; `s 487.0131(1) the justice or judge may order the person to keep the account open or active` |
| 487.013(2), 487.013(3), 487.0131(2), 487.0131(4), 487.014(2), 487.0141(2), 487.0141(10), 487.015(2), 487.016(2), 487.017(2), 487.018(3), 487.0191(2), 487.0131(8) | the person against whom the order is sought (no order unless the justice or judge is satisfied on oath) | the justice or judge | immunity / disability | `s 487.013(2) the justice or judge has the satisfaction required before making the order`; `s 487.013(3) the justice or judge has the further satisfaction required for an offence against a law of a foreign state`; `s 487.0131(2) the justice or judge has the satisfaction required before making the order`; `s 487.0131(4) the order contains the notification requirement`; `s 487.014(2) the justice or judge has the satisfaction required before making the order`; `s 487.0141(2) the justice or judge has the satisfaction required before making the order` (+7 more) |
| 487.013(4), 487.0131(3), 487.014(3), 487.0141(3), 487.015(3), 487.016(3), 487.017(3), 487.018(4), 487.0191(3) | - | - | none (the form of the order) | `s 487.013(4) the order is in Form 5.003`; `s 487.0131(3) the order is in Form 5.0032`; `s 487.014(3) the order is in Form 5.005`; `s 487.0141(3) the order is in Form 5.0051`; `s 487.015(3) the order is in Form 5.006`; `s 487.016(3) the order is in Form 5.007` (+3 more) |
| 487.013(5), 487.0131(5), 487.014(4), 487.0141(7), 487.015(5), 487.016(4), 487.017(4), 487.018(5) | the person under investigation for the offence (no order may be made against them) | the justice or judge | immunity / disability | `s 487.013(5) the order is barred against the person under investigation for the offence`; `s 487.0131(5) the order is barred against the person under investigation for the offence`; `s 487.014(4) the order is barred against the person under investigation for the offence`; `s 487.0141(7) the order is barred against the person under investigation for the offence`; `s 487.015(5) the order is barred against the person under investigation for the offence`; `s 487.016(4) the order is barred against the person under investigation for the offence` (+2 more) |
| 487.013(6), 487.0131(6), 487.0141(8) | the person ordered (the order expires after the stated days) | the peace officer or public officer | immunity / disability | `s 487.013(6) the order expires on the day`; `s 487.0131(6) the order expires on the day`; `s 487.0141(8) the order expires on the day` |
| 487.0131(7), 487.0141(9) | the justice or judge (renew for not more than 60 days) | the person ordered | power / liability | `s 487.0131(7) the justice or judge may renew the order for the period`; `s 487.0141(9) the justice or judge may renew the order for the period` |
| 487.014(1), 487.0141(1), 487.015(1), 487.016(1), 487.017(1), 487.018(1), 487.018(2) | the justice or judge (production orders) | the person ordered to produce or prepare and produce | power / liability | `s 487.014(1) the justice or judge may order the person to produce a document or to prepare and produce a document`; `s 487.0141(1) the justice or judge may order the person to produce a document on any of the dates specified in the order`; `s 487.015(1) the justice or judge may order the person to prepare and produce a document containing transmission data`; `s 487.016(1) the justice or judge may order the person to prepare and produce a document containing transmission data`; `s 487.017(1) the justice or judge may order the person to prepare and produce a document containing tracking data`; `s 487.018(1) the justice or judge may order the document to set out the data` (+1 more) |
| 487.0141(4), 487.0141(5), 487.0141(11) | the justice or judge (specify up to 10 dates; require copies of reports) | the person ordered | power / liability | `s 487.0141(4) the order may specify the dates`; `s 487.0141(5) the order may require the person to produce a copy of the reports`; `s 487.0141(11) the renewed order may specify the dates` |
| 487.0141(6) | the person ordered (not to be required to produce more than once in 72 hours, or documents that did not then exist) | the peace officer or public officer | immunity / disability | `s 487.0141(6)(a) the person may be required to produce documents again` |
| 487.015(4) | the peace officer or public officer (serve the order within 60 days, or one year) | the person ordered | power / liability | `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` |
| 487.015(6) | the justice or judge (a report on what was produced) | the peace officer or public officer | claim / duty | `s 487.015(6) the day from which the report is due as soon as feasible` |
| 487.019(1), 487.019(3) | the justice or judge (conditions; revoke or vary) | the person subject to the order | power / liability | `s 487.019(1) the order may contain the condition`; `s 487.019(3) the justice or judge may revoke or vary the order` |
| 487.019(2) | the justice or judge who made the order (it has effect throughout Canada) | the person ordered | power / liability | `s 487.019(2) the order has effect at the place` |
| 487.0191(1) | the justice or judge (order not to disclose the demand or order) | the person ordered | power / liability | `s 487.0191(1) the justice or judge may make an order prohibiting the person from disclosing the existence or contents of the demand or order` |
| 487.0191(4), 487.01921(1), 487.0193(1) | the person (apply in writing to revoke or vary) | the justice or judge (liable to hear it) | power / liability | `s 487.0191(4) the applicant may apply to revoke or vary the order`; `s 487.01921(1) the person may apply to revoke or vary the order`; `s 487.0193(1) the person, financial institution or entity may apply to revoke or vary the order` |
| 487.0192(1), 487.0192(2) | the person ordered (an order that states the officer, time, place and form) | the justice or judge who makes it | claim / duty | `s 487.0192(1) the order contains the particulars required`; `s 487.0192(2) the order made under section 487.015 contains the particulars required` |
| 487.0192(3) | the person ordered (produce on an electro-magnetic medium) | the peace officer or public officer | privilege / no-right | `s 487.0192(3) the order may specify that a document may be produced on or through an electro-magnetic medium` |
| 487.0192(4) | the person ordered (sections 489.1 and 490 do not apply to what they produce) | the peace officer or public officer | immunity / disability | `s 487.0192(4) the provision applies to the document` |
| 487.0192(5), 487.0192(6) | the Crown (a copy is admissible on proof by affidavit, a prepared document is an original) | the accused or other party who would object | power / liability | `s 487.0192(5) the copy is admissible in evidence`; `s 487.0192(6) the document is considered to be original for the purposes of the Canada Evidence Act` |
| 487.01921(2), 487.0193(2) | the peace officer or public officer named in the order (notice of the application) | the person who would apply (disabled from applying without notice) | claim / duty | `s 487.01921(2) the person may make the application`; `s 487.0193(2) the notice may be given` |
| 487.01921(3) | the peace officer or public officer | the person subject to the order (must comply pending the decision) | claim / duty | `s 487.01921(3) the person must comply with the order pending the decision` |
| 487.01921(4) | the person who applied (a hearing within 14 days) | the justice or judge | claim / duty | `s 487.01921(4) the hearing must be commenced` |
| 487.01921(5), 487.0193(4) | the justice or judge (revoke or vary) | the person subject to the order | power / liability | `s 487.01921(5) the justice or judge may revoke or vary the order`; `s 487.0193(4) the justice or judge may revoke or vary the order` |
| 487.0193(3) | the person, institution or entity (not required to prepare or produce until a final decision) | the peace officer or public officer | immunity / disability | `s 487.0193(3) the person, institution or entity is required to prepare or produce the document` |
| 487.0194(1), 487.0194(2), 487.0194(3), 487.0194(4) | the person to whom the data or documents relate (destruction of what was preserved) | the person who holds them (must destroy as soon as feasible, subject to a later order) | claim / duty | `s 487.0194(1) the person to whom a preservation demand is made must destroy it`; `s 487.0194(2) the person subject to a preservation order must destroy it`; `s 487.0194(3) the earlier day after which the person must destroy the computer data as soon as feasible`; `s 487.0194(4) the person must destroy the computer data when the document is obtained under a warrant` |
| 487.0195(1) | the officer who asks, and the person who voluntarily preserves, keeps open or provides | -: others have no right against it | privilege / no-right | `s 487.0195(1) a preservation demand, preservation order, keep account open or active order or production order is necessary for the officer to ask` |
| 487.0195(2) | the person who preserves, keeps open or provides at an officer's request | anyone who would sue or prosecute | immunity / disability | `s 487.0195(2) the person incurs criminal or civil liability for doing so` |
| 487.0196 | the officer (compliance is required despite self-incrimination); the individual (no use of the prepared document in a later criminal proceeding) | the person ordered; the Crown | claim / duty and immunity / disability | `s 487.0196 the document the individual was required to prepare may be used or received in evidence against them` |
| 487.0197, 487.0198, 487.0199 | the Crown (offences for contravening a demand, an order or section 487.0194) | the person who contravenes without lawful excuse | power / liability | `s 487.0197 the fine is within the maximum`; `s 487.0198 the person, financial institution or entity is guilty of an offence punishable on summary conviction`; `s 487.0199 the person is guilty of an offence punishable on summary conviction` |
| 487.02(1), 487.02(2) | the judge or justice (assistance order, which may be issued by telecommunication) | the person whose assistance is required | power / liability | `s 487.02(1) the assistance order has effect at the place`; `s 487.02(2) the order to provide assistance may be issued by a means of telecommunication` |
| 487.021(1), 487.021(2), 487.03 | - | - | none (487.021 a parliamentary review, machinery; 487.03 repealed) | - |
| 487.04 | - | - | none (definitions of the designated offences for sections 487.05 to 487.0911) | `s 487.04 the definitions apply in the section` |

## Marginal readings for a lawyer (ccc16)

The two readings the brief leaves for a lawyer: **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no (N2 of 2026-11-04); **(b)** a prohibition or grant limited by its own wording does not (the case outside the limit is `NOTHING`). Both are taken as the status quo. For each reading the other reading is the opposite answer: a branch resting on (a) answers `NOTHING` on the other reading, and a branch resting on (b) answers `JUST FALSE`.

The sites that need a lawyer first, each with its fork id: the failed "if" on a power (F1: NOTHING; other reading JUST FALSE); the literal "Where" on a power (F2: JUST FALSE; other reading NOTHING); the on-application and when kind (the name-test sweep above: NOTHING; other reading JUST FALSE, 26 sites); a stated period or maximum (F3, F17); the duty with an unmet trigger (F5); a met "unless" or "without lawful excuse" (F6); the exclusions (F10, in particular s 486.7(1)); the "until" sites (F11).

Per function (every layer-1 function with a `JUST FALSE` or a limited-by-its-own-wording `NOTHING` branch; `work/gen_notes.py` reads them from the `FALSE-kind` and `NOTHING-kind` comments): the count of branches resting on each reading, and the first words of the text for each.

| function | module | JUST FALSE branches (reading (a)) | NOTHING branches limited by wording (reading (b)) | first words |
| --- | --- | --- | --- | --- |
| `s 487.04 the definitions apply in the section` | dna-definitions | 0 | 1 | "In this section and in sections 487.05 to 487.0911," |
| `s 487.04 DNA` | dna-definitions | 1 | 0 | "DNA means deoxyribonucleic acid" |
| `s 487.04 Young Offenders Act` | dna-definitions | 1 | 0 | "Young Offenders Act means chapter Y-1 of the Revised Statutes of Canad" |
| `s 487.04 the offence is a primary designated offence` | dna-definitions | 4 | 0 | "primary designated offence means" |
| `s 487.04 secondary designated offence the answer of each of paragraphs (a) to (d.2)` | dna-definitions | 10 | 0 | "(i) an offence referred to in paragraph (a) or (b)" |
| `s 487.04 the paragraphs of a definition are read together` | dna-definitions | 1 | 0 | "secondary designated offence means an offence, other than a primary de" |
| `s 487.04 secondary designated offence (e) an attempt or a conspiracy` | dna-definitions | 2 | 0 | "(e) an attempt to commit or, other than for the purposes of subsection" |
| `s 487.04 the offence is a secondary designated offence` | dna-definitions | 1 | 0 | "secondary designated offence means an offence, other than a primary de" |
| `s 487.04 the offence is a designated offence` | dna-definitions | 1 | 0 | "designated offence means a primary designated offence or a secondary d" |
| `s 483 the judge or provincial court judge may do alone what two or more justices are authorized to do` | officials | 0 | 1 | "Every judge or provincial court judge authorized by the law of the pro" |
| `s 484 the judge or provincial court judge has the same power and authority to preserve order as the superior court of criminal jurisdiction` | officials | 0 | 1 | "in a court over which he presides" |
| `s 485(1) jurisdiction over the offence is lost by reason of the failure` | officials | 1 | 0 | "Jurisdiction over an offence is not lost by reason of the failure of a" |
| `s 485(1.1) jurisdiction over the accused is lost by reason of the failure to appear personally or in person` | officials | 1 | 1 | "Jurisdiction over an accused is not lost by reason of the failure of t" |
| `s 485(2) the court, judge, provincial court judge or justice may issue a summons` | officials | 2 | 0 | "Where jurisdiction over an accused or a defendant is lost and has not " |
| `s 485(2) the court, judge, provincial court judge or justice may issue a warrant for the arrest` | officials | 2 | 1 | "Where jurisdiction over an accused or a defendant is lost and has not " |
| `s 485(3) the proceedings are deemed to be dismissed for want of prosecution` | officials | 2 | 0 | "Where no summons or warrant is issued under subsection (2) within the " |
| `s 485(3) the proceedings may be recommenced` | officials | 1 | 2 | "shall not be recommenced except in accordance with section 485.1" |
| `s 485(4) the court, judge, provincial court judge or justice may adjourn the proceeding and make an order` | officials | 1 | 0 | "Where, in the opinion of the court, judge, provincial court judge or j" |
| `s 485(5) the provisions of Part XVI apply with such modifications as the circumstances require` | officials | 1 | 0 | "where a summons or warrant is issued under subsection (2)" |
| `s 485.1 a new information or a new indictment in respect of the same transaction is barred` | officials | 1 | 2 | "Where an indictment in respect of a transaction is dismissed or deemed" |
| `s 485.2(1) a justice or judge may issue a summons requiring the accused or offender to appear for the purposes of the Identification of Criminals Act` | officials | 0 | 1 | "may, on application in writing and on oath in Form 6.1, issue a summon" |
| `s 485.2(2) subsection (1) applies in respect of the offender` | officials | 1 | 0 | "Subsection (1) applies in respect of an offender only if proceedings a" |
| `s 485.2(3) the application states the reasons required` | officials | 1 | 0 | "The application must state the reasons why the measurements, processes" |
| `s 485.2(4) the justice or judge may proceed ex parte to determine the application` | officials | 0 | 1 | "an application made under subsection (1)" |
| `s 485.2(5) the application may be made by the means of telecommunication` | officials | 0 | 1 | "any means of telecommunication that produces a writing" |
| `s 485.2(6) the person may make a statement in writing instead of swearing an oath` | officials | 0 | 1 | "A person who uses a means of telecommunication referred to in subsecti" |
| `s 485.2(6) the statement is deemed to be a statement made under oath` | officials | 0 | 1 | "that statement is deemed to be a statement made under oath" |
| `s 485.2(7) the summons has the contents required` | officials | 1 | 0 | "The summons must" |
| `s 485.2(8) the summons was served as required` | officials | 3 | 0 | "The summons must be served by a peace officer" |
| `s 486(1) the proceedings against the accused are held in open court` | open-court | 0 | 1 | "but the presiding judge or justice may, on application of the prosecut" |
| `s 486(1) the presiding judge or justice may order the exclusion of the public or that the witness testify behind a screen` | open-court | 0 | 3 | "on application of the prosecutor or a witness or on his or her own mot" |
| `s 486(1.1) the application may be made to the judge or justice` | open-court | 0 | 4 | "during the proceedings, to the presiding judge or justice" |
| `s 486(2) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486(3) the judge or justice must state the reason for not making an order` | open-court | 2 | 1 | "the prosecutor or the accused applies for an order under subsection (1" |
| `s 486(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that an order is, or i" |
| `s 486.1(1) the judge or justice must order that a support person or a support animal be permitted` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is under " |
| `s 486.1(1.1) the judge or justice must order that a support person or a support animal be permitted for a victim` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is a vict" |
| `s 486.1(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | open-court | 1 | 0 | "If an application for an order under subsection (1) or (1.1) is not ma" |
| `s 486.1(2) the judge or justice may order that a support person or a support animal be permitted for another witness` | open-court | 0 | 2 | "on application of the prosecutor in respect of a witness, or on applic" |
| `s 486.1(2.1) the application may be made to the judge or justice` | open-court | 0 | 4 | "during the proceedings, to the presiding judge or justice" |
| `s 486.1(3) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.1(4) the judge or justice is barred from permitting a witness to be a support person` | open-court | 1 | 0 | "unless the judge or justice is of the opinion that doing so is necessa" |
| `s 486.1(5) the judge or justice may order that the support person and the witness not communicate with each other while the witness testifies` | open-court | 0 | 1 | "the support person and the witness not communicate with each other whi" |
| `s 486.1(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that an order is, or i" |
| `s 486.1(7) the judge or justice must include the reasons for their decision, in writing, in the record` | open-court | 1 | 0 | "If the judge or justice does not make an order under this section" |
| `s 486.2(1) the judge or justice must order that the witness testify outside the court room or behind a screen, at the option of the witness` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is under " |
| `s 486.2(1.1) the judge or justice must order that the victim testify outside the court room or behind a screen, at the option of the witness` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is a vict" |
| `s 486.2(1.2) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | open-court | 1 | 0 | "If an application for an order under subsection (1) or (1.1) is not ma" |
| `s 486.2(2) the judge or justice may order that another witness testify outside the court room or behind a screen, at the option of the witness` | open-court | 0 | 2 | "on application of the prosecutor in respect of a witness, or on applic" |
| `s 486.2(2.1) the application may be made to the judge or justice` | open-court | 0 | 4 | "during the proceedings, to the presiding judge or justice" |
| `s 486.2(3) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.2(4) the judge or justice must order that the witness testify in accordance with subsection (2)` | open-court | 1 | 0 | "If the judge or justice is of the opinion that it is necessary for a w" |
| `s 486.2(5) the witness is barred from testifying outside the court room in accordance with the order` | open-court | 1 | 1 | "unless arrangements are made for the accused, the judge or justice and" |
| `s 486.2(6) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that an order is, or i" |
| `s 486.2(7) the judge or justice must include the reasons for their decision, in writing, in the record` | open-court | 1 | 0 | "If the judge or justice does not make an order under this section" |
| `s 486.3(1) the judge or justice must order that the accused not personally cross-examine the witness under 18` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is under " |
| `s 486.3(1) the judge or justice must appoint counsel to conduct the cross-examination` | open-court | 1 | 0 | "If such an order is made, the judge or justice shall appoint counsel t" |
| `s 486.3(2) the judge or justice must order that the accused not personally cross-examine the victim` | open-court | 2 | 1 | "on application of the prosecutor in respect of a witness who is a vict" |
| `s 486.3(2) the judge or justice must appoint counsel to conduct the cross-examination` | open-court | 1 | 0 | "If such an order is made, the judge or justice shall appoint counsel t" |
| `s 486.3(2.1) the judge or justice must inquire of the prosecutor whether reasonable steps have been taken to inform the witness that an application may be made` | open-court | 1 | 0 | "If an application for an order under subsection (1) or (2) is not made" |
| `s 486.3(3) the judge or justice may order that the accused not personally cross-examine another witness` | open-court | 0 | 3 | "in respect of a witness who is not entitled to make an application und" |
| `s 486.3(3) the judge or justice must appoint counsel to conduct the cross-examination` | open-court | 1 | 0 | "If the order is made, the judge or justice shall appoint counsel to co" |
| `s 486.3(4) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.3(4.1) the application may be made to the judge or justice` | open-court | 0 | 4 | "during the proceedings, to the presiding judge or justice" |
| `s 486.3(5) an adverse inference may be drawn from the fact that counsel is, or is not, appointed under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that counsel is, or is" |
| `s 486.3(6) the judge or justice must include the reasons for their decision, in writing, in the record` | open-court | 1 | 0 | "If the judge or justice does not make an order under this section" |
| `s 486.31(1) the judge or justice may order that information that could identify the witness not be disclosed in the course of the proceedings` | open-court | 0 | 2 | "on application of the prosecutor in respect of a witness, or on applic" |
| `s 486.31(2) the judge or justice may hold a hearing, and the hearing may be in private` | open-court | 0 | 1 | "may hold a hearing to determine whether the order should be made" |
| `s 486.31(3) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.31(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that an order is, or i" |
| `s 486.7(1) the presiding judge or justice may make an order to protect the security of a witness` | open-court | 1 | 2 | "make any order, other than one that may be made under any of sections " |
| `s 486.7(2) the application may be made to the judge or justice` | open-court | 0 | 4 | "during the proceedings, to the presiding judge or justice" |
| `s 486.7(3) the judge or justice must consider the factor` | open-court | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.7(4) an adverse inference may be drawn from the fact that an order is, or is not, made under this section` | open-court | 1 | 0 | "No adverse inference may be drawn from the fact that an order is, or i" |
| `s 486.71 the judge or justice is prohibited from making more than one order regarding the same witness` | open-court | 1 | 1 | "nothing in sections 486 to 486.5 or 486.7 prohibits a judge or justice" |
| `s 487.011 the definitions apply in the section` | preservation | 0 | 1 | "The following definitions apply in this section and in sections 487.01" |
| `s 487.011 data` | preservation | 1 | 0 | "data means representations, including signs, signals or symbols, that " |
| `s 487.011 document` | preservation | 1 | 0 | "document means a medium on which data is registered or marked" |
| `s 487.011 judge` | preservation | 1 | 0 | "judge means a judge of a superior court of criminal jurisdiction or a " |
| `s 487.011 public officer` | preservation | 1 | 0 | "public officer means a public officer who is appointed or designated t" |
| `s 487.011 tracking data` | preservation | 1 | 0 | "tracking data means data that relates to the location of a transaction" |
| `s 487.011 transmission data` | preservation | 1 | 0 | "transmission data means data that" |
| `s 487.012(1) the peace officer or public officer may make a demand to preserve computer data` | preservation | 0 | 1 | "may make a demand to a person in Form 5.001 requiring them to preserve" |
| `s 487.012(2) the peace officer or public officer may make the demand` | preservation | 1 | 0 | "The peace officer or public officer may make the demand only if they h" |
| `s 487.012(3) the demand is barred against the person under investigation for the offence` | preservation | 0 | 1 | "A demand may not be made to a person who is under investigation for th" |
| `s 487.012(4) the peace officer or public officer may revoke the demand` | preservation | 0 | 1 | "may revoke the demand by notice given to the person at any time" |
| `s 487.012(4) the demand is in effect on the day` | preservation | 2 | 1 | "the demand expires" |
| `s 487.012(5) the officer who makes the demand may impose the condition in the demand` | preservation | 0 | 1 | "any conditions in the demand that they consider appropriate" |
| `s 487.012(5) the officer may revoke the condition at any time` | preservation | 0 | 1 | "may revoke a condition at any time by notice given to the person" |
| `s 487.012(6) another demand to preserve the same computer data in connection with the investigation is barred` | preservation | 0 | 1 | "may not make another demand requiring the person to preserve the same " |
| `s 487.013(1) the justice or judge may order the person to preserve computer data` | preservation | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.013(2) the justice or judge has the satisfaction required before making the order` | preservation | 1 | 0 | "must be satisfied by information on oath in Form 5.002" |
| `s 487.013(3) the justice or judge has the further satisfaction required for an offence against a law of a foreign state` | preservation | 1 | 1 | "the justice or judge must also be satisfied that a person or authority" |
| `s 487.013(4) the order is in Form 5.003` | preservation | 1 | 0 | "The order is to be in Form 5.003" |
| `s 487.013(5) the order is barred against the person under investigation for the offence` | preservation | 0 | 1 | "A person who is under investigation for an offence referred to in para" |
| `s 487.013(6) the order is in effect on the day` | preservation | 2 | 1 | "it expires 90 days after the day on which it is made" |
| `s 487.0131(1) the justice or judge may order the person to keep the account open or active` | preservation | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.0131(1) the person must keep the account open or active` | preservation | 1 | 1 | "unless the holder of the account requests that the person close or dea" |
| `s 487.0131(2) the justice or judge has the satisfaction required before making the order` | preservation | 1 | 0 | "must be satisfied by information on oath in Form 5.0031" |
| `s 487.0131(3) the order is in Form 5.0032` | preservation | 1 | 0 | "The order is to be in Form 5.0032" |
| `s 487.0131(4) the order contains the notification requirement` | preservation | 1 | 0 | "The order is to require the person to notify a peace officer or public" |
| `s 487.0131(5) the order is barred against the person under investigation for the offence` | preservation | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.0131(6) the order is in effect on the day` | preservation | 2 | 1 | "it expires 60 days after the day on which it is made" |
| `s 487.0131(7) the justice or judge may renew the order for the period` | preservation | 1 | 1 | "for a period of not more than 60 days" |
| `s 487.0131(8) the justice or judge has the satisfaction required before renewing the order` | preservation | 1 | 0 | "Before renewing the order, the justice or judge must be satisfied by i" |
| `s 487.014(1) the justice or judge may order the person to produce a document or to prepare and produce a document` | production-orders | 0 | 1 | "Subject to sections 487.015 to 487.018, on ex parte application made b" |
| `s 487.014(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.014(3) the order is in Form 5.005` | production-orders | 1 | 0 | "The order is to be in Form 5.005" |
| `s 487.014(4) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.0141(1) the justice or judge may order the person to produce a document on any of the dates specified in the order` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.0141(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.0141(3) the order is in Form 5.0051` | production-orders | 1 | 0 | "The order is to be in Form 5.0051" |
| `s 487.0141(4) the order may specify the dates` | production-orders | 2 | 0 | "The order may specify up to 10 dates" |
| `s 487.0141(5) the order may require the person to produce a copy of the reports` | production-orders | 0 | 1 | "if the justice or judge is satisfied by information on oath in Form 5." |
| `s 487.0141(6)(a) the person may be required to produce documents again` | production-orders | 1 | 1 | "The person must not be required to (a) produce documents more than onc" |
| `s 487.0141(6)(b) the person may be required to produce a copy of a document that was in their possession or control before the day on which the order is made` | production-orders | 1 | 1 | "The person must not be required to" |
| `s 487.0141(6)(c) the person may be required to prepare and produce a document that contains data that was in their possession or control before the day on which the order is made` | production-orders | 1 | 1 | "The person must not be required to" |
| `s 487.0141(7) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.0141(8) the order is in effect on the day` | production-orders | 2 | 1 | "it expires 60 days after the day on which it is made" |
| `s 487.0141(9) the justice or judge may renew the order for the period` | production-orders | 1 | 1 | "for a period of not more than 60 days" |
| `s 487.0141(10) the justice or judge has the satisfaction required before renewing the order` | production-orders | 1 | 0 | "Before renewing the order, the justice or judge must be satisfied by i" |
| `s 487.0141(11) the renewed order may specify the dates` | production-orders | 2 | 0 | "it may specify up to 10 dates during the period for which it is renewe" |
| `s 487.015(1) the justice or judge may order the person to prepare and produce a document containing transmission data` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer for " |
| `s 487.015(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.015(3) the order is in Form 5.006` | production-orders | 1 | 0 | "The order is to be in Form 5.006" |
| `s 487.015(4) the peace officer or public officer may serve the order on the person on the day` | production-orders | 3 | 0 | "within 60 days after the day on which the order is made" |
| `s 487.015(5) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.015(6) the report states what is required` | production-orders | 1 | 0 | "The report must state the name and address of each person on whom the " |
| `s 487.016(1) the justice or judge may order the person to prepare and produce a document containing transmission data` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.016(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.016(3) the order is in Form 5.007` | production-orders | 1 | 0 | "The order is to be in Form 5.007" |
| `s 487.016(4) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.017(1) the justice or judge may order the person to prepare and produce a document containing tracking data` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.017(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.017(3) the order is in Form 5.007` | production-orders | 1 | 0 | "The order is to be in Form 5.007" |
| `s 487.017(4) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A person who is under investigation for the offence referred to in sub" |
| `s 487.018(1) the justice or judge may order the document to set out the data` | production-orders | 0 | 2 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.018(2) the order may also require the document to set out the identifying data` | production-orders | 0 | 2 | "For the purpose of confirming the identity of a person who is named or" |
| `s 487.018(3) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.004" |
| `s 487.018(4) the order is in Form 5.008` | production-orders | 1 | 0 | "The order is to be in Form 5.008" |
| `s 487.018(5) the order is barred against the person under investigation for the offence` | production-orders | 0 | 1 | "A financial institution, person or entity that is under investigation " |
| `s 487.019(1) the order may contain the condition` | production-orders | 0 | 1 | "An order made under any of sections 487.013 to 487.018 may contain any" |
| `s 487.019(1) the order may contain the condition to protect a privileged communication` | production-orders | 0 | 1 | "including, in the case of an order made under section 487.014 or 487.0" |
| `s 487.019(2) the order has effect at the place` | production-orders | 0 | 1 | "The order has effect throughout Canada" |
| `s 487.019(3) the justice or judge may revoke or vary the order` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer, the" |
| `s 487.019(3) the peace officer or public officer must give notice of the revocation or variation to the person who is subject to the order` | production-orders | 0 | 1 | "The peace officer or public officer must give notice of the revocation" |
| `s 487.0191(1) the justice or judge may make an order prohibiting the person from disclosing the existence or contents of the demand or order` | production-orders | 0 | 1 | "On ex parte application made by a peace officer or public officer, a j" |
| `s 487.0191(2) the justice or judge has the satisfaction required before making the order` | production-orders | 1 | 0 | "must be satisfied by information on oath in Form 5.009" |
| `s 487.0191(3) the order is in Form 5.0091` | production-orders | 1 | 0 | "The order is to be in Form 5.0091" |
| `s 487.0191(4) the applicant may apply to revoke or vary the order` | production-orders | 0 | 1 | "may apply in writing to the justice or judge who made the order — or t" |
| `s 487.0192(1) the order contains the particulars required` | production-orders | 1 | 1 | "must require a person, financial institution or entity to produce the " |
| `s 487.0192(2) the order made under section 487.015 contains the particulars required` | production-orders | 1 | 1 | "must require a person to produce the document to a peace officer or pu" |
| `s 487.0192(3) the order may specify that a document may be produced on or through an electro-magnetic medium` | production-orders | 0 | 1 | "an order under any of sections 487.014 to 487.018" |
| `s 487.0192(4) the provision applies to the document` | production-orders | 1 | 1 | "sections 489.1 and 490 do not apply to a document that is produced und" |
| `s 487.0192(5) the copy is admissible in evidence` | production-orders | 0 | 1 | "is admissible in evidence in proceedings under this or any other Act o" |
| `s 487.0192(6) the document is considered to be original for the purposes of the Canada Evidence Act` | production-orders | 0 | 1 | "A document that is prepared for the purpose of production is considere" |
| `s 487.01921(1) the person may apply to revoke or vary the order` | production-orders | 0 | 1 | "A person who is subject to an order made under section 487.0131 may ap" |
| `s 487.01921(2) the person may make the application` | production-orders | 1 | 0 | "The person may make the application only if they give at least three d" |
| `s 487.01921(3) the person must comply with the order pending the decision` | production-orders | 1 | 0 | "must comply with the order until a decision is made with respect to th" |
| `s 487.01921(4) the hearing of the application is commenced as required` | production-orders | 1 | 0 | "The hearing of the application must be commenced within 14 days after " |
| `s 487.01921(5) the justice or judge may revoke or vary the order` | production-orders | 0 | 1 | "may revoke or vary the order if they are satisfied that it is unreason" |
| `s 487.0193(1) the person, financial institution or entity may apply to revoke or vary the order` | production-orders | 0 | 1 | "Before they are required by an order made under any of sections 487.01" |
| `s 487.0193(2) the person, institution or entity may make the application` | production-orders | 1 | 0 | "The person, institution or entity may make the application only if the" |
| `s 487.0193(3) the person, institution or entity is required to prepare or produce the document` | production-orders | 1 | 1 | "is not required to prepare or produce the document until a final decis" |
| `s 487.0193(4) the justice or judge may revoke or vary the order` | production-orders | 0 | 1 | "may revoke or vary the order if satisfied that" |
| `s 487.0194(1) the person to whom a preservation demand is made must destroy it` | production-orders | 2 | 1 | "as soon as feasible after the demand expires or is revoked" |
| `s 487.0194(2) the person subject to a preservation order must destroy it` | production-orders | 2 | 1 | "as soon as feasible after the order expires or is revoked" |
| `s 487.0194(4) the person must destroy the computer data when the document is obtained under a warrant` | production-orders | 0 | 1 | "a person who preserved computer data under a preservation demand or or" |
| `s 487.0195(1) a preservation demand, preservation order, keep account open or active order or production order is necessary for the officer to ask` | production-orders | 1 | 1 | "no preservation demand, preservation order, keep account open or activ" |
| `s 487.0195(2) the person incurs criminal or civil liability for doing so` | production-orders | 1 | 1 | "does not incur any criminal or civil liability for doing so" |
| `s 487.0196 the person is excused from complying with the order` | production-orders | 1 | 1 | "No one is excused from complying with an order made under any of secti" |
| `s 487.0196 the document the individual was required to prepare may be used or received in evidence against them` | production-orders | 1 | 2 | "no document that an individual is required to prepare may be used or r" |
| `s 487.0197 the person is guilty of an offence punishable on summary conviction` | production-orders | 0 | 1 | "A person who contravenes a preservation demand made under section 487." |
| `s 487.0197 the fine is within the maximum` | production-orders | 1 | 0 | "liable to a fine of not more than $5,000" |
| `s 487.0198 the person, financial institution or entity is guilty of an offence punishable on summary conviction` | production-orders | 0 | 1 | "that contravenes an order made under any of sections 487.013 to 487.01" |
| `s 487.0198 the punishment is within the maximum` | production-orders | 1 | 0 | "liable to a fine of not more than $250,000 or to imprisonment for a te" |
| `s 487.0199 the person is guilty of an offence punishable on summary conviction` | production-orders | 0 | 1 | "A person who contravenes section 487.0194 without lawful excuse" |
| `s 487.02(1) the judge or justice may order the person to provide assistance` | production-orders | 0 | 1 | "may order a person to provide assistance, if the person’s assistance m" |
| `s 487.02(1) the assistance order has effect at the place` | production-orders | 0 | 1 | "The order has effect throughout Canada" |
| `s 487.02(2) the order to provide assistance may be issued by a means of telecommunication` | production-orders | 0 | 1 | "If the authorization is given or the warrant is issued by a means of t" |
| `s 486.4(1) the presiding judge or justice may make an order directing that information that could identify the victim or a witness not be published` | publication-bans | 0 | 1 | "in proceedings in respect of" |
| `s 486.4(2)(a) the presiding judge or justice must inform the person of the right to make an application for the order` | publication-bans | 0 | 1 | "In proceedings in respect of the offences referred to in paragraph (1)" |
| `s 486.4(2)(b) the presiding judge or justice must make the order` | publication-bans | 1 | 1 | "on application made by the victim, the prosecutor or any such witness," |
| `s 486.4(2)(c) the presiding judge or justice must inform the witnesses and the victim of the order's existence and of their right to apply to revoke or vary it` | publication-bans | 1 | 0 | "if an order is made, as soon as feasible, inform the witnesses and the" |
| `s 486.4(2.1) the presiding judge or justice may make an order directing that information that could identify the victim not be published` | publication-bans | 0 | 1 | "in proceedings in respect of an offence other than an offence referred" |
| `s 486.4(2.2)(a) the presiding judge or justice must inform the victim of their right to make an application for the order` | publication-bans | 0 | 1 | "In proceedings in respect of an offence other than an offence referred" |
| `s 486.4(2.2)(b) the presiding judge or justice must make the order` | publication-bans | 1 | 1 | "on application of the victim or the prosecutor, make the order" |
| `s 486.4(2.2)(c) the presiding judge or justice must inform the victim of the existence of the order and of their right to apply to revoke or vary it` | publication-bans | 1 | 0 | "if an order is made, as soon as feasible, inform the victim of the exi" |
| `s 486.4(3) the judge or justice must make an order directing that information that could identify the person not be published` | publication-bans | 0 | 2 | "In proceedings in respect of an offence under section 163.1" |
| `s 486.4(3.1)(a), (b) the presiding judge or justice must inquire` | publication-bans | 0 | 1 | "If the prosecutor makes an application for an order under paragraph (2" |
| `s 486.4(3.1)(c) the presiding judge or justice must advise the prosecutor of their duty under subsection (3.2)` | publication-bans | 0 | 1 | "If the prosecutor makes an application for an order under paragraph (2" |
| `s 486.4(3.2) the prosecutor must inform the judge or justice of what they have done` | publication-bans | 1 | 0 | "If the prosecutor makes the application, they shall, as soon as feasib" |
| `s 486.4(3.2) what the prosecutor informs the judge or justice of is complete` | publication-bans | 1 | 0 | "inform the judge or justice that they have (a) informed the witnesses " |
| `s 486.4(4) the order applies to the disclosure of information` | publication-bans | 1 | 1 | "An order made under this section does not apply in either of the follo" |
| `s 486.4(5) the order applies to the disclosure of information by the victim or witness` | publication-bans | 1 | 1 | "An order made under this section does not apply in respect of the disc" |
| `s 486.5(1) the judge or justice may make an order directing that information that could identify the victim or witness not be published` | publication-bans | 1 | 2 | "Unless an order is made under section 486.4" |
| `s 486.5(2.1) the offence is one of the offences for the purposes of subsection (2)` | publication-bans | 1 | 0 | "The offences for the purposes of subsection (2) are" |
| `s 486.5(2) the judge or justice may make an order directing that information that could identify the justice system participant not be published` | publication-bans | 0 | 3 | "in respect of a justice system participant who is involved in proceedi" |
| `s 486.5(3) the order applies to the disclosure of information` | publication-bans | 1 | 1 | "An order made under this section does not apply in either of the follo" |
| `s 486.5(3.1) the order applies to the disclosure of information by the victim, witness or justice system participant` | publication-bans | 1 | 1 | "An order made under this section does not apply in respect of the disc" |
| `s 486.5(4)(a) the applicant has applied as required` | publication-bans | 1 | 0 | "An applicant for an order shall (a) apply in writing to the presiding " |
| `s 486.5(4)(b) the applicant has provided notice of the application` | publication-bans | 1 | 0 | "provide notice of the application to the prosecutor, the accused and a" |
| `s 486.5(5) the applicant has set out the grounds` | publication-bans | 1 | 0 | "An applicant for an order shall set out the grounds on which the appli" |
| `s 486.5(5.1)(a), (b) the judge or justice must inquire` | publication-bans | 0 | 1 | "If the prosecutor makes an application for an order under subsection (" |
| `s 486.5(5.1)(c) the judge or justice must advise the prosecutor of their duty under subsection (8.2)` | publication-bans | 0 | 1 | "If the prosecutor makes an application for an order under subsection (" |
| `s 486.5(6) the judge or justice may hold a hearing, and the hearing may be in private` | publication-bans | 0 | 1 | "may hold a hearing to determine whether an order should be made" |
| `s 486.5(7) the judge or justice must consider the factor` | publication-bans | 1 | 1 | "any other factor that the judge or justice considers relevant" |
| `s 486.5(8) the order may be subject to the condition` | publication-bans | 0 | 1 | "any conditions that the judge or justice thinks fit" |
| `s 486.5(8.1) the judge or justice must inform the victims, witnesses and justice system participants of the order's existence and of their right to apply to revoke or vary it` | publication-bans | 1 | 0 | "If an order is made, the judge or justice shall, as soon as feasible, " |
| `s 486.5(8.2) the prosecutor must inform the judge or justice of what they have done` | publication-bans | 1 | 0 | "If the prosecutor makes the application, they shall, as soon as feasib" |
| `s 486.5(8.2) what the prosecutor informs the judge or justice of is complete` | publication-bans | 1 | 0 | "inform the judge or justice that they have (a) informed the victims, w" |
| `s 486.5(9) the person is prohibited from publishing, broadcasting or transmitting what would be published` | publication-bans | 1 | 1 | "Unless the judge or justice refuses to make an order, no person shall " |
| `s 486.51(1) the prosecutor must make an application to vary or revoke the order on the person's behalf` | publication-bans | 1 | 0 | "If a person who is the subject of an order made under section 486.4 or" |
| `s 486.51(2) the court must vary or revoke the order without holding a hearing` | publication-bans | 2 | 0 | "is made by the person who is the subject of the order or by any other " |
| `s 486.51(3) the court must hold a hearing to determine whether the order should be varied or revoked` | publication-bans | 1 | 0 | "If the court is of the opinion that varying or revoking the order that" |
| `s 486.51(4) the court must take into account whether it is possible to vary the order in a manner that protects the privacy interests of any other person` | publication-bans | 0 | 1 | "In order to determine whether the order should be varied" |
| `s 486.51(5) the applicant is required to provide notice of the application to vary or revoke the order to the accused` | publication-bans | 1 | 0 | "The applicant is not required to provide notice of the application to " |
| `s 486.51(6) the accused is permitted to make submissions in relation to the application` | publication-bans | 1 | 0 | "The accused shall not be permitted to make submissions in relation to " |
| `s 486.51(7) the prosecutor must notify the accused` | publication-bans | 1 | 0 | "If the order is varied or revoked, the prosecutor shall notify the acc" |
| `s 486.6(1) the person is guilty of an offence punishable on summary conviction` | publication-bans | 0 | 1 | "Every person who fails to comply with an order made under any of subse" |
| `s 486.6(1.1) the prosecutor is barred from commencing or continuing a prosecution against the person who is the subject of the order` | publication-bans | 1 | 1 | "unless, in the opinion of the prosecutor," |
| `s 486.6(2) the order applies to prohibit the publication of information that could identify a victim, witness or justice system participant in those proceedings` | publication-bans | 0 | 1 | "in relation to proceedings taken against any person who fails to compl" |
| `s 487(1) the justice may issue a warrant to search the building, receptacle or place` | search-warrants | 0 | 1 | "A justice who is satisfied by information on oath in Form 1 that there" |
| `s 487(1) the warrant may authorize the person` | search-warrants | 0 | 1 | "authorizing a peace officer or a public officer who has been appointed" |
| `s 487(1) the warrant may authorize the act` | search-warrants | 0 | 1 | "(d) to search the building, receptacle or place for any such thing and" |
| `s 487(2) the warrant may be executed at the place` | search-warrants | 0 | 1 | "may be executed at any place in Canada" |
| `s 487(2) the officer who executes the warrant has the authority required` | search-warrants | 1 | 1 | "must have authority to act in that capacity in the place where the war" |
| `s 487(2.1) the person may do the act` | search-warrants | 0 | 2 | "A person authorized under this section to search a computer system in " |
| `s 487(2.2) the person in possession or control must permit the person carrying out the search to do the act` | search-warrants | 1 | 2 | "on presentation of the warrant" |
| `s 487(3) the search warrant may be in the form set out as Form 5` | search-warrants | 0 | 1 | "may be in the form set out as Form 5 in Part XXVIII, varied to suit th" |
| `s 487.01(1) the judge may issue a warrant in writing authorizing a peace officer to use the device, technique or procedure or do the thing` | search-warrants | 0 | 2 | "A provincial court judge, a judge of a superior court of criminal juri" |
| `s 487.01(2) subsection (1) permits the act` | search-warrants | 1 | 0 | "Nothing in subsection (1) shall be construed as to permit interference" |
| `s 487.01(3) the warrant contains the terms and conditions required` | search-warrants | 1 | 1 | "shall contain such terms and conditions as the judge considers advisab" |
| `s 487.01(4) the warrant contains the privacy terms and conditions required` | search-warrants | 1 | 1 | "shall contain such terms and conditions as the judge considers advisab" |
| `s 487.01(5) the provision applies, with such modifications as the circumstances require, to the warrant` | search-warrants | 0 | 1 | "to a warrant referred to in subsection (4)" |
| `s 487.01(5.1) the warrant requires notice of the covert entry and search as required` | search-warrants | 1 | 1 | "shall require, as part of the terms and conditions referred to in subs" |
| `s 487.01(5.2) the judge may grant an extension of the period for giving notice` | search-warrants | 2 | 0 | "Where the judge who issues a warrant under subsection (1) or any other" |
| `s 487.01(6) the general warrant may be executed at the place` | search-warrants | 0 | 1 | "may be executed at any place in Canada" |
| `s 487.01(6) the peace officer who executes the general warrant has the authority required` | search-warrants | 1 | 1 | "must have authority to act as a peace officer in the place where it is" |

(239 functions.)

## Seams (ccc16)

**Inputs this part takes from other sections (PLAN.md section 4 and section 6, row ccc16):**

- `s 342.1(2) computer data and computer system` (MAYBE BOOLEAN, answered by ccc12): taken by s 487.011 for "computer data" and "computer system".
- Section 2 terms, each a MAYBE BOOLEAN input where a rule turns on it: `s 2 criminal organization`, `s 2 criminal organization offence`, `s 2 intimate partner`, `s 2 justice system participant`, `s 2 offence-related property`, `s 2 public officer`, `s 2 serious offence`, `s 2 terrorism offence`, `s 2 victim`.
- `s 552 judge` (MAYBE BOOLEAN): s 487.01(1) "a judge as defined in section 552".
- `s 489.1` and `s 490` (ccc17) are named only as provisions (s 487.0192(4)); no answer is taken.
- Terms borrowed from other Acts are asked as facts: "adult" and "provincial court judge ... young person" (Youth Criminal Justice Act, in s 487.04), the Identification of Criminals Act (s 485.2), the Canada Evidence Act (s 487.0192(6)).

**What other parts ask of this one:** ss 487.051 to 487.0911 (ccc17) ask for `s 487.04 the offence is a primary designated offence`, `... a secondary designated offence` and `... a designated offence` (MAYBE BOOLEAN). The names agree with the plan; the argument is the record `s 487.04 facts of the offence` (the section and subsection of the offence as a core `Provision of the Code`, where that provision is found, how the person is charged, the purpose, whether it may be and is prosecuted by indictment, the maximum imprisonment, and the intent of an assault under s 246(1)). A seam the plan lacks: the instrument and vintage of the provision (F14), which the plan's R1 convention does not carry.

## Findings: what the text turns out to say (ccc16)

1. **Primary designated offence, paragraph (d), stops at (c.03).** Line 9423: "(d) an attempt to commit or, other than for the purposes of subsection 487.05(1), a conspiracy to commit an offence referred to in any of paragraphs (a) to (c.03)". Paragraph (c.1), the Foreign Interference and Security of Information Act offences, is outside that range, so an attempt or a conspiracy to commit such an offence is not a primary designated offence under (d). Encoded as written (F16).
2. **Secondary designated offence, paragraph (e)(i), names (a) or (b).** Lines 9539-9540: "(e) an attempt to commit or ... a conspiracy to commit (i) an offence referred to in paragraph (a) or (b) — which, for section 487.051 to apply, is prosecuted by indictment". Paragraph (a.1), the Cannabis Act offences, is not named, so an attempt or a conspiracy to commit one is outside (e)(i). Encoded as written (F16).
3. **Section numbers are decimals.** "sections 487.012 to 487.0199" takes in 487.0131, 487.0194 and 487.0199 but not 487.02; "sections 487.05 to 487.0911" takes in 487.051 and 487.0911 but not 487.1. Ranges are tests on the decimal.
4. **Among ss 486 to 486.31 and 486.7, the accused is named as an applicant only in s 486(3).** In ss 486.1 to 486.3 and 486.31 the applicants are the prosecutor and the witness; in s 486(1) and s 486.7(1) the judge or justice may also act on their own motion. The accused has no application of their own in the others: an accused's application answers NOTHING for a power and JUST FALSE for a duty whose trigger is the named applicant's application (F8).
5. **Paragraphs (a), (a.1) and (b) of "secondary designated offence" carry a condition (indictable, five years or more) that paragraph (c)'s list does not.** An offence listed in (c) is secondary by listing, whatever its mode of prosecution or maximum: summary-only provisions of this Act can be secondary designated offences. A finding of the test file, not of the encoding: the first run of `ccc16-tests-dna-rows.l4` showed nine failures, all in the generated fixtures for (a.1) and (b), which did not meet the paragraphs' own indictment and five-year conditions; the fixtures were corrected, no expected value was changed, and a not-indictable control was added for each paragraph.
6. **s 487.021 is a parliamentary review** ("Within seven years after the coming into force of this section, a comprehensive review ... shall be undertaken"): machinery that affects no one now, so inert (reason 2); s 487.03 and the repealed rows of the lists are shown repealed in this text (13 rows).

## What the stable binary does not accept (ccc16)

Each of these was met on 1.6.110 while writing this part; the binary governs.

- A section-level `GIVEN` that several rules share: not allowed on this build; each rule has its own `GIVEN`.
- A list literal whose rows are not each parenthesised and indented on continuation lines: a parse error. Rows are written `(Record OF a, b)`, one per line, each in its own parentheses (a leading comma before the parenthesis is accepted).
- Inline record construction inside an `#ASSERT` line (`Record OF ...` with `WITH`): rejected; the tests use named fixtures (functions that build the record) instead.
- `length` of a list is ambiguous with the prelude's: `count` is used.
- `NOT a AND b` parses as `NOT (a AND b)`: every `NOT` is parenthesised (a misread of this cost one test in s 487.04, caught by the assertion at the 1970 Code s 246(1) intent).
- A continuation line inside an `#ASSERT` is rejected: each is one line. `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (outside `LEST BREACH ... BECAUSE`) are not available: "not covered" is `NOTHING` or a constructor, asserted.
- No regulative construct was rejected: regulative rules (`PARTY ... MUST/MAY ... WITHIN ... HENCE ... LEST BREACH BY ... BECAUSE`) are accepted and run with `#TRACE`: `s 487.01921(4) the hearing must be commenced` and `s 487.0193(2) the notice may be given`. Their outcomes were identical on 1.6.110 and 1.6.109 (see below), and the same duties are also decision functions over the facts.

## Seat layer (ccc16)

79 questions in 6 groups, each with `@export` and `@desc` on every input, each beginning "Under section N,"; 241 cases. The seat calls layer-1 rules and restates none; where the text hands the person a phrase to pick (who applies, which order is sought, where the provision is found), a helper turns the phrase into the layer-1 constructor and an unrecognised phrase becomes the "another ..." constructor, which the layer-1 rule answers NOTHING.

**Procedural irregularities and the summons for the Identification of Criminals Act (ss 483 to 485.2)**

1. Under section 483, may a judge or provincial court judge alone do what two or more justices are authorized to do
2. Under section 485(1), is jurisdiction over the offence lost because a court failed to act at a particular time or an adjournment or remand rule was not followed
3. Under section 485(1.1), is jurisdiction over me lost because I did not appear personally or in person
4. Under section 485(2), may a summons be issued against me on the day proposed  *(retitled in the second pass)*
5. Under section 485(2), may a warrant for my arrest be issued on the day proposed  *(retitled in the second pass)*
6. Under section 485(3), are the proceedings against me deemed to be dismissed for want of prosecution
7. Under section 485.1, is a new information or a new indictment in respect of the same transaction barred  *(retitled in the second pass)*
8. Under section 485.2(1), may a justice or judge summon me to appear for the purposes of the Identification of Criminals Act
9. Under section 485.2(7), does the summons I was given have the contents the section requires
10. Under section 485.2(8), was the summons served on me as the section requires
**Open court, support persons, testimony and cross-examination (ss 486 to 486.3)**

11. Under section 486(1), must the proceedings against me be held in open court
12. Under section 486(1), may the judge or justice exclude the public from my trial or order a witness to testify behind a screen
13. Under section 486(3), must the judge or justice state the reason for not making an exclusion order on the application made  *(retitled in the second pass)*
14. Under section 486(4), may an adverse inference be drawn against me from the fact that an order is, or is not, made
15. Under section 486.1(1), must the court allow a support person or support animal for a witness against me who is under 18 or has a disability
16. Under section 486.1(1.1), must the court allow a support person or support animal for a witness who is the victim of a listed offence
17. Under section 486.1(4), is the judge or justice barred from permitting a witness to be a support person
18. Under section 486.1(6), may an adverse inference be drawn against me from the fact that a support person or animal order is, or is not, made
19. Under section 486.2(1), must the court order that a witness against me testify outside the court room or behind a screen so that the witness does not see me
20. Under section 486.2(5), is a witness barred from testifying outside the court room unless I can watch by closed-circuit television or videoconference and can communicate with my counsel
21. Under section 486.2(6), may an adverse inference be drawn against me from the fact that a testimony order is, or is not, made
22. Under section 486.3(1), must the court order that I not personally cross-examine a witness who is under 18
23. Under section 486.3(2), must the court order that I not personally cross-examine a witness who is the victim of a listed offence
24. Under section 486.3(3), may the court order that I not personally cross-examine a witness who is not entitled to apply under subsection (1) or (2)
25. Under section 486.3(5), may an adverse inference be drawn against me from the fact that counsel is, or is not, appointed
26. Under section 486.31(1), may the judge or justice order that information that could identify a witness not be disclosed in my proceedings
27. Under section 486.31(4), may an adverse inference be drawn against me from the fact that a non-disclosure order is, or is not, made
28. Under section 486.7(1), may the presiding judge or justice make an order to protect the security of a witness in my case
29. Under section 486.7(4), may an adverse inference be drawn against me from the fact that a witness security order is, or is not, made
30. Under section 486.71, is the judge or justice prohibited from making more than one order regarding the same witness
**Orders restricting publication of the identity of a victim or witness (ss 486.4 to 486.6)**

31. Under section 486.4(1), may the court ban publication of information that could identify the victim or a witness in my case
32. Under section 486.4(2), must the presiding judge or justice make a publication ban order on the application made  *(retitled in the second pass)*
33. Under section 486.4(4), does a publication ban order made under section 486.4 apply to the disclosure I make
34. Under section 486.5(1), may a judge or justice make a publication ban order for a victim or witness in my case
35. Under section 486.5(4)(b), did the applicant provide notice of the application for a publication ban to the prosecutor, to me and to any other person affected
36. Under section 486.5(9), am I prohibited from publishing, broadcasting or transmitting what the section covers
37. Under section 486.51(5), is the applicant required to give me notice of an application to vary or revoke a publication ban
38. Under section 486.51(6), am I permitted to make submissions on an application to vary or revoke a publication ban
39. Under section 486.51(7), is the prosecutor now required to notify me of a change to a publication ban order  *(retitled in the second pass)*
40. Under section 486.6(1), am I guilty of an offence punishable on summary conviction if I fail to comply with a publication ban order
41. Under section 486.6(1.1), is the prosecutor barred from prosecuting me for failing to comply with an order that protects me
**Search warrants and general warrants (ss 487 and 487.01)**

42. Under section 487(1), may a justice issue a warrant to search the building, receptacle or place
43. Under section 487(2.2), must I permit the person carrying out the search to use a computer system, obtain a hard copy of the data and copy it
44. Under section 487.01(1), may a judge issue a general warrant authorizing a peace officer to use a technique that would otherwise be an unreasonable search or seizure
45. Under section 487.01(2), does the general warrant provision permit interference with my bodily integrity
46. Under section 487.01(5.1), does the general warrant I was given for a covert entry require notice of the entry and search within the time the judge considers reasonable  *(retitled in the second pass)*
**Preservation demands and orders, production orders, and what follows (ss 487.011 to 487.02)**

47. Under section 487.012(2), may a peace officer or public officer make a preservation demand to me
48. Under section 487.012(3), is a preservation demand barred against me because I am under investigation for the offence
49. Under section 487.012(4), is the preservation demand made to me still in effect on a given day
50. Under section 487.012(6), is another demand to preserve the same computer data in connection with the investigation barred
51. Under section 487.013(5), is a preservation order barred against me because I am under investigation for the offence
52. Under section 487.0131(1), must I keep the account open or active that the order names
53. Under section 487.0131(5), is a keep-account-open order barred against me because I am under investigation for the offence
54. Under section 487.014(1), may a justice or judge order me to produce a document or to prepare and produce a document
55. Under section 487.014(4), is a general production order barred against me because I am under investigation for the offence
56. Under section 487.0141(6)(a), may I be required to produce documents again less than 72 hours after the last time
57. Under section 487.0141(7), is a production order for specified dates barred against me because I am under investigation for the offence
58. Under section 487.015(5), is an order to trace a specified communication barred against me because I am under investigation for the offence
59. Under section 487.016(4), is a production order for transmission data barred against me because I am under investigation for the offence
60. Under section 487.017(4), is a production order for tracking data barred against me because I am under investigation for the offence
61. Under section 487.018(5), is a production order for financial data barred against me because I am under investigation for the offence
62. Under section 487.0191(1), may a justice or judge order me not to disclose the existence or contents of a preservation demand or order
63. Under section 487.0192(5), is a copy of a document produced under a general production order or a production order for specified dates admissible in evidence against me on proof by affidavit that it is a true copy  *(retitled in the second pass)*
64. Under section 487.01921(2), may I make the application to revoke or vary a keep-account-open order
65. Under section 487.0193(2), may I make the application to revoke or vary a production order
66. Under section 487.0193(3), am I required to prepare or produce the document while my application to revoke or vary the production order is undecided
67. Under section 487.0195(2), do I incur criminal or civil liability for voluntarily preserving data, keeping an account open or providing a document at an officer's request
68. Under section 487.0196, am I excused from complying with a production order because the document may incriminate me
69. Under section 487.0196, may a document I was required to prepare be used or received in evidence against me in a later criminal proceeding
70. Under section 487.0197, am I guilty of an offence punishable on summary conviction if I contravene a preservation demand without lawful excuse
71. Under section 487.0197, what is the most I can be fined
72. Under section 487.0198, am I guilty of an offence punishable on summary conviction if I contravene a preservation or production order without lawful excuse
73. Under section 487.0198, what is the most I can be fined
74. Under section 487.0198, what is the longest term of imprisonment I can be sentenced to
75. Under section 487.0199, am I guilty of an offence punishable on summary conviction if I contravene section 487.0194 without lawful excuse
76. Under section 487.02(1), may a judge or justice order me to provide assistance to give effect to a warrant or authorization
**DNA analysis: is the offence a designated offence (s 487.04)**

77. Under section 487.04, is the offence a primary designated offence
78. Under section 487.04, is the offence a secondary designated offence
79. Under section 487.04, is the offence a designated offence

### Seat-question audit (first direction audit and second pass, 2026-11-12)

Every one of the 79 seat questions was read against the BODY of the layer-1 function it calls (`work/audit_dump.py`), not against its title: **79 read, 8 retitled, 71 read and left.** The first direction audit (a permission title over a bar, or the reverse) found no such mismatch: the six adverse-inference questions and the "permitted to make submissions" question are permission titles over functions whose answer is the text's flat negative, and read "no, may not" as JUST FALSE; every bar is titled as a bar. The second pass found 8 subject or scope mismatches: six of one shape, a name that carried, as a given, a status the function tests and answers JUST FALSE outside (the three months, the dismissal, the applicant, the variation), so that a "no" would be misread; and two of limb or scope (a general question over a specific body, and a name broader than the route the body answers). A question whose function answers NOTHING outside the stated status was left: "not covered" misreads nothing.

**Retitled** (eight names; in addition the `@export` text of question 6 (s 485(3)) was changed without a change of name, because it carried the three months as a given). The question, its `@export` and the cases that name it were regenerated; each affected assertion carries `-- RECONCILED 2026-11-12: question retitled (was ...); the answer is unchanged`, and no expected value changed:

- 4. `Under section 485(2), may a summons be issued against me on the day proposed`: the name carried "within three months after jurisdiction over me was lost" as a given; the function tests the dates and answers JUST FALSE outside them, so "no" would read "not even within three months". Now asks "on the day proposed" (the section gives the power only where jurisdiction was lost, which the function tests).
- 5. `Under section 485(2), may a warrant for my arrest be issued on the day proposed`: same as the summons question: the period and the loss of jurisdiction were givens in the name; the function tests the dates (and the public-interest consideration, NOTHING). Now asks "on the day proposed".
- 7. `Under section 485.1, is a new information or a new indictment in respect of the same transaction barred`: "after dismissal for want of prosecution" was a given in the name; the function tests the dismissal and answers JUST FALSE where there is none, which would read "not barred even after a dismissal".
- 13. `Under section 486(3), must the judge or justice state the reason for not making an exclusion order on the application made`: "when the prosecutor or I apply" was a given in the name; the function tests who applies and answers JUST FALSE for another applicant.
- 32. `Under section 486.4(2), must the presiding judge or justice make a publication ban order on the application made`: "when the victim, the prosecutor or a witness under 18 applies" was a given in the name; the function tests who applies and answers JUST FALSE for another applicant.
- 39. `Under section 486.51(7), is the prosecutor now required to notify me of a change to a publication ban order`: "if a publication ban order is varied or revoked" was a given in the name; the function tests it and answers JUST FALSE where it has not been. Now asks whether the prosecutor is now required to notify (the export no longer repeats the trigger).
- 46. `Under section 487.01(5.1), does the general warrant I was given for a covert entry require notice of the entry and search within the time the judge considers reasonable`: limb: the name asked the general rule ("does a general warrant for a covert entry require notice") while the function answers whether the warrant in hand has the required term.
- 63. `Under section 487.0192(5), is a copy of a document produced under a general production order or a production order for specified dates admissible in evidence against me on proof by affidavit that it is a true copy`: scope: the name said "a production order"; the function answers for a copy of a document produced under ss 487.014 or 487.0141 only (the export text already said so).

**Read, left** (one line of reason each):

- 1. `Under section 483, may a judge or provincial court judge alone do what two or more justices are authorized to do`: the name restates the function's own name; the added words are the text's own
- 2. `Under section 485(1), is jurisdiction over the offence lost because a court failed to act at a particular time or an adjournment or remand rule was not followed`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 3. `Under section 485(1.1), is jurisdiction over me lost because I did not appear personally or in person`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 6. `Under section 485(3), are the proceedings against me deemed to be dismissed for want of prosecution`: the name has no premise; the export text carried "because no summons or warrant was issued within the three months" as a given, which the function tests (JUST FALSE where one was issued), so the export was changed to ask as of the day I am asking; the name is left
- 8. `Under section 485.2(1), may a justice or judge summon me to appear for the purposes of the Identification of Criminals Act`: the name restates the function's own name; the added words are the text's own
- 9. `Under section 485.2(7), does the summons I was given have the contents the section requires`: the name restates the function's own name; the added words are the text's own
- 10. `Under section 485.2(8), was the summons served on me as the section requires`: the name restates the function's own name; the added words are the text's own
- 11. `Under section 486(1), must the proceedings against me be held in open court`: "must" over a function named "are held": the text says "shall be held" and the function answers TRUE when no order excludes the public, NOTHING otherwise; kept, flagged
- 12. `Under section 486(1), may the judge or justice exclude the public from my trial or order a witness to testify behind a screen`: the name restates the function's own name; the added words are the text's own
- 14. `Under section 486(4), may an adverse inference be drawn against me from the fact that an order is, or is not, made`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 15. `Under section 486.1(1), must the court allow a support person or support animal for a witness against me who is under 18 or has a disability`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 16. `Under section 486.1(1.1), must the court allow a support person or support animal for a witness who is the victim of a listed offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 17. `Under section 486.1(4), is the judge or justice barred from permitting a witness to be a support person`: a bar titled as a bar: JUST TRUE means the bar applies (direction checked)
- 18. `Under section 486.1(6), may an adverse inference be drawn against me from the fact that a support person or animal order is, or is not, made`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 19. `Under section 486.2(1), must the court order that a witness against me testify outside the court room or behind a screen so that the witness does not see me`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 20. `Under section 486.2(5), is a witness barred from testifying outside the court room unless I can watch by closed-circuit television or videoconference and can communicate with my counsel`: a bar with its own "unless" in the name; JUST TRUE means barred, JUST FALSE means the arrangements are made (direction checked)
- 21. `Under section 486.2(6), may an adverse inference be drawn against me from the fact that a testimony order is, or is not, made`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 22. `Under section 486.3(1), must the court order that I not personally cross-examine a witness who is under 18`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 23. `Under section 486.3(2), must the court order that I not personally cross-examine a witness who is the victim of a listed offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 24. `Under section 486.3(3), may the court order that I not personally cross-examine a witness who is not entitled to apply under subsection (1) or (2)`: the name restates the function's own name; the added words are the text's own
- 25. `Under section 486.3(5), may an adverse inference be drawn against me from the fact that counsel is, or is not, appointed`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 26. `Under section 486.31(1), may the judge or justice order that information that could identify a witness not be disclosed in my proceedings`: the name restates the function's own name; the added words are the text's own
- 27. `Under section 486.31(4), may an adverse inference be drawn against me from the fact that a non-disclosure order is, or is not, made`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 28. `Under section 486.7(1), may the presiding judge or justice make an order to protect the security of a witness in my case`: the name restates the function's own name; the added words are the text's own
- 29. `Under section 486.7(4), may an adverse inference be drawn against me from the fact that a witness security order is, or is not, made`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 30. `Under section 486.71, is the judge or justice prohibited from making more than one order regarding the same witness`: a bar titled as a bar: JUST TRUE means the bar applies (direction checked)
- 31. `Under section 486.4(1), may the court ban publication of information that could identify the victim or a witness in my case`: the name restates the function's own name; the added words are the text's own
- 33. `Under section 486.4(4), does a publication ban order made under section 486.4 apply to the disclosure I make`: the name restates the function's own name ("the order applies"); the function answers only JUST FALSE (an exception is met) or NOTHING; read as "does it apply: no"
- 34. `Under section 486.5(1), may a judge or justice make a publication ban order for a victim or witness in my case`: the name restates the function's own name; the added words are the text's own
- 35. `Under section 486.5(4)(b), did the applicant provide notice of the application for a publication ban to the prosecutor, to me and to any other person affected`: the name restates the function's own name; the added words are the text's own
- 36. `Under section 486.5(9), am I prohibited from publishing, broadcasting or transmitting what the section covers`: a bar titled as a bar: JUST TRUE means the bar applies (direction checked)
- 37. `Under section 486.51(5), is the applicant required to give me notice of an application to vary or revoke a publication ban`: the text says "is not required to provide notice"; JUST FALSE reads "not required"
- 38. `Under section 486.51(6), am I permitted to make submissions on an application to vary or revoke a publication ban`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 40. `Under section 486.6(1), am I guilty of an offence punishable on summary conviction if I fail to comply with a publication ban order`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 41. `Under section 486.6(1.1), is the prosecutor barred from prosecuting me for failing to comply with an order that protects me`: a bar titled as a bar: JUST TRUE means the bar applies (direction checked)
- 42. `Under section 487(1), may a justice issue a warrant to search the building, receptacle or place`: the name restates the function's own name; the added words are the text's own
- 43. `Under section 487(2.2), must I permit the person carrying out the search to use a computer system, obtain a hard copy of the data and copy it`: a duty titled "must"; the text says "shall"; JUST FALSE reads "not required" (direction checked)
- 44. `Under section 487.01(1), may a judge issue a general warrant authorizing a peace officer to use a technique that would otherwise be an unreasonable search or seizure`: the name restates the function's own name; the added words are the text's own
- 45. `Under section 487.01(2), does the general warrant provision permit interference with my bodily integrity`: the name restates the function's own name ("subsection (1) permits the act"); the act is an input; JUST FALSE reads "does not permit"
- 47. `Under section 487.012(2), may a peace officer or public officer make a preservation demand to me`: the name restates the function's own name; the added words are the text's own
- 48. `Under section 487.012(3), is a preservation demand barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 49. `Under section 487.012(4), is the preservation demand made to me still in effect on a given day`: the name restates the function's own name; the added words are the text's own
- 50. `Under section 487.012(6), is another demand to preserve the same computer data in connection with the investigation barred`: a bar titled as a bar: JUST TRUE means the bar applies (direction checked)
- 51. `Under section 487.013(5), is a preservation order barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 52. `Under section 487.0131(1), must I keep the account open or active that the order names`: a duty titled "must"; the text says "shall"; JUST FALSE reads "not required" (direction checked)
- 53. `Under section 487.0131(5), is a keep-account-open order barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 54. `Under section 487.014(1), may a justice or judge order me to produce a document or to prepare and produce a document`: the name restates the function's own name; the added words are the text's own
- 55. `Under section 487.014(4), is a general production order barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 56. `Under section 487.0141(6)(a), may I be required to produce documents again less than 72 hours after the last time`: the name adds "less than 72 hours", which the function tests as an input and answers JUST FALSE for; outside it the function answers NOTHING, so no "no" is misread
- 57. `Under section 487.0141(7), is a production order for specified dates barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 58. `Under section 487.015(5), is an order to trace a specified communication barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 59. `Under section 487.016(4), is a production order for transmission data barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 60. `Under section 487.017(4), is a production order for tracking data barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 61. `Under section 487.018(5), is a production order for financial data barred against me because I am under investigation for the offence`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 62. `Under section 487.0191(1), may a justice or judge order me not to disclose the existence or contents of a preservation demand or order`: the name restates the function's own name; the added words are the text's own
- 64. `Under section 487.01921(2), may I make the application to revoke or vary a keep-account-open order`: the name restates the function's own name; the added words are the text's own
- 65. `Under section 487.0193(2), may I make the application to revoke or vary a production order`: the name restates the function's own name; the added words are the text's own
- 66. `Under section 487.0193(3), am I required to prepare or produce the document while my application to revoke or vary the production order is undecided`: the name restates the function's own name; JUST FALSE reads "not required" while the application is undecided (an "until" bar)
- 67. `Under section 487.0195(2), do I incur criminal or civil liability for voluntarily preserving data, keeping an account open or providing a document at an officer's request`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 68. `Under section 487.0196, am I excused from complying with a production order because the document may incriminate me`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 69. `Under section 487.0196, may a document I was required to prepare be used or received in evidence against me in a later criminal proceeding`: a permission title over a flat negative ("No adverse inference may be drawn", "shall not be permitted"): JUST FALSE reads as "no, may not", the text's own words; direction checked
- 70. `Under section 487.0197, am I guilty of an offence punishable on summary conviction if I contravene a preservation demand without lawful excuse`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 71. `Under section 487.0197, what is the most I can be fined`: type: a number, as the name asks ("what is the most")
- 72. `Under section 487.0198, am I guilty of an offence punishable on summary conviction if I contravene a preservation or production order without lawful excuse`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 73. `Under section 487.0198, what is the most I can be fined`: type: a number, as the name asks
- 74. `Under section 487.0198, what is the longest term of imprisonment I can be sentenced to`: type: a phrase of years, as the name asks
- 75. `Under section 487.0199, am I guilty of an offence punishable on summary conviction if I contravene section 487.0194 without lawful excuse`: the name adds a status the function tests as an input; outside it the function answers NOTHING, so no "no" can be misread
- 76. `Under section 487.02(1), may a judge or justice order me to provide assistance to give effect to a warrant or authorization`: the name restates the function's own name; the added words are the text's own
- 77. `Under section 487.04, is the offence a primary designated offence`: the name restates the function's own name; the added words are the text's own
- 78. `Under section 487.04, is the offence a secondary designated offence`: the name restates the function's own name; the added words are the text's own
- 79. `Under section 487.04, is the offence a designated offence`: the name restates the function's own name; the added words are the text's own

## What check.sh prints (ccc16)

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc16-cases-seat.l4                            0       241       0        0         0 |      0       241       0        0  same
ccc16-dna-definitions.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc16-officials.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc16-open-court.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc16-preservation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc16-production-orders.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc16-publication-bans.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc16-search-warrants.l4                       0         0       0        0         0 |      0         0       0        0  same
ccc16-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc16-tests-dna-definitions.l4                 0       156       0        0         0 |      0       156       0        0  same
ccc16-tests-dna-rows.l4                        0       247       0        0         0 |      0       247       0        0  same
ccc16-tests-officials.l4                       0        77       0        0         0 |      0        77       0        0  same
ccc16-tests-open-court.l4                      0       236       0        0         0 |      0       236       0        0  same
ccc16-tests-preservation.l4                    0       111       0        0         0 |      0       111       0        0  same
ccc16-tests-production-orders.l4               0       272       0        0         0 |      0       272       0        0  same
ccc16-tests-publication-bans.l4                0       185       0        0         0 |      0       185       0        0  same
ccc16-tests-search-warrants.l4                 0        86       0        0         0 |      0        86       0        0  same
TOTAL (20 modules)                             0      1611       0        0           |      0      1611       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**The #TRACE comparison.** `ccc16-tests-production-orders.l4` holds four `#TRACE` directives (`s 487.01921(4) the hearing must be commenced` and `s 487.0193(2) the notice may be given`, each twice). Run on 1.6.110 and 1.6.109 with `JL4_LIBRARY_PATH` unset on both sides, each build printed 4,700 lines of output with 276 evaluations (272 assertions and the four traces), and the outputs are identical line for line apart from the file and range lines: three `FULFILLED` and one `BREACH` on each. (Both runs were checked to have produced evaluations before they were compared.) `check.sh` itself does not see a TRACE outcome.

The baseline on resume (before any edit this session) was 20 modules, 1600 satisfied, 9 failed, all nine in `ccc16-tests-dna-rows.l4`; the earlier baseline before the seat layer and the rows test was 17 modules, 1123 satisfied, 0 failed.

