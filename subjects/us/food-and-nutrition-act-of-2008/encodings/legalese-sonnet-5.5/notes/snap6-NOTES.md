# NOTES (snap6): Food and Nutrition Act of 2008 (United States, 7 U.S.C. ch. 51), sections 2026, 2031, 2033, 2034, 2035, 2036 and 2036a

Part agent snap6, lines 2392-2655, 2842-2950 and 2979-3264 of `usc07-ch51.txt`.
**The source text is a plain-text rendering made by a converter script from the United States Code; it is not the official text.
Nothing in this encoding is "verified against the official text".**
Title 7 is not positive law, editorial and statutory notes are omitted from the rendering, and the footnotes the converter kept are kept as they stand.

Where `PLAN.md` and the part brief (`BRIEF.md`) differ, the brief governs, as the brief says.
I found three places where the brief asks for more than the plan, and followed the brief: the rule of 2026-10-29 for `JUST FALSE` and `NOTHING` (a `MAYBE BOOLEAN` seam input passes `NOTHING` through, and every branch carries its kind); the seat layer, whose questions are named "Under section N, ..."; and `srcrefs.py check --strict` beside `--refs` (PLAN.md section 1 names only `--refs`). I found no place where the two conflict.
PLAN.md section 5 forecasts the core names `Party`, `Benefit`, `Area`, `Annual table` and `Kind of decision` for snap6; of the core types, none of `Benefit`, `Area`, `Annual table` and `Kind of decision` is used in any snap6 file, and of the `Party` constructors only `the Secretary` (93 code lines) and `the State agency` (41) are used; `the household` is named in a comment in `snap6-s2031.l4` and used by no rule (checked by grep over the 14 snap6 files).

## Seat (snap6)

One seat, as the Commons guide requires first: **a member of a household that applies for, or receives, benefits under the Supplemental Nutrition Assistance Program (SNAP)**, asking on facts they can state what the sections of snap6's ranges mean for them.
The seat layer is `snap6-seat.l4` (41 questions, each named "Under section N, ..." with `@export` and `@desc`, grouped under `§` headings in the text's order) and `snap6-cases-seat.l4` (123 assertions, all satisfied).
It imports `snap6-s2026`, `snap6-s2031`, `snap6-s2035` and `snap6-s2036a` and calls their rules; it restates none of them.
There is no seat for an official: the Secretary's, a State agency's and a grantee's own duties are in layer 1 only.
Questions are asked of **one** case, the text's natural unit: one household, one adult member (`s 2026(d)(3)`), one vehicle (`s 2026(h)`), one parent (`s 2031(c)(1)`); the list the layer-1 rule takes is built as a one-item list inside the question.
A seam input (an answer another section of the Act gives) stays `MAYBE BOOLEAN` or `MAYBE NUMBER` in the seat and is named for the answering section, so the person can leave it blank and the answer stays "not covered".
No question is asked of s 2033 (repealed), s 2034 (community food projects: grants to private nonprofit entities, Secretary and Congress) or s 2036 (commodities for the emergency food assistance program: purchases by the Secretary and State funds); they address only the Secretary, grantees and States, and nothing in them is done to a household member that the member could state facts about.
The sections asked are s 2026 (17 questions), s 2031 (16), s 2035 (5) and s 2036a (3), 41 in all.

Defaults ruled on 2026-10-18, followed or departed from:
- **Followed:** the Act alone (the cost-of-living tables and other instruments are not among snap6's inputs, so a number the text leaves to the Secretary or to a table is an input); the actors the text names (with FR-26-1, FR-31-5 and FR-35-1 for "the State"); a judgment the text hands to someone else answered as a conditional input (`MAYBE BOOLEAN`), never guessed; the Act's own definitions worked out from facts (s 2031(j), s 2034(a), s 2035(a), s 2036a(a)); one case as the natural unit; the Act's own terms, each with a plain gloss in a comment.
- **Departed from, as the brief of 2026-10-22 requires:** machinery is not left out. Provisions that address only an official (reports to Committees, audits, payments among governments, deadlines on the Secretary) are encoded in layer 1 as regulative rules and decision functions, and in layer 2 only for what they mean to the person (usually nothing, so no question).

## Method

Layer 1 is one module per section, each with a test file, written from the text mechanically quoted: every rule is preceded by `-- src:` lines copied by script from `usc07-ch51.txt` and an `@ref` locator.
`work/build.py` expands the sources in `work/src/` (the markers `#QREF`, `#Q`, `#HELPERS`, `#INCLUDE`, `#DEF`) so that no wording is retyped.
The expected values in the tests were decided from the text before each file was run; where a test failed, the module or the reading was reconsidered and the expected value was not edited to match.
Every top-level name, type and constructor begins with its section label (`s 2026(a)(2) ...`); each test file ends with a section that touches every constructor and field declared in its module.
A timed duty is both a regulative rule (run with `#TRACE`; the stable binary cannot assert a trace's outcome, so the expected outcome is written in a comment and printed by the run) and a decision function over days or dates (asserted on both sides of the limit).

Units: a percentage input is a number of percent as printed in the text (15 means 15 percent, never 0.15) in `s 2026(b)(1)(B)(iii)` and `(iii)(I)`, `s 2026(k)(2)(C)(i)`, `s 2036(a)(2)` and `s 2036a(d)(1)`; dollars, counts and days are plain numbers.

Checks run, on the stable binary 1.6.98 (main, 7689b0d, 2026-10-19) with `JL4_LIBRARY_PATH` unset, and on the main build 1.6.108 (main, 2ae7c9b, 2026-11-02) for the comparison:
- `l4 run` on every module (no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`: both counts are 0 in all 14 snap6 files);
- the trace outcomes of the six tests files on the stable build against the main build (identical, below);
- `srcrefs.py check --refs` and `check --strict` over every `.l4` file of snap6: 0 problems;
- `work/coverage.py`: the coverage audit below;
- `check.sh`, whose output is at the end of this file.

## Coverage (snap6)

units counted: 533; rows in the table: 533; non-blank lines in the three ranges: 652; lines not in any row: 0; lines in two rows: 0; unmapped units: 0; by disposition: encoded=416, fork=49, inert1=67, repealed=1.
Before the s 2026 rows were written, 346 of the 533 units had a row; after, all 533 have one.
Units are the text's own: every section, subsection, paragraph, subparagraph, clause, subclause and item of the ranges, plus the source credits; a heading line and a bare number are folded into the unit they head.
Every non-blank line of the three ranges (652) lies in exactly one unit, and no line lies in two.
Each unit has exactly one disposition: `encoded`, `inert` (reason 1 not operative: a heading, a bare number, the source credit; no unit of snap6 is reason 2 or reason 3), `fork` or `repealed or blank in this text`.
There is no out-of-scope row and no deferred row.

| section | units | encoded | inert (reason 1) | inert (reason 2) | inert (reason 3) | fork | repealed or blank in this text |
| --- | --- | --- | --- | --- | --- | --- | --- |
| s 2026 | 208 | 172 | 23 | 0 | 0 | 13 | 0 |
| s 2031 | 101 | 67 | 14 | 0 | 0 | 20 | 0 |
| s 2033 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| s 2034 | 58 | 47 | 9 | 0 | 0 | 2 | 0 |
| s 2035 | 38 | 24 | 7 | 0 | 0 | 7 | 0 |
| s 2036 | 26 | 16 | 4 | 0 | 0 | 6 | 0 |
| s 2036a | 101 | 90 | 10 | 0 | 0 | 1 | 0 |
| total | 533 | 416 | 67 | 0 | 0 | 49 | 1 |

s 2033 is repealed: the heading at line 2979 says so and the section has no text; its one row is `repealed or blank in this text`.

| unit | lines | text begins | disposition | L4 name or note |
| --- | --- | --- | --- | --- |
| s 2026 | 2392 | Research, demonstration, and evaluations | inert1 | the section heading (title) |
| s 2026(a) | 2393 | (a) Contracts or grants; issuance of aggregate allotments | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(a)(1) | 2394 | (1) The Secretary may enter into contracts with or make gran | encoded | `s 2026(a)(1) the Secretary's permission to enter into contracts or make grants for research` and `s 2026(a)(1) the waiver authority of subsection (b) extends to the instrument` |
| s 2026(a)(2) | 2395 | (2) The Secretary may, on application, permit not more than  | encoded | `s 2026(a)(2) the Secretary's permission to permit two State agencies to issue aggregate allotments`, `s 2026(a)(2) the number of State agencies permitted is within the limit`, `s 2026(a)(2) the household may receive the aggregate allotment`, `s 2026(a)(2) the household may begin to receive combined allotments`, `s 2026(a)(2) the first aggregate allotment was provided in time` |
| s 2026(b) | 2396 | (b) Pilot projects | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(b)(1) | 2397 | (1) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(b)(1)(A) | 2398 | (A) The Secretary may conduct on a trial basis, in one or mo | encoded | `s 2026(b)(1)(A) the Secretary's permission to conduct a pilot or experimental project` and `s 2026(b)(1)(A) the Secretary may waive the requirement of this chapter` |
| s 2026(b)(1)(B) | 2399 | (B) Project requirements.— | inert1 | a heading ("Project requirements"): its content is in the sub-units below |
| s 2026(b)(1)(B)(i) | 2400-2401 | (i) Program goal.— | encoded | `s 2026(b)(1)(B)(i) the Secretary may conduct the project` (lead-in and limbs (I) and (II)) |
| s 2026(b)(1)(B)(i)(I) | 2402 | (I) the project is consistent with the goal of the supplemen | encoded | a limb of s 2026(b)(1)(B)(i): see the rows above (s 2026(b)(1)(B)(i) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(i)(II) | 2403 | (II) the project includes an evaluation to determine the eff | encoded | a limb of s 2026(b)(1)(B)(i): see the rows above (s 2026(b)(1)(B)(i) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(ii) | 2404-2405 | (ii) Permissible projects.— | encoded | `s 2026(b)(1)(B)(ii) the Secretary may conduct the project for the purpose` (lead-in; purposes (I) to (IV) are the constructors of `s 2026 purpose of a project`) |
| s 2026(b)(1)(B)(ii)(I) | 2406 | (I) improve program administration; | encoded | a limb of s 2026(b)(1)(B)(ii): see the rows above (s 2026(b)(1)(B)(ii) the Secretary may conduct the project for the purpose) |
| s 2026(b)(1)(B)(ii)(II) | 2407 | (II) increase the self-sufficiency of supplemental nutrition | encoded | a limb of s 2026(b)(1)(B)(ii): see the rows above (s 2026(b)(1)(B)(ii) the Secretary may conduct the project for the purpose) |
| s 2026(b)(1)(B)(ii)(III) | 2408 | (III) test innovative welfare reform strategies; or | encoded | a limb of s 2026(b)(1)(B)(ii): see the rows above (s 2026(b)(1)(B)(ii) the Secretary may conduct the project for the purpose) |
| s 2026(b)(1)(B)(ii)(IV) | 2409 | (IV) allow greater conformity with the rules of other progra | encoded | a limb of s 2026(b)(1)(B)(ii): see the rows above (s 2026(b)(1)(B)(ii) the Secretary may conduct the project for the purpose) |
| s 2026(b)(1)(B)(iii) | 2410-2411 | (iii) Restrictions on permissible projects.— | encoded | `s 2026(b)(1)(B)(iii) the restrictions apply to the project` |
| s 2026(b)(1)(B)(iii)(I) | 2412 | (I) may not include more than 15 percent of the number of ho | encoded | `s 2026(b)(1)(B)(iii)(I) the project may include that share of the State's households` |
| s 2026(b)(1)(B)(iii)(II) | 2413 | (II) shall continue for not more than 5 years after the date | encoded | `s 2026(b)(1)(B)(iii)(II) the project may continue` |
| s 2026(b)(1)(B)(iv) | 2414-2415 | (iv) Impermissible projects.— | encoded | `s 2026(b)(1)(B)(iv) the Secretary may conduct the project` (lead-in; limbs (I) to (VII) are the fields of `s 2026 project`) |
| s 2026(b)(1)(B)(iv)(I) | 2416 | (I) involves the payment of the value of an allotment in the | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(II) | 2417 | (II) has the effect of substantially transferring funds made | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III) | 2418 | (III) is inconsistent with— | encoded | `s 2026(b)(1)(B)(iv)(III) the provision is one a project may not be inconsistent with` (lead-in; (aa) to (jj) are the constructors of `s 2026 provision`) |
| s 2026(b)(1)(B)(iv)(III)(aa) | 2419 | (aa) paragraphs (4) and (5) of section 2012(m) of this title | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(bb) | 2420 | (bb) the last sentence of section 2014(a) of this title, ins | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(cc) | 2421 | (cc) section 2014(c)(2) of this title; | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(dd) | 2422 | (dd) paragraph (2)(B), (4)(F)(i), or (4)(K) of section 2015( | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(ee) | 2423 | (ee) section 2017(b) of this title; | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(ff) | 2424 | (ff) section 2020(e)(2)(B) of this title; | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(gg) | 2425 | (gg) the time standard under section 2020(e)(3) of this titl | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(hh) | 2426 | (hh) subsection (a), (c), (g), (h)(1)(F), (h)(2), or (h)(3)  | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(ii) | 2427 | (ii) this paragraph; or | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(III)(jj) | 2428 | (jj) subsection (a)(1) or (g)(1) of section 2029 of this tit | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(IV) | 2429 | (IV) modifies the operation of section 2014 of this title so | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(IV)(aa) | 2430 | (aa) increasing the shelter deduction to households with no  | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(IV)(bb) | 2431 | (bb) absolving a State from acting with reasonable promptnes | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(V) | 2432 | (V) is not limited to a specific time period; | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(VI) | 2433 | (VI) waives a provision of section 2035 of this title; or | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(iv)(VII) | 2434 | (VII) waives a provision of section 2016(i) of this title. | encoded | a limb of s 2026(b)(1)(B)(iv): see the rows above (s 2026(b)(1)(B)(iv) the Secretary may conduct the project) |
| s 2026(b)(1)(B)(v) | 2435-2436 | (v) Additional included projects.— | encoded | `s 2026(b)(1)(B)(v) the project may be included in a pilot or experimental project` |
| s 2026(b)(1)(B)(vi) | 2437-2438 | (vi) Cash payment pilot projects.— | encoded | `s 2026(b)(1)(B)(vi) the project shall be continued` (seam: s 2027(a) appropriations) |
| s 2026(b)(1)(C) | 2439 | (C) | encoded | `s 2026(b)(1)(C) the waiver or demonstration program may be approved` (clause (i) with limbs (I) and (II), and clause (ii)) |
| s 2026(b)(1)(C)(i) | 2440 | (i) No waiver or demonstration program shall be approved und | encoded | a limb of s 2026(b)(1)(C): see the rows above (s 2026(b)(1)(C) the waiver or demonstration program may be approved) |
| s 2026(b)(1)(C)(i)(I) | 2441 | (I) any household whose food assistance is issued in a form  | encoded | a limb of s 2026(b)(1)(C): see the rows above (s 2026(b)(1)(C) the waiver or demonstration program may be approved) |
| s 2026(b)(1)(C)(i)(II) | 2442 | (II) the State agency conducting the demonstration project p | encoded | a limb of s 2026(b)(1)(C): see the rows above (s 2026(b)(1)(C) the waiver or demonstration program may be approved) |
| s 2026(b)(1)(C)(ii) | 2443 | (ii) Clause (i) shall not apply if a waiver or demonstration | encoded | a limb of s 2026(b)(1)(C): see the rows above (s 2026(b)(1)(C) the waiver or demonstration program may be approved) |
| s 2026(b)(1)(D) | 2444 | (D) Response to waivers.— | inert1 | a heading ("Response to waivers"): its content is in the sub-units below |
| s 2026(b)(1)(D)(i) | 2445-2446 | (i) Response.— | encoded | `s 2026(b)(1)(D)(i) the Secretary's duty to respond to a request for a waiver`, `s 2026(b)(1)(D)(i) the response is one the Secretary shall provide` (responses (I) to (IV)), `s 2026(b)(1)(D)(i) the Secretary responded in time` |
| s 2026(b)(1)(D)(i)(I) | 2447 | (I) approves the waiver request; | encoded | a limb of s 2026(b)(1)(D)(i): see the rows above (s 2026(b)(1)(D)(i) the Secretary's duty to respond to a request for a waiver) |
| s 2026(b)(1)(D)(i)(II) | 2448 | (II) denies the waiver request and describes any modificatio | encoded | a limb of s 2026(b)(1)(D)(i): see the rows above (s 2026(b)(1)(D)(i) the Secretary's duty to respond to a request for a waiver) |
| s 2026(b)(1)(D)(i)(III) | 2449 | (III) denies the waiver request and describes the grounds fo | encoded | a limb of s 2026(b)(1)(D)(i): see the rows above (s 2026(b)(1)(D)(i) the Secretary's duty to respond to a request for a waiver) |
| s 2026(b)(1)(D)(i)(IV) | 2450 | (IV) requests clarification of the waiver request. | encoded | a limb of s 2026(b)(1)(D)(i): see the rows above (s 2026(b)(1)(D)(i) the Secretary's duty to respond to a request for a waiver) |
| s 2026(b)(1)(D)(ii) | 2451-2452 | (ii) Failure to respond.— | encoded | `s 2026(b)(1)(D)(ii) the waiver is considered approved` |
| s 2026(b)(1)(D)(iii) | 2453-2454 | (iii) Notice of denial.— | encoded | `s 2026(b)(1)(D)(iii) the Secretary's duty to give the Committees a copy of the denied request` and `s 2026(b)(1)(D)(iii) the Secretary has given both Committees the copy and the reasons` |
| s 2026(b)(2) | 2455 | (2) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(b)(2)(A) | 2456 | (A) The Secretary may conduct demonstration projects to test | encoded | `s 2026(b)(2)(A) the Secretary's permission to conduct demonstration projects on employment and training` |
| s 2026(b)(2)(B) | 2457 | (B) Notwithstanding paragraph (1), the Secretary may, as par | encoded | `s 2026(b)(2)(B) the Secretary may waive requirements under section 2015(d)` and `s 2026(b)(2)(B) the work experience program is conducted as the text requires` |
| s 2026(b)(2)(C) | 2458 | (C) A State seeking such a waiver shall provide assurances t | encoded | `s 2026(b)(2)(C) the State has provided the assurances` and `s 2026(b)(2)(C) what the reference in the sections named is deemed to be` |
| s 2026(b)(2)(D) | 2459 | (D) Notwithstanding the other provisions of this paragraph,  | encoded | `s 2026(b)(2)(D) the participant may take part in the activity` |
| s 2026(b)(2)(E) | 2460 | (E) For the purposes of any project conducted under this par | encoded | `s 2026(b)(2)(E) the provisions affecting the rights of recipients may be waived` |
| s 2026(b)(2)(F) | 2461 | (F) At least 60 days prior to granting final approval of a p | encoded | `s 2026(b)(2)(F) the Secretary's duty to publish the terms and notify the Committees` and `s 2026(b)(2)(F) the Secretary published and notified at least 60 days before final approval` |
| s 2026(b)(2)(G) | 2462 | (G) Waivers may be granted under this paragraph to conduct p | encoded | `s 2026(b)(2)(G) waivers may be granted for the number of project areas` |
| s 2026(b)(2)(H) | 2463 | (H) A waiver for a change in program rules may be granted un | encoded | `s 2026(b)(2)(H) a waiver for a change in program rules may be granted` |
| s 2026(b)(2)(I) | 2464 | (I) The Secretary may not grant a waiver under this paragrap | encoded | `s 2026(b)(2)(I) the Secretary may grant a waiver under paragraph (2)` and `s 2026(b)(2)(I) the day as of which a reference to a provision of title IV of the Social Security Act is read` |
| s 2026(c) | 2465-2466 | (c) Evaluation measures; pilot programs for nutritional moni | fork:FR-26-2 | `s 2026(c) the Secretary's duty to develop and implement measures for evaluating the program`, `s 2026(c) the evaluations are made often enough`, `s 2026(c) the measures shall cover the impact`, `s 2026(c) the Secretary's duty to implement pilot programs to measure nutritional status`, `s 2026(c) the locations of the pilot programs are selected as the text requires`, `s 2026(c) the Secretary's duty to report on the progress of the pilot programs`, `s 2026(c) the date by which the progress report for the year is due`, `s 2026(c) the Secretary submitted the progress report for the year in time` |
| s 2026(d) | 2467 | (d) Employment initiatives program | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(d)(1) | 2468 | (1) Election to participate | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(d)(1)(A) | 2469-2470 | (A) In general | encoded | `s 2026(d)(1)(A) the State may elect to carry out an employment initiatives program` |
| s 2026(d)(1)(B) | 2471-2472 | (B) Requirement | encoded | `s 2026(d)(1)(B) the State is eligible to carry out an employment initiatives program` |
| s 2026(d)(2) | 2473 | (2) Procedure | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(d)(2)(A) | 2474-2475 | (A) In general | encoded | `s 2026(d)(2)(A) the State may use amounts equal to the allotments to provide cash benefits to the household` |
| s 2026(d)(2)(B) | 2476-2477 | (B) Payment | encoded | `s 2026(d)(2)(B) the Secretary's duty to pay the State the value of the allotments` and `s 2026(d)(2)(B) the amount the Secretary shall pay the State, in dollars` |
| s 2026(d)(2)(C) | 2478-2479 | (C) Other provisions | encoded | `s 2026(d)(2)(C)(i) the cash assistance is considered to be an allotment` and `s 2026(d)(2)(C)(ii) the household may receive the other supplemental nutrition assistance program benefits` (lead-in) |
| s 2026(d)(2)(C)(i) | 2480 | (i) cash assistance under this subsection shall be considere | encoded | `s 2026(d)(2)(C)(i) the cash assistance is considered to be an allotment` |
| s 2026(d)(2)(C)(ii) | 2481 | (ii) each household receiving cash benefits under this subse | encoded | `s 2026(d)(2)(C)(ii) the household may receive the other supplemental nutrition assistance program benefits` |
| s 2026(d)(2)(D) | 2482-2483 | (D) Additional payments | fork:FR-26-1 | `s 2026(d)(2)(D)(i) the State shall increase the cash benefits for the sales tax` and `s 2026(d)(2)(D)(ii) the State agency's duty to pay the cost of the increase` (lead-in) |
| s 2026(d)(2)(D)(i) | 2484 | (i) increase the cash benefits provided to each household pa | fork:FR-26-1 | `s 2026(d)(2)(D)(i) the State shall increase the cash benefits for the sales tax` |
| s 2026(d)(2)(D)(ii) | 2485 | (ii) pay the cost of any increase in cash benefits required  | fork:FR-26-1 | `s 2026(d)(2)(D)(ii) the State agency's duty to pay the cost of the increase` |
| s 2026(d)(3) | 2486-2487 | (3) Eligibility | encoded | `s 2026(d)(3) the household is eligible to receive cash benefits` (lead-in) and `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` |
| s 2026(d)(3)(A) | 2488 | (A) has worked in unsubsidized employment for not less than  | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (field: the days worked) |
| s 2026(d)(3)(B) | 2489 | (B) has earned not less than $350 per month from the employm | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (field: the least monthly earnings) |
| s 2026(d)(3)(C) | 2490 | (C) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(d)(3)(C)(i) | 2491 | (i) is receiving benefits under a State program funded under | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (field: receiving part A benefits) |
| s 2026(d)(3)(C)(ii) | 2492 | (ii) was receiving benefits under a State program funded und | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (fields: was receiving, no longer eligible) |
| s 2026(d)(3)(D) | 2493 | (D) is continuing to earn not less than $350 per month from  | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (field: continuing monthly earnings) |
| s 2026(d)(3)(E) | 2494 | (E) elects to receive cash benefits in lieu of supplemental  | encoded | `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` (field: elects cash benefits) |
| s 2026(d)(4) | 2495-2496 | (4) Evaluation | fork:FR-26-1 | `s 2026(d)(4) the State agency's duty to provide a written evaluation of the impact of cash assistance` and `s 2026(d)(4) the State has provided the evaluation the text requires` |
| s 2026(e) | 2497-2498 | (e) Study and report to Congressional committees of effect o | encoded | `s 2026(e) the Secretary's duty to conduct a study of the effects of the reductions in benefits`, `s 2026(e) the Secretary submitted the interim report in time`, `s 2026(e) the Secretary submitted the final report in time`, `s 2026(e) the study includes what the text requires` |
| s 2026(f) | 2499-2500 | (f) Demonstration projects for development and use of intell | encoded | `s 2026(f) the Secretary's permission to conduct a pilot project on intelligent benefit cards`, `s 2026(f) the Secretary may conduct the pilot project`, `s 2026(f) the card and the system are as the text requires` |
| s 2026(g) | 2501-2502 | (g) Study of effectiveness of employment and training progra | encoded | `s 2026(g) the Secretary's permission to carry out studies of employment and training programs` and `s 2026(g) the results are considered in developing the performance standards` |
| s 2026(g)(1) | 2503 | (1) collect such data for up to 3 years after the individual | encoded | `s 2026(g)(1) the data collected are within the period` |
| s 2026(g)(2) | 2504-2505 | (2) yield results that can be generalized to the national pr | encoded | `s 2026(g)(2) the studies yield results that can be generalized` (lead-in and the last sentence, `s 2026(g) the results are considered in developing the performance standards`) |
| s 2026(h) | 2506-2507 | (h) Demonstration projects for vehicle exclusion limits | encoded | `s 2026(h) the Secretary's duty to conduct demonstration projects on vehicle exclusion limits`, `s 2026(h) the demonstration projects evaluate the effects in both rural and urban areas`, `s 2026(h) the value of the vehicle over $4,500, in dollars`, `s 2026(h) the value of the vehicles counted as financial resources, in dollars` |
| s 2026(h)(1) | 2508 | (1) any licensed vehicle that is used to produce earned inco | encoded | `s 2026(h)(1) the value of the vehicle is excluded` and its complement `s 2026(h)(1) the value of the vehicle is not excluded` |
| s 2026(h)(2) | 2509 | (2) one licensed vehicle used to obtain, continue, or seek e | fork:FR-26-3 | `s 2026(h)(2) the vehicle is one of those from which one may be excluded` (and which one, in `s 2026(h) the value of the vehicles counted as financial resources, in dollars`) |
| s 2026(i) | 2510-2511 | (i) Testing resource accumulation | encoded | `s 2026(i) the Secretary's duty to conduct projects to test resource accumulation`, `s 2026(i) the projects are within the limits`, `s 2026(i) the resources excluded from consideration as a resource, in dollars`, `s 2026(i) the purpose is one the projects test` |
| s 2026(j) | 2512-2513 | (j) Demonstration projects directed at benefit trafficking | encoded | `s 2026(j) the Secretary's duty to use funds for demonstration projects directed at benefit trafficking` and `s 2026(j) the funds used are within the limit` |
| s 2026(k) | 2514 | (k) Pilot projects to evaluate health and nutrition promotio | inert1 | a heading ("Pilot projects to evaluate health and nutrition promotion ..."): its content is in the sub-units below |
| s 2026(k)(1) | 2515-2516 | (1) In general | encoded | `s 2026(k)(1) the Secretary's duty to carry out pilot projects on health and nutrition promotion` and `s 2026(k)(1) the pilot projects develop and test the methods the text requires` |
| s 2026(k)(1)(A) | 2517 | (A) of using the supplemental nutrition assistance program t | encoded | `s 2026(k)(1) the pilot projects develop and test the methods the text requires` (first input) |
| s 2026(k)(1)(B) | 2518 | (B) to reduce overweight, obesity (including childhood obesi | encoded | `s 2026(k)(1) the pilot projects develop and test the methods the text requires` (second input) |
| s 2026(k)(2) | 2519 | (2) Grants | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(k)(2)(A) | 2520-2521 | (A) In general | encoded | `s 2026(k)(2)(A) the Secretary's permission to enter into contracts or cooperative agreements or provide grants` |
| s 2026(k)(2)(B) | 2522-2523 | (B) Application | encoded | `s 2026(k)(2)(B) the organization is eligible to receive a contract, cooperative agreement, or grant` |
| s 2026(k)(2)(C) | 2524-2525 | (C) Selection criteria | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` and `s 2026(k)(2)(C) the pilot projects are evaluated against publicly disseminated criteria` (lead-in) |
| s 2026(k)(2)(C)(i) | 2526 | (i) identification of a low-income target audience that corr | encoded | `s 2026(k)(2)(C)(i) the individual is in the low-income target audience` (and constructor `s 2026 identification of a low-income target audience at or below 185 percent of the poverty level`) |
| s 2026(k)(2)(C)(ii) | 2527 | (ii) incorporation of a scientifically based strategy that i | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` (a constructor of `s 2026 selection criterion`) |
| s 2026(k)(2)(C)(iii) | 2528 | (iii) a commitment to a pilot project that allows for a rigo | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` (a constructor of `s 2026 selection criterion`) |
| s 2026(k)(2)(C)(iv) | 2529 | (iv) strategies to improve the nutritional value of food ser | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` (a constructor of `s 2026 selection criterion`) |
| s 2026(k)(2)(C)(v) | 2530 | (v) innovative ways to provide significant improvement to th | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` (a constructor of `s 2026 selection criterion`) |
| s 2026(k)(2)(C)(vi) | 2531 | (vi) other criteria, as determined by the Secretary. | encoded | `s 2026(k)(2)(C) the criterion is one the pilot projects may be evaluated against` (a constructor of `s 2026 selection criterion`) |
| s 2026(k)(2)(D) | 2532-2533 | (D) Use of funds | encoded | `s 2026(k)(2)(D) the funds may be used for the project` |
| s 2026(k)(3) | 2534-2535 | (3) Projects | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (lead-in) |
| s 2026(k)(3)(A) | 2536 | (A) increase the supplemental nutrition assistance purchasin | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(3)(B) | 2537 | (B) increase access to farmers [Footnote: 2 So in original.  | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(3)(C) | 2538 | (C) provide incentives to authorized supplemental nutrition  | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(3)(D) | 2539 | (D) subject authorized supplemental nutrition assistance pro | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(3)(E) | 2540 | (E) provide incentives at the point of purchase to encourage | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(3)(F) | 2541 | (F) provide to participating households integrated communica | encoded | `s 2026(k)(3) the pilot projects may include projects of this kind` (a constructor of `s 2026 kind of pilot project`) |
| s 2026(k)(4) | 2542 | (4) Evaluation and reporting | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(k)(4)(A) | 2543 | (A) Evaluation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(k)(4)(A)(i) | 2544 | (i) Independent evaluation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(k)(4)(A)(i)(I) | 2545-2546 | (I) In general | encoded | `s 2026(k)(4)(A)(i)(I) the Secretary's duty to provide for an independent evaluation` |
| s 2026(k)(4)(A)(i)(II) | 2547-2548 | (II) Requirement | encoded | `s 2026(k)(4)(A)(i)(II) the independent evaluation uses the methodologies the text requires` |
| s 2026(k)(4)(A)(ii) | 2549-2550 | (ii) Costs | encoded | `s 2026(k)(4)(A)(ii) the Secretary's permission to pay the costs of monitoring and evaluating a pilot project` |
| s 2026(k)(4)(B) | 2551-2552 | (B) Reporting | fork:FR-26-4 | `s 2026(k)(4)(B) the Secretary's duty to submit the report on the pilot projects`, `s 2026(k)(4)(B) the date by which the report for the fiscal year is due` (lead-in) |
| s 2026(k)(4)(B)(i) | 2553 | (i) the status of each pilot project; | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(B)(ii) | 2554 | (ii) the results of the evaluation completed during the prev | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(B)(iii) | 2555 | (iii) to the maximum extent practicable— | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(B)(iii)(I) | 2556 | (I) the impact of the pilot project on appropriate health, n | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(B)(iii)(II) | 2557 | (II) baseline information relevant to the stated goals and d | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(B)(iii)(III) | 2558 | (III) equivalent information about similar or identical meas | encoded | `s 2026(k)(4)(B) the report includes what the text requires` (a field of `s 2026 pilot project report`) |
| s 2026(k)(4)(C) | 2559-2560 | (C) Public dissemination | encoded | `s 2026(k)(4)(C) the Secretary's duty to share the evaluation results broadly` |
| s 2026(k)(5) | 2561 | (5) Funding | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(k)(5)(A) | 2562-2563 | (A) Authorization of appropriations | encoded | `s 2026(k)(5)(A) sums are authorized to be appropriated for the fiscal year` |
| s 2026(k)(5)(B) | 2564-2565 | (B) Mandatory funding | encoded | `s 2026(k)(5)(B) the Secretary's duty to make available the mandatory funding` and `s 2026(k)(5)(B) the amount the Secretary shall make available on the day, in dollars` |
| s 2026(l) | 2566-2567 | (l) Cooperation with program research and evaluation | fork:FR-26-1 | `s 2026(l) the participant shall cooperate and submit information` and `s 2026(l) the participant shall submit the information` (lead-in) |
| s 2026(l)(1) | 2568 | (1) cooperate with officials and contractors acting on behal | fork:FR-26-1 | `s 2026(l)(1) the State agency's duty to cooperate with the Secretary's officials and contractors` |
| s 2026(l)(2) | 2569 | (2) submit information at such time and in such manner as th | fork:FR-26-1 | `s 2026(l)(2) the State agency's duty to submit information` |
| s 2026(m) | 2570 | (m) Evaluation of child support enforcement cooperation requ | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(m)(1) | 2571-2572 | (1) In general | encoded | `s 2026(m)(1) the Secretary's duty to conduct an independent evaluation of the child support cooperation requirements` and `s 2026(m)(1) the evaluation is as the text requires` |
| s 2026(m)(1)(A) | 2573 | (A) to assess the implementation and impact of the eligibili | encoded | `s 2026(m)(1) the evaluation is as the text requires` (a field of `s 2026 evaluation of child support cooperation`) |
| s 2026(m)(1)(B) | 2574 | (B) to assess the factors that contributed to the decision o | encoded | `s 2026(m)(1) the evaluation is as the text requires` (a field of `s 2026 evaluation of child support cooperation`) |
| s 2026(m)(1)(C) | 2575 | (C) to review alternatives to the eligibility requirements d | encoded | `s 2026(m)(1) the evaluation is as the text requires` (a field of `s 2026 evaluation of child support cooperation`) |
| s 2026(m)(1)(D) | 2576 | (D) to evaluate the costs and benefits to households and to  | encoded | `s 2026(m)(1) the evaluation is as the text requires` (a field of `s 2026 evaluation of child support cooperation`) |
| s 2026(m)(2) | 2577-2578 | (2) Evaluation | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (lead-in) |
| s 2026(m)(2)(A) | 2579 | (A) the manner in which applicable State agencies implement  | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(A)(i) | 2580 | (i) the procedures used by each State to determine cooperati | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(A)(ii) | 2581 | (ii) the manner in which each State aligns the procedures fo | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(B) | 2582 | (B) the Federal, State, and local costs associated with impl | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(C) | 2583 | (C) the effect of those eligibility requirements on the esta | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(D) | 2584 | (D) with respect to the eligibility requirements under each  | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(D)(i) | 2585 | (i) the number of individuals subject to those requirements; | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(D)(ii) | 2586 | (ii) the number of individuals in each State who meet those  | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(D)(iii) | 2587 | (iii) the number of individuals in each State who fail to me | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(E) | 2588 | (E) the number of individuals in each State for whom good ca | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(F) | 2589 | (F) the impact of those eligibility requirements on the supp | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(F)(i) | 2590 | (i) individuals subject to those requirements; | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(F)(ii) | 2591 | (ii) the household members of those individuals, including c | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(2)(F)(iii) | 2592 | (iii) households with nontraditional family structures, incl | encoded | `s 2026(m)(2) the evaluation includes the assessment the text requires` (a field of `s 2026 assessment`) |
| s 2026(m)(3) | 2593-2594 | (3) State agency cooperation | encoded | `s 2026(m)(3) the State agency's duty to provide information for the evaluation` |
| s 2026(m)(4) | 2595-2596 | (4) Report | encoded | `s 2026(m)(4) the Secretary's duty to report on the evaluation`, `s 2026(m)(4) the date by which the report is due`, `s 2026(m)(4) the Secretary submitted the report in time` |
| s 2026(n) | 2597 | (n) Longitudinal data for research | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(n)(1) | 2598-2599 | (1) In general | encoded | `s 2026(n)(1) the State agency's permission to establish a longitudinal database` and `s 2026(n)(1) the State agency may establish a longitudinal database` |
| s 2026(n)(2) | 2600-2601 | (2) Purpose | encoded | `s 2026(n)(2) the database may be used this way` |
| s 2026(n)(3) | 2602-2603 | (3) Requirements for databases | encoded | `s 2026(n)(3) the Secretary's duty to complete the preparations before approving longitudinal databases` and `s 2026(n)(3) the Secretary has completed the preparations the text requires` (lead-in) |
| s 2026(n)(3)(A) | 2604 | (A) identify features that shall be standard across States s | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(B) | 2605 | (B) identify features of longitudinal databases established  | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(C) | 2606 | (C) identify a procedure for States operating longitudinal d | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(D) | 2607 | (D) establish the manner in which data security and privacy  | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(E) | 2608 | (E) provide direction to State agencies on the responsibilit | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(F) | 2609 | (F) provide a description of the documentation that States s | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(G) | 2610 | (G) consult with other Federal research agencies, including  | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(H) | 2611 | (H) consult with States that have already established databa | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(3)(I) | 2612 | (I) identify any other requirements determined appropriate b | encoded | `s 2026(n)(3) the Secretary has completed the preparations the text requires` (a field of `s 2026 preparations`) |
| s 2026(n)(4) | 2613 | (4) Included data | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(n)(4)(A) | 2614-2615 | (A) In general | encoded | `s 2026(n)(4)(A) the database includes the data` (lead-in) |
| s 2026(n)(4)(A)(i) | 2616 | (i) shall include monthly information about households and m | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(i)(I) | 2617 | (I) demographic characteristics; | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(i)(II) | 2618 | (II) income and financial resources (as described in section | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(i)(III) | 2619 | (III) employment status; | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(i)(IV) | 2620 | (IV) household circumstances, such as deductible expenses; a | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(i)(V) | 2621 | (V) the amount of the monthly allotment received under the s | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(ii) | 2622 | (ii) may include information from other State data sources s | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(ii)(I) | 2623 | (I) earnings and employment data from the State department o | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(ii)(II) | 2624 | (II) health insurance program data; or | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(A)(ii)(III) | 2625 | (III) data from participation in other programs administered | encoded | `s 2026(n)(4)(A) the database includes the data` (a constructor of `s 2026 kind of data`, or the lead-in of clause (i) or (ii)) |
| s 2026(n)(4)(B) | 2626-2627 | (B) Data protection | fork:FR-26-1 | `s 2026(n)(4)(B)(i) the State agency's duty to protect the privacy of household members` and `s 2026(n)(4)(B)(ii) the State agency's duty to make the data available` (lead-in) |
| s 2026(n)(4)(B)(i) | 2628 | (i) protect the privacy of information about each member of  | fork:FR-26-1 | `s 2026(n)(4)(B)(i) the State agency's duty to protect the privacy of household members` and `s 2026(n)(4)(B)(i) the database protects the privacy of household members` |
| s 2026(n)(4)(B)(ii) | 2629 | (ii) make the data under this paragraph available to researc | fork:FR-26-1 | `s 2026(n)(4)(B)(ii) the State agency's duty to make the data available` and `s 2026(n)(4)(B)(ii) the State has made the data available` |
| s 2026(n)(5) | 2630-2631 | (5) Approval | encoded | `s 2026(n)(5) the Secretary's duty to approve the establishment of longitudinal databases` and `s 2026(n)(5) the Secretary shall approve the establishment in the State` (lead-in) |
| s 2026(n)(5)(A) | 2632 | (A) meet the requirements for databases under paragraph (3)  | encoded | `s 2026(n)(5) the Secretary shall approve the establishment in the State` (limbs (A) to (C)) |
| s 2026(n)(5)(B) | 2633 | (B) reflect a range of participant numbers, demographics, op | encoded | `s 2026(n)(5) the Secretary shall approve the establishment in the State` (limbs (A) to (C)) |
| s 2026(n)(5)(C) | 2634 | (C) have the capacity to provide on a periodic and ongoing b | encoded | `s 2026(n)(5) the Secretary shall approve the establishment in the State` (limbs (A) to (C)) |
| s 2026(n)(6) | 2635 | (6) Grants | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(n)(6)(A) | 2636-2637 | (A) In general | encoded | `s 2026(n)(6)(A) the Secretary's permission to provide grants to approved States` and `s 2026(n)(6)(A) the Secretary may provide a grant to the State` |
| s 2026(n)(6)(B) | 2638-2639 | (B) Method of awarding grants | encoded | `s 2026(n)(6)(B) the amount of the grant, in dollars` |
| s 2026(n)(7) | 2640 | (7) Report | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2026(n)(7)(A) | 2641-2642 | (A) In general | encoded | `s 2026(n)(7)(A) the Secretary's duty to report on the feasibility of expanding longitudinal databases` and `s 2026(n)(7)(A) the date by which the report is due` |
| s 2026(n)(7)(B) | 2643-2644 | (B) Contents | encoded | `s 2026(n)(7)(B) the report describes what the text requires` (lead-in) |
| s 2026(n)(7)(B)(i) | 2645 | (i) the cost of expanding implementation of longitudinal dat | encoded | `s 2026(n)(7)(B) the report describes what the text requires` (an input, limbs (i) to (iii)) |
| s 2026(n)(7)(B)(ii) | 2646 | (ii) the challenges and benefits of using State longitudinal | encoded | `s 2026(n)(7)(B) the report describes what the text requires` (an input, limbs (i) to (iii)) |
| s 2026(n)(7)(B)(iii) | 2647 | (iii) alternatives to expanding implementation of longitudin | encoded | `s 2026(n)(7)(B) the report describes what the text requires` (an input, limbs (i) to (iii)) |
| s 2026(n)(8) | 2648-2649 | (8) Effect | encoded | `s 2026(n)(8) this subsection prevents or limits the State agency from operating the database` |
| s 2026(n)(9) | 2650-2651 | (9) Funding | encoded | `s 2026(n)(9) the Secretary's duty to use funds to carry out the longitudinal database subsection` and `s 2026(n)(9) the amount the Secretary shall use for the fiscal year, in dollars` |
| s 2026(n)(9)(A) | 2652 | (A) $20,000,000 for fiscal year 2019 to remain available thr | encoded | `s 2026(n)(9) the amount the Secretary shall use for the fiscal year, in dollars` (fiscal year 2019) and `s 2026(n)(9)(A) the fiscal year 2019 funds remain available in the fiscal year` |
| s 2026(n)(9)(B) | 2653 | (B) $5,000,000 for fiscal year 2022 and each fiscal year the | encoded | `s 2026(n)(9) the amount the Secretary shall use for the fiscal year, in dollars` (fiscal year 2022 on) |
| s 2026 source credit | 2654 | Source credit | inert1 | the source credit: amendment history, not operative |
| s 2031 | 2842 | Minnesota Family Investment Project | inert1 | the section heading (title) |
| s 2031(a) | 2843 | (a) In general | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(a)(1) | 2844 | (1) Subject to paragraph (2), upon written application of th | encoded | `s 2031(a)(1) the State may implement the Project` |
| s 2031(a)(2) | 2845 | (2) The Project may be implemented only in accordance with t | encoded | `s 2031(a)(2) the Project may be implemented` |
| s 2031(b) | 2846-2847 | (b) Required terms and conditions of Project | fork:FR-31-2 | `s 2031(b) the application complies with the requirements specified in subsection (b)` |
| s 2031(b)(1) | 2848 | (1) Only families may be eligible to receive assistance and  | encoded | `s 2031(b)(1) the group may be eligible to receive assistance and services through the Project` |
| s 2031(b)(2) | 2849 | (2) Participating families, families eligible for or partici | encoded | `s 2031(b)(2) the family may receive benefits under the supplemental nutrition assistance program` |
| s 2031(b)(3) | 2850 | (3) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(3)(A) | 2851 | (A) Subject to the provisions of this paragraph and any redu | encoded | `s 2031(b)(3)(A) the value of the assistance is enough` |
| s 2031(b)(3)(B) | 2852 | (B) For purposes of satisfying the requirement specified in  | encoded | `s 2031(b)(3)(B) the value of assistance provided, counting child care as the text counts it, in dollars` (lead-in; clauses (i) to (iii)) |
| s 2031(b)(3)(B)(i) | 2853 | (i) payments for child care expenses under the Project shall | encoded | `s 2031(b)(3)(B) the value of assistance provided, counting child care as the text counts it, in dollars` (families with earnings) |
| s 2031(b)(3)(B)(ii) | 2854 | (ii) payments for child care expenses for families without e | encoded | `s 2031(b)(3)(B) the value of assistance provided, counting child care as the text counts it, in dollars` (families without earnings) |
| s 2031(b)(3)(B)(iii) | 2855 | (iii) any child support payments not assigned to the State u | encoded | `s 2031(b)(3)(B)(iii) the child support counted in the aggregate value for a month, in dollars` |
| s 2031(b)(3)(C) | 2856 | (C) For purposes of satisfying the requirement specified in  | encoded | `s 2031(b)(3)(C) the State shall make the determination for the family` (lead-in and the last sentence; clauses (i) to (iv)) |
| s 2031(b)(3)(C)(i) | 2857 | (i) identify the sets of characteristics indicative of famil | encoded | `s 2031(b)(3)(C)(i) the State has identified the sets of characteristics` |
| s 2031(b)(3)(C)(ii) | 2858 | (ii) establish a mechanism to determine, for each participat | encoded | `s 2031(b)(3)(C) the State shall make the determination for the family` |
| s 2031(b)(3)(C)(iii) | 2859 | (iii) increase the amount of assistance provided under the P | encoded | `s 2031(b)(3)(C)(iii) the increase the State shall make in the assistance, in dollars` |
| s 2031(b)(3)(C)(iv) | 2860-2861 | (iv) increase the amount of assistance paid to participating | encoded | `s 2031(b)(3)(C)(iv) the State shall increase the amount of assistance paid to participating families for the sales tax`, `s 2031(b)(3)(C)(iv) the increase for the sales tax, in dollars` |
| s 2031(b)(3)(D) | 2862 | (D) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(3)(D)(i) | 2863 | (i) The State shall designate standardized amounts of assist | encoded | `s 2031(b)(3)(D)(i) the State has designated the amounts and notified the family` |
| s 2031(b)(3)(D)(ii) | 2864 | (ii) The amount of food assistance so designated shall be at | encoded | `s 2031(b)(3)(D)(ii) the designated food assistance is enough` |
| s 2031(b)(3)(D)(iii) | 2865 | (iii) The State shall periodically allow participating famil | encoded | `s 2031(b)(3)(D)(iii) the State has allowed the family the option` |
| s 2031(b)(3)(E) | 2866 | (E) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(3)(E)(i) | 2867 | (i) Individuals ineligible for the Project who are members o | encoded | `s 2031(b)(3)(E)(i) the individual's eligibility and benefits follow the standards of the supplemental nutrition assistance program` |
| s 2031(b)(3)(E)(ii) | 2868 | (ii) The State agency shall determine such individuals’ elig | encoded | `s 2031(b)(3)(E)(ii) the State agency determined the individual's eligibility and benefits without regard to the participating family` |
| s 2031(b)(3)(E)(iii) | 2869 | (iii) In computing such individuals’ income for purposes of  | encoded | `s 2031(b)(3)(E)(iii) the State agency applied the maximum excess shelter expense deduction` |
| s 2031(b)(3)(E)(iv) | 2870 | (iv) Such individuals’ monthly allotment shall be the higher | fork:FR-31-1 | `s 2031(b)(3)(E)(iv) the individual's monthly allotment, in dollars`, `s 2031(b)(3)(E)(iv) the individual's monthly allotment, rounding after taking the higher, in dollars` |
| s 2031(b)(4) | 2871 | (4) The Project shall include education, employment, and tra | encoded | `s 2031(b)(4) the Project includes the education, employment, and training services it shall include` |
| s 2031(b)(5) | 2872 | (5) The State may select families for participation in the P | encoded | `s 2031(b)(5) the State may select a family this way` |
| s 2031(b)(6) | 2873 | (6) Whenever selection for participation in the Project is a | encoded | `s 2031(b)(6) selection is accomplished through submission and approval of an application` (lead-in of (A) to (G)) |
| s 2031(b)(6)(A) | 2874 | (A) the State shall promptly determine eligibility for the P | fork:FR-31-5 | `s 2031(b)(6)(A) the State agency's duty to determine eligibility and issue assistance`, `s 2031(b)(6)(A) the State agency determined eligibility and issued assistance in time`, `s 2031(b)(6)(A) the date to which the assistance to an eligible family is retroactive` |
| s 2031(b)(6)(B) | 2875 | (B) in the case of families determined ineligible for the Pr | encoded | `s 2031(b)(6)(B) the application is deemed an application for the supplemental nutrition assistance program`, `s 2031(b)(6)(B) benefits under the supplemental nutrition assistance program shall be issued to the family` |
| s 2031(b)(6)(C) | 2876 | (C) expedited benefits shall be provided under terms no more | encoded | `s 2031(b)(6)(C) expedited benefits shall be provided to the family`, `s 2031(b)(6)(C) the expedited benefits take a form the text allows` |
| s 2031(b)(6)(D) | 2877 | (D) each individual who contacts the State in person during  | fork:FR-31-5 | `s 2031(b)(6)(D) the State agency's duty to give an application form the same day`, `s 2031(b)(6)(D) the individual received the form and was permitted to file on the same day` |
| s 2031(b)(6)(E) | 2878 | (E) provision shall be made for telephone contact by, mail d | encoded | `s 2031(b)(6)(E) provision has been made for the individual as the text requires` |
| s 2031(b)(6)(F) | 2879 | (F) a family may be represented by another person if the oth | encoded | `s 2031(b)(6)(F) a family may be represented by another person` |
| s 2031(b)(6)(F)(i) | 2880 | (i) restrict the number of families who may be represented b | fork:FR-31-5 | `s 2031(b)(6)(F)(i) the State agency's permission to restrict the number of families a person may represent` |
| s 2031(b)(6)(F)(ii) | 2881 | (ii) otherwise establish criteria and verification standards | fork:FR-31-5 | `s 2031(b)(6)(F)(ii) the State agency's permission to establish criteria and verification standards for representation` |
| s 2031(b)(6)(G) | 2882 | (G) the State shall provide a method for reviewing applicati | encoded | `s 2031(b)(6)(G) the State has provided the method the text requires for the family` |
| s 2031(b)(7) | 2883 | (7) Whenever selection for participation in the Project is a | encoded | `s 2031(b)(7) selection is accomplished by assigning families that are determined eligible for or participating in the part A of title IV program or the supplemental nutrition assistance program` (lead-in of (A) and (B)) |
| s 2031(b)(7)(A) | 2884 | (A) the State shall provide eligible families assistance und | encoded | `s 2031(b)(7)(A) the assistance is provided no later than the benefits would have been` |
| s 2031(b)(7)(B) | 2885 | (B) the State shall ensure that assistance under the Project | encoded | `s 2031(b)(7)(B) the State has ensured that there is no interruption in benefits` |
| s 2031(b)(8) | 2886 | (8) Paragraphs (1)(B) and (8) of section 2020(e) of this tit | encoded | `s 2031(b)(8) paragraphs (1)(B) and (8) of section 2020(e) apply to the person` |
| s 2031(b)(9) | 2887 | (9) Assistance provided under the Project shall be reduced t | fork:FR-31-3 | `s 2031(b)(9) the assistance after the reduction, in dollars` |
| s 2031(b)(10) | 2888 | (10) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(10)(A) | 2889 | (A) The State shall provide each family or family member who | fork:FR-31-5 | `s 2031(b)(10)(A) the State agency's duty to give notice of the supplemental nutrition assistance program`, `s 2031(b)(10)(A) the State has given the notice the text requires` |
| s 2031(b)(10)(B) | 2890 | (B) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(10)(B)(i) | 2891 | (i) Following the standards specified in subparagraph (C), t | encoded | `s 2031(b)(10)(B)(i) the State shall ensure that benefits under the supplemental nutrition assistance program are provided`, `s 2031(b)(10)(B)(i) the date to which benefits issued to the eligible family are retroactive` |
| s 2031(b)(10)(B)(ii) | 2892 | (ii) If sections 256.031 through 256.036 of the Minnesota St | fork:FR-31-5 | `s 2031(b)(10)(B)(ii) the State shall exclude the applicant, family or individual from the Project`, `s 2031(b)(10)(B)(ii) the State agency's duty to continue to pay the food assistance portion`, `s 2031(b)(10)(B)(ii) the State shall continue to pay from State funds an amount equal to the food assistance portion`, `s 2031(b)(10)(B)(ii) the date to which food benefits provided to an excluded family are retroactive`, `s 2031(b)(10)(B)(ii) the Secretary's duty to pay the State the value of the benefits`, `s 2031(b)(10)(B)(ii) the amount the Secretary shall pay the State, in dollars` |
| s 2031(b)(10)(C) | 2893 | (C) Each family whose Project participation is terminated sh | fork:FR-31-7 | `s 2031(b)(10)(C) the State has screened the family as the text requires`, `s 2031(b)(10)(C) the family or family member has been given the specific request`, `s 2031(b)(10)(C) the State agency's duty to give the specific request`, `s 2031(b)(10)(C) the State agency's duty to determine eligibility after the information is supplied`, `s 2031(b)(10)(C) the State determined eligibility in time`, `s 2031(b)(10)(C) the family or family member has been notified of the determination of ineligibility` |
| s 2031(b)(11) | 2894 | (11) Section 2020(e)(10) of this title shall apply with resp | encoded | `s 2031(b)(11) section 2020(e)(10) applies to the person`, `s 2031(b)(11) the family was given notice as the text requires` |
| s 2031(b)(12) | 2895 | (12) For each fiscal year, the Secretary shall not be liable | fork:FR-31-12 | `s 2031(b)(12) the most the Secretary is liable for in the fiscal year, other than costs for evaluating the Project, in dollars`, `s 2031(b)(12) the costs related to carrying out the Project for which the Secretary is liable, in dollars` |
| s 2031(b)(13) | 2896 | (13) The State shall carry out the supplemental nutrition as | fork:FR-31-5 | `s 2031(b)(13) the State agency's duty to carry out the supplemental nutrition assistance program throughout the State`, `s 2031(b)(13) the State has carried out the supplemental nutrition assistance program as the text requires` |
| s 2031(b)(14) | 2897 | (14) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(b)(14)(A) | 2898 | (A) Except as provided in subparagraph (B), the State will c | fork:FR-31-4 | `s 2031(b)(14)(A) the last day of the five-year period`, `s 2031(b)(14)(A) the day falls in the five-year period` |
| s 2031(b)(14)(B) | 2899 | (B) The Project may be terminated— | encoded | `s 2031(b)(14)(B) the first day on which the Project may be terminated` (lead-in; clauses (i) to (iii)) |
| s 2031(b)(14)(B)(i) | 2900 | (i) by the State one hundred and eighty days after the State | encoded | `s 2031(b)(14)(B) the first day on which the Project may be terminated` (route: the State) |
| s 2031(b)(14)(B)(ii) | 2901 | (ii) by the Secretary one hundred and eighty days after the  | encoded | `s 2031(b)(14)(B) the first day on which the Project may be terminated` (route: the Secretary) |
| s 2031(b)(14)(B)(iii) | 2902 | (iii) whenever the State and the Secretary jointly agree to  | encoded | `s 2031(b)(14)(B) the first day on which the Project may be terminated` (route: joint agreement) |
| s 2031(b)(15) | 2903 | (15) Not more than six thousand families may participate in  | encoded | `s 2031(b)(15) the number of families participating simultaneously is within the limit` |
| s 2031(c) | 2904-2905 | (c) Additional terms and conditions of Project | inert1 | the heading and the lead-in "The Project shall be subject to the following additional terms and conditions:"; the rules are in (1) to (3) |
| s 2031(c)(1) | 2906 | (1) The State may require any parent in a participating fami | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (lead-in; exemptions (A) to (F)) |
| s 2031(c)(1)(A) | 2907 | (A) is ill, incapacitated, or sixty years of age or older; | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(1)(B) | 2908 | (B) is needed in the home because of the illness or incapaci | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(1)(C) | 2909 | (C) is the parent of a child under one year of age and is pe | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(1)(D) | 2910 | (D) is the parent of a child under six years of age and is e | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(1)(E) | 2911 | (E) works thirty or more hours a week or, if the number of h | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(1)(F) | 2912 | (F) is in the second or third trimester of pregnancy. | encoded | `s 2031(c)(1) the State may require the parent to participate in education, employment, or training requirements` (the exemption is a limb of the function, tested on both sides) |
| s 2031(c)(2) | 2913 | (2) The State shall not require any parent of a child under  | encoded | `s 2031(c)(2) the State may require the parent to be employed or participate for the hours` |
| s 2031(c)(3) | 2914 | (3) For any period during which an individual required to pa | encoded | `s 2031(c)(3) the most the assistance to the family may be reduced by, in dollars`, `s 2031(c)(3) the assistance to the family may be reduced by the amount` |
| s 2031(d) | 2915 | (d) Funding | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(d)(1) | 2916 | (1) If an application submitted under subsection (a) complie | encoded | `s 2031(d)(1)(A) the Secretary shall approve the application` (lead-in: "If an application ... complies ... then the Secretary shall") |
| s 2031(d)(1)(A) | 2917 | (A) approve such application; and | encoded | `s 2031(d)(1)(A) the Secretary's duty to approve the application`, `s 2031(d)(1)(A) the Secretary shall approve the application` |
| s 2031(d)(1)(B) | 2918 | (B) subject to subsection (b)(12) from the funds appropriate | encoded | `s 2031(d)(1)(B) the Secretary's duty to pay the State each calendar quarter` (lead-in; clauses (i) and (ii)) |
| s 2031(d)(1)(B)(i) | 2919 | (i) the cost of food assistance provided under the Project e | encoded | `s 2031(d)(1)(B)(i) the payment for the cost of food assistance, in dollars` |
| s 2031(d)(1)(B)(ii) | 2920 | (ii) the administrative costs incurred by the State to provi | fork:FR-31-8 | `s 2031(d)(1)(B)(ii) the payment for administrative costs, in dollars`, `s 2031(d)(1)(B)(ii) the payments under subsection (g) of section 2025 are as the proviso requires` |
| s 2031(d)(2) | 2921 | (2) The Secretary shall periodically adjust payments made to | encoded | `s 2031(d)(2) the Secretary's duty to adjust the payments made to the State` (lead-in; clauses (A) and (B)) |
| s 2031(d)(2)(A) | 2922 | (A) the cost of benefits issued to individuals ineligible fo | fork:FR-31-9 | `s 2031(d)(2)(A) the adjustment for benefits issued to individuals ineligible for the Project, in dollars` |
| s 2031(d)(2)(B) | 2923 | (B) the cost of benefits issued to families exercising the o | fork:FR-31-9 | `s 2031(d)(2)(B) the adjustment for benefits issued to families exercising the option, in dollars` |
| s 2031(d)(3) | 2924 | (3) Payments under paragraph (1)(B) shall include adjustment | encoded | `s 2031(d)(3) the payment under paragraph (1)(B) including the adjustments, in dollars` |
| s 2031(e) | 2925-2926 | (e) Waiver | encoded | `s 2031(e) the Secretary's duty to waive compliance`, `s 2031(e) the Secretary shall waive compliance with the requirement` (heading and text) |
| s 2031(f) | 2927-2928 | (f) Project audits | encoded | `s 2031(f)(1) the Comptroller General has conducted the audits the text requires` (heading and lead-in "The Comptroller General ... shall—"; the Comptroller General has no party in the core, NEEDS-CORE.md) |
| s 2031(f)(1) | 2929 | (1) conduct periodic audits of the operation of the Project  | encoded | `s 2031(f)(1) the Comptroller General has conducted the audits the text requires` |
| s 2031(f)(2) | 2930 | (2) submit to the Secretary, the Secretary of Health and Hum | encoded | `s 2031(f)(2) the Comptroller General has submitted the report of the audit to all four recipients` |
| s 2031(g) | 2931 | (g) Construction | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(g)(1) | 2932 | (1) For purposes of any Federal, State, or local law other t | encoded | `s 2031(g)(1)(A) the cash assistance is treated in the same manner as benefit allotments under the supplemental nutrition assistance program` and `s 2031(g)(1)(B) the family is treated in the same manner as a participant in the supplemental nutrition assistance program` (the lead-in "For purposes of any Federal, State, or local law other than part A of title IV ... or this chapter" is their first input) |
| s 2031(g)(1)(A) | 2933 | (A) cash assistance provided under the Project that is desig | encoded | `s 2031(g)(1)(A) the cash assistance is treated in the same manner as benefit allotments under the supplemental nutrition assistance program` |
| s 2031(g)(1)(B) | 2934 | (B) participating families shall be treated in the same mann | encoded | `s 2031(g)(1)(B) the family is treated in the same manner as a participant in the supplemental nutrition assistance program` |
| s 2031(g)(2) | 2935 | (2) Nothing in this section shall— | encoded | `s 2031(g)(2)(A) this section allows the payments made to the State` and `s 2031(g)(2)(B) this section requires the Secretary to incur the costs` (the lead-in "Nothing in this section shall—") |
| s 2031(g)(2)(A) | 2936 | (A) allow payments made to the State under the Project to be | encoded | `s 2031(g)(2)(A) this section allows the payments made to the State` |
| s 2031(g)(2)(B) | 2937 | (B) require the Secretary to incur costs as a result of the  | encoded | `s 2031(g)(2)(B) this section requires the Secretary to incur the costs` |
| s 2031(h) | 2938-2939 | (h) Quality control | fork:FR-31-10 | `s 2031(h) the family is excluded from the sample`, `s 2031(h) the total value of allotments under section 2025(c)(1), in dollars` (heading and text) |
| s 2031(i) | 2940 | (i) Evaluation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2031(i)(1) | 2941 | (1) The State shall develop and implement a plan for an inde | fork:FR-31-5 | `s 2031(i)(1) the State agency's duty to develop and implement an evaluation plan`, `s 2031(i)(1) the plan contains what the text requires`, `s 2031(i)(1) the concern is one the evaluation plan shall satisfy` |
| s 2031(i)(2) | 2942 | (2) The State shall pay 50 percent of the cost of developing | encoded | `s 2031(i)(2) the State's share of the cost of the plan, in dollars`, `s 2031(i)(2) the Federal Government's share of the cost of the plan, in dollars` |
| s 2031(j) | 2943-2944 | (j) Definitions | inert1 | the heading and the lead-in "For purposes of this section, the following definitions apply:"; the definitions are in (1) to (4) |
| s 2031(j)(1) | 2945 | (1) The term “family” means the following individuals who li | fork:FR-31-6 | `s 2031(j)(1) the group is a family` |
| s 2031(j)(2) | 2946 | (2) The term “contract” means a plan to help a family pursue | encoded | `s 2031(j)(2) the document is a contract` |
| s 2031(j)(3) | 2947 | (3) The term “caregiver” means a minor child’s natural or ad | fork:FR-31-11 | `s 2031(j)(3) the person is a caregiver` |
| s 2031(j)(4) | 2948 | (4) The term “State” means the State of Minnesota. | encoded | `s 2031(j)(4) the name is the State` |
| s 2031 source credit | 2949 | Source credit | inert1 | the source credit: amendment history, not operative |
| s 2033 | 2979 | Repealed. Pub. L. 107–171, title IV, § 4124(b), May 13, 2002 | repealed | no rule: the heading says "Repealed. Pub. L. 107–171, title IV, § 4124(b), May 13, 2002, 116 Stat. 326" and no text follows (line 2979); there is no module for it |
| s 2034 | 2981 | Assistance for community food projects | inert1 | the section heading (title) |
| s 2034(a) | 2982-2983 | (a) Definitions | inert1 | the heading and the lead-in "In this section:"; the rules are in (a)(1) to (a)(3) |
| s 2034(a)(1) | 2984-2985 | (1) Community food project | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(A) | 2986 | (A) requires a 1-time contribution of Federal assistance to  | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(B) | 2987 | (B) is designed— | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(B)(i) | 2988 | (i) | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(a)(1)(B)(i)(I) | 2989 | (I) to meet the food needs of low-income individuals through | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(B)(i)(II) | 2990 | (II) to increase the self-reliance of communities in providi | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(B)(i)(III) | 2991 | (III) to promote comprehensive responses to local food, food | encoded | `s 2034(a)(1) the project is a community food project` (defined term "community food project") |
| s 2034(a)(1)(B)(ii) | 2992 | (ii) to meet specific State, local, or neighborhood food and | encoded | `s 2034(a)(1)(B)(ii) the need is one the text lists` (the three examples; the project-level test is `s 2034(a)(1)`) |
| s 2034(a)(1)(B)(ii)(I) | 2993 | (I) equipment necessary for the efficient operation of a pro | encoded | `s 2034(a)(1)(B)(ii) the need is one the text lists` (the three examples; the project-level test is `s 2034(a)(1)`) |
| s 2034(a)(1)(B)(ii)(II) | 2994 | (II) planning for long-term solutions; or | encoded | `s 2034(a)(1)(B)(ii) the need is one the text lists` (the three examples; the project-level test is `s 2034(a)(1)`) |
| s 2034(a)(1)(B)(ii)(III) | 2995 | (III) the creation of innovative marketing activities that m | encoded | `s 2034(a)(1)(B)(ii) the need is one the text lists` (the three examples; the project-level test is `s 2034(a)(1)`) |
| s 2034(a)(2) | 2996-2997 | (2) Gleaner | encoded | `s 2034(a)(2) the entity is a gleaner` (defined term "gleaner") |
| s 2034(a)(2)(A) | 2998 | (A) collects edible, surplus food that would be thrown away  | encoded | `s 2034(a)(2) the entity is a gleaner` (defined term "gleaner") |
| s 2034(a)(2)(B) | 2999 | (B) harvests for free distribution to the needy, or for dona | encoded | `s 2034(a)(2) the entity is a gleaner` (defined term "gleaner") |
| s 2034(a)(3) | 3000-3001 | (3) Hunger-free communities goal | encoded | `s 2034(a)(3) the goal is a hunger-free communities goal` and `s 2034(a)(3) the number of hunger-free communities goals` (defined term "hunger-free communities goal") |
| s 2034(b) | 3002 | (b) Authority to provide assistance | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(b)(1) | 3003-3004 | (1) In general | fork:FR-34-1 | `s 2034(b)(1) the Secretary may make a grant to assist the entity with the project` |
| s 2034(b)(2) | 3005-3006 | (2) Limitation on grants | encoded | `s 2034(b)(2) the most that may be provided as grants in the fiscal year, in dollars` and `s 2034(b)(2) the total provided as grants is within the limit` |
| s 2034(b)(2)(A) | 3007 | (A) $1,000,000 for fiscal year 1996; | encoded | `s 2034(b)(2) the most that may be provided as grants in the fiscal year, in dollars` and `s 2034(b)(2) the total provided as grants is within the limit` |
| s 2034(b)(2)(B) | 3008 | (B) $5,000,000 for each of fiscal years 2008 through 2014; | encoded | `s 2034(b)(2) the most that may be provided as grants in the fiscal year, in dollars` and `s 2034(b)(2) the total provided as grants is within the limit` |
| s 2034(b)(2)(C) | 3009 | (C) $9,000,000 for each of fiscal years 2015 through 2018; a | encoded | `s 2034(b)(2) the most that may be provided as grants in the fiscal year, in dollars` and `s 2034(b)(2) the total provided as grants is within the limit` |
| s 2034(b)(2)(D) | 3010 | (D) $5,000,000 for fiscal year 2019 and each fiscal year the | encoded | `s 2034(b)(2) the most that may be provided as grants in the fiscal year, in dollars` and `s 2034(b)(2) the total provided as grants is within the limit` |
| s 2034(c) | 3011-3012 | (c) Eligible entities | fork:FR-34-1 | `s 2034(c) the entity is eligible for a grant under subsection (b)` |
| s 2034(c)(1) | 3013 | (1) have experience in the area of— | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(1)(A) | 3014 | (A) community food work, particularly concerning small and m | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(1)(B) | 3015 | (B) job training and business development activities for foo | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(1)(C) | 3016 | (C) efforts to reduce food insecurity in the community, incl | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(2) | 3017 | (2) demonstrate competency to implement a project, provide f | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(3) | 3018 | (3) demonstrate a willingness to share information with rese | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(c)(4) | 3019 | (4) collaborate with 1 or more local partner organizations t | encoded | `s 2034(c) the entity is eligible for a grant under subsection (b)` (limbs (1) to (4)) |
| s 2034(d) | 3020-3021 | (d) Preference for certain projects | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(1) | 3022 | (1) develop linkages between 2 or more sectors of the food s | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(2) | 3023 | (2) support the development of entrepreneurial projects; | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(3) | 3024 | (3) develop innovative linkages between the for-profit and n | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(4) | 3025 | (4) encourage long-term planning activities, and multisystem | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(5) | 3026 | (5) develop new resources and strategies to help reduce food | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(5)(A) | 3027 | (A) developing creative food resources; | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(5)(B) | 3028 | (B) coordinating food services with park and recreation prog | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(d)(5)(C) | 3029 | (C) creating nutrition education programs for at-risk popula | encoded | `s 2034(d) the Secretary shall give the project a preference` (limbs (1) to (5)) |
| s 2034(e) | 3030 | (e) Matching funds requirements | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(e)(1) | 3031-3032 | (1) Requirements | encoded | `s 2034(e)(1) the Federal share is within the limit` |
| s 2034(e)(2) | 3033-3034 | (2) Calculation | encoded | `s 2034(e)(2) the contribution counts toward the non-Federal share` |
| s 2034(e)(3) | 3035-3036 | (3) Sources | encoded | `s 2034(e)(3) the entity may provide the non-Federal share through this source` |
| s 2034(f) | 3037 | (f) Term of grant | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(f)(1) | 3038-3039 | (1) Single grant | encoded | `s 2034(f)(1) the project may be supported by a grant under subsection (b)` |
| s 2034(f)(2) | 3040-3041 | (2) Term | encoded | `s 2034(f)(2) the term of the grant is within the limit` |
| s 2034(g) | 3042 | (g) Technical assistance and related information | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(g)(1) | 3043-3044 | (1) Technical assistance | encoded | `s 2034(g)(1) the Secretary's permission to provide technical assistance` |
| s 2034(g)(2) | 3045 | (2) Sharing information | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2034(g)(2)(A) | 3046-3047 | (A) In general | encoded | `s 2034(g)(2)(A) the Secretary's permission to provide for the sharing of information` |
| s 2034(g)(2)(B) | 3048-3049 | (B) Other interested parties | encoded | `s 2034(g)(2)(B) the Secretary's permission to share information with researchers and others` |
| s 2034(h) | 3050-3051 | (h) Reports to Congress | encoded | `s 2034(h) the date by which the report for the year is due` and `s 2034(h) the Secretary submitted the report for the year in time` |
| s 2034(h)(1) | 3052 | (1) a description of any activity funded; | encoded | `s 2034(h)(1) to (3) the report describes what it shall include` |
| s 2034(h)(2) | 3053 | (2) the degree of success of each activity funded in achievi | encoded | `s 2034(h)(1) to (3) the report describes what it shall include` |
| s 2034(h)(3) | 3054 | (3) the degree of success in improving the long-term capacit | encoded | `s 2034(h)(1) to (3) the report describes what it shall include` |
| s 2034 source credit | 3055 | Source credit | inert1 | the source credit: amendment history, not operative |
| s 2035 | 3057 | Simplified supplemental nutrition assistance program | inert1 | the section heading (title) of s 2035 |
| s 2035(a) | 3058-3059 | (a) “Federal costs” defined | encoded | `s 2035(a) the cost is a Federal cost for this section` (defined term "Federal costs") |
| s 2035(b) | 3060-3061 | (b) Election | encoded | `s 2035(b) the State may elect to carry out a Program there` |
| s 2035(c) | 3062-3063 | (c) Operation of Program | encoded | `s 2035(c) the household may participate in the Program` (lead-in; calls (c)(1) to (c)(3)) |
| s 2035(c)(1) | 3064 | (1) a household in which no members receive assistance under | encoded | `s 2035(c)(1) the household may participate in the Program` |
| s 2035(c)(2) | 3065 | (2) a household in which all members receive assistance unde | encoded | `s 2035(c)(2) the household is eligible to participate in the Program` |
| s 2035(c)(3) | 3066 | (3) if approved by the Secretary, a household in which 1 or  | encoded | `s 2035(c)(3) the household may be eligible to participate in the Program` |
| s 2035(c)(4) | 3067 | (4) subject to subsection (f), benefits under the Program sh | fork:FR-35-2 | `s 2035(c)(4) benefits under the Program may be determined under rules from this source` (and the (A) to (C) sources) |
| s 2035(c)(4)(A) | 3068 | (A) a State program funded under part A of title IV of the S | fork:FR-35-2 | `s 2035(c)(4) benefits under the Program may be determined under rules from this source` (and the (A) to (C) sources) |
| s 2035(c)(4)(B) | 3069 | (B) the supplemental nutrition assistance program; or | fork:FR-35-2 | `s 2035(c)(4) benefits under the Program may be determined under rules from this source` (and the (A) to (C) sources) |
| s 2035(c)(4)(C) | 3070 | (C) a combination of a State program funded under part A of  | fork:FR-35-2 | `s 2035(c)(4) benefits under the Program may be determined under rules from this source` (and the (A) to (C) sources) |
| s 2035(d) | 3071 | (d) Approval of Program | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2035(d)(1) | 3072-3073 | (1) State plan | fork:FR-35-4 | `s 2035(d)(1) the State agency may operate a Program` |
| s 2035(d)(2) | 3074-3075 | (2) Approval of plan | encoded | `s 2035(d)(2) the Secretary shall approve the State plan` |
| s 2035(d)(2)(A) | 3076 | (A) complies with this section; and | encoded | `s 2035(d)(2) the Secretary shall approve the State plan` |
| s 2035(d)(2)(B) | 3077 | (B) contains sufficient documentation that the plan will not | encoded | `s 2035(d)(2) the Secretary shall approve the State plan` |
| s 2035(e) | 3078 | (e) Increased Federal costs | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2035(e)(1) | 3079 | (1) Determination | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2035(e)(1)(A) | 3080-3081 | (A) In general | encoded | `s 2035(e)(1)(A) the Secretary's duty to determine whether the Program is increasing Federal costs` |
| s 2035(e)(1)(B) | 3082-3083 | (B) No excluded households | encoded | `s 2035(e)(1)(B) the Secretary's prohibition on requiring information on households not in the Program` |
| s 2035(e)(1)(C) | 3084-3085 | (C) Alternative accounting periods | encoded | `s 2035(e)(1)(C) the Secretary's permission to approve alternative accounting periods` |
| s 2035(e)(2) | 3086-3087 | (2) Notification | fork:FR-35-1 | `s 2035(e)(2) the Secretary's duty to notify the State` and its twin `s 2035(e)(2) the Secretary notified the State in time` |
| s 2035(e)(3) | 3088 | (3) Enforcement | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2035(e)(3)(A) | 3089-3090 | (A) Corrective action | fork:FR-35-3 | `s 2035(e)(3)(A) the State's duty to submit a plan for prompt corrective action` and its twin `s 2035(e)(3)(A) the State submitted its plan in time` |
| s 2035(e)(3)(B) | 3091-3092 | (B) Termination | encoded | `s 2035(e)(3)(B) the Secretary's duty to terminate the approval`, `s 2035(e)(3)(B) the Secretary shall terminate the approval of the State agency`, `s 2035(e)(3)(B) the State agency may operate a future Program` |
| s 2035(f) | 3093 | (f) Rules and procedures | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2035(f)(1) | 3094-3095 | (1) In general | encoded | `s 2035(f)(1) the State may follow the rules and procedures from this source` |
| s 2035(f)(2) | 3096-3097 | (2) Standardized deductions | encoded | `s 2035(f)(2) the State may standardize the deduction` and `s 2035(f)(2) the State has considered what it shall consider` |
| s 2035(f)(3) | 3098-3099 | (3) Requirements | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(A) | 3100 | (A) subsections (a) through (f) of section 2016 of this titl | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(B) | 3101 | (B) section 2017(a) of this title (except that the income of | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(C) | 3102 | (C) subsections (b) and (d) of section 2017 of this title; | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(D) | 3103 | (D) subsections (a), (c), (d), and (n) of section 2020 of th | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(E) | 3104 | (E) paragraphs (8), (12), (15), (17), (18), (22), and (23) o | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(F) | 3105 | (F) section 2020(e)(10) of this title (or a comparable requi | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(3)(G) | 3106 | (G) section 2025 of this title. | encoded | `s 2035(f)(3) the State complies with the requirements it shall comply with` (groups (A) to (G)); (B) also `s 2035(f)(3)(B) the household's income may be determined under this source` |
| s 2035(f)(4) | 3107-3108 | (4) Limitation on eligibility | encoded | `s 2035(f)(4) the household may receive benefits under this section as a result of its eligibility under the State program` |
| s 2035 source credit | 3109 | Source credit | inert1 | the source credit: amendment history, not operative |
| s 2036 | 3111 | Availability of commodities for emergency food assistance pr | inert1 | the section heading (title) |
| s 2036(a) | 3112 | (a) Purchase of commodities | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036(a)(1) | 3113-3114 | (1) In general | fork:FR-36-1 | `s 2036(a)(1) the Secretary shall purchase commodities in the fiscal year`, `s 2036(a)(1) the commodity is one the Secretary shall purchase`, `s 2036(a)(1) the Secretary's duty to purchase commodities and distribute them to States` |
| s 2036(a)(2) | 3115-3116 | (2) Amounts | fork:FR-36-2 | `s 2036(a)(2) the amount the Secretary shall use for the fiscal year, in dollars` (lead-in; calls (A) to (E)) |
| s 2036(a)(2)(A) | 3117 | (A) for fiscal year 2008, $190,000,000; | encoded | `s 2036(a)(2)(A) the amount for fiscal year 2008, in dollars` |
| s 2036(a)(2)(B) | 3118 | (B) for fiscal year 2009, $250,000,000; | encoded | `s 2036(a)(2)(B) the amount for fiscal year 2009, in dollars` |
| s 2036(a)(2)(C) | 3119 | (C) for each of fiscal years 2010 through 2023, the dollar a | fork:FR-36-2 | `s 2036(a)(2)(C) the amount for a fiscal year from 2010 through 2023, in dollars` |
| s 2036(a)(2)(D) | 3120 | (D) for each of fiscal years 2015 through 2023, the sum obta | fork:FR-36-3 | `s 2036(a)(2)(D) the amount for a fiscal year from 2015 through 2023, in dollars` |
| s 2036(a)(2)(D)(i) | 3121 | (i) for fiscal year 2015, $50,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(ii) | 3122 | (ii) for fiscal year 2016, $40,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(iii) | 3123 | (iii) for fiscal year 2017, $20,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(iv) | 3124 | (iv) for fiscal year 2018, $15,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(v) | 3125 | (v) for fiscal year 2019, $23,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(vi) | 3126 | (vi) for fiscal year 2020, $35,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(vii) | 3127 | (vii) for fiscal year 2021, $35,000,000; | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(viii) | 3128 | (viii) for fiscal year 2022, $35,000,000; and | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(D)(ix) | 3129 | (ix) for fiscal year 2023, $35,000,000; and | encoded | `s 2036(a)(2)(D) the sum added to the (C) amount for the fiscal year, in dollars` (the sums of clauses (i) to (ix)) |
| s 2036(a)(2)(E) | 3130 | (E) for fiscal year 2024 and each subsequent fiscal year, th | fork:FR-36-2 | `s 2036(a)(2)(E) the amount for fiscal year 2024 and each subsequent fiscal year, in dollars` |
| s 2036(a)(3) | 3131-3132 | (3) Funds availability | inert1 | the lead-in "For purposes of the funds described in this subsection, the Secretary shall—" and the heading "Funds availability"; the rules are in (A) and (B) |
| s 2036(a)(3)(A) | 3133 | (A) make the funds available for 2 fiscal years; and | fork:FR-36-4 | `s 2036(a)(3)(A) the funds are available in the fiscal year`, `s 2036(a)(3)(A) the Secretary's duty to make the funds available for 2 fiscal years` |
| s 2036(a)(3)(B) | 3134 | (B) allow States to carry over unexpended balances to the ne | encoded | `s 2036(a)(3)(B) the State may carry the balance over to the next fiscal year`, `s 2036(a)(3)(B) the Secretary's duty to allow States to carry over unexpended balances` |
| s 2036(b) | 3135-3136 | (b) Basis for commodity purchases | encoded | `s 2036(b) the purchases are based as the Secretary shall base them` (lead-in and heading; limbs (1) to (3)) |
| s 2036(b)(1) | 3137 | (1) agricultural market conditions; | encoded | `s 2036(b) the purchases are based as the Secretary shall base them` (field `agricultural market conditions`) |
| s 2036(b)(2) | 3138 | (2) preferences and needs of States and distributing agencie | encoded | `s 2036(b) the purchases are based as the Secretary shall base them` (field `preferences and needs of States and distributing agencies`) |
| s 2036(b)(3) | 3139 | (3) preferences of recipients. | encoded | `s 2036(b) the purchases are based as the Secretary shall base them` (field `preferences of recipients`) |
| s 2036 source credit | 3140 | Source credit | inert1 | the source credit: amendment history, not operative |
| s 2036a | 3142 | Nutrition education and obesity prevention grant program | inert1 | the section heading (title) |
| s 2036a(a) | 3143-3144 | (a) Definition of eligible individual | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(1) | 3145 | (1) an individual eligible for benefits under— | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(1)(A) | 3146 | (A) this chapter; | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(1)(B) | 3147 | (B) sections 1758(b)(1)(A) and 1766(c)(4) of title 42; or | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(1)(C) | 3148 | (C) section 1773(e)(1)(A) of title 42; | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(2) | 3149 | (2) an individual who resides in a community with a signific | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(a)(3) | 3150 | (3) such other low-income individual as is determined to be  | encoded | `s 2036a(a) the individual is an eligible individual` (defined term "eligible individual"; limbs (1)(A) to (C), (2), (3)) |
| s 2036a(b) | 3151-3152 | (b) Programs | encoded | `s 2036a(b) the State agency may implement the program for the individual` and `s 2036a(b) the State agency's permission to implement a program` |
| s 2036a(c) | 3153 | (c) Delivery of nutrition education and obesity prevention s | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(c)(1) | 3154-3155 | (1) In general | encoded | `s 2036a(c)(1) the State agency may deliver the services this way` (limbs (A) and (B)) |
| s 2036a(c)(1)(A) | 3156 | (A) directly to eligible individuals; or | encoded | `s 2036a(c)(1) the State agency may deliver the services this way` (limbs (A) and (B)) |
| s 2036a(c)(1)(B) | 3157 | (B) through agreements with other State or local agencies or | encoded | `s 2036a(c)(1) the State agency may deliver the services this way` (limbs (A) and (B)) |
| s 2036a(c)(2) | 3158 | (2) Nutrition education State plans | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(c)(2)(A) | 3159-3160 | (A) In general | encoded | `s 2036a(c)(2)(A) the State agency's duty to submit a nutrition education State plan` and `s 2036a(c)(2)(A) the State agency has met the duty to submit a plan` |
| s 2036a(c)(2)(B) | 3161-3162 | (B) Requirements | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (lead-in) |
| s 2036a(c)(2)(B)(i) | 3163 | (i) identify the uses of the funding for local projects; | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (field `it identifies the uses of the funding for local projects`) |
| s 2036a(c)(2)(B)(ii) | 3164 | (ii) ensure that the interventions are appropriate for eligi | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (field `it ensures that the interventions are appropriate ...`) |
| s 2036a(c)(2)(B)(iii) | 3165 | (iii) describe how the State agency shall use an electronic  | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (field `it describes how the State agency shall use an electronic reporting system ...`) |
| s 2036a(c)(2)(B)(iii)(I) | 3166 | (I) measure and evaluate the projects; and | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (same field: measure and evaluate the projects) |
| s 2036a(c)(2)(B)(iii)(II) | 3167 | (II) account for the allowable State agency administrative c | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(aa) | 3168 | (aa) salaries and benefits of State agency personnel; | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(bb) | 3169 | (bb) office supplies and equipment; | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(cc) | 3170 | (cc) travel costs; | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(dd) | 3171 | (dd) development and production of nutrition education mater | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(ee) | 3172 | (ee) memberships, subscriptions, and professional activities | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(ff) | 3173 | (ff) lease or rental costs; | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(gg) | 3174 | (gg) maintenance and repair expenses; | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(hh) | 3175 | (hh) indirect costs; and | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iii)(II)(ii) | 3176 | (ii) cost of using publicly-owned building space; and | encoded | `s 2036a(c)(2)(B)(iii)(II) the cost is in a category the text lists` (categories (aa) to (ii)) |
| s 2036a(c)(2)(B)(iv) | 3177 | (iv) conform to standards established by the Secretary throu | encoded | `s 2036a(c)(2)(B) the plan contains what it shall` (field `it conforms to standards established by the Secretary`) |
| s 2036a(c)(3) | 3178 | (3) Use of funds | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(c)(3)(A) | 3179-3180 | (A) In general | encoded | `s 2036a(c)(3)(A) the State agency may use the funds for the use` |
| s 2036a(c)(3)(A)(i) | 3181 | (i) individual and group-based nutrition education, health p | encoded | `s 2036a(c)(3)(A) the use is one of the examples the text gives` (examples (i) to (iii)) |
| s 2036a(c)(3)(A)(ii) | 3182 | (ii) comprehensive, multilevel interventions at multiple com | encoded | `s 2036a(c)(3)(A) the use is one of the examples the text gives` (examples (i) to (iii)) |
| s 2036a(c)(3)(A)(iii) | 3183 | (iii) community and public health approaches to improve nutr | encoded | `s 2036a(c)(3)(A) the use is one of the examples the text gives` (examples (i) to (iii)) |
| s 2036a(c)(3)(B) | 3184-3185 | (B) Consultation | encoded | `s 2036a(c)(3)(B) the Administrator's duty to consult` (FR-36a-2: the Administrator is acted for by the Secretary) |
| s 2036a(c)(3)(B)(i) | 3186 | (i) representatives of the academic and research communities | encoded | `s 2036a(c)(3)(B) the Administrator shall consult this person or body` (the groups (i) to (iv)) |
| s 2036a(c)(3)(B)(ii) | 3187 | (ii) nutrition education practitioners; | encoded | `s 2036a(c)(3)(B) the Administrator shall consult this person or body` (the groups (i) to (iv)) |
| s 2036a(c)(3)(B)(iii) | 3188 | (iii) representatives of State and local governments; and | encoded | `s 2036a(c)(3)(B) the Administrator shall consult this person or body` (the groups (i) to (iv)) |
| s 2036a(c)(3)(B)(iv) | 3189 | (iv) community organizations that serve low-income populatio | encoded | `s 2036a(c)(3)(B) the Administrator shall consult this person or body` (the groups (i) to (iv)) |
| s 2036a(c)(4) | 3190-3191 | (4) Notification | encoded | `s 2036a(c)(4) the State agency shall notify the person of the availability of the services` and `s 2036a(c)(4) the State agency's duty to notify` |
| s 2036a(c)(5) | 3192-3193 | (5) Coordination | encoded | `s 2036a(c)(5) the projects may be coordinated with other programs and strategies` |
| s 2036a(c)(6) | 3194-3195 | (6) Information clearinghouse | encoded | `s 2036a(c)(6) the Secretary's duty to establish an online clearinghouse` |
| s 2036a(c)(7) | 3196-3197 | (7) Technical assistance | encoded | `s 2036a(c)(7) the Secretary's duty to provide technical assistance` |
| s 2036a(c)(7)(A) | 3198 | (A) by identifying common challenges faced by entities descr | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(7)(B) | 3199 | (B) by coordinating efforts to address those common challeng | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(7)(C) | 3200 | (C) by collecting and disseminating information on evidence- | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(7)(D) | 3201 | (D) by facilitating communication between and among grantees | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(7)(E) | 3202 | (E) by assisting State agencies in creating or maintaining s | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(7)(F) | 3203 | (F) by performing or assisting with other activities, as det | encoded | `s 2036a(c)(7) the help is technical assistance the text lists` (forms (A) to (F)) |
| s 2036a(c)(8) | 3204-3205 | (8) Annual State report | encoded | `s 2036a(c)(8) the State agency's duty to submit an annual report` |
| s 2036a(c)(8)(A) | 3206 | (A) the use of funds on the State agency’s program, includin | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(8)(B) | 3207 | (B) a description of each project carried out by that agency | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(8)(C) | 3208 | (C) a comprehensive analysis of the impacts and outcomes— | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(8)(C)(i) | 3209 | (i) of the project, including with respect to the elements d | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(8)(C)(ii) | 3210 | (ii) to the extent practicable, of completed multiyear proje | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(8)(D) | 3211 | (D) the status of any ongoing multiyear project. | encoded | `s 2036a(c)(8) the annual State report includes what it shall` (items (A) to (D)) |
| s 2036a(c)(9) | 3212-3213 | (9) Annual Federal report | encoded | `s 2036a(c)(9) the Administrator's duty to submit an annual report to the Committees` (FR-36a-2) |
| s 2036a(c)(9)(A) | 3214 | (A) evaluates the level of coordination between— | encoded | `s 2036a(c)(9) the annual Federal report includes what it shall` (items (A) and (B)) |
| s 2036a(c)(9)(A)(i) | 3215 | (i) the nutrition education and obesity prevention grant pro | encoded | `s 2036a(c)(9) the annual Federal report includes what it shall` (items (A) and (B)) |
| s 2036a(c)(9)(A)(ii) | 3216 | (ii) the expanded food and nutrition education program under | encoded | `s 2036a(c)(9) the annual Federal report includes what it shall` (items (A) and (B)) |
| s 2036a(c)(9)(A)(iii) | 3217 | (iii) any other nutrition education program administered by  | encoded | `s 2036a(c)(9) the annual Federal report includes what it shall` (items (A) and (B)) |
| s 2036a(c)(9)(B) | 3218 | (B) includes the use of funds on such programs including Sta | encoded | `s 2036a(c)(9) the annual Federal report includes what it shall` (items (A) and (B)) |
| s 2036a(d) | 3219 | (d) Funding | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(d)(1) | 3220-3221 | (1) In general | encoded | `s 2036a(d)(1) the Secretary's duty to reserve the funds for allocation to State agencies` and `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` |
| s 2036a(d)(1)(A) | 3222 | (A) for fiscal year 2011, $375,000,000; | encoded | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2011: $375,000,000) |
| s 2036a(d)(1)(B) | 3223 | (B) for fiscal year 2012, $388,000,000; | encoded | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2012: $388,000,000) |
| s 2036a(d)(1)(C) | 3224 | (C) for fiscal year 2013, $285,000,000; | encoded | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2013: $285,000,000) |
| s 2036a(d)(1)(D) | 3225 | (D) for fiscal year 2014, $401,000,000; | encoded | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2014: $401,000,000) |
| s 2036a(d)(1)(E) | 3226 | (E) for fiscal year 2015, $407,000,000; and | encoded | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2015: $407,000,000) |
| s 2036a(d)(1)(F) | 3227 | (F) for each of fiscal years 2016 through 2025, the applicab | fork:FR-36a-1 | `s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` (2016 to 2025, increases only) |
| s 2036a(d)(2) | 3228 | (2) Allocation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(d)(2)(A) | 3229-3230 | (A) Initial allocation | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(i) | 3231 | (i) for each of fiscal years 2011 through 2013, 100 percent  | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii) | 3232 | (ii) subject to a reallocation under subparagraph (B)— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(I) | 3233 | (I) for fiscal year 2014— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(I)(aa) | 3234 | (aa) 90 percent shall be allocated to State agencies in acco | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(I)(bb) | 3235 | (bb) 10 percent shall be allocated to State agencies based o | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(II) | 3236 | (II) for fiscal year 2015— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(II)(aa) | 3237 | (aa) 80 percent shall be allocated to State agencies in acco | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(II)(bb) | 3238 | (bb) 20 percent shall be allocated in accordance with subcla | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(III) | 3239 | (III) for fiscal year 2016— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(III)(aa) | 3240 | (aa) 70 percent shall be allocated to State agencies in acco | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(III)(bb) | 3241 | (bb) 30 percent shall be allocated in accordance with subcla | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(IV) | 3242 | (IV) for fiscal year 2017— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(IV)(aa) | 3243 | (aa) 60 percent shall be allocated to State agencies in acco | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(IV)(bb) | 3244 | (bb) 40 percent shall be allocated in accordance with subcla | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(V) | 3245 | (V) for fiscal year 2018 and each fiscal year thereafter— | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(V)(aa) | 3246 | (aa) 50 percent shall be allocated to State agencies in acco | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(A)(ii)(V)(bb) | 3247 | (bb) 50 percent shall be allocated in accordance with subcla | encoded | `s 2036a(d)(2)(A) the percent allocated in proportion to fiscal year 2009 funding`, `s 2036a(d)(2)(A) the percent allocated in proportion to participation`, `s 2036a(d)(2)(A) the State agency's allocation before any reallocation, in dollars` |
| s 2036a(d)(2)(B) | 3248 | (B) Reallocation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(d)(2)(B)(i) | 3249-3250 | (i) In general | encoded | `s 2036a(d)(2)(B)(i) the Secretary shall reallocate the unexpended funds to the other State` and `s 2036a(d)(2)(B)(i) the Secretary's duty to reallocate` |
| s 2036a(d)(2)(B)(ii) | 3251 | (ii) Effect of additional funds | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(d)(2)(B)(ii)(I) | 3252-3253 | (I) Funds received | encoded | `s 2036a(d)(2)(B)(ii) the funds are part of the State agency's fiscal year 2009 base allocation` |
| s 2036a(d)(2)(B)(ii)(II) | 3254-3255 | (II) Funds surrendered | encoded | `s 2036a(d)(2)(B)(ii) the funds are part of the State agency's fiscal year 2009 base allocation` |
| s 2036a(d)(3) | 3256 | (3) Limitation on Federal financial participation | inert1 | a heading or bare number: its content is in the sub-units below |
| s 2036a(d)(3)(A) | 3257-3258 | (A) In general | encoded | `s 2036a(d)(3)(A) the source is a source of Federal financial participation in nutrition education and obesity prevention` |
| s 2036a(d)(3)(B) | 3259-3260 | (B) Exclusion | encoded | `s 2036a(d)(3)(B) the cost is eligible for reimbursement under section 2025(a)` |
| s 2036a(e) | 3261-3262 | (e) Implementation | encoded | `s 2036a(e) the Secretary published the description in time` |
| s 2036a source credit | 3263 | Source credit | inert1 | the source credit: amendment history, not operative |

## Fork register (snap6)

Every ambiguity found, the readings seen, the one taken ("Reading A (taken)"), and the text that licenses each.
Where the text does not choose, the function answers `NOTHING` or the reading is stated as an assumption.

### s 2026 (research, demonstration, and evaluations)

- **FR-26-1: who is "the State" when it is made to act?** (d)(2)(D) says "Each State that has elected to carry out an employment initiatives program ... shall (i) increase the cash benefits ... (ii) pay the cost of any increase" (lines 2482-2485); (d)(4) says "A State that operates a program under this subsection for 2 years shall provide to the Secretary a written evaluation" and, in the next sentence, "The State agency, with the concurrence of the Secretary, shall determine the content" (line 2496); (l) puts the duty on "States, State agencies, local agencies, institutions, facilities such as data consortiums, and contractors" (line 2567); (n)(4)(B) says "Any State that establishes a longitudinal database ... shall" (lines 2627-2629). The core has `the State agency` and no party for the State as a government. Reading A (taken): the rules name `the State agency`. Reading B: "the State" is a different party from the agency that runs the programs (NEEDS-CORE.md). The text does not say which body does each act, and (d)(4) uses both words for the same program.
- **FR-26-2: how long does the annual report of (c) run?** "The Secretary shall report on the progress of these pilot programs on an annual basis commencing on July 1, 1982" (line 2466). Reading A (taken): one report is due on 1 July of each year from 1982, with no end date, so the function answers for 1982 and later and `NOTHING` for an earlier year. Reading B: the first report is due on 1 July 1982 and each later one a year after the last one was submitted. The text names a start and no end, and does not say what happens if a report is late.
- **FR-26-3: which vehicle does (h)(2) exclude?** "(2) one licensed vehicle used to obtain, continue, or seek employment ..., used to pursue employment-related education or training, or used to secure food or the benefits" (line 2509), after "(1) any licensed vehicle that is used to produce earned income, necessary for transportation of an elderly or physically disabled household member, or used as the household's home" (line 2508). Reading A (taken): a vehicle that qualifies under (1) is excluded by (1) and does not use up the one vehicle of (2); of the others that qualify under (2), the one with the greatest value over $4,500 is the one excluded, so the household counts the least. Reading B: the household chooses which one. Reading C: the Secretary or the State chooses. The text says "one" and does not say who picks or what happens when a vehicle qualifies under both.
- **FR-26-4: does the report of (k)(4)(B) cover the year in which the last evaluation is completed?** "Not later than 90 days after the last day of fiscal year 2009 and each fiscal year thereafter until the completion of the last evaluation under subparagraph (A), the Secretary shall submit ... a report" (line 2552). Reading A (taken): a report is due for each fiscal year from 2009 up to and including the one in which the last evaluation is completed; the fiscal year ends on 30 September, so the report is due on 29 December. Reading B: "until the completion" stops the reports before the year of completion. The text does not say.

### s 2031 (Minnesota Family Investment Project)

- **FR-31-1: in what order are "the higher of $10 or 75 percent" and "rounded to the nearest lower whole dollar" applied?** (b)(3)(E)(iv) says the monthly allotment "shall be the higher of $10 or 75 percent of the amount calculated following the standards of the supplemental nutrition assistance program and the foregoing requirements of this subparagraph, rounded to the nearest lower whole dollar" (line 2870). Reading A (taken): take 75 percent of the amount, round it down, and the allotment is the higher of that and $10. Reading B: take the higher of $10 and 75 percent, then round down. The two agree for every amount because $10 is a whole number, and `snap6-tests-s2031.l4` asserts both functions on 0, 13, 14, 15, 100 and 101, and the second also on 1000.
- **FR-31-2: what does it mean for an application to "comply with the requirements specified in subsection (b)"?** (d)(1) makes the Secretary's duty to approve depend on it (line 2916); (b) says the application "shall provide an assurance that the Project shall satisfy all of the following requirements" (line 2847). Reading A (taken): the application complies when it provides that assurance (`s 2031(b) the application complies with the requirements specified in subsection (b)` is `JUST TRUE` on the assurance and `NOTHING` without it). Reading B: it complies only if the Project in fact satisfies every paragraph of (b), which the paragraph functions test one by one; a caller who wants B must also require each of them.
- **FR-31-3: can the reduction in (b)(9) take the assistance below nothing?** "Assistance provided under the Project shall be reduced to reflect the pro rata value of any benefits received under the supplemental nutrition assistance program for the same period" (line 2887). Reading A (taken): the reduced assistance is never below nothing (`s 2031(b)(9) the assistance after the reduction, in dollars` answers 0 when the benefits equal or exceed the assistance). Reading B: it can be negative, which would be a sum owed back. The text says "reduced" and names no refund.
- **FR-31-4: on which day does the five-year period of (b)(14)(A) end?** "a five-year period beginning on the date the first family receives assistance under the Project" (line 2898). Reading A (taken): the day before the fifth anniversary of that date, so a period begun on 1 June 2025 ends on 31 May 2030. Reading B: the fifth anniversary itself. A period begun on 29 February 2024 has no 29 February 2029; on the stable binary `Date 29 2 2029` is 1 March 2029, so the period ends on 28 February 2029 (asserted).
- **FR-31-5: who is "the State" when it is made to act?** (b)(6)(A), (D), (F), (G), (7), (10), (13) and (i) put duties and permissions on "the State" (for example line 2874), (b)(3)(E)(ii) on "the State agency" (line 2868), and (j)(4) says "State" means the State of Minnesota (line 2948). The core has `the State agency` and no party for the State as a government. Reading A (taken): the rules name `the State agency`. Reading B: "the State" is a different party from the agency that runs the programs (NEEDS-CORE.md). The text does not say which body does each act.
- **FR-31-6: is a group of minor children living together with no parent and no caregiver a "family"?** (j)(1): "a minor child or a group of minor children related to each other as siblings, half siblings, stepsiblings, or adopted siblings, together with their natural or adoptive parents, or their caregiver" (line 2945). Reading A (taken): not covered, `NOTHING` (the text names the children "together with" parents or a caregiver and says nothing of children without them). Reading B: it is a family, the parents and caregiver being additions. Reading C: it is not, `JUST FALSE`. The text does not choose.
- **FR-31-7: from what day do the ten days and five days of (b)(10)(C) run?** "within ten days after receiving the request" and "within five days after the State receives such information" (line 2893). Reading A (taken): from the day of receipt, so the twin takes days from receipt and the trace starts at receipt. Reading B: from the day the request or information is sent or mailed. The text names receipt in both and says nothing about proof of it.
- **FR-31-8: how much does the Secretary pay for the administrative costs of (d)(1)(B)(ii)?** "the administrative costs incurred by the State ... equal to the amount that otherwise would have been paid under such subsections had the Project not been implemented" (line 2920). Reading A (taken): the amount section 2025 would have paid, and never more than the costs the State incurred. Reading B: always the amount section 2025 would have paid, whatever the State incurred. Both phrases are in the text and they come apart when the costs are lower.
- **FR-31-9: is an adjustment under (d)(2) only for an excess?** (A) and (B) say "the cost of benefits issued ... in excess of the amount that would have been issued ... had the Project not been implemented" (lines 2922-2923). Reading A (taken): the adjustment is the excess and is never negative. Reading B: it is the signed difference, so a shortfall lowers the payment. The text names only the excess.
- **FR-31-10: what is counted as allotments in (h)?** "benefits and the amount of federal liability for food assistance provided under the Project as limited by subsection (b)(12) ... shall be treated as allotments issued under the supplemental nutrition assistance program" (line 2939). Reading A (taken): the total is the allotments issued, plus the benefits issued, plus the federal liability for food assistance capped at the (b)(12) limit. Reading B: "benefits" and "the amount of federal liability" name the same sum, counted once. The text joins them with "and".
- **FR-31-11: when do the parents "not reside in the same home" in (j)(3)?** "when the minor child's natural or adoptive parent or parents do not reside in the same home" (line 2947). Reading A (taken): no parent resides there, so a listed relative is a caregiver only when neither parent lives in the home. Reading B: the listed relative is a caregiver whenever the parents do not both live there. The text does not say what it means for one of two parents to be present.
- **FR-31-12: what is the ceiling in (b)(12)?** "the Secretary shall not be liable for any costs ... in excess of those that the Secretary would have been liable for had the Project not been implemented, except for costs for evaluating the Project, but shall adjust for the full amount of the federal share of increases or decreases in costs" (line 2895). Reading A (taken): the ceiling is the baseline plus the signed adjustment. Reading B: the ceiling is the baseline, and only increases are paid on top. The text says "increases or decreases".

### s 2033 (repealed)

- None.

### s 2034 (community food projects)

- **FR-34-1: may a grant go to a public food program service provider or a tribal organization?** (b)(1) says "the Secretary may make grants to assist eligible private nonprofit entities" (line 3004); (c) says "To be eligible for a grant under subsection (b), a public food program service provider, a tribal organization, or a private nonprofit entity, including gleaners, must" meet four conditions (lines 3011-3019). Reading A (taken for (c)): (c) is the eligibility test for all four kinds it names, so `s 2034(c) ...` answers `JUST TRUE` or `JUST FALSE` for a provider or a tribal organization as for a nonprofit. Reading B (taken for (b)(1)): the grant itself goes only to private nonprofit entities, so `s 2034(b)(1) ...` answers `JUST TRUE` only where the caller supplies `the entity is an eligible private nonprofit entity` as `JUST TRUE`, and `NOTHING` otherwise. The text does not say which paragraph controls, so whether a public food program service provider can actually be granted money is not answered.

### s 2035 (simplified program)

- **FR-35-1: who is "the State" in s 2035(e)(2) and (e)(3)(A)?** The text says the Secretary "shall notify the State" (line 3087) and "the State shall submit a plan" (line 3090), but (e)(3)(B) terminates "the approval of the State agency" (line 3092). Reading A (taken): the duty bearer is the State agency, the only State-side party the core has (`the State agency`), because (e)(3)(B) shows the State agency is the operator that is approved. Reading B: "the State" is the State government as a whole, a different party from the agency that operates the Program. Licensed by: line 3087 and 3090 ("the State") against 3081 and 3092 ("State agency"). Rule: `s 2035(e)(2) the Secretary's duty to notify the State`, `s 2035(e)(3)(A) the State's duty to submit a plan for prompt corrective action`.
- **FR-35-2: do (c)(4) and (f)(1) name the same sources?** (c)(4) says benefits "shall be determined under rules and procedures established by the State under" (A) a TANF-funded State program, (B) SNAP, or (C) a combination (lines 3067-3070). (f)(1) says a State "may follow the rules and procedures" established under a TANF-funded State program or SNAP, and does not name the combination (lines 3094-3095). Reading A (taken): each paragraph answers for its own list: `s 2035(c)(4) ...` is `JUST TRUE` for all three sources, `s 2035(f)(1) ...` is `JUST TRUE` for two and `NOTHING` for the combination (limited by its own wording), so the two functions can differ and a caller who wants the whole answer reads both. Reading B: (f)(1) restates (c)(4) and the combination is permitted by both. Reading C: (c)(4)'s "shall be determined under" makes the three sources the only ones, so a fourth is barred; not taken, because (c)(4) does not say "only".
- **FR-35-3: when does the 90 days of (e)(3)(A) start?** "after the date of a notification under paragraph (2)" (line 3090) can mean the day the Secretary sends it or the day the State receives it. Reading A (taken): the day the Secretary does the act `s 2035 notify the State that the Program has increased Federal costs` (the trace event time). Reading B: the day of receipt. The text states no rule for receipt.
- **FR-35-4: does the "unless" of (d)(1) grant anything?** "A State agency may not operate a Program unless the Secretary approves a State plan" (line 3073). Reading A (taken): it only bars: no approval is `JUST FALSE`; an approval lifts the bar and the function answers `NOTHING` (the permission to elect is in (b)). Reading B: approval makes operating lawful, `JUST TRUE`. The text gives the permission elsewhere ((b)), and "may not ... unless" is a prohibition with an exception.

### s 2036 (commodities for the emergency food assistance program)

- **FR-36-1: which fiscal years does the duty cover?** (a)(1) says "for each of the fiscal years 2014 through 2023, the Secretary shall purchase a dollar amount described in paragraph (2)" (line 3114), while (a)(2) gives amounts for fiscal year 2008, fiscal year 2009 and "fiscal year 2024 and each subsequent fiscal year" (lines 3117, 3118, 3130), all outside that range, and says the Secretary "shall use [them] to carry out paragraph (1)". Reading A (taken): each paragraph answers as written: `s 2036(a)(1) the Secretary shall purchase commodities in the fiscal year` is `JUST TRUE` for 2014 to 2023 and `NOTHING` outside (limited by its own wording), and `s 2036(a)(2) ...` states an amount for every year it names. Reading B: the range in (a)(1) is a remnant and the duty applies in every year (a)(2) has an amount for. Reading C: amounts for years outside 2014-2023 are idle because (a)(2) only supplies amounts to "carry out paragraph (1)". The text does not choose, so whether the Secretary must buy in 2024 and later is `NOTHING`, while the amount for 2024 is stated.
- **FR-36-2: what does "adjusted by the percentage" mean, and from when?** (C) says the amount in (B) "adjusted by the percentage by which the thrifty food plan has been adjusted under section 2012(u)(3) ... between June 30, 2008, and June 30 of the immediately preceding fiscal year" (line 3119); (E) the (D)(ix) total adjusted by the percentage "between June 30, 2023, and June 30 of the immediately preceding fiscal year" (line 3130). Reading A (taken): the percentage is a cumulative figure for the window and the amount is the base times (1 plus the percentage over 100); the base is always the fixed one ((B)'s $250,000,000, (D)(ix)'s total), never the previous year's result. Reading B: each year's amount is the previous year's adjusted by that year's percentage (compounding); with a cumulative percentage the two agree, with an annual one they do not. The figure is a conditional input (a published figure), so the caller states which it is.
- **FR-36-3: do (C) and (D) both apply to fiscal years 2015 to 2023?** (D) says "the sum obtained by adding the total dollar amount of commodities specified in subparagraph (C) and" a further sum (line 3120). Reading A (taken): for 2015 to 2023 the amount is (D)'s sum, which already contains (C)'s amount; (C) alone applies to 2010 to 2014. Reading B: the Secretary shall use (C)'s amount and also (D)'s sum, which counts (C) twice. Licensed by: "shall use ... (C) for each of fiscal years 2010 through 2023" and "(D) for each of fiscal years 2015 through 2023" both name 2015 to 2023.
- **FR-36-4: what are the "2 fiscal years" of (a)(3)(A)?** "make the funds available for 2 fiscal years" (line 3133). Reading A (taken): the fiscal year of the funds and the next. Reading B: the two fiscal years after the one in which the funds are provided. The text does not say; compare s 2036a(d)(1) "to remain available for obligation for a period of 2 fiscal years", which does not settle it either.

### s 2036a (nutrition education and obesity prevention grant program)

- **FR-36a-1: does a fall in the Consumer Price Index lower the (d)(1)(F) amount?** "the applicable amount during the preceding fiscal year, as adjusted to reflect any increases for the 12-month period ending the preceding June 30 in the Consumer Price Index for All Urban Consumers" (line 3227). Reading A (taken): only increases count ("any increases"), so a negative figure leaves the amount unchanged (`s 2036a(d)(1) the amount reserved for the fiscal year, in dollars` tests it: a fall of 5 percent leaves 415,140,000). Reading B: the amount is adjusted by the change in either direction. The text says "increases" and is silent about decreases.
- **FR-36a-2: who is "the Administrator of the Food and Nutrition Service"?** (c)(3)(A)-(B) and (c)(9) give the duties to "the Administrator of the Food and Nutrition Service" (lines 3180, 3185, 3213), (c)(6), (c)(7) and (d) to "the Secretary". The core has `the Secretary` and no Administrator. Reading A (taken): the Administrator acts for the Secretary, so the rules use `the Secretary` as the party; the need for an Administrator constructor is in NEEDS-CORE.md. Reading B: the Administrator is a separate office, and a rule that names `the Secretary` for the Administrator's duty is wrong about who must act.


## Jural relations (snap6)

One row per provision that creates a relation, in Hohfeld's terms: the holder of the right, privilege, power or immunity; the bearer of the correlative duty, no-right, liability or disability; the L4 rule that encodes it.
A provision that creates no relation (a definition, a counting rule, a cap) is listed once, with `none` as the holder.
Each relation is stated once, in layer 1, and named neutrally.

### s 2026 (research, demonstration, and evaluations)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2026(a)(1) | the Secretary: privilege to enter into research contracts and make grants; power to extend the (b) waivers to them | public or private organizations: liability to the Secretary's choice; no claim to a grant | `s 2026(a)(1) the Secretary's permission to enter into contracts or make grants for research`, `... the waiver authority of subsection (b) extends to the instrument` |
| s 2026(a)(2) | the Secretary: power, on application, to permit two State agencies; a household with benefits of $20 or less: privilege (at its option) to take an aggregate allotment | the State agency: liability to the Secretary's permission; the household: it receives nothing above $60 or for more than 3 months | `s 2026(a)(2) ...` (five rules and functions) |
| s 2026(a)(2), parenthesis | the Secretary and the household: the verification requirements of section 2020(e)(3) protect the program | the household: disability to begin to receive combined allotments before it has complied | `s 2026(a)(2) the household may begin to receive combined allotments` |
| s 2026(b)(1)(A) | the Secretary: privilege to run pilot or experimental projects; power to waive any requirement of the chapter to the extent necessary | households and State agencies in the project area: liability to the project and the waiver | `s 2026(b)(1)(A) ...` (a rule and a function) |
| s 2026(b)(1)(B)(i), (ii), (iii), (iv) | none (limits on the power in (A)) | the Secretary: disability to conduct a project that lacks the goal and evaluation, or that does what (iv)(I) to (VII) lists; a project that reduces benefits by more than 20 percent for more than 5 percent of households in the area: disability to exceed 15 percent of the State's households or 5 years without an extension | `s 2026(b)(1)(B)(i) ...` to `(iv)(III) ...` |
| s 2026(b)(1)(B)(v) | the Secretary: privilege to include the three kinds of project | households in a cash-payment project: liability to it | `s 2026(b)(1)(B)(v) ...` |
| s 2026(b)(1)(B)(vi) | the State: claim to continuation of the 1981 cash pilot project on request, subject to appropriations | the Secretary: duty to continue it | `s 2026(b)(1)(B)(vi) ...` |
| s 2026(b)(1)(C) | none (a bar) | the Secretary: disability to approve a waiver or demonstration program after 28 November 1990 unless sales tax is compensated and the State agency pays | `s 2026(b)(1)(C) ...` |
| s 2026(b)(1)(D)(i) | a State agency that requested a waiver: claim to a response within 60 days | the Secretary: duty to respond with one of the four responses | `s 2026(b)(1)(D)(i) ...` (a rule and two functions) |
| s 2026(b)(1)(D)(ii) | the State agency: immunity, on silence, from the Secretary's refusal; the waiver is deemed approved | the Secretary: disability to refuse after 60 days of silence, unless the chapter prohibits the approval | `s 2026(b)(1)(D)(ii) ...` |
| s 2026(b)(1)(D)(iii) | the Committees on Agriculture: claim to a copy and the reasons | the Secretary: duty to provide them on a denial under (i)(III) | `s 2026(b)(1)(D)(iii) ...` (a rule and a function) |
| s 2026(b)(2)(A), (B) | the Secretary: privilege to run employment and training demonstration projects; power to waive section 2015(d) | participants and State agencies: liability to the project and the waiver | `s 2026(b)(2)(A) ...`, `s 2026(b)(2)(B) ...` |
| s 2026(b)(2)(C) | the Secretary: claim to assurances from a State seeking the waiver | the State: duty to provide them; the sections named: deemed to speak of SNAP benefits | `s 2026(b)(2)(C) ...` (two functions) |
| s 2026(b)(2)(D) | a participant: immunity from conversion of SNAP benefits to cash without consent | the State and the Secretary: disability to convert without it | `s 2026(b)(2)(D) ...` |
| s 2026(b)(2)(E) | the Secretary: power to waive the provisions affecting recipients' rights, to the extent necessary to conform | recipients: liability to the waiver | `s 2026(b)(2)(E) ...` |
| s 2026(b)(2)(F) | the public and the Committees: claim to publication and notice 60 days before final approval | the Secretary: duty to publish and notify | `s 2026(b)(2)(F) ...` (a rule and a function) |
| s 2026(b)(2)(G), (H), (I) | none (limits) | the Secretary: disability to waive for more than 60 project areas, for a project not approved and evaluated or running more than 4 years, or on or after 22 August 1996 | `s 2026(b)(2)(G) ...`, `(H) ...`, `(I) ...` |
| s 2026(c), first sentence | the public: not stated by the text | the Secretary: duty to develop and implement measures for evaluating the program annually or more often | `s 2026(c) the Secretary's duty to develop and implement measures for evaluating the program` and two functions |
| s 2026(c), second and third sentences | not stated by the text | the Secretary: duty to implement the pilot programs, selecting locations as stated | `s 2026(c) the Secretary's duty to implement pilot programs to measure nutritional status`, `... locations ...` |
| s 2026(c), last sentence | the Committees on Agriculture: claim to an annual report from 1 July 1982 | the Secretary: duty to report | `s 2026(c) the Secretary's duty to report on the progress of the pilot programs` and two functions |
| s 2026(d)(1) | the State: power to elect an employment initiatives program, if at least 50 percent of its summer 1993 SNAP households also received part A benefits | the Secretary: liability to the election | `s 2026(d)(1)(A) ...`, `s 2026(d)(1)(B) ...` |
| s 2026(d)(2)(A) | the State: privilege to use amounts equal to the allotments to give cash benefits to an eligible household | the household's SNAP allotment: replaced | `s 2026(d)(2)(A) ...` |
| s 2026(d)(2)(B) | the State: claim to payment of the value of the allotments | the Secretary: duty to pay | `s 2026(d)(2)(B) the Secretary's duty to pay the State the value of the allotments` and the amount function |
| s 2026(d)(2)(C) | none (a deeming rule); a household receiving cash benefits: no claim to other SNAP benefits | the household: disability to receive other SNAP benefits in the period | `s 2026(d)(2)(C)(i) ...`, `(ii) ...` |
| s 2026(d)(2)(D) | a household in the program: claim to the sales tax increase, unless the Secretary found it unnecessary | the State (the State agency, FR-26-1): duty to increase the benefits and to pay the cost | `s 2026(d)(2)(D)(i) ...`, `s 2026(d)(2)(D)(ii) the State agency's duty to pay the cost of the increase` |
| s 2026(d)(3) | an adult member who meets (A) to (E): privilege (at its election) to cash benefits for the household | the household's SNAP allotment: replaced | `s 2026(d)(3) ...` (two functions) |
| s 2026(d)(4) | the Secretary: claim to a written evaluation after 2 years | the State (the State agency, FR-26-1): duty to provide it; the State agency: power, with the Secretary's concurrence, to fix its content | `s 2026(d)(4) ...` (a rule and a function) |
| s 2026(e) | the Committees on Agriculture: claim to the interim and final reports | the Secretary: duty to study and to report by 1 February 1984 and 1 March 1985 | `s 2026(e) ...` (a rule and three functions) |
| s 2026(f) | the Secretary: privilege to run pilot projects on intelligent benefit cards | none stated; households in the project: liability | `s 2026(f) ...` (a rule and two functions) |
| s 2026(g) | the Secretary: privilege to study employment and training programs; not stated by the text for the duty to consider the results | the Secretary: duty to consider the results in developing or updating the performance standards | `s 2026(g) ...` (a rule and three functions) |
| s 2026(h) | the Secretary: duty owed to no one named; a household: immunity from counting the value of a vehicle under (1) and one under (2) | the Secretary: duty to conduct a sufficient number of demonstration projects; the State agency: no-right to count the excluded vehicles | `s 2026(h) ...` (a rule and six functions) |
| s 2026(i) | households in the projects: privilege to accumulate up to $10,000 excluded as a resource | the Secretary: duty to conduct projects of up to 4 years and 11,000 households | `s 2026(i) ...` (a rule and three functions) |
| s 2026(j) | State or local SNAP agencies: privilege to test ideas with law enforcement | the Secretary: duty to use up to $4,000,000 | `s 2026(j) ...` (a rule and a function) |
| s 2026(k)(1) | not stated by the text | the Secretary: duty to carry out the pilot projects | `s 2026(k)(1) ...` |
| s 2026(k)(2) | the Secretary: privilege to contract, make cooperative agreements and grants; an organization: no claim, and a necessary step (the application) | the organization: liability; the Secretary: disability to fund a project that limits the use of benefits | `s 2026(k)(2)(A) ...` to `(D) ...` |
| s 2026(k)(3) | the Secretary: privilege to include the listed kinds of project | participating households: liability | `s 2026(k)(3) ...` |
| s 2026(k)(4) | the Secretary: duty to provide for an independent evaluation; privilege to pay the monitoring and evaluation costs; the Committees: claim to the report; the public: claim to dissemination | the Secretary: duty to evaluate, report and share the results | `s 2026(k)(4)(A)(i)(I) ...`, `(II) ...`, `(A)(ii) ...`, `(B) ...`, `(C) ...` |
| s 2026(k)(5) | the Secretary: privilege to spend what is appropriated for 2008 to 2012; the pilot project: claim to $20,000,000 on 1 October 2008 | Congress: authorises; the Secretary: duty to make the $20,000,000 available | `s 2026(k)(5)(A) ...`, `s 2026(k)(5)(B) ...` |
| s 2026(l) | the Secretary: claim to cooperation and to information at the time and in the manner required | States, State agencies, local agencies, institutions, facilities and contractors in SNAP: duty to cooperate and to submit, subject to section 2020(e)(8) (FR-26-1) | `s 2026(l)(1) ...`, `s 2026(l)(2) ...`, `s 2026(l) ...` |
| s 2026(m)(1), (2) | the Secretary of Health and Human Services: claim to be consulted (no party in the core) | the Secretary: duty to conduct the evaluation and assess (A) to (F) | `s 2026(m)(1) ...`, `s 2026(m)(2) ...` |
| s 2026(m)(3) | the Secretary: claim to information | each State agency selected: duty to provide it | `s 2026(m)(3) the State agency's duty to provide information for the evaluation` |
| s 2026(m)(4) | the Committees on Agriculture: claim to a report by 20 December 2021 | the Secretary: duty to report | `s 2026(m)(4) ...` (a rule and two functions) |
| s 2026(n)(1), (2) | a State agency: privilege, on the Secretary's approval, to establish a longitudinal database, to be used solely for research | the State agency: disability to use it for anything else | `s 2026(n)(1) ...`, `s 2026(n)(2) ...` |
| s 2026(n)(3) | State agencies: claim to the preparations before approval | the Secretary: duty to complete (A) to (I) before approving | `s 2026(n)(3) ...` (a rule and a function) |
| s 2026(n)(4) | researchers and the Secretary: claim to the data; household members: claim to privacy | the State (the State agency, FR-26-1): duty to protect privacy and make the data available; privilege to include data (A)(ii) | `s 2026(n)(4)(A) ...`, `(B)(i) ...`, `(B)(ii) ...` |
| s 2026(n)(5) | a State that meets (A) to (C): claim to approval | the Secretary: duty to approve | `s 2026(n)(5) ...` (a rule and a function) |
| s 2026(n)(6) | the Secretary: privilege to grant to approved States, in the amounts it decides | an approved State: no claim to a grant | `s 2026(n)(6)(A) ...`, `(B) ...` |
| s 2026(n)(7) | the Committees on Agriculture: claim to a report 4 years after the effective date | the Secretary: duty to report on cost, challenges and benefits, and alternatives | `s 2026(n)(7)(A) ...`, `(B) ...` |
| s 2026(n)(8) | State agencies: immunity from a limit on databases used for similar purposes | this subsection: disability to prevent or limit them | `s 2026(n)(8) ...` |
| s 2026(n)(9) | the Secretary: claim to the funds | the Secretary: duty to use $20,000,000 for 2019 (available to 2021) and $5,000,000 for 2022 and after | `s 2026(n)(9) ...` (a rule and two functions) |

### s 2031 (Minnesota Family Investment Project)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2031(a)(1) | the State: privilege to implement the Project once the Secretary approves its application | the Secretary: no-right to refuse a complying application (see (d)(1)(A)) | `s 2031(a)(1) the State may implement the Project` |
| s 2031(a)(2) | the Secretary of Health and Human Services: power to approve the application | the State: disability to implement the Project without that approval and outside this section | `s 2031(a)(2) the Project may be implemented` |
| s 2031(b) | the Secretary: claim to an assurance in the application | the State: duty to provide it | `s 2031(b) the application complies with the requirements specified in subsection (b)` |
| s 2031(b)(1) | the State: power to extend the Project to families | a group that is not a family: disability to be eligible | `s 2031(b)(1) the group may be eligible ...` |
| s 2031(b)(2) | none stated (the State's participating families lose SNAP) | participating, assigned and application-required families: disability to receive SNAP benefits | `s 2031(b)(2) the family may receive benefits under the supplemental nutrition assistance program` |
| s 2031(b)(3)(A), (B), (C)(iii) | a participating family: claim to assistance not less than it could get outside the Project | the State: duty to provide it and to make up any shortfall | `s 2031(b)(3)(A) ...`, `s 2031(b)(3)(B) ...`, `s 2031(b)(3)(C)(iii) ...` |
| s 2031(b)(3)(B)(iii) | a participating family: claim to have child support counted only above $50 a month | the State: duty so to count | `s 2031(b)(3)(B)(iii) ...` |
| s 2031(b)(3)(C)(i), (ii) | the Secretary: claim that the State identify and test the families at risk | the State: duty to identify the characteristics and determine for each such family; no duty for other families | `s 2031(b)(3)(C)(i) ...`, `s 2031(b)(3)(C) ...` |
| s 2031(b)(3)(C)(iv) | a participating family: claim to a sales-tax increase | the State: duty to increase the assistance where a sales tax on food is imposed | `s 2031(b)(3)(C)(iv) ...` (two rules) |
| s 2031(b)(3)(D)(i), (ii), (iii) | a participating family: claim to a monthly notice of the designated food amount, to at least the SNAP value, and to the option to take benefits | the State: duty to designate, to notify monthly, to set the amount at or above the SNAP value, and to allow the option periodically | `s 2031(b)(3)(D)(i) ...`, `(ii)`, `(iii)` |
| s 2031(b)(3)(E)(i)-(iv) | an individual ineligible for the Project in a household with a participating family: claim to SNAP determination on SNAP standards, without regard to the family, with the maximum excess shelter deduction, and to the monthly allotment (the higher of $10 or 75 percent, rounded down) | the State agency: duty to determine, calculate and issue so | `s 2031(b)(3)(E)(i) ...` to `(iv)` |
| s 2031(b)(4) | a participating family: claim to equivalent education, employment and training services | the State: duty to include them in the Project | `s 2031(b)(4) ...` |
| s 2031(b)(5) | the State: privilege to select families by application or by assignment | none stated | `s 2031(b)(5) the State may select a family this way` |
| s 2031(b)(6)(A) | an applicant family: claim to a determination and assistance, retroactive to the date of application, within thirty days | the State agency: duty so to determine and issue | `s 2031(b)(6)(A) ...` (three rules) |
| s 2031(b)(6)(B) | a family found ineligible on application: claim to have the application treated as a SNAP application and to SNAP benefits if eligible | the State: duty so to treat and to issue | `s 2031(b)(6)(B) ...` (two rules) |
| s 2031(b)(6)(C) | an applicant: claim to expedited benefits on terms no more restrictive than section 2020(e)(9) | the State: duty to provide them, in a permitted form | `s 2031(b)(6)(C) ...` (two rules) |
| s 2031(b)(6)(D) | an individual who contacts the State in person during office hours to ask for assistance: claim to an application form, and to file it, the same day | the State agency: duty to give it and permit filing that day | `s 2031(b)(6)(D) ...` (two rules) |
| s 2031(b)(6)(E) | an elderly, handicapped or hardship-bound individual: claim to telephone, mail and interview arrangements | the State: duty to make the provision | `s 2031(b)(6)(E) ...` |
| s 2031(b)(6)(F) | a family: privilege to be represented by a designated, aware adult | none stated | `s 2031(b)(6)(F) ...` |
| s 2031(b)(6)(F)(i), (ii) | the State: privilege to restrict the number of families a representative may represent and to set criteria and verification standards | a family and its representative: liability to the restriction and the standards | `s 2031(b)(6)(F)(i) ...`, `s 2031(b)(6)(F)(ii) ...` |
| s 2031(b)(6)(G) | a family with no permanent dwelling or fixed mailing address: claim to a method of review and distribution | the State: duty to provide it | `s 2031(b)(6)(G) ...` |
| s 2031(b)(7)(A), (B) | a family assigned to the Project: claim to assistance no later than SNAP would have come, and to no interruption | the State: duty so to provide and ensure | `s 2031(b)(7)(A) ...`, `s 2031(b)(7)(B) ...` |
| s 2031(b)(8), (11) | an applicant or participating family: claim to the protections of section 2020(e)(1)(B), (8) and (10), and (11) to notice consistent with the Social Security Act regulations | the State: duty to apply them | `s 2031(b)(8) ...`, `s 2031(b)(11) ...` (two rules) |
| s 2031(b)(9) | the Secretary: claim to a pro rata reduction | a participating family: liability to the reduction | `s 2031(b)(9) ...` |
| s 2031(b)(10)(A) | a family or member whose participation ends: claim to notice of SNAP and whom to contact | the State agency: duty to give it | `s 2031(b)(10)(A) ...` (two rules) |
| s 2031(b)(10)(B)(i) | a family or member whose participation ends: claim to SNAP benefits retroactive to the date of termination | the State: duty to ensure them if eligible | `s 2031(b)(10)(B)(i) ...` (two rules) |
| s 2031(b)(10)(B)(ii) | an excluded applicant, family or individual: claim to continued State-funded food assistance until SNAP is decided or ten days pass; the State: claim to be repaid by the Secretary | the State agency: duty to exclude and to keep paying; the Secretary: duty to pay the State | `s 2031(b)(10)(B)(ii) ...` (six rules) |
| s 2031(b)(10)(C) | a family whose participation is terminated: claim to screening, a specific request with help, a determination within five days of its information, and notice of ineligibility | the State: duty to screen, request, determine and notify | `s 2031(b)(10)(C) ...` (six rules) |
| s 2031(b)(12) | the Secretary: immunity from costs above the baseline plus adjustments | the State: no-right to more | `s 2031(b)(12) ...` (two rules) |
| s 2031(b)(13) | the Secretary and the State's households: claim that SNAP run statewide | the State agency: duty so to carry it out | `s 2031(b)(13) ...` (two rules) |
| s 2031(b)(14)(A), (B) | the Secretary and the State: claim to a five-year Project; each: power to end it by notice, after hearing, or by agreement | the other party: liability to termination after 180 days | `s 2031(b)(14)(A) ...` (two rules), `s 2031(b)(14)(B) ...` |
| s 2031(b)(15) | the Secretary: immunity from a larger Project | the State: disability to enrol more than six thousand families | `s 2031(b)(15) ...` |
| s 2031(c)(1) | the State: power to require a parent to take part in education, employment or training | an exempt parent: immunity; any other parent: liability | `s 2031(c)(1) ...` |
| s 2031(c)(2) | a single parent of a child under six: immunity from more than twenty hours | the State: disability | `s 2031(c)(2) ...` |
| s 2031(c)(3) | the State: power to reduce assistance by up to 10 percent for non-compliance without good cause | the family: liability, limited to that amount | `s 2031(c)(3) ...` (two rules) |
| s 2031(d)(1)(A) | the State: claim to approval of a complying application | the Secretary: duty to approve | `s 2031(d)(1)(A) ...` (two rules) |
| s 2031(d)(1)(B) | the State: claim to quarterly payment of the food assistance cost and of the administrative costs, equal to what would have been paid | the Secretary: duty to pay, subject to (b)(12) | `s 2031(d)(1)(B) ...`, `s 2031(d)(1)(B)(i) ...`, `s 2031(d)(1)(B)(ii) ...` (three rules) |
| s 2031(d)(2) | the State: claim to adjustment for the excess cost of benefits issued to ineligible individuals and option families | the Secretary: duty to adjust | `s 2031(d)(2) ...`, `s 2031(d)(2)(A) ...`, `s 2031(d)(2)(B) ...` |
| s 2031(d)(3) | the State: claim to payments adjusted for changes in conditions | the Secretary: duty to include the adjustments | `s 2031(d)(3) ...` |
| s 2031(e) | the State: claim to a waiver of any requirement of the chapter (other than section 2031) that would prevent the Project | the Secretary: duty to waive | `s 2031(e) ...` (two rules) |
| s 2031(f)(1), (2) | the Secretary and the Committees: claim to audits and reports | the Comptroller General: duty to audit and report (no party in the core) | `s 2031(f)(1) ...`, `s 2031(f)(2) ...` |
| s 2031(g)(1) | a participating family and the State: claim to SNAP treatment for other laws | any other law's administrator: liability | `s 2031(g)(1)(A) ...`, `s 2031(g)(1)(B) ...` |
| s 2031(g)(2) | the State and its eligible households: immunity from lower payments; the Secretary: immunity from costs above the baseline | none stated | `s 2031(g)(2)(A) ...`, `s 2031(g)(2)(B) ...` |
| s 2031(h) | the Secretary: power to count the Project's benefits as allotments; a participating family: immunity from the quality control sample | the State: none stated | `s 2031(h) ...` (two rules) |
| s 2031(i)(1) | the Secretary of Agriculture: claim to an evaluation plan with the content listed | the State agency: duty to develop and implement it | `s 2031(i)(1) ...` (three rules) |
| s 2031(i)(2) | the Federal Government and the State: each owes half | the State: duty to pay 50 percent; the Federal Government: duty to pay the remainder | `s 2031(i)(2) ...` (two rules) |
| s 2031(j)(1)-(4) | none (definitions) | none | `s 2031(j)(1) ...` to `s 2031(j)(4) ...` |

### s 2033 (repealed)

none (repealed): the heading says the section is repealed and the section has no text.

### s 2034 (community food projects)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2034(a)(1), (a)(2), (a)(3) | none (definitions) | none | `s 2034(a)(1) ...`, `s 2034(a)(1)(B)(ii) ...`, `s 2034(a)(2) ...`, `s 2034(a)(3) ...` |
| s 2034(b)(1) | the Secretary: power to make grants; an eligible private nonprofit entity: no claim (the text says "may") | the entity: liability to the Secretary's choice | `s 2034(b)(1) the Secretary may make a grant to assist the entity with the project` |
| s 2034(b)(2) | none (a cap) | the Secretary: disability to provide more than the cap | `s 2034(b)(2) ...` (two rules) |
| s 2034(c) | the applicant (a provider, a tribal organization, a nonprofit, a gleaner): privilege to apply once it meets (1) to (4) | the applicant: it must meet them; the Secretary: no-right to grant otherwise | `s 2034(c) the entity is eligible for a grant under subsection (b)` |
| s 2034(d) | a project designed as (1) to (5): claim to a preference | the Secretary: duty to give the preference | `s 2034(d) the Secretary shall give the project a preference` |
| s 2034(e) | the Secretary: claim that the Federal share is at most 50 percent and that the rest is provided in cash or in kind | the grantee: duty to provide the non-Federal share; the grantee's privilege to use State, local or private sources | `s 2034(e)(1)`, `(e)(2)`, `(e)(3)` rules |
| s 2034(f)(1), (f)(2) | the Secretary: immunity from a second grant for the project and from a term over 5 years | the grantee: disability | `s 2034(f)(1) ...`, `s 2034(f)(2) ...` |
| s 2034(g) | the Secretary: privilege to give assistance and to share information | an entity seeking assistance, government, private groups, the public, researchers: no-right | `s 2034(g)(1)`, `(g)(2)(A)`, `(g)(2)(B)` rules |
| s 2034(h) | Congress: claim to an annual report by 30 September | the Secretary: duty to submit, describing each grant | `s 2034(h) ...` (three rules) |

### s 2035 (simplified program)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2035(a) | none (a definition) | none | `s 2035(a) the cost is a Federal cost for this section` |
| s 2035(b) | the State: power to elect to carry out a Program | the Secretary and the State's households: liability to a Program the State operates once approved under (d) | `s 2035(b) the State may elect to carry out a Program there` |
| s 2035(c)(1) | the State agency: immunity from having to enrol such a household | a household with no member on a TANF-funded program: disability (it may not participate) | `s 2035(c)(1) the household may participate in the Program` |
| s 2035(c)(2) | a household all of whose members receive such assistance: claim to automatic eligibility | the State agency: duty to treat it as eligible | `s 2035(c)(2) the household is eligible to participate in the Program` |
| s 2035(c)(3) | the Secretary: power to approve; the mixed household: privilege to be eligible once approved | the household: liability to the Secretary's approval; the State agency: no-right until approval | `s 2035(c)(3) the household may be eligible to participate in the Program` |
| s 2035(c)(4), (f)(1) | the State: privilege to use the named rules | the Secretary: no-right | `s 2035(c)(4) ...`, `s 2035(f)(1) ...` |
| s 2035(d)(1) | the Secretary: power to approve a plan | the State agency: disability (it may not operate without approval) | `s 2035(d)(1) the State agency may operate a Program` |
| s 2035(d)(2) | the State: claim to approval when the Secretary determines (A) and (B) | the Secretary: duty to approve | `s 2035(d)(2) the Secretary shall approve the State plan` |
| s 2035(e)(1)(A) | not stated by the text | the Secretary: duty to determine | `s 2035(e)(1)(A) the Secretary's duty to determine whether the Program is increasing Federal costs` |
| s 2035(e)(1)(B) | the State agency: immunity from a reporting demand about excluded households | the Secretary: disability and duty not to require | `s 2035(e)(1)(B) the Secretary's prohibition on requiring information on households not in the Program` |
| s 2035(e)(1)(C) | the Secretary: privilege to approve alternative accounting periods | the State agency: no-right to refuse; it holds only the right to ask | `s 2035(e)(1)(C) the Secretary's permission to approve alternative accounting periods` |
| s 2035(e)(2) | the State: claim to notice within 30 days | the Secretary: duty to notify | `s 2035(e)(2) the Secretary's duty to notify the State` |
| s 2035(e)(3)(A) | the Secretary: claim to a corrective plan within 90 days | the State agency: duty to submit | `s 2035(e)(3)(A) the State's duty to submit a plan for prompt corrective action` |
| s 2035(e)(3)(B) | the Secretary: power to terminate (and, here, a duty to) | the State agency: liability to termination, then disability to operate a future Program | `s 2035(e)(3)(B) ...` (three rules) |
| s 2035(f)(2) | the State: privilege to standardize deductions | the Secretary: no-right | `s 2035(f)(2) the State may standardize the deduction` |
| s 2035(f)(2), second sentence | not stated by the text | the State: duty to consider work expenses, dependent care costs and shelter costs | `s 2035(f)(2) the State has considered what it shall consider` |
| s 2035(f)(3) | participating households and the Secretary (the requirements protect households; the text names no claimant) | the State: duty to comply with the listed requirements | `s 2035(f)(3) the State complies with the requirements it shall comply with` |
| s 2035(f)(4) | the Secretary: power to determine | a household eligible only under the State program: disability (may not receive benefits under this section unless the Secretary determines) | `s 2035(f)(4) ...` |

### s 2036 (commodities for the emergency food assistance program)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2036(a)(1) | the States: claim to receive commodities for distribution | the Secretary: duty to purchase and distribute | `s 2036(a)(1) the Secretary's duty to purchase commodities and distribute them to States`, `s 2036(a)(1) the Secretary shall purchase commodities in the fiscal year`, `s 2036(a)(1) the commodity is one the Secretary shall purchase` |
| s 2036(a)(2)(A) to (E) | the States (through the program): claim to the stated dollar amount | the Secretary: duty to use at least the stated amount | `s 2036(a)(2)(A)`, `(B)`, `(C)`, `(D)`, `(E)` amounts and `s 2036(a)(2) ...` |
| s 2036(a)(3)(A) | the States: claim to the funds for 2 fiscal years | the Secretary: duty to make them available | `s 2036(a)(3)(A) ...` (two rules) |
| s 2036(a)(3)(B) | the States: claim to carry over unexpended balances on the Secretary's terms | the Secretary: duty to allow, and power to set the terms | `s 2036(a)(3)(B) ...` (two rules) |
| s 2036(b) | none: States, distributing agencies and recipients have no claim (the text says "preferences") | the Secretary: duty to base purchases on the three things, to the extent practicable and appropriate | `s 2036(b) the purchases are based as the Secretary shall base them` |

### s 2036a (nutrition education and obesity prevention grant program)

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| s 2036a(a) | none (a definition); it fixes who may be reached by the program | none | `s 2036a(a) the individual is an eligible individual` |
| s 2036a(b) | the State agency: privilege to implement a program for eligible individuals | the Secretary and non-eligible individuals: no-right | `s 2036a(b) ...` (two rules) |
| s 2036a(c)(1) | the State agency: privilege to deliver directly or by agreement | the Secretary: no-right | `s 2036a(c)(1) the State agency may deliver the services this way` |
| s 2036a(c)(2)(A) | the Secretary: claim to a plan | a State agency that elects to provide the services: duty to submit it for approval | `s 2036a(c)(2)(A) ...` (two rules) |
| s 2036a(c)(2)(B) | the Secretary: claim that the plan has the four things | the State agency: duty | `s 2036a(c)(2)(B) the plan contains what it shall` |
| s 2036a(c)(3)(A) | the State agency: privilege to use funds for an evidence-based use the Administrator identified | the Administrator: no-right | `s 2036a(c)(3)(A) ...` (two rules) |
| s 2036a(c)(3)(B) | not stated | the Administrator: duty to consult the Directors and outside stakeholders | `s 2036a(c)(3)(B) ...` (two rules) |
| s 2036a(c)(4) | applicants, participants and eligible individuals under this chapter: claim to be told of the services, to the maximum extent practicable | the State agency: duty to notify | `s 2036a(c)(4) ...` (two rules) |
| s 2036a(c)(5) | the State agency: privilege to coordinate; the Secretary: power to approve | the Secretary's approval is a condition; projects outside State agency control: disability | `s 2036a(c)(5) the projects may be coordinated with other programs and strategies` |
| s 2036a(c)(6), (c)(7) | State agencies, local agencies, institutions of higher education and community organizations: claim to the clearinghouse; a State agency: claim to technical assistance | the Secretary: duty | `s 2036a(c)(6) ...`, `s 2036a(c)(7) ...` |
| s 2036a(c)(8) | the Secretary and the public: claim to an annual State report | each State agency that delivers the services: duty to submit it | `s 2036a(c)(8) ...` (three rules) |
| s 2036a(c)(9) | the two Committees: claim to an annual report | the Administrator: duty | `s 2036a(c)(9) ...` (two rules) |
| s 2036a(d)(1) | State agencies: claim to the reserved funds | the Secretary: duty to reserve them | `s 2036a(d)(1) ...` (two rules) |
| s 2036a(d)(2)(A) | each State agency: claim to its share | the Secretary: duty to allocate | `s 2036a(d)(2)(A) ...` (three rules) |
| s 2036a(d)(2)(B) | other States with approved plans: claim to reallocated funds | the Secretary: duty to reallocate; the State agency: liability to losing unexpended funds | `s 2036a(d)(2)(B)(i) ...`, `s 2036a(d)(2)(B)(ii) ...` |
| s 2036a(d)(3) | the Secretary: immunity from other Federal financial participation and from reimbursement above the grants | State agencies: disability | `s 2036a(d)(3)(A) ...`, `s 2036a(d)(3)(B) ...` |
| s 2036a(e) | the public: claim to a published description of the requirements | the Secretary: duty to publish by 1 January 2012 | `s 2036a(e) ...` |


## Marginal readings for a lawyer (snap6)

The rule of 2026-10-29 for `JUST FALSE` and `NOTHING` is assumed, not ruled by a lawyer.
Two readings are for a lawyer, and every branch below rests on one of them, with the other reading stated:
(a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text saying no;
(b) a prohibition or a grant limited by its own wording does not.

### s 2026 (research, demonstration, and evaluations)

Reading (a) is that a failed "if" counts as the text's no, and that flat negatives and plain-word limits count. Reading (b) is that a prohibition or a grant limited by its own wording does not.

- `s 2026(a)(2) the first aggregate allotment was provided in time`, `JUST FALSE`: "within 40 days of the last benefit issuance" is a time bound on a duty, which is not one of the words the brief lists; read as the text's no (reading (a)). Other reading: `NOTHING`. The same reading carries the "not later than" and "no later than" branches of `s 2026(b)(1)(D)(i) ... in time`, `s 2026(b)(2)(F) ...`, `s 2026(c) ... progress report ... in time`, `s 2026(e) ... interim report ... in time`, `... final report ... in time` and `s 2026(m)(4) ... report in time`; it is the same reading `s 2036a(e)` rests on.
- `s 2026(a)(2) the household may receive the aggregate allotment`, `NOTHING` when the household's benefits exceed $20 or it does not choose: "households whose monthly ... benefits do not exceed $20, at their option" limits the grant by its own wording (reading (b)). Other reading: "whose" states a condition and a household over $20 is `JUST FALSE`.
- `s 2026(b)(1)(B)(iii) the restrictions apply to the project`, `JUST FALSE`: "If the Secretary finds that a project ... would reduce benefits by more than 20 percent for more than 5 percent of households" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: `NOTHING`, the text says when the restrictions apply and not that they do not otherwise.
- `s 2026(b)(1)(B)(vi) the project shall be continued`, `JUST FALSE` when the State does not request it: "if the State so requests" is an "if" (reading (a)). Its `NOTHING` when appropriations are not shown (a `NOTHING` input) and also when section 2027(a) answers that they are not available (a `JUST FALSE` input, pinned by `snap6-tests-s2026.l4` line 164): "Subject to the availability of appropriations under section 2027(a)" is not one of the brief's words, so it limits the duty by its own wording and another section's `JUST FALSE` does not become this text's no (reading (b)). Other reading: "subject to" is a condition like the "if" beside it, and the answer is `JUST FALSE` for an input of `JUST FALSE`; that is how `s 2026(f)` reads its "subject to" (above) and how `s 2035(f)(3)` carries a requirement group's `JUST FALSE`. On the other side, `s 2036a(c)(5)` ("Subject to the approval of the Secretary", approval answered `JUST FALSE`) answers `NOTHING` as (vi) does. The encoding is split on "subject to" until a lawyer rules: it imports a no where the imported provision's own words are a flat negative or an "only if" (`s 2026(f)`, `s 2026(d)(1)(A)`), and answers `NOTHING` where the imported thing is a fact or an approval (vi), `s 2026(l)`, `s 2036a(c)(5)`. The change is one arm before the `OTHERWISE NOTHING` of the branch (`snap6-s2026.l4` line 396) and the test at line 164.
- `s 2026(b)(1)(D)(ii) the waiver is considered approved`, `JUST FALSE` when the Secretary did respond in accordance with clause (i): "If the Secretary does not provide a response" is an "if" (reading (a)). Other reading: `NOTHING`.
- `s 2026(b)(2)(G)`, `s 2026(g)(1)` and `s 2026(j)`: "up to 60 project areas", "up to 3 years" and "up to $4,000,000" are caps phrased positively; they are read as the same as "not more than", a flat negative (reading (a)). Other reading: `NOTHING` above the cap.
- `s 2026(c) the evaluations are made often enough`, `JUST FALSE`: "on an annual or more frequent basis" is read as the text's no to a longer interval (reading (a)). Other reading: `NOTHING`, because no brief word introduces it.
- `s 2026(d)(3) the adult member meets subparagraphs (A) to (E)` and `s 2026(d)(3) the household is eligible to receive cash benefits`, `JUST FALSE`: "if an adult member of the household" meets (A) to (E) is an "if" (reading (a)). Other reading: `NOTHING`.
- `s 2026(d)(2)(A) ...`, `JUST FALSE` when the household is not eligible under paragraph (3): "if the household is eligible under paragraph (3)" is an "if" (reading (a)). Other reading: `NOTHING`.
- `s 2026(f) the Secretary may conduct the pilot project`, `JUST FALSE` when the project is outside the restrictions: "subject to the restrictions imposed by subsection (b)(1) and section 2016(f)(2)" is read as importing those sections' own flat negatives ("may not conduct") (reading (a)). Other reading: "subject to" is not a brief word, so `NOTHING`, as for the "subject to" in `s 2026(l)` below.
- `s 2026(k)(2)(B) the organization is eligible ...`, `JUST FALSE` when no application was submitted: "To be eligible ..., an organization shall submit ... an application" states a necessary step in plain words, which this encoding treats as an "only if" (reading (a)). Other reading: `NOTHING`. Its `NOTHING` when the application was submitted is reading (b): the step is necessary and grants nothing.
- `s 2026(k)(2)(C)(i) the individual is in the low-income target audience`, `NOTHING` above 185 percent: the audience "corresponds to" households at or below 185 percent and the criteria "may include" it, a limit by its own wording (reading (b)).
- `s 2026(l) the participant shall submit the information`, `NOTHING` when the information is protected: "Subject to the requirements of this chapter, including protections under section 2020(e)(8)" is not a brief word, so it yields to that section's answer and does not make the duty `JUST FALSE` (reading (b)).
- `s 2026(n)(1) the State agency may establish a longitudinal database`, `NOTHING` without approval: "on approval by the Secretary" limits the permission by its own wording (reading (b)), as "Subject to the approval of the Secretary" is read in `s 2036a(c)(5)`. Other reading: `JUST FALSE`.
- `s 2026(n)(3) the Secretary has completed the preparations the text requires`, `JUST FALSE` when the Secretary has approved State agencies without completing them: "Prior to the approval of State agencies ..., the Secretary shall" reads as a condition on the approval (reading (a)). Other reading: `NOTHING`, the text names no consequence.
- `s 2026(d)(1)(A) the State may elect to carry out an employment initiatives program`, `JUST FALSE` when fewer than 50 percent of the State's summer 1993 households also received part A benefits: "Subject to the other provisions of this subsection" is read as importing the "only if" of subparagraph (B), whose own words are the no (reading (a)). Other reading: "subject to" is not one of the brief's words, so the answer is `NOTHING`. When the 50 percent is met the function answers `JUST TRUE` (the election is granted in the sentence itself), and `s 2026(d)(1)(B)` answers `NOTHING` (the "only if" bars and grants nothing); (A) takes the two counts and asks (B) itself so that (B)'s `NOTHING` is never read as "not supplied".
- `s 2026(n)(2) the database may be used this way`, `JUST FALSE` for any other use: "shall be used solely to conduct research" closes the list with "solely", which is read as the brief's "only" (reading (a)). Other reading: `NOTHING`, because "solely" is not one of the brief's words.
- Not marginal: `s 2026(b)(1)(B)(i)`, `(b)(1)(B)(iv)`, `(b)(1)(C)`, `(b)(2)(D)`, `(b)(2)(H)`, `(d)(1)(B)` and `(d)(2)(D)(i)` rest on "unless", "only" or "only if". `s 2026(b)(1)(B)(iii)(I)`, `(II)`, `(b)(2)(I)`, `(d)(2)(C)(ii)`, `(i)`, `(k)(2)(D)`, `(n)(4)(B)(i)` and `(n)(8)` rest on flat negatives ("may not", "shall not", "not to exceed", "not more than", "no", "Nothing in this subsection shall").

### s 2031 (Minnesota Family Investment Project)

- `s 2031(b)(3)(C)(iv) the State shall increase the amount of assistance paid to participating families for the sales tax`, `JUST FALSE`: "if the State or locality imposes a sales tax on food" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: `NOTHING`, the text says when the increase is owed and not that it is barred otherwise.
- `s 2031(b)(6)(F) a family may be represented by another person`, `JUST FALSE`: the permission is given "if" the person is designated and is an adult who is sufficiently aware; a failed "if" is the text's no (reading (a)). Other reading: `NOTHING`, representation on other terms is neither granted nor forbidden.
- `s 2031(b)(10)(B)(i) ...`, `JUST FALSE` when the household is not found eligible: "if such families or individuals are determined eligible" (reading (a)). Other reading: `NOTHING`.
- `s 2031(b)(10)(B)(ii) the State shall exclude ...`, `JUST FALSE` when the named provisions are not amended or the person is not affected: "If sections ... are amended" (reading (a)). Other reading: `NOTHING`.
- `s 2031(b)(10)(C) the family or family member has been given the specific request`, `JUST FALSE` when the screening does not indicate potential eligibility: "if the screening indicates potential eligibility" (reading (a)). Other reading: `NOTHING`.
- `s 2031(d)(1)(A) the Secretary shall approve the application`, `JUST FALSE` when the application does not comply: "If an application ... complies ..., then the Secretary shall" (reading (a)). Other reading: `NOTHING`, the duty is stated and a refusal is not.
- `s 2031(c)(1) the State may require the parent ...`, `JUST FALSE` for an exempt parent: "may require ... unless the individual is a parent in a family with one parent who" meets an exemption. "Unless" is one of the words the brief counts, so the exemption is the text's no; but the clause also limits the grant by its own wording, and under reading (b) the exempt parent would be `NOTHING`.
- The time bounds, `JUST FALSE` when late: `s 2031(b)(6)(A)` ("not later than thirty days"), `s 2031(b)(6)(D)` ("on the same day"), `s 2031(b)(10)(C)` ("within five days"), `s 2031(b)(7)(A)` ("no later than benefits would have been provided"). "Not later than" is not one of the words the brief lists; read as a bound the text states as a no to later action (as `s 2034(h)` and `s 2036a(e)` do). Other reading: `NOTHING` for a late act.
- `s 2031(b)(10)(B)(ii) the State shall continue to pay ...`, `JUST FALSE` after the State determines eligibility or the ten days pass: "until" is a word the brief counts.
- `s 2031(b)(6)(A)` to `(G)` (all but (F)(i) and (ii)) and `(b)(7)(A)`, `(b)(7)(B)`, `NOTHING` when selection is made another way: "Whenever selection ... is accomplished through ..." limits the paragraph by its own wording (reading (b)). Other reading: "whenever" is a plain variant of "if", and a failed "if" is `JUST FALSE`.
- `s 2031(b)(10)(C) the State determined eligibility in time`, `NOTHING` when the information was not supplied within ten days: "If the family or family member supplies such additional information within ten days" is an "if", but the function answers whether the State was on time, and a failed "if" means the five days never started (reading (b)). Other reading (a): `JUST FALSE`.
- `s 2031(b)(13) the State has carried out ...`, `NOTHING` when the State does not carry out the Project: "while the State carries out the Project" (reading (b)). Other reading: "while" is a word the brief counts, so `JUST FALSE`.
- `s 2031(c)(2) ...`, `NOTHING` for twenty hours or fewer and for parents it does not name: "shall not require ... more than twenty hours" is a flat negative for more than twenty and bars and grants nothing otherwise (reading (b)).
- `s 2031(c)(3) the assistance to the family may be reduced by the amount`, `NOTHING` when no required individual failed without good cause: "For any period during which" (reading (b)). Other reading (a): `JUST FALSE`.
- `s 2031(e) the Secretary shall waive compliance with the requirement`, `NOTHING` for a requirement in section 2031: "(other than this section)" (reading (b)). Other reading: `JUST FALSE`, the duty does not reach it.
- `s 2031(g)(1)(A)` and `(B)`, `NOTHING` for part A of title IV and this chapter: "other than part A of title IV ... or this chapter" (reading (b)). Other reading: `JUST FALSE`.
- `s 2031(g)(2)(A)` and `(B)`, `NOTHING` at or above the amounts: "Nothing in this section shall allow payments ... to be less than" bars and grants nothing (reading (b)).
- `s 2031(a)(2)`, `(b)(1)`: "only" closes the list and counts, but the functions answer `NOTHING` when the bar is not triggered: "only" grants nothing.
- Every definition in (j) answers `JUST FALSE` for what it does not cover: "means" is a definition, which the brief counts as the text's no.

### s 2033 (repealed)

- None: the section is repealed and has no branch.

### s 2034 (community food projects)

- `s 2034(c) ...`, the `JUST FALSE` branch: "To be eligible for a grant under subsection (b), ... must (1) ... (4)" states necessary conditions in plain words, which this encoding treats as an "only if". Other reading (b): the conditions are what the entity must show but the text does not say "no" to an entity that fails, so the answer would be `NOTHING`.
- `s 2034(a)(1)`, `(a)(2)`, `(a)(3)` `JUST FALSE` branches: each is a definition that says "means"; the brief's rule counts a "means" definition as the text's no.

### s 2035 (simplified program)

- `s 2035(c)(3) ...`, branch `WHEN JUST FALSE THEN JUST FALSE`: "if approved by the Secretary" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: the text only grants eligibility when approved and says nothing about the household that is not approved, so the answer would be `NOTHING`.
- `s 2035(d)(2) ...`, the `JUST FALSE` that an `every one of these holds` gives when the Secretary determined that the plan does not comply or lacks documentation: "The Secretary shall approve ... if the Secretary determines" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: the text says only when approval is owed, not that it is forbidden otherwise, so the answer would be `NOTHING`.
- `s 2035(e)(3)(B) the Secretary shall terminate ...`, branch that answers `JUST FALSE` when the State submitted and carried out the plan: "If the State does not submit a plan ... or carry out a plan" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: `NOTHING`.
- `s 2035(f)(4) ...`, `JUST FALSE` when the Secretary has not made the determination: "may not receive benefits ... unless the Secretary determines" is a prohibition limited by its own "unless". Reading (b) would not count a prohibition limited by its own wording as the text's no, but the "may not" is a flat negative, which reading (a) does count; the branch rests on reading (a).

### s 2036 (commodities for the emergency food assistance program)

- None: no branch of `snap6-s2036.l4` answers `JUST FALSE`, so no branch rests on a failed "if" or on a self-limiting wording counted as a no. Every "not covered" answer is `NOTHING`, with its kind in a comment.

### s 2036a (nutrition education and obesity prevention grant program)

- `s 2036a(a) ...`, the `JUST FALSE` branch: a definition that says "means" (the rule of 2026-10-29 counts it as the text's no).
- `s 2036a(c)(5) ...`, `the administrative control limb`'s `JUST FALSE`: "if the projects ... remain under the administrative control of the State agency" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: the "if" states a condition of the permission and the text does not forbid coordination otherwise, so `NOTHING`.
- `s 2036a(c)(5) ...`, `the approval limb`'s `NOTHING` when the Secretary has not approved: "Subject to the approval of the Secretary" is not one of the words the brief lists as making a failed condition the text's no, so it is a limit on a grant by its own wording (reading (b)). Other reading: "subject to" is a condition like "if", and a missing approval is `JUST FALSE`.
- `s 2036a(d)(2)(B)(i) ...`, the `JUST FALSE` when neither the Secretary's determination nor the State agency's election holds: "If the Secretary determines ... or in the case of a State agency that elects not to receive" is an "if"; a failed "if" counts as the text's no (reading (a)). Other reading: `NOTHING`.
- `s 2036a(d)(2)(B)(ii) ...`, `JUST FALSE` for surrendered funds: "shall not be considered to be part of" is a flat negative, which counts.
- `s 2036a(d)(3)(A) ...`, `JUST FALSE` for any other source: "shall be the only source" closes the list with "only".
- `s 2036a(d)(3)(B) ...`, `JUST FALSE` for costs in excess of the grants: "shall not be eligible for reimbursement" is a flat negative.
- `s 2036a(e) ...`, `JUST FALSE` after 1 January 2012: "Not later than January 1, 2012" is read as a bound the text states as a no to later publication. Other reading: a time bound on a duty is not one of the words the brief lists, so a late publication would be `NOTHING`. The same reading carries the "not later than" branches of `s 2034(h)`, `s 2035(e)(2)` and `s 2035(e)(3)(A)`.


### Reading a result: FALSE and NOTHING (snap6)

Every decision function in these modules answers a `MAYBE BOOLEAN`, a `MAYBE NUMBER` or a `MAYBE DATE`, and a function that always has an answer returns a plain `BOOLEAN`, `NUMBER` or `DATE`.
- **`JUST TRUE`** means the text grants or requires it: for example `s 2026(a)(2) the household may receive the aggregate allotment` is `JUST TRUE` for a household with $20 a month that chooses an allotment of $60 covering 3 months.
- **`JUST FALSE`** means the text says no in its own words, and in these sections that is one of four things: a flat negative ("not more than two State agencies", "shall not receive any other supplemental nutrition assistance program benefits", "shall not be used for any project", "Nothing in this subsection shall be construed to prevent or limit"); a condition the text introduces with "only if", "unless", "only", "solely" or "until" ("shall occur only with the consent of the participant", "unless the Secretary determines"); a failed "if" read clause by clause (reading (a): "if the State so requests", "if an adult member of the household"); or a limit stated as a time bound or a cap ("not later than", "within 40 days", "up to 60 project areas"; marginal readings, listed above).
- **`NOTHING`** means the Act's text in these sections does not answer: the list is not closed ("including, but not limited to", "may include", "such as"); the text is silent about what follows a failed duty (a duty with no consequence in the text answers `NOTHING` when it is not done); a term is undefined ("a sufficient number of demonstration projects"); the answer is another section's ("Subject to the availability of appropriations under section 2027(a)", "including protections under section 2020(e)(8)", the Secretary's determination); or the grant is limited by its own wording and the case falls outside it ("for households whose monthly ... benefits do not exceed $20"). **`NOTHING` is not "no"**: a household member told `NOTHING` should read that these sections do not say, not that the answer is no.
- A bar that grants nothing ("may not conduct a project unless", "may not operate a Program unless the Secretary approves a State plan", "A State shall be eligible ... only if") answers `JUST FALSE` when the condition fails, and `NOTHING`, not `JUST TRUE`, when it is met: lifting the bar is not granting the permission, which is somewhere else (for example `s 2026(b)(1)(B)(i)` and `s 2026(b)(1)(A)`). One flat-negative cap is asked in two forms, and the forms differ inside the limit. A question named for the limit (`s 2034(b)(2) the total provided as grants is within the limit`, `s 2034(e)(1)`, `s 2034(f)(2)`, `s 2031(b)(15)`, `s 2026(a)(2) the number of State agencies permitted is within the limit`, `s 2026(g)(1) ... within the period`, `s 2026(i) ... within the limits`) answers `JUST TRUE` at or below the limit and `JUST FALSE` past it. A question named for the permission (`s 2031(c)(2) the State may require ...`, `s 2026(b)(1)(B)(iii)(I) the project may include ...`, `(iii)(II) the project may continue`, `s 2026(b)(1)(B)(iv) the Secretary may conduct the project`, `s 2026(b)(2)(I) the Secretary may grant a waiver`) answers `NOTHING` inside the limit, because the bar does not grant the permission (the grant is in `s 2031(c)(1)`, `s 2026(b)(1)(A)` and `s 2026(b)(2)(A)` and `(B)`), and `JUST FALSE` past it. The ground is the brief's "limits a grant or prohibition in its own wording ... and the case falls outside the limit", and the name of a function must not claim more than the section says.
- A number that is a `MAYBE NUMBER` answers `NOTHING` when the text states no figure for the case (`s 2036(a)(2)` before 2008, `s 2034(b)(2)` for fiscal years 1997 to 2007, `s 2026(n)(9)` for fiscal years 2020 and 2021).
- A regulative rule is run with `#TRACE`: `FULFILLED` means the party did the act in time; a duty that lapses shows `BREACH` for the party named in `LEST BREACH BY`. The twin decision function says the same in days.
- A caller must never turn `NOTHING` into `FALSE`.

## Seams (snap6)

The seam inputs snap6 took, one per answer another part computes (PLAN.md sections 4 and 6), each a `GIVEN` parameter named for the answering section and typed as the answering function returns it.
The full ASKS and ANSWERS lists, and the seams the plan lacks, are in `SEAMS.md`; the ASKS are:

| input name | type | answering section | asked by |
| --- | --- | --- | --- |
| `s 2016(f)(2) the project is within the restrictions imposed by subsection (b)(1) and section 2016(f)(2)` | MAYBE BOOLEAN | s 2016 | `s 2026(f) the Secretary may conduct the pilot project` (snap6-s2026) |
| `s 2020(e)(3) the household has complied with all applicable verification requirements` | MAYBE BOOLEAN | s 2020 | `s 2026(a)(2) the household may begin to receive combined allotments` (snap6-s2026) |
| `s 2020(e)(8) the information is protected from disclosure` | MAYBE BOOLEAN | s 2020 | `s 2026(l) the participant shall submit the information` (snap6-s2026) |
| `s 2027(a) appropriations are available` | MAYBE BOOLEAN | s 2027 | `s 2026(b)(1)(B)(vi) the project shall be continued` (snap6-s2026) |
| `s 2014 the household is found eligible for the supplemental nutrition assistance program following the standards established under it` | MAYBE BOOLEAN | s 2014 | `s 2031(b)(10)(B)(i) the State shall ensure that benefits under the supplemental nutrition assistance program are provided` (snap6-s2031) |
| `s 2017 the monthly allotment calculated following the standards of the supplemental nutrition assistance program with the maximum excess shelter expense deduction of section 2014(e) applied, in dollars` | MAYBE NUMBER | s 2017 | `s 2031(b)(3)(E)(iv) the individual's monthly allotment, in dollars` (snap6-s2031) |
| `s 2017 the value of the benefits for which the family or individual would have been eligible in the absence of food assistance payments under this clause, from the date of termination from the Project to the date benefits are provided, in dollars` | MAYBE NUMBER | s 2017 | `s 2031(b)(10)(B)(ii) the amount the Secretary shall pay the State, in dollars` (snap6-s2031) |
| `s 2020 the date benefits would have been provided following the standards established under the supplemental nutrition assistance program` | MAYBE DATE | s 2020 | `s 2031(b)(7)(A) the assistance is provided no later than the benefits would have been` (snap6-s2031) |
| `s 2020(e)(9) the household is entitled to expedited service under paragraph (9)` | MAYBE BOOLEAN | s 2020 | `s 2031(b)(6)(C) expedited benefits shall be provided to the family` (snap6-s2031) |
| `s 2025 the amount that otherwise would have been paid under subsections (a), (g), (h)(2) and (h)(3) of section 2025 had the Project not been implemented, as estimated under a methodology satisfactory to the Secretary, in dollars` | MAYBE NUMBER | s 2025 | `s 2031(d)(1)(B)(ii) the payment for administrative costs, in dollars` (snap6-s2031) |
| `s 2016(a) to (f) the State meets the requirements of subsections (a) through (f) of section 2016` | MAYBE BOOLEAN | s 2016 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2017(a) the State meets the requirements of section 2017(a), leaving aside how the household's income was determined` | MAYBE BOOLEAN | s 2017 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2017(b) and (d) the State meets the requirements of subsections (b) and (d) of section 2017` | MAYBE BOOLEAN | s 2017 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2020(a), (c), (d) and (n) the State meets the requirements of those subsections of section 2020` | MAYBE BOOLEAN | s 2020 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2020(e) the State meets the requirements of paragraphs (8), (12), (15), (17), (18), (22) and (23) of section 2020(e)` | MAYBE BOOLEAN | s 2020 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2020(e)(10) the State meets section 2020(e)(10)` | MAYBE BOOLEAN | s 2020 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2025 the State meets the requirements of section 2025` | MAYBE BOOLEAN | s 2025 | `s 2035(f)(3) the State complies with the requirements it shall comply with` (snap6-s2035) |
| `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between June 30, 2008, and June 30 of the immediately preceding fiscal year` | NUMBER | s 2012 | `s 2036(a)(2) the amount the Secretary shall use for the fiscal year, in dollars` (snap6-s2036) |
| `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between June 30, 2008, and June 30, 2022` | NUMBER | s 2012 | `s 2036(a)(2) the amount the Secretary shall use for the fiscal year, in dollars` (snap6-s2036) |
| `s 2012(u)(3) the percentage by which the thrifty food plan was adjusted between June 30, 2023, and June 30 of the immediately preceding fiscal year` | NUMBER | s 2012 | `s 2036(a)(2) the amount the Secretary shall use for the fiscal year, in dollars` (snap6-s2036) |
| `s 2014 the individual is eligible for benefits under this chapter` | MAYBE BOOLEAN | s 2014 | `s 2036a(a) the individual is an eligible individual` (snap6-s2036a) |

## What the text turns out to say

Numbered findings; each ends "Asserted" where a test asserts it.

1. **s 2026(b)(1)(B)(iv)(I) turns on the day: a cash project approved on 21 August 1996 is outside the bar and one approved on 22 August 1996 is within it.** "unless the project was approved prior to August 22, 1996" makes 21 August the last day of the exception; `s 2026(b)(2)(I)` bars new employment and training waivers "on or after August 22, 1996" and reads title IV "as in effect on the day before August 22, 1996", which is 21 August. Asserted in `snap6-tests-s2026.l4` on 21 August, 22 August and 1 January 1990.
2. **s 2026(b)(1)(B)(iii) is a trigger and the two limits under it are bars that grant nothing.** The 15 percent and 5 year limits apply only to a project that would reduce benefits by more than 20 percent for more than 5 percent of the households in the area; below that, `s 2026(b)(1)(B)(iii)(I) ...` and `(II) ...` answer `NOTHING`, and above it `JUST FALSE` only for more than 15 percent or more than 5 years without an extension. Asserted.
3. **s 2026(a)(2) cannot answer `JUST TRUE` for combined allotments.** "no household shall begin to receive combined allotments under this section until it has complied with all applicable verification requirements" bars and grants nothing, so `s 2026(a)(2) the household may begin to receive combined allotments` is `JUST FALSE` or `NOTHING`; the permission is earlier in the paragraph. Asserted.
4. **s 2026(b)(1)(D)(ii) deems approval from silence only if the Secretary gave no response of the kinds in (i).** A response that approves, denies with modification or grounds, or asks for clarification stops the deeming, and any other response does not appear in the list. The function takes whether the Secretary "provided a response in accordance with clause (i)" and answers `JUST TRUE` only when none was. Asserted.
5. **s 2026(h): a vehicle that qualifies under (1) does not use up the one vehicle of (2).** (1) excludes "any" such vehicle, (2) excludes "one" of the rest (FR-26-3). Asserted with an income-producing vehicle and an employment vehicle together (the first is excluded by (1) and the second by (2), so the count is 0).
6. **s 2026(n)(9) states no amount for fiscal years 2020 and 2021, or before 2019.** (A) gives $20,000,000 for 2019 "to remain available through fiscal year 2021" and (B) gives $5,000,000 from 2022, so `s 2026(n)(9) ...` answers `NOTHING` for 2020 and 2021, while `s 2026(n)(9)(A) ...` answers `JUST TRUE` that the 2019 funds remain available in 2019 to 2021. Asserted.
7. **s 2026(n)(7)(A) needs a date the text does not give.** "4 years after the effective date of this subsection" has no date in this text, so the function takes the effective date as an input and answers `NOTHING` without it. Asserted on 20 December 2018 and 29 February 2020 (the due dates are 20 December 2022 and 29 February 2024).
8. **s 2026(k)(4)(B): the due date is 29 December of the fiscal year (FR-26-4).** The fiscal year ends on 30 September and 90 days later is 29 December in every year, because October to December have no leap day. Asserted for 2009 to 2012; the text gives no report for 2008 or earlier.
9. **s 2026(k)(5)(B) makes $20,000,000 available on one named day.** "On October 1, 2008" is the only day for which `s 2026(k)(5)(B) the amount ... on the day` answers a figure; every other day is `NOTHING`. Asserted on 30 September, 1 October and 2 October 2008.
10. **s 2026(m)(4) is 20 December 2021.** "Not later than 3 years after December 20, 2018" is computed by the function over days and asserted. A late report is `JUST FALSE` by marginal reading (a) (the time bound).
11. **s 2031(a)(2) can never answer `JUST TRUE`.** It says the Project "may be implemented only in accordance with this section and only if the Secretary of Health and Human Services approves", which bars and grants nothing; the grant is in (a)(1), and `s 2031(a)(1) ...` takes (a)(2)'s answer as a bar only. Asserted (`TRUE (JUST TRUE)` gives `NOTHING`).
12. **s 2031(b)(3)(E)(iv) gives the same answer in either order of rounding.** The monthly allotment is the higher of $10 and 75 percent of the SNAP amount, rounded down; because $10 is a whole number, rounding first or last agree (FR-31-1). Asserted on 0, 13, 14, 15, 100 and 101 for both functions, and 1000 for the second.
13. **s 2031(c)(1)(E) needs a figure from outside the text.** The exemption for a parent whose hours cannot be verified turns on "the Federal minimum hourly wage rate multiplied by thirty per week", which this text does not give, so `s 2031(c)(1) ...` takes it as an input in dollars (7.25 and 10 are asserted).
14. **s 2031(j)(2) uses "parental caregiver", which (j)(3) does not define.** (j)(3) defines "caregiver" and not "parental"; `s 2031(j)(2) ...` takes whether the person is a parental caregiver as a `MAYBE BOOLEAN` input, and answers `NOTHING` when it is not supplied.
15. **s 2031(b)(14)(A) on 29 February.** A period begun on 29 February 2024 ends on 28 February 2029, because `Date 29 2 2029` is 1 March 2029 on the stable binary (FR-31-4). Asserted.
16. **s 2034(b)(2) states no limit for fiscal years 1997 to 2007.** The function answers `NOTHING` for them. Asserted in `snap6-tests-s2034.l4`.
17. **s 2036(a)(1) names fiscal years 2014 to 2023 while (a)(2) states amounts for 2008, 2009 and 2024 onwards.** The duty to purchase is `NOTHING` outside 2014-2023 and the amounts are stated for every year (FR-36-1). Asserted in `snap6-tests-s2036.l4` (`2013`, `2024`, `2008` answer `NOTHING` for the duty).
18. **s 2036(a)(2)(E) needs two percentages.** The base, "(D)(ix)", is itself the fiscal year 2023 (C) amount plus $35,000,000, so fiscal year 2024 onwards needs the 2008-to-2022 percentage and the 2023-to-preceding-June percentage. Asserted (`10 3` gives 319,300,000).
19. **s 2036a(d)(1)(F) is recursive over ten years.** Each fiscal year's amount needs every earlier year's Consumer Price Index figure, so the function takes the whole list and answers `NOTHING` when a year is missing. Asserted.
20. **The Comptroller General has no party in the core.** (f) puts duties on the Comptroller General, so they are decision functions over facts and a need in NEEDS-CORE.md; they are not regulative rules.
21. **A `MAY` with a `WITHIN` that lapses continues into its `HENCE`.** Probe on `l4-stable-98` and `l4-main-108`: `PARTY the household MAY act WITHIN 10 HENCE r3 LEST FULFILLED` followed by `(WAITUNTIL 12)` prints the residual rule `r3`, not `FULFILLED`. So the household's ten days in (b)(10)(C) are not chained as a `MAY`; the State's duty after the information arrives is its own rule, traced from the day of receipt, and the ten-day condition is in the twin.

## What the stable binary does not accept

The binary governs where the skills describe a construct it rejects. Each of these was met in this encoding.
**Loud** (an error that names the construct):
- `BEFORE <date>` and `AFTER <date>` as a deadline: not accepted. A deadline that is a calendar date is a function over `Date` (for example `s 2026(c) the date by which the progress report for the year is due`).
- A nested `ELSE IF` followed by a second `ELSE`: parse error. `BRANCH` is used.
- A one-line `CONSIDER ... WHEN ... WHEN ...` inside a `WHERE`: parse error. It is written over several lines.
- A `LIST` argument on the line after `CONSIDER`: parse error. The `LIST` is built in a `WHERE` helper.
- A lambda (`\v -> ...`): not accepted. A top-level helper function is used (`s 2026(h)(1) the value of the vehicle is not excluded`).
- A rational literal (`725/100`): not accepted. A decimal (`7.25`) is. A negative number is written `(0 MINUS 1)`.
- `REFUSE` and `#ASSERT REFUSED`: do not exist; "not covered" is `NOTHING` and is asserted.
**Silent** (a wrong answer or a quiet difference, exit code 0):
- **A `MAY` with a `WITHIN` that lapses continues into its `HENCE`**, on the stable build and on the main build: `PARTY the household MAY act WITHIN 10 HENCE r LEST FULFILLED` followed by `(WAITUNTIL 12)` prints the residual rule `r`, not `FULFILLED`. snap6 therefore does not chain a household's steps through a `MAY ... WITHIN`; the timed steps are decision functions over days.
- **A `#TRACE` outcome cannot be asserted** (`#ASSERT <rule> EQUALS FULFILLED` fails, and `check.sh` counts assertion lines and not traces, so a trace that prints the wrong outcome moves no count). Every trace has its expected outcome written in a comment. There are 80 traces (39 in `snap6-tests-s2026.l4`, 19 in `snap6-tests-s2031.l4`, 10 in `snap6-tests-s2036a.l4`, 6 in `snap6-tests-s2035.l4`, 3 each in `snap6-tests-s2034.l4` and `snap6-tests-s2036.l4`); 75 are a party doing the act in time and print `FULFILLED`, and 5 are deliberate breaches and print `DEONTIC BREACHED: BREACH BY ...` (`snap6-tests-s2031.l4` lines 655, 662 and 689 for the State agency; `snap6-tests-s2035.l4` lines 171 and 183 for the Secretary), each as its comment says. Each tests file was run on the stable build and on the main build 1.6.108 and the trace outcomes compared: identical for all six, which `check.sh` does not do.
- `Date 29 2 2029` is 1 March 2029 (`Date` rolls an impossible date forward), so a period begun on 29 February 2024 ends on 28 February 2029 (FR-31-4).

## What the text does not answer

- What happens to a duty not done: no section of snap6's ranges gives a consequence for the Secretary's late report, a State's late plan or a missing evaluation except where it says so (s 2035(e)(3)(B) terminates approval; s 2031(b)(10)(B)(ii) keeps food assistance paid); a late or missed duty is `JUST FALSE` where the text sets a time and `NOTHING` where it does not.
- Which body is "the State" (FR-26-1, FR-31-5, FR-35-1), who is the Administrator (FR-36a-2), and what "promptly" (s 2031(b)(6)(A)) and "a sufficient number" (s 2026(h)) mean.
- The amount a grant, a payment or a threshold takes where the Act leaves it to the Secretary: `s 2026(n)(6)(B)` (the amount of a grant), `s 2031(c)(1)` (the Federal minimum hourly wage rate), `s 2036(a)(2)` (the thrifty food plan percentages).
- The effective date of s 2026(n) ("4 years after the effective date of this subsection"): not in this text.
- The percentages the text leaves to published figures (the thrifty food plan adjustment of s 2012(u)(3) in s 2036(a)(2); the Consumer Price Index in s 2036a(d)(1)): they are inputs, and the function answers `NOTHING` when one is missing.

## What would need doing before this encoding is worth relying on

- A lawyer's ruling on the two marginal readings, branch by branch (the list above).
- Checking each quoted passage against the official text of the Code, not the converter's rendering.
- Wiring the seam inputs to the other parts' answers at the merge (`SEAMS.md`) and hoisting the constructors in `NEEDS-CORE.md`.
- A second seat over the same modules for a State agency (`snap6-seat-state-agency.l4`), if the State agency's duties in s 2026, s 2031, s 2035 and s 2036a are wanted from its side.

## What check.sh prints

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
snap-core.l4                                   0         0       0        0         0 |      0         0       0        0  same
snap6-cases-seat.l4                            0       123       0        0         0 |      0       123       0        0  same
snap6-s2026.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2031.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2034.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2035.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2036.l4                                 0         0       0        0         0 |      0         0       0        0  same
snap6-s2036a.l4                                0         0       0        0         0 |      0         0       0        0  same
snap6-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
snap6-tests-s2026.l4                           0       575       0        0         0 |      0       575       0        0  same
snap6-tests-s2031.l4                           0       478       0        0         0 |      0       478       0        0  same
snap6-tests-s2034.l4                           0       123       0        0         0 |      0       123       0        0  same
snap6-tests-s2035.l4                           0        96       0        0         0 |      0        96       0        0  same
snap6-tests-s2036.l4                           0        66       0        0         0 |      0        66       0        0  same
snap6-tests-s2036a.l4                          0       167       0        0         0 |      0       167       0        0  same
TOTAL (15 modules)                             0      1628       0        0           |      0      1628       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit=0
```
