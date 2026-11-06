# NOTES (roc4): Rules of Court 2021 (Singapore), G.N. No. S 914/2021, Order 19, lines 2231-2875

Status (how each claim here was verified, 2026-11-05):
the counts of satisfied assertions come from running `check.sh` (output at the end of this file) on builds 1.6.109 and 1.6.108;
the coverage table and the marginal-readings tables were built by scripts (`work/cov.py`, `work/marginal.py`) from the text and from the modules, not typed;
the expected value of every assertion was written by hand from the text before the run;
a statement about what a main build accepts was probed on both builds on 2026-11-05 and names its probe.

**The text is a converter rendering, not the official text.**
The source file is a plain-text rendering made by a converter script from Singapore Statutes Online.
It is not the official text, and nothing in this row has been checked against the official text.
Where the rendering looks damaged (finding 1) the finding says so.

**PLAN.md section 2 is superseded for this row.**
PLAN.md section 2 had a function `... is filed in time` answer `NOTHING` outside a period the text states.
The ruling of 2026-11-05 (a), printed in BRIEF.md and copied below, governs instead: outside a period the text fixes in its own words, the answer is `JUST FALSE`.
Every timed function in this row follows the brief.

This part is Order 19 only: 41 rules in four Divisions (Division 1 General, rules 1-12; Division 2 District Court and Magistrate's Court to the General Division, rules 13-23; Division 3 General Division to Appellate Division or Court of Appeal, rules 24-40; Division 4 Medical Registration Act appeals, rule 41).

## Files

| file | what it is |
| --- | --- |
| `roc4-order-19-div-1.l4` | layer 1, rules 1-12 |
| `roc4-order-19-div-2.l4` | layer 1, rules 13-23 |
| `roc4-order-19-div-3.l4` | layer 1, rules 24-40 |
| `roc4-order-19-div-4.l4` | layer 1, rule 41 |
| `roc4-order-19-duties.l4` | layer 1, regulative form of the Order's timed duties and of the four bars that name the respondent (rules 8(3), 14(1), 15(1), 15(3), 17(4)-(10), 17(9), 18(3), 22, 25(1), 26(1), 26(8), 26(17), 30(4)-(11), 30(10), 31(3), 35(14), 36, 41(2)-(3)) |
| `roc4-tests-div-1.l4` ... `roc4-tests-div-4.l4`, `roc4-tests-duties.l4` | tests of the above |
| `roc4-seat.l4` | layer 2: 293 `@export`ed questions for a person in an appeal, rules 1-41 |
| `roc4-cases-seat.l4` | layer 2 cases: 914 assertions over the 293 questions |
| `roc-core.l4`, `roc-definitions.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` | supplied, not edited |

Every name in a layer-1 file begins with the provision's own label (`o 19 r 14(1) ...`).
The seat wiring helpers begin `o 19 seat`; the seat questions begin "Under Order 19, rule N,".

## Coverage (roc4)

Built by `work/cov.py` from the text (lines 2231-2875 of `inputs/SCJA1969-S914-2021.txt`) and from the names defined in the five layer-1 modules; no row was typed by hand.
A row is one Order heading, Division heading, rule heading, rule paragraph, sub-paragraph, item or defined term; each row has exactly one disposition.
The L4 name is the first function the module defines under that provision's label; "(+N more)" counts the others under the same label, and "in the rule for X" means the sub-paragraph is answered inside its parent paragraph's function.

Dispositions (486 rows): encoded 396; fork 44; inert (reason 1) 46.
Rows by kind: Division heading 4; Order heading and title 1; defined term 13; item 30; paragraph 204; rule heading 41; sub-paragraph 193.
There is no `repealed or blank in this text` row and no `inert` row of reason 2 or 3 in Order 19: every inert row is a heading or title (reason 1, not operative), the Order heading and title (1), the four Division headings (4) and the 41 rule headings (41).

Audit (all measured by script, `work/cov.py` and `work/mknotes.py`):

- The range holds 645 non-blank lines; every one falls in some row (uncovered: none).
- Compared with `inputs/RULE-INDEX.md`, section roc4: it lists 41 rules, 1 to 41 with none absent; this table has 41 rule-heading rows, and for each the first line of the rule body is the line RULE-INDEX gives (41 of 41 agree).
- The table has 486 rows now.
  Its first cut had 173 rows and left 55 non-blank lines uncovered (lines 2821-2875, the heading and body of rule 41), because the converter text uses non-breaking spaces where the script expected plain spaces: it found 32 of the 41 rule headings, so the rules after the first missed heading were cut short.
  The coverage check (every line in some row) is what showed it; the script was corrected and the table rebuilt.
- Units counted a second way, by pattern, as a cross-check: 196 numbered-paragraph markers plus 8 rules with no numbered paragraph give the 204 paragraph rows; the 31 lines that contain a "( x )" pattern but start no sub-paragraph row were read and are cross-references in running text (for example "paragraph (a), (b), (c) or (d)").
- Every "encoded" row has a test: `work/testcov.py` takes each of the 352 `o 19 ...` functions the four div modules define and finds its name in an assertion in `roc4-tests-div-*.l4` (352 of 352; 0 only through the seat; none without).
  Its first run found four without one (the two timing helpers behind rule 8(3), the rule 4(1A) period, and `o 19 r 41(10) listed provision applies`); 11 assertions were added to `roc4-tests-div-1.l4` and `-div-4.l4`.

Forks: the 44 `fork` rows point at the register below (F3 rule 4, F4 rule 8, F5 rule 26(2), F7 rule 41(10) and (12)); a row may also carry "hand-gathered", which names the E1 option B function that gathers it.

| row | lines | kind | disposition | L4 name | note |
| --- | --- | --- | --- | --- | --- |
| O 19 (title) | 2231-2232 | Order heading and title | inert (reason 1) | - | heading and title of the Order |
| O 19 Division 1 heading | 2233 | Division heading | inert (reason 1) | - | General |
| O 19 r 1 heading | 2234 | rule heading | inert (reason 1) | - | Scope of this Order (O. 19, r. 1) |
| O 19 r 1(a) | 2235 | sub-paragraph | encoded | `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` |  |
| O 19 r 1 | 2235-2251 | paragraph | encoded | `o 19 r 1 this Order applies` (+21 more) | hand-gathered: `o 19 r 1 this Order applies` (E1, option B) |
| O 19 r 1(a)(i) | 2236-2237 | item | encoded | in the rule for 1(a): `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` |  |
| O 19 r 1(a)(ii) | 2238-2239 | item | encoded | in the rule for 1(a): `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` |  |
| O 19 r 1(a)(iii) | 2240-2241 | item | encoded | in the rule for 1(a): `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` |  |
| O 19 r 1(b) | 2242-2243 | sub-paragraph | encoded | `o 19 r 1(b) this Order applies to an appeal against a judgment of the General Division` |  |
| O 19 r 1(c) | 2244-2245 | sub-paragraph | encoded | `o 19 r 1(c) this Order applies to an appeal against a judgment of the Appellate Division` |  |
| O 19 r 1(d) | 2246-2247 | sub-paragraph | encoded | `o 19 r 1(d) this Order applies to an appeal from a tribunal to the Appellate Division or the Court of Appeal` (+2 more) |  |
| O 19 r 1(e) | 2248-2249 | sub-paragraph | encoded | `o 19 r 1(e) this Order applies to an application to the appellate Court relating to an appeal` (+1 more) |  |
| O 19 r 1(f) | 2250-2251 | sub-paragraph | encoded | `o 19 r 1(f) this Order applies to an appeal against an order or decision of a Disciplinary Tribunal` |  |
| O 19 r 2 heading | 2252 | rule heading | inert (reason 1) | - | General matters and structure of this Order (O. 19, r. 2) |
| O 19 r 2(1) | 2253 | paragraph | encoded | `o 19 r 2(1) this Order yields to a written law on the right to appeal or on permission to appeal` |  |
| O 19 r 2(2) | 2253 | paragraph | encoded | `o 19 r 2(2) Division 2 concerns the appeal from the District Court or the Magistrate's Court to the General Division` |  |
| O 19 r 2(3)(a) | 2254-2255 | sub-paragraph | encoded | `o 19 r 2(3)(a) Division 3 concerns the appeal from the General Division to the Appellate Division or the Court of Appeal` |  |
| O 19 r 2(3) | 2254-2259 | paragraph | encoded | `o 19 r 2(3)(a) Division 3 concerns the appeal from the General Division to the Appellate Division or the Court of Appeal` (+2 more) |  |
| O 19 r 2(3)(b) | 2256-2257 | sub-paragraph | encoded | `o 19 r 2(3)(b) Division 3 concerns the appeal from a tribunal to the Appellate Division or the Court of Appeal` |  |
| O 19 r 2(3)(c) | 2258-2259 | sub-paragraph | encoded | `o 19 r 2(3)(c) Division 3 concerns the appeal from the Appellate Division to the Court of Appeal` |  |
| O 19 r 2(4) | 2260 | paragraph | encoded | `o 19 r 2(4) Division 4 concerns the appeal to the General Division from a Disciplinary Tribunal under the Medical Registration Act` |  |
| O 19 r 3 heading | 2261 | rule heading | inert (reason 1) | - | Definitions of this Order (O. 19, r. 3) |
| O 19 r 3 "bundle of authorities" | 2262 | defined term | encoded | `o 19 r 3 a document is a bundle of authorities` |  |
| O 19 r 3 | 2262-2277 | paragraph | encoded | `o 19 r 3 a decision is a judgment` (+39 more) |  |
| O 19 r 3 "core bundle of documents" | 2263 | defined term | encoded | `o 19 r 3 a document is part of a core bundle of documents` |  |
| O 19 r 3(a) | 2264-2265 | sub-paragraph | encoded | `o 19 r 3(a) a case where judgment is given or the action is dismissed at trial because one or more parties are absent` (+1 more) |  |
| O 19 r 3 "judgment" | 2264-2273 | defined term | encoded | `o 19 r 3 a decision is a judgment` |  |
| O 19 r 3(b) | 2266-2267 | sub-paragraph | encoded | `o 19 r 3(b) after damages are assessed or accounts are taken` |  |
| O 19 r 3(c) | 2268-2269 | sub-paragraph | encoded | `o 19 r 3(c) an application for a committal order for contempt of court` |  |
| O 19 r 3(d) | 2270-2271 | sub-paragraph | encoded | `o 19 r 3(d) an application for a prerogative order` |  |
| O 19 r 3(e) | 2272-2273 | sub-paragraph | encoded | `o 19 r 3(e) an appeal against a judgment described in paragraphs (a) to (d)` |  |
| O 19 r 3 "record of appeal" | 2274 | defined term | encoded | `o 19 r 3 a document is part of the record of appeal` |  |
| O 19 r 3 "record of proceedings" | 2275 | defined term | encoded | `o 19 r 3 a document is part of the record of proceedings` |  |
| O 19 r 3 "second core bundle" | 2276 | defined term | encoded | `o 19 r 3 a document is part of the second core bundle` |  |
| O 19 r 3 "trial" | 2277 | defined term | encoded | `o 19 r 3 a proceeding is part of the trial` |  |
| O 19 r 4 heading | 2278 | rule heading | inert (reason 1) | - | When time for appeal starts to run (O. 19, r. 4) |
| O 19 r 4(1) | 2279 | paragraph | fork | `o 19 r 4(1) the date after which the time for the filing starts to run` (+2 more) | F3; hand-gathered: `o 19 r 4 the date after which the time for the filing starts to run` (E1, option B) |
| O 19 r 4(1A) | 2280 | paragraph | fork | `o 19 r 4(1A) the date after which the time for the filing starts to run` (+2 more) | F3 |
| O 19 r 4(2)(a) | 2281 | sub-paragraph | encoded | `o 19 r 4(2)(a) the lower Court is deemed to have heard and determined the issue of costs` (+6 more) |  |
| O 19 r 4(2) | 2281-2291 | paragraph | encoded | `o 19 r 4(2)(a) the lower Court is deemed to have heard and determined the issue of costs` (+8 more) |  |
| O 19 r 4(2)(a)(i) | 2282-2283 | item | encoded | `o 19 r 4(2)(a)(i) decided on the parties' entitlement to costs, even if the amount of costs or disbursements has not been determined` |  |
| O 19 r 4(2)(a)(ii) | 2284-2285 | item | encoded | `o 19 r 4(2)(a)(ii) ordered that costs be assessed` |  |
| O 19 r 4(2)(a)(iii) | 2286-2287 | item | encoded | `o 19 r 4(2)(a)(iii) ordered that costs be reserved` |  |
| O 19 r 4(2)(a)(iv) | 2288-2289 | item | encoded | `o 19 r 4(2)(a)(iv) decided that there is to be no order as to costs or that each party is to bear its own costs` |  |
| O 19 r 4(2)(b) | 2290-2291 | sub-paragraph | fork | `o 19 r 4(2)(b) the date after which the time for the filing starts to run for the bifurcated portion` (+1 more) | F3 |
| O 19 r 5 heading | 2292 | rule heading | inert (reason 1) | - | Permission to intervene (O. 19, r. 5) |
| O 19 r 5(1) | 2293 | paragraph | encoded | `o 19 r 5(1) a person may apply to intervene in the appeal with the permission of the appellate Court` | gap: the text says a non-party "may apply to intervene ... with the permission of the appellate Court" and does not say whether it may intervene without permission; no function asks it |
| O 19 r 5(2) | 2293 | paragraph | encoded | `o 19 r 5(2) the application and the supporting affidavit are filed and served as required` | silent: no time limit for the application to intervene; no function |
| O 19 r 5(3) | 2294 | paragraph | encoded | `o 19 r 5(3) the supporting affidavit sets out the applicant's interest` |  |
| O 19 r 5(4) | 2295 | paragraph | encoded | `o 19 r 5(4) the appellate Court may impose conditions on the permission to intervene` (+1 more) |  |
| O 19 r 6 heading | 2296 | rule heading | inert (reason 1) | - | Stay of enforcement, etc. (O. 19, r. 6) |
| O 19 r 6(1) | 2297 | paragraph | encoded | `o 19 r 6(1) the appeal operates as a stay of enforcement or of proceedings under the decision of the lower Court` |  |
| O 19 r 6(2) | 2297 | paragraph | encoded | `o 19 r 6(2) an intermediate act or proceeding is invalidated by the appeal` |  |
| O 19 r 6(3) | 2298 | paragraph | fork | `o 19 r 6(3) interest is allowed for the time enforcement has been delayed by the appeal` | F10; silent: no rate of interest; no function |
| O 19 r 7 heading | 2299 | rule heading | inert (reason 1) | - | Powers of appellate Court (O. 19, r. 7) |
| O 19 r 7(1) | 2300 | paragraph | encoded | `o 19 r 7(1) the appellate Court may give directions for the non-party to state its case` (+1 more) |  |
| O 19 r 7(2) | 2300 | paragraph | encoded | `o 19 r 7(2) the appellate Court may allow or invite a non-party to give its views on any matter in the appeal` (+1 more) |  |
| O 19 r 7(3) | 2301 | paragraph | encoded | `o 19 r 7(3) the parties are allowed to make an oral submission at the hearing of the appeal` |  |
| O 19 r 7(4) | 2302 | paragraph | encoded | `o 19 r 7(4) the appellate Court may make an order although that part is not the subject of any appeal and the reason is not stated by anyone` |  |
| O 19 r 7(5) | 2303 | paragraph | encoded | `o 19 r 7(5) the appellate Court's powers to decide the merits are restricted` |  |
| O 19 r 7(6) | 2304 | paragraph | encoded | `o 19 r 7(6) the appellate Court may order a new trial` |  |
| O 19 r 7(7) | 2305 | paragraph | fork | `o 19 r 7(7) further evidence may be given` (+1 more) | F-OTHERTHAN |
| O 19 r 7(8) | 2306 | paragraph | encoded | `o 19 r 7(8) the further evidence is adduced as required` |  |
| O 19 r 8 heading | 2307 | rule heading | inert (reason 1) | - | Absence of parties (O. 19, r. 8) |
| O 19 r 8(1) | 2308 | paragraph | fork | `o 19 r 8(1) the appeal may be dismissed` | F4 |
| O 19 r 8(2) | 2308 | paragraph | fork | `o 19 r 8(2) the appeal may proceed in the absence of a respondent` | F4 |
| O 19 r 8(3) | 2309 | paragraph | fork | `o 19 r 8(3) the Court may restore the appeal for rehearing` (+7 more) | F-MUST |
| O 19 r 9 heading | 2310 | rule heading | inert (reason 1) | - | Expedited appeal (O. 19, r. 9) |
| O 19 r 9(1) | 2311 | paragraph | encoded | `o 19 r 9(1) the lower Court or the appellate Court may order an expedited appeal` |  |
| O 19 r 9(2) | 2311 | paragraph | encoded | `o 19 r 9(2) the lower Court or the appellate Court may dispense with or modify a provision for the purposes of the appeal` |  |
| O 19 r 10 heading | 2312 | rule heading | inert (reason 1) | - | Withdrawal of appeal or application (O. 19, r. 10) |
| O 19 r 10(1) | 2313 | paragraph | encoded | `o 19 r 10(1) the appeal or application may still be withdrawn` (+1 more) |  |
| O 19 r 10(2) | 2313 | paragraph | encoded | `o 19 r 10(2) the appeal or application is deemed withdrawn in relation to the relevant parties` (+1 more) |  |
| O 19 r 10(3)(a) | 2314-2315 | sub-paragraph | encoded | `o 19 r 10(3)(a) a party may request the appellate Court in writing for directions on those issues` |  |
| O 19 r 10(3) | 2314-2322 | paragraph | encoded | `o 19 r 10(3)(a) a party may request the appellate Court in writing for directions on those issues` (+3 more) |  |
| O 19 r 10(3)(b) | 2316-2317 | sub-paragraph | encoded | `o 19 r 10(3)(b) oral arguments may be made in the request` |  |
| O 19 r 10(3)(c) | 2318 | sub-paragraph | encoded | `o 19 r 10(3)(c)(i) the Registrar may remove the appeal or application from the list` (+1 more) |  |
| O 19 r 10(3)(c)(i) | 2319-2320 | item | encoded | `o 19 r 10(3)(c)(i) the Registrar may remove the appeal or application from the list` |  |
| O 19 r 10(3)(c)(ii) | 2321-2322 | item | encoded | `o 19 r 10(3)(c)(ii) the Registrar may give directions on the making of written submissions for the request` |  |
| O 19 r 10(4)(a) | 2323-2324 | sub-paragraph | encoded | `o 19 r 10(4)(a) the appeal or application remains on the list` |  |
| O 19 r 10(4) | 2323-2329 | paragraph | encoded | `o 19 r 10(4)(a) the appeal or application remains on the list` (+2 more) |  |
| O 19 r 10(4)(b) | 2325 | sub-paragraph | encoded | `o 19 r 10(4)(b)(i) the appellate Court may at the hearing decide an issue that remains outstanding` (+1 more) |  |
| O 19 r 10(4)(b)(i) | 2326-2327 | item | encoded | `o 19 r 10(4)(b)(i) the appellate Court may at the hearing decide an issue that remains outstanding` |  |
| O 19 r 10(4)(b)(ii) | 2328-2329 | item | encoded | `o 19 r 10(4)(b)(ii) the appellate Court may at the hearing make an order as to the disposal of the security for costs` |  |
| O 19 r 11 heading | 2330 | rule heading | inert (reason 1) | - | Consent judgment or order (O. 19, r. 11) |
| O 19 r 11(1) | 2331 | paragraph | encoded | `o 19 r 11(1) the Registrar is to inform the parties accordingly` (+1 more) |  |
| O 19 r 11(2) | 2331 | paragraph | encoded | `o 19 r 11(2) the appellate Court may give a further order or direction` |  |
| O 19 r 12 heading | 2332 | rule heading | inert (reason 1) | - | Judgment (O. 19, r. 12) |
| O 19 r 12(1)(a) | 2333-2334 | sub-paragraph | encoded | `o 19 r 12(1)(a) orally at a subsequent date` (+1 more) |  |
| O 19 r 12(1) | 2333-2336 | paragraph | encoded | `o 19 r 12(1) the appellate Court may give its decision in this way` (+6 more) |  |
| O 19 r 12(1)(b) | 2335-2336 | sub-paragraph | encoded | `o 19 r 12(1)(b) in writing at a subsequent date` (+1 more) |  |
| O 19 r 12(2)(a) | 2337-2338 | sub-paragraph | encoded | `o 19 r 12(2)(a) the appellate Court may direct the Registrar to inform the parties of its decision` |  |
| O 19 r 12(2) | 2337-2345 | paragraph | encoded | `o 19 r 12(2)(a) the appellate Court may direct the Registrar to inform the parties of its decision` (+1 more) |  |
| O 19 r 12(2)(b) | 2339-2340 | sub-paragraph | encoded | `o 19 r 12(2)(b) the parties are informed of what they are to be informed of` |  |
| O 19 r 12(3) | 2346 | paragraph | encoded | `o 19 r 12(3) a party is entitled to a copy of the decision` | silent: the amount of "the relevant charges"; no function |
| O 19 r 12(4) | 2347 | paragraph | encoded | `o 19 r 12(4) the judgment may be delivered orally despite the absence of one or more of the other Judges` |  |
| O 19 Division 2 heading | 2348 | Division heading | inert (reason 1) | - | Appeal from District Court and Magistrate’s Court to General Division |
| O 19 r 13 heading | 2349 | rule heading | inert (reason 1) | - | Scope of this Division (O. 19, r. 13) |
| O 19 r 13(1)(a) | 2350-2351 | sub-paragraph | encoded | in the rule for 13(1): `o 19 r 13(1) this Division applies to an appeal against a judgment of the District Court or Magistrate's Court` |  |
| O 19 r 13(1) | 2350-2355 | paragraph | encoded | `o 19 r 13(1) this Division applies to an appeal against a judgment of the District Court or Magistrate's Court` |  |
| O 19 r 13(1)(b) | 2352-2353 | sub-paragraph | encoded | in the rule for 13(1): `o 19 r 13(1) this Division applies to an appeal against a judgment of the District Court or Magistrate's Court` |  |
| O 19 r 13(1)(c) | 2354-2355 | sub-paragraph | encoded | in the rule for 13(1): `o 19 r 13(1) this Division applies to an appeal against a judgment of the District Court or Magistrate's Court` |  |
| O 19 r 13(2) | 2356 | paragraph | encoded | `o 19 r 13(2) a court is the lower Court` |  |
| O 19 r 13 "lower Court" | 2356 | defined term | encoded | `o 19 r 13(2) a court is the lower Court` |  |
| O 19 r 14 heading | 2357 | rule heading | inert (reason 1) | - | Bringing of appeal (O. 19, r. 14) |
| O 19 r 14(1) | 2358 | paragraph | fork | `o 19 r 14(1) the appellant must file and serve the notice of appeal within 14 days after the date of the judgment` (+4 more) | F12 |
| O 19 r 14(2) | 2358 | paragraph | encoded | `o 19 r 14(2) the General Division may extend the time for filing and serving the notice of appeal` (+1 more) |  |
| O 19 r 15 heading | 2359 | rule heading | inert (reason 1) | - | Permission to appeal (O. 19, r. 15) |
| O 19 r 15(1) | 2360 | paragraph | fork | `o 19 r 15(1) the application for permission to the lower Court is made and served as required` (+4 more) | F12 |
| O 19 r 15(2) | 2360 | paragraph | encoded | `o 19 r 15(2) the application for permission to the General Division is made and served as required` (+1 more) |  |
| O 19 r 15(3) | 2361 | paragraph | encoded | `o 19 r 15(3) the applicant must file and serve the notice of appeal within 14 days after permission is granted` (+3 more) |  |
| O 19 r 15(4) | 2362 | paragraph | encoded | `o 19 r 15(4) the General Division may extend the time for filing and serving an application for permission to appeal` (+1 more) |  |
| O 19 r 16 heading | 2363 | rule heading | inert (reason 1) | - | Security for costs (O. 19, r. 16) |
| O 19 r 16(1) | 2364 | paragraph | encoded | `o 19 r 16(1) the appellant has provided security for costs and filed the certificate as required` |  |
| O 19 r 16(2) | 2364 | paragraph | encoded | `o 19 r 16(2) the appellants need to provide only one set of security for the appeal` |  |
| O 19 r 16(3) | 2365 | paragraph | encoded | `o 19 r 16(3) the appellant must provide security for each respondent or each set of respondents` (+1 more) |  |
| O 19 r 16(4)(a) | 2366-2367 | sub-paragraph | encoded | `o 19 r 16(4)(a) a solicitor's undertaking in Form 37` |  |
| O 19 r 16(4) | 2366-2371 | paragraph | fork | `o 19 r 16(4) the security is in a form the text allows` (+4 more) | F-MUST |
| O 19 r 16(4)(b) | 2368-2369 | sub-paragraph | encoded | `o 19 r 16(4)(b) a deposit in the Registry or with the Accountant-General` |  |
| O 19 r 16(4)(c) | 2370-2371 | sub-paragraph | encoded | `o 19 r 16(4)(c) any other form` |  |
| O 19 r 16(5)(a) | 2372-2373 | sub-paragraph | encoded | `o 19 r 16(5)(a) the amount of security for a Magistrate's Court action` |  |
| O 19 r 16(5) | 2372-2375 | paragraph | encoded | `o 19 r 16(5) the amount of security the appellant must provide` (+3 more) |  |
| O 19 r 16(5)(b) | 2374-2375 | sub-paragraph | encoded | `o 19 r 16(5)(b) the amount of security for a District Court action` |  |
| O 19 r 16(6) | 2376 | paragraph | encoded | `o 19 r 16(6) a party may apply to the appellate Court to vary or waive the amount of security` |  |
| O 19 r 16(7) | 2377 | paragraph | encoded | `o 19 r 16(7) the appellate Court may order further security for costs to be given` |  |
| O 19 r 17 heading | 2378 | rule heading | inert (reason 1) | - | Documents to be filed (O. 19, r. 17) |
| O 19 r 17(1) | 2379 | paragraph | encoded | `o 19 r 17(1) the lower Court must issue its written grounds of decision` | silent: no deadline for the lower Court's written grounds of decision; no function |
| O 19 r 17(2) | 2379 | paragraph | encoded | `o 19 r 17(2) the Registry must notify the parties that the record of proceedings is ready for collection` |  |
| O 19 r 17(3)(a) | 2380-2381 | sub-paragraph | encoded | `o 19 r 17(3)(a) the appellant must apply in writing to the Registrar to proceed with the appeal and for a copy of the record of proceedings` |  |
| O 19 r 17(3) | 2380-2385 | paragraph | encoded | `o 19 r 17(3) no written grounds of decision are issued within 12 weeks` (+5 more) |  |
| O 19 r 17(3)(b) | 2382-2383 | sub-paragraph | encoded | `o 19 r 17(3)(b) the period of notice to strike out` (+1 more) |  |
| O 19 r 17(3)(c) | 2384-2385 | sub-paragraph | encoded | `o 19 r 17(3)(c) the respondent may apply to strike out the appeal` |  |
| O 19 r 17(4)(a) | 2386-2387 | sub-paragraph | encoded | `o 19 r 17(4)(a) the record of appeal` |  |
| O 19 r 17(4) | 2386-2394 | paragraph | encoded | `o 19 r 17(4) the appellant must file and serve the appellant's documents within 28 days and the respondent and the appellant must follow` (+8 more) | silent: rule 17 sets no page limit on the record of appeal (a core bundle has one in rule 19(2)); no function |
| O 19 r 17(4)(b) | 2388-2389 | sub-paragraph | encoded | `o 19 r 17(4)(b) the appellant's Case` |  |
| O 19 r 17(4)(c) | 2390-2391 | sub-paragraph | encoded | `o 19 r 17(4)(c) the appellant's core bundle of documents` |  |
| O 19 r 17(4)(d) | 2392-2393 | sub-paragraph | encoded | `o 19 r 17(4)(d) the appellant's bundle of authorities` |  |
| O 19 r 17(5) | 2395 | paragraph | encoded | `o 19 r 17(5) the appeal is deemed withdrawn` |  |
| O 19 r 17(6) | 2396 | paragraph | encoded | `o 19 r 17(6) the security for costs must be paid and the solicitor's undertaking is discharged` |  |
| O 19 r 17(7)(a) | 2397-2398 | sub-paragraph | encoded | `o 19 r 17(7)(a) the appellant or a party may request in writing to the General Division for directions on those issues` (+1 more) |  |
| O 19 r 17(7) | 2397-2402 | paragraph | encoded | `o 19 r 17(7)(a) the appellant or a party may request in writing to the General Division for directions on those issues` (+3 more) |  |
| O 19 r 17(7)(b) | 2399-2400 | sub-paragraph | encoded | `o 19 r 17(7)(b) oral arguments may be made in the request` |  |
| O 19 r 17(7)(c) | 2401-2402 | sub-paragraph | encoded | `o 19 r 17(7)(c) the Registrar of the Supreme Court may give directions on the making of written submissions for the request` |  |
| O 19 r 17(8)(a) | 2403-2404 | sub-paragraph | encoded | `o 19 r 17(8)(a) the respondent's Case` |  |
| O 19 r 17(8) | 2403-2409 | paragraph | fork | `o 19 r 17(8) the period for the respondent's documents` (+7 more) | F9 |
| O 19 r 17(8)(b) | 2405-2406 | sub-paragraph | encoded | `o 19 r 17(8)(b) the respondent's core bundle of documents` |  |
| O 19 r 17(8)(c) | 2407-2408 | sub-paragraph | encoded | `o 19 r 17(8)(c) the respondent's bundle of authorities` |  |
| O 19 r 17(9) | 2410 | paragraph | encoded | `o 19 r 17(9) the respondent is barred from making submissions at the hearing of the appeal` (+3 more) |  |
| O 19 r 17(10)(a) | 2411-2412 | sub-paragraph | encoded | `o 19 r 17(10)(a) the appellant's Reply` |  |
| O 19 r 17(10) | 2411-2417 | paragraph | fork | `o 19 r 17(10) the appellant's reply document is filed and served in time` (+6 more) | F9 |
| O 19 r 17(10)(b) | 2413-2414 | sub-paragraph | encoded | `o 19 r 17(10)(b) the second core bundle` |  |
| O 19 r 17(10)(c) | 2415-2416 | sub-paragraph | encoded | `o 19 r 17(10)(c) the appellant's second bundle of authorities` |  |
| O 19 r 17(11) | 2418 | paragraph | encoded | `o 19 r 17(11) all the appellants may join in one appellants' Case and in one appellants' Reply` |  |
| O 19 r 17(12) | 2419 | paragraph | encoded | `o 19 r 17(12) all the respondents may join in one respondents' Case` |  |
| O 19 r 17(13) | 2420 | paragraph | encoded | `o 19 r 17(13) a party with a passive interest is required to file a separate Case` (+1 more) |  |
| O 19 r 17(14) | 2421 | paragraph | encoded | `o 19 r 17(14) the appellant and the respondent may seek directions from the General Division to file a joint Case` |  |
| O 19 r 17(15) | 2422 | paragraph | encoded | `o 19 r 17(15) the parties have tried to agree on a single Case for each party and on the timelines` |  |
| O 19 r 17(16) | 2423 | paragraph | encoded | `o 19 r 17(16) the parties have requested a case conference or sought directions` |  |
| O 19 r 17(17) | 2424 | paragraph | encoded | `o 19 r 17(17) the parties have informed the Registrar of the agreed timelines and sought approval` |  |
| O 19 r 17(18) | 2425 | paragraph | encoded | `o 19 r 17(18) the parties have filed a joint record of appeal` |  |
| O 19 r 17(19) | 2426 | paragraph | encoded | `o 19 r 17(19) a document other than those set out in this Rule may be filed` |  |
| O 19 r 17(20) | 2427 | paragraph | encoded | `o 19 r 17(20) written submissions or skeletal arguments may be filed before or at the appeal` |  |
| O 19 r 18 heading | 2428 | rule heading | inert (reason 1) | - | Appellant’s Case, respondent’s Case and appellant’s Reply (O. 19, r. 18) |
| O 19 r 18(1)(a) | 2429-2430 | sub-paragraph | encoded | `o 19 r 18(1)(a) a succinct summary of the facts, the decision of the lower Court, contentions to be made at the appeal and the orders sought from the General Division` |  |
| O 19 r 18(1) | 2429-2440 | paragraph | fork | `o 19 r 18(1) the appellant's Case contains what it must contain` (+7 more) | F-MUST |
| O 19 r 18(1)(b) | 2431-2432 | sub-paragraph | encoded | `o 19 r 18(1)(b) detailed submissions on the facts and the legal issues, including the relevant authorities, highlighting any new points not raised in the lower Court` |  |
| O 19 r 18(1)(c) | 2433-2434 | sub-paragraph | encoded | `o 19 r 18(1)(c) references in the right-hand margin to the relevant pages in the record of appeal and the appellant's core bundle of documents` |  |
| O 19 r 18(1)(d) | 2435-2436 | sub-paragraph | encoded | `o 19 r 18(1)(d) submissions on the appropriate costs orders to be made on appeal` |  |
| O 19 r 18(1)(e) | 2437-2438 | sub-paragraph | encoded | `o 19 r 18(1)(e) submissions on the amount of costs and disbursements that should be awarded in respect of all parties to the appeal` |  |
| O 19 r 18(1)(f) | 2439-2440 | sub-paragraph | encoded | `o 19 r 18(1)(f) the name and signature of the appellant's solicitor` |  |
| O 19 r 18(2)(a) | 2441-2442 | sub-paragraph | encoded | `o 19 r 18(2)(a) a succinct summary of the contentions to be made at the appeal and the orders sought from the General Division` |  |
| O 19 r 18(2) | 2441-2458 | paragraph | encoded | `o 19 r 18(2) the respondent's Case contains what it must contain` (+9 more) |  |
| O 19 r 18(2)(b) | 2443-2444 | sub-paragraph | encoded | `o 19 r 18(2)(b) detailed submissions on the facts and the legal issues, including the relevant authorities, highlighting any new points not raised in the lower Court` |  |
| O 19 r 18(2)(c) | 2445-2446 | sub-paragraph | encoded | `o 19 r 18(2)(c) references in the right-hand margin to the relevant pages in the record of appeal and the respondent's core bundle of documents (if any)` |  |
| O 19 r 18(2)(d) | 2447 | sub-paragraph | encoded | `o 19 r 18(2)(d) the Case states so and sets out the reasons for the respondent's submissions` (+1 more) |  |
| O 19 r 18(2)(d)(i) | 2448-2449 | item | encoded | in the rule for 18(2)(d): `o 19 r 18(2)(d) the Case states so and sets out the reasons for the respondent's submissions` (+1 more) |  |
| O 19 r 18(2)(d)(ii) | 2450-2451 | item | encoded | in the rule for 18(2)(d): `o 19 r 18(2)(d) the Case states so and sets out the reasons for the respondent's submissions` (+1 more) |  |
| O 19 r 18(2)(e) | 2453-2454 | sub-paragraph | encoded | `o 19 r 18(2)(e) submissions on the appropriate costs orders to be made on appeal` |  |
| O 19 r 18(2)(f) | 2455-2456 | sub-paragraph | encoded | `o 19 r 18(2)(f) submissions on the amount of costs and disbursements that should be awarded in respect of all parties to the appeal` |  |
| O 19 r 18(2)(g) | 2457-2458 | sub-paragraph | encoded | `o 19 r 18(2)(g) the name and signature of the respondent's solicitor` |  |
| O 19 r 18(3) | 2459 | paragraph | encoded | `o 19 r 18(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` (+2 more) |  |
| O 19 r 18(4)(a) | 2460-2461 | sub-paragraph | encoded | `o 19 r 18(4)(a) the appellant's detailed submissions in reply to the respondent's submissions` |  |
| O 19 r 18(4) | 2460-2465 | paragraph | encoded | `o 19 r 18(4) the appellant's Reply contains what it must contain` (+4 more) |  |
| O 19 r 18(4)(b) | 2462-2463 | sub-paragraph | encoded | `o 19 r 18(4)(b) references in the right-hand margin to the relevant pages in the record of appeal and the core bundles` |  |
| O 19 r 18(4)(c) | 2464-2465 | sub-paragraph | encoded | `o 19 r 18(4)(c) the name and signature of the appellant's solicitor` |  |
| O 19 r 18(5) | 2466 | paragraph | encoded | `o 19 r 18(5) the Case or Reply contains everything the party intends to put forward` |  |
| O 19 r 19 heading | 2467 | rule heading | inert (reason 1) | - | Page limits (O. 19, r. 19) |
| O 19 r 19(1)(a) | 2468-2469 | sub-paragraph | encoded | `o 19 r 19(1)(a) the appellant's Case` |  |
| O 19 r 19(1) | 2468-2473 | paragraph | encoded | `o 19 r 19(1) the document is within the page limit` (+5 more) |  |
| O 19 r 19(1)(b) | 2470-2471 | sub-paragraph | encoded | `o 19 r 19(1)(b) the respondent's Case` |  |
| O 19 r 19(1)(c) | 2472-2473 | sub-paragraph | encoded | `o 19 r 19(1)(c) the appellant's Reply` |  |
| O 19 r 19(2)(a) | 2474-2475 | sub-paragraph | encoded | `o 19 r 19(2)(a) the appellant's core bundle of documents (excluding the written judgment or grounds of decision of the lower Court and the extracted order of the lower Court)` |  |
| O 19 r 19(2) | 2474-2479 | paragraph | encoded | `o 19 r 19(2) the document is within the page limit` (+5 more) | silent: rule 19 sets no page limit on a bundle of authorities in Division 2; no function |
| O 19 r 19(2)(b) | 2476-2477 | sub-paragraph | encoded | `o 19 r 19(2)(b) the respondent's core bundle of documents` |  |
| O 19 r 19(2)(c) | 2478-2479 | sub-paragraph | encoded | `o 19 r 19(2)(c) the second core bundle` |  |
| O 19 r 19(3)(a) | 2480-2481 | sub-paragraph | fork | `o 19 r 19(3)(a) the General Division may allow the page limit to be exceeded` | F8 |
| O 19 r 19(3) | 2480-2483 | paragraph | fork | `o 19 r 19(3)(a) the General Division may allow the page limit to be exceeded` (+2 more) | F8 |
| O 19 r 19(3)(b) | 2482-2483 | sub-paragraph | encoded | `o 19 r 19(3)(b) the amount payable for the pages in excess` (+1 more) |  |
| O 19 r 19(4) | 2484 | paragraph | encoded | `o 19 r 19(4) the General Division may waive, refund, defer or apportion the payment of the fees` |  |
| O 19 r 20 heading | 2485 | rule heading | inert (reason 1) | - | Payment out of security for costs and release of undertaking (O. 19, r. 20) |
| O 19 r 20(1) | 2486 | paragraph | encoded | `o 19 r 20(1) an order from the Court is needed for this Rule to apply` |  |
| O 19 r 20(2) | 2486 | paragraph | encoded | `o 19 r 20(2) the amount of the security paid to the respondent` (+2 more) |  |
| O 19 r 20(3) | 2487 | paragraph | encoded | `o 19 r 20(3) the security for costs must be paid to the appellant and the appellant's solicitor is released from any undertaking` |  |
| O 19 r 21 heading | 2488 | rule heading | inert (reason 1) | - | Further arguments (O. 19, r. 21) |
| O 19 r 21 | 2489 | paragraph | fork | `o 19 r 21 further arguments from the parties are allowed` | F13 |
| O 19 r 22 heading | 2490 | rule heading | inert (reason 1) | - | Registrar of State Courts to be notified of General Division’s judgment or order (O. 19, r. 22) |
| O 19 r 22 | 2491 | paragraph | encoded | `o 19 r 22 the appellant has notified the Registrar of the State Courts of the General Division's judgment or order` (+2 more) |  |
| O 19 r 23 heading | 2492 | rule heading | inert (reason 1) | - | Enforcement of judgments which have been subject matter of appeal (O. 19, r. 23) |
| O 19 r 23 | 2493 | paragraph | encoded | `o 19 r 23 the step for enforcement is taken in the right court` |  |
| O 19 Division 3 heading | 2494 | Division heading | inert (reason 1) | - | Appeals from General Division to Appellate Division or Court of Appeal, etc. |
| O 19 r 24 heading | 2495 | rule heading | inert (reason 1) | - | Scope of this Division (O. 19, r. 24) |
| O 19 r 24(a) | 2496-2497 | sub-paragraph | encoded | `o 19 r 24(a) this Division applies to an appeal to the Appellate Division against a judgment of the General Division` |  |
| O 19 r 24 | 2496-2505 | paragraph | encoded | `o 19 r 24 this Division applies` (+6 more) | hand-gathered: `o 19 r 24 this Division applies` (E1, option B) |
| O 19 r 24(b) | 2498-2499 | sub-paragraph | encoded | `o 19 r 24(b) this Division applies to an appeal to the Court of Appeal against a judgment of the General Division` |  |
| O 19 r 24(c) | 2500-2501 | sub-paragraph | encoded | `o 19 r 24(c) this Division applies to an appeal to the Court of Appeal against a judgment of the Appellate Division` |  |
| O 19 r 24(d) | 2502-2503 | sub-paragraph | encoded | `o 19 r 24(d) this Division applies to an application to the Appellate Division or the Court of Appeal relating to an appeal` |  |
| O 19 r 24(e) | 2504-2505 | sub-paragraph | encoded | `o 19 r 24(e) this Division applies to an appeal from a tribunal to the Appellate Division or the Court of Appeal` (+1 more) |  |
| O 19 r 25 heading | 2506 | rule heading | inert (reason 1) | - | Bringing of appeal (O. 19, r. 25) |
| O 19 r 25(1)(a) | 2507-2508 | sub-paragraph | encoded | `o 19 r 25(1)(a) the period for the notice of appeal` |  |
| O 19 r 25(1) | 2507-2510 | paragraph | fork | `o 19 r 25(1) the appellant must file and serve the notice of appeal within 28 days` (+5 more) | F12 |
| O 19 r 25(1)(b) | 2509-2510 | sub-paragraph | encoded | `o 19 r 25(1)(b) the period for the notice of appeal after a request for further arguments` |  |
| O 19 r 25(2) | 2511 | paragraph | encoded | `o 19 r 25(2) the appellate Court may extend the time for filing and serving the notice of appeal` (+1 more) |  |
| O 19 r 26 heading | 2512 | rule heading | inert (reason 1) | - | Permission to appeal (O. 19, r. 26) |
| O 19 r 26(1) | 2513 | paragraph | fork | `o 19 r 26(1) the application for permission is filed and served as required` (+3 more) | F12 |
| O 19 r 26(2)(a) | 2513-2514 | sub-paragraph | fork | in the rule for 26(2): `o 19 r 26(2) the Judge who made the decision may hear further arguments` (+4 more) | F5 |
| O 19 r 26(2) | 2513-2518 | paragraph | fork | `o 19 r 26(2) the Judge who made the decision may hear further arguments` (+4 more) | F5 |
| O 19 r 26(2)(b) | 2515-2516 | sub-paragraph | fork | `o 19 r 26(2)(b) the start of the 15th day after the date the decision is made` | F5 |
| O 19 r 26(2)(c) | 2517-2518 | sub-paragraph | fork | in the rule for 26(2): `o 19 r 26(2) the Judge who made the decision may hear further arguments` (+4 more) | F5 |
| O 19 r 26(3)(a) | 2519 | sub-paragraph | fork | `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` (+1 more) | F13 |
| O 19 r 26(3) | 2519-2528 | paragraph | encoded | `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` (+4 more) |  |
| O 19 r 26(3)(a)(i) | 2520-2521 | item | encoded | in the rule for 26(3)(a): `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` (+1 more) |  |
| O 19 r 26(3)(a)(ii) | 2522-2523 | item | encoded | in the rule for 26(3)(a): `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` (+1 more) |  |
| O 19 r 26(3)(b) | 2524 | sub-paragraph | encoded | `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` (+2 more) |  |
| O 19 r 26(3)(b)(i) | 2525-2526 | item | encoded | in the rule for 26(3)(b): `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` (+2 more) |  |
| O 19 r 26(3)(b)(ii) | 2527-2528 | item | encoded | in the rule for 26(3)(b): `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` (+2 more) |  |
| O 19 r 26(4) | 2529 | paragraph | encoded | `o 19 r 26(4) paragraphs (2) and (3) affect section 29B of the Supreme Court of Judicature Act` |  |
| O 19 r 26(5)(a) | 2530-2531 | sub-paragraph | encoded | in the rule for 26(5): `o 19 r 26(5) the Court of Appeal may grant permission to appeal against a decision of the Appellate Division` (+5 more) |  |
| O 19 r 26(5) | 2530-2536 | paragraph | encoded | `o 19 r 26(5) the Court of Appeal may grant permission to appeal against a decision of the Appellate Division` (+5 more) |  |
| O 19 r 26(5)(b) | 2532-2533 | sub-paragraph | encoded | `o 19 r 26(5)(b) the Court of Appeal may have regard to the matter` (+4 more) |  |
| O 19 r 26(6)(a) | 2537-2538 | sub-paragraph | encoded | in the rule for 26(6): `o 19 r 26(6) the party may apply to the relevant appellate Court for permission to appeal` (+1 more) |  |
| O 19 r 26(6) | 2537-2541 | paragraph | encoded | `o 19 r 26(6) the party may apply to the relevant appellate Court for permission to appeal` (+1 more) |  |
| O 19 r 26(6)(b) | 2539-2540 | sub-paragraph | encoded | in the rule for 26(6): `o 19 r 26(6) the party may apply to the relevant appellate Court for permission to appeal` (+1 more) |  |
| O 19 r 26(7)(a) | 2542-2543 | sub-paragraph | fork | `o 19 r 26(7)(a) the documents mentioned in paragraph (7) are filed with the application` | F-MUST |
| O 19 r 26(7) | 2542-2545 | paragraph | encoded | `o 19 r 26(7) the documents mentioned are filed and served with the application` (+2 more) | hand-gathered: `o 19 r 26(7) the documents mentioned are filed and served with the application` (E1, option B) |
| O 19 r 26(7)(b) | 2544-2545 | sub-paragraph | encoded | `o 19 r 26(7)(b) the applicant may file a bundle of documents with the application` |  |
| O 19 r 26(8)(a) | 2546-2547 | sub-paragraph | encoded | in the rule for 26(8): `o 19 r 26(8) the opposing party's submissions are filed and served as required` (+5 more) |  |
| O 19 r 26(8) | 2546-2550 | paragraph | encoded | `o 19 r 26(8) the opposing party's submissions are filed and served as required` (+5 more) |  |
| O 19 r 26(8)(b) | 2548-2549 | sub-paragraph | encoded | `o 19 r 26(8)(b) the opposing party may file and serve a bundle of documents with its submissions` |  |
| O 19 r 26(9) | 2551 | paragraph | encoded | `o 19 r 26(9) the application and the accompanying documents are served on all parties who have an interest in the appeal` |  |
| O 19 r 26(10) | 2552 | paragraph | encoded | `o 19 r 26(10) the written submissions are within the page limit and in the form specified` |  |
| O 19 r 26(11) | 2553 | paragraph | fork | `o 19 r 26(11) the bundle of documents is within the page limit` | F8 |
| O 19 r 26(12)(a) | 2554-2555 | sub-paragraph | fork | `o 19 r 26(12)(a) the appellate Court may allow the page limit for the written submissions to be exceeded` | F8 |
| O 19 r 26(12) | 2554-2557 | paragraph | fork | `o 19 r 26(12)(a) the appellate Court may allow the page limit for the written submissions to be exceeded` (+2 more) | F8 |
| O 19 r 26(12)(b) | 2556-2557 | sub-paragraph | encoded | `o 19 r 26(12)(b) the amount payable for the pages in excess` (+1 more) |  |
| O 19 r 26(13) | 2558 | paragraph | encoded | `o 19 r 26(13) the appellate Court may waive, refund, defer or apportion the payment of the fees` |  |
| O 19 r 26(14) | 2559 | paragraph | encoded | `o 19 r 26(14) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` |  |
| O 19 r 26(15) | 2560 | paragraph | encoded | `o 19 r 26(15) an affidavit may be filed in an application for permission to appeal` |  |
| O 19 r 26(16) | 2561 | paragraph | encoded | `o 19 r 26(16) oral arguments may be made in an application for permission to appeal` |  |
| O 19 r 26(17) | 2562 | paragraph | encoded | `o 19 r 26(17) the applicant must file and serve the notice of appeal within 14 days after permission is granted` (+3 more) |  |
| O 19 r 26(18) | 2563 | paragraph | encoded | `o 19 r 26(18) the appellate Court may extend the time for filing and serving an application for permission to appeal` |  |
| O 19 r 27 heading | 2564 | rule heading | inert (reason 1) | - | Security for costs (O. 19, r. 27) |
| O 19 r 27(1) | 2565 | paragraph | encoded | `o 19 r 27(1) the appellant has provided security for costs and filed the certificate as required` |  |
| O 19 r 27(2) | 2565 | paragraph | encoded | `o 19 r 27(2) the appellants need to provide only one set of security for the appeal` |  |
| O 19 r 27(3) | 2566 | paragraph | encoded | `o 19 r 27(3) the appellant must provide security for each respondent or each set of respondents` (+1 more) |  |
| O 19 r 27(4)(a) | 2567-2568 | sub-paragraph | encoded | `o 19 r 27(4)(a) a solicitor's undertaking in Form 37` |  |
| O 19 r 27(4) | 2567-2572 | paragraph | encoded | `o 19 r 27(4) the security is in a form the text allows` (+4 more) |  |
| O 19 r 27(4)(b) | 2569-2570 | sub-paragraph | encoded | `o 19 r 27(4)(b) a deposit in the Registry or with the Accountant-General` |  |
| O 19 r 27(4)(c) | 2571-2572 | sub-paragraph | encoded | `o 19 r 27(4)(c) any other form` |  |
| O 19 r 27(5) | 2573 | paragraph | encoded | `o 19 r 27(5) the amount of security` (+1 more) |  |
| O 19 r 27(6) | 2574 | paragraph | encoded | `o 19 r 27(6) a party may apply to the appellate Court to vary or waive the amount of security` |  |
| O 19 r 27(7) | 2575 | paragraph | encoded | `o 19 r 27(7) the appellate Court may order further security for costs to be given` |  |
| O 19 r 28 heading | 2576 | rule heading | inert (reason 1) | - | Related appeals (O. 19, r. 28) |
| O 19 r 28(1) | 2577 | paragraph | encoded | `o 19 r 28(1) the appellate Court may give directions for the filing and service of joint documents` |  |
| O 19 r 28(2) | 2577 | paragraph | encoded | `o 19 r 28(2) the directions in paragraph (1) may be given in this way` |  |
| O 19 r 28(3) | 2578 | paragraph | encoded | `o 19 r 28(3) the appellate Court may give directions under paragraph (1) even if the related appeals are of both kinds` |  |
| O 19 r 28(4) | 2579 | paragraph | encoded | `o 19 r 28(4) the appellate Court may direct modifications of the rules, including that this Division does not apply and Division 5 of Order 18 applies instead` |  |
| O 19 r 29 heading | 2580 | rule heading | inert (reason 1) | - | Appellate Court may specify rules that apply to appeals (O. 19, r. 29) |
| O 19 r 29(1)(a) | 2581-2582 | sub-paragraph | encoded | in the rule for 29(1): `o 19 r 29(1) the appellate Court may order that this Division, or any part of it, does not apply to an appeal before it, and that Division 5 of Order 18, or any part of it, applies instead` |  |
| O 19 r 29(1) | 2581-2584 | paragraph | encoded | `o 19 r 29(1) the appellate Court may order that this Division, or any part of it, does not apply to an appeal before it, and that Division 5 of Order 18, or any part of it, applies instead` |  |
| O 19 r 29(1)(b) | 2583-2584 | sub-paragraph | encoded | in the rule for 29(1): `o 19 r 29(1) the appellate Court may order that this Division, or any part of it, does not apply to an appeal before it, and that Division 5 of Order 18, or any part of it, applies instead` |  |
| O 19 r 29(2) | 2585 | paragraph | encoded | `o 19 r 29(2) the appellate Court may order or direct modifications of the rules applicable to an appeal before it` |  |
| O 19 r 29(3) | 2586 | paragraph | encoded | `o 19 r 29(3) the appellate Court may make an order or give a direction under this Rule` |  |
| O 19 r 30 heading | 2587 | rule heading | inert (reason 1) | - | Documents to be filed (O. 19, r. 30) |
| O 19 r 30(1) | 2588 | paragraph | encoded | `o 19 r 30(1) the lower Court must issue its written grounds of decision` |  |
| O 19 r 30(2) | 2588 | paragraph | encoded | `o 19 r 30(2) the Registry must notify the parties that the record of proceedings is ready for collection` |  |
| O 19 r 30(3)(a) | 2589-2590 | sub-paragraph | encoded | `o 19 r 30(3)(a) the appellant must apply in writing to the Registrar to proceed with the appeal and for a copy of the record of proceedings` |  |
| O 19 r 30(3) | 2589-2594 | paragraph | encoded | `o 19 r 30(3) no written grounds of decision are issued within 12 weeks` (+5 more) |  |
| O 19 r 30(3)(b) | 2591-2592 | sub-paragraph | encoded | `o 19 r 30(3)(b) the period of notice to strike out` (+1 more) |  |
| O 19 r 30(3)(c) | 2593-2594 | sub-paragraph | encoded | `o 19 r 30(3)(c) the respondent may apply to strike out the appeal` |  |
| O 19 r 30(4)(a) | 2595-2596 | sub-paragraph | encoded | `o 19 r 30(4)(a) the record of appeal` |  |
| O 19 r 30(4) | 2595-2603 | paragraph | encoded | `o 19 r 30(4) the appellant must file and serve the appellant's documents within 8 weeks and the respondent and the appellant must follow` (+8 more) |  |
| O 19 r 30(4)(b) | 2597-2598 | sub-paragraph | encoded | `o 19 r 30(4)(b) the appellant's Case` |  |
| O 19 r 30(4)(c) | 2599-2600 | sub-paragraph | encoded | `o 19 r 30(4)(c) the appellant's core bundle of documents` |  |
| O 19 r 30(4)(d) | 2601-2602 | sub-paragraph | encoded | `o 19 r 30(4)(d) the appellant's bundle of authorities` |  |
| O 19 r 30(5)(a) | 2604 | sub-paragraph | fork | `o 19 r 30(5)(a) the supplemental record of appeal comprises what it must` (+9 more) | F-MUST |
| O 19 r 30(5) | 2604-2625 | paragraph | encoded | `o 19 r 30(5) the appellant's document on an appeal from the Appellate Division is filed and served in time` (+16 more) |  |
| O 19 r 30(5)(a)(i) | 2605-2606 | item | encoded | `o 19 r 30(5)(a)(i) the notice of appeal to the Court of Appeal` |  |
| O 19 r 30(5)(a)(ii) | 2607-2608 | item | encoded | `o 19 r 30(5)(a)(ii) the certificate of payment for security for costs` |  |
| O 19 r 30(5)(a)(iii) | 2609-2610 | item | encoded | `o 19 r 30(5)(a)(iii) the written judgment or grounds of decision of the Appellate Division or, if there is none, the certified minute sheet of the Appellate Division` |  |
| O 19 r 30(5)(a)(iv) | 2611-2612 | item | encoded | `o 19 r 30(5)(a)(iv) the extracted order of the Appellate Division` |  |
| O 19 r 30(5)(a)(v) | 2613-2614 | item | encoded | `o 19 r 30(5)(a)(v) the order granting permission to appeal to the Court of Appeal` |  |
| O 19 r 30(5)(a)(vi) | 2615-2616 | item | encoded | `o 19 r 30(5)(a)(vi) the parties' Cases filed in the Appellate Division` |  |
| O 19 r 30(5)(a)(vii) | 2617-2618 | item | encoded | `o 19 r 30(5)(a)(vii) all documents filed in the Appellate Division, so far as they are relevant to the matter decided and the nature of the appeal` |  |
| O 19 r 30(5)(b) | 2619-2620 | sub-paragraph | encoded | `o 19 r 30(5)(b) the appellant's Case` |  |
| O 19 r 30(5)(c) | 2621-2622 | sub-paragraph | encoded | `o 19 r 30(5)(c) the appellant's core bundle of documents` |  |
| O 19 r 30(5)(d) | 2623-2624 | sub-paragraph | encoded | `o 19 r 30(5)(d) the appellant's bundle of authorities` |  |
| O 19 r 30(6) | 2626 | paragraph | encoded | `o 19 r 30(6) the appeal is deemed withdrawn` |  |
| O 19 r 30(7) | 2627 | paragraph | encoded | `o 19 r 30(7) the security for costs must be paid and the solicitor's undertaking is discharged` |  |
| O 19 r 30(8)(a) | 2628-2629 | sub-paragraph | encoded | `o 19 r 30(8)(a) the appellant or a party may request in writing to the appellate Court for directions on those issues` (+1 more) |  |
| O 19 r 30(8) | 2628-2633 | paragraph | encoded | `o 19 r 30(8)(a) the appellant or a party may request in writing to the appellate Court for directions on those issues` (+3 more) |  |
| O 19 r 30(8)(b) | 2630-2631 | sub-paragraph | encoded | `o 19 r 30(8)(b) oral arguments may be made in the request` |  |
| O 19 r 30(8)(c) | 2632-2633 | sub-paragraph | encoded | `o 19 r 30(8)(c) the Registrar of the Supreme Court may give directions on the making of written submissions for the request` |  |
| O 19 r 30(9)(a) | 2634-2635 | sub-paragraph | encoded | `o 19 r 30(9)(a) the respondent's Case` |  |
| O 19 r 30(9) | 2634-2640 | paragraph | fork | `o 19 r 30(9) the period for the respondent's documents` (+6 more) | F9 |
| O 19 r 30(9)(b) | 2636-2637 | sub-paragraph | encoded | `o 19 r 30(9)(b) the respondent's core bundle of documents` |  |
| O 19 r 30(9)(c) | 2638-2639 | sub-paragraph | encoded | `o 19 r 30(9)(c) the respondent's bundle of authorities` |  |
| O 19 r 30(10) | 2641 | paragraph | encoded | `o 19 r 30(10) the respondent is barred from making submissions at the hearing of the appeal` (+1 more) |  |
| O 19 r 30(11)(a) | 2642-2643 | sub-paragraph | encoded | `o 19 r 30(11)(a) the appellant's Reply` |  |
| O 19 r 30(11) | 2642-2648 | paragraph | fork | `o 19 r 30(11) the appellant's reply document is filed and served in time` (+6 more) | F9 |
| O 19 r 30(11)(b) | 2644-2645 | sub-paragraph | encoded | `o 19 r 30(11)(b) the second core bundle` |  |
| O 19 r 30(11)(c) | 2646-2647 | sub-paragraph | encoded | `o 19 r 30(11)(c) the appellant's second bundle of authorities` |  |
| O 19 r 30(12) | 2649 | paragraph | encoded | `o 19 r 30(12) all the appellants may join in one appellants' Case and in one appellants' Reply` |  |
| O 19 r 30(13) | 2650 | paragraph | encoded | `o 19 r 30(13) all the respondents may join in one respondents' Case` |  |
| O 19 r 30(14) | 2651 | paragraph | encoded | `o 19 r 30(14) a party with a passive interest is required to file a separate Case` (+1 more) |  |
| O 19 r 30(15) | 2652 | paragraph | encoded | `o 19 r 30(15) the appellant and the respondent may seek directions from the appellate Court to file a joint Case` |  |
| O 19 r 30(16) | 2653 | paragraph | encoded | `o 19 r 30(16) the parties have tried to agree on a single Case for each party and on the timelines` |  |
| O 19 r 30(17) | 2654 | paragraph | encoded | `o 19 r 30(17) the parties have requested a case conference or sought directions` |  |
| O 19 r 30(18) | 2655 | paragraph | encoded | `o 19 r 30(18) the parties have informed the Registrar of the agreed timelines and sought approval` |  |
| O 19 r 30(19) | 2656 | paragraph | encoded | `o 19 r 30(19) the parties have filed a joint record of appeal` |  |
| O 19 r 30(20) | 2657 | paragraph | encoded | `o 19 r 30(20) a document other than those set out in this Rule may be filed` |  |
| O 19 r 30(21) | 2658 | paragraph | encoded | `o 19 r 30(21) written submissions or skeletal arguments may be filed before or at the appeal` |  |
| O 19 r 31 heading | 2659 | rule heading | inert (reason 1) | - | Appellant’s Case, respondent’s Case and appellant’s Reply (O. 19, r. 31) |
| O 19 r 31(1)(a) | 2660-2661 | sub-paragraph | encoded | `o 19 r 31(1)(a) a succinct summary of the facts, the decision of the lower Court, contentions to be made at the appeal and the orders sought from the appellate Court` |  |
| O 19 r 31(1) | 2660-2672 | paragraph | encoded | `o 19 r 31(1) the appellant's Case contains what it must contain` (+7 more) |  |
| O 19 r 31(1)(b) | 2662-2663 | sub-paragraph | encoded | `o 19 r 31(1)(b) detailed submissions on the facts and the legal issues, including the relevant authorities, highlighting any new points not raised in the lower Court` |  |
| O 19 r 31(1)(c) | 2664-2665 | sub-paragraph | encoded | `o 19 r 31(1)(c) references in the right-hand margin to the relevant pages in the record of appeal, the supplemental record of appeal (where required under Rule 30(5)(a)) and the appellant's core bundle of documents` |  |
| O 19 r 31(1)(d) | 2666 | sub-paragraph | encoded | `o 19 r 31(1)(d)(i) in the concluding paragraphs, submissions on the appropriate costs orders to be made on appeal` (+1 more) |  |
| O 19 r 31(1)(d)(i) | 2667-2668 | item | encoded | `o 19 r 31(1)(d)(i) in the concluding paragraphs, submissions on the appropriate costs orders to be made on appeal` |  |
| O 19 r 31(1)(d)(ii) | 2669-2670 | item | encoded | `o 19 r 31(1)(d)(ii) in the concluding paragraphs, submissions on the amount of costs and disbursements that should be awarded in respect of all parties to the appeal` |  |
| O 19 r 31(1)(e) | 2671-2672 | sub-paragraph | encoded | `o 19 r 31(1)(e) the name and signature of the appellant's solicitor` |  |
| O 19 r 31(2)(a) | 2673-2674 | sub-paragraph | encoded | `o 19 r 31(2)(a) a succinct summary of the contentions to be made at the appeal and the orders sought from the appellate Court` |  |
| O 19 r 31(2) | 2673-2691 | paragraph | encoded | `o 19 r 31(2) the respondent's Case contains what it must contain` (+9 more) |  |
| O 19 r 31(2)(b) | 2675-2676 | sub-paragraph | encoded | `o 19 r 31(2)(b) detailed submissions on the facts and the legal issues, including the relevant authorities, highlighting any new points not raised in the lower Court` |  |
| O 19 r 31(2)(c) | 2677-2678 | sub-paragraph | encoded | `o 19 r 31(2)(c) references in the right-hand margin to the relevant pages in the record of appeal, the supplemental record of appeal (where required under Rule 30(5)(a)) and the respondent's core bundle of documents (if any)` |  |
| O 19 r 31(2)(d) | 2679 | sub-paragraph | encoded | `o 19 r 31(2)(d) the Case sets out those submissions and the reasons for them` (+1 more) |  |
| O 19 r 31(2)(d)(i) | 2680-2681 | item | encoded | in the rule for 31(2)(d): `o 19 r 31(2)(d) the Case sets out those submissions and the reasons for them` (+1 more) |  |
| O 19 r 31(2)(d)(ii) | 2682-2683 | item | encoded | in the rule for 31(2)(d): `o 19 r 31(2)(d) the Case sets out those submissions and the reasons for them` (+1 more) |  |
| O 19 r 31(2)(e) | 2685 | sub-paragraph | encoded | `o 19 r 31(2)(e)(i) in the concluding paragraphs, submissions on the appropriate costs orders to be made on appeal` (+1 more) |  |
| O 19 r 31(2)(e)(i) | 2686-2687 | item | encoded | `o 19 r 31(2)(e)(i) in the concluding paragraphs, submissions on the appropriate costs orders to be made on appeal` |  |
| O 19 r 31(2)(e)(ii) | 2688-2689 | item | encoded | `o 19 r 31(2)(e)(ii) in the concluding paragraphs, submissions on the amount of costs and disbursements that should be awarded in respect of all parties to the appeal` |  |
| O 19 r 31(2)(f) | 2690-2691 | sub-paragraph | encoded | `o 19 r 31(2)(f) the name and signature of the respondent's solicitor` |  |
| O 19 r 31(3) | 2692 | paragraph | encoded | `o 19 r 31(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` (+1 more) |  |
| O 19 r 31(4)(a) | 2693-2694 | sub-paragraph | encoded | `o 19 r 31(4)(a) the appellant's detailed submissions in reply to the respondent's submissions` |  |
| O 19 r 31(4) | 2693-2698 | paragraph | encoded | `o 19 r 31(4) the appellant's Reply contains what it must contain` (+4 more) |  |
| O 19 r 31(4)(b) | 2695-2696 | sub-paragraph | encoded | `o 19 r 31(4)(b) references in the right-hand margin to the relevant pages in the record of appeal, the supplemental record of appeal (where required under Rule 30(5)(a)), the appellant's core bundle of documents, the respondent's core bundle of documents (if any), and the second core bundle (if any)` |  |
| O 19 r 31(4)(c) | 2697-2698 | sub-paragraph | encoded | `o 19 r 31(4)(c) the name and signature of the appellant's solicitor` |  |
| O 19 r 31(5) | 2699 | paragraph | encoded | `o 19 r 31(5) the Case or Reply contains everything the party intends to put forward` |  |
| O 19 r 32 heading | 2700 | rule heading | inert (reason 1) | - | Page limits (O. 19, r. 32) |
| O 19 r 32(1)(a) | 2701-2702 | sub-paragraph | encoded | `o 19 r 32(1)(a) the appellant's Case` |  |
| O 19 r 32(1) | 2701-2706 | paragraph | encoded | `o 19 r 32(1) the document is within the page limit` (+5 more) |  |
| O 19 r 32(1)(b) | 2703-2704 | sub-paragraph | encoded | `o 19 r 32(1)(b) the respondent's Case` |  |
| O 19 r 32(1)(c) | 2705-2706 | sub-paragraph | encoded | `o 19 r 32(1)(c) the appellant's Reply` |  |
| O 19 r 32(2)(a) | 2707-2708 | sub-paragraph | encoded | `o 19 r 32(2)(a) the appellant's core bundle of documents (excluding the written judgment or grounds of decision of the lower Court and the extracted order of the lower Court)` |  |
| O 19 r 32(2) | 2707-2712 | paragraph | encoded | `o 19 r 32(2) the document is within the page limit` (+5 more) |  |
| O 19 r 32(2)(b) | 2709-2710 | sub-paragraph | encoded | `o 19 r 32(2)(b) the respondent's core bundle of documents` |  |
| O 19 r 32(2)(c) | 2711-2712 | sub-paragraph | encoded | `o 19 r 32(2)(c) the second core bundle` |  |
| O 19 r 32(3)(a) | 2713-2714 | sub-paragraph | fork | `o 19 r 32(3)(a) the appellate Court may allow the page limit to be exceeded` | F8 |
| O 19 r 32(3) | 2713-2716 | paragraph | fork | `o 19 r 32(3)(a) the appellate Court may allow the page limit to be exceeded` (+2 more) | F8 |
| O 19 r 32(3)(b) | 2715-2716 | sub-paragraph | encoded | `o 19 r 32(3)(b) the amount payable for the pages in excess` (+1 more) |  |
| O 19 r 32(4) | 2717 | paragraph | encoded | `o 19 r 32(4) the appellate Court may waive, refund, defer or apportion the payment of the fees` |  |
| O 19 r 33 heading | 2718 | rule heading | inert (reason 1) | - | Payment out of security for costs and release of undertaking (O. 19, r. 33) |
| O 19 r 33(1) | 2719 | paragraph | encoded | `o 19 r 33(1) an order from the Court is needed for this Rule to apply` |  |
| O 19 r 33(2) | 2719 | paragraph | encoded | `o 19 r 33(2) the amount of the security paid to the respondent` (+2 more) |  |
| O 19 r 33(3) | 2720 | paragraph | encoded | `o 19 r 33(3) the security for costs must be paid to the appellant and the appellant's solicitor is released from any undertaking` |  |
| O 19 r 33(4) | 2721 | paragraph | encoded | `o 19 r 33(4) paragraphs (2) and (3) apply, with necessary modifications, to the payment out of the security` |  |
| O 19 r 34 heading | 2722 | rule heading | inert (reason 1) | - | Further arguments (O. 19, r. 34) |
| O 19 r 34 | 2723 | paragraph | fork | `o 19 r 34 further arguments from the parties are allowed` | F13 |
| O 19 r 35 heading | 2724 | rule heading | inert (reason 1) | - | Applications to appellate Court (O. 19, r. 35) |
| O 19 r 35(1) | 2725 | paragraph | encoded | `o 19 r 35(1) the application to the appellate Court is made in a way the text allows` (+3 more) |  |
| O 19 r 35(2) | 2725 | paragraph | fork | `o 19 r 35(2) the application may be made in the first instance to the appellate Court` | F11 |
| O 19 r 35(3) | 2726 | paragraph | encoded | `o 19 r 35(3) oral arguments may be made in an application to the appellate Court` |  |
| O 19 r 35(4) | 2727 | paragraph | encoded | `o 19 r 35(4) a further affidavit may be filed` (+2 more) |  |
| O 19 r 35(5) | 2728 | paragraph | encoded | `o 19 r 35(5) a Case needs to be filed for the application` |  |
| O 19 r 35(6) | 2729 | paragraph | encoded | `o 19 r 35(6) the party has provided security for costs and filed the certificate as required` |  |
| O 19 r 35(7) | 2730 | paragraph | encoded | `o 19 r 35(7) the applicants need to provide only one set of security for the costs of the application` |  |
| O 19 r 35(8) | 2731 | paragraph | encoded | `o 19 r 35(8) the applicant must provide security for each opposing party or each set of opposing parties` (+1 more) |  |
| O 19 r 35(9)(a) | 2732-2733 | sub-paragraph | encoded | `o 19 r 35(9)(a) a solicitor's undertaking in Form 37` |  |
| O 19 r 35(9) | 2732-2737 | paragraph | encoded | `o 19 r 35(9) the security is in a form the text allows` (+4 more) |  |
| O 19 r 35(9)(b) | 2734-2735 | sub-paragraph | encoded | `o 19 r 35(9)(b) a deposit in the Registry or with the Accountant-General` |  |
| O 19 r 35(9)(c) | 2736-2737 | sub-paragraph | encoded | `o 19 r 35(9)(c) any other form` |  |
| O 19 r 35(10) | 2738 | paragraph | encoded | `o 19 r 35(10) the amount of security` (+1 more) |  |
| O 19 r 35(11) | 2739 | paragraph | encoded | `o 19 r 35(11) a party may apply to the appellate Court to vary or waive the amount of security` |  |
| O 19 r 35(12) | 2740 | paragraph | encoded | `o 19 r 35(12) the appellate Court may order further security for costs to be given` |  |
| O 19 r 35(13) | 2741 | paragraph | encoded | `o 19 r 35(13) the application to strike out a notice of appeal is made by summons supported by affidavit` |  |
| O 19 r 35(14) | 2742 | paragraph | encoded | `o 19 r 35(14) the applicant must file and serve the summons and the supporting affidavit within 14 days` (+4 more) |  |
| O 19 r 35(15) | 2743 | paragraph | encoded | `o 19 r 35(15) the affidavit in reply to the applicant's affidavit is filed and served as required` (+1 more) |  |
| O 19 r 35(16) | 2744 | paragraph | encoded | `o 19 r 35(16) a further affidavit may be received in evidence` |  |
| O 19 r 36 heading | 2745 | rule heading | inert (reason 1) | - | Application for permission under section 40(4)( b ) or 58(4)( b ) of Supreme Court of Judicature Act (O. 19, r. 36) |
| O 19 r 36(a) | 2746-2747 | sub-paragraph | encoded | in the rule for 36: `o 19 r 36 the applicant must file and serve the application for permission within 14 days` (+4 more) |  |
| O 19 r 36 | 2746-2750 | paragraph | encoded | `o 19 r 36 the applicant must file and serve the application for permission within 14 days` (+4 more) |  |
| O 19 r 36(b) | 2748-2749 | sub-paragraph | encoded | in the rule for 36: `o 19 r 36 the applicant must file and serve the application for permission within 14 days` (+4 more) |  |
| O 19 r 37 heading | 2751 | rule heading | inert (reason 1) | - | Written submissions for applications to appellate Court (O. 19, r. 37) |
| O 19 r 37(1) | 2752 | paragraph | fork | `o 19 r 37(1) the period for the written submissions and the bundle of authorities` (+1 more) | F9 |
| O 19 r 37(2) | 2752 | paragraph | encoded | `o 19 r 37(2) the written submissions are within the page limit` |  |
| O 19 r 37(3)(a) | 2753-2754 | sub-paragraph | fork | `o 19 r 37(3)(a) the appellate Court may allow the page limit to be exceeded` | F8 |
| O 19 r 37(3) | 2753-2756 | paragraph | fork | `o 19 r 37(3)(a) the appellate Court may allow the page limit to be exceeded` (+2 more) | F8 |
| O 19 r 37(3)(b) | 2755-2756 | sub-paragraph | encoded | `o 19 r 37(3)(b) the amount payable for the pages in excess` (+1 more) |  |
| O 19 r 37(4) | 2757 | paragraph | encoded | `o 19 r 37(4) the appellate Court may waive, refund, defer or apportion the payment of the fees` |  |
| O 19 r 37(5) | 2758 | paragraph | encoded | `o 19 r 37(5) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` |  |
| O 19 r 37(6)(a) | 2759-2760 | sub-paragraph | encoded | in the rule for 37(6): `o 19 r 37(6) the concluding paragraphs of the written submissions include what they must include` |  |
| O 19 r 37(6) | 2759-2762 | paragraph | fork | `o 19 r 37(6) the concluding paragraphs of the written submissions include what they must include` | F-MUST |
| O 19 r 37(6)(b) | 2761-2762 | sub-paragraph | encoded | in the rule for 37(6): `o 19 r 37(6) the concluding paragraphs of the written submissions include what they must include` |  |
| O 19 r 38 heading | 2763 | rule heading | inert (reason 1) | - | Powers in sections 40(1) and 58(1) of Supreme Court of Judicature Act exercisable by Registrar (O. 19, r. 38) |
| O 19 r 38(1)(a) | 2764-2765 | sub-paragraph | encoded | `o 19 r 38(1)(a) extension of time to file or serve a record of appeal, a supplemental record of appeal, an appellant's core bundle of documents, an appellant's Case or a respondent's Case` |  |
| O 19 r 38(1) | 2764-2784 | paragraph | encoded | `o 19 r 38(1) the Registrar may exercise the powers of the Appellate Division and the Court of Appeal in sections 40(1)(a) and 58(1)(a) of the Supreme Court of Judicature Act` (+8 more) |  |
| O 19 r 38(1)(b) | 2766-2767 | sub-paragraph | encoded | `o 19 r 38(1)(b) extension of time to file or serve an appellant's Reply, a respondent's core bundle of documents and an appellant's second core bundle, a bundle of authorities, written submissions or affidavits in an application, or a bundle of documents in an application for permission to appeal` |  |
| O 19 r 38(1)(c) | 2777-2778 | sub-paragraph | encoded | `o 19 r 38(1)(c) a direction under Rule 28(1)` |  |
| O 19 r 38(1)(d) | 2779-2780 | sub-paragraph | encoded | `o 19 r 38(1)(d) amendment of a document filed for an appeal or application` |  |
| O 19 r 38(1)(e) | 2781-2782 | sub-paragraph | encoded | `o 19 r 38(1)(e) expunging a document filed for an appeal or application, and consequential directions` |  |
| O 19 r 38(1)(f) | 2783-2784 | sub-paragraph | encoded | `o 19 r 38(1)(f) rescheduling of a hearing` |  |
| O 19 r 38(2) | 2785 | paragraph | encoded | `o 19 r 38(2) an application to vary or discharge may be made to a single Judge sitting in the Appellate Division or the Court of Appeal` (+3 more) |  |
| O 19 r 39 heading | 2786 | rule heading | inert (reason 1) | - | Transfer of appeal from Appellate Division to Court of Appeal (O. 19, r. 39) |
| O 19 r 39(1) | 2787 | paragraph | encoded | `o 19 r 39(1) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on the application` |  |
| O 19 r 39(2)(a) | 2787-2788 | sub-paragraph | encoded | in the rule for 39(2): `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` |  |
| O 19 r 39(2) | 2787-2792 | paragraph | encoded | `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` |  |
| O 19 r 39(2)(b) | 2789-2790 | sub-paragraph | encoded | in the rule for 39(2): `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` |  |
| O 19 r 39(2)(c) | 2791-2792 | sub-paragraph | encoded | in the rule for 39(2): `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` |  |
| O 19 r 39(3) | 2793 | paragraph | encoded | `o 19 r 39(3) the application under section 29D(2)(c)(i) is made, filed and served as required` (+1 more) |  |
| O 19 r 39(4) | 2794 | paragraph | encoded | `o 19 r 39(4) the application under section 29D(2)(c)(ii) is made, filed and served as required` (+1 more) |  |
| O 19 r 39(5)(a) | 2795-2796 | sub-paragraph | encoded | `o 19 r 39(5)(a) whether the proceedings relate to a matter of national or public importance` |  |
| O 19 r 39(5) | 2795-2808 | paragraph | encoded | `o 19 r 39(5) the Court of Appeal may have regard to the matter` (+8 more) |  |
| O 19 r 39(5)(b) | 2797-2798 | sub-paragraph | encoded | `o 19 r 39(5)(b) whether the appeal will raise a point of law of public importance` |  |
| O 19 r 39(5)(c) | 2799-2800 | sub-paragraph | encoded | `o 19 r 39(5)(c) the complexity and novelty of the issues in the appeal` |  |
| O 19 r 39(5)(d) | 2801-2802 | sub-paragraph | encoded | `o 19 r 39(5)(d) whether there is a decision of the Court of Appeal in relation to a point of law raised in the appeal which may be material to the outcome of the appeal` |  |
| O 19 r 39(5)(e) | 2803-2804 | sub-paragraph | encoded | `o 19 r 39(5)(e) whether there are conflicting judicial decisions` |  |
| O 19 r 39(5)(f) | 2805-2806 | sub-paragraph | encoded | `o 19 r 39(5)(f) the significance of the results of the proceedings` |  |
| O 19 r 39(5)(g) | 2807-2808 | sub-paragraph | encoded | `o 19 r 39(5)(g) any other relevant matter` |  |
| O 19 r 40 heading | 2809 | rule heading | inert (reason 1) | - | Transfer of appeal from Court of Appeal to Appellate Division of High Court (O. 19, r. 40) |
| O 19 r 40(1)(a) | 2810-2811 | sub-paragraph | encoded | `o 19 r 40(1)(a) the appeal was not made to the Court of Appeal in accordance with section 29C of the Supreme Court of Judicature Act` |  |
| O 19 r 40(1) | 2810-2815 | paragraph | encoded | `o 19 r 40(1) the Court of Appeal is to have regard to the matter` (+5 more) |  |
| O 19 r 40(1)(b) | 2812-2813 | sub-paragraph | encoded | `o 19 r 40(1)(b) none of the legal issues raised on appeal engage any of the matters set out in the Sixth Schedule to the Supreme Court of Judicature Act` |  |
| O 19 r 40(1)(c) | 2814-2815 | sub-paragraph | encoded | `o 19 r 40(1)(c) all of the legal issues raised on appeal in relation to the matters set out in the Sixth Schedule relate to issues of settled law` |  |
| O 19 r 40(2)(a) | 2816-2817 | sub-paragraph | encoded | in the rule for 40(2): `o 19 r 40(2) the application under section 29E(2)(b) is made, filed and served as required` (+1 more) |  |
| O 19 r 40(2) | 2816-2819 | paragraph | encoded | `o 19 r 40(2) the application under section 29E(2)(b) is made, filed and served as required` (+1 more) |  |
| O 19 r 40(2)(b) | 2818-2819 | sub-paragraph | encoded | `o 19 r 40(2)(b) the period for the application on the ground in section 29E(2)(b)` |  |
| O 19 Division 4 heading | 2820 | Division heading | inert (reason 1) | - | Appeals from Disciplinary Tribunal under Medical Registration Act |
| O 19 r 41 heading | 2821 | rule heading | inert (reason 1) | - | Appeals under section 59G of Medical Registration Act (O. 19, r. 41) |
| O 19 r 41(1) | 2822 | paragraph | encoded | `o 19 r 41(1) the appeal is brought by filing and serving an originating application` |  |
| O 19 r 41(2)(a) | 2823-2824 | sub-paragraph | encoded | `o 19 r 41(2)(a) the record of proceedings` |  |
| O 19 r 41(2) | 2823-2829 | paragraph | encoded | `o 19 r 41(2) the appellant must file and serve the appellant's documents within 8 weeks and the respondent must follow within 28 days` (+7 more) |  |
| O 19 r 41(2)(b) | 2825-2826 | sub-paragraph | encoded | `o 19 r 41(2)(b) the appellant's written submissions` |  |
| O 19 r 41(2)(c) | 2827-2828 | sub-paragraph | encoded | `o 19 r 41(2)(c) the appellant's bundle of authorities` |  |
| O 19 r 41(3)(a) | 2830-2831 | sub-paragraph | encoded | `o 19 r 41(3)(a) the respondent's written submissions` |  |
| O 19 r 41(3) | 2830-2834 | paragraph | encoded | `o 19 r 41(3) the period for the respondent's documents` (+5 more) |  |
| O 19 r 41(3)(b) | 2832-2833 | sub-paragraph | encoded | `o 19 r 41(3)(b) the respondent's bundle of authorities` |  |
| O 19 r 41(4) | 2835 | paragraph | encoded | `o 19 r 41(4) an affidavit may be filed in an appeal brought under paragraph (1)` |  |
| O 19 r 41(5) | 2836 | paragraph | encoded | `o 19 r 41(5) the written submissions are within the page limit` |  |
| O 19 r 41(6)(a) | 2837-2838 | sub-paragraph | fork | `o 19 r 41(6)(a) the General Division may allow the page limit to be exceeded` | F8 |
| O 19 r 41(6) | 2837-2840 | paragraph | fork | `o 19 r 41(6)(a) the General Division may allow the page limit to be exceeded` (+2 more) | F8 |
| O 19 r 41(6)(b) | 2839-2840 | sub-paragraph | encoded | `o 19 r 41(6)(b) the amount payable for the pages in excess` (+1 more) |  |
| O 19 r 41(7) | 2841 | paragraph | encoded | `o 19 r 41(7) the General Division may waive, refund, defer or apportion the payment of the fees` |  |
| O 19 r 41(8) | 2842 | paragraph | encoded | `o 19 r 41(8) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` |  |
| O 19 r 41(9)(a) | 2843-2844 | sub-paragraph | encoded | in the rule for 41(9): `o 19 r 41(9) the concluding paragraphs of the written submissions include what they must include` |  |
| O 19 r 41(9) | 2843-2846 | paragraph | encoded | `o 19 r 41(9) the concluding paragraphs of the written submissions include what they must include` |  |
| O 19 r 41(9)(b) | 2845-2846 | sub-paragraph | encoded | in the rule for 41(9): `o 19 r 41(9) the concluding paragraphs of the written submissions include what they must include` |  |
| O 19 r 41(10)(a) | 2847-2848 | sub-paragraph | encoded | `o 19 r 41(10)(a) Rule 7 (Powers of appellate Court)` |  |
| O 19 r 41(10) | 2847-2862 | paragraph | fork | `o 19 r 41(10) listed provision applies` (+18 more) | F7; silent: rule 41 sets no amount of security for an appeal under section 59G of the Medical Registration Act; no function; hand-gathered: `o 19 r 41 the provision applies to proceedings under section 59G of the Medical Registration Act` (E1, option B) |
| O 19 r 41(10)(b) | 2849-2850 | sub-paragraph | encoded | `o 19 r 41(10)(b) Rule 8 (Absence of parties)` |  |
| O 19 r 41(10)(c) | 2851-2852 | sub-paragraph | encoded | `o 19 r 41(10)(c) the reference in Rule 10 is to be disregarded` (+5 more) |  |
| O 19 r 41(10)(d) | 2853-2854 | sub-paragraph | encoded | `o 19 r 41(10)(d) Rule 11 (Consent judgment or order)` |  |
| O 19 r 41(10)(e) | 2855-2856 | sub-paragraph | encoded | `o 19 r 41(10)(e) Rule 12 (Judgment)` |  |
| O 19 r 41(10)(f) | 2857-2858 | sub-paragraph | encoded | `o 19 r 41(10)(f) Rule 34 (Further arguments)` |  |
| O 19 r 41(10)(g) | 2859-2860 | sub-paragraph | encoded | `o 19 r 41(10)(g) Rule 35(1) (Applications to appellate Court)` (+3 more) |  |
| O 19 r 41(10)(h) | 2861-2862 | sub-paragraph | encoded | `o 19 r 41(10)(h) Rule 37 (Written submissions for applications to appellate Court)` |  |
| O 19 r 41(11)(a) | 2863-2864 | sub-paragraph | encoded | `o 19 r 41(11)(a) a reference to the appellate Court` (+1 more) |  |
| O 19 r 41(11) | 2863-2866 | paragraph | encoded | `o 19 r 41(11) the court or body that the reference is read as` (+8 more) |  |
| O 19 r 41(11)(b) | 2865-2866 | sub-paragraph | encoded | `o 19 r 41(11)(b) a reference to the lower Court` (+1 more) |  |
| O 19 r 41(12)(a) | 2867-2868 | sub-paragraph | fork | `o 19 r 41(12)(a) Rule 1(f), which paragraph (12)(a) excepts` (+1 more) | F7 |
| O 19 r 41(12) | 2867-2870 | paragraph | fork | `o 19 r 41(12) the provision applies to proceedings under section 59G of the Medical Registration Act` (+3 more) | F7; hand-gathered: `o 19 r 41 the provision applies to proceedings under section 59G of the Medical Registration Act` (E1, option B) |
| O 19 r 41(12)(b) | 2869-2870 | sub-paragraph | encoded | `o 19 r 41(12)(b) Order 20` |  |
| O 19 r 41 "appellant" | 2871 | defined term | encoded | `o 19 r 41(13) a person is the appellant` |  |
| O 19 r 41(13) | 2871-2875 | paragraph | encoded | `o 19 r 41(13) a body is a Disciplinary Tribunal` (+18 more) |  |
| O 19 r 41 "bundle of authorities" | 2872 | defined term | encoded | `o 19 r 41(13) a document is a bundle of authorities` |  |
| O 19 r 41 "Disciplinary Tribunal" | 2873 | defined term | encoded | `o 19 r 41(13) a body is a Disciplinary Tribunal` |  |
| O 19 r 41 "record of proceedings" | 2874 | defined term | encoded | `o 19 r 41(13) a document is part of the record of proceedings` |  |
| O 19 r 41 "respondent" | 2875 | defined term | encoded | `o 19 r 41(13) a person is the respondent` |  |

## Fork register (roc4)

### The rulings, word for word as printed in BRIEF.md

The four bullets of "What they mean for your work" (BRIEF.md lines 75-78), which line 79 tells the part to put here:

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

The four rulings as the brief prints them first (BRIEF.md lines 69-72), with Meng's words:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### Forks this row took (roc4)

Places where the text can be read two ways with different outcomes, and the reading each module takes.
The labels F3, F4, F5, F7, F8, F9, F10, F11, F12 and F13 are the ones the module comments and coverage rows cite; there is no F1, F2 or F6 in this row.
F-OTHERTHAN and F-MUST are findings listed for a ruling: the sites they name answer as stated and none was changed on account of them.

**F3. Rule 4: what the answer is, the date time runs after, or the first day of the period** (modules: `roc4-order-19-div-1.l4`, rule 4).
Text: rule 4(1) "the time for the filing of an appeal ... does not start to run until after the lower Court has heard and determined all matters in the trial, including costs"; rule 4(1A) "the time ... does not start to run until after ..."; rule 4(2)(b) "starts to run from the date of that determination".
Reading 1 (taken): every function answers with the date AFTER WHICH the time runs, and the caller's count (O 3 r 3, in roc1's range) supplies the first day.
Licence: O 3 r 3(3), "Where an act is required to be done within a specified period after or from a specified date, the period begins immediately after that date" (text line 325), reads "from" and "after" alike.
Reading 2: the answer is the first day of the period, counted inclusively from the date in (2)(b).
That would put rule 4 in conflict with O 3 r 3(3) and would make "from" and "until after" differ in rule 4 alone.
Effect of the choice: a caller who wants the first day adds one day; nothing is lost.

**F4. Rule 8(1) and (2): what "fails to attend" means when the text says "the appellant or the appellant's solicitor"** (module: `roc4-order-19-div-1.l4`, rule 8).
Text: rule 8(1) "If the appellant or the appellant's solicitor fails to attend at the appeal, the appeal may be dismissed."; rule 8(2) "If the appellant or the appellant's solicitor attends and any respondent or the respondent's solicitor fails to attend, the appeal may proceed in the absence of such respondent."
Reading 1 (taken): the appellant side fails to attend when neither the appellant nor the solicitor attends.
Licence: rule 8(2) says the appellant side "attends" when "the appellant or the appellant's solicitor attends", so one of them suffices for attending, and failing to attend is the opposite of that.
Reading 2: the appeal may be dismissed when either of the two is absent.
Under reading 2 an appellant who attends alone, with the solicitor absent, could have the appeal dismissed; the text of rule 8(2) does not say that.
The same reading is applied to the respondent side in rule 8(2).

**F5. Rule 26(2): "the 15th day after the date on which the decision is made", set beside two moments** (module: `roc4-order-19-div-3.l4`, rule 26(2)).
Text: a request for further arguments must be made "before the earliest of the following: (a) the time at which the judgment or order relating to the decision is extracted; (b) the 15th day after the date on which the decision is made; (c) the time at which an application for permission to appeal against the decision is filed".
Paragraphs (a) and (c) are moments; paragraph (b) is a day.
Reading 1 (taken): every time is a count of minutes since midnight at the start of 1 January 2000; the 15th day is the decision date plus 15 days (O 3 r 3(3): the period begins immediately after the date), starting at that day's first minute; "before" is strict.
So a request made on the 15th day itself is not "before" it.
Reading 2: the 15th day is the end of that day, so a request on it is in time.
Reading 3: the 15th day is counted with the decision date as day 1 (a 14-day gap).
The text does not say which; reading 1 is the one that follows O 3 r 3(3) and treats a day as the interval it is.

**F7. Rule 41(10) and (12): which provisions of the Order apply to a Medical Registration Act appeal, when the text lists some that apply and some that do not** (module: `roc4-order-19-div-4.l4`, rule 41).
Text: rule 41(10) "Subject to this Rule and any other written law, the following Rules in this Order apply to proceedings before the General Division under section 59G of the Medical Registration Act ... (a) Rule 7 ... (h) Rule 37"; rule 41(12) "To avoid doubt, the following provisions do not apply ...: (a) Division 1 of this Order — except Rule 1(f) and the provisions mentioned in paragraph (10)(a) to (e); (b) Order 20."
Reading 1 (taken, by hand-gathering, E1 option B): a provision named in (12) as not applying answers `JUST FALSE`; a provision named in (10) answers `JUST TRUE` unless this Rule or a written law provides otherwise (a named input); any other provision answers `NOTHING`, because (10) does not say "only".
Reading 2: (10) is a closed list, so every provision it does not name does not apply (`JUST FALSE`).
Reading 3: only (12) removes anything, so everything else in the Order applies.
Rule 1(f) is named neither in (10) nor as not applying: (12)(a) takes it out of what does not apply without saying that it does, so the function answers `NOTHING` for it.
The "except ... (10)(a) to (e)" in (12)(a) stops at (e) because (10)(f) to (h) (Rules 34, 35 and 37) are in Division 3, which (12) does not mention (finding 6).
Division 3 rules other than those three are neither applied nor excluded for a Medical Registration Act appeal: rule 24's five limbs never reach it (they speak of appeals to the Appellate Division or the Court of Appeal), so those rules answer `NOTHING` through the gathered function.
Rule 41(12)(a), "except Rule 1(f)" (scenario 269): kept `NOTHING`.
The reviewer expected `JUST TRUE`, because rule 1(f) itself says the Order applies to these appeals; open question.

**F8. "In special circumstances" page-limit powers, and the 25-page bundle limit of rule 26(11)** (modules: `roc4-order-19-div-2.l4` rule 19(3)(a); `roc4-order-19-div-3.l4` rules 26(11), 26(12)(a), 32(3)(a), 37(3)(a); `roc4-order-19-div-4.l4` rule 41(6)(a)).
Text: rule 19(3) "The General Division may allow the page limit mentioned in paragraphs (1) and (2) to be exceeded — (a) in special circumstances; and (b) unless the General Division otherwise orders under paragraph (4), upon the payment of the fees ..."; rules 26(12), 32(3), 37(3) and 41(6) say the same of their own limits.
Rule 26(11) says only "The bundle of documents is subject to a page limit of 25 pages", with no "unless the appellate Court otherwise orders", and rule 26(12) points at the limit in paragraph (10), not at this one.
Reading 1 (taken): each power-to-exceed function answers `JUST TRUE` with special circumstances and `NOTHING` without them (`limited by its own wording`), because the text gives the power in special circumstances and does not say the Court may not allow excess pages otherwise.
For rule 26(11) the function asks only whether the bundle is within 25 pages.
Reading 2: "in special circumstances" is a "where" and the power answers `JUST FALSE` without them.
Reading 3 (rule 26(11) only): the text gives no power to exceed the 25 pages at all.
Open: can the court allow excess pages without special circumstances (rules 19(3), 32(3)), and can the 25-page limit be exceeded at all (rule 26(11)).

**F9. "(if any)" and "(if necessary)" read as "if"** (modules: `roc4-order-19-div-2.l4` rules 17(8), 17(10); `roc4-order-19-div-3.l4` rules 30(9), 30(11), 37(1)).
Text: the respondent's "core bundle of documents (if necessary)", the appellant's Reply "(if any)", the second core bundle "(if necessary)", the second bundle of authorities "(if any)", and "written submissions (if any)" in rule 37(1).
Reading 1 (taken): an "if" that is not met, so "is filed and served in time" answers `JUST FALSE` when the document is not required (the ruling on "if", 2026-11-05).
Reading 2: `NOTHING`, because the text asks nothing of the party and so says nothing about lateness.
Reading 3: `JUST TRUE`, because nothing is required and nothing is late.
The regulative rule for rule 17(10) takes "there is a Reply, a second core bundle or a second bundle to file" as a fact and ends in `FULFILLED` when there is none.

**F10. Rule 6(3): "for such time as enforcement has been delayed by the appeal"** (module: `roc4-order-19-div-1.l4`, rule 6(3)).
Text: "interest for such time as enforcement has been delayed by the appeal is to be allowed unless the lower Court or the appellate Court otherwise orders".
Reading 1 (taken): the time is a period the text fixes in its own words (ruling (a)), so with no time of delay the function answers `JUST FALSE`.
Reading 2: `NOTHING`, a scope limit without "only" (ruling (c)).

**F11. Rule 35(2): "Whenever under these Rules an application may be made either to the lower Court or to the appellate Court"** (module: `roc4-order-19-div-3.l4`, rule 35(2)).
Text: "Whenever ... it must not be made in the first instance to the appellate Court, except where there are special circumstances which make it impossible or impracticable to apply to the lower Court".
Reading 1 (taken): "whenever" counts as "where" (ruling of 2026-11-05), so where the Rules do not allow the application to go to either court the function answers `JUST FALSE`.
That `JUST FALSE` is this paragraph's answer: paragraph (2) gives no first-instance power there, and the function does not say that such an application may not go to the appellate Court under another provision.
Reading 2: `NOTHING`, a scope limit without "only".

**F12. A filing made before the period begins** (modules: every "filed and served in time" function; the rows marked are rules 14(1), 15(1), 25(1) and 26(1), which count from the date of the judgment or decision).
Text: O 3 r 3(3), "the period begins immediately after that date" (text line 325), and "within 14 days after the date of the judgment" in rule 14(1) and its like.
Reading 1 (taken): the functions compare the date of the act only with the last day (`AT MOST`), so an act done on the judgment date itself, before the period begins, counts as in time.
Reading 2: an act before the period begins is outside it and answers `JUST FALSE`.
The text does not say that an early filing is bad, and does not say that it is good.

**F13. A period that bounds a bar or a prohibition: the answer outside it stays `NOTHING`** (modules: `roc4-order-19-div-1.l4` rule 4(1) "has started to run"; `roc4-order-19-div-2.l4` rule 21; `roc4-order-19-div-3.l4` rules 26(3)(a) "may be filed" and 34; and the "subject to paragraphs (2), (3) and (4)" branch of rule 26(1)).
Text: rule 4(1) "does not start to run until after the lower Court has heard and determined all matters in the trial, including costs"; rule 26(3)(a) "may not be filed against the decision until the Judge ..."; rules 21 and 34 "After the General Division (the appellate Court) has heard the appeal and reserved its decision or after it has given its decision ... there are to be no further arguments from the parties".
Reading 1 (taken): each function answers `JUST FALSE` inside the bar or prohibition (rule 4(1): before the start date; rule 26(3)(a): until the Judge has acted; rules 21 and 34: after the hearing) and `NOTHING` on the other side, because the text does not say that the thing has happened or is allowed (ruling (d), and ruling (c) for rules 21 and 34).
The one exception is paragraph (1A) of rule 4, which is a positive start and makes "has started" `JUST TRUE` after its 30 days.
The branch of rule 26(1) that answers `NOTHING` when a request for further arguments has been made is the same shape: paragraph (3)(b) fixes the time then, and this function's period is not the one that governs.
Reading 2: `JUST FALSE` outside the period the text fixes in its own words (ruling (a)).
Under reading 2 "further arguments are allowed" would answer `JUST FALSE` before the hearing, and "has started to run" would answer `JUST FALSE` after the bar lapses; neither is what the text says.

**F-OTHERTHAN. Rule 7(7): "no such further evidence (other than evidence relating to matters occurring after the date of the decision appealed against) may be given except on special grounds"** (module: `roc4-order-19-div-1.l4`, rule 7(7)).
Three answers, as the module gives them: `o 19 r 7(7) the appellate Court has power to receive further evidence` answers `JUST TRUE` (`NOTHING` when a written law restricts it); `o 19 r 7(7) further evidence may be given` answers `JUST TRUE` when special grounds lift the bar; and the same function answers `NOTHING` for evidence the parenthesis takes out of the bar.
Reviewer expected `JUST TRUE` for the third (scenario 61); open question.

**F-MUST. A missing head of a "must contain" or "must include" list, and "must be" one of three forms** (modules: `roc4-order-19-div-2.l4` rules 16(4), 18(1); `roc4-order-19-div-3.l4` rules 26(7)(a), 30(5)(a), 37(6); `roc4-order-19-div-1.l4` rule 8(3) "must show good reason").
Answered `JUST FALSE`; the family rule does not list a bare must; open question.

**Notes on sites left as they are.**
Rule 17(3), asked on day 84 (the last day of the 12 weeks) with no grounds issued yet: `NOTHING`, because the grounds can still be issued that day; a reviewer scenario (114) expected another answer; open question.
Rule 6(1), "Except so far as the lower Court or the appellate Court may otherwise direct": `NOTHING` when a direction has been given, because what the direction says is outside the sources; a reviewer scenario (53) expected another answer; open question.
Rules 21 and 34, "after the General Division (or appellate Court) has heard the appeal and reserved its decision": the function answers `NOTHING` before that point; the bar itself is the `JUST FALSE` branch after it (fork F13).
Rules 9(2) ("In an expedited appeal"), 26(1) ("subject to paragraphs (2), (3) and (4)") and 35(4) ("A party who wishes to file an affidavit in reply"): scope limits without "only", `NOTHING` outside them.

### Hand-gathered functions (ruling E1, option B as guidance only)

Each function below gathers, by hand and in plain L4, the routes to one legal effect that the text spreads over several limbs.
Each limb still answers on its own in its own function (option C); the gathering is added for a reader and removes nothing.
No construct that gathers "by name" was used or proposed, and the Magna Carta pilot was not run.

| gathered function | what it gathers | file |
| --- | --- | --- |
| `o 19 r 1 this Order applies` | the six limbs (a) to (f) of rule 1 | `roc4-order-19-div-1.l4` |
| `o 19 r 2 the Division that concerns the appeal` | the Division rule 2 names for a route of appeal | `roc4-order-19-div-1.l4` |
| `o 19 r 4 the date after which the time for the filing starts to run` | rule 4(1) with (1A) and the exceptions in the opening words | `roc4-order-19-div-1.l4` |
| `o 19 r 24 this Division applies` | the five limbs (a) to (e) of rule 24 | `roc4-order-19-div-3.l4` |
| `o 19 r 26(7) the documents mentioned are filed and served with the application` | rule 26(7)(a) with (9): the seam that O 1 r 2(4)(c) asks for | `roc4-order-19-div-3.l4` |
| `o 19 r 41 the provision applies to proceedings under section 59G of the Medical Registration Act` | rule 41(10) with (12) (fork F7) | `roc4-order-19-div-4.l4` |

### How the rulings of 2026-11-04 and 2026-11-05 were applied in this row

- E1: option C everywhere, except the six functions above.
- N2: a flat negative answers `JUST FALSE` (15 branches carry a `FALSE-kind` comment of the class "flat negative" in the marginal-readings tables).
  Where the negative names its bearer, the prohibition is derived from that answer in `roc4-order-19-duties.l4` with `SHANT`: the four bars that name the respondent (rules 17(9), 18(3), 30(10), 31(3)).
  The Hohfeld kinds are not typed into any person-facing answer; they are in the table below.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
  Where the text fixes a period in its own words ("within", "not later than", "begins from ... until", "on the last day of", "for a period not exceeding", "at any time after X"), outside the period the answer is `JUST FALSE`.
  A "where ..." condition that is not met is `JUST FALSE`, like "if".
  A scope limit with no "only" is `NOTHING` outside the scope.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  A definition the text itself hands to a list is `JUST FALSE` when no head of the list holds, and a bare list stays `NOTHING`.
  "It is a defence ... to prove that X" is `JUST FALSE` for that provision's defence when X is not proved.
  "When", "upon" and "whenever" count as "where".
  "The property does not pass until X" is encoded as a bar in its own yes/no function (`JUST TRUE` before X, `JUST FALSE` after X) and never claims that the thing has happened.
- Assumed, not ruled: "once" and "in the event of" count as "where" (neither word occurs in rules 1 to 41 of this Order, so no site depends on it), and a function that returns a number, a date or a record cannot carry `JUST FALSE`, so it has a yes/no twin.
  The twins here: the number of sets of security in rules 16(3), 27(3) and 35(8) has the yes/no function "must provide security for each ..." beside it; the amount payable for excess pages in rules 19(3)(b), 26(12)(b), 32(3)(b), 37(3)(b) and 41(6)(b) has the yes/no function "the fees and additional fees ... are payable"; the date time runs after in rule 4 has `o 19 r 4(1A) this paragraph applies` and the bar function.
- Pass-through audit (2026-11-05): every function that calls another `MAYBE BOOLEAN` function and returns what it said was read, because `IF f ... EQUALS JUST TRUE THEN ... ELSE NOTHING` loses a `JUST FALSE` from `f`.
  Rules 1, 2 and 24 pass limbs through with `JUST TRUE` and end in `NOTHING` because their lists are not closed; rule 1(b)'s own `JUST FALSE` (a judgment of the Registrar) is passed on.
  Rule 4: the start-date function takes (1A) first; the "has started" function takes (1A) first and then the bar; neither loses a `JUST FALSE`.
  Rule 26(3)(a): "may be filed" answers `JUST FALSE` while the bar holds and `NOTHING` otherwise, including when no request for further arguments was made, where the bar function answers `JUST FALSE` ("If a request ... has been made" is not met); this is ruling (d), the bar never claims the thing has happened.
  Rule 26(7) and the gathered rule 41 function call functions that never answer `NOTHING`, or that never answer `JUST FALSE`; rules 41(10) and 41(12) pass a limb's answer straight through.
  The number-valued functions (the amount payable for excess pages, the number of sets of security) cannot carry `JUST FALSE`; the yes/no function beside each carries it.
- Periods (a): 33 branches answer `JUST FALSE` outside a period the text fixes.
- "Where", "when", "upon", "if", "after", "in the case of" not met (b), (c): 105 branches answer `JUST FALSE`.
  This pass moved 18 branches from `NOTHING` to `JUST FALSE` under that reading: the "on application", "upon application" and "if ... applies" powers (rules 14(2), 15(4), 19(4), 25(2), 26(13), 32(4), 37(4), 41(7)), the "(if any)" and "(if necessary)" documents (fork F9), "for such time as" (fork F10) and "whenever" (fork F11).
  The branches kept `NOTHING` as scope limits or open questions are named in forks F8 and the notes after F-MUST.
- Scope limit without "only" (c): the `limited by its own wording` and `list not closed` branches answer `NOTHING`.
- Delegated definitions (a): rule 41(13) hands "Disciplinary Tribunal" to section 2 of the Medical Registration Act; the function takes the Act's answer as an input and answers `JUST FALSE` when the input says the body is not one (the input is a `BOOLEAN` the caller states).
- "Until" bars (d): rule 4(1) has the bar as its own yes/no function (`o 19 r 4(1) the time for the filing cannot yet start to run`) and the "has started" function beside it.
  Meng's note on (d), "i hope we are using the deontic mechanisms to examine a trace", is a request about modelling and not part of the ruling; the rule 4(1) bar is a decision function only, and no regulative rule was written for it.
  The regulative rules in this row that a trace can run are the timed duties and the four bars that name the respondent, in `roc4-order-19-duties.l4`.
- "Unless the Court otherwise orders": where the text does not say what the order allows, the branch answers `NOTHING` (points outside the text); where the rule's own next paragraph supplies the displaced provision, `JUST FALSE`.

## Jural relations (roc4)

Hohfeld's correlatives: a claim is matched by a duty; a privilege (liberty) by a no-right; a power by a liability (being subject to the power); an immunity by a disability.
The kinds are recorded here and are not typed into any person-facing answer (ruling N2).
"The Court" is the court the rule names (the lower Court, the General Division, the appellate Court, the Court of Appeal).
A row names the main relations of its rule; where a rule has paragraphs that are all of one kind they are listed together.

| rule | relation | holder, and who bears the correlative |
| --- | --- | --- |
| 1 | none: scope | the six limbs say which appeals and applications the Order reaches |
| 2 | none: structure; (1) is a limit | the Order yields to written law on the right to appeal and on permission |
| 3 | none: definitions | "judgment", "record of appeal", "record of proceedings", "core bundle of documents", "second core bundle", "bundle of authorities", "trial" |
| 4 | none directly; "unless the Court otherwise orders" is a power | the Court may displace the start date; the parties are liable to it |
| 5 | (1) power to apply, with the Court's permission; (2), (3) duties | a non-party may apply to intervene; the Court's permission is a power and the parties are liable to it; the applicant must file and serve the application and the affidavit and set out the applicant's interest, and the parties to the appeal hold the claim to be served; (4) the Court's power to impose conditions, including security for costs, and the intervener is liable to it |
| 6 | (1), (2) disabilities; (3) claim | an appeal does not stay enforcement and does not invalidate an intermediate act (the appellant has no power to stay by appealing; the other side is immune), unless the Court directs otherwise; the party entitled to interest has a claim to it for the time enforcement was delayed, defeasible by the Court's order |
| 7 | (1), (2), (4)-(7) powers; (3) a limited privilege; (8) duty | the appellate Court's powers over parties and non-parties, which they are liable to; the parties may make only the oral submissions the Court orders; whoever adduces further evidence must do so in the manner directed |
| 8 | (1), (2) powers; (3) power and duties | the Court may dismiss or proceed in the absence (the absent party is liable); the absent party may apply to restore on the duties to file and serve within 14 days and to show good reason |
| 9 | powers and a privilege | any party may apply for an expedited appeal; the Court may order it and may dispense with or modify the Rules |
| 10 | (1) power; (2) duty and claim; (3) privilege and power; (4) powers | the appellant or applicant may withdraw by filing and serving Form 34 (the other parties are liable); on consent to payment of security the paying party must file the signed document and the receiving party has the claim to the security; a party may ask for directions and the Registrar may remove or direct; the Court keeps its powers at the hearing |
| 11 | privilege and power | the parties may tell the Registrar they wish to record a consent judgment; the Court may dispense with attendance and record it |
| 12 | powers; duty; claim | the Court may give its decision orally or in writing, and a Judge may deliver it despite another Judge's absence; the Registrar must inform the parties of the matters in (2)(b); every party has a claim to a copy of a written decision on paying the relevant charges |
| 13 | none: scope and definition | |
| 14 | (1) duty; (2) power | the appellant must file and serve the notice of appeal in Form 35 in 14 days (the parties with an interest hold the claim to be served); the General Division, and the lower Court if applied to in time, may extend |
| 15 | (1)-(3) duties; (4) power | a party needing permission must apply to the lower Court, or to the General Division after a refusal, and serve it within 14 days, and must file and serve the notice of appeal within 14 days of permission; the courts may extend time |
| 16 | (1), (3), (4), (5) duties; (2) no-duty; (6) privilege; (7) power | the appellant must provide security in the form and amount stated and file the certificate (the respondent holds the claim); co-appellants need provide only one set; any party may apply to vary or waive; the Court may order further security |
| 17 | duties, liabilities, privileges, disabilities | (1) the lower Court must issue its written grounds; (2) the Registry must notify; (3) the appellant must apply to proceed and the respondent has a privilege to apply or give 14 days' notice and then a power to apply to strike out; (4), (8), (10) the appellant and the respondent must file and serve their documents in the periods stated; (5), (9) the appeal is deemed withdrawn and the respondent is barred (liabilities of the defaulter) unless the Court orders otherwise; (6) a claim to the security on consent; (7) a privilege to ask for directions; (11), (12) privileges to join in one Case; (13) a passive party is under no duty to file a separate Case; (14) a privilege to seek directions for a joint Case; (15)-(18) duties to try to agree, to ask for a conference or directions, to inform the Registrar and to file a joint record; (19), (20) disabilities: no other document and no written submissions unless the General Division orders |
| 18 | duties; liability | the content each Case and Reply must have; (3) a respondent who fails (2)(d) is barred from those submissions unless the Court orders otherwise; (5) the Cases must contain everything the party intends to put forward |
| 19 | disabilities; power; duty | page limits bind the parties unless the General Division orders otherwise; it may allow excess in special circumstances on payment of the fees; (4) it may waive, refund, defer or apportion them |
| 20 | (1) none; (2), (3) duties and claims | the security must be paid to the respondent towards the costs ordered and the balance to the appellant, or all to the appellant if no costs are payable; the text does not name who must pay it out |
| 21 | disability | no further arguments after the General Division has heard and reserved, unless it directs otherwise |
| 22 | duty | the appellant must file a certified copy with the Registrar of the State Courts |
| 23 | duty | enforcement steps must be taken in the State Courts |
| 24 | none: scope | |
| 25 | (1) duty; (2) power | the appellant must file and serve Form 35 in 28 days; the courts may extend |
| 26 | duties, powers, disabilities, privileges | (1) a party must apply for permission in 14 days; (2), (3) the Judge may hear further arguments and the party cannot apply for permission until the Judge acts; (5) the Court of Appeal's power to grant permission on the stated grounds; (6) a power to apply to the other appellate Court; (7), (8) duties and privileges to file submissions and bundles; (9) duty to serve; (10), (11), (14) page-limit and one-set disabilities; (12), (13) the Court's powers over excess pages and fees; (15), (16) disabilities: no affidavit and no oral argument without leave; (17) duty to file Form 35 in 14 days; (18) power to extend |
| 27 | as rule 16 | security of $20,000 |
| 28 | powers | the appellate Court may give directions for joint documents in related appeals, on its own motion or on a request |
| 29 | powers | the appellate Court may order that Division 3 not apply and that Division 5 of Order 18 apply, and may modify the rules |
| 30 | as rule 17, with the differences in finding 2 | and (5): the record filed in the Appellate Division is treated as the record in the Court of Appeal |
| 31 | as rule 18 | |
| 32 | as rule 19 | page limits 55, 55 and 25 |
| 33 | as rule 20 | |
| 34 | disability | as rule 21 |
| 35 | duties, privileges, disabilities, powers | (1), (2), (13) how an application must be made; (3), (16) no oral arguments and no further affidavit without leave; (4), (15) a party may file an affidavit in reply and must file and serve it in the stated period; (5) no Case needs to be filed (the party is under no duty); (6)-(10) duty to provide security of $5,000, per opposing party; (11), (12) a power to apply to vary or waive and the Court's power to order more; (14) the applicant's duty to file the summons and affidavit in 14 days |
| 36 | duty | the applicant must file and serve the application in 14 days |
| 37 | duties, disabilities, powers | (1) the applicant and the opposing party must file written submissions in 14 days; (2), (5) page limit and one set; (3), (4) the Court's powers over excess and fees; (6) the concluding paragraphs must include the stated matters |
| 38 | (1) power; (2) power and immunity | the Registrar may exercise the stated powers in the six circumstances (the parties are liable); a party may apply to a single Judge to vary or discharge, and that Judge's decision is final |
| 39 | powers; duties | the Court of Appeal's power to transfer on application or its own motion; the applicant's duty to apply under Rule 35 and file and serve in the stated time; (5) matters the Court "may have regard to" |
| 40 | (1) duty; (2) duty | the Court of Appeal is to have regard to the stated matters; the applicant must apply under Rule 35 and file and serve in 14 days |
| 41 | duties; disabilities; powers; scope | (1)-(3) the appellant and the respondent must bring the appeal and file and serve in 8 weeks and 28 days; (4), (5), (8) disabilities; (6), (7) the General Division's powers over excess pages and fees; (9) content; (10)-(12) which provisions apply; (13) definitions |

## Marginal readings for a lawyer (roc4)

The brief gives two readings as the status quo: a failed "if" or "where" counts as the text's no, clause by clause, within the provision that holds it, and flat negatives count as the text's no; a prohibition or grant limited by its own wording does not.
Every branch below rests on one of them or on a reading of this row's own, and the other reading is stated.

### The readings to check first

These are the ones where a lawyer is most likely to disagree.

1. **A late act answers `JUST FALSE`, not `NOTHING`.** Every "is filed and served in time" function answers `JUST FALSE` after the last day (ruling 2026-11-05 (a)).
   Other reading: `NOTHING`, because the Court can extend time (rules 14(2), 15(4), 25(2), 26(18)) and rule 8(3) lets an absent party restore a dismissed appeal.
2. **"Specified time" is the period in the paragraph that imposes the duty.** Rules 17(5), 17(9), 30(6) and 30(10) say "within the specified time" and name none.
   Other reading: the phrase names nothing, so the consequences (deemed withdrawal, the bar) answer `NOTHING`.
3. **"Unless the appellate Court otherwise orders" is an input, and its effect depends on what is asked.**
   Where the proposition asked is the very consequence the order displaces (rules 17(5), 17(9), 18(3), 30(6), 30(10), 31(3)), an order answers `JUST FALSE`: the displacing provision is in the text and flips exactly that proposition.
   Where the text is a flat negative with an "unless ... otherwise orders" and says nothing of what an order allows (rules 10(3)(b), 17(7)(b), 17(19), 17(20), 26(16), 30(8)(b), 30(20), 30(21), 35(3)), the function answers `JUST FALSE` when no order has been made and `NOTHING` when one has (what the order allows is outside the sources).
   Rule 4(1) has both shapes: the date function answers `NOTHING` when an order or a written law may displace it, and the bar function ("cannot yet start to run") answers `JUST FALSE` when the Court has ordered otherwise.
   Other reading: `NOTHING` in every case where an order is possible.
4. **Rule 38(1)(a), (d) and (e): missing consent answers `JUST FALSE` for that limb.** The Registrar's power in those three limbs is given "and all of the parties consent"; when one does not, that limb answers `JUST FALSE`.
   Other reading: `NOTHING`, because the Registrar might act under another limb, and the list in rule 38(1) does not say "only".
5. **Rule 39(1): `JUST FALSE` unless the application is to the Court of Appeal on the ground that it is more appropriate for it to hear the appeal.** Other reading: `NOTHING`, because the paragraph says when the Court may act on that ground and does not say that it may not on any other.
6. **Rule 41(10) and (12), and rule 1(f): `NOTHING` for a provision neither paragraph names** (fork F7).
7. **Rules 30(4) and 35(4), "Except ...": the function for the general case answers `JUST FALSE` when the exception applies.** For rule 30(4) that is "Except for a case to which paragraph (5) applies"; for rule 35(4), "Except where Rule 26(15) provides otherwise".
   Other reading: `NOTHING`, because the exception removes the case from the paragraph without saying what then applies.
8. **Rule 30(5), "In the case of an appeal to the Court of Appeal against a decision of the Appellate Division": read like a "where".** For another route, the record-of-appeal function answers `JUST FALSE`.
   Other reading: `NOTHING`, because "in the case of" is a scope phrase, not a condition (ruling (c)).
9. **Rule 4(1) with (1A): "has started to run" is `JUST TRUE` only on the strength of paragraph (1A), and `NOTHING` on the lapse of the bar alone.** Paragraph (1A) says time "starts to run after the expiry of the 30-day period" when costs are not decided within it, so on the day after those 30 days "has started" answers `JUST TRUE` whether costs are still undecided or were decided later; paragraph (1) says only when time does not start, so on any other day after the bar has lapsed the function answers `NOTHING`, and before the start date `JUST FALSE`.
   Other reading: `JUST TRUE` whenever the bar has lapsed, because a bar that has lapsed means the time runs.
10. **Rule 26(3)(a), "may be filed": `NOTHING` after the Judge has acted.** The paragraph says the application "may not be filed ... until the Judge" acts, and not that it may be filed afterwards without more.
    Other reading: `JUST TRUE` once the Judge has acted.
11. **A "(if any)" or "(if necessary)" document answers `JUST FALSE` when none is required** (fork F9). Rules 17(8), 17(10), 30(9), 30(11) and 37(1): an "if" that is not met.
    Other readings: `NOTHING`, because the paragraphs speak of the document only when it exists; or `JUST TRUE`, because nothing is required of the party.
12. **A power given "on application", "upon application" or "if the party applies" answers `JUST FALSE` when there is no application.** Rules 14(2), 15(4), 19(4), 25(2), 26(13), 32(4), 37(4) and 41(7): "upon" and "on" count as "where".
    Other reading: `NOTHING`, because the paragraph gives the power on an application and does not say that the Court has none without one.
13. **Rules 6(3) ("for such time as enforcement has been delayed") and 35(2) ("Whenever under these Rules ... either to the lower Court or to the appellate Court"): `JUST FALSE` when the time or the case is absent** (forks F10 and F11).
    Other reading: `NOTHING`, scope limits without "only".
14. **"In special circumstances" powers (rules 19(3), 26(12), 32(3), 37(3), 41(6)) answer `NOTHING` without special circumstances** (fork F8).
    Other reading: `JUST FALSE`, because the phrase is a "where".
15. **A requirement to apply to a named court is checked (rules 15(1), 26(1)).** The function takes whether the application is made to the lower Court (rule 15(1)) or to the appellate Court (rule 26(1)) and answers `JUST FALSE` when it was made to another court.
    Other reading: the court is only in the function's name and the rule says nothing about another court.

### Every branch, by class

Counted from the comments in the four layer-1 modules by `work/marginal.py`: 308 `JUST FALSE` branches and 161 `NOTHING` branches carry a kind comment.
Each class below states the reading taken and the other reading.
The class of a `JUST FALSE` branch was decided by script from the words of its own comment and quote (a period, a "where/when/upon/if/after", an "Except/unless", a flat negative, or a requirement not met); a branch that is in the wrong class is a defect in the script, not a ruling, and the quote beside it is the check.

### JUST FALSE: A period the text fixes in its own words, and the act is outside it (33 branches)

- Reading taken: JUST FALSE (ruling of 2026-11-05 (a), which supersedes PLAN.md section 2).
- The other reading: NOTHING: the text states the period but not what follows a late act, and the Court can extend time in many places (for example rules 15(4), 25(2), 26(18)), so a late act is not by itself shown to be wrong.

| function | branches | first quote |
| --- | --- | --- |
| `o 19 r 8(3) the application to restore the appeal is filed and served in time` | 1 | "within 14 days after the dismissal or hearing of the appeal" |
| `o 19 r 8(3) the Court may restore the appeal for rehearing` | 1 | "within 14 days after the dismissal or hearing of the appeal" |
| `o 19 r 10(1) the appeal or application may still be withdrawn` | 1 | "at any time before the appeal or application is heard or dealt with" |
| `o 19 r 14(1) the notice of appeal is filed and served as required` | 1 | "within 14 days after the date of the judgment" |
| `o 19 r 15(1) the application for permission to the lower Court is made and served as required` | 1 | "within 14 days after the date of the judgment" |
| `o 19 r 15(2) the application for permission to the General Division is made and served as required` | 1 | "within 14 days after the date of the lower Court’s decision not to grant permission" |
| `o 19 r 15(3) the notice of appeal after permission is filed and served as required` | 1 | "within 14 days after the date of the decision granting permission" |
| `o 19 r 17(4) the appellant's document is filed and served in time` | 1 | "within 28 days after the date on which the Registry informs the parties that the record of proceedings is available" |
| `o 19 r 17(7)(a) the appellant or a party may request in writing to the General Division for directions on those issues` | 1 | "within 14 days after the date that the appeal is deemed withdrawn" |
| `o 19 r 17(8) the respondent's document is filed and served in time` | 1 | "within 28 days after the appellant serves the documents mentioned in paragraph (4) on the respondent" |
| `o 19 r 17(10) the appellant's reply document is filed and served in time` | 1 | "within 14 days after the respondent’s Case is served on the appellant" |
| `o 19 r 25(1) the notice of appeal is filed and served as required` | 1 | "within 28 days after the date of the lower Court’s judgment" |
| `o 19 r 26(1) the application for permission is filed and served as required` | 1 | "within 14 days after the date of the lower Court’s decision" |
| `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` | 1 | "within 14 days after the date the Judge affirms, varies or sets aside the decision after hearing further arguments or certifies ... that no furthe... |
| `o 19 r 26(6) the party may apply to the relevant appellate Court for permission to appeal` | 1 | "within 14 days after the date of the Registrar’s notification of the Appellate Division’s decision or the Court of Appeal’s decision" |
| `o 19 r 26(8) the opposing party's submissions are filed and served as required` | 1 | "within 14 days after the application, written submissions, any accompanying bundle of authorities and bundle of documents mentioned in paragraph (... |
| `o 19 r 26(17) the notice of appeal after permission is filed and served as required` | 1 | "within 14 days after the date of the decision granting permission" |
| `o 19 r 30(4) the appellant's document is filed and served in time` | 1 | "within 8 weeks after the date on which the Registry informs the parties that the record of proceedings is available" |
| `o 19 r 30(5) the appellant's document on an appeal from the Appellate Division is filed and served in time` | 1 | "within 8 weeks after the date on which the Registry informs the parties that the record of proceedings is available" |
| `o 19 r 30(8)(a) the appellant or a party may request in writing to the appellate Court for directions on those issues` | 1 | "within 14 days after the date that the appeal is deemed withdrawn" |
| `o 19 r 30(9) the respondent's document is filed and served in time` | 1 | "within 28 days after the appellant serves the documents mentioned in paragraph (4) or (5) on the respondent" |
| `o 19 r 30(11) the appellant's reply document is filed and served in time` | 1 | "within 14 days after the respondent’s Case is served on the appellant" |
| `o 19 r 35(4) the affidavit in reply is filed and served as required` | 1 | "within 14 days after the date the application and the affidavit in support of the application (if any) are served on that party" |
| `o 19 r 35(14) the summons and the supporting affidavit are filed and served as required` | 1 | "within 14 days after service of the notice of the appeal on the applicant" |
| `o 19 r 35(15) the affidavit in reply to the applicant's affidavit is filed and served as required` | 1 | "within 14 days after service of the applicant’s summons and affidavit on that party" |
| `o 19 r 36 the application for permission is filed and served as required` | 1 | "within 14 days after the date on which that direction or order is made" |
| `o 19 r 37(1) the written submissions and the bundle of authorities are filed and served as required` | 1 | "within 14 days after the date on which the opposing party’s affidavit in reply is to be filed and served" |
| `o 19 r 38(2) the application to vary or discharge is filed and served as required` | 1 | "within 14 days after the date on which that direction or order is made" |
| `o 19 r 39(3) the application under section 29D(2)(c)(i) is made, filed and served as required` | 1 | "within 14 days after the date of service of the notice of appeal on all parties who have an interest in the appeal" |
| `o 19 r 39(4) the application under section 29D(2)(c)(ii) is made, filed and served as required` | 1 | "no later than 14 days after the date of service of the appellant’s Case" |
| `o 19 r 40(2) the application under section 29E(2)(b) is made, filed and served as required` | 1 | "within 14 days after the date of service of the notice of appeal on all parties who have an interest in the appeal" |
| `o 19 r 41(2) the appellant's document is filed and served in time` | 1 | "within 8 weeks after the date on which the Registry informs the parties that the originating application has been fixed for hearing" |
| `o 19 r 41(3) the respondent's document is filed and served in time` | 1 | "within 28 days after the appellant serves the documents mentioned in paragraph (2) on the respondent" |

### JUST FALSE: A "where", "when", "upon", "if", "after" or "in the case of" that is not met (105 branches)

- Reading taken: JUST FALSE (rulings of 2026-11-05 (b) and (c): the failed condition is the text's no, clause by clause, within the provision that holds it).
- The other reading: NOTHING: "if A then B" does not itself say "if not A then not B".

| function | branches | first quote |
| --- | --- | --- |
| `o 19 r 4(1A) this paragraph applies` | 1 | "Where the lower Court does not hear and determine the issue of costs within 30 days" |
| `o 19 r 4(2)(b) this paragraph applies to a bifurcated portion` | 1 | "in the case of a bifurcated trial, where the lower Court has heard and determined a distinct bifurcated portion of the trial (including the issue ... |
| `o 19 r 5(4) the appellate Court may impose conditions on the permission to intervene` | 1 | "The appellate Court may impose conditions when the appellate Court grants permission to intervene" |
| `o 19 r 5(4) the condition of security for costs may be imposed on an intervening party` | 1 | "when the appellate Court grants permission to intervene" |
| `o 19 r 8(1) the appeal may be dismissed` | 1 | "If the appellant or the appellant’s solicitor fails to attend at the appeal, the appeal may be dismissed" |
| `o 19 r 8(2) the appeal may proceed in the absence of a respondent` | 1 | "If the appellant or the appellant’s solicitor attends and any respondent or the respondent’s solicitor fails to attend, the appeal may proceed in ... |
| `o 19 r 8(3) the Court may restore the appeal for rehearing` | 1 | "upon the application of the absent party" |
| `o 19 r 9(1) the lower Court or the appellate Court may order an expedited appeal` | 1 | "If the appeal is urgent or there is a special reason, the lower Court or the appellate Court may order an expedited appeal" |
| `o 19 r 10(2) the appeal or application is deemed withdrawn in relation to the relevant parties` | 1 | "Upon the filing of Form 34 and if there are no outstanding issues relating to costs or other matters" |
| `o 19 r 10(2) the security for costs must be paid and the solicitor's undertaking is discharged` | 1 | "if all the parties to the appeal or application consent to the payment of the security for costs ... and in such event" |
| `o 19 r 10(3)(a) a party may request the appellate Court in writing for directions on those issues` | 1 | "If there are any such outstanding issues mentioned in paragraph (2)" |
| `o 19 r 10(3)(c)(i) the Registrar may remove the appeal or application from the list` | 1 | "the Registrar may, upon receiving a request under sub‑paragraph ( a )" |
| `o 19 r 10(3)(c)(ii) the Registrar may give directions on the making of written submissions for the request` | 1 | "the Registrar may, upon receiving a request under sub‑paragraph ( a )" |
| `o 19 r 10(4)(a) the appeal or application remains on the list` | 1 | "if there are any such outstanding issues" |
| `o 19 r 10(4)(b)(i) the appellate Court may at the hearing decide an issue that remains outstanding` | 1 | "if there are any such outstanding issues" |
| `o 19 r 10(4)(b)(ii) the appellate Court may at the hearing make an order as to the disposal of the security for costs` | 1 | "if there are any such outstanding issues" |
| `o 19 r 11(1) the appellate Court may dispense with attendance and record the judgment or order in the agreed terms` | 1 | "Where the parties in any appeal or application to the appellate Court inform the Registrar that they wish to record a consent judgment or order" |
| `o 19 r 11(1) the Registrar is to inform the parties accordingly` | 1 | "Where the parties ... inform the Registrar ..., the Registrar is to inform the parties accordingly" |
| `o 19 r 12(2)(a) the appellate Court may direct the Registrar to inform the parties of its decision` | 1 | "Where the appellate Court has decided any matter without hearing oral arguments" |
| `o 19 r 12(2)(b) the parties are informed of what they are to be informed of` | 1 | "Where the appellate Court has decided any matter without hearing oral arguments" |
| `o 19 r 12(3) a party is entitled to a copy of the decision` | 1 | "upon payment of the relevant charges" |
| `o 19 r 14(2) the lower Court may extend the time for filing and serving the notice of appeal` | 2 | "if the appellant applies for such extension" |
| `o 19 r 15(1) the application for permission to the lower Court is made and served as required` | 1 | "Where permission to appeal is required" |
| `o 19 r 15(2) the application for permission to the General Division is made and served as required` | 1 | "Where the lower Court does not grant permission to appeal" |
| `o 19 r 15(3) the notice of appeal after permission is filed and served as required` | 1 | "Where permission to appeal is granted" |
| `o 19 r 15(4) the lower Court may extend the time for filing and serving an application for permission to appeal` | 2 | "if the application for such extension is made" |
| `o 19 r 16(2) the appellants need to provide only one set of security for the appeal` | 1 | "Where there is more than one appellant in the same appeal" |
| `o 19 r 16(3) the appellant must provide security for each respondent or each set of respondents` | 1 | "Where there is more than one respondent" |
| `o 19 r 17(1) the lower Court must issue its written grounds of decision` | 1 | "after the notice of appeal has been filed if the lower Court has not already done so" |
| `o 19 r 17(2) the Registry must notify the parties that the record of proceedings is ready for collection` | 1 | "The Registry must notify the parties when the record of proceedings is ready for collection" |
| `o 19 r 17(3) no written grounds of decision are issued within 12 weeks` | 1 | "If no written grounds of decision are issued within 12 weeks after the date of filing of the notice of appeal" |
| `o 19 r 17(3)(a) the appellant must apply in writing to the Registrar to proceed with the appeal and for a copy of the record of proceedings` | 1 | "If no written grounds of decision are issued within 12 weeks after the date of filing of the notice of appeal" |
| `o 19 r 17(3)(b) the respondent may apply in writing to the Registrar to proceed or give 14 days' written notice of intention to strike out the appeal` | 1 | "If no written grounds of decision are issued within 12 weeks ... if the appellant fails to do so" |
| `o 19 r 17(3)(c) the respondent may apply to strike out the appeal` | 1 | "after the expiry of the 14 days’ notice period mentioned in sub‑paragraph ( b ), the respondent may apply to strike out the appeal" |
| `o 19 r 17(5) the appeal is deemed withdrawn` | 1 | "Where the appellant fails to file and serve the record of appeal, the core bundle of documents or the appellant’s Case within the specified time" |
| `o 19 r 17(6) the security for costs must be paid and the solicitor's undertaking is discharged` | 1 | "Where an appeal is deemed withdrawn pursuant to paragraph (5) and if all the parties to the appeal consent to the payment of the security for costs" |
| `o 19 r 17(7)(a) the appellant or a party may request in writing to the General Division for directions on those issues` | 1 | "Where an appeal is deemed withdrawn pursuant to paragraph (5) and if there are any outstanding issues" |
| `o 19 r 17(7)(c) the Registrar of the Supreme Court may give directions on the making of written submissions for the request` | 1 | "the Registrar of the Supreme Court may, upon receiving a request under sub‑paragraph ( a )" |
| `o 19 r 17(8) the respondent's document is filed and served in time` | 1 | "the respondent’s core bundle of documents (if necessary)" |
| `o 19 r 17(9) the respondent is barred from making submissions at the hearing of the appeal` | 1 | "Where the respondent fails to file and serve the respondent’s Case within the specified time" |
| `o 19 r 17(11) all the appellants may join in one appellants' Case and in one appellants' Reply` | 1 | "Where there is more than one appellant in an appeal" |
| `o 19 r 17(12) all the respondents may join in one respondents' Case` | 1 | "Where there is more than one respondent in an appeal" |
| `o 19 r 17(14) the appellant and the respondent may seek directions from the General Division to file a joint Case` | 1 | "where there are special circumstances" |
| `o 19 r 17(16) the parties have requested a case conference or sought directions` | 1 | "Where the parties are unable to agree as mentioned in paragraph (15)" |
| `o 19 r 17(17) the parties have informed the Registrar of the agreed timelines and sought approval` | 1 | "Where the parties have agreed as mentioned in paragraph (15)" |
| `o 19 r 17(18) the parties have filed a joint record of appeal` | 1 | "Where there are 2 or more appeals arising from the same judgment" |
| `o 19 r 18(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` | 1 | "Where the respondent fails to comply with the requirements in paragraph (2)( d )" |
| `o 19 r 19(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "may allow the page limit ... to be exceeded ... upon the payment of the fees" |
| `o 19 r 19(4) the General Division may waive, refund, defer or apportion the payment of the fees` | 1 | "upon application" |
| `o 19 r 20(2) the security for costs must be paid to the respondent towards the costs ordered` | 2 | "Where costs are payable by the appellant to the respondent" |
| `o 19 r 20(3) the security for costs must be paid to the appellant and the appellant's solicitor is released from any undertaking` | 1 | "Where no costs are payable by the appellant to the respondent" |
| `o 19 r 25(2) the lower Court may extend the time for filing and serving the notice of appeal` | 2 | "if the appellant applies for such extension" |
| `o 19 r 26(1) the application for permission is filed and served as required` | 1 | "Where permission to appeal against a decision is required" |
| `o 19 r 26(2) the Judge who made the decision may hear further arguments` | 2 | "Where permission to appeal against a decision is required" |
| `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` | 1 | "If a request for further arguments in respect of a decision has been made under paragraph (2)" |
| `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` | 1 | "If a request for further arguments in respect of a decision has been made under paragraph (2)" |
| `o 19 r 26(5) the Court of Appeal may grant permission to appeal against a decision of the Appellate Division` | 1 | "Where permission to appeal under section 47(1) ... is required, the Court of Appeal may grant permission ..., where — (a) the appeal will raise a ... |
| `o 19 r 26(6) the party may apply to the relevant appellate Court for permission to appeal` | 1 | "where — (a) a party has made an application ...; and (b) the Appellate Division or the Court of Appeal has decided that the court ... is the Court... |
| `o 19 r 26(12)(b) the fees and additional fees for the pages in excess are payable` | 1 | "may allow the page limit ... to be exceeded ... upon the payment of the fees" |
| `o 19 r 26(13) the appellate Court may waive, refund, defer or apportion the payment of the fees` | 1 | "upon application" |
| `o 19 r 26(17) the notice of appeal after permission is filed and served as required` | 1 | "Where permission to appeal is granted" |
| `o 19 r 27(2) the appellants need to provide only one set of security for the appeal` | 1 | "Where there is more than one appellant in the same appeal" |
| `o 19 r 27(3) the appellant must provide security for each respondent or each set of respondents` | 1 | "Where there is more than one respondent" |
| `o 19 r 28(1) the appellate Court may give directions for the filing and service of joint documents` | 1 | "Where there are related appeals in the appellate Court" |
| `o 19 r 28(4) the appellate Court may direct modifications of the rules, including that this Division does not apply and Division 5 of Order 18 applies instead` | 1 | "Where the related appeals comprise one or more appeals filed under this Order and one or more appeals filed under Order 18" |
| `o 19 r 29(1) the appellate Court may order that this Division, or any part of it, does not apply to an appeal before it, and that Division 5 of Order 18, or any part of it, applies instead` | 1 | "The appellate Court may, if the appellate Court deems appropriate, order that" |
| `o 19 r 29(2) the appellate Court may order or direct modifications of the rules applicable to an appeal before it` | 1 | "The appellate Court may in any case if the appellate Court deems appropriate order or direct any modifications" |
| `o 19 r 30(1) the lower Court must issue its written grounds of decision` | 1 | "after the notice of appeal has been filed if the lower Court has not already done so" |
| `o 19 r 30(2) the Registry must notify the parties that the record of proceedings is ready for collection` | 1 | "The Registry must notify the parties when the record of proceedings is ready for collection" |
| `o 19 r 30(3) no written grounds of decision are issued within 12 weeks` | 1 | "If no written grounds of decision are issued within 12 weeks after the date of filing of the notice of appeal" |
| `o 19 r 30(3)(a) the appellant must apply in writing to the Registrar to proceed with the appeal and for a copy of the record of proceedings` | 1 | "If no written grounds of decision are issued within 12 weeks after the date of filing of the notice of appeal" |
| `o 19 r 30(3)(b) the respondent may apply in writing to the Registrar to proceed or give 14 days' written notice of intention to strike out the appeal` | 1 | "If no written grounds of decision are issued within 12 weeks ... if the appellant fails to do so" |
| `o 19 r 30(3)(c) the respondent may apply to strike out the appeal` | 1 | "after the expiry of the 14 days’ notice period mentioned in sub‑paragraph ( b ), the respondent may apply to strike out the appeal" |
| `o 19 r 30(5) the record of appeal filed in the Appellate Division is treated as the record of appeal in the Court of Appeal` | 1 | "In the case of an appeal to the Court of Appeal against a decision of the Appellate Division" |
| `o 19 r 30(6) the appeal is deemed withdrawn` | 1 | "Where the appellant fails to file and serve the record of appeal (including, where required under paragraph (5)( a ), the supplemental record of a... |
| `o 19 r 30(7) the security for costs must be paid and the solicitor's undertaking is discharged` | 1 | "Where an appeal is deemed withdrawn pursuant to paragraph (6) and if all the parties to the appeal consent to the payment of the security for costs" |
| `o 19 r 30(8)(a) the appellant or a party may request in writing to the appellate Court for directions on those issues` | 1 | "Where an appeal is deemed withdrawn pursuant to paragraph (6) and if there are any outstanding issues" |
| `o 19 r 30(8)(c) the Registrar of the Supreme Court may give directions on the making of written submissions for the request` | 1 | "the Registrar of the Supreme Court may, upon receiving a request under sub‑paragraph ( a )" |
| `o 19 r 30(9) the respondent's document is filed and served in time` | 1 | "the respondent’s core bundle of documents (if necessary)" |
| `o 19 r 30(10) the respondent is barred from making submissions at the hearing of the appeal` | 1 | "Where the respondent fails to file and serve the respondent’s Case within the specified time" |
| `o 19 r 30(12) all the appellants may join in one appellants' Case and in one appellants' Reply` | 1 | "Where there is more than one appellant in an appeal" |
| `o 19 r 30(13) all the respondents may join in one respondents' Case` | 1 | "Where there is more than one respondent in an appeal" |
| `o 19 r 30(15) the appellant and the respondent may seek directions from the appellate Court to file a joint Case` | 1 | "where there are special circumstances" |
| `o 19 r 30(17) the parties have requested a case conference or sought directions` | 1 | "Where the parties are unable to agree as mentioned in paragraph (16)" |
| `o 19 r 30(18) the parties have informed the Registrar of the agreed timelines and sought approval` | 1 | "Where the parties have agreed as mentioned in paragraph (16)" |
| `o 19 r 30(19) the parties have filed a joint record of appeal` | 1 | "Where there are 2 or more appeals arising from the same judgment" |
| `o 19 r 31(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` | 1 | "Where the respondent fails to comply with the requirements in paragraph (2)( d )" |
| `o 19 r 32(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "may allow the page limit ... to be exceeded ... upon the payment of the fees" |
| `o 19 r 32(4) the appellate Court may waive, refund, defer or apportion the payment of the fees` | 1 | "upon application" |
| `o 19 r 33(2) the security for costs must be paid to the respondent towards the costs ordered` | 2 | "Where costs are payable by the appellant to the respondent" |
| `o 19 r 33(3) the security for costs must be paid to the appellant and the appellant's solicitor is released from any undertaking` | 1 | "Where no costs are payable by the appellant to the respondent" |
| `o 19 r 35(7) the applicants need to provide only one set of security for the costs of the application` | 1 | "Where there is more than one applicant in an application" |
| `o 19 r 35(8) the applicant must provide security for each opposing party or each set of opposing parties` | 1 | "Where there is more than one opposing party" |
| `o 19 r 37(1) the written submissions and the bundle of authorities are filed and served as required` | 1 | "written submissions (if any)" |
| `o 19 r 37(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "may allow the page limit ... to be exceeded ... upon the payment of the fees" |
| `o 19 r 37(4) the appellate Court may waive, refund, defer or apportion the payment of the fees` | 1 | "upon application" |
| `o 19 r 39(5) the Court of Appeal may have regard to the matter` | 1 | "when determining whether it is more appropriate for the Court of Appeal to hear an appeal that has been made to the Appellate Division" |
| `o 19 r 41(6)(b) the fees and additional fees for the pages in excess are payable` | 1 | "may allow the page limit ... to be exceeded ... upon the payment of the fees" |
| `o 19 r 41(7) the General Division may waive, refund, defer or apportion the payment of the fees` | 1 | "upon application" |

### JUST FALSE: An "Except ..." or "unless ..." where the asked proposition is the one the exception removes (34 branches)

- Reading taken: JUST FALSE (the displacing provision is in the text, or the exception flips exactly the asked proposition).
- The other reading: NOTHING: the exception says only what it takes out, not that nothing else remains.

| function | branches | first quote |
| --- | --- | --- |
| `o 19 r 1(b) this Order applies to an appeal against a judgment of the General Division` | 1 | "except a judgment of the Registrar of the Supreme Court" |
| `o 19 r 1 this Order applies` | 1 | "except a judgment of the Registrar of the Supreme Court" |
| `o 19 r 4(1) the time for the filing cannot yet start to run` | 1 | "unless the Court otherwise orders" |
| `o 19 r 6(3) interest is allowed for the time enforcement has been delayed by the appeal` | 1 | "unless the lower Court or the appellate Court otherwise orders" |
| `o 19 r 7(7) further evidence may be given` | 1 | "no such further evidence ... may be given except on special grounds" |
| `o 19 r 10(3)(b) oral arguments may be made in the request` | 1 | "no oral arguments are to be made in a request under sub‑paragraph ( a ) unless the appellate Court otherwise directs" |
| `o 19 r 10(4)(a) the appeal or application remains on the list` | 1 | "Except as provided under paragraph (3)" |
| `o 19 r 10(4)(b)(i) the appellate Court may at the hearing decide an issue that remains outstanding` | 1 | "Except as provided under paragraph (3)" |
| `o 19 r 10(4)(b)(ii) the appellate Court may at the hearing make an order as to the disposal of the security for costs` | 1 | "Except as provided under paragraph (3)" |
| `o 19 r 17(5) the appeal is deemed withdrawn` | 1 | "the appeal is deemed withdrawn unless the appellate Court otherwise orders" |
| `o 19 r 17(7)(b) oral arguments may be made in the request` | 1 | "no oral arguments are to be made in a request under sub‑paragraph ( a ) unless the appellate Court otherwise directs" |
| `o 19 r 17(9) the respondent is barred from making submissions at the hearing of the appeal` | 1 | "is not allowed to make submissions at the hearing of the appeal unless the appellate Court otherwise orders" |
| `o 19 r 17(19) a document other than those set out in this Rule may be filed` | 1 | "No documents other than what have been set out in this Rule may be filed unless the General Division otherwise orders" |
| `o 19 r 17(20) written submissions or skeletal arguments may be filed before or at the appeal` | 1 | "No written submissions or skeletal arguments may be filed before or at the appeal unless the General Division otherwise orders" |
| `o 19 r 18(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` | 1 | "is not allowed to make the submissions mentioned in paragraph (2)( d ) unless the Court otherwise orders" |
| `o 19 r 19(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "unless the General Division otherwise orders under paragraph (4)" |
| `o 19 r 26(12)(b) the fees and additional fees for the pages in excess are payable` | 1 | "unless the appellate Court otherwise orders under paragraph (13)" |
| `o 19 r 26(16) oral arguments may be made in an application for permission to appeal` | 1 | "No oral arguments are to be made in an application for permission to appeal unless the appellate Court otherwise orders" |
| `o 19 r 30(4) the appellant's document is filed and served in time` | 1 | "Except for a case to which paragraph (5) applies" |
| `o 19 r 30(6) the appeal is deemed withdrawn` | 1 | "the appeal is deemed withdrawn unless the appellate Court otherwise orders" |
| `o 19 r 30(8)(b) oral arguments may be made in the request` | 1 | "no oral arguments are to be made in a request under sub‑paragraph ( a ) unless the appellate Court otherwise directs" |
| `o 19 r 30(10) the respondent is barred from making submissions at the hearing of the appeal` | 1 | "is not allowed to make submissions at the hearing of the appeal unless the appellate Court otherwise orders" |
| `o 19 r 30(20) a document other than those set out in this Rule may be filed` | 1 | "No documents other than what has been set out in this Rule may be filed unless the appellate Court otherwise orders" |
| `o 19 r 30(21) written submissions or skeletal arguments may be filed before or at the appeal` | 1 | "No written submissions or skeletal arguments may be filed before or at the appeal unless the appellate Court otherwise orders" |
| `o 19 r 31(3) the respondent is barred from making the submissions mentioned in paragraph (2)(d)` | 1 | "is not allowed to make the submissions mentioned in paragraph (2)( d ) unless the Court otherwise orders" |
| `o 19 r 32(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "unless the appellate Court otherwise orders under paragraph (4)" |
| `o 19 r 35(2) the application may be made in the first instance to the appellate Court` | 1 | "it must not be made in the first instance to the appellate Court, except where there are special circumstances" |
| `o 19 r 35(3) oral arguments may be made in an application to the appellate Court` | 1 | "No oral arguments are to be made in an application to the appellate Court unless the appellate Court otherwise orders" |
| `o 19 r 35(4) the affidavit in reply is filed and served as required` | 1 | "Except where Rule 26(15) provides otherwise" |
| `o 19 r 37(3)(b) the fees and additional fees for the pages in excess are payable` | 1 | "unless the appellate Court otherwise orders under paragraph (4)" |
| `o 19 r 37(5) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "There must not be more than one set of submissions for each party or set of parties represented by the same firm of solicitors unless the appellat... |
| `o 19 r 41(6)(b) the fees and additional fees for the pages in excess are payable` | 1 | "unless the General Division otherwise orders under paragraph (7)" |
| `o 19 r 41(8) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "There must not be more than one set of submissions for each party or set of parties represented by the same firm of solicitors unless the General ... |
| `o 19 r 41(12) the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | "the following provisions do not apply to proceedings before the General Division under section 59G ... (a) Division 1 of this Order — except Rule ... |

### JUST FALSE: A flat negative ("is not allowed", "must not", "there are to be no", "does not operate") (15 branches)

- Reading taken: JUST FALSE (ruling N2: a flat negative counts as the text's no).
- The other reading: NOTHING, or a prohibition typed in the person-facing answer (option C of N2, not taken).

| function | branches | first quote |
| --- | --- | --- |
| `o 19 r 4(1) the time for the filing cannot yet start to run` | 1 | "does not start to run until after the lower Court has heard and determined all matters in the trial, including costs" |
| `o 19 r 4(1) the time for the filing has started to run` | 1 | "does not start to run until after" |
| `o 19 r 6(1) the appeal operates as a stay of enforcement or of proceedings under the decision of the lower Court` | 1 | "an appeal does not operate as a stay of enforcement or of proceedings under the decision of the lower Court" |
| `o 19 r 6(2) an intermediate act or proceeding is invalidated by the appeal` | 1 | "no intermediate act or proceeding is to be invalidated by an appeal" |
| `o 19 r 17(13) a party with a passive interest is required to file a separate Case` | 1 | "is not required to file a separate Case" |
| `o 19 r 21 further arguments from the parties are allowed` | 1 | "there are to be no further arguments from the parties" |
| `o 19 r 26(3)(a) the application for permission to appeal cannot yet be filed against the decision` | 1 | "may not be filed against the decision until the Judge" |
| `o 19 r 26(3)(a) the application for permission to appeal may be filed against the decision` | 1 | "may not be filed against the decision until the Judge" |
| `o 19 r 26(14) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "There must not be more than one set of submissions for each party or set of parties represented by the same firm of solicitors" |
| `o 19 r 26(15) an affidavit may be filed in an application for permission to appeal` | 1 | "No affidavit is to be filed in an application for permission to appeal without the permission of the appellate Court" |
| `o 19 r 30(14) a party with a passive interest is required to file a separate Case` | 1 | "is not required to file a separate Case" |
| `o 19 r 34 further arguments from the parties are allowed` | 1 | "there are to be no further arguments from the parties" |
| `o 19 r 35(4) a further affidavit may be filed` | 1 | "no further affidavits may be filed without permission of the appellate Court" |
| `o 19 r 35(16) a further affidavit may be received in evidence` | 1 | "No further affidavit may be received in evidence without the permission of the appellate Court" |
| `o 19 r 41(4) an affidavit may be filed in an appeal brought under paragraph (1)` | 1 | "No affidavit is to be filed in an appeal brought under paragraph (1) without the permission of the General Division" |

### JUST FALSE: A requirement or definition that is not met (the text states what a thing must be or contain, and it is not) (121 branches)

- Reading taken: JUST FALSE: the thing the text asks about is not what the provision requires or lists.
- The other reading: NOTHING: the provision states the requirement and does not say what follows from missing it.

| function | branches | first quote |
| --- | --- | --- |
| `o 19 r 3 a document is a bundle of authorities` | 1 | "“bundle of authorities” means a compilation of authorities for the appeal" |
| `o 19 r 3 a document is part of a core bundle of documents` | 1 | "“core bundle of documents” means a certified copy of the judgment or grounds of decision of the lower Court, the extracted order of the lower Cour... |
| `o 19 r 3 a decision is a judgment` | 2 | "“judgment” means a judgment given by the lower Court" |
| `o 19 r 3 a document is part of the record of appeal` | 2 | "all documents filed in the lower Court (so far as are relevant to the matter decided and the nature of the appeal)" |
| `o 19 r 3 a document is part of the record of proceedings` | 2 | "and, in an appeal from the General Division, District Court or Magistrate’s Court, the certified transcript" |
| `o 19 r 3 a document is part of the second core bundle` | 2 | "not included in the appellant’s or respondent’s core bundle of documents" |
| `o 19 r 3 a proceeding is part of the trial` | 1 | "“trial” means the hearing on the merits of an originating claim or an originating application and includes all applications taken out or heard on ... |
| `o 19 r 4(2)(a) the lower Court is deemed to have heard and determined the issue of costs` | 1 | "the lower Court is deemed to have heard and determined the issue of costs when it has" |
| `o 19 r 5(2) the application and the supporting affidavit are filed and served as required` | 1 | "The application for permission to intervene and the supporting affidavit must be filed and served on all parties who have an interest in the appeal" |
| `o 19 r 5(3) the supporting affidavit sets out the applicant's interest` | 1 | "The supporting affidavit must set out the applicant’s interest in the appeal" |
| `o 19 r 6(3) interest is allowed for the time enforcement has been delayed by the appeal` | 1 | "interest for such time as enforcement has been delayed by the appeal" |
| `o 19 r 7(3) the parties are allowed to make an oral submission at the hearing of the appeal` | 1 | "the parties are allowed to make only such oral submissions as the appellate Court orders" |
| `o 19 r 7(5) the appellate Court's powers to decide the merits are restricted` | 1 | "The appellate Court’s powers to decide the merits of the appeal are not restricted by reason only that there was no appeal against any previous or... |
| `o 19 r 7(6) the appellate Court may order a new trial` | 1 | "The appellate Court may order a new trial only if substantial injustice will be caused otherwise" |
| `o 19 r 7(8) the further evidence is adduced as required` | 1 | "Such further evidence must be adduced in the manner directed by the appellate Court" |
| `o 19 r 8(3) the Court may restore the appeal for rehearing` | 1 | "must show good reason for that party’s absence" |
| `o 19 r 10(1) the notice of withdrawal is filed and served as required` | 1 | "by filing and serving a notice of withdrawal of the appeal or application in Form 34 on all the parties to the appeal or application" |
| `o 19 r 12(2)(b) the parties are informed of what they are to be informed of` | 1 | "the parties are to be informed of the following: (i) the Judge or Judges who constituted the appellate Court; (ii) the decision of the appellate C... |
| `o 19 r 13(2) a court is the lower Court` | 1 | "“lower Court” means the District Court or Magistrate’s Court (as the case may be) against which judgment an appeal is brought or being brought" |
| `o 19 r 14(1) the notice of appeal is filed and served as required` | 1 | "must file and serve on all parties who have an interest in the appeal a notice of appeal in Form 35" |
| `o 19 r 14(2) the General Division may extend the time for filing and serving the notice of appeal` | 1 | "on the appellant’s application made at any time" |
| `o 19 r 15(1) the application for permission to the lower Court is made and served as required` | 2 | "a party must apply for such permission from the lower Court" |
| `o 19 r 15(2) the application for permission to the General Division is made and served as required` | 1 | "must serve the application on all parties who have an interest in the appeal" |
| `o 19 r 15(3) the notice of appeal after permission is filed and served as required` | 1 | "must file and serve on all parties who have an interest in the appeal the notice of appeal in Form 35" |
| `o 19 r 15(4) the General Division may extend the time for filing and serving an application for permission to appeal` | 1 | "on an application made at any time" |
| `o 19 r 16(1) the appellant has provided security for costs and filed the certificate as required` | 1 | "The appellant must provide security for the respondent’s costs of the appeal and file a certificate for security for costs in Form 36 at the time ... |
| `o 19 r 16(4) the security is in a form the text allows` | 2 | "in the form of a solicitor’s undertaking in Form 37 which must be filed and served on the respondent" |
| `o 19 r 16(5) the security is in the amount the text requires` | 1 | "The appellant must provide security in the following amounts: (a) $3,000 for an appeal against a judgment in a Magistrate’s Court action; (b) $5,0... |
| `o 19 r 17(4) the appellant's document is filed and served in time` | 1 | "the appellant’s core bundle of documents, with the written judgment or grounds of decision of the lower Court and the extracted order of the lower... |
| `o 19 r 17(10) the appellant's reply document is filed and served in time` | 1 | "(if any)", "(if necessary)" -- an "if" that is not met (fork F9) |
| `o 19 r 17(15) the parties have tried to agree on a single Case for each party and on the timelines` | 1 | "must try to agree on filing a single Case for each party and on the timelines for such filing" |
| `o 19 r 17(16) the parties have requested a case conference or sought directions` | 1 | "they must request in writing for a case conference before the General Division or seek directions from the General Division" |
| `o 19 r 17(17) the parties have informed the Registrar of the agreed timelines and sought approval` | 1 | "they must inform the Registrar in writing of the timelines agreed, and seek the approval of the timelines by the General Division" |
| `o 19 r 17(18) the parties have filed a joint record of appeal` | 1 | "the parties must file a joint record of appeal" |
| `o 19 r 18(1) the appellant's Case contains what it must contain` | 1 | "The appellant’s Case must contain the following" |
| `o 19 r 18(2) the respondent's Case contains what it must contain` | 1 | "The respondent’s Case must contain the following" |
| `o 19 r 18(4) the appellant's Reply contains what it must contain` | 1 | "The appellant’s Reply (if any) must contain the following" |
| `o 19 r 18(5) the Case or Reply contains everything the party intends to put forward` | 1 | "must contain everything that the parties intend to put forward at the appeal and must be prepared on the basis that there will be no need to suppl... |
| `o 19 r 19(1) the document is within the page limit` | 1 | "are subject to the following page limits ... appellant’s Case — 35 pages; respondent’s Case — 35 pages; appellant’s Reply — 20 pages" |
| `o 19 r 19(2) the document is within the page limit` | 1 | "are subject to the following page limits ... 55 pages; ... 35 pages; ... 25 pages" |
| `o 19 r 20(1) an order from the Court is needed for this Rule to apply` | 1 | "This Rule applies without the need for an order from the Court" |
| `o 19 r 22 the appellant has notified the Registrar of the State Courts of the General Division's judgment or order` | 1 | "The appellant must file a certified copy of the General Division’s judgment or order with the Registrar of the State Courts" |
| `o 19 r 23 the step for enforcement is taken in the right court` | 1 | "The taking of any steps for the enforcement of a judgment or order ... must be in the State Courts" |
| `o 19 r 25(1) the notice of appeal is filed and served as required` | 1 | "must file and serve on all parties who have an interest in the appeal a notice of appeal in Form 35" |
| `o 19 r 25(2) the appellate Court may extend the time for filing and serving the notice of appeal` | 1 | "on the appellant’s application made at any time" |
| `o 19 r 26(1) the application for permission is filed and served as required` | 2 | "a party must apply for such permission from the appellate Court" |
| `o 19 r 26(2) the Judge who made the decision may hear further arguments` | 1 | "before the earliest of the following" |
| `o 19 r 26(3)(b) the application for permission is filed and served as required after further arguments` | 1 | "must file and serve the application for permission to appeal against the decision, and the documents mentioned in paragraph (7)" |
| `o 19 r 26(4) paragraphs (2) and (3) affect section 29B of the Supreme Court of Judicature Act` | 1 | "paragraphs (2) and (3) do not affect section 29B of the Supreme Court of Judicature Act" |
| `o 19 r 26(7)(a) the documents mentioned in paragraph (7) are filed with the application` | 1 | "must, at the time of filing the application, file written submissions and any accompanying bundle of authorities" |
| `o 19 r 26(8) the opposing party's submissions are filed and served as required` | 1 | "must file and serve written submissions and any accompanying bundle of authorities" |
| `o 19 r 26(9) the application and the accompanying documents are served on all parties who have an interest in the appeal` | 1 | "must be served on all parties who have an interest in the appeal" |
| `o 19 r 26(7) the documents mentioned are filed and served with the application` | 1 | "must, at the time of filing the application, file written submissions and any accompanying bundle of authorities" and "must be served on all parti... |
| `o 19 r 26(10) the written submissions are within the page limit and in the form specified` | 2 | "must be in the form specified in any practice directions issued by the Registrar" |
| `o 19 r 26(11) the bundle of documents is within the page limit` | 1 | "The bundle of documents is subject to a page limit of 25 pages" |
| `o 19 r 26(17) the notice of appeal after permission is filed and served as required` | 1 | "must file and serve on all parties who have an interest in the appeal the notice of appeal in Form 35" |
| `o 19 r 27(1) the appellant has provided security for costs and filed the certificate as required` | 1 | "The appellant must provide security for the respondent’s costs of the appeal and file a certificate for security for costs in Form 36 at the time ... |
| `o 19 r 27(4) the security is in a form the text allows` | 2 | "in the form of a solicitor’s undertaking in Form 37 which must be filed and served on the respondent" |
| `o 19 r 27(5) the security is in the amount the text requires` | 1 | "The appellant must provide security in the amount of $20,000" |
| `o 19 r 30(4) the appellant's document is filed and served in time` | 1 | "the appellant’s core bundle of documents, with the written judgment or grounds of decision of the lower Court (if any) and the extracted order of ... |
| `o 19 r 30(5)(a) the supplemental record of appeal comprises what it must` | 1 | "the appellant’s supplemental record of appeal comprising" |
| `o 19 r 30(5) the appellant's document on an appeal from the Appellate Division is filed and served in time` | 1 | "the appellant’s core bundle of documents, with the written judgment or grounds of decision of the lower Court and the extracted order of the lower... |
| `o 19 r 30(11) the appellant's reply document is filed and served in time` | 1 | "(if any)", "(if necessary)" -- an "if" that is not met (fork F9) |
| `o 19 r 30(16) the parties have tried to agree on a single Case for each party and on the timelines` | 1 | "must try to agree on filing a single Case for each party and on the timelines for such filing" |
| `o 19 r 30(17) the parties have requested a case conference or sought directions` | 1 | "they must request in writing for a case conference before the appellate Court or seek directions from the appellate Court" |
| `o 19 r 30(18) the parties have informed the Registrar of the agreed timelines and sought approval` | 1 | "they must inform the Registrar in writing of the timelines agreed, and seek the approval of the timelines by the appellate Court" |
| `o 19 r 30(19) the parties have filed a joint record of appeal` | 1 | "the parties must file a joint record of appeal" |
| `o 19 r 31(1) the appellant's Case contains what it must contain` | 1 | "The appellant’s Case must contain the following" |
| `o 19 r 31(2) the respondent's Case contains what it must contain` | 1 | "The respondent’s Case must contain the following" |
| `o 19 r 31(4) the appellant's Reply contains what it must contain` | 1 | "The appellant’s Reply (if any) must contain the following" |
| `o 19 r 31(5) the Case or Reply contains everything the party intends to put forward` | 1 | "must contain everything that the parties intend to put forward at the appeal and must be prepared on the basis that there will be no need to suppl... |
| `o 19 r 32(1) the document is within the page limit` | 1 | "are subject to the following page limits ... appellant’s Case — 55 pages; respondent’s Case — 55 pages; appellant’s Reply — 25 pages" |
| `o 19 r 32(2) the document is within the page limit` | 1 | "are subject to the following page limits ... 55 pages; ... 35 pages; ... 25 pages" |
| `o 19 r 33(1) an order from the Court is needed for this Rule to apply` | 1 | "This Rule applies without the need for an order from the Court" |
| `o 19 r 35(1) the application to the appellate Court is made in a way the text allows` | 1 | "Every application to the appellate Court must be made either by originating application or, in an appeal which is pending before the appellate Cou... |
| `o 19 r 35(2) the application may be made in the first instance to the appellate Court` | 1 | "Whenever under these Rules an application may be made either to the lower Court or to the appellate Court" |
| `o 19 r 35(4) the affidavit in reply is filed and served as required` | 1 | "file and serve that affidavit on the applicant and the other parties to the application" |
| `o 19 r 35(5) a Case needs to be filed for the application` | 1 | "No Case needs to be filed for applications to the appellate Court" |
| `o 19 r 35(6) the party has provided security for costs and filed the certificate as required` | 1 | "must provide security for the opposing party’s costs of the application and file a certificate for security for costs in Form 36 at the time that ... |
| `o 19 r 35(9) the security is in a form the text allows` | 2 | "in the form of a solicitor’s undertaking in Form 37 which must be filed and served on the respondent" |
| `o 19 r 35(10) the security is in the amount the text requires` | 1 | "The applicant must provide security in the amount of $5,000" |
| `o 19 r 35(13) the application to strike out a notice of appeal is made by summons supported by affidavit` | 1 | "must be made by summons supported by affidavit stating the grounds of the application" |
| `o 19 r 35(14) the summons and the supporting affidavit are filed and served as required` | 1 | "must be filed and served by the applicant on the parties to the application" |
| `o 19 r 35(15) the affidavit in reply to the applicant's affidavit is filed and served as required` | 1 | "must file and serve that party’s affidavit in reply, on the applicant and the other parties to the application" |
| `o 19 r 36 the application for permission is filed and served as required` | 1 | "must be filed and served on all parties who have an interest in the appeal" |
| `o 19 r 37(1) the written submissions and the bundle of authorities are filed and served as required` | 1 | "the applicant and the opposing party must file and serve written submissions (if any) as well as any bundle of authorities" |
| `o 19 r 37(2) the written submissions are within the page limit` | 1 | "subject to a page limit of 35 pages" |
| `o 19 r 37(6) the concluding paragraphs of the written submissions include what they must include` | 1 | "The concluding paragraphs of the written submissions must include" |
| `o 19 r 38(1) the Registrar may exercise the powers of the Appellate Division and the Court of Appeal in sections 40(1)(a) and 58(1)(a) of the Supreme Court of Judicature Act` | 3 | "and all of the parties consent to the making of the direction or order" |
| `o 19 r 38(2) the application to vary or discharge is filed and served as required` | 1 | "must be filed and served on all parties who have an interest in the appeal" |
| `o 19 r 39(1) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on the application` | 1 | "on an application to the Court of Appeal to transfer an appeal that has been made to the Appellate Division, on the ground that it is more appropr... |
| `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` | 1 | "may ... exercise its power under section 29D(1)( a ) of that Act only where" |
| `o 19 r 39(3) the application under section 29D(2)(c)(i) is made, filed and served as required` | 1 | "must be made in accordance with Rule 35, and must be filed and served" |
| `o 19 r 39(4) the application under section 29D(2)(c)(ii) is made, filed and served as required` | 1 | "must be made in accordance with Rule 35, and must be filed and served" |
| `o 19 r 40(1) the Court of Appeal is to have regard to the matter` | 1 | "in deciding whether to exercise the power in section 29E(1) of that Act on its own motion" |
| `o 19 r 40(2) the application under section 29E(2)(b) is made, filed and served as required` | 1 | "must be made in accordance with Rule 35; and must be filed and served" |
| `o 19 r 41(1) the appeal is brought by filing and serving an originating application` | 1 | "must bring the appeal by filing and serving an originating application on all parties who have an interest in the appeal" |
| `o 19 r 41(5) the written submissions are within the page limit` | 1 | "are subject to a page limit of 55 pages" |
| `o 19 r 41(9) the concluding paragraphs of the written submissions include what they must include` | 1 | "The concluding paragraphs of the written submissions must include" |
| `o 19 r 41(11) the provision is one to which the replacement of courts applies` | 3 | "the provisions mentioned in paragraph (10) apply as if" |
| `o 19 r 41(12) the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | "the following provisions do not apply to proceedings before the General Division under section 59G ... (b) Order 20" |
| `o 19 r 41 the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | "the following provisions do not apply to proceedings before the General Division under section 59G" |
| `o 19 r 41(13) a person is the appellant` | 1 | "“appellant” means the party who brings an appeal to the General Division under paragraph (1)" |
| `o 19 r 41(13) a document is a bundle of authorities` | 1 | "“bundle of authorities” means a compilation of authorities for the appeal" |
| `o 19 r 41(13) a body is a Disciplinary Tribunal` | 1 | "“Disciplinary Tribunal” has the meaning given by section 2 of the Medical Registration Act" |
| `o 19 r 41(13) a document is part of the record of proceedings` | 1 | "“record of proceedings” means any written grounds of decision, the record of evidence or notes of arguments taken, the affidavits or statutory dec... |
| `o 19 r 41(13) a person is the respondent` | 1 | "“respondent” means the respondent in the originating application filed under paragraph (1)" |

### NOTHING: A grant or scope limited by its own wording, with no "only" (72 branches)

- Reading taken: NOTHING outside the limit (ruling of 2026-11-05 (c)).
- The other reading: JUST FALSE: read the limit as "only these".

| function | branches | first reason |
| --- | --- | --- |
| `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` | 1 | paragraph (a) speaks only of "an appeal against any judgment of a Magistrate's Court or District Court" |
| `o 19 r 1(b) this Order applies to an appeal against a judgment of the General Division` | 2 | paragraph (b) speaks only of a judgment of the General Division |
| `o 19 r 1(c) this Order applies to an appeal against a judgment of the Appellate Division` | 2 | paragraph (c) speaks only of a judgment of the Appellate Division |
| `o 19 r 1(d) this Order applies to an appeal from a tribunal to the Appellate Division or the Court of Appeal` | 2 | paragraph (d) speaks only of an appeal "to the Appellate Division or the Court of Appeal pursuant to any written law" |
| `o 19 r 1(e) this Order applies to an application to the appellate Court relating to an appeal` | 2 | paragraph (e) speaks only of an application "relating to an appeal mentioned in paragraph (a), (b), (c) or (d)" |
| `o 19 r 1(f) this Order applies to an appeal against an order or decision of a Disciplinary Tribunal` | 1 | paragraph (f) speaks only of "an order or decision of a Disciplinary Tribunal under the Medical Registration Act" |
| `o 19 r 5(1) a person may apply to intervene in the appeal with the permission of the appellate Court` | 1 | paragraph (1) speaks only of "A person who is not a party in the appeal" |
| `o 19 r 7(1) the appellate Court may order a party to serve a document on a non-party to the appeal` | 1 | paragraph (1) speaks only of service "on a non-party to the appeal" |
| `o 19 r 7(1) the appellate Court may give directions for the non-party to state its case` | 1 | paragraph (1) speaks only of directions "for the non-party to state its case by affidavit, written submissions or any other means" |
| `o 19 r 7(2) the appellate Court may allow or invite a non-party to give its views on any matter in the appeal` | 1 | paragraph (2) speaks only of "any non-party to the appeal" |
| `o 19 r 7(2) the appellate Court may make a costs order in relation to a non-party` | 1 | paragraph (2) speaks only of costs orders "in relation to the non-party" |
| `o 19 r 7(4) the appellate Court may make an order although that part is not the subject of any appeal and the reason is not stated by anyone` | 1 | paragraph (4) speaks only of an order "relating to any part of the decision of the lower Court" |
| `o 19 r 7(7) further evidence may be given` | 1 | the bar excepts "evidence relating to matters occurring after the date of the decision appealed against"; the paragraph says nothing more about it |
| `o 19 r 9(2) the lower Court or the appellate Court may dispense with or modify a provision for the purposes of the appeal` | 1 | paragraph (2) speaks only of "an expedited appeal" |
| `o 19 r 11(2) the appellate Court may give a further order or direction` | 1 | paragraph (2) speaks only of orders or directions "incidental or consequential to any judgment or order" |
| `o 19 r 12(3) a party is entitled to a copy of the decision` | 1 | paragraph (3) speaks only of "any decision given in writing" |
| `o 19 r 12(4) the judgment may be delivered orally despite the absence of one or more of the other Judges` | 1 | paragraph (4) speaks only of delivery "orally by any Judge sitting in the appellate Court" |
| `o 19 r 16(5) the amount of security the appellant must provide` | 1 | paragraph (5) gives amounts for a Magistrate's Court action and a District Court action only as to those two courts |
| `o 19 r 16(5) the security is in the amount the text requires` | 1 | paragraph (5) names only the Magistrate's Court and the District Court |
| `o 19 r 16(6) a party may apply to the appellate Court to vary or waive the amount of security` | 1 | paragraph (6) speaks only of "Any party" |
| `o 19 r 16(7) the appellate Court may order further security for costs to be given` | 1 | paragraph (7) gives the power to order "further security for costs" |
| `o 19 r 17(13) a party with a passive interest is required to file a separate Case` | 1 | paragraph (13) speaks only of "A party whose interest in the appeal is passive" |
| `o 19 r 17(13) the passive party has ensured that its position is explained in one of the Cases` | 1 | paragraph (13) speaks only of "A party whose interest in the appeal is passive" |
| `o 19 r 17(15) the parties have tried to agree on a single Case for each party and on the timelines` | 1 | paragraph (15) speaks only of "All parties to 2 or more appeals to be heard together" |
| `o 19 r 19(3)(a) the General Division may allow the page limit to be exceeded` | 1 | the power is given "in special circumstances" |
| `o 19 r 21 further arguments from the parties are allowed` | 1 | the bar runs "after the General Division has heard the appeal and reserved its decision or after the General Division has given its decision" |
| `o 19 r 23 the step for enforcement is taken in the right court` | 1 | rule 23 speaks only of "a judgment or order which has been the subject matter of an appeal under this Division" |
| `o 19 r 26(1) the application for permission is filed and served as required` | 1 | "subject to paragraphs (2), (3) and (4)" -- paragraph (3)(b) fixes the time after further arguments |
| `o 19 r 26(7)(b) the applicant may file a bundle of documents with the application` | 1 | the applicant "may" file it; the text does not say what follows if it does not |
| `o 19 r 26(8) the opposing party's submissions are filed and served as required` | 1 | paragraph (8) speaks only of "A party who wishes to oppose an application for permission" |
| `o 19 r 26(8)(b) the opposing party may file and serve a bundle of documents with its submissions` | 1 | the party "may" file it; the text does not say what follows if it does not |
| `o 19 r 26(12)(a) the appellate Court may allow the page limit for the written submissions to be exceeded` | 1 | the power is given "in special circumstances" |
| `o 19 r 26(18) the appellate Court may extend the time for filing and serving an application for permission to appeal` | 1 | paragraph (18) gives the power to "extend the time for filing and serving an application for permission to appeal" |
| `o 19 r 27(6) a party may apply to the appellate Court to vary or waive the amount of security` | 1 | paragraph (6) speaks only of "Any party" |
| `o 19 r 27(7) the appellate Court may order further security for costs to be given` | 1 | paragraph (7) gives the power to order "further security for costs" |
| `o 19 r 28(3) the appellate Court may give directions under paragraph (1) even if the related appeals are of both kinds` | 1 | paragraph (3) speaks only of the case where the related appeals are of both kinds; paragraph (1) covers the rest |
| `o 19 r 30(14) a party with a passive interest is required to file a separate Case` | 1 | paragraph (14) speaks only of "A party whose interest in the appeal is passive" |
| `o 19 r 30(14) the passive party has ensured that its position is explained in one of the Cases` | 1 | paragraph (14) speaks only of "A party whose interest in the appeal is passive" |
| `o 19 r 30(16) the parties have tried to agree on a single Case for each party and on the timelines` | 1 | paragraph (16) speaks only of "All parties to 2 or more related appeals to be heard together" |
| `o 19 r 32(3)(a) the appellate Court may allow the page limit to be exceeded` | 1 | the power is given "in special circumstances" |
| `o 19 r 33(4) paragraphs (2) and (3) apply, with necessary modifications, to the payment out of the security` | 1 | paragraph (4) speaks only of "security for costs given under Rule 35(6)"; security under Rule 27 is paragraphs (2) and (3) themselves |
| `o 19 r 34 further arguments from the parties are allowed` | 1 | the bar runs "after the appellate Court has heard the appeal and reserved its decision or after the appellate Court has given its decision in the a... |
| `o 19 r 35(4) the affidavit in reply is filed and served as required` | 1 | paragraph (4) speaks only of a party who "wishes to file an affidavit in reply" |
| `o 19 r 35(5) a Case needs to be filed for the application` | 1 | paragraph (5) speaks only of "applications to the appellate Court" |
| `o 19 r 35(6) the party has provided security for costs and filed the certificate as required` | 1 | paragraph (6) speaks only of "The party who files an originating application or a summons to the appellate Court" |
| `o 19 r 35(11) a party may apply to the appellate Court to vary or waive the amount of security` | 1 | paragraph (11) speaks only of "Any party" |
| `o 19 r 35(12) the appellate Court may order further security for costs to be given` | 1 | paragraph (12) gives the power to order "further security for costs" |
| `o 19 r 35(13) the application to strike out a notice of appeal is made by summons supported by affidavit` | 1 | paragraph (13) speaks only of "Any application to the appellate Court to strike out a notice of appeal" |
| `o 19 r 35(15) the affidavit in reply to the applicant's affidavit is filed and served as required` | 1 | paragraph (15) speaks only of a party "who wishes to reply to the applicant’s affidavit" |
| `o 19 r 36 the application for permission is filed and served as required` | 1 | rule 36 speaks only of an application for permission under section 40(4)(b) or 58(4)(b) |
| `o 19 r 37(3)(a) the appellate Court may allow the page limit to be exceeded` | 1 | the power is given "in special circumstances" |
| `o 19 r 38(2) an application to vary or discharge may be made to a single Judge sitting in the Appellate Division or the Court of Appeal` | 1 | paragraph (2) speaks only of "any direction or order of the Registrar under paragraph (1)" |
| `o 19 r 38(2) the application to vary or discharge is filed and served as required` | 1 | paragraph (2) speaks only of an application "to vary or discharge any direction or order of the Registrar under paragraph (1)" |
| `o 19 r 38(2) the decision of that Judge is final` | 1 | paragraph (2) says only that "the decision of that Judge is final" |
| `o 19 r 39(2) the Court of Appeal may exercise its power under section 29D(1)(a) of the Supreme Court of Judicature Act on its own motion or on a reference` | 1 | paragraph (2) speaks only of the Court of Appeal acting "on its own motion or on a reference by the Appellate Division" |
| `o 19 r 39(3) the application under section 29D(2)(c)(i) is made, filed and served as required` | 1 | paragraph (3) speaks only of "An application under section 29D(2)( c )(i)" |
| `o 19 r 39(4) the application under section 29D(2)(c)(ii) is made, filed and served as required` | 1 | paragraph (4) speaks only of "An application under section 29D(2)( c )(ii)" |
| `o 19 r 39(5) the Court of Appeal may have regard to the matter` | 1 | "any other relevant matter" -- this matter is not relevant, and the text says nothing of an irrelevant one |
| `o 19 r 40(2) the application under section 29E(2)(b) is made, filed and served as required` | 1 | paragraph (2) speaks only of "An application under section 29E(2)( b )" |
| `o 19 r 41(1) the appeal is brought by filing and serving an originating application` | 1 | paragraph (1) speaks only of "A person who intends to appeal to the General Division under section 59G of the Medical Registration Act against a de... |
| `o 19 r 41(6)(a) the General Division may allow the page limit to be exceeded` | 1 | the power is given "in special circumstances" |
| `o 19 r 41(10) the provision applies to proceedings under section 59G of the Medical Registration Act` | 2 | paragraph (10) does not list it; its exclusion is paragraph (12), which has its own function |
| `o 19 r 41(10)(c) the reference in Rule 10 is to be disregarded` | 1 | paragraph (10)(c) disregards only "the references to security for costs in Rule 10(2) and (4)( b )(ii)" and says nothing of the rest |
| `o 19 r 41(11) the provision is one to which the replacement of courts applies` | 1 | paragraph (11) speaks of "the provisions mentioned in paragraph (10)", and Rule 1(f) is not among them |
| `o 19 r 41(11) the court or body that the reference is read as` | 2 | "For the purposes of an appeal under section 59G of the Medical Registration Act" |
| `o 19 r 41(12) the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | paragraph (12) says only that Division 1 (with its exceptions) and Order 20 do not apply, and says nothing of this provision |

### NOTHING: A provision that hands the answer to something outside the text (an order, a direction, "any written law", another Act) (37 branches)

- Reading taken: NOTHING (and the outside fact is a named input).
- The other reading: JUST FALSE for the provision on its own, treating the outside source as silent.

| function | branches | first reason |
| --- | --- | --- |
| `o 19 r 4 the date after which the time for the filing starts to run` | 1 | "Subject to any written law", "unless the Court otherwise orders" -- what the law or the order says is not in these sources; paragraph (1A) is not ... |
| `o 19 r 4(1) the time for the filing cannot yet start to run` | 1 | "Subject to any written law" |
| `o 19 r 6(1) the appeal operates as a stay of enforcement or of proceedings under the decision of the lower Court` | 1 | "Except so far as the lower Court or the appellate Court may otherwise direct" -- what the direction says is not in these sources |
| `o 19 r 6(2) an intermediate act or proceeding is invalidated by the appeal` | 1 | "Except so far as the appellate Court may otherwise direct" -- what the direction says is not in these sources |
| `o 19 r 7(7) the appellate Court has power to receive further evidence` | 1 | "Subject to any written law" -- the written law is not in these sources |
| `o 19 r 10(3)(b) oral arguments may be made in the request` | 1 | "unless the appellate Court otherwise directs" -- what the direction allows is not in these sources |
| `o 19 r 17(7)(b) oral arguments may be made in the request` | 1 | "unless the appellate Court otherwise directs" -- what the direction allows is not in these sources |
| `o 19 r 17(19) a document other than those set out in this Rule may be filed` | 1 | "unless the General Division otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 17(20) written submissions or skeletal arguments may be filed before or at the appeal` | 1 | "unless the General Division otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 19(1) the document is within the page limit` | 1 | "unless the General Division otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 19(2) the document is within the page limit` | 1 | "unless the General Division otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 19(3)(b) the amount payable for the pages in excess` | 1 | the fees are not payable here, or have been waived, refunded, deferred or apportioned, and the amount then is not in these sources |
| `o 19 r 21 further arguments from the parties are allowed` | 1 | "Unless the General Division otherwise directs" -- what the direction allows is not in these sources |
| `o 19 r 24(e) this Division applies to the tribunal appeal without modification` | 1 | "subject to such modifications as may be directed by the appellate Court" -- the direction is not in these sources |
| `o 19 r 25(1) the date after which the 28 days for the notice of appeal run` | 1 | the date is in section 29B(4)(b) of the Supreme Court of Judicature Act |
| `o 19 r 26(1) the application for permission is filed and served as required` | 1 | "and any written law" |
| `o 19 r 26(10) the written submissions are within the page limit and in the form specified` | 1 | "unless the appellate Court otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 26(12)(b) the amount payable for the pages in excess` | 1 | the fees are not payable here, or have been waived, refunded, deferred or apportioned, and the amount then is not in these sources |
| `o 19 r 26(14) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 26(16) oral arguments may be made in an application for permission to appeal` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 30(8)(b) oral arguments may be made in the request` | 1 | "unless the appellate Court otherwise directs" -- what the direction allows is not in these sources |
| `o 19 r 30(20) a document other than those set out in this Rule may be filed` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 30(21) written submissions or skeletal arguments may be filed before or at the appeal` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 32(1) the document is within the page limit` | 1 | "unless the appellate Court otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 32(2) the document is within the page limit` | 1 | "unless the appellate Court otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 32(3)(b) the amount payable for the pages in excess` | 1 | the fees are not payable here, or have been waived, refunded, deferred or apportioned, and the amount then is not in these sources |
| `o 19 r 34 further arguments from the parties are allowed` | 1 | "Unless the appellate Court otherwise directs" -- what the direction allows is not in these sources |
| `o 19 r 35(3) oral arguments may be made in an application to the appellate Court` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 37(1) the written submissions and the bundle of authorities are filed and served as required` | 2 | "Except where otherwise provided by any provision of these Rules or any other written law" -- the other provision is not named |
| `o 19 r 37(2) the written submissions are within the page limit` | 1 | "unless the appellate Court otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 37(3)(b) the amount payable for the pages in excess` | 1 | the fees are not payable here, or have been waived, refunded, deferred or apportioned, and the amount then is not in these sources |
| `o 19 r 37(5) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "unless the appellate Court otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 41(5) the written submissions are within the page limit` | 1 | "unless the General Division otherwise orders" -- the order's limit is not in these sources |
| `o 19 r 41(6)(b) the amount payable for the pages in excess` | 1 | the fees are not payable here, or have been waived, refunded, deferred or apportioned, and the amount then is not in these sources |
| `o 19 r 41(8) more than one set of submissions may be filed for a party or a set of parties represented by the same firm of solicitors` | 1 | "unless the General Division otherwise orders" -- what the order allows is not in these sources |
| `o 19 r 41(10) listed provision applies` | 1 | "Subject to this Rule and any other written law" -- the other provision is not named |

### NOTHING: The text is silent on the case asked (28 branches)

- Reading taken: NOTHING.
- The other reading: JUST FALSE: read silence as "not provided".

| function | branches | first reason |
| --- | --- | --- |
| `o 19 r 2(1) this Order yields to a written law on the right to appeal or on permission to appeal` | 1 | paragraph (1) says what this Order yields to; it does not say what follows when no such written law applies |
| `o 19 r 4(1) the date after which the time for the filing starts to run` | 1 | when the date is not yet known there is no start date to give |
| `o 19 r 4(1A) this paragraph applies` | 1 | the 30 days have not run out and costs are not yet determined, so the text does not yet say that the issue of costs was not determined within them |
| `o 19 r 4(1A) the date after which the time for the filing starts to run` | 1 | the paragraph does not apply, or not yet: there is no date to give |
| `o 19 r 4(1) the time for the filing has started to run` | 1 | the bar does not hold and (1A) does not start time, so the paragraphs do not say that it has started; a written law or an order may displace paragr... |
| `o 19 r 7(5) the appellate Court's powers to decide the merits are restricted` | 1 | the paragraph says nothing of a restriction for any other reason |
| `o 19 r 16(3) the number of sets of security the appellant must provide` | 1 | paragraph (3) speaks of "more than one respondent"; with one, paragraph (1) gives security for the respondent's costs |
| `o 19 r 17(3) no written grounds of decision are issued within 12 weeks` | 1 | the 12 weeks have not run out and no grounds are issued yet |
| `o 19 r 17(13) the passive party has ensured that its position is explained in one of the Cases` | 1 | the text says the party "should ensure" this and names no consequence |
| `o 19 r 20(2) the amount of the security paid to the respondent` | 2 | no costs are payable, so paragraph (3) applies |
| `o 19 r 20(2) the balance of the security paid to the appellant` | 1 | no costs are payable, so paragraph (3) applies |
| `o 19 r 26(3)(a) the application for permission to appeal may be filed against the decision` | 1 | paragraph (3)(a) says only when an application may NOT yet be filed; the time to file is paragraph (3)(b) |
| `o 19 r 26(3)(b) the date after which the 14 days for the application run` | 1 | the two events are alternatives (i) and (ii) and the text does not say which counts when both are given |
| `o 19 r 26(15) an affidavit may be filed in an application for permission to appeal` | 1 | the paragraph bars an affidavit "without the permission of the appellate Court" and does not say what follows when permission is given |
| `o 19 r 27(3) the number of sets of security the appellant must provide` | 1 | paragraph (3) speaks of "more than one respondent"; with one, paragraph (1) gives security for the respondent's costs |
| `o 19 r 29(3) the appellate Court may make an order or give a direction under this Rule` | 1 | "To avoid doubt" the Court may act on its own motion; the text does not say what else may set it going |
| `o 19 r 30(3) no written grounds of decision are issued within 12 weeks` | 1 | the 12 weeks have not run out and no grounds are issued yet |
| `o 19 r 30(14) the passive party has ensured that its position is explained in one of the Cases` | 1 | the text says the party "should ensure" this and names no consequence |
| `o 19 r 33(2) the amount of the security paid to the respondent` | 2 | no costs are payable, so paragraph (3) applies |
| `o 19 r 33(2) the balance of the security paid to the appellant` | 1 | no costs are payable, so paragraph (3) applies |
| `o 19 r 35(4) a further affidavit may be filed` | 1 | the paragraph bars further affidavits "without permission of the appellate Court" and does not say what follows when permission is given |
| `o 19 r 35(8) the number of sets of security the applicant must provide` | 1 | paragraph (8) speaks of "more than one opposing party"; with one, paragraph (6) gives security for the opposing party's costs |
| `o 19 r 35(16) a further affidavit may be received in evidence` | 1 | the paragraph bars a further affidavit "without the permission of the appellate Court" and does not say what follows when permission is given |
| `o 19 r 41(4) an affidavit may be filed in an appeal brought under paragraph (1)` | 1 | the paragraph bars an affidavit "without the permission of the General Division" and does not say what follows when permission is given |
| `o 19 r 41(10) the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | paragraph (10) does not list Rule 1(f), and paragraph (12)(a) only declines to exclude it |
| `o 19 r 41 the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | neither paragraph (10) nor paragraph (12) answers for this provision |

### NOTHING: A list with no "only" or "means", so it stays open (20 branches)

- Reading taken: NOTHING for an item not named.
- The other reading: JUST FALSE: read the list as closed.

| function | branches | first reason |
| --- | --- | --- |
| `o 19 r 1(a) this Order applies to an appeal against a judgment of a Magistrate's Court or District Court` | 1 | paragraph (a) names three kinds of judgment of those courts; a judgment of another kind is not mentioned |
| `o 19 r 1 this Order applies` | 1 | rule 1 lists six kinds of matter and does not say "only" |
| `o 19 r 2(2) Division 2 concerns the appeal from the District Court or the Magistrate's Court to the General Division` | 1 | "Division 2 of this Order concerns appeals from the District Court or the Magistrate’s Court to the General Division" does not say Division 2 conce... |
| `o 19 r 2(3)(a) Division 3 concerns the appeal from the General Division to the Appellate Division or the Court of Appeal` | 1 | paragraph (3)(a) does not say Division 3 concerns only these appeals |
| `o 19 r 2(3)(b) Division 3 concerns the appeal from a tribunal to the Appellate Division or the Court of Appeal` | 1 | paragraph (3)(b) does not say Division 3 concerns only these appeals |
| `o 19 r 2(3)(c) Division 3 concerns the appeal from the Appellate Division to the Court of Appeal` | 1 | paragraph (3)(c) does not say Division 3 concerns only these appeals |
| `o 19 r 2(4) Division 4 concerns the appeal to the General Division from a Disciplinary Tribunal under the Medical Registration Act` | 1 | paragraph (4) does not say Division 4 concerns only these appeals |
| `o 19 r 2 the Division that concerns the appeal` | 1 | paragraphs (2) to (4) name three routes and say "concerns", not "only" |
| `o 19 r 12(1) the appellate Court may give its decision in this way` | 1 | paragraph (1) names two ways, orally and in writing, each at the conclusion of the hearing or at a subsequent date, and does not say "only" |
| `o 19 r 13(1) this Division applies to an appeal against a judgment of the District Court or Magistrate's Court` | 1 | paragraph (1) names three kinds of judgment of the District Court or Magistrate's Court and does not say "only" |
| `o 19 r 24(a) this Division applies to an appeal to the Appellate Division against a judgment of the General Division` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 24(b) this Division applies to an appeal to the Court of Appeal against a judgment of the General Division` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 24(c) this Division applies to an appeal to the Court of Appeal against a judgment of the Appellate Division` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 24(d) this Division applies to an application to the Appellate Division or the Court of Appeal relating to an appeal` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 24(e) this Division applies to an appeal from a tribunal to the Appellate Division or the Court of Appeal` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 24 this Division applies` | 1 | rule 24 lists five kinds and does not say "only" |
| `o 19 r 28(2) the directions in paragraph (1) may be given in this way` | 1 | paragraph (2) names two ways and does not say "only" |
| `o 19 r 38(1) the Registrar may exercise the powers of the Appellate Division and the Court of Appeal in sections 40(1)(a) and 58(1)(a) of the Supreme Court of Judicature Act` | 1 | rule 38(1) lists six circumstances and does not say "only" |
| `o 19 r 40(1) the Court of Appeal is to have regard to the matter` | 1 | rule 40(1) lists three matters and does not say "only" |
| `o 19 r 41(10) the provision applies to proceedings under section 59G of the Medical Registration Act` | 1 | paragraph (10) lists provisions and does not say "only" |

### NOTHING: A definition that "includes" and so stays open (4 branches)

- Reading taken: NOTHING for an item not named.
- The other reading: JUST FALSE: read "includes" as "means".

| function | branches | first reason |
| --- | --- | --- |
| `o 19 r 3 an item may be in a bundle of authorities` | 1 | "including case authorities, statutes and law journal articles" does not close the list |
| `o 19 r 5(4) the condition of security for costs may be imposed on an intervening party` | 1 | "including ordering the intervening party to provide security for costs" names one condition and does not close the list |
| `o 19 r 26(5)(b) the Court of Appeal may have regard to the matter` | 1 | "including either or both of the following" names two matters and does not close the list |
| `o 19 r 41(13) an item may be in a bundle of authorities` | 1 | "including case authorities, statutes and law journal articles" does not close the list |

### Reading a result: FALSE and NOTHING (roc4)

A function in this row answers a question about one provision of Order 19, and every function that decides a proposition answers `JUST TRUE`, `JUST FALSE` or `NOTHING`.

- `JUST TRUE` means the text says yes on these facts: the act was in time, the requirement is met, the power is given.
- `JUST FALSE` means the text says no in its own words on these facts, and the comment `FALSE-kind` beside the branch quotes the words.
  In this row a "no" is one of five things: a stated period the act is outside, a "where/when/upon/if/after/in the case of" that is not met, an "Except" or "unless" that flips exactly the proposition asked, a flat negative ("is not allowed", "must not", "there are to be no"), or a requirement or definition that the facts do not meet.
  It never means "the Court would refuse": it means "this provision does not give the person what was asked about on these facts".
  A person who gets `JUST FALSE` on "is the notice of appeal filed and served as required?" has learned that this rule, on those dates, is not satisfied; whether the Court will extend time (rules 14(2), 25(2)) is a separate question that the extension rules answer.
- `NOTHING` means the text does not answer, and the comment `NOTHING-kind` beside the branch says why: the text is silent, a list is not closed, a definition "includes", a term is undefined, the answer is handed to something outside the text (an order, a direction, a written law, another Act), or the provision is limited by its own wording.
  A caller must never turn `NOTHING` into `FALSE`.
  It means "go and look at the thing the text points to", not "no".

One `NOTHING` is not a reading of the text.
The seat helpers `o 19 seat the date if it happened`, `o 19 seat the costs ordered if any` and `o 19 seat the moment if it happened` turn a person's yes or no and a number into a `MAYBE`, and their `NOTHING` means "the person did not say"; it carries the comment `input mapping` and not a `NOTHING-kind`.

The regulative rules in `roc4-order-19-duties.l4` end in `FULFILLED` or `BREACH`.
A `BREACH` there is the only failure state a regulative rule has on main; where the text's consequence of missing a time is not a wrong (an appeal deemed withdrawn, a respondent barred), the `BECAUSE` says so in the words of the text.

## Seams (roc4)

A seam is an answer that lives in another part's range or outside the sources, taken as an input.
One line each: asking section, answering section, input name, type.

| id | asking section | answering section | input name | type |
| --- | --- | --- | --- | --- |
| S-T1 | every rule with a period in this Order | O 3 r 3 (roc1): the count | `o 3 r 3 the last day for doing the act` | `DATE` |
| S-T2 | every rule that decides whether an act was in time | O 3 r 4 (roc1): extension or shortening | `o 3 r 4 the last day as extended or shortened` | `MAYBE DATE` (`NOTHING` = not extended) |
| S-V3 | rules 19(3)(b), 26(12)(b), 32(3)(b), 37(3)(b), 41(6)(b): the fee for pages in excess is payable | the Fourth Schedule item (roc12) | `sch 4 the fee for this document` | `NUMBER` |
| O 1 r 2(4)(c) | O 1 r 2(4)(c) (keel) asks this Order | O 19 r 26(7) with (9): this row answers | `o 19 r 26(7) the documents mentioned are filed and served with the application` (the keel's input is `o 18 r 29(7) or o 19 r 26(7) the documents mentioned are filed and served with it`) | `MAYBE BOOLEAN` |
| keel | rule 8(1), (2) ask whether a person attends the hearing | `roc-definitions.l4`, `o 1 r 3(1) a person attends` | `the appellant attends the appeal` and the like, each a plain `BOOLEAN` | not called: asked as a fact about the hearing (comment at `roc4-order-19-div-1.l4:796`) |
| outside the sources | rules 25, 26, 36, 38, 39, 40 and 41 | the Supreme Court of Judicature Act and the Medical Registration Act | one named `BOOLEAN` or `MAYBE DATE` per fact, named for the section (for example `section 29B(4)(b) of the Supreme Court of Judicature Act the date mentioned`) | as named |

**This part computes none of its deadlines under O 3 r 3.**
Every function that decides whether an act was in time takes `o 3 r 3 the last day for doing the act` (S-T1) as an input, most of them also take `o 3 r 4 the last day as extended or shortened` (S-T2), and they compare the date of the act with the last day, most of them through the helper `o 19 r 8(3) the act is done by the last day` in this row.
Those functions are, by rule: 8(3), 14(1), 15(1), 15(2), 15(3), 17(3), 17(4), 17(7)(a), 17(8), 17(10), 25(1), 26(1), 26(3)(b), 26(6), 26(8), 26(17), 30(3), 30(4), 30(5), 30(8)(a), 30(9), 30(11), 35(4), 35(14), 35(15), 36, 37(1), 38(2), 39(3), 39(4), 40(2), 41(2) and 41(3).
The regulative rules in `roc4-order-19-duties.l4` state each period as a `WITHIN` clause of the length in the text and run it from the event that starts it in trace time; they do not count calendar days either.
Two dates are worked out here by plain calendar arithmetic and not under O 3 r 3: the end of the 30 days in rule 4(1A) (fork F3) and the 15th day in rule 26(2) (fork F5).

**Period audit (2026-11-05).** Every function that tests a time against a period, deadline or window the text states was read, and each answers one of two ways.
52 functions answer `JUST TRUE` inside the period and `JUST FALSE` outside it, and every one has a test on both sides: 36 compare a date or a moment with the last day or with a moment (the 32 "filed and served in time" and like functions of rules 8(3), 14(1), 15(1)-(3), 17(4), 17(7)(a), 17(8), 17(10), 25(1), 26(1), 26(2), 26(3)(b), 26(6), 26(8), 26(17), 30(4), 30(5), 30(8)(a), 30(9), 30(11), 35(4), 35(14), 35(15), 36, 37(1), 38(2), 39(3), 39(4), 40(2), 41(2) and 41(3), plus the 12-week functions of rules 17(3) and 30(3), the 30-day function of rule 4(1A) and the bar function of rule 4(1)), and 16 take a yes/no input that stands for "inside the period" (rules 8(3) "may restore", 10(1), 14(2), 15(4) and 25(2) "before the time expires", 17(3)(a)-(c), 30(3)(a)-(c), 17(5), 17(9), 30(6), 30(10) and 26(3)(a) "cannot yet be filed").
None answers `NOTHING` outside a period the text fixes, so none was changed: 0 functions changed.
Three of the 52 answer `NOTHING` inside their window while the event is still undetermined (rules 17(3), 30(3) and 4(1A): the days have not run out and nothing has happened yet), which is not an answer outside a period.
Four functions stay `NOTHING` outside a bar on purpose, with `JUST FALSE` as the other reading (fork F13): rule 4(1) "has started to run", rule 26(3)(a) "may be filed", and rules 21 and 34 "further arguments are allowed"; the "subject to" branch of rule 26(1) is the same shape.
The date and moment functions (rule 4(1A) and rule 4 date, rule 26(2)(b) moment, rule 26(3)(b) date) cannot carry `JUST FALSE`; each has a yes/no twin that does.
One side of the window is the early one: an act done before the period begins counts as in time (fork F12).

**"The duty does not arise" is answered by the function that states the duty, with `JUST FALSE`.**
No compliance function answers `JUST TRUE` for a duty whose trigger is not met, and no companion function "the duty arises" was written.
For example `o 19 r 15(1) the application for permission to the lower Court is made and served as required` answers `JUST FALSE` where permission is not required ("Where permission to appeal is required" is a "where" that is not met), and `o 19 r 16(3) the appellant must provide security for each respondent or each set of respondents` answers `JUST FALSE` with one respondent.
The regulative rules in `roc4-order-19-duties.l4` are the other way round: where the trigger is not met they end in `FULFILLED`, because a rule that does not bite has nothing to say (the guard of rule 17(10) and the four bars on the respondent).

Not threaded, and why:

- S-L2 (an override that switches another provision off): O 1 r 2(5)(a) says paragraphs (1) to (4) of rule 26 do not apply to an application for permission mentioned in O 1 r 2(4)(c), and O 1 r 2(5)(b) reads "the time provided under this Rule" in rule 26(6)(a) as that rule's time.
  The overriding section is in the keel; PLAN.md section 5 (S-L2) says the overridden part does not thread an input for it, and rule 26 does not.
- S-F1 and S-S1 (when a document is deemed filed; the day service is deemed effected): PLAN.md names them `o 28 r 10 the moment the document is deemed filed` (`Moment`) and `o 7 r 8 the day service is deemed effected` (`DATE`).
  This row asks `the date the document is filed` and `the date the document is served` (both `DATE`), because every period in this Order is counted in days and compared with the last day.
  The service input has the type S-S1 gives; the filing input is a `DATE` where S-F1 gives a `Moment`, so wiring S-F1 into this row takes the day of the moment (a seam the plan lacks: the type differs).
  Rule 26(2) is the one place this row uses `Moment` (fork F5).
- `o 1 r 3(1) a defined term has its defined meaning` (the keel's rule for "unless the context otherwise requires"): not threaded, as PLAN.md section 7, item 9 says of every part (comment at `roc4-order-19-div-1.l4:313`).

## Dependencies

Copied nothing, needed nothing.
O 3 r 3(1) says "The Interpretation Act does not apply to the calculation of time in these Rules" (text line 324), so no staged Interpretation Act module is used; the periods of this Order are counted by O 3 r 3, which is another part's range and arrives here as the seam S-T1.
Section references to the Supreme Court of Judicature Act and the Medical Registration Act are taken as named inputs (Seams, last row), because those Acts are not among the sources.

## Unstable dialect

I looked at time (every period runs from an event and is counted by O 3 r 3, in roc1's range), at rule versions (13 amendment marks in the range, 11 of `S 37/2024 wef 01/02/2024` and 2 of `S 206/2022 wef 01/04/2022`, but the text shows only the current wording and not the earlier one, so there is nothing to version) and at workarounds on main (a deontic cannot be asserted, and a `LEST` after a `MAY` is ignored; both are dialect rows, not shapes in the text), and found no shape that earns a second encoding; I wrote none.

## What the text turns out to say (roc4)

Numbered findings from reading and encoding Order 19.
Each one was checked against the text at the line given, on 2026-11-05.

1. **The rendering has stray punctuation and line breaks.** Line 2289, rule 4(2)(a)(iv), ends "...each party is to bear its own costs.; and", with a full stop before the semicolon.
   The converter also puts list markers at the end of the line above their text ("( a )" after a dash) and amendment notes in the running text ("[S 37/2024 wef 01/02/2024]").
   None of it changes the sense; every quotation in this row is a mechanical copy of the rendering, so it carries these too.
2. **Rules 17 and 30 are the same sequence with different numbers, and differ in three places.**
   The appellant has 28 days in rule 17(4) and 8 weeks in rule 30(4) and (5), both from the day the Registry informs the parties that the record of proceedings is available.
   Rule 30(4)(c) adds "(if any)" after "the written judgment or grounds of decision of the lower Court"; rule 17(4)(c) does not.
   Rule 30(5) adds the route from the Appellate Division to the Court of Appeal, with a supplemental record of appeal.
   The respondent's 28 days (rules 17(8), 30(9)) and the appellant's Reply 14 days (rules 17(10), 30(11)) are the same.
3. **"Within the specified time" names no time.** Rules 17(5), 17(9), 30(6) and 30(10) use the phrase; the time is the one in the paragraph that imposes the duty.
   This row reads it so (marginal reading 2).
4. **Rule 8(3) has two starting events and one "must".** The 14 days run "after the dismissal or hearing of the appeal", and the absent party "must file and serve any such application" and "must show good reason".
   This row reads the first "must" as the manner of applying and the second as a condition of the Court's power, so the regulative rule is a `MAY` with a 14-day window, not a duty to apply.
5. **Rule 26(2) sets two moments beside one day** (fork F5): "the time at which the judgment or order ... is extracted", "the 15th day after the date on which the decision is made", "the time at which an application for permission to appeal against the decision is filed".
6. **Rule 41(12)(a) stops its exception at paragraph (10)(e) because (10)(f) to (h) are in Division 3.** Rule 41(10) lists Rules 7, 8, 10, 11 and 12 (Division 1, rules 1-12) at (a) to (e), and Rules 34, 35 and 37 (Division 3, rules 24-40) at (f) to (h); paragraph (12)(a) disapplies Division 1 "except Rule 1(f) and the provisions mentioned in paragraph (10)(a) to (e)", and says nothing about Division 3.
7. **Rule 41(10) has no "only".** It lists eight provisions that apply "subject to this Rule and any other written law", and rule 41(12) lists two that do not "to avoid doubt"; every other provision of the Order is neither (fork F7).
8. **The amounts and page limits are in the text, and differ by court.**
   Security for costs: $3,000 (Magistrate's Court action) and $5,000 (District Court action) in rule 16(5); $20,000 in rule 27(5); $5,000 for an application in rule 35(10).
   Page limits for Cases: 35, 35 and 20 pages in rule 19(1); 55, 55 and 25 in rule 32(1); 15 pages for permission submissions and 25 for the bundle of documents in rule 26(10) and (11); 35 pages in rule 37(2); 55 pages in rule 41(5).
   Core bundles: 55, 35 and 25 pages in rules 19(2) and 32(2).
   The text's amounts and limits are constants in the modules, copied from the rule that states them; the amount a person actually provided, or the pages actually filed, is the input.
9. **The clock of each document starts at service, not filing.** Rule 17(8) and rule 41(3) run the respondent's 28 days "after the appellant serves the documents", and rule 17(10) runs the Reply's 14 days "after the respondent's Case is served on the appellant".
   The regulative rules start each step's clock when the step before it is done, and the decision functions take the date the document is served as an input.
10. **Paragraph (10) of rule 17 says "must" about things that exist only "if any".** The appellant "must file and serve" the Reply "(if any)", the second core bundle "(if necessary)" and the second bundle of authorities "(if any)".
    The regulative rule therefore takes whether there is anything to file as a fact, and has no third step when there is not.

## What the text does not answer (roc4)

1. What follows a late Reply, second core bundle or second bundle of authorities (rules 17(10), 30(11)): no consequence is stated, so the regulative rule's `BREACH` says so.
2. What follows a late notice of appeal (rules 14(1), 25(1)) or a late application for permission (rules 15(1), 26(1)): the Order states the extension powers (rules 14(2), 15(4), 25(2), 26(18)) and no other consequence.
3. What an order or direction allows, wherever the text says "unless the Court otherwise orders" or "otherwise directs" and does not say what the order may allow.
4. Whether a provision not named in rule 41(10) or (12), or rule 1(f), applies to a Medical Registration Act appeal (fork F7).
5. Whether the time for an appeal "has started" once the bar in rule 4(1) has lapsed and paragraph (1A) does not start it (costs decided within the 30 days); paragraph (1) says only when time does not start, and paragraph (1A) is the one positive start.
6. Whether an application for permission may be filed after the Judge has acted under rule 26(3)(a); the paragraph says only when it may not.
7. Whether rule 24's five limbs are all the cases this Division applies to; the rule does not say "only".
8. A time limit for rule 5(2) (the application to intervene and the affidavit) or rule 22 (the certified copy to the Registrar of the State Courts): none is stated.
9. Who pays out the security for costs under rules 20 and 33: the text says it "must be paid" and does not name the payer.
10. Whether a non-party may intervene without the permission of the appellate Court (rule 5(1)): the paragraph says a non-party "may apply to intervene ... with the permission" and does not say what follows without it; no function asks it.
11. The rate of interest in rule 6(3), the amount of "the relevant charges" for a copy of a decision in rule 12(3), and the amount of security in an appeal under section 59G of the Medical Registration Act (rule 41): none is stated, so there is no function for them.
12. A deadline for the lower Court's written grounds of decision in rule 17(1) (rule 17(3) runs 12 weeks from the notice of appeal for the appellant's step, and does not bind the lower Court), a page limit on the record of appeal in rule 17, and a page limit on a bundle of authorities in Division 2 (rule 19 sets limits for the Case, the Reply and the core bundles only): none is stated.
13. Whether the lower Court, the appellate Court or the General Division may allow excess pages without special circumstances, and whether the 25-page bundle limit of rule 26(11) can be exceeded at all (fork F8).

## What the main binary does not accept

Probed on 2026-11-05 on 1.6.109 and 1.6.108; both gave the same result each time.

1. **`#ASSERT` on a regulative rule.** `#ASSERT <deontic rule> EQUALS FULFILLED` is `DiagnosticSeverity_Error`, code `eval/unsupported-equality` (probe `work/probe/deont-assert.l4`).
   So every duty in `roc4-order-19-duties.l4` is run with `#TRACE` and its expected outcome is written beside it; `check.sh` does not see a `#TRACE` outcome, so the outcomes were compared by hand across the two builds (the two outputs are identical, `work/duties-l4-main-109.out` against `work/duties-l4-main-108.out`).
   Each duty also has a decision-function twin, which is asserted, in `roc4-order-19-div-1.l4`, `-div-2.l4`, `-div-3.l4` and `-div-4.l4`.
2. **A `LEST` after a `MAY` is ignored.** A `MAY ... WITHIN 14 HENCE FULFILLED LEST BREACH` with the act done on day 15 gives `FULFILLED` (probe `work/probe/may-lest.l4`).
   The skills say the same of main and say that the unstable dialect lapses into the `LEST`.
   The `MAY` in this row (rule 8(3)) therefore carries no `LEST`.
3. **An `ELSE IF` chain inside a `WHEN` branch of a `CONSIDER`.** It gives `parse/indentation`; a `BRANCH` with `IF ... THEN ...` lines and an `OTHERWISE`, in the same place, evaluates (probes `work/probe/elseif1.l4` and `elseif2.l4`).
   Every multi-way choice inside a `CONSIDER` in this row uses `BRANCH`.
4. **`REFUSE`, `BECAUSE` outside a `LEST BREACH` clause, and `YMD`** are not used, as the brief says; none was needed.

## What `check.sh` printed

Command: `L4=<scratchpad>/bin/l4-main-109 L4_MAIN=<scratchpad>/bin/l4-main-108 ./check.sh` in this folder, target `main` (the default), run on 2026-11-05 after the last edit; exit status 0.
Baseline it replaced: the folder as supplied had two modules (`roc-core.l4`, `roc-definitions.l4`), which print 0 errors and 0 satisfied on both builds; the row's own files add 12 modules and 2016 satisfied assertions (0 errors, 0 failed, 0 refused in total).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc4-cases-seat.l4                             0       914       0        0         0 |      0       914       0        0  same
roc4-order-19-div-1.l4                         0         0       0        0         0 |      0         0       0        0  same
roc4-order-19-div-2.l4                         0         0       0        0         0 |      0         0       0        0  same
roc4-order-19-div-3.l4                         0         0       0        0         0 |      0         0       0        0  same
roc4-order-19-div-4.l4                         0         0       0        0         0 |      0         0       0        0  same
roc4-order-19-duties.l4                        0         0       0        0         0 |      0         0       0        0  same
roc4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc4-tests-div-1.l4                            0       261       0        0         0 |      0       261       0        0  same
roc4-tests-div-2.l4                            0       228       0        0         0 |      0       228       0        0  same
roc4-tests-div-3.l4                            0       495       0        0         0 |      0       495       0        0  same
roc4-tests-div-4.l4                            0        98       0        0         0 |      0        98       0        0  same
roc4-tests-duties.l4                           0        20       0        0         0 |      0        20       0        0  same
TOTAL (14 modules)                             0      2016       0        0           |      0      2016       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Reading it: the first group of columns is build 1.6.109 and the group after the bar is build 1.6.108 (main, 2ae7c9b, 2026-11-02); every row says `same`.
The `#TRACE` outcomes in `roc4-tests-duties.l4` are not counted in `satisfied`; they were compared by hand across the two builds and are identical (`work/duties-l4-main-109.out` against `work/duties-l4-main-108.out`, no difference).
