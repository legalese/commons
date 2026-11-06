# NOTES.md (scja2): the Supreme Court of Judicature Act 1969 (Singapore), sections 30 to 72

Status (2026-11-05): written and run.
Every number below was printed by a command run on 2026-11-05 on the files in this folder: `check.sh` (section "What check.sh prints"), `srcrefs.py check --refs` and `--strict`, `cov.py` (the coverage table), and `l4 run` with both main builds.
Nothing here is a claim about what a court would decide.

Edition: Supreme Court of Judicature Act 1969, 2020 Revised Edition, informal consolidation, "version in force from 1/7/2024".
**The text is a plain-text rendering made by a converter script (`SCJA1969.txt`); it is not the official text, and nothing in this part claims to have been verified against the official text.**
This part's range is lines 2310 to 4320 of that file: Part 4 (the Appellate Division, ss 30 to 47), Part 5 (the Court of Appeal, ss 48 to 60M, including Division 3 criminal jurisdiction, ss 60D and 60E, and Division 4, the post-appeal application in a capital case, ss 60F to 60M) and Part 6 (officers and offices, ss 61 to 72).
Target: `main`.
Written and run with main build 1.6.109 (4c887e0, 2026-11-04) and compared by `check.sh` with main build 1.6.108 (2ae7c9b, 2026-11-02).
No `unstable` binary was used.

**The brief says layer 1 imports `scja-core.l4` and `scja-definitions.l4`; there is no `scja-definitions.l4`.**
`PLAN.md` and the keel's `NOTES.md` both say none was written: section 2 and the other definitions lie in the parts' own ranges, so a second module would give two modules the same `s 2 ...` names.
Every module of this part therefore imports `scja-core` (and `prelude`, `daydate`) only, plus `sgia-interpretation-time` where it counts a period (section "Dependencies").
No definition in this range is borrowed from section 2: the definitions this range needs are its own (section 60F) or are asked as plain facts.

## What this part is

Two layers, as the brief asks.

**Layer 1, the law, objectively.**
Nine modules follow the text's structure, section by section, with the Act's own numbering in every name (`s 41(10)(b) ...`), `-- src:` quote lines and an `@ref` locator above every declaration, and a test file beside each module.
The Appellate Division (ss 30 to 45) and the Court of Appeal (ss 48 to 60C) say much the same thing twice.
Under ruling E1 (option C) each section's answer is written on its own; the two sets are kept alike in wording so that a reader can compare them, and where the Act differs the encoding differs (section "Findings", 3).
**Layer 2, the seat.**
`scja2-seat.l4` has 77 exported questions, each named "Under section N, ...", for a person who wishes to start, defend or appeal a civil case in the High Court or the Court of Appeal.
`scja2-cases-seat.l4` asserts every one of them at least twice (233 assertions, 71 of them `NOTHING`, the answer "the Act does not say") with facts that person would state.
There is no seat for an official: the Judges' appointment (ss 30, 48), the sittings the Chief Justice appoints (ss 34(1)(a), 34(2), 52(1)(a), 52(2)), the criminal jurisdiction (ss 60D, 60E), the capital-case procedure (ss 60F to 60M) and the sections of Part 6 that address only an officer (ss 61, 62(1), 63, 64(1)(b) and (c), 64(2) and (3), 66, 67, 68(1), 69 to 71, 72(3)) are in layer 1 and the person meets them only through the questions in the seat.
The 77 questions are a selection, not one question per provision a litigant could meet: they ask which court has jurisdiction, how many Judges may hear the case and who may not sit, how it is heard and decided, when it may be dismissed without a hearing, what orders and further evidence the court may allow, the time limit for asking the full panel to rehear, whether a new trial may be ordered, whether an appeal stops enforcement, and whether the person may appeal from the Appellate Division.
The seat column of the coverage table shows, for every unit, whether it has a question.

| file | provisions | what it holds |
| --- | --- | --- |
| `scja2-part4-ad-general.l4` | ss 30 to 34 | the President of the Appellate Division and who presides, jurisdiction, composition, how a decision is made, sittings |
| `scja2-part4-ad-civil.l4` | ss 35 to 45 | the civil jurisdiction, smaller panels, oral hearing, summary dismissal, applications, incidental directions, hearing of appeals and further evidence, costs, new trial, immaterial errors, no stay |
| `scja2-part4-ad-appeals.l4` | ss 46, 47 | no appeal in certain cases; permission to appeal to the Court of Appeal |
| `scja2-part5-ca-general.l4` | ss 48 to 52 | the same matters for the Court of Appeal |
| `scja2-part5-ca-civil.l4` | ss 53 to 60C | the same matters for the Court of Appeal (53 has four limbs where 35 has two; 60A has two limbs where 43 has one) |
| `scja2-part5-ca-criminal.l4` | ss 60D, 60E | the criminal jurisdiction; composition and who may not sit |
| `scja2-part5-ca-capital-defs.l4` | s 60F | the definitions of Division 4 |
| `scja2-part5-ca-capital.l4` | ss 60G to 60M | permission for a PACC application, hearing, pending applications, abuse of process |
| `scja2-part6-officers.l4` | ss 61 to 72 | Registrar, Sheriff, Accountant, subordinate officers, commissioners for oaths, oaths of office, the Registry |
| `scja2-tests-part4-ad-general.l4`, `scja2-tests-part4-ad-civil.l4`, `scja2-tests-part4-ad-appeals.l4`, `scja2-tests-part5-ca-general.l4`, `scja2-tests-part5-ca-civil.l4`, `scja2-tests-part5-ca-criminal.l4`, `scja2-tests-part5-ca-capital-defs.l4`, `scja2-tests-part5-ca-capital.l4`, `scja2-tests-part6-officers.l4` | the same | one test file per module |
| `scja2-seat.l4`, `scja2-cases-seat.l4` | ss 31 to 72 | the questions and their cases |
| `sgia-interpretation-time.l4` | (a dependency, copied unchanged) | the Interpretation Act 1965's time rules |

The `.l4` files in this folder were generated by a script from templates kept in a work directory that is not shipped; the files here are the artefact, and a hand edit of one is the way to change it.

How the files are shaped, in the order a reader meets it:

- Every decision function returns `MAYBE BOOLEAN` (or `MAYBE` of a type): `JUST TRUE`, `JUST FALSE` or `NOTHING`.
  Every `JUST FALSE` branch carries a `-- FALSE-kind (the text says no in its own words): "<the words>"` comment, and every `NOTHING` branch a `-- NOTHING-kind (<why>)` comment, as the brief asks.
- The six kinds of case the Commons guide leaves to a case-by-case decision (an "unless" once met, a bare "must" not done, "listed in" a Schedule, a duty whose "if" is unmet, "(other than X)", a missing event in a ledger) are decided site by site in `## Judgment calls (scja2)`, each with the other reading.
- A caller never turns `NOTHING` into `FALSE`: where a section takes another section's answer as an input (seams, section "Seams"), the input is typed `MAYBE` and `NOTHING` is passed through.
- A prohibition with no gate is written as the permission it negates ("the Judge may sit ..."), so that `JUST FALSE` is the text's own no; a prohibition with a gate or an exception is written as the bar ("the bar ... applies": `JUST TRUE` inside the bar, `JUST FALSE` outside it), and the SHANT rule is derived from the function where the text names the bearer (ruling N2; the eleven rules are listed under N2 in the fork register).
- Where a section imposes a duty, permission or prohibition on a named party it is also a regulative rule (`PARTY ... MUST / MAY / SHANT ...`) with a `#TRACE`, and the same duty is a decision function that the tests assert (section "What the main binary does not accept", 3).
- Every top-level name, every `DECLARE`d type and every constructor begins with its provision's label.
  The seat's own wiring helpers begin `scja2 seat:` instead, because they belong to no provision and another part's seat could otherwise define the same helper (finding 7).

## Dependencies

One dependency was needed, and it is staged and copied unchanged.

| module | Commons path | blob | Commons main | sections used |
| --- | --- | --- | --- | --- |
| `sgia-interpretation-time.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4` | `fe60ab2c1f2326a5b061e163761bd63e4f47e12a` | `d468311a6ea4bab765b1ee7ccc8f0d7ccb29a357` | Interpretation Act 1965 s 50(a), (b) and (d), through `the last day of the period once section 50(b) is applied` (ss 41(10)(b), 59(10)(b)) and `is an excluded day` (s 72(1), (2)) |

- The copy in this folder carries the staged 3-line header that says where it came from, so `git hash-object` on it gives a different value from the blob above; remove the first 3 lines and it gives the blob (as `DEPENDENCIES.md` states). `cmp` of the copy against the staged file in `inputs/DEPENDENCIES/` reported them identical on 2026-11-05.
- **The module's own answer for a period counted "after" a day is `NOTHING`**: its `the last day of a period` answers `NOTHING` for the counting word `After`, because the Interpretation Act has no rule for it (its header says so).
  Sections 41(10)(b) and 59(10)(b) say "the expiration of 7 days after the date on which the decision ... is made".
  This part did not call that function.
  It called the module's `the last day of the period once section 50(b) is applied`, which the module provides "for a period (weeks, months, years, or days 'after' an event) whose counting the Act does not give", with the last day worked out here as the decision date plus 7 (the keel's constant `the Act's number of days for ss 41(10)(b) and 59(10)(b)`), the unit `Days`, the day's public holidays, and `a contrary intention appears` set to `FALSE`.
  The module's comment names its own fork F4 (does section 50(b) reach every period, or periods of days only?); for a period of days the module's two readings give the same date, so the choice between them does not matter here.
  What is this part's own reading, and is fork F3 below, is that the 7 days are counted from the day after the decision and section 50(b) is applied to the last day; a reader who takes the module's `After` answer gets `NOTHING` for both sections.
- `sgia-p1-definitions.l4` (the 92 definitions of the Interpretation Act) is staged for this text but was not needed, and was not copied.
- The Rules of Court count their own periods (ss 60G(3) to (5), 60H(1) to (3)); those periods are plain inputs and the Interpretation Act module is not used for them.
- For the lead, to paste into `encoding.json`:

```json
"dependencies": [{"module": "sgia-interpretation-time.l4", "commons_path": "subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-interpretation-time.l4", "blob": "fe60ab2c1f2326a5b061e163761bd63e4f47e12a", "commons_main": "d468311a6ea4bab765b1ee7ccc8f0d7ccb29a357", "used": "Interpretation Act 1965 s 50(a), (b), (d)"}]
```

Provisions of other Acts that this range depends on (the Criminal Procedure Code 2010, the Legal Profession Act 1966, the Police Force Act 2004, the Post-appeal Applications in Capital Cases Act 2022, the Extradition Act 1968) are not staged; each borrowed fact is a plain yes/no input whose name says which section it is, and none is a dependency.

## Unstable dialect

I looked at time (the one period counted under the Interpretation Act, ss 41(10)(b), 59(10)(b); the weekday test in s 72; the Rules of Court periods in ss 60G(3) to (5) and 60H(1) to (3)), at versions (the `[Act ... wef ...]` tags in lines 2310 to 4320 are amendment tags, and the text gives no rule that is in force on different dates) and at workarounds (none was forced on main beyond those in "What the main binary does not accept"), and found no shape that the unstable dialect would express better; no second, unstable encoding was written.

## Coverage (scja2)

- Text units counted (script, units.tsv): 422 (sections, subsections, paragraphs, sub-paragraphs and the s 60F definitions, Examples and limbs).
- Rows in the table: before this part wrote anything, 0 for lines 2310-4320 (the keel's table covers lines 1-45 only); after, 422 unit rows plus 218 rows for the 340 lines that are not provisions, 640 rows in all.
- Unit rows by disposition: encoded 344, fork 76, inert 2, repealed or blank in this text 0 (the text shows no repealed or blank provision in lines 2310-4320).
- Line rows (all inert, reason 1): 218 rows covering 340 lines (page furniture and amendment tags 149 rows / 255 lines; section headings 57 rows / 65 lines; Part and Division headings 12 rows / 20 lines).
- Non-blank lines in lines 2310-4320: 1331. Lines in no row (script check): 0.
- Inert unit rows (reason 2): `s 68(3)`, `s 70`.

| unit (lines) | opens with | disposition | where it is encoded | asserts | seat |
| --- | --- | --- | --- | --- | --- |
| `s 30` (2318-2339) | 30.—(1) The Chief Justice may appoint a Judge of the Appella | encoded | by the rows below |  |  |
| `s 30(1)` (2318-2319) | 30.—(1) The Chief Justice may appoint a Judge of the Appella | fork (fork F17) | `s 30(1) the Chief Justice may appoint the Judge to be the President of the Appellate Division` [function, scja2-part4-ad-general.l4] | 2 |  |
| `s 30(2)` (2323-2324) | (2) If no appointment is made under subsection (1), the Chie | encoded | `s 30(2) the Chief Justice is the President of the Appellate Division` [function, scja2-part4-ad-general.l4] | 2 |  |
| `s 30(3)` (2328-2339) | (3) In a sitting of the Appellate Division — | encoded | by the rows below |  |  |
| `s 30(3)(a)` (2330-2331) | (a) the most senior Supreme Court Judge, as determined by | encoded | `s 30(3)(a) the Judge is to preside in a sitting of the Appellate Division` [function, scja2-part4-ad-general.l4] | 3 |  |
| `s 30(3)(b)` (2338-2339) | (b) if there is no Supreme Court Judge, the Chief Justice is | encoded | `s 30(3)(b) the Chief Justice is to appoint a person to preside in a sitting of the Appellate Di…` [function, scja2-part4-ad-general.l4] | 2 |  |
| `s 31` (2345-2361) | 31.—(1) The Appellate Division has the civil jurisdiction | encoded | by the rows below |  |  |
| `s 31(1)` (2345-2346) | 31.—(1) The Appellate Division has the civil jurisdiction | encoded | `s 31(1) the Appellate Division has the civil jurisdiction mentioned in section 35 over the matt…` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 31(2)` (2350) | (2) The Appellate Division has no criminal jurisdiction. | fork (fork F2) | `s 31(2) the Appellate Division has criminal jurisdiction over the proceeding` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 31(3)` (2354-2356) | (3) The Appellate Division has, in an appeal and for any pur | encoded | `s 31(3) the Appellate Division has the jurisdiction or power of the court or tribunal from whic…` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 31(4)` (2360-2361) | (4) The Appellate Division may decide any question that need | encoded | `s 31(4) the Appellate Division may decide the question` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 32` (2367-2381) | 32.—(1) Subject to this Act, the jurisdiction of the Appella | encoded | by the rows below |  |  |
| `s 32(1)` (2367-2369) | 32.—(1) Subject to this Act, the jurisdiction of the Appella | fork (fork F6) | `s 32(1) the number of Judges is one that the subsection provides for` [function, scja2-part4-ad-general.l4] | 5 | yes (1) |
| `s 32(2)` (2373-2375) | (2) A Judge must not sit in the Appellate Division to hear o | encoded | `s 32(2) the Judge may sit in the Appellate Division to hear or decide the matter` [function, scja2-part4-ad-general.l4]; `s 32(2) party` [type, scja2-part4-ad-general.l4]; `s 32(2) the Judge who made the decision appealed from` [constructor, scja2-part4-ad-general.l4]; `s 32(2) act` [type, scja2-part4-ad-general.l4]; and 2 more with the same label | 3 | yes (1) |
| `s 32(3)` (2379-2381) | (3) Section 10A applies in relation to proceedings before th | encoded | `s 32(3) the Appellate Division may summon assessors as section 10A allows` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 33` (2387-2400) | 33.—(1) A decision of the Appellate Division is to be made i | encoded | by the rows below |  |  |
| `s 33(1)` (2387-2389) | 33.—(1) A decision of the Appellate Division is to be made i | encoded | `s 33(1) the decision goes the way of the opinion of the majority of the Judges hearing the case` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 33(2)` (2398-2400) | (2) An appeal or application to the Appellate Division is to | encoded | `s 33(2) the appeal or application is dismissed because the Judges hearing it are evenly divided` [function, scja2-part4-ad-general.l4] | 3 | yes (1) |
| `s 34` (2406-2417) | 34.—(1) The Appellate Division — | encoded | by the rows below |  |  |
| `s 34(1)` (2406-2412) | 34.—(1) The Appellate Division — | encoded | by the rows below |  |  |
| `s 34(1)(a)` (2408-2409) | (a) is to sit on such dates and at such places as the Chief  | encoded | `s 34(1)(a) the date is one that the Chief Justice appointed` [function, scja2-part4-ad-general.l4]; `s 34(1)(a) the place is one that the Chief Justice appointed` [function, scja2-part4-ad-general.l4] | 4 |  |
| `s 34(1)(b)` (2411-2412) | (b) may sit on a Saturday, Sunday or public holiday, or duri | encoded | `s 34(1)(b) the Appellate Division may sit on the day` [function, scja2-part4-ad-general.l4] | 4 |  |
| `s 34(2)` (2416-2417) | (2) The Chief Justice may cancel or postpone a sitting appoi | encoded | `s 34(2) the Chief Justice may cancel or postpone the sitting` [function, scja2-part4-ad-general.l4] | 2 |  |
| `s 35` (2425-2441) | 35.—(1) This Division applies to the Appellate Division in t | encoded | by the rows below |  |  |
| `s 35(1)` (2425-2426) | 35.—(1) This Division applies to the Appellate Division in t | encoded | `s 35(1) this Division applies to the Appellate Division` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 35(2)` (2430-2441) | (2) The civil jurisdiction of the Appellate Division consist | fork (fork F15) | `s 35(2) the matter is one of the matters of the civil jurisdiction of the Appellate Division` [function, scja2-part4-ad-civil.l4] | 5 | yes (1) |
| `s 35(2)(a)` (2435-2437) | (a) any appeal against any decision made by the General | fork (fork F1, F2) | `s 35(2)(a) the matter is an appeal against a decision of the General Division in a civil cause …` [function, scja2-part4-ad-civil.l4] | 8 |  |
| `s 35(2)(b)` (2439-2441) | (b) any appeal or other process that any written law provide | encoded | `s 35(2)(b) the matter is an appeal or other process that lies, or is transferred, to the Appell…` [function, scja2-part4-ad-civil.l4] | 3 |  |
| `s 36` (2452-2478) | 36.—(1) Despite section 32(1), a case before the Appellate | encoded | by the rows below |  |  |
| `s 36(1)` (2452-2458) | 36.—(1) Despite section 32(1), a case before the Appellate | fork (fork F10, F12) | `s 36(1) the case may be heard and decided by that number of Judges` [function, scja2-part4-ad-civil.l4] | 11 | yes (1) |
| `s 36(1)(a)` (2456) | (a) either a single Judge or 2 Judges; or | encoded | covered by the `s 36(1)` definition above |  |  |
| `s 36(1)(b)` (2458) | (b) 2 Judges. | encoded | covered by the `s 36(1)` definition above |  |  |
| `s 36(2)` (2462-2464) | (2) A Judge must not sit in the Appellate Division to hear o | encoded | `s 36(2) the Judge may sit in the Appellate Division to hear or decide the application` [function, scja2-part4-ad-civil.l4]; `s 36(2) party` [type, scja2-part4-ad-civil.l4]; `s 36(2) the Judge who made the direction or order` [constructor, scja2-part4-ad-civil.l4]; `s 36(2) act` [type, scja2-part4-ad-civil.l4]; and 2 more with the same label | 2 | yes (1) |
| `s 36(3)` (2468-2478) | (3) Where the Appellate Division is constituted by 3 or more | fork (fork F16) | by the rows below |  |  |
| `s 36(3)(a)` (2473-2475) | (a) the Appellate Division must continue to hear and decide | encoded | `s 36(3)(a) the Appellate Division must continue to hear and decide the case` [function, scja2-part4-ad-civil.l4] | 6 | yes (1) |
| `s 36(3)(b)` (2477-2478) | (b) the case must be reheard if it cannot continue under | encoded | `s 36(3)(b) the case must be reheard` [function, scja2-part4-ad-civil.l4] | 6 | yes (1) |
| `s 37` (2484-2510) | 37.—(1) Subject to subsection (2), the Appellate Division ma | encoded | by the rows below |  |  |
| `s 37(1)` (2484-2486) | 37.—(1) Subject to subsection (2), the Appellate Division ma | fork (fork F13) | `s 37(1) the Appellate Division may decide the matter without hearing oral arguments` [function, scja2-part4-ad-civil.l4] | 2 | yes (1) |
| `s 37(2)` (2488-2490) | (2) Subsection (1) does not allow any part of a proceeding w | fork (fork F8) | `s 37(2) the part of the proceeding where oral evidence is given may be conducted without an ora…` [function, scja2-part4-ad-civil.l4]; `s 37(2) the bar on conducting the part of the proceeding without an oral hearing applies` [function, scja2-part4-ad-civil.l4] | 8 |  |
| `s 37(3)` (2492-2496) | (3) Subject to subsection (4), the Appellate Division may, i | encoded | `s 37(3) the Appellate Division may direct that the matter be heard in an asynchronous manner by…` [function, scja2-part4-ad-civil.l4] | 2 | yes (1) |
| `s 37(4)` (2503-2506) | (4) The Appellate Division must not hear a matter in an | fork (fork F8) | `s 37(4) the bar on hearing the matter in an asynchronous manner applies to the Appellate Divisi…` [function, scja2-part4-ad-civil.l4]; `s 37(4) party` [type, scja2-part4-ad-civil.l4]; `s 37(4) the Appellate Division` [constructor, scja2-part4-ad-civil.l4]; `s 37(4) act` [type, scja2-part4-ad-civil.l4]; and 2 more with the same label | 2 |  |
| `s 37(5)` (2508-2510) | (5) To avoid doubt, this section does not affect the power o | encoded | `s 37(5) the Appellate Division may hear oral arguments before deciding the matter` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 38` (2516-2557) | 38.—(1) The Appellate Division may summarily dismiss any | encoded | by the rows below |  |  |
| `s 38(1)` (2516-2530) | 38.—(1) The Appellate Division may summarily dismiss any | encoded | `s 38(1) the Appellate Division may summarily dismiss the appeal or application on its own motion` [function, scja2-part4-ad-civil.l4] | 5 | yes (1) |
| `s 38(1)(a)` (2520-2521) | (a) the Appellate Division does not have the jurisdiction to | encoded | covered by the `s 38(1)` definition above |  |  |
| `s 38(1)(b)` (2523-2527) | (b) the Appellate Division or the Court of Appeal has alread | encoded | covered by the `s 38(1)` definition above |  |  |
| `s 38(1)(c)` (2529-2530) | (c) such conditions as may be prescribed by the Rules of Cou | encoded | covered by the `s 38(1)` definition above |  |  |
| `s 38(2)` (2534-2542) | (2) Before summarily dismissing any appeal or application un | fork (fork F11) | `s 38(2) the Appellate Division has met the requirements before summarily dismissing, as the sec…` [function, scja2-part4-ad-civil.l4]; `s 38(2) party` [type, scja2-part4-ad-civil.l4]; `s 38(2) the Appellate Division` [constructor, scja2-part4-ad-civil.l4]; `s 38(2) act` [type, scja2-part4-ad-civil.l4]; and 1 more with the same label | 3 | yes (1) |
| `s 38(2)(a)` (2537-2539) | (a) give the appellant or applicant a reasonable opportunity | encoded | `s 38(2)(a) gives the appellant or applicant a reasonable opportunity to show cause` [constructor, scja2-part4-ad-civil.l4] | 0 |  |
| `s 38(2)(b)` (2541-2542) | (b) consider any representations made by the appellant or | encoded | `s 38(2)(b) considers the representations made` [constructor, scja2-part4-ad-civil.l4] | 0 |  |
| `s 38(3)` (2546-2547) | (3) The Appellate Division may exercise its powers under thi | encoded | `s 38(3) the Appellate Division may exercise its powers under this section without hearing oral …` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 38(4)` (2556-2557) | (4) In this section, “appeal” includes part of an appeal and | encoded | `s 38(4) the thing is an appeal or an application for the purposes of this section` [function, scja2-part4-ad-civil.l4] | 4 |  |
| `s 39` (2563-2565) | 39. Where an application may be made either to the General | encoded | `s 39 the application must first be made to the General Division` [function, scja2-part4-ad-civil.l4]; `s 39 the court to which the application must first be made` [function, scja2-part4-ad-civil.l4] | 4 | yes (1) |
| `s 40` (2571-2618) | 40.—(1) The Appellate Division may make one or more of the | encoded | by the rows below |  |  |
| `s 40(1)` (2571-2583) | 40.—(1) The Appellate Division may make one or more of the | encoded | `s 40(1) kind of direction or order` [type, scja2-part4-ad-civil.l4]; `s 40(1) another direction or order` [constructor, scja2-part4-ad-civil.l4]; `s 40(1) the Appellate Division may make the direction or order in the pending matter` [function, scja2-part4-ad-civil.l4] | 7 | yes (1) |
| `s 40(1)(a)` (2575-2576) | (a) any direction or order incidental to the pending matter  | encoded | `s 40(1)(a) a direction or order incidental to the pending matter not involving the decision of …` [constructor, scja2-part4-ad-civil.l4] | 3 |  |
| `s 40(1)(b)` (2578-2579) | (b) any interim order to prevent prejudice to the claims of  | encoded | `s 40(1)(b) an interim order to prevent prejudice to the claims of the parties pending the deter…` [constructor, scja2-part4-ad-civil.l4] | 2 |  |
| `s 40(1)(c)` (2581-2583) | (c) any order for security for costs, and for the dismissal  | encoded | `s 40(1)(c) an order for security for costs, or for the dismissal of the pending matter for defa…` [constructor, scja2-part4-ad-civil.l4] | 2 |  |
| `s 40(2)` (2587-2588) | (2) A direction or an order under subsection (1) may be made | encoded | `s 40(2) the Appellate Division may make the direction or order on its own motion or on the appl…` [function, scja2-part4-ad-civil.l4] | 3 |  |
| `s 40(3)` (2592-2593) | (3) A direction or an order under subsection (1) may be made | encoded | `s 40(3) the direction or order may be made by that number of Judges` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 40(4)` (2597-2612) | (4) A direction or an order under subsection (1) may also be | encoded | `s 40(4) the direction or order may be made by a single Judge` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 40(4)(a)` (2600-2601) | (a) the direction or order may be varied or discharged by | encoded | `s 40(4)(a) the direction or order may be varied or discharged by those Judges` [function, scja2-part4-ad-civil.l4] | 3 |  |
| `s 40(4)(b)` (2603-2612) | (b) an application to vary or discharge the direction or ord | encoded | `s 40(4)(b) an application to vary or discharge the direction or order may be made` [function, scja2-part4-ad-civil.l4]; `s 40(4)(b) the decision to give or refuse permission is final` [function, scja2-part4-ad-civil.l4] | 5 | yes (2) |
| `s 40(5)` (2618) | (5) Subsections (3) and (4) apply despite section 32(1). | encoded | `s 40(5) section 32(1) does not stand in the way of the direction or order` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41` (2624-2729) | 41.—(1) Appeals to the Appellate Division are to be by way o | encoded | by the rows below |  |  |
| `s 41(1)` (2624-2625) | 41.—(1) Appeals to the Appellate Division are to be by way o | encoded | `s 41(1) the appeal is by way of rehearing` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41(2)` (2629-2631) | (2) In hearing and deciding an appeal, the Appellate Divisio | encoded | `s 41(2) the Appellate Division has the power or duty of the court or tribunal from which the ap…` [function, scja2-part4-ad-civil.l4] | 3 |  |
| `s 41(3)` (2635-2644) | (3) The Appellate Division may receive further evidence — | encoded | `s 41(3) manner of receiving further evidence` [type, scja2-part4-ad-civil.l4]; `s 41(3) in a manner that the Appellate Division does not allow` [constructor, scja2-part4-ad-civil.l4]; `s 41(3) the Appellate Division may receive further evidence in that manner` [function, scja2-part4-ad-civil.l4] | 6 |  |
| `s 41(3)(a)` (2637) | (a) by oral examination in court; | encoded | `s 41(3)(a) by oral examination in court` [constructor, scja2-part4-ad-civil.l4] | 1 |  |
| `s 41(3)(b)` (2639) | (b) by affidavit; | encoded | `s 41(3)(b) by affidavit` [constructor, scja2-part4-ad-civil.l4] | 1 |  |
| `s 41(3)(c)` (2641-2642) | (c) by deposition taken before an examiner or a commissioner | encoded | `s 41(3)(c) by deposition taken before an examiner or a commissioner` [constructor, scja2-part4-ad-civil.l4] | 1 |  |
| `s 41(3)(d)` (2644) | (d) in any other manner that the Appellate Division allows. | encoded | `s 41(3)(d) in any other manner that the Appellate Division allows` [constructor, scja2-part4-ad-civil.l4] | 1 |  |
| `s 41(4)` (2648-2650) | (4) Except as provided in subsection (5), such further evide | fork (fork F8) | `s 41(4) the further evidence may be given to the Appellate Division` [function, scja2-part4-ad-civil.l4]; `s 41(4) the bar on giving the further evidence to the Appellate Division applies` [function, scja2-part4-ad-civil.l4] | 10 | yes (1) |
| `s 41(5)` (2656-2658) | (5) Such further evidence may be given to the Appellate Divi | encoded | `s 41(5) the further evidence may be given to the Appellate Division without permission` [function, scja2-part4-ad-civil.l4] | 2 | yes (1) |
| `s 41(6)` (2664-2665) | (6) The Appellate Division may draw any inference of fact, g | encoded | `s 41(6) the Appellate Division may draw any inference of fact, give any judgment and make any o…` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41(7)` (2674-2683) | (7) The powers in this section — | encoded | by the rows below |  |  |
| `s 41(7)(a)` (2676-2678) | (a) may be exercised in relation to any part of the decision | encoded | `s 41(7)(a) the power may be exercised in relation to that part of the decision appealed against` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41(7)(b)` (2680-2683) | (b) may be exercised in favour of any party to the decision | encoded | `s 41(7)(b) the power may be exercised in favour of that party` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41(8)` (2687-2691) | (8) Where an application for permission to adduce further ev | encoded | `s 41(8) a party may request the full panel to rehear arguments on the application for permissio…` [function, scja2-part4-ad-civil.l4]; `s 41(8) party` [type, scja2-part4-ad-civil.l4]; `s 41(8) a party to the appeal` [constructor, scja2-part4-ad-civil.l4]; `s 41(8) act` [type, scja2-part4-ad-civil.l4]; and 2 more with the same label | 2 | yes (1) |
| `s 41(9)` (2695-2703) | (9) No request may be made under subsection (8) in respect o | fork (fork F8) | `s 41(9) the bar on a request under subsection (8) applies` [function, scja2-part4-ad-civil.l4] | 6 | yes (1) |
| `s 41(9)(a)` (2700-2701) | (a) by 2 Judges, where the Appellate Division hearing the | encoded | covered by the `s 41(9)` definition above |  |  |
| `s 41(9)(b)` (2703) | (b) by 3 or more Judges. | encoded | covered by the `s 41(9)` definition above |  |  |
| `s 41(10)` (2707-2716) | (10) A request under subsection (8) must be made before the  | fork (fork F3) | `s 41(10) the request under subsection (8) is made in time` [function, scja2-part4-ad-civil.l4] | 6 | yes (1) |
| `s 41(10)(a)` (2710-2712) | (a) the time at which the judgment or order relating to the | encoded | `s 41(10)(a) the request is made before the time at which the judgment or order is extracted` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 41(10)(b)` (2714-2716) | (b) the expiration of 7 days after the date on which the dec | fork (fork F3) | `s 41(10)(b) the last day of the 7 days after the date on which the decision is made` [function, scja2-part4-ad-civil.l4] | 3 |  |
| `s 41(11)` (2720-2729) | (11) After rehearing arguments on a request mentioned in | encoded | `s 41(11) the Appellate Division may affirm, vary or set aside the decision on the application f…` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 42` (2735-2736) | 42. The Appellate Division may make any order as to the cost | encoded | `s 42 the Appellate Division may make the order as to costs` [function, scja2-part4-ad-civil.l4] | 2 | yes (1) |
| `s 43` (2742-2769) | 43.—(1) Subject to this Act, the Appellate Division may orde | encoded | by the rows below |  |  |
| `s 43(1)` (2742-2745) | 43.—(1) Subject to this Act, the Appellate Division may orde | fork (fork F1, F14) | `s 43(1) the Appellate Division may order a new trial of the matter` [function, scja2-part4-ad-civil.l4] | 7 | yes (1) |
| `s 43(2)` (2749-2751) | (2) A new trial must not be ordered on the ground of an impr | fork (fork F8) | `s 43(2) a new trial may be ordered on that ground` [function, scja2-part4-ad-civil.l4]; `s 43(2) the bar on a new trial on that ground applies` [function, scja2-part4-ad-civil.l4] | 6 | yes (1) |
| `s 43(3)` (2755-2763) | (3) If the substantial wrong or miscarriage of justice menti | encoded | by the rows below |  |  |
| `s 43(3)(a)` (2759-2760) | (a) give final judgment in respect of the unaffected part of | encoded | `s 43(3)(a) the Appellate Division may give final judgment in respect of the unaffected part of …` [function, scja2-part4-ad-civil.l4] | 2 | yes (1) |
| `s 43(3)(b)` (2762-2763) | (b) direct a new trial in respect of the affected part of th | encoded | `s 43(3)(b) the Appellate Division may direct a new trial in respect of the affected part of the…` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 43(4)` (2767-2769) | (4) A new trial may be ordered on any question without inter | encoded | `s 43(4) the new trial may be ordered on that question without interfering with the finding or d…` [function, scja2-part4-ad-civil.l4] | 2 |  |
| `s 44` (2775-2778) | 44. The Appellate Division may not reverse or substantially  | encoded | `s 44 the Appellate Division may reverse or substantially vary the decision, or order a new tria…` [function, scja2-part4-ad-civil.l4]; `s 44 party` [type, scja2-part4-ad-civil.l4]; `s 44 the Appellate Division` [constructor, scja2-part4-ad-civil.l4]; `s 44 act` [type, scja2-part4-ad-civil.l4]; and 2 more with the same label | 3 | yes (1) |
| `s 45` (2789-2799) | 45.—(1) An appeal to the Appellate Division does not operate | encoded | by the rows below |  |  |
| `s 45(1)` (2789-2792) | 45.—(1) An appeal to the Appellate Division does not operate | fork (fork F8) | `s 45(1) the appeal operates as a stay of execution or enforcement or of proceedings under the d…` [function, scja2-part4-ad-civil.l4]; `s 45(1) the rule that the appeal does not operate as a stay applies` [function, scja2-part4-ad-civil.l4] | 4 | yes (1) |
| `s 45(2)` (2798-2799) | (2) No intermediate act or proceeding is to be invalidated e | fork (fork F8) | `s 45(2) the intermediate act or proceeding is invalidated` [function, scja2-part4-ad-civil.l4]; `s 45(2) the rule that no intermediate act or proceeding is invalidated applies` [function, scja2-part4-ad-civil.l4] | 4 | yes (1) |
| `s 46` (2812-2813) | 46. An appeal cannot be brought against a decision of the Ap | fork (fork F12) | `s 46 an appeal can be brought against the decision of the Appellate Division` [function, scja2-part4-ad-appeals.l4] | 3 | yes (1) |
| `s 47` (2819-2866) | 47.—(1) An appeal against a decision of the Appellate Divisi | encoded | by the rows below |  |  |
| `s 47(1)` (2819-2821) | 47.—(1) An appeal against a decision of the Appellate Divisi | encoded | `s 47(1) an appeal against the decision may be brought` [function, scja2-part4-ad-appeals.l4] | 5 | yes (1) |
| `s 47(2)` (2827-2828) | (2) The Court of Appeal may grant permission under subsectio | encoded | `s 47(2) the Court of Appeal may grant permission under subsection (1)` [function, scja2-part4-ad-appeals.l4] | 2 | yes (1) |
| `s 47(3)` (2834-2837) | (3) In deciding whether to grant permission under subsection | encoded | `s 47(3) the Court of Appeal is to have regard to the matter` [function, scja2-part4-ad-appeals.l4] | 2 |  |
| `s 47(4)` (2848-2866) | (4) To avoid doubt — | encoded | by the rows below |  |  |
| `s 47(4)(a)` (2850-2852) | (a) the Court of Appeal is not required to grant permission | encoded | `s 47(4)(a) the Court of Appeal is required to grant permission under subsection (1)` [function, scja2-part4-ad-appeals.l4] | 2 |  |
| `s 47(4)(b)` (2856-2866) | (b) permission may be granted under subsection (1) even if t | encoded | `s 47(4)(b) permission may be granted under subsection (1) despite the history of the appeal` [function, scja2-part4-ad-appeals.l4] | 3 | yes (1) |
| `s 47(4)(b)(i)` (2860-2862) | (i) was made in an appeal transferred by the Court of | encoded | covered by the `s 47(4)(b)` definition above |  |  |
| `s 47(4)(b)(ii)` (2864-2866) | (ii) was made in an appeal to the Appellate Division that | encoded | covered by the `s 47(4)(b)` definition above |  |  |
| `s 48` (2880-2892) | 48.—(1) The Chief Justice is the President of the Court of A | encoded | by the rows below |  |  |
| `s 48(1)` (2880-2882) | 48.—(1) The Chief Justice is the President of the Court of A | fork (fork F17) | `s 48(1) the Judge is the President of the Court of Appeal` [function, scja2-part5-ca-general.l4]; `s 48(1) the Chief Justice may appoint the Judge to be a Vice-President of the Court of Appeal` [function, scja2-part5-ca-general.l4] | 4 |  |
| `s 48(2)` (2886-2892) | (2) In a sitting of the Court of Appeal — | encoded | by the rows below |  |  |
| `s 48(2)(a)` (2888-2889) | (a) the most senior Supreme Court Judge, as determined by | encoded | `s 48(2)(a) the Judge is to preside in a sitting of the Court of Appeal` [function, scja2-part5-ca-general.l4] | 3 |  |
| `s 48(2)(b)` (2891-2892) | (b) if there is no Supreme Court Judge, the Chief Justice is | encoded | `s 48(2)(b) the Chief Justice is to appoint a person to preside in a sitting of the Court of App…` [function, scja2-part5-ca-general.l4] | 2 |  |
| `s 49` (2903-2917) | 49.—(1) The Court of Appeal has the civil jurisdiction menti | encoded | by the rows below |  |  |
| `s 49(1)` (2903-2906) | 49.—(1) The Court of Appeal has the civil jurisdiction menti | encoded | `s 49(1) the Court of Appeal has jurisdiction over the matter` [function, scja2-part5-ca-general.l4] | 5 | yes (1) |
| `s 49(2)` (2910-2912) | (2) The Court of Appeal has, in an appeal and for any purpos | encoded | `s 49(2) the Court of Appeal has the jurisdiction or power of the court or tribunal from which t…` [function, scja2-part5-ca-general.l4] | 3 | yes (1) |
| `s 49(3)` (2916-2917) | (3) The Court of Appeal may decide any question that needs t | encoded | `s 49(3) the Court of Appeal may decide the question` [function, scja2-part5-ca-general.l4] | 3 | yes (1) |
| `s 50` (2923-2936) | 50.—(1) Subject to this Act, the jurisdiction of the Court o | encoded | by the rows below |  |  |
| `s 50(1)` (2923-2924) | 50.—(1) Subject to this Act, the jurisdiction of the Court o | fork (fork F6) | `s 50(1) the number of Judges is one that the subsection provides for` [function, scja2-part5-ca-general.l4] | 5 | yes (1) |
| `s 50(2)` (2928-2930) | (2) A Judge must not sit in the Court of Appeal to hear or d | encoded | `s 50(2) the Judge may sit in the Court of Appeal to hear or decide the matter` [function, scja2-part5-ca-general.l4]; `s 50(2) party` [type, scja2-part5-ca-general.l4]; `s 50(2) the Judge who made the decision appealed from` [constructor, scja2-part5-ca-general.l4]; `s 50(2) act` [type, scja2-part5-ca-general.l4]; and 2 more with the same label | 3 | yes (1) |
| `s 50(3)` (2934-2936) | (3) Section 10A applies in relation to proceedings before th | encoded | `s 50(3) the Court of Appeal may summon assessors as section 10A allows` [function, scja2-part5-ca-general.l4] | 3 | yes (1) |
| `s 51` (2942-2950) | 51.—(1) A decision of the Court of Appeal is to be made in | encoded | by the rows below |  |  |
| `s 51(1)` (2942-2944) | 51.—(1) A decision of the Court of Appeal is to be made in | encoded | `s 51(1) the decision goes the way of the opinion of the majority of the Judges hearing the case` [function, scja2-part5-ca-general.l4] | 3 | yes (1) |
| `s 51(2)` (2948-2950) | (2) An appeal or application to the Court of Appeal is to be | encoded | `s 51(2) the appeal or application is dismissed because the Judges hearing it are evenly divided` [function, scja2-part5-ca-general.l4] | 3 | yes (1) |
| `s 52` (2961-2972) | 52.—(1) The Court of Appeal — | encoded | by the rows below |  |  |
| `s 52(1)` (2961-2967) | 52.—(1) The Court of Appeal — | encoded | by the rows below |  |  |
| `s 52(1)(a)` (2963-2964) | (a) is to sit on such dates and at such places as the Chief  | encoded | `s 52(1)(a) the date is one that the Chief Justice appointed` [function, scja2-part5-ca-general.l4]; `s 52(1)(a) the place is one that the Chief Justice appointed` [function, scja2-part5-ca-general.l4] | 4 |  |
| `s 52(1)(b)` (2966-2967) | (b) may sit on a Saturday, Sunday or public holiday, or duri | encoded | `s 52(1)(b) the Court of Appeal may sit on the day` [function, scja2-part5-ca-general.l4] | 4 |  |
| `s 52(2)` (2971-2972) | (2) The Chief Justice may cancel or postpone a sitting appoi | encoded | `s 52(2) the Chief Justice may cancel or postpone the sitting` [function, scja2-part5-ca-general.l4] | 2 |  |
| `s 53` (2980-3020) | 53.—(1) This Division applies to the Court of Appeal in the | encoded | by the rows below |  |  |
| `s 53(1)` (2980-2981) | 53.—(1) This Division applies to the Court of Appeal in the | encoded | `s 53(1) this Division applies to the Court of Appeal` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 53(2)` (2985-3020) | (2) The civil jurisdiction of the Court of Appeal consists o | fork (fork F15) | `s 53(2) the matter is one of the matters of the civil jurisdiction of the Court of Appeal` [function, scja2-part5-ca-civil.l4] | 4 | yes (1) |
| `s 53(2)(a)` (2990-2992) | (a) any appeal against any decision made by the General | fork (fork F1, F2) | `s 53(2)(a) the matter is an appeal against a decision of the General Division in a civil cause …` [function, scja2-part5-ca-civil.l4] | 8 |  |
| `s 53(2)(b)` (2994) | (b) any appeal from the Appellate Division; | encoded | `s 53(2)(b) the matter is an appeal from the Appellate Division` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 53(2)(c)` (2996-2998) | (c) any appeal or other process that any written law provide | encoded | `s 53(2)(c) the matter is an appeal or other process that lies, or is transferred, to the Court …` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 53(2)(d)` (3000-3020) | (d) any application (whether made to the General Division, t | encoded | `s 53(2)(d) the matter is an application to which either or both of the criminal-link limbs apply` [function, scja2-part5-ca-civil.l4] | 6 |  |
| `s 53(2)(d)(i)` (3004-3006) | (i) a common question of law or fact arises in both the | encoded | `s 53(2)(d)(i) the application raises a common question with a matter in the criminal jurisdicti…` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 53(2)(d)(ii)` (3013-3020) | (ii) any relief claimed in the application — | encoded | by the rows below |  |  |
| `s 53(2)(d)(ii)(A)` (3015-3016) | (A) may affect any matter falling within the | encoded | `s 53(2)(d)(ii)(A) the relief claimed may affect a matter in the criminal jurisdiction` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 53(2)(d)(ii)(B)` (3018-3020) | (B) may affect the outcome of any matter falling | encoded | `s 53(2)(d)(ii)(B) the relief claimed may affect the outcome of a matter in the criminal jurisdi…` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 54` (3026-3051) | 54.—(1) Despite section 50(1), a case before the Court of Ap | encoded | by the rows below |  |  |
| `s 54(1)` (3026-3031) | 54.—(1) Despite section 50(1), a case before the Court of Ap | fork (fork F10, F12) | `s 54(1) the case may be heard and decided by that number of Judges` [function, scja2-part5-ca-civil.l4] | 11 | yes (1) |
| `s 54(1)(a)` (3029) | (a) either a single Judge or 2 Judges; or | encoded | covered by the `s 54(1)` definition above |  |  |
| `s 54(1)(b)` (3031) | (b) 2 Judges. | encoded | covered by the `s 54(1)` definition above |  |  |
| `s 54(2)` (3035-3037) | (2) A Judge must not sit in the Court of Appeal to hear or d | encoded | `s 54(2) the Judge may sit in the Court of Appeal to hear or decide the application` [function, scja2-part5-ca-civil.l4]; `s 54(2) party` [type, scja2-part5-ca-civil.l4]; `s 54(2) the Judge who made the direction or order` [constructor, scja2-part5-ca-civil.l4]; `s 54(2) act` [type, scja2-part5-ca-civil.l4]; and 2 more with the same label | 2 | yes (1) |
| `s 54(3)` (3041-3051) | (3) Where the Court of Appeal is constituted by 3 or more Ju | fork (fork F16) | by the rows below |  |  |
| `s 54(3)(a)` (3046-3048) | (a) the Court of Appeal must continue to hear and decide the | encoded | `s 54(3)(a) the Court of Appeal must continue to hear and decide the case` [function, scja2-part5-ca-civil.l4] | 6 | yes (1) |
| `s 54(3)(b)` (3050-3051) | (b) the case must be reheard if it cannot continue under | encoded | `s 54(3)(b) the case must be reheard` [function, scja2-part5-ca-civil.l4] | 6 | yes (1) |
| `s 55` (3057-3082) | 55.—(1) Subject to subsection (2), the Court of Appeal may d | encoded | by the rows below |  |  |
| `s 55(1)` (3057-3059) | 55.—(1) Subject to subsection (2), the Court of Appeal may d | fork (fork F13) | `s 55(1) the Court of Appeal may decide the matter without hearing oral arguments` [function, scja2-part5-ca-civil.l4] | 2 | yes (1) |
| `s 55(2)` (3066-3068) | (2) Subsection (1) does not allow any part of a proceeding w | fork (fork F8) | `s 55(2) the part of the proceeding where oral evidence is given may be conducted without an ora…` [function, scja2-part5-ca-civil.l4]; `s 55(2) the bar on conducting the part of the proceeding without an oral hearing applies` [function, scja2-part5-ca-civil.l4] | 8 |  |
| `s 55(3)` (3070-3074) | (3) Subject to subsection (4), the Court of Appeal may, in a | encoded | `s 55(3) the Court of Appeal may direct that the matter be heard in an asynchronous manner by ex…` [function, scja2-part5-ca-civil.l4] | 2 | yes (1) |
| `s 55(4)` (3076-3078) | (4) The Court of Appeal must not hear a matter in an asynchr | fork (fork F8) | `s 55(4) the bar on hearing the matter in an asynchronous manner applies to the Court of Appeal` [function, scja2-part5-ca-civil.l4]; `s 55(4) party` [type, scja2-part5-ca-civil.l4]; `s 55(4) the Court of Appeal` [constructor, scja2-part5-ca-civil.l4]; `s 55(4) act` [type, scja2-part5-ca-civil.l4]; and 2 more with the same label | 2 |  |
| `s 55(5)` (3080-3082) | (5) To avoid doubt, this section does not affect the power o | encoded | `s 55(5) the Court of Appeal may hear oral arguments before deciding the matter` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 56` (3088-3128) | 56.—(1) The Court of Appeal may summarily dismiss any appeal | encoded | by the rows below |  |  |
| `s 56(1)` (3088-3101) | 56.—(1) The Court of Appeal may summarily dismiss any appeal | encoded | `s 56(1) the Court of Appeal may summarily dismiss the appeal or application on its own motion` [function, scja2-part5-ca-civil.l4] | 5 | yes (1) |
| `s 56(1)(a)` (3092-3093) | (a) the Court of Appeal does not have the jurisdiction to he | encoded | covered by the `s 56(1)` definition above |  |  |
| `s 56(1)(b)` (3095-3098) | (b) the Court of Appeal has already decided every issue in t | encoded | covered by the `s 56(1)` definition above |  |  |
| `s 56(1)(c)` (3100-3101) | (c) such conditions as may be prescribed by the Rules of Cou | encoded | covered by the `s 56(1)` definition above |  |  |
| `s 56(2)` (3105-3118) | (2) Before summarily dismissing any appeal or application un | fork (fork F11) | `s 56(2) the Court of Appeal has met the requirements before summarily dismissing, as the sectio…` [function, scja2-part5-ca-civil.l4]; `s 56(2) party` [type, scja2-part5-ca-civil.l4]; `s 56(2) the Court of Appeal` [constructor, scja2-part5-ca-civil.l4]; `s 56(2) act` [type, scja2-part5-ca-civil.l4]; and 1 more with the same label | 3 | yes (1) |
| `s 56(2)(a)` (3108-3110) | (a) give the appellant or applicant a reasonable opportunity | encoded | `s 56(2)(a) gives the appellant or applicant a reasonable opportunity to show cause` [constructor, scja2-part5-ca-civil.l4] | 0 |  |
| `s 56(2)(b)` (3117-3118) | (b) consider any representations made by the appellant or | encoded | `s 56(2)(b) considers the representations made` [constructor, scja2-part5-ca-civil.l4] | 0 |  |
| `s 56(3)` (3122-3123) | (3) The Court of Appeal may exercise its powers under this s | encoded | `s 56(3) the Court of Appeal may exercise its powers under this section without hearing oral arg…` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 56(4)` (3127-3128) | (4) In this section, “appeal” includes part of an appeal and | encoded | `s 56(4) the thing is an appeal or an application for the purposes of this section` [function, scja2-part5-ca-civil.l4] | 4 |  |
| `s 57` (3134-3135) | 57. Where an application may be made either to the Court of | encoded | `s 57 the application must first be made to the other court` [function, scja2-part5-ca-civil.l4]; `s 57 the court to which the application must first be made` [function, scja2-part5-ca-civil.l4] | 5 | yes (1) |
| `s 58` (3141-3187) | 58.—(1) The Court of Appeal may make one or more of the | encoded | by the rows below |  |  |
| `s 58(1)` (3141-3153) | 58.—(1) The Court of Appeal may make one or more of the | encoded | `s 58(1) kind of direction or order` [type, scja2-part5-ca-civil.l4]; `s 58(1) another direction or order` [constructor, scja2-part5-ca-civil.l4]; `s 58(1) the Court of Appeal may make the direction or order in the pending matter` [function, scja2-part5-ca-civil.l4] | 7 | yes (1) |
| `s 58(1)(a)` (3145-3146) | (a) any direction or order incidental to the pending matter  | encoded | `s 58(1)(a) a direction or order incidental to the pending matter not involving the decision of …` [constructor, scja2-part5-ca-civil.l4] | 3 |  |
| `s 58(1)(b)` (3148-3149) | (b) any interim order to prevent prejudice to the claims of  | encoded | `s 58(1)(b) an interim order to prevent prejudice to the claims of the parties pending the deter…` [constructor, scja2-part5-ca-civil.l4] | 2 |  |
| `s 58(1)(c)` (3151-3153) | (c) any order for security for costs, and for the dismissal  | encoded | `s 58(1)(c) an order for security for costs, or for the dismissal of the pending matter for defa…` [constructor, scja2-part5-ca-civil.l4] | 2 |  |
| `s 58(2)` (3157-3158) | (2) A direction or an order under subsection (1) may be made | encoded | `s 58(2) the Court of Appeal may make the direction or order on its own motion or on the applica…` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 58(3)` (3162-3163) | (3) A direction or an order under subsection (1) may be made | encoded | `s 58(3) the direction or order may be made by that number of Judges` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 58(4)` (3167-3181) | (4) A direction or an order under subsection (1) may also be | encoded | `s 58(4) the direction or order may be made by a single Judge` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 58(4)(a)` (3175-3176) | (a) the direction or order may be varied or discharged by | encoded | `s 58(4)(a) the direction or order may be varied or discharged by those Judges` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 58(4)(b)` (3178-3181) | (b) an application to vary or discharge the direction or ord | encoded | `s 58(4)(b) an application to vary or discharge the direction or order may be made` [function, scja2-part5-ca-civil.l4]; `s 58(4)(b) the decision to give or refuse permission is final` [function, scja2-part5-ca-civil.l4] | 5 | yes (2) |
| `s 58(5)` (3187) | (5) Subsections (3) and (4) apply despite section 50(1). | encoded | `s 58(5) section 50(1) does not stand in the way of the direction or order` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59` (3193-3297) | 59.—(1) Appeals to the Court of Appeal are to be by way of | encoded | by the rows below |  |  |
| `s 59(1)` (3193-3194) | 59.—(1) Appeals to the Court of Appeal are to be by way of | encoded | `s 59(1) the appeal is by way of rehearing` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59(2)` (3198-3200) | (2) In hearing and deciding an appeal, the Court of Appeal h | encoded | `s 59(2) the Court of Appeal has the power or duty of the court or tribunal from which the appea…` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 59(3)` (3204-3213) | (3) The Court of Appeal may receive further evidence — | encoded | `s 59(3) manner of receiving further evidence` [type, scja2-part5-ca-civil.l4]; `s 59(3) in a manner that the Court of Appeal does not allow` [constructor, scja2-part5-ca-civil.l4]; `s 59(3) the Court of Appeal may receive further evidence in that manner` [function, scja2-part5-ca-civil.l4] | 6 |  |
| `s 59(3)(a)` (3206) | (a) by oral examination in court; | encoded | `s 59(3)(a) by oral examination in court` [constructor, scja2-part5-ca-civil.l4] | 1 |  |
| `s 59(3)(b)` (3208) | (b) by affidavit; | encoded | `s 59(3)(b) by affidavit` [constructor, scja2-part5-ca-civil.l4] | 1 |  |
| `s 59(3)(c)` (3210-3211) | (c) by deposition taken before an examiner or a commissioner | encoded | `s 59(3)(c) by deposition taken before an examiner or a commissioner` [constructor, scja2-part5-ca-civil.l4] | 1 |  |
| `s 59(3)(d)` (3213) | (d) in any other manner that the Court of Appeal allows. | encoded | `s 59(3)(d) in any other manner that the Court of Appeal allows` [constructor, scja2-part5-ca-civil.l4] | 1 |  |
| `s 59(4)` (3217-3219) | (4) Except as provided in subsection (5), such further evide | fork (fork F8) | `s 59(4) the further evidence may be given to the Court of Appeal` [function, scja2-part5-ca-civil.l4]; `s 59(4) the bar on giving the further evidence to the Court of Appeal applies` [function, scja2-part5-ca-civil.l4] | 10 | yes (1) |
| `s 59(5)` (3225-3227) | (5) Such further evidence may be given to the Court of Appea | encoded | `s 59(5) the further evidence may be given to the Court of Appeal without permission` [function, scja2-part5-ca-civil.l4] | 2 | yes (1) |
| `s 59(6)` (3238-3239) | (6) The Court of Appeal may draw any inference of fact, give | encoded | `s 59(6) the Court of Appeal may draw any inference of fact, give any judgment and make any order` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59(7)` (3243-3252) | (7) The powers in this section — | encoded | by the rows below |  |  |
| `s 59(7)(a)` (3245-3247) | (a) may be exercised in relation to any part of the decision | encoded | `s 59(7)(a) the power may be exercised in relation to that part of the decision appealed against` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59(7)(b)` (3249-3252) | (b) may be exercised in favour of any party to the decision | encoded | `s 59(7)(b) the power may be exercised in favour of that party` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59(8)` (3256-3260) | (8) Where an application for permission to adduce further ev | encoded | `s 59(8) a party may request the full panel to rehear arguments on the application for permissio…` [function, scja2-part5-ca-civil.l4]; `s 59(8) party` [type, scja2-part5-ca-civil.l4]; `s 59(8) a party to the appeal` [constructor, scja2-part5-ca-civil.l4]; `s 59(8) act` [type, scja2-part5-ca-civil.l4]; and 2 more with the same label | 2 | yes (1) |
| `s 59(9)` (3264-3272) | (9) No request may be made under subsection (8) in respect o | fork (fork F8) | `s 59(9) the bar on a request under subsection (8) applies` [function, scja2-part5-ca-civil.l4] | 6 | yes (1) |
| `s 59(9)(a)` (3269-3270) | (a) by 2 Judges, where the Court of Appeal hearing the appea | encoded | covered by the `s 59(9)` definition above |  |  |
| `s 59(9)(b)` (3272) | (b) by 3 or more Judges. | encoded | covered by the `s 59(9)` definition above |  |  |
| `s 59(10)` (3276-3285) | (10) A request under subsection (8) must be made before the  | fork (fork F3) | `s 59(10) the request under subsection (8) is made in time` [function, scja2-part5-ca-civil.l4] | 6 | yes (1) |
| `s 59(10)(a)` (3279-3281) | (a) the time at which the judgment or order relating to the | encoded | `s 59(10)(a) the request is made before the time at which the judgment or order is extracted` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 59(10)(b)` (3283-3285) | (b) the expiration of 7 days after the date on which the dec | fork (fork F3) | `s 59(10)(b) the last day of the 7 days after the date on which the decision is made` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 59(11)` (3294-3297) | (11) After rehearing arguments on a request mentioned in | encoded | `s 59(11) the Court of Appeal may affirm, vary or set aside the decision on the application for …` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 60` (3303-3304) | 60. The Court of Appeal may make any order as to the costs o | encoded | `s 60 the Court of Appeal may make the order as to costs` [function, scja2-part5-ca-civil.l4] | 2 | yes (1) |
| `s 60A` (3310-3343) | 60A.—(1) Subject to this Act, the Court of Appeal may order  | encoded | by the rows below |  |  |
| `s 60A(1)` (3310-3319) | 60A.—(1) Subject to this Act, the Court of Appeal may order  | encoded | by the rows below |  | yes (1) |
| `s 60A(1)(a)` (3313-3315) | (a) any matter that has been tried by the General Division i | fork (fork F1, F14) | `s 60A(1)(a) the Court of Appeal may order a new trial of a matter tried by the General Division` [function, scja2-part5-ca-civil.l4] | 7 |  |
| `s 60A(1)(b)` (3317-3319) | (b) any matter that has been tried by the Appellate Division | fork (fork F14) | `s 60A(1)(b) the Court of Appeal may order a new trial of a matter tried by the Appellate Divisi…` [function, scja2-part5-ca-civil.l4] | 3 |  |
| `s 60A(2)` (3323-3325) | (2) A new trial must not be ordered on the ground of an impr | fork (fork F8) | `s 60A(2) a new trial may be ordered on that ground` [function, scja2-part5-ca-civil.l4]; `s 60A(2) the bar on a new trial on that ground applies` [function, scja2-part5-ca-civil.l4] | 6 | yes (1) |
| `s 60A(3)` (3329-3337) | (3) If the substantial wrong or miscarriage of justice menti | encoded | by the rows below |  |  |
| `s 60A(3)(a)` (3333-3334) | (a) give final judgment in respect of the unaffected part of | encoded | `s 60A(3)(a) the Court of Appeal may give final judgment in respect of the unaffected part of th…` [function, scja2-part5-ca-civil.l4] | 2 | yes (1) |
| `s 60A(3)(b)` (3336-3337) | (b) direct a new trial in respect of the affected part of th | encoded | `s 60A(3)(b) the Court of Appeal may direct a new trial in respect of the affected part of the c…` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 60A(4)` (3341-3343) | (4) A new trial may be ordered on any question without inter | encoded | `s 60A(4) the new trial may be ordered on that question without interfering with the finding or …` [function, scja2-part5-ca-civil.l4] | 2 |  |
| `s 60B` (3354-3358) | 60B. The Court of Appeal may not reverse or substantially va | encoded | `s 60B the Court of Appeal may reverse or substantially vary the decision, or order a new trial,…` [function, scja2-part5-ca-civil.l4]; `s 60B party` [type, scja2-part5-ca-civil.l4]; `s 60B the Court of Appeal` [constructor, scja2-part5-ca-civil.l4]; `s 60B act` [type, scja2-part5-ca-civil.l4]; and 2 more with the same label | 3 | yes (1) |
| `s 60C` (3364-3374) | 60C.—(1) An appeal to the Court of Appeal does not operate a | encoded | by the rows below |  |  |
| `s 60C(1)` (3364-3367) | 60C.—(1) An appeal to the Court of Appeal does not operate a | fork (fork F8) | `s 60C(1) the appeal operates as a stay of execution or enforcement or of proceedings under the …` [function, scja2-part5-ca-civil.l4]; `s 60C(1) the rule that the appeal does not operate as a stay applies` [function, scja2-part5-ca-civil.l4] | 4 | yes (1) |
| `s 60C(2)` (3373-3374) | (2) No intermediate act or proceeding is to be invalidated e | fork (fork F8) | `s 60C(2) the intermediate act or proceeding is invalidated` [function, scja2-part5-ca-civil.l4]; `s 60C(2) the rule that no intermediate act or proceeding is invalidated applies` [function, scja2-part5-ca-civil.l4] | 4 | yes (1) |
| `s 60D` (3384-3418) | 60D. The criminal jurisdiction of the Court of Appeal consis | fork (fork F15) | `s 60D kind of matter` [type, scja2-part5-ca-criminal.l4]; `s 60D another kind of matter` [constructor, scja2-part5-ca-criminal.l4]; `s 60D the matter is one of the matters of the criminal jurisdiction of the Court of Appeal` [function, scja2-part5-ca-criminal.l4] | 9 |  |
| `s 60D(a)` (3389-3390) | (a) any appeal against any decision made by the General | encoded | `s 60D(a) an appeal against a decision made by the General Division in the exercise of its origi…` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(b)` (3392-3393) | (b) any petition for confirmation under Division 1A of Part  | encoded | `s 60D(b) a petition for confirmation under Division 1A of Part 20 of the Criminal Procedure Cod…` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(c)` (3395-3397) | (c) any review of a decision of the Court of Appeal, or a | encoded | `s 60D(c) a review of a decision of the Court of Appeal, or a decision of the General Division, …` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(d)` (3399-3400) | (d) any case stated to the Court of Appeal under section 395 | encoded | `s 60D(d) a case stated to the Court of Appeal under section 395 or 396 of the Criminal Procedur…` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(e)` (3407-3408) | (e) any reference to the Court of Appeal under section 397 o | encoded | `s 60D(e) a reference to the Court of Appeal under section 397 of the Criminal Procedure Code 20…` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(f)` (3410-3411) | (f) any motion to the Court of Appeal under Division 5 of | encoded | `s 60D(f) a motion to the Court of Appeal under Division 5 of Part 20 of the Criminal Procedure …` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60D(g)` (3417-3418) | (g) any reference to the Court of Appeal under section 18 of | encoded | `s 60D(g) a reference to the Court of Appeal under section 18 of the Extradition Act 1968` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60E` (3424-3446) | 60E.—(1) Despite section 50(1), a case before the Court of A | encoded | by the rows below |  |  |
| `s 60E(1)` (3424-3426) | 60E.—(1) Despite section 50(1), a case before the Court of A | fork (fork F12) | `s 60E(1) the case may be heard and determined by that number of Judges despite section 50(1)` [function, scja2-part5-ca-criminal.l4] | 9 |  |
| `s 60E(2)` (3430-3446) | (2) A Judge must not sit in the Court of Appeal to hear or d | encoded | `s 60E(2) kind of matter` [type, scja2-part5-ca-criminal.l4]; `s 60E(2) a matter related to a matter in paragraphs (a) to (d)` [constructor, scja2-part5-ca-criminal.l4]; `s 60E(2) another matter` [constructor, scja2-part5-ca-criminal.l4]; `s 60E(2) the Judge may sit in the Court of Appeal to hear or decide the matter` [function, scja2-part5-ca-criminal.l4]; and 5 more with the same label | 8 |  |
| `s 60E(2)(a)` (3434-3435) | (a) an appeal against a conviction before the Judge or a | encoded | `s 60E(2)(a) an appeal against a conviction before the Judge or a sentence passed by the Judge` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60E(2)(b)` (3437-3439) | (b) any petition for confirmation under Division 1A of Part  | encoded | `s 60E(2)(b) a petition for confirmation under Division 1A of Part 20 of the Criminal Procedure …` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60E(2)(c)` (3441-3442) | (c) any case stated by the Judge under section 395 of the | encoded | `s 60E(2)(c) a case stated by the Judge under section 395 of the Criminal Procedure Code 2010` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60E(2)(d)` (3444-3446) | (d) any reference under section 397 of the Criminal Procedur | encoded | `s 60E(2)(d) a reference under section 397 of the Criminal Procedure Code 2010 of a question of …` [constructor, scja2-part5-ca-criminal.l4] | 1 |  |
| `s 60F` (3462-3599) | 60F. In this Division, unless the context otherwise requires | encoded | by the rows below |  |  |
| `s 60F chapeau` (3462) | 60F. In this Division, unless the context otherwise requires | encoded | `s 60F chapeau the definitions of this Division apply in this use` [function, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "application for PACC permission"` (3464-3465) | “application for PACC permission” means an application for | encoded | `s 60F "application for PACC permission" the application is an application for PACC permission` [function, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "application for review permission"` (3467-3468) | “application for review permission” means an application for | encoded | `s 60F "application for review permission" the application is an application for review permissi…` [function, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "counsel"` (3470) | “counsel” means any advocate and solicitor; | encoded | `s 60F "counsel" the person is counsel` [function, scja2-part5-ca-capital-defs.l4] | 3 |  |
| `s 60F "Judge of the Court of Appeal"` (3472-3474) | “Judge of the Court of Appeal” means a Judge sitting in the | encoded | `s 60F "Judge of the Court of Appeal" the Judge is a Judge of the Court of Appeal` [function, scja2-part5-ca-capital-defs.l4] | 3 |  |
| `s 60F "PACP"` (3476) | “PACP” means a prisoner awaiting capital punishment; | encoded | `s 60F "PACP" the person is a PACP` [function, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "post-appeal application in a capital case"` (3478-3493) | “post-appeal application in a capital case” or “PACC | encoded | `s 60F "post-appeal application in a capital case" the application is a PACC application` [function, scja2-part5-ca-capital-defs.l4] | 9 |  |
| `s 60F "post-appeal application in a capital case"(a)` (3482) | (a) made by a PACP after the relevant date; and | encoded | covered by the `s 60F "post-appeal application in a capital case"` definition above |  |  |
| `s 60F "post-appeal application in a capital case"(b)` (3484-3493) | (b) to which either of the following applies: | encoded | by the rows below |  |  |
| `s 60F "post-appeal application in a capital case"(b)(i)` (3486-3487) | (i) the application is for a stay of the execution of | encoded | covered by the `s 60F "post-appeal application in a capital case"` definition above |  |  |
| `s 60F "post-appeal application in a capital case"(b)(ii)` (3489-3493) | (ii) the determination of the application calls into | encoded | `s 60F "post-appeal application in a capital case"(b)(ii) the determination calls into question …` [function, scja2-part5-ca-capital-defs.l4] | 7 |  |
| `s 60F Examples` (3495-3526) | Examples | encoded | `s 60F Examples kind of application` [type, scja2-part5-ca-capital-defs.l4]; `s 60F Examples another application` [constructor, scja2-part5-ca-capital-defs.l4]; `s 60F Examples the application is an example of an application made by a PACP whose determinati…` [function, scja2-part5-ca-capital-defs.l4] | 9 |  |
| `s 60F Examples(a)` (3502) | (a) an application challenging the President’s order; | encoded | `s 60F Examples(a) an application challenging the President's order` [constructor, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F Examples(b)` (3504-3505) | (b) an application challenging the manner in which the death | encoded | `s 60F Examples(b) an application challenging the manner in which the death sentence is to be ca…` [constructor, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F Examples(c)` (3507-3516) | (c) an application challenging the imposition of the sentenc | encoded | `s 60F Examples(c) an application challenging the imposition of the sentence of death as a form …` [constructor, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F Examples(d)` (3518-3522) | (d) an application challenging the Public Prosecutor’s decis | encoded | `s 60F Examples(d) an application challenging the Public Prosecutor's decision not to certify th…` [constructor, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F Examples(e)` (3524-3526) | (e) an application challenging the Public Prosecutor’s decis | encoded | `s 60F Examples(e) an application challenging the Public Prosecutor's decision to institute and …` [constructor, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "President’s order"` (3528-3531) | “President’s order”, in relation to a PACP, means the order  | encoded | `s 60F "President's order" the order is the President's order` [function, scja2-part5-ca-capital-defs.l4] | 2 |  |
| `s 60F "relevant application"` (3533-3541) | “relevant application” means — | encoded | `s 60F "relevant application" kind of application` [type, scja2-part5-ca-capital-defs.l4]; `s 60F "relevant application" another application` [constructor, scja2-part5-ca-capital-defs.l4]; `s 60F "relevant application" the application is a relevant application` [function, scja2-part5-ca-capital-defs.l4] | 6 |  |
| `s 60F "relevant application"(a)` (3535) | (a) an application for PACC permission; | encoded | `s 60F "relevant application"(a) an application for PACC permission` [constructor, scja2-part5-ca-capital-defs.l4] | 1 |  |
| `s 60F "relevant application"(b)` (3537) | (b) a PACC application; | encoded | `s 60F "relevant application"(b) a PACC application` [constructor, scja2-part5-ca-capital-defs.l4] | 1 |  |
| `s 60F "relevant application"(c)` (3539) | (c) an application for review permission; or | encoded | `s 60F "relevant application"(c) an application for review permission` [constructor, scja2-part5-ca-capital-defs.l4] | 1 |  |
| `s 60F "relevant application"(d)` (3541) | (d) a review application; | encoded | `s 60F "relevant application"(d) a review application` [constructor, scja2-part5-ca-capital-defs.l4] | 1 |  |
| `s 60F "relevant date"` (3543-3593) | “relevant date” means — | encoded | `s 60F "relevant date" the relevant date` [function, scja2-part5-ca-capital-defs.l4]; `s 60F "relevant date" it is made after the relevant date` [function, scja2-part5-ca-capital-defs.l4] | 14 |  |
| `s 60F "relevant date"(a)` (3545-3575) | (a) in relation to the first PACC application by a | fork (fork F19) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(a)(i)` (3548-3553) | (i) the date of dismissal of the appeal by the Court | encoded | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(a)(ii)` (3555-3568) | (ii) the date of imposition of the sentence of death | encoded | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(a)(iii)` (3570-3575) | (iii) the date of the issuance by the Court of Appeal | encoded | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)` (3577-3593) | (b) in relation to the second or any subsequent PACC | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)(i)` (3581) | (i) the date mentioned in paragraph (a); or | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)(ii)` (3583-3590) | (ii) if prior to the making of the instant application, | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)(ii)(A)` (3586-3588) | (A) any application for PACC permission | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)(ii)(B)` (3590) | (B) any PACC application, | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "relevant date"(b)(ii) [second, as printed]` (3592-3593) | (ii) in relation to the PACP, the date of the most | fork (fork F4) | covered by the `s 60F "relevant date"` definition above |  |  |
| `s 60F "review application"` (3595-3599) | “review application” means a review application within the | encoded | `s 60F "review application" the application is a review application` [function, scja2-part5-ca-capital-defs.l4] | 3 |  |
| `s 60G` (3605-3745) | 60G.—(1) Subject to section 60I, before making a PACC | encoded | by the rows below |  |  |
| `s 60G(1)` (3605-3607) | 60G.—(1) Subject to section 60I, before making a PACC | fork (fork F8, F11) | `s 60G(1) the applicant has obtained the permission of the Court of Appeal before making the PAC…` [function, scja2-part5-ca-capital.l4]; `s 60G(1) party` [type, scja2-part5-ca-capital.l4]; `s 60G(1) the applicant` [constructor, scja2-part5-ca-capital.l4]; `s 60G(1) act` [type, scja2-part5-ca-capital.l4]; and 3 more with the same label | 4 |  |
| `s 60G(2)` (3609-3610) | (2) Despite section 50(1), an application for PACC permissio | encoded | `s 60G(2) the application for PACC permission may be heard and determined by a single Judge of t…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(3)` (3617-3618) | (3) An application for PACC permission must be fixed for hea | fork (fork F11) | `s 60G(3) the application for PACC permission is fixed for hearing within the prescribed period,…` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60G(4)` (3620-3623) | (4) The applicant in an application for PACC permission must | fork (fork F11) | `s 60G(4) the applicant files the written submissions and other documents within the prescribed …` [function, scja2-part5-ca-capital.l4]; `s 60G(4) party` [type, scja2-part5-ca-capital.l4]; `s 60G(4) the applicant in an application for PACC permission` [constructor, scja2-part5-ca-capital.l4]; `s 60G(4) act` [type, scja2-part5-ca-capital.l4]; and 2 more with the same label | 3 |  |
| `s 60G(5)` (3625-3627) | (5) The respondent in an application for PACC permission may | encoded | `s 60G(5) the respondent files written submissions within the prescribed period` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60G(6)` (3629-3630) | (6) The Registrar or any Supreme Court Judge may extend or | encoded | `s 60G(6) the person may extend or abridge the period` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60G(7)` (3632-3648) | (7) In deciding whether or not to grant an application for P | fork (fork F11) | `s 60G(7) the Court of Appeal has considered the matters it must consider in deciding whether to…` [function, scja2-part5-ca-capital.l4] | 5 |  |
| `s 60G(7)(a)` (3635-3638) | (a) whether the PACC application to be made is based on | encoded | covered by the `s 60G(7)` definition above |  |  |
| `s 60G(7)(b)` (3640-3643) | (b) whether there was any delay in filing the application fo | encoded | covered by the `s 60G(7)` definition above |  |  |
| `s 60G(7)(c)` (3645) | (c) whether subsection (4) is complied with; | encoded | covered by the `s 60G(7)` definition above |  |  |
| `s 60G(7)(d)` (3647-3648) | (d) whether the PACC application to be made has a reasonable | encoded | covered by the `s 60G(7)` definition above |  |  |
| `s 60G(8)` (3650-3652) | (8) An application for PACC permission may, without being se | encoded | `s 60G(8) the application for PACC permission may be summarily dealt with by a written order wit…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(9)` (3654-3667) | (9) Before summarily refusing an application for PACC permis | encoded | by the rows below |  |  |
| `s 60G(9)(a)` (3658-3659) | (a) must consider the applicant’s written submissions, if an | fork (fork F11) | `s 60G(9)(a) the Court of Appeal has considered the applicant's written submissions before summa…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(9)(b)` (3666-3667) | (b) may, but is not required to, consider the respondent’s | encoded | `s 60G(9)(b) the Court of Appeal is required to consider the respondent's written submissions be…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(10)` (3669-3676) | (10) Before summarily granting an application for PACC | encoded | by the rows below |  |  |
| `s 60G(10)(a)` (3673-3674) | (a) must consider the applicant’s written submissions, if an | fork (fork F11) | `s 60G(10)(a) the Court of Appeal has considered the applicant's written submissions before summ…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(10)(b)` (3676) | (b) must consider the respondent’s written submissions, if a | fork (fork F11) | `s 60G(10)(b) the Court of Appeal has considered the respondent's written submissions before sum…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(11)` (3678-3693) | (11) The Court of Appeal may — | fork (fork F9) | `s 60G(11) stage` [type, scja2-part5-ca-capital.l4]; `s 60G(11) at another stage` [constructor, scja2-part5-ca-capital.l4]; `s 60G(11) measure` [type, scja2-part5-ca-capital.l4]; `s 60G(11) another measure` [constructor, scja2-part5-ca-capital.l4]; and 1 more with the same label | 10 |  |
| `s 60G(11)(a)` (3680) | (a) before deciding any application for PACC permission; | encoded | `s 60G(11)(a) before deciding any application for PACC permission` [constructor, scja2-part5-ca-capital.l4] | 7 |  |
| `s 60G(11)(b)` (3682) | (b) when granting an application for PACC permission; or | encoded | `s 60G(11)(b) when granting an application for PACC permission` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60G(11)(c)` (3684-3687) | (c) when summarily granting an application for PACC | encoded | `s 60G(11)(c) when summarily granting an application for PACC permission` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60G(11)(d)` (3689-3691) | (d) make any incidental directions or give any interim order | encoded | `s 60G(11)(d) making an incidental direction or giving an interim order, including a stay of exe…` [constructor, scja2-part5-ca-capital.l4] | 6 |  |
| `s 60G(11)(e)` (3693) | (e) take additional evidence. | encoded | `s 60G(11)(e) taking additional evidence` [constructor, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60G(12)` (3695-3705) | (12) The Court of Appeal may, if it thinks additional eviden | encoded | by the rows below |  |  |
| `s 60G(12)(a)` (3698-3700) | (a) where the application for PACC permission is dealt with  | fork (fork F18) | `s 60G(12)(a) the Court of Appeal may take the evidence itself where a single Judge deals with t…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60G(12)(b)` (3702-3705) | (b) where the application for PACC permission is dealt with  | encoded | `s 60G(12)(b) the Court of Appeal may either take the evidence itself or have it taken by one of…` [function, scja2-part5-ca-capital.l4] | 5 |  |
| `s 60G(13)` (3707-3709) | (13) If the Court of Appeal does not grant the application f | fork (fork F8) | `s 60G(13) the bar on further proceedings in respect of the PACC application applies` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(14)` (3716-3718) | (14) Subsection (13) does not prevent the taking of any proc | encoded | `s 60G(14) subsection (13) prevents the proceedings` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60G(15)` (3720-3745) | (15) Despite any provision in this section, if an applicatio | fork (fork F8, F19) | `s 60G(15) the Court of Appeal may grant the application for PACC permission` [function, scja2-part5-ca-capital.l4]; `s 60G(15) the bar on granting the application for PACC permission applies` [function, scja2-part5-ca-capital.l4]; `s 60G(15) party` [type, scja2-part5-ca-capital.l4]; `s 60G(15) the Court of Appeal` [constructor, scja2-part5-ca-capital.l4]; and 3 more with the same label | 11 |  |
| `s 60G(15)(a)` (3724-3727) | (a) to have abused the process of the court in relation to a | encoded | covered by the `s 60G(15)` definition above |  |  |
| `s 60G(15)(b)` (3729-3736) | (b) to have abused the process of the court in order to dela | fork (fork F13, F19) | covered by the `s 60G(15)` definition above |  |  |
| `s 60G(15)(c)` (3738-3741) | (c) the PACP adduces material (being evidence or legal | encoded | covered by the `s 60G(15)` definition above |  |  |
| `s 60G(15)(d)` (3743-3745) | (d) the material could not, even with reasonable diligence, | encoded | covered by the `s 60G(15)` definition above |  |  |
| `s 60H` (3751-3820) | 60H.—(1) Subject to section 60I, where the Court of Appeal g | encoded | by the rows below |  |  |
| `s 60H(1)` (3751-3754) | 60H.—(1) Subject to section 60I, where the Court of Appeal g | fork (fork F8, F11) | `s 60H(1) the PACC application is made to the Court of Appeal and fixed for hearing within the p…` [function, scja2-part5-ca-capital.l4] | 5 |  |
| `s 60H(2)` (3756-3758) | (2) The applicant in a PACC application must file such docum | fork (fork F11) | `s 60H(2) the applicant files the documents in support within the prescribed period, as the sect…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60H(3)` (3765-3767) | (3) The respondent in a PACC application must file such docu | fork (fork F11) | `s 60H(3) the respondent files the documents in relation to the application within the prescribe…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60H(4)` (3769-3770) | (4) The Registrar or any Supreme Court Judge may extend or | encoded | `s 60H(4) the person may extend or abridge the period` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60H(5)` (3772-3775) | (5) The Court of Appeal which hears a PACC application may | encoded | `s 60H(5) the Court of Appeal may exercise the power and make the order` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60H(6)` (3777-3778) | (6) A PACC application may, without being set down for heari | encoded | `s 60H(6) the PACC application may be summarily dealt with by a written order without being set …` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60H(7)` (3780-3787) | (7) Before summarily refusing a PACC application under | encoded | by the rows below |  |  |
| `s 60H(7)(a)` (3783-3784) | (a) must consider the applicant’s written submissions, if an | fork (fork F11) | `s 60H(7)(a) the Court of Appeal has considered the applicant's written submissions before summa…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60H(7)(b)` (3786-3787) | (b) may, but is not required to, consider the respondent’s | encoded | `s 60H(7)(b) the Court of Appeal is required to consider the respondent's written submissions be…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60H(8)` (3789-3795) | (8) Except where subsection (7) applies, before summarily de | fork (fork F8, F11) | `s 60H(8) the Court of Appeal has considered both sets of written submissions before summarily d…` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60H(8)(a)` (3792-3793) | (a) must consider the applicant’s written submissions, if an | encoded | covered by the `s 60H(8)` definition above |  |  |
| `s 60H(8)(b)` (3795) | (b) must consider the respondent’s written submissions, if a | encoded | covered by the `s 60H(8)` definition above |  |  |
| `s 60H(9)` (3797-3811) | (9) The Court of Appeal may — | fork (fork F9) | `s 60H(9) the Court of Appeal may take the measure at the stage of the PACC application` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60H(9)(a)` (3799) | (a) before deciding a PACC application; | encoded | covered by the `s 60H(9)` definition above |  |  |
| `s 60H(9)(b)` (3801) | (b) when granting a PACC application; or | encoded | covered by the `s 60H(9)` definition above |  |  |
| `s 60H(9)(c)` (3803-3805) | (c) when summarily granting a PACC application, | encoded | covered by the `s 60H(9)` definition above |  |  |
| `s 60H(9)(d)` (3807-3809) | (d) make any incidental directions or give any interim order | encoded | covered by the `s 60H(9)` definition above |  |  |
| `s 60H(9)(e)` (3811) | (e) take additional evidence. | encoded | covered by the `s 60H(9)` definition above |  |  |
| `s 60H(10)` (3818-3820) | (10) The Court of Appeal may, if it thinks additional eviden | encoded | `s 60H(10) the Court of Appeal may either take the evidence itself or have it taken by one of th…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60I` (3827-3856) | 60I.—(1) Where any application for PACC permission, or any | encoded | by the rows below |  |  |
| `s 60I(1)` (3827-3833) | 60I.—(1) Where any application for PACC permission, or any | fork (fork F8) | `s 60I(1) the PACP can make a subsequent application for PACC permission or a subsequent PACC ap…` [function, scja2-part5-ca-capital.l4]; `s 60I(1) the bar on a subsequent application applies to the PACP` [function, scja2-part5-ca-capital.l4]; `s 60I(1) party` [type, scja2-part5-ca-capital.l4]; `s 60I(1) the PACP` [constructor, scja2-part5-ca-capital.l4]; and 3 more with the same label | 8 |  |
| `s 60I(2)` (3835-3846) | (2) The Court of Appeal dealing with the specified applicati | encoded | `s 60I(2) what the Court of Appeal does` [type, scja2-part5-ca-capital.l4]; `s 60I(2) does something else` [constructor, scja2-part5-ca-capital.l4]; `s 60I(2) the Court of Appeal dealing with the specified application may do it` [function, scja2-part5-ca-capital.l4] | 5 |  |
| `s 60I(2)(a)` (3838-3840) | (a) grant permission for the PACP to adduce further material | encoded | `s 60I(2)(a) grants permission for the PACP to adduce further material when dealing with the spe…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60I(2)(b)` (3842-3844) | (b) grant permission for the PACP to make the subsequent | encoded | `s 60I(2)(b) grants permission for the PACP to make the subsequent application separately under …` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60I(2)(c)` (3846) | (c) refuse to grant permission under paragraph (a) or (b). | encoded | `s 60I(2)(c) refuses to grant permission under paragraph (a) or (b)` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60I(3)` (3848-3856) | (3) When dealing with any specified application or subsequen | encoded | `s 60I(3) the Court of Appeal may give the direction` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60I(3)(a)` (3852-3853) | (a) in the case of a specified application — in respect of t | encoded | covered by the `s 60I(3)` definition above |  |  |
| `s 60I(3)(b)` (3855-3856) | (b) in the case of a subsequent application — in respect of  | encoded | covered by the `s 60I(3)` definition above |  |  |
| `s 60J` (3869-3917) | 60J.—(1) Where any application or action by a PACP (called i | encoded | by the rows below |  |  |
| `s 60J(1)` (3869-3874) | 60J.—(1) Where any application or action by a PACP (called i | fork (fork F13) | `s 60J(1) the Court of Appeal may determine whether the specified application is, or the specifi…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60J(2)` (3876-3877) | (2) Despite section 50(1), a determination under subsection  | encoded | `s 60J(2) the determination may be made by a single Judge of the Court of Appeal despite section…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60J(3)` (3879-3890) | (3) If the Court of Appeal makes a determination under | encoded | `s 60J(3) what the Court of Appeal does` [type, scja2-part5-ca-capital.l4]; `s 60J(3) does something else` [constructor, scja2-part5-ca-capital.l4]; `s 60J(3) the Court of Appeal may do it` [function, scja2-part5-ca-capital.l4] | 5 |  |
| `s 60J(3)(a)` (3884-3887) | (a) proceed to determine the specified application, or that  | encoded | `s 60J(3)(a) proceeds to determine the specified application, or that part of the specified acti…` [constructor, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60J(3)(b)` (3889-3890) | (b) strike out the specified application or specified action | encoded | `s 60J(3)(b) strikes out the specified application or specified action, in whole or in part` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60J(4)` (3892-3899) | (4) The Court of Appeal may, in making any determination und | encoded | `s 60J(4) the Court of Appeal may make incidental directions, give interim orders or take additi…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60J(4)(a)` (3895-3897) | (a) make any incidental directions or give any interim order | encoded | covered by the `s 60J(4)` definition above |  |  |
| `s 60J(4)(b)` (3899) | (b) take additional evidence. | encoded | covered by the `s 60J(4)` definition above |  |  |
| `s 60J(5)` (3901-3917) | (5) The Court of Appeal may, if it thinks additional evidenc | encoded | by the rows below |  |  |
| `s 60J(5)(a)` (3904-3906) | (a) where the determination under subsection (1) is being | encoded | `s 60J(5)(a) the Court of Appeal may take the evidence itself where a single Judge makes the det…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60J(5)(b)` (3908-3917) | (b) where the determination under subsection (1) is being | encoded | `s 60J(5)(b) the Court of Appeal may either take the evidence itself or have it taken by one of …` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60K` (3924-3925) | 60K. Nothing in this Division affects the operation of Divis | encoded | `s 60K the provision affects the operation of Division 1B of Part 20 of the Criminal Procedure C…` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60L` (3931-3933) | 60L. Despite anything in this Act or any other written law,  | encoded | `s 60L the court may grant a stay of execution of the death sentence` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60M` (3940-4046) | 60M.—(1) When dealing with any application or action, the Co | encoded | by the rows below |  |  |
| `s 60M(1)` (3940-3953) | 60M.—(1) When dealing with any application or action, the Co | encoded | `s 60M(1) the Court of Appeal may decide whether to make a finding of abuse of process` [function, scja2-part5-ca-capital.l4] | 6 |  |
| `s 60M(1)(a)` (3947-3948) | (a) committed an abuse of process, in the case of a relevant | encoded | `s 60M(1)(a) the finding may be that the person committed an abuse of process in the case of a r…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60M(1)(b)` (3950-3953) | (b) committed an abuse of process in order to delay or frust | fork (fork F13) | `s 60M(1)(b) the finding may be that the person committed an abuse of process in order to delay …` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60M(2)` (3955-4030) | (2) In deciding whether to make a finding under subsection ( | encoded | `s 60M(2) kind of application` [type, scja2-part5-ca-capital.l4]; `s 60M(2) matter` [type, scja2-part5-ca-capital.l4]; `s 60M(2) the matters that the Court of Appeal may take into account for the kind of application` [function, scja2-part5-ca-capital.l4]; `s 60M(2) the Court of Appeal may inquire into and take into account the matter` [function, scja2-part5-ca-capital.l4] | 14 |  |
| `s 60M(2)(a)` (3959-3978) | (a) in relation to an application for PACC permission — | encoded | `s 60M(2)(a) an application for PACC permission` [constructor, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60M(2)(a)(i)` (3961-3970) | (i) whether the PACC application to be made is based on | encoded | `s 60M(2)(a)(i) whether the PACC application to be made is based on material that could not, eve…` [constructor, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60M(2)(a)(ii)` (3972-3975) | (ii) whether there was any delay in filing the application | encoded | `s 60M(2)(a)(ii) whether there was any delay in filing the application for PACC permission after…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(a)(iii)` (3977-3978) | (iii) whether the PACP has complied with | encoded | `s 60M(2)(a)(iii) whether the PACP has complied with section 60G(4)` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(b)` (3980-3993) | (b) in relation to a PACC application — | encoded | `s 60M(2)(b) a PACC application` [constructor, scja2-part5-ca-capital.l4] | 4 |  |
| `s 60M(2)(b)(i)` (3982-3985) | (i) whether the PACC application was based on material | encoded | `s 60M(2)(b)(i) whether the PACC application was based on material that could not, even with rea…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(b)(ii)` (3987-3990) | (ii) whether there was any delay in filing the application | encoded | `s 60M(2)(b)(ii) whether there was any delay in filing the application for PACC permission after…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(b)(iii)` (3992-3993) | (iii) whether the PACP has complied with | encoded | `s 60M(2)(b)(iii) whether the PACP has complied with section 60H(2)` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(c)` (3995-4009) | (c) in relation to an application for review permission — | encoded | `s 60M(2)(c) an application for review permission` [constructor, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60M(2)(c)(i)` (3997-3999) | (i) whether the PACP has complied with the conditions | encoded | `s 60M(2)(c)(i) whether the PACP has complied with the conditions or the requirements in section…` [constructor, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60M(2)(c)(ii)` (4001-4005) | (ii) whether the application for review permission was | encoded | `s 60M(2)(c)(ii) whether the application for review permission was filed within a reasonable tim…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(c)(iii)` (4007-4009) | (iii) whether the PACP has complied with | encoded | `s 60M(2)(c)(iii) whether the PACP has complied with section 394H(3) of the Criminal Procedure C…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(d)` (4016-4030) | (d) in relation to a review application — | encoded | `s 60M(2)(d) a review application` [constructor, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60M(2)(d)(i)` (4018-4020) | (i) whether the PACP has complied with the conditions | encoded | `s 60M(2)(d)(i) whether the PACP has complied with the conditions or the requirements in section…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(d)(ii)` (4022-4027) | (ii) whether the application for review permission | encoded | `s 60M(2)(d)(ii) whether the application for review permission granted in respect of the review …` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(2)(d)(iii)` (4029-4030) | (iii) whether the PACP has complied with section 394I(2) | encoded | `s 60M(2)(d)(iii) whether the PACP has complied with section 394I(2) of the Criminal Procedure C…` [constructor, scja2-part5-ca-capital.l4] | 1 |  |
| `s 60M(3)` (4032-4034) | (3) Despite section 50(1), where a relevant application is h | encoded | `s 60M(3) a finding under subsection (1) may be made by that Judge despite section 50(1)` [function, scja2-part5-ca-capital.l4] | 2 |  |
| `s 60M(4)` (4036-4046) | (4) In deciding whether to make a finding under subsection ( | encoded | by the rows below |  |  |
| `s 60M(4)(a)` (4039-4041) | (a) where the relevant application is being heard by a singl | encoded | `s 60M(4)(a) the Court of Appeal may take the evidence itself where a single Judge hears the rel…` [function, scja2-part5-ca-capital.l4] | 3 |  |
| `s 60M(4)(b)` (4043-4046) | (b) where the relevant application is being heard by 3 or an | encoded | `s 60M(4)(b) the Court of Appeal may either take the evidence itself or have it taken by one of …` [function, scja2-part5-ca-capital.l4] | 4 |  |
| `s 61` (4065-4072) | 61.—(1) The President may, on the recommendation of the Chie | encoded | by the rows below |  |  |
| `s 61(1)` (4065-4067) | 61.—(1) The President may, on the recommendation of the Chie | encoded | `s 61(1) the President may appoint the officer of the Supreme Court` [function, scja2-part6-officers.l4]; `s 61(1) the President may appoint: the recommendation` [function, scja2-part6-officers.l4] | 7 |  |
| `s 61(2)` (4069-4072) | (2) A person must not be appointed to be or to act as the Re | fork (fork F8) | `s 61(2) the person may be appointed to be or to act as the Registrar, the Deputy Registrar or a…` [function, scja2-part6-officers.l4]; `s 61(2) the bar on appointing the person to be or to act as the Registrar, the Deputy Registrar…` [function, scja2-part6-officers.l4] | 4 |  |
| `s 62` (4077-4084) | 62.—(1) The Registrar, the Deputy Registrar and the Assistan | encoded | by the rows below |  |  |
| `s 62(1)` (4077-4080) | 62.—(1) The Registrar, the Deputy Registrar and the Assistan | encoded | `s 62(1) the Registrar, the Deputy Registrar and the Assistant Registrars have the jurisdiction,…` [function, scja2-part6-officers.l4] | 2 |  |
| `s 62(2)` (4082-4084) | (2) Subject to Rules of Court, all the powers and duties con | fork (fork F8) | `s 62(2) the officer may exercise or perform the powers and duties conferred and imposed on the …` [function, scja2-part6-officers.l4] | 5 | yes (1) |
| `s 63` (4093-4098) | 63.—(1) The Registrar is the Sheriff and the Deputy Registra | encoded | by the rows below |  |  |
| `s 63(1)` (4093-4095) | 63.—(1) The Registrar is the Sheriff and the Deputy Registra | encoded | `s 63(1) the office of the Sheriff that the officer holds` [function, scja2-part6-officers.l4]; `s 63(1) the officer is a Sheriff, Deputy Sheriff or Assistant Sheriff of the Supreme Court` [function, scja2-part6-officers.l4] | 8 |  |
| `s 63(2)` (4097-4098) | (2) The Deputy Sheriff and the Assistant Sheriffs have all t | encoded | `s 63(2) the officer has all the powers and privileges and may perform all the duties of the She…` [function, scja2-part6-officers.l4] | 3 |  |
| `s 64` (4107-4133) | 64.—(1) The Sheriff or his or her officers must — | encoded | by the rows below |  |  |
| `s 64(1)` (4107-4118) | 64.—(1) The Sheriff or his or her officers must — | encoded | `s 64(1) party` [type, scja2-part6-officers.l4]; `s 64(1) the Sheriff or the Sheriff's officer` [constructor, scja2-part6-officers.l4]; `s 64(1) act` [type, scja2-part6-officers.l4] | 0 |  |
| `s 64(1)(a)` (4109-4111) | (a) execute all writs, summonses, rules, orders, warrants, | encoded | `s 64(1)(a) executes the process of the Supreme Court given to the Sheriff by the Court for that…` [constructor, scja2-part6-officers.l4]; `s 64(1)(a) the Sheriff or the Sheriff's officer must execute the process` [function, scja2-part6-officers.l4]; `s 64(1)(a) and (b) the duty of the Sheriff to execute the process and make a return` [function, scja2-part6-officers.l4] | 2 | yes (1) |
| `s 64(1)(b)` (4113-4115) | (b) make a return of the same together with the manner of th | encoded | `s 64(1)(b) makes a return of the process together with the manner of its execution to the Supre…` [constructor, scja2-part6-officers.l4]; `s 64(1)(b) the Sheriff or the Sheriff's officer must make a return of the process and the manne…` [function, scja2-part6-officers.l4] | 2 |  |
| `s 64(1)(c)` (4117-4118) | (c) receive all persons committed to his or her custody by t | encoded | `s 64(1)(c) receives a person committed to the Sheriff's custody by the Supreme Court` [constructor, scja2-part6-officers.l4]; `s 64(1)(c) the Sheriff or the Sheriff's officer must receive the person` [function, scja2-part6-officers.l4]; `s 64(1)(c) the duty of the Sheriff to receive the persons committed to the Sheriff's custody` [function, scja2-part6-officers.l4] | 2 |  |
| `s 64(2)` (4120-4125) | (2) The Sheriff or his or her officers in executing any enfo | encoded | `s 64(2) the Sheriff or the Sheriff's officer may effect an entry into the building` [function, scja2-part6-officers.l4]; `s 64(2) the Sheriff or the Sheriff's officer may break open any outer or inner door or window o…` [function, scja2-part6-officers.l4] | 6 |  |
| `s 64(3)` (4129-4133) | (3) The Sheriff may engage any auxiliary police officer appo | encoded | `s 64(3) kind of person` [type, scja2-part6-officers.l4]; `s 64(3) an auxiliary police officer appointed under the Police Force Act 2004` [constructor, scja2-part6-officers.l4]; `s 64(3) a security agency` [constructor, scja2-part6-officers.l4]; `s 64(3) a provider of transport and of warehousing` [constructor, scja2-part6-officers.l4]; and 6 more with the same label | 18 |  |
| `s 65` (4141-4143) | 65. Where in any cause or matter the Sheriff is an intereste | encoded | `s 65 the court may appoint an officer or a person to act in the place of the Sheriff` [function, scja2-part6-officers.l4] | 2 | yes (1) |
| `s 65A` (4147-4161) | 65A.—(1) Subject to such directions as may be given by the C | encoded | by the rows below |  |  |
| `s 65A(1)` (4147-4158) | 65A.—(1) Subject to such directions as may be given by the C | fork (fork F8) | `s 65A(1) kind of person` [type, scja2-part6-officers.l4]; `s 65A(1) a solicitor` [constructor, scja2-part6-officers.l4]; `s 65A(1) a person employed by a solicitor` [constructor, scja2-part6-officers.l4]; `s 65A(1) another person` [constructor, scja2-part6-officers.l4]; and 1 more with the same label | 10 |  |
| `s 65A(2)` (4160-4161) | (2) Section 79(2) applies to a solicitor or person authorise | encoded | `s 65A(2) the solicitor or person authorised under subsection (1) is not liable to be sued` [function, scja2-part6-officers.l4] | 4 |  |
| `s 66` (4169-4176) | 66.—(1) An Accountant is to be appointed by the Chief Justic | encoded | by the rows below |  |  |
| `s 66(1)` (4169-4170) | 66.—(1) An Accountant is to be appointed by the Chief Justic | fork (fork F7) | `s 66(1) the Accountant is appointed as the Act requires` [function, scja2-part6-officers.l4] | 2 |  |
| `s 66(2)` (4172-4176) | (2) The Accountant must do all things necessary to execute t | encoded | `s 66(2) party` [type, scja2-part6-officers.l4]; `s 66(2) the Accountant` [constructor, scja2-part6-officers.l4]; `s 66(2) act` [type, scja2-part6-officers.l4]; `s 66(2) does all things necessary to execute an order of the Supreme Court relating to suitors'…` [constructor, scja2-part6-officers.l4]; and 2 more with the same label | 2 |  |
| `s 67` (4184-4193) | 67.—(1) There are to be attached to the Supreme Court | encoded | by the rows below |  |  |
| `s 67(1)` (4184-4188) | 67.—(1) There are to be attached to the Supreme Court | fork (fork F5) | `s 67(1) officers of that kind are to be attached to the Supreme Court` [function, scja2-part6-officers.l4] | 7 |  |
| `s 67(2)` (4190-4193) | (2) Those of the officers attached to the Supreme Court as m | encoded | `s 67(2) the officer may be attached to that Judge` [function, scja2-part6-officers.l4] | 4 |  |
| `s 68` (4197-4243) | 68.—(1) The Registrar, the Deputy Registrar and the Assistan | encoded | by the rows below |  |  |
| `s 68(1)` (4197-4198) | 68.—(1) The Registrar, the Deputy Registrar and the Assistan | encoded | `s 68(1) the officer is an ex-officio commissioner for oaths` [function, scja2-part6-officers.l4] | 4 |  |
| `s 68(2)` (4205-4237) | (2) The Senate of the Singapore Academy of Law may appoint f | encoded | `s 68(2) the Senate of the Singapore Academy of Law may appoint the person to be a commissioner …` [function, scja2-part6-officers.l4]; `s 68(2) thing a commissioner for oaths may do` [type, scja2-part6-officers.l4]; `s 68(2) another thing` [constructor, scja2-part6-officers.l4]; `s 68(2) the commissioner for oaths appointed by the Senate may do the thing` [function, scja2-part6-officers.l4] | 15 | yes (1) |
| `s 68(2)(a)` (4210-4212) | (a) receive acknowledgements of married women in all cases | encoded | `s 68(2)(a) receive acknowledgements of married women in all cases where such acknowledgements a…` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(b)` (4214-4215) | (b) receive acknowledgements of recognisances of bail and | encoded | `s 68(2)(b) receive acknowledgements of recognisances of bail and bail bonds` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(c)` (4217-4235) | (c) administer oaths for — | encoded | by the rows below |  |  |
| `s 68(2)(c)(i)` (4219) | (i) the justification for bail; | encoded | `s 68(2)(c)(i) administer oaths for the justification for bail` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(c)(ii)` (4221) | (ii) taking any affidavit or affirmation; | encoded | `s 68(2)(c)(ii) administer oaths for taking any affidavit or affirmation` [constructor, scja2-part6-officers.l4] | 4 |  |
| `s 68(2)(c)(iii)` (4223-4225) | (iii) receiving and taking the answer, plea, demurrer, | encoded | `s 68(2)(c)(iii) administer oaths for receiving and taking the answer, plea, demurrer, disclaime…` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(c)(iv)` (4227-4229) | (iv) the examination of any witnesses upon any | encoded | `s 68(2)(c)(iv) administer oaths for the examination of any witnesses upon any interrogatories o…` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(c)(v)` (4231) | (v) swearing executors and administrators; and | encoded | `s 68(2)(c)(v) administer oaths for swearing executors and administrators` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(c)(vi)` (4233-4235) | (vi) swearing persons in any cause or matter which is | encoded | `s 68(2)(c)(vi) administer oaths for swearing persons in any cause or matter which is pending or…` [constructor, scja2-part6-officers.l4] | 1 |  |
| `s 68(2)(d)` (4237) | (d) take and receive statutory declarations. | encoded | `s 68(2)(d) take and receive statutory declarations` [constructor, scja2-part6-officers.l4] | 2 |  |
| `s 68(3)` (4239-4243) | (3) The Senate of the Singapore Academy of Law may make rule | inert (reason 2: a rule-making power of the Senate of the Singapore Academy of Law (the rules for the appointment and conduct of commissioners for oaths, their fees and fees to the Academy): rule-making machinery; no decision follows from it) | none |  |  |
| `s 69` (4247-4275) | 69.—(1) The Registrar, the Deputy Registrar, the Assistant | encoded | by the rows below |  |  |
| `s 69(1)` (4247-4257) | 69.—(1) The Registrar, the Deputy Registrar, the Assistant | fork (fork F11, F12) | `s 69(1) party` [type, scja2-part6-officers.l4]; `s 69(1) the officer` [constructor, scja2-part6-officers.l4]; `s 69(1) act` [type, scja2-part6-officers.l4]; `s 69(1) takes and subscribes the appropriate oath of office set out in the Second Schedule` [constructor, scja2-part6-officers.l4]; and 2 more with the same label | 9 |  |
| `s 69(2)` (4261-4275) | (2) To avoid doubt, where an oath of office is required to b | encoded | `s 69(2) way of taking the oath` [type, scja2-part6-officers.l4]; `s 69(2) through a live video link` [constructor, scja2-part6-officers.l4]; `s 69(2) through a live television link` [constructor, scja2-part6-officers.l4]; `s 69(2) in another way` [constructor, scja2-part6-officers.l4]; and 1 more with the same label | 14 |  |
| `s 69(2)(a)` (4268-4270) | (a) maintain visual contact and communicate with the person | encoded | covered by the `s 69(2)` definition above |  |  |
| `s 69(2)(b)` (4272-4273) | (b) confirm the identity of the person taking the oath and a | encoded | covered by the `s 69(2)` definition above |  |  |
| `s 69(2)(c)` (4275) | (c) verify by inspection the oath to be subscribed. | encoded | covered by the `s 69(2)` definition above |  |  |
| `s 70` (4281-4283) | 70. The Chief Justice may make such rules and regulations as | inert (reason 2: the Chief Justice's power to make rules and regulations for the apportionment of work among the officers of the Supreme Court: rule-making machinery; no decision follows from it) | none |  |  |
| `s 71` (4291-4296) | 71.—(1) There shall be an office of the Supreme Court called | encoded | by the rows below |  |  |
| `s 71(1)` (4291-4293) | 71.—(1) There shall be an office of the Supreme Court called | encoded | `s 71(1) the department is part of the Registry of the Supreme Court` [function, scja2-part6-officers.l4] | 2 |  |
| `s 71(2)` (4295-4296) | (2) The Registry is under the control and supervision of the | encoded | `s 71(2) the officer has the control and supervision of the Registry` [function, scja2-part6-officers.l4] | 2 |  |
| `s 72` (4300-4319) | 72.—(1) The Registry of the Supreme Court is to be open on e | encoded | by the rows below |  |  |
| `s 72(1)` (4300-4301) | 72.—(1) The Registry of the Supreme Court is to be open on e | fork (fork F13) | `s 72(1) the day is a Saturday` [function, scja2-part6-officers.l4]; `s 72(1) the Registry of the Supreme Court is to be open on the day` [function, scja2-part6-officers.l4] | 10 | yes (1) |
| `s 72(2)` (4308-4316) | (2) Despite subsection (1), the Registrar may lawfully sit o | encoded | `s 72(2) the Registrar may lawfully sit or carry out the business of the Registry on the day` [function, scja2-part6-officers.l4] | 7 | yes (1) |
| `s 72(2)(a)` (4312-4313) | (a) the Chief Justice has directed the Registrar to do so on | encoded | covered by the `s 72(2)` definition above |  |  |
| `s 72(2)(b)` (4315-4316) | (b) in the opinion of the Registrar, the business to be | encoded | covered by the `s 72(2)` definition above |  |  |
| `s 72(3)` (4318-4319) | (3) The office hours of the Registry are such times as the C | encoded | `s 72(3) the times are the office hours of the Registry` [function, scja2-part6-officers.l4] | 2 |  |

Rows for lines that are not provisions (inert, reason 1: page furniture, amendment tags, headings, Part and Division headings):

| lines | kind | text |
| --- | --- | --- |
| 2310-2314 | Part or Division heading, inert (reason 1) | PART 4 / APPELLATE DIVISION OF HIGH COURT / Division 1 — General |
| 2316 | section heading, inert (reason 1) | President |
| 2321 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2326 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2333-2336 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 2341 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2343 | section heading, inert (reason 1) | Jurisdiction — general |
| 2348 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2352 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2358 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2363 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2365 | section heading, inert (reason 1) | Composition — general |
| 2371 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2377 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2383 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2385 | section heading, inert (reason 1) | Decisions how made |
| 2391-2396 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 45  Judicature Act 1969                  |
| 2402 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2404 | section heading, inert (reason 1) | Sittings |
| 2414 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2419 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2421 | Part or Division heading, inert (reason 1) | Division 2 — Civil jurisdiction |
| 2423 | section heading, inert (reason 1) | Civil jurisdiction |
| 2428 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2443-2448 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.       Judicature Act 1969       |
| 2450 | section heading, inert (reason 1) | Composition — further provisions |
| 2460 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2466 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2480 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2482 | section heading, inert (reason 1) | Oral hearing not needed for appellate ma |
| 2498-2501 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 47  Judicature Act 1969                  |
| 2512 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2514 | section heading, inert (reason 1) | Summary dismissal of certain matters |
| 2532 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2544 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2549-2554 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 2559 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2561 | section heading, inert (reason 1) | Applications |
| 2567 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2569 | section heading, inert (reason 1) | Incidental directions and interim orders |
| 2585 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2590 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2595 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2606-2609 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 49  Judicature Act 1969                  |
| 2614-2616 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2620 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2622 | section heading, inert (reason 1) | Hearing of appeals |
| 2627 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2633 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2646 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2652-2654 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2660-2662 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2667-2672 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 2685 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2693 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2705 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2718 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2723-2726 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 51  Judicature Act 1969                  |
| 2731 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2733 | section heading, inert (reason 1) | Costs of appeal |
| 2738 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2740 | section heading, inert (reason 1) | New trial |
| 2747 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2753 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2765 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2771 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2773 | section heading, inert (reason 1) | Immaterial errors |
| 2780-2785 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 2787 | section heading, inert (reason 1) | Appeal not to operate as stay of executi |
| 2794-2796 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2801-2803 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2805-2806 | Part or Division heading, inert (reason 1) | Division 3 — Matters that are non-appeal / appealable only with permission |
| 2808 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2810 | section heading, inert (reason 1) | No appeal in certain cases |
| 2815 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2817 | section heading, inert (reason 1) | Permission required to appeal |
| 2823-2825 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2830-2832 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2839-2846 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] / Informal Consolidation – version in forc / Supreme Court of / 53                    Judicature Act 196 |
| 2854 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 2868-2870 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 2872-2876 | Part or Division heading, inert (reason 1) | PART 5 / COURT OF APPEAL / Division 1 — General |
| 2878 | section heading, inert (reason 1) | President and Vice-Presidents |
| 2884 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2894-2899 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.                Judicature Act 1 |
| 2901 | section heading, inert (reason 1) | Jurisdiction — general |
| 2908 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 2914 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2919 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2921 | section heading, inert (reason 1) | Composition — general |
| 2926 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2932 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2938 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2940 | section heading, inert (reason 1) | Decisions how made |
| 2946 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2952-2957 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 55        Judicature Act 1969            |
| 2959 | section heading, inert (reason 1) | Sittings |
| 2969 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2974 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 2976 | Part or Division heading, inert (reason 1) | Division 2 — Civil jurisdiction |
| 2978 | section heading, inert (reason 1) | Civil jurisdiction |
| 2983 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3008-3011 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.       Judicature Act 1969       |
| 3022 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3024 | section heading, inert (reason 1) | Composition — further provisions |
| 3033 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3039 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3053 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3055 | section heading, inert (reason 1) | Oral hearing not needed for appellate ma |
| 3061-3064 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 57  Judicature Act 1969                  |
| 3084 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3086 | section heading, inert (reason 1) | Summary dismissal of certain matters |
| 3103 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3112-3115 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3120 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3125 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3130 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3132 | section heading, inert (reason 1) | Applications |
| 3137 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3139 | section heading, inert (reason 1) | Incidental directions and interim orders |
| 3155 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3160 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3165 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3170-3173 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 59  Judicature Act 1969                  |
| 3183-3185 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 3189 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3191 | section heading, inert (reason 1) | Hearing of appeals |
| 3196 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3202 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3215 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3221-3223 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 3229-3236 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3241 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3254 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3262 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3274 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3287-3292 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] / Informal Consolidation – version in forc / Supreme Court of / 61  Judicature Act 1969                  |
| 3299 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3301 | section heading, inert (reason 1) | Costs of appeal |
| 3306 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3308 | section heading, inert (reason 1) | New trial |
| 3321 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3327 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3339 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3345-3350 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.           Judicature Act 1969   |
| 3352 | section heading, inert (reason 1) | Immaterial errors |
| 3360 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3362 | section heading, inert (reason 1) | Appeal not to operate as stay of executi |
| 3369-3371 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 3376-3378 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 25 of 2021 wef 01/04/2022] |
| 3380 | Part or Division heading, inert (reason 1) | Division 3 — Criminal jurisdiction |
| 3382 | section heading, inert (reason 1) | Criminal jurisdiction |
| 3402-3405 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 63  Judicature Act 1969                  |
| 3413-3415 | page furniture or amendment tag, inert (reason 1) | [40/2019] / [Act 17 of 2022 wef 01/07/2022] |
| 3420 | page furniture or amendment tag, inert (reason 1) | [Act 17 of 2022 wef 01/07/2022] |
| 3422 | section heading, inert (reason 1) | Composition when exercising criminal jur |
| 3428 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 3448 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 3450-3451 | Part or Division heading, inert (reason 1) | Division 4 — Post-appeal application in / capital case and finding of abuse of pro |
| 3453-3458 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3460 | section heading, inert (reason 1) | Interpretation of this Division |
| 3510-3513 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 65  Judicature Act 1969                  |
| 3562-3565 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3601 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3603 | section heading, inert (reason 1) | Application for permission to make PACC  |
| 3612-3615 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 67  Judicature Act 1969                  |
| 3661-3664 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3711-3714 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 69  Judicature Act 1969                  |
| 3747 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3749 | section heading, inert (reason 1) | Hearing of PACC application |
| 3760-3763 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3813-3816 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 71  Judicature Act 1969                  |
| 3822 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3824-3825 | section heading, inert (reason 1) | Procedure for making PACC application, e / pending PACC application, etc. |
| 3858-3863 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 3865-3867 | section heading, inert (reason 1) | Court of Appeal may determine whether ap / action contains, application for PACC pe / application, etc. |
| 3911-3914 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 73  Judicature Act 1969                  |
| 3919 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3921-3922 | section heading, inert (reason 1) | Operation of Division 1B of Part 20 of C / Code 2010 |
| 3927 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3929 | section heading, inert (reason 1) | Stay of execution of death sentence |
| 3935 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 3937-3938 | section heading, inert (reason 1) | Power of Court of Appeal to make finding / when dealing with application or action |
| 3964-3967 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 4011-4014 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 75  Judicature Act 1969                  |
| 4048 | page furniture or amendment tag, inert (reason 1) | [Act 41 of 2022 wef 28/06/2024] |
| 4050-4053 | Part or Division heading, inert (reason 1) | PART 6 / OFFICERS AND OFFICES / Division 1 — Registrar |
| 4055-4060 | page furniture or amendment tag, inert (reason 1) | [40/2019] / Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 4062-4063 | section heading, inert (reason 1) | Appointment of Registrar, Deputy Registr / Registrars |
| 4074-4075 | section heading, inert (reason 1) | Powers and duties of Registrar, Deputy R / Registrars |
| 4086 | Part or Division heading, inert (reason 1) | Division 2 — Sheriff |
| 4088 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 4090-4091 | section heading, inert (reason 1) | Sheriff, Deputy Sheriff and Assistant Sh / Court |
| 4100-4103 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 77  Judicature Act 1969                  |
| 4105 | section heading, inert (reason 1) | Powers and duties of Sheriff |
| 4127 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] |
| 4135-4137 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2021 wef 01/04/2022] / [*Updated to be consistent with the 2020 |
| 4139 | section heading, inert (reason 1) | Sheriff not to act when an interested pa |
| 4145 | section heading, inert (reason 1) | Solicitor authorised to act as officer o |
| 4152-4155 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 4163 | Part or Division heading, inert (reason 1) | Division 3 — Accountant |
| 4165 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 4167 | section heading, inert (reason 1) | Duties of Accountant |
| 4178 | Part or Division heading, inert (reason 1) | Division 4 — Subordinate officers |
| 4180 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 4182 | section heading, inert (reason 1) | Subordinate officers of Supreme Court |
| 4195 | section heading, inert (reason 1) | Commissioners for oaths |
| 4200-4203 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 79  Judicature Act 1969                  |
| 4245 | section heading, inert (reason 1) | Oaths of officers |
| 4251-4254 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 2020 Ed.  Judicature Act 1969            |
| 4259 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2023 wef 01/12/2023] |
| 4277 | page furniture or amendment tag, inert (reason 1) | [Act 25 of 2023 wef 01/12/2023] |
| 4279 | section heading, inert (reason 1) | Apportionment of work |
| 4285 | Part or Division heading, inert (reason 1) | Division 5 — Offices |
| 4287 | page furniture or amendment tag, inert (reason 1) | [40/2019] |
| 4289 | section heading, inert (reason 1) | Registry of Supreme Court |
| 4298 | section heading, inert (reason 1) | Registry to be open throughout the year |
| 4303-4306 | page furniture or amendment tag, inert (reason 1) | Informal Consolidation – version in forc / Supreme Court of / 81  Judicature Act 1969                  |

## Fork register (scja2)

### The rulings that bind this part (word for word, as the brief prints them)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

### How the rulings were applied in this range

- **E1.** Each section's answer is written on its own (option C), in the Appellate Division sections (ss 30 to 45) and again in the Court of Appeal sections (ss 48 to 60C).
  No construct gathers a legal effect by name from several sections, and the Magna Carta pilot was not run.
  Where a function gathers routes by hand (option B as guidance) it gathers inside one section or one provision, to follow the text's own list: `s 35(2)` (two limbs) and `s 53(2)` (four limbs) gather the limbs the subsection lists; `s 49(1)` gathers the three jurisdictions it names (sections 53, 60D and Division 4).
  Nothing gathers across ss 35 and 53, or across Part 4 and Part 5.
- **N2.** A flat negative is a no.
  The Hohfeld kinds are in `## Jural relations (scja2)` and not in any answer.
  Where the text names who bears a prohibition, the prohibition is a regulative `SHANT` rule derived from the decision function (for a prohibition with a gate, the function phrased as the bar), with a `#TRACE` in which the bearer does the forbidden act and the rule is breached.
  There are eleven, each named `... the prohibition on ...`: `s 32(2)` and `s 50(2)` (a Judge must not sit on an appeal from the Judge's own decision), `s 36(2)` and `s 54(2)` (a Judge must not sit on an application to discharge or vary the Judge's own direction or order), `s 37(4)` and `s 55(4)` (the court must not hear a matter asynchronously where that is inconsistent with its duty of fairness), `s 44` and `s 60B` (the court may not reverse or vary on account of an immaterial error), `s 60E(2)` (a Judge must not sit on the matters listed), `s 60G(15)` (the Court of Appeal must not grant permission after a finding of abuse of process unless new material is adduced) and `s 60I(1)` (the PACP cannot make a subsequent application without permission).
  Prohibitions whose text names no bearer have no `SHANT` rule, only the decision function: `s 37(2)`/`55(2)` ("Subsection (1) does not allow"), `s 41(9)`/`59(9)` ("No request may be made"), `s 43(2)`/`60A(2)` ("A new trial must not be ordered"), `s 45(2)`/`60C(2)` ("No intermediate act ... is to be invalidated"), `s 46` ("An appeal cannot be brought"), `s 60G(13)` ("no further proceedings may be taken"), `s 60L` ("may only be granted by the Court of Appeal") and `s 61(2)` ("A person must not be appointed": the person is the object of the appointment, and the text does not say who must not appoint).
  Where such a prohibition has a gate or an exception, the function that answers "does the bar apply?" is named as the bar (`s 41(9) the bar on a request under subsection (8) applies`, `s 60G(13) the bar on further proceedings ... applies`, and the bar functions beside `s 37(2)`, `s 41(4)`, `s 43(2)`, `s 45(1)`, `s 45(2)`, `s 60G(15)`, `s 60I(1)` and `s 61(2)` and their Court of Appeal twins), so that `JUST TRUE` is "the bar applies" and `JUST FALSE` is "it does not on these facts" (fork F8).
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
  (a) A period the text fixes in its own words: outside it, `JUST FALSE`.
  Applied at ss 41(10) and 59(10) (the 7 days, and "before the earlier of" two events), and kept at s 60G(5) (the respondent "may file" within the prescribed period, an input from the Rules of Court): a grant bounded by "within such period" is a grant with an unmet condition once the period has run out, so `JUST FALSE` (ruling (b) read with the "where" rule); the other reading is `NOTHING`, because the period is not fixed in the text's own words.
  Not applied at the "must" sites ss 60G(3), 60G(4) and 60H(1) to (3): the periods there are "as is prescribed" by the Rules of Court, which are not among the sources, so they are inputs and not periods the text fixes in its own words, and a period run out on a bare "must" gives `NOTHING` (fork F11); no period given gives `NOTHING` at every one of these sites.
  (b) A "where" that is not met: `JUST FALSE`.
  Applied at every site listed in marginal reading M2, and a condition the text puts as "only" or "only with" is `JUST FALSE` when unmet at ss 40(4)(b), 41(4), 47(1), 47(2), 58(4)(b), 59(4) and 60L.
  Fork F8 below records the sites where the "where" or "if" gates a prohibition, and follows this ruling there.
  (c) A scope limit with no "only": `NOTHING` outside the scope.
  Applied wherever a function says "limited by its own wording".
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  (a) No definition in this range is handed to a list in the way the ruling's example is (a definition that sends the reader to a Schedule).
  The definitions of section 60F are "means" definitions, which the brief's rule of 2026-10-29 answers `JUST FALSE` ("a definition that says \"means\"") when none of their conditions is met; `s 35(2)`, `s 53(2)`, `s 60D` and `s 60F "relevant application"` are lists the text closes with "consists of" or "means", and answer `JUST FALSE` when no head holds (marginal reading M1).
  The Examples under "post-appeal application in a capital case" are a list that is not closed, so `NOTHING`.
  (b) This range has no defence provision and no section that says "it is a defence".
  (c) "When", "upon" and "whenever" were treated as "where": ss 60G(11), 60H(9), 60I(3), 60M(1) (fork F9 for the first two).
  (d) This range has no "until" bar: a grep of lines 2310 to 4320 for "until" finds none.
  The bar functions that exist are bars with a gate or an "unless" or "except" (F8).
  Where a result is a date, a court, an officer or a list, and so cannot carry `JUST FALSE`, a yes/no function sits beside it: `s 41(10)(b)` and `s 59(10)(b)` return a date, and the yes/no twins are `s 41(10)` and `s 59(10)` (in time or not); `s 39 the court to which the application must first be made` and `s 57 ...` return a court, and the twins are `s 39 the application must first be made to the General Division` and `s 57 the application must first be made to the other court`; `s 63(1) the office of the Sheriff that the officer holds` returns an officer, and the twin is `s 63(1) the officer is a Sheriff, Deputy Sheriff or Assistant Sheriff of the Supreme Court`; `s 60F "relevant date" the relevant date` returns a date, and the twin that can say `JUST FALSE` is `s 60F "relevant date" it is made after the relevant date`; `s 60M(2) the matters that the Court of Appeal may take into account for the kind of application` returns a list, and the twin is `s 60M(2) the Court of Appeal may inquire into and take into account the matter`.

### The forks I took

Each row gives the readings I saw, the one taken, and the text that licenses it.
Every one is assumed, not ruled, and is for a lawyer to confirm.
"Where" names the rows of the coverage table that carry the fork.

| id | provision and text | readings | taken | where |
| --- | --- | --- | --- | --- |
| **F1** (K1) | ss 35(2)(a), 53(2)(a): "any appeal against any decision made by the General Division in any civil cause or matter ..."; ss 43(1), 60A(1)(a): "any matter that has been tried by the General Division ...". Does "General Division" include the Singapore International Commercial Court? | (A) yes: s 18A calls the SICC "a division of the General Division" and s 18C applies the Act to it as to the General Division; (B) no: s 18J(4) says "General Division" does not include the SICC in that section, s 18I(1) gives it its own powers, and the Sixth Schedule para 1(f) lists a SICC appeal apart (all as the keel's K1 records; checked against the text on 2026-11-05: s 18A at line 1317, s 18C at 1344, s 18I(1) at 1566, s 18J(4) at 1610, the Sixth Schedule para 1(f) at 6209) | `NOTHING` when the court is the SICC; `JUST TRUE` or `JUST FALSE` is never answered for it | `s 35(2)(a)`, `s 53(2)(a)`, `s 43(1)`, `s 60A(1)(a)` (and the seat questions `Under section 35(2)`, `53(2)`, `43(1)`, `60A(1)`, `31(1)`, `49(1)`). **Where "the General Division" appears and the fact is an input, the person states it and K1 is theirs to decide:** ss 39 (returns the court `General Division` as the first court, not a SICC decision), 44 (the error "does not affect ... the jurisdiction of the General Division"), 45(1) (a stay ordered by "the General Division or the Appellate Division"), 60D(a) (the kind of matter), 60H(5) (a power the General Division could exercise). Sections 60B and 60C(1) speak of "the court whose decision is appealed against" and do not name the General Division |
| **F2** (K4) | s 31(2): "The Appellate Division has no criminal jurisdiction." ss 35(2)(a), 53(2)(a): "civil cause or matter". Section 20 (lines 1705 to 1710) and s 74(5) (lines 4830 to 4832) name three kinds of proceeding: civil, quasi-criminal, criminal. | (A) quasi-criminal is a kind of criminal: s 31(2) `JUST FALSE`; (B) it is a kind of civil: s 35(2)(a) can be met; (C) it is a third kind (the keel's reading) | (C): s 31(2) gives `NOTHING` for a quasi-criminal proceeding (the text names "criminal" and the proceeding is not that); s 35(2)(a) and s 53(2)(a) give `JUST FALSE` (the proceeding is not a civil cause or matter, and the list is closed by "consists of") | `s 31(2)`, `s 35(2)(a)`, `s 53(2)(a)`; asserted in the tests of ss 31 and 35(2)(a)/53(2)(a) |
| **F3** | ss 41(10)(b), 59(10)(b): "the expiration of 7 days after the date on which the decision ... is made". Is a period counted "after" a date counted from the day after it, with section 50(b) of the Interpretation Act (a last day that is a Sunday or public holiday moves to the next day that is not) applied to its last day? | (A) yes: the last day is the date plus 7, section 50(b) moves it, and a request made on the last day is in time (it is made before the expiration); (B) the staged module's own answer for a period counted `After` is `NOTHING` (the Act has no rule for it); (C) the day of the decision counts as day 1, so the last day is the date plus 6 | (A): section 50(a) excludes the day of an event, and the module offers `the last day of the period once section 50(b) is applied` for a last day worked out elsewhere (its comment: "the rule reaches the last day of every period"); the module's `NOTHING` function was not called | `s 41(10)`, `s 41(10)(b)`, `s 59(10)`, `s 59(10)(b)`; boundary tests on the last day, the day after, a Sunday last day and a public-holiday last day |
| **F4** | s 60F "relevant date" paragraph (b): "(i) the date mentioned in paragraph (a); or (ii) if prior to the making of the instant application, there has been a determination of (A) any application for PACC permission ...; or (B) any PACC application, [(ii)] in relation to the PACP, the date of the most recent of any such determination". The second "(ii)" is printed twice, at lines 3583 and 3592 (finding 1). | (1) where an earlier determination exists the relevant date is the date of the most recent one, and otherwise the date in paragraph (a); (2) the paragraph (a) date is always an alternative, so an application is "after the relevant date" if it is after either date; (3) the second "(ii)" is a separate limb | (1): "or" joins two alternatives and the second is conditioned on a prior determination, so the conditioned limb applies when its condition holds and the first otherwise; the function returns `NOTHING` when none of the paragraph (a) dates is given, or two are, and the text does not say which prevails | `s 60F "relevant date"(b)`, `(b)(i)`, `(b)(ii)`, `(b)(ii)(A)`, `(b)(ii)(B)`, the stray `(ii)`; the function `s 60F "relevant date" the relevant date` |
| **F5** | s 67(1): "commissioners for oaths, interpreters, clerks, process servers and other officers as, from time to time, appear to the Chief Justice to be necessary". Does "as ... appear to the Chief Justice to be necessary" qualify only "other officers", or the whole list? | (1) only "other officers"; (2) every kind in the list | (1): the four kinds are named and "other officers as ... appear" is the open-ended limb; under (2) each named kind would be attached only as it appears necessary | `s 67(1)` |
| **F6** | ss 32(1), 50(1): "the jurisdiction of the Appellate Division [Court of Appeal] is to be exercised by 3 or any greater uneven number of Judges". Is any other number the text's no? | (1) the subsection says which numbers exercise the jurisdiction and does not say "only", so another number is not answered; (2) "is to be" is mandatory, and s 36(1) and s 54(1) ("Despite section 32(1) [50(1)] ...") suggest that a smaller panel is otherwise forbidden, so another number is `JUST FALSE`: an even number of Judges, and 1 or 2 Judges where no head of the Seventh Schedule provides for them, answer `JUST FALSE` and only 3 or a greater uneven number answers `JUST TRUE` | (1), under the scope-limit ruling (c): there is no "only", "must not" or "nothing but" | `s 32(1)`, `s 50(1)`; seat questions `Under section 32(1)`, `50(1)` |
| **F7** | s 66(1): "An Accountant is to be appointed by the Chief Justice for the Supreme Court." Is an appointment by anyone else the text's no? | (1) the text says who appoints, and is silent on the validity of another's appointment; (2) "is to be appointed by" is mandatory, so another appointer is `JUST FALSE` | (1), for the same reason as F6 | `s 66(1)` |
| **F8** | **A gate, an exception or a "subject to" that qualifies a prohibition, a duty or a power.** Three cases. **(a) An unmet "where" or "if" gate on a prohibition.** Ruling (b) of the periods ruling says a "where" that is not met answers `JUST FALSE`; the brief's rule of 2026-10-29 reads "if" the same way. For "Where any application ... is pending determination, the PACP cannot make a subsequent application ..." (s 60I(1)) the ruling gives `JUST FALSE` when nothing is pending. **(b) An "unless" or "except" that is met.** s 45(1): "does not operate as a stay ..., unless the General Division or the Appellate Division so orders": the bar is lifted, and the section does not say what the order has the effect of. **(c) "Subject to X" where X applies.** s 60G(1) "Subject to section 60I". | For (a): (1) taken, the ruling, applied to the function that asks the provision's own question, which for a prohibition is "is it barred": the bar function answers `JUST FALSE` when the gate is unmet; (2) the other reading: the unmet gate leaves the section silent on every function, so `NOTHING`, because "if A then B" does not say "if not A then not B" (this was this part's first answer, and it departed from the ruling; it was withdrawn on 2026-11-05). How the function is named matters: a function named as the permission ("the PACP can make a subsequent application") would answer `JUST FALSE` both inside the gate (the bar) and outside it, and so could never say `JUST TRUE` or `NOTHING`; so the pure-gate prohibitions are phrased as the bar ("the bar ... applies": `JUST TRUE` inside the gate, `JUST FALSE` outside it) at `s 37(4)`, `s 55(4)`, `s 41(9)`, `s 59(9)` and `s 60G(13)`, and the three prohibitions that have both a gate and an "unless" keep a function named as the grant and add the bar function beside it (`s 37(2)`/`55(2)`, `s 60G(15)`, `s 60I(1)`). The four grant-named functions (`s 37(2)`, `s 55(2)`, `s 60G(15)`, `s 60I(1)`) ask a different question, "may it be done", and when the gate is unmet the prohibition is not triggered and the text is silent on the grant, so they answer `NOTHING` for an unmet gate (changed on 2026-11-06 from `JUST FALSE`, which read as "the Court may not", the opposite of the truth; the other reading, `JUST FALSE` on the grant-named function, is recorded here with that reason). The bar functions beside them answer `JUST FALSE` for an unmet gate, which is the ruling. A check of the grant-named functions of the other prohibitions (ss 32(2), 36(2), 44, 50(2), 54(2), 60B, 60E(2), 60G(14), 61(2)) found none that answers `JUST FALSE` for an unmet gate; they answer `NOTHING` there already. For (b) and (c): the ruling does not speak; (1) the lifted bar or the displaced subsection answers `JUST TRUE` (the thing is then allowed); (2) taken: `NOTHING` on the permission function, because lifting a bar does not itself grant, and a displaced subsection says nothing further; the bar function answers `JUST FALSE` when the bar is lifted. | (1) for (a), on the bar function, following the ruling, and `NOTHING` on the grant-named function; (2) for (b) and (c). The brief's rule of 2026-10-29 for a grant or prohibition limited by its own wording ("without", "against the will of", "when", a stated period, a named complement) is the rule for a scope limit and is not what these gates are (see also M3). | (a) `s 37(2)`, `s 55(2)`, `s 37(4)`, `s 55(4)`, `s 41(9)`, `s 59(9)`, `s 60G(13)`, `s 60G(15)`, `s 60I(1)`; (b) `s 37(2)`, `s 55(2)`, `s 41(4)`, `s 59(4)`, `s 43(2)`, `s 60A(2)`, `s 45(1)`, `s 60C(1)`, `s 45(2)`, `s 60C(2)`, `s 60G(15)`, `s 60I(1)`, `s 61(2)`; (c) `s 60G(1)`, `s 60H(1)`, `s 60H(8)` ("Except where subsection (7) applies"), `s 62(2)` ("Subject to Rules of Court"), `s 65A(1)` ("Subject to such directions as may be given by the Chief Justice") |
| **F9** | ss 60G(11), 60H(9): "The Court of Appeal may (a) before deciding any application ...; (b) when granting ...; or (c) when summarily granting ..., do one or both of the following". | (1) "when" counts as "where" (ruling (c)), so a stage outside the three is `JUST FALSE`; (2) the three stages are a scope limit with no "only", so `NOTHING` | (1), as ruling (c) directs | `s 60G(11)`, `s 60H(9)` |
| **F10** | ss 36(1), 54(1): "Despite section 32(1), a case ... may, if the Seventh Schedule so provides, be heard and decided by (a) either a single Judge or 2 Judges; or (b) 2 Judges." The Schedule is another part's; suppose it provides "a single Judge" alone. | (1) paragraph (a) ("either a single Judge or 2 Judges") covers it, so 1 Judge is `JUST TRUE`; (2) it is neither limb, so `NOTHING` | (2): a single Judge alone is the Tenth Schedule's panel under s 60E(1), and neither limb names it | `s 36(1)`, `s 54(1)` |
| **F11** (QB) | **A bare "must" that is not done.** ss 38(2), 56(2) ("must -- (a) give ... a reasonable opportunity to show cause ...; and (b) consider any representations"); s 60G(1) ("must apply ... for, and obtain, the permission"); s 60G(3), (4) and s 60H(1) to (3) ("must be fixed ... must file ... within such period as is prescribed"); s 60G(7), (9)(a), (10)(a) and (b), s 60H(7)(a) and (8) ("must consider"); s 69(1) ("must, before exercising the functions ..., take and subscribe"). The text states the duty and says nothing of what follows when it is not done. | (1) the duty is a duty and not a condition: the question "was it done?" answers `JUST TRUE` when it was and `NOTHING` when it was not, and the regulative rule next to it carries the breach; (2) a requirement not met is the text's no: `JUST FALSE` | (1); the functions are named "... as the section requires" so that the name does not claim a yes/no fact. Periods that the Rules of Court prescribe are not periods the text fixes (ruling (a) does not reach them). Not changed: ss 41(10) and 59(10), whose time is fixed in the text, answer `JUST FALSE` outside it | the functions listed in `## Judgment calls (scja2)`, QB |
| **F12** (QC) | **"Listed in" a Schedule.** s 46 (Ninth Schedule), ss 36(1) and 54(1) (Seventh Schedule), s 60E(1) (Tenth Schedule), s 69(1) (Second Schedule). The Schedule is another part's text. | (1) the Schedule's answer is a yes/no/not-known input; at ss 36(1), 54(1) and 60E(1) "does not provide" is `JUST FALSE` ("if the Schedule so provides" is unmet, ruling (b)), at s 46 "not on the list" is `NOTHING` (the bar is for the listed cases and whether an appeal lies elsewhere is for s 47), not known is `NOTHING` everywhere; (2) "does not provide" is `NOTHING` at ss 36(1), 54(1) and 60E(1) as well, because the Schedule is not in this part's range | (1) | `s 36(1)`, `s 54(1)`, `s 60E(1)`, `s 46`, `s 69(1)` |
| **F13** (QE) | **"Other than" inside a grant.** ss 37(1), 55(1) ("may decide any matter without hearing oral arguments, other than a matter prescribed by the Rules of Court"); s 60G(15)(b); s 60M(1)(b) ("(other than a relevant application)"); s 60J(1) ("filed in a court other than the Court of Appeal"); s 72(1) ("except on Saturdays, Sundays and public holidays"). | (1) a scope statement: a case inside the carve-out answers `NOTHING` (the Rules of Court are not among the sources; paragraph (a) deals with a relevant application); (2) an express exclusion: the case inside the carve-out answers `JUST FALSE` | (1) at ss 37(1), 55(1) and 60M(1)(b); s 60J(1) is a "where" and follows QD (`JUST FALSE` when filed in the Court of Appeal); s 72(1) takes (2), because the sentence states the days the Registry is open and closes the list with "except" | `s 37(1)`, `s 55(1)`, `s 60G(15)`, `s 60M(1)(b)`, `s 60J(1)`, `s 72(1)` |
| **F14** | **A matter tried in the exercise of civil jurisdiction.** ss 43(1), 60A(1)(a) ("any matter that has been tried by the General Division in the exercise of the original or appellate civil jurisdiction of the General Division"), s 60A(1)(b) ("... by the Appellate Division in the exercise of the civil jurisdiction of the Appellate Division"). A matter tried by the General Division may be a criminal one. | (1) the function takes a plain yes/no input, "tried in the exercise of civil jurisdiction", and a matter tried in the exercise of criminal jurisdiction answers `NOTHING` (a scope limit with no "only", ruling (c)); (2) such a matter answers `JUST FALSE` | (1) | `s 43(1)`, `s 60A(1)(a)`, `s 60A(1)(b)` and the seat questions `Under section 43(1)`, `60A(1)` (which ask the person whether the matter was a civil one). Checked, no change: ss 35(1) and 53(1) take "exercising its civil jurisdiction" as an input, ss 35(2)(a), 53(2)(a) and 47(1) read the proceeding's nature from the decision record, and s 53(2)(d) is itself about the link to the criminal jurisdiction; s 60A(1)(b) got the input although the Appellate Division has no criminal jurisdiction (s 31(2)), so that the three functions read alike |
| **F15** | ss 35(2), 53(2) and 60D: "The civil [criminal] jurisdiction of the Appellate Division [Court of Appeal] consists of the following matters". Is the list closed? | (1) closed: a matter in none of the heads is `JUST FALSE`; (2) open: it is `NOTHING`, because the lists do not say "only" | (1), under the ruling on delegated definitions (a) read with the brief's rule that "means" and closed lists answer `JUST FALSE`; s 49(1) ("has the civil jurisdiction ..., the criminal jurisdiction ... and the jurisdiction ...") is not closed and answers `NOTHING` (M1) | `s 35(2)`, `s 53(2)`, `s 60D` |
| **F16** | ss 36(3), 54(3): "Where the Appellate Division [Court of Appeal] is constituted by 3 or more Judges to hear and decide a case and one or more of those Judges are unable for any reason to continue". Does the subsection reach a panel of 2 Judges (allowed by s 36(1)) that loses a Judge? | (1) "3 or more" is a "where" that is not met, so paragraphs (a) and (b) both answer `JUST FALSE` for a 2-Judge panel; (2) the subsection is silent about a 2-Judge panel (a scope limit with no "only"), so both answer `NOTHING` | (1), ruling (b); what happens to a 2-Judge panel that loses a Judge is not answered by the Act, and the two functions saying `JUST FALSE` do not say it is dismissed or continues | `s 36(3)(a)`, `s 36(3)(b)`, `s 54(3)(a)`, `s 54(3)(b)` and the seat questions on them |
| **F17** | ss 30(1), 48(1): "The Chief Justice may appoint a Judge of the Appellate Division [Court of Appeal] to be the President". May the Chief Justice appoint someone who is not a Judge of that court? | (1) the grant names the class and does not say "only", so a person outside it answers `NOTHING`; (2) the named class is the only class, so `JUST FALSE` | (1), ruling (c) | `s 30(1)`, `s 48(1)` |
| **F18** | s 60G(12): "(a) where the application for PACC permission is dealt with by a single Judge of the Court of Appeal -- take such evidence itself; or (b) where ... 3 or any greater uneven number of Judges ... -- either take such evidence itself or have such evidence taken by one of those Judges". May a single Judge take the evidence under (a)? | (1) yes: where a single Judge deals with the application the Court of Appeal is that Judge, so "itself" is the single Judge and paragraph (a) answers `JUST TRUE` for it (and `JUST FALSE` for a panel of 3 or more, where paragraph (b) is the one that applies, M5); (2) the paragraph speaks of the Court of Appeal and not of the Judge, so a single Judge's power to take the evidence is `NOTHING` | (1) | `s 60G(12)(a)`, `s 60G(12)(b)`, and the twins `s 60J(5)`, `s 60M(4)` |
| **F19** | s 60G(15)(a) and s 60F "relevant date": "the date of commencement of the Post-appeal Applications in Capital Cases Act 2022". The text marks the provisions "[Act 41 of 2022 wef 28/06/2024]" (for example at lines 3601 and 3747) and never says that Act 41 of 2022 is the Post-appeal Applications in Capital Cases Act 2022 or that 28/06/2024 is its date of commencement. | (1) the date is not given as such, and the question whether a relevant application was filed on or after it is a plain yes/no input that the caller answers (s 60G(15) takes it inside "as paragraph (a) or (b) describes"; s 60F "relevant date" words "whether before, on or after" the commencement need no date); (2) the date is 28/06/2024, taken from the marks | (1) | `s 60G(15)`, `s 60F "relevant date"(a)` |

### What the text does not choose (explicit "not covered" values)

Collected in `## Findings` under "What the text does not answer"; every one is a `NOTHING` or a named constructor, asserted in the tests.

## Judgment calls (scja2)

Six kinds of case have no convention in the Commons guide, and each is decided here case by case, gut first, with the other reading written down so that a lawyer or a later editor can flip it.
The six are: QA, an "unless" or "except" once it is met; QB, a bare "must" that is not done; QC, "listed in Schedule N"; QD, a duty, power or prohibition whose "if" or "where" is not met; QE, "(other than X)"; QF, a missing event in a state ledger.
Every line below gives the provision, the function with its file and line, the answer taken, and the other reading.
All of them are assumed, not ruled, and are for a lawyer to confirm.
The lines were written one site at a time from the code as it stands after the fix round of 2026-11-05, and every file:line below was checked against the generated file: a script confirmed that each cited line opens a function definition, and the names were read against each line by hand.

File abbreviations: `AG` is `scja2-part4-ad-general.l4`, `AC` is `scja2-part4-ad-civil.l4`, `AA` is `scja2-part4-ad-appeals.l4`, `CG` is `scja2-part5-ca-general.l4`, `CC` is `scja2-part5-ca-civil.l4`, `CR` is `scja2-part5-ca-criminal.l4`, `CD` is `scja2-part5-ca-capital-defs.l4`, `CP` is `scja2-part5-ca-capital.l4`, `OF` is `scja2-part6-officers.l4`.
A line that gives an Appellate Division site and its Court of Appeal twin names both: they are written alike, so the same reading is taken at both.

### QA: an "unless" or "except" once it is met

The convention taken for a prohibition that has an "unless" or "except": the function that is named as the permission answers `NOTHING` when the exception is met, because lifting a bar does not itself grant the thing.
A second function, named as the bar ("the bar ... applies"), answers `JUST FALSE` in that case and `JUST TRUE` when the bar bites, so a person who asks "am I barred?" gets a definite answer.
The other reading, at every line: a met "unless" answers `JUST TRUE` on the permission function (the thing is then allowed), and the bar function is not needed.

- **s 37(2) and s 55(2)** ("unless all the parties consent"): `AC:210`, twin bar `AC:226`; `CC:284`, twin bar `CC:300`. Consent given: the permission function answers `NOTHING`, the bar function `JUST FALSE`. Other reading: `JUST TRUE`.
- **s 41(4) and s 59(4)** ("only with the permission of the Appellate Division [Court of Appeal] and on special grounds", "Except as provided in subsection (5)"): `AC:601`, bar `AC:617`; `CC:671`, bar `CC:687`. Permission and special grounds both present: the "only" condition is met and the permission function answers `JUST TRUE`; where subsection (5) applies, the permission function answers `NOTHING` (the subsection yields to another one) and the bar function `JUST FALSE`. Other reading: where subsection (5) applies, `JUST TRUE`.
- **s 43(2) and s 60A(2)** ("unless the improper admission or rejection has caused a substantial wrong or a miscarriage of justice"): `AC:836`, bar `AC:852`; `CC:918`, bar `CC:934`. The unless is met: `NOTHING` on the permission function (subsection (1) is what grants a new trial), `JUST FALSE` on the bar function. Other reading: `JUST TRUE`.
- **s 45(1) and s 60C(1)** ("unless ... so orders"): `AC:940`, rule function `AC:954`; `CC:1024`, rule function `CC:1038`. A stay has been ordered: `NOTHING` on "the appeal operates as a stay" (the section does not say what the order has the effect of), `JUST FALSE` on "the rule that the appeal does not operate as a stay applies". Other reading: `JUST TRUE`, the order produces a stay.
- **s 45(2) and s 60C(2)** ("except so far as the Appellate Division [Court of Appeal] directs"): `AC:965`, rule function `AC:977`; `CC:1049`, rule function `CC:1061`. The court directs invalidation: `NOTHING` on "the act is invalidated", `JUST FALSE` on "the rule that no act is invalidated applies". Other reading: `JUST TRUE`.
- **s 60G(15)** ("must not grant ... unless -- (c) ... and (d) ..."): `CP:362`, bar `CP:397`. New material that could not have been adduced earlier: `NOTHING` on the permission function, `JUST FALSE` on the bar function. Other reading: `JUST TRUE` (the Court may then grant).
- **s 60I(1)** ("cannot make a subsequent application ... unless the PACP has the permission of the Court of Appeal dealing with the specified application"): `CP:636`, bar `CP:656`. Permission given: `NOTHING` on the permission function, `JUST FALSE` on the bar function. Other reading: `JUST TRUE`.
- **s 61(2)** ("must not be appointed ... unless he or she is a qualified person"): `OF:46`, bar `OF:60`. A qualified person: `NOTHING` on "the person may be appointed" (section 61(1) is what grants the appointment), `JUST FALSE` on the bar function. Other reading: `JUST TRUE`.
- **s 60H(8)** ("Except where subsection (7) applies, ... the Court of Appeal ... must consider"): `CP:574`. Subsection (7) applies: `NOTHING` (the subsection yields to subsection (7), which has its own function at `CP:545`); no bar twin, because this is a duty and not a prohibition. Other reading: `JUST FALSE`, subsection (8) does not apply.
- **s 60F chapeau** ("In this Division, unless the context otherwise requires"): `CD:21`. The context requires otherwise: `JUST FALSE`, the definitions do not apply in that use, because the chapeau is a rule about what the defined words mean and not a bar. Other reading: `NOTHING`.
- **"Subject to" a displacing provision** (not a QA case in the guide's words, kept here beside them): s 60G(1) "Subject to section 60I" (`CP:24`), s 60H(1) "Subject to section 60I" (`CP:452`), s 62(2) "subject to Rules of Court" (`OF:88`), s 65A(1) "subject to such directions as may be given by the Chief Justice" (`OF:320`). Where the displacing provision applies the function answers `NOTHING`, because the displaced subsection says nothing further. Other reading: `JUST TRUE`.

### QB: a bare "must" that is not done

The convention taken: a duty stated as a flat "must", with no "if", no "only" and no consequence in the text, is a duty and not a condition.
A function that asks "was it done?" answers `JUST TRUE` when it was done and `NOTHING` when it was not: the text states the duty and does not say what follows from a failure, and the regulative rule next to it carries the breach.
Each such function is named so that it ends "... as the section requires", which tells a reader that it asks whether a requirement is met and does not state a fact.
A function that asks "does the duty bind this person?" answers `JUST TRUE` for a person it binds and `NOTHING` for one outside its words (limited by its own wording).
The other reading at every "was it done" line: `JUST FALSE`, the requirement is not met.

- **s 38(2) and s 56(2)** (before summarily dismissing, the court "must" give a reasonable opportunity to show cause and consider the representations): `AC:334`, `CC:405`; the regulative duty rules are at `AC:353` and `CC:424`. Either step not done: `NOTHING`.
- **s 60G(1)** ("the applicant must apply to the Court of Appeal for, and obtain, the permission"): `CP:24`; the duty rule is at `CP:41`. Permission not obtained: `NOTHING`; obtained: `JUST TRUE`. Where section 60I applies: `NOTHING` (QA, "subject to").
- **s 60G(3)** (the application "must be fixed for hearing within such period as is prescribed"): `CP:72`. The period is an input from the Rules of Court, which are not among the sources; outside it: `NOTHING`. The periods ruling (a) of 2026-11-05 covers "a period the text fixes in its own words", and this period is not fixed in the text, so it does not reach here.
- **s 60G(4)** (the applicant "must file written submissions ... within such periods as are prescribed"): `CP:90`; the duty rule is at `CP:110` (two traces, in time and out of time). Outside the period: `NOTHING`, for the same reason as s 60G(3).
- **s 60G(7)** (the Court of Appeal "must consider the following matters"): `CP:172`. One of the four not considered: `NOTHING`.
- **s 60G(9)(a) and s 60G(10)(a), (b)** (before summarily refusing or granting, the Court "must consider" the applicant's and, for granting, the respondent's written submissions): `CP:198`, `CP:222`, `CP:232`. Not considered: `NOTHING`. Paragraph 60G(9)(b) ("may, but is not required to") is a flat negative and keeps `JUST FALSE` (`CP:209`).
- **s 60H(1)** (the PACC application "must be made to the Court of Appeal, and fixed for hearing, within such period as is prescribed"): `CP:452`. Permission not granted: `JUST FALSE` (QD, "where"); the period run out: `NOTHING`.
- **s 60H(2), s 60H(3)** (the applicant and the respondent "must file such documents ... within such period"): `CP:475`, `CP:492`. Outside the period: `NOTHING`.
- **s 60H(7)(a), s 60H(8)** (before summarily refusing, or deciding on the merits, the Court "must consider" the written submissions): `CP:545`, `CP:574`. Not considered: `NOTHING`. Paragraph 60H(7)(b) ("may, but is not required to") keeps `JUST FALSE` (`CP:556`).
- **s 69(1)** (the Registrar, the Deputy Registrar, the Assistant Registrars and the officers the Chief Justice requires "must, before exercising the functions of their respective offices, take and subscribe the appropriate oath"): `OF:546`; the duty rule is at `OF:561`. No oath taken: `NOTHING`; an oath taken that is not the one in the Second Schedule: `JUST FALSE` (the Schedule's answer is an input, QC). An officer the duty does not bind: `NOTHING`.
- **Does the duty bind?** s 64(1)(a), (b), (c) (the Sheriff "must" execute process, make a return, receive persons): `OF:155`, `OF:167`, `OF:178`; s 66(2) (the Accountant "must do all things necessary"): `OF:369`. These ask whether the duty binds on the facts, and answer `JUST TRUE` when it does and `NOTHING` when the facts are outside the words. Nothing was changed here in the fix round: the question is not "was it done".
- **Not changed, a time the text fixes in its own words**: s 41(10)(a), (b) and s 59(10)(a), (b) (the request "must be made before the earlier of" two events, and within 7 days). The periods ruling (a) applies, so a request outside the time answers `JUST FALSE`. Other reading: `NOTHING`, as a bare "must".

### QC: "listed in Schedule N"

The convention taken: the Schedule is another part's text, so whether the case is on its list is a plain yes/no/not-known input (`MAYBE BOOLEAN`), and the function never decides the list's content.
Not known: `NOTHING`, with the comment `-- NOTHING-kind (points outside the text)`.
A case that the input says is not on the list is not turned into a general "no" except where the section itself says so.
The other reading at every line: the Schedule's content is encoded here as a closed list, which this part does not do.

- **s 46** (an appeal "cannot be brought ... in the cases specified in the Ninth Schedule"): `AA:19`. On the list: `JUST FALSE`; not on the list: `NOTHING` (whether an appeal lies in another case is for section 47); not known: `NOTHING`.
- **s 36(1) and s 54(1)** ("Despite section 32(1), a case ... may, if the Seventh Schedule so provides, be heard and decided by (a) either a single Judge or 2 Judges; or (b) 2 Judges"): `AC:96`, `CC:170`. The function takes two inputs: whether the Seventh Schedule allows fewer than 3 Judges in the case, and which smaller panel it allows. Schedule does not allow: `JUST FALSE` (the "if" is not met, ruling (b)); not known: `NOTHING`; allows, with the panel given: `JUST TRUE` or `JUST FALSE` for the number of Judges, and a panel of "a single Judge" alone is `NOTHING` (fork F10). Other reading: the Schedule's answer is one input and "does not allow" is `NOTHING`.
- **s 60E(1)** ("if the Tenth Schedule so provides, be heard and determined by a single Judge"): `CR:69`. The same two inputs, and the same three-way answer, for the Tenth Schedule and a single Judge.
- **s 69(1)** (the oath "set out in the Second Schedule"): `OF:546`. Whether the oath taken is the appropriate one is an input (`MAYBE BOOLEAN`); not known: `NOTHING`.

### QD: a duty, power or prohibition whose "if" or "where" is not met

The convention taken is the ruling of 2026-11-05, parts (b) and (c): an "if", "where", "when" or "upon" that is not met answers `JUST FALSE`, which reads "this provision does not give the power or duty on these facts" and never "no power or duty exists anywhere"; for a prohibition the ruling is applied to the function that asks the provision's own question, "is it barred", and a function that asks "may it be done" answers `NOTHING` when the gate is unmet, because the prohibition is not triggered and the text is silent on the grant.
For a prohibition the function is named as the bar ("the bar ... applies"), so that `JUST FALSE` reads "the bar does not apply on these facts" and `JUST TRUE` reads "the bar applies", which is the form the ruling of 2026-11-05 on "until" bars (part (d)) takes.
The other reading at every line: the unmet gate answers `NOTHING`, because "if A then B" does not say "if not A then not B" (M0(a)).

Prohibitions with a gate (the ruling's literal rule, with the function phrased as the bar):

- **s 37(4) and s 55(4)** ("must not hear a matter in an asynchronous manner if to do so would be inconsistent with the court's duty ... fairly"): `AC:255`, `CC:328`. Inconsistent: `JUST TRUE` (the bar applies); not inconsistent: `JUST FALSE`. The `SHANT` rule is at `AC:270` and `CC:342`.
- **s 41(9) and s 59(9)** ("No request may be made under subsection (8) ... where the Appellate Division that first decided the application is constituted -- (a) by 2 Judges, where the Appellate Division hearing the appeal is constituted by 2 Judges; or (b) by 3 or more Judges"): `AC:700`, `CC:770`. The seat question "am I barred" calls this function. Where the bar applies: `JUST TRUE`; otherwise `JUST FALSE`.
- **s 60G(13)** ("If the Court of Appeal does not grant the application for PACC permission, ... no further proceedings may be taken"): `CP:316`. Not granted: `JUST TRUE`; granted: `JUST FALSE`.
- **s 37(2) and s 55(2)** ("any part of a proceeding where oral evidence is given"): the bar function `AC:226`, `CC:300` answers `JUST FALSE` when no oral evidence is given in the part, which is the ruling; the permission function `AC:210`, `CC:284` asks "may the part be conducted without an oral hearing" and answers `NOTHING` there, because the prohibition is not triggered and the text is silent on that question (subsection (1) is what allows it). Other reading: `JUST FALSE` on the permission function too, which reads as "may not", the opposite of the truth.
- **s 60G(15)** ("if an application for PACC permission is made by a PACP, and prior to the making of that application, the applicant is found ... to have abused the process of the court"): bar `CP:397`, permission function `CP:362`. No such finding: `JUST FALSE` on the bar function, `NOTHING` on the permission function (the prohibition is not triggered and the text is silent on the grant). Other reading: `JUST FALSE` on both.
- **s 60I(1)** ("Where any application ... is pending determination"): bar `CP:656`, permission function `CP:636`. Nothing pending: `JUST FALSE` on the bar function, `NOTHING` on the permission function, for the same reason. Other reading: `JUST FALSE` on both.

Reading note on the four permission functions (s 37(2), s 55(2), s 60G(15), s 60I(1)): their names are phrased as a grant ("the Court of Appeal may grant ..."), and they ask a different question from the bar function, so the two do not answer alike on an unmet gate; read the bar function for "does the bar apply" and the permission function for "may it be done".

Grants, powers and duties:

- **s 30(2)** ("If no appointment is made under subsection (1), the Chief Justice is the President"): `AG:31`. An appointment was made: `JUST FALSE`.
- **s 30(3)(b) and s 48(2)(b)** ("if there is no Supreme Court Judge, the Chief Justice is to appoint a person to preside"): `AG:58`, `CG:60`. A Supreme Court Judge is sitting: `JUST FALSE`. (Which Judge is "the most senior Supreme Court Judge, as determined by section 4" is an input to `AG:43` and `CG:45`: the ranking is section 4's, not this part's, seam 12.)
- **s 33(2) and s 51(2)** ("is to be dismissed if the Judges ... are evenly divided"): `AG:196`, `CG:188`. Not evenly divided: `JUST FALSE`.
- **s 34(1)(b) and s 52(1)(b)** ("may sit on a Saturday, Sunday or public holiday, or during a vacation, if the Chief Justice so appoints"): `AG:232`, `CG:224`. No such appointment: `JUST FALSE`; a day that is none of those: `NOTHING` (limited by its own wording).
- **s 36(3)(a), (b) and s 54(3)(a), (b)** ("Where the Appellate Division [Court of Appeal] is constituted by 3 or more Judges ... and one or more ... are unable ... to continue"): `AC:166`, `AC:181`, `CC:240`, `CC:255`. A panel of fewer than 3, or none unable: `JUST FALSE` for both paragraphs (fork F16 gives the other reading for a 2-Judge panel); every party consents and at least 2 remain: (a) `JUST TRUE`, (b) `JUST FALSE`.
- **s 39 and s 57** ("Where an application may be made either to the General Division or to the Appellate Division"): `AC:400`, `CC:470`, and the functions that return the court at `AC:412`, `CC:482`. No choice of two courts: `JUST FALSE`.
- **s 41(5) and s 59(5)** ("if the evidence relates to matters occurring after the date of the decision appealed against"): `AC:631`, `CC:701`. It does not: `JUST FALSE`.
- **s 41(8) and s 59(8)** ("Where an application for permission to adduce further evidence ... is heard and decided by a single Judge or 2 Judges"): `AC:683`, `CC:753`. Decided by 3 or more: `JUST FALSE`.
- **s 43(3)(a), (b) and s 60A(3)(a), (b)** ("If the substantial wrong or miscarriage of justice ... affects only part of a case"): `AC:865`, `AC:876`, `CC:947`, `CC:958`. It affects the whole case: `JUST FALSE`.
- **s 60G(12)(a), (b)** ("may, if it thinks additional evidence needs to be taken ... (a) where ... a single Judge ... (b) where ... 3 or any greater uneven number"): `CP:286`, `CP:302`. Evidence not thought needed, or the wrong panel for the paragraph: `JUST FALSE` (a pair of alternatives, M5).
- **s 60H(10)** ("may, if it thinks additional evidence needs to be taken"): `CP:617`. Not thought needed: `JUST FALSE`.
- **s 60J(5)(a), (b) and s 60M(4)(a), (b)**: `CP:811`, `CP:827`, `CP:1037`, `CP:1053`. As s 60G(12).
- **s 60H(1)** ("where the Court of Appeal grants the application for PACC permission"): `CP:452`. Not granted: `JUST FALSE`.
- **s 60I(3)** ("When dealing with any specified application or subsequent application under this section"): `CP:722`. Not dealing with one: `JUST FALSE` ("when" counts as "where", ruling (c)).
- **s 60J(1)** ("Where any application or action by a PACP ... is filed in a court other than the Court of Appeal"): `CP:742`. Filed in the Court of Appeal: `JUST FALSE`.
- **s 60J(3)** ("If the Court of Appeal makes a determination under subsection (1)"): `CP:778`. No determination: `JUST FALSE`.
- **s 60M(1)** ("When dealing with any application or action ... on its own motion or upon the application of the Attorney-General or the Public Prosecutor"): `CP:883`. Not dealing with one, or neither motion nor application by those two: `JUST FALSE` ("when" and "upon" count as "where").
- **s 60M(3)** ("where a relevant application is heard before a single Judge"): `CP:1024`. Not heard before a single Judge: `JUST FALSE`.
- **s 61(1)** ("on the recommendation of the Chief Justice"): `OF:23`. No recommendation: `JUST FALSE`; an officer other than the three named: `NOTHING` (limited by its own wording).
- **s 65** ("Where in any cause or matter the Sheriff is an interested party"): `OF:297`. The Sheriff is not an interested party: `JUST FALSE`.
- **s 69(2)** ("where an oath of office is required to be taken and subscribed under subsection (1)"): `OF:594`. No oath required: `JUST FALSE`.

### QE: "(other than X)"

The convention taken: a carve-out stated as "other than X" or "except X" inside a grant or a duty is a scope statement, and a case inside the carve-out answers `NOTHING` (limited by its own wording, or points outside the text when X is given by the Rules of Court), unless the carve-out is itself the whole rule, as at s 72(1).
The other reading at every line except s 72(1): the carve-out is an express exclusion and the case inside it answers `JUST FALSE`.

- **s 37(1) and s 55(1)** ("may decide any matter without hearing oral arguments, other than a matter prescribed by the Rules of Court"): `AC:197`, `CC:271`. A matter the Rules prescribe: `NOTHING` (points outside the text: the Rules of Court are not among the sources, and the text does not say what happens to a prescribed matter). Other reading: `JUST FALSE`, because "other than" expressly excludes the matter from the allowance, so the Court may not decide it without oral arguments.
- **s 60G(15)(b)** ("in relation to an application (other than a relevant application) or action"): `CP:362`. The carve-out is folded into one plain yes/no input, "found ... to have abused the process of the court as paragraph (a) or (b) describes", which the caller sets; the function does not test "relevant application" itself. Other reading: a separate input and a `JUST FALSE` branch.
- **s 60J(1)** ("filed in a court other than the Court of Appeal"): `CP:742`. This is a "where", so QD applies: filed in the Court of Appeal is `JUST FALSE`. Other reading: `NOTHING`.
- **s 60M(1)(b)** ("in the case of an application (other than a relevant application) or action"): `CP:912`. An application that is a relevant application: `NOTHING` (paragraph (a) deals with it). Other reading: `JUST FALSE`.
- **s 72(1)** ("open on every day of the year except on Saturdays, Sundays and public holidays"): `OF:652`. On a Saturday, Sunday or public holiday: `JUST FALSE`, because the sentence states the days on which the Registry is open and closes the list with "except". Other reading: `NOTHING`, "is to be open" says nothing of the excluded days.

### QF: a missing event in a state ledger

None. No section in this range keeps a ledger or a state that is changed by events, so there is no missing event to decide.

## Jural relations (scja2)

Each row gives the Hohfeld relation the provision creates (power, liability, duty, claim-right, privilege, no-right, disability, immunity, or `none` for a definition, a status, a counting rule or a saving), who holds it, who bears it, what it is about, and the name that every function of the provision begins with (a search for the label finds them all).
Where the text does not say who holds the claim-right that correlates with a duty, the row says "not named"; no holder is invented.
Under ruling N2 these kinds stay here, in the table, and are not typed into any answer.
Twin provisions (Appellate Division sections 30 to 45 and Court of Appeal sections 48 to 60C) share a row where they say the same; each is encoded on its own (E1, option C).

| provision | relation | holder | bearer | content | L4 names |
| --- | --- | --- | --- | --- | --- |
| s 30(1) | power | the Chief Justice | a Judge of the Appellate Division (liability to be appointed) | appoint a Judge of the Appellate Division to be its President | `s 30(1) ...` |
| s 30(2) | none | - | - | default designation: if no appointment is made, the Chief Justice is the President of the Appellate Division | `s 30(2) ...` |
| s 30(3), s 48(2) | duty (a); power (b) | (a) the most senior Supreme Court Judge, as determined by section 4; (b) the Chief Justice | (a) claim-right: not named; (b) liability of the person appointed to preside | (a) preside in a sitting (who is the most senior Judge is section 4's, seam 12); (b) where there is no Supreme Court Judge, appoint a person to preside | `s 30(3)(a) ...`, `s 30(3)(b) ...`, `s 48(2)(a) ...`, `s 48(2)(b) ...` |
| s 48(1) | none (status); power | the Chief Justice | the Justices of the Court of Appeal (liability to be appointed) | the Chief Justice is the President of the Court of Appeal and may appoint Vice-Presidents from among the Justices | `s 48(1) ...` |
| s 31(1), s 49(1) | power (jurisdiction) | the Appellate Division; the Court of Appeal | the parties to a matter within the jurisdiction (liability) | has the civil jurisdiction in section 35 (Appellate Division); has the civil jurisdiction in section 53, the criminal jurisdiction in section 60D and the jurisdiction over Division 4 applications (Court of Appeal) | `s 31(1) ...`, `s 49(1) ...` |
| s 31(2) | disability | the Appellate Division | persons in criminal proceedings (immunity) | the Appellate Division has no criminal jurisdiction (fork F2: quasi-criminal) | `s 31(2) ...` |
| s 31(3), s 49(2) | power | the Appellate Division; the Court of Appeal | the court or tribunal appealed from (its powers pass to the appeal court) | in an appeal, all the jurisdiction and powers of the court or tribunal appealed from | `s 31(3) ...`, `s 49(2) ...` |
| s 31(4), s 49(3) | power | the Appellate Division; the Court of Appeal | the parties (liability) | decide any question that needs to be decided to do justice in a case before it | `s 31(4) ...`, `s 49(3) ...` |
| s 32(1), s 50(1) | none (condition on how a power is exercised) | - | - | the jurisdiction is exercised by 3 or any greater uneven number of Judges, subject to the Act (fork F6) | `s 32(1) ...`, `s 50(1) ...` |
| s 32(2), s 50(2) | duty (not to sit) | claim-right: not named (the parties to the appeal) | the Judge who made the decision appealed from | must not sit to hear or decide an appeal from the Judge's own decision, or a related matter | `s 32(2) the prohibition on the Judge`, `s 50(2) the prohibition on the Judge` (regulative, derived under N2) |
| s 32(3), s 50(3) | none (extends another provision) | - | - | section 10A (assessors) applies to the court as it applies to the General Division; the answer is section 10A's, passed through (seam 13) | `s 32(3) ...`, `s 50(3) ...` |
| s 33(1), s 51(1) | none (rule of decision) | - | - | a decision is made in accordance with the opinion of the majority of the Judges hearing the case | `s 33(1) ...`, `s 51(1) ...` |
| s 33(2), s 51(2) | duty | the court | claim-right: not named (the party opposing the appeal or application benefits) | an appeal or application is to be dismissed if the Judges are evenly divided | `s 33(2) ...`, `s 51(2) ...` |
| s 34(1), s 52(1) | (a) power; liability; (b) privilege | (a) the Chief Justice (power), the court (liability); (b) the court | (a) the court sits as appointed; (b) no-right: not named | (a) the court is to sit on the dates and at the places the Chief Justice appoints; (b) it may sit on a Saturday, Sunday or public holiday, or in a vacation, if the Chief Justice so appoints | `s 34(1)(a) ...`, `s 34(1)(b) ...`, `s 52(1)(a) ...`, `s 52(1)(b) ...` (seam 11 answered here) |
| s 34(2), s 52(2) | power | the Chief Justice | the court and the parties (liability) | cancel or postpone a sitting appointed under subsection (1) | `s 34(2) ...`, `s 52(2) ...` |
| s 35(1), s 53(1) | none (scope) | - | - | the Division applies to the court in the exercise of its civil jurisdiction | `s 35(1) ...`, `s 53(1) ...` |
| s 35(2), s 53(2) | power (jurisdiction) | the Appellate Division; the Court of Appeal | the parties (liability) | the civil jurisdiction consists of the matters listed (a closed list; forks F1, F2; the transfer limb is seam 20) | `s 35(2) ...`, `s 53(2) ...` |
| s 36(1), s 54(1) | privilege | the court | no-right of the parties to insist on 3 Judges | a case may be heard and decided by a smaller panel if the Seventh Schedule so provides (fork F10; seam 14) | `s 36(1) ...`, `s 54(1) ...` |
| s 36(2), s 54(2) | duty (not to sit) | claim-right: not named | the Judge who made the direction or order | must not sit to hear an application to discharge or vary the Judge's own direction or order under section 40(1) (58(1)) | `s 36(2) the prohibition on the Judge`, `s 54(2) the prohibition on the Judge` (regulative, derived under N2) |
| s 36(3), s 54(3) | duty | the court | claim-right: the parties, who must all consent (their consent is a power) for the case to continue | continue to hear the case if every party consents and at least 2 Judges remain; otherwise rehear | `s 36(3) ...`, `s 54(3) ...` |
| s 37(1), s 55(1) | power | the court | the parties (liability) | decide a matter without hearing oral arguments, other than a matter the Rules of Court prescribe | `s 37(1) ...`, `s 55(1) ...` |
| s 37(2), s 55(2) | disability (lifted by the parties' consent) | the court | the parties | may not conduct a part where oral evidence is given without an oral hearing, unless all the parties consent (fork F8) | `s 37(2) ...`, `s 55(2) ...` |
| s 37(3), s 55(3) | power | the court | the parties (liability) | direct that a matter be heard asynchronously by exchange of written correspondence | `s 37(3) ...`, `s 55(3) ...` |
| s 37(4), s 55(4) | duty (not to hear asynchronously where unfair) | claim-right: the parties (the duty is to ensure fairness to all parties) | the court | must not hear a matter asynchronously if that would be inconsistent with its duty to ensure fairness | `s 37(4) the prohibition on the Appellate Division`, `s 55(4) the prohibition on the Court of Appeal` (regulative, derived under N2) |
| s 37(5), s 55(5) | none (saving) | - | - | to avoid doubt, the section does not affect the court's power to hear oral arguments | `s 37(5) ...`, `s 55(5) ...` |
| s 38(1), s 56(1) | power | the court | the appellant or applicant (liability) | summarily dismiss an appeal or application on its own motion in the three cases listed | `s 38(1) ...`, `s 56(1) ...` |
| s 38(2), s 56(2) | duty | claim-right: the appellant or applicant | the court | before summarily dismissing, give a reasonable opportunity to show cause and consider the representations | `s 38(2) the duties before summary dismissal`, `s 56(2) the duties before summary dismissal` (regulative) |
| s 38(3), s 56(3) | privilege | the court | no-right: not named | may exercise the summary-dismissal power without hearing oral arguments | `s 38(3) ...`, `s 56(3) ...` |
| s 38(4), s 56(4) | none (definition) | - | - | "appeal" includes part of an appeal and "application" includes part of an application | `s 38(4) ...`, `s 56(4) ...` |
| s 39, s 57 | duty | claim-right: not named | the applicant | an application that may be made to either court must first be made to the General Division (s 39) or to the other court (s 57) | `s 39 ...`, `s 57 ...` |
| s 40(1), s 58(1) | power | the court | the parties (liability) | make incidental directions and orders in a pending appeal or application | `s 40(1) ...`, `s 58(1) ...` |
| s 40(2), s 58(2) | power; power | the court (on its own motion); a party (to apply) | the parties (liability); the court (liability to be asked) | a direction or order may be made on the court's own motion or on a party's application | `s 40(2) ...`, `s 58(2) ...` |
| s 40(3), s 58(3) | none (who may exercise the power) | - | - | a direction or order may be made by 2 Judges | `s 40(3) ...`, `s 58(3) ...` |
| s 40(4), s 58(4) | power (a); disability (b) | (a) 2 other Judges; (b) the applicant who seeks to vary or discharge | (a) the single Judge's direction or order (liability); (b) the applicant needs permission, and a Judge's decision to give or refuse it is final (immunity) | (a) a single Judge's direction or order may be varied or discharged by 2 other Judges; (b) an application to vary or discharge may only be made with a Judge's permission | `s 40(4)(a) ...`, `s 40(4)(b) ...`, `s 58(4)(a) ...`, `s 58(4)(b) ...` |
| s 40(5), s 58(5) | none (applies despite another provision) | - | - | subsections (3) and (4) apply despite section 32(1) (50(1)) | `s 40(5) ...`, `s 58(5) ...` |
| s 41(1), s 59(1) | none (nature of the proceeding) | - | - | appeals are by way of rehearing | `s 41(1) ...`, `s 59(1) ...` |
| s 41(2), s 59(2) | power; duty | the court | the parties (liability) | has all the powers and duties, as to amendment or otherwise, of the court or tribunal appealed from | `s 41(2) ...`, `s 59(2) ...` |
| s 41(3), s 59(3) | power | the court | the parties (liability) | receive further evidence by oral examination, affidavit or deposition | `s 41(3) ...`, `s 59(3) ...` |
| s 41(4), s 59(4) | disability (lifted by permission and special grounds) | the court | the party who would give further evidence | further evidence may be given only with the court's permission and on special grounds, except as subsection (5) provides (fork F8) | `s 41(4) ...`, `s 59(4) ...` |
| s 41(5), s 59(5) | privilege | the party giving further evidence | no-right of the court to refuse | may give further evidence without permission if it relates to matters after the date of the decision appealed against | `s 41(5) ...`, `s 59(5) ...` |
| s 41(6), s 59(6) | power | the court | the parties (liability) | draw any inference of fact, give any judgment and make any order | `s 41(6) ...`, `s 59(6) ...` |
| s 41(7), s 59(7) | none (scope of the powers) | - | - | the powers may be exercised on any part of the decision and in favour of any party | `s 41(7)(a) ...`, `s 41(7)(b) ...`, `s 59(7)(a) ...`, `s 59(7)(b) ...` |
| s 41(8), s 59(8) | power | any party | the full panel (liability to rehear arguments) | request the full panel to rehear arguments on an application for permission to adduce further evidence decided by a single Judge or 2 Judges | `s 41(8) ...`, `s 59(8) ...`, `s 41(8) and (10) the request`, `s 59(8) and (10) the request` (regulative) |
| s 41(9), s 59(9) | disability | the party | - | no request may be made where the court that first decided was 2 Judges and the appeal bench is 2 Judges, or was 3 or more Judges (fork F8) | `s 41(9) ...`, `s 59(9) ...` |
| s 41(10), s 59(10) | none (time limit on the power in subsection (8)) | - | - | the request must be made before the earlier of the extraction of the judgment or order and the expiration of 7 days after the decision (fork F3) | `s 41(10) ...`, `s 41(10)(a) ...`, `s 41(10)(b) ...`, `s 59(10) ...`, `s 59(10)(a) ...`, `s 59(10)(b) ...` |
| s 41(11), s 59(11) | power | the court | the parties (liability) | after rehearing arguments on the request, affirm, vary or set aside the decision on the application | `s 41(11) ...`, `s 59(11) ...` |
| s 42, s 60 | power | the court | the parties (liability) | make any order as to the costs of an appeal or of the proceedings below | `s 42 ...`, `s 60 ...` |
| s 43(1), s 60A(1) | power | the court | the parties (liability) | order a new trial of a matter tried by the General Division (and, for the Court of Appeal, a matter tried by the Appellate Division) (fork F1) | `s 43(1) ...`, `s 60A(1) ...` |
| s 43(2), s 60A(2) | disability (lifted when the improper admission or rejection caused a substantial wrong) | the court | the party who would gain a new trial | a new trial must not be ordered on the ground of an improper admission or rejection of evidence unless it caused a substantial wrong or a miscarriage of justice (fork F8) | `s 43(2) ...`, `s 60A(2) ...` |
| s 43(3), s 60A(3) | power | the court | the parties (liability) | where the wrong affects only part of a case or some of the parties, give final judgment on the rest and direct a new trial of the affected part | `s 43(3)(a) ...`, `s 43(3)(b) ...`, `s 60A(3)(a) ...`, `s 60A(3)(b) ...` |
| s 43(4), s 60A(4) | power | the court | the parties (liability) | order a new trial on any question without interfering with the finding on any other question | `s 43(4) ...`, `s 60A(4) ...` |
| s 44, s 60B | disability; duty (not to reverse) | claim-right: not named (the party who won below) | the court | may not reverse or substantially vary a decision, or order a new trial, on account of an error that does not affect the merits or the jurisdiction | `s 44 the prohibition on the Appellate Division`, `s 60B the prohibition on the Court of Appeal` (regulative, derived under N2) |
| s 45(1), s 60C(1) | none (rule of effect); power | the General Division or the Appellate Division (s 45); the court appealed from or the Court of Appeal (s 60C) | the party who would enforce the decision (liability to a stay) | an appeal does not stay execution or enforcement, unless the named court so orders (fork F8) | `s 45(1) ...`, `s 60C(1) ...` |
| s 45(2), s 60C(2) | immunity; power | the person who did the intermediate act; the court (power to direct otherwise) | - | no intermediate act or proceeding is invalidated except as the court directs (fork F8) | `s 45(2) ...`, `s 60C(2) ...` |
| s 46 | disability | the party who would appeal | - | an appeal cannot be brought in the cases specified in the Ninth Schedule (seam 15) | `s 46 ...` |
| s 47(1) | power (conditional on permission) | the party who would appeal; the Court of Appeal (power to give permission) | the Appellate Division's decision (liability to be appealed) | an appeal against a decision made in the Appellate Division's appellate civil jurisdiction may be brought only with the Court of Appeal's permission | `s 47(1) ...` |
| s 47(2) | disability (lifted when the appeal raises a point of law of public importance) | the Court of Appeal | the applicant for permission | may grant permission only if the appeal raises a point of law of public importance | `s 47(2) ...` |
| s 47(3) | duty | claim-right: not named | the Court of Appeal | have regard to the matters the Rules of Court prescribe (an input; no period or matter is invented) | `s 47(3) ...` |
| s 47(4) | none (to avoid doubt); no-right | - | the applicant has no right to permission even if the point of law is of public importance | (a) the Court of Appeal need not grant permission; (b) permission may be granted even if the Appellate Division's decision was made in an appeal transferred under section 29E(1) or one the Court of Appeal declined to transfer (seam 19) | `s 47(4)(a) ...`, `s 47(4)(b) ...` |
| s 60D | power (jurisdiction) | the Court of Appeal | persons in criminal proceedings (liability) | the criminal jurisdiction consists of the matters in paragraphs (a) to (g), subject to the Act or other written law (K1 for paragraph (a)) | `s 60D(a) ...` to `s 60D(g) ...`, `s 60D ...` |
| s 60E(1) | privilege | the Court of Appeal | no-right of the accused to insist on 3 Judges | a case may be heard and determined by a single Judge if the Tenth Schedule so provides (seam 16) | `s 60E(1) ...` |
| s 60E(2) | duty (not to sit) | claim-right: not named | a Judge who dealt with the earlier stage | must not sit to hear a matter listed in paragraphs (a) to (d), or a related matter | `s 60E(2) the prohibition on the Judge` (regulative, derived under N2) |
| s 60F, s 60F chapeau | none (definitions) | - | - | the terms the Division uses; the definitions apply "unless the context otherwise requires" | `s 60F chapeau ...` |
| s 60F "application for PACC permission" | none (definition) | - | - | means an application for permission to make a PACC application | `s 60F ...` |
| s 60F "application for review permission" | none (definition) | - | - | means an application for permission to make a review application | `s 60F ...` |
| s 60F "counsel" | none (definition) | - | - | means any advocate and solicitor | `s 60F ...` |
| s 60F "Judge of the Court of Appeal" | none (definition) | - | - | means a Judge sitting in the Court of Appeal in accordance with the Act and the Constitution | `s 60F ...` |
| s 60F "PACP" | none (definition) | - | - | means a prisoner awaiting capital punishment | `s 60F ...` |
| s 60F "post-appeal application in a capital case" | none (definition) | - | - | means an application, not a review application, made by a PACP after the relevant date and either for a stay of execution of the death sentence or whose determination calls into question the conviction, the sentence or its carrying out (limb (b)(ii) is the one that uses the relevant date; see fork F4) | `s 60F ...` |
| s 60F Examples | none (illustrations) | - | - | five examples (a) to (e) of an application whose determination calls into question the conviction, the sentence or its carrying out; the list illustrates and does not close the definition, so a case outside it answers NOTHING | `s 60F Examples ...` |
| s 60F "President’s order" | none (definition) | - | - | means the President's order under section 313(1)(f) of the Criminal Procedure Code 2010 that the sentence of death is to be carried out against the PACP | `s 60F ...` |
| s 60F "relevant application" | none (definition) | - | - | means an application for PACC permission, a PACC application, an application for review permission, or a review application (a list closed by "means") | `s 60F ...` |
| s 60F "relevant date" | none (definition; a counting rule) | - | - | for a PACP's first PACC application, the date of the dismissal of the appeal, the imposition of the sentence by the Court of Appeal, or the dismissal of the petition for confirmation; for a later one, the same date or the date of the most recent determination (fork F4) | `s 60F "relevant date" the relevant date`, `s 60F "relevant date" it is made after the relevant date` |
| s 60F "review application" | none (definition) | - | - | means a review application within section 394F of the Criminal Procedure Code 2010 where it reviews an earlier decision of the Court of Appeal on the offence for which the sentence of death was imposed | `s 60F ...` |
| s 60G(1) | duty | claim-right: not named | the applicant | before making a PACC application, apply for and obtain the Court of Appeal's permission (fork F8: the gate "subject to section 60I") | `s 60G(1) the duty of the applicant before making a PACC application` (regulative) |
| s 60G(2) | privilege | the Court of Appeal | no-right of the applicant to insist on 3 Judges | an application for PACC permission may be heard and determined by a single Judge | `s 60G(2) ...` |
| s 60G(3) | duty (bearer not named) | claim-right: not named | not named ("must be fixed") | an application for PACC permission must be fixed for hearing within the Rules of Court's period (an input) | `s 60G(3) ...` |
| s 60G(4) | duty | claim-right: not named | the applicant | file written submissions, and the other documents the Rules of Court prescribe, within the period | `s 60G(4) the duty of the applicant to file written submissions` (regulative) |
| s 60G(5) | privilege | the respondent | no-right: not named | may file written submissions within the period | `s 60G(5) ...` |
| s 60G(6) | power | the Registrar or any Supreme Court Judge | the parties (liability) | extend or abridge a period in subsection (3), (4) or (5) | `s 60G(6) ...` |
| s 60G(7) | duty | claim-right: not named | the Court of Appeal | in deciding whether to grant permission, consider the listed matters | `s 60G(7) ...` |
| s 60G(8) | power | the Court of Appeal | the applicant (liability) | summarily deal with an application by written order, without setting it down for hearing | `s 60G(8) ...` |
| s 60G(9), s 60G(10) | duty (a); privilege (b) | the Court of Appeal (duty to consider the applicant's submissions; privilege to consider the respondent's) | claim-right: the applicant (a); no-right: the respondent (b) | before summarily refusing (9) or granting (10), consider the matters in subsection (7) and the submissions | `s 60G(9)(a) ...`, `s 60G(9)(b) ...`, `s 60G(10)(a) ...`, `s 60G(10)(b) ...` |
| s 60G(11) | power | the Court of Appeal | the applicant and respondent (liability) | at the three stages, make incidental directions or interim orders (including a stay of execution of the death sentence) and take additional evidence (fork F9) | `s 60G(11) ...` |
| s 60G(12) | power | the Court of Appeal | the parties (liability) | take additional evidence itself, or have it taken by one of the Judges where 3 or more Judges deal with the application | `s 60G(12)(a) ...`, `s 60G(12)(b) ...` |
| s 60G(13) | disability; immunity | the PACP and anyone who would continue the proceedings | the PACC application (it cannot proceed) | if permission is not granted, no further proceedings may be taken on the PACC application (fork F8) | `s 60G(13) ...` |
| s 60G(14) | none (saving) | - | - | subsection (13) does not prevent proceedings against the PACP's counsel about the counsel's conduct in the permission application | `s 60G(14) ...` |
| s 60G(15) | duty (not to grant); disability (lifted by new material) | claim-right: not named | the Court of Appeal | after a finding of abuse of process, must not grant permission unless the PACP adduces material not adduced before and that could not with reasonable diligence have been | `s 60G(15) the prohibition on the Court of Appeal` (regulative, derived under N2) |
| s 60H(1) | duty (bearer not named) | claim-right: not named | not named ("must be made ... and fixed") | where permission is granted, the PACC application must be made to the Court of Appeal and fixed for hearing within the Rules of Court's period | `s 60H(1) ...` |
| s 60H(2), s 60H(3) | duty | claim-right: not named | the applicant (2); the respondent (3) | file the documents the Rules of Court prescribe, within the period | `s 60H(2) ...`, `s 60H(3) ...` |
| s 60H(4) | power | the Registrar or any Supreme Court Judge | the parties (liability) | extend or abridge a period in subsection (1), (2) or (3) | `s 60H(4) ...` |
| s 60H(5) | power | the Court of Appeal hearing a PACC application | the parties (liability) | exercise any power and make any order that the Appellate Division or the General Division could have exercised or made (K1) | `s 60H(5) ...` |
| s 60H(6) | power | the Court of Appeal | the applicant (liability) | summarily deal with a PACC application by written order | `s 60H(6) ...` |
| s 60H(7) | duty (a); privilege (b) | the Court of Appeal | claim-right: the applicant (a); no-right: the respondent (b) | before summarily refusing, consider the applicant's submissions and may consider the respondent's | `s 60H(7)(a) ...`, `s 60H(7)(b) ...` |
| s 60H(8) | duty | claim-right: not named | the Court of Appeal | except where subsection (7) applies, before summarily deciding on the merits, consider the applicant's and the respondent's submissions | `s 60H(8) ...` |
| s 60H(9) | power | the Court of Appeal | the parties (liability) | at the three stages, make incidental directions or interim orders and take additional evidence (fork F9) | `s 60H(9) ...` |
| s 60H(10) | power | the Court of Appeal | the parties (liability) | take additional evidence itself or have it taken by one of the Judges | `s 60H(10) ...` |
| s 60I(1) | disability (lifted by the permission of the Court of Appeal) | the PACP | the Court of Appeal's permission | while a specified application is pending, cannot make a subsequent application without permission (fork F8) | `s 60I(1) the prohibition on the PACP` (regulative, derived under N2) |
| s 60I(2) | power | the Court of Appeal dealing with the specified application | the PACP (liability) | grant permission to adduce further material, grant permission to make the subsequent application separately, or refuse | `s 60I(2) ...` |
| s 60I(3) | power | the Court of Appeal | the PACP (liability) | give the directions it thinks necessary or expedient on a specified or subsequent application | `s 60I(3) ...` |
| s 60J(1) | power | the Court of Appeal | the PACP (liability) | where an application or action is filed in another court, determine whether it is or contains an application for PACC permission or a PACC application | `s 60J(1) ...` |
| s 60J(2) | privilege | the Court of Appeal | no-right: not named | a single Judge may make the determination | `s 60J(2) ...` |
| s 60J(3) | power | the Court of Appeal | the PACP (liability) | after a determination that the filing is or contains a PACC application, the measures the subsection lists | `s 60J(3) ...` |
| s 60J(4) | power | the Court of Appeal | the parties (liability) | make incidental directions or interim orders, and take additional evidence, in making the determination | `s 60J(4) ...` |
| s 60J(5) | power | the Court of Appeal | the parties (liability) | take additional evidence itself or have it taken by one of the Judges | `s 60J(5)(a) ...`, `s 60J(5)(b) ...` |
| s 60K | none (saving) | - | - | nothing in the Division affects Division 1B of Part 20 of the Criminal Procedure Code 2010 | `s 60K ...` |
| s 60L | power (exclusive); disability | the Court of Appeal | every other court (disability) | only the Court of Appeal may grant a stay of execution of the death sentence | `s 60L ...` |
| s 60M(1) | power; power | the Court of Appeal (on its own motion); the Attorney-General or the Public Prosecutor (to apply) | the PACP and the PACP's counsel (liability) | decide whether to make a finding of abuse of process | `s 60M(1) ...` |
| s 60M(2) | privilege | the Court of Appeal | no-right: not named | inquire into and take into account the listed matters | `s 60M(2) ...` |
| s 60M(3) | privilege | the Court of Appeal | no-right: not named | a single Judge may make the finding where a relevant application is heard before a single Judge | `s 60M(3) ...` |
| s 60M(4) | power | the Court of Appeal | the parties (liability) | take additional evidence necessary, itself or by a Judge | `s 60M(4)(a) ...`, `s 60M(4)(b) ...` |
| s 61(1) | power | the President (on the Chief Justice's recommendation) | the person appointed (liability) | appoint a Registrar, a Deputy Registrar and Assistant Registrars | `s 61(1) ...` |
| s 61(2) | disability (lifted when the person is a qualified person) | the appointer | - | no one may be appointed Registrar, Deputy Registrar or Assistant Registrar unless a qualified person under the Legal Profession Act 1966 (fork F8) | `s 61(2) ...` |
| s 62(1) | none (delegation to the Rules of Court) | - | - | the Registrar, Deputy Registrar and Assistant Registrars have the jurisdiction, powers and duties the Rules of Court prescribe | `s 62(1) ...` |
| s 62(2) | power | the Deputy Registrar and Assistant Registrars | - | may exercise or perform the Registrar's powers and duties, subject to Rules of Court (fork F8) | `s 62(2) ...` |
| s 63(1) | none (status) | - | - | the Registrar is the Sheriff, the Deputy Registrar the Deputy Sheriff, the Assistant Registrars the Assistant Sheriffs | `s 63(1) ...` |
| s 63(2) | power | the Deputy Sheriff and Assistant Sheriffs | - | have all the powers and privileges and may perform all the duties of the Sheriff | `s 63(2) ...` |
| s 64(1) | duty | claim-right: the Supreme Court | the Sheriff or the Sheriff's officers | (a) execute process given by the Court; (b) make a return of it, with the manner of execution; (c) receive persons committed to custody | `s 64(1)(a) and (b) the duty of the Sheriff to execute the process and make a return`, `s 64(1)(c) the duty of the Sheriff to receive the persons committed to the Sheriff's custody` (regulative) |
| s 64(2) | privilege | the Sheriff or officers | the occupier (no-right) | in executing an enforcement order or a writ of distress, enter a building and break open a door or window using reasonable force | `s 64(2) ...` |
| s 64(3) | privilege | the Sheriff | no-right: not named | engage auxiliary police officers, security agencies and others to assist | `s 64(3) ...` |
| s 65 | power | the court | the Sheriff (liability to be replaced) | where the Sheriff is an interested party, appoint an officer or person to act in the Sheriff's place | `s 65 ...` |
| s 65A(1) | power | the Registrar | the solicitor or person employed by a solicitor (liability) | authorise a solicitor, or a person employed by one, to exercise the powers and perform the duties of a Deputy Sheriff or Assistant Sheriff, subject to the Chief Justice's directions (fork F8) | `s 65A(1) ...` |
| s 65A(2) | none (applies another provision) | - | - | section 79(2) applies to the authorised person as to an officer of the Supreme Court (seam 17) | `s 65A(2) ...` |
| s 66(1) | power | the Chief Justice | the person appointed (liability) | appoint an Accountant for the Supreme Court (fork F7) | `s 66(1) ...` |
| s 66(2) | duty | claim-right: the Supreme Court | the Accountant | do all things necessary to execute the orders of the Supreme Court about suitors' money and securities | `s 66(2) the duty of the Accountant to execute the orders of the Supreme Court` (regulative) |
| s 67(1) | none (establishment); power | the Chief Justice (decides what appears necessary) | - | commissioners for oaths, interpreters, clerks, process servers and other officers are attached as appear necessary to the Chief Justice (fork F5) | `s 67(1) ...` |
| s 67(2) | power | the Chief Justice (approval) | the officer (liability to be attached to a Judge) | officers may, with the Chief Justice's approval, be attached to a particular Judge | `s 67(2) ...` |
| s 68(1) | none (status) | - | - | the Registrar, Deputy Registrar and Assistant Registrars are ex-officio commissioners for oaths | `s 68(1) ...` |
| s 68(2) | power; privilege | the Senate of the Singapore Academy of Law (to appoint); the commissioner (to do the listed things) | the person appointed (liability) | appoint fit and proper persons as commissioners for oaths, who may do the listed things | `s 68(2) ...` |
| s 68(3) | power (rule-making) | the Senate of the Singapore Academy of Law | commissioners for oaths | make rules for appointment, conduct and fees: not encoded (inert, reason 2) | - |
| s 69(1) | duty | claim-right: not named | the Registrar, Deputy Registrar, Assistant Registrars and officers the Chief Justice requires | before exercising their functions, take and subscribe the appropriate oath in the Second Schedule (seam 18) | `s 69(1) the duty of the officer to take and subscribe the oath of office` (regulative) |
| s 69(2) | privilege (to avoid doubt) | the person taking the oath | no-right: not named | may take the oath by live video or television link meeting the three conditions | `s 69(2) ...` |
| s 70 | power (rule-making) | the Chief Justice | the officers of the Supreme Court | make rules for the apportionment of work: not encoded (inert, reason 2) | - |
| s 71(1) | none (establishment); power | the Chief Justice (determines the departments) | - | there is an office called the Registry comprising the departments the Chief Justice determines | `s 71(1) ...` |
| s 71(2) | none (status) | - | - | the Registry is under the control and supervision of the Registrar | `s 71(2) ...` |
| s 72(1) | duty (bearer not named) | claim-right: not named (the public) | not named ("is to be open") | the Registry is open on every day except Saturdays, Sundays and public holidays | `s 72(1) ...` |
| s 72(2) | privilege | the Registrar | no-right: not named | may lawfully sit or carry out the Registry's business on a Saturday, Sunday or public holiday if the Chief Justice has directed so, or the Registrar thinks the business extremely urgent | `s 72(2) ...` |
| s 72(3) | power | the Chief Justice | the Registry (liability) | fix the office hours of the Registry | `s 72(3) ...` |

Rows: 138, covering 191 provisions (every section without subsections, every subsection, and the section 60F definitions) in lines 2310 to 4320; the script that rendered this table checked that none is missing.

## Marginal readings for a lawyer (scja2)

Each reading below is a place where a careful lawyer could answer differently from the encoding, ordered by how likely it is to change an answer.
None is a ruling of Meng's beyond those in the fork register; every one is "assumed, not ruled" and is for a lawyer to confirm.

**M0. The two readings the brief marks "for a lawyer", and the branches that rest on them.**
(a) *A failed "if", "where" or "when" counts as the text's no, and a flat negative counts as the text saying no.* The other reading: "if A then B" does not say "if not A then not B", and "may not" says nothing of the converse, so each such branch would answer `NOTHING`.
The branches resting on the first limb are the unmet-gate branches listed in M2 (64 `FALSE-kind` comments in layer 1 say that an "if", "where", "when" or "upon" is not met, by a search for `is not met` and `counts as "where"` in the generated files, twins counted separately).
The branches resting on the second limb are the flat negatives in ss 31(2), 32(2), 36(2), 37(2), 37(4), 41(9), 43(2), 44, 45(1), 45(2), 46, 50(2), 54(2), 55(2), 55(4), 59(9), 60A(2), 60B, 60C(1), 60C(2), 60E(2), 60G(13), 60G(14), 60G(15), 60I(1) and 61(2), and the bare-"must" sites of fork F11 for the opposite reason (there the flat statement of a duty is not read as a no), and the "only" conditions in ss 40(4)(b), 41(4), 47(1), 47(2), 58(4)(b), 59(4) and 60L (the sections listed are the authority; no count of them is claimed).
(b) *A prohibition or grant limited by its own wording does not count as a no*: the case outside the limit answers `NOTHING`. The other reading: it counts as a no. Every `-- NOTHING-kind (limited by its own wording)` comment in layer 1 rests on this (153 of them, twins counted separately, by a search for `-- NOTHING-kind (limited by its own wording)`).

**M1. A list the text closes answers `JUST FALSE` when no head holds, and a list it leaves open answers `NOTHING`.**
"Consists of the following matters" (ss 35(2), 53(2), 60D) and "means" (s 60F "relevant application") close their lists, so a matter in none of the heads is `JUST FALSE`.
The Examples under s 60F "post-appeal application in a capital case" illustrate and do not close, so a case outside them is `NOTHING`.
Other reading: a list the text does not close with "only" answers `NOTHING` for an unlisted matter, even if it says "consists of".
Section 49(1) ("has the civil jurisdiction ..., the criminal jurisdiction ... and the jurisdiction ...") does not close its list with "only", so a matter in none of the three limbs is `NOTHING`.
One consequence for a quasi-criminal proceeding (fork F2): s 35(2)(a) and s 53(2)(a) answer `JUST FALSE` (not a civil cause or matter, by the closed list) while s 31(2) answers `NOTHING` (the text names "criminal" and says nothing of a quasi-criminal proceeding).

**M2. A "where", "if", "when" or "upon" that is not met on a positive grant or duty answers `JUST FALSE`** (the ruling of 2026-11-05, parts (b) and (c)).
This reads, in a lawyer's terms, as "this provision does not give the power or duty on these facts", and never as "no power or duty exists anywhere".
It applies at ss 30(2) (no appointment made), 30(3)(b) and 48(2)(b) (no Supreme Court Judge), 33(2) and 51(2) (not evenly divided), 34(1)(b) and 52(1)(b) (no appointment by the Chief Justice), 36(3) and 54(3) (the numbers of Judges and the consent), 39 and 57 (no choice of two courts), 41(5) and 59(5) (the evidence is not about later matters), 41(8) and 59(8) (not decided by a single Judge or 2 Judges), 43(3) and 60A(3) (the wrong does not affect only part), 60G(12), 60H(10), 60J(5) and 60M(4) ("if it thinks additional evidence needs to be taken", "where ... a single Judge", "where ... 3 or more"), 60H(1) (permission not granted), 60I(3) and 60M(1) ("when dealing with"), 60J(1) (not filed in another court), 60J(3), 60M(3), 61(1) (not on the Chief Justice's recommendation), 65 (the Sheriff is not an interested party) and 69(2) (no oath required).
Other reading: each of these answers `NOTHING` (M0(a)).

**M3. A gate on a prohibition that is not met answers `JUST FALSE` on the bar function and `NOTHING` on the grant-named function (fork F8, case (a)).**
This follows part (b) of the ruling of 2026-11-05 ("a 'where ...' condition: when it fails the answer is `JUST FALSE`"), and part (d) of the ruling on "until" bars (encode the bar: `JUST TRUE` inside it, `JUST FALSE` outside it).
For s 60I(1) the function `s 60I(1) the bar on a subsequent application applies to the PACP` answers `JUST TRUE` when a specified application is pending and the PACP has no permission, and `JUST FALSE` when nothing is pending and `JUST FALSE` when the Court of Appeal has given permission.
The function named as the permission (`s 60I(1) the PACP can make a subsequent application ...`) asks "may the PACP", and when nothing is pending the prohibition is not triggered and the text is silent on that, so it answers `NOTHING`; `JUST FALSE` there would read "the PACP may not", the opposite of the truth.
The same choice is made at ss 37(4) and 55(4), 41(9) and 59(9), 60G(13), 60G(15) and the "where oral evidence is given" gate of ss 37(2) and 55(2) (see F8 for the full list); at ss 37(4), 55(4), 41(9), 59(9) and 60G(13) the only function is the bar function.
Other readings: (1) the unmet gate leaves the section silent on every function, so `NOTHING` on the bar function too (this was this part's first answer, and it departed from the literal text of the ruling); (2) the grant-named function answers `JUST FALSE` as well (this was the answer from 2026-11-05 to 2026-11-06, and was withdrawn because it reads as "may not").
To go back to (1), change the unmet-gate branch of the bar functions to `NOTHING`; to go to (2), change the unmet-gate branch of the four grant-named functions to `JUST FALSE`.
The seat was audited for the same mismatch: of its 77 questions only `Under section 41(9)` and `Under section 59(9)` are worded as a bar ("am I barred ..."), and they call the bar function; the others are worded as the permission and call the permission function (`Under section 45(1)`, "does my appeal stop the decision I am appealing from being enforced?", calls the grant-named function, which answers `NOTHING` when a stay has been ordered).

**M4. An "unless" or "except" that is met answers `NOTHING` on the function named as the permission, `JUST FALSE` on the function named as the bar, and `JUST FALSE` on s 60F's chapeau.**
Where the text says something must not happen "unless" X, or "except" Y (ss 37(2), 55(2), 41(4), 59(4), 43(2), 60A(2), 45(1), 60C(1), 45(2), 60C(2), 60G(15), 60I(1), 61(2): the sites listed under F8(b)) and X or Y holds, the bar is lifted: the permission function answers `NOTHING` (the section does not itself grant the thing) and the bar function answers `JUST FALSE` (the bar does not apply).
The chapeau of s 60F ("In this Division, unless the context otherwise requires, ...") is a rule about what the defined words mean, not a bar, so when the context does require otherwise the answer is `JUST FALSE`: the definitions do not apply in that use.
Other reading: a met "unless" answers `JUST TRUE` on the permission function (the thing is then allowed), and a met "unless context otherwise requires" answers `NOTHING`.

**M5. In a pair of alternative paragraphs, a `JUST FALSE` from one paragraph's function means "this paragraph does not apply", and the other paragraph may say yes.**
This is the reading most likely to be mistaken for an inversion.
Section 60G(12)(a) lets the Court of Appeal take the evidence itself "where the application ... is dealt with by a single Judge"; the function for (a) answers `JUST FALSE` when 3 Judges deal with the application.
That is not "the Court may not take the evidence itself" in that case: paragraph (b) says it may (either itself or by one of the Judges).
The same holds for ss 60J(5)(a) and (b), 60M(4)(a) and (b), and for ss 36(3)(a) and (b) (continue if every party consents and at least 2 Judges remain; otherwise rehear).
Other reading: a `JUST FALSE` from paragraph (a) is a no for the court. Read the two functions together; the seat questions that ask about these sections are phrased for the pair (`Under section 36(3)(a)` and `Under section 36(3)(b)` for the Appellate Division, and 54(3)(a), (b) for the Court of Appeal).

**M6. Section 31(1) answers `NOTHING`, not `JUST FALSE`, for a matter that section 35(2) says is not in the list.**
Section 31(1) gives the Appellate Division "the civil jurisdiction mentioned in section 35"; it does not say that the Appellate Division has no other jurisdiction.
So a `JUST FALSE` from s 35(2) is turned into `NOTHING` at s 31(1), deliberately (the comment on the branch says "limited by its own wording").
This is a different thing from the rule that a caller never turns `NOTHING` into `JUST FALSE`: here a `JUST FALSE` becomes `NOTHING`. A lawyer who thinks the two sections together exclude the matter would read the s 35(2) answer, which is `JUST FALSE`.
Other reading: s 31(1) answers `JUST FALSE`.

**M7. Panel sizes: another number is not the text's no (forks F6 and F10).**
Sections 32(1) and 50(1) say the jurisdiction "is to be exercised by 3 or any greater uneven number of Judges", subject to the Act; a bench of 2 or of 4 answers `NOTHING`, because the subsections do not say "only".
Sections 36(1) and 54(1) let a smaller panel sit "if the Seventh Schedule so provides"; the encoding takes the Schedule's answer as two inputs: whether the Schedule allows fewer than 3 Judges in the case (yes: go on; no: `JUST FALSE`, because the "if" is not met; not known: `NOTHING`), and which smaller panel it allows; if the Schedule provides "a single Judge" alone, the answer is `NOTHING` for the subsection's two limbs.
Section 60E(1) is built the same way for the Tenth Schedule and a single Judge.
Other reading: "is to be exercised by" is mandatory, so another number answers `JUST FALSE` (an even number, and 1 or 2 Judges where no head of the Seventh Schedule provides for them); and a single Judge alone falls in limb (a) and answers `JUST TRUE`.

**M8. Time (forks F3 and the Rules of Court).**
The 7 days in ss 41(10)(b) and 59(10)(b) are counted from the day after the decision, and section 50(b) of the Interpretation Act moves a last day that is a Sunday or public holiday to the next day that is not.
A reader who takes the staged Interpretation Act module's own answer for a period counted "after" gets `NOTHING`.
The periods the Rules of Court prescribe (ss 60G(3) to (5), 60H(1) to (3)) are plain inputs; if the person does not know the period, the answer is `NOTHING`; if the period is known and has run out, the answer is `JUST FALSE` at s 60G(5) (a "may file") and `NOTHING` at the bare "must" sites ss 60G(3), 60G(4) and 60H(1) to (3) (fork F11).
Other readings: the day of the decision counts as day 1; or the Interpretation Act's silence on "after" answers `NOTHING` (fork F3).

**M9. The Singapore International Commercial Court (fork F1).**
Whether a decision of the SICC is a decision "of the General Division" is not settled by the text, so the four functions that depend on the court named answer `NOTHING` for it (ss 35(2)(a), 53(2)(a), 43(1), 60A(1)(a)), and the seat asks the person for the court that made the decision.
Other readings: the SICC is a division of the General Division, so the answer is `JUST TRUE`; or it is not, so the answer is `JUST FALSE` (fork F1).

**M10. A fact the person may not know is asked as "yes, no or I am not sure"** in the seat.
"I am not sure" becomes `NOTHING` at the point the rule reads it, and no function turns it into `JUST FALSE`.
An answer that depends on section 10A or on a Schedule (section 10A, the Seventh Schedule and the Ninth Schedule: seams 13, 14 and 15) is `NOTHING` while the person is not sure; `Under section 32(3)`, `36(1)`, `46`, `50(3)` and `54(1)` each have an assertion for that case.

### Reading a result: FALSE and NOTHING (scja2)

A seat question and a layer-1 function return one of three answers.

- **`JUST TRUE` ("yes").** The text says yes to this case in its own words, or the case meets every limb of a definition or condition.
- **`JUST FALSE` ("no").** The text says no to this case in its own words: a definition that says "means", a condition introduced by "if", "where", "only if" or "unless" that is not met on a grant or duty, a flat negative ("must not", "may not", "cannot", "no ... may"), or a period the text fixes and the case is outside. A prohibition with no gate is asked as the permission it negates ("may the Judge sit ..."), so `JUST FALSE` there reads as "the Judge must not"; a prohibition with a gate or an exception is asked as the bar ("the bar ... applies"), so `JUST TRUE` there reads as "forbidden" and `JUST FALSE` as "the bar does not apply on these facts" (M3).
- **`NOTHING` ("the Act does not say").** The text does not answer on these facts. Each `NOTHING` branch names why, in a comment beginning `-- NOTHING-kind (...)`: *silent* (the text has no rule for this case), *list not closed* (the text lists examples or limbs and does not say "only"), *includes* (the text says "includes" and the case is outside the named things), *undefined term* (a word the text does not define, such as K1's "General Division" for the SICC), *points outside the text* (the answer is in another Act, a Schedule or the Rules of Court, which are inputs), or *limited by its own wording* (the provision speaks only of what it names). The seat never shows `NOTHING` as "no".

How a caller treats the answers: a function that takes another section's answer as an input passes `NOTHING` through unchanged and never turns it into `JUST FALSE`. The exception recorded in M6 goes the other way, `JUST FALSE` to `NOTHING`, never `NOTHING` to `JUST FALSE`.

Sorted by how they show up:

- **Loud (the tool tells you).** A wrong type or a missing input is a type error from `l4 check`; a name that is not in scope is `name-not-in-definition` or `check/not-a-function`; an assertion that does not hold is "assertion failed". None of these returns an answer.
- **Silent (an answer comes back, exit code 0, and it can read wrongly).**
  1. A `JUST FALSE` from one alternative paragraph reads as "may not" and means "this paragraph does not apply" (M5).
  2. A `NOTHING` where a lawyer expects `JUST FALSE`: a met "unless" on the permission function (M4), a requirement that was not done under a bare "must" (fork F11: the "... as the section requires" functions), a list the text does not close (M1), a panel size the text does not forbid (M7), a quasi-criminal proceeding at s 31(2) (M1).
  3. A `NOTHING` where a lawyer expects `JUST FALSE`, at the other end: s 31(1) for a matter s 35(2) excludes (M6).
  4. A `JUST FALSE` that means only "not by this provision" (M2).
  5. An "I am not sure" input makes the answer `NOTHING`, and the question returns it with exit code 0 as it would any other answer; it is the person's gap, not the Act's.
  6. A trace that neither breaches nor fulfils: s 64(1)(b)'s return has no time in the text, so a trace in which the Sheriff executes the process and makes no return ends with the return still owed (`#TRACE` prints the pending obligation), not with a breach, and not with a pass (finding 2).
  7. A bar function and a permission function on the same section have opposite polarity: `JUST TRUE` on `s 41(9) the bar on a request under subsection (8) applies` means the request is barred, and `JUST TRUE` on a function named as a permission means it is allowed. The name says which, and the seat question that calls a bar function is worded as the bar ("am I barred ...").
  8. An unmet gate on a grant-named prohibition function (`s 37(2)`, `s 55(2)`, `s 60G(15)`, `s 60I(1)`) answers `NOTHING` (the prohibition is not triggered and the text is silent on the grant), while the bar function beside it answers `JUST FALSE` ("no bar"); a reader who expects the same answer from both is reading one of them wrongly, and `JUST TRUE` appears only on the bar function, inside the gate with no exception met.

## Seams (scja2)

The first column is the asker and the second the answerer, as in `PLAN.md`; the input names are the exact `GIVEN` names, character for character, so the lead can connect them at the merge.
A seam whose answering section can say `NOTHING` is typed `MAYBE ...` and the asking function passes `NOTHING` through.
The row numbers are `PLAN.md`'s.

**Asked by this part (rows 12 to 20).**

| # | asking function (module) | answering section (part) | input name | type |
| --- | --- | --- | --- | --- |
| 12 | `s 30(3)(a) the Judge is to preside in a sitting of the Appellate Division` (`scja2-part4-ad-general`); `s 48(2)(a) the Judge is to preside in a sitting of the Court of Appeal` (`scja2-part5-ca-general`) | s 4 (scja1) | `s 4 the most senior Supreme Court Judge among those sitting` | MAYBE `Judge` |
| 13 | `s 32(3) the Appellate Division may summon assessors as section 10A allows` (`scja2-part4-ad-general`); `s 50(3) the Court of Appeal may summon assessors as section 10A allows` (`scja2-part5-ca-general`) | s 10A (scja1) | `s 10A the court may summon assessors` | MAYBE BOOLEAN |
| 14 | `s 36(1) the case may be heard and decided by that number of Judges` (`scja2-part4-ad-civil`); `s 54(1) ...` (`scja2-part5-ca-civil`) | Seventh Schedule (scja3) | `sch 7 the smaller panel the Seventh Schedule allows` | MAYBE `Smaller panel` |
| 15 | `s 46 an appeal can be brought against the decision of the Appellate Division` (`scja2-part4-ad-appeals`) | Ninth Schedule (scja3) | `sch 9 the Appellate Division decision is a case specified in the Ninth Schedule` | MAYBE BOOLEAN |
| 16 | `s 60E(1) the case may be heard and determined by that number of Judges` (`scja2-part5-ca-criminal`) | Tenth Schedule (scja3) | `sch 10 the smaller panel the Tenth Schedule allows` | MAYBE `Smaller panel` |
| 17 | `s 65A(2) the solicitor or person authorised under subsection (1) is not liable to be sued` (`scja2-part6-officers`) | s 79(2) (scja3) | `s 79(2) the officer is not liable to be sued` | MAYBE BOOLEAN |
| 18 | `s 69(1) the officer has taken and subscribed the oath before exercising the functions of the office, as the section requires` (`scja2-part6-officers`) | Second Schedule (scja3) | `sch 2 the oath taken is the appropriate oath of office set out in the Second Schedule` | MAYBE BOOLEAN |
| 19 | `s 47(4)(b) permission may be granted under subsection (1) despite the history of the appeal` (`scja2-part4-ad-appeals`) | ss 29E(1), 29D(1) (scja1) | `s 29E(1) the appeal was transferred to the Appellate Division`; `s 29D(1) the Court of Appeal declined to transfer the appeal to itself` | BOOLEAN each (facts a party can state) |
| 20 | `s 35(2)(b) the matter is an appeal or other process that lies, or is transferred, to the Appellate Division` (`scja2-part4-ad-civil`); `s 53(2)(c) the matter is an appeal or other process that lies, or is transferred, to the Court of Appeal` (`scja2-part5-ca-civil`) | ss 29E(1), 29D(1) (scja1) | `s 29E(1) the appeal was transferred to the Appellate Division` (asked by 35(2)(b)); `s 29D(1) the appeal was transferred to the Court of Appeal` (asked by 53(2)(c)) | BOOLEAN each (facts) |

Each asking function uses only the one input of row 20 that concerns its own court; `PLAN.md` lists both because the two courts' functions are twins.
Rows 19 and 20 are facts a party can state, so they are not `MAYBE`; the seat asks them as yes/no.

**Answered by this part (row 11).**

| # | asking section (part) | answering function (module) | input name in `PLAN.md` |
| --- | --- | --- | --- |
| 11 | s 8A(6) (scja1) | `s 34(1)(a) the place is one that the Chief Justice appointed` (`scja2-part4-ad-general`) and `s 52(1)(a) the place is one that the Chief Justice appointed` (`scja2-part5-ca-general`) | `s 34(1)(a) or s 52(1)(a) the place is one the Chief Justice appointed` (MAYBE BOOLEAN) |

The answering functions take one plain fact, `the Chief Justice has appointed the place`, and answer `JUST TRUE` when it holds and `NOTHING` when it does not (the text does not say that a sitting at another place is invalid).
The names differ from `PLAN.md`'s input name because the lead connects the input to the function at the merge; the type, `MAYBE BOOLEAN`, is the same.

**Not seams** (`PLAN.md` lists rule-making and prescribing powers, among them ss 47(3) and 60G(3) to (5), as not seams): this part takes what the Rules of Court prescribe as plain inputs named for the section: s 47(3) (the matter is one the Rules of Court prescribe: a `BOOLEAN`), ss 60G(3) to (5) and 60H(1) to (3) (the prescribed period in days: a `MAYBE NUMBER`).
Sections 41(10)(b) and 59(10)(b) call the staged Interpretation Act module directly (section "Dependencies").

## Findings

Numbered; each says what was observed and where.
Findings 1, 5 and 6 are about the plain-text rendering, not about the Act, and nothing in them claims the official text reads the same.

1. **The definition of "relevant date" in s 60F prints sub-paragraph "(ii)" twice in paragraph (b)**, at lines 3583 ("(ii) if prior to the making of the instant application, there has been a determination of --") and 3592 ("(ii) in relation to the PACP, the date of the most recent of any such determination;"), with (A) and (B) between them.
   The second reads as the tail of the first (the date of the most recent such determination), and is encoded as the end of limb (b)(ii) (fork F4); the coverage table carries it as its own row, `s 60F "relevant date"(b)(ii) [second, as printed]`.
2. **Section 64(1)(b) fixes no time for the return.**
   The Sheriff "must ... make a return of the same together with the manner of the execution thereof to the Supreme Court from which the process issued".
   The regulative rule `s 64(1)(a) and (b) ...` has no `WITHIN`, so a trace in which the Sheriff executes the process and makes no return ends with the return still owed and not with a breach (the second `#TRACE` after the rule shows it).
3. **The Appellate Division sections and their Court of Appeal twins differ in places, and the encoding differs with them.**
   Section 53(2) lists four heads where s 35(2) lists two: it adds "any appeal from the Appellate Division" (b) and (d) an application, made to any of the three courts, in which a common question of law or fact arises with a matter in the Court of Appeal's criminal jurisdiction, or any relief claimed may affect that matter or its outcome; s 35(2) says "any written law" and s 53(2) says "any other written law".
   Section 60A(1) has two heads (a matter tried by the General Division, or by the Appellate Division) where s 43(1) has one.
   Section 49(1) names three jurisdictions (civil, criminal, and Division 4) where s 31(1) names one, and s 31(2) ("no criminal jurisdiction") has no twin.
   Section 57 sends an application to "the other court" first, where s 39 sends it to the General Division first.
   Sections 45(1) and 60C(1) differ in whose stay counts (the General Division or the Appellate Division; the court appealed from or the Court of Appeal), and ss 44 and 60B differ in whose jurisdiction an immaterial error must not affect.
4. **The staged Interpretation Act module has no rule for a period counted "after" a day, and answers `NOTHING`** (finding of the module itself, restated here because sections 41(10)(b) and 59(10)(b) say "7 days after the date on which the decision ... is made"); see `## Dependencies` and fork F3.
5. **Sections 60G(11) and 60H(9) letter their last two items "(d)" and "(e)"** after the three stages "(a)", "(b)", "(c)", although the items follow "do one or both of the following" and read as a second list.
   The encoding labels the items as printed, (d) and (e), and `s 60G(11)` and `s 60H(9)` take the stage and the measure as two separate inputs.
6. **The heading of s 60J is printed after the page furniture at the foot of s 60I(3), as three lines** ("Court of Appeal may determine whether application is, or action contains, application for PACC permission or PACC application, etc.", lines 3865 to 3867), and is classed as a heading (inert, reason 1), not as part of s 60I(3)(b).
7. **The seat's wiring helpers carry the prefix `scja2 seat:` and not a section label.**
   The brief requires every name to begin with its section label, but a helper such as "what I say, as a fact" belongs to no section, and a merged seat layer imports every part at once, so two parts cannot define the same name.
   The prefix `scja2 seat:` is not a section label and cannot be another part's (`scja1`, `scja3`), and every helper, its type and its constructors carry it.

### What the text does not answer

- **Who must not appoint, in s 61(2).** The text says a person "must not be appointed to be or to act as" a Registrar unless a qualified person; it names the object of the appointment and not the appointer, so there is no `SHANT` rule for it, and a met "unless" answers `NOTHING`.
- **What follows from a bench of another size** (ss 32(1), 50(1)), **from a Judge sitting contrary to a prohibition** (ss 32(2), 36(2), 50(2), 54(2), 60E(2)), **or from a sitting at a date or place the Chief Justice did not appoint** (ss 34(1)(a), 52(1)(a)): the text states the rule and no consequence.
- **Whom the Chief Justice may appoint to preside** where there is no Supreme Court Judge (ss 30(3)(b), 48(2)(b)): the text says "a person".
- **What a stay ordered under s 45(1) or s 60C(1) covers**, and whether an invalidity direction under s 45(2) or s 60C(2) is itself reviewable.
- **The time for the return** (finding 2), **and the periods** in ss 60G(3) to (5) and 60H(1) to (3), which the text leaves to the Rules of Court, which are not among the sources.
- **Whether the Singapore International Commercial Court is "the General Division"** (fork F1) **and whether a quasi-criminal proceeding is "criminal"** (fork F2).
- **Which of two readings of the stray "(ii)"** the official text intends (finding 1).
- **Who is "the most senior Supreme Court Judge, as determined by section 4"** (ss 30(3)(a), 48(2)(a)). Section 4 is not in this part's range, so the ranking is a plain input (`s 4 the most senior Supreme Court Judge among those sitting`, seam 12), and the function compares the Judge asked about with it; it does not compute the ranking. So it does not say who presides in a sitting of a Justice of the Court of Appeal, a Judge of the Appellate Division and a Judge of the High Court (section 4 ranks the Justices of the Court of Appeal ahead of the Judges of the Appellate Division, at paragraphs (c) and (e)), nor in a sitting of a Judge of the High Court and two Senior Judges (the definition of "Supreme Court Judge" at line 428 names the Chief Justice, a Justice of the Court of Appeal, a Judge of the Appellate Division and a Judge of the High Court, and no Senior Judge); each answer depends on the input, which the caller supplies.
- **The time limit for filing a notice of appeal to the Appellate Division, the court fee for filing an appeal in the Court of Appeal, and who may appear for a party (rights of audience) before either court.** Lines 2310 to 4320 contain no provision on any of the three (a search of them for "notice of appeal", "fee", "audience" and "appear for" finds only the Senate's fee-setting rule-making power at s 68(3) for commissioners for oaths, which is inert), so no function was written and the answer to each is `NOTHING`.
- **The seat does not ask those three silent questions** ("Does this Act set the deadline for my notice of appeal?", "Who may appear for me?" and the fee question). Every seat question is named "Under section N", calls a layer-1 function and is asserted against it; these have no section in this range and so no function to call, and a question would return a constant `NOTHING`.
- **Who may cancel or postpone a sitting** (ss 34(2), 52(2)). The text gives the power to the Chief Justice; it does not say whether anyone else may. The function takes "the sitting was appointed under subsection (1)" as a plain fact and has no input for who cancels, so it cannot answer for another person.
- **What happens to a panel of 2 Judges that loses a Judge** (ss 36(3), 54(3)). The subsections speak of a panel "of 3 or more Judges"; a 2-Judge panel (allowed by ss 36(1), 54(1)) that loses a Judge is outside their words, and the text gives no rule for it. Both functions answer `JUST FALSE` for it under the "where" ruling (fork F16), which is not an answer to what the Court does.
- **Section 68(3) (the Senate's rule-making power over commissioners for oaths) and s 70 (the Chief Justice's power to make rules for the apportionment of work)** are inert in the coverage table (reason 2): rule-making machinery from which no decision follows, so no function was written for either. A lawyer who wants them encoded would add a function for the holder of the power, in the way of `s 62(1)`.
- **Whether a matter tried in the exercise of criminal jurisdiction can be ordered to be retried** under ss 43(1) and 60A(1) is not answered: the sections speak of "civil jurisdiction" only, and the functions answer `NOTHING` for a matter that was not tried in the exercise of civil jurisdiction (fork F14).

## What the main binary does not accept

Each item was met while writing this part on main build 1.6.109 and re-run on 1.6.108.
All of them are loud (an error from `l4 check` or `l4 run`).

1. **`??` is not an operator.** A default of the form `x ?? y` on a `MAYBE NUMBER` is a parse error (it was met in a first draft of s 60H(1)). The encoding uses `CONSIDER` on the `MAYBE` with `WHEN NOTHING` and `WHEN JUST n`.
2. **A `LIST` whose members sit on separate lines needs a comma between members.** Without commas the members are parsed as one function application and `l4 check` reports `check/not-a-function`.
3. **A function whose definition head names arguments must name all of the `GIVEN` names.** One fewer gives `name-not-in-definition` (met at s 72(2), where the head now lists all four).
4. **A call that is compared needs brackets.** `#ASSERT (f x) EQUALS JUST TRUE`; without them the type checker reports a `MAYBE` where a `BOOLEAN` was expected (`PLAN.md`'s recipe says the same).
5. **A `#TRACE`'s outcome cannot be asserted, and `check.sh` does not count it.** The 21 regulative rules in this part have 23 traces between them (read from the output of `l4 run`): each of the eleven `SHANT` rules has one trace, which ends in `BREACH`; eight duty rules have one trace each, which ends in `FULFILLED` (`s 38(2)`, `s 56(2)`, `s 41(8) and (10)`, `s 59(8) and (10)`, `s 60G(1)`, `s 64(1)(c)`, `s 66(2)`, `s 69(1)`); `s 60G(4)` has two, `FULFILLED` and `BREACH`; and `s 64(1)(a) and (b)` has two, `FULFILLED` and one that ends with the return still owed (finding 2). Each rule therefore has a decision-function twin over the same facts, and the tests assert the twin: the prohibitions are the permission functions `s 32(2) the Judge may sit ...`, `s 36(2)` and `s 44` (each with its Court of Appeal twin) and `s 60E(2)`, and the bar functions `s 37(4) the bar on hearing the matter in an asynchronous manner applies to ...` (with its twin `s 55(4)`), `s 60G(15) the bar on granting ... applies` and `s 60I(1) the bar on a subsequent application applies to the PACP` (the last two have a grant-named function beside them and no Court of Appeal twin); the duties are the functions `s 38(2)` and `s 56(2)` (the requirements are met, "... as the section requires"), `s 41(8)`, `s 41(10)`, `s 60G(1)` ("... as the section requires"), `s 60G(4)` ("... as the section requires"), `s 64(1)(a)`, `s 64(1)(b)`, `s 64(1)(c)`, `s 66(2)` and `s 69(1)` ("... as the section requires"). The traces were read by eye and compared between the two builds with a script (identical; section "What check.sh prints").

## What check.sh prints

Run on 2026-11-05 in this folder, with `L4` set to main build 1.6.109 (4c887e0, 2026-11-04) and `L4_MAIN` to main build 1.6.108 (2ae7c9b, 2026-11-02), after the last edit to any `.l4` file here.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
scja-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
scja2-cases-seat.l4                            0       233       0        0         0 |      0       233       0        0  same
scja2-part4-ad-appeals.l4                      0         0       0        0         0 |      0         0       0        0  same
scja2-part4-ad-civil.l4                        0         0       0        0         0 |      0         0       0        0  same
scja2-part4-ad-general.l4                      0         0       0        0         0 |      0         0       0        0  same
scja2-part5-ca-capital-defs.l4                 0         0       0        0         0 |      0         0       0        0  same
scja2-part5-ca-capital.l4                      0         0       0        0         0 |      0         0       0        0  same
scja2-part5-ca-civil.l4                        0         0       0        0         0 |      0         0       0        0  same
scja2-part5-ca-criminal.l4                     0         0       0        0         0 |      0         0       0        0  same
scja2-part5-ca-general.l4                      0         0       0        0         0 |      0         0       0        0  same
scja2-part6-officers.l4                        0         0       0        0         0 |      0         0       0        0  same
scja2-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
scja2-tests-part4-ad-appeals.l4                0        17       0        0         0 |      0        17       0        0  same
scja2-tests-part4-ad-civil.l4                  0       180       0        0         0 |      0       180       0        0  same
scja2-tests-part4-ad-general.l4                0        48       0        0         0 |      0        48       0        0  same
scja2-tests-part5-ca-capital-defs.l4           0        60       0        0         0 |      0        60       0        0  same
scja2-tests-part5-ca-capital.l4                0       171       0        0         0 |      0       171       0        0  same
scja2-tests-part5-ca-civil.l4                  0       197       0        0         0 |      0       197       0        0  same
scja2-tests-part5-ca-criminal.l4               0        23       0        0         0 |      0        23       0        0  same
scja2-tests-part5-ca-general.l4                0        47       0        0         0 |      0        47       0        0  same
scja2-tests-part6-officers.l4                  0       132       0        0         0 |      0       132       0        0  same
sgia-interpretation-time.l4                    0         0       0        0         0 |      0         0       0        0  same
TOTAL (22 modules)                             0      1108       0        0           |      0      1108       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**Baseline it replaced.**
`check.sh` as supplied, run in a copy of this folder that held only `check.sh`, `srcrefs.py` and the keel `scja-core.l4`, printed one module and no assertion: `scja-core.l4  0 errors, 0 satisfied, 0 failed, 0 refused, same on both builds` and `TOTAL (1 modules) 0 0 0 0`.
This part's run prints 22 modules (the keel, the dependency, nine layer-1 modules, nine test files and the seat pair) and 1108 satisfied assertions on each build: 0 errors, 0 failed, 0 refused, every module `same`.
The 1108 are the tests of nine modules (17 + 180 + 48 + 60 + 171 + 197 + 23 + 47 + 132 = 875) and the 233 assertions over the 77 seat questions.

**What the `same` column does not see**, as the script says: a different `#TRACE` outcome, or any difference no assertion exercises.
So the two builds were also compared whole: `l4 check` and `l4 run` were run on every one of the 22 files on each build and the outputs compared after dropping the `Info |` header line: 411,267 bytes on each, identical, which includes the 23 `#TRACE` results (`eval/result`) and the 1108 `eval/assertion-passed` messages (1131 diagnostics in all).
Every diagnostic on either build has severity `Information`; none is an error or a warning, and a search of the output for `is at the end of the file`, `follows code on its line` and `Unknown annotation` found nothing.

**Source locators.**
`python3 -I srcrefs.py check --refs ../../../inputs/SCJA1969.txt scja2-*.l4`, `check --strict` and plain `check` each printed `srcrefs check: 1326 src: lines, 275 runs, 275 locators, 0 problems`.
(`--refs` and `--strict` are alternatives in the script's usage line, so each was run alone.)
