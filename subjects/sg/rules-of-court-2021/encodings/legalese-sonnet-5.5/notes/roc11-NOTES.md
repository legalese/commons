# NOTES (roc11): Rules of Court 2021, Orders 57 to 63

Singapore, Rules of Court 2021 (G.N. No. S 914/2021), version as at 5 November 2026, lines 6796 to 7399 of `SCJA1969-S914-2021.txt`.
Order 57 Personal Data Protection Act 2012; Order 58 hire-purchase; Order 59 proceedings by and against Government; Order 60 reciprocal enforcement of judgments; Order 61 Securities and Futures Act civil liability actions; Order 62 civil penalty actions; Order 63 disgorgement against a third party.
`work/` is this run's scratch folder beside the deposit (the scripts that made the tables below, and the check logs); it is not part of the shipped folder, so every table below is inlined here.
Built for the `main` row with `l4` 1.6.109 and checked on 1.6.108 as well.
The source is a plain-text rendering by a converter script from Singapore Statutes Online; it is not the official text, and nothing here has been checked against the official text.

Files, all in this folder: `roc11-order-57.l4`, `-58`, `-59`, `-60`, `-61`, `-62`, `-63` (layer 1); `roc11-tests-order-57.l4` to `-63` (tests); `roc11-seat.l4` and `roc11-cases-seat.l4` (layer 2); `NOTES.md`; `PROGRESS.md`.
Layer 1 has 155 FALSE-kind comments and 284 NOTHING-kind comments, one on every `JUST FALSE` and every `NOTHING` result.
Tests: O 57 215, O 58 29, O 59 202, O 60 146, O 61 182, O 62 207, O 63 157; seat cases 663; seat questions 242.

## Coverage (roc11)

One row per unit of the text (Order, rule, defined term, subrule, paragraph, sub-paragraph, item), made by `work/units.py` from the raw text and joined to the layer-1 files by `work/coverage.py`; each row has exactly one disposition.
The L4 name is the function (or enum constructor) whose `@ref` or label names the unit; where a unit holds only sub-units, the name is the first sub-unit's.
Dispositions: `encoded` a rule, definition or table in layer 1 with a test and an `@ref`; `fork` the text reads two ways (the row points at the fork register); `inert` (reason 1, not operative) the Order's number and title only; `repealed or blank in this text` O 60 r 9(3).
No `out-of-scope` or `deferred` row exists.

Audit: rows 464; dispositions {'inert': 7, 'encoded': 443, 'fork': 13, 'repealed or blank in this text': 1}; range of unit lines 6796-7399; non-blank lines 6796-7399: 604; not in any row: []; units with no L4 name: 0 [].

| unit | lines | disposition | L4 name (file:line) |
| --- | --- | --- | --- |
| O 57 | 6796-6883 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 57 r 1 | 6798-6801 | encoded | `o 57 r 1 the meaning of the defined term` (order-57:55); `o 57 r 1 a reference to a section is a reference to a section in the Act` (order-57:68) (+5 more) |
| O 57 r 1 "Act" | 6799-6800 | encoded | `o 57 r 1 the meaning of the defined term` (order-57:55); `o 57 r 1 a reference to a section is a reference to a section in the Act` (order-57:68) (+5 more) |
| O 57 r 1 "Appeal Committee" | 6800-6801 | encoded | `o 57 r 1 the meaning of the defined term` (order-57:55); `o 57 r 1 a reference to a section is a reference to a section in the Act` (order-57:68) (+5 more) |
| O 57 r 1 "Commission" | 6801-6801 | encoded | `o 57 r 1 the meaning of the defined term` (order-57:55); `o 57 r 1 a reference to a section is a reference to a section in the Act` (order-57:68) (+5 more) |
| O 57 r 2 | 6802-6803 | encoded | `o 57 r 2 the power under section 48M may be exercised by the person` (order-57:138) |
| O 57 r 2(1) | 6803-6803 | encoded | `o 57 r 2(1) the power under section 48M may be exercised by the person` (order-57:110) |
| O 57 r 2(2) | 6803-6803 | encoded | `o 57 r 2(2) the power under section 48M(4) may be exercised by the person` (order-57:125) |
| O 57 r 3 | 6804-6814 | encoded | `o 57 r 3 the application to register is made in the way the Rule requires` (order-57:237); `o 57 r 3 the application to register in the District Court is made in the way the Rule requires` (order-57:255) (+10 more) |
| O 57 r 3(a) | 6805-6807 | fork | fork register: FORK O 57 r 3(a); `o 57 r 3(a) the instrument is a Direction` (order-57:176) |
| O 57 r 3(b) | 6807-6812 | fork | fork register: FORK O 57 r 3(b); `o 57 r 3(b) the instrument is a Notice` (order-57:194) |
| O 57 r 3(b)(i) | 6808-6810 | encoded | `o 57 r 3(b) the instrument is a Notice` (order-57:194) |
| O 57 r 3(b)(ii) | 6810-6812 | encoded | `o 57 r 3(b) the instrument is a Notice` (order-57:194) |
| O 57 r 3(c) | 6812-6814 | fork | fork register: FORK O 57 r 3(c); `o 57 r 3(c) the instrument is a Decision` (order-57:207) |
| O 57 r 4 | 6815-6840 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1) | 6816-6834 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1)(a) | 6816-6818 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1)(b) | 6818-6820 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1)(c) | 6820-6822 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1)(d) | 6822-6834 | encoded | `o 57 r 4(1)(d)(ii) the affidavit may state the matter the Rule requires about appeals` (order-57:416); `o 57 r 4(1)(d)(ii)(A) the affidavit may state that it has not been appealed against and the time allowed for appealing has expired` (order-57:387) |
| O 57 r 4(1)(d)(i) | 6823-6825 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(1)(d)(ii) | 6825-6830 | encoded | `o 57 r 4(1)(d)(ii) the affidavit may state the matter the Rule requires about appeals` (order-57:416) |
| O 57 r 4(1)(d)(ii)(A) | 6826-6828 | encoded | `o 57 r 4(1)(d)(ii)(A) the affidavit may state that it has not been appealed against and the time allowed for appealing has expired` (order-57:387) |
| O 57 r 4(1)(d)(ii)(B) | 6828-6830 | encoded | `o 57 r 4(1)(d)(ii)(B) the affidavit may state that all appeals have been finally disposed of and no further appeal is feasible` (order-57:399) |
| O 57 r 4(1)(d)(iii) | 6830-6832 | encoded | `o 57 r 4(1)(d)(iii) the affidavit may state that it has not been complied with` (order-57:428) |
| O 57 r 4(1)(d)(iv) | 6832-6834 | encoded | `o 57 r 4(1) the matters the affidavit has not yet stated` (order-57:298); `o 57 r 4(1) the affidavit supporting the application states what the Rule requires` (order-57:329) (+4 more) |
| O 57 r 4(2) | 6834-6840 | encoded | `o 57 r 4(2) the additional statement is required` (order-57:344); `o 57 r 4(2) the affidavit makes the additional statement the Rule requires` (order-57:361) (+4 more) |
| O 57 r 4(2)(a) | 6834-6836 | encoded | `o 57 r 4(2)(a) the affidavit may state that no application to reconsider was made and the time allowed to apply has expired` (order-57:442) |
| O 57 r 4(2)(b) | 6836-6840 | encoded | `o 57 r 4(2)(b)(i) the affidavit may state that the decision on reconsideration has not been appealed against and the time allowed for appealing has expired` (order-57:460); `o 57 r 4(2)(b)(ii) the affidavit may state that all appeals against the decision on reconsideration have been finally disposed of and the time allowed for a further appeal has expired` (order-57:482) |
| O 57 r 4(2)(b)(i) | 6837-6839 | encoded | `o 57 r 4(2)(b)(i) the affidavit may state that the decision on reconsideration has not been appealed against and the time allowed for appealing has expired` (order-57:460) |
| O 57 r 4(2)(b)(ii) | 6839-6840 | encoded | `o 57 r 4(2)(b)(ii) the affidavit may state that all appeals against the decision on reconsideration have been finally disposed of and the time allowed for a further appeal has expired` (order-57:482) |
| O 57 r 5 | 6841-6844 | encoded | `o 57 r 5(1) the order for registration is drawn up and served as the Rule requires` (order-57:532); `o 57 r 5(1) the form of the order for registration` (order-57:524) |
| O 57 r 5(1) | 6842-6842 | encoded | `o 57 r 5(1) the order for registration is drawn up and served as the Rule requires` (order-57:532); `o 57 r 5(1) the form of the order for registration` (order-57:524) |
| O 57 r 5(2) | 6842-6843 | encoded | `o 57 r 5(2) the order must state the period and contain the notification` (order-57:542); `o 57 r 5(2) the order for registration states and notifies what the Rule requires` (order-57:553) |
| O 57 r 5(3) | 6843-6844 | encoded | `o 57 r 5(3) the application to extend the period is made before the period expires` (order-57:566) |
| O 57 r 5(4) | 6844-6844 | encoded | `o 57 r 5(4) the Court may extend the period on such terms as it thinks fit` (order-57:575) |
| O 57 r 6 | 6845-6846 | encoded | `o 57 r 6 the register kept in the Registry contains the registered item` (order-57:589) |
| O 57 r 7 | 6847-6856 | encoded | `o 57 r 7(1) the notice of registration is served as the Rule requires` (order-57:609); `o 57 r 7(2) permission is needed to serve the notice out of Singapore` (order-57:622) (+1 more) |
| O 57 r 7(1) | 6848-6848 | encoded | `o 57 r 7(1) the notice of registration is served as the Rule requires` (order-57:609) |
| O 57 r 7(2) | 6848-6849 | encoded | `o 57 r 7(2) permission is needed to serve the notice out of Singapore` (order-57:622); `o 57 r 7(2) a rule of Order 8 applies to the notice` (order-57:635) |
| O 57 r 7(3) | 6849-6856 | encoded | `o 57 r 7(3) the matters the notice has not yet stated` (order-57:661); `o 57 r 7(3) the notice of registration states what the Rule requires` (order-57:679) |
| O 57 r 7(3)(a) | 6849-6851 | encoded | `o 57 r 7(3) the matters the notice has not yet stated` (order-57:661); `o 57 r 7(3) the notice of registration states what the Rule requires` (order-57:679) |
| O 57 r 7(3)(b) | 6851-6853 | encoded | `o 57 r 7(3) the matters the notice has not yet stated` (order-57:661); `o 57 r 7(3) the notice of registration states what the Rule requires` (order-57:679) |
| O 57 r 7(3)(c) | 6853-6855 | encoded | `o 57 r 7(3) the matters the notice has not yet stated` (order-57:661); `o 57 r 7(3) the notice of registration states what the Rule requires` (order-57:679) |
| O 57 r 7(3)(d) | 6855-6856 | encoded | `o 57 r 7(3) the matters the notice has not yet stated` (order-57:661); `o 57 r 7(3) the notice of registration states what the Rule requires` (order-57:679) |
| O 57 r 8 | 6857-6859 | encoded | `o 57 r 8(1) the period for endorsing the notice` (order-57:691); `o 57 r 8(1) the notice is endorsed in time` (order-57:715) (+6 more) |
| O 57 r 8(1) | 6858-6858 | encoded | `o 57 r 8(1) the period for endorsing the notice` (order-57:691); `o 57 r 8(1) the notice is endorsed in time` (order-57:715) (+6 more) |
| O 57 r 8(2) | 6858-6859 | encoded | `o 57 r 8(2) the person seeking to enforce may apply for an enforcement order without the permission of the Court` (order-57:783) |
| O 57 r 8(3) | 6859-6859 | encoded | `o 57 r 8(3) the affidavit of service states the date of endorsement` (order-57:793) |
| O 57 r 9 | 6860-6866 | encoded | `o 57 r 9(1) the application to set aside the registration is made as the Rule requires` (order-57:807); `o 57 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-57:821) |
| O 57 r 9(1) | 6861-6861 | encoded | `o 57 r 9(1) the application to set aside the registration is made as the Rule requires` (order-57:807) |
| O 57 r 9(2) | 6861-6866 | encoded | `o 57 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-57:821) |
| O 57 r 9(2)(a) | 6861-6863 | encoded | `o 57 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-57:821) |
| O 57 r 9(2)(b) | 6863-6866 | encoded | `o 57 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-57:821) |
| O 57 r 9(3) | 6866-6866 | encoded | `o 57 r 9(3) the Court may order the registration to be set aside on such terms as it thinks fit` (order-57:830) |
| O 57 r 10 | 6867-6869 | encoded | `o 57 r 10 whoever issues the enforcement order` (order-57:888); `o 57 r 10 issue the enforcement order` (order-57:891) |
| O 57 r 10(1) | 6868-6868 | encoded | `o 57 r 10(1) an enforcement order cannot yet be issued because the specified period has not expired` (order-57:849); `o 57 r 10(1) the prohibition on issuing the enforcement order` (order-57:894) |
| O 57 r 10(2) | 6868-6869 | encoded | `o 57 r 10(2) an enforcement order cannot yet be issued because the application to set aside is not disposed of` (order-57:864); `o 57 r 10(2) the prohibition on issuing the enforcement order while the application is undisposed` (order-57:908) |
| O 57 r 10(3) | 6869-6869 | encoded | `o 57 r 10(3) the party applying for an enforcement order has produced what the Rule requires` (order-57:878) |
| O 57 r 11 | 6870-6879 | encoded | `o 57 r 11(1)(a) the application for an order specified in section 48M(4) may be made at this time` (order-57:936); `o 57 r 11(1)(b) the application is an application for an enforcement order under Rule 10` (order-57:947) |
| O 57 r 11(1) | 6871-6875 | encoded | `o 57 r 11(1)(a) the application for an order specified in section 48M(4) may be made at this time` (order-57:936); `o 57 r 11(1)(b) the application is an application for an enforcement order under Rule 10` (order-57:947) |
| O 57 r 11(1)(a) | 6871-6873 | encoded | `o 57 r 11(1)(a) together with the application for registration` (order-57:925); `o 57 r 11(1)(a) at a time after the application for registration` (order-57:926) (+2 more) |
| O 57 r 11(1)(b) | 6873-6875 | encoded | `o 57 r 11(1)(b) the application is an application for an enforcement order under Rule 10` (order-57:947) |
| O 57 r 11(2) | 6875-6876 | encoded | `o 57 r 11(2) the application may be made in this way` (order-57:961); `o 57 r 11(2) by summons supported by an affidavit, with notice` (order-57:953) (+1 more) |
| O 57 r 11(3) | 6876-6879 | encoded | `o 57 r 11(3) the matters the affidavit has not yet stated` (order-57:980); `o 57 r 11(3) the affidavit states what the Rule requires` (order-57:992) |
| O 57 r 11(3)(a) | 6876-6878 | encoded | `o 57 r 11(3) the matters the affidavit has not yet stated` (order-57:980); `o 57 r 11(3) the affidavit states what the Rule requires` (order-57:992) |
| O 57 r 11(3)(b) | 6878-6879 | encoded | `o 57 r 11(3) the matters the affidavit has not yet stated` (order-57:980); `o 57 r 11(3) the affidavit states what the Rule requires` (order-57:992) |
| O 57 r 12 | 6880-6881 | encoded | `o 57 r 12 the period for serving a copy on the Commission` (order-57:1004); `o 57 r 12 the duty to serve a copy on the Commission arises` (order-57:1014) (+4 more) |
| O 57 r 13 | 6882-6883 | encoded | `o 57 r 13 the period for transmitting a copy to the Commission` (order-57:1059); `o 57 r 13 the duty to transmit a copy to the Commission arises` (order-57:1068) (+4 more) |
| O 58 | 6884-6902 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 58 r 1 | 6886-6887 | encoded | `o 58 r 1 these Rules apply to the proceedings` (order-58:32) |
| O 58 r 2 | 6888-6889 | encoded | `o 58 r 2 the section is one that the Rule names` (order-58:54); `o 58 r 2 the application is made as the Rule requires` (order-58:69) (+6 more) |
| O 58 r 3 | 6890-6902 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(a) | 6891-6893 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(b) | 6893-6895 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(c) | 6895-6897 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(d) | 6897-6899 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(e) | 6899-6901 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 58 r 3(f) | 6901-6902 | encoded | `o 58 r 3 the duty to give the particulars arises` (order-58:97); `o 58 r 3 the particulars still to be given` (order-58:117) (+1 more) |
| O 59 | 6903-6969 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 59 r 1 | 6905-6910 | encoded | `o 59 r 1(1) these Rules apply to the proceedings` (order-59:44); `o 59 r 1(2) a reference to a section is a reference to a section in the Act` (order-59:60) (+7 more) |
| O 59 r 1(1) | 6906-6906 | encoded | `o 59 r 1(1) these Rules apply to the proceedings` (order-59:44) |
| O 59 r 1(2) | 6906-6910 | encoded | `o 59 r 1(2) a reference to a section is a reference to a section in the Act` (order-59:60); `o 59 r 1(2) the Act` (order-59:51) (+6 more) |
| O 59 r 1(2) "Act" | 6906-6908 | encoded | `o 59 r 1(2) the Act` (order-59:51) |
| O 59 r 1(2) "civil proceedings to which the Government is a party" | 6908-6909 | encoded | `o 59 r 1(2) "civil proceedings to which the Government is a party" the provision that gives its meaning` (order-59:84) |
| O 59 r 1(2) "order" | 6909-6910 | encoded | `o 59 r 1(2) "order" the thing is within the term` (order-59:99) |
| O 59 r 1(2) "order against the Government" | 6910-6910 | encoded | `o 59 r 1(2) "order against the Government" the order is an order against the Government` (order-59:114) |
| O 59 r 2 | 6911-6916 | encoded | `o 59 r 2(1) the matters the endorsement has not yet stated` (order-59:132); `o 59 r 2(1) the endorsement of claim states what the Rule requires` (order-59:143) |
| O 59 r 2(1) | 6912-6912 | encoded | `o 59 r 2(1) the matters the endorsement has not yet stated` (order-59:132); `o 59 r 2(1) the endorsement of claim states what the Rule requires` (order-59:143) |
| O 59 r 2(2) | 6912-6913 | encoded | `o 59 r 2(2) the defendant may apply to the claimant by notice for a further and better statement` (order-59:161) |
| O 59 r 2(3) | 6913-6916 | fork | fork register: FORK O 59 r 2(3); `o 59 r 2(3) the time for filing a notice of intention to contest or not contest cannot yet expire` (order-59:194); `o 59 r 2(3)(b) the claimant's application is made and served as the Rule requires` (order-59:221) |
| O 59 r 2(3)(a) | 6913-6915 | encoded | `o 59 r 2(3)(a) the period after the defendant's written notification` (order-59:169) |
| O 59 r 2(3)(b) | 6915-6916 | encoded | `o 59 r 2(3)(b) the period after the Court's decision` (order-59:174); `o 59 r 2(3)(b) the period for serving the summons before the return day` (order-59:208) (+1 more) |
| O 59 r 3 | 6917-6922 | encoded | `o 59 r 3(1) the provision applies to the service of the process` (order-59:241); `o 59 r 3(2) personal service on the Government is requisite` (order-59:251) (+1 more) |
| O 59 r 3(1) | 6918-6918 | encoded | `o 59 r 3(1) the provision applies to the service of the process` (order-59:241) |
| O 59 r 3(2) | 6918-6922 | encoded | `o 59 r 3(2) personal service on the Government is requisite` (order-59:251); `o 59 r 3(2) service on the Government is effected as the Rule requires` (order-59:266) |
| O 59 r 3(2)(a) | 6918-6920 | encoded | `o 59 r 3(2) personal service on the Government is requisite` (order-59:251); `o 59 r 3(2) service on the Government is effected as the Rule requires` (order-59:266) |
| O 59 r 3(2)(b) | 6920-6922 | encoded | `o 59 r 3(2) personal service on the Government is requisite` (order-59:251); `o 59 r 3(2) service on the Government is effected as the Rule requires` (order-59:266) |
| O 59 r 3(3) | 6922-6922 | encoded | `o 59 r 3(3) the provision applies to the service` (order-59:281) |
| O 59 r 4 | 6923-6928 | encoded | `o 59 r 4(1) a person may make a counterclaim or plead a set-off` (order-59:302); `o 59 r 4(2) the permission of the Court is required for the counterclaim or set-off` (order-59:333) (+7 more) |
| O 59 r 4(1) | 6924-6924 | encoded | `o 59 r 4(1) a person may make a counterclaim or plead a set-off` (order-59:302) |
| O 59 r 4(2) | 6924-6928 | encoded | `o 59 r 4(2) the permission of the Court is required for the counterclaim or set-off` (order-59:333); `o 59 r 4(2) the counterclaim may be made or the set-off pleaded` (order-59:356) (+6 more) |
| O 59 r 4(2)(a) | 6924-6926 | encoded | `o 59 r 4(2) the permission of the Court is required for the counterclaim or set-off` (order-59:333); `o 59 r 4(2) the counterclaim may be made or the set-off pleaded` (order-59:356) (+6 more) |
| O 59 r 4(2)(b) | 6926-6928 | encoded | `o 59 r 4(2) the permission of the Court is required for the counterclaim or set-off` (order-59:333); `o 59 r 4(2) the counterclaim may be made or the set-off pleaded` (order-59:356) (+6 more) |
| O 59 r 4(3) | 6928-6928 | encoded | `o 59 r 4(3) the application for permission is made as the Rule requires` (order-59:369) |
| O 59 r 5 | 6929-6937 | encoded | `o 59 r 5(1) an application against the Government may be made under the provision` (order-59:396); `o 59 r 5(1) proceedings against the Government` (order-59:382) (+1 more) |
| O 59 r 5(1) | 6930-6934 | encoded | `o 59 r 5(1) an application against the Government may be made under the provision` (order-59:396); `o 59 r 5(1) proceedings against the Government` (order-59:382) (+1 more) |
| O 59 r 5(1)(a) | 6930-6932 | encoded | `o 59 r 5(1) an application against the Government may be made under the provision` (order-59:396); `o 59 r 5(1) proceedings against the Government` (order-59:382) (+1 more) |
| O 59 r 5(1)(b) | 6932-6934 | encoded | `o 59 r 5(1) an application against the Government may be made under the provision` (order-59:396); `o 59 r 5(1) proceedings against the Government` (order-59:382) (+1 more) |
| O 59 r 5(2) | 6934-6937 | encoded | `o 59 r 5(2) the affidavit in support is made by a person the Rule allows` (order-59:421); `o 59 r 5(2) someone else` (order-59:411) |
| O 59 r 5(2)(a) | 6934-6936 | encoded | `o 59 r 5(2)(a) the solicitor acting for the Government` (order-59:408) |
| O 59 r 5(2)(b) | 6936-6937 | encoded | `o 59 r 5(2)(b) an officer duly authorised by the solicitor so acting` (order-59:409); `o 59 r 5(2)(b) an officer duly authorised by the department concerned` (order-59:410) |
| O 59 r 6 | 6938-6947 | encoded | `o 59 r 6(1) this Rule applies to the application` (order-59:437); `o 59 r 6(2) the application is made as the Rule requires` (order-59:447) |
| O 59 r 6(1) | 6939-6939 | encoded | `o 59 r 6(1) this Rule applies to the application` (order-59:437) |
| O 59 r 6(2) | 6939-6940 | encoded | `o 59 r 6(2) the application is made as the Rule requires` (order-59:447) |
| O 59 r 6(3) | 6940-6941 | encoded | `o 59 r 6(3) the person is made defendant as the Rule requires` (order-59:460) |
| O 59 r 6(4) | 6941-6945 | encoded | `o 59 r 6(4) the matters the originating application has not yet satisfied` (order-59:484); `o 59 r 6(4) the originating application is what the Rule requires` (order-59:500) |
| O 59 r 6(4)(a) | 6941-6943 | encoded | `o 59 r 6(4) the matters the originating application has not yet satisfied` (order-59:484); `o 59 r 6(4) the originating application is what the Rule requires` (order-59:500) |
| O 59 r 6(4)(b) | 6943-6945 | encoded | `o 59 r 6(4) the matters the originating application has not yet satisfied` (order-59:484); `o 59 r 6(4) the originating application is what the Rule requires` (order-59:500) |
| O 59 r 6(5) | 6945-6946 | encoded | `o 59 r 6(5) the affidavit is evidence of those facts` (order-59:517); `o 59 r 6(5) the course is open` (order-59:538) (+3 more) |
| O 59 r 6(6) | 6946-6947 | encoded | `o 59 r 6(6) the duty to name a time for compliance with each term arises` (order-59:550); `o 59 r 6(6) the order names a time as the Rule requires` (order-59:565) |
| O 59 r 6(7) | 6947-6947 | encoded | `o 59 r 6(7) this Rule requires the Government to proceed by way of an application under it` (order-59:580); `o 59 r 6(7) this Rule prevents the Government from availing itself of another procedure open under these Rules` (order-59:589) |
| O 59 r 7 | 6948-6950 | encoded | `o 59 r 7(1) judgment in default is barred without permission` (order-59:618); `o 59 r 7(1) judgment in default may be entered against the Government` (order-59:633) (+6 more) |
| O 59 r 7(1) | 6949-6949 | encoded | `o 59 r 7(1) judgment in default is barred without permission` (order-59:618); `o 59 r 7(1) judgment in default may be entered against the Government` (order-59:633) (+6 more) |
| O 59 r 7(2) | 6949-6950 | encoded | `o 59 r 7(2) Order 10 rule 5(1)(a) applies` (order-59:647) |
| O 59 r 7(3) | 6950-6950 | encoded | `o 59 r 7(3) the application for permission is made and served as the Rule requires` (order-59:665); `o 59 r 7(3) the period for serving the summons before the return day` (order-59:653) |
| O 59 r 8 | 6951-6952 | encoded | `o 59 r 8(1) the third party notice may be issued` (order-59:686); `o 59 r 8(1) the application for permission is made and served as the Rule requires` (order-59:701) |
| O 59 r 8(1) | 6952-6952 | encoded | `o 59 r 8(1) the third party notice may be issued` (order-59:686); `o 59 r 8(1) the application for permission is made and served as the Rule requires` (order-59:701) |
| O 59 r 8(2) | 6952-6952 | encoded | `o 59 r 8(2) the Court may grant permission to issue the notice` (order-59:715) |
| O 59 r 9 | 6953-6954 | encoded | `o 59 r 9(1) the order requires disclosure of the document` (order-59:732); `o 59 r 9(2) the affidavit verifying the list is made by the officer the Court directed` (order-59:743) |
| O 59 r 9(1) | 6954-6954 | encoded | `o 59 r 9(1) the order requires disclosure of the document` (order-59:732) |
| O 59 r 9(2) | 6954-6954 | encoded | `o 59 r 9(2) the affidavit verifying the list is made by the officer the Court directed` (order-59:743) |
| O 59 r 10 | 6955-6956 | encoded | `o 59 r 10 the Court's powers in regard to the taking of evidence are exercisable as between subjects` (order-59:759) |
| O 59 r 11 | 6957-6959 | encoded | `o 59 r 11(1) the provision applies in respect of the order` (order-59:775); `o 59 r 11(2) the application may be made in this way` (order-59:790) |
| O 59 r 11(1) | 6958-6958 | encoded | `o 59 r 11(1) the provision applies in respect of the order` (order-59:775) |
| O 59 r 11(2) | 6958-6959 | encoded | `o 59 r 11(2) the application may be made in this way` (order-59:790) |
| O 59 r 11(3) | 6959-6959 | encoded | `o 59 r 11(3) the certificate is in the form the Rule requires` (order-59:804); `o 59 r 11(3) the form of the certificate` (order-59:798) |
| O 59 r 12 | 6960-6967 | encoded | `o 59 r 12(1) the order may be made` (order-59:830); `o 59 r 12(1) the order has effect` (order-59:845) (+1 more) |
| O 59 r 12(1) | 6961-6966 | encoded | `o 59 r 12(1) the order may be made` (order-59:830); `o 59 r 12(1) the order has effect` (order-59:845) (+1 more) |
| O 59 r 12(1)(a) | 6961-6963 | encoded | `o 59 r 12(1)(a) an order for the attachment of debts under Order 22` (order-59:814) |
| O 59 r 12(1)(b) | 6963-6966 | encoded | `o 59 r 12(1)(b) an order for the appointment of a receiver under Order 13, Rule 9` (order-59:815) |
| O 59 r 12(2) | 6966-6967 | encoded | `o 59 r 12(2) the application is made and served as the Rule requires` (order-59:869); `o 59 r 12(2) the period for serving the summons before the return day` (order-59:853) |
| O 59 r 12(3) | 6967-6967 | encoded | `o 59 r 12(3) Order 22 rule 10 applies to the application` (order-59:886); `o 59 r 12(3) the Court has power to order an enforcement order to be issued against the Government` (order-59:895) |
| O 59 r 13 | 6968-6969 | encoded | `o 59 r 13(1) the application is made as the Rule requires` (order-59:909); `o 59 r 13(2) the application may be made in this way and at this time` (order-59:930) (+3 more) |
| O 59 r 13(1) | 6969-6969 | encoded | `o 59 r 13(1) the application is made as the Rule requires` (order-59:909) |
| O 59 r 13(2) | 6969-6969 | encoded | `o 59 r 13(2) the application may be made in this way and at this time` (order-59:930); `o 59 r 13(2) before the trial` (order-59:918) (+2 more) |
| O 60 | 6970-7053 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 60 r 1 | 6972-6973 | encoded | `o 60 r 1 a reference to a section is a reference to a section in the Act` (order-60:49); `o 60 r 1 the Act` (order-60:40) |
| O 60 r 1 "Act" | 6973-6973 | encoded | `o 60 r 1 the Act` (order-60:40) |
| O 60 r 1A | 6974-6975 | encoded | `o 60 r 1A the power conferred on the General Division by the Act may be exercised by the person` (order-60:66) |
| O 60 r 2 | 6976-6977 | encoded | `o 60 r 2 the application for registration is made in the way the Rule requires` (order-60:85) |
| O 60 r 3 | 6978-6993 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1) | 6979-6992 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(a) | 6979-6981 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(b) | 6981-6983 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(c) | 6983-6990 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(c)(i) | 6984-6986 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(c)(ii) | 6986-6988 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(c)(iii) | 6988-6990 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(1)(d) | 6990-6992 | encoded | `o 60 r 3(1) the matters the affidavit has not yet stated` (order-60:128); `o 60 r 3(1) the affidavit supporting the application states what the Rule requires` (order-60:154) |
| O 60 r 3(2) | 6992-6993 | encoded | `o 60 r 3(2) the duty to state the provisions arises` (order-60:166); `o 60 r 3(2) the affidavit states the provisions in respect of which registration is sought` (order-60:177) |
| O 60 r 3(3) | 6993-6993 | encoded | `o 60 r 3(3) the affidavit is accompanied by the other evidence the Rule requires` (order-60:191) |
| O 60 r 4 | 6994-6995 | encoded | `o 60 r 4 the Court may order the judgment creditor to give security for costs` (order-60:204) |
| O 60 r 5 | 6996-6998 | encoded | `o 60 r 5(1) the order giving permission to register is drawn up and served as the Rule requires` (order-60:221); `o 60 r 5(1) the form of the order giving permission to register` (order-60:213) |
| O 60 r 5(1) | 6997-6997 | encoded | `o 60 r 5(1) the order giving permission to register is drawn up and served as the Rule requires` (order-60:221); `o 60 r 5(1) the form of the order giving permission to register` (order-60:213) |
| O 60 r 5(2) | 6997-6998 | encoded | `o 60 r 5(2) the order states the period and contains the notification` (order-60:231) |
| O 60 r 5(3) | 6998-6998 | fork | fork register: FORK O 60 r 5(3); `o 60 r 5(3) the Court may extend the period for applying to set aside the registration` (order-60:242) |
| O 60 r 6 | 6999-7001 | encoded | `o 60 r 6(1) the register kept in the Registry contains the judgment` (order-60:256); `o 60 r 6(2) the register includes particulars of the enforcement order` (order-60:269) |
| O 60 r 6(1) | 7000-7001 | encoded | `o 60 r 6(1) the register kept in the Registry contains the judgment` (order-60:256) |
| O 60 r 6(2) | 7001-7001 | encoded | `o 60 r 6(2) the register includes particulars of the enforcement order` (order-60:269) |
| O 60 r 7 | 7002-7011 | encoded | `o 60 r 7(1) the notice of registration is served as the Rule requires` (order-60:289); `o 60 r 7(2) permission is needed to serve the notice out of Singapore` (order-60:301) (+1 more) |
| O 60 r 7(1) | 7003-7003 | encoded | `o 60 r 7(1) the notice of registration is served as the Rule requires` (order-60:289) |
| O 60 r 7(2) | 7003-7004 | encoded | `o 60 r 7(2) permission is needed to serve the notice out of Singapore` (order-60:301); `o 60 r 7(2) a rule of Order 8 applies to the notice` (order-60:311) |
| O 60 r 7(3) | 7004-7011 | encoded | `o 60 r 7(3) the matters the notice has not yet stated` (order-60:337); `o 60 r 7(3) the notice of registration states what the Rule requires` (order-60:355) |
| O 60 r 7(3)(a) | 7004-7006 | encoded | `o 60 r 7(3) the matters the notice has not yet stated` (order-60:337); `o 60 r 7(3) the notice of registration states what the Rule requires` (order-60:355) |
| O 60 r 7(3)(b) | 7006-7008 | encoded | `o 60 r 7(3) the matters the notice has not yet stated` (order-60:337); `o 60 r 7(3) the notice of registration states what the Rule requires` (order-60:355) |
| O 60 r 7(3)(c) | 7008-7010 | encoded | `o 60 r 7(3) the matters the notice has not yet stated` (order-60:337); `o 60 r 7(3) the notice of registration states what the Rule requires` (order-60:355) |
| O 60 r 7(3)(d) | 7010-7011 | encoded | `o 60 r 7(3) the matters the notice has not yet stated` (order-60:337); `o 60 r 7(3) the notice of registration states what the Rule requires` (order-60:355) |
| O 60 r 8 | 7012-7013 | encoded | `o 60 r 8(1) the period for endorsing the notice` (order-60:366); `o 60 r 8(1) the last day for endorsing the notice` (order-60:379) (+7 more) |
| O 60 r 8(1) | 7013-7013 | encoded | `o 60 r 8(1) the period for endorsing the notice` (order-60:366); `o 60 r 8(1) the last day for endorsing the notice` (order-60:379) (+7 more) |
| O 60 r 8(2) | 7013-7013 | encoded | `o 60 r 8(2) the affidavit of service states the date of endorsement` (order-60:465) |
| O 60 r 9 | 7014-7016 | encoded | `o 60 r 9(1) the application to set aside the registration is made as the Rule requires` (order-60:479); `o 60 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-60:489) |
| O 60 r 9(1) | 7015-7015 | encoded | `o 60 r 9(1) the application to set aside the registration is made as the Rule requires` (order-60:479) |
| O 60 r 9(2) | 7015-7016 | encoded | `o 60 r 9(2) the Court may order the issue to be tried as an issue in an action is tried` (order-60:489) |
| O 60 r 9(3) | 7016-7016 | repealed or blank in this text | the text shows "[ Deleted by S 91/2023 wef 01/03/2023 ]" |
| O 60 r 10 | 7017-7020 | encoded | `o 60 r 10 whoever issues the enforcement order` (order-60:546); `o 60 r 10 issue the enforcement order` (order-60:549) |
| O 60 r 10(1) | 7018-7019 | encoded | `o 60 r 10(1) an enforcement order cannot yet be issued because the specified period has not expired` (order-60:508); `o 60 r 10(1) the prohibition on issuing the enforcement order` (order-60:552) |
| O 60 r 10(2) | 7019-7020 | encoded | `o 60 r 10(2) an enforcement order cannot yet be issued because the application to set aside is not finally determined` (order-60:523); `o 60 r 10(2) the prohibition on issuing the enforcement order while the application is undetermined` (order-60:565) |
| O 60 r 10(3) | 7020-7020 | encoded | `o 60 r 10(3) the party applying for an enforcement order has produced what the Rule requires` (order-60:537) |
| O 60 r 11 | 7021-7022 | encoded | `o 60 r 11 the question is determined in accordance with the extending Order` (order-60:588) |
| O 60 r 12 | 7023-7024 | fork | fork register: FORK O 60 r 12; `o 60 r 12 the rule has effect subject to the provision of the extending Order` (order-60:605) |
| O 60 r 13 | 7025-7053 | encoded | `o 60 r 13(1) the application for certified copies is made in the way the Rule requires` (order-60:638); `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679) (+1 more) |
| O 60 r 13(1) | 7026-7026 | encoded | `o 60 r 13(1) the application for certified copies is made in the way the Rule requires` (order-60:638) |
| O 60 r 13(2) | 7026-7038 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(a) | 7026-7028 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(b) | 7028-7030 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(c) | 7030-7032 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(d) | 7032-7034 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(e) | 7034-7036 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(2)(f) | 7036-7038 | encoded | `o 60 r 13(2) the matters the affidavit has not yet covered` (order-60:679); `o 60 r 13(2) the affidavit supporting the application covers what the Rule requires` (order-60:708) |
| O 60 r 13(3) | 7038-7053 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(a) | 7038-7040 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(b) | 7040-7042 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(c) | 7042-7044 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(d) | 7044-7046 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(e) | 7046-7048 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(f) | 7048-7050 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(g) | 7050-7052 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 60 r 13(3)(h) | 7052-7053 | encoded | `o 60 r 13(3) the matters the copies and certificate have not yet satisfied` (order-60:749); `o 60 r 13(3) the certified copies and certificate are what the Rule requires` (order-60:782) |
| O 61 | 7054-7149 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 61 r 1 | 7056-7083 | encoded | `o 61 r 1 a proceeding under section 234` (order-61:42); `o 61 r 1 a proceeding under section 235` (order-61:43) (+7 more) |
| O 61 r 1(1) | 7057-7083 | encoded | `o 61 r 1(1) a reference to a section is a reference to a section in the Act` (order-61:63); `o 61 r 1(1) the Act` (order-61:54) |
| O 61 r 1(1) "Act" | 7057-7058 | encoded | `o 61 r 1(1) the Act` (order-61:54) |
| O 61 r 1(1) "claimant" | 7058-7068 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "claimant"(a) | 7058-7060 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "claimant"(b) | 7060-7062 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "claimant"(c) | 7062-7064 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "claimant"(d) | 7064-7066 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "claimant"(e) | 7066-7068 | encoded | `o 61 r 1(1) "claimant" the section that gives its meaning` (order-61:86) |
| O 61 r 1(1) "contravening person" | 7068-7080 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(a) | 7068-7070 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(b) | 7070-7072 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(c) | 7072-7074 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(d) | 7074-7076 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(e) | 7076-7078 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "contravening person"(f) | 7078-7080 | encoded | `o 61 r 1(1) "contravening person" the section that gives its meaning` (order-61:114) |
| O 61 r 1(1) "defendant corporation" | 7080-7081 | encoded | `o 61 r 1(1) "defendant corporation" the section that gives its meaning` (order-61:129) |
| O 61 r 1(1) "defendant individual" | 7081-7082 | encoded | `o 61 r 1(1) "defendant individual" the person is a defendant individual` (order-61:145) |
| O 61 r 1(1) "defendant partnership" | 7082-7083 | encoded | `o 61 r 1(1) "defendant partnership" the section that gives its meaning` (order-61:133) |
| O 61 r 1(2) | 7083-7083 | encoded | `o 61 r 1(2) these Rules apply to the proceeding` (order-61:158) |
| O 61 r 2 | 7084-7099 | encoded | `o 61 r 2(1) the action is one that the Rule names` (order-61:172); `o 61 r 2(1) the action is commenced as the Rule requires` (order-61:185) |
| O 61 r 2(1) | 7085-7085 | encoded | `o 61 r 2(1) the action is one that the Rule names` (order-61:172); `o 61 r 2(1) the action is commenced as the Rule requires` (order-61:185) |
| O 61 r 2(2) | 7085-7086 | encoded | `o 61 r 2(2) the application for permission is made as the Rule requires` (order-61:200) |
| O 61 r 2(3) | 7086-7087 | encoded | `o 61 r 2(3) the provision applies to the originating application` (order-61:217) |
| O 61 r 2(4) | 7087-7097 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(4)(a) | 7087-7089 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(4)(b) | 7089-7091 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(4)(c) | 7091-7093 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(4)(d) | 7093-7095 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(4)(e) | 7095-7097 | encoded | `o 61 r 2(4) the matters the affidavit has not yet set out` (order-61:254); `o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires` (order-61:275) |
| O 61 r 2(5) | 7097-7098 | encoded | `o 61 r 2(5) the application is served as the Rule requires in the first instance` (order-61:288) |
| O 61 r 2(6) | 7098-7099 | encoded | `o 61 r 2(6) the application to continue the stayed action is made as the Rule requires` (order-61:304) |
| O 61 r 2(7) | 7099-7099 | encoded | `o 61 r 2(7) the application to continue is served as the Rule requires in the first instance` (order-61:319) |
| O 61 r 3 | 7100-7112 | encoded | `o 61 r 3(1) the claimant may apply for directions on claims for compensation` (order-61:344); `o 61 r 3(1) the Court may fix a return date for hearing the application` (order-61:361) |
| O 61 r 3(1) | 7101-7106 | encoded | `o 61 r 3(1) the claimant may apply for directions on claims for compensation` (order-61:344); `o 61 r 3(1) the Court may fix a return date for hearing the application` (order-61:361) |
| O 61 r 3(1)(a) | 7101-7103 | encoded | `o 61 r 3(1) the claimant may apply for directions on claims for compensation` (order-61:344); `o 61 r 3(1) the Court may fix a return date for hearing the application` (order-61:361) |
| O 61 r 3(1)(b) | 7103-7106 | encoded | `o 61 r 3(1) the claimant may apply for directions on claims for compensation` (order-61:344); `o 61 r 3(1) the Court may fix a return date for hearing the application` (order-61:361) |
| O 61 r 3(2) | 7106-7107 | encoded | `o 61 r 3(2) an application cannot yet be made because the conviction or order is not yet final` (order-61:376); `o 61 r 3(2) the claimant` (order-61:387) (+2 more) |
| O 61 r 3(3) | 7107-7108 | encoded | `o 61 r 3(3) the application for directions is made as the Rule requires` (order-61:411) |
| O 61 r 3(4) | 7108-7109 | encoded | `o 61 r 3(4) the provision applies to the originating application` (order-61:426) |
| O 61 r 3(5) | 7109-7110 | encoded | `o 61 r 3(5) the period for serving the application before the return date` (order-61:446); `o 61 r 3(5) the duty to serve the application personally in time arises` (order-61:455) (+2 more) |
| O 61 r 3(6) | 7110-7111 | encoded | `o 61 r 3(6) the period for advertising the application before the return date` (order-61:494); `o 61 r 3(6) the application is advertised as the Rule requires` (order-61:507) (+2 more) |
| O 61 r 3(7) | 7111-7112 | encoded | `o 61 r 3(7) the matters the advertisement has not yet stated` (order-61:535); `o 61 r 3(7) the advertisement states what the Rule requires` (order-61:545) (+1 more) |
| O 61 r 3(8) | 7112-7112 | fork | fork register: FORK O 61 r 3(8); `o 61 r 3(8) the application is deemed dismissed` (order-61:565); `o 61 r 3(8) the Court must cancel the appointment of the time and place for the hearing` (order-61:580) |
| O 61 r 4 | 7113-7128 | encoded | `o 61 r 4(1) the period for filing the affidavit of claim before the return date` (order-61:596); `o 61 r 4(1) the duty to file an affidavit of claim arises` (order-61:605) (+1 more) |
| O 61 r 4(1) | 7114-7114 | encoded | `o 61 r 4(1) the period for filing the affidavit of claim before the return date` (order-61:596); `o 61 r 4(1) the duty to file an affidavit of claim arises` (order-61:605) (+1 more) |
| O 61 r 4(2) | 7114-7122 | encoded | `o 61 r 4(2) the matters the affidavit has not yet covered` (order-61:650); `o 61 r 4(2) the affidavit of claim covers what the Rule requires` (order-61:670) |
| O 61 r 4(2)(a) | 7114-7116 | encoded | `o 61 r 4(2) the matters the affidavit has not yet covered` (order-61:650); `o 61 r 4(2) the affidavit of claim covers what the Rule requires` (order-61:670) |
| O 61 r 4(2)(b) | 7116-7118 | encoded | `o 61 r 4(2) the matters the affidavit has not yet covered` (order-61:650); `o 61 r 4(2) the affidavit of claim covers what the Rule requires` (order-61:670) |
| O 61 r 4(2)(c) | 7118-7120 | encoded | `o 61 r 4(2) the matters the affidavit has not yet covered` (order-61:650); `o 61 r 4(2) the affidavit of claim covers what the Rule requires` (order-61:670) |
| O 61 r 4(2)(d) | 7120-7122 | encoded | `o 61 r 4(2) the matters the affidavit has not yet covered` (order-61:650); `o 61 r 4(2) the affidavit of claim covers what the Rule requires` (order-61:670) |
| O 61 r 4(3) | 7122-7128 | encoded | `o 61 r 4(3) the exhibits may include` (order-61:692); `o 61 r 4(3) another exhibit` (order-61:681) |
| O 61 r 4(3)(a) | 7122-7124 | encoded | `o 61 r 4(3)(a) trade notes or slips` (order-61:678) |
| O 61 r 4(3)(b) | 7124-7126 | encoded | `o 61 r 4(3)(b) statements of accounts for the relevant period` (order-61:679) |
| O 61 r 4(3)(c) | 7126-7128 | encoded | `o 61 r 4(3)(c) copies of instructions given to a broker or remisier` (order-61:680) |
| O 61 r 4(4) | 7128-7128 | encoded | `o 61 r 4(4) the period for serving a copy of the affidavit on the subject` (order-61:700); `o 61 r 4(4) the claimant serves a copy of the affidavit on the subject in time` (order-61:711) (+3 more) |
| O 61 r 5 | 7129-7145 | encoded | `o 61 r 5(1) the Court may give directions or make orders on the hearing` (order-61:778); `o 61 r 5(1) the Court may give this kind of direction or make this kind of order` (order-61:804) (+1 more) |
| O 61 r 5(1) | 7130-7144 | encoded | `o 61 r 5(1) the Court may give directions or make orders on the hearing` (order-61:778); `o 61 r 5(1) the Court may give this kind of direction or make this kind of order` (order-61:804) (+1 more) |
| O 61 r 5(1)(a) | 7130-7132 | encoded | `o 61 r 5(1)(a) for the filing of such further affidavit as the Court considers necessary` (order-61:746) |
| O 61 r 5(1)(b) | 7132-7134 | encoded | `o 61 r 5(1)(b) on the manner in which proceedings are to be instituted by the claimants against the defendant` (order-61:747) |
| O 61 r 5(1)(c) | 7134-7136 | encoded | `o 61 r 5(1)(c) that an issue between the claimants and the defendant be stated and tried` (order-61:748) |
| O 61 r 5(1)(d) | 7136-7138 | encoded | `o 61 r 5(1)(d) that the matter be adjourned` (order-61:749) |
| O 61 r 5(1)(e) | 7138-7140 | encoded | `o 61 r 5(1)(e) that further advertisements be made in addition to that required under Rule 3(6)` (order-61:750) |
| O 61 r 5(1)(f) | 7140-7142 | encoded | `o 61 r 5(1)(f) for the substitution of the claimant making the application with another claimant` (order-61:751) |
| O 61 r 5(1)(g) | 7142-7144 | encoded | `o 61 r 5(1)(g) that the application be dismissed` (order-61:752) |
| O 61 r 5(2) | 7144-7145 | encoded | `o 61 r 5(2) the Court may make such order as it deems appropriate against the contravening person` (order-61:818) |
| O 61 r 5(3) | 7145-7145 | encoded | `o 61 r 5(3) the Court may declare the claimant forever barred` (order-61:829) |
| O 61 r 6 | 7146-7147 | encoded | `o 61 r 6 the Court may make such order as to costs or any other matter as it thinks just` (order-61:843) |
| O 61 r 7 | 7148-7149 | encoded | `o 61 r 7(1) Order 15 applies to the trial of the issue` (order-61:859); `o 61 r 7(2) the Court may give such judgment or make such order as finally to dispose of all questions` (order-61:868) |
| O 61 r 7(1) | 7149-7149 | encoded | `o 61 r 7(1) Order 15 applies to the trial of the issue` (order-61:859) |
| O 61 r 7(2) | 7149-7149 | encoded | `o 61 r 7(2) the Court may give such judgment or make such order as finally to dispose of all questions` (order-61:868) |
| O 62 | 7150-7302 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 62 r 1 | 7152-7169 | encoded | `o 62 r 1 a proceeding under section 137ZD` (order-62:44); `o 62 r 1 a proceeding under section 232` (order-62:45) (+6 more) |
| O 62 r 1(1) | 7153-7169 | encoded | `o 62 r 1(1) a reference to a section is a reference to a section in the Act` (order-62:64); `o 62 r 1(1) the Act` (order-62:55) |
| O 62 r 1(1) "Act" | 7153-7154 | encoded | `o 62 r 1(1) the Act` (order-62:55) |
| O 62 r 1(1) "Authority" | 7154-7155 | encoded | `o 62 r 1(1) "Authority" who it is` (order-62:74) |
| O 62 r 1(1) "civil penalty action" | 7155-7156 | encoded | `o 62 r 1(1) "civil penalty action" the proceeding is a civil penalty action` (order-62:83) |
| O 62 r 1(1) "Code" | 7156-7157 | encoded | `o 62 r 1(1) "Code" which Code` (order-62:90) |
| O 62 r 1(1) "Commercial Affairs Officer" | 7157-7158 | encoded | `o 62 r 1(1) "Commercial Affairs Officer" the person is a Commercial Affairs Officer` (order-62:96) |
| O 62 r 1(1) "contravening person" | 7158-7168 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "contravening person"(a) | 7158-7160 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "contravening person"(b) | 7160-7162 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "contravening person"(c) | 7162-7164 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "contravening person"(d) | 7164-7166 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "contravening person"(e) | 7166-7168 | encoded | `o 62 r 1(1) "contravening person" the section that gives its meaning` (order-62:116) |
| O 62 r 1(1) "police officer" | 7168-7169 | encoded | `o 62 r 1(1) "police officer" the person is a police officer` (order-62:131) |
| O 62 r 1(2) | 7169-7169 | encoded | `o 62 r 1(2) these Rules apply to the proceeding` (order-62:141) |
| O 62 r 2 | 7170-7186 | encoded | `o 62 r 2(1) the civil penalty action is commenced as the Rule requires` (order-62:155); `o 62 r 2(2) the provision applies to the civil penalty action` (order-62:171) |
| O 62 r 2(1) | 7171-7171 | encoded | `o 62 r 2(1) the civil penalty action is commenced as the Rule requires` (order-62:155) |
| O 62 r 2(2) | 7171-7172 | encoded | `o 62 r 2(2) the provision applies to the civil penalty action` (order-62:171) |
| O 62 r 2(3) | 7172-7182 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(3)(a) | 7172-7174 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(3)(b) | 7174-7176 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(3)(c) | 7176-7178 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(3)(d) | 7178-7180 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(3)(e) | 7180-7182 | encoded | `o 62 r 2(3) the matters the endorsement has not yet stated` (order-62:214); `o 62 r 2(3) the endorsement states what the Rule requires` (order-62:238) |
| O 62 r 2(4) | 7182-7186 | encoded | `o 62 r 2(4) the address for service of the Authority` (order-62:262); `o 62 r 2(4) the Authority sues in another way` (order-62:249) |
| O 62 r 2(4)(a) | 7182-7184 | encoded | `o 62 r 2(4)(a) the Authority sues by a solicitor` (order-62:247) |
| O 62 r 2(4)(b) | 7184-7186 | encoded | `o 62 r 2(4)(b) the Authority sues in person` (order-62:248) |
| O 62 r 2(5) | 7186-7186 | encoded | `o 62 r 2(5) the provision that refers to the consent of the Public Prosecutor` (order-62:273); `o 62 r 2(5) the duty to file the consent of the Public Prosecutor arises` (order-62:290) (+1 more) |
| O 62 r 3 | 7187-7188 | encoded | `o 62 r 3(1) the provision applies to the pleadings in the civil penalty action` (order-62:320); `o 62 r 3(2) the defence applies to the civil penalty action` (order-62:351) |
| O 62 r 3(1) | 7188-7188 | encoded | `o 62 r 3(1) the provision applies to the pleadings in the civil penalty action` (order-62:320) |
| O 62 r 3(2) | 7188-7188 | encoded | `o 62 r 3(2) the defence applies to the civil penalty action` (order-62:351) |
| O 62 r 4 | 7189-7203 | encoded | `o 62 r 4(1) the Authority may apply to the Court for judgment` (order-62:379); `o 62 r 4(1) the Court must give such judgment as the Authority appears entitled to` (order-62:396) |
| O 62 r 4(1) | 7190-7195 | encoded | `o 62 r 4(1) the Authority may apply to the Court for judgment` (order-62:379); `o 62 r 4(1) the Court must give such judgment as the Authority appears entitled to` (order-62:396) |
| O 62 r 4(1)(a) | 7190-7192 | encoded | `o 62 r 4(1) the Authority may apply to the Court for judgment` (order-62:379); `o 62 r 4(1) the Court must give such judgment as the Authority appears entitled to` (order-62:396) |
| O 62 r 4(1)(b) | 7192-7195 | encoded | `o 62 r 4(1) the Authority may apply to the Court for judgment` (order-62:379); `o 62 r 4(1) the Court must give such judgment as the Authority appears entitled to` (order-62:396) |
| O 62 r 4(2) | 7195-7196 | encoded | `o 62 r 4(2) the application is made as the Rule requires` (order-62:407) |
| O 62 r 4(3) | 7196-7201 | encoded | `o 62 r 4(3) the Authority may proceed as if the defendant had filed and served a notice of intention to contest or not contest` (order-62:432) |
| O 62 r 4(3)(a) | 7196-7198 | encoded | `o 62 r 4(3) the Authority may proceed as if the defendant had filed and served a notice of intention to contest or not contest` (order-62:432) |
| O 62 r 4(3)(b) | 7198-7201 | encoded | `o 62 r 4(3) the Authority may proceed as if the defendant had filed and served a notice of intention to contest or not contest` (order-62:432) |
| O 62 r 4(4) | 7201-7202 | fork | fork register: FORK O 62 r 4(4); `o 62 r 4(4) the Authority may enter judgment against the defendant for costs` (order-62:458) |
| O 62 r 4(5) | 7202-7203 | encoded | `o 62 r 4(5) the application for permission is made as the Rule requires` (order-62:476); `o 62 r 4(5) the duty to serve the summons on the defendant arises` (order-62:490) (+1 more) |
| O 62 r 4(6) | 7203-7203 | encoded | `o 62 r 4(6) the provision applies to the civil penalty action` (order-62:519) |
| O 62 r 5 | 7204-7210 | encoded | `o 62 r 5(1) the Authority may apply to the Court for judgment` (order-62:544); `o 62 r 5(1) the Court must give such judgment as the Authority appears entitled to` (order-62:556) |
| O 62 r 5(1) | 7205-7205 | encoded | `o 62 r 5(1) the Authority may apply to the Court for judgment` (order-62:544); `o 62 r 5(1) the Court must give such judgment as the Authority appears entitled to` (order-62:556) |
| O 62 r 5(2) | 7205-7209 | encoded | `o 62 r 5(2) the Authority may take the course` (order-62:581) |
| O 62 r 5(2)(a) | 7205-7207 | encoded | `o 62 r 5(2)(a) apply for judgment against the defendant in default and proceed against the others` (order-62:562) |
| O 62 r 5(2)(b) | 7207-7209 | encoded | `o 62 r 5(2)(b) set down the action for judgment against the defendant in default with the others` (order-62:563) |
| O 62 r 5(3) | 7209-7210 | encoded | `o 62 r 5(3) the application is made as the Rule requires` (order-62:595) |
| O 62 r 5(4) | 7210-7210 | encoded | `o 62 r 5(4) the provision applies to the civil penalty action` (order-62:609) |
| O 62 r 6 | 7211-7212 | encoded | `o 62 r 6 the Authority is required to make or add a person as a defendant` (order-62:630) |
| O 62 r 7 | 7213-7214 | encoded | `o 62 r 7(1) the third party notice may be issued` (order-62:645); `o 62 r 7(2) the application for permission is made and served as the Rule requires` (order-62:662) (+1 more) |
| O 62 r 7(1) | 7214-7214 | encoded | `o 62 r 7(1) the third party notice may be issued` (order-62:645) |
| O 62 r 7(2) | 7214-7214 | encoded | `o 62 r 7(2) the application for permission is made and served as the Rule requires` (order-62:662); `o 62 r 7(2) the form of the summons` (order-62:653) |
| O 62 r 8 | 7215-7287 | encoded | `o 62 r 8(1) Order 11 applies to the civil penalty action` (order-62:681); `o 62 r 8(2) the Authority may be required to give production of documents or produce them for inspection` (order-62:692) |
| O 62 r 8(1) | 7216-7216 | encoded | `o 62 r 8(1) Order 11 applies to the civil penalty action` (order-62:681) |
| O 62 r 8(2) | 7216-7217 | encoded | `o 62 r 8(2) the Authority may be required to give production of documents or produce them for inspection` (order-62:692) |
| O 62 r 8(3) | 7217-7218 | encoded | `o 62 r 8(3) the order requires disclosure of the document` (order-62:705) |
| O 62 r 8(4) | 7218-7240 | encoded | `o 62 r 8(4) the Authority may be ordered to give production of the document or produce it for inspection` (order-62:752); `o 62 r 8(4) a document of another kind` (order-62:723) |
| O 62 r 8(4)(a) | 7218-7220 | encoded | `o 62 r 8(4)(a) a book voluntarily produced by the defendant or contravening person to the Authority` (order-62:712) |
| O 62 r 8(4)(b) | 7220-7222 | encoded | `o 62 r 8(4)(b) a book produced by or seized from any person pursuant to section 163, 163A or 164` (order-62:713) |
| O 62 r 8(4)(c) | 7222-7224 | encoded | `o 62 r 8(4)(c) an acknowledgment of receipt issued by the Authority for a book referred to in (a) or (b)` (order-62:714) |
| O 62 r 8(4)(d) | 7224-7226 | encoded | `o 62 r 8(4)(d) correspondence between the Authority or its solicitors and the defendant or contravening person, or their agents or solicitors` (order-62:715) |
| O 62 r 8(4)(e) | 7226-7228 | encoded | `o 62 r 8(4)(e) an examination requirement served on the defendant or contravening person pursuant to section 154` (order-62:716) |
| O 62 r 8(4)(f) | 7228-7230 | encoded | `o 62 r 8(4)(f) a production requirement served on the defendant or contravening person pursuant to section 163` (order-62:717) |
| O 62 r 8(4)(g) | 7230-7232 | encoded | `o 62 r 8(4)(g) a written notice or written production requirement in respect of the premises pursuant to section 163A` (order-62:718) |
| O 62 r 8(4)(h) | 7232-7234 | encoded | `o 62 r 8(4)(h) a warrant issued in respect of the premises pursuant to section 164` (order-62:719) |
| O 62 r 8(4)(i) | 7234-7236 | encoded | `o 62 r 8(4)(i) a written record made pursuant to section 158 of statements made to the Authority` (order-62:720) |
| O 62 r 8(4)(j) | 7236-7238 | encoded | `o 62 r 8(4)(j) trading information relating to the trading activities which the Authority relies on or will rely on in the action` (order-62:721) |
| O 62 r 8(4)(k) | 7238-7240 | encoded | `o 62 r 8(4)(k) any other document which the Authority relies on or will rely on in the action` (order-62:722) |
| O 62 r 8(5) | 7240-7267 | encoded | `o 62 r 8(5) the Authority may be ordered to give production of the document or produce it for inspection` (order-62:809); `o 62 r 8(5) a document of another kind` (order-62:775) |
| O 62 r 8(5)(a) | 7240-7242 | encoded | `o 62 r 8(5)(a) a book voluntarily produced by the defendant or contravening person to a Commercial Affairs Officer or a police officer` (order-62:762) |
| O 62 r 8(5)(b) | 7242-7244 | encoded | `o 62 r 8(5)(b) a book or document produced by any person to such an officer under section 20 of the Code` (order-62:763) |
| O 62 r 8(5)(c) | 7244-7246 | encoded | `o 62 r 8(5)(c) a book or document seized by such an officer under section 35 of the Code` (order-62:764) |
| O 62 r 8(5)(d) | 7246-7248 | encoded | `o 62 r 8(5)(d) a book or document placed in safe custody by such an officer under section 78 of the Code` (order-62:765) |
| O 62 r 8(5)(e) | 7248-7257 | encoded | `o 62 r 8(5)(e)(i) an acknowledgment of receipt for a book or document referred to in (a), (b), (c) or (d)` (order-62:766); `o 62 r 8(5)(e)(ii) an acknowledgment of receipt for any other thing produced under section 20 of the Code` (order-62:767) |
| O 62 r 8(5)(e)(i) | 7249-7251 | encoded | `o 62 r 8(5)(e)(i) an acknowledgment of receipt for a book or document referred to in (a), (b), (c) or (d)` (order-62:766) |
| O 62 r 8(5)(e)(ii) | 7251-7253 | encoded | `o 62 r 8(5)(e)(ii) an acknowledgment of receipt for any other thing produced under section 20 of the Code` (order-62:767) |
| O 62 r 8(5)(e)(iii) | 7253-7255 | encoded | `o 62 r 8(5)(e)(iii) an acknowledgment of receipt for any other property seized under section 35 of the Code` (order-62:768) |
| O 62 r 8(5)(e)(iv) | 7255-7257 | encoded | `o 62 r 8(5)(e)(iv) an acknowledgment of receipt for any other article placed in safe custody under section 78 of the Code` (order-62:769) |
| O 62 r 8(5)(f) | 7257-7259 | encoded | `o 62 r 8(5)(f) a written order issued by such an officer under section 20 of the Code` (order-62:770) |
| O 62 r 8(5)(g) | 7259-7261 | encoded | `o 62 r 8(5)(g) a written order issued to the defendant or contravening person by such an officer under section 21 of the Code` (order-62:771) |
| O 62 r 8(5)(h) | 7261-7263 | encoded | `o 62 r 8(5)(h) a statement made by any person to such an officer under section 22 of the Code` (order-62:772) |
| O 62 r 8(5)(i) | 7263-7265 | encoded | `o 62 r 8(5)(i) a statement made by the defendant or contravening person to such an officer under section 23 of the Code` (order-62:773) |
| O 62 r 8(5)(j) | 7265-7267 | encoded | `o 62 r 8(5)(j) a search warrant issued in respect of the premises under section 24 of the Code` (order-62:774) |
| O 62 r 8(6) | 7267-7286 | fork | fork register: FORK O 62 r 8(6); `o 62 r 8(6) an order may be made for the Authority to give production of the document or produce it for inspection` (order-62:864); `o 62 r 8(6) none of these descriptions` (order-62:828) |
| O 62 r 8(6)(a) | 7267-7269 | encoded | `o 62 r 8(6)(a) a document in the Authority's possession, custody or power as a result of its supervisory functions, duties or powers under a written law other than the Act` (order-62:819) |
| O 62 r 8(6)(b) | 7269-7271 | encoded | `o 62 r 8(6)(b) a complaint or request received by the Authority to investigate or provide assistance on a possible or alleged contravention of the Act, or a similar document received by the Authority` (order-62:820) |
| O 62 r 8(6)(c) | 7271-7273 | encoded | `o 62 r 8(6)(c) the Authority's internal books` (order-62:821) |
| O 62 r 8(6)(d) | 7273-7275 | encoded | `o 62 r 8(6)(d) correspondence between the Authority and the Government or a statutory body` (order-62:822) |
| O 62 r 8(6)(e) | 7275-7277 | encoded | `o 62 r 8(6)(e) a document sent by the Authority to the Government or a statutory body but not provided under section 168B` (order-62:823) |
| O 62 r 8(6)(f) | 7277-7279 | encoded | `o 62 r 8(6)(f) a document received by the Authority from the Government or a statutory body but not referred to in paragraph (5)` (order-62:824) |
| O 62 r 8(6)(g) | 7279-7286 | encoded | `o 62 r 8(6)(g)(i) correspondence between the Authority and an overseas regulatory authority` (order-62:825); `o 62 r 8(6)(g)(ii) correspondence between the Authority and a securities exchange, futures exchange or clearing house` (order-62:826) |
| O 62 r 8(6)(g)(i) | 7280-7282 | encoded | `o 62 r 8(6)(g)(i) correspondence between the Authority and an overseas regulatory authority` (order-62:825) |
| O 62 r 8(6)(g)(ii) | 7282-7284 | encoded | `o 62 r 8(6)(g)(ii) correspondence between the Authority and a securities exchange, futures exchange or clearing house` (order-62:826) |
| O 62 r 8(6)(g)(iii) | 7284-7286 | encoded | `o 62 r 8(6)(g)(iii) correspondence between the Authority and the complainant` (order-62:827) |
| O 62 r 8(7) | 7286-7287 | encoded | `o 62 r 8(7) paragraph (6) affects the operation of the Evidence Act` (order-62:880) |
| O 62 r 8(8) | 7287-7287 | encoded | `o 62 r 8(8) "book" the provision that gives its meaning` (order-62:887) |
| O 62 r 8(8) "book" | 7287-7287 | encoded | `o 62 r 8(8) "book" the provision that gives its meaning` (order-62:887) |
| O 62 r 9 | 7288-7289 | encoded | `o 62 r 9 Order 9 applies to the civil penalty action` (order-62:897) |
| O 62 r 10 | 7290-7291 | encoded | `o 62 r 10 the provision applies to the civil penalty action` (order-62:907) |
| O 62 r 11 | 7292-7293 | encoded | `o 62 r 11 the duty to file the consent of the Public Prosecutor arises` (order-62:922); `o 62 r 11 the Authority files the consent as the Rule requires` (order-62:932) |
| O 62 r 12 | 7294-7302 | encoded | `o 62 r 12(1) an order may be made for the costs of the defendant to be paid by the Authority` (order-62:955); `o 62 r 12(2) the Court may make such order as to costs as it thinks just` (order-62:968) |
| O 62 r 12(1) | 7295-7295 | fork | fork register: FORK O 62 r 12(1); `o 62 r 12(1) an order may be made for the costs of the defendant to be paid by the Authority` (order-62:955) |
| O 62 r 12(2) | 7295-7296 | encoded | `o 62 r 12(2) the Court may make such order as to costs as it thinks just` (order-62:968) |
| O 62 r 12(3) | 7296-7301 | encoded | `o 62 r 12(3) the costs include the item` (order-62:991) |
| O 62 r 12(3)(a) | 7296-7298 | encoded | `o 62 r 12(3) the costs include the item` (order-62:991) |
| O 62 r 12(3)(b) | 7298-7301 | encoded | `o 62 r 12(3) the costs include the item` (order-62:991) |
| O 62 r 12(4) | 7301-7302 | encoded | `o 62 r 12(4) the costs are in accordance with the scale of fees` (order-62:1006); `o 62 r 12(4) the costs may be assessed in accordance with Order 21` (order-62:1019) |
| O 62 r 12(5) | 7302-7302 | encoded | `o 62 r 12(5) the duty to pay the costs to the Authority arises` (order-62:1031); `o 62 r 12(5) the costs are paid to the Authority as the Rule requires` (order-62:1045) |
| O 63 | 7303-7399 | inert | reason 1 (not operative): the Order's number and title; its rules have their own rows |
| O 63 r 1 | 7305-7311 | encoded | `o 63 r 1(1) a reference to a section is a reference to a section in the Act` (order-63:49); `o 63 r 1(1) the Act` (order-63:40) (+1 more) |
| O 63 r 1(1) | 7306-7311 | encoded | `o 63 r 1(1) a reference to a section is a reference to a section in the Act` (order-63:49); `o 63 r 1(1) the Act` (order-63:40) (+1 more) |
| O 63 r 1(1) "Act" | 7306-7307 | encoded | `o 63 r 1(1) the Act` (order-63:40) |
| O 63 r 1(1) "Authority" | 7307-7308 | encoded | `o 63 r 1(1) the Authority` (order-63:59) |
| O 63 r 1(1) "claimant" | 7308-7309 | encoded | `o 63 r 1(1) "claimant" the section that gives its meaning` (order-63:63) |
| O 63 r 1(1) "order for disgorgement" | 7309-7310 | encoded | `o 63 r 1(1) "order for disgorgement" the order is an order for disgorgement` (order-63:75) |
| O 63 r 1(1) "third party" | 7310-7311 | encoded | `o 63 r 1(1) "third party" the section that gives its meaning` (order-63:67) |
| O 63 r 1(2) | 7311-7311 | encoded | `o 63 r 1(2) these Rules apply to the proceeding` (order-63:84) |
| O 63 r 2 | 7312-7339 | encoded | `o 63 r 2(1) the application for an order for disgorgement may be made in this way` (order-63:101); `o 63 r 2(2) the provision applies to the originating application` (order-63:116) |
| O 63 r 2(1) | 7313-7313 | encoded | `o 63 r 2(1) the application for an order for disgorgement may be made in this way` (order-63:101) |
| O 63 r 2(2) | 7313-7314 | encoded | `o 63 r 2(2) the provision applies to the originating application` (order-63:116) |
| O 63 r 2(3) | 7314-7332 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(a) | 7314-7323 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(a)(i) | 7315-7317 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(a)(ii) | 7317-7319 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(a)(iii) | 7319-7321 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(a)(iv) | 7321-7323 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(b) | 7323-7332 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(b)(i) | 7324-7326 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(b)(ii) | 7326-7328 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(b)(iii) | 7328-7330 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(3)(b)(iv) | 7330-7332 | encoded | `o 63 r 2(3) the matters the affidavit has not yet set out` (order-63:166); `o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires` (order-63:199) |
| O 63 r 2(4) | 7332-7337 | encoded | `o 63 r 2(4) the period for serving the application before the hearing` (order-63:213); `o 63 r 2(4) the duty to serve the application personally in time arises` (order-63:222) (+2 more) |
| O 63 r 2(4)(a) | 7332-7334 | encoded | `o 63 r 2(4) the period for serving the application before the hearing` (order-63:213); `o 63 r 2(4) the duty to serve the application personally in time arises` (order-63:222) (+2 more) |
| O 63 r 2(4)(b) | 7334-7337 | encoded | `o 63 r 2(4) the period for serving the application before the hearing` (order-63:213); `o 63 r 2(4) the duty to serve the application personally in time arises` (order-63:222) (+2 more) |
| O 63 r 2(5) | 7337-7338 | encoded | `o 63 r 2(5) the application is deemed dismissed` (order-63:267) |
| O 63 r 2(6) | 7338-7339 | fork | fork register: FORK O 63 r 2(6); `o 63 r 2(6) the Court may direct the applicant to serve a notice to show cause on the third party` (order-63:284); `o 63 r 2(6) the form of the notice to show cause` (order-63:277) |
| O 63 r 2(7) | 7339-7339 | encoded | `o 63 r 2(7) the person may show cause by affidavit or otherwise to the satisfaction of the Court` (order-63:293) |
| O 63 r 3 | 7340-7349 | encoded | `o 63 r 3(1) the person may apply for directions on claims for compensation` (order-63:310); `o 63 r 3(1) the Court may fix a return date for hearing the application` (order-63:323) |
| O 63 r 3(1) | 7341-7341 | encoded | `o 63 r 3(1) the person may apply for directions on claims for compensation` (order-63:310); `o 63 r 3(1) the Court may fix a return date for hearing the application` (order-63:323) |
| O 63 r 3(2) | 7341-7342 | encoded | `o 63 r 3(2) the application for directions is made as the Rule requires` (order-63:336) |
| O 63 r 3(3) | 7342-7347 | encoded | `o 63 r 3(3) the period for serving the application before the return date` (order-63:351); `o 63 r 3(3) the duty to serve the application personally in time arises` (order-63:360) (+2 more) |
| O 63 r 3(3)(a) | 7342-7344 | encoded | `o 63 r 3(3) the period for serving the application before the return date` (order-63:351); `o 63 r 3(3) the duty to serve the application personally in time arises` (order-63:360) (+2 more) |
| O 63 r 3(3)(b) | 7344-7347 | encoded | `o 63 r 3(3) the period for serving the application before the return date` (order-63:351); `o 63 r 3(3) the duty to serve the application personally in time arises` (order-63:360) (+2 more) |
| O 63 r 3(4) | 7347-7348 | encoded | `o 63 r 3(4) the period for advertising the application before the return date` (order-63:403); `o 63 r 3(4) the application is advertised as the Rule requires` (order-63:416) (+2 more) |
| O 63 r 3(5) | 7348-7349 | encoded | `o 63 r 3(5) the matters the advertisement has not yet stated` (order-63:444); `o 63 r 3(5) the advertisement states what the Rule requires` (order-63:454) (+1 more) |
| O 63 r 3(6) | 7349-7349 | fork | fork register: FORK O 63 r 3(6); `o 63 r 3(6) the application is deemed dismissed` (order-63:473); `o 63 r 3(6) the Court must cancel the appointment of the time and place for the hearing` (order-63:488) |
| O 63 r 4 | 7350-7365 | encoded | `o 63 r 4(1) the period for filing the affidavit of claim before the return date` (order-63:502); `o 63 r 4(1) the duty to file an affidavit of claim arises` (order-63:511) (+1 more) |
| O 63 r 4(1) | 7351-7351 | encoded | `o 63 r 4(1) the period for filing the affidavit of claim before the return date` (order-63:502); `o 63 r 4(1) the duty to file an affidavit of claim arises` (order-63:511) (+1 more) |
| O 63 r 4(2) | 7351-7359 | encoded | `o 63 r 4(2) the matters the affidavit has not yet covered` (order-63:555); `o 63 r 4(2) the affidavit of claim covers what the Rule requires` (order-63:575) |
| O 63 r 4(2)(a) | 7351-7353 | encoded | `o 63 r 4(2) the matters the affidavit has not yet covered` (order-63:555); `o 63 r 4(2) the affidavit of claim covers what the Rule requires` (order-63:575) |
| O 63 r 4(2)(b) | 7353-7355 | encoded | `o 63 r 4(2) the matters the affidavit has not yet covered` (order-63:555); `o 63 r 4(2) the affidavit of claim covers what the Rule requires` (order-63:575) |
| O 63 r 4(2)(c) | 7355-7357 | encoded | `o 63 r 4(2) the matters the affidavit has not yet covered` (order-63:555); `o 63 r 4(2) the affidavit of claim covers what the Rule requires` (order-63:575) |
| O 63 r 4(2)(d) | 7357-7359 | encoded | `o 63 r 4(2) the matters the affidavit has not yet covered` (order-63:555); `o 63 r 4(2) the affidavit of claim covers what the Rule requires` (order-63:575) |
| O 63 r 4(3) | 7359-7365 | encoded | `o 63 r 4(3) the exhibits may include` (order-63:595); `o 63 r 4(3) another exhibit` (order-63:584) |
| O 63 r 4(3)(a) | 7359-7361 | encoded | `o 63 r 4(3)(a) trade notes or slips` (order-63:581) |
| O 63 r 4(3)(b) | 7361-7363 | encoded | `o 63 r 4(3)(b) statements of accounts for the relevant period` (order-63:582) |
| O 63 r 4(3)(c) | 7363-7365 | encoded | `o 63 r 4(3)(c) copies of instructions given to a broker or remisier` (order-63:583) |
| O 63 r 4(4) | 7365-7365 | encoded | `o 63 r 4(4) the period for serving a copy of the affidavit on the third party` (order-63:602); `o 63 r 4(4) the claimant serves a copy of the affidavit on the third party in time` (order-63:613) (+3 more) |
| O 63 r 5 | 7366-7393 | encoded | `o 63 r 5(1) the Court may give directions or make orders after the hearing` (order-63:693); `o 63 r 5(1) the Court may give this kind of direction or make this kind of order` (order-63:730) (+2 more) |
| O 63 r 5(1) | 7367-7388 | fork | fork register: FORK O 63 r 5(1); `o 63 r 5(1) the Court may give directions or make orders after the hearing` (order-63:693); `o 63 r 5(1) the Court may give this kind of direction or make this kind of order` (order-63:730) (+2 more) |
| O 63 r 5(1)(a) | 7367-7369 | encoded | `o 63 r 5(1)(a) the hearing of an application under Rule 2(1)` (order-63:648) |
| O 63 r 5(1)(b) | 7369-7371 | encoded | `o 63 r 5(1)(b) the hearing of the third party under Rule 2(7)` (order-63:649) |
| O 63 r 5(1)(c) | 7371-7374 | encoded | `o 63 r 5(1)(c) the hearing of an application under Rule 3(1)` (order-63:650) |
| O 63 r 5(1)(d) | 7374-7376 | encoded | `o 63 r 5(1)(d) for the filing of such further affidavits as the Court considers necessary` (order-63:654) |
| O 63 r 5(1)(e) | 7376-7378 | encoded | `o 63 r 5(1)(e) on the manner in which proceedings are to be instituted against the third party` (order-63:655) |
| O 63 r 5(1)(f) | 7378-7380 | encoded | `o 63 r 5(1)(f) that an issue be stated and tried` (order-63:656) |
| O 63 r 5(1)(g) | 7380-7382 | encoded | `o 63 r 5(1)(g) that the matter be adjourned` (order-63:657) |
| O 63 r 5(1)(h) | 7382-7384 | encoded | `o 63 r 5(1)(h) that further advertisements be made in addition to that required under Rule 3(4)` (order-63:658) |
| O 63 r 5(1)(i) | 7384-7386 | encoded | `o 63 r 5(1)(i) for the substitution of the claimant making the application under Rule 2(1) or 3(1) with another claimant` (order-63:659) |
| O 63 r 5(1)(j) | 7386-7388 | encoded | `o 63 r 5(1)(j) that the application under Rule 2(1) or 3(1) be dismissed` (order-63:660) |
| O 63 r 5(2) | 7388-7393 | encoded | `o 63 r 5(2) the Court may make such order as it deems appropriate` (order-63:751) |
| O 63 r 5(2)(a) | 7388-7390 | encoded | `o 63 r 5(2) the Court may make such order as it deems appropriate` (order-63:751) |
| O 63 r 5(2)(b) | 7390-7393 | encoded | `o 63 r 5(2) the Court may make such order as it deems appropriate` (order-63:751) |
| O 63 r 5(3) | 7393-7393 | encoded | `o 63 r 5(3) the Court may declare the claimant forever barred` (order-63:765) |
| O 63 r 6 | 7394-7395 | encoded | `o 63 r 6 the Court may make such order as to costs or any other matter as it thinks just` (order-63:779) |
| O 63 r 7 | 7396-7397 | encoded | `o 63 r 7(1) Order 15 applies to the trial of the issue` (order-63:795); `o 63 r 7(2) the Court may give such judgment or make such order as finally to dispose of all questions` (order-63:804) |
| O 63 r 7(1) | 7397-7397 | encoded | `o 63 r 7(1) Order 15 applies to the trial of the issue` (order-63:795) |
| O 63 r 7(2) | 7397-7397 | encoded | `o 63 r 7(2) the Court may give such judgment or make such order as finally to dispose of all questions` (order-63:804) |
| O 63 r 8 | 7398-7399 | encoded | `o 63 r 8(1) a rule of Order 62 applies to the application` (order-63:819); `o 63 r 8(2) a reference to the defendant in Order 62 rule 8 is a reference to` (order-63:836) |
| O 63 r 8(1) | 7399-7399 | encoded | `o 63 r 8(1) a rule of Order 62 applies to the application` (order-63:819) |
| O 63 r 8(2) | 7399-7399 | encoded | `o 63 r 8(2) a reference to the defendant in Order 62 rule 8 is a reference to` (order-63:836) |

## Fork register (roc11)

### The rulings of 2026-11-04 and 2026-11-05, word for word from the brief

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### Where option B of E1 was used by hand

Option B (gathering a legal effect's routes by hand, plain L4, no language construct) was used in two places: `o 57 r 2 the power under section 48M may be exercised by the person` gathers paragraphs (1) and (2) of O 57 r 2, and `o 57 r 3 the instrument is a Direction, a Notice or a Decision` gathers limbs (a), (b) and (c) of O 57 r 3.
Every other legal effect is answered section by section (option C).

### The periods ruling and the keel

The brief (ruling (a) of 2026-11-05) says a period the text fixes in its own words gives `JUST FALSE` outside the period; roc11 follows the brief (for example `o 62 r 4(1)`, `o 59 r 2(2)`, `o 59 r 13(2)`).
PLAN.md section 2 now agrees with ruling (a): a stated period answers `JUST FALSE` outside it.
Every "... in time" function in layer 1 (`o 57 r 8(1)`, `o 57 r 12`, `o 57 r 13`, `o 60 r 8(1)`, `o 61 r 4(1)`, `o 61 r 4(4)`, `o 63 r 4(1)`, `o 63 r 4(4)`, and the others in the Marginal readings table under "period fixed in the text's own words") answers `JUST TRUE` inside the period and `JUST FALSE` outside it.
Where such a function answers `NOTHING`, it is for a reason other than the period: the time has not yet run out and the act is not yet done, or the duty does not arise at all (QD).
The keel's own period functions (for example `o 6 r 6(1)`) were not read or called by roc11, so I have not checked what they answer outside their periods; whoever merges the parts should align them with ruling (a) if they differ.
roc11 does not call those functions: every period is an input date (see Seams).

### Judgment calls

Format: `question | provision | function | file:line | answer taken | other reading`.
The line is the line of the function's definition in the named layer-1 file; the tag that licenses the line is in a comment inside or just above the function.
A tag in a function is a place a lawyer can overrule; none is mentioned in a function name or a `@desc`.

Counts: QA 12, QB 76, QC 3, QD 16, QE 2, QF not applicable.

```
QA | O 57 r 8(2) | o 57 r 8(2) the person seeking to enforce may apply for an enforcement order without the permission of the Court | roc11-order-57.l4:783 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE (the exception permits it)
QA | O 59 r 4(2) | o 59 r 4(2) the counterclaim may be made or the set-off pleaded | roc11-order-59.l4:356 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE (the exception permits it).
QA | O 59 r 7(1) | o 59 r 7(1) judgment in default may be entered against the Government | roc11-order-59.l4:633 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE.
QA | O 59 r 7(2) | o 59 r 7(2) Order 10 rule 5(1)(a) applies | roc11-order-59.l4:647 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE
QA | O 59 r 8(1) | o 59 r 8(1) the third party notice may be issued | roc11-order-59.l4:686 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE
QA | O 59 r 8(2) | o 59 r 8(2) the Court may grant permission to issue the notice | roc11-order-59.l4:715 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE.
QA | O 60 r 4 | o 60 r 4 the Court may order the judgment creditor to give security for costs | roc11-order-60.l4:204 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST FALSE
QA | O 60 r 8(1) | o 60 r 8(1) the judgment creditor may apply for an enforcement order without the permission of the Court | roc11-order-60.l4:455 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE (the exception permits it)
QA | O 61 r 6 | o 61 r 6 the Court may make such order as to costs or any other matter as it thinks just | roc11-order-61.l4:843 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST FALSE
QA | O 62 r 7(1) | o 62 r 7(1) the third party notice may be issued | roc11-order-62.l4:645 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE
QA | O 62 r 8(6) | o 62 r 8(6) an order may be made for the Authority to give production of the document or produce it for inspection | roc11-order-62.l4:864 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST TRUE
QA | O 63 r 6 | o 63 r 6 the Court may make such order as to costs or any other matter as it thinks just | roc11-order-63.l4:779 | NOTHING when the "unless" or "except" is met (a lifted bar grants nothing) | JUST FALSE
QB | O 57 r 3 | o 57 r 3 the application to register is made in the way the Rule requires | roc11-order-57.l4:237 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 4(1) | o 57 r 4(1) the affidavit supporting the application states what the Rule requires | roc11-order-57.l4:329 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 4(2) | o 57 r 4(2) the affidavit makes the additional statement the Rule requires | roc11-order-57.l4:361 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 5(1) | o 57 r 5(1) the order for registration is drawn up and served as the Rule requires | roc11-order-57.l4:532 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 5(2) | o 57 r 5(2) the order for registration states and notifies what the Rule requires | roc11-order-57.l4:553 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 6 | o 57 r 6 the register kept in the Registry contains the registered item | roc11-order-57.l4:589 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 7(1) | o 57 r 7(1) the notice of registration is served as the Rule requires | roc11-order-57.l4:609 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 7(3) | o 57 r 7(3) the notice of registration states what the Rule requires | roc11-order-57.l4:679 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 8(1) | o 57 r 8(1) the endorsement is what the Rule requires | roc11-order-57.l4:744 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 8(3) | o 57 r 8(3) the affidavit of service states the date of endorsement | roc11-order-57.l4:793 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 9(1) | o 57 r 9(1) the application to set aside the registration is made as the Rule requires | roc11-order-57.l4:807 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 10(3) | o 57 r 10(3) the party applying for an enforcement order has produced what the Rule requires | roc11-order-57.l4:878 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 57 r 11(3) | o 57 r 11(3) the affidavit states what the Rule requires | roc11-order-57.l4:992 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 58 r 2 | o 58 r 2 the application is made as the Rule requires | roc11-order-58.l4:69 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 58 r 3 | o 58 r 3 the statement of claim gives the particulars | roc11-order-58.l4:142 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 2(1) | o 59 r 2(1) the endorsement of claim states what the Rule requires | roc11-order-59.l4:143 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 2(3)(b) | o 59 r 2(3)(b) the claimant's application is made and served as the Rule requires | roc11-order-59.l4:221 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 3(2) | o 59 r 3(2) service on the Government is effected as the Rule requires | roc11-order-59.l4:266 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 4(3) | o 59 r 4(3) the application for permission is made as the Rule requires | roc11-order-59.l4:369 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 5(2) | o 59 r 5(2) the affidavit in support is made by a person the Rule allows | roc11-order-59.l4:421 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 6(2) | o 59 r 6(2) the application is made as the Rule requires | roc11-order-59.l4:447 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 6(3) | o 59 r 6(3) the person is made defendant as the Rule requires | roc11-order-59.l4:460 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 6(4) | o 59 r 6(4) the originating application is what the Rule requires | roc11-order-59.l4:500 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 6(6) | o 59 r 6(6) the order names a time as the Rule requires | roc11-order-59.l4:565 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 7(3) | o 59 r 7(3) the application for permission is made and served as the Rule requires | roc11-order-59.l4:665 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 8(1) | o 59 r 8(1) the application for permission is made and served as the Rule requires | roc11-order-59.l4:701 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 9(2) | o 59 r 9(2) the affidavit verifying the list is made by the officer the Court directed | roc11-order-59.l4:743 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 11(3) | o 59 r 11(3) the certificate is in the form the Rule requires | roc11-order-59.l4:804 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 12(2) | o 59 r 12(2) the application is made and served as the Rule requires | roc11-order-59.l4:869 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 59 r 13(1) | o 59 r 13(1) the application is made as the Rule requires | roc11-order-59.l4:909 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 2 | o 60 r 2 the application for registration is made in the way the Rule requires | roc11-order-60.l4:85 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 3(1) | o 60 r 3(1) the affidavit supporting the application states what the Rule requires | roc11-order-60.l4:154 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 3(2) | o 60 r 3(2) the affidavit states the provisions in respect of which registration is sought | roc11-order-60.l4:177 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 3(3) | o 60 r 3(3) the affidavit is accompanied by the other evidence the Rule requires | roc11-order-60.l4:191 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 5(1) | o 60 r 5(1) the order giving permission to register is drawn up and served as the Rule requires | roc11-order-60.l4:221 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 5(2) | o 60 r 5(2) the order states the period and contains the notification | roc11-order-60.l4:231 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 6(1) | o 60 r 6(1) the register kept in the Registry contains the judgment | roc11-order-60.l4:256 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 6(2) | o 60 r 6(2) the register includes particulars of the enforcement order | roc11-order-60.l4:269 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 7(1) | o 60 r 7(1) the notice of registration is served as the Rule requires | roc11-order-60.l4:289 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 7(3) | o 60 r 7(3) the notice of registration states what the Rule requires | roc11-order-60.l4:355 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 8(1) | o 60 r 8(1) the endorsement is what the Rule requires | roc11-order-60.l4:420 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 8(2) | o 60 r 8(2) the affidavit of service states the date of endorsement | roc11-order-60.l4:465 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 9(1) | o 60 r 9(1) the application to set aside the registration is made as the Rule requires | roc11-order-60.l4:479 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 10(3) | o 60 r 10(3) the party applying for an enforcement order has produced what the Rule requires | roc11-order-60.l4:537 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 13(1) | o 60 r 13(1) the application for certified copies is made in the way the Rule requires | roc11-order-60.l4:638 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 13(2) | o 60 r 13(2) the affidavit supporting the application covers what the Rule requires | roc11-order-60.l4:708 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 60 r 13(3) | o 60 r 13(3) the certified copies and certificate are what the Rule requires | roc11-order-60.l4:782 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(1) | o 61 r 2(1) the action is commenced as the Rule requires | roc11-order-61.l4:185 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(2) | o 61 r 2(2) the application for permission is made as the Rule requires | roc11-order-61.l4:200 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(4) | o 61 r 2(4) the affidavit supporting the application sets out what the Rule requires | roc11-order-61.l4:275 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(5) | o 61 r 2(5) the application is served as the Rule requires in the first instance | roc11-order-61.l4:288 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(6) | o 61 r 2(6) the application to continue the stayed action is made as the Rule requires | roc11-order-61.l4:304 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 2(7) | o 61 r 2(7) the application to continue is served as the Rule requires in the first instance | roc11-order-61.l4:319 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 3(3) | o 61 r 3(3) the application for directions is made as the Rule requires | roc11-order-61.l4:411 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 3(5) | o 61 r 3(5) the application is served as the Rule requires | roc11-order-61.l4:469 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 3(6) | o 61 r 3(6) the application is advertised as the Rule requires | roc11-order-61.l4:507 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 3(7) | o 61 r 3(7) the advertisement states what the Rule requires | roc11-order-61.l4:545 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 61 r 4(2) | o 61 r 4(2) the affidavit of claim covers what the Rule requires | roc11-order-61.l4:670 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 2(1) | o 62 r 2(1) the civil penalty action is commenced as the Rule requires | roc11-order-62.l4:155 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 2(3) | o 62 r 2(3) the endorsement states what the Rule requires | roc11-order-62.l4:238 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 2(5) | o 62 r 2(5) the Authority files the consent as the Rule requires | roc11-order-62.l4:300 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 4(2) | o 62 r 4(2) the application is made as the Rule requires | roc11-order-62.l4:407 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 4(5) | o 62 r 4(5) the application for permission is made as the Rule requires | roc11-order-62.l4:476 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 4(5) | o 62 r 4(5) the summons is served on the defendant as the Rule requires | roc11-order-62.l4:505 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 5(3) | o 62 r 5(3) the application is made as the Rule requires | roc11-order-62.l4:595 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 7(2) | o 62 r 7(2) the application for permission is made and served as the Rule requires | roc11-order-62.l4:662 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 11 | o 62 r 11 the Authority files the consent as the Rule requires | roc11-order-62.l4:932 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 12(4) | o 62 r 12(4) the costs are in accordance with the scale of fees | roc11-order-62.l4:1006 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 62 r 12(5) | o 62 r 12(5) the costs are paid to the Authority as the Rule requires | roc11-order-62.l4:1045 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 2(3) | o 63 r 2(3) the affidavit supporting the application sets out what the Rule requires | roc11-order-63.l4:199 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 2(4) | o 63 r 2(4) the application and affidavit are served as the Rule requires | roc11-order-63.l4:240 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 3(2) | o 63 r 3(2) the application for directions is made as the Rule requires | roc11-order-63.l4:336 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 3(3) | o 63 r 3(3) the application is served as the Rule requires | roc11-order-63.l4:378 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 3(4) | o 63 r 3(4) the application is advertised as the Rule requires | roc11-order-63.l4:416 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 3(5) | o 63 r 3(5) the advertisement states what the Rule requires | roc11-order-63.l4:454 | NOTHING for a bare "must" not done | JUST FALSE
QB | O 63 r 4(2) | o 63 r 4(2) the affidavit of claim covers what the Rule requires | roc11-order-63.l4:575 | NOTHING for a bare "must" not done | JUST FALSE
QC | O 61 r 1(1) | o 61 r 1(1) "claimant" the section that gives its meaning | roc11-order-61.l4:86 | NOTHING when no paragraph of the list holds | JUST FALSE (the definition is the list); a STRING cannot carry JUST FALSE, so the other reading would need a yes/no twin
QC | O 62 r 1(1) | o 62 r 1(1) "contravening person" the section that gives its meaning | roc11-order-62.l4:116 | NOTHING when no paragraph of the list holds | JUST FALSE (the definition is the list); a STRING cannot carry JUST FALSE, so the other reading would need a yes/no twin
QC | O 62 r 2(4) | o 62 r 2(4) the address for service of the Authority | roc11-order-62.l4:262 | NOTHING when no paragraph of the list holds | JUST FALSE (a STRING cannot carry it)
QD | O 57 r 4(2) | o 57 r 4(2) the affidavit makes the additional statement the Rule requires | roc11-order-57.l4:361 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 57 r 4(2) the additional statement is required` says whether it arises] | JUST TRUE (nothing is unmet)
QD | O 57 r 5(2) | o 57 r 5(2) the order for registration states and notifies what the Rule requires | roc11-order-57.l4:553 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 57 r 5(2) the order must state the period and contain the notification` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 57 r 12 | o 57 r 12 the claimant serves a copy on the Commission in time | roc11-order-57.l4:1025 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 57 r 12 the duty to serve a copy on the Commission arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 57 r 13 | o 57 r 13 the person transmits a copy to the Commission in time | roc11-order-57.l4:1079 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 57 r 13 the duty to transmit a copy to the Commission arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 58 r 3 | o 58 r 3 the statement of claim gives the particulars | roc11-order-58.l4:142 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 58 r 3 the duty to give the particulars arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 59 r 6(6) | o 59 r 6(6) the order names a time as the Rule requires | roc11-order-59.l4:565 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 59 r 6(6) the duty to name a time for compliance with each term arises` answers JUST FALSE or NOTHING] | JUST TRUE (nothing is unmet)
QD | O 60 r 3(2) | o 60 r 3(2) the affidavit states the provisions in respect of which registration is sought | roc11-order-60.l4:177 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 60 r 3(2) the duty to state the provisions arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 61 r 3(5) | o 61 r 3(5) the application is served as the Rule requires | roc11-order-61.l4:469 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 61 r 3(5) the duty to serve the application personally in time arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 61 r 4(1) | o 61 r 4(1) the claimant files the affidavit of claim in time | roc11-order-61.l4:617 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 61 r 4(1) the duty to file an affidavit of claim arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 62 r 2(5) | o 62 r 2(5) the Authority files the consent as the Rule requires | roc11-order-62.l4:300 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 62 r 2(5) the duty to file the consent of the Public Prosecutor arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 62 r 4(5) | o 62 r 4(5) the summons is served on the defendant as the Rule requires | roc11-order-62.l4:505 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 62 r 4(5) the duty to serve the summons on the defendant arises` answers JUST FALSE or NOTHING] | JUST TRUE (nothing is unmet)
QD | O 62 r 11 | o 62 r 11 the Authority files the consent as the Rule requires | roc11-order-62.l4:932 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 62 r 11 the duty to file the consent of the Public Prosecutor arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 62 r 12(5) | o 62 r 12(5) the costs are paid to the Authority as the Rule requires | roc11-order-62.l4:1045 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 62 r 12(5) the duty to pay the costs to the Authority arises` answers JUST FALSE or NOTHING] | JUST TRUE (nothing is unmet)
QD | O 63 r 2(4) | o 63 r 2(4) the application and affidavit are served as the Rule requires | roc11-order-63.l4:240 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 63 r 2(4) the duty to serve the application personally in time arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 63 r 3(3) | o 63 r 3(3) the application is served as the Rule requires | roc11-order-63.l4:378 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 63 r 3(3) the duty to serve the application personally in time arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QD | O 63 r 4(1) | o 63 r 4(1) the claimant files the affidavit of claim in time | roc11-order-63.l4:523 | compliance function NOTHING when the duty does not arise; the companion answers the trigger [NOTHING, and the companion `o 63 r 4(1) the duty to file an affidavit of claim arises` answers JUST FALSE] | JUST TRUE (nothing is unmet)
QE | O 61 r 3(1) | o 61 r 3(1) the claimant may apply for directions on claims for compensation | roc11-order-61.l4:344 | NOTHING for the item taken out | JUST FALSE (read as "except": a civil penalty order made by default judgment or by consent cannot found an application under rule 3(1), so a claimant who relies only on one may not apply)
QE | O 62 r 2(2) | o 62 r 2(2) the provision applies to the civil penalty action | roc11-order-62.l4:171 | NOTHING for the item taken out | JUST FALSE (read as "except": Order 6, Rule 5(3) and (4) do not apply to a civil penalty action)
QF | not applicable | this encoding writes no events to the state ledger | | | 
```

### Other forks (readings the text licenses on both sides)

Format as above; the answer taken is the reading the function encodes.

```
FORK | O 57 r 3(a) | o 57 r 3(a) the instrument is a Direction | roc11-order-57.l4:176 | NOTHING, because the parenthesis gives the class a name and carries neither "means" nor "only", the words that make a definition say no in its own words | JUST FALSE, because the parenthesis is the definition of the term and an instrument outside its description is not a Direction in this Order (the same question arises wherever a rule says "(called ...)")
    licenses: both readings: "(called in this Order a Direction)" (raw line 6806) beside the definitions that do say "means a Data Protection Appeal Committee nominated under section 48P(4)" (raw line 6800): taken, "called" names the class and, with no "means" and no "only", does not say that an instrument outside it is not a Direction; other, the parenthesis is the definition, so an instrument outside the description is not a Direction
FORK | O 57 r 3(b) | o 57 r 3(b) the instrument is a Notice | roc11-order-57.l4:194 | NOTHING, as for a Direction, because "called" is neither "means" nor "only" | JUST FALSE, because the parenthesis defines the term, so a notice outside the description (a penalty alone, or a notice by someone else) is not a Notice in this Order
    licenses: both readings: "(called in this Order a Notice)" (raw line 6808): taken, a naming only (NOTHING for a notice outside the description); other, a definition (JUST FALSE)
FORK | O 57 r 3(c) | o 57 r 3(c) the instrument is a Decision | roc11-order-57.l4:207 | NOTHING, as for a Direction, because "called" is neither "means" nor "only" | JUST FALSE, because the parenthesis defines the term, so an instrument outside the description is not a Decision in this Order
    licenses: both readings: "(called in this Order a Decision)" (raw line 6813): taken, a naming only (NOTHING for an instrument outside the description); other, a definition (JUST FALSE)
FORK | O 59 r 2(3) | o 59 r 2(3) the time for filing a notice of intention to contest or not contest cannot yet expire | roc11-order-59.l4:194 | whichever of (a) and (b) comes first ends the bar | both must have happened.
    licenses: taken: "the time limited for filing and serving a notice of intention to contest or not contest does not expire until" (raw line 6913) then "4 days after the defendant has notified the claimant in writing that the defendant is satisfied with the statement supplied in compliance with the notice; or" (raw line 6914), read as ending at the first event; other: "4 days after the Court has, on the application of the claimant by summons served on the defendant at least 14 days before the return day, decided that no further information as to the matters referred to in paragraph (1) is reasonably required" (raw line 6916), read as a second event that must also have happened
FORK | O 60 r 5(3) | o 60 r 5(3) the Court may extend the period for applying to set aside the registration | roc11-order-60.l4:242 | JUST FALSE (a window fixed in the text's own words, ruling of 2026-11-05 (a)) | NOTHING
    licenses: taken: "on an application made at any time while it remains competent for any party to apply to have the registration set aside" (raw line 6998), a window fixed in the text's own words; other: "The Court may, on an application made at any time while it remains competent" (raw line 6998) is a grant with no "only", so outside the window the text is silent
FORK | O 60 r 12 | o 60 r 12 the rule has effect subject to the provision of the extending Order | roc11-order-60.l4:605 | includes rule 1A (the range 1 to 11 contains it) | NOTHING (rule 1A is not named).
    licenses: taken: "Rules 1 to 11 are, in relation to any judgment registered or sought to be registered under the Act, to have effect subject to" (raw line 7024) with rule 1A ("The powers conferred on the General Division by the Act may be exercised by a Judge in chambers and the Registrar" (raw line 6975)) lying between rules 1 and 2; other: the range names rules 1 to 11 and not 1A
FORK | O 61 r 3(8) | o 61 r 3(8) the Court must cancel the appointment of the time and place for the hearing | roc11-order-61.l4:580 | the trailing "unless" qualifies both limbs, the cancellation and the deeming | it qualifies the deeming only
    licenses: both readings: "the appointment of the time and place at which the application is to be heard must be cancelled by the Court and the application is deemed dismissed, unless the Court otherwise directs" (raw line 7112): taken, "unless" follows both limbs joined by "and"; other, it follows the last limb only
FORK | O 62 r 4(4) | o 62 r 4(4) the Authority may enter judgment against the defendant for costs | roc11-order-62.l4:458 | "with the permission of the Court" read as a condition of the grant, so that without it the text does not answer | JUST FALSE.
    licenses: both readings: "enter judgment with the permission of the Court against that defendant for costs" (raw line 7201): taken, permission is a condition of the grant and the text is silent without it; other, no permission means no
FORK | O 62 r 8(6) | o 62 r 8(6) an order may be made for the Authority to give production of the document or produce it for inspection | roc11-order-62.l4:864 | the "except that" bars an order for a described document whether or not the document is also listed in (4) or (5) (so the Authority's internal book that it relies on, (4)(k) and (6)(c) together, is barred): the exclusion is worded "a document" and not "a document apart from those listed", and (6)(f) carves paragraph (5) out of itself by name, which would be surplus if the "except that" could not reach a listed document | a listed document is reachable, because the sentence is about documents "apart from those listed in paragraphs (4) and (5)" and the "except that" is an exception to the "unless" limb of that sentence, so it takes away the strong-grounds route for a described unlisted document and leaves (4) and (5) alone ("may also be ordered").
    licenses: taken: "except that no order may be made in respect of a document falling within any of the following descriptions" (raw line 7267) is worded "a document", not "a document apart from those listed", and "but is not referred to in paragraph (5)" (raw line 7278) carves paragraph (5) out of description (f) by name, which would be surplus if the exclusion could not reach a listed document; other: "any document apart from those listed in paragraphs (4) and (5) unless the Court is of the opinion that there are strong and exceptional grounds" (raw line 7267) is the sentence the "except that" ends, so the exception is to its "unless" limb, and "The Authority may also be ordered to give production of or produce for inspection under Order 11 the following documents" (raw line 7240) leaves a listed document reachable
FORK | O 62 r 12(1) | o 62 r 12(1) an order may be made for the costs of the defendant to be paid by the Authority | roc11-order-62.l4:955 | the trailing "after the commencement of the civil penalty action" governs every ground in the list (the death, the bankruptcy or winding up, and the commencement of bankruptcy or winding up proceedings), so the bar applies only where the ground arose after the action began | it governs only "the commencement of bankruptcy or winding up proceedings against the defendant", so a death, bankruptcy or winding up that happened before the action began is within the bar too.
    licenses: both readings: "on the ground of the death or the bankruptcy or winding up of the defendant, or the commencement of bankruptcy or winding up proceedings against the defendant, after the commencement of the civil penalty action" (raw line 7295): taken, "after the commencement of the civil penalty action" qualifies every ground in the list; other, it qualifies only "the commencement of bankruptcy or winding up proceedings against the defendant"
FORK | O 63 r 2(6) | o 63 r 2(6) the Court may direct the applicant to serve a notice to show cause on the third party | roc11-order-63.l4:284 | "After hearing" is read as a condition like "when" and "upon" (ruling of 2026-11-05 (c)): not yet heard is JUST FALSE | NOTHING
    licenses: both readings: "After hearing an application under paragraph (1), the Court may direct the applicant to serve on the third party a notice under section 236L(2)" (raw line 7338): taken, "After hearing" is a condition like "when" and "upon" (ruling 2026-11-05 (c)), so before the hearing the answer is JUST FALSE; other, a scope limit, NOTHING
FORK | O 63 r 3(6) | o 63 r 3(6) the application is deemed dismissed | roc11-order-63.l4:473 | the trailing "unless" qualifies both limbs, the cancellation and the deeming | it qualifies the deeming only
    licenses: both readings: "the appointment of the time and place at which the application is to be heard is to be cancelled by the Court and the application is deemed dismissed, unless the Court otherwise directs" (raw line 7349): taken, "unless" follows both limbs joined by "and"; other, it follows the last limb only
FORK | O 63 r 5(1) | o 63 r 5(1) the Court may give directions or make orders after the hearing | roc11-order-63.l4:693 | "provided" attaches to item (c) only, where it stands | it attaches to all three hearings.
    licenses: both readings: "an application under Rule 3(1), provided all the persons on whom the application has been served and all claimants who have filed their affidavits of claim appear" (raw line 7372): taken, "provided" stands in item (c) and qualifies it alone; other, it qualifies all of (a), (b) and (c)
```

Each `licenses:` line quotes the raw text that licenses the readings, with its raw line number (checked against the raw file by `work/notes.py` when this file is generated); the comment above the function in layer 1 repeats the choice.

## Jural relations (roc11)

The kinds are the encoder's reading and are recorded here only (ruling N2: no Hohfeld kind is typed into a person-facing answer).
A bearer is named only where the text names one; where it does not (a passive "must not be issued"), the row says so.
`SHANT` is derived only for the "until" bars that carry a regulative rule and a trace: `o 57 r 10`, `o 60 r 10`, `o 61 r 3(2)`.
The other flat negatives (for example `o 59 r 4(1)`, `o 59 r 8(2)`, `o 62 r 7(1)`) are answered by the yes/no function and have no `SHANT` rule; see finding 9.

| provision | bearer | kind | what | where |
| --- | --- | --- | --- | --- |
| O 57 r 2(1) | a District Judge in chambers; the Registrar | power | to exercise the powers the District Court has under section 48M | `o 57 r 2(1) ...` |
| O 57 r 2(2) | anyone other than a District Judge | disability | the section 48M(4) powers may only be exercised by a District Judge | `o 57 r 2(2) ...` |
| O 57 r 3 | a person holding a Commission Direction or Notice or an Appeal Committee Decision | power | to apply to register it in the District Court | `o 57 r 3 ...` |
| O 57 r 4 | the applicant | duty | to support the application by an affidavit stating what the Rule lists | `o 57 r 4(1) ...`, `o 57 r 4(2) ...` |
| O 57 r 5(3), (4) | a party; the Court | power; power | to apply to extend the specified period before it expires; to extend it on such terms as the Court thinks fit | `o 57 r 5(3) ...`, `o 57 r 5(4) ...` |
| O 57 r 7 | the person serving the notice of registration | duty; disability | to serve it as the Rule says; to serve out of Singapore only with the Court's permission where the Rule says so | `o 57 r 7(1) ...`, `o 57 r 7(2) ...` |
| O 57 r 8(1) | the person who served the notice | duty | to endorse the notice with the day of the week and the date of service within 3 days, or a longer period the Court allows | `o 57 r 8(1) the duty to endorse the notice`; traces |
| O 57 r 9 | a person applying to set aside the registration (the text names none); the Court | power; power | to apply by summons supported by an affidavit; to try an issue and to set aside on terms | `o 57 r 9(1) ...` to `o 57 r 9(3) ...` |
| O 57 r 10(1), (2) | whoever issues the enforcement order (a placeholder: the text is passive) | duty (SHANT) | not to issue an enforcement order until the specified period has expired, or while the application to set aside is undisposed | `o 57 r 10 the prohibition ...`; traces |
| O 57 r 10(3) | the party applying for an enforcement order | duty | to produce an affidavit of service and any order made | `o 57 r 10(3) ...` |
| O 57 r 11 | an applicant | power | to apply for an order in section 48M(4) with or after the application to register, by summons with an affidavit, without notice if urgent | `o 57 r 11(1)(a) ...`, `o 57 r 11(2) ...` |
| O 57 r 12 | the claimant in section 48O(1) proceedings | duty (claim-right of the Commission) | to serve a copy on the Commission not later than 14 days after service on the defendant | `o 57 r 12 ...`; traces |
| O 57 r 13 | a person granted a judgment or order under section 48O | duty (claim-right of the Commission) | to transmit a copy to the Commission within 3 days after its date | `o 57 r 13 ...`; traces |
| O 58 r 2 | the applicant under section 5(3), 10, 32, 43 or 44 | duty | to apply by originating application supported by an affidavit of grounds | `o 58 r 2 ...` |
| O 58 r 3 | a claimant claiming money under a hire-purchase agreement | duty | to give the listed particulars in the statement of claim | `o 58 r 3 ...` |
| O 59 r 2 | the claimant against the Government; the defendant | duty; power | to state the circumstances, department and officers; to ask by notice for a further statement before the time to contest expires | `o 59 r 2(1) ...`, `o 59 r 2(2) ...` |
| O 59 r 2(3) | the defendant | immunity | the time for a notice of intention to contest does not expire until the days after notification or the Court's decision | `o 59 r 2(3) ...` |
| O 59 r 3 | the Government | immunity; no-duty | service-out rules do not apply to the process; personal service is not requisite | `o 59 r 3(1) ...`, `o 59 r 3(2) ...` |
| O 59 r 4 | a person in proceedings by the Government; the Government in proceedings against it | disability | no counterclaim or set-off for taxes, duties or penalties; none without permission in the cases of r 4(2) | `o 59 r 4(1) ...`, `o 59 r 4(2) ...` |
| O 59 r 5 | an applicant against the Government | disability | no summary-judgment application under the Order 9 rules named | `o 59 r 5(1) ...` |
| O 59 r 6(6) | the Court as maker of the order (the text is passive) | duty | to name a time for compliance with each term of an order in the Government's favour unless it otherwise determines | `o 59 r 6(6) ...` |
| O 59 r 6(7) | the Government | privilege | is not required to use the section 21 application where it claims only money, and may use any other procedure | `o 59 r 6(7) ...` |
| O 59 r 7 | a claimant against the Government | disability | no judgment in default and no operation of Order 10 r 5(1)(a) without the Court's permission | `o 59 r 7(1) ...`, `o 59 r 7(2) ...` |
| O 59 r 8 | a defendant; the Court | disability; duty (not named as SHANT) | no third party notice for the Government without permission; permission not to be granted unless the Court is satisfied | `o 59 r 8(1) ...`, `o 59 r 8(2) ...` |
| O 59 r 9(1) | a party seeking production | disability (immunity of the Government) | an order under section 34(1) does not require disclosure of a document withheld on the public-interest ground | `o 59 r 9(1) ...` |
| O 59 r 11(1), 12(1) | a judgment creditor of the Government | disability (immunity of the Government) | Orders 22 and 23 and Order 13 r 9 do not apply; no attachment or receiver in respect of money due from the Government | `o 59 r 11(1) ...`, `o 59 r 12(1) ...` |
| O 59 r 12(3) | the Court | disability | no power to order an enforcement order against the Government | `o 59 r 12(3) ...` |
| O 60 rules 2 to 13 | the judgment creditor; the person served; the Court; whoever issues the enforcement order | as O 57 rules 3 to 11 | the same shape as O 57 for registering a foreign judgment, with security for costs (r 4) and certified copies (r 13) | `o 60 r 3(1) ...` to `o 60 r 13(3) ...`; traces |
| O 61 r 2 | a person who suffered loss | power | to commence an action by originating claim, or to apply for permission by originating application | `o 61 r 2(1) ...`, `o 61 r 2(2) ...` |
| O 61 r 3(2) | the claimant | duty (SHANT) | not to apply for directions before the conviction or order is final | `o 61 r 3(2) ...`; traces |
| O 61 r 3(5)-(6) | the claimant applying for directions | duty | to serve the application personally at least 28 clear days before the hearing; to advertise in Form 91 at least 21 clear days before | `o 61 r 3(5) ...`, `o 61 r 3(6) ...` |
| O 61 r 4 | a person desiring to claim | duty | to file an affidavit of claim at least 7 clear days before the return date and to serve a copy within 3 days | `o 61 r 4(1) ...`, `o 61 r 4(4) ...`; traces |
| O 62 r 2 | the Authority | duty | to commence by originating claim; to endorse the matters of r 2(3); to file the Public Prosecutor's consent on presenting the claim for sealing | `o 62 r 2(1) ...`, `o 62 r 2(3) ...`, `o 62 r 2(5) ...` |
| O 62 r 4, 5 | the Authority | power | to apply for judgment on default of notice or of defence; to proceed as if the defendant had filed; to enter judgment for costs with permission | `o 62 r 4(1) ...` to `o 62 r 5(2) ...` |
| O 62 r 6 | the Authority | no-duty | is not required to make or add any person as a defendant | `o 62 r 6 ...` |
| O 62 r 3(2), 7(1) | a defendant (the text is passive) | disability | no defence of tender; no third party notice without the Court's permission | `o 62 r 3(2) ...`, `o 62 r 7(1) ...` |
| O 62 r 8 | the Authority | liability; immunity | may be ordered to produce the documents of r 8(4) and (5); no order for the descriptions of r 8(6)(a) to (g); strong and exceptional grounds for any other | `o 62 r 8(4) ...` to `o 62 r 8(6) ...` |
| O 62 r 11 | the Authority | duty | to file the consent of the Public Prosecutor when an order is sought under the sections named | `o 62 r 11 ...` |
| O 62 r 12(5) | whoever recovers the costs (the text names none) | duty (claim-right of the Authority) | to pay costs awarded to the Authority, when recovered, to the Authority | `o 62 r 12(5) ...` |
| O 62 r 12(1) | a defendant | disability | no order for the defendant's costs where the Authority discontinues or withdraws on the grounds named | `o 62 r 12(1) ...` |
| O 63 r 2 | the applicant (the Authority or a claimant); the third party | power; duty; power | to apply by originating application with an affidavit and personal service 28 clear days before; the third party may show cause | `o 63 r 2(1) ...` to `o 63 r 2(7) ...` |
| O 63 r 3 | a claimant | power; duty | to apply for directions on claims for compensation; to serve and advertise as the Rule says; failing which the application is deemed dismissed | `o 63 r 3(1) ...` to `o 63 r 3(6) ...` |
| O 63 r 4 | a claimant | duty | to file an affidavit of claim at least 7 clear days before the return date and to serve a copy within 3 days | `o 63 r 4(1) ...`, `o 63 r 4(4) ...`; traces |
| O 63 r 5(3) | a claimant who filed an affidavit of claim and does not appear or does not comply with an order; the Court | liability; power | the Court may declare the claimant and those claiming under the claimant forever barred from bringing any claim against the third party | `o 63 r 5(3) ...` |

## Marginal readings for a lawyer (roc11)

Two readings are the status quo of the brief: (a) a failed "if", "where", "when", "upon" or "whenever" counts as the text's no, clause by clause, within the provision that holds it, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording, and a scope limit with no "only", answers `NOTHING`.
Branches that rest on a choice a lawyer may overrule, by hand:

1. **O 57 r 3, "called in this Order a Direction / a Notice / a Decision" (a fork at each of `(a)`, `(b)`, `(c)`).** The instruments the description fits answer `JUST TRUE`; an instrument it does not fit answers `NOTHING`, because "called" gives the class a name and, unlike "means" (which O 57 r 1 uses for "Appeal Committee" and "Commission", and which answers `JUST FALSE` for a non-member), says neither "means" nor "only". The other reading: the parenthesis is the definition, so an instrument outside the description is not a Direction, Notice or Decision (`JUST FALSE`). The same question arises wherever a rule says "(called ...)", and the answer should be the same there.
2. **O 57 r 3(b), a Notice.** A Notice is "a sum comprising" a financial penalty "and" interest on it; a notice for the penalty alone answers `NOTHING`. The other reading: it is a Notice.
3. **"(if any)", "any other" and "if so" items.** O 58 r 3(e) ("(if any)") and (f) ("any other claim"), O 60 r 3(1)(d) (interest, "(if any)"), r 13(2) (the third annexure, "(if any)" pleadings, and item (c), "and, if so") and r 13(3)(b), (c) (the certificate, "(if any)") are required only when the thing exists. The other reading: required always.
4. **Passive prohibitions with no bearer.** O 57 r 10 and O 60 r 10 say an enforcement order "must not be issued"; the regulative rule names a placeholder party, `whoever issues the enforcement order`, and the bar is also a plain yes/no function. The other reading: no regulative rule.
5. **"Applies with changes" (S-L1).** Where an Order applies another "with" or "subject to" changes it does not state (O 59 r 12(3), O 62 r 8(1) and (2), O 63 r 8), roc11 answers `JUST TRUE` that it applies and leaves what changes to the other part.
6. **A "means" definition says no outside itself.** `o 62 r 1(1) "civil penalty action"`, `o 59 r 1(2) "order against the Government"`, `o 61 r 1(1) "defendant individual"` and the other "means" definitions answer `JUST FALSE` for a case outside the definition. The other reading: `NOTHING`.
7. **Permission as the price of a grant.** O 62 r 4(4) ("enter judgment with the permission of the Court") answers `NOTHING` without permission; see the fork register. The other reading: `JUST FALSE`.
8. **"Despite" and "subject to" clauses.** A clause that gives way to another Order (O 60 r 4, O 61 r 6, O 63 r 6, "Subject to Rules 1 to 5") answers `NOTHING` where the other Order speaks (QA in the register).
9. **May the affidavit state it? (O 57 r 4(1)(d)(ii) and (iii), r 4(2)(a) and (b)).** The functions that ask what the affidavit says are kept; the functions that ask whether the facts allow each statement to be made answer `JUST TRUE` when they do and `JUST FALSE` when they do not (an appeal pending, the time to appeal not expired, the instrument already complied with, a reconsideration pending, the time to apply or to appeal further not expired). The facts are the facts as the deponent believes them ("to the best of the information or belief of the deponent"). The Rule does not say what follows when an affidavit states what the facts do not bear out (O 3 r 2(4) says what the Court may do about non-compliance). The other reading: `NOTHING`, because the Rule says what the affidavit must state and not what the facts must be.
10. **The court (O 57 r 3).** The Rule opens "An application to register in the District Court". An application to register in another court answers `NOTHING` (a scope limit with no "only"). The other reading: the court does not matter to the mode of application (`JUST TRUE` for the same mode in any court).
11. **The window in O 57 r 11(1)(a).** An application for an order specified in section 48M(4) "may be made together with, or at any time after" the application to register. An application made before the application to register is outside the window the text fixes and answers `JUST FALSE` (ruling (a)). The other reading: `NOTHING`, because the sentence grants and does not forbid. Two other windows in the range are fixed the same way (O 59 r 13(2) "at any time before trial or ... at the trial", and O 60 r 5(3) "while it remains competent"); no other branch of roc11 answers `NOTHING` for a time outside a window the text states.

Every `JUST FALSE` branch in layer 1, one row per function (functions with a JUST FALSE branch: 123; branches: 155):

| function | file:line | rests on | quote (the text's words) | the other reading |
| --- | --- | --- | --- | --- |
| `o 57 r 1 the panel is an Appeal Committee` | order-57:85 | means-definition | "means a Data Protection Appeal Committee nominated under section 48P(4)" | NOTHING (read "means" as not closing the class) |
| `o 57 r 1 the body is the Commission` | order-57:95 | means-definition | "means the Personal Data Protection Commission established by section 5" | NOTHING (read "means" as not closing the class) |
| `o 57 r 2(2) the power under section 48M(4) may be exercised by the person` | order-57:125 | flat negative (ruling N2) | "may only be exercised by a District Judge" | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 4(1)(d)(ii)(A) the affidavit may state that it has not been appealed against and the time allowed for appealing has expired` | order-57:387 | flat negative (ruling N2) | "the Direction, Notice or Decision has not been appealed against and the time allowed fo..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 4(1)(d)(ii)(B) the affidavit may state that all appeals have been finally disposed of and no further appeal is feasible` | order-57:399 | flat negative (ruling N2) | "have been finally disposed of and no further appeal is feasible" | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 4(1)(d)(ii) the affidavit may state the matter the Rule requires about appeals` | order-57:416 | the text's no in other words (flat negative, deeming or exclusion) | "as at the date of the application" | NOTHING |
| `o 57 r 4(1)(d)(iii) the affidavit may state that it has not been complied with` | order-57:428 | flat negative (ruling N2) | "the Direction, Notice or Decision has not been complied with" | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 4(2)(a) the affidavit may state that no application to reconsider was made and the time allowed to apply has expired` | order-57:442 | flat negative (ruling N2) | "there has been no application made under section 48N(1) to the Commission to reconsider..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 4(2)(b)(i) the affidavit may state that the decision on reconsideration has not been appealed against and the time allowed for appealing has expired` | order-57:460 | unmet condition: if / where / when / upon / after (ruling (b)) | "upon reconsideration of the Direction or Notice has not been appealed against and the t..." | NOTHING (an unmet condition is silence, not a no) |
| `o 57 r 4(2)(b)(ii) the affidavit may state that all appeals against the decision on reconsideration have been finally disposed of and the time allowed for a further appeal has expired` | order-57:482 | the text's no in other words (flat negative, deeming or exclusion) | "have been finally disposed of and the time allowed for making a further appeal (where a..." | NOTHING |
| `o 57 r 4(2) the affidavit may state the additional matter the Rule requires about reconsideration` | order-57:509 | the text's no in other words (flat negative, deeming or exclusion) | "at the date of the application" | NOTHING |
| `o 57 r 5(2) the order must state the period and contain the notification` | order-57:542 | duty or deeming lifted by an exception | "Unless the Court otherwise directs" | NOTHING (a lifted duty says nothing) |
| `o 57 r 5(3) the application to extend the period is made before the period expires` | order-57:566 | the text's no in other words (flat negative, deeming or exclusion) | "must be made before the expiry of that period" | NOTHING |
| `o 57 r 7(2) permission is needed to serve the notice out of Singapore` | order-57:622 | the text's no in other words (flat negative, deeming or exclusion) | "is permissible without permission" | NOTHING |
| `o 57 r 8(1) the notice is endorsed in time` | order-57:715 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Within 3 days after service of the notice of registration or within such longer period ..." ; "Within 3 days after service of the notice of registration or within such longer period ..." | NOTHING (outside the period the text is silent) |
| `o 57 r 8(2) the person seeking to enforce may apply for an enforcement order without the permission of the Court` | order-57:783 | flat negative (ruling N2) | "may not apply for an enforcement order to enforce the Direction, Notice or Decision wit..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 10(1) an enforcement order cannot yet be issued because the specified period has not expired` | order-57:849 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Where, pursuant to Rule 5(2), there is a specified period within which an application m..." ; "until after the expiry of the specified period" | NOTHING (outside the period the text is silent) |
| `o 57 r 10(2) an enforcement order cannot yet be issued because the application to set aside is not disposed of` | order-57:864 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "If an application is made to set aside the registration" ; "until after such application is disposed of" | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 57 r 11(1)(a) the application for an order specified in section 48M(4) may be made at this time` | order-57:936 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "together with, or at any time after, an application for registration" | NOTHING (outside the period the text is silent) |
| `o 57 r 11(1)(b) the application is an application for an enforcement order under Rule 10` | order-57:947 | flat negative (ruling N2) | "does not constitute an application for an enforcement order" | NOTHING (a flat negative is not itself the answer asked) |
| `o 57 r 11(2) the application may be made in this way` | order-57:961 | unmet condition: if / where / when / upon / after (ruling (b)) | "where the case is one of urgency, may be made without notice" | NOTHING (an unmet condition is silence, not a no) |
| `o 57 r 12 the duty to serve a copy on the Commission arises` | order-57:1014 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where any claim is made for relief in civil proceedings under section 48O(1)" | NOTHING (an unmet condition is silence, not a no) |
| `o 57 r 12 the claimant serves a copy on the Commission in time` | order-57:1025 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "not later than 14 days after service of the originating claim or originating applicatio..." | NOTHING (outside the period the text is silent) |
| `o 57 r 13 the duty to transmit a copy to the Commission arises` | order-57:1068 | the text's no in other words (flat negative, deeming or exclusion) | "Any person who is granted any judgment or order by a Court pursuant to section 48O" | NOTHING |
| `o 57 r 13 the person transmits a copy to the Commission in time` | order-57:1079 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "within 3 days after the date of the judgment or order" | NOTHING (outside the period the text is silent) |
| `o 58 r 3 the duty to give the particulars arises` | order-58:97 | the text's no in other words (flat negative, deeming or exclusion) | "is for the recovery of money arising out of a hire-purchase agreement" | NOTHING |
| `o 59 r 1(2) "order against the Government" the order is an order against the Government` | order-59:114 | means-definition | "means any order (including an order for costs) made in any civil proceedings by or agai..." | NOTHING (read "means" as not closing the class) |
| `o 59 r 2(2) the defendant may apply to the claimant by notice for a further and better statement` | order-59:161 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "If in civil proceedings against the Government a defendant considers that the originati..." ; "before the expiration of the time limited for filing and serving a notice of intention ..." | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 59 r 2(3) the time for filing a notice of intention to contest or not contest cannot yet expire` | order-59:194 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Where a defendant gives a notice under this Rule" ; "does not expire until" ; "does not expire until" (+1 more) | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 59 r 2(3)(b) the claimant's application is made and served as the Rule requires` | order-59:221 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "served on the defendant at least 14 days before the return day" | NOTHING (outside the period the text is silent) |
| `o 59 r 3(1) the provision applies to the service of the process` | order-59:241 | flat negative (ruling N2) | "Order 7, Order 8 and any other provision of these Rules relating to service out of Sing..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 3(2) personal service on the Government is requisite` | order-59:251 | flat negative (ruling N2) | "Personal service of any document required to be served on the Government for the purpos..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 3(3) the provision applies to the service` | order-59:281 | flat negative (ruling N2) | "Order 7, Rule 3 does not apply" | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 4(1) a person may make a counterclaim or plead a set-off` | order-59:302 | flat negative (ruling N2) | "a person may not in any proceedings by the Government make any counterclaim or plead a ..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 4(2) the permission of the Court is required for the counterclaim or set-off` | order-59:333 | unmet condition: if / where / when / upon / after (ruling (b)) | "if the Government is sued or sues in the name of a Government department and the subjec..." | NOTHING (an unmet condition is silence, not a no) |
| `o 59 r 4(2) the counterclaim may be made or the set-off pleaded` | order-59:356 | flat negative (ruling N2) | "no counterclaim may be made, or set-off pleaded, without the permission of the Court" | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 5(1) an application against the Government may be made under the provision` | order-59:396 | flat negative (ruling N2); the text's no in other words (flat negative, deeming or exclusion) | "No application against the Government may be made" ; "under Order 9, Rule 17(11) or 19, in any proceedings by the Government" | NOTHING (a flat negative is not itself the answer asked); NOTHING |
| `o 59 r 6(5) the course is open` | order-59:538 | unmet condition: if / where / when / upon / after (ruling (b)) | "if evidence is filed disputing any of those facts" | NOTHING (an unmet condition is silence, not a no) |
| `o 59 r 6(6) the duty to name a time for compliance with each term arises` | order-59:550 | duty or deeming lifted by an exception | "unless the Court otherwise determines" | NOTHING (a lifted duty says nothing) |
| `o 59 r 6(7) this Rule requires the Government to proceed by way of an application under it` | order-59:580 | the text's no in other words (flat negative, deeming or exclusion) | "is to be construed as requiring the Government to proceed by way of an application to w..." | NOTHING |
| `o 59 r 6(7) this Rule prevents the Government from availing itself of another procedure open under these Rules` | order-59:589 | the text's no in other words (flat negative, deeming or exclusion) | "or as preventing the Government from availing itself of any other procedure which is op..." | NOTHING |
| `o 59 r 7(1) judgment in default is barred without permission` | order-59:618 | duty or deeming lifted by an exception | "Except with the permission of the Court" | NOTHING (a lifted duty says nothing) |
| `o 59 r 7(1) judgment in default may be entered against the Government` | order-59:633 | flat negative (ruling N2) | "no judgment in default of notice of intention to contest or not contest or of pleading ..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 7(2) Order 10 rule 5(1)(a) applies` | order-59:647 | flat negative (ruling N2) | "does not apply in the case of third party proceedings against the Government" | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 7(3) the application for permission is made and served as the Rule requires` | order-59:665 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "the summons must be served at least 14 days before the return day" | NOTHING (outside the period the text is silent) |
| `o 59 r 8(1) the third party notice may be issued` | order-59:686 | flat negative (ruling N2) | "must not be issued without the permission of the Court" | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 8(2) the Court may grant permission to issue the notice` | order-59:715 | flat negative (ruling N2) | "Permission to issue such a notice for service on the Government must not be granted unl..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 9(1) the order requires disclosure of the document` | order-59:732 | flat negative (ruling N2) | "is to be construed as not requiring the disclosure of any document the withholding of w..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 11(1) the provision applies in respect of the order` | order-59:775 | flat negative (ruling N2) | "Nothing in Order 22, Order 23 and Order 13, Rule 9 apply in respect of any order agains..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 59 r 12(1) the order may be made` | order-59:830 | the text's no in other words (flat negative, deeming or exclusion) | "may be made or have effect in respect of any money due or accruing due, or alleged to b..." | NOTHING |
| `o 59 r 12(1) the order has effect` | order-59:845 | the text's no in other words (flat negative, deeming or exclusion) | "may be made or have effect in respect of any money due or accruing due, or alleged to b..." | NOTHING |
| `o 59 r 12(2) the application is made and served as the Rule requires` | order-59:869 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "served at least 4 days before the return day" | NOTHING (outside the period the text is silent) |
| `o 59 r 12(3) the Court has power to order an enforcement order to be issued against the Government` | order-59:895 | duty or deeming lifted by an exception | "except that the Court does not have power to order an enforcement order to be issued ag..." | NOTHING (a lifted duty says nothing) |
| `o 59 r 13(2) the application may be made in this way and at this time` | order-59:930 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "may be made by summons to the Court at any time before trial or may be made at the tria..." | NOTHING (outside the period the text is silent) |
| `o 60 r 3(2) the duty to state the provisions arises` | order-60:166 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where a judgment sought to be registered under the Act is in respect of different matte..." | NOTHING (an unmet condition is silence, not a no) |
| `o 60 r 5(3) the Court may extend the period for applying to set aside the registration` | order-60:242 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "on an application made at any time while it remains competent for any party to apply to..." | NOTHING (outside the period the text is silent) |
| `o 60 r 7(2) permission is needed to serve the notice out of Singapore` | order-60:301 | the text's no in other words (flat negative, deeming or exclusion) | "is permissible without permission" | NOTHING |
| `o 60 r 8(1) the notice is endorsed in time` | order-60:391 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Within 3 days after service of the notice of registration or within such longer period ..." ; "Within 3 days after service of the notice of registration or within such longer period ..." | NOTHING (outside the period the text is silent) |
| `o 60 r 8(1) the judgment creditor may apply for an enforcement order without the permission of the Court` | order-60:455 | flat negative (ruling N2) | "the judgment creditor may not apply for an enforcement order to enforce the judgment to..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 60 r 10(1) an enforcement order cannot yet be issued because the specified period has not expired` | order-60:508 | the text's no in other words (flat negative, deeming or exclusion); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "to enforce a judgment registered under the Act" ; "until after the expiration of the period" | NOTHING; NOTHING (outside the period the text is silent) |
| `o 60 r 10(2) an enforcement order cannot yet be issued because the application to set aside is not finally determined` | order-60:523 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "If an application is made to set aside the registration of a judgment" ; "until after such application is finally determined" | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 60 r 12 the rule has effect subject to the provision of the extending Order` | order-60:605 | the text's no in other words (flat negative, deeming or exclusion) | "any such provisions contained in the Order extending that Act to the country of the ori..." | NOTHING |
| `o 61 r 1(1) "defendant individual" the person is a defendant individual` | order-61:145 | means-definition | "means an individual liable to an order for a civil penalty under section 236H in respec..." | NOTHING (read "means" as not closing the class) |
| `o 61 r 2(3) the provision applies to the originating application` | order-61:217 | duty or deeming lifted by an exception | "Unless expressly modified in this Rule" | NOTHING (a lifted duty says nothing) |
| `o 61 r 2(5) the application is served as the Rule requires in the first instance` | order-61:288 | flat negative (ruling N2) | "must in the first instance be served only on the contravening person, the defendant cor..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 61 r 2(7) the application to continue is served as the Rule requires in the first instance` | order-61:319 | flat negative (ruling N2) | "must in the first instance be served only on the defendant" | NOTHING (a flat negative is not itself the answer asked) |
| `o 61 r 3(2) an application cannot yet be made because the conviction or order is not yet final` | order-61:376 | the text's no in other words (flat negative, deeming or exclusion); flat negative (ruling N2) | "An application under paragraph (1)" ; "must not be made before the conviction or the order making the civil penalty has been m..." | NOTHING; NOTHING (a flat negative is not itself the answer asked) |
| `o 61 r 3(4) the provision applies to the originating application` | order-61:426 | duty or deeming lifted by an exception | "Unless expressly modified in this Rule" | NOTHING (a lifted duty says nothing) |
| `o 61 r 3(5) the duty to serve the application personally in time arises` | order-61:455 | duty or deeming lifted by an exception | "Unless the Court otherwise orders" | NOTHING (a lifted duty says nothing) |
| `o 61 r 3(5) the application is served as the Rule requires` | order-61:469 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "at least 28 clear days or such longer time as the Court may direct before the return date" | NOTHING (outside the period the text is silent) |
| `o 61 r 3(6) the application is advertised as the Rule requires` | order-61:507 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "at least 21 clear days or such longer time as the Court may direct before the return date" | NOTHING (outside the period the text is silent) |
| `o 61 r 3(8) the application is deemed dismissed` | order-61:565 | unmet condition: if / where / when / upon / after (ruling (b)); duty or deeming lifted by an exception | "If the claimant making the application or the claimant's solicitor does not comply with..." ; "unless the Court otherwise directs" | NOTHING (an unmet condition is silence, not a no); NOTHING (a lifted duty says nothing) |
| `o 61 r 3(8) the Court must cancel the appointment of the time and place for the hearing` | order-61:580 | unmet condition: if / where / when / upon / after (ruling (b)); duty or deeming lifted by an exception | "If the claimant making the application or the claimant's solicitor does not comply with..." ; "unless the Court otherwise directs" | NOTHING (an unmet condition is silence, not a no); NOTHING (a lifted duty says nothing) |
| `o 61 r 4(1) the duty to file an affidavit of claim arises` | order-61:605 | the text's no in other words (flat negative, deeming or exclusion) | "each claimant desiring to claim compensation against the contravening person" | NOTHING |
| `o 61 r 4(1) the claimant files the affidavit of claim in time` | order-61:617 | the text's no in other words (flat negative, deeming or exclusion) | "At least 7 clear days before the return date of the application" ; "At least 7 clear days before the return date of the application" | NOTHING |
| `o 61 r 4(4) the claimant serves a copy of the affidavit on the subject in time` | order-61:711 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "within 3 days of the filing of the same" ; "within 3 days of the filing of the same" | NOTHING (outside the period the text is silent) |
| `o 61 r 5(1) the Court may give directions or make orders on the hearing` | order-61:778 | unmet condition: if / where / when / upon / after (ruling (b)) | "where, on the hearing of an application made under Rule 3(1), all the persons on whom t..." | NOTHING (an unmet condition is silence, not a no) |
| `o 61 r 5(1) the Court may give this kind of direction or make this kind of order` | order-61:804 | unmet condition: if / where / when / upon / after (ruling (b)) | "where, on the hearing of an application made under Rule 3(1), all the persons on whom t..." | NOTHING (an unmet condition is silence, not a no) |
| `o 61 r 5(2) the Court may make such order as it deems appropriate against the contravening person` | order-61:818 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where a contravening person, defendant corporation, defendant partnership or defendant ..." | NOTHING (an unmet condition is silence, not a no) |
| `o 61 r 5(3) the Court may declare the claimant forever barred` | order-61:829 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where a claimant having filed an affidavit of claim under Rule 4 does not appear on the..." | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 1(1) "civil penalty action" the proceeding is a civil penalty action` | order-62:83 | means-definition | "means any proceeding commenced by the Authority under section 137ZD, 232, 236B(3), 236C..." | NOTHING (read "means" as not closing the class) |
| `o 62 r 1(1) "Commercial Affairs Officer" the person is a Commercial Affairs Officer` | order-62:96 | means-definition | "means a Commercial Affairs Officer appointed under section 64 of the Police Force Act" | NOTHING (read "means" as not closing the class) |
| `o 62 r 1(1) "police officer" the person is a police officer` | order-62:131 | means-definition | "means a member of the Singapore Police Force who is deployed in the Commercial Affairs ..." | NOTHING (read "means" as not closing the class) |
| `o 62 r 2(2) the provision applies to the civil penalty action` | order-62:171 | duty or deeming lifted by an exception | "unless modified by this Rule" | NOTHING (a lifted duty says nothing) |
| `o 62 r 2(5) the duty to file the consent of the Public Prosecutor arises` | order-62:290 | unmet condition: if / where / when / upon / after (ruling (b)) | "on presenting the originating claim for sealing" | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 3(2) the defence applies to the civil penalty action` | order-62:351 | flat negative (ruling N2) | "The defence of tender does not apply to a civil penalty action" | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 4(1) the Authority may apply to the Court for judgment` | order-62:379 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Where the Authority has not applied for any order apart from an order for a civil penal..." ; "after the time limited for filing and serving the notice" ; "upon filing an affidavit proving due service of the originating claim on the defendant" (+1 more) | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 62 r 4(1) the Court must give such judgment as the Authority appears entitled to` | order-62:396 | unmet condition: if / where / when / upon / after (ruling (b)) | "upon hearing the application the Court must give such judgment as the Authority appears..." | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 4(3) the Authority may proceed as if the defendant had filed and served a notice of intention to contest or not contest` | order-62:432 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "Where the Authority has applied for any other order in addition to an order for a civil..." ; "after the time limited for filing and serving the notice" ; "upon filing an affidavit proving due service of the originating claim on the defendant" (+1 more) | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 62 r 4(4) the Authority may enter judgment against the defendant for costs` | order-62:458 | flat negative (ruling N2); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "it has become unnecessary for the Authority to proceed with the civil penalty action, t..." ; "after the time limited for filing and serving the notice" | NOTHING (a flat negative is not itself the answer asked); NOTHING (outside the period the text is silent) |
| `o 62 r 4(5) the duty to serve the summons on the defendant arises` | order-62:490 | duty or deeming lifted by an exception | "unless the Court otherwise orders" | NOTHING (a lifted duty says nothing) |
| `o 62 r 5(1) the Authority may apply to the Court for judgment` | order-62:544 | unmet condition: if / where / when / upon / after (ruling (b)); period fixed in the text's own words (ruling of 2026-11-05 (a)) | "If the defendant or all the defendants (where there is more than one) fails or fail to ..." ; "after the expiration of the period fixed under these Rules for service of the defence" | NOTHING (an unmet condition is silence, not a no); NOTHING (outside the period the text is silent) |
| `o 62 r 5(1) the Court must give such judgment as the Authority appears entitled to` | order-62:556 | unmet condition: if / where / when / upon / after (ruling (b)) | "on the hearing of the application, the Court must give such judgment as the Authority a..." | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 5(2) the Authority may take the course` | order-62:581 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where the Authority brings a civil penalty action against more than one defendant, then..." ; "if the claim against the defendant in default is severable from the claim against the o..." | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 6 the Authority is required to make or add a person as a defendant` | order-62:630 | flat negative (ruling N2) | "the Authority is not required to make or add any person as a defendant to a civil penal..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 7(1) the third party notice may be issued` | order-62:645 | flat negative (ruling N2) | "must not be issued without the permission of the Court" | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 8(3) the order requires disclosure of the document` | order-62:705 | flat negative (ruling N2) | "is to be construed as not requiring the disclosure of any document the withholding of w..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 8(6) an order may be made for the Authority to give production of the document or produce it for inspection` | order-62:864 | period fixed in the text's own words (ruling of 2026-11-05 (a)); flat negative (ruling N2) | "no order may be made in respect of a document falling within any of the following descr..." ; "may not be ordered to give production of or produce for inspection under Order 11 any d..." | NOTHING (outside the period the text is silent); NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 8(7) paragraph (6) affects the operation of the Evidence Act` | order-62:880 | flat negative (ruling N2) | "Nothing in paragraph (6) affects the operation of the Evidence Act" | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 10 the provision applies to the civil penalty action` | order-62:907 | flat negative (ruling N2) | "Order 5 and Order 14 do not apply to a civil penalty action" | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 11 the duty to file the consent of the Public Prosecutor arises` | order-62:922 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where an order is sought under section 137ZD(3) or 232(4), or under section 232(4) read..." | NOTHING (an unmet condition is silence, not a no) |
| `o 62 r 12(1) an order may be made for the costs of the defendant to be paid by the Authority` | order-62:955 | flat negative (ruling N2) | "no order may be made for the costs of a defendant to be paid by the Authority where the..." | NOTHING (a flat negative is not itself the answer asked) |
| `o 62 r 12(3) the costs include the item` | order-62:991 | the text's no in other words (flat negative, deeming or exclusion) | "appears as an advocate on behalf of the Authority and costs are awarded to the Authority" | NOTHING |
| `o 62 r 12(5) the duty to pay the costs to the Authority arises` | order-62:1031 | the text's no in other words (flat negative, deeming or exclusion) | "when recovered, must be paid to the Authority" | NOTHING |
| `o 63 r 1(1) "order for disgorgement" the order is an order for disgorgement` | order-63:75 | means-definition | "means an order applied for under section 236L(1)" | NOTHING (read "means" as not closing the class) |
| `o 63 r 2(2) the provision applies to the originating application` | order-63:116 | duty or deeming lifted by an exception | "Unless modified expressly in this Rule" | NOTHING (a lifted duty says nothing) |
| `o 63 r 2(4) the duty to serve the application personally in time arises` | order-63:222 | duty or deeming lifted by an exception | "Unless the Court otherwise orders" | NOTHING (a lifted duty says nothing) |
| `o 63 r 2(4) the application and affidavit are served as the Rule requires` | order-63:240 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "at least 28 clear days or such longer time as the Court may direct, before the hearing ..." | NOTHING (outside the period the text is silent) |
| `o 63 r 2(5) the application is deemed dismissed` | order-63:267 | unmet condition: if / where / when / upon / after (ruling (b)); duty or deeming lifted by an exception | "If the applicant for the order for disgorgement or the applicant's solicitor does not c..." ; "unless the Court otherwise directs" | NOTHING (an unmet condition is silence, not a no); NOTHING (a lifted duty says nothing) |
| `o 63 r 2(6) the Court may direct the applicant to serve a notice to show cause on the third party` | order-63:284 | unmet condition: if / where / when / upon / after (ruling (b)) | "After hearing an application under paragraph (1), the Court may direct the applicant" | NOTHING (an unmet condition is silence, not a no) |
| `o 63 r 3(1) the person may apply for directions on claims for compensation` | order-63:310 | unmet condition: if / where / when / upon / after (ruling (b)) | "If an order for disgorgement has been made final in accordance with section 236L(11)" | NOTHING (an unmet condition is silence, not a no) |
| `o 63 r 3(3) the duty to serve the application personally in time arises` | order-63:360 | duty or deeming lifted by an exception | "Unless the Court otherwise orders" | NOTHING (a lifted duty says nothing) |
| `o 63 r 3(3) the application is served as the Rule requires` | order-63:378 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "at least 28 clear days or such longer time as the Court may direct, before the return date" | NOTHING (outside the period the text is silent) |
| `o 63 r 3(4) the application is advertised as the Rule requires` | order-63:416 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "at least 21 clear days or such longer time as the Court may direct before the return date" | NOTHING (outside the period the text is silent) |
| `o 63 r 3(6) the application is deemed dismissed` | order-63:473 | unmet condition: if / where / when / upon / after (ruling (b)); duty or deeming lifted by an exception | "If the applicant for directions or the applicant's solicitor does not comply with parag..." ; "unless the Court otherwise directs" | NOTHING (an unmet condition is silence, not a no); NOTHING (a lifted duty says nothing) |
| `o 63 r 3(6) the Court must cancel the appointment of the time and place for the hearing` | order-63:488 | unmet condition: if / where / when / upon / after (ruling (b)); duty or deeming lifted by an exception | "If the applicant for directions or the applicant's solicitor does not comply with parag..." ; "unless the Court otherwise directs" | NOTHING (an unmet condition is silence, not a no); NOTHING (a lifted duty says nothing) |
| `o 63 r 4(1) the duty to file an affidavit of claim arises` | order-63:511 | the text's no in other words (flat negative, deeming or exclusion) | "each claimant desiring to file a claim for compensation under section 236L(6)" | NOTHING |
| `o 63 r 4(1) the claimant files the affidavit of claim in time` | order-63:523 | the text's no in other words (flat negative, deeming or exclusion) | "At least 7 clear days before the return date of the application under Rule 3(1)" ; "At least 7 clear days before the return date of the application under Rule 3(1)" | NOTHING |
| `o 63 r 4(4) the claimant serves a copy of the affidavit on the third party in time` | order-63:613 | period fixed in the text's own words (ruling of 2026-11-05 (a)) | "within 3 days of the filing of the same" ; "within 3 days of the filing of the same" | NOTHING (outside the period the text is silent) |
| `o 63 r 5(1) the Court may give directions or make orders after the hearing` | order-63:693 | the text's no in other words (flat negative, deeming or exclusion) | "provided all the persons on whom the application has been served and all claimants who ..." ; "the Court may, after hearing" | NOTHING |
| `o 63 r 5(1) the Court may give this kind of direction or make this kind of order` | order-63:730 | the text's no in other words (flat negative, deeming or exclusion) | "the Court may, after hearing" | NOTHING |
| `o 63 r 5(2) the Court may make such order as it deems appropriate` | order-63:751 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where the third party (or, where applicable, any other interested party referred to in ..." | NOTHING (an unmet condition is silence, not a no) |
| `o 63 r 5(3) the Court may declare the claimant forever barred` | order-63:765 | unmet condition: if / where / when / upon / after (ruling (b)) | "Where a claimant, having filed an affidavit of claim under Rule 4, does not appear on t..." | NOTHING (an unmet condition is silence, not a no) |

### Reading a result: FALSE and NOTHING (roc11)

Every question in this row has the answer type `MAYBE BOOLEAN` (a few ask for a string, a list or a date and say so).
**`JUST TRUE`** means the text of Orders 57 to 63 says yes on the facts given: the thing is allowed, required, applies, or is in time.
**`JUST FALSE`** means the text says no in its own words. In this row that is one of five things: a "means" definition and the case lies outside it; a flat negative ("no order may be made", "does not apply", "is not required"); a period the text fixes ("not later than 14 days", "until after the expiry") and the act lies outside it; a condition the clause itself states ("where", "if", "upon", "when", "after hearing") that the facts do not meet; or a duty or deeming that the clause lifts by its own exception ("unless the Court otherwise directs").
**`NOTHING`** means the Orders do not answer on these facts. In this row that is: a rule that reaches only the cases it names ("An application under section 4", "a civil penalty action") and the facts are outside it; a bare "must" that was not done, where the Orders say nothing about the consequence (O 3 r 2(4) says what the Court may do about non-compliance); a bar that has been lifted by its exception, which grants nothing; a list that is not closed ("includes", "called"); a term defined in the Act, which is not among the sources; a point decided by another Order.
A caller must never turn `NOTHING` into `FALSE`: "not covered" is not "not allowed".
An answer that comes back `NOTHING` means the question goes to a lawyer or to the Order named in the comment beside the branch.

## Seams (roc11)

Each seam below is a plain input in layer 1 and in the seat; the merged file replaces it with a call to the part that owns the answer.

| seam (PLAN.md section 8) | what roc11 takes | where |
| --- | --- | --- |
| S-T1 `o 3 r 3 the last day for doing the act` | a `DATE` input wherever the text fixes a period: "at least N clear days before", "within N days after", "not later than". The seat asks for it as the last day "counted as Order 3, Rule 3 counts it" and compares the act's date with it; both sides of every last day are tested. | O 57 r 5(3), r 8(1), r 10(1), r 12, r 13; O 59 r 2(2), r 2(3), r 2(3)(b), r 7(3), r 12(2); O 60 r 8(1), r 10(1); O 61 r 3(5), r 3(6), r 4(1), r 4(4); O 62 r 4(1), r 4(3), r 4(4), r 5(1); O 63 r 2(4), r 3(3), r 3(4), r 4(1), r 4(4) |
| S-T1 variants | `o 6 r 6 the last day for filing and serving a notice of intention to contest or not contest` (O 59 r 2(2), O 62 r 4); `the last day of the period fixed under these Rules for service of the defence` (O 62 r 5(1)). The plan has no names for these two; the merged file should wire them to roc2 (Order 6). | O 59 r 2(2); O 62 r 4(1), r 5(1) |
| S-T2 `o 3 r 4 the last day as extended or shortened` | not threaded. The last-day input is whatever last day the person gives; one who has an extension under O 3 r 4 gives the extended day. | all |
| S-S1 `o 7 r 8 the day service is deemed effected` | not threaded by name. "The date it was served" is a plain `DATE` input. The return date of an application is fixed by the Court and is an input. | O 59 r 2(3)(b), r 7(3), r 12(2); O 61 r 3(5); O 63 r 2(4), r 3(3) |
| S-F1 `o 28 r 10 the moment the document is deemed filed` | not threaded. "The date I filed" is a plain `DATE` input, not a `Moment`; the merge may take the date part of roc7's answer. | O 61 r 4(1); O 63 r 4(1) |
| S-L1 (applies with changes) | `JUST TRUE` that the other provision applies; the changes are left to its part. | O 59 r 12(3); O 62 r 2(2), r 8(1)-(2); O 63 r 8 |
| S-L2 (an override that switches another provision off) | a flat statement about the overridden provision, `JUST FALSE`; the overridden part does not thread an input. | O 59 r 3(1), (3), r 4(1), r 5(1), r 11(1), r 12(1); O 62 r 10 |
| S-P1 (Forms) | the Form number as a `STRING` constant: Form 22 (O 62 r 7(2)), 86 (O 57 r 5(1)), 87 (O 59 r 11(3)), 88 (O 60 r 5(1)), 91 (O 61 r 3(6)), 92 (O 63 r 2(6)), 93 (O 63 r 3(4)). | as listed |
| not in the plan: Orders cannot import each other | O 63 r 8 applies rules of Order 62 to the Authority's application; roc11 cannot import its own Order 62 module into Order 63 under the parts rule, so it takes the rule number as a `STRING` input (`rule number of Order 62`). | O 63 r 8 |

A merged seat should also wire the last-day inputs to roc1's `o 3 r 3 the last day for doing the act` so the person is not asked to count days; the seat's `@desc` text says how the day is counted, so the question reads the same after the wiring.

## Dependencies (roc11)

Every layer-1 file imports `prelude`, `daydate` and `roc-core`; none copies a name from another part.
Time is counted by O 3 r 3 (roc1), which by O 3 r 3(1) disapplies the Interpretation Act for the Rules' time; roc11 asks for the result as an input and does not count days.

## Unstable dialect (roc11)

I looked at time, versions and workarounds and found none to record: the `wef` markers in the range are all 01/03/2023, before 2026-04-01, and nothing here needs the unstable dialect.

## What the text turns out to say (roc11)

1. O 60 r 9(3) is blank in this text: "[ Deleted by S 91/2023 wef 01/03/2023 ]" (raw line 7016). It is the only deleted subrule in the range; its row is `repealed or blank in this text`. All 12 `wef` markers in the range read 01/03/2023.
2. O 59 r 2(3) gives two ends to the time to contest, "(a) 4 days after the defendant has notified ... satisfied" and "(b) 4 days after the Court has ... decided", joined by "or", and does not say which governs if both happen. roc11 takes the earlier (fork `O 59 r 2(3)`).
3. O 62 r 8(6) bars an order for the seven described kinds of document ("except that no order may be made in respect of a document falling within any of the following descriptions"). The sentence is about "any document apart from those listed in paragraphs (4) and (5)", and the "except that" ends it, so the text can be read two ways when a document is both listed and described (for example a document the Authority relies on, (4)(k), that is also its internal books, (6)(c)). roc11 reads the exclusion as flat, because it is worded "a document" and because description (f) carves paragraph (5) out of itself by name, which would be surplus if the exclusion could not reach a listed document; a listed document that is also described therefore answers `JUST FALSE`. The other reading (the exception is to the "unless" limb only, and (4) and (5) are untouched, "may also be ordered") is recorded in the fork (`O 62 r 8(6)`).
4. O 62 r 4(4) lets the Authority "enter judgment with the permission of the Court" but does not say what follows without it; roc11 answers `NOTHING` (fork `O 62 r 4(4)`).
5. O 61 r 3(8) and O 63 r 3(6) end with "unless the Court otherwise directs" after two consequences joined by "and" (cancel the appointment; deem the application dismissed); the text does not say whether the exception reaches both. roc11 reads it as reaching both (forks).
6. O 63 r 5(1) has a proviso ("provided ...") that stands after item (c) only; roc11 attaches it to (c) alone (fork `O 63 r 5(1)`).
7. O 57 r 10(2) and O 60 r 10(2) are passive ("must not be issued"): they name no one who is barred. The regulative rule has a placeholder party.
8. O 63 r 8 applies Order 62 rules 6, 7, 8, 10 and 12 to the Authority's application against a third party "with the necessary modifications". Because a part cannot import another, roc11 can only say that the rule applies (`JUST TRUE`) and what the defendant means in rule 8 (`o 63 r 8(2)`), not run Order 62's answers.
9. Flat negatives in Orders 59, 62 and 63 name the bearer only by role ("a person", "the Court", "the Authority") and have no `SHANT` rule; the yes/no functions carry them (ruling N2 says the prohibition is derived "where the text names who bears" it; roc11 derived it only for the "until" bars with traces). This is a gap against N2 that the merge has to decide: adding a `SHANT` rule for each flat negative with a named bearer touches `o 59 r 4(1)`, `o 59 r 8(2)`, `o 62 r 7(1)`, `o 62 r 8(6)` and similar sites.
10. `NOT (x) AND y` and `NOT (x) OR y` group as `NOT (x AND y)` and `NOT (x OR y)` on both 1.6.109 and 1.6.108, and nothing warns (a two-assertion file in `work/scratch/notprec.l4` passes on both builds only because `(NOT (TRUE) AND FALSE)` is `TRUE` and `(NOT (TRUE) OR TRUE)` is `FALSE`). A test caught it in `o 59 r 12(1)` (the case "attachment order, no money due from the Government" came back `JUST FALSE` instead of `NOTHING`: `roc11-tests-order-59.l4` line 257 failed until the left operand was written `(NOT (x)) AND y`). A scan of all seven sources (`work/` script, balanced parentheses) finds no other site.
11. O 62 r 12(1) ends "... on the ground of the death or the bankruptcy or winding up of the defendant, or the commencement of bankruptcy or winding up proceedings against the defendant, after the commencement of the civil penalty action". The text does not say whether "after the commencement of the civil penalty action" governs every ground or only the last. roc11 takes every ground (so a death or bankruptcy that predates the action is outside the bar); the function has one input that the person answers on that reading (fork `O 62 r 12(1)`).
12. O 57 r 3 names three classes with "(called in this Order a Direction / a Notice / a Decision)" and defines two others in rule 1 with "means". roc11 treats the first form as a naming (`NOTHING` outside the description) and the second as a definition (`JUST FALSE`); the text itself does not say the two forms differ (forks `O 57 r 3(a)`, `(b)`, `(c)`).
13. A rule that restricts a grant to those who "make" a payment or file by a date is encoded with the date as an input; no function adds a day to a date. "After the time limited" is `GREATER THAN` the last day, and "before the expiry" is `AT MOST` the last day, so both sides of every last day are tested.

### What the text does not answer (roc11)

Things a person may ask that Orders 57 to 63 leave to another instrument or to the Court, so that no function answers them (each is `NOTHING` or not asked):

- The court fee for an application to register (O 57 r 3): not in these Orders.
- The number of days in the period to apply to set aside a registration (O 57 r 5(2), O 60 r 5(2)): the Rules say the order "must state" the period and leave its length to each order.
- The limitation period for an action under section 234 (O 61 r 2(1)): not in these Orders.
- Whether the Government may be ordered to give security for costs (O 59): the Order does not say.
- The amount of a civil penalty (O 62): not in the Order.
- How a copy is served on the Commission (O 57 r 12): the rule fixes the time (not later than 14 days) and not the mode.
- When the time to file a notice of intention to contest expires once the bar of O 59 r 2(3) lifts: the text says it "does not expire until" a stated event and gives no expiry date of its own.
- Whether the Court may order the judgment debtor, and not the judgment creditor, to give security (O 60 r 4): the text speaks of the judgment creditor only.
- Whether the Court may direct that the O 60 r 5(2) order need not state the set-aside period: unlike O 57 r 5(2), O 60 r 5(2) has no "unless the Court otherwise directs", and the encoding has no input for a direction there.
- Whether the Court may set a registration aside "on such terms as the Court thinks fit" under Order 60: O 57 r 9(3) says so for a registration under Order 57, and O 60 r 9(3) is deleted, so Order 60 says nothing equivalent.
- Who bears the duty in O 57 r 12 (the claimant in the section 48O(1) proceedings) and O 57 r 13 (the person granted the judgment or order): the person who bears it is the PARTY of the regulative rule, and a yes/no function does not ask it.

## What the main binary does not accept (roc11)

Checked on main 1.6.109 and 1.6.108 (check.sh runs both).
- **Loud.** `kind NOT EQUALS x` is a parse error (`parse/unexpected-NOT`, found at `o 59 r 12(1)` while writing O 59); write `NOT (kind EQUALS x)`.
- **Loud.** A parameter named like a top-level function (the parameter `the notice is endorsed in time` inside the function of that name in O 57 r 8(1)) gave an error; the parameter was renamed `the answer on whether the notice was endorsed in time`.
- Not used, checked by `grep` over the 18 files of this folder: `REFUSE`, `#CHECK`, `YMD`, `TYPICALLY`, set operations (`SET OF`, `setFromList`, `UNION`) and `•` bullets (the brief bans them or main rejects them); every `BECAUSE` follows a `LEST BREACH`; `WAIT UNTIL` is spelled `WAITUNTIL`.
- **Silent, exit 0.** `NOT (x) AND y` and `NOT (x) OR y` misgroup (finding 10). Every `NOT` in layer 1 is now parenthesised with its operand and the other operand outside the `NOT`.
- **Silent.** A trace prints `FULFILLED` or `BREACH` and no assertion line, so `check.sh` counts cannot see a difference between builds. The 24 traces (O 57: 11, O 60: 7, O 61: 4, O 63: 2) were read by hand (`DOES` at the last day is `FULFILLED`, `WAITUNTIL` after it is `BREACH`), and the full `l4 run` output of each of the four files is byte-identical on 1.6.109 and 1.6.108 (md5 equal).
- A list of strings is written as a vertical `LIST` block, one string per line, with commas; an inline `LIST "a", "b"` of two or more strings is not used (`work/vertlist.py` rewrote 11 such lists).

## What check.sh prints (roc11)

Run from this folder as `L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh` (target main); exit status 0.
The two keel modules (`roc-core.l4`, `roc-definitions.l4`) print 0 errors and 0 assertions in this run, so the baseline the 16 roc11 modules were added to is 2 modules and 0 satisfied assertions (no earlier run was made); with roc11 the total is 18 modules and 1801 satisfied assertions, 0 failed, 0 refused, all 18 `same` on main 1.6.108.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc11-cases-seat.l4                            0       663       0        0         0 |      0       663       0        0  same
roc11-order-57.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-58.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-59.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-60.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-61.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-62.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-order-63.l4                              0         0       0        0         0 |      0         0       0        0  same
roc11-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
roc11-tests-order-57.l4                        0       215       0        0         0 |      0       215       0        0  same
roc11-tests-order-58.l4                        0        29       0        0         0 |      0        29       0        0  same
roc11-tests-order-59.l4                        0       202       0        0         0 |      0       202       0        0  same
roc11-tests-order-60.l4                        0       146       0        0         0 |      0       146       0        0  same
roc11-tests-order-61.l4                        0       182       0        0         0 |      0       182       0        0  same
roc11-tests-order-62.l4                        0       207       0        0         0 |      0       207       0        0  same
roc11-tests-order-63.l4                        0       157       0        0         0 |      0       157       0        0  same
TOTAL (18 modules)                             0      1801       0        0           |      0      1801       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

