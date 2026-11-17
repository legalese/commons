# NOTES: the Criminal Code (Canada), lines 16684-17450 (ccc29): Part XXVII (summary convictions), Part XXVIII (miscellaneous) and the schedules in them

Status of this file, 2026-11-17: written and checked against the deposit in the same session; the counts of the coverage table, the fork register, the name-test sweep and the check.sh figures were produced by scripts that read the files (the generators are in `work/`), the audit counts, the findings and the party columns of the Hohfeld table were written by hand, and `check.sh` was run on both stable builds after the last edit to a `.l4` file (section "What check.sh prints").
Nothing here is verified against the official text: the source is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation; `inputs/SOURCES.md` records that the Justice Laws index page gave the Act as current to 2026-09-30 and last amended on 2026-07-18, and that is a statement about the page, not a check of this text.
The defined terms in the text carry their French equivalents in parentheses (`clerk of the appeal court ... (greffier de la cour d'appel)`); the quote lines of the layer-1 comments copy them verbatim, and nothing French is encoded.

## What this part is

- Part agent `ccc29`, one of 32; ranges 16684-17450 (`inputs/PARTS.md`): sections 785 to 849, the schedule to Part XX.1 (repealed), the schedule to Part XXII.1, the schedule to Part XXV (section 762) and the schedule to Part XXVII (section 840).
  The Forms (Form 1 and after) begin at line 17451, which `inputs/PARTS.md` gives to ccc30; there is no Form text in this part's range, and section 849's reference to the Forms is encoded as the rule it states.
- Layer 1 (the law, objectively) is eight modules, one schedule module and their test files; layer 2 is the seat layer `ccc29-seat.l4` with its cases `ccc29-cases-seat.l4`.
- Where `inputs/PLAN.md` and the brief or `inputs/PARTS.md` differ, the brief governs.
  Three places: (1) PLAN names the seam other parts ask `Schedule to Part XXII.1 the offence is listed`; the brief's naming rule makes every name begin with the provision's own label, so the function is `sch XXII.1 the offence is listed` (the lead joins the two names at the merge); (2) PLAN says "then Forms 1 to the point where ccc30 begins", while `inputs/PARTS.md` ends this part's range at line 17450, before Form 1 at line 17451, so this part encodes no Form; (3) PLAN names the input it expects from ccc11 `s 320.11 the person is an analyst`; the input in this part is `s 320.11 the person is an analyst` (an input's name is local to its function, and the lead binds it to ccc11's function at the merge).
- The three modules of the keel are read-only copies.
  This part does not edit them and does not redefine any name they define.

## Seat

The seat is a person who is, or may be, accused of an offence under the Criminal Code (the accused).
The seat layer asks, in the person's own terms, what the summary-conviction procedure does to them (the time limit, the general penalty, how they may appear, what the court may do in their absence, costs), what a peace bond can require of them and what happens if they refuse, how they appeal and by when, and the electronic-document and schedule provisions that touch them.
There is never a seat for an official: a duty or power of a court, a justice or a clerk appears only as what it means to the person.
The seat has 74 questions in six groups (the `§` headings of `ccc29-seat.l4`); the audit of their names is in "Seat-question audit (ccc29)".
Schedule XXV (which court and officer hold a release order or recognizance in each province) is a table that designates officials; it has layer-1 functions but no seat question, because it answers nothing a person states facts about.

## Coverage (ccc29)

One row per section, subsection, paragraph, subparagraph, defined term, schedule paragraph, schedule item and table row of lines 16684-17450, built from the text by `work/coverage.py` (a script that reads the raw file); every one of the 741 non-blank lines of the range falls in at least one row (the script asserts it).
The L4 names are the declarations whose `@ref` locator covers the row most narrowly (found by a script over the generated `.l4` files, not typed).
A row whose disposition is `fork` is encoded too: the fork register says which reading the encoding takes.

| disposition | rows |
| --- | --- |
| encoded | 355 |
| fork | 107 |
| inert (reason 1) | 37 |
| inert (reason 2) | 5 |
| inert (reason 3) | 0 |
| repealed or blank in this text | 23 |
| total | 527 |

"Encoded" is read from the `@ref` locators: a row is encoded when a declaration's `@ref` span contains it, the narrowest span being the one named.
58 rows are covered only by a span more than 25 lines wider than the row: the 28 entries of paragraph 1 of schedule XXII.1 (one table function, `sch XXII.1 para 1 the words of the entry that names the provision`) and the 30 items of schedule XXVII that carry an amount (one table function, `sch XXVII the amount in dollars stated in the row of the item`); each of those rows has its own branch and its own generated assertion (for example `ccc29-tests-xxviii-7-schedules.l4` lines 79 and 215), and the generated test file was read for item 3 and item 29 and for entry (z.4).

Rows left `inert`: the headings and the editorial note (reason 1: not operative); the five rows of section 810.3(5), the Governor in Council's power to make regulations (reason 2: machinery).
No row is `out-of-scope` or `deferred`.

| row | lines | kind | disposition | fork | L4 name(s) |
| --- | --- | --- | --- | --- | --- |
| PART XXVII | 16684-16684 | part-heading | inert (reason 1) |  |  |
| heading: Interpretation @16686 | 16686-16686 | heading | inert (reason 1) |  |  |
| s 785 lead-in | 16687-16688 | lead-in | encoded |  | `s 785 the definitions apply` |
| s 785 "clerk of the appeal court" | 16689-16689 | definition | encoded |  | `s 785 clerk of the appeal court` |
| s 785 "informant" | 16690-16690 | definition | encoded |  | `s 785 informant` |
| s 785 "information" | 16691-16691 | definition | encoded |  | `s 785 information` |
| s 785 "information" (a) | 16692-16692 | def-paragraph | encoded |  | `s 785 information` |
| s 785 "information" (b) | 16693-16693 | def-paragraph | encoded |  | `s 785 information` |
| s 785 "order" | 16694-16694 | definition | encoded |  | `s 785 order` |
| s 785 "proceedings" | 16695-16695 | definition | encoded |  | `s 785 proceedings` |
| s 785 "proceedings" (a) | 16696-16696 | def-paragraph | encoded |  | `s 785 proceedings` |
| s 785 "proceedings" (b) | 16697-16697 | def-paragraph | encoded |  | `s 785 proceedings` |
| s 785 "prosecutor" | 16698-16698 | definition | encoded |  | `s 785 prosecutor: who the person is`; `s 785 prosecutor` |
| s 785 "sentence" | 16699-16699 | definition | encoded |  | `s 785 sentence` |
| s 785 "sentence" (a) | 16700-16700 | def-paragraph | encoded |  | `s 785 sentence` |
| s 785 "sentence" (b) | 16701-16701 | def-paragraph | encoded |  | `s 785 sentence` |
| s 785 "sentence" (c) | 16702-16702 | def-paragraph | encoded |  | `s 785 sentence` |
| s 785 "sentence" (d) | 16703-16703 | def-paragraph | encoded |  | `s 785 sentence` |
| s 785 "sentence" (e) | 16704-16704 | def-paragraph | encoded |  | `s 785 sentence` |
| s 785 "summary conviction court" | 16705-16705 | definition | encoded |  | `s 785 summary conviction court` |
| s 785 "summary conviction court" (a) | 16706-16706 | def-paragraph | encoded |  | `s 785 summary conviction court` |
| s 785 "summary conviction court" (b) | 16707-16707 | def-paragraph | encoded |  | `s 785 summary conviction court` |
| s 785 "summary conviction court" (c) | 16708-16708 | def-paragraph | encoded |  | `s 785 summary conviction court` |
| s 785 "trial" | 16709-16709 | definition | encoded |  | `s 785 trial` |
| s 786(1) | 16710-16711 | subsection | encoded |  | `s 786(1) this Part applies to the proceedings` |
| s 786(2) | 16712-16713 | subsection | fork | F-786-2 | `s 786(2) the proceedings are barred because they were instituted more than 12 months after the subject matter arose`; `s 786(2) the day on which the 12 months end` |
| heading: Punishment @16715 | 16715-16715 | heading | inert (reason 1) |  |  |
| s 787(1) | 16716-16717 | subsection | fork | F-787-1 | `s 787(1) the general penalty as stated in section 787(1)`; `s 787(1) the general penalty applies to the offence`; `s 787(1) the fine is not more than $5,000`; `s 787(1) the term of imprisonment is not more than two years less a day` |
| s 787(2) | 16718-16719 | subsection | fork | F-787-2 | `s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order`; `s 787(2) the longest term of imprisonment the court may order in default` |
| heading: Information @16721 | 16721-16721 | heading | inert (reason 1) |  |  |
| s 788(1) | 16722-16723 | subsection | encoded |  | `s 788(1) the proceedings are required to be commenced by laying an information in Form 2`; `s 788(1) the informant is to lay an information in Form 2` |
| s 788(2) | 16724-16725 | subsection | encoded |  | `s 788(2) one justice may do the act` |
| s 788(2)(a) | 16726-16726 | paragraph | encoded |  | `s 788(2) act` |
| s 788(2)(b) | 16727-16727 | paragraph | encoded |  | `s 788(2) act` |
| s 788(2)(c) | 16728-16728 | paragraph | encoded |  | `s 788(2) act` |
| s 789(1) | 16729-16730 | subsection | encoded |  | `s 789(1)(a) the information is required to be in writing and under oath` |
| s 789(1)(a) | 16731-16731 | paragraph | encoded |  | `s 789(1)(a) the information is required to be in writing and under oath` |
| s 789(1)(b) | 16732-16732 | paragraph | encoded |  | `s 789(1)(b) the information may charge more than one offence or relate to more than one matter of complaint`; `s 789(1)(b) each offence or matter of complaint is required to be set out in a separate count` |
| s 789(2) | 16733-16734 | subsection | encoded |  | `s 789(2) the information is barred from containing any reference to previous convictions` |
| s 790(1) | 16735-16736 | subsection | encoded |  | `s 790(1) the justice is not required to be a justice before whom the trial is held` |
| s 790(2) | 16737-16738 | subsection | fork | F-790-2 | `s 790(2) the justices are required to be present and act together at the trial`; `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` |
| s 790(3) | 16739-16739 | repealed | repealed or blank in this text |  |  |
| s 790(4) | 16739-16739 | repealed | repealed or blank in this text |  |  |
| s 791 | 16740-16740 | repealed | repealed or blank in this text |  |  |
| s 792 | 16741-16741 | repealed | repealed or blank in this text |  |  |
| heading: Defects and Objections @16743 | 16743-16743 | heading | inert (reason 1) |  |  |
| s 793 | 16744-16744 | repealed | repealed or blank in this text |  |  |
| s 794(1) | 16745-16746 | subsection | encoded |  | `s 794(1) the information need not set out or negative the exception, exemption, proviso, excuse or qualification` |
| s 794(2) | 16747-16747 | repealed | repealed or blank in this text |  |  |
| heading: Application @16749 | 16749-16749 | heading | inert (reason 1) |  |  |
| s 795 | 16750-16751 | section | encoded |  | `s 795 Part of the Code`; `s 795 the provisions apply, with any necessary modifications, to proceedings under this Part`; `s 795 compelling appearance`; `s 795 not inconsistent` |
| s 796 | 16752-16752 | repealed | repealed or blank in this text |  |  |
| s 797 | 16752-16752 | repealed | repealed or blank in this text |  |  |
| heading: Trial @16754 | 16754-16754 | heading | inert (reason 1) |  |  |
| s 798 | 16755-16756 | section | encoded |  | `s 798 the summary conviction court has jurisdiction to try, determine and adjudge the proceedings` |
| s 799 | 16757-16758 | section | fork | F-799 | `s 799 course`; `s 799 the summary conviction court may take the course` |
| s 800(1) | 16759-16760 | subsection | encoded |  | `s 800(1) the summary conviction court is required to hold the trial`; `s 800(1) the court is to hold the trial` |
| s 800(2) | 16761-16762 | subsection | fork | F-800-2 | `s 800(2) way of appearing`; `s 800(2) a defendant may appear in the way`; `s 800(2) the summary conviction court may require the defendant to appear personally`; `s 800(2) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await the defendant's appearance` |
| s 800(2.1) | 16763-16763 | repealed | repealed or blank in this text |  |  |
| s 800(3) | 16764-16765 | subsection | fork | F-800-3 | `s 800(3) the organization is required to appear by counsel or agent`; `s 800(3) the summary conviction court may proceed ex parte to hold the trial` |
| s 801(1) | 16766-16767 | subsection | encoded |  | `s 801(1) the substance of the information is required to be stated to the defendant` |
| s 801(1)(a) | 16768-16768 | paragraph | encoded |  | `s 801(1)(a) the defendant is required to be asked whether they plead guilty or not guilty to the information` |
| s 801(1)(b) | 16769-16769 | paragraph | encoded |  | `s 801(1)(b) the defendant is required to be asked whether they have cause to show why an order should not be made against them` |
| s 801(2) | 16770-16771 | subsection | encoded |  | `s 801(2) the summary conviction court is required to convict the defendant, discharge the defendant under section 730 or make an order against the defendant` |
| s 801(3) | 16772-16773 | subsection | encoded |  | `s 801(3) the summary conviction court is required to proceed with the trial and take the evidence in accordance with Part XVIII` |
| s 801(4) | 16774-16774 | repealed | repealed or blank in this text |  |  |
| s 801(5) | 16774-16774 | repealed | repealed or blank in this text |  |  |
| s 802(1) | 16775-16776 | subsection | fork | F-802-1 | `s 802(1) the prosecutor is entitled personally to conduct the case`; `s 802(1) the defendant is entitled to make full answer and defence` |
| s 802(2) | 16777-16778 | subsection | encoded |  | `s 802(2) way of examining`; `s 802(2) the prosecutor or defendant may examine and cross-examine witnesses in the way` |
| s 802(3) | 16779-16780 | subsection | encoded |  | `s 802(3) the witness is required to be examined under oath` |
| s 802.1 | 16781-16782 | section | encoded |  | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` |
| s 802.1(a) | 16783-16783 | paragraph | encoded |  | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` |
| s 802.1(b) | 16784-16784 | paragraph | encoded |  | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` |
| s 802.1(c) | 16785-16785 | paragraph | encoded |  | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` |
| s 803(1) | 16786-16787 | subsection | fork | F-803-1 | `s 803(1) the summary conviction court may adjourn the trial to a time and place to be appointed and stated in the presence of the parties or their counsel or agents` |
| s 803(1.1) | 16788-16789 | subsection | encoded |  | `s 803(1.1) the summary conviction court is required to consider the interests of justice`; `s 803(1.1) the summary conviction court is required to consider the interests of any victim of the offence in question` |
| s 803(2) | 16790-16791 | subsection | fork | F-803-2 | `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant` |
| s 803(2)(a) | 16792-16792 | paragraph | fork | F-803-2 | `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant` |
| s 803(2)(b) | 16793-16793 | paragraph | fork | F-803-2 | `s 803(2)(b) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await their appearance under the warrant` |
| s 803(3) | 16794-16795 | subsection | encoded |  | `s 803(3) the consent of the Attorney General is required before the proceedings under section 145 are instituted or proceeded with` |
| s 803(4) | 16796-16797 | subsection | fork | F-803-4 | `s 803(4) the summary conviction court may dismiss the information with or without costs` |
| s 803(5) | 16798-16798 | repealed | repealed or blank in this text |  |  |
| s 803(6) | 16798-16798 | repealed | repealed or blank in this text |  |  |
| s 803(7) | 16798-16798 | repealed | repealed or blank in this text |  |  |
| s 803(8) | 16798-16798 | repealed | repealed or blank in this text |  |  |
| heading: Adjudication @16800 | 16800-16800 | heading | inert (reason 1) |  |  |
| s 804 | 16801-16802 | section | encoded |  | `s 804 the summary conviction court is required to convict the defendant, discharge the defendant under section 730, make an order against the defendant or dismiss the information`; `s 804 the court is to decide` |
| s 805 | 16803-16803 | repealed | repealed or blank in this text |  |  |
| s 806(1) | 16804-16805 | subsection | encoded |  | `s 806(1) a minute or memorandum indicating that the matter was dealt with under this Part is required to be made by the summary conviction court`; `s 806(1) a conviction or order in Form 35 or 36 and a certified copy are required to be drawn up and the certified copy delivered to the person making the request`; `s 806(1) the form to be drawn up` |
| s 806(2) | 16806-16807 | subsection | encoded |  | `s 806(2) the summary conviction court is required to issue a warrant of committal in Form 21 or 22`; `s 806(2) the court is to issue a warrant of committal`; `s 806(2) section 528 applies in respect of the warrant of committal` |
| s 806(3) | 16808-16809 | subsection | encoded |  | `s 806(3) the copy of the warrant of committal is admissible in evidence in any proceeding` |
| s 807 | 16810-16811 | section | encoded |  | `s 807 the most that is to be paid to the person aggrieved`; `s 807 the residue to be applied in the manner in which other penalties imposed by law are directed to be applied` |
| s 808(1) | 16812-16813 | subsection | fork | F-808-1 | `s 808(1) the summary conviction court may draw up an order of dismissal`; `s 808(1) the summary conviction court is required to give the defendant a certified copy of the order of dismissal` |
| s 808(2) | 16814-16815 | subsection | encoded |  | `s 808(2) the certified copy of the order of dismissal is a bar to the subsequent proceedings` |
| s 809(1) | 16816-16817 | subsection | fork | F-809-1 | `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant` |
| s 809(1)(a) | 16818-16818 | paragraph | fork | F-809-1 | `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant` |
| s 809(1)(b) | 16819-16819 | paragraph | fork | F-809-1 | `s 809(1)(b) the summary conviction court may award costs to be paid to the defendant by the informant` |
| s 809(2) | 16820-16821 | subsection | encoded |  | `s 809(2) the order for costs is required to be set out in the conviction, order or order of dismissal` |
| s 809(3) | 16822-16823 | subsection | encoded |  | `s 809(3) the amount for which the defendant is liable to serve the term of imprisonment imposed in default of payment` |
| s 809(4) | 16824-16825 | subsection | encoded |  | `s 809(4) the person who is liable to pay the costs is, in default of payment, liable to imprisonment for one month`; `s 809(4) the term of imprisonment in default of payment of the costs` |
| s 809(5) | 16826-16827 | subsection | encoded |  | `s 809(5) costs` |
| heading: Sureties to Keep the Peace @16829 | 16829-16829 | heading | inert (reason 1) |  |  |
| s 810(1) | 16830-16831 | subsection | fork | F-810-1 | `s 810(1) an information may be laid before a justice` |
| s 810(1)(a) | 16832-16832 | paragraph | encoded |  | `s 810(1) feared event` |
| s 810(1)(b) | 16833-16833 | paragraph | encoded |  | `s 810(1) feared event` |
| s 810(2) | 16834-16835 | subsection | encoded |  | `s 810(2) the justice is required to cause the parties to appear`; `s 810(2) the justice is to cause the parties to appear` |
| heading: Adjudication @16836 | 16836-16836 | heading | inert (reason 1) |  |  |
| s 810(3) | 16837-16837 | subsection | fork | F-810-3 | `s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties`; `s 810(3) the period of the recognizance is not more than 12 months` |
| s 810(3.01) | 16838-16839 | subsection | fork | F-810-3.01 | `s 810(3.01) the justice or court may commit the defendant to prison`; `s 810(3.01) the term of imprisonment is not more than 12 months` |
| s 810(3.02) | 16840-16841 | subsection | encoded |  | `s 810(3.02) the justice or court may add the condition to the recognizance` |
| s 810(3.02)(a) | 16842-16842 | paragraph | encoded |  | `s 810(3.02) condition` |
| s 810(3.02)(b) | 16843-16843 | paragraph | encoded |  | `s 810(3.02) condition` |
| s 810(3.02)(c) | 16844-16844 | paragraph | encoded |  | `s 810(3.02) condition` |
| s 810(3.1) | 16845-16846 | subsection | encoded |  | `s 810(3.1) the justice or court is required to consider whether a firearms prohibition is desirable`; `s 810(3.1) the justice or court is required to add the firearms condition`; `s 810(3.1) the justice or court is to consider the firearms condition`; `s 810(3.1) the justice or court is to add the firearms condition if it is desirable` |
| s 810(3.11) | 16847-16848 | subsection | encoded |  | `s 810(3.11) the justice or court is required to specify in the order the manner and method`; `s 810(3.11) the justice or court is to specify the manner and method` |
| s 810(3.11)(a) | 16849-16849 | paragraph | encoded |  | `s 810(3.11) matter to be specified` |
| s 810(3.11)(b) | 16850-16850 | paragraph | encoded |  | `s 810(3.11) matter to be specified` |
| s 810(3.12) | 16851-16852 | subsection | encoded |  | `s 810(3.12) the justice or court is required to include in the record a statement of the reasons for not adding the condition`; `s 810(3.12) the justice or court is to include a statement of reasons in the record` |
| s 810(3.2) | 16853-16854 | subsection | encoded |  | `s 810(3.2) the justice or court is required to consider whether it is desirable to add the condition`; `s 810(3.2) the justice or court is to consider the supplementary conditions` |
| s 810(3.2)(a) | 16855-16855 | paragraph | encoded |  | `s 810(3.2) supplementary condition` |
| s 810(3.2)(b) | 16856-16856 | paragraph | encoded |  | `s 810(3.2) supplementary condition` |
| s 810(4) | 16857-16858 | subsection | encoded |  | `s 810(4) the warrant of committal may be in Form 23` |
| s 810(4.1) | 16859-16860 | subsection | fork | F-810-4.1 | `s 810(4.1) the justice or court may vary the conditions fixed in the recognizance` |
| s 810(5) | 16861-16862 | subsection | encoded |  | `s 810(5) the provisions of this Part apply to the proceedings` |
| s 810.01(1) | 16863-16864 | subsection | fork | F-810.01-1 | `s 810.01(1) the person may lay an information before a provincial court judge` |
| s 810.01(2) | 16865-16866 | subsection | encoded |  | `s 810.01(2) the provincial court judge may cause the parties to appear` |
| heading: Adjudication @16867 | 16867-16867 | heading | inert (reason 1) |  |  |
| s 810.01(3) | 16868-16868 | subsection | fork | F-810.01-3 | `s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance`; `s 810.01(3) the period of the recognizance is not more than 12 months` |
| s 810.01(3.1) | 16869-16870 | subsection | fork | F-810.01-3.1 | `s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period`; `s 810.01(3.1) the longer period of the recognizance is not more than two years` |
| s 810.01(4) | 16871-16872 | subsection | fork | F-810.01-4 | `s 810.01(4) the provincial court judge may commit the defendant to prison`; `s 810.01(4) the term of imprisonment does not exceed twelve months` |
| s 810.01(4.1) | 16873-16874 | subsection | encoded |  | `s 810.01(4.1) the provincial court judge may add the condition to the recognizance` |
| s 810.01(4.1)(a) | 16875-16875 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(b) | 16876-16876 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(c) | 16877-16877 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(d) | 16878-16878 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(e) | 16879-16879 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(f) | 16880-16880 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(4.1)(g) | 16881-16881 | paragraph | encoded |  | `s 810.01(4.1) condition` |
| s 810.01(5) | 16882-16883 | subsection | encoded |  | `s 810.01(5) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.01(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.01(5) the judge is to consider the firearms condition`; `s 810.01(5) the judge is to add the firearms condition if it is desirable` |
| s 810.01(5.1) | 16884-16885 | subsection | encoded |  | `s 810.01(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.01(5.1) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.01(5.2) | 16886-16887 | subsection | encoded |  | `s 810.01(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition`; `s 810.01(5.2) the judge is to include a statement of reasons in the record` |
| s 810.01(6) | 16888-16889 | subsection | fork | F-810.01-6 | `s 810.01(6) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.01(7) | 16890-16891 | subsection | encoded |  | `s 810.01(7) subsections 810(4) and (5) apply to the recognizance` |
| s 810.01(8) | 16892-16893 | subsection | encoded |  | `s 810.01(8) person`; `s 810.01(8) Attorney General` |
| s 810.011(1) | 16894-16895 | subsection | fork | F-810.011-1 | `s 810.011(1) the person may lay an information before a provincial court judge` |
| s 810.011(2) | 16896-16897 | subsection | encoded |  | `s 810.011(2) the provincial court judge may cause the parties to appear` |
| heading: Adjudication @16898 | 16898-16898 | heading | inert (reason 1) |  |  |
| s 810.011(3) | 16899-16899 | subsection | fork | F-810.011-3 | `s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties`; `s 810.011(3) the period of the recognizance is not more than 12 months` |
| s 810.011(4) | 16900-16901 | subsection | fork | F-810.011-4 | `s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period`; `s 810.011(4) the longer period of the recognizance is not more than five years` |
| s 810.011(5) | 16902-16903 | subsection | fork | F-810.011-5 | `s 810.011(5) the provincial court judge may commit the defendant to prison`; `s 810.011(5) the term of imprisonment is not more than 12 months` |
| s 810.011(6) | 16904-16905 | subsection | encoded |  | `s 810.011(6) the provincial court judge may add the condition to the recognizance` |
| s 810.011(6)(a) | 16906-16906 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(6)(b) | 16907-16907 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(6)(c) | 16908-16908 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(6)(d) | 16909-16909 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(6)(e) | 16910-16910 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(6)(f) | 16911-16911 | paragraph | encoded |  | `s 810.011(6) condition` |
| s 810.011(7) | 16912-16913 | subsection | encoded |  | `s 810.011(7) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.011(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies` |
| s 810.011(8) | 16914-16915 | subsection | encoded |  | `s 810.011(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` |
| s 810.011(9) | 16916-16917 | subsection | encoded |  | `s 810.011(9) the provincial court judge is required to consider whether a passport condition is desirable`; `s 810.011(9) the provincial court judge is required to add the passport condition and specify the period during which it applies` |
| s 810.011(10) | 16918-16919 | subsection | encoded |  | `s 810.011(10) the provincial court judge is required to consider whether a geographic-area condition is desirable`; `s 810.011(10) the provincial court judge is required to add the geographic-area condition and specify the period during which it applies` |
| s 810.011(11) | 16920-16921 | subsection | encoded |  | `s 810.011(11) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition` |
| s 810.011(12) | 16922-16923 | subsection | fork | F-810.011-12 | `s 810.011(12) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.011(13) | 16924-16925 | subsection | encoded |  | `s 810.011(13) subsections 810(4) and (5) apply to the recognizance` |
| s 810.011(14) | 16926-16927 | subsection | encoded |  | `s 810.011(14) person`; `s 810.011(14) Attorney General` |
| s 810.011(15) | 16928-16929 | subsection | fork | F-810.011-15 | `s 810.011 report action`; `s 810.011(15) the Attorney General of Canada is to prepare and lay the annual report` |
| s 810.02(1) | 16930-16931 | subsection | fork | F-810.02-1 | `s 810.02(1) the person may lay an information before a provincial court judge` |
| s 810.02(2) | 16932-16933 | subsection | encoded |  | `s 810.02(2) the judge may cause the parties to appear before a provincial court judge` |
| heading: Adjudication @16934 | 16934-16934 | heading | inert (reason 1) |  |  |
| s 810.02(3) | 16935-16935 | subsection | fork | F-810.02-3 | `s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance`; `s 810.02(3) the period of the recognizance is not more than 12 months` |
| s 810.02(4) | 16936-16937 | subsection | fork | F-810.02-4 | `s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period`; `s 810.02(4) the longer period of the recognizance is not more than two years` |
| s 810.02(5) | 16938-16939 | subsection | fork | F-810.02-5 | `s 810.02(5) the provincial court judge may commit the defendant to prison`; `s 810.02(5) the term of imprisonment does not exceed 12 months` |
| s 810.02(6) | 16940-16941 | subsection | encoded |  | `s 810.02(6) the provincial court judge may add the condition to the recognizance` |
| s 810.02(6)(a) | 16942-16942 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(b) | 16943-16943 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(c) | 16944-16944 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(d) | 16945-16945 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(e) | 16946-16946 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(f) | 16947-16947 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(6)(g) | 16948-16948 | paragraph | encoded |  | `s 810.02(6) condition` |
| s 810.02(7) | 16949-16950 | subsection | encoded |  | `s 810.02(7) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.02(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.02(7) the judge is to consider the firearms condition`; `s 810.02(7) the judge is to add the firearms condition if it is desirable` |
| s 810.02(8) | 16951-16952 | subsection | encoded |  | `s 810.02(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.02(8) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.02(9) | 16953-16954 | subsection | fork | F-810.02-9 | `s 810.02(9) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.03(1) | 16955-16956 | subsection | fork | F-810.03-1 | `s 810.03(1) the person may lay an information before a justice` |
| s 810.03(2) | 16957-16958 | subsection | encoded |  | `s 810.03(2) the justice may cause the parties to appear before a justice` |
| s 810.03(3) | 16959-16960 | subsection | fork | F-810.03-3 | `s 810.03(3) the justice may order the defendant to enter into a recognizance`; `s 810.03(3) the period of the recognizance is not more than 12 months` |
| s 810.03(4) | 16961-16962 | subsection | fork | F-810.03-4, F-810.03-4b | `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period`; `s 810.03(4) the longer period of the recognizance is not more than two years` |
| s 810.03(4.1) | 16963-16964 | subsection | encoded |  | `s 810.03(4.1) the justice is required to consider whether it would be more appropriate to recommend Indigenous support services`; `s 810.03(4.1) the justice is to consider recommending Indigenous support services` |
| s 810.03(5) | 16965-16966 | subsection | fork | F-810.03-5 | `s 810.03(5) the justice may commit the defendant to prison`; `s 810.03(5) the term of imprisonment does not exceed 12 months` |
| s 810.03(6) | 16967-16968 | subsection | encoded |  | `s 810.03(6) the justice may add the condition to the recognizance` |
| s 810.03(6)(a) | 16969-16969 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(b) | 16970-16970 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(c) | 16971-16971 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(d) | 16972-16972 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(e) | 16973-16973 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(f) | 16974-16974 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(g) | 16975-16975 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(6)(h) | 16976-16976 | paragraph | encoded |  | `s 810.03(6) condition` |
| s 810.03(7) | 16977-16978 | subsection | encoded |  | `s 810.03(7) the justice is required to consider whether a firearms prohibition is desirable`; `s 810.03(7) the justice is required to add the firearms condition and specify the period during which it applies`; `s 810.03(7) the justice is to consider the firearms condition`; `s 810.03(7) the justice is to add the firearms condition if it is desirable` |
| s 810.03(8) | 16979-16980 | subsection | encoded |  | `s 810.03(8) the justice is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.03(8) the justice is to specify how the things and authorizations are to be surrendered` |
| s 810.03(9) | 16981-16982 | subsection | encoded |  | `s 810.03(9) the justice is required to include in the record a statement of the reasons for not adding the condition`; `s 810.03(9) the justice is to include a statement of reasons in the record` |
| s 810.03(10) | 16983-16984 | subsection | fork | F-810.03-10 | `s 810.03(10) the justice may vary the conditions fixed in the recognizance` |
| s 810.03(11) | 16985-16986 | subsection | encoded |  | `s 810.03(11) the justice is required, before varying any conditions, to consider the safety and security needs of the person on whose behalf the information is laid`; `s 810.03(11) the justice is to consider the safety and security needs` |
| s 810.03(12) | 16987-16988 | subsection | encoded |  | `s 810.03(12) the warrant of committal may be in Form 23` |
| s 810.03(13) | 16989-16990 | subsection | encoded |  | `s 810.03(13) the provisions of this Part apply to the proceedings` |
| s 810.1(1) | 16991-16992 | subsection | fork | F-810.1-1 | `s 810.1(1) the feared offence is one of those listed`; `s 810.1(1) the person may lay an information before a provincial court judge` |
| s 810.1(2) | 16993-16994 | subsection | encoded |  | `s 810.1(2) the provincial court judge may cause the parties to appear` |
| heading: Adjudication @16995 | 16995-16995 | heading | inert (reason 1) |  |  |
| s 810.1(3) | 16996-16996 | subsection | fork | F-810.1-3 | `s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance`; `s 810.1(3) the period of the recognizance does not exceed 12 months` |
| s 810.1(3.01) | 16997-16998 | subsection | fork | F-810.1-3.01 | `s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period`; `s 810.1(3.01) the longer period of the recognizance is not more than two years` |
| s 810.1(3.02) | 16999-17000 | subsection | encoded |  | `s 810.1(3.02) the provincial court judge may add the condition to the recognizance` |
| s 810.1(3.02)(a) | 17001-17001 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(a.1) | 17002-17002 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(b) | 17003-17003 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(b.1) | 17004-17004 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(c) | 17005-17005 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(d) | 17006-17006 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(e) | 17007-17007 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(f) | 17008-17008 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(g) | 17009-17009 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(h) | 17010-17010 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.02)(i) | 17011-17011 | paragraph | encoded |  | `s 810.1(3.02) condition` |
| s 810.1(3.03) | 17012-17013 | subsection | encoded |  | `s 810.1(3.03) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.1(3.03) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.1(3.03) the judge is to consider the firearms condition`; `s 810.1(3.03) the judge is to add the firearms condition if it is desirable` |
| s 810.1(3.04) | 17014-17015 | subsection | encoded |  | `s 810.1(3.04) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.1(3.04) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.1(3.05) | 17016-17017 | subsection | encoded |  | `s 810.1(3.05) the provincial court judge is required to consider whether a reporting condition is desirable`; `s 810.1(3.05) the provincial court judge is required to add the reporting condition`; `s 810.1(3.05) the judge is to consider the reporting condition`; `s 810.1(3.05) the judge is to add the reporting condition if it is desirable` |
| s 810.1(3.1) | 17018-17019 | subsection | fork | F-810.1-3.1 | `s 810.1(3.1) the provincial court judge may commit the defendant to prison`; `s 810.1(3.1) the term of imprisonment does not exceed twelve months` |
| s 810.1(4) | 17020-17021 | subsection | fork | F-810.1-4 | `s 810.1(4) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.1(5) | 17022-17023 | subsection | encoded |  | `s 810.1(5) subsections 810(4) and (5) apply to the recognizance` |
| s 810.2(1) | 17024-17025 | subsection | fork | F-810.2-1 | `s 810.2(1) the person may lay an information before a provincial court judge` |
| s 810.2(2) | 17026-17027 | subsection | encoded |  | `s 810.2(2) the provincial court judge may cause the parties to appear` |
| heading: Adjudication @17028 | 17028-17028 | heading | inert (reason 1) |  |  |
| s 810.2(3) | 17029-17029 | subsection | fork | F-810.2-3 | `s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance`; `s 810.2(3) the period of the recognizance does not exceed 12 months` |
| s 810.2(3.1) | 17030-17031 | subsection | fork | F-810.2-3.1 | `s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period`; `s 810.2(3.1) the longer period of the recognizance does not exceed two years` |
| s 810.2(4) | 17032-17033 | subsection | fork | F-810.2-4 | `s 810.2(4) the provincial court judge may commit the defendant to prison`; `s 810.2(4) the term of imprisonment does not exceed twelve months` |
| s 810.2(4.1) | 17034-17035 | subsection | encoded |  | `s 810.2(4.1) the provincial court judge may add the condition to the recognizance` |
| s 810.2(4.1)(a) | 17036-17036 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(b) | 17037-17037 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(c) | 17038-17038 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(d) | 17039-17039 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(e) | 17040-17040 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(f) | 17041-17041 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(4.1)(g) | 17042-17042 | paragraph | encoded |  | `s 810.2(4.1) condition` |
| s 810.2(5) | 17043-17044 | subsection | encoded |  | `s 810.2(5) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.2(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.2(5) the judge is to consider the firearms condition`; `s 810.2(5) the judge is to add the firearms condition if it is desirable` |
| s 810.2(5.1) | 17045-17046 | subsection | encoded |  | `s 810.2(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.2(5.1) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.2(5.2) | 17047-17048 | subsection | encoded |  | `s 810.2(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition`; `s 810.2(5.2) the judge is to include a statement of reasons in the record` |
| s 810.2(6) | 17049-17050 | subsection | encoded |  | `s 810.2(6) the provincial court judge is required to consider whether a reporting condition is desirable`; `s 810.2(6) the provincial court judge is required to add the reporting condition`; `s 810.2(6) the judge is to consider the reporting condition`; `s 810.2(6) the judge is to add the reporting condition if it is desirable` |
| s 810.2(7) | 17051-17052 | subsection | fork | F-810.2-7 | `s 810.2(7) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.2(8) | 17053-17054 | subsection | encoded |  | `s 810.2(8) subsections 810(4) and (5) apply to the recognizance` |
| s 810.21(1) | 17055-17056 | subsection | fork | F-810.21-1 | `s 810.21(1) the section is one of 83.3 and 810 to 810.2`; `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` |
| heading: Application @17057 | 17057-17057 | heading | inert (reason 1) |  |  |
| s 810.21(2) | 17058-17058 | subsection | encoded |  | `s 810.21(2) sections 714.1 to 714.8 and Part XXII.01 apply to the proceedings` |
| s 810.22(1) | 17059-17060 | subsection | fork | F-810.22-1 | `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` |
| s 810.22(2) | 17061-17062 | subsection | fork | F-810.22-2 | `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` |
| s 810.22(2)(a) | 17063-17063 | paragraph | fork | F-810.22-2 | `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` |
| s 810.22(2)(b) | 17064-17064 | paragraph | fork | F-810.22-2 | `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` |
| s 810.22(3) | 17065-17066 | subsection | fork | F-810.22-3 | `s 810.22(3) the powers of the judge in relation to the order may be exercised by another judge of the same court` |
| s 810.3(1) | 17067-17068 | subsection | encoded |  | `s 810.3(1) the authority is required to designate or specify the matter`; `s 810.3(1) the authority is to designate or specify the matter` |
| s 810.3(1)(a) | 17069-17069 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(b) | 17070-17070 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(c) | 17071-17071 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(d) | 17072-17072 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(e) | 17073-17073 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(f) | 17074-17074 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(g) | 17075-17075 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(1)(h) | 17076-17076 | paragraph | encoded |  | `s 810.3 designating authority` |
| s 810.3(2) | 17077-17078 | subsection | encoded |  | `s 810.3(2) the authority may make the designation` |
| s 810.3(2)(a) | 17079-17079 | paragraph | encoded |  | `s 810.3(2) designation` |
| s 810.3(2)(b) | 17080-17080 | paragraph | encoded |  | `s 810.3(2) designation` |
| s 810.3(3) | 17081-17082 | subsection | encoded |  | `s 810.3(3) the taking, analysis, storage, handling or destruction of the sample, or the protection or destruction of the record, is barred` |
| s 810.3(4) | 17083-17084 | subsection | fork | F-810.3(4) | `s 810.3(4) the authority is required to cause the samples to be destroyed within the period prescribed by regulation`; `s 810.3(4) the authority is to cause the samples to be destroyed` |
| s 810.3(5) | 17085-17086 | subsection | inert (reason 2) |  |  |
| s 810.3(5)(a) | 17087-17087 | paragraph | inert (reason 2) |  |  |
| s 810.3(5)(b) | 17088-17088 | paragraph | inert (reason 2) |  |  |
| s 810.3(5)(c) | 17089-17089 | paragraph | inert (reason 2) |  |  |
| s 810.3(5)(d) | 17090-17090 | paragraph | inert (reason 2) |  |  |
| s 810.3(6) | 17091-17092 | subsection | encoded |  | `s 810.3(6) the notice is required to specify the places and times at which and the days on which the defendant must provide samples`; `s 810.3(6) the first sample is barred because it is taken earlier than 24 hours after the defendant is served with the notice`; `s 810.3(6) the subsequent samples are taken at regular intervals of at least seven days` |
| s 810.4(1) | 17093-17094 | subsection | encoded |  | `s 810.4(1) the use of the bodily substance is barred` |
| s 810.4(2) | 17095-17096 | subsection | encoded |  | `s 810.4(2) the use or disclosure of the results of the analysis is barred` |
| s 810.4(3) | 17097-17098 | subsection | fork | F-810.4-3 | `s 810.4(3) use or disclosure`; `s 810.4(3) the results may be disclosed or used` |
| s 810.4(4) | 17099-17100 | subsection | fork | F-810.4-4 | `s 810.4(4) the person is guilty of an offence punishable on summary conviction`; `s 810.4(4) the punishment for the offence` |
| s 810.5(1) | 17101-17102 | subsection | encoded |  | `s 810.5(1) sections 486 to 486.5 and 486.7 apply to the proceedings` |
| s 810.5(2) | 17103-17104 | subsection | fork | F-810.5-2 | `s 810.5(2) the person is guilty of an offence under section 486.6` |
| s 811 | 17105-17106 | section | encoded |  | `s 811 the person is guilty of an offence`; `s 811 the class of the offence` |
| s 811(a) | 17107-17107 | paragraph | encoded |  | `s 811(a) the punishment on indictment` |
| s 811(b) | 17108-17108 | paragraph | fork | F-811-b | `s 811(b) the punishment on summary conviction` |
| s 811.1(1) | 17109-17110 | subsection | encoded |  | `s 811.1(1) the certificate is admissible in evidence`; `s 811.1(1) the certificate is proof of the statements contained in it without proof of the signature or official character` |
| s 811.1(2) | 17111-17112 | subsection | encoded |  | `s 811.1(2) analyst` |
| s 811.1(3) | 17113-17114 | subsection | encoded |  | `s 811.1(3) the certificate is barred from admission in evidence` |
| s 811.1(4) | 17115-17116 | subsection | fork | F-811.1-4 | `s 811.1(4) the party may require the attendance of the analyst for cross-examination` |
| heading: Appeal @17118 | 17118-17118 | heading | inert (reason 1) |  |  |
| s 812(1) | 17119-17120 | subsection | encoded |  | `s 812(1) the appeal court for sections 813 to 828` |
| s 812(1)(a) | 17121-17121 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(1)(b) | 17122-17122 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(1)(c) | 17123-17123 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(1)(d) | 17124-17124 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(1)(e) | 17125-17125 | repealed | repealed or blank in this text |  |  |
| s 812(1)(f) | 17126-17126 | repealed | repealed or blank in this text |  |  |
| s 812(1)(g) | 17127-17127 | repealed | repealed or blank in this text |  |  |
| s 812(1)(h) | 17128-17128 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(1)(i) | 17129-17129 | paragraph | encoded |  | `s 812(1) province or territory` |
| s 812(2) | 17130-17131 | subsection | encoded |  | `s 812(2) the appeal court once subsection (2) is applied` |
| s 813 | 17132-17133 | section | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(a) | 17134-17134 | paragraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(a)(i) | 17135-17135 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(a)(ii) | 17136-17136 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(a)(iii) | 17137-17137 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(b) | 17138-17138 | paragraph | encoded |  | `s 813 the prosecution side may appeal` |
| s 813(b)(i) | 17139-17139 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(b)(ii) | 17140-17140 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 813(b)(iii) | 17141-17142 | subparagraph | encoded |  | `s 813 appellant`; `s 813 the person may appeal to the appeal court` |
| s 814(1) | 17143-17144 | subsection | fork | F-814 | `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` |
| s 814(2) | 17145-17146 | subsection | fork | F-814 | `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` |
| s 814(3) | 17147-17148 | subsection | fork | F-814 | `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` |
| s 814(4) | 17149-17150 | subsection | encoded |  | `s 814 place of hearing`; `s 814 the place at which the appeal under section 813 is required to be heard` |
| s 815(1) | 17151-17152 | subsection | encoded |  | `s 815(1) the appellant is required to give notice of appeal`; `s 815(1) the notice of appeal is given within the period directed by the rules of court`; `s 815(1) the appellant is to give notice of appeal` |
| s 815(2) | 17153-17154 | subsection | encoded |  | `s 815(2) the appeal court or a judge thereof may extend the time within which notice of appeal may be given` |
| heading: Interim Release of Appellant @17156 | 17156-17156 | heading | inert (reason 1) |  |  |
| s 816(1) | 17157-17158 | subsection | encoded |  | `s 816(1) the appellant is required to remain in custody`; `s 816(1) the release order is required to include the condition that the person surrender themselves into custody in accordance with the order` |
| s 816(1.1) | 17159-17160 | subsection | encoded |  | `s 816(1.1) the person having the custody of the appellant is required to release the appellant immediately`; `s 816(1.1) the custodian is to release the appellant` |
| s 816(2) | 17161-17162 | subsection | encoded |  | `s 816(2) sections 495.1, 512.3 and 524 apply to the proceedings` |
| s 817(1) | 17163-17164 | subsection | encoded |  | `s 817(1) the prosecutor is required to appear before a justice`; `s 817(1) the justice is required to order that the prosecutor enter into a recognizance`; `s 817(1) the justice is to order that the prosecutor enter into a recognizance`; `s 817(1) the prosecutor is to appear before a justice` |
| s 817(2) | 17165-17166 | subsection | encoded |  | `s 817(2) the condition of the recognizance is that the prosecutor will appear personally or by counsel at the sittings of the appeal court` |
| s 817(3) | 17167-17168 | subsection | encoded |  | `s 817(3) section 817 does not apply` |
| s 817(4) | 17169-17169 | repealed | repealed or blank in this text |  |  |
| s 818(1) | 17170-17171 | subsection | fork | F-818-1 | `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` |
| s 818(2) | 17172-17173 | subsection | encoded |  | `s 818(2) the appeal court is required to dismiss the application or allow it` |
| s 818(2)(a) | 17174-17174 | paragraph | encoded |  | `s 818(2) the appeal court is required to dismiss the application or allow it` |
| s 818(2)(b) | 17175-17175 | paragraph | fork | F-818-2b | `s 818(2)(b) the appeal court may allow the application, vacate the order made by the justice and make the order that it considers should have been made` |
| s 818(3) | 17176-17177 | subsection | encoded |  | `s 818(3) the order has the same force and effect as if it had been made by the justice` |
| s 819(1) | 17178-17179 | subsection | fork | F-819-1 | `s 819(1) the day on which the thirty days expire`; `s 819(1) the person having the custody of the appellant is required to apply to the appeal court to fix a date for the hearing`; `s 819(1) the custodian is to apply to the appeal court` |
| s 819(2) | 17180-17181 | subsection | encoded |  | `s 819(2) the appeal court is required to fix a date for the hearing and give directions for expediting it`; `s 819(2) the appeal court is to fix a date for the hearing` |
| s 820(1) | 17182-17183 | subsection | encoded |  | `s 820(1) the person waives the right of appeal under section 813 by paying the fine` |
| s 820(2) | 17184-17185 | subsection | encoded |  | `s 820(2) the conviction, order or sentence is deemed not to have been appealed against` |
| heading: Procedure on Appeal @17187 | 17187-17187 | heading | inert (reason 1) |  |  |
| s 821(1) | 17188-17189 | subsection | fork | F-821-1 | `s 821(1) the clerk of the appeal court is required to notify the summary conviction court of the appeal`; `s 821(1) the summary conviction court is required to transmit the conviction, order or order of dismissal and all other material to the appeal court`; `s 821(1) the material is transmitted in time`; `s 821(1) the material is required to be kept by the clerk of the appeal court with the records of the appeal court`; `s 821(1) the summary conviction court is to transmit the material`; `s 821(1) the clerk is to notify the summary conviction court` |
| s 821(2) | 17190-17191 | subsection | encoded |  | `s 821(2) the appeal is barred from being dismissed by the appeal court` |
| s 821(3) | 17192-17193 | subsection | encoded |  | `s 821(3) the appellant is required to cause a transcript to be furnished to the appeal court and the respondent` |
| s 822(1) | 17194-17195 | subsection | encoded |  | `s 822(1) the provision applies to the appeal` |
| s 822(2) | 17196-17197 | subsection | encoded |  | `s 822(2) the new trial is required to be held before a summary conviction court other than the court that tried the defendant in the first instance` |
| s 822(3) | 17198-17199 | subsection | fork | F-822-3 | `s 822(3) the appeal court may make an order for the release or detention of the appellant pending the new trial`; `s 822(3) the order may be enforced as if made by a justice under section 515 and the provisions of Part XVI apply to it` |
| s 822(4) | 17200-17201 | subsection | fork | F-822-4 | `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo`; `s 822(4) sections 793 to 809 apply to the trial de novo` |
| s 822(5) | 17202-17203 | subsection | encoded |  | `s 822(5) the evidence that is read has the same force and effect as if the witness had given it before the appeal court` |
| s 822(5)(a) | 17204-17204 | paragraph | fork | F-822-5 | `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` |
| s 822(5)(b) | 17205-17205 | paragraph | fork | F-822-5 | `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` |
| s 822(5)(c) | 17206-17207 | paragraph | fork | F-822-5 | `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` |
| s 822(6) | 17208-17209 | subsection | fork | F-822-6 | `s 822(6) the appeal court may make the order`; `s 822(6) the appeal court may take into account any time spent in custody by the defendant as a result of the offence` |
| s 822(6)(a) | 17210-17210 | paragraph | encoded |  | `s 822(6) the appeal court is required to consider the fitness of the sentence appealed against` |
| s 822(6)(b) | 17211-17212 | paragraph | encoded |  | `s 822(6)(b) the varied sentence is within the limits prescribed by law` |
| s 822(7) | 17213-17214 | subsection | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(a) | 17215-17215 | paragraph | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(a)(i) | 17216-17216 | subparagraph | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(a)(ii) | 17217-17217 | subparagraph | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(a)(iii) | 17218-17219 | subparagraph | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(a)(iv) | 17220-17220 | subparagraph | fork | F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(b) | 17221-17221 | paragraph | encoded |  | `s 822(7)(b) judgment is barred from being given in favour of the appellant and the court is required to make an order curing the defect` |
| s 823 | 17222-17222 | repealed | repealed or blank in this text |  |  |
| s 824(1) | 17223-17224 | subsection | encoded |  | `s 824(1) the appeal court may adjourn the hearing of an appeal` |
| s 824(2) | 17225-17226 | subsection | encoded |  | `s 824(2) the appeal court is required to consider the interests of justice`; `s 824(2) the appeal court is required to consider the interests of any victim of the offence in question` |
| s 825 | 17227-17228 | section | fork | F-825 | `s 825 the appeal court may order that the appeal be dismissed` |
| s 825(a) | 17229-17229 | paragraph | fork | F-825 | `s 825 the appeal court may order that the appeal be dismissed` |
| s 825(b) | 17230-17231 | paragraph | fork | F-825 | `s 825 the appeal court may order that the appeal be dismissed` |
| s 826 | 17232-17233 | section | fork | F-826 | `s 826 the appeal court may make the order with respect to costs` |
| s 827(1) | 17234-17235 | subsection | encoded |  | `s 827(1) the order is required to direct that the costs be paid to the clerk of the court and to fix the period within which they are to be paid` |
| s 827(2) | 17236-17237 | subsection | encoded |  | `s 827(2) the clerk of the court is required to issue a certificate in Form 42` |
| s 827(3) | 17238-17239 | subsection | fork | F-827-3 | `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26`; `s 827(3) the term of imprisonment does not exceed one month` |
| s 828(1) | 17240-17241 | subsection | encoded |  | `s 828(1) the conviction or order may be enforced in the way` |
| s 828(1)(a) | 17242-17242 | paragraph | encoded |  | `s 828(1) way of enforcing` |
| s 828(1)(b) | 17243-17243 | paragraph | encoded |  | `s 828(1) way of enforcing` |
| s 828(2) | 17244-17245 | subsection | fork | F-828-2 | `s 828(2) the summary conviction court or a justice may issue a warrant of committal as if no appeal had been taken` |
| s 828(3) | 17246-17247 | subsection | encoded |  | `s 828(3) document`; `s 828(3) the clerk of the appeal court is required to send the document to the justice`; `s 828(3) the clerk of the appeal court is to send the conviction or order to the justice` |
| heading: Summary Appeal on Transcript or Agreed Statement of Facts @17249 | 17249-17249 | heading | inert (reason 1) |  |  |
| s 829(1) | 17250-17251 | subsection | encoded |  | `s 829 appeal court`; `s 829 the appeal court for sections 830 to 838` |
| s 829(2) | 17252-17253 | subsection | encoded |  | `s 829 appeal court`; `s 829 the appeal court for sections 830 to 838` |
| s 830(1) | 17254-17255 | subsection | encoded |  | `s 830(1) the person may appeal against the decision on the ground` |
| s 830(1)(a) | 17256-17256 | paragraph | encoded |  | `s 830(1) ground` |
| s 830(1)(b) | 17257-17257 | paragraph | encoded |  | `s 830(1) ground` |
| s 830(1)(c) | 17258-17258 | paragraph | encoded |  | `s 830(1) ground` |
| s 830(2) | 17259-17260 | subsection | encoded |  | `s 830(2) the appeal is required to be based on a transcript of the proceedings appealed from` |
| s 830(3) | 17261-17262 | subsection | encoded |  | `s 830(3) the notice of appeal is served and filed within thirty days after the date of the decision`; `s 830(3) the last day for serving and filing the notice of appeal` |
| s 830(4) | 17263-17264 | subsection | encoded |  | `s 830(4) the Attorney General of Canada has the same rights of appeal as the Attorney General of a province` |
| heading: Application @17265 | 17265-17265 | heading | inert (reason 1) |  |  |
| s 831 | 17266-17266 | section | fork | F-831 | `s 831 the provision applies to the appeal`; `s 831 the appeal court is required to give such directions as it thinks necessary for expediting the hearing of the appeal` |
| s 832(1) | 17267-17268 | subsection | fork | F-832-1 | `s 832(1) course`; `s 832(1) the appeal court may take the course` |
| s 832(2) | 17269-17270 | subsection | encoded |  | `s 832(2) subsection (1) does not apply` |
| s 833 | 17271-17272 | section | encoded |  | `s 833 a writ of certiorari or other writ is required to remove the conviction, judgment, verdict or other final order or determination` |
| s 834(1) | 17273-17274 | subsection | fork | F-834-1 | `s 834(1) the appeal court may take the course` |
| s 834(1)(a) | 17275-17275 | paragraph | encoded |  | `s 834(1) the appeal court is required to hear and determine the grounds of appeal` |
| s 834(1)(b) | 17276-17277 | paragraph | encoded |  | `s 834(1) the appeal court is required to hear and determine the grounds of appeal` |
| s 834(2) | 17278-17279 | subsection | fork | F-834-2 | `s 834(2) the authority and jurisdiction may be exercised by a judge of the court sitting in chambers` |
| s 835(1) | 17280-17281 | subsection | encoded |  | `s 835(1) the summary conviction court or a justice has the same authority to enforce the conviction, order or determination as if no appeal had been taken` |
| s 835(2) | 17282-17283 | subsection | encoded |  | `s 835(2) the order may be enforced by the process of the appeal court` |
| s 836 | 17284-17285 | section | encoded |  | `s 836 the person is taken to have abandoned all rights of appeal under section 813` |
| s 837 | 17286-17287 | section | encoded |  | `s 837 no appeal under section 830 lies from the conviction or order` |
| s 838 | 17288-17289 | section | encoded |  | `s 838 the appeal court or a judge thereof may extend the time period` |
| heading: Appeals to Court of Appeal @17291 | 17291-17291 | heading | inert (reason 1) |  |  |
| s 839(1) | 17292-17293 | subsection | fork | F-839-1 | `s 839(1) an appeal to the court of appeal may be taken against the decision`; `s 839(1) the decision is one named`; `s 839(1) the named decision may be appealed` |
| s 839(1)(a) | 17294-17294 | paragraph | encoded |  | `s 839(1) decision` |
| s 839(1)(b) | 17295-17295 | paragraph | encoded |  | `s 839(1) decision` |
| s 839(1.1) | 17296-17297 | subsection | fork | F-839-1.1 | `s 839(1.1) an appeal to the Court of Appeal of Nunavut may be taken against the decision` |
| s 839(2) | 17298-17299 | subsection | encoded |  | `s 839(2) the provision applies to the appeal` |
| s 839(3) | 17300-17301 | subsection | encoded |  | `s 839(3) the court of appeal may make the order with respect to costs` |
| s 839(4) | 17302-17303 | subsection | encoded |  | `s 839(4) the decision may be enforced in the same manner as if it had been made by the summary conviction court` |
| s 839(5) | 17304-17305 | subsection | encoded |  | `s 839(5) the Attorney General of Canada has the same rights of appeal as the Attorney General of a province` |
| heading: Fees and Allowances @17307 | 17307-17307 | heading | inert (reason 1) |  |  |
| s 840(1) | 17308-17309 | subsection | encoded |  | `s 840(1) the fee or allowance may be taken or allowed in proceedings before summary conviction courts and justices` |
| s 840(2) | 17310-17311 | subsection | fork | F-840-2 | `s 840(2) the lieutenant governor in council may order that all or any of the fees and allowances shall not be taken or allowed in the province`; `s 840(2) the lieutenant governor in council may fix other fees and allowances to be taken or allowed instead` |
| PART XXVIII | 17313-17313 | part-heading | inert (reason 1) |  |  |
| heading: Electronic Documents @17315 | 17315-17315 | heading | inert (reason 1) |  |  |
| s 841 lead-in | 17316-17317 | lead-in | encoded |  | `s 841 the definitions apply` |
| s 841 "data" | 17318-17318 | definition | encoded |  | `s 841 data` |
| s 841 "electronic document" | 17319-17319 | definition | encoded |  | `s 841 electronic document` |
| s 842 | 17320-17321 | section | fork | F-842 | `s 842 a court may create, collect, receive, store, transfer, distribute, publish or otherwise deal with electronic documents` |
| s 843(1) | 17322-17323 | subsection | fork | F-843-1 | `s 843(1) a court may accept the transfer of data by electronic means` |
| s 843(2) | 17324-17325 | subsection | encoded |  | `s 843(2) the filing is complete` |
| s 844 | 17326-17327 | section | encoded |  | `s 844 the requirement that a document be made in writing is satisfied` |
| s 845 | 17328-17329 | section | fork | F-845 | `s 845 the court may accept a signature in an electronic document` |
| s 846 | 17330-17331 | section | fork | F-846 | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` |
| s 846(a) | 17332-17332 | paragraph | fork | F-846 | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` |
| s 846(b) | 17333-17333 | paragraph | fork | F-846 | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` |
| s 846(c) | 17334-17334 | paragraph | fork | F-846 | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` |
| s 847 | 17335-17336 | section | fork | F-847 | `s 847 the person is entitled to obtain a printed copy of the electronic document from the court` |
| s 848 | 17337-17337 | repealed | repealed or blank in this text |  |  |
| heading: Forms @17339 | 17339-17339 | heading | inert (reason 1) |  |  |
| heading: Forms @17340 | 17340-17340 | heading | inert (reason 1) |  |  |
| s 849(1) | 17341-17341 | subsection | encoded |  | `s 849(1) the form is deemed to be good, valid and sufficient` |
| s 849(2) | 17342-17343 | subsection | encoded |  | `s 849(2) the justice is required to attach or affix a seal` |
| s 849(3) | 17344-17345 | subsection | encoded |  | `s 849(3) the pre-printed portion is required to be printed in both official languages` |
| s 849 editorial note | 17346-17346 | note | inert (reason 1) |  |  |
| sch XX.1 heading | 17348-17348 | schedule-heading | inert (reason 1) |  |  |
| sch XX.1 | 17349-17349 | repealed | repealed or blank in this text |  |  |
| sch XXII.1 heading | 17351-17351 | schedule-heading | inert (reason 1) |  |  |
| sch XXII.1 para 1 | 17352-17352 | schedule-para | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(a) | 17353-17353 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(b) | 17354-17354 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(c) | 17355-17355 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(d) | 17356-17356 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(e) | 17357-17357 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(f) | 17358-17358 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(g) | 17359-17359 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(h) | 17360-17360 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(i) | 17361-17361 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(j) | 17362-17362 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(k) | 17363-17363 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(l) | 17364-17364 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(m) | 17365-17365 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(n) | 17366-17366 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(o) | 17367-17367 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(p) | 17368-17368 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(q) | 17369-17369 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(r) | 17370-17370 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(s) | 17371-17371 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(t) | 17372-17372 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(u) | 17373-17373 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(v) | 17374-17374 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(w) | 17375-17375 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(x) | 17376-17376 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(x.1) | 17377-17377 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(y) | 17378-17378 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(z) | 17379-17379 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(z.1) | 17380-17380 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(z.2) | 17381-17381 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(z.3) | 17382-17382 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 1(z.4) | 17383-17383 | schedule-item | encoded |  | `sch XXII.1 para 1 the words of the entry that names the provision` |
| sch XXII.1 para 2 | 17384-17384 | schedule-para | encoded |  | `sch XXII.1 para 2 the offence is one of those listed` |
| sch XXII.1 para 2(a) | 17385-17385 | schedule-item | encoded |  | `sch XXII.1 para 2 the offence is one of those listed` |
| sch XXII.1 para 2(b) | 17386-17386 | schedule-item | encoded |  | `sch XXII.1 para 2 the offence is one of those listed` |
| sch XXII.1 para 3 | 17387-17387 | schedule-para | fork | F-sch-XXII.1-3 | `sch XXII.1 para 3 the conspiracy, attempt, accessory or counselling is one of those listed` |
| sch XXV heading | 17389-17389 | schedule-heading | inert (reason 1) |  |  |
| sch XXV header row | 17390-17390 | schedule-row | inert (reason 1) |  |  |
| sch XXV Ontario row 1 | 17391-17391 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Ontario row 2 | 17392-17392 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Quebec row 1 | 17393-17393 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Nova Scotia row 1 | 17394-17394 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV New Brunswick row 1 | 17395-17395 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV British Columbia row 1 | 17396-17396 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV British Columbia row 2 | 17397-17397 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Prince Edward Island row 1 | 17398-17398 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Manitoba row 1 | 17399-17399 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Saskatchewan row 1 | 17400-17400 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Alberta row 1 | 17401-17401 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Newfoundland and Labrador row 1 | 17402-17402 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Yukon row 1 | 17403-17403 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Northwest Territories row 1 | 17404-17404 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXV Nunavut row 1 | 17405-17405 | schedule-row | encoded |  | `sch XXV row`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory` |
| sch XXVII heading | 17407-17407 | schedule-heading | inert (reason 1) |  |  |
| sch XXVII heading: Fees and Allowances That May Be Charged by Summary Conviction Courts and Justices | 17409-17409 | heading | inert (reason 1) |  |  |
| sch XXVII item 1 | 17410-17410 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 2 | 17411-17411 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 3 | 17412-17412 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 4 | 17413-17413 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 5 | 17414-17414 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 5 | 17415-17415 | schedule-note | encoded |  | `sch XXVII note after item 5 a further subpoena may be issued on behalf of the party in the proceeding`; `sch XXVII note after item 5 the subpoena may contain the number of names` |
| sch XXVII item 6 | 17416-17416 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 7 | 17417-17417 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 8 | 17418-17418 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 9 | 17419-17419 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 10 | 17420-17420 | schedule-item | encoded |  | `sch XXVII item 10 the fee applies` |
| sch XXVII item 11 | 17421-17421 | schedule-item | fork | F-sch-XXVII-11 | `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` |
| sch XXVII item 12 | 17422-17422 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 13 | 17423-17423 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 14 | 17424-17424 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 15 | 17425-17425 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 15 | 17426-17426 | schedule-note | encoded |  | `sch XXVII note after item 15 the item may be charged` |
| sch XXVII item 16 | 17427-17427 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 17 | 17428-17428 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII heading: Fees and Allowances That May Be Allowed to Peace Officers | 17430-17430 | heading | inert (reason 1) |  |  |
| sch XXVII item 18 | 17431-17431 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 19 | 17432-17432 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 20 | 17433-17433 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 20 | 17434-17434 | schedule-note | fork | F-sch-XXVII-20 | `sch XXVII note after item 20 reasonable costs of transportation may be allowed` |
| sch XXVII item 21 | 17435-17435 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 22 | 17436-17436 | schedule-item | encoded |  | `sch XXVII item 22 the fee applies` |
| sch XXVII item 23 | 17437-17437 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 23 | 17438-17438 | schedule-note | encoded |  | `sch XXVII note after item 23 a charge may be made under item 23 in respect of the service` |
| sch XXVII item 24 | 17439-17439 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 24 | 17440-17440 | schedule-note | encoded |  | `sch XXVII note after item 24 the amount charged for the day is within the limit` |
| sch XXVII heading: Fees and Allowances That May Be Allowed to Witnesses | 17442-17442 | heading | inert (reason 1) |  |  |
| sch XXVII item 25 | 17443-17443 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 26 | 17444-17444 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII heading: Fees and Allowances That May Be Allowed to Interpreters | 17446-17446 | heading | inert (reason 1) |  |  |
| sch XXVII item 27 | 17447-17447 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 28 | 17448-17448 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII item 29 | 17449-17449 | schedule-item | encoded |  | `sch XXVII payee group`; `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| s 809(5) "costs" | 16826-16827 | definition | encoded |  | `s 809(5) costs` |
| s 810.01(8) "Attorney General" | 16892-16893 | definition | encoded |  | `s 810.01(8) person`; `s 810.01(8) Attorney General` |
| s 810.011(14) "Attorney General" | 16926-16927 | definition | encoded |  | `s 810.011(14) person`; `s 810.011(14) Attorney General` |
| s 811.1(2) "analyst" | 17111-17112 | definition | encoded |  | `s 811.1(2) analyst` |

## Fork register (ccc29)

One row per ambiguity: the function(s), the reading taken, the other reading, and the text that licenses each.
The rows of the two groups the brief says not to decide (the "where, when, upon" gates and the "entitled" functions) are listed here and nowhere else; the answer the part already gave them is kept.

| id | function(s) | reading taken | other reading | text that licenses the readings (quoted from the text, with the module comment's module:line; for a name-test fork, the gate and its tag) |
| --- | --- | --- | --- | --- |
| F-786-2 | `s 786(2) the day on which the 12 months end` | The 12 months run from the day the subject matter arose to the same day of the month 12 months later (the last day of the month where the month has no such day) (fork F-786-2: the other reading rolls 29 February forward to 1 March). | roll 29 February forward to 1 March (the comment names it) | "No proceedings shall be instituted more than 12 months after the time when the subject matter of the proceedings arose" (xxvii-a-interpretation-penalty:234) |
| F-787-1 | `s 787(1) the term of imprisonment is not more than two years less a day` | A term of imprisonment is asked in whole months: "two years less a day" is 23 months and the last month's days but one, so a term of 23 whole months is inside it and a term of 24 whole months is not (fork F-787-1: a term in days is not converted). | convert a term stated in days into months (this part asks whole months only) | "a term of imprisonment of not more than two years less a day" (xxvii-a-interpretation-penalty:269) |
| F-787-2 | `s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is authorized by law, but the law does not provide" (fork F-787-2) |
| F-790-2 | `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-790-2); answers JUST FALSE when "Where" or "thereafter" fails |
| F-799 | `s 799 the summary conviction court may take the course` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-799); answers JUST FALSE when "Where ... does not appear" fails |
| F-800-2 | `s 800(2) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await the defendant's appearance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if it thinks fit" (fork F-800-2) |
| F-800-3 | `s 800(3) the summary conviction court may proceed ex parte to hold the trial` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-800-3); answers JUST FALSE when "Where ... if it does not appear ... on proof of service" fails |
| F-802-1 | `s 802(1) the prosecutor is entitled personally to conduct the case`; `s 802(1) the defendant is entitled to make full answer and defence` | the answer the part already gives (an entitlement is a claim, not a power); LISTED, not decided | the other answer (JUST FALSE for NOTHING, or the reverse) | listed, "entitled" (F-802-1); no JUST FALSE branch, answers NOTHING outside the scope |
| F-803-1 | `s 803(1) the summary conviction court may adjourn the trial to a time and place to be appointed and stated in the presence of the parties or their counsel or agents` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-803-1); answers JUST FALSE outside "before or during the trial" |
| F-803-2 | `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant`; `s 803(2)(b) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await their appearance under the warrant` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If a defendant ... does not appear" (fork F-803-2) |
| F-803-4 | `s 803(4) the summary conviction court may dismiss the information with or without costs` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-803-4); answers JUST FALSE when "Where the prosecutor does not appear" fails |
| F-808-1 | `s 808(1) the summary conviction court may draw up an order of dismissal` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) (two gates: counted as flipped AND listed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | listed, where/when/upon kind AND flipped (F-808-1): the "Where the summary conviction court dismisses an information" gate answers JUST FALSE; the "if requested by the defendant" gate answers NOTHING |
| F-809-1 | `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant`; `s 809(1)(b) the summary conviction court may award costs to be paid to the defendant by the informant` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-809-1); answers JUST FALSE when "where the summary conviction court convicts" fails; NOTHING when the costs are not ones it considers reasonable (limit in its own wording) |
| F-810-1 | `s 810(1) an information may be laid before a justice` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate "any person who fears on reasonable grounds" (fork F-810-1) |
| F-810-3 | `s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810-3) |
| F-810-3.01 | `s 810(3.01) the justice or court may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810-3.01) |
| F-810-4.1 | `s 810(4.1) the justice or court may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810-4.1); answers JUST FALSE when there is no application of the informant or the defendant |
| F-810.01-1 | `s 810.01(1) the person may lay an information before a provincial court judge` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate and "with the Attorney General's consent" (fork F-810.01-1) |
| F-810.01-3 | `s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.01-3) |
| F-810.01-3.1 | `s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.01-3.1) |
| F-810.01-4 | `s 810.01(4) the provincial court judge may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.01-4) |
| F-810.01-6 | `s 810.01(6) the provincial court judge may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.01-6); answers JUST FALSE when no one of the three applies |
| F-810.011-1 | `s 810.011(1) the person may lay an information before a provincial court judge` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate and "with the Attorney General's consent" (fork F-810.011-1) |
| F-810.011-12 | `s 810.011(12) the provincial court judge may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.011-12); answers JUST FALSE when no one of the three applies |
| F-810.011-15 | `s 810.011 report action` | @fork F-810.011-15: "Each year" says how often, not by when; no deadline, consequence or sitting-day rule is stated, so none is encoded. | add a deadline, a consequence or a sitting-day rule (the text states none, so the encoder would be inventing one) | "Each year, the Attorney General of Canada shall prepare and cause to be laid before each House of Parliament a report" (xxviii-0-peace-810:781) |
| F-810.011-3 | `s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.011-3) |
| F-810.011-4 | `s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.011-4) |
| F-810.011-5 | `s 810.011(5) the provincial court judge may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.011-5) |
| F-810.02-1 | `s 810.02(1) the person may lay an information before a provincial court judge` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate "A person who fears on reasonable grounds" (fork F-810.02-1) |
| F-810.02-3 | `s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.02-3) |
| F-810.02-4 | `s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.02-4) |
| F-810.02-5 | `s 810.02(5) the provincial court judge may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.02-5) |
| F-810.02-9 | `s 810.02(9) the provincial court judge may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.02-9); answers JUST FALSE when neither the informant nor the defendant applies |
| F-810.03-1 | `s 810.03(1) the person may lay an information before a justice` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate "Any person who fears on reasonable grounds" (fork F-810.03-1) |
| F-810.03-10 | `s 810.03(10) the justice may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.03-10); answers JUST FALSE when no one of the four applies |
| F-810.03-3 | `s 810.03(3) the justice may order the defendant to enter into a recognizance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.03-3) |
| F-810.03-4 | `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the justice is also satisfied" (fork F-810.03-4) |
| F-810.03-4b | `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period` | Seam (PLAN section 6, [T]): section 3.01(2)(f) lists subsection 810.03(4), so "an offence in the commission of which violence was used, threatened or attempted" includes the offences section 3.01(1) lists; that answer is an input (fork F-810.03-4b). | the victim limb of s 810.03(4) must also be shown for an offence counted only through section 3.01(1) (this part lets the s 3.01 answer stand on its own) | "includes a reference to any of the following offences" (xxviii-1-peace-810-02:255) |
| F-810.03-5 | `s 810.03(5) the justice may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.03-5) |
| F-810.1-1 | `s 810.1(1) the person may lay an information before a provincial court judge` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate "Any person who fears on reasonable grounds" (fork F-810.1-1) |
| F-810.1-1b | `s 810.1(1) the feared offence is one of those listed`; `s 810.1(1) the person may lay an information before a provincial court judge` | "whether or not the person or persons in respect of whom it is feared that the offence will be committed are named": naming them is not a condition, so the function above takes no input for it (fork F-810.1-1b). | naming the person or persons is a condition of the information | "whether or not the person or persons in respect of whom it is" (xxviii-2-peace-810-1:58) |
| F-810.1-3 | `s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.1-3) |
| F-810.1-3.01 | `s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.1-3.01) |
| F-810.1-3.1 | `s 810.1(3.1) the provincial court judge may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.1-3.1) |
| F-810.1-4 | `s 810.1(4) the provincial court judge may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.1-4); answers JUST FALSE when neither the informant nor the defendant applies |
| F-810.2-1 | `s 810.2(1) the person may lay an information before a provincial court judge` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; relative-clause gate and "with the consent of the Attorney General" (fork F-810.2-1) |
| F-810.2-3 | `s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.2-3) |
| F-810.2-3.1 | `s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.2-3.1) |
| F-810.2-4 | `s 810.2(4) the provincial court judge may commit the defendant to prison` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.2-4) |
| F-810.2-7 | `s 810.2(7) the provincial court judge may vary the conditions fixed in the recognizance` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-810.2-7); answers JUST FALSE when no one of the three applies |
| F-810.21-1 | `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` | "810 to 810.2" is read in the Code's own order, which includes sections 810.01, 810.011, 810.02, 810.03 and 810.1 (fork F-810.21-1). Name test: NOTHING when the gate fails (the failed gate leaves the power unaffirmed). | "810 to 810.2" means only sections 810, 810.1 and 810.2 (the sections numbered in the range as whole numbers or one decimal) | "any of sections 83.3 and 810 to 810.2" (xxviii-3-peace-810-21:11) |
| F-810.22-1 | `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) (two gates: counted as flipped AND listed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING AND listed, where/when/upon kind (F-810.22-1): "If a person who is bound ... becomes a resident ..." answers NOTHING; "on application of a peace officer or the Attorney General" answers JUST FALSE |
| F-810.22-2 | `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` | Fork F-810.22-2: read as alternatives, one consent suffices; read as cases, each consent is required where its own "if" holds. The part takes the second reading (cumulative), and answers NOTHING where neither "if" holds. | the two consents are alternatives: one suffices (the comment names it) | "The transfer may be granted only with" (xxviii-3-peace-810-21:72) |
| F-810.22-3 | `s 810.22(3) the powers of the judge in relation to the order may be exercised by another judge of the same court` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "If the judge ... is for any reason unable to act" (fork F-810.22-3) |
| F-810.3(4) | `s 810.3(4) the authority is required to cause the samples to be destroyed within the period prescribed by regulation` | Fork F-810.3(4): the period is "prescribed by regulation" (outside these sources) and the text does not say when it starts, so no deadline is encoded; the duty is. | encode a deadline of some length (the text states none and defers to regulation) | "within the period prescribed by regulation" (xxviii-3-peace-810-21:194) |
| F-810.4-3 | `s 810.4(3) the results may be disclosed or used` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the results are made anonymous" for the research limb (fork F-810.4-3) |
| F-810.4-4 | `s 810.4(4) the punishment for the offence` | The text names no penalty for this offence: it is "punishable on summary conviction", so the general penalty of section 787(1) applies unless the law otherwise provides (fork F-810.4-4). | no penalty is stated, so the penalty is NOTHING and the general penalty of s 787(1) is not borrowed | "is guilty of an offence punishable on summary conviction" (xxviii-3-peace-810-21:308) |
| F-810.5-2 | `s 810.5(2) the person is guilty of an offence under section 486.6` | Fork F-810.5-2: "486.4(1) to (3)" is taken as the three subsections named; a range in the Code's order would also take in any subsection numbered between (2) and (3), and the text of this part does not show section 486.4. | "486.4(1) to (3)" is a range in the Code's order (the comment names it) | "any of subsections 486.4(1) to (3)" (xxviii-3-peace-810-21:330) |
| F-811-b | `s 811(b) the punishment on summary conviction` | The text names no penalty for limb (b): the general penalty of section 787(1) applies unless the law otherwise provides (fork F-811-b). | no penalty is stated for limb (b), so the penalty is NOTHING and the general penalty of s 787(1) is not borrowed | "an offence punishable on summary conviction" (xxviii-3-peace-810-21:377) |
| F-811.1-4 | `s 811.1(4) the party may require the attendance of the analyst for cross-examination` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "If a certificate of an analyst is produced against a party" and "with leave of the court" (fork F-811.1-4) |
| F-814 | `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-814): "on the application of one of the parties" answers JUST FALSE; NOTHING for the places that subsections (1) to (3) do not name |
| F-818-1 | `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-818-1): "Where a justice makes an order under section 817" and "before or at any time during the hearing" answer JUST FALSE |
| F-818-2b | `s 818(2)(b) the appeal court may allow the application, vacate the order made by the justice and make the order that it considers should have been made` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the person applying for the review shows cause" (fork F-818-2b) |
| F-819-1 | `s 819(1) the day on which the thirty days expire` | Fork F-819-1: "within thirty days from the day on which notice was given" is counted from the day after that day: the thirty days expire on the notice day PLUS 30. The other reading counts the notice day as day 1. | count the notice day as day 1, so the thirty days expire on the notice day PLUS 29 (the comment names it) | "within thirty days from the day on which notice of his appeal was given" (xxviii-4-appeal-812:438) |
| F-821-1 | `s 821(1) the material is transmitted in time` | Fork F-821-1: "before the time when the appeal is to be heard" is read at the level of the day: the material is in time if it is transmitted on a day before the hearing day, or by the further day the appeal court directs. | read to the time of day, so that material transmitted on the hearing day but before the hearing is in time | "before the time when the appeal is to be heard" (xxviii-4-appeal-812:532) |
| F-822-3 | `s 822(3) the appeal court may make an order for the release or detention of the appellant pending the new trial` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-822-3): "Where an appeal court orders a new trial" answers JUST FALSE |
| F-822-4 | `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) (two gates: counted as flipped AND listed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING AND listed, where/when/upon kind (F-822-4): "if an appeal is taken under section 813 and ... is of the opinion" answers NOTHING; "on application of the defendant, the informant, the Attorney General or the Attorney General's agent" answers JUST FALSE |
| F-822-5 | `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "if that evidence has been authenticated" and "if (a), (b) or (c)" (fork F-822-5) |
| F-822-6 | `s 822(6) the appeal court may make the order` | Fork F-822-6: "unless the sentence is one fixed by law" is read as limiting the duty to consider, not the power to order; the other reading limits both. Name test: JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided. | "unless the sentence is one fixed by law" limits both the duty to consider and the power to order (the comment names it) | "unless the sentence is one fixed by law" (xxviii-4-appeal-812:719) |
| F-822-7 | `s 822(7)(a) judgment is barred from being given in favour of the appellant` | Fork F-822-7: "unless it is shown (iii) ... and (iv) ..." is read literally: both (iii) and (iv) are shown for either ground. The other reading asks (iv) only where the ground is a variance. | ask (iv) only where the ground is a variance (the comment names it) | "unless it is shown" (xxviii-4-appeal-812:759) |
| F-825 | `s 825 the appeal court may order that the appeal be dismissed` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-825): "on proof that notice of an appeal has been given and that (a) or (b)" answers JUST FALSE |
| F-826 | `s 826 the appeal court may make the order with respect to costs` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-826): "Where an appeal is heard and determined or is abandoned or is dismissed for want of prosecution" answers JUST FALSE; NOTHING where the order is not one it considers just and reasonable |
| F-827-3 | `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26`; `s 827(3) the term of imprisonment does not exceed one month` | Fork F-827-3: "one month" is asked in whole months, as in section 787(1); a term in days is not converted. Name test: JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided. | convert a term stated in days into months (this part asks whole months only) | "a term not exceeding one month" (xxviii-4-appeal-812:890) |
| F-828-2 | `s 828(2) the summary conviction court or a justice may issue a warrant of committal as if no appeal had been taken` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-828-2): "Where an appeal taken against a conviction or order adjudging payment of a sum of money is dismissed" answers JUST FALSE |
| F-831 | `s 831 the appeal court is required to give such directions as it thinks necessary for expediting the hearing of the appeal` | Fork F-831: "except that" is read as replacing the duty of section 819(2) to fix a date by a duty to give directions only; the other reading adds the directions to the date-fixing duty. | the directions are added to the date-fixing duty of s 819(2) (the comment names it) | "except that on receiving an application by the person having the custody of an appellant" (xxviii-5-appeal-829:133) |
| F-832-1 | `s 832(1) the appeal court may take the course` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "If a notice of appeal is filed under section 830" and "if the defendant is the appellant" (fork F-832-1) |
| F-834-1 | `s 834(1) the appeal court may take the course` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-834-1): "When a notice of appeal is filed pursuant to section 830" answers JUST FALSE |
| F-834-2 | `s 834(2) the authority and jurisdiction may be exercised by a judge of the court sitting in chambers` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-834-2): "Where the authority and jurisdiction of the appeal court may be exercised by a judge of that court" answers JUST FALSE |
| F-839-1 | `s 839(1) an appeal to the court of appeal may be taken against the decision` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "on any ground that involves a question of law alone" and "with leave of that court or a judge thereof" (fork F-839-1); the "except where that court is the court of appeal" limb is closed by the text and sits in the helper s 839(1) the named decision may be appealed |
| F-839-1.1 | `s 839(1.1) an appeal to the Court of Appeal of Nunavut may be taken against the decision` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "with leave of that court or a judge of that court" and "on any ground that involves a question of law alone" (fork F-839-1.1) |
| F-840-2 | `s 840(2) the lieutenant governor in council may fix other fees and allowances to be taken or allowed instead` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where/when/upon kind (F-840-2): "when the lieutenant governor in council so orders" answers JUST FALSE |
| F-842 | `s 842 a court may create, collect, receive, store, transfer, distribute, publish or otherwise deal with electronic documents` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if it does so in accordance with an Act or with the rules of court" (fork F-842) |
| F-843-1 | `s 843(1) a court may accept the transfer of data by electronic means` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gate "if the transfer is made in accordance with the laws of the place where the transfer originates or the laws of the place where the data is received" (fork F-843-1) |
| F-845 | `s 845 the court may accept a signature in an electronic document` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "If this Act requires a document to be signed" and "if the signature is made in accordance with an Act or the rules of court" (fork F-845) |
| F-846 | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` | NOTHING when the gate fails (the failed gate leaves the power unaffirmed) | JUST FALSE (a failed "if" read as the text's own no: reading (a) of the brief) | flipped to NOTHING; gates "If under this Act an information ... is to be made" and "if (a), (b) and (c)" (fork F-846) |
| F-847 | `s 847 the person is entitled to obtain a printed copy of the electronic document from the court` | the answer the part already gives (an entitlement is a claim, not a power); LISTED, not decided | the other answer (JUST FALSE for NOTHING, or the reverse) | listed, "entitled" (F-847): "in the case of a document in electronic form" answers NOTHING; "on payment of a reasonable fee" answers JUST FALSE |
| F-sch-XXII.1 | `sch XXII.1 para 1 the offence is one of those listed` | The schedule's own title does not say "only", so an offence it does not name answers NOTHING (fork F-sch-XXII.1). | the list is closed, so an offence the schedule does not name is JUST FALSE | "Offences in respect of which a remediation agreement may be entered into" (xxviii-7-schedules:26) |
| F-sch-XXII.1-3 | `sch XXII.1 para 3 the conspiracy, attempt, accessory or counselling is one of those listed` | Fork F-sch-XXII.1-3: "an offence referred to in section 1 or 2" is read as paragraph 1 or 2 of this schedule (the schedule has paragraphs, not sections). | "section 1 or 2" means sections 1 and 2 of the Criminal Code (this part reads the schedule's own paragraphs 1 and 2) | "an offence referred to in section 1 or 2" (xxviii-7-schedules:148) |
| F-sch-XXVII-11 | `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` | the answer the part already gives (an entitlement is a claim, not a power); LISTED, not decided | the other answer (JUST FALSE for NOTHING, or the reverse) | listed, "entitled" and a where-kind gate (F-sch-XXVII-11): "Where two or more justices hear and determine a proceeding" answers JUST FALSE |
| F-sch-XXVII-20 | `sch XXVII note after item 20 reasonable costs of transportation may be allowed` | JUST FALSE when the gate fails (ruling (b) of 2026-11-05 on "where" conditions); LISTED, not decided | NOTHING (the guide's line on grants) | listed, where-kind (F-sch-XXVII-20): "Where a public conveyance is not used" answers JUST FALSE |

90 fork ids in all (19 with a comment of their own in a module and 71 name-test forks recorded by their tag only).

### Name-test sweep of 2026-11-12

Every function of this part whose name contains "may", "permitted", "power", "entitled" or "authorized" (118 of the part's 391 named functions) was read against the three tests of `name-test-sweep.md`.
The modules were written to the ruling (it is in the brief), so the sweep changed no answer and restated no assertion.
It did change three comments: `s 813 the person may appeal to the appeal court` and `sch XXVII note after item 15 the item may be charged` went from "listed" to "kept JUST FALSE" (the text closes the gate with "except where" and "only where"), and `s 840(1) the fee or allowance may be taken or allowed in proceedings before summary conviction courts and justices` went from "no JUST FALSE branch" to "kept JUST FALSE" (the text closes the gate with "Subject to subsection (2)").
The counts below are read from the `-- @name-test:` comment on each function; no function of the set lacks one.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 47 | 6 | 31 | 4 |

A function with two gates is counted in two columns: flipped AND listed (`s 808(1) the summary conviction court may draw up an order of dismissal`, `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference`, `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division`, `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo`); listed "may" AND listed "entitled" (`sch XXVII item 11 each justice is entitled to the fee authorized by item 9`).
So the four columns hold 83 distinct functions, the outside group holds 35, and 83 + 35 = 118, the size of the set.

**Flipped to NOTHING (one fork line each, in the fork register above and in the marginal readings below)** (47):

- `s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order` (F-787-2)
- `s 800(2) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await the defendant's appearance` (F-800-2)
- `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant` (F-803-2)
- `s 803(2)(b) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await their appearance under the warrant` (F-803-2)
- `s 808(1) the summary conviction court may draw up an order of dismissal` (F-808-1)
- `s 810(1) an information may be laid before a justice` (F-810-1)
- `s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties` (F-810-3)
- `s 810(3.01) the justice or court may commit the defendant to prison` (F-810-3.01)
- `s 810.01(1) the person may lay an information before a provincial court judge` (F-810.01-1)
- `s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance` (F-810.01-3)
- `s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` (F-810.01-3.1)
- `s 810.01(4) the provincial court judge may commit the defendant to prison` (F-810.01-4)
- `s 810.011(1) the person may lay an information before a provincial court judge` (F-810.011-1)
- `s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties` (F-810.011-3)
- `s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` (F-810.011-4)
- `s 810.011(5) the provincial court judge may commit the defendant to prison` (F-810.011-5)
- `s 810.02(1) the person may lay an information before a provincial court judge` (F-810.02-1)
- `s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance` (F-810.02-3)
- `s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` (F-810.02-4)
- `s 810.02(5) the provincial court judge may commit the defendant to prison` (F-810.02-5)
- `s 810.03(1) the person may lay an information before a justice` (F-810.03-1)
- `s 810.03(3) the justice may order the defendant to enter into a recognizance` (F-810.03-3)
- `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period` (F-810.03-4, F-810.03-4b)
- `s 810.03(5) the justice may commit the defendant to prison` (F-810.03-5)
- `s 810.1(1) the person may lay an information before a provincial court judge` (F-810.1-1)
- `s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance` (F-810.1-3)
- `s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period` (F-810.1-3.01)
- `s 810.1(3.1) the provincial court judge may commit the defendant to prison` (F-810.1-3.1)
- `s 810.2(1) the person may lay an information before a provincial court judge` (F-810.2-1)
- `s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance` (F-810.2-3)
- `s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` (F-810.2-3.1)
- `s 810.2(4) the provincial court judge may commit the defendant to prison` (F-810.2-4)
- `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` (F-810.21-1)
- `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` (F-810.22-1)
- `s 810.22(3) the powers of the judge in relation to the order may be exercised by another judge of the same court` (F-810.22-3)
- `s 810.4(3) the results may be disclosed or used` (F-810.4-3)
- `s 811.1(4) the party may require the attendance of the analyst for cross-examination` (F-811.1-4)
- `s 818(2)(b) the appeal court may allow the application, vacate the order made by the justice and make the order that it considers should have been made` (F-818-2b)
- `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo` (F-822-4)
- `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` (F-822-5)
- `s 832(1) the appeal court may take the course` (F-832-1)
- `s 839(1) an appeal to the court of appeal may be taken against the decision` (F-839-1)
- `s 839(1.1) an appeal to the Court of Appeal of Nunavut may be taken against the decision` (F-839-1.1)
- `s 842 a court may create, collect, receive, store, transfer, distribute, publish or otherwise deal with electronic documents` (F-842)
- `s 843(1) a court may accept the transfer of data by electronic means` (F-843-1)
- `s 845 the court may accept a signature in an electronic document` (F-845)
- `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` (F-846)

**Kept JUST FALSE: the text closes the gate itself** (6):

- `s 813 the person may appeal to the appeal court`
- `s 839(1) the named decision may be appealed`
- `s 840(1) the fee or allowance may be taken or allowed in proceedings before summary conviction courts and justices`
- `sch XXVII note after item 5 a further subpoena may be issued on behalf of the party in the proceeding`
- `sch XXVII note after item 15 the item may be charged`
- `sch XXVII note after item 23 a charge may be made under item 23 in respect of the service`

**Listed: "may" with a where/when/upon-kind gate (assumed, not ruled, that the equivalents "on application", "before or during", "on proof", "when ... so orders" go with this group; the answer is kept)** (31):

- `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` (F-790-2)
- `s 799 the summary conviction court may take the course` (F-799)
- `s 800(3) the summary conviction court may proceed ex parte to hold the trial` (F-800-3)
- `s 803(1) the summary conviction court may adjourn the trial to a time and place to be appointed and stated in the presence of the parties or their counsel or agents` (F-803-1)
- `s 803(4) the summary conviction court may dismiss the information with or without costs` (F-803-4)
- `s 808(1) the summary conviction court may draw up an order of dismissal` (F-808-1)
- `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant` (F-809-1)
- `s 809(1)(b) the summary conviction court may award costs to be paid to the defendant by the informant` (F-809-1)
- `s 810(4.1) the justice or court may vary the conditions fixed in the recognizance` (F-810-4.1)
- `s 810.01(6) the provincial court judge may vary the conditions fixed in the recognizance` (F-810.01-6)
- `s 810.011(12) the provincial court judge may vary the conditions fixed in the recognizance` (F-810.011-12)
- `s 810.02(9) the provincial court judge may vary the conditions fixed in the recognizance` (F-810.02-9)
- `s 810.03(10) the justice may vary the conditions fixed in the recognizance` (F-810.03-10)
- `s 810.1(4) the provincial court judge may vary the conditions fixed in the recognizance` (F-810.1-4)
- `s 810.2(7) the provincial court judge may vary the conditions fixed in the recognizance` (F-810.2-7)
- `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` (F-810.21-1)
- `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` (F-810.22-1)
- `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` (F-814)
- `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` (F-818-1)
- `s 822(3) the appeal court may make an order for the release or detention of the appellant pending the new trial` (F-822-3)
- `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo` (F-822-4)
- `s 822(6) the appeal court may make the order` (F-822-6)
- `s 825 the appeal court may order that the appeal be dismissed` (F-825)
- `s 826 the appeal court may make the order with respect to costs` (F-826)
- `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26` (F-827-3)
- `s 828(2) the summary conviction court or a justice may issue a warrant of committal as if no appeal had been taken` (F-828-2)
- `s 834(1) the appeal court may take the course` (F-834-1)
- `s 834(2) the authority and jurisdiction may be exercised by a judge of the court sitting in chambers` (F-834-2)
- `s 840(2) the lieutenant governor in council may fix other fees and allowances to be taken or allowed instead` (F-840-2)
- `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` (F-sch-XXVII-11)
- `sch XXVII note after item 20 reasonable costs of transportation may be allowed` (F-sch-XXVII-20)

**Listed: "entitled"** (4):

- `s 802(1) the prosecutor is entitled personally to conduct the case` (F-802-1)
- `s 802(1) the defendant is entitled to make full answer and defence` (F-802-1)
- `s 847 the person is entitled to obtain a printed copy of the electronic document from the court` (F-847)
- `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` (F-sch-XXVII-11)

**Outside the four counts** (named for a power or a liberty, but no "if" gate answers JUST FALSE: the answer is NOTHING because the case falls outside the section's own scope, or the function returns a value): 35.

**"It is lawful" functions:** scoped (kept): 0; unscoped and retitled to "s N makes it lawful ...": 0.
No function of this part has "lawful" in its name, so the "it is lawful" rule applies to none.

## Jural relations (ccc29)

Hohfeld's four pairs: a duty has a correlative claim; a power a correlative liability; a privilege (liberty) a correlative no-right; an immunity a correlative disability.
Each row names one relation of one provision: the first column of parties holds the first incident of the pair (the duty, the power, the privilege or the immunity) and the second holds its correlative (the claim, the liability, the no-right or the disability); the rule functions that encode it are listed, and where a provision has a decision function and a regulative rule over the same facts (`is required to ...` and `is to ...`) both are in the one row.
A prohibition on conduct (`no person shall use ...`, `the information shall not contain ...`) is written as a duty to refrain with the claim in the person protected; a bar on the power of a party to act (`may not appear by agent`, `no proceedings shall be instituted ...`, `no appeal lies`) is written as an immunity in the person who is protected and a disability in the person who cannot act.
The relations were assigned by one explicit rule per provision (`work/jural2.py`) from the function names, which restate the text, and the resulting table was read once for sense on 2026-11-17; the parties are this part's reading of who holds each incident, assumed and not ruled, and a lawyer may regroup them.

| provision | relation | first incident held by | correlative held by | rule(s) |
| --- | --- | --- | --- | --- |
| s 786(2) | immunity / disability | the defendant | the informant and the prosecutor | `s 786(2) the proceedings are barred because they were instituted more than 12 months after the subject matter arose` |
| s 787(1) | power / liability | the court | a person convicted of an offence punishable on summary conviction | `s 787(1) the general penalty applies to the offence`; `s 787(1) the fine is not more than $5,000`; `s 787(1) the term of imprisonment is not more than two years less a day` |
| s 787(2) | power / liability | the court | a person ordered to pay a fine or money | `s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order` |
| s 788(1) | duty / claim | the informant | the defendant | `s 788(1) the proceedings are required to be commenced by laying an information in Form 2`; `s 788(1) the informant is to lay an information in Form 2` |
| s 788(2) | power / liability | a justice | the parties | `s 788(2) one justice may do the act` |
| s 789(1)(a) | duty / claim | the informant | the defendant | `s 789(1)(a) the information is required to be in writing and under oath` |
| s 789(1)(b) | power / liability | the informant | the defendant | `s 789(1)(b) the information may charge more than one offence or relate to more than one matter of complaint` |
| s 789(1)(b) | duty / claim | the informant | the defendant | `s 789(1)(b) each offence or matter of complaint is required to be set out in a separate count` |
| s 789(2) | duty / claim | the informant | the defendant | `s 789(2) the information is barred from containing any reference to previous convictions` |
| s 790(1) | privilege / no-right | the justice before whom the information is laid | the defendant | `s 790(1) the justice is not required to be a justice before whom the trial is held` |
| s 790(2) | duty / claim | the justices | the defendant | `s 790(2) the justices are required to be present and act together at the trial` |
| s 790(2) | power / liability | one justice | the parties | `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` |
| s 794(1) | privilege / no-right | the informant | the defendant | `s 794(1) the information need not set out or negative the exception, exemption, proviso, excuse or qualification` |
| s 798 | power / liability | the summary conviction court | the defendant | `s 798 the summary conviction court has jurisdiction to try, determine and adjudge the proceedings` |
| s 799 | power / liability | the summary conviction court | the defendant | `s 799 the summary conviction court may take the course` |
| s 800(1) | duty / claim | the summary conviction court | the prosecutor and the defendant | `s 800(1) the summary conviction court is required to hold the trial`; `s 800(1) the court is to hold the trial` |
| s 800(2) | privilege / no-right | the defendant | the summary conviction court | `s 800(2) a defendant may appear in the way` |
| s 800(2) | power / liability | the summary conviction court | the defendant | `s 800(2) the summary conviction court may require the defendant to appear personally`; `s 800(2) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await the defendant's appearance` |
| s 800(3) | duty / claim | a defendant that is an organization | the summary conviction court | `s 800(3) the organization is required to appear by counsel or agent` |
| s 800(3) | power / liability | the summary conviction court | the defendant | `s 800(3) the summary conviction court may proceed ex parte to hold the trial` |
| s 801(1) | duty / claim | the summary conviction court | the defendant | `s 801(1) the substance of the information is required to be stated to the defendant` |
| s 801(1)(a) | duty / claim | the summary conviction court | the defendant | `s 801(1)(a) the defendant is required to be asked whether they plead guilty or not guilty to the information` |
| s 801(1)(b) | duty / claim | the summary conviction court | the defendant | `s 801(1)(b) the defendant is required to be asked whether they have cause to show why an order should not be made against them` |
| s 801(2) | duty / claim | the summary conviction court | the prosecutor and the defendant | `s 801(2) the summary conviction court is required to convict the defendant, discharge the defendant under section 730 or make an order against the defendant` |
| s 801(3) | duty / claim | the summary conviction court | the prosecutor and the defendant | `s 801(3) the summary conviction court is required to proceed with the trial and take the evidence in accordance with Part XVIII` |
| s 802(1) | duty / claim | the summary conviction court | the prosecutor and the defendant (each as to its own entitlement) | `s 802(1) the prosecutor is entitled personally to conduct the case`; `s 802(1) the defendant is entitled to make full answer and defence` |
| s 802(2) | privilege / no-right | the prosecutor and the defendant | the other party | `s 802(2) the prosecutor or defendant may examine and cross-examine witnesses in the way` |
| s 802(3) | duty / claim | the summary conviction court | the parties | `s 802(3) the witness is required to be examined under oath` |
| s 802.1 | immunity / disability | the summary conviction court | the defendant | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` |
| s 803(1) | power / liability | the summary conviction court | the parties | `s 803(1) the summary conviction court may adjourn the trial to a time and place to be appointed and stated in the presence of the parties or their counsel or agents` |
| s 803(1.1) | duty / claim | the summary conviction court | the parties | `s 803(1.1) the summary conviction court is required to consider the interests of justice`; `s 803(1.1) the summary conviction court is required to consider the interests of any victim of the offence in question` |
| s 803(2)(a) | power / liability | the summary conviction court | the defendant | `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant` |
| s 803(2)(b) | power / liability | the summary conviction court | the defendant | `s 803(2)(b) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await their appearance under the warrant` |
| s 803(3) | immunity / disability | the defendant | the informant (no proceedings under section 145 without the Attorney General's consent) | `s 803(3) the consent of the Attorney General is required before the proceedings under section 145 are instituted or proceeded with` |
| s 803(4) | power / liability | the summary conviction court | the informant | `s 803(4) the summary conviction court may dismiss the information with or without costs` |
| s 804 | duty / claim | the summary conviction court | the parties | `s 804 the summary conviction court is required to convict the defendant, discharge the defendant under section 730, make an order against the defendant or dismiss the information`; `s 804 the court is to decide` |
| s 806(1) | duty / claim | the summary conviction court | the defendant | `s 806(1) a minute or memorandum indicating that the matter was dealt with under this Part is required to be made by the summary conviction court` |
| s 806(2) | duty / claim | the summary conviction court | the defendant | `s 806(2) the summary conviction court is required to issue a warrant of committal in Form 21 or 22`; `s 806(2) the court is to issue a warrant of committal` |
| s 808(1) | power / liability | the summary conviction court | the parties | `s 808(1) the summary conviction court may draw up an order of dismissal` |
| s 808(1) | duty / claim | the summary conviction court | the defendant | `s 808(1) the summary conviction court is required to give the defendant a certified copy of the order of dismissal` |
| s 808(2) | immunity / disability | the defendant | the informant | `s 808(2) the certified copy of the order of dismissal is a bar to the subsequent proceedings` |
| s 809(1)(a) | power / liability | the summary conviction court | the defendant | `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant` |
| s 809(1)(b) | power / liability | the summary conviction court | the informant | `s 809(1)(b) the summary conviction court may award costs to be paid to the defendant by the informant` |
| s 809(2) | duty / claim | the summary conviction court | the parties | `s 809(2) the order for costs is required to be set out in the conviction, order or order of dismissal` |
| s 809(3) | power / liability | the summary conviction court | the person liable to pay the costs or the sum | `s 809(3) the amount for which the defendant is liable to serve the term of imprisonment imposed in default of payment` |
| s 809(4) | power / liability | the summary conviction court | the person liable to pay the costs or the sum | `s 809(4) the person who is liable to pay the costs is, in default of payment, liable to imprisonment for one month`; `s 809(4) the term of imprisonment in default of payment of the costs` |
| s 810(1) | power / liability | the person who fears (the informant) | the defendant | `s 810(1) an information may be laid before a justice` |
| s 810(2) | duty / claim | a justice | the defendant and the informant | `s 810(2) the justice is required to cause the parties to appear`; `s 810(2) the justice is to cause the parties to appear` |
| s 810(3) | power / liability | a justice or the summary conviction court | the defendant and the informant | `s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties` |
| s 810(3.01) | power / liability | a justice or the summary conviction court | the defendant and the informant | `s 810(3.01) the justice or court may commit the defendant to prison` |
| s 810(3.02) | power / liability | a justice or the summary conviction court | the defendant and the informant | `s 810(3.02) the justice or court may add the condition to the recognizance` |
| s 810(3.1) | duty / claim | a justice or the summary conviction court | the defendant and the informant | `s 810(3.1) the justice or court is required to consider whether a firearms prohibition is desirable`; `s 810(3.1) the justice or court is required to add the firearms condition`; `s 810(3.1) the justice or court is to consider the firearms condition`; `s 810(3.1) the justice or court is to add the firearms condition if it is desirable` |
| s 810(3.11) | duty / claim | a justice or the summary conviction court | the defendant and the informant | `s 810(3.11) the justice or court is required to specify in the order the manner and method`; `s 810(3.11) the justice or court is to specify the manner and method` |
| s 810(3.12) | duty / claim | a justice or the summary conviction court | the defendant and the informant | `s 810(3.12) the justice or court is required to include in the record a statement of the reasons for not adding the condition`; `s 810(3.12) the justice or court is to include a statement of reasons in the record` |
| s 810(3.2) | duty / claim | a justice or the summary conviction court | the defendant and the informant | `s 810(3.2) the justice or court is required to consider whether it is desirable to add the condition`; `s 810(3.2) the justice or court is to consider the supplementary conditions` |
| s 810(4.1) | power / liability | a justice or the summary conviction court | the defendant and the informant | `s 810(4.1) the justice or court may vary the conditions fixed in the recognizance` |
| s 810.01(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.01(1) the person may lay an information before a provincial court judge` |
| s 810.01(2) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(2) the provincial court judge may cause the parties to appear` |
| s 810.01(3) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance` |
| s 810.01(3.1) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` |
| s 810.01(4) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(4) the provincial court judge may commit the defendant to prison` |
| s 810.01(4.1) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(4.1) the provincial court judge may add the condition to the recognizance` |
| s 810.01(5) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.01(5) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.01(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.01(5) the judge is to consider the firearms condition`; `s 810.01(5) the judge is to add the firearms condition if it is desirable` |
| s 810.01(5.1) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.01(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.01(5.1) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.01(5.2) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.01(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition`; `s 810.01(5.2) the judge is to include a statement of reasons in the record` |
| s 810.01(6) | power / liability | a provincial court judge | the defendant and the informant | `s 810.01(6) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.011(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.011(1) the person may lay an information before a provincial court judge` |
| s 810.011(2) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(2) the provincial court judge may cause the parties to appear` |
| s 810.011(3) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties` |
| s 810.011(4) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` |
| s 810.011(5) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(5) the provincial court judge may commit the defendant to prison` |
| s 810.011(6) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(6) the provincial court judge may add the condition to the recognizance` |
| s 810.011(7) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.011(7) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.011(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies` |
| s 810.011(8) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.011(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` |
| s 810.011(9) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.011(9) the provincial court judge is required to consider whether a passport condition is desirable`; `s 810.011(9) the provincial court judge is required to add the passport condition and specify the period during which it applies` |
| s 810.011(10) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.011(10) the provincial court judge is required to consider whether a geographic-area condition is desirable`; `s 810.011(10) the provincial court judge is required to add the geographic-area condition and specify the period during which it applies` |
| s 810.011(11) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.011(11) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition` |
| s 810.011(12) | power / liability | a provincial court judge | the defendant and the informant | `s 810.011(12) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.011(15) | duty / claim | the Attorney General of Canada | each House of Parliament | `s 810.011(15) the Attorney General of Canada is to prepare and lay the annual report` |
| s 810.02(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.02(1) the person may lay an information before a provincial court judge` |
| s 810.02(2) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(2) the judge may cause the parties to appear before a provincial court judge` |
| s 810.02(3) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance` |
| s 810.02(4) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` |
| s 810.02(5) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(5) the provincial court judge may commit the defendant to prison` |
| s 810.02(6) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(6) the provincial court judge may add the condition to the recognizance` |
| s 810.02(7) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.02(7) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.02(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.02(7) the judge is to consider the firearms condition`; `s 810.02(7) the judge is to add the firearms condition if it is desirable` |
| s 810.02(8) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.02(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.02(8) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.02(9) | power / liability | a provincial court judge | the defendant and the informant | `s 810.02(9) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.03(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.03(1) the person may lay an information before a justice` |
| s 810.03(2) | power / liability | a justice | the defendant and the informant | `s 810.03(2) the justice may cause the parties to appear before a justice` |
| s 810.03(3) | power / liability | a justice | the defendant and the informant | `s 810.03(3) the justice may order the defendant to enter into a recognizance` |
| s 810.03(4) | power / liability | a justice | the defendant and the informant | `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period` |
| s 810.03(4.1) | duty / claim | a justice | the defendant and the informant | `s 810.03(4.1) the justice is required to consider whether it would be more appropriate to recommend Indigenous support services`; `s 810.03(4.1) the justice is to consider recommending Indigenous support services` |
| s 810.03(5) | power / liability | a justice | the defendant and the informant | `s 810.03(5) the justice may commit the defendant to prison` |
| s 810.03(6) | power / liability | a justice | the defendant and the informant | `s 810.03(6) the justice may add the condition to the recognizance` |
| s 810.03(7) | duty / claim | a justice | the defendant and the informant | `s 810.03(7) the justice is required to consider whether a firearms prohibition is desirable`; `s 810.03(7) the justice is required to add the firearms condition and specify the period during which it applies`; `s 810.03(7) the justice is to consider the firearms condition`; `s 810.03(7) the justice is to add the firearms condition if it is desirable` |
| s 810.03(8) | duty / claim | a justice | the defendant and the informant | `s 810.03(8) the justice is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.03(8) the justice is to specify how the things and authorizations are to be surrendered` |
| s 810.03(9) | duty / claim | a justice | the defendant and the informant | `s 810.03(9) the justice is required to include in the record a statement of the reasons for not adding the condition`; `s 810.03(9) the justice is to include a statement of reasons in the record` |
| s 810.03(10) | power / liability | a justice | the defendant and the informant | `s 810.03(10) the justice may vary the conditions fixed in the recognizance` |
| s 810.03(11) | duty / claim | a justice | the defendant and the informant | `s 810.03(11) the justice is required, before varying any conditions, to consider the safety and security needs of the person on whose behalf the information is laid`; `s 810.03(11) the justice is to consider the safety and security needs` |
| s 810.03(12) | power / liability | a justice | the defendant and the informant | `s 810.03(12) the warrant of committal may be in Form 23` |
| s 810.1(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.1(1) the person may lay an information before a provincial court judge` |
| s 810.1(2) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(2) the provincial court judge may cause the parties to appear` |
| s 810.1(3) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance` |
| s 810.1(3.01) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period` |
| s 810.1(3.02) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(3.02) the provincial court judge may add the condition to the recognizance` |
| s 810.1(3.03) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.1(3.03) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.1(3.03) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.1(3.03) the judge is to consider the firearms condition`; `s 810.1(3.03) the judge is to add the firearms condition if it is desirable` |
| s 810.1(3.04) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.1(3.04) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.1(3.04) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.1(3.05) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.1(3.05) the provincial court judge is required to consider whether a reporting condition is desirable`; `s 810.1(3.05) the provincial court judge is required to add the reporting condition`; `s 810.1(3.05) the judge is to consider the reporting condition`; `s 810.1(3.05) the judge is to add the reporting condition if it is desirable` |
| s 810.1(3.1) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(3.1) the provincial court judge may commit the defendant to prison` |
| s 810.1(4) | power / liability | a provincial court judge | the defendant and the informant | `s 810.1(4) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.2(1) | power / liability | the person who fears (the informant) | the defendant | `s 810.2(1) the person may lay an information before a provincial court judge` |
| s 810.2(2) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(2) the provincial court judge may cause the parties to appear` |
| s 810.2(3) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance` |
| s 810.2(3.1) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` |
| s 810.2(4) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(4) the provincial court judge may commit the defendant to prison` |
| s 810.2(4.1) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(4.1) the provincial court judge may add the condition to the recognizance` |
| s 810.2(5) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.2(5) the provincial court judge is required to consider whether a firearms prohibition is desirable`; `s 810.2(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies`; `s 810.2(5) the judge is to consider the firearms condition`; `s 810.2(5) the judge is to add the firearms condition if it is desirable` |
| s 810.2(5.1) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.2(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered`; `s 810.2(5.1) the judge is to specify how the things and authorizations are to be surrendered` |
| s 810.2(5.2) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.2(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition`; `s 810.2(5.2) the judge is to include a statement of reasons in the record` |
| s 810.2(6) | duty / claim | a provincial court judge | the defendant and the informant | `s 810.2(6) the provincial court judge is required to consider whether a reporting condition is desirable`; `s 810.2(6) the provincial court judge is required to add the reporting condition`; `s 810.2(6) the judge is to consider the reporting condition`; `s 810.2(6) the judge is to add the reporting condition if it is desirable` |
| s 810.2(7) | power / liability | a provincial court judge | the defendant and the informant | `s 810.2(7) the provincial court judge may vary the conditions fixed in the recognizance` |
| s 810.21(1) | power / liability | a provincial court judge | the defendant | `s 810.21(1) the section is one of 83.3 and 810 to 810.2`; `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` |
| s 810.22(1) | power / liability | a provincial court judge | the defendant | `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` |
| s 810.22(2) | immunity / disability | the defendant | a provincial court judge (no transfer without the consents) | `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` |
| s 810.22(3) | power / liability | another judge of the same court | the defendant | `s 810.22(3) the powers of the judge in relation to the order may be exercised by another judge of the same court` |
| s 810.3(1) | duty / claim | the Attorney General of a province or the minister of justice of a territory | the persons who take, analyse or store the samples | `s 810.3(1) the authority is required to designate or specify the matter`; `s 810.3(1) the authority is to designate or specify the matter` |
| s 810.3(2) | power / liability | the Attorney General of a province or the minister of justice of a territory | the persons designated | `s 810.3(2) the authority may make the designation` |
| s 810.3(3) | immunity / disability | the defendant | whoever would take, analyse or destroy a sample outside the designations | `s 810.3(3) the taking, analysis, storage, handling or destruction of the sample, or the protection or destruction of the record, is barred` |
| s 810.3(4) | duty / claim | the Attorney General of a province or the minister of justice of a territory, or a person authorized by them | the defendant | `s 810.3(4) the authority is required to cause the samples to be destroyed within the period prescribed by regulation`; `s 810.3(4) the authority is to cause the samples to be destroyed` |
| s 810.3(6) | immunity / disability | the defendant | the authority (no first sample earlier than 24 hours after service) | `s 810.3(6) the notice is required to specify the places and times at which and the days on which the defendant must provide samples`; `s 810.3(6) the first sample is barred because it is taken earlier than 24 hours after the defendant is served with the notice`; `s 810.3(6) the subsequent samples are taken at regular intervals of at least seven days` |
| s 810.4(1) | duty / claim | any person | the defendant | `s 810.4(1) the use of the bodily substance is barred` |
| s 810.4(2) | duty / claim | any person | the defendant | `s 810.4(2) the use or disclosure of the results of the analysis is barred` |
| s 810.4(3) | privilege / no-right | the person who may use or disclose the results under subsection (3) | the defendant | `s 810.4(3) the results may be disclosed or used` |
| s 810.4(4) | power / liability | the Crown (the prosecutor) | the person who contravenes or fails to comply | `s 810.4(4) the person is guilty of an offence punishable on summary conviction`; `s 810.4(4) the punishment for the offence` |
| s 810.5(2) | power / liability | the Crown (the prosecutor) | the person who contravenes or fails to comply | `s 810.5(2) the person is guilty of an offence under section 486.6` |
| s 811 | power / liability | the Crown (the prosecutor) | the person who contravenes or fails to comply | `s 811 the person is guilty of an offence`; `s 811 the class of the offence` |
| s 811(a) | power / liability | the Crown (the prosecutor) | the person who contravenes or fails to comply | `s 811(a) the punishment on indictment` |
| s 811(b) | power / liability | the Crown (the prosecutor) | the person who contravenes or fails to comply | `s 811(b) the punishment on summary conviction` |
| s 811.1(1) | privilege / no-right | the prosecutor | the defendant | `s 811.1(1) the certificate is admissible in evidence`; `s 811.1(1) the certificate is proof of the statements contained in it without proof of the signature or official character` |
| s 811.1(3) | immunity / disability | the defendant | the prosecutor (certificate of an analyst not admitted without notice) | `s 811.1(3) the certificate is barred from admission in evidence` |
| s 811.1(4) | power / liability | the party against whom the certificate is produced | the prosecutor or the other party | `s 811.1(4) the party may require the attendance of the analyst for cross-examination` |
| s 813 | power / liability | the appellant (the defendant, the informant or the Attorney General) | the respondent | `s 813 the person may appeal to the appeal court`; `s 813 the prosecution side may appeal` |
| s 814 | power / liability | a judge of the appeal court | the appellant and the respondent | `s 814 the place at which the appeal under section 813 is required to be heard`; `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` |
| s 815(1) | duty / claim | the appellant | the respondent | `s 815(1) the appellant is required to give notice of appeal`; `s 815(1) the notice of appeal is given within the period directed by the rules of court`; `s 815(1) the appellant is to give notice of appeal` |
| s 815(2) | power / liability | the appeal court or a judge of it | the appellant | `s 815(2) the appeal court or a judge thereof may extend the time within which notice of appeal may be given` |
| s 816(1) | duty / claim | the appellant | the court that holds the appellant | `s 816(1) the appellant is required to remain in custody` |
| s 816(1) | duty / claim | the appeal court | the Crown | `s 816(1) the release order is required to include the condition that the person surrender themselves into custody in accordance with the order` |
| s 816(1.1) | duty / claim | the person having custody of the appellant | the appellant | `s 816(1.1) the person having the custody of the appellant is required to release the appellant immediately`; `s 816(1.1) the custodian is to release the appellant` |
| s 817(1) | duty / claim | the prosecutor or the justice (each as the sentence names) | the respondent | `s 817(1) the prosecutor is required to appear before a justice`; `s 817(1) the justice is required to order that the prosecutor enter into a recognizance`; `s 817(1) the justice is to order that the prosecutor enter into a recognizance`; `s 817(1) the prosecutor is to appear before a justice` |
| s 817(3) | immunity / disability | the Attorney General | a justice | `s 817(3) section 817 does not apply` |
| s 818(1) | power / liability | the appellant or the respondent | the other party | `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` |
| s 818(2) | duty / claim | the appeal court | the applicant | `s 818(2) the appeal court is required to dismiss the application or allow it` |
| s 818(2)(b) | power / liability | the appeal court | the appellant and the respondent | `s 818(2)(b) the appeal court may allow the application, vacate the order made by the justice and make the order that it considers should have been made` |
| s 819(1) | duty / claim | the person having custody of the appellant | the appellant | `s 819(1) the day on which the thirty days expire`; `s 819(1) the person having the custody of the appellant is required to apply to the appeal court to fix a date for the hearing`; `s 819(1) the custodian is to apply to the appeal court` |
| s 819(2) | duty / claim | the appeal court | the appellant | `s 819(2) the appeal court is required to fix a date for the hearing and give directions for expediting it`; `s 819(2) the appeal court is to fix a date for the hearing` |
| s 820(1) | immunity / disability | the appellant | the respondent | `s 820(1) the person waives the right of appeal under section 813 by paying the fine` |
| s 821(1) | duty / claim | the clerk of the appeal court and the summary conviction court | the appeal court | `s 821(1) the clerk of the appeal court is required to notify the summary conviction court of the appeal`; `s 821(1) the summary conviction court is required to transmit the conviction, order or order of dismissal and all other material to the appeal court`; `s 821(1) the material is transmitted in time`; `s 821(1) the material is required to be kept by the clerk of the appeal court with the records of the appeal court`; `s 821(1) the summary conviction court is to transmit the material`; `s 821(1) the clerk is to notify the summary conviction court` |
| s 821(2) | immunity / disability | the appellant | the appeal court | `s 821(2) the appeal is barred from being dismissed by the appeal court` |
| s 821(3) | duty / claim | the appellant | the appeal court and the respondent | `s 821(3) the appellant is required to cause a transcript to be furnished to the appeal court and the respondent` |
| s 822(2) | duty / claim | the appeal court | the defendant | `s 822(2) the new trial is required to be held before a summary conviction court other than the court that tried the defendant in the first instance` |
| s 822(3) | power / liability | the appeal court | the appellant and the respondent | `s 822(3) the appeal court may make an order for the release or detention of the appellant pending the new trial`; `s 822(3) the order may be enforced as if made by a justice under section 515 and the provisions of Part XVI apply to it` |
| s 822(4) | power / liability | the appeal court | the appellant and the respondent | `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo`; `s 822(4) sections 793 to 809 apply to the trial de novo` |
| s 822(5) | power / liability | the appeal court | the appellant and the respondent | `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read`; `s 822(5) the evidence that is read has the same force and effect as if the witness had given it before the appeal court` |
| s 822(6) | duty / claim | the appeal court | the appellant and the respondent | `s 822(6) the appeal court is required to consider the fitness of the sentence appealed against` |
| s 822(6) | power / liability | the appeal court | the appellant and the respondent | `s 822(6) the appeal court may make the order`; `s 822(6) the appeal court may take into account any time spent in custody by the defendant as a result of the offence` |
| s 822(7)(a) | immunity / disability | the respondent | the appellant | `s 822(7)(a) judgment is barred from being given in favour of the appellant` |
| s 822(7)(b) | immunity / disability | the respondent | the appellant | `s 822(7)(b) judgment is barred from being given in favour of the appellant and the court is required to make an order curing the defect` |
| s 824(1) | power / liability | the appeal court | the appellant and the respondent | `s 824(1) the appeal court may adjourn the hearing of an appeal` |
| s 824(2) | duty / claim | the appeal court | the appellant and the respondent | `s 824(2) the appeal court is required to consider the interests of justice`; `s 824(2) the appeal court is required to consider the interests of any victim of the offence in question` |
| s 825 | power / liability | the appeal court | the appellant and the respondent | `s 825 the appeal court may order that the appeal be dismissed` |
| s 826 | power / liability | the appeal court | the appellant and the respondent | `s 826 the appeal court may make the order with respect to costs` |
| s 827(1) | duty / claim | the appeal court | the party entitled to the costs | `s 827(1) the order is required to direct that the costs be paid to the clerk of the court and to fix the period within which they are to be paid` |
| s 827(2) | duty / claim | the clerk of the court | the party entitled to the costs | `s 827(2) the clerk of the court is required to issue a certificate in Form 42` |
| s 827(3) | power / liability | a justice | the defaulter | `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26`; `s 827(3) the term of imprisonment does not exceed one month` |
| s 828(1) | power / liability | the summary conviction court | the defendant | `s 828(1) the conviction or order may be enforced in the way` |
| s 828(2) | power / liability | the summary conviction court | the defendant | `s 828(2) the summary conviction court or a justice may issue a warrant of committal as if no appeal had been taken` |
| s 828(3) | duty / claim | the clerk of the appeal court | a justice | `s 828(3) the clerk of the appeal court is required to send the document to the justice`; `s 828(3) the clerk of the appeal court is to send the conviction or order to the justice` |
| s 830(1) | power / liability | the person who is a party or the Attorney General | the other party | `s 830(1) the person may appeal against the decision on the ground` |
| s 830(2) | duty / claim | the appellant | the respondent | `s 830(2) the appeal is required to be based on a transcript of the proceedings appealed from` |
| s 830(3) | duty / claim | the appellant | the respondent | `s 830(3) the notice of appeal is served and filed within thirty days after the date of the decision`; `s 830(3) the last day for serving and filing the notice of appeal` |
| s 830(4) | power / liability | the Attorney General of Canada | the respondent | `s 830(4) the Attorney General of Canada has the same rights of appeal as the Attorney General of a province` |
| s 831 | duty / claim | the appeal court | the appellant and the respondent | `s 831 the provision applies to the appeal`; `s 831 the appeal court is required to give such directions as it thinks necessary for expediting the hearing of the appeal` |
| s 832(1) | power / liability | the appeal court | the appellant | `s 832(1) the appeal court may take the course` |
| s 832(2) | immunity / disability | the Attorney General | the appeal court | `s 832(2) subsection (1) does not apply` |
| s 833 | immunity / disability | the appellant | the court | `s 833 a writ of certiorari or other writ is required to remove the conviction, judgment, verdict or other final order or determination` |
| s 834(1) | duty / claim | the appeal court | the appellant and the respondent | `s 834(1) the appeal court is required to hear and determine the grounds of appeal` |
| s 834(1) | power / liability | the appeal court | the appellant and the respondent | `s 834(1) the appeal court may take the course` |
| s 834(2) | power / liability | a judge of the appeal court sitting in chambers | the appellant and the respondent | `s 834(2) the authority and jurisdiction may be exercised by a judge of the court sitting in chambers` |
| s 835(1) | power / liability | the summary conviction court or a justice | the defendant | `s 835(1) the summary conviction court or a justice has the same authority to enforce the conviction, order or determination as if no appeal had been taken` |
| s 835(2) | power / liability | the appeal court | the person against whom the order is made | `s 835(2) the order may be enforced by the process of the appeal court` |
| s 837 | immunity / disability | the defendant | the prosecution side | `s 837 no appeal under section 830 lies from the conviction or order` |
| s 838 | power / liability | the appeal court or a judge of it | the appellant and the respondent | `s 838 the appeal court or a judge thereof may extend the time period` |
| s 839(1) | power / liability | the appellant (with leave of the court of appeal) | the respondent | `s 839(1) an appeal to the court of appeal may be taken against the decision`; `s 839(1) the decision is one named`; `s 839(1) the named decision may be appealed` |
| s 839(1.1) | power / liability | the appellant (with leave of the court of appeal) | the respondent | `s 839(1.1) an appeal to the Court of Appeal of Nunavut may be taken against the decision` |
| s 839(3) | power / liability | the court of appeal | the appellant and the respondent | `s 839(3) the court of appeal may make the order with respect to costs` |
| s 839(4) | power / liability | the summary conviction court | the person against whom the decision is enforced | `s 839(4) the decision may be enforced in the same manner as if it had been made by the summary conviction court` |
| s 839(5) | power / liability | the Attorney General of Canada | the respondent | `s 839(5) the Attorney General of Canada has the same rights of appeal as the Attorney General of a province` |
| s 840(1) | power / liability | a summary conviction court or a justice | the person charged the fee | `s 840(1) the fee or allowance may be taken or allowed in proceedings before summary conviction courts and justices` |
| s 840(2) | power / liability | the lieutenant governor in council of a province | the person charged the fee | `s 840(2) the lieutenant governor in council may order that all or any of the fees and allowances shall not be taken or allowed in the province`; `s 840(2) the lieutenant governor in council may fix other fees and allowances to be taken or allowed instead` |
| s 842 | privilege / no-right | a court | the person who files or deals with the electronic document | `s 842 a court may create, collect, receive, store, transfer, distribute, publish or otherwise deal with electronic documents` |
| s 843(1) | privilege / no-right | a court | the person who files or deals with the electronic document | `s 843(1) a court may accept the transfer of data by electronic means` |
| s 845 | privilege / no-right | a court | the person who files or deals with the electronic document | `s 845 the court may accept a signature in an electronic document` |
| s 846 | privilege / no-right | a court | the person who files or deals with the electronic document | `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` |
| s 847 | duty / claim | the court | the person entitled to a copy | `s 847 the person is entitled to obtain a printed copy of the electronic document from the court` |
| s 849(1) | immunity / disability | the person using the form | the other party | `s 849(1) the form is deemed to be good, valid and sufficient` |
| s 849(2) | duty / claim | a justice or the summary conviction court | the person charged | `s 849(2) the justice is required to attach or affix a seal` |
| s 849(3) | duty / claim | a justice or the summary conviction court | the person charged | `s 849(3) the pre-printed portion is required to be printed in both official languages` |
| sch XXVII | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII the amount in dollars stated in the row of the item`; `sch XXVII the words of the item`; `sch XXVII the unit of the amount of the item`; `sch XXVII the group under which the item stands` |
| sch XXVII note after item 5 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII note after item 5 a further subpoena may be issued on behalf of the party in the proceeding`; `sch XXVII note after item 5 the subpoena may contain the number of names` |
| sch XXVII item 10 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII item 10 the fee applies` |
| sch XXVII item 11 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` |
| sch XXVII note after item 15 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII note after item 15 the item may be charged` |
| sch XXVII note after item 20 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII note after item 20 reasonable costs of transportation may be allowed` |
| sch XXVII note after item 23 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII note after item 23 a charge may be made under item 23 in respect of the service` |
| sch XXVII item 22 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII item 22 the fee applies` |
| sch XXVII note after item 24 | power / liability | the court, justice, peace officer, witness or interpreter the item names | the person charged the fee | `sch XXVII note after item 24 the amount charged for the day is within the limit` |

**Provisions that create no relation (`none`)**: definitions, counting rules, deeming rules, applications of other provisions, lists and tables (83 functions): `s 785 the definitions apply`; `s 785 clerk of the appeal court`; `s 785 informant`; `s 785 information`; `s 785 order`; `s 785 proceedings`; `s 785 prosecutor`; `s 785 sentence`; `s 785 summary conviction court`; `s 785 trial`; `s 786(1) this Part applies to the proceedings`; `s 786(2) the day on which the 12 months end`; `s 787(1) the general penalty as stated in section 787(1)`; `s 787(2) the longest term of imprisonment the court may order in default`; `s 795 the provisions apply, with any necessary modifications, to proceedings under this Part`; `s 795 compelling appearance`; `s 795 not inconsistent`; `s 806(1) a conviction or order in Form 35 or 36 and a certified copy are required to be drawn up and the certified copy delivered to the person making the request`; `s 806(1) the form to be drawn up`; `s 806(2) section 528 applies in respect of the warrant of committal`; `s 806(3) the copy of the warrant of committal is admissible in evidence in any proceeding`; `s 807 the most that is to be paid to the person aggrieved`; `s 807 the residue to be applied in the manner in which other penalties imposed by law are directed to be applied`; `s 809(5) costs`; `s 810(3) the period of the recognizance is not more than 12 months`; `s 810(3.01) the term of imprisonment is not more than 12 months`; `s 810(4) the warrant of committal may be in Form 23`; `s 810(5) the provisions of this Part apply to the proceedings`; `s 810.01(3) the period of the recognizance is not more than 12 months`; `s 810.01(3.1) the longer period of the recognizance is not more than two years`; `s 810.01(4) the term of imprisonment does not exceed twelve months`; `s 810.01(7) subsections 810(4) and (5) apply to the recognizance`; `s 810.01(8) Attorney General`; `s 810.011(3) the period of the recognizance is not more than 12 months`; `s 810.011(4) the longer period of the recognizance is not more than five years`; `s 810.011(5) the term of imprisonment is not more than 12 months`; `s 810.011(13) subsections 810(4) and (5) apply to the recognizance`; `s 810.011(14) Attorney General`; `s 810.02(3) the period of the recognizance is not more than 12 months`; `s 810.02(4) the longer period of the recognizance is not more than two years`; `s 810.02(5) the term of imprisonment does not exceed 12 months`; `s 810.03(3) the period of the recognizance is not more than 12 months`; `s 810.03(4) the longer period of the recognizance is not more than two years`; `s 810.03(5) the term of imprisonment does not exceed 12 months`; `s 810.03(13) the provisions of this Part apply to the proceedings`; `s 810.1(1) the feared offence is one of those listed`; `s 810.1(3) the period of the recognizance does not exceed 12 months`; `s 810.1(3.01) the longer period of the recognizance is not more than two years`; `s 810.1(3.1) the term of imprisonment does not exceed twelve months`; `s 810.1(5) subsections 810(4) and (5) apply to the recognizance`; `s 810.2(3) the period of the recognizance does not exceed 12 months`; `s 810.2(3.1) the longer period of the recognizance does not exceed two years`; `s 810.2(4) the term of imprisonment does not exceed twelve months`; `s 810.2(8) subsections 810(4) and (5) apply to the recognizance`; `s 810.21(2) sections 714.1 to 714.8 and Part XXII.01 apply to the proceedings`; `s 810.5(1) sections 486 to 486.5 and 486.7 apply to the proceedings`; `s 811.1(2) analyst`; `s 812(1) the appeal court for sections 813 to 828`; `s 812(2) the appeal court once subsection (2) is applied`; `s 816(2) sections 495.1, 512.3 and 524 apply to the proceedings`; `s 817(2) the condition of the recognizance is that the prosecutor will appear personally or by counsel at the sittings of the appeal court`; `s 818(3) the order has the same force and effect as if it had been made by the justice`; `s 820(2) the conviction, order or sentence is deemed not to have been appealed against`; `s 822(1) the provision applies to the appeal`; `s 822(6)(b) the varied sentence is within the limits prescribed by law`; `s 829 the appeal court for sections 830 to 838`; `s 836 the person is taken to have abandoned all rights of appeal under section 813`; `s 839(2) the provision applies to the appeal`; `s 841 the definitions apply`; `s 841 data`; `s 841 electronic document`; `s 843(2) the filing is complete`; `s 844 the requirement that a document be made in writing is satisfied`; `sch XX.1 the schedule has any entry`; `sch XXII.1 para 1 the offence is one of those listed`; `sch XXII.1 para 1 the words of the entry that names the provision`; `sch XXII.1 para 2 the offence is one of those listed`; `sch XXII.1 para 3 the conspiracy, attempt, accessory or counselling is one of those listed`; `sch XXII.1 the offence is listed`; `sch XXV column I the province or territory of the row`; `sch XXV column II the court of the row`; `sch XXV column III the officer of the row`; `sch XXV the rows of the province or territory`.

## Marginal readings for a lawyer (ccc29)

Readings (a) and (b) of the brief are taken as the status quo: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Every branch of this part that answers `JUST FALSE` rests on reading (a), whether it is a failed "if", "unless", "where" or "when" or a stated limit or flat negative; each is listed below with the other reading (`NOTHING`), and the count is given under the table (the comment on each branch is `-- FALSE-kind`).
Every branch that answers `NOTHING` as "limited by its own wording" rests on reading (b); they are counted, not listed, at the foot of this section, because they number in the hundreds and the other reading (`JUST FALSE`) is the same for all.

| function | line | what the branch rests on | quoted words | other reading |
| --- | --- | --- | --- | --- |
| `s 785 informant` | xxvii-a-interpretation-penalty:56 | a closed definition ("means") | "informant means a person who lays an information" | NOTHING |
| `s 785 order` | xxvii-a-interpretation-penalty:82 | a closed definition ("means") | "order means any order, including an order for the payment of money" | NOTHING |
| `s 785 proceedings` | xxvii-a-interpretation-penalty:96 | a closed definition ("means") | "proceedings means" | NOTHING |
| `s 785 prosecutor` | xxvii-a-interpretation-penalty:115 | failed condition | "where the Attorney General does not intervene" | NOTHING |
| `s 785 prosecutor` | xxvii-a-interpretation-penalty:117 | a closed definition ("means") | "prosecutor means the Attorney General" | NOTHING |
| `s 785 summary conviction court` | xxvii-a-interpretation-penalty:191 | a closed definition ("means") | "summary conviction court means a person who has jurisdiction in the territorial division" | NOTHING |
| `s 786(1) this Part applies to the proceedings` | xxvii-a-interpretation-penalty:216 | failed condition | "Except where otherwise provided by law" | NOTHING |
| `s 786(2) the proceedings are barred because they were instituted more than 12 months after the subject matter arose` | xxvii-a-interpretation-penalty:230 | failed condition | "unless the prosecutor and the defendant so agree" | NOTHING |
| `s 786(2) the proceedings are barred because they were instituted more than 12 months after the subject matter arose` | xxvii-a-interpretation-penalty:231 | stated limit or flat negative | "No proceedings shall be instituted more than 12 months after" | NOTHING |
| `s 787(1) the general penalty applies to the offence` | xxvii-a-interpretation-penalty:258 | failed condition | "Unless otherwise provided by law" | NOTHING |
| `s 787(1) the fine is not more than $5,000` | xxvii-a-interpretation-penalty:267 | stated limit or flat negative | "a fine of not more than $5,000" | NOTHING |
| `s 787(1) the term of imprisonment is not more than two years less a day` | xxvii-a-interpretation-penalty:276 | stated limit or flat negative | "a term of imprisonment of not more than two years less a day" | NOTHING |
| `s 789(1)(b) each offence or matter of complaint is required to be set out in a separate count` | xxvii-b-information-trial:98 | failed condition | "but where more than one offence is charged or the information relates to more than one matter of complaint" | NOTHING |
| `s 790(2) the justices are required to be present and act together at the trial` | xxvii-b-information-trial:133 | failed condition | "Where two or more justices have jurisdiction with respect to proceedings" | NOTHING |
| `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` | xxvii-b-information-trial:142 | failed condition | "Where two or more justices have jurisdiction with respect to proceedings" | NOTHING |
| `s 790(2) one justice may do anything required or authorized to be done in connection with the proceedings` | xxvii-b-information-trial:143 | stated limit or flat negative | "one justice may thereafter do anything" | NOTHING |
| `s 795 not inconsistent` | xxvii-b-information-trial:202 | stated limit or flat negative | "insofar as they are not inconsistent with this Part" | NOTHING |
| `s 799 the summary conviction court may take the course` | xxvii-b-information-trial:248 | failed condition | "Where, in proceedings to which this Part applies, the defendant appears for the trial and the prosecutor, having had due notice, does not appear" | NOTHING |
| `s 800(1) the summary conviction court is required to hold the trial` | xxvii-b-information-trial:259 | failed condition | "Where the prosecutor and defendant appear for the trial" | NOTHING |
| `s 800(3) the organization is required to appear by counsel or agent` | xxvii-b-information-trial:317 | failed condition | "Where the defendant is an organization" | NOTHING |
| `s 800(3) the summary conviction court may proceed ex parte to hold the trial` | xxvii-b-information-trial:332 | failed condition | "if it does not appear, the summary conviction court may, on proof of service of the summons" | NOTHING |
| `s 801(1) the substance of the information is required to be stated to the defendant` | xxvii-b-information-trial:345 | failed condition | "Where the defendant appears for the trial" | NOTHING |
| `s 801(1)(a) the defendant is required to be asked whether they plead guilty or not guilty to the information` | xxvii-b-information-trial:354 | failed condition | "where the proceedings are in respect of an offence that is punishable on summary conviction" | NOTHING |
| `s 801(1)(b) the defendant is required to be asked whether they have cause to show why an order should not be made against them` | xxvii-b-information-trial:363 | failed condition | "in proceedings where a justice is authorized by law to make an order" | NOTHING |
| `s 801(2) the summary conviction court is required to convict the defendant, discharge the defendant under section 730 or make an order against the defendant` | xxvii-b-information-trial:375 | failed condition | "Where the defendant pleads guilty or does not show sufficient cause why an order should not be made against him" | NOTHING |
| `s 801(3) the summary conviction court is required to proceed with the trial and take the evidence in accordance with Part XVIII` | xxvii-b-information-trial:387 | failed condition | "Where the defendant pleads not guilty or states that he has cause to show why an order should not be made against him" | NOTHING |
| `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` | xxvii-b-information-trial:456 | failed condition | "if he or she is liable, on summary conviction, to imprisonment for a term of more than six months" | NOTHING |
| `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` | xxvii-b-information-trial:457 | failed condition | "unless (a) the defendant is an organization" | NOTHING |
| `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` | xxvii-b-information-trial:458 | stated limit or flat negative | "(b) the defendant is appearing to request an adjournment of the proceedings" | NOTHING |
| `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent` | xxvii-b-information-trial:459 | stated limit or flat negative | "(c) the agent is authorized to do so under a program approved" | NOTHING |
| `s 803(1) the summary conviction court may adjourn the trial to a time and place to be appointed and stated in the presence of the parties or their counsel or agents` | xxvii-b-information-trial:473 | stated limit or flat negative | "before or during the trial" | NOTHING |
| `s 803(1.1) the summary conviction court is required to consider the interests of justice` | xxvii-b-information-trial:484 | stated limit or flat negative | "In deciding whether to adjourn the trial under subsection (1)" | NOTHING |
| `s 803(1.1) the summary conviction court is required to consider the interests of any victim of the offence in question` | xxvii-b-information-trial:492 | stated limit or flat negative | "In deciding whether to adjourn the trial under subsection (1)" | NOTHING |
| `s 803(1.1) the summary conviction court is required to consider the interests of any victim of the offence in question` | xxvii-b-information-trial:493 | failed condition | "if information related to the victim's interests is readily available" | NOTHING |
| `s 803(3) the consent of the Attorney General is required before the proceedings under section 145 are instituted or proceeded with` | xxvii-b-information-trial:536 | failed condition | "If the summary conviction court proceeds in the manner described in paragraph (2)(a)" | NOTHING |
| `s 803(4) the summary conviction court may dismiss the information with or without costs` | xxvii-b-information-trial:548 | failed condition | "Where the prosecutor does not appear at the time and place appointed for the resumption of an adjourned trial" | NOTHING |
| `s 804 the summary conviction court is required to convict the defendant, discharge the defendant under section 730, make an order against the defendant or dismiss the information` | xxvii-b-information-trial:561 | failed condition | "When the summary conviction court has heard the prosecutor, defendant and witnesses" | NOTHING |
| `s 806(1) a minute or memorandum indicating that the matter was dealt with under this Part is required to be made by the summary conviction court` | xxvii-b-information-trial:587 | failed condition | "If a defendant is convicted or an order is made in relation to the defendant" | NOTHING |
| `s 806(1) a conviction or order in Form 35 or 36 and a certified copy are required to be drawn up and the certified copy delivered to the person making the request` | xxvii-b-information-trial:600 | failed condition | "If a defendant is convicted or an order is made in relation to the defendant" | NOTHING |
| `s 806(2) the summary conviction court is required to issue a warrant of committal in Form 21 or 22` | xxvii-b-information-trial:619 | failed condition | "Where a defendant is convicted or an order is made against him" | NOTHING |
| `s 806(3) the copy of the warrant of committal is admissible in evidence in any proceeding` | xxvii-b-information-trial:649 | failed condition | "If a warrant of committal in Form 21 is signed by a clerk of a court" | NOTHING |
| `s 808(1) the summary conviction court may draw up an order of dismissal` | xxvii-b-information-trial:687 | failed condition | "Where the summary conviction court dismisses an information" | NOTHING |
| `s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant` | xxvii-b-information-trial:723 | failed condition | "where the summary conviction court convicts or makes an order against the defendant" | NOTHING |
| `s 809(1)(b) the summary conviction court may award costs to be paid to the defendant by the informant` | xxvii-b-information-trial:734 | failed condition | "where the summary conviction court dismisses an information" | NOTHING |
| `s 809(4) the person who is liable to pay the costs is, in default of payment, liable to imprisonment for one month` | xxvii-b-information-trial:772 | failed condition | "Where no fine or sum of money is adjudged to be paid by a defendant, but costs are awarded against the defendant or informant" | NOTHING |
| `s 810(3) the period of the recognizance is not more than 12 months` | xxviii-0-peace-810:86 | stated limit or flat negative | "for a period of not more than 12 months" | NOTHING |
| `s 810(3.01) the term of imprisonment is not more than 12 months` | xxviii-0-peace-810:106 | stated limit or flat negative | "a term of not more than 12 months" | NOTHING |
| `s 810(3.1) the justice or court is required to consider whether a firearms prohibition is desirable` | xxviii-0-peace-810:145 | stated limit or flat negative | "Before making an order under subsection (3)" | NOTHING |
| `s 810(3.1) the justice or court is required to add the firearms condition` | xxviii-0-peace-810:153 | failed condition | "if the justice or summary conviction court decides that it is so desirable" | NOTHING |
| `s 810(3.11) the justice or court is required to specify in the order the manner and method` | xxviii-0-peace-810:189 | failed condition | "Where the justice or summary conviction court adds a condition described in subsection (3.1)" | NOTHING |
| `s 810(3.12) the justice or court is required to include in the record a statement of the reasons for not adding the condition` | xxviii-0-peace-810:206 | failed condition | "Where the justice or summary conviction court does not add a condition described in subsection (3.1)" | NOTHING |
| `s 810(3.2) the justice or court is required to consider whether it is desirable to add the condition` | xxviii-0-peace-810:235 | stated limit or flat negative | "Before making an order under subsection (3)" | NOTHING |
| `s 810(4.1) the justice or court may vary the conditions fixed in the recognizance` | xxviii-0-peace-810:266 | failed condition | "on application of the informant or the defendant" | NOTHING |
| `s 810.01(3) the period of the recognizance is not more than 12 months` | xxviii-0-peace-810:323 | stated limit or flat negative | "for a period of not more than 12 months" | NOTHING |
| `s 810.01(3.1) the longer period of the recognizance is not more than two years` | xxviii-0-peace-810:343 | stated limit or flat negative | "for a period of not more than two years" | NOTHING |
| `s 810.01(4) the term of imprisonment does not exceed twelve months` | xxviii-0-peace-810:363 | stated limit or flat negative | "a term not exceeding twelve months" | NOTHING |
| `s 810.01(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies` | xxviii-0-peace-810:423 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.01(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-0-peace-810:453 | failed condition | "If the provincial court judge adds a condition described in subsection (5)" | NOTHING |
| `s 810.01(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition` | xxviii-0-peace-810:470 | failed condition | "If the provincial court judge does not add a condition described in subsection (5)" | NOTHING |
| `s 810.01(6) the provincial court judge may vary the conditions fixed in the recognizance` | xxviii-0-peace-810:490 | failed condition | "on application of the informant, the Attorney General or the defendant" | NOTHING |
| `s 810.01(8) Attorney General` | xxviii-0-peace-810:523 | a closed definition ("means") | "Attorney General means either the Attorney General of Canada or the Attorney General of the province" | NOTHING |
| `s 810.011(3) the period of the recognizance is not more than 12 months` | xxviii-0-peace-810:570 | stated limit or flat negative | "for a period of not more than 12 months" | NOTHING |
| `s 810.011(4) the longer period of the recognizance is not more than five years` | xxviii-0-peace-810:590 | stated limit or flat negative | "for a period of not more than five years" | NOTHING |
| `s 810.011(5) the term of imprisonment is not more than 12 months` | xxviii-0-peace-810:610 | stated limit or flat negative | "a term of not more than 12 months" | NOTHING |
| `s 810.011(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies` | xxviii-0-peace-810:667 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.011(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-0-peace-810:678 | failed condition | "If the provincial court judge adds a condition described in subsection (7)" | NOTHING |
| `s 810.011(9) the provincial court judge is required to add the passport condition and specify the period during which it applies` | xxviii-0-peace-810:697 | failed condition | "If the judge decides that it is desirable" | NOTHING |
| `s 810.011(10) the provincial court judge is required to add the geographic-area condition and specify the period during which it applies` | xxviii-0-peace-810:716 | failed condition | "If the judge decides that it is desirable" | NOTHING |
| `s 810.011(11) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition` | xxviii-0-peace-810:727 | failed condition | "If the provincial court judge does not add a condition described in subsection (7), (9) or (10)" | NOTHING |
| `s 810.011(12) the provincial court judge may vary the conditions fixed in the recognizance` | xxviii-0-peace-810:741 | failed condition | "on application of the informant, the Attorney General or the defendant" | NOTHING |
| `s 810.011(14) Attorney General` | xxviii-0-peace-810:774 | a closed definition ("means") | "Attorney General means either the Attorney General of Canada or the Attorney General of the province" | NOTHING |
| `s 810.02(3) the period of the recognizance is not more than 12 months` | xxviii-1-peace-810-02:55 | stated limit or flat negative | "for a period of not more than 12 months" | NOTHING |
| `s 810.02(4) the longer period of the recognizance is not more than two years` | xxviii-1-peace-810-02:75 | stated limit or flat negative | "for a period of not more than two years" | NOTHING |
| `s 810.02(5) the term of imprisonment does not exceed 12 months` | xxviii-1-peace-810-02:95 | stated limit or flat negative | "a term not exceeding 12 months" | NOTHING |
| `s 810.02(7) the provincial court judge is required to add the firearms condition and specify the period during which it applies` | xxviii-1-peace-810-02:154 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.02(8) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-1-peace-810-02:183 | failed condition | "If the provincial court judge adds a condition described in subsection (7)" | NOTHING |
| `s 810.02(9) the provincial court judge may vary the conditions fixed in the recognizance` | xxviii-1-peace-810-02:202 | failed condition | "on application of the informant or the defendant" | NOTHING |
| `s 810.03(3) the period of the recognizance is not more than 12 months` | xxviii-1-peace-810-02:248 | stated limit or flat negative | "for a period of not more than 12 months" | NOTHING |
| `s 810.03(4) the longer period of the recognizance is not more than two years` | xxviii-1-peace-810-02:273 | stated limit or flat negative | "for a period of not more than two years" | NOTHING |
| `s 810.03(4.1) the justice is required to consider whether it would be more appropriate to recommend Indigenous support services` | xxviii-1-peace-810-02:284 | failed condition | "If the defendant or the person on whose behalf the information is laid is Indigenous" | NOTHING |
| `s 810.03(5) the term of imprisonment does not exceed 12 months` | xxviii-1-peace-810-02:318 | stated limit or flat negative | "a term not exceeding 12 months" | NOTHING |
| `s 810.03(7) the justice is required to add the firearms condition and specify the period during which it applies` | xxviii-1-peace-810-02:381 | failed condition | "If the justice decides that it is desirable to do so" | NOTHING |
| `s 810.03(8) the justice is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-1-peace-810-02:405 | failed condition | "If the justice adds a condition described in subsection (7)" | NOTHING |
| `s 810.03(9) the justice is required to include in the record a statement of the reasons for not adding the condition` | xxviii-1-peace-810-02:422 | failed condition | "If the justice does not add a condition described in subsection (7)" | NOTHING |
| `s 810.03(10) the justice may vary the conditions fixed in the recognizance` | xxviii-1-peace-810-02:443 | failed condition | "on application of the Attorney General, the informant, the person on whose behalf the information is laid or the defendant" | NOTHING |
| `s 810.03(11) the justice is required, before varying any conditions, to consider the safety and security needs of the person on whose behalf the information is laid` | xxviii-1-peace-810-02:454 | failed condition | "If the defendant makes an application under subsection (10)" | NOTHING |
| `s 810.1(3) the period of the recognizance does not exceed 12 months` | xxviii-2-peace-810-1:89 | stated limit or flat negative | "for a period that does not exceed 12 months" | NOTHING |
| `s 810.1(3.01) the longer period of the recognizance is not more than two years` | xxviii-2-peace-810-1:109 | stated limit or flat negative | "for a period of not more than two years" | NOTHING |
| `s 810.1(3.03) the provincial court judge is required to add the firearms condition and specify the period during which it applies` | xxviii-2-peace-810-1:181 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.1(3.04) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-2-peace-810-1:212 | failed condition | "If the provincial court judge adds a condition described in subsection (3.03)" | NOTHING |
| `s 810.1(3.05) the provincial court judge is required to add the reporting condition` | xxviii-2-peace-810-1:237 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.1(3.1) the term of imprisonment does not exceed twelve months` | xxviii-2-peace-810-1:270 | stated limit or flat negative | "a term not exceeding twelve months" | NOTHING |
| `s 810.1(4) the provincial court judge may vary the conditions fixed in the recognizance` | xxviii-2-peace-810-1:283 | failed condition | "on application of the informant or the defendant" | NOTHING |
| `s 810.2(3) the period of the recognizance does not exceed 12 months` | xxviii-2-peace-810-1:340 | stated limit or flat negative | "for a period that does not exceed 12 months" | NOTHING |
| `s 810.2(3.1) the longer period of the recognizance does not exceed two years` | xxviii-2-peace-810-1:360 | stated limit or flat negative | "for a period that does not exceed two years" | NOTHING |
| `s 810.2(4) the term of imprisonment does not exceed twelve months` | xxviii-2-peace-810-1:380 | stated limit or flat negative | "a term not exceeding twelve months" | NOTHING |
| `s 810.2(5) the provincial court judge is required to add the firearms condition and specify the period during which it applies` | xxviii-2-peace-810-1:440 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.2(5.1) the provincial court judge is required to specify in the recognizance how the things and authorizations are to be surrendered` | xxviii-2-peace-810-1:472 | failed condition | "If the provincial court judge adds a condition described in subsection (5)" | NOTHING |
| `s 810.2(5.2) the provincial court judge is required to include in the record a statement of the reasons for not adding the condition` | xxviii-2-peace-810-1:489 | failed condition | "If the provincial court judge does not add a condition described in subsection (5)" | NOTHING |
| `s 810.2(6) the provincial court judge is required to add the reporting condition` | xxviii-2-peace-810-1:514 | failed condition | "If the judge decides that it is desirable to do so" | NOTHING |
| `s 810.2(7) the provincial court judge may vary the conditions fixed in the recognizance` | xxviii-2-peace-810-1:541 | failed condition | "on application of the informant, of the Attorney General or of the defendant" | NOTHING |
| `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` | xxviii-3-peace-810-21:33 | failed condition | "on application of the prosecutor" | NOTHING |
| `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` | xxviii-3-peace-810-21:63 | failed condition | "on application of a peace officer or the Attorney General" | NOTHING |
| `s 810.22(2) the transfer is barred for want of the consent that the subsection requires` | xxviii-3-peace-810-21:83 | stated limit or flat negative | "The transfer may be granted only with" | NOTHING |
| `s 810.3(3) the taking, analysis, storage, handling or destruction of the sample, or the protection or destruction of the record, is barred` | xxviii-3-peace-810-21:187 | failed condition | "except in accordance with the designations and specifications made under subsection (1)" | NOTHING |
| `s 810.3(4) the authority is required to cause the samples to be destroyed within the period prescribed by regulation` | xxviii-3-peace-810-21:201 | failed condition | "unless the samples are reasonably expected to be used as evidence in a proceeding for an offence under section 811" | NOTHING |
| `s 810.3(6) the first sample is barred because it is taken earlier than 24 hours after the defendant is served with the notice` | xxviii-3-peace-810-21:229 | stated limit or flat negative | "The first sample may not be taken earlier than 24 hours after the defendant is served with the notice" | NOTHING |
| `s 810.3(6) the subsequent samples are taken at regular intervals of at least seven days` | xxviii-3-peace-810-21:239 | stated limit or flat negative | "subsequent samples must be taken at regular intervals of at least seven days" | NOTHING |
| `s 810.4(1) the use of the bodily substance is barred` | xxviii-3-peace-810-21:253 | failed condition | "except for the purpose of determining whether a defendant is complying with a condition" | NOTHING |
| `s 810.4(2) the use or disclosure of the results of the analysis is barred` | xxviii-3-peace-810-21:266 | failed condition | "Subject to subsection (3)" | NOTHING |
| `s 810.4(4) the person is guilty of an offence punishable on summary conviction` | xxviii-3-peace-810-21:304 | stated limit or flat negative | "Every person who contravenes subsection (1) or (2) is guilty" | NOTHING |
| `s 810.5(2) the person is guilty of an offence under section 486.6` | xxviii-3-peace-810-21:347 | stated limit or flat negative | "Every person who fails to comply with an order" | NOTHING |
| `s 811 the person is guilty of an offence` | xxviii-3-peace-810-21:364 | stated limit or flat negative | "who commits a breach of the recognizance is guilty" | NOTHING |
| `s 811.1(1) the certificate is proof of the statements contained in it without proof of the signature or official character` | xxviii-3-peace-810-21:406 | stated limit or flat negative | "in the absence of evidence to the contrary, is proof of the statements" | NOTHING |
| `s 811.1(3) the certificate is barred from admission in evidence` | xxviii-3-peace-810-21:428 | failed condition | "unless the party intending to produce it has, before the trial, given reasonable notice and a copy of the certificate" | NOTHING |
| `s 813 the person may appeal to the appeal court` | xxviii-4-appeal-812:121 | failed condition | "Except where otherwise provided by law" | NOTHING |
| `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` | xxviii-4-appeal-812:198 | failed condition | "on the application of one of the parties" | NOTHING |
| `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` | xxviii-4-appeal-812:199 | failed condition | "on the application of one of the parties" | NOTHING |
| `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` | xxviii-4-appeal-812:200 | failed condition | "on the application of one of the parties" | NOTHING |
| `s 814 the judge of the appeal court may appoint another place for the hearing of the appeal` | xxviii-4-appeal-812:201 | failed condition | "on the application of one of the parties" | NOTHING |
| `s 815(1) the notice of appeal is given within the period directed by the rules of court` | xxviii-4-appeal-812:231 | stated limit or flat negative | "within such period as may be directed by rules of court" | NOTHING |
| `s 816(1) the appellant is required to remain in custody` | xxviii-4-appeal-812:271 | failed condition | "if they are in custody" | NOTHING |
| `s 816(1) the appellant is required to remain in custody` | xxviii-4-appeal-812:272 | failed condition | "unless the appeal court at which the appeal is to be heard makes a release order" | NOTHING |
| `s 816(1.1) the person having the custody of the appellant is required to release the appellant immediately` | xxviii-4-appeal-812:292 | failed condition | "if the appellant complies with the order" | NOTHING |
| `s 817(1) the prosecutor is required to appear before a justice` | xxviii-4-appeal-812:329 | stated limit or flat negative | "This section does not apply in respect of an appeal taken by the Attorney General" | NOTHING |
| `s 817(1) the prosecutor is required to appear before a justice` | xxviii-4-appeal-812:330 | stated limit or flat negative | "immediately after filing the notice of appeal and proof of service of the notice" | NOTHING |
| `s 817(1) the justice is required to order that the prosecutor enter into a recognizance` | xxviii-4-appeal-812:340 | stated limit or flat negative | "after giving the prosecutor and the respondent a reasonable opportunity to be heard" | NOTHING |
| `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` | xxviii-4-appeal-812:395 | failed condition | "Where a justice makes an order under section 817" | NOTHING |
| `s 818(1) the appellant or the respondent may apply to the appeal court for a review of the order made by the justice` | xxviii-4-appeal-812:397 | stated limit or flat negative | "before or at any time during the hearing of the appeal" | NOTHING |
| `s 818(2) the appeal court is required to dismiss the application or allow it` | xxviii-4-appeal-812:412 | failed condition | "On the hearing of an application under this section, the appeal court, after giving the appellant and the respondent a reasonable opportunity to be he" | NOTHING |
| `s 819(1) the person having the custody of the appellant is required to apply to the appeal court to fix a date for the hearing` | xxviii-4-appeal-812:450 | failed condition | "Where, in the case of an appellant who has been convicted by a summary conviction court and who is in custody pending the hearing of his appeal" | NOTHING |
| `s 819(1) the person having the custody of the appellant is required to apply to the appeal court to fix a date for the hearing` | xxviii-4-appeal-812:451 | stated limit or flat negative | "the hearing of his appeal has not commenced within thirty days" | NOTHING |
| `s 819(2) the appeal court is required to fix a date for the hearing and give directions for expediting it` | xxviii-4-appeal-812:479 | failed condition | "On receiving an application under subsection (1), the appeal court shall, after giving the prosecutor a reasonable opportunity to be heard" | NOTHING |
| `s 820(1) the person waives the right of appeal under section 813 by paying the fine` | xxviii-4-appeal-812:496 | stated limit or flat negative | "A person does not waive his right of appeal under section 813 by reason only that he pays the fine imposed on conviction" | NOTHING |
| `s 820(2) the conviction, order or sentence is deemed not to have been appealed against` | xxviii-4-appeal-812:507 | failed condition | "until the contrary is shown" | NOTHING |
| `s 821(1) the clerk of the appeal court is required to notify the summary conviction court of the appeal` | xxviii-4-appeal-812:521 | failed condition | "Where a notice of appeal has been given in accordance with the rules referred to in section 815" | NOTHING |
| `s 821(1) the summary conviction court is required to transmit the conviction, order or order of dismissal and all other material to the appeal court` | xxviii-4-appeal-812:529 | failed condition | "on receipt of the notification" | NOTHING |
| `s 821(1) the material is transmitted in time` | xxviii-4-appeal-812:543 | failed condition | "before the time when the appeal is to be heard, or within such further time as the appeal court may direct" | NOTHING |
| `s 821(3) the appellant is required to cause a transcript to be furnished to the appeal court and the respondent` | xxviii-4-appeal-812:591 | failed condition | "Where the evidence on a trial before a summary conviction court has been taken by a stenographer duly sworn or by a sound recording apparatus" | NOTHING |
| `s 821(3) the appellant is required to cause a transcript to be furnished to the appeal court and the respondent` | xxviii-4-appeal-812:592 | failed condition | "unless the appeal court otherwise orders or the rules referred to in section 815 otherwise provide" | NOTHING |
| `s 822(1) the provision applies to the appeal` | xxviii-4-appeal-812:605 | stated limit or flat negative | "with the exception of subsections 683(3) and 686(5)" | NOTHING |
| `s 822(2) the new trial is required to be held before a summary conviction court other than the court that tried the defendant in the first instance` | xxviii-4-appeal-812:618 | failed condition | "Where an appeal court orders a new trial" | NOTHING |
| `s 822(2) the new trial is required to be held before a summary conviction court other than the court that tried the defendant in the first instance` | xxviii-4-appeal-812:619 | failed condition | "unless the appeal court directs that the new trial be held before the summary conviction court that tried the accused in the first instance" | NOTHING |
| `s 822(3) the appeal court may make an order for the release or detention of the appellant pending the new trial` | xxviii-4-appeal-812:632 | failed condition | "Where an appeal court orders a new trial" | NOTHING |
| `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo` | xxviii-4-appeal-812:655 | failed condition | "on application of the defendant, the informant, the Attorney General or the Attorney General's agent" | NOTHING |
| `s 822(6) the appeal court is required to consider the fitness of the sentence appealed against` | xxviii-4-appeal-812:708 | failed condition | "Where an appeal is taken under subsection (4) against sentence" | NOTHING |
| `s 822(6) the appeal court is required to consider the fitness of the sentence appealed against` | xxviii-4-appeal-812:709 | failed condition | "unless the sentence is one fixed by law" | NOTHING |
| `s 822(6) the appeal court may make the order` | xxviii-4-appeal-812:729 | failed condition | "Where an appeal is taken under subsection (4) against sentence" | NOTHING |
| `s 822(6)(b) the varied sentence is within the limits prescribed by law` | xxviii-4-appeal-812:737 | stated limit or flat negative | "vary the sentence within the limits prescribed by law" | NOTHING |
| `s 822(7)(a) judgment is barred from being given in favour of the appellant` | xxviii-4-appeal-812:767 | failed condition | "unless it is shown (iii) that the objection was taken at the trial, and (iv) that an adjournment of the trial was refused" | NOTHING |
| `s 824(2) the appeal court is required to consider the interests of justice` | xxviii-4-appeal-812:800 | stated limit or flat negative | "In deciding whether to adjourn the hearing" | NOTHING |
| `s 824(2) the appeal court is required to consider the interests of any victim of the offence in question` | xxviii-4-appeal-812:808 | stated limit or flat negative | "In deciding whether to adjourn the hearing" | NOTHING |
| `s 824(2) the appeal court is required to consider the interests of any victim of the offence in question` | xxviii-4-appeal-812:809 | failed condition | "if information related to the victim's interests is readily available" | NOTHING |
| `s 825 the appeal court may order that the appeal be dismissed` | xxviii-4-appeal-812:829 | failed condition | "on proof that notice of an appeal has been given and that (a) ... or (b) ..." | NOTHING |
| `s 826 the appeal court may make the order with respect to costs` | xxviii-4-appeal-812:841 | failed condition | "Where an appeal is heard and determined or is abandoned or is dismissed for want of prosecution" | NOTHING |
| `s 827(1) the order is required to direct that the costs be paid to the clerk of the court and to fix the period within which they are to be paid` | xxviii-4-appeal-812:854 | failed condition | "Where the appeal court orders the appellant or respondent to pay costs" | NOTHING |
| `s 827(2) the clerk of the court is required to issue a certificate in Form 42` | xxviii-4-appeal-812:867 | failed condition | "Where costs are not paid in full within the period fixed for payment" | NOTHING |
| `s 827(2) the clerk of the court is required to issue a certificate in Form 42` | xxviii-4-appeal-812:868 | stated limit or flat negative | "and the person who has been ordered to pay them has not been bound by a recognizance to pay them" | NOTHING |
| `s 827(2) the clerk of the court is required to issue a certificate in Form 42` | xxviii-4-appeal-812:869 | failed condition | "on application by the person entitled to the costs, or by any person on his behalf" | NOTHING |
| `s 827(2) the clerk of the court is required to issue a certificate in Form 42` | xxviii-4-appeal-812:870 | failed condition | "on payment of any fee to which the clerk of the court is entitled" | NOTHING |
| `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26` | xxviii-4-appeal-812:885 | failed condition | "on production of the certificate" | NOTHING |
| `s 827(3) the justice may commit the defaulter to imprisonment by warrant in Form 26` | xxviii-4-appeal-812:886 | failed condition | "unless the amount of the costs ... are sooner paid" | NOTHING |
| `s 827(3) the term of imprisonment does not exceed one month` | xxviii-4-appeal-812:896 | stated limit or flat negative | "a term not exceeding one month" | NOTHING |
| `s 828(2) the summary conviction court or a justice may issue a warrant of committal as if no appeal had been taken` | xxviii-4-appeal-812:932 | failed condition | "Where an appeal taken against a conviction or order adjudging payment of a sum of money is dismissed" | NOTHING |
| `s 828(3) the clerk of the appeal court is required to send the document to the justice` | xxviii-4-appeal-812:958 | failed condition | "except the notice of intention to appeal" | NOTHING |
| `s 828(3) the clerk of the appeal court is required to send the document to the justice` | xxviii-4-appeal-812:959 | failed condition | "except ... any undertaking" | NOTHING |
| `s 828(3) the clerk of the appeal court is required to send the document to the justice` | xxviii-4-appeal-812:960 | failed condition | "except ... release order" | NOTHING |
| `s 828(3) the clerk of the appeal court is required to send the document to the justice` | xxviii-4-appeal-812:961 | failed condition | "except ... recognizance" | NOTHING |
| `s 828(3) the clerk of the appeal court is required to send the document to the justice` | xxviii-4-appeal-812:963 | failed condition | "When a conviction or order that has been made by an appeal court is to be enforced by a justice" | NOTHING |
| `s 830(2) the appeal is required to be based on a transcript of the proceedings appealed from` | xxviii-5-appeal-829:85 | failed condition | "unless the appellant files with the appeal court, within fifteen days of the filing of the notice of appeal, a statement of facts agreed to in writing" | NOTHING |
| `s 830(3) the notice of appeal is served and filed within thirty days after the date of the decision` | xxviii-5-appeal-829:100 | stated limit or flat negative | "within thirty days after the date of the conviction, judgment or verdict of acquittal or other final order or determination" | NOTHING |
| `s 831 the appeal court is required to give such directions as it thinks necessary for expediting the hearing of the appeal` | xxviii-5-appeal-829:140 | failed condition | "on receiving an application ... the appeal court shall, after giving the prosecutor a reasonable opportunity to be heard" | NOTHING |
| `s 833 a writ of certiorari or other writ is required to remove the conviction, judgment, verdict or other final order or determination` | xxviii-5-appeal-829:182 | stated limit or flat negative | "No writ of certiorari or other writ is required" | NOTHING |
| `s 834(1) the appeal court is required to hear and determine the grounds of appeal` | xxviii-5-appeal-829:197 | failed condition | "When a notice of appeal is filed pursuant to section 830" | NOTHING |
| `s 834(1) the appeal court may take the course` | xxviii-5-appeal-829:216 | failed condition | "When a notice of appeal is filed pursuant to section 830" | NOTHING |
| `s 834(2) the authority and jurisdiction may be exercised by a judge of the court sitting in chambers` | xxviii-5-appeal-829:228 | failed condition | "Where the authority and jurisdiction of the appeal court may be exercised by a judge of that court" | NOTHING |
| `s 835(1) the summary conviction court or a justice has the same authority to enforce the conviction, order or determination as if no appeal had been taken` | xxviii-5-appeal-829:242 | failed condition | "Where the appeal court renders its decision on an appeal" | NOTHING |
| `s 839(1) the named decision may be appealed` | xxviii-5-appeal-829:339 | failed condition | "except where that court is the court of appeal" | NOTHING |
| `s 840(1) the fee or allowance may be taken or allowed in proceedings before summary conviction courts and justices` | xxviii-5-appeal-829:416 | failed condition | "Subject to subsection (2) ... shall not be taken or allowed" | NOTHING |
| `s 840(2) the lieutenant governor in council may fix other fees and allowances to be taken or allowed instead` | xxviii-5-appeal-829:440 | failed condition | "when the lieutenant governor in council so orders" | NOTHING |
| `s 841 data` | xxviii-6-part-xxviii:32 | a closed definition ("means") | "data means representations of information or concepts, in any form" | NOTHING |
| `s 843(2) the filing is complete` | xxviii-6-part-xxviii:88 | failed condition | "If a document is required to be filed in a court and the filing is done by transfer of data by electronic means" | NOTHING |
| `s 843(2) the filing is complete` | xxviii-6-part-xxviii:89 | failed condition | "the filing is complete when the transfer is accepted by the court" | NOTHING |
| `s 847 the person is entitled to obtain a printed copy of the electronic document from the court` | xxviii-6-part-xxviii:151 | failed condition | "on payment of a reasonable fee determined in accordance with a tariff of fees" | NOTHING |
| `s 849(2) the justice is required to attach or affix a seal` | xxviii-6-part-xxviii:175 | stated limit or flat negative | "No justice is required to attach or affix a seal" | NOTHING |
| `sch XXVII note after item 5 a further subpoena may be issued on behalf of the party in the proceeding` | xxviii-7-schedules:520 | failed condition | "Only one subpoena may be issued on behalf of a party in any proceeding, unless ..." | NOTHING |
| `sch XXVII item 10 the fee applies` | xxviii-7-schedules:538 | failed condition | "Where hearing lasts more than two hours" | NOTHING |
| `sch XXVII item 11 each justice is entitled to the fee authorized by item 9` | xxviii-7-schedules:548 | failed condition | "Where two or more justices hear and determine a proceeding" | NOTHING |
| `sch XXVII note after item 15 the item may be charged` | xxviii-7-schedules:560 | stated limit or flat negative | "Items 14 and 15 may be charged only where there has been an adjudication" | NOTHING |
| `sch XXVII note after item 20 reasonable costs of transportation may be allowed` | xxviii-7-schedules:573 | failed condition | "Where a public conveyance is not used" | NOTHING |
| `sch XXVII note after item 23 a charge may be made under item 23 in respect of the service` | xxviii-7-schedules:583 | stated limit or flat negative | "No charge may be made under this item in respect of a service for which a charge is made under item 22" | NOTHING |
| `sch XXVII item 22 the fee applies` | xxviii-7-schedules:593 | failed condition | "if the journey is of necessity over a route different from that taken by the peace officer to make the arrest" | NOTHING |


### The name test: each function that answers NOTHING where a plain reading would answer JUST FALSE (reading (a) is the other reading)

Each row is one fork line of the ruling of 2026-11-12: the function is named for a grant or a power, its "if" gate failing answers `NOTHING`, and the other reading is `JUST FALSE` (a failed "if" read as the text's own no).

| function | gate | fork |
| --- | --- | --- |
| `s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order` | flipped to NOTHING; gate "If ... is authorized by law, but the law does not provide" (fork F-787-2) | F-787-2 |
| `s 800(2) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await the defendant's appearance` | flipped to NOTHING; gate "if it thinks fit" (fork F-800-2) | F-800-2 |
| `s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant` | flipped to NOTHING; gate "If a defendant ... does not appear" (fork F-803-2) | F-803-2 |
| `s 803(2)(b) the summary conviction court may issue a warrant in Form 7 for the arrest of the defendant and adjourn the trial to await their appearance under the warrant` | flipped to NOTHING; gate "If a defendant ... does not appear" and "if it thinks fit" (fork F-803-2) | F-803-2 |
| `s 808(1) the summary conviction court may draw up an order of dismissal` | listed, where/when/upon kind AND flipped (F-808-1): the "Where the summary conviction court dismisses an information" gate answers JUST FALSE; the "if requested by the defendant" gate answers NOTHING | F-808-1 |
| `s 810(1) an information may be laid before a justice` | flipped to NOTHING; relative-clause gate "any person who fears on reasonable grounds" (fork F-810-1) | F-810-1 |
| `s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810-3) | F-810-3 |
| `s 810(3.01) the justice or court may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810-3.01) | F-810-3.01 |
| `s 810.01(1) the person may lay an information before a provincial court judge` | flipped to NOTHING; relative-clause gate and "with the Attorney General's consent" (fork F-810.01-1) | F-810.01-1 |
| `s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.01-3) | F-810.01-3 |
| `s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.01-3.1) | F-810.01-3.1 |
| `s 810.01(4) the provincial court judge may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.01-4) | F-810.01-4 |
| `s 810.011(1) the person may lay an information before a provincial court judge` | flipped to NOTHING; relative-clause gate and "with the Attorney General's consent" (fork F-810.011-1) | F-810.011-1 |
| `s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.011-3) | F-810.011-3 |
| `s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.011-4) | F-810.011-4 |
| `s 810.011(5) the provincial court judge may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.011-5) | F-810.011-5 |
| `s 810.02(1) the person may lay an information before a provincial court judge` | flipped to NOTHING; relative-clause gate "A person who fears on reasonable grounds" (fork F-810.02-1) | F-810.02-1 |
| `s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.02-3) | F-810.02-3 |
| `s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.02-4) | F-810.02-4 |
| `s 810.02(5) the provincial court judge may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.02-5) | F-810.02-5 |
| `s 810.03(1) the person may lay an information before a justice` | flipped to NOTHING; relative-clause gate "Any person who fears on reasonable grounds" (fork F-810.03-1) | F-810.03-1 |
| `s 810.03(3) the justice may order the defendant to enter into a recognizance` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.03-3) | F-810.03-3 |
| `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the justice is also satisfied" (fork F-810.03-4) | F-810.03-4, F-810.03-4b |
| `s 810.03(5) the justice may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.03-5) | F-810.03-5 |
| `s 810.1(1) the person may lay an information before a provincial court judge` | flipped to NOTHING; relative-clause gate "Any person who fears on reasonable grounds" (fork F-810.1-1) | F-810.1-1 |
| `s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.1-3) | F-810.1-3 |
| `s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.1-3.01) | F-810.1-3.01 |
| `s 810.1(3.1) the provincial court judge may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.1-3.1) | F-810.1-3.1 |
| `s 810.2(1) the person may lay an information before a provincial court judge` | flipped to NOTHING; relative-clause gate and "with the consent of the Attorney General" (fork F-810.2-1) | F-810.2-1 |
| `s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance` | flipped to NOTHING; gate "If ... is satisfied" (fork F-810.2-3) | F-810.2-3 |
| `s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period` | flipped to NOTHING; gate "if the provincial court judge is also satisfied" (fork F-810.2-3.1) | F-810.2-3.1 |
| `s 810.2(4) the provincial court judge may commit the defendant to prison` | flipped to NOTHING; gate "if the defendant fails or refuses" (fork F-810.2-4) | F-810.2-4 |
| `s 810.21(1) a provincial court judge may order that the defendant appear by audioconference or videoconference` | flipped to NOTHING AND listed, where/when/upon kind (F-810.21-1): "If a defendant is required to appear" answers NOTHING; "on application of the prosecutor" answers JUST FALSE | F-810.21-1 |
| `s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division` | flipped to NOTHING AND listed, where/when/upon kind (F-810.22-1): "If a person who is bound ... becomes a resident ..." answers NOTHING; "on application of a peace officer or the Attorney General" ans | F-810.22-1 |
| `s 810.22(3) the powers of the judge in relation to the order may be exercised by another judge of the same court` | flipped to NOTHING; gate "If the judge ... is for any reason unable to act" (fork F-810.22-3) | F-810.22-3 |
| `s 810.4(3) the results may be disclosed or used` | flipped to NOTHING; gate "if the results are made anonymous" for the research limb (fork F-810.4-3) | F-810.4-3 |
| `s 811.1(4) the party may require the attendance of the analyst for cross-examination` | flipped to NOTHING; gates "If a certificate of an analyst is produced against a party" and "with leave of the court" (fork F-811.1-4) | F-811.1-4 |
| `s 818(2)(b) the appeal court may allow the application, vacate the order made by the justice and make the order that it considers should have been made` | flipped to NOTHING; gate "if the person applying for the review shows cause" (fork F-818-2b) | F-818-2b |
| `s 822(4) the appeal court may order that the appeal be heard by way of trial de novo` | flipped to NOTHING AND listed, where/when/upon kind (F-822-4): "if an appeal is taken under section 813 and ... is of the opinion" answers NOTHING; "on application of the defendant, the informant, the | F-822-4 |
| `s 822(5) the appeal court may permit the evidence of the witness taken before the summary conviction court to be read` | flipped to NOTHING; gates "if that evidence has been authenticated" and "if (a), (b) or (c)" (fork F-822-5) | F-822-5 |
| `s 832(1) the appeal court may take the course` | flipped to NOTHING; gates "If a notice of appeal is filed under section 830" and "if the defendant is the appellant" (fork F-832-1) | F-832-1 |
| `s 839(1) an appeal to the court of appeal may be taken against the decision` | flipped to NOTHING; gates "on any ground that involves a question of law alone" and "with leave of that court or a judge thereof" (fork F-839-1); the "except where that court is the court of appeal" l | F-839-1 |
| `s 839(1.1) an appeal to the Court of Appeal of Nunavut may be taken against the decision` | flipped to NOTHING; gates "with leave of that court or a judge of that court" and "on any ground that involves a question of law alone" (fork F-839-1.1) | F-839-1.1 |
| `s 842 a court may create, collect, receive, store, transfer, distribute, publish or otherwise deal with electronic documents` | flipped to NOTHING; gate "if it does so in accordance with an Act or with the rules of court" (fork F-842) | F-842 |
| `s 843(1) a court may accept the transfer of data by electronic means` | flipped to NOTHING; gate "if the transfer is made in accordance with the laws of the place where the transfer originates or the laws of the place where the data is received" (fork F-843-1) | F-843-1 |
| `s 845 the court may accept a signature in an electronic document` | flipped to NOTHING; gates "If this Act requires a document to be signed" and "if the signature is made in accordance with an Act or the rules of court" (fork F-845) | F-845 |
| `s 846 the court may accept the information, affidavit, solemn declaration or statement in the form of an electronic document` | flipped to NOTHING; gates "If under this Act an information ... is to be made" and "if (a), (b) and (c)" (fork F-846) | F-846 |

Branches resting on reading (a): 192 (listed above).
Branches resting on reading (b) ("limited by its own wording"): 204.

### Assumptions that are not forks of the text (assumed, not ruled)

- **M-1: the custodian.** Sections 816(1.1) and 819(1) speak of "the person having the custody of the appellant"; the text names no office, so the regulative rules use the core party `the keeper of a prison`.
- **M-2: "immediately" and "forthwith"** are `WITHIN 0` days in the regulative rules of sections 816(1.1) ("immediately release"), 817(1) ("immediately after filing") and 819(1) ("forthwith on the expiration").
- **M-3: plain facts in the seat.** The seat layer asks a `MAYBE BOOLEAN` seam of layer 1 (the answers of section 2 "organization", section 785 "proceedings", section 810.4(3) and section 3.01) as a yes-or-no fact and passes it as `JUST` of that answer; the seat cannot state "not covered".
- **M-4: the justice's satisfaction** ("if the justice is satisfied by the evidence adduced that the informant has reasonable grounds for the fear") is a plain input in every peace-bond section: the text hands the judgment to the justice, and the encoding never guesses it.
- **M-5: dates.** The 12-month limit of section 786(2) is date arithmetic on `Date day month year` (`add months`), tested on both sides of the last day, including the 29 February case (`ccc29-tests-xxvii-a.l4` lines 120-121); the last days of sections 819(1) and 830(3) are the day of the event `PLUS 30`.

### Reading a result: FALSE and NOTHING (ccc29)

Every function of this part answers `MAYBE BOOLEAN` (or `MAYBE NUMBER`) unless it returns a value that has only one answer (a date, a punishment).
`JUST TRUE` is a yes the text gives.
`JUST FALSE` is a no the text gives in its own words: a stated maximum ("not more than $5,000", "not more than 12 months"), a flat negative ("No proceedings shall be instituted", "may not appear by agent"), an "unless" or "except" ("unless the prosecutor and the defendant so agree"), or a "where" or "when" condition that the section itself states and that is not met (listed, not flipped: see the fork register).
`NOTHING` is "the text does not answer on these facts": the case falls outside what the section grants or bars in its own wording (a power whose "if" is not satisfied, a list the text does not close, a rule that applies "to an appeal under section 813" and the case is not one), the text is silent, or it points outside the sources (a regulation, the rules of court, a power or an Act that is not among them).
In this part a "no" is therefore a question answered by the text: a recognizance is longer than 12 months; a fine is more than $5,000; the proceedings were instituted more than 12 months after the subject matter arose and nobody agreed.
"Not covered" is an `NOTHING`: a justice who is not satisfied has not been given the power to order a recognizance, and the function does not say the justice may not.
A caller must never turn `NOTHING` into `FALSE`.
The comments `-- FALSE-kind (the text says no in its own words): "<quote>"` and `-- NOTHING-kind (<why>)` on every branch say which kind it is and why; `check.sh` does not read them, and the lint in "What check.sh prints" does.

## Seams (ccc29)

Seams are taken as inputs; this part never recomputes another part's answer.

### Seams this part asks (PLAN section 6)

| asking section | answering section | the input | type | taken in |
| --- | --- | --- | --- | --- |
| s 810.03(4) | keel s 3.01(1), (2)(f) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN | `s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period`; text: section 3.01(2)(f) lists subsection 810.03(4) (paragraph (f) is at line 271 of `inputs/R.S.C.-1985-c.-C-46.txt`); fork F-810.03-4b |
| s 811.1(2), (4) | ccc11 s 320.11 | `s 320.11 the person is an analyst` | MAYBE BOOLEAN | `s 811.1(2) analyst` |
| s 788(1) | this part s 785 "proceedings" | `the proceedings are proceedings under this Part, by s 785 proceedings` | MAYBE BOOLEAN | `s 788(1) the proceedings are required to be commenced by laying an information in Form 2` (an answer of this part's own module, taken as an input so that the seat can ask it as a plain fact) |
| s 802.1 | keel s 2 "organization" | `s 2 organization` | MAYBE BOOLEAN | `s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent`; a NOTHING input gives NOTHING unless an exception already gives JUST FALSE (tested) |
| s 800(3) | keel s 2 "organization" | `s 2 organization` | MAYBE BOOLEAN | `s 800(3) the organization is required to appear by counsel or agent` |
| s 810.4(2) | this part s 810.4(3) | `the use or disclosure is one that subsection (3) allows, by s 810.4(3) the results may be disclosed or used` | MAYBE BOOLEAN | `s 810.4(2) the use or disclosure of the results of the analysis is barred` |

Seams other parts ask of this part (PLAN section 6):

| asked by | the input name there | this part's function | type |
| --- | --- | --- | --- |
| ccc25: ss 715.32(2), 715.43(2) and (3) | `Schedule to Part XXII.1 the offence is listed` | `sch XXII.1 the offence is listed` (takes the record `sch XXII.1 offence`: the provision, and whether the offence is under section 3 or section 4 of the Corruption of Foreign Public Officials Act; for a conspiracy, an attempt, an accessory after the fact or a counselling, the record is the offence it relates to: paragraph 3) | MAYBE BOOLEAN |
| ccc2 to ccc13: "punishable on summary conviction" with no penalty stated | `s 787(1) the general penalty for an offence punishable on summary conviction` | `s 787(1) the general penalty as stated in section 787(1)` | `Punishment` |

The function that answers it is named `s 787(1) the general penalty as stated in section 787(1)`: it was renamed at assembly (2026-11-17) to avoid a collision with the seat input of the same name in ccc10 and the layer-1 inputs of other parts (`check/ambiguous-identifier` in the merged module); the rename is assumed, not ruled, and the name other parts ask for is unchanged, so the lead binds their input to this function at the merge.

A seam this part found that the plan lacks: section 811(a) and (b) name no penalty for limb (b), so the general penalty of section 787(1) applies unless the law otherwise provides (`s 811(b) the punishment on summary conviction` returns it, fork F-811-b); section 810.4(4) is the same (fork F-810.4-4).
The Schedule to Part XXV (section 762) is asked by whichever part holds section 762; this part provides `sch XXV the rows of the province or territory`, `sch XXV column II the court of the row` and `sch XXV column III the officer of the row`.

## Findings (ccc29): what the text turns out to say

1. Items 3 and 4 of the schedule to Part XXVII carry the same words and the same amount ("Warrant where summons issued in first instance $ 0.30", lines 17412 and 17413); both are encoded as written.
2. Section 812(1) has three consecutive repealed paragraphs, (e), (f) and (g), repealed in 1992, 2015 and 2026 (lines 17125-17127: "[Repealed, 2026, c. 11, s. 45]"); the consolidation therefore includes a 2026 amendment.
3. Section 811 names no penalty for limb (b), and section 810.4(4) names none; both rest on the general penalty of section 787(1) ("Unless otherwise provided by law"), which this part returns under the name other parts ask for.
4. Section 802.1 bars an agent only where the defendant is liable on summary conviction to more than six months' imprisonment, and then lists three exceptions (an organization, an adjournment request, an agent authorized by a provincial program); the first exception turns on the section 2 definition of organization, taken as an input.
5. Section 3.01(2)(f) lists subsection 810.03(4), so "an offence in the commission of which violence was used, threatened or attempted" in that subsection includes the offences section 3.01(1) lists (an offence of a sexual nature or committed for a sexual purpose, criminal harassment under section 264, trafficking in persons under section 279.01, trafficking of a person under the age of 18 years under section 279.011); the section 3.01 answer is an input.
6. Section 822(7)(a) bars judgment for the appellant on an objection to an information or process unless BOTH that the objection was taken at the trial AND that an adjournment was refused although the variance had deceived or misled the appellant are shown (fork F-822-7).
7. The schedule to Part XXV has two rows each for Ontario and British Columbia (lines 17391-17392 and 17396-17397); the second row has no entry in Column I and continues the province above it.
8. The schedule to Part XX.1 is shown repealed ("[Repealed, 2005, c. 22, s. 37]", line 17349); section 848 and section 823 are repealed.
9. The editorial note of section 849 (line 17346) says the forms are at the end of the Act; the Forms begin at line 17451 and are another part's.
10. Section 839(1)(b) excludes a decision of an appeal court that is the court of appeal; the function answers `JUST FALSE` for that limb because the text closes it with "except where".
11. Part XXVII is sections 785 to 840 and Part XXVIII begins at line 17313 with section 841 at line 17317, so the lead-in "In this Part," of section 785 covers sections 785 to 840 only.
12. Section 810.21(1) says "any of sections 83.3 and 810 to 810.2"; read in the Code's order the range takes in 810.01, 810.011, 810.02, 810.03 and 810.1 (fork F-810.21-1).

### What the text does not answer

- The period for giving notice of appeal (s 815(1)) and for the other time limits "directed by the rules of court": an input.
- The period within which samples are to be destroyed (s 810.3(4)): "prescribed by regulation", outside the sources; no deadline is encoded.
- The office of "the person having the custody of the appellant" (ss 816(1.1), 819(1)): no office is named (M-1).
- When the Attorney General of Canada's annual report under s 810.011(15) is due: "each year" is the only time given (F-810.011-15).
- Whether section 810.4(4) and section 811(b) carry any penalty other than the general one (F-810.4-4, F-811-b).
- Whether the sections that say "within thirty days" count the day of the event (F-819-1).

## What the stable binary does not accept (ccc29)

The brief states the limits of the stable build (1.6.110 and 1.6.109); this part worked inside them and did not re-measure them.
What follows is what this part met, each item checked against the files of the deposit on 2026-11-17.

- **`parse/indentation` on an `ELSE CONSIDER` in section 839(1)**; the cause was not isolated (section 813 has an `IF ... ELSE CONSIDER ...` and compiles on both builds, so the failure was something about that shape, not `ELSE CONSIDER` alone).
  Fix used: a `BRANCH`, with the decision test and the appeal test written as two helper functions, `s 839(1) the decision is one named` and `s 839(1) the named decision may be appealed`.
- **`REFUSE` and `#ASSERT REFUSED` do not exist** (the brief says so): "not covered" is `NOTHING` throughout, asserted with `EQUALS NOTHING` (for example `ccc29-tests-xxvii-b.l4` line 110).
- **Regulative rules are run, not asserted.**
  Every regulative rule of this part is exercised with `#TRACE`, one event per line, and the outcome (`FULFILLED`, `BREACH` or a residual obligation) is read from the output; `check.sh` counts assertions only and says so in its own header (lines 29-32 of `check.sh`: a trace outcome is compared by hand).
  Every regulative rule also has a decision function over the same facts, and those are asserted.
  Where a consequence needs its own deadline or party, `HENCE` names a separate `DEONTIC` rule (the rules named after `HENCE` are those of ss 810(3.1), 810.01(5), 810.02(7), 810.03(7), 810.1(3.03) and (3.05), 810.2(5) and (6), 817(1), 819(2) and 821(1)).
- **A `#ASSERT` is one line** (the brief says so): the longest of this part, in `ccc29-tests-xxviii-7-schedules.l4`, is 379 characters.
- **Every `NOT` is parenthesised** (the brief says so).
- **No name is defined in more than one file of the part**: a script over the 25 `ccc29-` files found none, so the "name defined in two imported modules" limit never applied.
- **`JL4_LIBRARY_PATH` was left unset on both builds**, as the brief asks, for the `#TRACE` comparison.

## Seat-question audit (ccc29)

The seat layer has 74 questions.
**First audit** (direction: each title read against the name of the function it calls, as the brief asks): 0 mismatches.
Every one of the 74 titles restates its function's own name, differing only by the person ("I", "me" for "the defendant"), the form of the question ("is", "may", "what is"), word order, or "is not more than" against "does not exceed" (ss 810.1(3) and 810.2(3)); every bar is titled as a bar and every grant as a grant.

**Second audit** (each title read against the BODY of the function, branch by branch, on 2026-11-17, against the four criteria of `seat-audit-second-pass.md`): 74 questions read; 1 retitled; 14 read and left, listed below with a reason; the other 59 agree on limb, premise, modal and answer type without a note.

Retitled (criterion 1: the title named one appellant, "I", where the body answers for each kind of appellant the input names, with the decision tested as well):

| function | was | now |
| --- | --- | --- |
| `s 813 the person may appeal to the appeal court` | `Under section 813, may I appeal to the appeal court?` | `Under section 813, may the appellant (the defendant, the informant or the Attorney General) appeal to the appeal court against the decision?` |

The cases file of the seat is generated from the layer-1 function a question calls, so its cases carry the new name; no assertion broke and none was restated.

Read, left (14):

- Q1 `Under section 786(2), are the proceedings barred because they were instituted more than 12 months after the subject matter arose?`: the title carries "because they were instituted more than 12 months after the subject matter arose"; the body computes exactly that (an instituted date against the day the 12 months end) and the function's own name says it.
- Q9 `Under section 794(1), need the information not set out or negative the exception, exemption, proviso, excuse or qualification?`: a double negative ("need not ... not set out"); wording only, and it restates the function's own name; the body answers JUST TRUE when the matter is one prescribed by law.
- Q12 `Under section 801(1)(a), am I required to be asked whether I plead guilty or not guilty to the information?`: the title omits the gate "where the defendant appears for the trial"; the body tests it (and the summary-conviction limb), so the title carries no premise the function does not compute.
- Q17 `Under section 803(4), may the summary conviction court dismiss the information with or without costs?`: the title omits the gate "the prosecutor does not appear at the resumption of an adjourned trial"; the body tests it, and the function's own name carries the same words.
- Q40 `Under section 810.03(4), may the justice order that I enter into the recognizance for a longer period?`: the title omits the violence and victim premises of s 810.03(4); the body tests them and the s 3.01 seam; the function's own name carries the same words.
- Q52 `Under section 811, am I guilty of an offence?`: "am I guilty of an offence" is scoped by "Under section 811"; the body answers three ways (NOTHING outside the sections named, JUST TRUE for a breach, JUST FALSE otherwise) and the title restates the function's own name; JUST FALSE reads as "not guilty of the section 811 offence".
- Q55 `Under section 815(1), am I, as an appellant, required to give notice of appeal?`: "as an appellant" is a status the body tests as a separate input; the function's own name carries "the appellant is required".
- Q58 `Under section 816(1), am I, as an appellant, required to remain in custody?`: "as an appellant" is a status the body tests (the defendant before a summary conviction court, an appellant under s 813); the function's own name carries "the appellant is required to remain in custody".
- Q60 `Under section 820(1), do I waive my right of appeal under section 813 by paying the fine?`: the body can answer only JUST FALSE (the text says a person "does not waive") or NOTHING, never JUST TRUE; the title restates the function's own name and the "by reason only" limb is a premise the body computes.
- Q63 `Under section 830(1), may I appeal against the decision on the ground?`: "may I appeal" over a body that also tests that the person is a party or the Attorney General; the function's own name carries "the person may appeal".
- Q64 `Under section 830(2), is the appeal required to be based on a transcript of the proceedings appealed from?`: the body answers JUST TRUE unless the statement-of-facts route is shown (JUST FALSE), so the title asks the duty and the body answers the duty; it restates the function's own name.
- Q68 `Under section 837, does no appeal under section 830 lie from the conviction or order?`: a double negative ("does no appeal ... lie"); the body answers JUST TRUE where the law provides no appeal lies, otherwise NOTHING; it restates the function's own name and s 837.
- Q69 `Under section 839(1), may an appeal to the court of appeal be taken against the decision?`: the body tests three gates (a question of law alone, leave, a named decision) in a BRANCH, each failing to NOTHING; the title asks the section's one question and restates the function's own name.
- Q74 `Under schedule XXVII, what is the amount in dollars stated in the row of the item?`: a value question: the body returns the amount of the item, NOTHING for item 11 which states none; the type of the answer (a number) matches the title's "what is".

All 74 seat questions, in order:


**Summary conviction proceedings: the time limit and the general penalty (sections 786 and 787)**

- Under section 786(2), are the proceedings barred because they were instituted more than 12 months after the subject matter arose? (`s 786(2) the proceedings are barred because they were instituted more than 12 months after the subject matter arose`)
- Under section 786(2), on what day do the 12 months end? (`s 786(2) the day on which the 12 months end`)
- Under section 787(1), does the general penalty apply to the offence? (`s 787(1) the general penalty applies to the offence`)
- Under section 787(1), is the fine not more than $5,000? (`s 787(1) the fine is not more than $5,000`)
- Under section 787(1), is the term of imprisonment not more than two years less a day? (`s 787(1) the term of imprisonment is not more than two years less a day`)
- Under section 787(2), may the court order imprisonment in default of payment of the fine or compliance with the order? (`s 787(2) the court may order imprisonment in default of payment of the fine or compliance with the order`)

**The information and the trial (sections 788 to 809)**

- Under section 788(1), are the proceedings required to be commenced by laying an information in Form 2? (`s 788(1) the proceedings are required to be commenced by laying an information in Form 2`)
- Under section 789(2), is the information barred from containing any reference to previous convictions? (`s 789(2) the information is barred from containing any reference to previous convictions`)
- Under section 794(1), need the information not set out or negative the exception, exemption, proviso, excuse or qualification? (`s 794(1) the information need not set out or negative the exception, exemption, proviso, excuse or qualification`)
- Under section 800(2), may I appear in the way I propose? (`s 800(2) a defendant may appear in the way`)
- Under section 800(2), may the summary conviction court require me to appear personally? (`s 800(2) the summary conviction court may require the defendant to appear personally`)
- Under section 801(1)(a), am I required to be asked whether I plead guilty or not guilty to the information? (`s 801(1)(a) the defendant is required to be asked whether they plead guilty or not guilty to the information`)
- Under section 802(1), am I entitled to make full answer and defence? (`s 802(1) the defendant is entitled to make full answer and defence`)
- Under section 802(2), may I examine and cross-examine witnesses in the way I propose? (`s 802(2) the prosecutor or defendant may examine and cross-examine witnesses in the way`)
- Under section 802.1, am I barred from appearing or examining or cross-examining witnesses by agent? (`s 802.1 the defendant is barred from appearing or examining or cross-examining witnesses by agent`)
- Under section 803(2)(a), may the summary conviction court proceed ex parte to hear and determine the proceedings in my absence? (`s 803(2)(a) the summary conviction court may proceed ex parte to hear and determine the proceedings in the absence of the defendant`)
- Under section 803(4), may the summary conviction court dismiss the information with or without costs? (`s 803(4) the summary conviction court may dismiss the information with or without costs`)
- Under section 808(2), is the certified copy of the order of dismissal a bar to the subsequent proceedings? (`s 808(2) the certified copy of the order of dismissal is a bar to the subsequent proceedings`)
- Under section 809(1)(a), may the summary conviction court award costs to be paid by me to the informant? (`s 809(1)(a) the summary conviction court may award costs to be paid to the informant by the defendant`)
- Under section 809(3), what is the amount for which I am liable to serve the term of imprisonment imposed in default of payment? (`s 809(3) the amount for which the defendant is liable to serve the term of imprisonment imposed in default of payment`)
- Under section 809(4), is the person who is liable to pay the costs, in default of payment, liable to imprisonment for one month? (`s 809(4) the person who is liable to pay the costs is, in default of payment, liable to imprisonment for one month`)

**Peace bonds and recognizances (sections 810 to 811.1)**

- Under section 810(3), may the justice or court order that I enter into a recognizance, with or without sureties? (`s 810(3) the justice or court may order that the defendant enter into a recognizance, with or without sureties`)
- Under section 810(3), is the period of the recognizance not more than 12 months? (`s 810(3) the period of the recognizance is not more than 12 months`)
- Under section 810(3.01), may the justice or court commit me to prison? (`s 810(3.01) the justice or court may commit the defendant to prison`)
- Under section 810.01(3), may the provincial court judge order that I enter into a recognizance? (`s 810.01(3) the provincial court judge may order that the defendant enter into a recognizance`)
- Under section 810.01(3), is the period of the recognizance not more than 12 months? (`s 810.01(3) the period of the recognizance is not more than 12 months`)
- Under section 810.01(4), may the provincial court judge commit me to prison? (`s 810.01(4) the provincial court judge may commit the defendant to prison`)
- Under section 810.01(3.1), may the provincial court judge order that I enter into the recognizance for a longer period? (`s 810.01(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period`)
- Under section 810.011(3), may the provincial court judge order that I enter into a recognizance, with or without sureties? (`s 810.011(3) the provincial court judge may order that the defendant enter into a recognizance, with or without sureties`)
- Under section 810.011(3), is the period of the recognizance not more than 12 months? (`s 810.011(3) the period of the recognizance is not more than 12 months`)
- Under section 810.011(5), may the provincial court judge commit me to prison? (`s 810.011(5) the provincial court judge may commit the defendant to prison`)
- Under section 810.011(4), may the provincial court judge order that I enter into the recognizance for a longer period? (`s 810.011(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period`)
- Under section 810.02(3), may the provincial court judge order that I enter into a recognizance? (`s 810.02(3) the provincial court judge may order that the defendant enter into a recognizance`)
- Under section 810.02(3), is the period of the recognizance not more than 12 months? (`s 810.02(3) the period of the recognizance is not more than 12 months`)
- Under section 810.02(5), may the provincial court judge commit me to prison? (`s 810.02(5) the provincial court judge may commit the defendant to prison`)
- Under section 810.02(4), may the provincial court judge order that I enter into the recognizance for a longer period? (`s 810.02(4) the provincial court judge may order that the defendant enter into the recognizance for a longer period`)
- Under section 810.03(3), may the justice order me to enter into a recognizance? (`s 810.03(3) the justice may order the defendant to enter into a recognizance`)
- Under section 810.03(3), is the period of the recognizance not more than 12 months? (`s 810.03(3) the period of the recognizance is not more than 12 months`)
- Under section 810.03(5), may the justice commit me to prison? (`s 810.03(5) the justice may commit the defendant to prison`)
- Under section 810.03(4), may the justice order that I enter into the recognizance for a longer period? (`s 810.03(4) the justice may order the defendant to enter into the recognizance for a longer period`)
- Under section 810.1(3), may the provincial court judge order that I enter into a recognizance? (`s 810.1(3) the provincial court judge may order that the defendant enter into a recognizance`)
- Under section 810.1(3), is the period of the recognizance not more than 12 months? (`s 810.1(3) the period of the recognizance does not exceed 12 months`)
- Under section 810.1(3.1), may the provincial court judge commit me to prison? (`s 810.1(3.1) the provincial court judge may commit the defendant to prison`)
- Under section 810.1(3.01), may the provincial court judge order that I enter into the recognizance for a longer period? (`s 810.1(3.01) the provincial court judge may order that the defendant enter into the recognizance for a longer period`)
- Under section 810.2(3), may the provincial court judge order that I enter into a recognizance? (`s 810.2(3) the provincial court judge may order that the defendant enter into a recognizance`)
- Under section 810.2(3), is the period of the recognizance not more than 12 months? (`s 810.2(3) the period of the recognizance does not exceed 12 months`)
- Under section 810.2(4), may the provincial court judge commit me to prison? (`s 810.2(4) the provincial court judge may commit the defendant to prison`)
- Under section 810.2(3.1), may the provincial court judge order that I enter into the recognizance for a longer period? (`s 810.2(3.1) the provincial court judge may order that the defendant enter into the recognizance for a longer period`)
- Under section 810.22(1), may a provincial court judge transfer the order to a provincial court judge in the other territorial division? (`s 810.22(1) a provincial court judge may transfer the order to a provincial court judge in the other territorial division`)
- Under section 810.4(1), is the use of the bodily substance barred? (`s 810.4(1) the use of the bodily substance is barred`)
- Under section 810.4(2), is the use or disclosure of the results of the analysis barred? (`s 810.4(2) the use or disclosure of the results of the analysis is barred`)
- Under section 811, am I guilty of an offence? (`s 811 the person is guilty of an offence`)
- Under section 811.1(4), may I require the attendance of the analyst for cross-examination? (`s 811.1(4) the party may require the attendance of the analyst for cross-examination`)

**Appeals in summary conviction matters (sections 812 to 840)**

- Under section 813, may the appellant (the defendant, the informant or the Attorney General) appeal to the appeal court against the decision? (`s 813 the person may appeal to the appeal court`)
- Under section 815(1), am I, as an appellant, required to give notice of appeal? (`s 815(1) the appellant is required to give notice of appeal`)
- Under section 815(1), is the notice of appeal given within the period directed by the rules of court? (`s 815(1) the notice of appeal is given within the period directed by the rules of court`)
- Under section 815(2), may the appeal court or a judge thereof extend the time within which notice of appeal may be given? (`s 815(2) the appeal court or a judge thereof may extend the time within which notice of appeal may be given`)
- Under section 816(1), am I, as an appellant, required to remain in custody? (`s 816(1) the appellant is required to remain in custody`)
- Under section 819(1), on what day do the thirty days expire? (`s 819(1) the day on which the thirty days expire`)
- Under section 820(1), do I waive my right of appeal under section 813 by paying the fine? (`s 820(1) the person waives the right of appeal under section 813 by paying the fine`)
- Under section 822(4), may the appeal court order that the appeal be heard by way of trial de novo? (`s 822(4) the appeal court may order that the appeal be heard by way of trial de novo`)
- Under section 827(3), does the term of imprisonment not exceed one month? (`s 827(3) the term of imprisonment does not exceed one month`)
- Under section 830(1), may I appeal against the decision on the ground? (`s 830(1) the person may appeal against the decision on the ground`)
- Under section 830(2), is the appeal required to be based on a transcript of the proceedings appealed from? (`s 830(2) the appeal is required to be based on a transcript of the proceedings appealed from`)
- Under section 830(3), is the notice of appeal served and filed within thirty days after the date of the decision? (`s 830(3) the notice of appeal is served and filed within thirty days after the date of the decision`)
- Under section 830(3), what is the last day for serving and filing the notice of appeal? (`s 830(3) the last day for serving and filing the notice of appeal`)
- Under section 836, am I taken to have abandoned all my rights of appeal under section 813? (`s 836 the person is taken to have abandoned all rights of appeal under section 813`)
- Under section 837, does no appeal under section 830 lie from the conviction or order? (`s 837 no appeal under section 830 lies from the conviction or order`)
- Under section 839(1), may an appeal to the court of appeal be taken against the decision? (`s 839(1) an appeal to the court of appeal may be taken against the decision`)

**Electronic documents and forms (sections 841 to 849)**

- Under section 843(2), is the filing complete? (`s 843(2) the filing is complete`)
- Under section 847, am I entitled to obtain a printed copy of the electronic document from the court? (`s 847 the person is entitled to obtain a printed copy of the electronic document from the court`)
- Under section 849(1), is the form deemed to be good, valid and sufficient? (`s 849(1) the form is deemed to be good, valid and sufficient`)

**Schedules (schedule XXII.1 and schedule XXVII)**

- Under schedule XXII.1, is the offence listed? (`sch XXII.1 the offence is listed`)
- Under schedule XXVII, what is the amount in dollars stated in the row of the item? (`sch XXVII the amount in dollars stated in the row of the item`)

## What check.sh prints (ccc29)

Run on 2026-11-17 with `L4=<1.6.110 build> L4_MAIN=<1.6.109 build> ./check.sh` (default target `main`; `JL4_LIBRARY_PATH` unset), after the last edit to a `.l4` file.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc29-cases-seat.l4                            0       207       0        0         0 |      0       207       0        0  same
ccc29-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc29-tests-xxvii-a.l4                         0        96       0        0         0 |      0        96       0        0  same
ccc29-tests-xxvii-b.l4                         0       158       0        0         0 |      0       158       0        0  same
ccc29-tests-xxviii-0-peace-810.l4              0       138       0        0         0 |      0       138       0        0  same
ccc29-tests-xxviii-1-peace-810-02.l4           0        87       0        0         0 |      0        87       0        0  same
ccc29-tests-xxviii-2-peace-810-1.l4            0       125       0        0         0 |      0       125       0        0  same
ccc29-tests-xxviii-3-peace-810-21.l4           0       126       0        0         0 |      0       126       0        0  same
ccc29-tests-xxviii-4-appeal-812.l4             0       203       0        0         0 |      0       203       0        0  same
ccc29-tests-xxviii-5-appeal-829.l4             0        96       0        0         0 |      0        96       0        0  same
ccc29-tests-xxviii-6-part-xxviii.l4            0        46       0        0         0 |      0        46       0        0  same
ccc29-tests-xxviii-7-schedules.l4              0       284       0        0         0 |      0       284       0        0  same
ccc29-xxvii-a-interpretation-penalty.l4        0         0       0        0         0 |      0         0       0        0  same
ccc29-xxvii-b-information-trial.l4             0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-0-peace-810.l4                    0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-1-peace-810-02.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-2-peace-810-1.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-3-peace-810-21.l4                 0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-4-appeal-812.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-5-appeal-829.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-6-part-xxviii.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc29-xxviii-7-schedules.l4                    0         0       0        0         0 |      0         0       0        0  same
TOTAL (25 modules)                             0      1566       0        0           |      0      1566       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Baselines it replaced: `TOTAL (3 modules) 0 0 0 0` (the three keel modules alone, before this part wrote anything) and `TOTAL (11 modules) 0 471 0 0 | 0 471 0 0` (the first run of the resumed session, before any edit, on the 11 modules then in the deposit); the run before the last additions was `TOTAL (25 modules) 0 1548 0 0 | 0 1548 0 0`, and the last additions were 18 assertions (module A tests +4, module 1-peace tests +4, schedules tests +6, seat cases +4).

**Lint of the FALSE-kind and NOTHING-kind comments** (a script over the layer-1 modules): lint over the layer-1 modules (work/lint.py): 445 result branches read by script, 192 JUST FALSE (each carrying a FALSE-kind comment with a quotation) and 253 NOTHING (each carrying a NOTHING-kind comment whose reason is one of the six in the brief); 0 branches without a comment, 0 reasons outside the list, and every quoted fragment was found in the text of lines 16684-17450 (0 not found); a line that carries a kind comment without a JUST FALSE or NOTHING result was looked for and none exists.

**#TRACE comparison across the two builds** (`JL4_LIBRARY_PATH` unset on both; both runs produced evaluations): #TRACE directives: 38 in 6 files; evaluations read: 38 on 1.6.110, 38 on 1.6.109; differing outcomes: 0.
Outcomes on 1.6.110: BREACH x3, FULFILLED x35
Outcomes on 1.6.109: BREACH x3, FULFILLED x35

Of the 38 traces, 35 are compliant-path traces (`FULFILLED`) and 3 are breach-path traces (`BREACH`, printed `DEONTIC BREACHED`), all in `ccc29-tests-xxviii-4-appeal-812.l4`: s 816(1.1), s 817(1) (the prosecutor) and s 819(1), each fed its action one day after a `WITHIN 0` deadline.
The other 32 rules cannot be driven to `BREACH`: each is a `MUST` with no `WITHIN` and no `LEST` (the text gives no time), and a probe on s 800(1) on both builds showed that the action fed one hundred days late reads `FULFILLED` and the same action by another party leaves the obligation unmatched, so no breach trace was forced for them: `s 788(1) the informant is to lay an information in Form 2`; `s 800(1) the court is to hold the trial`; `s 804 the court is to decide`; `s 806(2) the court is to issue a warrant of committal`; `s 810(2) the justice is to cause the parties to appear`; `s 810(3.1) the justice or court is to consider the firearms condition`; `s 810(3.11) the justice or court is to specify the manner and method`; `s 810(3.12) the justice or court is to include a statement of reasons in the record`; `s 810(3.2) the justice or court is to consider the supplementary conditions`; `s 810.01(5) the judge is to consider the firearms condition`; `s 810.01(5.1) the judge is to specify how the things and authorizations are to be surrendered`; `s 810.01(5.2) the judge is to include a statement of reasons in the record`; `s 810.011(15) the Attorney General of Canada is to prepare and lay the annual report`; `s 810.02(7) the judge is to consider the firearms condition`; `s 810.02(8) the judge is to specify how the things and authorizations are to be surrendered`; `s 810.03(11) the justice is to consider the safety and security needs`; `s 810.03(4.1) the justice is to consider recommending Indigenous support services`; `s 810.03(7) the justice is to consider the firearms condition`; `s 810.03(8) the justice is to specify how the things and authorizations are to be surrendered`; `s 810.03(9) the justice is to include a statement of reasons in the record`; `s 810.1(3.03) the judge is to consider the firearms condition`; `s 810.1(3.04) the judge is to specify how the things and authorizations are to be surrendered`; `s 810.1(3.05) the judge is to consider the reporting condition`; `s 810.2(5) the judge is to consider the firearms condition`; `s 810.2(5.1) the judge is to specify how the things and authorizations are to be surrendered`; `s 810.2(5.2) the judge is to include a statement of reasons in the record`; `s 810.2(6) the judge is to consider the reporting condition`; `s 810.3(1) the authority is to designate or specify the matter`; `s 810.3(4) the authority is to cause the samples to be destroyed`; `s 815(1) the appellant is to give notice of appeal`; `s 821(1) the clerk is to notify the summary conviction court`; `s 828(3) the clerk of the appeal court is to send the conviction or order to the justice`.

**srcrefs** (`python3 -I srcrefs.py check --refs` and `--strict` over every `.l4` file of the part): python3 -I srcrefs.py check --refs and check --strict over the 25 ccc29-*.l4 files: 731 src: lines, 240 runs, 425 locators, 0 problems (same line in both modes).

## Files (ccc29)

- `ccc29-cases-seat.l4`
- `ccc29-seat.l4`
- `ccc29-tests-xxvii-a.l4`
- `ccc29-tests-xxvii-b.l4`
- `ccc29-tests-xxviii-0-peace-810.l4`
- `ccc29-tests-xxviii-1-peace-810-02.l4`
- `ccc29-tests-xxviii-2-peace-810-1.l4`
- `ccc29-tests-xxviii-3-peace-810-21.l4`
- `ccc29-tests-xxviii-4-appeal-812.l4`
- `ccc29-tests-xxviii-5-appeal-829.l4`
- `ccc29-tests-xxviii-6-part-xxviii.l4`
- `ccc29-tests-xxviii-7-schedules.l4`
- `ccc29-xxvii-a-interpretation-penalty.l4`
- `ccc29-xxvii-b-information-trial.l4`
- `ccc29-xxviii-0-peace-810.l4`
- `ccc29-xxviii-1-peace-810-02.l4`
- `ccc29-xxviii-2-peace-810-1.l4`
- `ccc29-xxviii-3-peace-810-21.l4`
- `ccc29-xxviii-4-appeal-812.l4`
- `ccc29-xxviii-5-appeal-829.l4`
- `ccc29-xxviii-6-part-xxviii.l4`
- `ccc29-xxviii-7-schedules.l4`
- `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`
