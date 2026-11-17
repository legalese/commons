# ccc25: Part XXII.1 Remediation Agreements and Part XXII.2 Alternative Measures and Restorative Justice Processes
Criminal Code (Canada), R.S.C. 1985, c. C-46, sections 715.3 to 715.6, lines 14872-15170 of the plain-text rendering of the Justice Laws Website consolidation (current to 2026-09-30).
Run `dst-ccc25`, part agent `ccc25`, written by Claude Sonnet 5.5 (one run, resumed twice after weekly-limit stops; the first pass and the two follow-up tasks of 2026-11-12 are all in it).
Status, verified by running the commands under "What check.sh prints (ccc25)" after the last edit of any `.l4` file: 8 modules, 626 assertions satisfied and none failed, refused or in error on both stable builds; 68 `#TRACE` outcomes equal to their hand-written expectations on both builds; 0 srcrefs problems in both modes; 0 lint problems; 0 warnings.
Nothing here is verified against the official text: the source is a converter's rendering, not the official consolidation, and the French equivalents in parentheses after a defined term are not encoded.
The lead's task message calls the range "miscarriages of justice and compensation"; the text of the range holds Part XXII.1 (Remediation Agreements) and Part XXII.2 (Alternative Measures and Restorative Justice Processes), and that is what is encoded (finding 1).

Files, all under `deposit/encodings/legalese-sonnet-5.5/`:

| file | what it is |
| --- | --- |
| `ccc25-remediation-negotiation.l4` | layer 1, ss 715.3 to 715.35: definitions, acting for a victim, purpose, conditions for negotiating, the notice, the contents of the agreement, the independent monitor |
| `ccc25-remediation-approval.l4` | layer 1, ss 715.36 to 715.43: informing victims, approval, the stay, variation, termination, completion, the deadline, publication, deletion of an offence |
| `ccc25-alternative-measures.l4` | layer 1, ss 715.44 to 715.6: Part XXII.2 definitions, principles, warnings and referrals, alternative measures, restorative justice, conferences, records |
| `ccc25-tests-remediation-negotiation.l4`, `ccc25-tests-remediation-approval.l4`, `ccc25-tests-alternative-measures.l4` | tests of the three modules: 479 assertions and 68 `#TRACE`s, expectations written by hand from the text |
| `ccc25-seat.l4` | layer 2: 54 questions for a person accused of an offence |
| `ccc25-cases-seat.l4` | 147 assertions over the 54 questions; every question has at least one case |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file, the working log, and the types and constructors the core lacks |

The scripts that built and checked these files (`build.py`, the test generators, `lint.py`, `traces.py`, `coverage.py`, `build_notes.py`) are in `work/`, which is not shipped.

## Coverage (ccc25)
One row per non-blank line of lines 14872-15169 (line 15170 is blank), each with exactly one disposition: `encoded`, `inert` (reason 1: not operative; reason 2: machinery), `fork` (the reading is in the fork register and the function named encodes the chosen reading), or `repealed or blank in this text` (none in this range).
There is no `out-of-scope` or `deferred` row.
The last column counts the `#ASSERT`s in the three layer-1 tests files that name the function; a row that names two functions adds their counts, and a regulative rule is run by `#TRACE` (68 in all) and is listed beside its decision function.
non-blank lines in 14872-15169: 287; rows: 287; dispositions: {'inert (reason 1)': 100, 'encoded': 93, 'fork': 86, 'inert (reason 2)': 8}; layer-1 #ASSERTs: 479; #TRACEs: 68.
Audit counts: 287 non-blank lines counted independently with `awk` in 14872-15169; 287 rows; no line is in no row and none is in two (`work/coverage.py` checks both).
The table was built one row per line, so the count of rows before and after the audit is the same, 287 and 287, and no row had to be added.
Every `encoded` and `fork` row names a function that at least one assertion names.
Inert rows with reason 1 are the Part titles, the headings, the two lead-ins "The following definitions apply in this Part", and the two purpose clauses (ss 715.31 and 715.45); with reason 2, the regulation-making power (s 715.43(1)) and the power to amend the schedule (s 715.43(2)).
The purpose and power rows keep their words as quotations in constants (`s 715.31 ...`, `s 715.45 ...`, `s 715.43(1) and (2) ...`) so that a reader holding the source beside the module sees nothing skipped; those constants are not rules.

| line | unit (opening words) | disposition | L4 names | forks | #ASSERTs naming it |
| ---: | --- | --- | --- | --- | ---: |
| 14872 | PART XXII.1 Remediation Agreements | inert (reason 1) | the Part's title and its first heading |  | 0 |
| 14873 | Definitions | inert (reason 1) | the Part's title and its first heading |  | 0 |
| 14874 | 715.3 (1) The following definitions apply in this Part. | inert (reason 1) | lead-in: it sets the scope of the five definitions below and states no rule of its own |  | 0 |
| 14875 | court means a superior court of criminal jurisdiction but do... | encoded | `s 715.3(1) court` |  | 5 |
| 14876 | offence means any offence listed in the schedule to this Par... | encoded | `s 715.3(1) offence` |  | 3 |
| 14877 | organization has the same meaning as in section 2 but does n... | encoded | `s 715.3(1) organization` |  | 7 |
| 14878 | remediation agreement means an agreement, between an organiz... | fork | `s 715.3(1) remediation agreement` | F22 | 11 |
| 14879 | victim has the same meaning as in section 2 but, with respec... | fork | `s 715.3(1) victim` | F23 | 6 |
| 14880 | Acting on victim’s behalf | inert (reason 1) | heading |  | 0 |
| 14881 | (2) For the purposes of this Part, a third party not referre... | fork | `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf` | F1, F2.1; listed: F10.2 ("when authorized") | 6 |
| 14882 | Purpose | inert (reason 1) | heading |  | 0 |
| 14883 | 715.31 The purpose of this Part is to establish a remediatio... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14884 | (a) to denounce an organization’s wrongdoing and the harm th... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14885 | (b) to hold the organization accountable for its wrongdoing ... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14886 | (c) to contribute to respect for the law by imposing an obli... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14887 | (d) to encourage voluntary disclosure of the wrongdoing; | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14888 | (e) to provide reparations for harm done to victims or to th... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14889 | (f) to reduce the negative consequences of the wrongdoing fo... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.31 the purpose of this Part as the text states it` |  | 0 |
| 14890 | Conditions for remediation agreement | inert (reason 1) | heading |  | 0 |
| 14891 | 715.32 (1) The prosecutor may enter into negotiations for a ... | fork | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`; rules: `s 715.32(1) the prosecutor's permission to enter into negotiations` | F2.2 | 11 |
| 14892 | (a) the prosecutor is of the opinion that there is a reasona... | fork | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`; rules: `s 715.32(1) the prosecutor's permission to enter into negotiations` | F2.2 | 11 |
| 14893 | (b) the prosecutor is of the opinion that the act or omissio... | fork | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`; rules: `s 715.32(1) the prosecutor's permission to enter into negotiations` | F2.2 | 11 |
| 14894 | (c) the prosecutor is of the opinion that negotiating the ag... | fork | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`; rules: `s 715.32(1) the prosecutor's permission to enter into negotiations` | F2.2 | 11 |
| 14895 | (d) the Attorney General has consented to the negotiation of... | fork | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`; rules: `s 715.32(1) the prosecutor's permission to enter into negotiations` | F2.2 | 11 |
| 14896 | Factors to consider | inert (reason 1) | heading |  | 0 |
| 14897 | (2) For the purposes of paragraph (1)(c), the prosecutor mus... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14898 | (a) the circumstances in which the act or omission that form... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14899 | (b) the nature and gravity of the act or omission and its im... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14900 | (c) the degree of involvement of senior officers of the orga... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14901 | (d) whether the organization has taken disciplinary action, ... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14902 | (e) whether the organization has made reparations or taken o... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14903 | (f) whether the organization has identified or expressed a w... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14904 | (g) whether the organization — or any of its representatives... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14905 | (h) whether the organization — or any of its representatives... | encoded | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` |  | 18 |
| 14906 | (i) any other factor that the prosecutor considers relevant. | fork | `s 715.32(2) the prosecutor must consider the factor`; rules: `s 715.32(2) the prosecutor's duty to consider the factors` | F19 | 18 |
| 14907 | Factors not to consider | inert (reason 1) | heading |  | 0 |
| 14908 | (3) Despite paragraph (2)(i), if the organization is alleged... | encoded | `s 715.32(3) the prosecutor must not consider the matter`; rules: `s 715.32(3) the prosecutor's prohibition on considering the national economic interest` |  | 5 |
| 14909 | Notice to organization — invitation to negotiate | inert (reason 1) | heading |  | 0 |
| 14910 | 715.33 (1) If the prosecutor wishes to negotiate a remediati... | fork | `s 715.33(1) the prosecutor must give the organization written notice of the offer to enter into negotiations`; `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)`; rules: `s 715.33(1) the prosecutor's duty to give written notice` | F8.1, F4 | 14 |
| 14911 | (a) a summary description of the offence to which the agreem... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14912 | (b) an indication of the voluntary nature of the negotiation... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14913 | (c) an indication of the legal effects of the agreement; | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14914 | (d) an indication that, by agreeing to the terms of this not... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14915 | (e) an indication that negotiations must be carried out in g... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14916 | (f) an indication of how the information disclosed by the or... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14917 | (g) a warning that knowingly making false or misleading stat... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14918 | (h) an indication that either party may withdraw from the ne... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14919 | (i) an indication that reasonable efforts must be made by bo... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14920 | (j) a deadline to accept the offer to negotiate according to... | encoded | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |  | 12 |
| 14921 | Admissions not admissible in evidence | inert (reason 1) | heading |  | 0 |
| 14922 | (2) No admission, confession or statement accepting responsi... | fork | `s 715.33(2) the admission is inadmissible in evidence against the organization` | F3 | 7 |
| 14923 | Mandatory contents of agreement | inert (reason 1) | heading |  | 0 |
| 14924 | 715.34 (1) A remediation agreement must include | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F4 | 27 |
| 14925 | (a) a statement of facts related to the offence that the org... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14926 | (b) the organization’s admission of responsibility for the a... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14927 | (c) an indication of the obligation for the organization to ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14928 | (d) an indication of the obligation for the organization to ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14929 | (e) with respect to any property, benefit or advantage ident... | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F7 | 27 |
| 14930 | (i) forfeit it to Her Majesty in right of Canada, to be disp... | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F7 | 27 |
| 14931 | (ii) forfeit it to Her Majesty in right of a province, to be... | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F7 | 27 |
| 14932 | (iii) otherwise deal with it, as the prosecutor directs; | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F7 | 27 |
| 14933 | (f) an indication of the obligation for the organization to ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14934 | (g) an indication of any reparations, including restitution ... | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F5 | 27 |
| 14935 | (h) an indication of the obligation for the organization to ... | fork | `s 715.34(1) the remediation agreement includes everything that it must include` | F7 | 27 |
| 14936 | (i) an indication of the obligation for the organization to ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14937 | (j) an indication of the legal effects of the agreement; | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14938 | (k) an acknowledgement by the organization that the agreemen... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14939 | (l) an indication of the use that can be made of information... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14940 | (m) a warning that the breach of any term of the agreement m... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14941 | (n) an indication of the obligation for the organization not... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14942 | (o) a notice of the prosecutor’s right to vary or terminate ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14943 | (p) an indication of the deadline by which the organization ... | encoded | `s 715.34(1) the remediation agreement includes everything that it must include` |  | 27 |
| 14944 | Admissions not admissible in evidence | inert (reason 1) | heading |  | 0 |
| 14945 | (2) No admission, confession or statement accepting responsi... | fork | `s 715.34(2) the admission is inadmissible in evidence against the organization` | F3 | 7 |
| 14946 | Optional content of agreement | inert (reason 1) | heading |  | 0 |
| 14947 | (3) A remediation agreement may include, among other things, | encoded | `s 715.34(3) the remediation agreement may include the term` |  | 4 |
| 14948 | (a) an indication of the obligation for the organization to ... | encoded | `s 715.34(3) the remediation agreement may include the term` |  | 4 |
| 14949 | (b) an indication of the obligation for the organization to ... | encoded | `s 715.34(3) the remediation agreement may include the term` |  | 4 |
| 14950 | (c) an indication of the fact that an independent monitor ha... | encoded | `s 715.34(3) the remediation agreement may include the term` |  | 4 |
| 14951 | Independent monitor — conflict of interest | inert (reason 1) | heading |  | 0 |
| 14952 | 715.35 A candidate for appointment as an independent monitor... | encoded | `s 715.35 the candidate must notify the prosecutor in writing of the relationship`; rules: `s 715.35 the candidate's duty to notify the prosecutor` |  | 4 |
| 14953 | Duty to inform victims | inert (reason 1) | heading |  | 0 |
| 14954 | 715.36 (1) After an organization has accepted the offer to n... | fork | `s 715.36(1) the prosecutor must take reasonable steps to inform any victim, or any third party acting on the victim’s behalf, that a remediation agreement may be entered into`; rules: `s 715.36(1) the prosecutor's duty to inform victims` | F8.2 | 2 |
| 14955 | Interpretation | inert (reason 1) | heading |  | 0 |
| 14956 | (2) The duty to inform any victim is to be construed and app... | encoded | `s 715.36(2) the duty to inform any victim is to be construed and applied in that manner` |  | 7 |
| 14957 | Reasons | inert (reason 1) | heading |  | 0 |
| 14958 | (3) If the prosecutor elects not to inform a victim or third... | fork | `s 715.36(3) the prosecutor must provide the court with a statement of the reasons why it was not appropriate to inform`; rules: `s 715.36(3) the prosecutor's duty to give the court a statement of reasons` | F8.3 | 2 |
| 14959 | Application for court approval | inert (reason 1) | heading |  | 0 |
| 14960 | 715.37 (1) When the prosecutor and the organization have agr... | fork | `s 715.37(1) the prosecutor must apply to the court in writing for an order approving the agreement`; rules: `s 715.37(1) the prosecutor's duty to apply for approval` | F8.4 | 2 |
| 14961 | Coming into force | inert (reason 1) | heading |  | 0 |
| 14962 | (2) The coming into force of the agreement is subject to the... | encoded | `s 715.37(2) the court’s approval, to which the coming into force of the agreement is subject, has been given` |  | 2 |
| 14963 | Consideration of victims | inert (reason 1) | heading |  | 0 |
| 14964 | (3) To determine whether to approve the agreement, the court... | encoded | `s 715.37(3) the court must consider the matter in determining whether to approve the agreement`; rules: `s 715.37(3) the court's duty to consider the matters` |  | 5 |
| 14965 | (a) any reparations, statement and other measure referred to... | encoded | `s 715.37(3) the court must consider the matter in determining whether to approve the agreement`; rules: `s 715.37(3) the court's duty to consider the matters` |  | 5 |
| 14966 | (b) any statement made by the prosecutor under subsection 71... | encoded | `s 715.37(3) the court must consider the matter in determining whether to approve the agreement`; rules: `s 715.37(3) the court's duty to consider the matters` |  | 5 |
| 14967 | (c) any victim or community impact statement presented to th... | encoded | `s 715.37(3) the court must consider the matter in determining whether to approve the agreement`; rules: `s 715.37(3) the court's duty to consider the matters` |  | 5 |
| 14968 | (d) any victim surcharge referred to in paragraph 715.34(1)(h). | encoded | `s 715.37(3) the court must consider the matter in determining whether to approve the agreement`; rules: `s 715.37(3) the court's duty to consider the matters` |  | 5 |
| 14969 | Victim or community impact statement | inert (reason 1) | heading |  | 0 |
| 14970 | (4) For the purpose of paragraph (3)(c), the rules provided ... | fork | `s 715.37(4) the rules in the provision apply for the purpose of paragraph (3)(c)` | F16 | 9 |
| 14971 | (a) a victim or community impact statement, or any other evi... | encoded | `s 715.37(4)(a) the court must consider the statement or evidence when determining whether to approve the agreement under subsection (6)`; rules: `s 715.37(4)(a) the court's duty to consider the statement or evidence` |  | 2 |
| 14972 | (b) the inquiry referred to in subsection 722(2) must be mad... | encoded | `s 715.37(4)(b) the inquiry referred to in subsection 722(2) is made at the hearing of the application, as required` |  | 4 |
| 14973 | (c) the duty of the clerk under section 722.1 or subsection ... | encoded | `s 715.37(4)(c) the duty of the clerk is deemed to be the duty of the prosecutor to make reasonable efforts to provide a copy of the statement to the organization or counsel for the organization`; rules: `s 715.37(4)(c) the prosecutor's deemed duty to provide a copy of the statement` |  | 2 |
| 14974 | Victim surcharge | inert (reason 1) | heading |  | 0 |
| 14975 | (5) For the purpose of paragraph 715.34(1)(h), the amount of... | fork | `s 715.37(5) the amount of the victim surcharge in dollars`; `s 715.37(5) the victim surcharge is payable to the treasurer of the province in which the application for approval is made` | F17 | 7 |
| 14976 | Approval order | inert (reason 1) | heading |  | 0 |
| 14977 | (6) The court must, by order, approve the agreement if it is... | fork | `s 715.37(6) the court must, by order, approve the agreement`; rules: `s 715.37(6) the court's duty to approve the agreement` | F8.5 | 4 |
| 14978 | (a) the organization is charged with an offence to which the... | fork | `s 715.37(6) the court must, by order, approve the agreement`; rules: `s 715.37(6) the court's duty to approve the agreement` | F8.5 | 4 |
| 14979 | (b) the agreement is in the public interest; and | fork | `s 715.37(6) the court must, by order, approve the agreement`; rules: `s 715.37(6) the court's duty to approve the agreement` | F8.5 | 4 |
| 14980 | (c) the terms of the agreement are fair, reasonable and prop... | fork | `s 715.37(6) the court must, by order, approve the agreement`; rules: `s 715.37(6) the court's duty to approve the agreement` | F8.5 | 4 |
| 14981 | Stay of proceedings | inert (reason 1) | heading |  | 0 |
| 14982 | (7) As soon as practicable after the court approves the agre... | fork | `s 715.37(7) the prosecutor must direct the clerk or other proper officer of the court to make an entry on the record`; `s 715.37(7) the proceedings against the organization in respect of the offence are stayed`; rules: `s 715.37(7) the prosecutor's duty to direct the entry and the clerk's duty to make it immediately` | F8.6, F9 | 6 |
| 14983 | Other proceedings | inert (reason 1) | heading |  | 0 |
| 14984 | (8) No other proceedings may be initiated against the organi... | encoded | `s 715.37(8) no other proceedings may be initiated against the organization for the same offence` |  | 3 |
| 14985 | Limitation period | inert (reason 1) | heading |  | 0 |
| 14986 | (9) The running of a limitation period in respect of any off... | encoded | `s 715.37(9) the running of the limitation period is suspended` |  | 3 |
| 14987 | Variation order | inert (reason 1) | heading |  | 0 |
| 14988 | 715.38 On application by the prosecutor, the court must, by ... | fork | `s 715.38 the court must, by order, approve the modification to the remediation agreement`; `s 715.38 the modification is deemed to form part of the agreement`; rules: `s 715.38 the court's duty to approve the modification` | F8.7 | 7 |
| 14989 | Termination order | inert (reason 1) | heading |  | 0 |
| 14990 | 715.39 (1) On application by the prosecutor, the court must,... | fork | `s 715.39(1) the court must, by order, terminate the agreement`; rules: `s 715.39(1) the court's duty to terminate the agreement` | F8.8 | 3 |
| 14991 | Recommencement of proceedings | inert (reason 1) | heading |  | 0 |
| 14992 | (2) As soon as the order is made, proceedings stayed in acco... | fork | `s 715.39(2) the stayed proceedings may be recommenced without a new information or a new indictment`; rules: `s 715.39(2) the prosecutor's permission to recommence the proceedings by notice` | F10.1 (listed: upon) | 3 |
| 14993 | Stay of proceedings | inert (reason 1) | heading |  | 0 |
| 14994 | (3) If no notice is given within one year after the order is... | fork | `s 715.39(3) the last day on which notice of recommencement can be given to the clerk`; `s 715.39(3) the proceedings are deemed never to have been commenced` | F11 | 13 |
| 14995 | Order declaring successful completion | inert (reason 1) | heading |  | 0 |
| 14996 | 715.4 (1) On application by the prosecutor, the court must, ... | fork | `s 715.4(1) the court must, by order, declare that the terms of the agreement were met`; rules: `s 715.4(1) the court's duty to declare that the terms were met` | F8.9 | 3 |
| 14997 | Stay of proceedings | inert (reason 1) | heading |  | 0 |
| 14998 | (2) The order stays the proceedings against the organization... | encoded | `s 715.4(2) the order has the effect` |  | 9 |
| 14999 | Deadline | inert (reason 1) | heading |  | 0 |
| 15000 | 715.41 (1) The prosecutor must, as soon as practicable after... | fork | `s 715.41(1) the prosecutor must apply to the court in writing for the order`; `s 715.41(1) the court may issue the order as it deems appropriate`; rules: `s 715.41(1) the prosecutor's duty to apply after the deadline` | F8.10 | 11 |
| 15001 | Deeming | inert (reason 1) | heading |  | 0 |
| 15002 | (2) The agreement is deemed to remain in force until a court... | encoded | `s 715.41(2) the agreement is deemed to remain in force` |  | 4 |
| 15003 | Publication | inert (reason 1) | heading |  | 0 |
| 15004 | 715.42 (1) Subject to subsection (2), the following must be ... | fork | `s 715.42(1) the court must publish the item as soon as practicable`; rules: `s 715.42(1) the court's duty to publish` | F18 | 7 |
| 15005 | (a) the remediation agreement approved by the court; | fork | `s 715.42(1) the court must publish the item as soon as practicable`; rules: `s 715.42(1) the court's duty to publish` | F18 | 7 |
| 15006 | (b) an order made under any of sections 715.37 to 715.41 and... | fork | `s 715.42(1) the court must publish the item as soon as practicable`; rules: `s 715.42(1) the court's duty to publish` | F18 | 7 |
| 15007 | (c) a decision made under subsection (2) or (5) and the reas... | fork | `s 715.42(1) the court must publish the item as soon as practicable`; rules: `s 715.42(1) the court's duty to publish` | F18 | 7 |
| 15008 | Decision not to publish | inert (reason 1) | heading |  | 0 |
| 15009 | (2) The court may decide not to publish the agreement or any... | fork | `s 715.42(2) the court may decide not to publish the item`; rules: `s 715.42(2) the court's permission not to publish` | F2.3 | 6 |
| 15010 | Factors to be considered | inert (reason 1) | heading |  | 0 |
| 15011 | (3) To decide whether the proper administration of justice r... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15012 | (a) society’s interest in encouraging the reporting of offen... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15013 | (b) whether it is necessary to protect the identity of any v... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15014 | (c) the prevention of any adverse effect to any ongoing inve... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15015 | (d) whether effective alternatives to the decision referred ... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15016 | (e) the salutary and deleterious effects of making the decis... | encoded | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` |  | 7 |
| 15017 | (f) any other factor that the court considers relevant. | fork | `s 715.42(3) the court must consider the factor`; rules: `s 715.42(3) the court's duty to consider the factors` | F19 | 7 |
| 15018 | Conditions | inert (reason 1) | heading |  | 0 |
| 15019 | (4) The court may make its decision subject to any condition... | encoded | `s 715.42(4) the court may make its decision subject to the condition` |  | 3 |
| 15020 | Review of decision | inert (reason 1) | heading |  | 0 |
| 15021 | (5) On application by any person, the court must review the ... | fork | `s 715.42(5) the court must review the decision made under subsection (2)`; `s 715.42(5) the court must publish the agreement, order or reasons, in whole or in part, as soon as practicable`; rules: `s 715.42(5) the court's duty to review the decision`; `s 715.42(5) the court's duty to publish after the review` | F8.11, F8.12 | 6 |
| 15022 | Regulations | inert (reason 1) | heading |  | 0 |
| 15023 | 715.43 (1) On the recommendation of the Minister of Justice,... | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15024 | (a) the form of the remediation agreement; and | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15025 | (b) the verification of compliance by an independent monitor... | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15026 | (i) the qualifications for monitors, | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15027 | (ii) the process to select a monitor, | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15028 | (iii) the form and content of a conflict of interest notific... | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15029 | (iv) reporting requirements. | inert (reason 2) | regulation-making power: machinery; quoted in the constant `s 715.43(1) and (2) the regulation-making and schedule-amending powers as the text states them` |  | 0 |
| 15030 | Amendment of schedule | inert (reason 1) | heading |  | 0 |
| 15031 | (2) On the recommendation of the Minister of Justice, the Go... | inert (reason 2) | power to amend the schedule by order: machinery; quoted in the same constant |  | 0 |
| 15032 | Deleting offence | inert (reason 1) | heading |  | 0 |
| 15033 | (3) If the Governor in Council orders the deletion of an off... | fork | `s 715.43(3) this Part continues to apply to the organization despite the deletion of the offence from the schedule` | F29 | 6 |
| 15035 | PART XXII.2 Alternative Measures and Restorative Justice Pro... | inert (reason 1) | the Part's title |  | 0 |
| 15037 | Definitions | inert (reason 1) | headings |  | 0 |
| 15038 | Definitions | inert (reason 1) | headings |  | 0 |
| 15039 | 715.44 The following definitions apply in this Part. | inert (reason 1) | lead-in: it sets the scope of the three definitions below and states no rule of its own |  | 0 |
| 15040 | alternative measures means measures other than judicial proc... | encoded | `s 715.44 alternative measures` |  | 5 |
| 15041 | restorative justice, in respect of the criminal justice syst... | encoded | `s 715.44 restorative justice` |  | 3 |
| 15042 | restorative justice process means a process that provides an... | encoded | `s 715.44 restorative justice process` |  | 5 |
| 15044 | Purpose and Principles | inert (reason 1) | headings |  | 0 |
| 15045 | Purpose | inert (reason 1) | headings |  | 0 |
| 15046 | 715.45 The purpose of this Part is to contribute to the resp... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15047 | (a) holding a person alleged to have committed an offence or... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15048 | (b) promoting a sense of responsibility for the offence or a... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15049 | (c) repairing the harm caused to the victim and the community; | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15050 | (d) promoting the rehabilitation and reintegration of the pe... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15051 | (e) preventing further harm and involvement in the criminal ... | inert (reason 1) | a purpose clause that creates no rule; quoted in the constant `s 715.45 the purpose of this Part as the text states it` |  | 0 |
| 15052 | Principles | inert (reason 1) | heading |  | 0 |
| 15053 | 715.46 The following principles apply to this Part: | encoded | `s 715.46 the principle applies to this Part` |  | 5 |
| 15054 | (a) judicial resources are more appropriately used in relati... | encoded | `s 715.46 the principle applies to this Part` |  | 5 |
| 15055 | (b) measures that are taken under this Part allow for effect... | encoded | `s 715.46 the principle applies to this Part` |  | 5 |
| 15056 | (c) crime has a harmful impact on victims and on society and... | encoded | `s 715.46 the principle applies to this Part` |  | 5 |
| 15057 | (d) measures that are taken under this Part take into accoun... | encoded | `s 715.46 the principle applies to this Part` |  | 5 |
| 15059 | Warnings and Referrals | inert (reason 1) | headings |  | 0 |
| 15060 | Warnings and referrals — police | inert (reason 1) | headings |  | 0 |
| 15061 | 715.47 (1) A police officer must, if it is appropriate in th... | fork | `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`; rules: `s 715.47(1) the police officer's duty to consider the options` | F6, F8.13 | 11 |
| 15062 | (a) taking no further action; | fork | `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`; rules: `s 715.47(1) the police officer's duty to consider the options` | F6, F8.13 | 11 |
| 15063 | (b) issuing a warning to the person; or | fork | `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`; rules: `s 715.47(1) the police officer's duty to consider the options` | F6, F8.13 | 11 |
| 15064 | (c) with the consent of the person, referring them to a prog... | fork | `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`; rules: `s 715.47(1) the police officer's duty to consider the options` | F6, F8.13 | 11 |
| 15065 | Validity of charges | inert (reason 1) | heading |  | 0 |
| 15066 | (2) The failure of a police officer to consider the options ... | fork | `s 715.47(2) the failure of the police officer to consider the options invalidates the subsequent charges` | F20 | 3 |
| 15067 | Warnings and referrals — prosecutor | inert (reason 1) | heading |  | 0 |
| 15068 | 715.48 (1) A prosecutor must, if it is appropriate in the ci... | fork | `s 715.48(1) the prosecutor must consider the option before commencing or continuing judicial proceedings`; rules: `s 715.48(1) the prosecutor's duty to consider the options` | F8.14 | 9 |
| 15069 | (a) issuing a warning to the person; or | fork | `s 715.48(1) the prosecutor must consider the option before commencing or continuing judicial proceedings`; rules: `s 715.48(1) the prosecutor's duty to consider the options` | F8.14 | 9 |
| 15070 | (b) with the consent of the person, referring them to a prog... | fork | `s 715.48(1) the prosecutor must consider the option before commencing or continuing judicial proceedings`; rules: `s 715.48(1) the prosecutor's duty to consider the options` | F8.14 | 9 |
| 15071 | Validity of proceedings | inert (reason 1) | heading |  | 0 |
| 15072 | (2) The failure of a prosecutor to consider the options set ... | fork | `s 715.48(2) the failure of the prosecutor to consider the options invalidates the proceedings` | F20 | 3 |
| 15074 | Alternative Measures | inert (reason 1) | heading |  | 0 |
| 15076 | Conditions for Use | inert (reason 1) | headings |  | 0 |
| 15077 | Conditions | inert (reason 1) | headings |  | 0 |
| 15078 | 715.49 Alternative measures may be used in respect of a pers... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15079 | (a) the alternative measures are part of a program of altern... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15080 | (b) the person who is considering whether to use the alterna... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15081 | (c) the person alleged to have committed the offence, having... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15082 | (d) the person alleged to have committed the offence has, be... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15083 | (e) the person alleged to have committed the offence accepts... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15084 | (f) in the opinion of the Attorney General or the Attorney G... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15085 | (g) the prosecution of the offence is not in any way barred ... | fork | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` | F2.4 | 8 |
| 15087 | Restrictions on Use | inert (reason 1) | headings |  | 0 |
| 15088 | Restrictions | inert (reason 1) | headings |  | 0 |
| 15089 | 715.5 Alternative measures must not be used in respect of a ... | fork | `s 715.5 alternative measures must not be used in respect of the person` | F21 | 4 |
| 15090 | (a) denies participation or involvement in the commission of... | fork | `s 715.5 alternative measures must not be used in respect of the person` | F21 | 4 |
| 15091 | (b) expresses the wish to have any charge against them dealt... | fork | `s 715.5 alternative measures must not be used in respect of the person` | F21 | 4 |
| 15092 | Admissions not admissible in evidence | inert (reason 1) | heading |  | 0 |
| 15093 | 715.51 No admission, confession or statement accepting respo... | encoded | `s 715.51 the admission is inadmissible in evidence against the person` |  | 4 |
| 15094 | No bar to proceedings | inert (reason 1) | heading |  | 0 |
| 15095 | 715.52 (1) The use of alternative measures in respect of a p... | encoded | `s 715.52(1) the use of alternative measures is a bar to proceedings against the person under this Act` |  | 3 |
| 15096 | (a) if the court is satisfied on a balance of probabilities ... | fork | `s 715.52(1)(a) the court must dismiss the charge`; rules: `s 715.52(1)(a) the court's duty to dismiss the charge` | F8.15 | 3 |
| 15097 | (b) if the court is satisfied on a balance of probabilities ... | fork | `s 715.52(1)(b) the court may dismiss the charge`; rules: `s 715.52(1)(b) the court's permission to dismiss the charge` | F2.5; listed: F10.3 ("where a charge is laid") | 5 |
| 15098 | Laying of information or other process | inert (reason 1) | heading |  | 0 |
| 15099 | (2) Subject to subsection (1), nothing in this Part is to be... | fork | `s 715.52(2) this Part is to be construed as preventing the person from doing the act` | F25 | 6 |
| 15101 | Restorative Justice Processes | inert (reason 1) | heading |  | 0 |
| 15103 | Principles | inert (reason 1) | headings |  | 0 |
| 15104 | Principles | inert (reason 1) | headings |  | 0 |
| 15105 | 715.53 The following additional principles apply to the use ... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15106 | (a) restorative justice processes prioritize the acknowledge... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15107 | (b) they are voluntary and participants must fully and freel... | encoded | `s 715.53 the principle applies to the use of restorative justice processes`; `s 715.53(b) the participant must fully and freely consent to participate`; `s 715.53(b) the participant may freely withdraw from the restorative justice process at any time` |  | 12 |
| 15108 | (c) they take into consideration the safety and security of ... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15109 | (d) they are based on courtesy, compassion and respect, incl... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15110 | (e) they foster and support the meaningful participation of ... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15111 | (f) they enable participants to communicate openly and hones... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15112 | (g) they provide opportunities for understanding, healing an... | encoded | `s 715.53 the principle applies to the use of restorative justice processes` |  | 8 |
| 15113 | Application | inert (reason 1) | heading |  | 0 |
| 15114 | 715.54 (1) A restorative justice process may be used at any ... | encoded | `s 715.54(1) a restorative justice process may be used at the stage` |  | 2 |
| 15115 | Restorative justice process — forms | inert (reason 1) | heading |  | 0 |
| 15116 | (2) A restorative justice process may take various forms, in... | encoded | `s 715.54(2) a restorative justice process may take the form` |  | 4 |
| 15117 | For greater certainty | inert (reason 1) | heading |  | 0 |
| 15118 | (3) For greater certainty, sections 715.49 to 715.52 apply w... | fork | `s 715.54(3) the provision applies to the restorative justice process` | F13, F16 | 8 |
| 15120 | Conferences | inert (reason 1) | headings |  | 0 |
| 15121 | Conference may be convened | inert (reason 1) | headings |  | 0 |
| 15122 | 715.55 (1) A judge, justice or any person authorized under t... | fork | `s 715.55(1) the person may, on request or on their own initiative, convene or cause to be convened a conference`; `s 715.55(1) the person participates in the conference`; rules: `s 715.55(1) a judge's permission to convene a conference`; `s 715.55(1) a justice's permission to convene a conference` | F24 | 10 |
| 15123 | Objective | inert (reason 1) | heading |  | 0 |
| 15124 | (2) The objective of a conference is, among other things, to... | encoded | `s 715.55(2) the objective is an objective of a conference` |  | 3 |
| 15125 | Rules — establishment | inert (reason 1) | heading |  | 0 |
| 15126 | (3) The Attorney General or any other minister designated by... | fork | `s 715.55(3) the person may establish rules and practices for the convening and conducting of the conference`; rules: `s 715.55(3) the Attorney General's permission to establish rules and practices` | F28 | 4 |
| 15127 | Rules to apply | inert (reason 1) | heading |  | 0 |
| 15128 | (4) In provinces and territories where rules and practices a... | fork | `s 715.55(4) the conference must be convened and conducted in accordance with the rules and practices` | F8.16 | 3 |
| 15130 | Records | inert (reason 1) | headings |  | 0 |
| 15131 | Records — warnings or referrals | inert (reason 1) | headings |  | 0 |
| 15132 | 715.56 Sections 715.57 to 715.6 apply only in respect of per... | fork | `s 715.56 the provision applies in respect of the person` | F26 | 12 |
| 15133 | Record keeping | inert (reason 1) | heading |  | 0 |
| 15134 | 715.57 The police officer who issues a warning or makes a re... | fork | `s 715.57 the police officer is to keep a record of the warning issued or referral made, including the identity of the person warned or referred`; rules: `s 715.57 the police officer's duty to keep a record` | F6 | 2 |
| 15135 | Police records | inert (reason 1) | heading |  | 0 |
| 15136 | 715.58 (1) A record relating to any offence alleged to have ... | encoded | `s 715.58(1) the record may be kept by the police force` |  | 3 |
| 15137 | Disclosure by peace officer | inert (reason 1) | heading |  | 0 |
| 15138 | (2) A peace officer may disclose to any person any informati... | encoded | `s 715.58(2) a peace officer may disclose the information to any person`; rules: `s 715.58(2) a peace officer's permission to disclose information to any person` |  | 3 |
| 15139 | Other disclosure | inert (reason 1) | heading |  | 0 |
| 15140 | (3) A peace officer may disclose to an insurance company any... | encoded | `s 715.58(3) a peace officer may disclose the information to an insurance company`; rules: `s 715.58(3) a peace officer's permission to disclose information to an insurance company` |  | 3 |
| 15141 | Government records | inert (reason 1) | heading |  | 0 |
| 15142 | 715.59 (1) A department or agency of any government in Canad... | encoded | `s 715.59(1) the department or agency may keep records containing the information` |  | 5 |
| 15143 | (a) for the purposes of an investigation of an offence alleg... | encoded | `s 715.59(1) the department or agency may keep records containing the information` |  | 5 |
| 15144 | (b) for use in proceedings against a person under this Act; or | encoded | `s 715.59(1) the department or agency may keep records containing the information` |  | 5 |
| 15145 | (c) as a result of the use of alternative measures to deal w... | encoded | `s 715.59(1) the department or agency may keep records containing the information` |  | 5 |
| 15146 | Records kept — alternative measures | inert (reason 1) | heading |  | 0 |
| 15147 | (2) Any person or organization may keep records containing i... | encoded | `s 715.59(2) the person or organization may keep records containing the information` |  | 2 |
| 15148 | Disclosure of records | inert (reason 1) | heading |  | 0 |
| 15149 | 715.6 (1) Any information contained in a record that is kept... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15150 | (a) any judge or court for any purpose relating to proceedin... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15151 | (b) any peace officer | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15152 | (i) for the purpose of investigating any offence that the pe... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15153 | (ii) for any purpose related to the administration of the ca... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15154 | (c) any member of a department or agency of a government in ... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15155 | (i) engaged in the administration of alternative measures in... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15156 | (ii) preparing a report in respect of the person as required... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15157 | (d) any other person who is deemed, or any person within a c... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15158 | (i) desirable in the public interest for research or statist... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15159 | (ii) desirable in the interest of the proper administration ... | fork | `s 715.6(1) the information may be made available to the recipient` | F2.6, F14 | 14 |
| 15160 | Access to information — alternative measures | inert (reason 1) | heading |  | 0 |
| 15161 | (2) Information contained in the record, other than the iden... | fork | `s 715.6(2) the information may be made available to the recipient` | F15 | 3 |
| 15162 | Subsequent disclosure | inert (reason 1) | heading |  | 0 |
| 15163 | (3) If a record is made available for inspection to any pers... | fork | `s 715.6(3) the person may subsequently disclose the information contained in the record`; `s 715.6(3) the person may not disclose the information in a form that would reasonably be expected to identify the person to whom it relates` | F2.7 (the grant, flipped); F30 (the bar); the text closes the identifying-form gate itself (kept JUST FALSE) | 7 |
| 15164 | Information and copies | inert (reason 1) | heading |  | 0 |
| 15165 | (4) Any person to whom a record is authorized to be made ava... | encoded | `s 715.6(4) the person may be given the information contained in the record and a copy of any part of the record` |  | 2 |
| 15166 | Evidence of warning or referral not admissible | inert (reason 1) | heading |  | 0 |
| 15167 | (5) Evidence that an individual has received a warning or re... | encoded | `s 715.6(5) the evidence is inadmissible` |  | 10 |
| 15168 | Record keeping — period | inert (reason 1) | heading |  | 0 |
| 15169 | (6) A record kept under any of sections 715.57 to 715.59 may... | fork | `s 715.6(6) the record may not be introduced into evidence` | F11, F12 | 7 |

## Fork register (ccc25)
Every ambiguity that changes an answer: the reading taken, the other reading, and the text that licenses each.
A row marked F2.n is a function named for a grant that answers NOTHING because an "if" gate failed (the coordinator's name-test ruling of 2026-11-12, below).
F8.n are the sites of one reading (a duty whose gate is unmet), one line each.
A comment in a module that says "fork F2", "fork F8" or "fork F10" points at that family, F2.n, F8.n or F10.n.
Listed, not decided (group (i) of the ruling): "may" functions whose gate is "where", "when" or "upon": F10.1 (s 715.39(2)), F10.2 (s 715.3(2)) and F10.3 (s 715.52(1)(b)), one row per function, each keeping the answer its first version gave.
Listed, not decided (group (ii)): "entitled"-named functions: none in this range.

- **F1** (s 715.3(2); `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf`)
  Reading taken: "A third party not referred to in section 2.2" is read as: the keel's composed answer for section 2.2 is not JUST TRUE for this person, so an answer of NOTHING or JUST FALSE from section 2.2 both leave the person "not referred to".
  Other reading: "Referred to" covers every person section 2.2(1) mentions by relationship, including one section 2.2(2) then bars; such a person would be outside this subsection too.
  Licence: the words "a third party not referred to in section 2.2" (src:14881).
- **F2.1** (s 715.3(2); `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf`)
  Reading taken: NOTHING when the court has authorized the third party but neither the victim requests it nor the prosecutor deems it appropriate (an "if" gate on a grant named "may", the coordinator's name-test ruling of 2026-11-12).
  Other reading: JUST FALSE, a failed "if" read as the text's own no ("may not").
  Licence: "if the victim requests it or the prosecutor deems it appropriate" (src:14881). The same function also carries a "when" gate, listed as F10.2: when the court has not authorized the third party the answer is JUST FALSE (the periods ruling, (c) of 2026-11-05).
- **F2.2** (s 715.32(1); `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`)
  Reading taken: NOTHING when any of conditions (a) to (d) is unmet, or the body is not an organization of this Part, or the offence is not listed (a grant named "may" with an "if" gate not closed by "only if").
  Other reading: JUST FALSE, a failed "if" read as the text's own no.
  Licence: "may enter into negotiations ... if the following conditions are met" (src:14891).
- **F2.3** (s 715.42(2); `s 715.42(2) the court may decide not to publish the item`)
  Reading taken: NOTHING when the court is not satisfied that non-publication is necessary for the proper administration of justice.
  Other reading: JUST FALSE, a failed "if" read as the text's own no.
  Licence: "may decide not to publish ... if it is satisfied that the non-publication is necessary" (src:15009).
- **F2.4** (s 715.49; `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence`)
  Reading taken: NOTHING when any of conditions (a) to (g) is unmet.
  Other reading: JUST FALSE, a failed "if" read as the text's own no (alternative measures may not be used).
  Licence: "may be used ... if the following conditions are met" (src:15078). Section 715.5 is the text's own bar for the two cases it names.
- **F2.5** (s 715.52(1)(b); `s 715.52(1)(b) the court may dismiss the charge`)
  Reading taken: NOTHING when the court is not satisfied of partial compliance or does not think the prosecution unfair.
  Other reading: JUST FALSE, a failed "if" read as the text's own no. The function also carries a "where" gate (no charge laid: JUST FALSE, listed as F10.3).
  Licence: "the court may dismiss the charge if, in the opinion of the court, the prosecution of the charge would be unfair" (src:15097).
- **F2.6** (s 715.6(1); `s 715.6(1) the information may be made available to the recipient`)
  Reading taken: NOTHING for a recipient under paragraph (d) when the judge is satisfied of neither (i) nor (ii).
  Other reading: JUST FALSE, a failed "if" read as the text's own no.
  Licence: "if the judge is satisfied that the disclosure is (i) desirable in the public interest for research or statistical purposes, or (ii) desirable in the interest of the proper administration of justice" (src:15157-15159).
- **F2.7** (s 715.6(3); `s 715.6(3) the person may subsequently disclose the information contained in the record`)
  Reading taken: NOTHING when the record was not made available for inspection under subparagraph (1)(d)(i). JUST FALSE is kept where the form would reasonably be expected to identify the person, because the text closes that gate with "may not".
  Other reading: JUST FALSE for the first case too.
  Licence: "If a record is made available for inspection to any person under subparagraph (1)(d)(i), that person may subsequently disclose information contained in the record but may not disclose the information in any form that would reasonably be expected to identify the person" (src:15163).
- **F3** (ss 715.33(2), 715.34(2); `s 715.33(2) the admission is inadmissible in evidence against the organization`; `s 715.34(2) the admission is inadmissible in evidence against the organization`)
  Reading taken: Once the exception is met (the statement is in the statement of facts or admission of responsibility, and the agreement is approved) the answer is JUST FALSE: the text itself carves it out of the bar.
  Other reading: NOTHING: the subsection is silent on whether such a statement is admissible.
  Licence: "except those contained in the statement of facts ... if the parties reach an agreement and it is approved by the court" (src:14922, src:14945). The case-by-case list names "an 'unless' or 'except' once it is met".
- **F4** (ss 715.33(1), 715.34(1); `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)`; `s 715.34(1) the remediation agreement includes everything that it must include`)
  Reading taken: A "must include" requirement that is not met is JUST FALSE: the text states the requirement in its own words.
  Other reading: NOTHING: a bare "must" not done leaves the text silent on the consequence.
  Licence: "the notice must include" (src:14910); "A remediation agreement must include" (src:14924). The case-by-case list names "a bare 'must' not done".
- **F5** (s 715.34(1)(g); `s 715.34(1) the remediation agreement includes everything that it must include`)
  Reading taken: "An indication of any reparations ... or a statement by the prosecutor of the reasons why reparations ... are not appropriate ... and an indication of any measure required in lieu" is read as: reparations, OR (the statement AND the measure in lieu).
  Other reading: (Reparations OR the statement) AND the measure in lieu, so a measure is always required.
  Licence: the order of the words "or a statement ... and an indication of any measure required in lieu" (src:14934).
- **F6** (ss 715.47, 715.57; `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`; `s 715.57 the police officer is to keep a record of the warning issued or referral made, including the identity of the person warned or referred`)
  Reading taken: "Police officer" is read as the core's `a peace officer` (section 2 defines "peace officer" and not "police officer"; NEEDS-CORE.md asks for a constructor).
  Other reading: A police officer who is not a peace officer: nothing in the sources decides.
  Licence: the words "police officer" (src:15061, src:15134) beside "peace officer" (src:15138).
- **F7** (s 715.34(1)(e), (h); `s 715.34(1) the remediation agreement includes everything that it must include`)
  Reading taken: Paragraph (e) is met when the agreement identifies no property, benefit or advantage, because the obligation attaches only to property "identified in the agreement"; paragraph (h) is met when every offence in the agreement is an offence under section 3 or 4 of the Corruption of Foreign Public Officials Act.
  Other reading: (e) requires some statement even where no property is identified; (h) is per offence, so an agreement that covers both kinds of offence needs a surcharge term for the other kind (the function takes one flag for "every offence").
  Licence: "with respect to any property, benefit or advantage identified in the agreement" (src:14929); "for each offence ... other than an offence under section 3 or 4" (src:14935).
- **F8.1** (s 715.33(1); `s 715.33(1) the prosecutor must give the organization written notice of the offer to enter into negotiations`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.2** (s 715.36(1); `s 715.36(1) the prosecutor must take reasonable steps to inform any victim, or any third party acting on the victim’s behalf, that a remediation agreement may be entered into`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.3** (s 715.36(3); `s 715.36(3) the prosecutor must provide the court with a statement of the reasons why it was not appropriate to inform`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.4** (s 715.37(1); `s 715.37(1) the prosecutor must apply to the court in writing for an order approving the agreement`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.5** (s 715.37(6); `s 715.37(6) the court must, by order, approve the agreement`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.6** (s 715.37(7); `s 715.37(7) the prosecutor must direct the clerk or other proper officer of the court to make an entry on the record`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.7** (s 715.38; `s 715.38 the court must, by order, approve the modification to the remediation agreement`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.8** (s 715.39(1); `s 715.39(1) the court must, by order, terminate the agreement`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.9** (s 715.4(1); `s 715.4(1) the court must, by order, declare that the terms of the agreement were met`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.10** (s 715.41(1); `s 715.41(1) the prosecutor must apply to the court in writing for the order`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.11** (s 715.42(5); `s 715.42(5) the court must review the decision made under subsection (2)`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.12** (s 715.42(5); `s 715.42(5) the court must publish the agreement, order or reasons, in whole or in part, as soon as practicable`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.13** (s 715.47(1); `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.14** (s 715.48(1); `s 715.48(1) the prosecutor must consider the option before commencing or continuing judicial proceedings`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.15** (s 715.52(1)(a); `s 715.52(1)(a) the court must dismiss the charge`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F8.16** (s 715.55(4); `s 715.55(4) the conference must be convened and conducted in accordance with the rules and practices`)
  Reading taken: A duty whose "if", "where", "when" or "after" gate is unmet answers JUST FALSE (the duty has not arisen).
  Other reading: NOTHING: the text says when the duty arises and is silent on what follows if it has not.
  Licence: the gate words of the provision (see the function's own comments); this is one of the six questions of 2026-11-05 decided case by case, and the sites share this one reading.
- **F9** (s 715.37(7); `s 715.37(7) the prosecutor must direct the clerk or other proper officer of the court to make an entry on the record`; rule `s 715.37(7) the prosecutor's duty to direct the entry and the clerk's duty to make it immediately`)
  Reading taken: "That entry must be made immediately" is read as the clerk's duty WITHIN 0 from the prosecutor's direction; "as soon as practicable" states no number, so the prosecutor's duty has no WITHIN.
  Other reading: "Immediately" as a short period of days: the text gives no number.
  Licence: "As soon as practicable after the court approves the agreement, the prosecutor must direct the clerk ... and that entry must be made immediately" (src:14982).
- **F10.1** (s 715.39(2); `s 715.39(2) the stayed proceedings may be recommenced without a new information or a new indictment`)
  Reading taken: LISTED, NOT FLIPPED (group (i) of the name-test ruling): the first-pass answer stands. "As soon as the order is made" is an "upon"-kind gate on a grant named "may"; the answer is JUST FALSE before an order (ruling (c) of 2026-11-05: "when", "upon" and "whenever" count as "where").
  Other reading: NOTHING, by the Guide's line that a grant limited in its own wording and outside the limit is not covered. ASSUMED, NOT RULED, that these equivalents go with the listed group: a question for the maintainer or a lawyer.
  Licence: "As soon as the order is made, proceedings stayed ... may be recommenced" (src:14992).
- **F10.2** (s 715.3(2); `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf`)
  Reading taken: LISTED, NOT FLIPPED (group (i)): the first-pass answer stands. "When authorized to do so by the court" is a "when" gate on a grant named "may"; when the court has not authorized the third party the answer is JUST FALSE (ruling (c) of 2026-11-05). The function's separate "if the victim requests it or the prosecutor deems it appropriate" gate is an "if" and is flipped (F2.1).
  Other reading: NOTHING when the court has not authorized the third party (the Guide's line on grants). ASSUMED, NOT RULED, that these equivalents go with the listed group.
  Licence: "may also act on a victim’s behalf when authorized to do so by the court" (src:14881).
- **F10.3** (s 715.52(1)(b); `s 715.52(1)(b) the court may dismiss the charge`)
  Reading taken: LISTED, NOT FLIPPED (group (i)): the first-pass answer stands. "In the case where a charge is laid" is a "where"-kind gate on a grant named "may"; when no charge is laid the answer is JUST FALSE (ruling (c) of 2026-11-05). The function's "if, in the opinion of the court, the prosecution of the charge would be unfair" gate is an "if" and is flipped (F2.5).
  Other reading: NOTHING when no charge is laid (the Guide's line on grants). ASSUMED, NOT RULED, that these equivalents go with the listed group.
  Licence: "but, in the case where a charge is laid against that person in respect of that offence" (src:15095), which governs paragraphs (a) and (b).
- **F11** (ss 715.39(3), 715.6(6); `s 715.39(3) the last day on which notice of recommencement can be given to the clerk`; `s 715.6(6) the record may not be introduced into evidence`)
  Reading taken: "Within one year after the order is made" ends on the first anniversary (the same date one year on); "more than two years after the end of the period" begins the day after the second anniversary. The library's `add years` clamps 29 February to 28 February, so a period that starts on 29 February 2024 has its second anniversary on 28 February 2026.
  Other reading: The year ends the day before the anniversary, or is counted as 365 or 366 days from the day after; for 29 February the anniversary is 1 March.
  Licence: "within one year after the order is made" (src:14994); "more than two years after the end of the period" (src:15169).
- **F12** (s 715.6(6); `s 715.6(6) the record may not be introduced into evidence`)
  Reading taken: Before the second anniversary the bar does not apply: JUST FALSE (a "more than two years after" time gate on a bar, ruling (a) of 2026-11-05 on periods).
  Other reading: NOTHING: the sentence does not say what is permitted before two years.
  Licence: "may not be introduced into evidence, except for the purposes set out in paragraph 721(3)(c), more than two years after" (src:15169).
- **F13** (s 715.54(3); `s 715.54(3) the provision applies to the restorative justice process`)
  Reading taken: When the restorative justice process is not used as an alternative measure the answer for sections 715.49 to 715.52 is JUST FALSE (a "when" gate, ruling (c) of 2026-11-05).
  Other reading: NOTHING: the subsection opens "For greater certainty" and may be read as declaratory only, saying nothing about other uses. Listed for a lawyer.
  Licence: "For greater certainty, sections 715.49 to 715.52 apply when a restorative justice process is used as an alternative measure" (src:15118).
- **F14** (s 715.6(1)(d); `s 715.6(1) the information may be made available to the recipient`)
  Reading taken: "To the extent directed by the judge" limits how much may be made available; the function answers whether the information may be made available to the recipient, and the extent is left to the judge.
  Other reading: The extent as an input that the function applies.
  Licence: "to the extent directed by the judge" (src:15157).
- **F15** (s 715.6(2); `s 715.6(2) the information may be made available to the recipient`)
  Reading taken: For the identity of the person the answer is NOTHING: "other than the identity" limits the grant and the text does not say the identity may not be made available.
  Other reading: JUST FALSE for the identity.
  Licence: "Information contained in the record, other than the identity of the person to whom the record relates, may be made available" (src:15161). The case-by-case list names "(other than X)".
- **F16** (ss 715.37(4), 715.54(3), 715.56; `s 715.37(4) the rules in the provision apply for the purpose of paragraph (3)(c)`; `s 715.54(3) the provision applies to the restorative justice process`; `s 715.56 the provision applies in respect of the person`)
  Reading taken: Sections named by number are tested against the core's `Provision of the Code`, section as a decimal: 715.5 is section 715.5, which is 715.50 and sorts between 715.49 and 715.51; section 715.6 is 715.60 and sorts after 715.59. The exception "other than subsection 722(6)" is the section 722 with subsection "(6)".
  Other reading: A list of strings.
  Licence: the core's own comment on the record (no section number ends in a zero after the point); "sections 722 to 722.2 apply, other than subsection 722(6)" (src:14970).
- **F17** (s 715.37(5); `s 715.37(5) the amount of the victim surcharge in dollars`; `s 715.37(5) the victim surcharge is payable to the treasurer of the province in which the application for approval is made`)
  Reading taken: The surcharge is 30% of the penalty unless the prosecutor deems another percentage appropriate (a number the caller supplies, never guessed); for an offence under section 3 or 4 of the Corruption of Foreign Public Officials Act the answer is NOTHING because the figure is stated "for the purpose of paragraph 715.34(1)(h)", which excludes that offence; "payable to the treasurer of the province" is the flag that the application is made in a province.
  Other reading: A surcharge of 30% for that offence too.
  Licence: "For the purpose of paragraph 715.34(1)(h), the amount of the victim surcharge is 30% of any penalty ... or any other percentage that the prosecutor deems appropriate" (src:14975).
- **F18** (s 715.42(1); `s 715.42(1) the court must publish the item as soon as practicable`)
  Reading taken: "Subject to subsection (2)" takes the agreement and the orders and reasons out of the duty to publish when the court has decided not to publish; paragraph (c), a decision under (2) or (5), is published even then, because (2) lets the court withhold only the agreement and the paragraph (1)(b) orders and reasons.
  Other reading: A decision under (2) can itself be withheld.
  Licence: "Subject to subsection (2), the following must be published" (src:15004) against "may decide not to publish the agreement or any order or reasons referred to in paragraph (1)(b)" (src:15009).
- **F19** (ss 715.32(2)(i), 715.42(3)(f); `s 715.32(2) the prosecutor must consider the factor`; `s 715.42(3) the court must consider the factor`)
  Reading taken: A factor named only as "any other factor that the prosecutor (or the court) considers relevant" is a factor to consider only when the decision-maker does consider it relevant (JUST TRUE); otherwise NOTHING.
  Other reading: Every factor of the world is one the decision-maker must consider (never); or JUST FALSE for a factor not considered relevant.
  Licence: "any other factor that the prosecutor considers relevant" (src:14906); "any other factor that the court considers relevant" (src:15017).
- **F20** (ss 715.47(2), 715.48(2); `s 715.47(2) the failure of the police officer to consider the options invalidates the subsequent charges`; `s 715.48(2) the failure of the prosecutor to consider the options invalidates the proceedings`)
  Reading taken: "Does not invalidate" is a flat negative: for the failure and the subsequent charges (or proceedings) the answer is JUST FALSE to "does it invalidate"; outside that, NOTHING (ruling N2, option A: flat negatives count as a no).
  Other reading: NOTHING for the covered case too.
  Licence: "does not invalidate any subsequent charges against the person for the offence" (src:15066); "does not invalidate any proceedings" (src:15072).
- **F21** (s 715.5; `s 715.5 alternative measures must not be used in respect of the person`)
  Reading taken: JUST TRUE where the person denies involvement or wishes the charge dealt with by the court; NOTHING otherwise (the bar's own wording does not reach any other person, and no "only" closes it). No party is named, so there is no regulative rule.
  Other reading: JUST FALSE for a person who does neither.
  Licence: "Alternative measures must not be used in respect of a person who (a) denies participation or involvement in the commission of the offence; or (b) expresses the wish to have any charge against them dealt with by the court" (src:15089-15091).
- **F22** (s 715.3(1) "remediation agreement"; `s 715.3(1) remediation agreement`)
  Reading taken: When one limb is a plain no (not an agreement, the organization is not accused, the other party is not a prosecutor, no stay, or the organization or offence answer is JUST FALSE) the answer is JUST FALSE even if another limb's answer is NOTHING; NOTHING only when no limb is a plain no and one is not covered.
  Other reading: NOTHING whenever any limb is NOTHING.
  Licence: "remediation agreement means an agreement, between an organization accused of having committed an offence and a prosecutor, to stay any proceedings" (src:14878): a "means" definition says no in its own words.
- **F23** (s 715.3(1) "victim"; `s 715.3(1) victim`)
  Reading taken: For an offence under section 3 or 4 of the Corruption of Foreign Public Officials Act, a person outside Canada is a victim whatever section 2 answers.
  Other reading: Section 2's answer first, with the extension only as a fallback.
  Licence: "it includes any person outside Canada" (src:14879).
- **F24** (s 715.55(1); `s 715.55(1) the person may, on request or on their own initiative, convene or cause to be convened a conference`; `s 715.55(1) the person participates in the conference`)
  Reading taken: A person "authorized under the rules and practices referred to in subsection (3)" is a flag input because the core has no constructor for them (NEEDS-CORE.md); a provincial court judge is a justice by section 2, but the function tests the constructor `a justice`, so the caller passes `a justice`.
  Other reading: The core's constructors extended.
  Licence: "A judge, justice or any person authorized under the rules and practices" (src:15122).
- **F25** (s 715.52(2); `s 715.52(2) this Part is to be construed as preventing the person from doing the act`)
  Reading taken: "Subject to subsection (1)": where subsection (1)(a) requires the court to dismiss the charge, the answer is NOTHING, not JUST FALSE, because subsection (1) prevails and this subsection does not say.
  Other reading: JUST FALSE throughout.
  Licence: "Subject to subsection (1), nothing in this Part is to be construed as preventing any person from laying an information" (src:15099).
- **F26** (s 715.56; `s 715.56 the provision applies in respect of the person`)
  Reading taken: "Apply only in respect of persons who have been issued a warning or a referral": for a section from 715.57 to 715.6 and a person who has not been issued one, JUST FALSE (the text closes the list with "only"); for any other section, NOTHING. The text is in tension with sections 715.59(1)(c), 715.59(2) and 715.6(1)(c)(i), which speak of records of alternative measures (finding 12).
  Other reading: A reading that gives 715.59 and 715.6 their full work for alternative-measure records without a warning or referral.
  Licence: "Sections 715.57 to 715.6 apply only in respect of persons who have been issued a warning or a referral under section 715.47 or 715.48" (src:15132).
- **F27** (ccc25-seat.l4; every seat question)
  Reading taken: Where a layer-1 function takes the answer of another section as a MAYBE BOOLEAN seam input, the seat asks a plain yes or no and passes JUST TRUE or JUST FALSE; the one exception is "is the third party one of the persons section 2.2 names", whose "no" is passed as NOTHING, never as JUST FALSE, because section 2.2 itself answers NOTHING outside the persons it names.
  Other reading: Asking a three-way answer (yes, no, not covered) from the person.
  Licence: the brief's rule that the plain inputs are facts the person can state; the seam rule that a NOTHING must never become FALSE.
- **F28** (s 715.55(3); `s 715.55(3) the person may establish rules and practices for the convening and conducting of the conference`)
  Reading taken: "Other than for conferences convened or caused to be convened by a judge or justice" is the text's own carve-out out of the grant, so a conference convened by a judge or justice answers JUST FALSE (kept; the sweep lists "only if", "only where", "may not ... unless" and a list closed with "only" as closing words, and "other than" is not among them, so this is a judgment of mine, one of the "(other than X)" sites that the 2026-11-05 ruling decides case by case). It differs from F15 (s 715.6(2), "other than the identity", NOTHING) because here the text names a bearer and a class of cases that the section takes out of the grant.
  Other reading: NOTHING, a grant limited in its own wording and the case outside the limit (the Guide's line on grants); then 715.55(3) and 715.6(2) would read alike.
  Licence: "may establish rules and practices for the convening and conducting of conferences, other than for conferences convened or caused to be convened by a judge or justice" (src:15126).
- **F29** (s 715.43(3); `s 715.43(3) this Part continues to apply to the organization despite the deletion of the offence from the schedule`)
  Reading taken: When no deletion has been ordered, or the organization is not alleged to have committed the offence, the subsection does not speak: NOTHING. When a deletion has been ordered and no notice was sent before the order took effect, the answer is JUST FALSE (the text's own "if a notice ... was sent ... before the day").
  Other reading: JUST FALSE when no deletion has been ordered (a failed "If" on the provision's own question).
  Licence: "If the Governor in Council orders the deletion of an offence from the schedule to this Part, this Part continues to apply to an organization alleged to have committed that offence if a notice referred to in section 715.33 respecting that offence was sent to the organization before the day on which the order comes into force" (src:15033).
- **F30** (s 715.6(3); `s 715.6(3) the person may not disclose the information in a form that would reasonably be expected to identify the person to whom it relates`)
  Reading taken: The bar speaks only of a person to whom a record was made available under (1)(d)(i), and only of an identifying form: for a person to whom no record was made available, or for a form that would not identify, the answer is NOTHING.
  Other reading: JUST FALSE for a person to whom no record was made available (a failed "If" on a bar). The like site is s 715.32(3), a bar whose "if" gate (an offence under section 3 or 4 of the Corruption of Foreign Public Officials Act is alleged) answers JUST FALSE when it fails: there the "if" is a condition on the bar itself and the bar names its bearer (the prosecutor), while in s 715.6(3) the "If" describes the persons the subsection is about, so a person outside it is not covered.
  Licence: "If a record is made available for inspection to any person under subparagraph (1)(d)(i), that person ... may not disclose the information in any form that would reasonably be expected to identify the person to whom it relates" (src:15163).

### Rulings that govern these forks, word for word
Each is copied from the brief of this run; none is new.

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

> - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

> **A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).


### Name-test sweep of 2026-11-12
The sweep read every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorized", and every one named "it is lawful ...", against the three tests of `name-test-sweep.md`.
The layer-1 modules were written with the ruling already in force, so the 7 flips are in the first version of every file and no assertion had to be restated for them (nothing in this sweep changed an answer that an earlier assertion expected).
The seat questions that call a flipped function return its answer unchanged, and their cases in `ccc25-cases-seat.l4` expect NOTHING where the function answers NOTHING (for example the cases of `Under section 715.32(1)` and `Under section 715.42(2)`).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| ---: | ---: | ---: | ---: |
| 7 | 2 | 3 | 0 |

The counts are of gates, not of functions, so three functions appear in two columns: `s 715.3(2)` (its "if" gate flipped, F2.1; its "when authorized" gate listed, F10.2), `s 715.52(1)(b)` (its "if" gate flipped, F2.5; its "in the case where a charge is laid" gate listed, F10.3), and `s 715.6(3) the person may subsequently disclose` (its "if" gate flipped, F2.7; its closing "may not disclose ... in any form that would reasonably be expected to identify" kept JUST FALSE).
There are 7 functions flipped, 2 kept, 3 listed, and 9 distinct functions in all (7 + 2 + 3 less the 3 that appear twice).

**Group (i) is listed, not changed.** `s 715.39(2)`, `s 715.3(2)` (for its "when" gate) and `s 715.52(1)(b)` (for its "where" gate) answer JUST FALSE, as they did in the first version of their modules, and each has its own row (F10.1 to F10.3) with the other reading.
The seven flipped answers were in the first version too, so the sweep changed no answer and restated no assertion.

Flipped to NOTHING (a grant named "may" whose "if" gate failed; fork rows F2.1 to F2.7):
- `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf`
- `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement`
- `s 715.42(2) the court may decide not to publish the item`
- `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence`
- `s 715.52(1)(b) the court may dismiss the charge`
- `s 715.6(1) the information may be made available to the recipient`
- `s 715.6(3) the person may subsequently disclose the information contained in the record`

Kept JUST FALSE because the text closes the gate itself:
- `s 715.55(3) the person may establish rules and practices for the convening and conducting of the conference` ("other than for conferences convened or caused to be convened by a judge or justice"; F28: "other than" is not one of the closing words the sweep lists, so keeping JUST FALSE is my judgment and the other reading, NOTHING, is in the register)
- `s 715.6(3) the person may subsequently disclose the information contained in the record` ("but may not disclose the information in any form that would reasonably be expected to identify"; the same function is also in the flipped list, for its "if" gate)

Listed with a where/when/upon-kind gate (JUST FALSE as the Guide's ruling (b) and the 2026-11-05 ruling (c) give; the other reading is in the fork register; ASSUMED, NOT RULED):
- `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf`
- `s 715.39(2) the stayed proceedings may be recommenced without a new information or a new indictment`
- `s 715.52(1)(b) the court may dismiss the charge`

Listed as "entitled": none (no function of this part is named "entitled").

Outside the sweep: named "it is lawful": 0 scoped ("s N makes it lawful ...") and 0 unscoped and retitled; no function of this part has that name.

Not counted in the table, and kept JUST FALSE as the ruling says of a bar, a duty or the provision's own question:
- bars whose names carry "may" or "must not": `s 715.32(3) the prosecutor must not consider the matter`; `s 715.37(8) no other proceedings may be initiated against the organization for the same offence`; `s 715.6(3) the person may not disclose the information in a form that would reasonably be expected to identify the person to whom it relates`; `s 715.6(6) the record may not be introduced into evidence`; `s 715.5 alternative measures must not be used in respect of the person`;
- a duty whose name carries "may": `s 715.36(1) the prosecutor must take reasonable steps to inform any victim, or any third party acting on the victim’s behalf, that a remediation agreement may be entered into`.

Named for a grant but never answering JUST FALSE on a failed "if" (a scope limit or a discretion, so nothing to flip, NOTHING was already the answer): `s 715.34(3) the remediation agreement may include the term`; `s 715.41(1) the court may issue the order as it deems appropriate`; `s 715.42(4) the court may make its decision subject to the condition`; `s 715.53(b) the participant may freely withdraw from the restorative justice process at any time`; `s 715.54(1) a restorative justice process may be used at the stage`; `s 715.54(2) a restorative justice process may take the form`; `s 715.55(1) the person may, on request or on their own initiative, convene or cause to be convened a conference`; `s 715.58(1) the record may be kept by the police force`; `s 715.58(2) a peace officer may disclose the information to any person`; `s 715.58(3) a peace officer may disclose the information to an insurance company`; `s 715.59(1) the department or agency may keep records containing the information`; `s 715.59(2) the person or organization may keep records containing the information`; `s 715.6(2) the information may be made available to the recipient`; `s 715.6(4) the person may be given the information contained in the record and a copy of any part of the record`.
The two powers of section 715.43(1) and (2) are inert machinery and carry no function.


## Jural relations (ccc25)
Each rule where a party is named, the Hohfeld kind, and the parties.
A rule that names no party (the contents of the agreement, the bar on other proceedings, the suspension of a limitation period) states a requirement or an effect and has no row here.

| provision | rule | kind | bearer and holder |
| --- | --- | --- | --- |
| 715.3(2) | a third party may act for a victim when authorized | power of the court to authorize; privilege of the third party | the court over the third party and the victim |
| 715.32(1) | the prosecutor may negotiate a remediation agreement | privilege | the prosecutor; no claim in the organization |
| 715.32(2) | the prosecutor must consider the factors | duty | the prosecutor; no holder named |
| 715.32(3) | the prosecutor must not consider three matters | duty not to (SHANT) | the prosecutor |
| 715.33(1) | the prosecutor must give written notice | duty and claim | the prosecutor owes the organization |
| 715.33(2), 715.34(2) | admissions made in negotiation or under the agreement are inadmissible | immunity | the organization against the use of its statements |
| 715.35 | a candidate monitor must notify the prosecutor of a relationship | duty and claim | the candidate owes the prosecutor |
| 715.36(1) | the prosecutor must take reasonable steps to inform victims | duty and claim | the prosecutor owes the victim |
| 715.36(3) | the prosecutor must give the court a statement of reasons | duty and claim | the prosecutor owes the court |
| 715.37(1) | the prosecutor must apply for approval | duty | the prosecutor |
| 715.37(3), (4)(a) | the court must consider the listed matters and the victim impact statement | duty | the court |
| 715.37(4)(c) | the prosecutor's deemed duty to provide a copy of the statement | duty and claim | the prosecutor owes the organization or its counsel |
| 715.37(6) | the court must approve the agreement | duty and claim | the court owes the prosecutor and the organization |
| 715.37(7) | the prosecutor must direct the clerk; the clerk must make the entry immediately | duty and duty | the prosecutor, then the clerk |
| 715.37(8) | no other proceedings may be initiated for the same offence | immunity and disability | the organization is immune; any prosecutor lacks the power |
| 715.38, 715.39(1), 715.4(1) | the court must approve a modification, terminate, declare the terms met | duty and claim | the court owes the prosecutor |
| 715.39(2) | the prosecutor may recommence by notice to the clerk | power and liability | the prosecutor's power; the organization's liability |
| 715.4(2) | the order stays the proceedings and no other may be initiated | immunity | the organization |
| 715.41(1) | the prosecutor must apply after the deadline; the court may issue an order | duty; power | the prosecutor; the court |
| 715.42(1), (5) | the court must publish; must review on application and publish | duty and claim | the court owes any person who applies |
| 715.42(2), (4) | the court may decide not to publish and may impose conditions | power | the court |
| 715.42(3) | the court must consider six factors | duty | the court |
| 715.43(3) | Part XXII.1 continues to apply after deletion | liability (the organization's) | the organization |
| 715.47(1), 715.48(1) | the police officer, the prosecutor, must consider a warning, referral or no action | duty without a correlative claim (ss 715.47(2) and 715.48(2) deny invalidity for a failure) | the police officer; the prosecutor |
| 715.49 | alternative measures may be used if the conditions are met | privilege (power) of the authority | the person who decides |
| 715.5 | alternative measures must not be used for a person who denies or wants the court | disability and immunity | the authority lacks the power; the person is immune |
| 715.51 | an admission made as a condition of an alternative measure is inadmissible | immunity | the person who made it |
| 715.52(1)(a), (b) | the court must dismiss on total compliance; may dismiss on partial compliance | duty and claim; power | the court and the accused |
| 715.53(b) | a participant may freely withdraw, and must freely consent | privilege; claim to a free choice | the participant |
| 715.55(1), (3) | a judge or justice may convene a conference; the Attorney General may establish rules | power | the judge, the justice, the Attorney General |
| 715.57 | the police officer is to keep a record | duty | the police officer |
| 715.58(1), (2), (3), 715.59, 715.6(1), (2), (4) | records may be kept and made available | privilege | the keeper of the record; the recipient has no claim |
| 715.6(3) | the recipient may not disclose in an identifying form | duty and claim | the recipient owes the person identified |
| 715.6(5), (6) | the evidence and the record are inadmissible | immunity and disability | the individual; any court lacks the power to receive them |

## Marginal readings for a lawyer (ccc25)
The readings most likely to change an answer, each with the other reading, taken from the fork register; each of F2.1 to F2.7 is one line.

- **F1** (s 715.3(2)): "A third party not referred to in section 2.2" is read as: the keel's composed answer for section 2.2 is not JUST TRUE for this person, so an answer of NOTHING or JUST FALSE from section 2.2 both leave the person "not referred to". Other reading: "Referred to" covers every person section 2.2(1) mentions by relationship, including one section 2.2(2) then bars; such a person would be outside this subsection too.
- **F2.1** (s 715.3(2)): NOTHING when the court has authorized the third party but neither the victim requests it nor the prosecutor deems it appropriate (an "if" gate on a grant named "may", the coordinator's name-test ruling of 2026-11-12). Other reading: JUST FALSE, a failed "if" read as the text's own no ("may not").
- **F2.2** (s 715.32(1)): NOTHING when any of conditions (a) to (d) is unmet, or the body is not an organization of this Part, or the offence is not listed (a grant named "may" with an "if" gate not closed by "only if"). Other reading: JUST FALSE, a failed "if" read as the text's own no.
- **F2.3** (s 715.42(2)): NOTHING when the court is not satisfied that non-publication is necessary for the proper administration of justice. Other reading: JUST FALSE, a failed "if" read as the text's own no.
- **F2.4** (s 715.49): NOTHING when any of conditions (a) to (g) is unmet. Other reading: JUST FALSE, a failed "if" read as the text's own no (alternative measures may not be used).
- **F2.5** (s 715.52(1)(b)): NOTHING when the court is not satisfied of partial compliance or does not think the prosecution unfair. Other reading: JUST FALSE, a failed "if" read as the text's own no. The function also carries a "where" gate (no charge laid: JUST FALSE, listed as F10.3).
- **F2.6** (s 715.6(1)): NOTHING for a recipient under paragraph (d) when the judge is satisfied of neither (i) nor (ii). Other reading: JUST FALSE, a failed "if" read as the text's own no.
- **F2.7** (s 715.6(3)): NOTHING when the record was not made available for inspection under subparagraph (1)(d)(i). JUST FALSE is kept where the form would reasonably be expected to identify the person, because the text closes that gate with "may not". Other reading: JUST FALSE for the first case too.
- **F3** (ss 715.33(2), 715.34(2)): Once the exception is met (the statement is in the statement of facts or admission of responsibility, and the agreement is approved) the answer is JUST FALSE: the text itself carves it out of the bar. Other reading: NOTHING: the subsection is silent on whether such a statement is admissible.
- **F4** (ss 715.33(1), 715.34(1)): A "must include" requirement that is not met is JUST FALSE: the text states the requirement in its own words. Other reading: NOTHING: a bare "must" not done leaves the text silent on the consequence.
- **F5** (s 715.34(1)(g)): "An indication of any reparations ... or a statement by the prosecutor of the reasons why reparations ... are not appropriate ... and an indication of any measure required in lieu" is read as: reparations, OR (the statement AND the measure in lieu). Other reading: (Reparations OR the statement) AND the measure in lieu, so a measure is always required.
- **F6** (ss 715.47, 715.57): "Police officer" is read as the core's `a peace officer` (section 2 defines "peace officer" and not "police officer"; NEEDS-CORE.md asks for a constructor). Other reading: A police officer who is not a peace officer: nothing in the sources decides.
- **F7** (s 715.34(1)(e), (h)): Paragraph (e) is met when the agreement identifies no property, benefit or advantage, because the obligation attaches only to property "identified in the agreement"; paragraph (h) is met when every offence in the agreement is an offence under section 3 or 4 of the Corruption of Foreign Public Officials Act. Other reading: (e) requires some statement even where no property is identified; (h) is per offence, so an agreement that covers both kinds of offence needs a surcharge term for the other kind (the function takes one flag for "every offence").
- **F11** (ss 715.39(3), 715.6(6)): "Within one year after the order is made" ends on the first anniversary (the same date one year on); "more than two years after the end of the period" begins the day after the second anniversary. The library's `add years` clamps 29 February to 28 February, so a period that starts on 29 February 2024 has its second anniversary on 28 February 2026. Other reading: The year ends the day before the anniversary, or is counted as 365 or 366 days from the day after; for 29 February the anniversary is 1 March.
- **F12** (s 715.6(6)): Before the second anniversary the bar does not apply: JUST FALSE (a "more than two years after" time gate on a bar, ruling (a) of 2026-11-05 on periods). Other reading: NOTHING: the sentence does not say what is permitted before two years.
- **F13** (s 715.54(3)): When the restorative justice process is not used as an alternative measure the answer for sections 715.49 to 715.52 is JUST FALSE (a "when" gate, ruling (c) of 2026-11-05). Other reading: NOTHING: the subsection opens "For greater certainty" and may be read as declaratory only, saying nothing about other uses. Listed for a lawyer.
- **F15** (s 715.6(2)): For the identity of the person the answer is NOTHING: "other than the identity" limits the grant and the text does not say the identity may not be made available. Other reading: JUST FALSE for the identity.
- **F18** (s 715.42(1)): "Subject to subsection (2)" takes the agreement and the orders and reasons out of the duty to publish when the court has decided not to publish; paragraph (c), a decision under (2) or (5), is published even then, because (2) lets the court withhold only the agreement and the paragraph (1)(b) orders and reasons. Other reading: A decision under (2) can itself be withheld.
- **F26** (s 715.56): "Apply only in respect of persons who have been issued a warning or a referral": for a section from 715.57 to 715.6 and a person who has not been issued one, JUST FALSE (the text closes the list with "only"); for any other section, NOTHING. The text is in tension with sections 715.59(1)(c), 715.59(2) and 715.6(1)(c)(i), which speak of records of alternative measures (finding 12). Other reading: A reading that gives 715.59 and 715.6 their full work for alternative-measure records without a warning or referral.
- **F28** (s 715.55(3)): "Other than for conferences convened or caused to be convened by a judge or justice" is the text's own carve-out out of the grant, so a conference convened by a judge or justice answers JUST FALSE (kept; the sweep lists "only if", "only where", "may not ... unless" and a list closed with "only" as closing words, and "other than" is not among them, so this is a judgment of mine, one of the "(other than X)" sites that the 2026-11-05 ruling decides case by case). It differs from F15 (s 715.6(2), "other than the identity", NOTHING) because here the text names a bearer and a class of cases that the section takes out of the grant. Other reading: NOTHING, a grant limited in its own wording and the case outside the limit (the Guide's line on grants); then 715.55(3) and 715.6(2) would read alike.

### Reading a result: FALSE and NOTHING (ccc25)
This is the rule of 2026-10-29 (assumed, not ruled by a lawyer) with the rulings of 2026-11-04, 2026-11-05 and 2026-11-12 that settle parts of it; the rulings are copied word for word in the fork register.
`JUST TRUE` means the facts bring the case within the rule on the text's own words.
`JUST FALSE` means the text says no in its own words: a "means" definition, a condition the text introduces with "if", "where", "when", "while", "until" or "except", a list closed with "only", a flat negative ("does not", "may not").
`NOTHING` means not covered: the text lists without closing the list, says "includes" or "among other things", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit; a grant named "may" whose "if" gate fails is NOTHING.
A caller must never turn `NOTHING` into `FALSE`.
Two readings are open for a lawyer and are not decided here: a "may" whose gate is "where", "when" or "upon" (F10.1 to F10.3), and an "entitled" function (none here).
Every `JUST FALSE` and `NOTHING` branch of the layer-1 modules carries a comment that begins `FALSE-kind` or `NOTHING-kind` and, where the branch rests on the text's words, quotes them; `work/lint.py` found all 57 `JUST FALSE` and 75 `NOTHING` branches tagged and all 141 quotation fragments in the text.

## Seams (ccc25)
Each answer taken from another section or another part is an input named for the section it comes from, typed `MAYBE BOOLEAN`, as PLAN.md names them; the seat asks the person a plain yes or no where it can (F27).

| asking section | answering section | input | answer type | what the rule does with NOTHING |
| --- | --- | --- | --- | --- |
| s 715.3(1) "court" | s 2 "superior court of criminal jurisdiction" (keel) | `s 2 superior court of criminal jurisdiction: the body is one` | MAYBE BOOLEAN | carried through |
| s 715.3(1) "offence" | the Schedule to Part XXII.1 (ccc29, lines 17351-17388) | `Schedule to Part XXII.1 the offence is listed` | MAYBE BOOLEAN | carried through; used by "remediation agreement" and s 715.32(1) |
| s 715.3(1) "organization" | s 2 "organization" (keel) | `s 2 organization: the body is an organization` | MAYBE BOOLEAN | carried through; the three exclusions answer first |
| s 715.3(1) "victim" | s 2 "victim" (keel) | `s 2 victim: the person is a victim` | MAYBE BOOLEAN | carried through; the extension for a section 3 or 4 offence of the Corruption of Foreign Public Officials Act answers first (F23) |
| s 715.3(2) | s 2.2 composed (keel) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN | anything other than JUST TRUE counts as "not referred to" (F1) |
| s 715.37(4) | ss 722 to 722.2 | none: the sections are tested against `Provision of the Code` (seam rule R1) | the core record | n/a |

Seams the plan lacks, or places differently (findings 2, 3 and 15):
- Section 715.6(6) turns on "the purposes set out in paragraph 721(3)(c)"; that is another part's range, and the function takes a plain BOOLEAN, `the introduction into evidence is for the purposes set out in paragraph 721(3)(c)`, which could be a MAYBE BOOLEAN input named for the section once the answering part is known.
- Section 715.49(g), "the prosecution of the offence is not in any way barred at law", is a plain BOOLEAN input: it points at the whole law, not at a section of the sources.
- Offences and sections of other Acts (sections 3 and 4 of the Corruption of Foreign Public Officials Act; paragraph 4(1)(b.2) of the Seized Property Management Act) are plain BOOLEAN inputs or quoted words, never looked up.

## What the text turns out to say (ccc25)
Numbered findings, each read from the text of the range.

1. **The range is two Parts, not "miscarriages of justice and compensation".** The lead's task message labels lines 14872-15170 with that phrase; the text holds Part XXII.1 Remediation Agreements and Part XXII.2 Alternative Measures and Restorative Justice Processes (the Part headings are at lines 14872 and 15035). The sections encoded are ss 715.3 to 715.6.
2. **The plan puts the section 2.2 seam on the wrong section.** PLAN.md's ccc25 row names s 715.37 for the section 2.2 answer; the words "a third party not referred to in section 2.2" are in s 715.3(2) (line 14881), and that is where the input is taken. Section 715.37(4) names ss 722 to 722.2, not 2.2.
3. **Only one of the Schedule's named sections turns on the Schedule's contents.** The plan's seam row for the Schedule names ss 715.32(2), 715.43(2) and (3), which is also what the Schedule's own heading says ("Section 715.3 and subsections 715.32(2) and 715.43(2) and (3)", line 17351). Section 715.3(1) "offence" is the rule that turns on it ("any offence listed in the schedule", line 14876), so it is where the input is taken; s 715.32(2)(h) (line 14905) names offences "not listed in the schedule" only as a factor to consider; s 715.43(2) (line 15031) is a power to amend the schedule, inert machinery; s 715.43(3) turns on a deletion order and a notice date, not on whether an offence is listed.
4. **A remediation agreement is only for an organization.** "Organization" is section 2's definition without a public body, trade union or municipality (line 14877), and "remediation agreement" is an agreement "between an organization accused of having committed an offence and a prosecutor" (line 14878). An individual accused never meets Part XXII.1, so the seat questions of that Part ask about "my organization".
5. **The victim surcharge has no figure for a Corruption of Foreign Public Officials Act offence.** Section 715.34(1)(h) excludes an offence under section 3 or 4 of that Act, and s 715.37(5) states the 30% "for the purpose of paragraph 715.34(1)(h)"; the function answers NOTHING for that offence (F17).
6. **The stay needs two steps.** Section 715.37(7) has the prosecutor direct the clerk "as soon as practicable" after approval, and the entry "must be made immediately"; the proceedings are stayed "after which time", so the function that asks whether they are stayed answers JUST FALSE until the entry is made.
7. **Notice of recommencement has a last day that is the earlier of two days.** Section 715.39(3) deems the proceedings never commenced if no notice is given within one year after the order, or before the time for commencing expires, "whichever is earlier"; the time for commencing is outside the sources, so it is an input date.
8. **Publication has a hole in it.** Section 715.42(1) is "Subject to subsection (2)", but (2) lets the court withhold only the agreement and the paragraph (1)(b) orders and reasons, so a decision under (2) or (5), paragraph (1)(c), is always published (F18).
9. **A person under 18 is outside "alternative measures".** Section 715.44 defines the term for a person "18 years of age or older"; for a younger person the definition says no. Any regime for young persons is not in the sources.
10. **The grant and the bar of Part XXII.2 are independent.** Section 715.49 lets alternative measures be used "if" seven conditions are met; s 715.5 bars them for a person who denies involvement or wants the court to deal with the charge. A person who fails a condition of 715.49 is not "barred" by 715.5 (it answers NOTHING for them), and a person caught by 715.5 is barred whatever 715.49 says.
11. **Dismissal after alternative measures is a duty for total compliance and a discretion for partial.** Section 715.52(1)(a) says "must dismiss" for total compliance, (b) says "may dismiss" for partial compliance with an unfairness test; the use of alternative measures is "not a bar" to the charge itself.
12. **Section 715.56 sits uneasily with sections 715.59 and 715.6.** It says ss 715.57 to 715.6 "apply only in respect of persons who have been issued a warning or a referral under section 715.47 or 715.48", yet 715.59(1)(c) and 715.59(2) speak of records of information obtained "as a result of the use of alternative measures" (lines 15145 and 15147), and 715.6(1)(c)(i) gives access to those "engaged in the administration of alternative measures in respect of the person" (line 15155). Read literally, those provisions do not apply to a person who was dealt with by an alternative measure without a warning or referral (F26). Whether Parliament meant that is for a lawyer.
13. **The two-year period in s 715.6(6) runs from the end of the alternative measure,** not from the warning or the record: "more than two years after the end of the period during which the alternative measure was applied".
14. **Two different words for the officer.** Sections 715.47 and 715.57 say "police officer"; s 715.58(2) says "peace officer". Section 2 defines "peace officer" only (F6).
15. **Where a rule needs another provision's answer the text uses a number.** Sections 715.37(4), 715.54(3) and 715.56 name sections by number, so they are tested against `Provision of the Code` (F16); the decimal order puts section 715.5 between 715.49 and 715.51 and section 715.6 after 715.59.

## What the stable binary does not accept (ccc25)
Measured on both stable builds (1.6.110 and 1.6.109) on 2026-11-16:
- `a AND b AND (k NOT EQUALS x)` is a parse error on both builds (`parse/unexpected-AND`, reported at the second `AND`); `a AND b AND (NOT (k EQUALS x))` parses on both. No infix `NOT EQUALS` is used in these modules: a negated equality is written `NOT (k EQUALS x)`.
- A `DEONTIC` value cannot be compared in an `#ASSERT`; every duty and permission of this part is therefore also a decision function that is asserted, and each regulative rule is run by `#TRACE` on both builds with the outcome written beside it as `-- EXPECT FULFILLED|BREACHED|STANDING`.
- `l4 run` exits 0 on a file whose only `#ASSERT` fails (`#ASSERT 1 EQUALS 2`): exit status 0 and three lines naming the failure on both 1.6.110 and 1.6.109, measured 2026-11-17. Every result in this file was therefore read from `check.sh`'s counts and not from an exit status.
Constructs the brief rules out (`REFUSE`, `BECAUSE` except in `LEST BREACH ... BECAUSE`, `TYPICALLY` on fields, opaque `DECLARE`, `WAIT UNTIL`, a self-defined `YMD`) were not used and not tested here. Every other construct used was accepted by both builds with the same counts.
Not seen by `check.sh`, so compared by a separate run: a `#TRACE` outcome. `work/traces.py` ran all 68 on both builds with `JL4_LIBRARY_PATH` unset, matched each to its expectation, and failed on any file whose run produced fewer evaluations than it has `#TRACE`s (all 68 evaluations occurred on each build).

## The seat (ccc25)
Seat: a person who is, or may be, accused of an offence. For Part XXII.1 that person is an organization accused of a listed offence (finding 4); for Part XXII.2 it is any person alleged to have committed an offence.
There is no seat for an official: the duties of the prosecutor, the court and the clerk appear in the seat only for what they mean to the accused (must the prosecutor give us notice, must the court approve, are the proceedings stayed).
Each question takes plain inputs, one per fact the person can state, each with an `@desc` worded as the person would be asked; it builds the layer-1 function's inputs and calls the function, and restates no rule.
Questions begin "Under section N," and are grouped under two `§` headings in the text's order.
The 54 questions and the function each calls:

| section | question (the @export text) | layer-1 function it calls |
| --- | --- | --- |
| 715.3(1) | Under section 715.3(1), is my body an organization for the purposes of Part XXII.1 (remediation agreements)? | `s 715.3(1) organization` |
| 715.3(1) | Under section 715.3(1), is this agreement a remediation agreement? | `s 715.3(1) remediation agreement` |
| 715.3(1) | Under section 715.3(1), is this person a victim for the purposes of Part XXII.1? | `s 715.3(1) victim` |
| 715.3(2) | Under section 715.3(2), may a third party who is not one of the persons named in section 2.2 act on the victim’s behalf? | `s 715.3(2) a third party not referred to in section 2.2 may act on the victim’s behalf` |
| 715.32(1) | Under section 715.32(1), may the prosecutor enter into negotiations for a remediation agreement with my organization? | `s 715.32(1) the prosecutor may enter into negotiations for a remediation agreement` |
| 715.32(3) | Under section 715.32(3), does this subsection bar the prosecutor from considering this matter? | `s 715.32(3) the prosecutor must not consider the matter` |
| 715.33(1) | Under section 715.33(1), must the prosecutor give my organization written notice of the offer to enter into negotiations? | `s 715.33(1) the prosecutor must give the organization written notice of the offer to enter into negotiations` |
| 715.33(1) | Under section 715.33(1), does the notice I received meet the requirement that it be written and include each of paragraphs (a) to (j)? | `s 715.33(1) the notice meets the requirement that it be written and include each of paragraphs (a) to (j)` |
| 715.33(2) | Under section 715.33(2), is this admission or statement accepting responsibility, made by my organization during the negotiations, inadmissible in evidence against it? | `s 715.33(2) the admission is inadmissible in evidence against the organization` |
| 715.34(1) | Under section 715.34(1), does the remediation agreement include everything that it must include? | `s 715.34(1) the remediation agreement includes everything that it must include` |
| 715.34(2) | Under section 715.34(2), is this admission or statement accepting responsibility, made by my organization as a result of the agreement, inadmissible in evidence against it? | `s 715.34(2) the admission is inadmissible in evidence against the organization` |
| 715.34(3) | Under section 715.34(3), may the remediation agreement include this term? | `s 715.34(3) the remediation agreement may include the term` |
| 715.35 | Under section 715.35, must a candidate for appointment as an independent monitor notify the prosecutor in writing of a relationship? | `s 715.35 the candidate must notify the prosecutor in writing of the relationship` |
| 715.36(1) | Under section 715.36(1), must the prosecutor take reasonable steps to inform any victim that a remediation agreement may be entered into? | `s 715.36(1) the prosecutor must take reasonable steps to inform any victim, or any third party acting on the victim’s behalf, that a remediation agreement may be entered into` |
| 715.37(1) | Under section 715.37(1), must the prosecutor apply to the court in writing for an order approving the agreement? | `s 715.37(1) the prosecutor must apply to the court in writing for an order approving the agreement` |
| 715.37(5) | Under section 715.37(5), what is the amount of the victim surcharge, in dollars? | `s 715.37(5) the amount of the victim surcharge in dollars` |
| 715.37(6) | Under section 715.37(6), must the court, by order, approve the agreement? | `s 715.37(6) the court must, by order, approve the agreement` |
| 715.37(7) | Under section 715.37(7), are the proceedings against my organization in respect of the offence stayed? | `s 715.37(7) the proceedings against the organization in respect of the offence are stayed` |
| 715.37(8) | Under section 715.37(8), does this subsection bar the initiation of other proceedings against my organization for the same offence? | `s 715.37(8) no other proceedings may be initiated against the organization for the same offence` |
| 715.37(9) | Under section 715.37(9), is the running of the limitation period suspended? | `s 715.37(9) the running of the limitation period is suspended` |
| 715.38 | Under section 715.38, must the court, by order, approve a modification to the remediation agreement? | `s 715.38 the court must, by order, approve the modification to the remediation agreement` |
| 715.39(1) | Under section 715.39(1), must the court, by order, terminate the agreement? | `s 715.39(1) the court must, by order, terminate the agreement` |
| 715.39(2) | Under section 715.39(2), may the stayed proceedings be recommenced without a new information or a new indictment? | `s 715.39(2) the stayed proceedings may be recommenced without a new information or a new indictment` |
| 715.39(3) | Under section 715.39(3), what is the last day on which notice of recommencement can be given to the clerk? | `s 715.39(3) the last day on which notice of recommencement can be given to the clerk` |
| 715.39(3) | Under section 715.39(3), are the proceedings deemed never to have been commenced? | `s 715.39(3) the proceedings are deemed never to have been commenced` |
| 715.4(1) | Under section 715.4(1), must the court, by order, declare that the terms of the agreement were met? | `s 715.4(1) the court must, by order, declare that the terms of the agreement were met` |
| 715.41(2) | Under section 715.41(2), is the agreement deemed to remain in force? | `s 715.41(2) the agreement is deemed to remain in force` |
| 715.42(2) | Under section 715.42(2), may the court decide not to publish this item? | `s 715.42(2) the court may decide not to publish the item` |
| 715.43(3) | Under section 715.43(3), does Part XXII.1 continue to apply to my organization despite the deletion of the offence from the schedule? | `s 715.43(3) this Part continues to apply to the organization despite the deletion of the offence from the schedule` |
| 715.44 | Under section 715.44, are these measures alternative measures? | `s 715.44 alternative measures` |
| 715.44 | Under section 715.44, is this process a restorative justice process? | `s 715.44 restorative justice process` |
| 715.47(1) | Under section 715.47(1), must the police officer consider this option instead of proceeding with the laying of an information against me? | `s 715.47(1) the police officer must consider the option instead of proceeding with the laying of an information` |
| 715.47(2) | Under section 715.47(2), does the police officer’s failure to consider the options invalidate the subsequent charges against me? | `s 715.47(2) the failure of the police officer to consider the options invalidates the subsequent charges` |
| 715.48(1) | Under section 715.48(1), must the prosecutor consider this option before commencing or continuing judicial proceedings against me? | `s 715.48(1) the prosecutor must consider the option before commencing or continuing judicial proceedings` |
| 715.48(2) | Under section 715.48(2), does the prosecutor’s failure to consider the options invalidate the proceedings against me? | `s 715.48(2) the failure of the prosecutor to consider the options invalidates the proceedings` |
| 715.49 | Under section 715.49, may alternative measures be used in my case? | `s 715.49 alternative measures may be used in respect of the person alleged to have committed the offence` |
| 715.5 | Under section 715.5, are alternative measures barred in my case? | `s 715.5 alternative measures must not be used in respect of the person` |
| 715.51 | Under section 715.51, is what I admitted as a condition of being dealt with by an alternative measure inadmissible in evidence against me? | `s 715.51 the admission is inadmissible in evidence against the person` |
| 715.52(1) | Under section 715.52(1), is my use of alternative measures a bar to proceedings against me under the Criminal Code? | `s 715.52(1) the use of alternative measures is a bar to proceedings against the person under this Act` |
| 715.52(1)(a) | Under section 715.52(1)(a), must the court dismiss the charge against me? | `s 715.52(1)(a) the court must dismiss the charge` |
| 715.52(1)(b) | Under section 715.52(1)(b), may the court dismiss the charge against me? | `s 715.52(1)(b) the court may dismiss the charge` |
| 715.52(2) | Under section 715.52(2), is Part XXII.2 to be construed as preventing this act? | `s 715.52(2) this Part is to be construed as preventing the person from doing the act` |
| 715.53(b) | Under section 715.53(b), may I freely withdraw from the restorative justice process at any time? | `s 715.53(b) the participant may freely withdraw from the restorative justice process at any time` |
| 715.54(1) | Under section 715.54(1), may a restorative justice process be used at this stage? | `s 715.54(1) a restorative justice process may be used at the stage` |
| 715.54(3) | Under section 715.54(3), do sections 715.49 to 715.52 apply to the restorative justice process (name the section you mean)? | `s 715.54(3) the provision applies to the restorative justice process` |
| 715.55(1) | Under section 715.55(1), does this person participate in the conference? | `s 715.55(1) the person participates in the conference` |
| 715.55(4) | Under section 715.55(4), must the conference be convened and conducted in accordance with the rules and practices of the province or territory? | `s 715.55(4) the conference must be convened and conducted in accordance with the rules and practices` |
| 715.56 | Under section 715.56, do sections 715.57 to 715.6 apply in respect of me (name the section you mean)? | `s 715.56 the provision applies in respect of the person` |
| 715.57 | Under section 715.57, is the police officer to keep a record of the warning issued or referral made? | `s 715.57 the police officer is to keep a record of the warning issued or referral made, including the identity of the person warned or referred` |
| 715.58(2) | Under section 715.58(2), may a peace officer disclose this information to any person? | `s 715.58(2) a peace officer may disclose the information to any person` |
| 715.6(1) | Under section 715.6(1), may the information in the record be made available to this recipient? | `s 715.6(1) the information may be made available to the recipient` |
| 715.6(3) | Under section 715.6(3), is the person barred from disclosing the information in a form that would reasonably be expected to identify me? | `s 715.6(3) the person may not disclose the information in a form that would reasonably be expected to identify the person to whom it relates` |
| 715.6(5) | Under section 715.6(5), is this evidence inadmissible? | `s 715.6(5) the evidence is inadmissible` |
| 715.6(6) | Under section 715.6(6), does this subsection bar the introduction of the record into evidence? | `s 715.6(6) the record may not be introduced into evidence` |

### Direction audit and the second audit pass (2026-11-12 task 1)
First direction audit: every question was read for direction and subject against the function it calls (a "may" title over a permission, a "must" title over a duty, a title that names a bar over a bar). None differed in direction (a permission titled over a bar, or the reverse) and none in subject ("must" against "have").
Second pass, against the BODY of each function and not against its title: 54 questions read, 7 retitled, 47 read and left.
Criteria used are the four of the instruction: retitle only for a different limb, route or scope than the body answers; a premise, qualifier or consequence the function does not compute; a wrong polarity or modal; a different type of answer.
All seven fall under the first criterion (a different limb, route or scope than the body answers): 715.33(2) and 715.34(2) asked about anything the organization said where the function answers for an admission, confession or statement accepting responsibility; 715.32(3), 715.37(8) and 715.6(6) asked a general "is it barred" over one bar; 715.54(3) and 715.56 asked about "this section" where the function answers for a range of sections. None fell under the second, third or fourth criteria.

| section | was | now |
| --- | --- | --- |
| 715.33(2) | Under section 715.33(2), is what my organization said during the negotiations inadmissible in evidence against it? | Under section 715.33(2), is this admission or statement accepting responsibility, made by my organization during the negotiations, inadmissible in evidence against it? |
| 715.34(2) | Under section 715.34(2), is what my organization said as a result of the agreement inadmissible in evidence against it? | Under section 715.34(2), is this admission or statement accepting responsibility, made by my organization as a result of the agreement, inadmissible in evidence against it? |
| 715.32(3) | Under section 715.32(3), is the prosecutor barred from considering this matter? | Under section 715.32(3), does this subsection bar the prosecutor from considering this matter? |
| 715.37(8) | Under section 715.37(8), is the initiation of other proceedings against my organization for the same offence barred? | Under section 715.37(8), does this subsection bar the initiation of other proceedings against my organization for the same offence? |
| 715.6(6) | Under section 715.6(6), is the introduction of the record into evidence barred? | Under section 715.6(6), does this subsection bar the introduction of the record into evidence? |
| 715.54(3) | Under section 715.54(3), does this section of the Code apply to the restorative justice process? | Under section 715.54(3), do sections 715.49 to 715.52 apply to the restorative justice process (name the section you mean)? |
| 715.56 | Under section 715.56, does this section of the Code apply in respect of me? | Under section 715.56, do sections 715.57 to 715.6 apply in respect of me (name the section you mean)? |

Why each was changed: the two admissibility titles asked about "what my organization said" where the function answers only for an admission, confession or statement accepting responsibility (the function's own name says "the admission"); the three "barred" titles asked a general question over one subsection's bar, so that a `JUST FALSE` would be misread as "may proceed" (for 715.32(3) the answer is JUST FALSE when no offence under section 3 or 4 of the Corruption of Foreign Public Officials Act is alleged; for 715.37(8) when the agreement is not in force; for 715.6(6) within two years of the end of the period or for the purposes of paragraph 721(3)(c)); the two "does this section of the Code apply" titles asked about every section where the function answers only for sections 715.49 to 715.52 (s 715.54(3)) or 715.57 to 715.6 (s 715.56) and NOTHING for any other.
Read and left, with the cases where I hesitated: `Under section 715.6(5), is this evidence inadmissible?` restates the function's own name (`the evidence is inadmissible`), the purpose limit is an input of the function, and the answer outside it is NOTHING, never JUST FALSE; `Under section 715.5, are alternative measures barred in my case?` and `Under section 715.6(3), is the person barred from disclosing ...?` ask over bars that answer only JUST TRUE or NOTHING, so "barred" cannot be misread as "free"; `Under section 715.3(2), may a third party who is not one of the persons named in section 2.2 act ...?` carries a status that the function tests as an input and carries in its own name; `Under section 715.32(1), may the prosecutor enter into negotiations ... with my organization?` carries "my organization", a status the function tests as an input; `Under section 715.39(3), what is the last day on which notice of recommencement can be given to the clerk?` restates the function's own name and the answer is a date, as the title asks; `Under section 715.37(5), what is the amount of the victim surcharge, in dollars?` answers a number, as the title asks, and NOTHING for the one offence the text excludes; `Under section 715.43(3), does Part XXII.1 continue to apply to my organization despite the deletion of the offence from the schedule?` carries "my organization", a status that the function tests as a separate input.
The other 39 differ from their function's name only in wording or in a status the function tests as a separate input.
Assertions restated: 21 assertions of `ccc25-cases-seat.l4` carry the new names and a `-- RECONCILED 2026-11-12: was <the original assertion>` comment in place; their expected values are unchanged.

## What check.sh prints (ccc25)
Baseline before any file of this part was written (3 modules of the keel, no assertion):
```
TOTAL (3 modules)                              0         0       0        0           |      0         0       0        0
```
After the last edit, `L4=.../l4-main-110 L4_MAIN=.../l4-main-109 ./check.sh` with `JL4_LIBRARY_PATH` unset; exit status 0, captured without a pipe:
```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc25-alternative-measures.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc25-cases-seat.l4                            0       147       0        0         0 |      0       147       0        0  same
ccc25-remediation-approval.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc25-remediation-negotiation.l4               0         0       0        0         0 |      0         0       0        0  same
ccc25-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc25-tests-alternative-measures.l4            0       196       0        0         0 |      0       196       0        0  same
ccc25-tests-remediation-approval.l4            0       148       0        0         0 |      0       148       0        0  same
ccc25-tests-remediation-negotiation.l4         0       135       0        0         0 |      0       135       0        0  same
TOTAL (11 modules)                             0       626       0        0           |      0       626       0        0
```
The 626 assertions written (479 in the three layer-1 tests files, 147 in the seat cases) equal the 626 satisfied; no module is expected to fail.
The TOTAL before the follow-up tasks (the first pass, with the first-pass seat titles) was 11 modules, 623 satisfied, 0 failed, 0 refused, 0 errors; the follow-up tasks added three section-716 boundary cases for `s 715.56` (two in the tests file, one in the seat cases; section 716 is above 715.6, so the answer is NOTHING), which is the whole difference from 623 to 626, and the retitles moved no outcome.
Also run, all after the last edit:
- `srcrefs.py check --refs` and `--strict`, each over all eight `ccc25-*.l4` files: 243 `src:` lines, 119 runs, 149 locators, 0 problems in each.
- `work/lint.py` over the three layer-1 modules: 57 `JUST FALSE` branches, 75 `NOTHING` branches, 141 quotation fragments, all found in the text, 0 problems; a control (a copy of one module with a made-up phrase put inside one quotation) gave 1 problem, rerun 2026-11-17 after the last edit.
- `work/traces.py` over the three tests files (the seat cases file has no `#TRACE`): 68 `#TRACE`, 68 evaluations on each build, 0 mismatches.
- `DiagnosticSeverity_Warning` and `_Error` counted over every `ccc25-*` file on both builds: 0 and 0.

## PLAN against the brief; about the text (ccc25)
- PLAN.md says a part gets only `ccc-core.l4`; the brief says the keel's `ccc-core.l4` and `ccc-definitions.l4` sit in the folder and may be imported. The layer-1 modules import only `ccc-core` and take section 2 answers as inputs, as the plan says; the seat imports `ccc-definitions` to call `s 2 organization`.
- PLAN.md has the seam rows under "### ccc25" of its section 6 (the brief calls them section 8 of the plan).
- The seat questions of Part XXII.1 are asked from an organization's seat, not an individual's, because the Part applies to organizations only (finding 4); the brief's seat is "a person who is, or may be, accused", and an organization is one.
- The text is the Justice Laws Website consolidation as rendered by a converter script; it is not the official text, and the French version, which is equally authoritative, is not among the sources.
