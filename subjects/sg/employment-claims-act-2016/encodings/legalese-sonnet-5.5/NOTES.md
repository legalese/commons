# Employment Claims Act 2016 (Singapore): encoding notes

Row: `legalese-sonnet-5.5`, subject `sg/employment-claims-act-2016`, main dialect.
Written 2026-11-05 by one encoder (Sonnet 5.5), with no subagents, from `ECA2016.txt` alone.
Revised the same day to apply two rulings of 2026-11-05 (printed under Forks), to fill the gaps listed under Coverage and Dependencies, and to record the open questions and the judgment calls.

**Status: draft, not reviewed by a lawyer.**
How each claim below was checked is stated where it is made; the checks are these, run on 2026-11-05 and printed in full under "What check.sh prints".

| check | what it covers | result |
| --- | --- | --- |
| `check.sh` | every module, on build 1.6.109 (main 4c887e0) and again on build 1.6.108 (main 2ae7c9b) | 1170 satisfied, 0 failed, 0 refused, 0 errors over 17 modules; the same four counts on build 108 |
| `srcrefs.py check` | every `-- src:` line is a verbatim line of the deposited text, and every `@ref` locator points at lines that exist | srcrefs check: 1560 src: lines, 310 runs, 243 locators, 0 problems |
| `coverage.py` | every non-blank line of the text falls in exactly one coverage row | 585 rows; 0 text lines in no row; 0 in more than one row |
| `kinds.py lint` | every `JUST FALSE` and every `NOTHING` result in layer 1 carries its `FALSE-kind` or `NOTHING-kind` comment | 319 branches (186 JUST FALSE, 133 NOTHING); 0 without a comment; 0 NOTHING comments with no allowed reason; 0 FALSE comments with no quotation; 0 scope-limit NOTHING branches with no ruling tag |
| `jural.py check` | every layer-1 function is matched by a row of the Jural relations table | 244 functions, 111 rows, 145 keys; 0 functions without a row; 0 keys matching no function; 0 functions not named in any test or case |

**The text is a converter rendering and is unofficial.**
`inputs/ECA2016.txt` is a plain-text rendering made by a converter script from the Singapore Statutes Online informal consolidation (2020 Revised Edition, in force from 1 April 2025, retrieved 2026-10-01, as `inputs/SOURCES.md` records).
It is not the official text, and the licence note (`inputs/STUB-SOURCE-LICENSE.md`, "Status of the text (cl.8)") records that Singapore Statutes Online reproduces an unofficial consolidation.
Nothing here is verified against the official text, and nothing here is legal advice.
Page headers, page numbers and amendment notes survive in the rendering, and in at least one place a word is visibly missing (s 19(3), fork F8).

## Seat

**An employee, or a former employee, with a salary-related claim against an employer, asking on facts they can state whether they may bring it to the tribunal, in what time, with what steps and at what cost, and what follows.**

**Why this seat.**
Commons rules (2026-10-18, restated in `inputs/COMMONS-CLAUDE.md`) that every encoding is written from the seat of the individual to whom the law is applied, with decisions phrased as that person would ask them and facts that person could state.
In this Act that individual is the person who has a money dispute with an employer and wants the tribunal to decide it: they are the "claimant" who must first ask the Commissioner for mediation (Part 2) and then lodge a claim (Part 3), and almost every operative section either lets them do something, requires something of them, or says what is done to them.
The other persons the Act addresses (the employer as respondent, the Commissioner, mediators, the tribunal, the courts) are met only through the claimant's questions.

Layer 1 (the modules named below) takes nobody's point of view and follows the Act's own structure.
Layer 2 is two files: `eca-seat.l4`, which asks the questions, and `eca-cases-seat.l4`, which asserts an answer for each.
The seat imports the layer-1 modules and calls their functions.
Each of its 93 questions has `@export`, and every input has an `@desc`, takes plain inputs (yes, no, a number, a date as day, month and year, or a choice from a list), and is a single call into layer 1 with its inputs built by small wiring helpers; no seat question contains a rule of its own (checked by `seatcheck.py`, which also checks that every input has an `@desc` and every question has a case: every `DECIDE` body calls a layer-1 function and contains none of `AND`, `OR`, `NOT`, `IF`, `THEN`, `BRANCH`, `CONSIDER`, `GREATER`, `LESS`, `PLUS`, `MINUS`).
There is no seat for an official (the Commissioner, an approved mediator, the tribunal, a court or a Minister): what an official may or must do is in layer 1, and the person meets it as the answer to a question about their own claim.
No employer seat is written; the Commons rulings of 2026-10-21 make further seats optional.

A fact the person may not know is asked as `Yes / No / I am not sure`, and "I am not sure" becomes `NOTHING`.
A date is asked as day, month and year; any of them given as 0 means "I do not know" and becomes `NOTHING`.
An amount, fee, claim limit or period that regulations, Rules of Court or practice directions set is asked as a number, and 0 means "I do not know".
So a fee that really is nil cannot be stated in the seat (finding 35).

The questions, in the order of the Act:


**Must I ask for mediation first, and by when? (ss 3 and 4)**

1. Must I submit a mediation request before I lodge my claim (s 3(1) and (8))?
2. Does my mediation request cover every dispute my claim will be lodged for (s 3(1))?
3. By what date must I submit my mediation request (s 3(2))?
4. Is my mediation request in time if I submit it on this date (s 3(2))?
5. Must my mediation request list this dispute (s 3(3)(a))?
6. Must my mediation request leave this dispute out because the claim cannot be lodged (s 3(3)(c))?
7. Is the fee I am paying with my mediation request enough (s 3(3)(d))?
8. Can the Commissioner refuse to accept my mediation request (s 3(4)(a))?
9. May the Commissioner waive, remit or refund my mediation fee (s 3(4)(b))?
10. Must the Commissioner refer my dispute to an approved mediator once my request is accepted (s 3(5))?
11. May someone else submit my mediation request for me (s 3(6)(b))?
12. Must the approved mediator hold the first mediation session (s 4(1))?
13. May the mediator decide not to hold any mediation session (s 4(2))?
14. Must my mediation session be held in private (s 4(3))?
15. May the same mediator take my dispute together with others (s 4(4) and (5))?
16. Can this person represent me, or the other side, at the mediation (s 5(1) to (3))?

**Will I get a claim referral certificate? (s 6)**

17. Is my dispute still unresolved (s 6(4))?
18. Must the mediator give me a claim referral certificate for this dispute (s 6(2))?
19. Can the mediator discontinue the mediation and refuse me a certificate because I did not attend (s 6(3))?

**If my dispute settles at mediation (s 7)**

20. Is my settlement agreement in the form the Rules of Court prescribe (s 7(1)(a))?
21. Is the most I can be paid for salary-type disputes in my settlement within the claim limit (s 7(1)(b))?
22. Is the total payable to me for wrongful dismissal in my settlement within the claim limit (s 7(1)(c))?
23. Is my settlement agreement signed as the Act requires (s 7(1)(d))?
24. May a District Court register my settlement agreement (s 7(2))?
25. May a District Court refuse to register my settlement agreement because my application is late (s 7(2))?
26. From what date does my registered settlement agreement have the force of a judgment (s 7(3)(a))?
27. Can I take proceedings on my registered settlement agreement as on a judgment (s 7(3)(b))?
28. Does the amount in my registered settlement agreement carry interest as a judgment debt (s 7(3)(c))?
29. May I apply to a District Court to set aside the registration of my settlement agreement (s 7(4))?
30. Can a District Court set aside my settlement agreement (s 7(5) and (6))?

**May I bring my claim to the tribunal? (ss 12 to 17)**

31. Is my claim made by and against the right people (s 12(2))?
32. May my employer bring a claim against me about this matter (s 12(2)(c))?
33. Is my claim for what the Act allows a tribunal claim to be for (s 12(3))?
34. Does each amount I claim relate to a specified employment dispute (s 12(4))?
35. Is my claim supported by a claim referral certificate for every dispute (s 12(5))?
36. Am I in time to lodge my claim after my certificate was issued (s 12(6))?
37. Is the total I claim within the claim limits (s 12(7))?
38. May I abandon the amount over the claim limit (s 15(1))?
39. How much of my salary-type claim is over the claim limit (s 15(1)(a))?
40. How much of my wrongful dismissal claim is over the claim limit (s 15(1)(b))?
41. If I abandon the excess, does the tribunal have jurisdiction over my claim (s 15(2)(b))?
42. If I abandon the excess, does the tribunal's order fully discharge all demands for the claim (s 15(2)(c))?
43. Can I recover the amount I abandoned later (s 15(3))?
44. Can I split my claim into separate proceedings (s 14)?
45. Is my claim barred because it is already before another court or the Commissioner (s 16(1))?
46. Can either side start court proceedings about my claim after it is lodged (s 16(2))?
47. After my dismissal, am I barred from claiming salary in lieu of notice because I made representations to the Minister (s 16(3))?
48. Is the claim I lodged deemed discontinued because I then made representations to the Minister (s 16(4)(a))?
49. From what date is the claim I lodged deemed discontinued (s 16(4)(b))?
50. After my dismissal, am I barred from a wrongful dismissal claim because I made representations to the Minister (s 16(5))?
51. Is the wrongful dismissal claim I lodged deemed discontinued because I then made representations (s 16(6)(a))?
52. Am I barred from claiming employment assistance payment because I made representations under section 8B(1) (s 16(7))?
53. Is my employment assistance payment claim stayed because I then made representations (s 16(8)(a))?
54. Has the stay on my employment assistance payment claim ended (s 16(8))?
55. May I proceed with my employment assistance payment claim once the Minister has decided (s 16(8)(c))?
56. Can my employer defend my employment assistance payment claim by saying I was not eligible, if they did not say so at the mediation (s 16(9))?
57. Does the tribunal have jurisdiction to hear and determine my claim (s 12(1))?

**How do I lodge my claim, and what must come with it? (s 13)**

58. Is my claim lodged once I file it with the Registry (s 13(1))?
59. Did I file my claim in the form and manner required (s 13(2)(a))?
60. Does a certificate for every dispute come with my claim (s 13(2)(b)(i))?
61. Do all the other documents required come with my claim (s 13(2)(b)(ii))?
62. Is the court fee I am paying with my claim enough (s 13(2)(b)(iii))?

**At the hearing: representation, privacy, evidence and burden of proof (ss 18 to 21 and 27)**

63. Can this person represent me, or the other side, at the tribunal (s 19(1) to (3))?
64. Will the proceedings on my claim be conducted in private (s 18(1))?
65. May the tribunal let this person observe my hearing (s 18(4))?
66. May the tribunal decide my claim without me if I do not turn up (s 20(8))?
67. Must the tribunal have regard to the tripartite guidelines on wrongful dismissal (s 20(7)(a))?
68. May the tribunal draw an inference against my employer because it did not meet an obligation it had (s 21(2))?
69. Do I have to give my evidence on oath (s 21(3))?
70. Must the tribunal tell me what evidence it found itself (s 21(6))?
71. Who must prove an allegation that someone is not the employer or the employee (s 27(1))?
72. If I was dismissed without notice, must my employer prove it had just cause (s 27(2)(a))?
73. If I was dismissed with notice for poor performance or misconduct, must my employer prove that (s 27(2)(b))?

**What the tribunal can order, and what it can cost me (s 22)**

74. May the tribunal make this order on my claim (s 22(1))?
75. May the tribunal take this into account when deciding whether to order me to pay costs (s 22(2))?
76. Is the total the tribunal orders for salary-type disputes within the claim limit (s 22(4))?
77. How much of the total I am ordered to pay is the amount, leaving out costs (s 22(6)(a))?
78. How much of what I have paid goes to the amount, and how much to the costs (s 22(6)(b))?
79. How much of what I have paid is applied to the costs (s 22(6)(b))?
80. Must the tribunal dismiss my claim because it has no jurisdiction (s 22(7))?
81. Can the tribunal send my dispute back to mediation instead of deciding it (s 22(8))?
82. By what date may the tribunal correct its order (s 22(10))?
83. Can a tribunal's order be enforced like a District Court judgment (s 22(12))?

**If I want to appeal, or the other side does (ss 23 to 26)**

84. Can I appeal against the tribunal's order (s 23(1) and (2))?
85. Is the District Court's order on my appeal final (s 23(4))?
86. Does my appeal stop the tribunal's order being enforced against me (s 24(1))?
87. Is enforcement of the order stayed while the appeal is pending (s 24(1))?
88. Can the High Court order a stay of the order against me (s 24(4))?
89. Is the High Court's decision final (s 26)?

**Can my contract stop me, and who may see my information? (ss 28 to 31)**

90. Is a term in my contract that stops me from claiming void (s 28)?
91. May the Commissioner, the mediator, the tribunal magistrate or the Registrar share information about my claim (s 29(1))?
92. May the tribunal publish its order or decision on my claim (s 29(2))?
93. Can I make the mediator or the Commissioner personally liable for what they did (s 30(3))?

## What is encoded and what is not

| module | what it holds | assertions |
| --- | --- | --- |
| `eca-nouns.l4` | the types the other modules share: the actors, the acts, the kinds of dispute, the kinds of party and representative | none (types only) |
| `eca-schedules.l4` | the First to Fourth Schedules, one entry per item, with the item number | 71 in `eca-tests-schedules.l4` |
| `eca-part1-preliminary.l4` | s 2(1): the 29 defined terms; s 2(2); s 2(3) | 134 in `eca-tests-part1.l4` |
| `eca-part2-mediation.l4` | ss 3 to 7: the mediation request, the time limits, the mediator, representation, the certificate, settlement | 209 in `eca-tests-part2.l4` |
| `eca-part3-jurisdiction.l4` | ss 8 to 11 (the tribunals, their magistrates, the Registry) and ss 12 to 17: jurisdiction, lodging, abandoning the excess, other proceedings, transfer | 259 in `eca-tests-part3-jurisdiction.l4` |
| `eca-part3-proceedings.l4` | ss 18 to 22: privacy, representation, the hearing, evidence, orders | 143 in `eca-tests-part3-proceedings.l4` |
| `eca-part3-appeals.l4` | ss 23 to 27: appeal, stay, powers of the High Court, finality, burden of proof | 78 in `eca-tests-part3-appeals.l4` |
| `eca-part4-miscellaneous.l4` | ss 28 to 31 and 35(2): contracting out, disclosure, protection, public servants, guidelines | 41 in `eca-tests-part4.l4` |
| `eca-seat.l4`, `eca-cases-seat.l4` | the seat layer | 235 cases in `eca-cases-seat.l4` |

Layer 1 holds 244 named functions, every one used by at least one assertion.
Every rule carries `-- src:` lines copied from the text by a generator script (it is kept beside this folder, not in it, and is not part of the row; nothing is typed from memory) and an `@ref` locator, and `srcrefs.py`, which is in the row, checks every `-- src:` line against the text and every locator against its lines.
Duties and permissions that name a party are also written as regulative rules (`PARTY ... MUST / MAY / SHANT ... WITHIN ... HENCE ... LEST`) and run with `#TRACE`: ss 3(1) and (2), 3(5), 4(1), 5(1)(b) and (c), 6(2), 19(1)(b) and (c), 21(6), 21(8)(a) and (b), and 22(10).
Each of those has a decision function as its twin, and the decision function is what carries the assertions (finding 36).

**Encoded as stated, with the borrowed or prescribed fact asked as an input (Commons Guide section 4, as the brief states it):**
the meanings the Act borrows from other Acts (`salary`, `workman`, `employment assistance payment`, `tripartite mediation`, the periods in s 65(2A) and (2B) of the Employment Act 1968, the representations under the Industrial Relations Act 1960 and the Retirement and Re-employment Act 1993);
every fee, claim limit and period that regulations or Rules of Court prescribe (the mediation fee, the court fee, the claim limits in s 12(7), the period in s 12(6), the periods in s 7(2) and (4) and s 17(2));
the classes of employee, employer, representative and observer that regulations prescribe.
No figure for any of these comes from memory; each is a number or a yes/no the person states, and the test figures in the cases (60 days, 20000, 100, 50, and 8000, 9000 and 10000 for claim limits and totals) are labelled as test figures.

**Not encoded, and why** (the inert rows of the coverage table): the title page, arrangement of sections, long title, headings, the Legislative History and the Comparative Table (reason 1, not operative); the short title (s 1) and the powers to make regulations, Rules of Court, orders and guidelines (reason 2, machinery): ss 3(6)(a) and (c) to (g), 3(7), 4(6), 12(8), 18(5), 32, 33, 34 and 35(1).
Each machinery row of the coverage table says "stated gap: no function" and what arrives in the encoding as an input instead.
The Minister's powers (ss 3(7), 32, 35(1)) are machinery, but an order made under s 3(7) or s 32 would change the answers; the Act's own periods and the Schedules as printed are used (finding 37).
Sections 8 to 11 (the tribunals, their magistrates, the Registry) are encoded as decision functions about who may do what; the instruments of appointment and the Registry's records are outside the encoding.
The text shows no repealed or blank provision, so reason 3 is not used.

## Dependencies

**The Interpretation Act time module: read, and not used.**
It was staged as `DEPENDENCIES/sg-interpretation-act/sgia-interpretation-time.l4` (git blob `fe60ab2c1f2326a5b061e163761bd63e4f47e12a` in Commons main d468311a6).
The staged copy carries a 3-line header, so `git hash-object` on the copy gives a different value; with the first 3 lines removed it gives that blob (I ran it on 2026-11-05).
This row does not import it and does not copy it: no module here has an `IMPORT` of it, and the folder holds no `sgia-` file.
I read its header, the `s 50` functions and the `s 2(1)` function for "month" and "year".

What I found, and why I did not use it (each point is checkable in the module):
- **Months and years.**
  The module has no rule for a period of months or years: its `the last day of a period` answers `NOTHING` for every unit but days counted "from" an event (header, lines 20 to 23, and the function's `OTHERWISE NOTHING`), and its `what the Act says the unit means` gives only "calendar month" for a month.
  Every period this Act counts in months or years (s 3(2)(b), (d), (e), (f), (g) and s 3(3)(a)(ii)) would therefore come out `NOTHING`.
  So the month-end question (fork F6: six months after 31 August 2025) is not answered by the Interpretation Act; it stays a fork, and I took the reading `add months` gives, which clamps to the last day of the shorter month.
- **Days "after" an event.**
  Section 50(a) of the Interpretation Act excludes the day of the event from a period of days "from" it, which is the reading I took in fork F7 for "within 14 days after" (s 22(10)) and "within the prescribed period after" (s 12(6)).
  The module counts only "from"; these provisions say "after", and for "after" the module answers `NOTHING`.
  So I did not rely on it; it agrees with F7 and does not decide it.
- **Sundays and public holidays are not modelled, and this is a gap in the encoding, not a choice the Act makes.**
  Section 50(b) of the Interpretation Act says that if the last day of a period is a Sunday or a public holiday, the period includes the next day that is neither; (c) says the same for an act directed for such a day; (d) excludes those days from a period of not more than 6 days.
  Nothing in layer 1 takes a Sunday or a public holiday as a fact.
  The functions that work out a last day are `s 3(2) the last day by which the mediation request must be submitted` (with its paragraphs (a) to (g)), `s 12(6) the claim is lodged within the prescribed period after the certificate was issued` and `s 22(10) the last day on which the tribunal may make the correction`.
  For each, an act done on the next working day after a last day that is a Sunday or a public holiday is answered `JUST FALSE` here, and would be in time under s 50(b) unless a contrary intention appears.
  The module has `the last day of the period once section 50(b) is applied`, which takes the last day as worked out, the unit, a list of public holidays and a yes/no for a contrary intention; wiring it in needs the list of public holidays as an input of each function above, which changes their signatures, and I did not do that.
  To fill later.
- **Definitions.**
  I did not open `sgia-p1-definitions.l4` (blob `ca5e2607c635962769a753d71154ad4ae6055f59`; the same 3-line header) except to look up one entry, "Gazette" (s 2(1), entry 32).
  The encoding asks "have the guidelines been published in the Gazette" as a yes/no input (s 35(2)) and does not use the look-up.
  No other word of this Act was checked against the 92 entries.

**The other Acts the text borrows from are not staged, so each borrowed fact is a named input of the encoding.**
They are listed below: not staged; to fill later.
The lines are lines of `inputs/ECA2016.txt` that name the Act, found by the script that builds this file (`src:` numbers as in the `-- src:` lines of the modules); the row names are the coverage rows that contain them.
A year in the text with no Act below would stop that script.

| Act | where this Act's text names it (coverage row, `src:` line) | what the encoding takes as a named input, or does instead |
| --- | --- | --- |
| Employment Act 1968 | s 2(1) “approved mediator”(c) (src:135); s 2(1) “authorised person” (src:147); s 2(1) “Commissioner” (src:169); s 2(1) “salary” (src:261); s 2(1) “workman” (src:295); s 2(3) (src:316); s 3(2)(a) (src:335); s 3(2)(d) (src:355); s 3(2)(e) (src:360); s 4(5)(c) (src:552); s 12(2)(b) (src:896); s 16(1)(b) (src:1067); s 18(3) (src:1274); s 27(1)(b)(ii) (src:1759); s 27(2)(a) (src:1770); s 27(2)(c) (src:1784); s 27(2)(d) (src:1797, 1799); Sch 2 group heading (src:2241); Sch 2 item 13 (src:2244); Sch 2 item 14 (src:2248); Sch 2 item 15 (src:2252); Sch 2 item 16 (src:2256); Sch 2 item 17 (src:2260); Sch 2 item 18 (src:2264); Sch 2 item 19 (src:2267); Sch 2 item 20 (src:2271); Sch 2 item 21 (src:2274); Sch 2 item 22 (src:2276); Sch 2 item 23 (src:2281); Sch 2 item 24 (src:2283); Sch 2 item 25 (src:2292); Sch 2 item 26 (src:2298); Sch 2 item 27 (src:2301); Sch 2 item 28 (src:2306); Sch 2 item 29 (src:2309); Sch 2 item 30 (src:2311); Sch 2 item 31 (src:2315); Sch 2 item 32 (src:2320); Sch 3 item 1 (src:2393); Sch 3 item 2 (src:2402); Sch 3 item 3 (src:2409, 2412); Sch 4 item 1 (src:2424) | `salary` and `workman` as s 2(1) of that Act gives them (yes/no/unsure inputs of the s 2(1) definitions here); the Commissioner for Labour appointed under its s 3(1) and an authorised person appointed under its s 3(3); the last day of the period in its s 65(2A), as extended under s 65(2B) (an input of `s 3(2)(a)`); the dismissals of its s 14(1) and (2) and s 84(1) and (2) (yes/no inputs of s 27(2)(a) to (d); paragraphs (d) and (e) of s 3(2) are tied to claims under its s 14(2) and s 84(2)); the item names of the Schedules, which are named constructors. Not staged; to fill later. |
| Retirement and Re-employment Act 1993 | s 2(1) “approved mediator”(d) (src:138); s 2(1) “employment assistance payment” (src:221); s 2(1) “tripartite guidelines on re‑employment” (src:285); s 3(2)(b) (src:341); s 3(2)(c) (src:346); s 16(3)(a)(ii) (src:1099, 1100); s 16(4)(a)(ii) (src:1126); s 16(7) (src:1168); s 16(8) (src:1187); s 16(9) (src:1214); s 27(1)(b)(iii) (src:1761); Sch 2 group heading (src:2379); Sch 2 item 45 (src:2382) | `employment assistance payment` as its s 2(1) gives it (an input of the s 2(1) definition); representations under its s 8(1) and s 8B(1) (yes/no inputs of s 16(3), (5) and (7)); the dispute of its s 8A(3) and the last day determined under its s 8B(8) (inputs of s 3(2)(b) and (c)); the guidelines issued under its s 11B (an input of the s 2(1) definition). Not staged; to fill later. |
| Industrial Relations Act 1960 | s 2(1) “claim referral certificate”(b) (src:159); s 2(1) “Industrial Arbitration Court” (src:224, 225); s 2(1) “tripartite mediation” (src:292); s 7(9) (src:799); s 16(3)(a)(i) (src:1095); s 16(4)(a)(i) (src:1122); s 16(5)(a) (src:1141); s 16(6)(a) (src:1159) | an Industrial Arbitration Court established under its s 3 (an input of the s 2(1) definition); `tripartite mediation` as its s 30F gives it (an input of the s 2(1) definition and of s 3(8)); representations under its s 35(3) (yes/no inputs of s 16); whether its s 30H(3) to (9) applies (an input of s 7(9)); a certificate issued under its s 30H(6), which is one of the two routes to a claim referral certificate in s 2(1) (a named constructor of the kind of issue). Not staged; to fill later. |
| State Courts Act 1970 | s 2(1) “tribunal” (src:278); s 8 (src:811); s 30(1) (src:1877) | whether a body was constituted under its s 4 (an input of the s 2(1) definition of `tribunal`; s 8 asks only whether the person is the President); the protection a Magistrate has under it (s 30(1) is encoded as the section states it, and what the protection is is not looked up). Not staged; to fill later. |
| Legal Profession Act 1966 | s 9(2) (src:825, 826) | a `qualified person` as its s 2(1) defines one (a yes/no/unsure input of `s 9(2) the individual is eligible for appointment as a tribunal magistrate`). Not staged; to fill later. |
| Child Development Co-Savings Act 2001 | s 27(1)(b)(i) (src:1757); s 27(2)(d) (src:1794, 1795); Sch 2 group heading (src:2171); Sch 2 item 1 (src:2175); Sch 2 item 2 (src:2183); Sch 2 item 3 (src:2187); Sch 2 item 4 (src:2190); Sch 2 item 4A (src:2193); Sch 2 item 5 (src:2198); Sch 2 item 6 (src:2201); Sch 3 item 3 (src:2408) | the female employee mentioned in its s 12(1) (a yes/no input of s 27(2)(d)); the item names of Schedule 2, which name its ss 12AA, 12B and 12E and are named constructors. Not staged; to fill later. |
| Child Development Co-Savings (Part-Time Employees) Regulations 2008 | Sch 2 group heading (src:2203, 2204); Sch 2 item 7 (src:2207, 2208); Sch 2 item 8 (src:2211, 2212); Sch 2 item 9 (src:2215, 2216); Sch 2 item 10 (src:2219, 2220); Sch 2 item 10A (src:2223, 2224); Sch 2 item 11 (src:2229, 2230); Sch 2 item 12 (src:2238, 2239); Sch 2 group heading (src:2323); Sch 2 item 33 (src:2325, 2326); Sch 2 item 34 (src:2329, 2330); Sch 2 item 35 (src:2333, 2334); Sch 2 item 36 (src:2338); Sch 2 item 37 (src:2345, 2346); Sch 2 item 38 (src:2350, 2351); Sch 2 item 39 (src:2355, 2356); Sch 2 item 40 (src:2360, 2361); Sch 2 item 41 (src:2363, 2364); Sch 2 item 42 (src:2368, 2369); Sch 2 item 43 (src:2372); Sch 2 item 44 (src:2376) | none: the regulations are named only in the item names of Schedule 2, which are named constructors. Not staged; to fill later. |
| Employment of Foreign Manpower (Work Passes) Regulations 2012 | Sch 4 item 2 (src:2427, 2428); Sch 4 item 3 (src:2431) | none: the regulations are named only in the item names of the Fourth Schedule (items 2 and 3), which are named constructors. Not staged; to fill later. |
| Penal Code 1871 | s 31(1) (src:1895); s 31(2) (src:1899) | none: s 31 deems an approved mediator and an authorised person to be public servants "for the purposes of the Penal Code 1871", and the encoding answers whether the deeming applies; what follows under the Code is not modelled. Not staged; to fill later. |
| Limited Liability Partnerships Act 2005 | s 5(5) “body corporate” (src:602, 603); s 19(5) “body corporate” (src:1350, 1351) | whether a body is a limited liability partnership as its s 2(1) defines one (a yes/no input of s 5(5) and s 19(5)). Not staged; to fill later. |
| Supreme Court of Judicature Act 1969 | s 33(1) (src:1916) | none: s 33(1) names the Rules Committee appointed under its s 80(3), which is machinery; what the Rules of Court prescribe arrives as inputs. Not staged; to fill later. |

Regulations, Rules of Court and practice directions that this Act refers to are likewise not staged: the fees, claim limits, periods, forms and prescribed classes they set are inputs (see "What the text does not answer").

## Jural relations

Hohfeld's correlatives: a claim-right is matched by a duty; a privilege by a no-right; a power by a liability (being subject to the power, not an obligation); an immunity by a disability.
The kinds are recorded here and are not typed into the person-facing answers (ruling N2, below).
Each provision that creates a relation has a row; a definition or a counting rule is `none`.
A key beginning with `~` in `jural-relations.tsv` is a provision that is not encoded (machinery), listed here because it does create a power.
Where the text addresses a party without naming who benefits, the holder is "not named in the text".
`jural.py check` confirms that every layer-1 function is matched by a row, that every row's key matches a function, and that every function is named in at least one test or case: 244 functions, 111 rows, 145 keys; 0 functions without a row; 0 keys matching no function; 0 functions not named in any test or case.

| Provision | Holder | Kind | Bearer | How it is encoded |
| --- | --- | --- | --- | --- |
| s 2(1) | none | definition | none | 29 defined terms: each is a membership function (is this person or thing within the term), tested on both sides; no relation is created |
| s 2(2) | none | reading rule | none | for a counterclaim, `claimant` and `respondent` change places; a function over a small typed representation |
| s 2(3) | Deputy Commissioner, Principal Assistant Commissioner or Assistant Commissioner for Labour, if authorised | power | any claimant or respondent whose request the Commissioner would deal with (liability) | power to do what the Commissioner may do; authorisation is an input; an unauthorised officer is JUST FALSE (reading (a), M-list) |
| s 3(1), s 3(8) | Commissioner | claim-right | claimant: duty to submit a mediation request before lodging a claim (no duty if a tripartite mediation was conducted) | MUST with a twin decision function; the exception is s 3(8) |
| s 3(2) | Commissioner | claim-right | claimant: duty to submit the request by the time the paragraph names | MUST ... WITHIN carried by the decision function `by the time`; the last day for each of (a) to (g) is a counting rule (fork F6) |
| s 3(3)(a) | Commissioner | claim-right | claimant: duty to list every dispute that meets the stated requirements | decision function; conditions (i) to (iii) are counting rules |
| s 3(3)(b), s 3(3)(c) | Commissioner | claim-right | claimant: duty not to list a dispute (SHANT derived from the answer, N2) | decision functions; the bearer is named by the text, so the prohibition is derived from the answer |
| s 3(3)(d) | Commissioner | claim-right | claimant: duty to accompany the request with the prescribed fee | decision function; the fee is an input |
| s 3(4)(a) | Commissioner | power | claimant (liability to have the request refused) | decision function: JUST TRUE if (i) or (ii), else JUST FALSE (reading (a)) |
| s 3(4)(b) | Commissioner | power | claimant (liability: the fee may be waived, remitted or refunded) | constant JUST TRUE: the grant has no condition |
| s 3(4)(c) | Commissioner | power | a prescribed person or class (liability: the fee may be paid to them in lieu of the Consolidated Fund) | NOTHING outside the prescribed class (reading (b)) |
| s 3(5) | claimant | claim-right | Commissioner: duty, on accepting the request, to refer every listed dispute to an approved mediator | MUST with a twin decision function |
| s 4(1) | claimant and respondent | claim-right | approved mediator: duty to conduct the first mediation session | MUST with a twin decision function |
| s 4(2) | approved mediator | privilege | claimant and respondent (no-right: they cannot insist on a session) | decision function: JUST TRUE if satisfied there is no reasonable prospect, else JUST FALSE (reading (a)) |
| s 4(3) | parties to the mediation | claim-right | approved mediator: duty to hold each session in private | decision function |
| s 4(4), s 4(5) | Commissioner and the approved mediator | privilege | the claimants and the respondent (no-right: they cannot object to disputes being taken together) | decision functions; (5)(a) to (c) are the cases in which (4) applies |
| s 5(1) | not named in the text | claim-right | party to a mediation: duty to act in person, and not to be represented by an advocate and solicitor or by an agent | decision function and two SHANT rules (N2: derived from the answer), run with #TRACE |
| s 5(2), s 5(3) | a party (non-individual or individual) | privilege | the other party (no-right) | decision function over a small representation of who may represent whom; whether regulations prescribe an individual is an input, which is also all that subsection (4) adds |
| s 5(5) | none | definition | none | `body corporate` and `officer` for s 5 |
| s 6(1), s 6(4) | none | counting rule | none | when s 6 applies; when a dispute is unresolved |
| s 6(2) | claimant | claim-right | approved mediator: duty to issue a claim referral certificate for an unresolved dispute in the three cases | MUST with a twin decision function |
| s 6(3) | approved mediator | power | claimant (liability: mediation discontinued and certificate refused) | decision function: JUST TRUE for a claimant who fails to attend without reasonable excuse, else JUST FALSE (reading (a)) |
| s 7(1) | not named in the text | claim-right | parties to the settlement: duty to use the prescribed form, keep each party's total within the limit, and sign | four decision functions; form and limits are inputs |
| s 7(2) | District Court | power | any party to the settlement agreement (liability: registration on application; refusal if late) | two decision functions |
| s 7(3)(a) | none | status rule | none | from the date of registration the agreement has the force of a judgment: a date function |
| s 7(3)(b) | party entitled under the registered agreement | privilege | party liable under it (no-right) | decision function |
| s 7(3)(c) | person to whom the amount is payable | claim-right | party liable: duty to pay interest as on a judgment debt | decision function |
| s 7(4) | any party to the registered agreement | power | the other parties (liability: registration may be set aside) | decision function; the period is an input (NOTHING outside it, reading (b)) |
| s 7(5), s 7(6) | District Court | power | the parties (liability: registration or the agreement set aside; the dispute referred for mediation) | decision functions; (6)(a) to (d) are the conditions of the power |
| s 7(7) | claimant | claim-right | approved mediator: duty to issue a certificate for a dispute referred back by the District Court | decision functions, with no regulative rule; (7)(b) is a power as in s 6(3) |
| s 7(8), s 7(9) | none | counting rule | none | when a referred dispute is unresolved; to avoid doubt, another Act's procedure applies (asked as a fact) |
| s 9(6) | former tribunal magistrate | power | the parties to the case (liability: judgment may be given after the appointment ended) | decision function |
| s 11(3) | registrar for the tribunals | power | the parties (liability: the tribunal's powers exercised by the registrar to the extent authorised) | decision function |
| s 11(4) | deputy registrar and assistant registrar for the tribunals | power | the parties (liability) | decision function over the office |
| s 12(1) | tribunal | power | respondent (liability to be sued before the tribunal) | decision function gathering (2) to (7) by hand (E1 option B as guidance only); NOTHING when a requirement fails (reading (b)) |
| s 12(2), s 12(3), s 12(4), s 12(5), s 12(6), s 12(7) | none | condition of the power in s 12(1) | none | one decision function per requirement; JUST FALSE when the requirement is not met (reading (a), a requirement worded "must") |
| s 13(1) | none | counting rule | none | when a claim is lodged |
| s 13(2) | not named in the text | claim-right | claimant: duty to file in the form and manner required and to bring the certificate, the other documents and the fee | decision functions; form, documents and fee are inputs |
| s 14 | respondent | immunity | claimant (disability: cannot divide the claim only to come within the jurisdiction) | decision function |
| s 15(1) | claimant | power | respondent (liability: the excess abandoned) | decision function |
| s 15(2)(a) | none | deeming rule | none | the s 12(7) requirement is deemed satisfied |
| s 15(2)(b) | tribunal | power | respondent (liability) | decision function: depends on the abandonment |
| s 15(2)(c) | respondent | immunity | claimant (disability: no further demand in respect of the claim) | decision function |
| s 15(3) | respondent | immunity | claimant (disability: cannot recover the excess anywhere) | decision function |
| s 16(1) | respondent | immunity | claimant (disability: cannot lodge while other proceedings are pending or the Commissioner has decided) | decision function |
| s 16(2) | respondent | immunity | claimant (disability: no proceedings in another court once lodged) | decision function; "unless" the claim ends |
| s 16(3), s 16(5), s 16(7) | respondent or employer | immunity | dismissed employee (disability: cannot lodge after making representations) | decision functions; (7) has an "unless" |
| s 16(4), s 16(6), s 16(8)(b) | none | deeming rule | none | the claim is deemed discontinued, and the date it takes effect |
| s 16(8)(a), s 16(8)(c) | respondent; then employee | immunity; then privilege | employee (disability while stayed); then the respondent (no-right) | decision functions: stayed until the Minister decides; may proceed if the Minister decides to allow |
| s 16(9) | employee | immunity | employer (disability: cannot defend on the eligibility ground not raised at mediation) | decision function |
| s 17(1) | appropriate court | power | the parties to the proceedings (liability to transfer) | decision function |
| s 17(2) | not named in the text | claim-right | applicant: duty to apply within the time and manner prescribed | decision function |
| s 17(3) | appropriate court | power | the parties (liability to terms) | decision function |
| s 17(4) | respondent | immunity | claimant (disability: execution stayed until the counterclaim ends, unless the court orders otherwise) | decision function |
| s 17(5) | none | definition | none | `appropriate court` |
| s 18(1) | parties | claim-right | tribunal: duty to conduct proceedings in private | decision function |
| s 18(2), s 18(3), s 18(4) | tribunal | power | the parties (liability: individuals allowed to assist, sit, participate or observe) | decision functions; prescribed individuals are inputs |
| s 18(6) | tribunal | privilege | the parties (no-right: claims may be heard together) | decision function |
| s 19(1) | not named in the text | claim-right | party to proceedings: duty to act in person and not to be represented by an advocate and solicitor or by an agent | decision function and two SHANT rules derived from it (N2) |
| s 19(2), s 19(3) | a party | privilege | the other party (no-right) | decision function; s 19(3) has a word missing in the text (fork F8); subsection (4) adds only that regulations may prescribe different individuals, carried by the input about regulations |
| s 19(5) | none | definition | none | `body corporate` and `officer` for s 19 |
| s 20(1), s 20(2) | parties | claim-right | tribunal: duty to proceed informally, to identify the issues and to ensure the evidence is adduced | decision functions |
| s 20(3), s 20(4) | tribunal | power | the parties; the person summoned (liability) | decision functions |
| s 20(5), s 20(6) | tribunal | privilege | the parties (no-right) | decision functions |
| s 20(7) | parties to a wrongful dismissal claim | claim-right | tribunal: duty to have regard to the guidelines and to calculate compensation by the regulations | decision functions |
| s 20(8) | tribunal | power | absent party (liability: decision in absence) | decision function: JUST FALSE if the absence had a reasonable excuse (reading (a)) |
| s 21(1), s 21(5) | tribunal | privilege | the parties (no-right) | decision functions |
| s 21(2), s 21(4), s 21(7) | tribunal | power | the party who failed; the person giving evidence; the party giving written evidence (liability) | decision functions |
| s 21(3) | person giving evidence | privilege | tribunal (no-right to require an oath, subject to (4)) | decision function |
| s 21(6) | every party | claim-right | tribunal: duty to disclose what it obtained | MUST with a twin decision function |
| s 21(8) | not named in the text | claim-right | tribunal: duty to make a summary of the facts and issues and notes of the proceedings (no duty to keep a record of evidence) | MUST rules for (a) and (b) with twin decision functions |
| s 22(1), s 22(3) | tribunal | power | the parties (liability to the orders and conditions) | decision functions |
| s 22(2) | tribunal | privilege | the parties (no-right) | decision function; the list is not closed |
| s 22(4), s 22(5) | party ordered to pay | immunity | tribunal (disability: total must not exceed the claim limit) | decision functions; limit is an input |
| s 22(6) | none | counting rule | none | the amount without costs; how a payment is applied |
| s 22(7) | respondent | claim-right | tribunal: duty to dismiss a claim or part outside its jurisdiction | decision function |
| s 22(8), s 22(9) | tribunal | power | the parties (liability: referral to mediation, attendance in person) | decision functions |
| s 22(10), s 22(11) | tribunal | power | the parties (liability: correction within 14 days) | MAY ... WITHIN 14 run with #TRACE; the 14-day limit is carried by decision functions (fork F7) |
| s 22(12) | party in whose favour the order is made | power | party against whom it is made (liability to enforcement as a District Court judgment) | decision function |
| s 23(1), s 23(2) | any party | power | the other party (liability: appeal with permission) | decision functions |
| s 23(3) | District Court | power | the parties (liability: time extended or matter remitted) | decision functions |
| s 23(4) | the party who benefits from the order | immunity | the other party (disability: no appeal) | decision function |
| s 24(1) | party in whose favour the order is made | power | appellant (liability: enforcement is not stayed by the appeal alone) | decision function |
| s 24(2), s 24(4) | District Court or General Division of the High Court | power | the parties (liability to a stay and to conditions) | decision functions |
| s 24(3) | the party who benefits | immunity | the other party (disability: no appeal) | decision function |
| s 25 | General Division of the High Court | power | the parties (liability) | decision function; "must not" limits in (2) |
| s 25(3), s 25(4) | General Division of the High Court; then parties | privilege; then claim-right | parties (no-right); then the Court (duty) | decision functions |
| s 26 | the party who benefits | immunity | the other party (disability) | decision function |
| s 27 | the other party | claim-right | the person who makes the allegation, or the employer: burden of proving it | decision functions; a burden is recorded as a duty-like rule |
| s 28 | employee or other party to the agreement | immunity | the other party to the agreement (disability: cannot rely on a void term) | decision functions |
| s 29(1), s 29(2) | Commissioner, approved mediator, tribunal magistrate, Registrar | privilege | the person the information concerns (no-right) | decision functions |
| s 29(3) | none | definition | none | `law enforcement agency` and `public agency` |
| s 30(1), s 30(2), s 30(3) | tribunal magistrate; Registrar; approved mediator and others | immunity | any person who would sue them personally (disability) | decision functions |
| s 31 | none | deeming rule | none | approved mediator and authorised person are deemed public servants |
| s 35(2) | tribunal and the General Division of the High Court | privilege | the parties (no-right) | decision function |
| sch 1, sch 2, sch 3, sch 4 | none | table | none | the matters, written laws and obligations the Schedules list: item-number functions, one entry per row, each tested |
| s 1 | none | short title | none | not encoded: machinery (inert, reason 2) |
| s 3(6)(a), s 3(6)(c) to (g), s 4(6), s 12(8), s 18(5), s 34 | Minister | power | claimants, respondents and others (liability to regulations: manner, fee, persons, period, claim limits, compensation) | not encoded: rule- and regulation-making power (inert, reason 2); what the regulations prescribe arrives in layer 1 as an input, never a figure from memory; s 3(6)(b), the persons who may submit on a claimant's behalf, is encoded (row above) |
| s 3(6)(b) | Minister (by regulations) | power | claimants (liability: the persons who may submit a request on their behalf are those the regulations prescribe) | decision function over a MAYBE input: what the regulations prescribe is not among the sources |
| s 3(7) | Minister | power | claimants and respondents (liability: the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii) may be lengthened or shortened by order) | not encoded: power to change the Act's own periods (inert, reason 2); the Act's periods are used as printed, and an order would change the answers (NOTES finding) |
| s 8 | President | power | the State Courts (liability: one or more Employment Claims Tribunals may be constituted under s 4 of the State Courts Act 1970) | decision function over who acts |
| s 9(1) | none | constitution of an office | none | decision function: who may preside over a tribunal |
| s 9(2) | none | condition on a power | none | eligibility for appointment under s 9(1)(a); "qualified person" under the Legal Profession Act 1966 is an input |
| s 9(3) | President | power | the individual appointed (liability: may be re-appointed) | decision function; the term itself is whatever the instrument of appointment says |
| s 9(4) | President, on the Chief Justice's recommendation | power | the individual appointed under s 9(1)(a) (liability: the appointment may be revoked at any time) | decision function |
| s 9(5) | Presiding Judge of the State Courts | power | any District Judge (liability: may be designated a tribunal magistrate) | decision function |
| s 10 | none | establishment of an office, and a statement of what it keeps | none | constant decision functions: the Registry is established and keeps all records of the tribunals |
| s 11(1) | none | designation of an office-holder | none | decision function: the registrar of the State Courts is the registrar for the tribunals |
| s 11(2) | Chief Justice | power | the individuals appointed (liability: deputy registrars, assistant registrars and other officers may be appointed for the tribunals) | decision function |
| s 32, s 33 | Minister; Rules Committee | power | all persons subject to the Act (liability: Schedules amended, Rules of Court made) | not encoded: power to amend the Schedules and to make Rules of Court (inert, reason 2); what the Rules prescribe arrives as an input |
| s 35(1) | Minister | power | none directly (liability of no one until guidelines are published) | not encoded: power to issue tripartite guidelines (inert, reason 2); the effect of publication is s 35(2) |

## Coverage

The coverage table is built by `coverage.py` from the text itself, and `coverage-dispositions.tsv` supplies each row's disposition.
A row inherits its disposition from the longest matching prefix of its id; a row that the encoding cites with an `@ref` range is `encoded` unless the TSV marks it `fork`; a heading marked inert reason 1 stays inert even where an enclosing `@ref` range happens to span its line.
There is one row per section, per numbered subsection, per lettered paragraph, per roman sub-paragraph, per capital-letter paragraph, per defined term, per schedule item and per heading.

**Dispositions.**
Rows: 585.
Encoded: 403.
Fork: 53.
Inert: 129 (reason 1: 58; reason 2: 71; reason 3: 0; reason 1 is not operative, reason 2 is machinery, reason 3 is repealed or blank).
Repealed or blank in this text: 0 (the text shows none; the "Omitted as having had effect" lines are in the Comparative Table and concern the earlier edition).
There is no out-of-scope row and no deferred row.
No row was moved out of inert: this is a new encoding with no earlier table.

**Audit, printed by the script.**
2587 lines in the file; 171 page-furniture lines (page header/footer: 102, page number: 4, amendment note: 64, amendment note, cut off before its closing bracket: 1); 1652 other non-blank lines; 0 in no row; 0 in more than one row.
The page furniture is excluded by class, and the classes are printed above: the running page header and footer, the page numbers, and the bracketed amendment notes such as `[55/2018]` (one note is cut off in the rendering, `[34A`, and is counted with them).
Every other non-blank line of the text falls in exactly one row: no line is in none and none is in two.

**Units counted two ways.**
By marker, without the row builder: 35 sections; 115 numbered subsections that do not begin a section; 239 lettered paragraphs (this count includes each line that begins "(i)", which is a letter in s 33(2)(i) and the first roman numeral elsewhere); 23 roman sub-paragraphs from "(ii)" on; 9 capital-letter paragraphs; 35 defined terms; 71 schedule items.
By the rows themselves: 35 sections; 115 such subsections; 271 lettered, roman or capital-letter paragraphs; 35 defined terms; 71 schedule items; 35 section headings.
They agree (the script stops if they do not): 239 + 23 + 9 = 271 paragraph-level rows.
Rows before and after: the first version of the row builder, which stopped at lettered paragraphs, produced 535 rows; after roman sub-paragraph and capital-letter rows were added it produced 585.
There was no earlier coverage table for this row.

**What "encoded" means here, and its limit.**
A row is marked `encoded` when an `@ref` range in a layer-1 module overlaps its lines.
`coverage.py` also checks that every significant line of every encoded or fork row lies inside some `@ref` range: 0 do not.
That shows each provision is cited, not that the rule is right.
A fork row names the fork (F1, F6, F7, F8, F9, F10, F11) and also lies under the rule that encodes the reading taken.
The Schedule 2 group headings are inert reason 1 even though the item names carry the Act each item belongs to.

| Row | Lines | Begins | Disposition | Reason, fork or where it is encoded |
| --- | --- | --- | --- | --- |
| front | 1-18 | THE STATUTES OF THE REPUBLIC OF SINGAPORE | inert | reason 1 not operative: title page and contents page |
| arrangement | 20-100 | ARRANGEMENT OF SECTIONS | inert | reason 1 not operative: the arrangement of sections is a table of contents |
| long-title | 102-106 | An Act to facilitate the expeditious resolut | inert | reason 1 not operative: the long title states a purpose and creates no rule |
| enactment | 108-108 | [1 April 2017] | inert | reason 1 not operative: the date of enactment |
| part1 | 113-115 | PART 1 | inert | reason 1 not operative: Part heading |
| s1/heading | 117-117 | Short title | inert | reason 1 not operative: marginal heading of a section |
| s1 | 119-119 | 1. This Act is the Employment Claims Act 201 | inert | reason 2 machinery: short title |
| s2/heading | 121-121 | Interpretation | inert | reason 1 not operative: marginal heading of a section |
| s2(1) | 123-123 | 2.—(1) In this Act, unless the context other | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator” | 125-127 | “approved mediator” means any individual app | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator”(a) | 129-130 | (a) a mediation under Part 2 of a specified  | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator”(b) | 132-132 | (b) a tripartite mediation; | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator”(c) | 134-135 | (c) a mediation mentioned in section 115(2A) | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator”(d) | 137-138 | (d) a consultation or conciliation under sec | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“approved mediator”(e) | 140-144 | (e) a mediation or conciliation of any dispu | encoded | part1-preliminary: s 2(1) the person is an approved mediator |
| s2(1)/“authorised person” | 146-149 | “authorised person” means an individual appo | encoded | part1-preliminary: s 2(1) the person is an authorised person |
| s2(1)/“claim” | 151-152 | “claim” means a claim lodged with a tribunal | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the thing is a claim |
| s2(1)/“claim referral certificate” | 154-155 | “claim referral certificate” means a claim r | encoded | part1-preliminary: s 2(1) the certificate is a claim referral certificate |
| s2(1)/“claim referral certificate”(a) | 157-157 | (a) section 6(2) or 7(7)(a); or | encoded | part1-preliminary: s 2(1) the certificate is a claim referral certificate |
| s2(1)/“claim referral certificate”(b) | 159-159 | (b) section 30H(6) of the Industrial Relatio | encoded | part1-preliminary: s 2(1) the certificate is a claim referral certificate |
| s2(1)/“claimant” | 164-166 | “claimant” means a person who lodges a claim | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is a claimant |
| s2(1)/“Commissioner” | 168-169 | “Commissioner” means the Commissioner for La | encoded | part1-preliminary: s 2(1) the person is the Commissioner |
| s2(1)/“contract of service” | 171-174 | “contract of service” means an agreement, wh | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the agreement is a contract of service |
| s2(1)/“court” | 176-176 | “court” means any court of competent jurisdi | encoded | part1-preliminary: s 2(1) the body is a court |
| s2(1)/“employee” | 178-180 | “employee” means an individual who has enter | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employee |
| s2(1)/“employee”(a) | 182-184 | (a) any employee of the Government within a  | fork | F1 closed or open reading of "means ... and includes" (the item inside the list); encoded: part1-preliminary: s 2(1) the person is an employee |
| s2(1)/“employee”(b) | 186-191 | (b) for an employment dispute relating to th | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employee |
| s2(1)/“employer” | 193-194 | “employer” means any person who employs an i | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employer”(a) | 196-199 | (a) the Government in respect of any categor | fork | F1 closed or open reading of "means ... and includes" (the item inside the list); encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employer”(b) | 201-201 | (b) a statutory body; | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employer”(c) | 203-204 | (c) a person duly authorised by an employer  | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employer”(d) | 206-208 | (d) a person who owns, carries on or is resp | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employer”(e) | 213-218 | (e) for an employment dispute relating to th | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is an employer |
| s2(1)/“employment assistance payment” | 220-221 | “employment assistance payment” has the mean | encoded | part1-preliminary: s 2(1) the payment is an employment assistance payment |
| s2(1)/“Industrial Arbitration Court” | 223-225 | “Industrial Arbitration Court” means an Indu | encoded | part1-preliminary: s 2(1) the court is an Industrial Arbitration Court |
| s2(1)/“mediation” | 227-227 | “mediation” includes — | encoded | part1-preliminary: s 2(1) the thing is mediation |
| s2(1)/“mediation”(a) | 229-230 | (a) the undertaking of any activity for the  | encoded | part1-preliminary: s 2(1) the thing is mediation |
| s2(1)/“mediation”(b) | 232-235 | (b) the bringing together of the parties to  | encoded | part1-preliminary: s 2(1) the thing is mediation |
| s2(1)/“mediation”(c) | 237-238 | (c) the follow‑up of any matter which is the | encoded | part1-preliminary: s 2(1) the thing is mediation |
| s2(1)/“mediation request” | 240-241 | “mediation request” means a request for a me | encoded | part1-preliminary: s 2(1) the request is a mediation request |
| s2(1)/“mediation session” | 243-244 | “mediation session” means a meeting between  | encoded | part1-preliminary: s 2(1) the meeting is a mediation session |
| s2(1)/“Registrar” | 246-247 | “Registrar” means the registrar, a deputy re | encoded | part1-preliminary: s 2(1) the officer is a Registrar |
| s2(1)/“Registry” | 249-250 | “Registry” means the registry established un | encoded | part1-preliminary: s 2(1) the registry is the Registry |
| s2(1)/“respondent” | 252-255 | “respondent” means a person against whom a c | fork | F1 closed or open reading of "means ... and includes"; encoded: part1-preliminary: s 2(1) the person is a respondent |
| s2(1)/“salary” | 260-261 | “salary” has the meaning given by section 2( | encoded | part1-preliminary: s 2(1) the payment is salary |
| s2(1)/“specified contractual dispute” | 263-266 | “specified contractual dispute” means a disp | encoded | part1-preliminary: s 2(1) the dispute is a specified contractual dispute |
| s2(1)/“specified employment dispute” | 268-270 | “specified employment dispute” means a speci | encoded | part1-preliminary: s 2(1) the dispute is a specified employment dispute |
| s2(1)/“specified statutory dispute” | 272-274 | “specified statutory dispute” means a disput | encoded | part1-preliminary: s 2(1) the dispute is a specified statutory dispute |
| s2(1)/“tribunal” | 276-278 | “tribunal” means a subordinate court called  | encoded | part1-preliminary: s 2(1) the body is a tribunal |
| s2(1)/“tribunal magistrate” | 280-281 | “tribunal magistrate” means a tribunal magis | encoded | part1-preliminary: s 2(1) the person is a tribunal magistrate |
| s2(1)/“tripartite guidelines on re‑employment” | 283-285 | “tripartite guidelines on re‑employment” mea | encoded | part1-preliminary: s 2(1) the guidelines are the tripartite guidelines o... |
| s2(1)/“tripartite guidelines on wrongful dismissal” | 287-289 | “tripartite guidelines on wrongful dismissal | encoded | part1-preliminary: s 2(1) the guidelines are the tripartite guidelines o... |
| s2(1)/“tripartite mediation” | 291-292 | “tripartite mediation” has the meaning given | encoded | part1-preliminary: s 2(1) the mediation is a tripartite mediation |
| s2(1)/“workman” | 294-295 | “workman” has the meaning given by section 2 | encoded | part1-preliminary: s 2(1) the person is a workman |
| s2(1)/“wrongful dismissal dispute” | 297-298 | “wrongful dismissal dispute” means a dispute | encoded | part1-preliminary: s 2(1) the dispute is a wrongful dismissal dispute |
| s2(2) | 302-303 | (2) When this Act is applied to a countercla | fork | F12 "When" read as "where" (ruled): the references keep their ordinary meaning when the Act is not applied to a counterclaim; a yes-or-no twin carries the no; encoded: part1-preliminary: s 2(2) the person a reference in the Act is a referen...; part1-preliminary: s 2(2) a reference to the claimant or the respondent ... |
| s2(2)(a) | 308-309 | (a) any reference to a claimant is a referen | encoded | part1-preliminary: s 2(2) the person a reference in the Act is a referen...; part1-preliminary: s 2(2) a reference to the claimant or the respondent ... |
| s2(2)(b) | 311-312 | (b) any reference to a respondent is a refer | encoded | part1-preliminary: s 2(2) the person a reference in the Act is a referen...; part1-preliminary: s 2(2) a reference to the claimant or the respondent ... |
| s2(3) | 314-318 | (3) Any Deputy Commissioner for Labour, Prin | encoded | part1-preliminary: s 2(3) the officer may carry out a function or duty o... |
| part2 | 320-322 | PART 2 | inert | reason 1 not operative: Part heading |
| s3/heading | 324-324 | Mediation of specified employment dispute | inert | reason 1 not operative: marginal heading of a section |
| s3(1) | 326-329 | 3.—(1) Before a claimant lodges a claim agai | encoded | part2-mediation: s 3(1) the claimant must submit a mediation request b...; part2-mediation: s 3(1) the mediation request relates to every specifi...; +1 more |
| s3(2) | 331-332 | (2) The mediation request must be submitted  | encoded | part2-mediation: s 3(1) and (2) the claimant's duty to submit a mediat...; part2-mediation: s 3(2) the last day by which the mediation request mu...; +1 more |
| s3(2)(a) | 334-338 | (a) for any specified employment dispute con | encoded | part2-mediation: s 3(2)(a) the last day for a request about recovering...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(b) | 340-343 | (b) for any re‑employment dispute described  | fork | F6 how "N months after" is counted when the later month is shorter; encoded: part2-mediation: s 3(2)(b) the last day for a request about a re-emplo...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(c) | 345-347 | (c) for any re‑employment dispute under sect | encoded | part2-mediation: s 3(2)(c) the last day for a request about a re-emplo...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(d) | 349-356 | (d) for any wrongful dismissal dispute in re | fork | F6 how "N months after" is counted when the later month is shorter; encoded: part2-mediation: s 3(2)(d) the last day for a request about a wrongful...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(e) | 358-361 | (e) for any wrongful dismissal dispute in re | fork | F6 how "N months after" is counted when the later month is shorter; encoded: part2-mediation: s 3(2)(e) the last day for a request about a wrongful...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(f) | 363-368 | (f) for any specified employment dispute (no | fork | F6 how "N months after" is counted when the later month is shorter; encoded: part2-mediation: s 3(2)(f) the last day for a request about another sp...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(2)(g) | 370-373 | (g) for any other specified employment dispu | fork | F6 how "N months after" is counted when the later month is shorter; encoded: part2-mediation: s 3(2)(g) the last day for a request about any other ...; part2-mediation: s 3(2) the last day by which the mediation request mu... |
| s3(3) | 377-377 | (3) The mediation request — | encoded | part2-mediation: s 3(3)(a) the mediation request must list the specifi... |
| s3(3)(a) | 379-382 | (a) subject to paragraphs (b) and (c), must  | encoded | part2-mediation: s 3(3)(a) the mediation request must list the specifi... |
| s3(3)(a)(i) | 384-386 | (i) if there is a claim for an amount relati | encoded | part2-mediation: s 3(3)(a) the mediation request must list the specifi... |
| s3(3)(a)(ii) | 388-391 | (ii) the material facts giving rise to the d | fork | F6 how "one year before" is counted when the earlier month is shorter; encoded: part2-mediation: s 3(3)(a) the mediation request must list the specifi... |
| s3(3)(a)(iii) | 393-403 | (iii) the dispute is not listed in an earlie | encoded | part2-mediation: s 3(3)(a) the mediation request must list the specifi... |
| s3(3)(b) | 405-405 | (b) must not list a specified employment dis | encoded | part2-mediation: s 3(3)(b) the mediation request must not list the spe... |
| s3(3)(b)(i) | 407-409 | (i) paragraph (a) requires an earlier mediat | encoded | part2-mediation: s 3(3)(b) the mediation request must not list the spe... |
| s3(3)(b)(ii) | 411-412 | (ii) the requirements prescribed for this su | encoded | part2-mediation: s 3(3)(b) the mediation request must not list the spe... |
| s3(3)(c) | 414-414 | (c) must not list a specified employment dis | encoded | part2-mediation: s 3(3)(c) the mediation request must not list the spe... |
| s3(3)(c)(i) | 416-417 | (i) there is a claim for an amount relating  | encoded | part2-mediation: s 3(3)(c) the mediation request must not list the spe... |
| s3(3)(c)(ii) | 419-420 | (ii) under section 16, that claim cannot be  | encoded | part2-mediation: s 3(3)(c) the mediation request must not list the spe... |
| s3(3)(d) | 422-423 | (d) must be accompanied by the prescribed fe | encoded | part2-mediation: s 3(3)(d) the mediation request is accompanied by the... |
| s3(4) | 427-427 | (4) The Commissioner may — | encoded | part2-mediation: s 3(4)(a) the Commissioner may refuse to accept the m... |
| s3(4)(a) | 429-429 | (a) refuse to accept a mediation request if  | encoded | part2-mediation: s 3(4)(a) the Commissioner may refuse to accept the m... |
| s3(4)(a)(i) | 431-432 | (i) that request does not comply with the re | encoded | part2-mediation: s 3(4)(a) the Commissioner may refuse to accept the m... |
| s3(4)(a)(ii) | 434-435 | (ii) the requirement in section 12(7) cannot | encoded | part2-mediation: s 3(4)(a) the Commissioner may refuse to accept the m... |
| s3(4)(b) | 437-438 | (b) waive, remit or refund, wholly or in par | encoded | part2-mediation: s 3(4)(b) the Commissioner may waive, remit or refund... |
| s3(4)(c) | 440-443 | (c) pay the whole or a part of the fee menti | encoded | part2-mediation: s 3(4)(c) the Commissioner may pay the whole or a par... |
| s3(5) | 445-447 | (5) Upon accepting the mediation request, th | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part2-mediation: s 3(5) the Commissioner must refer the specified empl...; part2-mediation: s 3(5) the Commissioner's duty to refer the listed di... |
| s3(6) | 452-452 | (6) Regulations made under section 34 may — | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(a) | 454-455 | (a) prescribe the manner in which a mediatio | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(b) | 457-465 | (b) prescribe the persons (or classes of per | encoded | part2-mediation: s 3(6)(b) the person may submit the mediation request... |
| s3(6)(c) | 467-468 | (c) prescribe the requirements mentioned in | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(d) | 470-473 | (d) prescribe the fee mentioned in subsectio | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(e) | 475-476 | (e) prescribe any person or class of persons | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(f) | 478-481 | (f) provide for the review by the Commission | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(6)(g) | 483-485 | (g) provide for the amendment of the list of | inert | reason 2 machinery: regulation-making power (the manner, the fee and the persons it covers arrive in the encoding as inputs); stated gap: no function |
| s3(7) | 487-490 | (7) The Minister may, by order in the Gazett | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to lengthen or shorten the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii), for all claimants or a class; stated gap: no function, the Act's own periods are used as printed, and an order made under it would change the answers |
| s3(7)(a) | 492-492 | (a) the period of 6 months mentioned in subs | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to lengthen or shorten the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii), for all claimants or a class; stated gap: no function, the Act's own periods are used as printed, and an order made under it would change the answers |
| s3(7)(b) | 494-494 | (b) the period of one year mentioned in subs | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to lengthen or shorten the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii), for all claimants or a class; stated gap: no function, the Act's own periods are used as printed, and an order made under it would change the answers |
| s3(7)(c) | 496-496 | (c) the period of one year mentioned in subs | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to lengthen or shorten the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii), for all claimants or a class; stated gap: no function, the Act's own periods are used as printed, and an order made under it would change the answers |
| s3(8) | 501-503 | (8) This section does not apply to a claim i | encoded | part2-mediation: s 3(8) section 3 does not apply to the claim |
| s4/heading | 505-505 | Conduct of mediation sessions | inert | reason 1 not operative: marginal heading of a section |
| s4(1) | 507-510 | 4.—(1) An approved mediator must conduct the | fork | F9 "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" (assumed, not ruled); encoded: part2-mediation: s 4(1) the approved mediator must conduct the first m...; part2-mediation: s 4(1) the approved mediator's duty to conduct the fi... |
| s4(2) | 512-515 | (2) Despite subsection (1), an approved medi | encoded | part2-mediation: s 4(2) the approved mediator need not conduct a media... |
| s4(3) | 517-517 | (3) Each mediation session must be held in p | encoded | part2-mediation: s 4(3) the mediation session must be held in private |
| s4(4) | 519-519 | (4) Despite subsection (3) — | encoded | part2-mediation: s 4(4) the same approved mediator may take the disput... |
| s4(4)(a) | 521-523 | (a) the Commissioner may refer all of the sp | encoded | part2-mediation: s 4(4) the same approved mediator may take the disput... |
| s4(4)(b) | 525-528 | (b) that approved mediator may conduct the m | encoded | part2-mediation: s 4(4) the same approved mediator may take the disput... |
| s4(5) | 532-532 | (5) Subsection (4) applies where — | encoded | part2-mediation: s 4(5) subsection (4) applies |
| s4(5)(a) | 534-538 | (a) 2 or more claimants have submitted to th | encoded | part2-mediation: s 4(5) subsection (4) applies |
| s4(5)(b) | 540-544 | (b) 2 claimants intend to lodge claims again | encoded | part2-mediation: s 4(5) subsection (4) applies |
| s4(5)(c) | 549-553 | (c) the same claimant has submitted to the C | encoded | part2-mediation: s 4(5) subsection (4) applies |
| s4(6) | 557-558 | (6) Regulations made under section 34 may pr | inert | reason 2 machinery: regulation-making power |
| s5/heading | 560-560 | Representation at mediation under this Part | inert | reason 1 not operative: marginal heading of a section |
| s5(1) | 562-563 | 5.—(1) Except as provided in subsections (2) | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med...; part2-mediation: s 5(1)(b) the party's prohibition on representation b...; +1 more |
| s5(1)(a) | 565-565 | (a) must act in person; | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med...; part2-mediation: s 5(1)(b) the party's prohibition on representation b...; +1 more |
| s5(1)(b) | 567-567 | (b) cannot be represented by an advocate and | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med...; part2-mediation: s 5(1)(b) the party's prohibition on representation b...; +1 more |
| s5(1)(c) | 569-570 | (c) cannot be represented by an agent, wheth | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med...; part2-mediation: s 5(1)(b) the party's prohibition on representation b...; +1 more |
| s5(2) | 572-572 | (2) A party other than an individual may be  | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(2)(a) | 574-574 | (a) if the party is the Government, by a pub | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(2)(b) | 576-577 | (b) if the party is a body corporate, by an  | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(2)(c) | 579-580 | (c) if the party is a partnership, by a part | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(2)(d) | 582-584 | (d) if the party is an unincorporated associ | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(2)(e) | 586-587 | (e) by any other individual prescribed by re | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(3) | 589-590 | (3) A party who is an individual may be repr | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(4) | 592-594 | (4) For the purposes of subsections (2)(e) a | encoded | part2-mediation: s 5(1) to (3) the party may be represented at the med... |
| s5(5) | 599-599 | (5) In this section — | encoded | part2-mediation: s 5(5) the entity is a body corporate |
| s5(5)/“body corporate” | 601-603 | “body corporate” includes a limited liabilit | encoded | part2-mediation: s 5(5) the entity is a body corporate |
| s5(5)/“officer” | 605-608 | “officer”, in relation to a body corporate,  | encoded | part2-mediation: s 5(5) the person is an officer of the body corporate |
| s6/heading | 610-610 | Claim referral certificate | inert | reason 1 not operative: marginal heading of a section |
| s6(1) | 612-612 | 6.—(1) This section applies where — | encoded | part2-mediation: s 6(1) section 6 applies |
| s6(1)(a) | 614-615 | (a) a claimant submits to the Commissioner a | encoded | part2-mediation: s 6(1) section 6 applies |
| s6(1)(b) | 617-618 | (b) the Commissioner refers any specified em | encoded | part2-mediation: s 6(1) section 6 applies |
| s6(2) | 620-623 | (2) The approved mediator to whom is referre | encoded | part2-mediation: s 6(2) the approved mediator must issue the claimant ...; part2-mediation: s 6(2) the approved mediator's duty to issue a claim ...; +1 more |
| s6(2)(a) | 625-626 | (a) the respondent is given reasonable notic | encoded | part2-mediation: s 6(2) the approved mediator must issue the claimant ...; part2-mediation: s 6(2) the approved mediator's duty to issue a claim ... |
| s6(2)(b) | 628-630 | (b) no settlement is reached at the end of t | encoded | part2-mediation: s 6(2) the approved mediator must issue the claimant ...; part2-mediation: s 6(2) the approved mediator's duty to issue a claim ... |
| s6(2)(c) | 632-634 | (c) the approved mediator is satisfied that  | encoded | part2-mediation: s 6(2) the approved mediator must issue the claimant ...; part2-mediation: s 6(2) the approved mediator's duty to issue a claim ... |
| s6(3) | 636-638 | (3) Despite subsection (2), if a claimant su | encoded | part2-mediation: s 6(3) the approved mediator may discontinue the medi... |
| s6(3)(a) | 640-640 | (a) discontinue the mediation; and | encoded | part2-mediation: s 6(3) the approved mediator may discontinue the medi... |
| s6(3)(b) | 645-647 | (b) refuse to issue to the claimant a claim  | encoded | part2-mediation: s 6(3) the approved mediator may discontinue the medi... |
| s6(4) | 649-650 | (4) In this section, a specified employment  | encoded | part2-mediation: s 6(4) the specified employment dispute is unresolved |
| s6(4)(a) | 652-652 | (a) is not settled; and | encoded | part2-mediation: s 6(4) the specified employment dispute is unresolved |
| s6(4)(b) | 654-655 | (b) is not withdrawn from the list of specif | encoded | part2-mediation: s 6(4) the specified employment dispute is unresolved |
| s7/heading | 657-657 | Settlement of specified employment dispute | inert | reason 1 not operative: marginal heading of a section |
| s7(1) | 659-661 | 7.—(1) Where a specified employment dispute  | encoded | part2-mediation: s 7(1)(a) the settlement agreement is in the form pre... |
| s7(1)(a) | 663-665 | (a) the parties to the settlement must enter | encoded | part2-mediation: s 7(1)(a) the settlement agreement is in the form pre... |
| s7(1)(b) | 667-672 | (b) the total amount payable to a party unde | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part2-mediation: s 7(1)(b) the total amount payable to the party for c... |
| s7(1)(c) | 674-678 | (c) the total amount payable to a party unde | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part2-mediation: s 7(1)(c) the total amount payable to the party for w... |
| s7(1)(d) | 680-681 | (d) the settlement agreement must be signed  | encoded | part2-mediation: s 7(1)(d) the settlement agreement is signed by or on... |
| s7(2) | 685-688 | (2) A District Court may register a settleme | fork | F9 "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" (assumed, not ruled); encoded: part2-mediation: s 7(2) a District Court may register the settlement a...; part2-mediation: s 7(2) a District Court may refuse to register the se... |
| s7(3) | 693-694 | (3) Where the settlement agreement is regist | encoded | part2-mediation: s 7(3)(a) the date from which the settlement agreemen... |
| s7(3)(a) | 696-699 | (a) the settlement agreement is, for the pur | encoded | part2-mediation: s 7(3)(a) the date from which the settlement agreemen... |
| s7(3)(b) | 703-705 | (b) proceedings may be taken on the settleme | encoded | part2-mediation: s 7(3)(b) proceedings may be taken on the settlement ... |
| s7(3)(c) | 707-709 | (c) any amount (payable to a person) for whi | encoded | part2-mediation: s 7(3)(c) an amount for which the settlement agreemen... |
| s7(4) | 711-715 | (4) Where a settlement agreement is register | fork | F10 "within the period prescribed by Rules of Court": a period fixed by reference, not in the text's own words; encoded: part2-mediation: s 7(4) a party may apply to set aside the registration |
| s7(5) | 717-718 | (5) A District Court hearing an application  | encoded | part2-mediation: s 7(5)(a) a District Court may set aside the registra... |
| s7(5)(a) | 720-720 | (a) set aside the registration of the settle | encoded | part2-mediation: s 7(5)(a) a District Court may set aside the registra... |
| s7(5)(b) | 722-722 | (b) do either or both of the following: | encoded | part2-mediation: s 7(5)(b)(i) a District Court may set aside the settl... |
| s7(5)(b)(i) | 724-724 | (i) set aside the settlement agreement; | encoded | part2-mediation: s 7(5)(b)(i) a District Court may set aside the settl... |
| s7(5)(b)(ii) | 726-734 | (ii) refer any specified employment dispute  | encoded | part2-mediation: s 7(5)(b)(ii) the kind of mediation a District Court ... |
| s7(6) | 739-739 | (6) For the purposes of subsection (5), the  | encoded | part2-mediation: s 7(6) a condition for setting aside is satisfied |
| s7(6)(a) | 741-743 | (a) the settlement agreement is void or void | encoded | part2-mediation: s 7(6) a condition for setting aside is satisfied |
| s7(6)(b) | 745-746 | (b) the settlement agreement includes subjec | encoded | part2-mediation: s 7(6) a condition for setting aside is satisfied |
| s7(6)(c) | 748-749 | (c) any term of the settlement agreement is  | encoded | part2-mediation: s 7(6) a condition for setting aside is satisfied |
| s7(6)(d) | 751-752 | (d) the registration of the settlement agree | encoded | part2-mediation: s 7(6) a condition for setting aside is satisfied |
| s7(7) | 754-757 | (7) Where a District Court sets aside under  | encoded | part2-mediation: s 7(7)(a) the approved mediator must issue the claima... |
| s7(7)(a) | 759-761 | (a) the approved mediator must issue to the  | encoded | part2-mediation: s 7(7)(a) the approved mediator must issue the claima... |
| s7(7)(a)(i) | 763-764 | (i) the respondent is given reasonable notic | encoded | part2-mediation: s 7(7)(a) the approved mediator must issue the claima... |
| s7(7)(a)(ii) | 766-769 | (ii) no settlement is reached at the end of  | encoded | part2-mediation: s 7(7)(a) the approved mediator must issue the claima... |
| s7(7)(a)(iii) | 771-774 | (iii) the approved mediator is satisfied tha | encoded | part2-mediation: s 7(7)(a) the approved mediator must issue the claima... |
| s7(7)(b) | 776-778 | (b) despite paragraph (a), if the claimant,  | encoded | part2-mediation: s 7(7)(b) the approved mediator may discontinue the m... |
| s7(7)(b)(i) | 780-780 | (i) discontinue the mediation; and | encoded | part2-mediation: s 7(7)(b) the approved mediator may discontinue the m... |
| s7(7)(b)(ii) | 782-789 | (ii) refuse to issue to the claimant a claim | encoded | part2-mediation: s 7(7)(b) the approved mediator may discontinue the m... |
| s7(8) | 791-792 | (8) In subsection (7), a specified employmen | encoded | part2-mediation: s 7(8) the specified employment dispute referred by t... |
| s7(9) | 794-801 | (9) To avoid doubt, where a District Court s | encoded | part2-mediation: s 7(9) section 30H(3) to (9) of the Industrial Relati... |
| part3 | 803-805 | PART 3 | inert | reason 1 not operative: Part heading |
| div1 | 807-807 | Division 1 — Establishment of tribunals and  | inert | reason 1 not operative: Division heading |
| s8/heading | 809-809 | Establishment of tribunals | inert | reason 1 not operative: marginal heading of a section |
| s8 | 811-812 | 8. The President may, under section 4 of the | encoded | part3-jurisdiction: s 8 the person may constitute one or more Employment ... |
| s9/heading | 814-814 | Appointment and qualifications of tribunal m | inert | reason 1 not operative: marginal heading of a section |
| s9(1) | 816-816 | 9.—(1) A tribunal is presided over by — | encoded | part3-jurisdiction: s 9(1) the individual presides over a tribunal as a t... |
| s9(1)(a) | 818-819 | (a) a tribunal magistrate appointed by the P | encoded | part3-jurisdiction: s 9(1) the individual presides over a tribunal as a t... |
| s9(1)(b) | 821-821 | (b) a tribunal magistrate designated under s | encoded | part3-jurisdiction: s 9(1) the individual presides over a tribunal as a t... |
| s9(2) | 823-826 | (2) An individual is eligible for appointmen | encoded | part3-jurisdiction: s 9(2) the individual is eligible for appointment as ... |
| s9(3) | 828-830 | (3) An individual appointed under subsection | encoded | part3-jurisdiction: s 9(3) the individual may be re-appointed as a tribun... |
| s9(4) | 835-837 | (4) Despite subsection (3), the President ma | fork | F9 "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" (assumed, not ruled); encoded: part3-jurisdiction: s 9(4) the President may revoke the appointment of th... |
| s9(5) | 839-840 | (5) The Presiding Judge of the State Courts  | encoded | part3-jurisdiction: s 9(5) the person may designate the individual as a t... |
| s9(6) | 842-847 | (6) Any individual appointed under subsectio | encoded | part3-jurisdiction: s 9(6) the individual may sit as a tribunal magistrat... |
| s10/heading | 849-849 | Registry | inert | reason 1 not operative: marginal heading of a section |
| s10(1) | 850-850 | 10.—(1) A registry is established for the tr | encoded | part3-jurisdiction: s 10(1) a registry is established for the tribunals |
| s10(2) | 851-851 | (2) The Registry keeps all records of the tr | encoded | part3-jurisdiction: s 10(2) the Registry keeps all records of the tribunals |
| s11/heading | 853-854 | Registrar, deputy registrars, assistant regi | inert | reason 1 not operative: marginal heading of a section |
| s11(1) | 856-857 | 11.—(1) The registrar of the State Courts is | encoded | part3-jurisdiction: s 11(1) the person is the registrar for the tribunals |
| s11(2) | 859-861 | (2) The Chief Justice may appoint deputy reg | encoded | part3-jurisdiction: s 11(2) the person may appoint deputy registrars, ass... |
| s11(3) | 863-865 | (3) To the extent authorised by this Act or  | encoded | part3-jurisdiction: s 11(3) the registrar for the tribunals may exercise ... |
| s11(4) | 867-869 | (4) All the powers and duties of the registr | encoded | part3-jurisdiction: s 11(4) the officer may exercise and perform the powe... |
| div2 | 871-871 | Division 2 — Jurisdiction of tribunals | inert | reason 1 not operative: Division heading |
| s12/heading | 873-873 | Jurisdiction of tribunal to hear and determi | inert | reason 1 not operative: marginal heading of a section |
| s12(1) | 875-882 | 12.—(1) Subject to this Act, a tribunal has  | encoded | part3-jurisdiction: s 12(1) the date on which the dispute arose does not ...; part3-jurisdiction: s 12(1) the tribunal has jurisdiction to hear and det... |
| s12(2) | 884-884 | (2) The claim must be made — | encoded | part3-jurisdiction: s 12(2) the claim is made as the subsection requires |
| s12(2)(a) | 886-890 | (a) by an employee who is prescribed or belo | encoded | part3-jurisdiction: s 12(2)(a) the claim is made by an employee in a pres...; part3-jurisdiction: s 12(2) the claim is made as the subsection requires |
| s12(2)(b) | 892-896 | (b) by an employee who is prescribed or belo | encoded | part3-jurisdiction: s 12(2)(b) the claim is made by an employee in a pres...; part3-jurisdiction: s 12(2) the claim is made as the subsection requires |
| s12(2)(c) | 898-903 | (c) by an employer who is prescribed or belo | encoded | part3-jurisdiction: s 12(2)(c) the claim is made by an employer in a pres...; part3-jurisdiction: s 12(2) the claim is made as the subsection requires |
| s12(2)(c)(i) | 905-906 | (i) any matter specified in item 17 of the F | encoded | part3-jurisdiction: s 12(2)(c)(i) the matter is specified in item 17 of t...; part3-jurisdiction: s 12(2)(c) the claim is made by an employer in a pres...; +1 more |
| s12(2)(c)(ii) | 908-910 | (ii) any other matter specified in the First | encoded | part3-jurisdiction: s 12(2)(c) the claim is made by an employer in a pres...; part3-jurisdiction: s 12(2) the claim is made as the subsection requires |
| s12(3) | 914-914 | (3) The claim must be for either or both of  | encoded | part3-jurisdiction: s 12(3) the claim is for what the subsection requires |
| s12(3)(a) | 916-917 | (a) one or more amounts alleged to be payabl | encoded | part3-jurisdiction: s 12(3) the claim is for what the subsection requires |
| s12(3)(b) | 919-921 | (b) reinstatement, by the respondent, of the | encoded | part3-jurisdiction: s 12(3) the claim is for what the subsection requires |
| s12(4) | 925-926 | (4) Each amount alleged to be payable under  | encoded | part3-jurisdiction: s 12(4) each amount alleged to be payable relates to ... |
| s12(5) | 931-933 | (5) The claim must be supported by a claim r | encoded | part3-jurisdiction: s 12(5) the claim is supported by a claim referral ce... |
| s12(6) | 935-937 | (6) The claim must be lodged with the tribun | fork | F7 how the days "after" the date of issue are counted; encoded: part3-jurisdiction: s 12(6) the claim is lodged within the prescribed per... |
| s12(7) | 939-940 | (7) The total amount alleged to be payable u | encoded | part3-jurisdiction: s 12(7) the total amount alleged satisfies the condit... |
| s12(7)(a) | 942-947 | (a) the total amount alleged to be payable u | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-jurisdiction: s 12(7)(a) the total alleged for contractual and stat...; part3-jurisdiction: s 12(7) the total amount alleged satisfies the condit... |
| s12(7)(b) | 949-953 | (b) the total amount alleged to be payable u | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-jurisdiction: s 12(7)(b) the total alleged for wrongful dismissal d...; part3-jurisdiction: s 12(7) the total amount alleged satisfies the condit... |
| s12(8) | 957-957 | (8) Regulations made under section 34 may — | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s12(8)(a) | 959-961 | (a) prescribe different employees or classes | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s12(8)(b) | 963-965 | (b) prescribe different employers or classes | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s12(8)(c) | 967-967 | (c) prescribe any matter mentioned in subsec | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s12(8)(d) | 969-971 | (d) prescribe the period in subsection (6),  | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s12(8)(e) | 973-975 | (e) prescribe the claim limits in subsection | inert | reason 2 machinery: regulation-making power (the classes, the period in s 12(6) and the claim limits in s 12(7) arrive in the encoding as inputs) |
| s13/heading | 982-982 | Lodging of claim | inert | reason 1 not operative: marginal heading of a section |
| s13(1) | 984-985 | 13.—(1) A claim is lodged with a tribunal by | encoded | part3-jurisdiction: s 13(1) the claim is lodged with the tribunal |
| s13(2) | 987-987 | (2) Every claim — | encoded | part3-jurisdiction: s 13(2)(a) the claim is filed in the form and manner ... |
| s13(2)(a) | 989-989 | (a) must be filed in the form and manner — | encoded | part3-jurisdiction: s 13(2)(a) the claim is filed in the form and manner ... |
| s13(2)(a)(i) | 991-992 | (i) prescribed by Rules of Court made under  | encoded | part3-jurisdiction: s 13(2)(a) the claim is filed in the form and manner ... |
| s13(2)(a)(ii) | 994-995 | (ii) specified in practice directions issued | encoded | part3-jurisdiction: s 13(2)(a) the claim is filed in the form and manner ... |
| s13(2)(b) | 997-997 | (b) must be accompanied by — | encoded | part3-jurisdiction: s 13(2)(b)(i) the claim is accompanied by a claim ref... |
| s13(2)(b)(i) | 999-1001 | (i) a claim referral certificate issued in r | encoded | part3-jurisdiction: s 13(2)(b)(i) the claim is accompanied by a claim ref... |
| s13(2)(b)(ii) | 1003-1003 | (ii) any other documents that may be — | encoded | part3-jurisdiction: s 13(2)(b)(ii) the claim is accompanied by the other ... |
| s13(2)(b)(ii)(A) | 1005-1006 | (A) prescribed by Rules of Court made under | encoded | part3-jurisdiction: s 13(2)(b)(ii) the claim is accompanied by the other ... |
| s13(2)(b)(ii)(B) | 1008-1009 | (B) specified in practice directions issued  | encoded | part3-jurisdiction: s 13(2)(b)(ii) the claim is accompanied by the other ... |
| s13(2)(b)(iii) | 1011-1012 | (iii) the court fee (if any) prescribed by R | encoded | part3-jurisdiction: s 13(2)(b)(iii) the claim is accompanied by the court... |
| s14/heading | 1014-1014 | No division of claim | inert | reason 1 not operative: marginal heading of a section |
| s14 | 1016-1019 | 14. A claim cannot be divided and pursued in | encoded | part3-jurisdiction: s 14 the claim cannot be divided and pursued in separ... |
| s15/heading | 1021-1021 | Claimant may abandon part of claim | inert | reason 1 not operative: marginal heading of a section |
| s15(1) | 1023-1023 | 15.—(1) Where — | encoded | part3-jurisdiction: s 15(1) the claimant may abandon the excess amount; part3-jurisdiction: s 15(1)(a) the excess amount over the prescribed clai...; +1 more |
| s15(1)(a) | 1025-1033 | (a) the total amount alleged to be payable u | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-jurisdiction: s 15(1) the claimant may abandon the excess amount; part3-jurisdiction: s 15(1)(a) the excess amount over the prescribed clai...; +1 more |
| s15(1)(b) | 1035-1040 | (b) the total amount alleged to be payable u | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-jurisdiction: s 15(1) the claimant may abandon the excess amount; part3-jurisdiction: s 15(1)(a) the excess amount over the prescribed clai...; +1 more |
| s15(2) | 1041-1041 | (2) If the claimant abandons the excess amou | encoded | part3-jurisdiction: s 15(2)(a) the requirement in section 12(7) is deemed...; part3-jurisdiction: s 15(2)(b) section 15(2) gives the tribunal jurisdict...; +1 more |
| s15(2)(a) | 1043-1044 | (a) the requirement in section 12(7) is deem | encoded | part3-jurisdiction: s 15(2)(a) the requirement in section 12(7) is deemed...; part3-jurisdiction: s 15(2)(b) section 15(2) gives the tribunal jurisdict...; +1 more |
| s15(2)(b) | 1046-1047 | (b) the tribunal has jurisdiction to hear an | encoded | part3-jurisdiction: s 15(2)(b) section 15(2) gives the tribunal jurisdict...; part3-jurisdiction: s 15(2)(c) an order of the tribunal in relation to th... |
| s15(2)(c) | 1049-1050 | (c) an order of the tribunal in relation to  | encoded | part3-jurisdiction: s 15(2)(c) an order of the tribunal in relation to th... |
| s15(3) | 1054-1055 | (3) Where the claimant has abandoned the exc | encoded | part3-jurisdiction: s 15(3) the claimant cannot recover the excess amount... |
| s16/heading | 1057-1057 | Other proceedings relating to claim | inert | reason 1 not operative: marginal heading of a section |
| s16(1) | 1059-1060 | 16.—(1) A claim relating to a specified empl | encoded | part3-jurisdiction: s 16(1) the claim cannot be lodged with a tribunal |
| s16(1)(a) | 1062-1064 | (a) any proceedings relating to that claim a | encoded | part3-jurisdiction: s 16(1) the claim cannot be lodged with a tribunal |
| s16(1)(b) | 1066-1069 | (b) a claim lodged under section 119 of the  | encoded | part3-jurisdiction: s 16(1) the claim cannot be lodged with a tribunal |
| s16(2) | 1073-1082 | (2) Despite any other written law, where a c | encoded | part3-jurisdiction: s 16(2) no proceedings relating to the claim can be c... |
| s16(3) | 1086-1090 | (3) Where an employee is dismissed, the empl | encoded | part3-jurisdiction: s 16(3) the matter is specified in item 17 of the Fir...; part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(a) | 1092-1092 | (a) the employee — | encoded | part3-jurisdiction: s 16(3)(a) the representations are under section 35(3...; part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(a)(i) | 1094-1096 | (i) has made representations in writing unde | encoded | part3-jurisdiction: s 16(3)(a) the representations are under section 35(3...; part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(a)(ii) | 1098-1101 | (ii) has made representations in writing und | encoded | part3-jurisdiction: s 16(3)(a) the representations are under section 35(3...; part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(b) | 1103-1103 | (b) either of the following applies: | encoded | part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(b)(i) | 1105-1106 | (i) the employee does not withdraw those | encoded | part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(3)(b)(ii) | 1108-1109 | (ii) the Minister concerned makes a decision | encoded | part3-jurisdiction: s 16(3) the employee cannot lodge the claim |
| s16(4) | 1113-1117 | (4) Where an employee is dismissed, and the  | encoded | part3-jurisdiction: s 16(4)(a) the claim is deemed to be discontinued |
| s16(4)(a) | 1119-1119 | (a) the claim is deemed to be discontinued,  | encoded | part3-jurisdiction: s 16(4)(a) the claim is deemed to be discontinued |
| s16(4)(a)(i) | 1121-1123 | (i) makes representations in writing under s | encoded | part3-jurisdiction: s 16(4)(a) the claim is deemed to be discontinued |
| s16(4)(a)(ii) | 1125-1127 | (ii) makes representations in writing under  | encoded | part3-jurisdiction: s 16(4)(a) the claim is deemed to be discontinued |
| s16(4)(b) | 1132-1133 | (b) the claim is deemed to be discontinued w | encoded | part3-jurisdiction: s 16(4)(b) the date with effect from which the claim ... |
| s16(5) | 1137-1138 | (5) Where an employee is dismissed, the empl | encoded | part3-jurisdiction: s 16(5) the employee cannot lodge the claim relating ... |
| s16(5)(a) | 1140-1142 | (a) the employee has made representations in | encoded | part3-jurisdiction: s 16(5) the employee cannot lodge the claim relating ... |
| s16(5)(b) | 1144-1144 | (b) either of the following applies: | encoded | part3-jurisdiction: s 16(5) the employee cannot lodge the claim relating ... |
| s16(5)(b)(i) | 1146-1147 | (i) the employee does not withdraw those | encoded | part3-jurisdiction: s 16(5) the employee cannot lodge the claim relating ... |
| s16(5)(b)(ii) | 1149-1150 | (ii) the Minister concerned makes a decision | encoded | part3-jurisdiction: s 16(5) the employee cannot lodge the claim relating ... |
| s16(6) | 1154-1155 | (6) Where an employee is dismissed, and the  | encoded | part3-jurisdiction: s 16(6)(a) the claim relating to a wrongful dismissal... |
| s16(6)(a) | 1157-1160 | (a) the claim is deemed to be discontinued,  | encoded | part3-jurisdiction: s 16(6)(a) the claim relating to a wrongful dismissal... |
| s16(6)(b) | 1162-1163 | (b) the claim is deemed to be discontinued w | encoded | part3-jurisdiction: s 16(6)(b) the date with effect from which the claim ... |
| s16(7) | 1167-1170 | (7) Where an employee has made representatio | encoded | part3-jurisdiction: s 16(7) the employee cannot lodge a claim for employm... |
| s16(7)(a) | 1172-1176 | (a) that Minister allows, under section 8B(7 | encoded | part3-jurisdiction: s 16(7) the employee cannot lodge a claim for employm... |
| s16(7)(b) | 1178-1179 | (b) a claim referral certificate is issued i | encoded | part3-jurisdiction: s 16(7) the employee cannot lodge a claim for employm... |
| s16(8) | 1184-1188 | (8) Where, after an employee has lodged with | encoded | part3-jurisdiction: s 16(8)(a) the claim is stayed; part3-jurisdiction: s 16(8)(a) the stay on the claim has ended |
| s16(8)(a) | 1190-1195 | (a) the claim is stayed until that Minister  | fork | F13 "stayed until that Minister decides" is two questions (ruled, second ruling of 2026-11-05, (d)): the bar and has the stay ended; encoded: part3-jurisdiction: s 16(8)(a) the claim is stayed; part3-jurisdiction: s 16(8)(a) the stay on the claim has ended |
| s16(8)(b) | 1197-1202 | (b) if that Minister decides not to allow th | encoded | part3-jurisdiction: s 16(8)(a) the stay on the claim has ended; part3-jurisdiction: s 16(8)(b) the date with effect from which the claim ... |
| s16(8)(c) | 1204-1208 | (c) if that Minister decides to allow the em | encoded | part3-jurisdiction: s 16(8)(a) the stay on the claim has ended; part3-jurisdiction: s 16(8)(c) the employee may proceed with the claim |
| s16(9) | 1210-1216 | (9) Where an employee has lodged with a trib | fork | F14 "if the employer did not raise this defence during the mediation": a bar on a defence, not a defence to prove; no ruling of 2026-11-05 applies; encoded: part3-jurisdiction: s 16(9) the employer cannot defend the claim on the g... |
| s17/heading | 1218-1218 | Transfer of proceedings | inert | reason 1 not operative: marginal heading of a section |
| s17(1) | 1220-1229 | 17.—(1) Where it appears to an appropriate c | encoded | part3-jurisdiction: s 17(1) the court may order the proceedings or the co... |
| s17(2) | 1231-1232 | (2) An application under subsection (1) must | encoded | part3-jurisdiction: s 17(2) the application is made as required |
| s17(3) | 1234-1235 | (3) An order under subsection (1) may be mad | encoded | part3-jurisdiction: s 17(3) the court may make the order on any terms it ... |
| s17(4) | 1237-1243 | (4) Where the appropriate court orders under | fork | F13 "stayed until the proceedings on the counterclaim are concluded" is two questions (ruled, second ruling of 2026-11-05, (d)): the bar and has the stay ended; encoded: part3-jurisdiction: s 17(4) execution or enforcement of the tribunal's or...; part3-jurisdiction: s 17(4) the stay on execution or enforcement of the t... |
| s17(5) | 1247-1248 | (5) In this section, “appropriate court” mea | encoded | part3-jurisdiction: s 17(5) the court is an appropriate court |
| div3 | 1252-1252 | Division 3 — Proceedings before tribunal | inert | reason 1 not operative: Division heading |
| s18/heading | 1254-1255 | Proceedings conducted in private unless trib | inert | reason 1 not operative: marginal heading of a section |
| s18(1) | 1257-1258 | 18.—(1) Subject to subsections (2), (3), (4) | encoded | part3-proceedings: s 18(1) the proceedings before the tribunal are condu... |
| s18(2) | 1262-1264 | (2) A tribunal may, on its own initiative or | encoded | part3-proceedings: s 18(2)(a) the tribunal may allow individuals to assi...; part3-proceedings: s 18(2)(b) the tribunal may allow the individual to s... |
| s18(2)(a) | 1266-1267 | (a) allow one or more individuals to assist  | encoded | part3-proceedings: s 18(2)(a) the tribunal may allow individuals to assi...; part3-proceedings: s 18(2)(b) the tribunal may allow the individual to s... |
| s18(2)(b) | 1269-1271 | (b) allow one or more individuals of skill a | encoded | part3-proceedings: s 18(2)(b) the tribunal may allow the individual to s... |
| s18(3) | 1273-1275 | (3) A tribunal may permit an officer appoint | encoded | part3-proceedings: s 18(3) the tribunal may permit the officer to partic... |
| s18(3)(a) | 1280-1280 | (a) giving evidence in the proceedings; | encoded | part3-proceedings: s 18(3) the tribunal may permit the officer to partic... |
| s18(3)(b) | 1282-1283 | (b) producing any document, record or thing  | encoded | part3-proceedings: s 18(3) the tribunal may permit the officer to partic... |
| s18(3)(c) | 1285-1285 | (c) making submissions in the proceedings. | encoded | part3-proceedings: s 18(3) the tribunal may permit the officer to partic... |
| s18(4) | 1289-1290 | (4) A tribunal may permit one or more of the | encoded | part3-proceedings: s 18(4) the tribunal may permit the individual to obs... |
| s18(4)(a) | 1292-1292 | (a) any prescribed individual; | encoded | part3-proceedings: s 18(4) the tribunal may permit the individual to obs... |
| s18(4)(b) | 1294-1295 | (b) any individual belonging to a prescribed | encoded | part3-proceedings: s 18(4) the tribunal may permit the individual to obs... |
| s18(4)(c) | 1297-1297 | (c) any other individual that the tribunal d | encoded | part3-proceedings: s 18(4) the tribunal may permit the individual to obs... |
| s18(5) | 1299-1301 | (5) Regulations made under section 34 may pr | inert | reason 2 machinery: regulation-making power |
| s18(6) | 1303-1306 | (6) To avoid doubt, subsection (1) does not  | encoded | part3-proceedings: s 18(6) subsection (1) does not prevent the tribunal ... |
| s19/heading | 1308-1308 | Representation before tribunal | inert | reason 1 not operative: marginal heading of a section |
| s19(1) | 1310-1311 | 19.—(1) Except as provided in subsections (2 | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th...; part3-proceedings: s 19(1)(b) the party's prohibition on representation ...; +1 more |
| s19(1)(a) | 1313-1313 | (a) must act in person; | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th...; part3-proceedings: s 19(1)(b) the party's prohibition on representation ...; +1 more |
| s19(1)(b) | 1315-1315 | (b) cannot be represented by an advocate and | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th...; part3-proceedings: s 19(1)(b) the party's prohibition on representation ...; +1 more |
| s19(1)(c) | 1317-1318 | (c) cannot be represented by an agent, wheth | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th...; part3-proceedings: s 19(1)(c) the party's prohibition on representation ... |
| s19(2) | 1320-1320 | (2) A party other than an individual may be  | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(2)(a) | 1322-1322 | (a) if the party is the Government, by a pub | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(2)(b) | 1324-1325 | (b) if the party is a body corporate, by an  | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(2)(c) | 1327-1328 | (c) if the party is a partnership, by a part | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(2)(d) | 1333-1335 | (d) if the party is an unincorporated associ | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(2)(e) | 1337-1338 | (e) by any other individual prescribed by re | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(3) | 1340-1341 | (3) A party who is an individual may be repr | fork | F8 a word missing from the text: "any other individual by regulations"; encoded: part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(4) | 1343-1345 | (4) For the purposes of subsections (2)(e) a | encoded | part3-proceedings: s 19(1) to (3) the party may be represented before th... |
| s19(5) | 1347-1347 | (5) In this section — | encoded | part3-proceedings: s 19(5) the entity is a body corporate |
| s19(5)/“body corporate” | 1349-1351 | “body corporate” includes a limited liabilit | encoded | part3-proceedings: s 19(5) the entity is a body corporate |
| s19(5)/“officer” | 1353-1356 | “officer”, in relation to a body corporate,  | encoded | part3-proceedings: s 19(5) the person is an officer of the body corporate |
| s20/heading | 1358-1358 | Hearing to be informal, etc. | inert | reason 1 not operative: marginal heading of a section |
| s20(1) | 1360-1361 | 20.—(1) Proceedings before a tribunal are to | encoded | part3-proceedings: s 20(1) the proceedings before the tribunal are to be... |
| s20(2) | 1363-1364 | (2) A tribunal, when dealing with any claim, | encoded | part3-proceedings: s 20(2)(a) the tribunal is to identify the relevant i...; part3-proceedings: s 20(2)(b) the tribunal is to ensure that the relevan... |
| s20(2)(a) | 1366-1366 | (a) is to identify the relevant issues in th | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 20(2)(a) the tribunal is to identify the relevant i...; part3-proceedings: s 20(2)(b) the tribunal is to ensure that the relevan... |
| s20(2)(b) | 1368-1369 | (b) is to ensure that the relevant evidence  | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 20(2)(b) the tribunal is to ensure that the relevan... |
| s20(3) | 1371-1376 | (3) In adopting a judge‑led approach, a trib | fork | F9 "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" (assumed, not ruled); encoded: part3-proceedings: s 20(3) the tribunal may direct a party to appear bef... |
| s20(4) | 1381-1382 | (4) A tribunal may, on its own initiative or | encoded | part3-proceedings: s 20(4) the tribunal may summon the person |
| s20(4)(a) | 1384-1384 | (a) give evidence in any proceedings before  | encoded | part3-proceedings: s 20(4) the tribunal may summon the person |
| s20(4)(b) | 1386-1387 | (b) produce any document, record or thing wh | encoded | part3-proceedings: s 20(4) the tribunal may summon the person |
| s20(5) | 1389-1391 | (5) A tribunal may inquire into any matter w | encoded | part3-proceedings: s 20(5) the tribunal may inquire into the matter |
| s20(6) | 1393-1396 | (6) When deciding any claim for employment a | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 20(6) the tribunal may take into account the tripar... |
| s20(7) | 1400-1401 | (7) When deciding any claim involving a wron | encoded | part3-proceedings: s 20(7)(a) the tribunal is to have regard to the trip...; part3-proceedings: s 20(7)(b) the tribunal is to calculate the compensat... |
| s20(7)(a) | 1403-1404 | (a) is to have regard to the tripartite guid | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 20(7)(a) the tribunal is to have regard to the trip...; part3-proceedings: s 20(7)(b) the tribunal is to calculate the compensat... |
| s20(7)(b) | 1406-1408 | (b) if any compensation is claimed, is to ca | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 20(7)(b) the tribunal is to calculate the compensat... |
| s20(8) | 1412-1416 | (8) To avoid doubt, if any party to any proc | encoded | part3-proceedings: s 20(8) the tribunal may hear the claim and make its ... |
| s21/heading | 1418-1418 | Evidence | inert | reason 1 not operative: marginal heading of a section |
| s21(1) | 1420-1420 | 21.—(1) A tribunal — | encoded | part3-proceedings: s 21(1)(a) the tribunal is not bound by the rules of ...; part3-proceedings: s 21(1)(b) the tribunal may inform itself on any matt... |
| s21(1)(a) | 1422-1423 | (a) is not bound by the rules of evidence in | encoded | part3-proceedings: s 21(1)(a) the tribunal is not bound by the rules of ...; part3-proceedings: s 21(1)(b) the tribunal may inform itself on any matt... |
| s21(1)(b) | 1425-1426 | (b) may inform itself on any matter in any m | encoded | part3-proceedings: s 21(1)(b) the tribunal may inform itself on any matt... |
| s21(2) | 1431-1436 | (2) A tribunal may draw any inferences that  | encoded | part3-proceedings: s 21(2) the tribunal may draw any inference it thinks...; part3-proceedings: s 21(2) the inference may include that unavailable ev... |
| s21(3) | 1440-1441 | (3) Subject to subsection (4), evidence tend | encoded | part3-proceedings: s 21(3) the evidence need not be given on oath or aff... |
| s21(4) | 1443-1443 | (4) A tribunal may — | encoded | part3-proceedings: s 21(4)(a) the tribunal may require evidence to be gi...; part3-proceedings: s 21(4)(b) the tribunal may administer an oath or aff... |
| s21(4)(a) | 1445-1447 | (a) require the whole or any part of any evi | encoded | part3-proceedings: s 21(4)(a) the tribunal may require evidence to be gi...; part3-proceedings: s 21(4)(b) the tribunal may administer an oath or aff... |
| s21(4)(b) | 1449-1449 | (b) for that purpose, administer an oath or  | encoded | part3-proceedings: s 21(4)(b) the tribunal may administer an oath or aff... |
| s21(5) | 1451-1453 | (5) A tribunal may, on its own initiative, s | encoded | part3-proceedings: s 21(5) the tribunal may seek other evidence and make... |
| s21(6) | 1455-1457 | (6) All evidence and information obtained by | encoded | part3-proceedings: s 21(6) the evidence and information must be disclose...; part3-proceedings: s 21(6) the tribunal's duty to disclose the evidence ... |
| s21(7) | 1459-1460 | (7) A tribunal may require any written evide | encoded | part3-proceedings: s 21(7) the tribunal may require written evidence to ... |
| s21(8) | 1462-1463 | (8) A tribunal need not keep a record of the | encoded | part3-proceedings: s 21(8) the tribunal need not keep a record of the ev...; part3-proceedings: s 21(8)(a) the tribunal must make a summary of the fa...; +3 more |
| s21(8)(a) | 1465-1466 | (a) a summary of the facts and issues in dis | encoded | part3-proceedings: s 21(8) the tribunal need not keep a record of the ev...; part3-proceedings: s 21(8)(a) the tribunal must make a summary of the fa...; +3 more |
| s21(8)(b) | 1468-1468 | (b) notes of the proceedings. | encoded | part3-proceedings: s 21(8) the tribunal need not keep a record of the ev...; part3-proceedings: s 21(8)(b) the tribunal must make notes of the procee...; +1 more |
| s22/heading | 1470-1470 | Orders of tribunal | inert | reason 1 not operative: marginal heading of a section |
| s22(1) | 1471-1473 | 22.—(1) A tribunal may determine a claim wit | encoded | part3-proceedings: s 22(1) the tribunal may make the order |
| s22(1)(a) | 1474-1474 | (a) an order requiring a party to pay money  | encoded | part3-proceedings: s 22(1) the tribunal may make the order |
| s22(1)(b) | 1475-1475 | (b) an order dismissing the whole or any par | encoded | part3-proceedings: s 22(1) the tribunal may make the order |
| s22(1)(c) | 1480-1480 | (c) an order requiring a party to pay costs  | encoded | part3-proceedings: s 22(1) the tribunal may make the order |
| s22(1)(d) | 1482-1483 | (d) an order requiring an employer to reinst | encoded | part3-proceedings: s 22(1) the tribunal may make the order |
| s22(2) | 1487-1488 | (2) In deciding whether to make an order und | encoded | part3-proceedings: s 22(2) the tribunal may take the matter into account... |
| s22(2)(a) | 1490-1490 | (a) whether the claim was frivolous or vexat | encoded | part3-proceedings: s 22(2) the tribunal may take the matter into account... |
| s22(2)(b) | 1492-1495 | (b) whether a party without reasonable excus | encoded | part3-proceedings: s 22(2) the tribunal may take the matter into account... |
| s22(2)(c) | 1497-1499 | (c) whether any party without reasonable exc | encoded | part3-proceedings: s 22(2) the tribunal may take the matter into account... |
| s22(3) | 1501-1502 | (3) A tribunal’s order under subsection (1)  | encoded | part3-proceedings: s 22(3) the order is subject to any conditions the tr... |
| s22(4) | 1504-1508 | (4) The total amount of money that a tribuna | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-proceedings: s 22(4) the total ordered to be paid for contractual ... |
| s22(5) | 1512-1516 | (5) The total amount of money that a tribuna | fork | F11 "(if any)": a total of nothing against a limit that is not known; encoded: part3-proceedings: s 22(5) the total ordered to be paid for wrongful dis... |
| s22(6) | 1520-1520 | (6) To avoid doubt — | encoded | part3-proceedings: s 22(6)(a) the amount of money ordered under subsecti... |
| s22(6)(a) | 1522-1524 | (a) any amount of money that a tribunal orde | encoded | part3-proceedings: s 22(6)(a) the amount of money ordered under subsecti... |
| s22(6)(b) | 1526-1534 | (b) where a tribunal orders a party to pay a | encoded | part3-proceedings: s 22(6)(b) the part of the payment applied to the amo...; part3-proceedings: s 22(6)(b) the part of the payment applied to the cos... |
| s22(7) | 1536-1538 | (7) Where a tribunal does not have jurisdict | encoded | part3-proceedings: s 22(7) the claim or the part must be dismissed for l... |
| s22(8) | 1540-1546 | (8) A tribunal may, instead of determining a | encoded | part3-proceedings: s 22(8) the kind of mediation the tribunal may refer ... |
| s22(9) | 1548-1550 | (9) A tribunal may, when making a referral u | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-proceedings: s 22(9) the tribunal may order the parties to attend ... |
| s22(10) | 1552-1556 | (10) A tribunal may correct an order made by | fork | F7 how the 14 days "after" the date the order is made are counted; encoded: part3-proceedings: s 22(10) the last day on which the tribunal may make ...; part3-proceedings: s 22(10) the tribunal may make the correction; +1 more |
| s22(10)(a) | 1558-1558 | (a) a clerical mistake; | encoded | part3-proceedings: s 22(10) the tribunal may make the correction |
| s22(10)(b) | 1560-1560 | (b) an error arising from an accidental slip | encoded | part3-proceedings: s 22(10) the tribunal may make the correction |
| s22(10)(c) | 1562-1564 | (c) a material miscalculation of figures, or | encoded | part3-proceedings: s 22(10) the tribunal may make the correction |
| s22(10)(d) | 1566-1566 | (d) a defect of form. | encoded | part3-proceedings: s 22(10) the tribunal may make the correction |
| s22(11) | 1568-1570 | (11) The tribunal may make the correction in | encoded | part3-proceedings: s 22(11) the tribunal may make the correction on its ... |
| s22(12) | 1572-1574 | (12) Every order made by a tribunal under su | encoded | part3-proceedings: s 22(12) the order may be enforced in the same manner... |
| div4 | 1579-1579 | Division 4 — Appeals | inert | reason 1 not operative: Division heading |
| s23/heading | 1581-1581 | Appeal to General Division of High Court | inert | reason 1 not operative: marginal heading of a section |
| s23(1) | 1583-1585 | 23.—(1) Any party to proceedings before a tr | encoded | part3-appeals: s 23(1) the party may appeal to the General Division ...; part3-appeals: s 23(1) the court is the one to which the party may a...; +1 more |
| s23(1)(a) | 1587-1587 | (a) on any ground involving a question of la | encoded | part3-appeals: s 23(1) the party may appeal to the General Division ...; part3-appeals: s 23(1) and (2) an appeal lies to the General Divisio... |
| s23(1)(b) | 1589-1590 | (b) on the ground that the claim was outside | encoded | part3-appeals: s 23(1) the party may appeal to the General Division ...; part3-appeals: s 23(1) and (2) an appeal lies to the General Divisio... |
| s23(2) | 1594-1595 | (2) An appeal lies to the General Division o | encoded | part3-appeals: s 23(2) the condition that a District Court gives per...; part3-appeals: s 23(1) and (2) an appeal lies to the General Divisio... |
| s23(3) | 1601-1604 | (3) Where the only reason for appealing agai | encoded | part3-appeals: s 23(3)(a) a District Court may extend the time under...; part3-appeals: s 23(3)(b) a District Court may remit the matter to a... |
| s23(3)(a) | 1606-1607 | (a) extend the time under section 22(10) for | encoded | part3-appeals: s 23(3)(a) a District Court may extend the time under...; part3-appeals: s 23(3)(b) a District Court may remit the matter to a... |
| s23(3)(b) | 1609-1612 | (b) remit the matter to a tribunal for the c | encoded | part3-appeals: s 23(3)(b) a District Court may remit the matter to a... |
| s23(4) | 1616-1616 | (4) Each of the following is final and is no | encoded | part3-appeals: s 23(4) the order is final and is not subject to any ... |
| s23(4)(a) | 1618-1619 | (a) any order of a District Court giving or  | encoded | part3-appeals: s 23(4) the order is final and is not subject to any ... |
| s23(4)(b) | 1623-1626 | (b) any order of a District Court extending  | encoded | part3-appeals: s 23(4) the order is final and is not subject to any ... |
| s23(4)(c) | 1628-1629 | (c) any order of a District Court remitting  | encoded | part3-appeals: s 23(4) the order is final and is not subject to any ... |
| s24/heading | 1634-1634 | Appeal does not operate as stay of execution | inert | reason 1 not operative: marginal heading of a section |
| s24(1) | 1636-1639 | 24.—(1) An appeal against an order made by a | encoded | part3-appeals: s 24(1) the appeal by itself operates as a stay of ex...; part3-appeals: s 24(1) execution or enforcement of the order is stay... |
| s24(2) | 1645-1650 | (2) A District Court or the General Division | encoded | part3-appeals: s 24(2) the court may direct that a stay be subject t... |
| s24(3) | 1656-1658 | (3) Any order or direction of a District Cou | encoded | part3-appeals: s 24(3) the order or direction is final and is not su... |
| s24(4) | 1662-1664 | (4) The General Division of the High Court m | encoded | part3-appeals: s 24(4) the conditions for the General Division of th... |
| s24(4)(a) | 1666-1667 | (a) a District Court has given under section | encoded | part3-appeals: s 24(4) the conditions for the General Division of th... |
| s24(4)(b) | 1671-1673 | (b) no application was made to any District  | encoded | part3-appeals: s 24(4) the conditions for the General Division of th... |
| s25/heading | 1679-1679 | Powers of General Division of High Court on  | inert | reason 1 not operative: marginal heading of a section |
| s25(1) | 1680-1682 | 25.—(1) On an appeal against an order made b | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(1)(a) | 1683-1683 | (a) dismiss the appeal; | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(1)(b) | 1684-1684 | (b) allow the appeal and set aside or vary t | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(1)(c) | 1689-1692 | (c) remit the matter to the tribunal for rec | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(2) | 1696-1698 | (2) The General Division of the High Court m | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(2)(a) | 1700-1701 | (a) reverse or vary any determination made b | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(2)(b) | 1703-1703 | (b) receive further evidence. | encoded | part3-appeals: s 25 the General Division of the High Court may take ... |
| s25(3) | 1707-1711 | (3) When deciding an appeal against an order | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-appeals: s 25(3) the General Division of the High Court may ta... |
| s25(4) | 1715-1717 | (4) When deciding an appeal against an order | encoded | part3-appeals: s 25(4)(a) the General Division of the High Court is ...; part3-appeals: s 25(4)(b) the General Division of the High Court is ... |
| s25(4)(a) | 1719-1720 | (a) is to have regard to the tripartite guid | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-appeals: s 25(4)(a) the General Division of the High Court is ...; part3-appeals: s 25(4)(b) the General Division of the High Court is ... |
| s25(4)(b) | 1722-1724 | (b) if any compensation is claimed, is to ca | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part3-appeals: s 25(4)(b) the General Division of the High Court is ... |
| s26/heading | 1728-1728 | Finality of decision of General Division of  | inert | reason 1 not operative: marginal heading of a section |
| s26 | 1730-1731 | 26. Any judgment, order or direction of the  | encoded | part3-appeals: s 26 the judgment, order or direction of the General ... |
| s26(a) | 1733-1733 | (a) an appeal against an order made by a tri | encoded | part3-appeals: s 26 the judgment, order or direction of the General ... |
| s26(b) | 1735-1736 | (b) an application for a stay of execution o | encoded | part3-appeals: s 26 the judgment, order or direction of the General ... |
| s27/heading | 1744-1744 | Burden of proof | inert | reason 1 not operative: marginal heading of a section |
| s27(1) | 1746-1748 | 27.—(1) In any proceedings under this Act be | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(1)(a) | 1750-1751 | (a) an allegation that the person is not the | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(1)(b) | 1753-1755 | (b) an allegation that the person is not a p | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(1)(b)(i) | 1757-1757 | (i) the Child Development Co‑Savings Act 200 | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(1)(b)(ii) | 1759-1759 | (ii) the Employment Act 1968; | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(1)(b)(iii) | 1761-1761 | (iii) the Retirement and Re‑employment Act 1 | encoded | part3-appeals: s 27(1) the person who makes the allegation bears the... |
| s27(2) | 1765-1766 | (2) In any proceedings under this Act before | encoded | part3-appeals: s 27(2)(a) the employer bears the burden of proving t...; part3-appeals: s 27(2)(b) the employer bears the burden of proving t...; +2 more |
| s27(2)(a) | 1768-1773 | (a) where an employee is dismissed without n | encoded | part3-appeals: s 27(2)(a) the employer bears the burden of proving t...; part3-appeals: s 27(2)(b) the employer bears the burden of proving t...; +2 more |
| s27(2)(b) | 1775-1780 | (b) where an employee is dismissed with noti | encoded | part3-appeals: s 27(2)(b) the employer bears the burden of proving t...; part3-appeals: s 27(2)(c) the employer bears the burden of proving t...; +1 more |
| s27(2)(c) | 1782-1788 | (c) where a notice of dismissal is given to  | encoded | part3-appeals: s 27(2)(c) the employer bears the burden of proving t...; part3-appeals: s 27(2)(d) the employer bears the burden of proving t... |
| s27(2)(d) | 1793-1803 | (d) where a notice of dismissal is given to  | encoded | part3-appeals: s 27(2)(d) the employer bears the burden of proving t... |
| part4 | 1807-1809 | PART 4 | inert | reason 1 not operative: Part heading |
| s28/heading | 1811-1811 | Restriction on contracting out | inert | reason 1 not operative: marginal heading of a section |
| s28 | 1813-1814 | 28. Any provision in any agreement (whether  | encoded | part4-miscellaneous: s 28 the date on which the agreement was made does no...; part4-miscellaneous: s 28 the provision in the agreement is void to that e... |
| s28(a) | 1816-1816 | (a) to exclude or limit the jurisdiction of  | encoded | part4-miscellaneous: s 28 the provision in the agreement is void to that e... |
| s28(b) | 1818-1818 | (b) to prevent a person from — | encoded | part4-miscellaneous: s 28 the provision in the agreement is void to that e... |
| s28(b)(i) | 1820-1820 | (i) submitting a mediation request; or | encoded | part4-miscellaneous: s 28 the provision in the agreement is void to that e... |
| s28(b)(ii) | 1822-1823 | (ii) making a claim, an application or an ap | encoded | part4-miscellaneous: s 28 the provision in the agreement is void to that e... |
| s29/heading | 1825-1825 | Disclosure of information | inert | reason 1 not operative: marginal heading of a section |
| s29(1) | 1827-1831 | 29.—(1) Despite sections 4 and 18, the Commi | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(a) | 1833-1834 | (a) is necessary for or in connection with t | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(b) | 1836-1837 | (b) is necessary for providing financial or  | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(c) | 1842-1843 | (c) is made to assist a law enforcement agen | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(d) | 1845-1846 | (d) is made to a public agency for the purpo | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(e) | 1848-1849 | (e) is made to a public agency, and is neces | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(1)(f) | 1851-1852 | (f) is made for any other purpose that may b | encoded | part4-miscellaneous: s 29(1) the person may disclose the information |
| s29(2) | 1854-1855 | (2) Despite section 18, a tribunal magistrat | encoded | part4-miscellaneous: s 29(2) the person may publish the information |
| s29(3) | 1859-1859 | (3) In this section — | encoded | part4-miscellaneous: s 29(3) the body is a law enforcement agency |
| s29(3)/“law enforcement agency” | 1861-1863 | “law enforcement agency” means any authority | encoded | part4-miscellaneous: s 29(3) the body is a law enforcement agency |
| s29(3)/“public agency” | 1865-1865 | “public agency” means — | encoded | part4-miscellaneous: s 29(3) the body is a public agency |
| s29(3)/“public agency”(a) | 1867-1868 | (a) the Government, including any ministry,  | encoded | part4-miscellaneous: s 29(3) the body is a public agency |
| s29(3)/“public agency”(b) | 1870-1872 | (b) any statutory body or tribunal that is p | encoded | part4-miscellaneous: s 29(3) the body is a public agency |
| s30/heading | 1874-1874 | Protection from personal liability | inert | reason 1 not operative: marginal heading of a section |
| s30(1) | 1876-1877 | 30.—(1) A tribunal magistrate has and enjoys | encoded | part4-miscellaneous: s 30(1) the person has the same protection that a Mag... |
| s30(2) | 1879-1880 | (2) A Registrar, when exercising the jurisdi | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part4-miscellaneous: s 30(2) the Registrar has the same protection as a tr... |
| s30(3) | 1882-1886 | (3) No liability shall lie personally agains | encoded | part4-miscellaneous: s 30(3) no liability lies personally against the person |
| s31/heading | 1891-1891 | Public servants | inert | reason 1 not operative: marginal heading of a section |
| s31(1) | 1893-1895 | 31.—(1) Every approved mediator, when carryi | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part4-miscellaneous: s 31(1) the approved mediator is deemed to be a publi... |
| s31(2) | 1897-1899 | (2) Every authorised person, when carrying o | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part4-miscellaneous: s 31(2) the authorised person is deemed to be a publi... |
| s32/heading | 1901-1901 | Amendment of Schedules | inert | reason 1 not operative: marginal heading of a section |
| s32(1) | 1903-1904 | 32.—(1) The Minister may, by order in the Ga | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to amend any Schedule, with savings and transitional provisions; stated gap: no function, the Schedules are encoded as they stand in the text, and an order would change the answers |
| s32(2) | 1908-1911 | (2) The Minister may, in an order made under | inert | reason 2 machinery: the Minister's power, by order in the Gazette, to amend any Schedule, with savings and transitional provisions; stated gap: no function, the Schedules are encoded as they stand in the text, and an order would change the answers |
| s33/heading | 1913-1913 | Rules of Court | inert | reason 1 not operative: marginal heading of a section |
| s33(1) | 1915-1917 | 33.—(1) The Rules Committee appointed under  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a) | 1919-1919 | (a) to regulate and prescribe — | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i) | 1921-1921 | (i) the procedure and practice to be followe | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(A) | 1923-1926 | (A) in an application under section 7(2) to  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(B) | 1928-1931 | (B) in an application under section 7(4) to  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(C) | 1933-1933 | (C) in the tribunals and the Registry; | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(D) | 1935-1946 | (D) in an application under section 17(1) to | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(E) | 1948-1950 | (E) in an appeal to the General Division of  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(F) | 1952-1956 | (F) in an application to a District Court fo | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(i)(G) | 1960-1964 | (G) in an application to the General Divisio | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(a)(ii) | 1968-1969 | (ii) any matters incidental to or relating t | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(b) | 1971-1971 | (b) to provide for the enforcement of orders | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(c) | 1973-1974 | (c) to provide for fees and costs for the pr | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(1)(d) | 1976-1977 | (d) to prescribe any matters required by thi | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2) | 1981-1982 | (2) Without limiting subsection (1), the Rul | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(a) | 1984-1986 | (a) the part of the business and the jurisdi | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(b) | 1991-1993 | (b) the form and content of documents to be  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(c) | 1995-1997 | (c) the manner in which and time within whic | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(d) | 1999-2001 | (d) the functions, powers and duties of the  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(d)(i) | 2003-2003 | (i) the service of documents and giving of n | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(d)(ii) | 2005-2006 | (ii) the enlargement or abridgement of time  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(d)(iii) | 2008-2008 | (iii) the conduct of proceedings; | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(e) | 2010-2013 | (e) the manner in which, and the time within | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(f) | 2015-2015 | (f) the withdrawal and amendment of claims; | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(g) | 2017-2018 | (g) the summoning of witnesses and the payme | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(h) | 2020-2024 | (h) the means by which particular facts may  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(i) | 2026-2026 | (i) the transfer of proceedings from a tribu | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(j) | 2028-2028 | (j) the joinder of parties in proceedings be | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(k) | 2030-2032 | (k) the cases in which a person absent, but  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(l) | 2034-2036 | (l) the circumstances in which an order of a | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(m) | 2041-2044 | (m) the circumstances in which any decision, | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(n) | 2046-2049 | (n) the circumstances in which any decision, | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(o) | 2051-2053 | (o) the scales of allowances, costs and fees | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(p) | 2055-2057 | (p) the fees to be charged for anything done | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(q) | 2059-2060 | (q) the waiver, refund or remission, whether | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(2)(r) | 2062-2065 | (r) the circumstances (in addition to those  | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(3) | 2069-2072 | (3) The Rules of Court made under this secti | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s33(4) | 2074-2075 | (4) All Rules of Court made under this secti | inert | reason 2 machinery: the Rules Committee's power to make Rules of Court; stated gap: no function, and what the Rules prescribe arrives in the encoding as inputs |
| s34/heading | 2077-2077 | Regulations | inert | reason 1 not operative: marginal heading of a section |
| s34(1) | 2078-2078 | 34.—(1) The Minister may make regulations — | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(a) | 2079-2079 | (a) for carrying out the purposes and provis | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(b) | 2080-2081 | (b) to prescribe how compensation is to be c | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(c) | 2086-2088 | (c) to provide for the fees to be charged fo | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(d) | 2090-2092 | (d) to provide for the waiver, refund or rem | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(e) | 2094-2097 | (e) to exempt any person or class of persons | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(f) | 2099-2102 | (f) to exclude any specified employment disp | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(g) | 2104-2107 | (g) to provide for the service of documents, | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(1)(h) | 2109-2110 | (h) to prescribe any matters required by thi | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s34(2) | 2114-2115 | (2) The powers conferred by this section do  | inert | reason 2 machinery: the Minister's power to make regulations; stated gap: no function, and what the regulations prescribe arrives in the encoding as inputs |
| s35/heading | 2117-2117 | Tripartite guidelines on wrongful dismissal | inert | reason 1 not operative: marginal heading of a section |
| s35(1) | 2119-2120 | 35.—(1) The Minister may issue guidelines on | inert | reason 2 machinery: the Minister's power to issue guidelines on what constitutes wrongful dismissal; stated gap: no function, and the guidelines themselves are not among the sources (s 35(2), which gives them effect, is encoded) |
| s35(2) | 2124-2126 | (2) Upon the publication of those guidelines | fork | F12 "when", "upon" or "whenever" read as "where" (ruled, second ruling of 2026-11-05, (c)); decided here to be a condition and not a description of the occasion; encoded: part4-miscellaneous: s 35(2) regard may be had to the guidelines for the p... |
| sch1 | 2135-2140 | FIRST SCHEDULE | inert | reason 1 not operative: heading, sections referred to and title of the First Schedule |
| sch1/item1 | 2142-2142 | 1. Allowance (however described in the contr | encoded | schedules: sch 1 item number of |
| sch1/item2 | 2143-2143 | 2. Annual wage supplement | encoded | schedules: sch 1 item number of |
| sch1/item3 | 2144-2144 | 3. Bonus payment | encoded | schedules: sch 1 item number of |
| sch1/item4 | 2145-2145 | 4. Commission | encoded | schedules: sch 1 item number of |
| sch1/item5 | 2147-2147 | 5. Deduction from salary | encoded | schedules: sch 1 item number of |
| sch1/item6 | 2148-2148 | 6. Employment assistance payment | encoded | schedules: sch 1 item number of |
| sch1/item7 | 2149-2149 | 7. Incentive payment (however described in t | encoded | schedules: sch 1 item number of |
| sch1/item8 | 2150-2150 | 8. Medical benefit | encoded | schedules: sch 1 item number of |
| sch1/item9 | 2151-2151 | 9. Overtime payment | encoded | schedules: sch 1 item number of |
| sch1/item10 | 2153-2153 | 10. Pay for extra work | encoded | schedules: sch 1 item number of |
| sch1/item11 | 2154-2154 | 11. Pay for public holiday or paid leave | encoded | schedules: sch 1 item number of |
| sch1/item12 | 2155-2155 | 12. Pay for work on public holiday | encoded | schedules: sch 1 item number of |
| sch1/item13 | 2156-2156 | 13. Pay for work on rest day | encoded | schedules: sch 1 item number of |
| sch1/item14 | 2158-2158 | 14. Payment in lieu of unconsumed leave | encoded | schedules: sch 1 item number of |
| sch1/item15 | 2159-2159 | 15. Reimbursement for expenses incurred whil | encoded | schedules: sch 1 item number of |
| sch1/item16 | 2160-2160 | 16. Salary | encoded | schedules: sch 1 item number of |
| sch1/item17 | 2161-2161 | 17. Salary in lieu of notice of termination | encoded | schedules: sch 1 item number of |
| sch1/item18 | 2162-2162 | 18. Termination benefit (including retrenchm | encoded | schedules: sch 1 item number of |
| sch2 | 2164-2169 | SECOND SCHEDULE | inert | reason 1 not operative: heading, sections referred to and title of the Second Schedule |
| sch2/group2171 | 2171-2171 | Matters under Child Development Co‑Savings A | inert | reason 1 not operative: group heading in the Second Schedule |
| sch2/item1 | 2173-2180 | 1. Female employee’s entitlement to paid mat | encoded | schedules: sch 2 item number of |
| sch2/item2 | 2182-2184 | 2. Female employee’s entitlement to paid ado | encoded | schedules: sch 2 item number of |
| sch2/item3 | 2186-2187 | 3. Employee’s entitlement to paid childcare  | encoded | schedules: sch 2 item number of |
| sch2/item4 | 2189-2190 | 4. Employee’s entitlement to paid extended c | encoded | schedules: sch 2 item number of |
| sch2/item4A | 2192-2193 | 4A. Employee’s entitlement to paid shared pa | encoded | schedules: sch 2 item number of |
| sch2/item5 | 2197-2198 | 5. Male employee’s entitlement to paid share | encoded | schedules: sch 2 item number of |
| sch2/item6 | 2200-2201 | 6. Male employee’s entitlement to paid pater | encoded | schedules: sch 2 item number of |
| sch2/group2203 | 2203-2204 | Matters under Child Development Co‑Savings ( | inert | reason 1 not operative: group heading in the Second Schedule |
| sch2/item7 | 2206-2208 | 7. Female part‑time employee’s entitlement t | encoded | schedules: sch 2 item number of |
| sch2/item8 | 2210-2212 | 8. Part‑time employee’s entitlement to paid  | encoded | schedules: sch 2 item number of |
| sch2/item9 | 2214-2216 | 9. Part‑time employee’s entitlement to paid  | encoded | schedules: sch 2 item number of |
| sch2/item10 | 2218-2220 | 10. Female part‑time employee’s entitlement  | encoded | schedules: sch 2 item number of |
| sch2/item10A | 2222-2224 | 10A. Part-time employee’s entitlement to pai | encoded | schedules: sch 2 item number of |
| sch2/item11 | 2228-2235 | 11. Male part‑time employee’s entitlement to | encoded | schedules: sch 2 item number of |
| sch2/item12 | 2237-2239 | 12. Male part‑time employee’s entitlement to | encoded | schedules: sch 2 item number of |
| sch2/group2241 | 2241-2241 | Matters under Employment Act 1968 | inert | reason 1 not operative: group heading in the Second Schedule |
| sch2/item13 | 2243-2245 | 13. Employee’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item14 | 2247-2249 | 14. Employer’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item15 | 2251-2253 | 15. Employee’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item16 | 2255-2257 | 16. Employer’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item17 | 2259-2260 | 17. Employee’s entitlement to payment of sal | encoded | schedules: sch 2 item number of |
| sch2/item18 | 2262-2264 | 18. Employee’s entitlement to recover from t | encoded | schedules: sch 2 item number of |
| sch2/item19 | 2266-2268 | 19. Employee’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item20 | 2270-2271 | 20. Employee’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item21 | 2273-2274 | 21. Employee’s entitlement to payment under  | encoded | schedules: sch 2 item number of |
| sch2/item22 | 2276-2278 | 22. Entitlement of employee, to whom section | encoded | schedules: sch 2 item number of |
| sch2/item23 | 2280-2281 | 23. Employee’s entitlement to paid annual le | encoded | schedules: sch 2 item number of |
| sch2/item24 | 2283-2290 | 24. Entitlement, under section 57 of the Emp | encoded | schedules: sch 2 item number of |
| sch2/item25 | 2292-2294 | 25. Entitlement, under section 65 of the Emp | encoded | schedules: sch 2 item number of |
| sch2/item26 | 2296-2298 | 26. Female employee’s entitlement to paid ma | encoded | schedules: sch 2 item number of |
| sch2/item27 | 2300-2303 | 27. Entitlement of person nominated by femal | encoded | schedules: sch 2 item number of |
| sch2/item28 | 2305-2306 | 28. Employee’s entitlement to paid childcare | encoded | schedules: sch 2 item number of |
| sch2/item29 | 2308-2309 | 29. Employee’s entitlement to paid holiday ( | encoded | schedules: sch 2 item number of |
| sch2/item30 | 2311-2313 | 30. Employee’s entitlement under section 88( | encoded | schedules: sch 2 item number of |
| sch2/item31 | 2315-2317 | 31. Employee’s entitlement under section 88( | encoded | schedules: sch 2 item number of |
| sch2/item32 | 2319-2321 | 32. Employee’s entitlement to paid sick leav | encoded | schedules: sch 2 item number of |
| sch2/group2323 | 2323-2323 | Matters under Employment (Part‑Time Employee | inert | reason 1 not operative: group heading in the Second Schedule |
| sch2/item33 | 2325-2327 | 33. Part‑time employee’s entitlement to paym | encoded | schedules: sch 2 item number of |
| sch2/item34 | 2329-2331 | 34. Part‑time employee’s entitlement to paym | encoded | schedules: sch 2 item number of |
| sch2/item35 | 2333-2335 | 35. Part‑time employee’s entitlement to paym | encoded | schedules: sch 2 item number of |
| sch2/item36 | 2337-2343 | 36. Part‑time employee’s entitlement to paid | encoded | schedules: sch 2 item number of |
| sch2/item37 | 2345-2348 | 37. Part‑time employee’s entitlement under r | encoded | schedules: sch 2 item number of |
| sch2/item38 | 2350-2353 | 38. Part‑time employee’s entitlement under r | encoded | schedules: sch 2 item number of |
| sch2/item39 | 2355-2358 | 39. Part‑time employee’s entitlement to allo | encoded | schedules: sch 2 item number of |
| sch2/item40 | 2360-2361 | 40. Part‑time employee’s entitlement to paid | encoded | schedules: sch 2 item number of |
| sch2/item41 | 2363-2366 | 41. Part‑time employee’s entitlement to allo | encoded | schedules: sch 2 item number of |
| sch2/item42 | 2368-2369 | 42. Part‑time employee’s entitlement to paid | encoded | schedules: sch 2 item number of |
| sch2/item43 | 2371-2373 | 43. Part‑time employee’s entitlement to paid | encoded | schedules: sch 2 item number of |
| sch2/item44 | 2375-2377 | 44. Female part‑time employee’s entitlement  | encoded | schedules: sch 2 item number of |
| sch2/group2379 | 2379-2379 | Matters under Retirement and Re‑employment A | inert | reason 1 not operative: group heading in the Second Schedule |
| sch2/item45 | 2381-2382 | 45. Employee’s entitlement to employment ass | encoded | schedules: sch 2 item number of |
| sch3 | 2386-2390 | THIRD SCHEDULE | inert | reason 1 not operative: heading, sections referred to and title of the Third Schedule |
| sch3/item1 | 2392-2399 | 1. Any dispute, in relation to which an empl | encoded | schedules: sch 3 item number of |
| sch3/item2 | 2401-2405 | 2. Any dispute, in relation to which a femal | encoded | schedules: sch 3 item number of |
| sch3/item3 | 2407-2413 | 3. Any dispute, in relation to which a femal | encoded | schedules: sch 3 item number of |
| sch4 | 2417-2421 | FOURTH SCHEDULE | inert | reason 1 not operative: heading, sections referred to and title of the Fourth Schedule |
| sch4/item1 | 2423-2424 | 1. An employer’s obligations under sections  | encoded | schedules: sch 4 item number of |
| sch4/item2 | 2426-2428 | 2. An employer’s obligations under paragraph | encoded | schedules: sch 4 item number of |
| sch4/item3 | 2430-2431 | 3. An employer’s obligations under paragraph | encoded | schedules: sch 4 item number of |
| history | 2436-2526 | LEGISLATIVE HISTORY | inert | reason 1 not operative: the Legislative History says of itself that it is not part of the Act |
| comparative | 2529-2582 | COMPARATIVE TABLE | inert | reason 1 not operative: the Comparative Table only locates the old numbering; its "Omitted as having had effect" lines concern provisions of the earlier edition, not text of this Act |

## Forks

The two rulings of 2026-11-04 below are printed word for word from the brief and bind this row.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**First ruling of 2026-11-05 (Meng), on how a `NOTHING` is told from a `JUST FALSE` where the text limits a rule by its own wording.**
Meng's ruling, verbatim: "i agree with your lean: no for a and b; nothing for c."
The three parts it speaks of are, in this file, I(a), I(b) and I(c):
- I(a) Where the text fixes a period in its own words ("within", "not later than", "begins from ... until", "not earlier than one year before"), outside the period the answer is `JUST FALSE`.
- I(b) A "where ..." condition that is not met is `JUST FALSE`, like "if".
- I(c) A scope limit with no "only" (a rule given to a stated class or case): outside the scope the answer is `NOTHING`.

Each branch that rests on this ruling carries `[ruled I(a)]`, `[ruled I(b)]` or `[scope limit, ruled I(c)]` in its comment.

**Second ruling of 2026-11-05 (Meng, typed 06:04:54.553Z; recorded in the Commons guide, section 5, in the bullet beginning "Delegated definitions, defences and "until" bars").**
It is given here as it was relayed to me, in four parts called II(a) to II(d):
- II(a) A definition the text itself hands to a list ("... has effect for determining what is ..."): when no head holds, `JUST FALSE`; a bare list with no such hand-off answers `NOTHING`.
- II(b) "It is a defence ... to prove that X": when X is not proved, `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" (never "no defence at all").
- II(c) "when", "upon" and "whenever" count as "where": unmet is `JUST FALSE` (a relative clause such as "upon which" is not a "where").
- II(d) "X does not happen until Y" and "stayed until Y": the bar is its own yes/no question (`JUST TRUE` before Y, `JUST FALSE` after), and the "has it happened" question is never answered yes on the strength of the bar alone (`JUST FALSE` before Y, `NOTHING` after).

Assumed, not ruled, with the second ruling: "in the event of" and "once" count as "where" too (the text has neither word, so no site rests on this); a function that returns a number, a date or a record cannot carry `JUST FALSE`, so a yes/no twin is added where a ruling calls for a no.
Each branch that rests on the second ruling carries `[ruled II(c)]` or `[ruled II(d)]`; the sites are tabulated under "Sites decided by the rulings of 2026-11-05".
What I decided at each site, and why, is in forks F12 (II(c)), F13 (II(d)) and F14 (II(a) and II(b), where I found no site).
The words I extended it to without a ruling ("in adopting", "after" an event, "on the application of", "on the recommendation of") are fork F9.

**Where I hand-gathered a legal effect (E1, option B as guidance for gathering by hand only).**
Each of these is one plain L4 function that gathers the routes to one legal effect; nothing in the language does it, and each section's own answer is still encoded on its own (option C).
- `s 12(1) the tribunal has jurisdiction to hear and determine the claim` gathers the requirements of s 12(2) to (7), with s 15(2)(a) deeming s 12(7) satisfied.
- `s 12(2) the claim is made as the subsection requires` gathers the three routes (a), (b) and (c).
- `s 12(7) the total amount alleged satisfies the conditions` gathers (a) and (b).
- `s 23(1) and (2) an appeal lies to the General Division of the High Court` gathers s 23(1)(a) and (b) with the permission in (2).
- `s 2(1) the dispute is a specified employment dispute` is the aggregator of the three kinds the definition names (contractual, statutory, wrongful dismissal).
- The seat's `Does the tribunal have jurisdiction over my claim` gathers the six per-requirement answers into one call of the layer-1 s 12(1) function.
- Smaller gatherings of the same kind, by hand: `s 3(2) the last day by which the mediation request must be submitted` picks the right paragraph of s 3(2); `s 5(1) to (3)` and `s 19(1) to (3)` gather the rule and its exceptions into one function over who may represent whom.

### The forks

A fork is a place where the text can be read two or more ways with different outcomes.
Each entry gives every reading, the words that license each, the reading taken, and the rows that rest on it.

| id | where | readings and the words that license each | taken | rows |
| --- | --- | --- | --- | --- |
| F1 | s 2(1) `claim`, `claimant`, `respondent`, `employee`, `employer`, `contract of service` (each says "means ... and includes") | (1) closed: "means" fixes the term as the main limb or one of the included items, so a thing outside both is not within the term; JUST FALSE. (2) open: "includes" extends a term, so a thing outside both is not said to be outside it; NOTHING. Licensed by the same sentence: "“employee” means an individual who has entered into and works under a contract of service with an employer, and includes —" | (1), because the brief's rule makes a definition that says "means" the text's own no. A definition that says only "includes" (`mediation`) is open: NOTHING outside | the F1 rows of the coverage table |
| F6 | s 3(2)(b), (d), (e), (f), (g) and s 3(3)(a)(ii): "6 months after", "one month after", "2 months after", "one year after", "one year before" | (1) a date in a shorter month is clamped to that month's last day: 6 months after 31 August 2025 is 28 February 2026 (what `add months` in the `daydate` library does; `builtins.md:228` of the skill says it clamps). (2) a date in a shorter month overflows into the next: 31 February 2026 is 3 March 2026. The Act gives no rule for it, and the Interpretation Act, whose time module was staged and read, has none either: it defines a month as a "calendar month" and answers `NOTHING` for a period of months or years (see Dependencies) | (1). The difference matters only on the last days of 29, 30 and 31-day months | rows s3(2)(b), (d), (e), (f), (g), s3(3)(a)(ii) |
| F7 | s 12(6) "within the prescribed period after the date of issue" and s 22(10) "within 14 days after the date" | (1) the day the certificate is issued, or the order made, is not counted, and the last day is: issued on 1 January, 60 days allowed, last day 2 March 2026. (2) the day itself counts as day 1: last day 1 March. The Act says "after the date" and does not say how days are counted | (1). Section 50(a) of the Interpretation Act excludes the day of the event from a period of days "from" it, which agrees; the staged module counts only "from", and these provisions say "after", so it is not relied on | rows s12(6), s22(10) |
| F8 | s 19(3): "A party who is an individual may be represented by any other individual by regulations made under section 34." | (1) the word "prescribed" is missing from the rendering, so the sentence reads as s 5(3) does: "by any other individual prescribed by regulations made under section 34"; licensed by s 5(3), by s 19(2)(e) ("any other individual prescribed by regulations made under section 34") and by s 19(4), which speaks of the regulations that "may prescribe different individuals" for (2)(e) and (3). (2) the sentence is literal and grants nothing definite, so an individual party's right to be represented by anyone but the persons the Act names is not covered | (1). Under (2) the rows would answer NOTHING where they now answer JUST TRUE for a prescribed individual | row s19(3) |
| F9 | the words "in adopting" (s 20(3)), "as soon as ... after" an event (s 4(1)), "on the application of" (s 7(2)) and "on the recommendation of" (s 9(4)), where each introduces a rule that applies only once something has happened or been asked (for example s 7(2) "A District Court may, on the application of any party to the settlement agreement, ...") | (1) read as "where": the words state the event the rule is about, so when the event has not happened the answer is `JUST FALSE`, as for "when" under II(c). (2) the words only place the rule in a setting or name who sets it going, and are not a condition on it, so when the event has not happened the rule is not spoken to and the answer is `NOTHING` (or, for s 9(4) and s 7(2), a scope limit on the power) | (1). This is **assumed, not ruled**: the second ruling names "when", "upon" and "whenever" and I extended it to these words. The two stretchiest are s 7(2) and s 9(4). If it is (2), these rows move to `NOTHING` | s 4(1), s 7(2), s 9(4), s 20(3) |
| F10 | s 7(4) "within the period prescribed by Rules of Court" | (1) the text fixes the period in its own words, though by reference to Rules of Court that are not among the sources, so outside the period (as the person states it) the answer is `JUST FALSE` (ruled I(a)). (2) a period the text does not state is a fact that points outside the text, so the answer is `NOTHING` | (1), because the person states whether they are within the period and that fact decides; if they do not know, the answer is `NOTHING` | row s7(4) |
| F11 | "(if any)" in s 7(1)(b) and (c), s 12(7)(a) and (b), s 22(4) and (5), and the excess in s 15(1) (for example s 12(7)(a): "every specified contractual dispute (if any) and every specified statutory dispute (if any)") | (1) a total of nothing cannot exceed a limit, so with no dispute of the kind the total is within the limit whatever the limit is, and the excess is nothing. This assumes that no prescribed limit is below nothing. (2) the limit is not known, so the answer is `NOTHING` even for a total of nothing | (1). A positive total against a limit that is not known stays `NOTHING` | rows s7(1)(b), s7(1)(c), s12(7)(a), s12(7)(b), s15(1), s15(1)(a), s15(1)(b), s22(4), s22(5) |
| F12 | "when", "upon" and "whenever" in s 2(2), s 3(5), s 20(2)(a) and (b), s 20(6), s 20(7)(a) and (b), s 22(9), s 25(3), s 25(4)(a) and (b), s 30(2), s 31(1), s 31(2) and s 35(2): "When this Act is applied to a counterclaim", "Upon accepting the mediation request", "A tribunal, when dealing with any claim", "When deciding any claim for employment assistance payment", "when making a referral under subsection (8)", "A Registrar, when exercising the jurisdiction and powers of a tribunal", "Upon the publication of those guidelines in the Gazette" | (1) a condition: the clause names an event or state that the rule is given for, so when it is not met the answer is `JUST FALSE` (ruled II(c)). (2) a description of the occasion: the clause only names the activity in which the body is engaged, and the rule is a scope limit (`NOTHING` outside it, I(c)). Licensed by the same words: the main clause is a duty, a permission, a deeming or a protection that the text gives on that occasion and no other | (1) at all fifteen sites. None is a relative clause ("upon which"), and each function already takes the occasion as its own yes/no input (for s 31(1), s 31(2) and s 30(2) the input joins the class and the occasion, see below). I found no site where the clause merely restates who the subject is. If a site is (2), it moves to `NOTHING` and is one of the F12 rows. Limits: (i) in s 30(2), s 31(1) and s 31(2) the one input says "a Registrar exercising the jurisdiction of a tribunal" or "an approved mediator carrying out the functions of an approved mediator", so a person who is not in the class at all also gets `JUST FALSE` here, where I(c) would give `NOTHING` for the class limit; separating the two needs a second input, which changes the signature. (ii) s 2(2) returns a person, which cannot carry `JUST FALSE`: the twin `s 2(2) a reference to the claimant or the respondent is read as a reference to a party to the counterclaim` says no when the Act is not applied to a counterclaim. (iii) "once" and "in the event of" do not occur in the text. (iv) The other functions that return a date or a kind under a ruled condition (s 7(3)(a), s 7(5)(b)(ii), s 16(4)(b), s 16(6)(b), s 16(8)(b), s 22(8)) answer `NOTHING` when the condition is not met and have no twin; none rests on the second ruling, and the sibling yes/no functions (s 16(4)(a), s 16(6)(a)) carry the no for two of them | s 2(2), s 3(5), s 25(3), s 25(4)(a), s 25(4)(b), s 20(2)(a), s 20(2)(b), s 20(6), s 20(7)(a), s 20(7)(b), s 22(9), s 30(2), s 31(1), s 31(2), s 35(2) |
| F13 | s 16(8)(a) "the claim is stayed until that Minister decides whether to allow" and s 17(4) "execution or enforcement on the tribunal's order is stayed until the proceedings on the counterclaim are concluded" | (1) the stayed function is the bar question of II(d), and "has the stay ended" is a separate question. (2) the stayed function alone, read as "is the claim now stayed or not", answers both. Licensed by the same words: "stayed until Y" says the stay stands until Y and says nothing of what Y does | (1). `s 16(8)(a) the claim is stayed` and `s 17(4) execution or enforcement of the tribunal's order is stayed` already are the bar question: `JUST TRUE` while the stay stands, `JUST FALSE` once the Minister has decided or the proceedings are concluded (or the court has otherwise ordered), and `JUST FALSE` where the "Where" is unmet. New twins: `s 16(8)(a) the stay on the claim has ended` is `JUST FALSE` while the bar stands, `JUST TRUE` only where (c) says in its own words that the employee may proceed (the Minister decided to allow), and `NOTHING` where the Minister decided not to allow (the claim is deemed discontinued under (b) and the text does not say it proceeds); `s 17(4) the stay on execution or enforcement of the tribunal's order has ended` is `JUST FALSE` while the bar stands and `NOTHING` after, because the text does not say that execution then proceeds. The seat has the twin for s 16(8)(a) (`Has the stay on my employment assistance payment claim ended`); the seat has no question on s 17(4) | rows s16(8)(a), s17(4) |
| F14 | s 16(9) "the employer ... cannot defend the claim on the ground that the employee does not satisfy the re-employment eligibility criteria ..., if the employer did not raise this defence during the mediation" (src:1210-1216); and the whole text for II(a) and II(b) | s 16(9) is read as (1) a bar on a ground of defence, with an "if" condition: not a defence that is made out by proving something, so II(b) does not apply, and the wording "this section gives no defence on these facts" is not used. (2) a defence to prove, so that where the employer has not proved it the answer is `JUST FALSE` for that provision's defence. The word "defence" occurs once in the operative text, at that line, and no sentence says "it is a defence ... to prove". Section 27(2) puts a burden of proof on the employer; it does not use the word "defence", and its functions answer whether the burden lies on the employer, so II(b) does not apply there either | (1). The function is unchanged: `JUST FALSE` where the claim is not for employment assistance payment or the employer did raise the defence at the mediation (the "Where" and "if" rules). II(a): no definition in the text is handed to a list by words such as "has effect for determining" (a search of the operative text for "has effect" and "for determining" finds nothing); the four Schedules are titled lists with "Sections ..." cross-references. Whether a sentence such as "means ... any matter specified in the First Schedule" is a hand-off is the judgment call recorded under "Judgment calls" (QC), and I took those definitions as closed "means" definitions (F1) | row s16(9) |

### Open questions

Q1 to Q8 are places where I answer `NOTHING` and the review expected `JUST FALSE`; Q9 is the s 12(3) seat question, where I could not find a `NOTHING` to flip (its row says what I did find); Q10 has the same shape as Q4 and was not raised by the review.
Each is a scope limit with no "only" (ruled I(c) on 2026-11-05), or sits beside one, and Meng's ruling was "nothing for c"; I left each as it is, and each is for a lawyer.
The line "reviewer expected JUST FALSE; open question" is verbatim in the "taken" column of Q1 to Q9; the assertion that shows the answer is named in the last column, and the build of this file fails if the named assertion text is not in the named file.

| id | where | the two answers | taken | rows | asserted in |
| --- | --- | --- | --- | --- | --- |
| Q1 | s 3(3)(a)(iii) (and (i)): "in relation to which all of the following requirements are satisfied" | (1) `NOTHING`: the duty is to list a dispute that meets (i), (ii) and (iii), so a dispute failing (i) or (iii) is outside it, and the text does not say it must not be listed. (2) `JUST FALSE`: the requirements are conditions of the duty, so failing one is the text's no. (The one-year period (ii) is `JUST FALSE` by ruling I(a) either way.) | (1). reviewer expected JUST FALSE; open question | s3(3)(a) | `eca-tests-part2.l4` |
| Q2 | s 12(1): "in relation to which all applicable requirements set out in subsections (2) to (7) are satisfied" | (1) `NOTHING`: the grant is for a claim that meets the requirements, and the text does not say in so many words that the tribunal lacks jurisdiction otherwise. (2) `JUST FALSE`: the requirements are conditions of the jurisdiction. The per-requirement answers (s 12(2) to (7)) are `JUST FALSE` already | (1). reviewer expected JUST FALSE; open question | s12(1) | `eca-cases-seat.l4` |
| Q3 | s 16(3): the bar is for a claim about "a matter specified in item 17 of the First Schedule, or item 13 or 15 of the Second Schedule"; First Schedule item 16 is not among the named items and the clause has no "only" | (1) `NOTHING`: any other matter is outside the bar. (2) `JUST FALSE`: the named items are the whole of it. For a named item whose "if" is unmet the answer is `JUST FALSE` already | (1). reviewer expected JUST FALSE; open question | s16(3) | `eca-tests-part3-jurisdiction.l4` |
| Q4 | s 18(6): "for the avoidance of doubt", subsection (1) does not prevent the tribunal from hearing claims together where conditions are met | (1) `NOTHING`: the clause settles only the case it names. (2) `JUST FALSE`: where the conditions fail, (1) does prevent it | (1). reviewer expected JUST FALSE; open question | s18(6) | `eca-tests-part3-proceedings.l4` |
| Q5 | s 22(10): the tribunal may correct "to the extent necessary to rectify" four kinds of error | (1) `NOTHING`: a correction that is not one of the four things (a change of the merits) is outside the extent, and the clause has no "only". (2) `JUST FALSE`: the extent is the whole of the power. A correction after the 14 days is `JUST FALSE` already (ruled I(a)) | (1). reviewer expected JUST FALSE; open question | s22(10) | `eca-tests-part3-proceedings.l4` |
| Q6 | s 23(1) (two functions) and the seat question `Can I appeal`: an appeal "on the ground" of a question of law or lack of jurisdiction | (1) `NOTHING` on a question of fact: two grounds are granted, with no "only" (s 25(2)(a) bars the High Court from reversing a finding of fact, but s 23 does not say an appeal on fact cannot be brought). (2) `JUST FALSE`: the two grounds are the whole of the right | (1). reviewer expected JUST FALSE; open question | s23(1), s23(1) and (2), seat `Can I appeal` | `eca-cases-seat.l4` |
| Q7 | s 28: a provision is void "to the extent that it purports" to do one of the things named | (1) `NOTHING` for a provision that does something else: the section speaks only of those. (2) `JUST FALSE`: what the section does not name is not void by it | (1). reviewer expected JUST FALSE; open question | s28 | `eca-tests-part4.l4` |
| Q8 | s 30(3): no personal liability for the Commissioner, an authorised individual or an approved mediator, who acts "in good faith and with reasonable care" | (1) `NOTHING` for a person not named, or one who did not so act: the section gives the protection to those and does not say liability lies otherwise. (2) `JUST FALSE`: outside the named persons and the good-faith condition there is no protection | (1). reviewer expected JUST FALSE; open question | s30(3) | `eca-tests-part4.l4` |
| Q9 | the seat question `Is my claim the kind the Act allows` (s 12(3): the claim "must be for either or both" of amounts payable or reinstatement in a wrongful dismissal case) | The layer-1 function `s 12(3) the claim is for what the subsection requires` answers `JUST FALSE` whenever neither limb holds, and on the seat's three yes/no inputs the question never answers `NOTHING`: all eight combinations are asserted. I could not identify the case in which `JUST FALSE` was expected and `NOTHING` given, so I left it as it is | as it is. reviewer expected JUST FALSE; open question | s12(3) | `eca-cases-seat.l4` |
| Q10 | s 7(9): "for the avoidance of doubt", section 30H(3) to (9) of the Industrial Relations Act 1960 applies to a dispute referred for tripartite mediation after a District Court sets the agreement aside | (1) `NOTHING` otherwise: the clause settles only the case it names, the same shape as Q4. (2) `JUST FALSE`. Not raised by the review; I list it because it has the shape of Q4 and I have answered it the same way | (1). Not in the review's list; open question | s7(9) | `eca-tests-part2.l4` |

### Judgment calls

Six questions (QA to QF) have no convention: each site is a judgment call, taken on the text's own words and open to a reviewer's overruling.
I read every site below against its text, and in each the text's own words point the way the code goes, so I changed none; the reason is in the "answer taken" cell, and the same reason serves every line of a question where it is not repeated.
I added no twin function for them.
A question is answered one way across its sites, except where the line gives the reason it differs: under QA, the bar functions (s 16(2), s 16(7), s 17(4)) against the s 24(1) pair; under QC, the "means" definitions, s 12(2)(c) and s 16(4)(a) (`JUST FALSE`) against s 16(3) and s 21(2) (`NOTHING`).
For each I record every site where it arises: the question, the provision, the function, the file and line of the function, the answer my code gives, and the other reading.
The questions, in a line each: QA, a bar with "unless" or "except" where the exception is met; QB, a bare "must" that is not done, in a function that asks whether it was met; QC, a sentence that asks whether something is "listed in" a Schedule, where the text does not say the Schedule "has effect for determining" it; QD, a duty whose "if" or "where" is unmet; QE, "other than X"; QF, a missing event in a ledger.
A duty or a deeming lifted by an exception is not QA: the requirement does not apply and the answer is `JUST FALSE`.
A question that does not arise gets a line saying so; QF is the only one.
The function named on a line is the one the question arises in; the same function can appear under more than one question, and under the open questions and forks above.
One function that the script classes as a "must" requirement, `s 7(6) a condition for setting aside is satisfied` ("the conditions are as follows"), has no bare "must" in it and is not listed under QB.

| question | provision | function | file:line | answer taken | other reading |
| --- | --- | --- | --- | --- | --- |
| QA | s 5(2) and (3): "Except as provided in subsections (2) and (3)" | `s 5(1) to (3) the party may be represented at the mediation by the representative` | `eca-part2-mediation.l4:616` | `JUST TRUE` where (2) or (3) names the representative; (2) and (3) grant in the text's own words ("may be represented"), so the exception permits | `NOTHING` (a lifted bar grants nothing) |
| QA | s 19(2) and (3): "Except as provided in subsections (2) and (3)" | `s 19(1) to (3) the party may be represented before the tribunal by the representative` | `eca-part3-proceedings.l4:182` | `JUST TRUE` where (2) or (3) names the representative; (2) and (3) grant in the text's own words ("may be represented"), so the exception permits | `NOTHING` (a lifted bar grants nothing) |
| QA | s 16(2): "unless the claim is withdrawn, discontinued or dismissed for lack of jurisdiction" | `s 16(2) no proceedings relating to the claim can be commenced in any other court or an Industrial Arbitration Court by either party against the other` | `eca-part3-jurisdiction.l4:776` | `JUST FALSE` for the bar question once the exception is met (the bar does not hold); the function is the bar itself, and once the "unless" is met the text no longer says the bar holds | `NOTHING` (a lifted bar grants nothing) |
| QA | s 16(7): "unless (a) ... and (b) ..." | `s 16(7) the employee cannot lodge a claim for employment assistance payment` | `eca-part3-jurisdiction.l4:976` | `JUST FALSE` for the bar question once (a) and (b) are met; the function is the bar itself, and once the "unless" is met the text no longer says the bar holds | `NOTHING` (a lifted bar grants nothing) |
| QA | s 17(4): "unless that court at any time otherwise orders" | `s 17(4) execution or enforcement of the tribunal's order is stayed` | `eca-part3-jurisdiction.l4:1178` | `JUST FALSE` for the bar question once the court has otherwise ordered; the has-ended twin answers `NOTHING`; the function is the bar of II(d); "stayed until Y" and "unless the court otherwise orders" both end it | `NOTHING` (a lifted bar grants nothing) |
| QA | s 24(1): "unless a District Court or the General Division of the High Court orders otherwise" | `s 24(1) the appeal by itself operates as a stay of execution or enforcement of the order` | `eca-part3-appeals.l4:146` | `NOTHING` when a court has ordered otherwise (the unless lifts the no); the function asks the positive question the text denies, so it is the permission side and a lifted bar grants nothing | `JUST TRUE` (the order makes the appeal operate as a stay), or `JUST FALSE` ("by itself" stays false) |
| QA | s 24(1): the same sentence, as the question whether enforcement is stayed | `s 24(1) execution or enforcement of the order is stayed pending the appeal` | `eca-part3-appeals.l4:162` | `JUST TRUE` when a court has ordered a stay; a different question from the one above: the court's order is the stay, and the text says so by "orders otherwise" | `NOTHING` (a lifted bar grants nothing) |
| QB | s 3(1): "the claimant must submit to the Commissioner a mediation request relating to every specifi" | `s 3(1) the mediation request relates to every specified employment dispute for which the claim will be lodged` | `eca-part2-mediation.l4:59` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 3(2): "The mediation request must be submitted to the Commissioner in the prescribed manner by th" | `s 3(2) the mediation request is submitted by the time` | `eca-part2-mediation.l4:245` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 3(3)(d): "must be accompanied by the prescribed fee for a mediation under this Part" | `s 3(3)(d) the mediation request is accompanied by the prescribed fee` | `eca-part2-mediation.l4:342` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 5(1): "a party to a mediation under this Part (a) must act in person" | `s 5(1) to (3) the party may be represented at the mediation by the representative` | `eca-part2-mediation.l4:616` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 7(1)(a): "the parties to the settlement must enter into a settlement agreement in the form prescribe" | `s 7(1)(a) the settlement agreement is in the form prescribed` | `eca-part2-mediation.l4:802` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 7(1)(d): "the settlement agreement must be signed by or on behalf of each party" | `s 7(1)(d) the settlement agreement is signed by or on behalf of each party` | `eca-part2-mediation.l4:867` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(2)(a): "The claim must be made —" | `s 12(2)(a) the claim is made by an employee in a prescribed class against the employer` | `eca-part3-jurisdiction.l4:227` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(2)(b): "The claim must be made —" | `s 12(2)(b) the claim is made by an employee in a prescribed class against a person liable under section 65 of the Employment Act 1968` | `eca-part3-jurisdiction.l4:248` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(2)(c): "The claim must be made —" | `s 12(2)(c) the claim is made by an employer in a prescribed class against an employee about a matter the paragraph names` | `eca-part3-jurisdiction.l4:287` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(2): "The claim must be made —" | `s 12(2) the claim is made as the subsection requires` | `eca-part3-jurisdiction.l4:332` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(3): "The claim must be for either or both of the following" | `s 12(3) the claim is for what the subsection requires` | `eca-part3-jurisdiction.l4:352` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(4): "Each amount alleged to be payable under the claim must relate to a specified employment di" | `s 12(4) each amount alleged to be payable relates to a specified employment dispute` | `eca-part3-jurisdiction.l4:365` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(5): "The claim must be supported by a claim referral certificate issued in respect of every spe" | `s 12(5) the claim is supported by a claim referral certificate for every specified employment dispute` | `eca-part3-jurisdiction.l4:379` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(6): "The claim must be lodged with the tribunal within the prescribed period after the date of " | `s 12(6) the claim is lodged within the prescribed period after the certificate was issued` | `eca-part3-jurisdiction.l4:394` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 12(7): "The total amount alleged to be payable under the claim must satisfy the following conditio" | `s 12(7) the total amount alleged satisfies the conditions` | `eca-part3-jurisdiction.l4:471` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 13(2)(a): "Every claim must be filed in the form and manner prescribed by Rules of Court ... or speci" | `s 13(2)(a) the claim is filed in the form and manner required` | `eca-part3-jurisdiction.l4:524` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 13(2)(b)(i): "Every claim must be accompanied by a claim referral certificate issued in respect of every" | `s 13(2)(b)(i) the claim is accompanied by a claim referral certificate for every specified employment dispute` | `eca-part3-jurisdiction.l4:541` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 13(2)(b)(ii): "Every claim must be accompanied by any other documents that may be prescribed ... or speci" | `s 13(2)(b)(ii) the claim is accompanied by the other documents required` | `eca-part3-jurisdiction.l4:556` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 17(2): "An application under subsection (1) must be made within the time and manner prescribed by " | `s 17(2) the application is made as required` | `eca-part3-jurisdiction.l4:1148` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QB | s 19(1): "a party to proceedings before a tribunal (a) must act in person" | `s 19(1) to (3) the party may be represented before the tribunal by the representative` | `eca-part3-proceedings.l4:182` | `JUST FALSE` where the requirement is not met; the function asks a plain yes/no whose facts are given, and the text states the requirement itself, so its answer to "is it met" is no and not silence | `NOTHING` (a bare "must" is not among the flat negatives) |
| QC | s 2(1) "specified contractual dispute": "about any matter specified in the First Schedule" | `s 2(1) the dispute is a specified contractual dispute` | `eca-part1-preliminary.l4:369` | `JUST FALSE` for a matter in the Second or Third Schedule or in none (read as a closed "means", fork F1); "means" closes the definition (fork F1) | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 2(1) "specified statutory dispute": "about any matter specified in the Second Schedule" | `s 2(1) the dispute is a specified statutory dispute` | `eca-part1-preliminary.l4:387` | `JUST FALSE` for a matter in the First or Third Schedule or in none (a closed "means", F1); "means" closes the definition (fork F1) | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 2(1) "wrongful dismissal dispute": "specified in the Third Schedule" | `s 2(1) the dispute is a wrongful dismissal dispute` | `eca-part1-preliminary.l4:404` | `JUST FALSE` for a matter in the First or Second Schedule or in none (a closed "means", F1); "means" closes the definition (fork F1) | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 12(2)(c)(i): "item 17 of the First Schedule or item 14 or 16 of the Second Schedule" | `s 12(2)(c)(i) the matter is specified in item 17 of the First Schedule or item 14 or 16 of the Second Schedule` | `eca-part3-jurisdiction.l4:209` | `FALSE` (a plain yes/no function) for any other matter; a yes/no classification of the Schedule's own numbering, not a legal answer; it cannot carry NOTHING | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 12(2)(c)(ii): "any other matter specified in the First or Second Schedule" | `s 12(2)(c) the matter is specified in the First or Second Schedule` | `eca-part3-jurisdiction.l4:261` | `FALSE` (a plain yes/no function) for a Third Schedule matter or none; a yes/no classification of the Schedule's own numbering, not a legal answer; it cannot carry NOTHING | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 12(2)(c): the same limbs, in the function that decides the claim | `s 12(2)(c) the claim is made by an employer in a prescribed class against an employee about a matter the paragraph names` | `eca-part3-jurisdiction.l4:287` | `JUST FALSE` where the matter is in neither Schedule, tested before the employer class; "The claim must be made" is a requirement, so a matter outside the lists fails it | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 16(3): "item 17 of the First Schedule, or item 13 or 15 of the Second Schedule" | `s 16(3) the matter is specified in item 17 of the First Schedule or item 13 or 15 of the Second Schedule` | `eca-part3-jurisdiction.l4:793` | `FALSE` (a plain yes/no function) for any other matter; a yes/no classification of the Schedule's own numbering, not a legal answer; it cannot carry NOTHING | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 16(3): the same list, in the function that decides the bar (open question Q3) | `s 16(3) the employee cannot lodge the claim` | `eca-part3-jurisdiction.l4:846` | `NOTHING` for a matter outside the named items; a scope limit with no "only" (ruled I(c)); open question Q3 | `JUST FALSE` (the sentence hands its definition to the list) |
| QC | s 16(4)(a): the same list | `s 16(4)(a) the claim is deemed to be discontinued` | `eca-part3-jurisdiction.l4:876` | `JUST FALSE` for a matter outside the named items; the "Where" condition of s 16(4) (ruled I(b)) | `NOTHING` (a bare list: no paragraph holds) |
| QC | s 21(2): "any written law specified in the Fourth Schedule" | `s 21(2) the tribunal may draw any inference it thinks fit from the party's failure` | `eca-part3-proceedings.l4:409` | `NOTHING` for an obligation outside the Fourth Schedule; a scope limit with no "only" (ruled I(c)) | `JUST FALSE` (the sentence hands its definition to the list) |
| QD | s 3(5): "Upon accepting the mediation request, the Commissioner must ... refer" | `s 3(5) the Commissioner must refer the specified employment dispute for mediation by an approved mediator` | `eca-part2-mediation.l4:403` | `JUST FALSE` when the request is not accepted (the regulative rule `s 3(5) the Commissioner's duty to refer the listed disputes for mediation` is run with `#TRACE`): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 4(1): "as soon as is reasonably practicable after that dispute is referred" | `s 4(1) the approved mediator must conduct the first mediation session` | `eca-part2-mediation.l4:452` | `JUST FALSE` when the dispute has not been referred (fork F9): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 6(2): "This section applies where ..." and "must issue ... if" (a), (b) or (c) | `s 6(2) the approved mediator must issue the claimant a claim referral certificate for the dispute` | `eca-part2-mediation.l4:722` | `JUST FALSE` when section 6 does not apply or no limb holds: the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 7(7)(a): "Where a District Court sets aside ..." | `s 7(7)(a) the approved mediator must issue the claimant a claim referral certificate for the dispute referred by the District Court` | `eca-part2-mediation.l4:1080` | `JUST FALSE` when the District Court has not set aside and referred, or no limb holds: the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 20(2)(a): "A tribunal, when dealing with any claim" | `s 20(2)(a) the tribunal is to identify the relevant issues in the claim` | `eca-part3-proceedings.l4:253` | `JUST FALSE` when the tribunal is not dealing with a claim (ruled II(c)): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 20(2)(b): "A tribunal, when dealing with any claim" | `s 20(2)(b) the tribunal is to ensure that the relevant evidence is adduced by the parties` | `eca-part3-proceedings.l4:267` | `JUST FALSE` when the tribunal is not dealing with a claim (ruled II(c)): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 20(7)(a): "When deciding any claim involving a wrongful dismissal dispute" | `s 20(7)(a) the tribunal is to have regard to the tripartite guidelines on wrongful dismissal` | `eca-part3-proceedings.l4:339` | `JUST FALSE` when the tribunal is not deciding such a claim (ruled II(c)): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 20(7)(b): "When deciding any claim involving a wrongful dismissal dispute" and "if any compensation is claimed" | `s 20(7)(b) the tribunal is to calculate the compensation in accordance with the regulations made under section 34(1)` | `eca-part3-proceedings.l4:357` | `JUST FALSE` when the tribunal is not deciding such a claim or no compensation is claimed (ruled II(c) and the "if" rule): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 22(7): "Where a tribunal does not have jurisdiction to determine a claim" | `s 22(7) the claim or the part must be dismissed for lack of jurisdiction` | `eca-part3-proceedings.l4:709` | `JUST FALSE` when the tribunal has jurisdiction (ruled I(b)): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 25(4)(a): "When deciding an appeal ... on a claim involving a wrongful dismissal dispute" | `s 25(4)(a) the General Division of the High Court is to have regard to the tripartite guidelines on wrongful dismissal` | `eca-part3-appeals.l4:278` | `JUST FALSE` when the appeal is of another kind (ruled II(c)): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QD | s 25(4)(b): "When deciding an appeal ... on a claim involving a wrongful dismissal dispute" and "if any compensation is claimed" | `s 25(4)(b) the General Division of the High Court is to calculate the compensation in accordance with the regulations made under section 34(1)` | `eca-part3-appeals.l4:297` | `JUST FALSE` when the appeal is of another kind or no compensation is claimed (ruled II(c) and the "if" rule): the function says whether the duty holds, with no separate compliance function; the function is the "does the duty hold" question, and the text makes the duty depend on its trigger in its own words; no compliance function is written | a compliance function that answers `NOTHING` when the duty does not arise, with a companion "the duty arises" that answers `JUST FALSE` |
| QE | s 5(2): "A party other than an individual may be represented" | `s 5(1) to (3) the party may be represented at the mediation by the representative` | `eca-part2-mediation.l4:616` | `JUST FALSE` for an individual party with a (2) representative; (1)(a) "must act in person" and (1)(b), (c) say no for an individual in the text's own words, so the phrase does not leave the individual in silence | `NOTHING` for the individual, since (2) does not cover them and says nothing of them |
| QE | s 19(2): "A party other than an individual may be represented" | `s 19(1) to (3) the party may be represented before the tribunal by the representative` | `eca-part3-proceedings.l4:182` | `JUST FALSE` for an individual party with a (2) representative; (1)(a) "must act in person" and (1)(b), (c) say no for an individual in the text's own words, so the phrase does not leave the individual in silence | `NOTHING` for the individual, since (2) does not cover them and says nothing of them |
| QF | not applicable | this encoding writes no events to a state ledger | | not applicable | not applicable |

**Looked at, and not forks.**
Each of these was entered as a fork in an earlier pass of this encoding and was removed after being tested against the definition above: the text, read either way, does not give two outcomes, or the outcome is fixed by a rule the brief states.
- The meanings borrowed from other Acts (`salary`, `workman`, `employment assistance payment`, `tripartite mediation`) and the "prescribed" categories of Government employee and employer in s 2(1): the brief's Guide section 4 rule asks the borrowed fact as an input; there is one reading.
- s 2(2) (a counterclaim): "When this Act is applied to a counterclaim" is a "where" (II(c)), so for an ordinary claim the answer is `JUST FALSE`. The function that returns the person cannot say so (tag `[no yes-or-no]`), so its yes/no twin `s 2(2) a reference to the claimant or the respondent is read as a reference to a party to the counterclaim` carries the no (fork F12).
- s 2(3) (an officer "if authorised"): the failed "if" is reading (a), listed under "Marginal readings for a lawyer"; an officer not appointed under s 3(1) of the Employment Act 1968 is outside the grant, and that is NOTHING by ruling (c).
- s 12(1) (jurisdiction when a requirement fails): an open question (Q2 above).
- s 3(3)(a) "subject to paragraphs (b) and (c)", s 18(1) "subject to subsections (2), (3), (4) and (5)" and s 24(1) "unless a District Court or the General Division of the High Court orders otherwise": the exceptions are in the text's own words and are encoded as written; for s 24(1) the court's order is now an input of its own function (`s 24(1) execution or enforcement of the order is stayed pending the appeal`).

## How to read an answer

### Reading a result: FALSE and NOTHING

Every function that answers a yes-or-no question answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.

- **`JUST FALSE` means the Act itself says no to this case, in its own words.**
  In this Act that is: a definition that says "means" (the thing is not within the term); a condition the text introduces with "if", "only if", "unless" or "until", when the condition is not met; a flat negative ("cannot be represented", "must not exceed", "does not operate as a stay") that reaches the case; a requirement worded "must" that is not met (an extension of reading (a), explained under "Marginal readings for a lawyer"); and, by the rulings of 2026-11-05, a period the text fixes in its own words ("within", "not later than", "begins from ... until", "not earlier than one year before") when the case is outside it (I(a)), a "where ..." condition that is not met (I(b)), a "when", "upon" or "whenever" condition that is not met (II(c)), the bar of a "stayed until Y" after Y, and "has the stay ended" while the bar stands (II(d)).
  I also read "in adopting", "after" an event, "on the application of" and "on the recommendation of" as "where" (assumed, not ruled: fork F9).
  Every such branch in layer 1 carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`; a branch that rests on a ruling adds `[ruled I(a)]`, `[ruled I(b)]`, `[ruled II(c)]` or `[ruled II(d)]`, and one that rests on the assumption adds `[assumed: when]`.
- **`NOTHING` means the Act does not answer on these facts: "not covered".**
  It is never a no, and a caller must never turn it into one.
  In this Act it comes from six causes, and every such branch carries `-- NOTHING-kind (<cause>)`: silent; list not closed; includes; undefined term; points outside the text (a fee, limit, period, form or class that regulations, Rules of Court or another Act supply); limited by its own wording (a grant, duty or protection given to a stated class or case, with no "only", and the case falls outside it).
  The first ruling of 2026-11-05, I(c), is that this is `NOTHING`, and each such branch says which of three it is: `[scope limit, ruled I(c)]`; `[no yes-or-no]`, where the function returns a value (a person, a date, an amount) and so has no `JUST FALSE` to give; or `[open question; reviewer expected JUST FALSE]`, the places listed under "Open questions".
- Asking the same question of a case the person is unsure about gives `NOTHING` too: "I am not sure" is not a no.
- In the seat, the answer to "may I ...?" is `JUST TRUE` only when the Act gives the permission on the facts stated.
  The person-facing answers do not say which Hohfeld kind a rule is; that is in "Jural relations".
- `REFUSE` does not exist on the main binary, so "not covered" is `NOTHING` throughout, and every case file asserts it with `EQUALS NOTHING`.

## Marginal readings for a lawyer

The brief asks for every branch that rests on one of two readings, to be listed with the other reading stated.
**Reading (a)**: a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" ("if A then B" does not itself say "if not A then not B"); and a flat negative counts as the text saying no.
**Reading (b)**: a prohibition or a grant limited by its own wording does not count as a no for a case outside the limit.
The second half of (a), the flat negative, was ruled on 2026-11-04 (N2) and is listed here only so that nothing is hidden; the failed "if" half is for a lawyer.
Reading (b) was open when this row was first delivered and has since been ruled in three parts (the first ruling of 2026-11-05, printed under Forks): a period the text fixes in its own words gives `JUST FALSE` outside it; a "where" condition not met gives `JUST FALSE`; and a scope limit with no "only" gives `NOTHING` outside the scope.
A second ruling of the same day decided "when", "upon" and "whenever" (as "where") and the "stayed until" bars.
So the first table lists what is still a reading for a lawyer, and the second lists the sites the rulings decided.
I added one more class under (a) because the Act uses it heavily: a requirement worded "must" ("The claim must be supported by a claim referral certificate") that is not met is answered `JUST FALSE`, as if it were "only if"; the other reading is `NOTHING`, since "must" is not one of the words that the brief says make a no.
A "means" definition and a list closed with "only" are the text's own no and are not marginal.
Where one function has several such branches the row says how many.

Branch counts, by script: 319 branches in layer 1 answer `JUST FALSE` or `NOTHING`.
Still marginal, for a lawyer: 37 rest on a failed "if" (reading (a)), 15 on a flat negative (reading (a), ruled N2), 26 on a "must" requirement (reading (a) extended), 4 on "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" (assumed, not ruled: fork F9), and 11 on a scope limit that the review expected to be `JUST FALSE` (open questions).
Decided by the rulings of 2026-11-05: 3 read a period the text fixes in its own words as `JUST FALSE` outside it (I(a)), 39 read a "where" condition that is not met as `JUST FALSE` (I(b)), 45 read a scope limit with no "only" as `NOTHING` outside the scope (I(c)), 7 are scope limits in a function that returns a value, so they have no yes-or-no to give, 15 read "when", "upon" or "whenever" as "where" (II(c)), and 6 are the two questions of a "stayed until" bar (II(d)).
The other 111 are not marginal (a "means" definition, a list closed with "only", or a `NOTHING` for a cause other than a limit).
Distinct functions: 35 for a failed "if"; 12 for a flat negative; 21 for a "must" requirement; 4 for the assumed reading of "where"; 10 for an open question; 3 + 35 + 43 + 7 + 15 + 4 under the rulings (a function can appear under more than one reading).
The first table has 82 rows and the second 107, one per function and reading.
The classes: `a-if` is a failed "if"-type condition counted as the text's no; `a-flat` is a flat negative counted as the text's no; `a-must` is a requirement worded "must" counted as the text's no; `w` is the assumed reading of the words in fork F9 as "where"; `o` is an open question; `r-a`, `r-b` and `c` are the three parts of the first ruling; `v` is a scope limit in a function that returns a value; `r2c` and `r2d` are the second ruling's (c) and (d).

| # | Function | Module:line | Rests on | The words | Answer given | The other reading |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | `s 2(3) the officer may carry out a function or duty or exercise a power of the Commissioner under this Act` | part1-preliminary:572 | (a) a failed condition | may, if authorised by the Commissioner, carry out any function or duty | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M2 | `s 3(8) section 3 does not apply to the claim` | part2-mediation:31 | (a) a failed condition | This section does not apply to a claim if a tripartite mediation has been conducted | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M3 | `s 3(1) the claimant must submit a mediation request before lodging the claim` | part2-mediation:45 | (a) a failed condition | This section does not apply to a claim if a tripartite mediation has been conducted | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M4 | `s 3(1) the mediation request relates to every specified employment dispute for which the claim will be lodged` | part2-mediation:63 | (a) a requirement worded "must", not met | the claimant must submit to the Commissioner a mediation request relating to every specified employment dispute for which the c... | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M5 | `s 3(2) the mediation request is submitted by the time` | part2-mediation:253 | (a) a requirement worded "must", not met | The mediation request must be submitted to the Commissioner in the prescribed manner by the following time | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M6 | `s 3(3)(a) the mediation request must list the specified employment dispute` | part2-mediation:295 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | in relation to which all of the following requirements are satisfied | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M7 | `s 3(3)(b) the mediation request must not list the specified employment dispute` (and 1 more branch of the same kind) | part2-mediation:311 | (a) a failed condition | must not list a specified employment dispute if | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M8 | `s 3(3)(c) the mediation request must not list the specified employment dispute` | part2-mediation:333 | (a) a failed condition | must not list a specified employment dispute if | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M9 | `s 3(3)(d) the mediation request is accompanied by the prescribed fee` | part2-mediation:350 | (a) a requirement worded "must", not met | must be accompanied by the prescribed fee for a mediation under this Part | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M10 | `s 3(4)(a) the Commissioner may refuse to accept the mediation request` | part2-mediation:369 | (a) a failed condition | refuse to accept a mediation request if | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M11 | `s 4(1) the approved mediator must conduct the first mediation session` | part2-mediation:456 | assumed, not ruled: "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" | as soon as is reasonably practicable after that dispute is referred under section 3(5), 7(5)(b)(ii) or 22(8) to the approved me... | JUST FALSE | NOTHING: the words fix the scope of the rule and are not a condition on it (fork F9) |
| M12 | `s 4(2) the approved mediator need not conduct a mediation session` | part2-mediation:483 | (a) a failed condition | need not conduct any mediation session for a specified employment dispute, if the approved mediator is satisfied that there is ... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M13 | `s 5(1) to (3) the party may be represented at the mediation by the representative` (and 1 more branch of the same kind) | part2-mediation:631 | (a) a flat negative | cannot be represented by an advocate and solicitor | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M14 | `s 5(1) to (3) the party may be represented at the mediation by the representative` | part2-mediation:635 | (a) a requirement worded "must", not met | a party to a mediation under this Part (a) must act in person | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M15 | `s 6(4) the specified employment dispute is unresolved` | part2-mediation:700 | (a) a failed condition | a specified employment dispute listed in a mediation request is unresolved if the dispute — (a) is not settled; and (b) is not ... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M16 | `s 6(2) the approved mediator must issue the claimant a claim referral certificate for the dispute` | part2-mediation:734 | (a) a failed condition | must issue to the claimant a claim referral certificate ... if | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M17 | `s 6(3) the approved mediator may discontinue the mediation and refuse to issue a claim referral certificate` | part2-mediation:787 | (a) a failed condition | if a claimant submits a mediation request but, without reasonable excuse, fails to attend any mediation session to which that r... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M18 | `s 7(1)(a) the settlement agreement is in the form prescribed` | part2-mediation:808 | (a) a requirement worded "must", not met | the parties to the settlement must enter into a settlement agreement in the form prescribed by Rules of Court | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M19 | `s 7(1)(b) the total amount payable to the party for contractual and statutory disputes is within the limit` | part2-mediation:834 | (a) a flat negative | must not exceed the prescribed claim limit in section 12(7)(a) | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M20 | `s 7(1)(c) the total amount payable to the party for wrongful dismissal disputes is within the limit` | part2-mediation:857 | (a) a flat negative | must not exceed the prescribed claim limit in section 12(7)(b) | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M21 | `s 7(1)(d) the settlement agreement is signed by or on behalf of each party` | part2-mediation:873 | (a) a requirement worded "must", not met | the settlement agreement must be signed by or on behalf of each party | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M22 | `s 7(2) a District Court may register the settlement agreement` | part2-mediation:887 | assumed, not ruled: "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" | may, on the application of any party to the settlement agreement | JUST FALSE | NOTHING: the words fix the scope of the rule and are not a condition on it (fork F9) |
| M23 | `s 7(2) a District Court may refuse to register the settlement agreement` | part2-mediation:904 | (a) a failed condition | may refuse to register if the application is not made within the period prescribed by Rules of Court | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M24 | `s 7(6) a condition for setting aside is satisfied` | part2-mediation:988 | (a) a requirement worded "must", not met | For the purposes of subsection (5), the conditions are as follows | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M25 | `s 7(5)(a) a District Court may set aside the registration of the settlement agreement` | part2-mediation:1001 | (a) a failed condition | may, if any condition in subsection (6) is satisfied | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M26 | `s 7(5)(b)(i) a District Court may set aside the settlement agreement` | part2-mediation:1015 | (a) a failed condition | may, if any condition in subsection (6) is satisfied | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M27 | `s 7(8) the specified employment dispute referred by the District Court is unresolved` | part2-mediation:1053 | (a) a failed condition | a specified employment dispute is unresolved if the dispute is not settled and is not withdrawn by the claimant | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M28 | `s 7(7)(a) the approved mediator must issue the claimant a claim referral certificate for the dispute referred by the District Court` | part2-mediation:1090 | (a) a failed condition | must issue to the claimant a claim referral certificate ... if | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M29 | `s 7(7)(b) the approved mediator may discontinue the mediation and refuse to issue a claim referral certificate for the disputes referred by the District Court` | part2-mediation:1111 | (a) a failed condition | if the claimant, without reasonable excuse, fails to attend any mediation session, the approved mediator may | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M30 | `s 7(9) section 30H(3) to (9) of the Industrial Relations Act 1960 applies to the dispute` | part2-mediation:1130 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | for the avoidance of doubt | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M31 | `s 23(2) the condition that a District Court gives permission to appeal is met` | part3-appeals:26 | (a) a failed condition | An appeal lies to the General Division of the High Court under this section only if permission to appeal is given by a District... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M32 | `s 23(1) the party may appeal to the General Division of the High Court against the order on the ground` | part3-appeals:44 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | any party | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M33 | `s 23(1) and (2) an appeal lies to the General Division of the High Court` | part3-appeals:75 | (a) a failed condition | only if permission to appeal is given by a District Court | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M34 | `s 23(1) and (2) an appeal lies to the General Division of the High Court` | part3-appeals:78 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | (limited by its own wording) [open question; reviewer expected JUST FALSE]: the right to appeal in (1) is limited to the two gr... | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M35 | `s 24(1) the appeal by itself operates as a stay of execution or enforcement of the order` | part3-appeals:149 | (a) a flat negative | An appeal against an order made by a tribunal under section 22(1) does not operate as a stay of execution or enforcement of tha... | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M36 | `s 24(1) execution or enforcement of the order is stayed pending the appeal` | part3-appeals:168 | (a) a flat negative | An appeal against an order made by a tribunal under section 22(1) does not operate as a stay of execution or enforcement of tha... | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M37 | `s 24(4) the conditions for the General Division of the High Court to order a stay are met` | part3-appeals:219 | (a) a failed condition | may order a stay ..., or give a direction under subsection (2), only if — (a) a District Court has given ... permission to appe... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M38 | `s 25 the General Division of the High Court may take the step on the appeal` (and 1 more branch of the same kind) | part3-appeals:248 | (a) a flat negative | but must not — (a) reverse or vary any determination made by a tribunal on a question of fact | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M39 | `s 25(4)(b) the General Division of the High Court is to calculate the compensation in accordance with the regulations made under section 34(1)` | part3-appeals:303 | (a) a failed condition | (b) if any compensation is claimed, is to calculate the amount of that compensation in accordance with any regulations | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M40 | `s 9(2) the individual is eligible for appointment as a tribunal magistrate` | part3-jurisdiction:61 | (a) a failed condition | An individual is eligible for appointment under subsection (1)(a) as a tribunal magistrate if the individual is a qualified person | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M41 | `s 9(4) the President may revoke the appointment of the tribunal magistrate` | part3-jurisdiction:90 | assumed, not ruled: "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" | the President may, on the recommendation of the Chief Justice, at any time revoke | JUST FALSE | NOTHING: the words fix the scope of the rule and are not a condition on it (fork F9) |
| M42 | `s 12(2)(a) the claim is made by an employee in a prescribed class against the employer` (and 1 more branch of the same kind) | part3-jurisdiction:230 | (a) a requirement worded "must", not met | The claim must be made — | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M43 | `s 12(2)(b) the claim is made by an employee in a prescribed class against a person liable under section 65 of the Employment Act 1968` (and 1 more branch of the same kind) | part3-jurisdiction:251 | (a) a requirement worded "must", not met | The claim must be made — | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M44 | `s 12(2)(c) the claim is made by an employer in a prescribed class against an employee about a matter the paragraph names` (and 3 more branches of the same kind) | part3-jurisdiction:290 | (a) a requirement worded "must", not met | The claim must be made — | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M45 | `s 12(2) the claim is made as the subsection requires` | part3-jurisdiction:338 | (a) a requirement worded "must", not met | The claim must be made — | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M46 | `s 12(3) the claim is for what the subsection requires` | part3-jurisdiction:356 | (a) a requirement worded "must", not met | The claim must be for either or both of the following | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M47 | `s 12(4) each amount alleged to be payable relates to a specified employment dispute` | part3-jurisdiction:369 | (a) a requirement worded "must", not met | Each amount alleged to be payable under the claim must relate to a specified employment dispute | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M48 | `s 12(5) the claim is supported by a claim referral certificate for every specified employment dispute` | part3-jurisdiction:383 | (a) a requirement worded "must", not met | The claim must be supported by a claim referral certificate issued in respect of every specified employment dispute for which t... | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M49 | `s 12(6) the claim is lodged within the prescribed period after the certificate was issued` | part3-jurisdiction:402 | (a) a requirement worded "must", not met | The claim must be lodged with the tribunal within the prescribed period after the date of issue of the claim referral certificate | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M50 | `s 12(7)(a) the total alleged for contractual and statutory disputes is within the claim limit` | part3-jurisdiction:427 | (a) a flat negative | must not exceed the prescribed claim limit applicable to the claimant | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M51 | `s 12(7)(b) the total alleged for wrongful dismissal disputes is within the claim limit` | part3-jurisdiction:451 | (a) a flat negative | must not exceed the prescribed claim limit applicable to the claimant | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M52 | `s 12(7) the total amount alleged satisfies the conditions` | part3-jurisdiction:474 | (a) a requirement worded "must", not met | The total amount alleged to be payable under the claim must satisfy the following conditions | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M53 | `s 12(1) the tribunal has jurisdiction to hear and determine the claim` | part3-jurisdiction:497 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | in relation to which all applicable requirements set out in subsections (2) to (7) are satisfied | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M54 | `s 13(2)(a) the claim is filed in the form and manner required` | part3-jurisdiction:530 | (a) a requirement worded "must", not met | Every claim must be filed in the form and manner prescribed by Rules of Court ... or specified in practice directions | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M55 | `s 13(2)(b)(i) the claim is accompanied by a claim referral certificate for every specified employment dispute` | part3-jurisdiction:545 | (a) a requirement worded "must", not met | Every claim must be accompanied by a claim referral certificate issued in respect of every specified employment dispute for whi... | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M56 | `s 13(2)(b)(ii) the claim is accompanied by the other documents required` | part3-jurisdiction:564 | (a) a requirement worded "must", not met | Every claim must be accompanied by any other documents that may be prescribed ... or specified | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M57 | `s 13(2)(b)(iii) the claim is accompanied by the court fee prescribed` | part3-jurisdiction:581 | (a) a failed condition | Every claim must be accompanied by the court fee (if any) prescribed | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M58 | `s 14 the claim cannot be divided and pursued in separate proceedings before a tribunal` | part3-jurisdiction:597 | (a) a failed condition | A claim cannot be divided and pursued in separate proceedings before a tribunal if the only reason for doing so is to bring the... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M59 | `s 15(2)(a) the requirement in section 12(7) is deemed to be satisfied under this paragraph` | part3-jurisdiction:696 | (a) a failed condition | If the claimant abandons the excess amount — (a) the requirement in section 12(7) is deemed to be satisfied | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M60 | `s 15(2)(b) section 15(2) gives the tribunal jurisdiction to hear and determine the claim` | part3-jurisdiction:711 | (a) a failed condition | If the claimant abandons the excess amount — ... (b) the tribunal has jurisdiction to hear and determine the claim | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M61 | `s 15(2)(c) an order of the tribunal in relation to the claim fully discharges all demands in respect of the claim` | part3-jurisdiction:728 | (a) a failed condition | If the claimant abandons the excess amount — ... (c) an order of the tribunal in relation to the claim fully discharges all dem... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M62 | `s 16(1) the claim cannot be lodged with a tribunal` | part3-jurisdiction:763 | (a) a failed condition | A claim relating to a specified employment dispute cannot be lodged with a tribunal if — (a) any proceedings relating to that c... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M63 | `s 16(2) no proceedings relating to the claim can be commenced in any other court or an Industrial Arbitration Court by either party against the other` | part3-jurisdiction:782 | (a) a failed condition | unless the claim is withdrawn, discontinued or dismissed for lack of jurisdiction | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M64 | `s 16(3) the employee cannot lodge the claim` | part3-jurisdiction:851 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | a claim for any amount relating to a specified employment dispute concerning a matter specified in item 17 of the First Schedul... | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M65 | `s 16(4)(a) the claim is deemed to be discontinued` | part3-jurisdiction:882 | (a) a failed condition | the claim is deemed to be discontinued, if the employee makes representations in writing under section 35(3) ... or section 8(1) | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M66 | `s 16(6)(a) the claim relating to a wrongful dismissal dispute is deemed to be discontinued` | part3-jurisdiction:944 | (a) a failed condition | the claim is deemed to be discontinued, if the employee makes representations in writing under section 35(3) of the Industrial ... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M67 | `s 16(7) the employee cannot lodge a claim for employment assistance payment` | part3-jurisdiction:981 | (a) a failed condition | cannot lodge with a tribunal a claim for employment assistance payment, unless — (a) that Minister allows ... a mediation reque... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M68 | `s 16(8)(c) the employee may proceed with the claim` (and 1 more branch of the same kind) | part3-jurisdiction:1081 | (a) a failed condition | (c) if that Minister decides to allow the employee to submit ... a mediation request ..., the employee may proceed with the claim | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M69 | `s 17(2) the application is made as required` | part3-jurisdiction:1156 | (a) a requirement worded "must", not met | An application under subsection (1) must be made within the time and manner prescribed by Rules of Court | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M70 | `s 18(6) subsection (1) does not prevent the tribunal from hearing the claims together` | part3-proceedings:113 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | (limited by its own wording) [open question; reviewer expected JUST FALSE]: an avoidance-of-doubt clause that settles only the ... | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M71 | `s 19(1) to (3) the party may be represented before the tribunal by the representative` (and 1 more branch of the same kind) | part3-proceedings:197 | (a) a flat negative | cannot be represented by an advocate and solicitor | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M72 | `s 19(1) to (3) the party may be represented before the tribunal by the representative` | part3-proceedings:201 | (a) a requirement worded "must", not met | a party to proceedings before a tribunal (a) must act in person | JUST FALSE | NOTHING: "must" is not one of the words that make a no ("if", "only if", "unless", a flat negative) |
| M73 | `s 20(3) the tribunal may direct a party to appear before it` | part3-proceedings:287 | assumed, not ruled: "in adopting", "after" an event, "on the application of" or "on the recommendation of" read as "where" | In adopting a judge-led approach | JUST FALSE | NOTHING: the words fix the scope of the rule and are not a condition on it (fork F9) |
| M74 | `s 20(7)(b) the tribunal is to calculate the compensation in accordance with the regulations made under section 34(1)` | part3-proceedings:363 | (a) a failed condition | (b) if any compensation is claimed, is to calculate the amount of that compensation in accordance with any regulations | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M75 | `s 20(8) the tribunal may hear the claim and make its decision in the absence of the party` | part3-proceedings:378 | (a) a failed condition | if any party to any proceedings before a tribunal, without reasonable excuse, fails to attend those proceedings, a tribunal may... | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M76 | `s 21(3) the evidence need not be given on oath or affirmation` | part3-proceedings:442 | (a) a flat negative | Subject to subsection (4), evidence tendered to a tribunal need not be given on oath or affirmation | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M77 | `s 22(4) the total ordered to be paid for contractual and statutory disputes is within the claim limit` | part3-proceedings:632 | (a) a flat negative | must not exceed the prescribed claim limit in section 12(7)(a) that is applicable to the party | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M78 | `s 22(5) the total ordered to be paid for wrongful dismissal disputes is within the claim limit` | part3-proceedings:656 | (a) a flat negative | must not exceed the prescribed claim limit in section 12(7)(b) that is applicable to the party | JUST FALSE | NOTHING: a flat negative is not a no for a case it does not reach (ruled N2, 2026-11-04: it counts as the no) |
| M79 | `s 22(10) the tribunal may make the correction` | part3-proceedings:781 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | to the extent necessary to rectify | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M80 | `s 28 the provision in the agreement is void to that extent` | part4-miscellaneous:45 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | to the extent that it purports | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |
| M81 | `s 29(1) the person may disclose the information` | part4-miscellaneous:119 | (a) a failed condition | may disclose information ... if the disclosure is — (a) ... (f) for any other purpose prescribed by regulations | JUST FALSE | NOTHING: "if A then B" does not itself say "if not A then not B" |
| M82 | `s 30(3) no liability lies personally against the person` (and 1 more branch of the same kind) | part4-miscellaneous:174 | open question: a scope limit with no "only" (ruled I(c)); the review expected JUST FALSE | the Commissioner, an individual authorised ..., or an approved mediator | NOTHING | JUST FALSE: the limit is itself the text's no for any case outside it |

### Sites decided by the rulings of 2026-11-05

107 rows, one per function and part of a ruling.
Each row names the part of the ruling it rests on and the answer given, and shows the other reading.

| # | Function | Module:line | Rests on | The words | Answer given | The other reading |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | `s 2(2) the person a reference in the Act is a reference to` | part1-preliminary:535 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | When this Act is applied to a counterclaim | NOTHING | none: a value cannot be JUST FALSE |
| R2 | `s 2(2) a reference to the claimant or the respondent is read as a reference to a party to the counterclaim` | part1-preliminary:551 | II(c) a "when", "upon" or "whenever" condition not met | When this Act is applied to a counterclaim lodged with a tribunal | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R3 | `s 2(3) the officer may carry out a function or duty or exercise a power of the Commissioner under this Act` | part1-preliminary:569 | I(c) outside a scope limit with no "only" | appointed under section 3(1) of the Employment Act 1968 | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R4 | `s 3(1) the claimant must submit a mediation request before lodging the claim` | part2-mediation:48 | I(c) outside a scope limit with no "only" | relating to every specified employment dispute for which the claim will be lodged | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R5 | `s 3(3)(a) the mediation request must list the specified employment dispute` | part2-mediation:288 | I(a) outside a period the text fixes in its own words | (ii) the material facts giving rise to the dispute occurred not earlier than one year before the date on which that request is ... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R6 | `s 3(4)(c) the Commissioner may pay the whole or a part of the fee to the person` | part2-mediation:393 | I(c) outside a scope limit with no "only" | to a person who is prescribed, or who belongs to a class of persons that is prescribed | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R7 | `s 3(5) the Commissioner must refer the specified employment dispute for mediation by an approved mediator` | part2-mediation:406 | II(c) a "when", "upon" or "whenever" condition not met | Upon accepting the mediation request | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R8 | `s 3(5) the Commissioner must refer the specified employment dispute for mediation by an approved mediator` | part2-mediation:409 | I(c) outside a scope limit with no "only" | every specified employment dispute listed in | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R9 | `s 4(3) the mediation session must be held in private` | part2-mediation:494 | I(c) outside a scope limit with no "only" | Each mediation session | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R10 | `s 4(5) subsection (4) applies` | part2-mediation:525 | I(b) a "where" condition not met | Subsection (4) applies where | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R11 | `s 4(4) the same approved mediator may take the disputes together` | part2-mediation:543 | I(b) a "where" condition not met | Subsection (4) applies where | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R12 | `s 6(1) section 6 applies` | part2-mediation:684 | I(b) a "where" condition not met | This section applies where | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R13 | `s 6(2) the approved mediator must issue the claimant a claim referral certificate for the dispute` | part2-mediation:725 | I(b) a "where" condition not met | This section applies where | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R14 | `s 6(2) the approved mediator must issue the claimant a claim referral certificate for the dispute` | part2-mediation:729 | I(c) outside a scope limit with no "only" | in respect of every unresolved specified employment dispute | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R15 | `s 6(2) the claim referral certificate is issued to the person` | part2-mediation:769 | I(c) outside a scope limit with no "only" | to the claimant | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R16 | `s 7(1)(a) the settlement agreement is in the form prescribed` | part2-mediation:805 | I(b) a "where" condition not met | Where a specified employment dispute is settled | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R17 | `s 7(1)(b) the total amount payable to the party for contractual and statutory disputes is within the limit` | part2-mediation:827 | I(b) a "where" condition not met | Where a specified employment dispute is settled | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R18 | `s 7(1)(c) the total amount payable to the party for wrongful dismissal disputes is within the limit` | part2-mediation:850 | I(b) a "where" condition not met | Where a specified employment dispute is settled | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R19 | `s 7(1)(d) the settlement agreement is signed by or on behalf of each party` | part2-mediation:870 | I(b) a "where" condition not met | Where a specified employment dispute is settled | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R20 | `s 7(3)(a) the date from which the settlement agreement has the force and effect of a judgment for execution or enforcement` | part2-mediation:921 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | Where the settlement agreement is registered in a District Court | NOTHING | none: a value cannot be JUST FALSE |
| R21 | `s 7(3)(b) proceedings may be taken on the settlement agreement as on a judgment` | part2-mediation:933 | I(b) a "where" condition not met | Where the settlement agreement is registered in a District Court | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R22 | `s 7(3)(c) an amount for which the settlement agreement is registered carries interest as a judgment debt` | part2-mediation:945 | I(b) a "where" condition not met | Where the settlement agreement is registered in a District Court | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R23 | `s 7(4) a party may apply to set aside the registration` | part2-mediation:960 | I(b) a "where" condition not met | Where a settlement agreement is registered in a District Court | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R24 | `s 7(4) a party may apply to set aside the registration` | part2-mediation:963 | I(a) outside a period the text fixes in its own words | within the period prescribed by Rules of Court | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R25 | `s 7(5)(b)(ii) the kind of mediation a District Court may refer the dispute to` | part2-mediation:1040 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | may, if any condition in subsection (6) is satisfied | NOTHING | none: a value cannot be JUST FALSE |
| R26 | `s 7(7)(a) the approved mediator must issue the claimant a claim referral certificate for the dispute referred by the District Court` | part2-mediation:1083 | I(b) a "where" condition not met | Where a District Court sets aside ... and refers ... for mediation under this Part, the following apply | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R27 | `s 7(7)(a) the approved mediator must issue the claimant a claim referral certificate for the dispute referred by the District Court` | part2-mediation:1085 | I(c) outside a scope limit with no "only" | in respect of every unresolved specified employment dispute so referred | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R28 | `s 7(7)(b) the approved mediator may discontinue the mediation and refuse to issue a claim referral certificate for the disputes referred by the District Court` | part2-mediation:1108 | I(b) a "where" condition not met | Where a District Court sets aside ... and refers ... for mediation under this Part, the following apply | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R29 | `s 23(1) the court is the one to which the party may appeal` | part3-appeals:57 | I(c) outside a scope limit with no "only" | to the General Division of the High Court | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R30 | `s 23(3)(a) a District Court may extend the time under section 22(10) for the correction of the order` | part3-appeals:94 | I(b) a "where" condition not met | Where the only reason for appealing ... is to rectify anything mentioned in section 22(10)(a) to (d) | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R31 | `s 23(3)(b) a District Court may remit the matter to a tribunal for the correction of the order` | part3-appeals:113 | I(b) a "where" condition not met | Where the only reason for appealing ... is to rectify anything mentioned in section 22(10)(a) to (d) | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R32 | `s 24(1) execution or enforcement of the order is stayed pending the appeal` | part3-appeals:165 | I(c) outside a scope limit with no "only" | an appeal against an order made by a tribunal under section 22(1) | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R33 | `s 24(2) the court may direct that a stay be subject to any conditions it thinks fit` (and 1 more branch of the same kind) | part3-appeals:185 | I(c) outside a scope limit with no "only" | a District Court or the General Division of the High Court | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R34 | `s 24(3) the order or direction is final and is not subject to any appeal` | part3-appeals:200 | I(c) outside a scope limit with no "only" | Any order or direction of a District Court on an application for a stay | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R35 | `s 25(3) the General Division of the High Court may take into account the tripartite guidelines on re-employment` | part3-appeals:267 | II(c) a "when", "upon" or "whenever" condition not met | When deciding an appeal against an order made by a tribunal on a claim for employment assistance payment | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R36 | `s 25(4)(a) the General Division of the High Court is to have regard to the tripartite guidelines on wrongful dismissal` | part3-appeals:282 | II(c) a "when", "upon" or "whenever" condition not met | When deciding an appeal ... on a claim involving a wrongful dismissal dispute | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R37 | `s 25(4)(b) the General Division of the High Court is to calculate the compensation in accordance with the regulations made under section 34(1)` | part3-appeals:300 | II(c) a "when", "upon" or "whenever" condition not met | When deciding an appeal ... on a claim involving a wrongful dismissal dispute | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R38 | `s 27(1) the person who makes the allegation bears the burden of proving it` | part3-appeals:345 | I(c) outside a scope limit with no "only" | any of the following allegations | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R39 | `s 27(2)(a) the employer bears the burden of proving that the employee was dismissed with just cause or excuse` | part3-appeals:364 | I(c) outside a scope limit with no "only" | In any proceedings under this Act before a tribunal or the General Division of the High Court, the following apply | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R40 | `s 27(2)(a) the employer bears the burden of proving that the employee was dismissed with just cause or excuse` | part3-appeals:367 | I(b) a "where" condition not met | where an employee is dismissed without notice ... and the employee lodges a claim mentioned in section 14(2) | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R41 | `s 27(2)(b) the employer bears the burden of proving the ground for giving the notice of dismissal` | part3-appeals:392 | I(c) outside a scope limit with no "only" | In any proceedings under this Act before a tribunal or the General Division of the High Court, the following apply | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R42 | `s 27(2)(b) the employer bears the burden of proving the ground for giving the notice of dismissal` | part3-appeals:395 | I(b) a "where" condition not met | where an employee is dismissed with notice ... and the notice of dismissal is or purports to be given on the ground that there ... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R43 | `s 27(2)(c) the employer bears the burden of proving that the female employee was dismissed with sufficient cause` | part3-appeals:427 | I(c) outside a scope limit with no "only" | In any proceedings under this Act before a tribunal or the General Division of the High Court, the following apply | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R44 | `s 27(2)(c) the employer bears the burden of proving that the female employee was dismissed with sufficient cause` | part3-appeals:430 | I(b) a "where" condition not met | where a notice of dismissal is given to a female employee ... in the circumstances mentioned in section 84(1)(a), (b) or (c) | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R45 | `s 27(2)(d) the employer bears the burden of proving that the female employee mentioned in section 12(1) of the Child Development Co-Savings Act 2001 was dismissed with sufficient cause` | part3-appeals:473 | I(c) outside a scope limit with no "only" | In any proceedings under this Act before a tribunal or the General Division of the High Court, the following apply | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R46 | `s 27(2)(d) the employer bears the burden of proving that the female employee mentioned in section 12(1) of the Child Development Co-Savings Act 2001 was dismissed with sufficient cause` | part3-appeals:476 | I(b) a "where" condition not met | where a notice of dismissal is given to a female employee mentioned in section 12(1) of the Child Development Co-Savings Act 20... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R47 | `s 8 the person may constitute one or more Employment Claims Tribunals under section 4 of the State Courts Act 1970` | part3-jurisdiction:28 | I(c) outside a scope limit with no "only" | The President | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R48 | `s 9(3) the individual may be re-appointed as a tribunal magistrate` | part3-jurisdiction:74 | I(c) outside a scope limit with no "only" | An individual appointed under subsection (1)(a) | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R49 | `s 9(4) the President may revoke the appointment of the tribunal magistrate` | part3-jurisdiction:87 | I(c) outside a scope limit with no "only" | the appointment under subsection (1)(a) | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R50 | `s 9(5) the person may designate the individual as a tribunal magistrate` | part3-jurisdiction:103 | I(c) outside a scope limit with no "only" | The Presiding Judge of the State Courts | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R51 | `s 11(2) the person may appoint deputy registrars, assistant registrars and other officers for the tribunals` | part3-jurisdiction:138 | I(c) outside a scope limit with no "only" | The Chief Justice | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R52 | `s 9(6) the individual may sit as a tribunal magistrate in relation to the case` | part3-jurisdiction:158 | I(c) outside a scope limit with no "only" | any case heard by the individual as a tribunal magistrate | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R53 | `s 11(3) the registrar for the tribunals may exercise the jurisdiction and powers of a tribunal` | part3-jurisdiction:171 | I(c) outside a scope limit with no "only" | To the extent authorised by this Act or by Rules of Court | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R54 | `s 11(4) the officer may exercise and perform the powers and duties of the registrar for the tribunals` | part3-jurisdiction:187 | I(c) outside a scope limit with no "only" | only | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R55 | `s 15(1) the claimant may abandon the excess amount` | part3-jurisdiction:625 | I(b) a "where" condition not met | Where — (a) the total amount ... exceeds the prescribed claim limit in section 12(7)(a) ...; or (b) the total amount ... exceed... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R56 | `s 15(3) the claimant cannot recover the excess amount in a tribunal or any other court` | part3-jurisdiction:740 | I(b) a "where" condition not met | Where the claimant has abandoned the excess amount, the claimant cannot recover that amount | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R57 | `s 16(2) no proceedings relating to the claim can be commenced in any other court or an Industrial Arbitration Court by either party against the other` | part3-jurisdiction:779 | I(b) a "where" condition not met | where a claim relating to a specified employment dispute is lodged with a tribunal | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R58 | `s 16(3) the employee cannot lodge the claim` (and 2 more branches of the same kind) | part3-jurisdiction:849 | I(b) a "where" condition not met | Where an employee is dismissed, the employee cannot lodge | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R59 | `s 16(4)(a) the claim is deemed to be discontinued` | part3-jurisdiction:879 | I(b) a "where" condition not met | Where an employee is dismissed, and the employee lodges with a tribunal a claim ... concerning a matter specified in item 17 of... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R60 | `s 16(4)(b) the date with effect from which the claim is deemed to be discontinued` | part3-jurisdiction:895 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | (limited by its own wording) [no yes-or-no]: the date is that of the representations that discontinue the claim under (a); the ... | NOTHING | none: a value cannot be JUST FALSE |
| R61 | `s 16(5) the employee cannot lodge the claim relating to a wrongful dismissal dispute` (and 2 more branches of the same kind) | part3-jurisdiction:918 | I(b) a "where" condition not met | Where an employee is dismissed, the employee cannot lodge | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R62 | `s 16(5) the employee cannot lodge the claim relating to a wrongful dismissal dispute` | part3-jurisdiction:920 | I(c) outside a scope limit with no "only" | a claim relating to a wrongful dismissal dispute | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R63 | `s 16(6)(a) the claim relating to a wrongful dismissal dispute is deemed to be discontinued` | part3-jurisdiction:941 | I(b) a "where" condition not met | Where an employee is dismissed, and the employee lodges with a tribunal a claim relating to a wrongful dismissal dispute | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R64 | `s 16(6)(b) the date with effect from which the claim relating to a wrongful dismissal dispute is deemed to be discontinued` | part3-jurisdiction:957 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | (limited by its own wording) [no yes-or-no]: the date is that of the representations that discontinue the claim under (a); the ... | NOTHING | none: a value cannot be JUST FALSE |
| R65 | `s 16(7) the employee cannot lodge a claim for employment assistance payment` | part3-jurisdiction:979 | I(b) a "where" condition not met | Where an employee has made representations in writing under section 8B(1) | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R66 | `s 16(8)(a) the claim is stayed` | part3-jurisdiction:1003 | I(b) a "where" condition not met | Where, after an employee has lodged with a tribunal a claim for employment assistance payment, the employee makes representations | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R67 | `s 16(8)(a) the claim is stayed` | part3-jurisdiction:1006 | II(d) an "until" bar: the bar after Y, or has the stay ended | the claim is stayed until that Minister decides | bar: JUST FALSE after Y; ended: JUST FALSE while the bar stands, NOTHING after | ended: JUST TRUE after Y on the strength of the bar alone (the reading the second ruling rejects) |
| R68 | `s 16(8)(a) the stay on the claim has ended` | part3-jurisdiction:1039 | I(b) a "where" condition not met | Where, after an employee has lodged with a tribunal a claim for employment assistance payment, the employee makes representations | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R69 | `s 16(8)(a) the stay on the claim has ended` (and 1 more branch of the same kind) | part3-jurisdiction:1041 | II(d) an "until" bar: the bar after Y, or has the stay ended | the claim is stayed until that Minister decides | bar: JUST FALSE after Y; ended: JUST FALSE while the bar stands, NOTHING after | ended: JUST TRUE after Y on the strength of the bar alone (the reading the second ruling rejects) |
| R70 | `s 16(8)(b) the date with effect from which the claim is deemed to be discontinued` | part3-jurisdiction:1063 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | if that Minister decides not to allow | NOTHING | none: a value cannot be JUST FALSE |
| R71 | `s 16(8)(c) the employee may proceed with the claim` | part3-jurisdiction:1079 | I(b) a "where" condition not met | Where, after an employee has lodged with a tribunal a claim for employment assistance payment, the employee makes representations | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R72 | `s 16(9) the employer cannot defend the claim on the ground that the employee does not satisfy the re-employment eligibility criteria` | part3-jurisdiction:1102 | I(b) a "where" condition not met | Where an employee has lodged with a tribunal a claim for employment assistance payment, the employer of the employee cannot def... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R73 | `s 17(1) the court may order the proceedings or the counterclaim to be transferred to it` | part3-jurisdiction:1135 | I(c) outside a scope limit with no "only" | an appropriate court | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R74 | `s 17(1) the court may order the proceedings or the counterclaim to be transferred to it` | part3-jurisdiction:1140 | I(b) a "where" condition not met | Where it appears to an appropriate court, on the application of a party to any proceedings before a tribunal, that there is suf... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R75 | `s 17(4) execution or enforcement of the tribunal's order is stayed` | part3-jurisdiction:1181 | I(b) a "where" condition not met | Where the appropriate court orders ... that a counterclaim ... be transferred ..., and the tribunal determines the claim ... by... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R76 | `s 17(4) execution or enforcement of the tribunal's order is stayed` | part3-jurisdiction:1184 | II(d) an "until" bar: the bar after Y, or has the stay ended | execution or enforcement on the tribunal's order is stayed until the proceedings on the counterclaim are concluded | bar: JUST FALSE after Y; ended: JUST FALSE while the bar stands, NOTHING after | ended: JUST TRUE after Y on the strength of the bar alone (the reading the second ruling rejects) |
| R77 | `s 17(4) the stay on execution or enforcement of the tribunal's order has ended` | part3-jurisdiction:1203 | I(b) a "where" condition not met | Where the appropriate court orders ... that a counterclaim ... be transferred ..., and the tribunal determines the claim ... by... | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R78 | `s 17(4) the stay on execution or enforcement of the tribunal's order has ended` (and 1 more branch of the same kind) | part3-jurisdiction:1205 | II(d) an "until" bar: the bar after Y, or has the stay ended | execution or enforcement on the tribunal's order is stayed until the proceedings on the counterclaim are concluded | bar: JUST FALSE after Y; ended: JUST FALSE while the bar stands, NOTHING after | ended: JUST TRUE after Y on the strength of the bar alone (the reading the second ruling rejects) |
| R79 | `s 18(1) the proceedings before the tribunal are conducted in private` | part3-proceedings:28 | I(c) outside a scope limit with no "only" | all proceedings before a tribunal | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R80 | `s 18(2)(b) the tribunal may allow the individual to sit with the tribunal and act as an assessor` | part3-proceedings:62 | I(c) outside a scope limit with no "only" | individuals of skill and experience in the matter | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R81 | `s 18(3) the tribunal may permit the officer to participate in the proceedings` | part3-proceedings:80 | I(c) outside a scope limit with no "only" | an officer appointed under section 3(2) of the Employment Act 1968 | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R82 | `s 18(4) the tribunal may permit the individual to observe the hearing of the claim` | part3-proceedings:97 | I(c) outside a scope limit with no "only" | (limited by its own wording) [scope limit, ruled I(c)]: the permission is for the three kinds of individual; whether an individ... | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R83 | `s 20(1) the proceedings before the tribunal are to be conducted in an informal manner` | part3-proceedings:244 | I(c) outside a scope limit with no "only" | Proceedings before a tribunal | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R84 | `s 20(2)(a) the tribunal is to identify the relevant issues in the claim` | part3-proceedings:257 | II(c) a "when", "upon" or "whenever" condition not met | A tribunal, when dealing with any claim | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R85 | `s 20(2)(b) the tribunal is to ensure that the relevant evidence is adduced by the parties` | part3-proceedings:271 | II(c) a "when", "upon" or "whenever" condition not met | A tribunal, when dealing with any claim | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R86 | `s 20(4) the tribunal may summon the person` | part3-proceedings:302 | I(c) outside a scope limit with no "only" | to do either or both | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R87 | `s 20(5) the tribunal may inquire into the matter` | part3-proceedings:315 | I(c) outside a scope limit with no "only" | any matter which the tribunal considers relevant to a claim | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R88 | `s 20(6) the tribunal may take into account the tripartite guidelines on re-employment` | part3-proceedings:329 | II(c) a "when", "upon" or "whenever" condition not met | When deciding any claim for employment assistance payment, or calculating the amount | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R89 | `s 20(7)(a) the tribunal is to have regard to the tripartite guidelines on wrongful dismissal` | part3-proceedings:343 | II(c) a "when", "upon" or "whenever" condition not met | When deciding any claim involving a wrongful dismissal dispute | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R90 | `s 20(7)(b) the tribunal is to calculate the compensation in accordance with the regulations made under section 34(1)` | part3-proceedings:360 | II(c) a "when", "upon" or "whenever" condition not met | When deciding any claim involving a wrongful dismissal dispute | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R91 | `s 21(2) the tribunal may draw any inference it thinks fit from the party's failure` (and 1 more branch of the same kind) | part3-proceedings:415 | I(c) outside a scope limit with no "only" | failure to comply with any obligation of that party under any written law specified in the Fourth Schedule | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R92 | `s 21(6) the evidence and information must be disclosed to every party to the proceedings` | part3-proceedings:479 | I(c) outside a scope limit with no "only" | evidence and information obtained by a tribunal under subsection (5) | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R93 | `s 21(8)(a) the tribunal must make a summary of the facts and issues in dispute` | part3-proceedings:519 | I(c) outside a scope limit with no "only" | any proceedings before the tribunal | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R94 | `s 21(8)(b) the tribunal must make notes of the proceedings` | part3-proceedings:533 | I(c) outside a scope limit with no "only" | any proceedings before the tribunal | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R95 | `s 22(1) the tribunal may make the order` | part3-proceedings:577 | I(c) outside a scope limit with no "only" | to determine a claim within the tribunal's jurisdiction | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R96 | `s 22(7) the claim or the part must be dismissed for lack of jurisdiction` | part3-proceedings:713 | I(b) a "where" condition not met | Where a tribunal does not have jurisdiction to determine a claim or a part of it | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R97 | `s 22(8) the kind of mediation the tribunal may refer the dispute to` | part3-proceedings:732 | outside a scope limit, in a function that returns a value (a person, a date, an amount), so there is no yes-or-no to refuse | arose from a mediation under Part 2 | NOTHING | none: a value cannot be JUST FALSE |
| R98 | `s 22(9) the tribunal may order the parties to attend the mediation personally` | part3-proceedings:745 | II(c) a "when", "upon" or "whenever" condition not met | when making a referral under subsection (8) | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R99 | `s 22(10) the tribunal may make the correction` | part3-proceedings:778 | I(a) outside a period the text fixes in its own words | within 14 days after the date on which the order is made | JUST FALSE | NOTHING (the reading the first ruling of 2026-11-05 rejects) |
| R100 | `s 22(12) the order may be enforced in the same manner as a judgment given or an order made by a District Court` | part3-proceedings:815 | I(c) outside a scope limit with no "only" | Every order made by a tribunal under subsection (1) | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R101 | `s 29(1) the person may disclose the information` | part4-miscellaneous:113 | I(c) outside a scope limit with no "only" | the Commissioner, an approved mediator, a tribunal magistrate or a Registrar | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R102 | `s 29(2) the person may publish the information` | part4-miscellaneous:132 | I(c) outside a scope limit with no "only" | a tribunal magistrate or a Registrar | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R103 | `s 30(1) the person has the same protection that a Magistrate has under the State Courts Act 1970` | part4-miscellaneous:147 | I(c) outside a scope limit with no "only" | A tribunal magistrate has and enjoys the same protection | NOTHING | JUST FALSE (the reading the first ruling of 2026-11-05 rejects) |
| R104 | `s 30(2) the Registrar has the same protection as a tribunal magistrate` | part4-miscellaneous:159 | II(c) a "when", "upon" or "whenever" condition not met | A Registrar, when exercising the jurisdiction and powers of a tribunal | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R105 | `s 31(1) the approved mediator is deemed to be a public servant for the purposes of the Penal Code 1871` | part4-miscellaneous:191 | II(c) a "when", "upon" or "whenever" condition not met | when carrying out the functions and duties of an approved mediator | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R106 | `s 31(2) the authorised person is deemed to be a public servant for the purposes of the Penal Code 1871` | part4-miscellaneous:204 | II(c) a "when", "upon" or "whenever" condition not met | when carrying out any function or duty of the Commissioner under this Act | JUST FALSE | NOTHING (the reading the second ruling rejects) |
| R107 | `s 35(2) regard may be had to the guidelines for the purposes of sections 20(7) and 25(4)` | part4-miscellaneous:219 | II(c) a "when", "upon" or "whenever" condition not met | Upon the publication of those guidelines in the Gazette | JUST FALSE | NOTHING (the reading the second ruling rejects) |

## Findings: what the text turns out to say

Numbered; each ends "Asserted." where an assertion in this folder asserts it, and the assertion is named by the file it is in (the build of this file fails if the named assertion text is not in the file).

1. `I am not sure` is not a no. A fact the person is unsure of arrives as `NOTHING`, and a rule that needs it answers `NOTHING`. Asserted.
2. The last day to submit a mediation request is counted with `add months`, which clamps to the last day of a shorter month: six months after 31 August 2025 is 28 February 2026, not 1 or 3 March (fork F6). Asserted.
3. A request submitted on 28 February 2026 is in time for that employee, and one submitted on 1 March 2026 is not (s 3(2)(f), "not later than 6 months after the last day of employment"). Asserted.
4. s 3(3)(a)(ii): a dispute whose material facts occurred exactly one year before the request meets the requirement; one day earlier it is outside a period the text fixes in its own words ("not earlier than one year before"), so the answer is `JUST FALSE` (ruled I(a)), whatever (i) and (iii) say. Asserted.
5. s 3(8): the duty to submit a mediation request before lodging does not apply once a tripartite mediation has been conducted. Asserted.
6. s 3(3)(c): a request must leave out a dispute that has a claim for an amount which section 16 bars from being lodged, and must not leave it out otherwise. Asserted.
7. s 3(4)(c): the Commissioner's power to pay the fee to a prescribed person is a grant to a stated class, so for a person who is not prescribed the answer is `NOTHING` (ruled I(c)). Asserted.
8. s 2(3): an officer the section names, who is not authorised by the Commissioner, may not act (`JUST FALSE`, a failed "if", reading (a)); an officer not appointed under s 3(1) of the Employment Act 1968 is outside the grant (`NOTHING`, ruled I(c)). Asserted.
9. s 7(1)(b) and (c): a settlement may equal the claim limit and may not exceed it. The limit is prescribed (s 12(7)) and is asked as a number; 0 means unknown. Asserted.
10. s 12(2)(c): an employer may bring a claim against an employee only for a matter in item 17 of the First Schedule, item 14 or 16 of the Second Schedule, or any other matter in the First or Second Schedule that regulations prescribe; item 16 of the First Schedule is not one of the named items. Asserted.
11. s 12(2)(c): limb (ii) is tested on its own words ("any other matter specified in the First or Second Schedule"): a Third Schedule matter, or no matter in the Schedules, gives `JUST FALSE` whatever the regulations prescribe and even where the employer's class is not known; item 16 of the First Schedule is neither named in limb (i) nor excluded, so it is limb (ii) and needs the regulations to prescribe it. The seat asks the employer's side with its own question. Asserted.
12. s 12(1) answers `NOTHING`, not no, when a requirement of s 12(2) to (7) fails: it grants jurisdiction for a claim that meets them and does not say in so many words that there is none otherwise (an open question, Q2; the reviewer expected `JUST FALSE`). The clear no is in the per-requirement answer, such as s 12(7). The seat's headline question gathers the six requirement answers by hand (see "Where I hand-gathered a legal effect"). Asserted.
13. s 15(1): the permission to abandon the excess is given by limb (a) alone or by limb (b) alone ("or"): a salary-type total of 10000 against a limit of 8000 gives `JUST TRUE` whatever is known of the other limit; two totals not over their limits give `JUST FALSE` ("Where" not met, ruled I(b)); a positive total against a limit that is not known gives `NOTHING`. The excess itself is a number: 10000 over 8000 is 2000. Asserted.
14. s 12(7), s 7(1), s 22(4) and (5): a total of nothing ("(if any)") is within a limit that is not known, because nothing exceeds any limit (fork F11); a positive total against a limit that is not known stays `NOTHING`. Asserted.
15. s 15(2)(a): when the claimant abandons the excess, the s 12(7) requirement is deemed satisfied, so s 12(1) answers `JUST TRUE` even where the total exceeds the limit. Asserted.
16. s 12(6): the day the certificate issued is not counted and the last day is (fork F7). Issued on 1 January 2026 with 60 days allowed, lodging on 2 March is in time and on 3 March is not. The 60 is a test figure; the Act states no period. Asserted.
17. s 16(2): once a claim is lodged, no other proceedings may be started in any other court, unless the claim is withdrawn, discontinued or dismissed for lack of jurisdiction. Asserted.
18. s 16(4): a lodged claim is deemed discontinued only where the dismissed employee makes representations under s 35(3) of the Industrial Relations Act 1960, and from the date the representations are made. Asserted.
19. s 16(7): an employee who made representations under s 8B(1) of the Retirement and Re-employment Act 1993 cannot lodge a claim for employment assistance payment unless the Minister allows a mediation request and a certificate issues; with both, the bar does not apply. Asserted.
20. s 19(3) is missing a word in the rendering (fork F8); it is read as s 5(3) reads, "prescribed by regulations". Asserted.
21. s 19(1)(b) and (c): a party cannot be represented by an advocate and solicitor or by an agent, paid or otherwise, and the Government may be represented by a public officer. Asserted.
22. s 20(8): the tribunal may decide in the absence of a party who, without reasonable excuse, fails to attend; where the party had a reasonable excuse the answer is `JUST FALSE` (reading (a)). Asserted.
23. s 22(6)(b): money paid is applied first to the amount ordered under s 22(1)(a), then to the costs. Asserted.
24. s 22(10): the tribunal may correct its order within 14 days after the date the order is made; for an order made on 25 February 2026 the last day is 11 March 2026 (fork F7). A correction on the 14th day is `JUST TRUE` and on the 15th `JUST FALSE`, for an order and for a statement of grounds (ruled I(a)); a District Court's extension under s 23(3)(a) is not an input. Asserted.
25. s 23: an appeal lies only with a District Court's permission, and only on a question of law or on lack of jurisdiction. An appeal on a question of fact answers `NOTHING`: the Act grants two grounds and does not say "only" (an open question, Q6). Asserted.
26. s 24(1): an appeal does not by itself stop enforcement of the tribunal's order. Asserted.
27. Gaps the first delivery had, now filled with what the text supports: s 3(1) (the request must relate to every dispute the claim will be lodged for), s 3(6)(b) (who may submit a request for a claimant is whom the regulations prescribe), s 6(2) (the certificate is issued to the claimant) and s 23(1) (the appeal is to the General Division of the High Court; a District Court only gives or refuses permission). Asserted.
28. s 24(1), the other half: an appeal does not stay enforcement by itself, but enforcement is stayed where a District Court or the General Division of the High Court orders a stay: with an appeal and an order the answer is `JUST TRUE`, with an appeal and no order `JUST FALSE`, and with no appeal the clause is not spoken to (`NOTHING`). Asserted.
29. ss 8 to 11 (the tribunals, their magistrates, the Registry) are decision functions about who may do what: a tribunal is presided over by a magistrate appointed under s 9(1)(a) or designated under s 9(5); eligibility for appointment under s 9(2) needs a "qualified person" as defined in the Legal Profession Act 1966 (an input, not staged); the President may revoke an appointment only on the Chief Justice's recommendation (fork F9); the Registry and its records are constants. Asserted.
30. The second ruling's (c), "when", "upon" and "whenever" count as "where": a rule given on an occasion is `JUST FALSE` when the occasion has not happened, and `JUST TRUE` when it has (and its other conditions hold). Examples: the Commissioner has not accepted the mediation request (s 3(5)); the tribunal is not dealing with a claim (s 20(2)(a)); the guidelines are not published in the Gazette (s 35(2)). Each of the fifteen functions of fork F12 (these fourteen and the s 2(2) twin below) has an assertion in its test module ending `EQUALS JUST TRUE` and one ending `EQUALS JUST FALSE`. Asserted.
31. s 2(2): "When this Act is applied to a counterclaim" is a "where", so for an ordinary claim a reference to the claimant is not read as a reference to the person making the counterclaim: the yes/no twin says `JUST FALSE`, and the function that returns the person cannot say so (it answers `NOTHING`). Asserted.
32. The second ruling's (d), "stayed until Y": s 16(8)(a) and s 17(4) are the bar question (`JUST TRUE` before Y, `JUST FALSE` after) and each has a second function, whether the stay has ended, which is `JUST FALSE` while the bar stands and is never `JUST TRUE` on the strength of the bar alone: after the Minister decides to allow, (c) says in its own words that the employee may proceed (`JUST TRUE`); after the Minister decides not to allow, and after the counterclaim proceedings are concluded, the text does not say that the claim or execution then proceeds (`NOTHING`) (fork F13). Asserted.
33. s 27(2)(a): where an employee dismissed without notice claims under s 14(2) of the Employment Act 1968, the employer bears the burden of proving just cause or excuse. Asserted.
34. The Act states no mediation fee, court fee, claim limit or period. Each is an input, and a seat question answers `NOTHING` where it is unknown. Asserted.
35. Because 0 means "I do not know" in the seat, a fee that is really nil cannot be stated: s 13(2)(b)(iii) says "the court fee (if any)", and a person who owes none can only say 0 and be answered `NOTHING`. This is a limit of the seat convention, not of the Act. Asserted.
36. A regulative rule is run with `#TRACE` and read by eye; every one has a decision function with assertions as its twin, because a trace prints no assertion line and `check.sh` cannot count it. A `MAY ... WITHIN` trace is always `FULFILLED` (see "What the main binary does not accept"), so the 14-day limit in s 22(10) is carried by the decision function.
37. A Minister's order under s 3(7) can lengthen or shorten the periods in s 3(2)(f) and (g) and s 3(3)(a)(ii); the Act's own periods are used as printed, and an order would change the answers.
38. `add days` is not in `daydate`; day arithmetic uses `DATE_FROM_SERIAL` and `DATE_SERIAL`. `add months` and `add years` clamp the day of the month.
39. An unbracketed `NOT a OR NOT b` gives a wrong answer on main without an error (with `a` and `b` both `FALSE` it returns `FALSE`, and the bracketed form returns `TRUE`); every `NOT` here is bracketed.

## What the main binary does not accept

Sorted by how the failure shows up.

**Silent: it returns a wrong answer with a clean exit.**
- `NOT a OR NOT b` and `NOT a AND NOT b` on one line, with no brackets, give wrong answers without an error.
  Measured on build 109 on 2026-11-05 with `a` and `b` both `FALSE`: `NOT a OR NOT b` returns `FALSE`, and `(NOT a) OR (NOT b)` returns `TRUE`.
  It cost four failing assertions in Part 2 before I saw it; every `NOT` in this row is now written `(NOT x)`.
  (`dialects.md`: main reads `NOT a OR b` as `NOT (a OR b)` and accepts it; unstable gives an error.)
- A `MAY ... WITHIN n` rule with no `LEST`, run with `#TRACE`, ends `FULFILLED` whether or not the permission lapsed (`dialects.md`: "a lapsed `MAY` without one is `FULFILLED` on both" builds), so the 14-day limit of s 22(10) cannot be read from the trace.
  The limit is carried by decision functions (`the last day on which the tribunal may make the correction`, and the `MAY` is also asserted through them) and is asserted there.
- `check.sh` counts assertions and errors, and does not see a different `#TRACE` outcome.
  I compared the full output of the two modules that run `#TRACE` (`eca-tests-part2.l4`, `eca-tests-part3-proceedings.l4`) between build 109 and the unstable build 1104 by diff, after joining lines, dropping brackets and dropping the `Code:` line of each diagnostic (see "Unstable dialect").

**Loud: an error that names the line.**
- A section-level `GIVEN`, `TYPICALLY`, an opaque `DECLARE`, `SET OF`, `REFUSE`, `#ASSERT REFUSED`, `YMD` and `@lang` are not accepted; none is used.
  `BECAUSE` is accepted only in `LEST BREACH ... BECAUSE`; a prohibition is written `SHANT`.
- `DECLARE T IS ONE OF A, B` on one line is a parse error; constructors go one per line.
  `ELSE` after `HENCE` is a parse error; the lapse is `LEST`.
- A genitive as a function argument, `f facts's x`, is "not a function": it is written `f (facts's x)`.
- `add days` is not in `daydate` (it is in `actus-schedule`); days are added with `DATE_FROM_SERIAL ((DATE_SERIAL d) PLUS n)` and subtracted with `(DATE_SERIAL a) MINUS (DATE_SERIAL b)`.
- A hyphenated module name must be written in backticks in `IMPORT`.
- A name defined in two imported modules cannot be used; every function name here carries its section number, and constructors are unique across all types in a module.
- An `#ASSERT` must be on one line.
- A `DATE` after `WITHIN` is a type error ("The WITHIN clause of a regulative rule is expected to be of type ..." with `NUMBER`; measured on build 109 on 2026-11-05).
  So a regulative rule here takes a number of days (`the number of days allowed by section 3(2)`), and the decision function computes the last day from the date.

## What check.sh prints

Run from the row folder on 2026-11-05 as `L4=<build 109> L4_MAIN=<build 108> ./check.sh`.
The `l4` that wrote and checked the row: `1.6.109 (main, 4c887e0, 2026-11-04)`.
The main build `check.sh` compared it with: `1.6.108 (main, 2ae7c9b, 2026-11-02)`.
The first delivery of this row recorded 1040 satisfied, 0 failed, 0 refused, 0 errors over 17 modules (in `encoding.json` at the time); this revision prints the figures below.
The last intermediate run before the seat and cases were first written was 828 satisfied, 0 failed, 0 refused, 0 errors.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
eca-cases-seat.l4                              0       235       0        0         0 |      0       235       0        0  same
eca-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
eca-part1-preliminary.l4                       0         0       0        0         0 |      0         0       0        0  same
eca-part2-mediation.l4                         0         0       0        0         0 |      0         0       0        0  same
eca-part3-appeals.l4                           0         0       0        0         0 |      0         0       0        0  same
eca-part3-jurisdiction.l4                      0         0       0        0         0 |      0         0       0        0  same
eca-part3-proceedings.l4                       0         0       0        0         0 |      0         0       0        0  same
eca-part4-miscellaneous.l4                     0         0       0        0         0 |      0         0       0        0  same
eca-schedules.l4                               0         0       0        0         0 |      0         0       0        0  same
eca-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
eca-tests-part1.l4                             0       134       0        0         0 |      0       134       0        0  same
eca-tests-part2.l4                             0       209       0        0         0 |      0       209       0        0  same
eca-tests-part3-appeals.l4                     0        78       0        0         0 |      0        78       0        0  same
eca-tests-part3-jurisdiction.l4                0       259       0        0         0 |      0       259       0        0  same
eca-tests-part3-proceedings.l4                 0       143       0        0         0 |      0       143       0        0  same
eca-tests-part4.l4                             0        41       0        0         0 |      0        41       0        0  same
eca-tests-schedules.l4                         0        71       0        0         0 |      0        71       0        0  same
TOTAL (17 modules)                             0      1170       0        0           |      0      1170       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## What the text does not answer

The Act leaves these to instruments that are not among the sources, or does not say:
- the mediation fee (s 3(3)(d)), the court fee (s 13(2)(b)(iii)) and the claim limits (s 12(7)): the Act states no figure for any of them;
- the period for lodging after a certificate issues (s 12(6)), the period for applying to register or to set aside a settlement agreement (s 7(2), (4)) and the time and manner of an application to transfer (s 17(2));
- the forms, the manner of filing and the documents required (ss 3(2), 13(2), 7(1)(a)), which are in Rules of Court and practice directions;
- which employees, employers, representatives and observers regulations prescribe (ss 2(1), 5(2)(e) and (3), 12(2), 18(4), 19(2)(e) and (3));
- what the borrowed definitions mean (`salary`, `workman`, `employment assistance payment`, `tripartite mediation`), and the periods in s 65(2A) and (2B) of the Employment Act 1968;
- the regulations that calculate compensation for a wrongful dismissal (ss 20(7)(b), 25(4)(b));
- whether a ground of appeal other than the two in s 23(1) is barred (the Act grants two grounds and does not say "only");
- whether a claim that fails a requirement of s 12 is without jurisdiction in so many words (s 12(1) grants jurisdiction; s 22(7) speaks of a tribunal that "does not have jurisdiction");
- what follows if a claimant lodges a claim without a certificate, other than that s 13(2)(b)(i) says the claim "must be accompanied" by one;
- whether a last day that is a Sunday or a public holiday moves to the next day: the Interpretation Act s 50(b) says it does, and this encoding does not apply it (see Dependencies);
- whether a District Court has extended the time under s 22(10) (s 23(3)(a)): a correction after the 14th day is answered `JUST FALSE` here, and a District Court's extension is not an input;
- the figure of the excess in s 15(1): it is the difference between the total claimed and the claim limit, so it is known only when the limit is.

## Unstable dialect

I read `references/dialects.md` of the `writing-l4-rules` skill against the shapes this Act needs, and I ran the finished main row on the unstable build 1104 (sha256 `7b64926ba7eb92a62a55ba402343bd777c19d4cdb59f26e0cd027cc2f71a8bc1`).
What I found:
- **Time and versions.**
  The Act has deadlines counted from events (ss 3(2), 3(3)(a)(ii), 12(6), 22(10)) and it carries amendments in force from different days (the margin notes `[55/2018]`, `[40/2019]`, `[Act 25 of 2021 wef 01/04/2022]`); the row encodes the one version in force from 1 April 2025.
  On main the deadlines are decision functions over `Date d m y`, and a regulative rule that needs a deadline takes a precomputed number of days (the workaround: `the number of days allowed by section 3(2)` instead of a date).
- **Other workarounds on main.**
  Bracketed `NOT`; `NOTHING` and named constructors where unstable has `REFUSE`; no section `GIVEN`, so each function takes its own inputs; no `TYPICALLY`; `Date d m y` for `YMD`; days added with `DATE_FROM_SERIAL`; `MAY ... WITHIN` with no `LEST`, because main ignores a `LEST` after `MAY`.
- **What the row does on unstable.**
  Every test module and the case file give the same assertion counts on the unstable build as on main (134, 209, 78, 259, 143, 41, 71, 235, none failing), and the two modules that run `#TRACE` print the same outcomes after the pretty-printer's line breaks and brackets are normalised and the `Code:` line of each diagnostic is dropped (main prints `eval/assertion-passed` where unstable prints `<none>`).
  So the main row reads the same on both builds as far as this comparison goes; it does not compare anything an assertion or trace does not exercise.
- **Decision.**
  I did not write a second encoding on unstable.
  A time-aware rule on unstable could state the 14-day permission in s 22(10) and the deadlines in s 3(2) directly, and that is the one shape that might have earned one; I judged that it would restyle the same answers rather than change them, and I did not do it in this pass.
  If a second encoding is wanted, those two provisions are where to start.

## What would need doing before it is worth relying on

1. A lawyer reads "Marginal readings for a lawyer" and rules on reading (a) (the failed "if" and the "must" requirement); every row rests on that ruling.
2. A lawyer reads the ten forks (F1, F6, F7, F8, F9, F10, F11, F12, F13, F14) and confirms or reverses the reading taken; F9, F10 and F11 are assumed, not ruled (they extend the rulings of 2026-11-05 to words they do not name), and F12 to F14 record what I decided at each site of the second ruling.
3. The text is checked against the official Singapore Statutes Online version, which this converter rendering is not, and against the current in-force date: the encoding is of the consolidation in force from 1 April 2025.
4. The regulations, Rules of Court and practice directions that supply the fees, limits, periods, forms and prescribed classes are brought in as a second source, so that the inputs have figures; until then the seat answers `NOTHING` wherever a figure decides.
5. A lawyer confirms the Hohfeld kinds in "Jural relations", which the ruling N2 holds back from the person-facing answers until a lawyer confirms the typing.
6. A Minister's order under s 3(7), or an amendment of the Schedules under s 32, is checked for: either would change the answers.
7. The seat is put in front of an employee (not a lawyer) to see whether the questions read as they would ask them; the 0-means-unknown convention in particular is a limitation (finding 35).
8. A lawyer rules on the ten open questions ("Open questions"): each is a place where the Act's words could be a scope limit (`NOTHING`) or a condition (`JUST FALSE`).
9. The dependencies are filled: the Interpretation Act's s 50(b) is wired in with a list of public holidays, and the other Acts in "Dependencies" are staged, so that the inputs that stand for them have content.

## The text

Everything above is about `inputs/ECA2016.txt`, a converter rendering and unofficial text of the informal consolidation of the Employment Claims Act 2016, 2020 Revised Edition, in force from 1 April 2025.
The licence note is `SOURCE-LICENSE.md`, which points at the subject-level note deposited with the text.
