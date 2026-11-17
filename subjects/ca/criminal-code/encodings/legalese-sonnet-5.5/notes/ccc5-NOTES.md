# NOTES (ccc5) -- the Criminal Code (Canada), R.S.C., 1985, c. C-46, lines 2382-2989: Part III from section 110.4 to section 117.15, and Part IV (sections 118 to 149)

Status (2026-11-13, part agent `ccc5`, model Sonnet 5.5): written and checked by the agent; no lawyer has read it against the text.
Every claim about what the text says was read from the plain-text rendering in `inputs/` while writing; every claim about the encoding was checked by running it (numbers below come from `check.sh` and `srcrefs.py`).

## What is encoded, and what is not

Lines 2382-2989 hold 408 units (sections, subsections, paragraphs, subparagraphs, the six defined terms of section 118, group headings and repealed lines): sections 110.4 to 117.15 (the second half of Part III) and all of Part IV (sections 118 to 149).
Everything in those lines is encoded as layer-1 L4 except the heading rows, the lead-in of section 118 and the regulation-making power of section 117.15(1) and (2) (see Coverage).
Layer 1 is seven modules and seven test files, one per run of the text; layer 2 is `ccc5-seat.l4` and `ccc5-cases-seat.l4`.
Nothing here depends on any other part: every answer from another part or from section 2 is an input (see Seams).

## Seat

The seat is the one the brief fixes: **a person who is, or may be, accused of an offence under the Criminal Code (the accused), asking, on facts they can state, whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply at each stage from arrest through trial, sentence and appeal, and what follows from a conviction.**
(Assumed, not ruled: Singapore's Penal Code is the model, as the maintainer instructed on 2026-11-09, but this is a plain seat layer with no charge-generator contract.)
In this range the seat meets two kinds of provision.
The Part III provisions are procedures that a judge, a justice or a peace officer carries out on a person: an application for a prohibition order, a search, a seizure, a surrender, a forfeiture.
They are encoded for what they decide about the person (the notice the person must be given, the order the person may face, the period of it, the right to appeal, the right to the return of a thing), and the seat asks those questions in the first person ("Under section 111(5), is the provincial court judge bound to make an order prohibiting me ...").
The Part IV provisions are offences, and the seat asks, for each, whether the person's facts make it out, whether it is indictable, summary or both, and the greatest imprisonment on indictment.
There is no seat for an official: a judge, a justice, an officer or a minister appears only as the party whose duty or power the person is told about.

## How the encoding was built, and where this brief departs from `inputs/PLAN.md`

- The text is the plain-text rendering, made by a converter script, of the Justice Laws Website consolidation current to 2026-09-30 (`inputs/SOURCES.md`). It is not the official text, and nothing here is claimed to be verified against the official text. The French version is equally authoritative and was not among the sources.
- Every quotation (`-- src:N | text` lines) was produced by `srcrefs.py quote` from the raw file by script, never typed; `srcrefs.py check --strict` reports 0 problems on every file (numbers below).
- The L4 was generated from compact specifications (a rule generator written for this run, kept outside the deposit in `../../../work/`), so every limb of every offence has the same shape: one function over BOOLEAN facts, `JUST TRUE` when every element is present, the exceptions first as `JUST FALSE`, and `NOTHING` otherwise. Tests were generated from the same specifications: for each rule, every element present; each element missing in turn; each alternative alone; each exception; each "whether or not" fact both ways. The expected values come from the specification (the reading of the text), not from running the code; a failing assertion would have been a finding.
- Hand-written L4 covers what the generator cannot: periods and dates (ss 110.4(3) and (4), 111(5), 117.0101(3), 117.0102(2) and (3), 117.03(2), 117.05(1), 117.06(1)(a)), lists by section number (ss 111(7), 117.05(6), 117.11), the Part XXVII appeal rule, the definitions of section 118 that are lists, the remedy of section 117, and four regulative rules.
- Where `inputs/PLAN.md` and the brief differ, the brief governs: (1) the brief says layer 1 imports `ccc-definitions.l4`; this part does not, because every `s 2` function there takes a capacity enum (a `s 2 peace officer capacity`), not a fact a person can state, so the section 2 answers are inputs typed `MAYBE BOOLEAN` named `s 2 <term>: ...` as PLAN section 4 says; (2) the PLAN says a part gets only the core, the brief says the definitions module is also in the folder; (3) PLAN section 8 (the seams list the brief cites) is not in this copy of the plan, so the seams below are those of sections 3, 4 and 6.
- The keel's three modules sit in the folder unchanged and are not edited. `ccc-definitions.l4` and `ccc-interpretation.l4` are present and checked by `check.sh` but not imported by any `ccc5-` file.

## Answer table: the classes and the stated maxima in the range

Each cell is a function of layer 1 whose `@ref` quotes the provision. "Indictable" means the section says "guilty of an indictable offence"; "both" means the section gives an indictable limb and a summary-conviction limb (and no penalty for the summary limb, which `s 787(1)` supplies and is an input here).

| function | class of the offence |
| --- | --- |
| `s 117.01(3) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 119(1) the class of the offence` | an indictable offence |
| `s 120 the class of the offence` | an indictable offence |
| `s 121(3) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 121.1(4) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 122 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 123(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 123(2) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 124 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 125 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 126(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 127(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 128 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 129 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 130(2) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 132 the class of the offence` | an indictable offence |
| `s 134(1) the class of the offence` | an offence punishable on summary conviction |
| `s 136(1) the class of the offence` | an indictable offence |
| `s 137 the class of the offence` | an indictable offence |
| `s 138 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 139(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 139(2) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 140(2) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 141(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 142 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 144 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 145(1) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 145(2) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 145(3) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 145(4) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 145(5) the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 146 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 147 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |
| `s 148 the class of the offence` | an offence that the section makes both indictable and punishable on summary conviction |

| function | greatest imprisonment on indictment |
| --- | --- |
| `s 117.01(3)(a) the punishment on indictment` | ten years |
| `s 119(1) the punishment on indictment` | fourteen years |
| `s 120 the punishment on indictment` | fourteen years |
| `s 121(3)(a) the punishment on indictment` | five years |
| `s 121.1(4)(a) the punishment on indictment` | five years |
| `s 122(a) the punishment on indictment` | five years |
| `s 123(1) the punishment on indictment` | five years |
| `s 123(2) the punishment on indictment` | five years |
| `s 124 the punishment on indictment` | five years |
| `s 125 the punishment on indictment` | five years |
| `s 126(1)(a) the punishment on indictment` | two years |
| `s 127(1)(a) the punishment on indictment` | two years |
| `s 128 the punishment on indictment` | two years |
| `s 129(d) the punishment on indictment` | two years |
| `s 130(2)(a) the punishment on indictment` | five years |
| `s 132 the punishment on indictment` | fourteen years |
| `s 136(1) the punishment on indictment` | fourteen years |
| `s 137 the punishment on indictment` | fourteen years |
| `s 138 the punishment on indictment` | two years |
| `s 139(1)(c) the punishment on indictment` | two years |
| `s 139(2)(a) the punishment on indictment` | ten years |
| `s 140(2)(a) the punishment on indictment` | five years |
| `s 141(1)(a) the punishment on indictment` | two years |
| `s 142(a) the punishment on indictment` | five years |
| `s 144 the punishment on indictment` | ten years |
| `s 145(1)(a) the punishment on indictment` | two years |
| `s 145(2) the punishment on indictment` | two years |
| `s 145(3)(a) the punishment on indictment` | two years |
| `s 145(4) the punishment on indictment` | two years |
| `s 145(5) the punishment on indictment` | two years |
| `s 146 the punishment on indictment` | two years |
| `s 147 the punishment on indictment` | five years |
| `s 148 the punishment on indictment` | five years |

Section 134(1) states only a summary-conviction limb, and its function takes `s 787(1) the general penalty ...` as the whole penalty.

## Coverage (ccc5)

Audit: the table was built once, by script (`work/units.py`), from lines 2382-2989 of `R.S.C.-1985-c.-C-46.txt`: **408 rows** before and **408 rows** after (no row was added, removed or merged by hand). The script checks that every one of the **598 non-blank lines** of the range falls in exactly one row (0 lines missing, 0 doubly covered). A marginal note (the italic heading line before a provision) belongs to the row of the provision it heads; flush-out text after a list belongs to the row of the last paragraph.

Dispositions: **encoded** 228; **fork** 159; **inert** 12; **repealed or blank in this text** 9. Total 408.
There is no `out-of-scope` and no `deferred` row. A `fork` row is encoded too: it points at the fork-register entry that records the reading taken.

| unit | lines | kind | disposition | L4 name |
| --- | --- | --- | --- | --- |
| s 110.4(1) | 2382-2383 | subsection | fork (FA-1) | `s 110.4(1) the provincial court judge may fix a date for the hearing of an application under subsection 111(1)`; `s 110.4(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` |
| s 110.4(2) | 2384-2385 | subsection | encoded | `s 110.4(2)(a) the application for the order under subsection 110.1(3) is deemed an application made under subsection 111(1)` |
| s 110.4(2)(a) | 2386 | paragraph | encoded | `s 110.4(2)(a) the application for the order under subsection 110.1(3) is deemed an application made under subsection 111(1)` |
| s 110.4(2)(b) | 2387 | paragraph | fork (FM-19) | `s 110.4(2)(b) the Attorney General who becomes the applicant` |
| s 110.4(3) | 2388-2389 | subsection | fork (FA-2) | `s 110.4(3) the date fixed for the hearing is before the end of the period of the order`; `s 110.4(3) the provincial court judge may adjourn the hearing` |
| s 110.4(4) | 2390-2391 | subsection | fork (FM-5) | `s 110.4(4) the provincial court judge is bound to cause notice to be served on the Attorney General`; `s 110.4(4) the notice was served not later than 15 days before the date fixed`; `s 110.4(4) the judge must cause notice to be served on the Attorney General`; `s 110.4(4) cause notice to be served on the Attorney General`; `s 110.4(4) act` |
| s 110.4(5) | 2392-2393 | subsection | encoded | `s 110.4(5) the provincial court judge is bound to cancel the hearing` |
| s 111(1) | 2394-2395 | subsection | fork (FA-3) | `s 111(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order prohibiting a person from possessing weapons` |
| s 111(2) | 2396-2397 | subsection | encoded | `s 111(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` |
| s 111(3) | 2398-2399 | subsection | fork (FM-4) | `s 111(3) the provincial court judge is bound to hear all relevant evidence presented by or on behalf of the applicant and the person` |
| s 111(4) | 2400-2401 | subsection | fork (FA-4) | `s 111(4) the provincial court judge may proceed ex parte to hear and determine the application` |
| s 111(5) | 2402-2403 | subsection | fork (FM-2) | `s 111(5) the provincial court judge is bound to make an order prohibiting the person from possessing the things`; `s 111(5) the period of the order is not more than five years`; `s 111(5) the order begins on the day on which it is made` |
| s 111(6) | 2404-2405 | subsection | encoded | `s 111(6) the provincial court judge is bound to include a statement of reasons in the record` |
| s 111(7) | 2406-2407 | subsection | encoded | `s 111(7) sections 113 to 117 apply to the order, tested by section number` |
| s 111(8) | 2408-2409 | subsection | fork (FA-5) | `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` |
| s 111(9) | 2410-2411 | subsection | fork (FA-6) | `s 111(9) the Attorney General may appeal to the superior court against the decision not to make an order` |
| s 111(10) | 2412-2413 | subsection | fork (FM-21) | `s 111(10) the provision of Part XXVII applies to the appeal` |
| s 111(11) | 2414 | repealed | repealed or blank in this text | the text shows: "(11) [Repealed, 2023, c. 32, s. 5]" |
| s 112 | 2415-2416 | section | fork (FA-7) | `s 112 a provincial court judge may revoke the order` |
| s 113(1) | 2417-2418 | subsection | fork (FA-8) | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` |
| s 113(1)(a) | 2419 | paragraph | fork (FA-8) | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` |
| s 113(1)(b) | 2420-2421 | paragraph | fork (FA-8) | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` |
| s 113(2) | 2422-2423 | subsection | encoded | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| s 113(2)(a) | 2424 | paragraph | encoded | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| s 113(2)(b) | 2425 | paragraph | encoded | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| s 113(2)(c) | 2426 | paragraph | encoded | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| s 113(3) | 2427-2428 | subsection | fork (FA-9) | `s 113(3)(a) an authorization, licence or registration certificate is barred from being denied solely on the basis of the prohibition order or the offence` |
| s 113(3)(a) | 2429 | paragraph | fork (FA-9) | `s 113(3)(a) an authorization, licence or registration certificate is barred from being denied solely on the basis of the prohibition order or the offence` |
| s 113(3)(b) | 2430 | paragraph | fork (FA-10) | `s 113(3)(b) the authorization or licence may be issued to the person for the duration of the order`; `s 113(3)(b) the chief firearms officer may attach further terms and conditions to the authorization or licence` |
| s 113(4) | 2431-2432 | subsection | fork (FA-12) | `s 113(4) an order under subsection (1) may be made during the proceedings` |
| s 113(5) | 2433-2434 | subsection | encoded | `s 113(5) competent authority` |
| s 114 | 2435-2436 | section | fork (FA-13) | `s 114 the competent authority may require the person to surrender the things and documents`; `s 114 the authority is bound to specify in the order a reasonable period for surrendering`; `s 114 section 117.01 does not apply to the person during the specified period` |
| s 114(a) | 2437 | paragraph | fork (FA-13) | `s 114 the competent authority may require the person to surrender the things and documents` |
| s 114(b) | 2438-2439 | paragraph | fork (FA-13) | `s 114 the competent authority may require the person to surrender the things and documents` |
| s 115(1) | 2440-2441 | subsection | encoded | `s 115(1) the thing is forfeited to Her Majesty` |
| s 115(1.1) | 2442-2443 | subsection | encoded | `s 115(1.1) subsection (1) does not apply to the order` |
| s 115(2) | 2444-2445 | subsection | encoded | `s 115(2) the thing forfeited is to be disposed of or otherwise dealt with as the Attorney General directs` |
| s 116(1) | 2446-2447 | subsection | encoded | `s 116(1) the authorization, licence or registration certificate is revoked or amended on the commencement of the prohibition order` |
| s 116(2) | 2448-2449 | subsection | encoded | `s 116(2) the authorization, licence or registration certificate remains revoked or amended` |
| s 117 | 2450-2451 | section | encoded | `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid`; `s 117 what the order for the owner is`; `s 117 state of the thing`; `s 117 order for the owner`; `s 117 the thing still exists`; `s 117 the thing was sold`; `s 117 the thing was destroyed`; `s 117 the thing is returned to the owner`; `s 117 the proceeds of the sale are paid to the owner`; `s 117 an amount equal to the value of the thing is paid to the owner` |
| s 117(a) | 2452 | paragraph | encoded | `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid` |
| s 117(b) | 2453-2454 | paragraph | encoded | `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid` |
| s 117.01(1) | 2455-2456 | subsection | encoded | `s 117.01(1) the person possesses a prohibited thing while prohibited from doing so by an order` |
| s 117.01(2) | 2457-2458 | subsection | encoded | `s 117.01(2) the person wilfully fails to surrender an authorization, licence or registration certificate when required by an order` |
| s 117.01(3) | 2459-2460 | subsection | fork (FM-12) | `s 117.01(3) the person who commits an offence under subsection (1) or (2) is guilty of an offence`; `s 117.01(3) the class of the offence` |
| s 117.01(3)(a) | 2461 | paragraph | encoded | `s 117.01(3)(a) the punishment on indictment` |
| s 117.01(3)(b) | 2462 | paragraph | encoded | `s 117.01(3)(b) the punishment on summary conviction` |
| s 117.01(4) | 2463-2464 | subsection | encoded | `s 117.01(4) subsection (1) does not apply to a person who possessed a firearm in accordance with an authorization or licence issued as a result of an order under subsection 113(1)` |
| Limitations on Access | 2466 | heading | inert (reason 1: heading) | Limitations on Access |
| s 117.0101(1) | 2467-2468 | subsection | fork (FA-17) | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` |
| s 117.0101(1)(a) | 2469 | paragraph | fork (FA-17) | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` |
| s 117.0101(1)(b) | 2470 | paragraph | fork (FA-17) | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` |
| s 117.0101(2) | 2471-2472 | subsection | fork (FA-18) | `s 117.0101(2) the provincial court judge may hold the hearing in private` |
| s 117.0101(3) | 2473-2474 | subsection | fork (FM-3) | `s 117.0101(3) the provincial court judge is bound to make an emergency limitations on access order`; `s 117.0101(3) the period of the order is not more than 30 days`; `s 117.0101(3) the order begins on the day on which it is made` |
| s 117.0101(4) | 2475-2476 | subsection | encoded | `s 117.0101(4) a copy of the order is to be served on the person to whom it is addressed` |
| s 117.0101(5) | 2477-2478 | subsection | encoded | `s 117.0101(5) the provincial court judge is bound to impose terms and conditions that are the least intrusive possible` |
| s 117.0101(6) | 2479-2480 | subsection | fork (FA-19) | `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` |
| s 117.0101(7) | 2481-2482 | subsection | fork (FA-20) | `s 117.0101(7) the peace officer may search for and seize without a warrant` |
| s 117.0101(8) | 2483-2484 | subsection | encoded | `s 117.0101(8) the peace officer is bound to make a report immediately to a justice having jurisdiction`; `s 117.0101(8) the report shows what the subsection requires` |
| s 117.0101(8)(a) | 2485 | paragraph | encoded | `s 117.0101(8) the report shows what the subsection requires` |
| s 117.0101(8)(b) | 2486 | paragraph | encoded | `s 117.0101(8) the report shows what the subsection requires` |
| s 117.0101(9) | 2487-2488 | subsection | fork (FA-21) | `s 117.0101(9) the provincial court judge may require the person to surrender the things`; `s 117.0101(9) the judge is bound to specify in the order a reasonable period for surrendering the thing` |
| s 117.0101(10) | 2489-2490 | subsection | encoded | `s 117.0101(10) the judge may issue the warrant or include the requirement to surrender` |
| s 117.0101(11) | 2491-2492 | subsection | fork (FA-22) | `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` |
| s 117.0101(12) | 2493-2494 | subsection | encoded | `s 117.0101(12) the things are to be returned to the person` |
| s 117.0101(12)(a) | 2495 | paragraph | encoded | `s 117.0101(12) the things are to be returned to the person` |
| s 117.0101(12)(b) | 2496 | paragraph | encoded | `s 117.0101(12) the things are to be returned to the person` |
| s 117.0102(1) | 2497-2498 | subsection | fork (FA-23) | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 117.0102(1)(a) | 2499 | paragraph | fork (FA-23) | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 117.0102(1)(b) | 2500 | paragraph | fork (FA-23) | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 117.0102(1)(c) | 2501 | paragraph | fork (FA-23) | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 117.0102(1)(d) | 2502 | paragraph | fork (FA-23) | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 117.0102(2) | 2503-2504 | subsection | fork (FM-24) | `s 117.0102(2) the order made under subsection (1) expires on the day in question`; `s 117.0102(3) the day on which the order made under subsection (1) ceases to have effect` |
| s 117.0102(3) | 2505-2506 | subsection | fork (FM-24) | `s 117.0102(2) the order made under subsection (1) expires on the day in question`; `s 117.0102(3) the day on which the order made under subsection (1) ceases to have effect` |
| s 117.0102(3)(a) | 2507 | paragraph | encoded | `s 117.0102(2) the order made under subsection (1) expires on the day in question`; `s 117.0102(3) the day on which the order made under subsection (1) ceases to have effect` |
| s 117.0102(3)(b) | 2508 | paragraph | encoded | `s 117.0102(2) the order made under subsection (1) expires on the day in question`; `s 117.0102(3) the day on which the order made under subsection (1) ceases to have effect` |
| s 117.0102(4) | 2509-2510 | subsection | encoded | `s 117.0102(4) the documents are to be placed in a packet and sealed by the judge` |
| s 117.0102(5) | 2511-2512 | subsection | fork (FA-24) | `s 117.0102(5) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` |
| s 117.0103(1) | 2513-2514 | subsection | fork (FA-25) | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` |
| s 117.0103(1)(a) | 2515 | paragraph | fork (FA-25) | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` |
| s 117.0103(1)(b) | 2516 | paragraph | fork (FA-25) | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` |
| s 117.0103(1)(c) | 2517 | paragraph | fork (FA-25) | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` |
| s 117.0103(2) | 2518-2519 | subsection | fork (FA-26) | `s 117.0103(2) the order may be for any period, definite or indefinite, that the judge considers necessary` |
| s 117.0103(3) | 2520-2521 | subsection | encoded | `s 117.0103(3) the originals of the documents are to be placed in a packet and sealed by the judge` |
| s 117.0103(4) | 2522-2523 | subsection | fork (FA-27) | `s 117.0103(4) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` |
| s 117.0103(5) | 2524-2525 | subsection | encoded | `s 117.0103(5) any order made under this section that is still in force applies in respect of the hearing` |
| s 117.0104(1) | 2526-2527 | subsection | fork (FA-28) | `s 117.0104(1) the provincial court judge may fix a date for the hearing of an application under subsection 117.011(1)`; `s 117.0104(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` |
| s 117.0104(2) | 2528-2529 | subsection | encoded | `s 117.0104(2)(a) the application for the order under subsection 117.0101(3) is deemed an application made under subsection 117.011(1)` |
| s 117.0104(2)(a) | 2530 | paragraph | encoded | `s 117.0104(2)(a) the application for the order under subsection 117.0101(3) is deemed an application made under subsection 117.011(1)` |
| s 117.0104(2)(b) | 2531 | paragraph | fork (FM-19) | `s 117.0104(2)(b) the Attorney General who becomes the applicant` |
| s 117.0104(3) | 2532-2533 | subsection | fork (FA-29) | `s 117.0104(3) the date fixed for the hearing is before the end of the period of the order`; `s 117.0104(3) the provincial court judge may adjourn the hearing` |
| s 117.0104(4) | 2534-2535 | subsection | fork (FM-5) | `s 117.0104(4) the provincial court judge is bound to cause notice to be served on the Attorney General`; `s 117.0104(4) the notice was served not later than 15 days before the date fixed`; `s 117.0104(4) the judge must cause notice to be served on the Attorney General`; `s 117.0104(4) cause notice to be served on the Attorney General`; `s 117.0104(4) act` |
| s 117.0104(5) | 2536-2537 | subsection | encoded | `s 117.0104(5) the provincial court judge is bound to cancel the hearing` |
| s 117.011(1) | 2538-2539 | subsection | fork (FA-30) | `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` |
| s 117.011(1)(a) | 2540 | paragraph | fork (FA-30) | `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` |
| s 117.011(1)(b) | 2541 | paragraph | fork (FA-30) | `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` |
| s 117.011(2) | 2542-2543 | subsection | encoded | `s 117.011(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` |
| s 117.011(3) | 2544-2545 | subsection | fork (FM-4) | `s 117.011(3) the provincial court judge is bound to hear all relevant evidence presented by or on behalf of the applicant and the person` |
| s 117.011(4) | 2546-2547 | subsection | fork (FA-31) | `s 117.011(4) the provincial court judge may proceed ex parte to hear and determine the application` |
| s 117.011(5) | 2548-2549 | subsection | encoded | `s 117.011(5) the provincial court judge is bound to make an order imposing terms and conditions on the person's use and possession` |
| s 117.011(6) | 2550-2551 | subsection | encoded | `s 117.011(6) the provincial court judge is bound to impose terms and conditions that are the least intrusive possible` |
| s 117.011(7) | 2552-2553 | subsection | fork (FA-32) | `s 117.011(7) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` |
| s 117.011(8) | 2554-2555 | subsection | fork (FA-33) | `s 117.011(8) the Attorney General may appeal to the superior court against the decision not to make an order` |
| s 117.011(9) | 2556-2557 | subsection | fork (FM-21) | `s 117.011(9) the provision of Part XXVII applies to the appeal` |
| s 117.012 | 2558-2559 | section | fork (FA-34) | `s 117.012 a provincial court judge may revoke the order` |
| Search and Seizure | 2561 | heading | inert (reason 1: heading) | Search and Seizure |
| s 117.02(1) | 2562-2563 | subsection | fork (FA-35) | `s 117.02(1) the peace officer may search without a warrant and seize` |
| s 117.02(1)(a) | 2564 | paragraph | fork (FA-35) | `s 117.02(1) the peace officer may search without a warrant and seize` |
| s 117.02(1)(b) | 2565-2566 | paragraph | fork (FA-35) | `s 117.02(1) the peace officer may search without a warrant and seize` |
| s 117.02(2) | 2567-2568 | subsection | encoded | `s 117.02(2) the thing seized is to be dealt with in accordance with sections 490 and 491` |
| s 117.03(1) | 2569-2570 | subsection | fork (FA-36) | `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` |
| s 117.03(1)(a) | 2571 | paragraph | fork (FA-36) | `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` |
| s 117.03(1)(b) | 2572-2573 | paragraph | fork (FA-36) | `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` |
| s 117.03(2) | 2574-2575 | subsection | fork (FM-6) | `s 117.03(2) the thing is to be returned without delay`; `s 117.03(2) the claim is made within 14 days after the seizure`; `s 117.03(2) act`; `s 117.03(2) claim the thing and produce the licence`; `s 117.03(2) return the thing to the person`; `s 117.03(2) the person may claim the thing within 14 days and the officer must then return it` |
| s 117.03(2)(a) | 2576 | paragraph | encoded | `s 117.03(2) the thing is to be returned without delay` |
| s 117.03(2)(b) | 2577-2578 | paragraph | encoded | `s 117.03(2) the thing is to be returned without delay` |
| s 117.03(3) | 2579-2580 | subsection | fork (FA-37) | `s 117.03(3) the peace officer is bound to take the thing forthwith before a provincial court judge`; `s 117.03(3) the provincial court judge may declare the thing forfeited to Her Majesty` |
| s 117.04(1) | 2581-2582 | subsection | fork (FA-38) | `s 117.04(1) the justice may issue a warrant authorizing a peace officer to search the building, receptacle or place and seize` |
| s 117.04(2) | 2583-2584 | subsection | fork (FA-39) | `s 117.04(2) the peace officer may search for and seize without a warrant` |
| s 117.04(3) | 2585-2586 | subsection | encoded | `s 117.04(3) the peace officer is bound to make a report immediately to a justice having jurisdiction`; `s 117.04(3) the report shows what the subsection requires` |
| s 117.04(3)(a) | 2587 | paragraph | encoded | `s 117.04(3) the report shows what the subsection requires` |
| s 117.04(3)(b) | 2588 | paragraph | encoded | `s 117.04(3) the report shows what the subsection requires` |
| s 117.04(4) | 2589-2590 | subsection | encoded | `s 117.04(4) every authorization, licence and registration certificate held by the person is revoked as at the time of the seizure` |
| s 117.05(1) | 2591-2592 | subsection | fork (FM-7) | `s 117.05(1) the justice is bound to fix a date for the hearing and direct that notice of it be given`; `s 117.05(1) the application is made within 30 days after the execution or the seizure`; `s 117.05(1) act`; `s 117.05(1) apply for an order for the disposition of the thing or document`; `s 117.05(1) fix a date for the hearing and direct that notice be given`; `s 117.05(1) the peace officer may apply within 30 days and the justice must then fix a date for the hearing` |
| s 117.05(2) | 2593-2594 | subsection | fork (FA-40) | `s 117.05(2) the justice may proceed ex parte to hear and determine the application` |
| s 117.05(3) | 2595-2596 | subsection | encoded | `s 117.05(3) the justice is bound to hear all relevant evidence, including evidence respecting the value of the thing` |
| s 117.05(4) | 2597-2598 | subsection | encoded | `s 117.05(4)(a) the justice is bound to order that any thing seized be forfeited to Her Majesty or otherwise disposed of` |
| s 117.05(4)(a) | 2599 | paragraph | encoded | `s 117.05(4)(a) the justice is bound to order that any thing seized be forfeited to Her Majesty or otherwise disposed of` |
| s 117.05(4)(b) | 2600 | paragraph | fork (FM-2) | `s 117.05(4)(b) the justice is bound to order that the person's possession be prohibited`; `s 117.05(4)(b) the period of the order is not more than five years`; `s 117.05(4)(b) the order begins on the day on which it is made` |
| s 117.05(5) | 2601-2602 | subsection | encoded | `s 117.05(5) the justice is bound to include a statement of reasons in the record` |
| s 117.05(6) | 2603-2604 | subsection | encoded | `s 117.05(6) sections 113 to 117 apply to the order, tested by section number` |
| s 117.05(7) | 2605-2606 | subsection | fork (FA-41) | `s 117.05(7) the person may appeal to the superior court against the order` |
| s 117.05(8) | 2607-2608 | subsection | fork (FA-42) | `s 117.05(8) the Attorney General may appeal to the superior court against the failure to make the finding or the order` |
| s 117.05(9) | 2609-2610 | subsection | fork (FM-21) | `s 117.05(9) the provision of Part XXVII applies to the appeal` |
| s 117.06(1) | 2611-2612 | subsection | fork (FM-7) | `s 117.06(1) the thing or document is to be returned to the person from whom it was seized` |
| s 117.06(1)(a) | 2613 | paragraph | encoded | `s 117.06(1) the thing or document is to be returned to the person from whom it was seized`; `s 117.06(1)(a) no application was made within thirty days` |
| s 117.06(1)(b) | 2614 | paragraph | encoded | `s 117.06(1) the thing or document is to be returned to the person from whom it was seized` |
| s 117.06(2) | 2615-2616 | subsection | fork (FA-43) | `s 117.06(2) the justice may order that the revocation be reversed and the authorization, licence or registration certificate restored` |
| Exempted Persons | 2618 | heading | inert (reason 1: heading) | Exempted Persons |
| s 117.07(1) | 2619-2620 | subsection | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(a) | 2621 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(b) | 2622 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(c) | 2623 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(d) | 2624 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(e) | 2625 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(f) | 2626 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(1)(g) | 2627 | paragraph | fork (FA-44) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.07(2) | 2628-2629 | subsection | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(a) | 2630 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(b) | 2631 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(c) | 2632 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(d) | 2633 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(e) | 2634 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(e)(i) | 2635 | subparagraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(e)(ii) | 2636 | subparagraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(f) | 2637 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(g) | 2638 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(h) | 2639 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(i) | 2640 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.07(2)(j) | 2641 | paragraph | encoded | `s 117.07(2) public officer` |
| s 117.071 | 2642-2643 | section | fork (FA-45) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.071(a) | 2644 | paragraph | fork (FA-45) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.071(b) | 2645 | paragraph | fork (FA-45) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.071(c) | 2646 | paragraph | fork (FA-45) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.071(d) | 2647 | paragraph | fork (FA-45) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.08 | 2648-2649 | section | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(a) | 2650 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(b) | 2651 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(c) | 2652 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(d) | 2653 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(e) | 2654 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(f) | 2655 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.08(g) | 2656-2657 | paragraph | fork (FA-46) | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| s 117.09(1) | 2658-2659 | subsection | fork (FA-47) | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| s 117.09(1)(a) | 2660 | paragraph | fork (FA-47) | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| s 117.09(1)(b) | 2661 | paragraph | fork (FA-47) | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| s 117.09(1)(c) | 2662 | paragraph | fork (FA-47) | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| s 117.09(1)(d) | 2663 | paragraph | fork (FA-47) | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| s 117.09(2) | 2664-2665 | subsection | fork (FA-48) | `s 117.09(2) the employee of a licensed business is not guilty of an offence by reason only of dealing with a partially manufactured barrelled weapon` |
| s 117.09(3) | 2666-2667 | subsection | fork (FA-49) | `s 117.09(3) the employee of a carrier is not guilty of an offence by reason only of possessing or transferring the listed things in their duties` |
| s 117.09(4) | 2668-2669 | subsection | fork (FA-50) | `s 117.09(4) the employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a functioning imitation antique firearm` |
| s 117.09(5) | 2670-2671 | subsection | fork (FA-51) | `s 117.09(5) the designated employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a firearm` |
| s 117.09(6) | 2672-2673 | subsection | fork (FA-52) | `s 117.09(6) the provincial minister is barred from designating the individual for the purpose of subsection (5)` |
| s 117.09(7) | 2674-2675 | subsection | fork (FA-53) | `s 117.09(7) the provincial minister may attach a condition to the designation` |
| s 117.1 | 2676-2677 | section | fork (FM-17) | `s 117.1 sections 117.07 to 117.09 do not apply to the person` |
| General | 2679 | heading | inert (reason 1: heading) | General |
| s 117.11 | 2680-2681 | section | fork (FM-23) | `s 117.11 the onus is on the accused to prove that the person is the holder of the authorization, licence or registration certificate` |
| s 117.12(1) | 2682-2683 | subsection | encoded | `s 117.12(1) a document purporting to be an authorization, a licence or a registration certificate is evidence of the statements contained in it` |
| s 117.12(2) | 2684-2685 | subsection | encoded | `s 117.12(2) a certified copy is admissible in evidence`; `s 117.12(2) the certified copy has the same probative force as the original would have had` |
| s 117.13(1) | 2686-2687 | subsection | encoded | `s 117.13(1) a certificate of an analyst is evidence without proof of the signature or official character` |
| s 117.13(2) | 2688-2689 | subsection | fork (FA-54) | `s 117.13(2) the party against whom a certificate of an analyst is produced may, with leave of the court, require the attendance of the analyst` |
| s 117.13(3) | 2690-2691 | subsection | fork (FA-55) | `s 117.13(3) the certificate of an analyst is barred from admission for want of reasonable notice before the trial` |
| s 117.13(4) and (5) | 2692 | repealed | repealed or blank in this text | the text shows: "(4) and (5) [Repealed, 2008, c. 18, s. 2]" |
| s 117.14(1) | 2693-2694 | subsection | fork (FA-56) | `s 117.14(1) the Governor in Council may declare an amnesty period` |
| s 117.14(2) | 2695-2696 | subsection | fork (FA-57) | `s 117.14(2) the order declares the amnesty period for a purpose subsection (2) names` |
| s 117.14(2)(a) | 2697 | paragraph | fork (FA-57) | `s 117.14(2) the order declares the amnesty period for a purpose subsection (2) names` |
| s 117.14(2)(b) | 2698 | paragraph | fork (FA-57) | `s 117.14(2) the order declares the amnesty period for a purpose subsection (2) names` |
| s 117.14(3) | 2699-2700 | subsection | fork (FA-58) | `s 117.14(3) the person is not guilty of an offence under this Part by reason only of doing a thing provided for in an amnesty order` |
| s 117.14(4) | 2701-2702 | subsection | encoded | `s 117.14(4) the proceedings are a nullity` |
| s 117.15(1) | 2703-2704 | subsection | inert (reason 2) | regulation-making power of the Governor in Council ("prescribing anything that by this Part is to be or may be prescribed") |
| s 117.15(2) | 2705-2706 | subsection | inert (reason 2) | a limit on that regulation-making power (the Governor in Council may not prescribe a thing reasonable for hunting or sporting use as prohibited) |
| s 117.15(3) | 2707 | repealed | repealed or blank in this text | the text shows: "(3) [Repealed, 2019, c. 9, s. 18]" |
| s 117.15(4) | 2708 | repealed | repealed or blank in this text | the text shows: "(4) [Repealed, 2019, c. 9, s. 18]" |
| PART IV Offences Against the Administration of Law and Justice | 2710 | heading | inert (reason 1: heading) | PART IV Offences Against the Administration of Law and Justice |
| Interpretation | 2712 | heading | inert (reason 1: heading) | Interpretation |
| s 118 | 2713-2714 | section | inert (reason 1) | the lead-in "In this Part," only sets the scope of the definitions; the scope is carried by the names `s 118 ...` and by the Part IV functions that take them as inputs |
| s 118 "evidence or statement" | 2715 | definition | encoded | `s 118 evidence or statement` |
| s 118 "government" | 2716 | definition | encoded | `s 118 government` |
| s 118 "government" (a) | 2717 | paragraph | encoded | `s 118 government` |
| s 118 "government" (b) | 2718 | paragraph | encoded | `s 118 government` |
| s 118 "government" (c) | 2719 | paragraph | encoded | `s 118 government` |
| s 118 "judicial proceeding" | 2720 | definition | encoded | `s 118 judicial proceeding` |
| s 118 "judicial proceeding" (a) | 2721 | paragraph | encoded | `s 118 judicial proceeding` |
| s 118 "judicial proceeding" (b) | 2722 | paragraph | encoded | `s 118 judicial proceeding` |
| s 118 "judicial proceeding" (c) | 2723 | paragraph | encoded | `s 118 judicial proceeding` |
| s 118 "judicial proceeding" (d) | 2724 | paragraph | encoded | `s 118 judicial proceeding` |
| s 118 "judicial proceeding" (e) | 2725-2726 | paragraph | encoded | `s 118 judicial proceeding` |
| s 118 "office" | 2727 | definition | fork (FM-9) | `s 118 office` |
| s 118 "office" (a) | 2728 | paragraph | encoded | `s 118 office` |
| s 118 "office" (b) | 2729 | paragraph | encoded | `s 118 office` |
| s 118 "office" (c) | 2730 | paragraph | encoded | `s 118 office` |
| s 118 "official" | 2731 | definition | fork (FM-9) | `s 118 official` |
| s 118 "official" (a) | 2732 | paragraph | encoded | `s 118 official` |
| s 118 "official" (b) | 2733 | paragraph | encoded | `s 118 official` |
| s 118 "witness" | 2734 | definition | fork (FM-8) | `s 118 witness` |
| Corruption and Disobedience | 2736 | heading | inert (reason 1: heading) | Corruption and Disobedience |
| s 119(1) | 2737-2738 | subsection | fork (FM-12) | `s 119(1) the person is guilty of an indictable offence under subsection (1)`; `s 119(1) the class of the offence`; `s 119(1) the punishment on indictment` |
| s 119(1)(a) | 2739 | paragraph | encoded | `s 119(1)(a) the holder of a judicial office or legislator corruptly accepts or obtains a benefit` |
| s 119(1)(b) | 2740 | paragraph | encoded | `s 119(1)(b) the person corruptly gives or offers a benefit to a judicial officer or legislator` |
| s 119(2) | 2741-2742 | subsection | fork (FA-14) | `s 119(2) the proceedings against a holder of a judicial office are barred for want of the written consent of the Attorney General of Canada` |
| s 120 | 2743-2744 | section | fork (FM-12) | `s 120 the person is guilty of an indictable offence under section 120`; `s 120 the class of the offence`; `s 120 the punishment on indictment` |
| s 120(a) | 2745 | paragraph | encoded | `s 120(a) the officer or person employed in the administration of criminal law corruptly accepts or obtains a benefit with a stated intent` |
| s 120(a)(i) | 2746 | subparagraph | encoded | `s 120(a) the officer or person employed in the administration of criminal law corruptly accepts or obtains a benefit with a stated intent` |
| s 120(a)(ii) | 2747 | subparagraph | encoded | `s 120(a) the officer or person employed in the administration of criminal law corruptly accepts or obtains a benefit with a stated intent` |
| s 120(a)(iii) | 2748 | subparagraph | encoded | `s 120(a) the officer or person employed in the administration of criminal law corruptly accepts or obtains a benefit with a stated intent` |
| s 120(b) | 2749 | paragraph | encoded | `s 120(b) the person corruptly gives or offers a benefit to an officer with a stated intent` |
| s 121(1) | 2750-2751 | subsection | fork (FM-12) | `s 121(1) the person commits an offence under subsection (1)` |
| s 121(1)(a) | 2752 | paragraph | encoded | `s 121(1)(a) the person gives to an official, or an official takes, a benefit for cooperation or influence in government business` |
| s 121(1)(a)(i) | 2753 | subparagraph | encoded | `s 121(1)(a) the person gives to an official, or an official takes, a benefit for cooperation or influence in government business` |
| s 121(1)(a)(ii) | 2754-2755 | subparagraph | encoded | `s 121(1)(a) the person gives to an official, or an official takes, a benefit for cooperation or influence in government business` |
| s 121(1)(a)(iii) | 2756 | subparagraph | encoded | `s 121(1)(a) the person gives to an official, or an official takes, a benefit for cooperation or influence in government business` |
| s 121(1)(a)(iv) | 2757-2758 | subparagraph | encoded | `s 121(1)(a) the person gives to an official, or an official takes, a benefit for cooperation or influence in government business` |
| s 121(1)(b) | 2759 | paragraph | encoded | `s 121(1)(b) the person having dealings with the government pays or confers a benefit on its employee or official without written consent` |
| s 121(1)(c) | 2760 | paragraph | encoded | `s 121(1)(c) the official or employee of the government takes a benefit from a person dealing with it without written consent` |
| s 121(1)(d) | 2761 | paragraph | encoded | `s 121(1)(d) the person with, or pretending to have, influence demands or accepts a reward for it` |
| s 121(1)(d)(i) | 2762 | subparagraph | encoded | `s 121(1)(d) the person with, or pretending to have, influence demands or accepts a reward for it` |
| s 121(1)(d)(ii) | 2763 | subparagraph | encoded | `s 121(1)(d) the person with, or pretending to have, influence demands or accepts a reward for it` |
| s 121(1)(e) | 2764 | paragraph | encoded | `s 121(1)(e) the person gives or offers a reward to a minister or an official for cooperation or influence` |
| s 121(1)(e)(i) | 2765 | subparagraph | encoded | `s 121(1)(e) the person gives or offers a reward to a minister or an official for cooperation or influence` |
| s 121(1)(e)(ii) | 2766 | subparagraph | encoded | `s 121(1)(e) the person gives or offers a reward to a minister or an official for cooperation or influence` |
| s 121(1)(f) | 2767 | paragraph | encoded | `s 121(1)(f) the person having tendered for a government contract gives, offers, demands or accepts a reward for a tender's withdrawal` |
| s 121(1)(f)(i) | 2768 | subparagraph | encoded | `s 121(1)(f) the person having tendered for a government contract gives, offers, demands or accepts a reward for a tender's withdrawal` |
| s 121(1)(f)(ii) | 2769 | subparagraph | encoded | `s 121(1)(f) the person having tendered for a government contract gives, offers, demands or accepts a reward for a tender's withdrawal` |
| s 121(2) | 2770-2771 | subsection | encoded | `s 121(2) the contractor subscribes to an election fund to obtain or retain a government contract` |
| s 121(2)(a) | 2772 | paragraph | encoded | `s 121(2) the contractor subscribes to an election fund to obtain or retain a government contract` |
| s 121(2)(b) | 2773 | paragraph | encoded | `s 121(2) the contractor subscribes to an election fund to obtain or retain a government contract` |
| s 121(3) | 2774-2775 | subsection | encoded | `s 121(3)(a) the punishment on indictment`; `s 121(3) the class of the offence` |
| s 121(3)(a) | 2776 | paragraph | encoded | `s 121(3)(a) the punishment on indictment` |
| s 121(3)(b) | 2777 | paragraph | encoded | `s 121(3)(b) the punishment on summary conviction` |
| s 121.1(1) | 2778-2779 | subsection | encoded | `s 121.1(1) the person deals in unstamped tobacco` |
| s 121.1(2) | 2780-2781 | subsection | encoded | `s 121.1(2) subsection (1) does not apply in the circumstances the Excise Act, 2001 describes` |
| s 121.1(3) | 2782-2783 | subsection | encoded | `s 121.1(3) the tobacco grower does not contravene subsection (1) by reason only of possessing raw leaf tobacco described in section 31 of the Excise Act, 2001` |
| s 121.1(4) | 2784-2785 | subsection | encoded | `s 121.1(4) the person who contravenes subsection (1) is guilty of an offence`; `s 121.1(4) the class of the offence` |
| s 121.1(4)(a) | 2786 | paragraph | encoded | `s 121.1(4)(a) the punishment on indictment` |
| s 121.1(4)(b) | 2787 | paragraph | encoded | `s 121.1(4)(b) the punishment on summary conviction` |
| s 121.1(5) | 2788 | repealed | repealed or blank in this text | the text shows: "(5) [Repealed, 2022, c. 15, s. 9]" |
| s 122 | 2789-2790 | section | encoded | `s 122 the official commits fraud or a breach of trust in connection with the duties of their office`; `s 122 the class of the offence` |
| s 122(a) | 2791 | paragraph | encoded | `s 122(a) the punishment on indictment` |
| s 122(b) | 2792 | paragraph | encoded | `s 122(b) the punishment on summary conviction` |
| s 123(1) | 2793-2794 | subsection | encoded | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act`; `s 123(1) the punishment on indictment`; `s 123(1) the punishment on summary conviction`; `s 123(1) the class of the offence` |
| s 123(1)(a) | 2795 | paragraph | encoded | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act` |
| s 123(1)(b) | 2796 | paragraph | encoded | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act` |
| s 123(1)(c) | 2797 | paragraph | encoded | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act` |
| s 123(1)(d) | 2798 | paragraph | encoded | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act` |
| s 123(2) | 2799-2800 | subsection | encoded | `s 123(2) the person influences or attempts to influence a municipal official by suppression of the truth, threats, deceit or unlawful means`; `s 123(2) the punishment on indictment`; `s 123(2) the punishment on summary conviction`; `s 123(2) the class of the offence` |
| s 123(2)(a) | 2801 | paragraph | encoded | `s 123(2) the person influences or attempts to influence a municipal official by suppression of the truth, threats, deceit or unlawful means` |
| s 123(2)(b) | 2802 | paragraph | encoded | `s 123(2) the person influences or attempts to influence a municipal official by suppression of the truth, threats, deceit or unlawful means` |
| s 123(2)(c) | 2803 | paragraph | encoded | `s 123(2) the person influences or attempts to influence a municipal official by suppression of the truth, threats, deceit or unlawful means` |
| s 123(3) | 2804-2805 | subsection | encoded | `s 123(3) municipal official` |
| s 124 | 2806-2807 | section | fork (FM-12) | `s 124 the person is guilty of an offence under section 124`; `s 124 the class of the offence`; `s 124 the punishment on indictment`; `s 124 the punishment on summary conviction` |
| s 124(a) | 2808 | paragraph | encoded | `s 124(a) the person purports to sell an appointment to or resignation from an office, or takes a reward for it` |
| s 124(b) | 2809 | paragraph | encoded | `s 124(b) the person purports to purchase an appointment to or resignation from an office, or gives a reward for it` |
| s 125 | 2810-2811 | section | fork (FM-12) | `s 125 the person is guilty of an offence under section 125`; `s 125 the class of the offence`; `s 125 the punishment on indictment`; `s 125 the punishment on summary conviction` |
| s 125(a) | 2812 | paragraph | encoded | `s 125(a) the person receives, gives or procures a reward as consideration for influence to secure an appointment to an office` |
| s 125(b) | 2813 | paragraph | encoded | `s 125(b) the person solicits, recommends or negotiates about an appointment to or resignation from an office in expectation of a reward` |
| s 125(c) | 2814 | paragraph | encoded | `s 125(c) the person without lawful authority keeps a place for transacting business relating to offices` |
| s 125(c)(i) | 2815 | subparagraph | encoded | `s 125(c) the person without lawful authority keeps a place for transacting business relating to offices` |
| s 125(c)(ii) | 2816 | subparagraph | encoded | `s 125(c) the person without lawful authority keeps a place for transacting business relating to offices` |
| s 125(c)(iii) | 2817 | subparagraph | encoded | `s 125(c) the person without lawful authority keeps a place for transacting business relating to offices` |
| s 126(1) | 2818-2819 | subsection | fork (FM-11) | `s 126(1) the person is guilty of an offence by intentionally contravening an Act of Parliament`; `s 126(1) the class of the offence` |
| s 126(1)(a) | 2820 | paragraph | encoded | `s 126(1)(a) the punishment on indictment` |
| s 126(1)(b) | 2821 | paragraph | encoded | `s 126(1)(b) the punishment on summary conviction` |
| s 126(2) | 2822-2823 | subsection | fork (FA-15) | `s 126(2) proceedings may be instituted at the instance of the Government of Canada` |
| s 127(1) | 2824-2825 | subsection | fork (FM-10) | `s 127(1) the person is guilty of an offence by disobeying a lawful order of a court or authorized body`; `s 127(1) the class of the offence` |
| s 127(1)(a) | 2826 | paragraph | encoded | `s 127(1)(a) the punishment on indictment` |
| s 127(1)(b) | 2827 | paragraph | encoded | `s 127(1)(b) the punishment on summary conviction` |
| s 127(2) | 2828-2829 | subsection | fork (FA-16) | `s 127(2) proceedings for contravening or conspiring to contravene the order may be instituted and conducted at the instance of the Government of Canada` |
| s 128 | 2830-2831 | section | fork (FM-12) | `s 128 the person is guilty of an offence under section 128`; `s 128 the class of the offence`; `s 128 the punishment on indictment`; `s 128 the punishment on summary conviction` |
| s 128(a) | 2832 | paragraph | encoded | `s 128(a) the peace officer or coroner intentionally misconducts themselves in the execution of a process` |
| s 128(b) | 2833 | paragraph | encoded | `s 128(b) the peace officer or coroner intentionally makes a false return to a process` |
| s 129 | 2834-2835 | section | fork (FM-12) | `s 129 the person is guilty of an offence under section 129`; `s 129 the class of the offence` |
| s 129(a) | 2836 | paragraph | encoded | `s 129(a) the person resists or wilfully obstructs a public officer or peace officer in the execution of their duty` |
| s 129(b) | 2837 | paragraph | encoded | `s 129(b) the person omits without reasonable excuse to assist a public officer or peace officer after reasonable notice` |
| s 129(c) | 2838-2839 | paragraph | encoded | `s 129(c) the person resists or wilfully obstructs a person in the lawful execution of a process against lands or goods, or in a lawful distress or seizure` |
| s 129(d) | 2840 | paragraph | encoded | `s 129(d) the punishment on indictment` |
| s 129(e) | 2841 | paragraph | encoded | `s 129(e) the punishment on summary conviction` |
| s 130(1) | 2842-2843 | subsection | fork (FM-12) | `s 130(1) the person commits an offence under subsection (1)` |
| s 130(1)(a) | 2844 | paragraph | encoded | `s 130(1)(a) the person falsely represents themselves to be a peace officer or a public officer` |
| s 130(1)(b) | 2845 | paragraph | encoded | `s 130(1)(b) the person who is neither uses a badge, uniform or equipment likely to cause others to believe they are one` |
| s 130(2) | 2846-2847 | subsection | encoded | `s 130(2)(a) the punishment on indictment`; `s 130(2) the class of the offence` |
| s 130(2)(a) | 2848 | paragraph | encoded | `s 130(2)(a) the punishment on indictment` |
| s 130(2)(b) | 2849 | paragraph | encoded | `s 130(2)(b) the punishment on summary conviction` |
| s 130.1 | 2850-2851 | section | encoded | `s 130.1 the sentencing court is bound to treat as aggravating that the accused personated an officer to facilitate another offence` |
| Misleading Justice | 2853 | heading | inert (reason 1: heading) | Misleading Justice |
| s 131(1) | 2854-2855 | subsection | encoded | `s 131(1) the person commits perjury by a false statement under oath or solemn affirmation` |
| s 131(1.1) | 2856-2857 | subsection | encoded | `s 131(1.1) the person commits perjury by a false statement given by video link or under a mutual legal assistance order` |
| s 131(2) | 2858-2859 | subsection | fork (FM-25) | `s 131(2) subsection (1) applies whether or not the statement is made in a judicial proceeding` |
| s 131(3) | 2860-2861 | subsection | encoded | `s 131(3) subsections (1) and (1.1) do not apply to a statement made by a person not specially permitted, authorized or required by law to make it` |
| s 132 | 2862-2863 | section | encoded | `s 132 the person who commits perjury is guilty of an indictable offence`; `s 132 the class of the offence`; `s 132 the punishment on indictment` |
| s 133 | 2864-2865 | section | fork (FA-59) | `s 133 the accused is barred from being convicted of perjury on the evidence of only one witness unless it is corroborated in a material particular` |
| s 134(1) | 2866-2867 | subsection | encoded | `s 134(1) the person makes a false statement under oath or solemn affirmation without being permitted, authorized or required by law`; `s 134(1) the punishment on summary conviction`; `s 134(1) the class of the offence` |
| s 134(2) | 2868-2869 | subsection | encoded | `s 134(2) subsection (1) does not apply to a statement made in the course of a criminal investigation` |
| s 135 | 2870 | repealed | repealed or blank in this text | the text shows: "135 [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 17]" |
| s 136(1) | 2871-2872 | subsection | encoded | `s 136(1) the witness is guilty of giving contradictory evidence`; `s 136(1) the class of the offence`; `s 136(1) the punishment on indictment` |
| s 136(1.1) | 2873-2874 | subsection | encoded | `s 136(1.1) the evidence is deemed to be evidence given by a witness in a judicial proceeding` |
| s 136(2) | 2875-2876 | subsection | encoded | `s 136(2) the evidence is evidence for the purposes of section 136` |
| s 136(2.1) | 2877-2878 | subsection | encoded | `s 136(2.1) a certificate is evidence that the evidence was given in a judicial proceeding` |
| s 136(3) | 2879-2880 | subsection | fork (FA-60) | `s 136(3) the proceedings are barred for want of the consent of the Attorney General` |
| s 137 | 2881-2882 | section | encoded | `s 137 the person fabricates anything to be used as evidence in a judicial proceeding`; `s 137 the class of the offence`; `s 137 the punishment on indictment` |
| s 138 | 2883-2884 | section | fork (FM-12) | `s 138 the person is guilty of an offence under section 138`; `s 138 the class of the offence`; `s 138 the punishment on indictment`; `s 138 the punishment on summary conviction` |
| s 138(a) | 2885 | paragraph | encoded | `s 138(a) the person signs a writing that purports to be an affidavit or statutory declaration sworn or declared before them when it was not` |
| s 138(b) | 2886 | paragraph | encoded | `s 138(b) the person uses or offers for use a writing purporting to be an affidavit or statutory declaration that they know was not sworn or declared` |
| s 138(c) | 2887 | paragraph | encoded | `s 138(c) the person signs as affiant or declarant a writing purporting to have been sworn or declared by them when it was not` |
| s 139(1) | 2888-2889 | subsection | fork (FM-12) | `s 139(1) the person is guilty of an offence under subsection (1)`; `s 139(1) the class of the offence` |
| s 139(1)(a) | 2890 | paragraph | encoded | `s 139(1)(a) the person attempts to obstruct justice by indemnifying a surety` |
| s 139(1)(b) | 2891-2892 | paragraph | encoded | `s 139(1)(b) the surety attempts to obstruct justice by accepting a fee or indemnity` |
| s 139(1)(c) | 2893 | paragraph | encoded | `s 139(1)(c) the punishment on indictment` |
| s 139(1)(d) | 2894 | paragraph | encoded | `s 139(1)(d) the punishment on summary conviction` |
| s 139(2) | 2895-2896 | subsection | encoded | `s 139(2) the person intentionally attempts to obstruct, pervert or defeat the course of justice otherwise than as subsection (1) describes`; `s 139(2) the class of the offence` |
| s 139(2)(a) | 2897 | paragraph | encoded | `s 139(2)(a) the punishment on indictment` |
| s 139(2)(b) | 2898 | paragraph | encoded | `s 139(2)(b) the punishment on summary conviction` |
| s 139(3) | 2899-2900 | subsection | fork (FA-61) | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` |
| s 139(3)(a) | 2901 | paragraph | fork (FA-61) | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` |
| s 139(3)(b) | 2902 | paragraph | fork (FA-61) | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` |
| s 139(3)(c) | 2903 | paragraph | fork (FA-61) | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` |
| s 140(1) | 2904-2905 | subsection | encoded | `s 140(1) the person commits public mischief` |
| s 140(1)(a) | 2906 | paragraph | encoded | `s 140(1) the person commits public mischief` |
| s 140(1)(b) | 2907 | paragraph | encoded | `s 140(1) the person commits public mischief` |
| s 140(1)(c) | 2908 | paragraph | encoded | `s 140(1) the person commits public mischief` |
| s 140(1)(d) | 2909 | paragraph | encoded | `s 140(1) the person commits public mischief` |
| s 140(2) | 2910-2911 | subsection | encoded | `s 140(2)(a) the punishment on indictment`; `s 140(2) the class of the offence` |
| s 140(2)(a) | 2912 | paragraph | encoded | `s 140(2)(a) the punishment on indictment` |
| s 140(2)(b) | 2913 | paragraph | encoded | `s 140(2)(b) the punishment on summary conviction` |
| s 141(1) | 2914-2915 | subsection | encoded | `s 141(1) the person asks for or obtains valuable consideration for agreeing to compound or conceal an indictable offence`; `s 141(1) the class of the offence` |
| s 141(1)(a) | 2916 | paragraph | encoded | `s 141(1)(a) the punishment on indictment` |
| s 141(1)(b) | 2917 | paragraph | encoded | `s 141(1)(b) the punishment on summary conviction` |
| s 141(2) | 2918-2919 | subsection | fork (FA-62) | `s 141(2) the exception for diversion agreements applies` |
| s 141(2)(a) | 2920 | paragraph | fork (FA-62) | `s 141(2) the exception for diversion agreements applies` |
| s 141(2)(b) | 2921 | paragraph | fork (FA-62) | `s 141(2) the exception for diversion agreements applies` |
| s 142 | 2922-2923 | section | encoded | `s 142 the person corruptly accepts valuable consideration for helping to recover property obtained by an indictable offence`; `s 142 the class of the offence` |
| s 142(a) | 2924 | paragraph | encoded | `s 142(a) the punishment on indictment` |
| s 142(b) | 2925 | paragraph | encoded | `s 142(b) the punishment on summary conviction` |
| s 143 | 2926 | repealed | repealed or blank in this text | the text shows: "143 [Repealed, 2018, c. 29, s. 8]" |
| Escapes and Rescues | 2928 | heading | inert (reason 1: heading) | Escapes and Rescues |
| s 144 | 2929-2930 | section | fork (FM-12) | `s 144 the person is guilty of an offence under section 144`; `s 144 the class of the offence`; `s 144 the punishment on indictment`; `s 144 the punishment on summary conviction` |
| s 144(a) | 2931 | paragraph | encoded | `s 144(a) the person by force or violence breaks a prison with intent to set at liberty a person confined in it` |
| s 144(b) | 2932 | paragraph | encoded | `s 144(b) the person confined in a prison with intent to escape forcibly breaks out of, or makes a breach in, a cell or other place within it` |
| s 145(1) | 2933-2934 | subsection | fork (FM-12) | `s 145(1) the person escapes from lawful custody`; `s 145(1) the person is guilty of an offence under subsection (1)`; `s 145(1) the person is at large before the end of a term of imprisonment without lawful excuse`; `s 145(1) the class of the offence` |
| s 145(1)(a) | 2935 | paragraph | encoded | `s 145(1)(a) the punishment on indictment` |
| s 145(1)(b) | 2936 | paragraph | encoded | `s 145(1)(b) the punishment on summary conviction` |
| s 145(2) | 2937-2938 | subsection | fork (FM-12) | `s 145(2) the person is guilty of an offence under subsection (2)`; `s 145(2) the class of the offence`; `s 145(2) the punishment on indictment`; `s 145(2) the punishment on summary conviction` |
| s 145(2)(a) | 2939 | paragraph | encoded | `s 145(2)(a) the person at large on a release order fails without lawful excuse to attend court` |
| s 145(2)(b) | 2940 | paragraph | encoded | `s 145(2)(b) the person who has appeared fails without lawful excuse to attend court again as required` |
| s 145(2)(c) | 2941 | paragraph | encoded | `s 145(2)(c) the person fails to surrender in accordance with an order of the court, justice or judge` |
| s 145(2)(d) | 2942 | paragraph | encoded | `s 145(2)(d) the person fails without lawful excuse to comply with an order made under section 515.01` |
| s 145(3) | 2943-2944 | subsection | encoded | `s 145(3) the person named in an appearance notice or served with a summons fails without lawful excuse to appear or attend`; `s 145(3) the person is guilty of an offence under subsection (3)`; `s 145(3) the class of the offence` |
| s 145(3)(a) | 2945 | paragraph | encoded | `s 145(3)(a) the punishment on indictment` |
| s 145(3)(b) | 2946 | paragraph | encoded | `s 145(3)(b) the punishment on summary conviction` |
| s 145(4) | 2947-2948 | subsection | fork (FM-12) | `s 145(4) the person is guilty of an offence under subsection (4)`; `s 145(4) the class of the offence`; `s 145(4) the punishment on indictment`; `s 145(4) the punishment on summary conviction` |
| s 145(4)(a) | 2949 | paragraph | encoded | `s 145(4)(a) the person at large on an undertaking fails without lawful excuse to comply with a condition` |
| s 145(4)(b) | 2950 | paragraph | encoded | `s 145(4)(b) the person at large on a confirmed undertaking fails without lawful excuse to appear or attend` |
| s 145(5) | 2951-2952 | subsection | fork (FM-12) | `s 145(5) the person is guilty of an offence under subsection (5)`; `s 145(5) the class of the offence`; `s 145(5) the punishment on indictment`; `s 145(5) the punishment on summary conviction` |
| s 145(5)(a) | 2953 | paragraph | encoded | `s 145(5)(a) the person at large on a release order fails without lawful excuse to comply with a condition other than to attend court` |
| s 145(5)(b) | 2954 | paragraph | encoded | `s 145(5)(b) the person bound by an order under section 515(12), 516.1(1) or 522(2.1) fails without lawful excuse to comply` |
| s 145(5.1) | 2955 | repealed | repealed or blank in this text | the text shows: "(5.1) [Repealed, 2019, c. 25, s. 47]" |
| s 145(6) | 2956-2957 | subsection | fork (FM-15) | `s 145(6) a defective statement of the alleged offence in an appearance notice or undertaking is not a lawful excuse` |
| s 145(7) | 2958 | repealed | repealed or blank in this text | the text shows: "(7) [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 20]" |
| s 145(8) | 2959-2960 | subsection | fork (FA-63) | `s 145(8) the failure is with lawful excuse because the Attorney General has made an election under section 50 of the Contraventions Act` |
| s 145(9) | 2961-2962 | subsection | encoded | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 145(9)(a) | 2963 | paragraph | encoded | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 145(9)(b) | 2964 | paragraph | encoded | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 145(9)(c) | 2965 | paragraph | encoded | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 145(9)(d) | 2966 | paragraph | encoded | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 145(10) | 2967-2968 | subsection | fork (FA-64) | `s 145(10) the accused may, with leave of the court, require the person who made the certificate to attend for cross-examination` |
| s 145(11) | 2969-2970 | subsection | fork (FA-65) | `s 145(11) the certificate is barred from reception in evidence for want of reasonable notice before the trial` |
| s 146 | 2971-2972 | section | fork (FM-12) | `s 146 the person is guilty of an offence under section 146`; `s 146 the class of the offence`; `s 146 the punishment on indictment`; `s 146 the punishment on summary conviction` |
| s 146(a) | 2973 | paragraph | encoded | `s 146(a) the person permits a person in lawful custody to escape by failing to perform a legal duty` |
| s 146(b) | 2974 | paragraph | encoded | `s 146(b) the person conveys a thing into a prison with intent to facilitate an escape` |
| s 146(c) | 2975 | paragraph | encoded | `s 146(c) the person under colour of pretended authority directs or procures the discharge of a prisoner who is not entitled to be discharged` |
| s 147 | 2976-2977 | section | fork (FM-12) | `s 147 the person is guilty of an offence under section 147`; `s 147 the class of the offence`; `s 147 the punishment on indictment`; `s 147 the punishment on summary conviction` |
| s 147(a) | 2978 | paragraph | encoded | `s 147(a) the person rescues a person from lawful custody or assists a person in escaping or attempting to escape from lawful custody` |
| s 147(b) | 2979 | paragraph | encoded | `s 147(b) the peace officer wilfully permits a person in their lawful custody to escape` |
| s 147(c) | 2980 | paragraph | encoded | `s 147(c) the officer of or employee in a prison wilfully permits a person to escape from lawful custody in it` |
| s 148 | 2981-2982 | section | fork (FM-12) | `s 148 the person is guilty of an offence under section 148`; `s 148 the class of the offence`; `s 148 the punishment on indictment`; `s 148 the punishment on summary conviction` |
| s 148(a) | 2983 | paragraph | encoded | `s 148(a) the person knowingly assists a prisoner of war in Canada to escape from a place where they are detained` |
| s 148(b) | 2984 | paragraph | encoded | `s 148(b) the person knowingly assists a prisoner of war on parole in Canada to escape from the place where they are at large on parole` |
| s 149(1) | 2985-2986 | subsection | fork (FA-66) | `s 149(1) the court may order that the term of imprisonment for an escape be served in a penitentiary` |
| s 149(2) | 2987-2988 | subsection | encoded | `s 149(2) escape` |

## Fork register (ccc5)

The rulings below are copied word for word from the brief (which copies them from the Commons guide); the rows after them are the forks of this part.

**Ruling of 2026-11-12 on grants and powers (three limits), word for word from the brief:**

> **A function named for a grant or a power answers `NOTHING`, not `JUST FALSE`, when an "if" gate fails (ruling of 2026-11-12, three limits).** A layer-1 function NAMED for a grant or a power ("may", "is permitted to", "has power to") that answers `JUST FALSE` because an "if" gate failed reads as "may not", a grant turned into a bar. The guide's "In short" sentence gives `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". (1) Answer `NOTHING` for such a function, with one fork line in NOTES.md (fork register and marginal readings) that names the other reading. (2) Keep `JUST FALSE` wherever the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question. (3) Do NOT decide two groups by yourself; list them in the fork register with a count and leave the answer as the guide's rulings give it: "may" functions whose gate is "where", "when" or "upon" (ruling (b) says `JUST FALSE`, the line on grants points the other way: a question for a lawyer), and "entitled"-named functions (a claim, not a power).

**Rulings of 2026-11-04, 2026-11-05 and the case-by-case instruction, word for word from the brief:**



- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The counts the ruling of 2026-11-12 asks for are in the subsection "Name-test sweep of 2026-11-12", below the table.

| id | provision / function | answer taken | other reading | what licenses each reading |
| --- | --- | --- | --- | --- |
| FA-1 | `s 110.4(1) the provincial court judge may fix a date for the hearing of an application under subsection 111(1)` (s 110.4(1)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-2 | `s 110.4(3) the provincial court judge may adjourn the hearing` (s 110.4(3)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-3 | `s 111(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order prohibiting a person from possessing weapons` (s 111(1)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-4 | `s 111(4) the provincial court judge may proceed ex parte to hear and determine the application` (s 111(4)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-5 | `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` (s 111(8)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-6 | `s 111(9) the Attorney General may appeal to the superior court against the decision not to make an order` (s 111(9)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-7 | `s 112 a provincial court judge may revoke the order` (s 112) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-8 | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` (s 113(1), s 113(1)(a), s 113(1)(b)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-9 | `s 113(3)(a) an authorization, licence or registration certificate is barred from being denied solely on the basis of the prohibition order or the offence` (s 113(3), s 113(3)(a)) | JUST FALSE when the "where" fails | NOTHING | bar-where: a bar with a "where" gate: JUST FALSE under ruling (b) of 2026-11-05 and the line of 2026-11-12 that a bar keeps JUST FALSE |
| FA-10 | `s 113(3)(b) the authorization or licence may be issued to the person for the duration of the order` (s 113(3)(b)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-11 | `s 113(3)(b) the chief firearms officer may attach further terms and conditions to the authorization or licence` (s 113(3)(b)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-12 | `s 113(4) an order under subsection (1) may be made during the proceedings` (s 113(4)) | NOTHING outside the list | JUST FALSE | list-open: a list the text does not close ("Without restricting the generality of subsection (2)", "For greater certainty", "any purpose referred to"): NOTHING outside the list (list not closed) |
| FA-13 | `s 114 the competent authority may require the person to surrender the things and documents` (s 114, s 114(a), s 114(b)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-14 | `s 119(2) the proceedings against a holder of a judicial office are barred for want of the written consent of the Attorney General of Canada` (s 119(2)) | JUST FALSE when consent was given | NOTHING | bar-without: a bar worded "without the consent of": read as "unless the consent was given", so consent gives JUST FALSE; the other reading is that "without" limits the prohibition in its own wording and the case outside the limit is NOTHING |
| FA-15 | `s 126(2) proceedings may be instituted at the instance of the Government of Canada` (s 126(2)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-16 | `s 127(2) proceedings for contravening or conspiring to contravene the order may be instituted and conducted at the instance of the Government of Canada` (s 127(2)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-17 | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` (s 117.0101(1), s 117.0101(1)(a), s 117.0101(1)(b)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-18 | `s 117.0101(2) the provincial court judge may hold the hearing in private` (s 117.0101(2)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-19 | `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` (s 117.0101(6)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-20 | `s 117.0101(7) the peace officer may search for and seize without a warrant` (s 117.0101(7)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-21 | `s 117.0101(9) the provincial court judge may require the person to surrender the things` (s 117.0101(9)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-22 | `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` (s 117.0101(11)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-23 | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` (s 117.0102(1), s 117.0102(1)(a), s 117.0102(1)(b)...) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-24 | `s 117.0102(5) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` (s 117.0102(5)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-25 | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` (s 117.0103(1), s 117.0103(1)(a), s 117.0103(1)(b)...) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-26 | `s 117.0103(2) the order may be for any period, definite or indefinite, that the judge considers necessary` (s 117.0103(2)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-27 | `s 117.0103(4) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` (s 117.0103(4)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-28 | `s 117.0104(1) the provincial court judge may fix a date for the hearing of an application under subsection 117.011(1)` (s 117.0104(1)) | NOTHING | JUST FALSE | power-if: a "may" power whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers") fails: ruling of 2026-11-12 (1) gives NOTHING; the other reading is that a failed gate is the text's no (ruling (a) of 2026-11-05), JUST FALSE, which a reader takes as "may not" |
| FA-29 | `s 117.0104(3) the provincial court judge may adjourn the hearing` (s 117.0104(3)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-30 | `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` (s 117.011(1), s 117.011(1)(a), s 117.011(1)(b)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-31 | `s 117.011(4) the provincial court judge may proceed ex parte to hear and determine the application` (s 117.011(4)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-32 | `s 117.011(7) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` (s 117.011(7)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-33 | `s 117.011(8) the Attorney General may appeal to the superior court against the decision not to make an order` (s 117.011(8)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-34 | `s 117.012 a provincial court judge may revoke the order` (s 117.012) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-35 | `s 117.02(1) the peace officer may search without a warrant and seize` (s 117.02(1), s 117.02(1)(a), s 117.02(1)(b)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-36 | `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` (s 117.03(1), s 117.03(1)(a), s 117.03(1)(b)) | JUST FALSE when the "unless" is met | JUST FALSE is not a bar on the whole power | power-unless: the power is closed by "unless": JUST FALSE where the exception holds (ruling (2) of 2026-11-12); NOTHING where the gate (the failure to produce) is not shown |
| FA-37 | `s 117.03(3) the provincial court judge may declare the thing forfeited to Her Majesty` (s 117.03(3)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-38 | `s 117.04(1) the justice may issue a warrant authorizing a peace officer to search the building, receptacle or place and seize` (s 117.04(1)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-39 | `s 117.04(2) the peace officer may search for and seize without a warrant` (s 117.04(2)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-40 | `s 117.05(2) the justice may proceed ex parte to hear and determine the application` (s 117.05(2)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-41 | `s 117.05(7) the person may appeal to the superior court against the order` (s 117.05(7)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-42 | `s 117.05(8) the Attorney General may appeal to the superior court against the failure to make the finding or the order` (s 117.05(8)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-43 | `s 117.06(2) the justice may order that the revocation be reversed and the authorization, licence or registration certificate restored` (s 117.06(2)) | JUST FALSE | NOTHING | power-where: a "may" power whose gate is "where", "when" or "upon", or a condition of that kind ("on application by", "on being issued a receipt", "before or at any time during", "after affording"; the equivalents are ASSUMED, NOT RULED, to go with the group): ruling (b) of 2026-11-05 says JUST FALSE; the line on grants of 2026-11-12 points to NOTHING: listed, not flipped, left as the guide's rulings give it, a question for the maintainer or a lawyer (test 3(i) of 2026-11-12) |
| FA-44 | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` (s 117.07(1), s 117.07(1)(a), s 117.07(1)(b)...) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-45 | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` (s 117.071, s 117.071(a), s 117.071(b)...) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-46 | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` (s 117.08, s 117.08(a), s 117.08(b)...) | NOTHING when the "if" fails | JUST FALSE | immunity-if: an exemption closed by a trailing "if the individual does so on behalf of ...": NOTHING when it fails (grant-like, ruling of 2026-11-12); the other reading is JUST FALSE (ruling (a)) |
| FA-47 | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` (s 117.09(1), s 117.09(1)(a), s 117.09(1)(b)...) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-48 | `s 117.09(2) the employee of a licensed business is not guilty of an offence by reason only of dealing with a partially manufactured barrelled weapon` (s 117.09(2)) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-49 | `s 117.09(3) the employee of a carrier is not guilty of an offence by reason only of possessing or transferring the listed things in their duties` (s 117.09(3)) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-50 | `s 117.09(4) the employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a functioning imitation antique firearm` (s 117.09(4)) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-51 | `s 117.09(5) the designated employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a firearm` (s 117.09(5)) | NOTHING when the "if" fails | JUST FALSE | immunity-if: an exemption closed by a trailing "if the individual does so on behalf of ...": NOTHING when it fails (grant-like, ruling of 2026-11-12); the other reading is JUST FALSE (ruling (a)) |
| FA-52 | `s 117.09(6) the provincial minister is barred from designating the individual for the purpose of subsection (5)` (s 117.09(6)) | JUST FALSE when the "where" fails | NOTHING | bar-where: a bar with a "where" gate: JUST FALSE under ruling (b) of 2026-11-05 and the line of 2026-11-12 that a bar keeps JUST FALSE |
| FA-53 | `s 117.09(7) the provincial minister may attach a condition to the designation` (s 117.09(7)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-54 | `s 117.13(2) the party against whom a certificate of an analyst is produced may, with leave of the court, require the attendance of the analyst` (s 117.13(2)) | NOTHING | JUST FALSE | power-with-leave: a "may ... with leave of the court" power: the leave is a gate in the text's own wording; without it the answer is NOTHING; the other reading is JUST FALSE |
| FA-55 | `s 117.13(3) the certificate of an analyst is barred from admission for want of reasonable notice before the trial` (s 117.13(3)) | JUST FALSE when the "unless" is met | NOTHING | bar-unless: a bar closed by "unless": JUST FALSE (the text closes the gate itself) |
| FA-56 | `s 117.14(1) the Governor in Council may declare an amnesty period` (s 117.14(1)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FA-57 | `s 117.14(2) the order declares the amnesty period for a purpose subsection (2) names` (s 117.14(2), s 117.14(2)(a), s 117.14(2)(b)) | NOTHING outside the list | JUST FALSE | list-open: a list the text does not close ("Without restricting the generality of subsection (2)", "For greater certainty", "any purpose referred to"): NOTHING outside the list (list not closed) |
| FA-58 | `s 117.14(3) the person is not guilty of an offence under this Part by reason only of doing a thing provided for in an amnesty order` (s 117.14(3)) | NOTHING when the gate fails | JUST FALSE | immunity: an exemption or immunity ("no person is guilty ... by reason only that"): when the gate fails the text does not say the person is guilty; NOTHING; the other reading treats a failed gate as the text's no |
| FA-59 | `s 133 the accused is barred from being convicted of perjury on the evidence of only one witness unless it is corroborated in a material particular` (s 133) | JUST FALSE when the "unless" is met | NOTHING | bar-unless: a bar closed by "unless": JUST FALSE (the text closes the gate itself) |
| FA-60 | `s 136(3) the proceedings are barred for want of the consent of the Attorney General` (s 136(3)) | JUST FALSE when consent was given | NOTHING | bar-without: a bar worded "without the consent of": read as "unless the consent was given", so consent gives JUST FALSE; the other reading is that "without" limits the prohibition in its own wording and the case outside the limit is NOTHING |
| FA-61 | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` (s 139(3), s 139(3)(a), s 139(3)(b)...) | NOTHING outside the list | JUST FALSE | list-open: a list the text does not close ("Without restricting the generality of subsection (2)", "For greater certainty", "any purpose referred to"): NOTHING outside the list (list not closed) |
| FA-62 | `s 141(2) the exception for diversion agreements applies` (s 141(2), s 141(2)(a), s 141(2)(b)) | JUST FALSE when the "where" fails | NOTHING | where-exception: an exception worded "No offence is committed ... where ...": the "where" condition failing gives JUST FALSE under ruling (b) of 2026-11-05, worded "this section gives no exception on these facts"; the other reading is NOTHING |
| FA-63 | `s 145(8) the failure is with lawful excuse because the Attorney General has made an election under section 50 of the Contraventions Act` (s 145(8)) | JUST FALSE when the "if" fails | NOTHING | defence-if: "it is a lawful excuse ... if" an election is made: not met gives JUST FALSE for this provision's excuse, worded "this section gives no excuse on these facts" (ruling (b) of 2026-11-05 on defences), never "no excuse at all" |
| FA-64 | `s 145(10) the accused may, with leave of the court, require the person who made the certificate to attend for cross-examination` (s 145(10)) | NOTHING | JUST FALSE | power-with-leave: a "may ... with leave of the court" power: the leave is a gate in the text's own wording; without it the answer is NOTHING; the other reading is JUST FALSE |
| FA-65 | `s 145(11) the certificate is barred from reception in evidence for want of reasonable notice before the trial` (s 145(11)) | JUST FALSE when the "unless" is met | NOTHING | bar-unless: a bar closed by "unless": JUST FALSE (the text closes the gate itself) |
| FA-66 | `s 149(1) the court may order that the term of imprisonment for an escape be served in a penitentiary` (s 149(1)) | NOTHING | JUST FALSE | power-scope: a "may" power limited by its scope (a relative clause, "in the same circumstances as", a list: no "if", "where" or "only"): ruling (c) of 2026-11-05 gives NOTHING outside the scope |
| FM-1 | `s 110.4(3), s 117.0104(3): "before the end of the period"` (s 110.4(3), s 117.0104(3)) | strictly before the day the period ends: a hearing on the last day is JUST FALSE | a hearing on the last day of the period is "before the end" | "The date fixed for the hearing must be before the end of the period for which the order ... is in force"; the text does not say whether the last day counts |
| FM-2 | `s 111(5), s 117.05(4)(b): "not exceeding five years" as a Length of time` (s 111(5), s 117.05(4)(b)) | a period is compared in calendar months first (60 months); days count only when the months already equal 60 (5 years and 1 day exceeds; 4 years 11 months and 40 days is read as 59 months) | days converted to a fraction of a month | the Code gives no rule for adding days to months in a period stated in years |
| FM-3 | `s 117.0101(3): "not exceeding 30 days"` (s 117.0101(3)) | a period stated in days only: years 0, months 0, days at most 30; a period of one month is JUST FALSE | one month (28 to 31 days) read as possibly within 30 days | the text states the limit in days |
| FM-4 | `s 111(3), s 117.011(3), s 117.05(3): "Subject to subsection (4)"` (s 111(3), s 117.011(3)) | when the judge proceeds ex parte under subsection (4), the duty to hear the person's evidence answers NOTHING (limited by its own wording) | JUST FALSE (the text closes the duty when (4) applies) | "Subject to" points to an exception without saying "unless" or "only" |
| FM-5 | `s 110.4(4), s 117.0104(4): "as soon as feasible but not later than 15 days before"` (s 110.4(4), s 117.0104(4)) | only the outer limit is encoded (a date test and a regulative rule with WITHIN n MINUS 15); "as soon as feasible" is a judgment with no number | a regulative rule with a second, earlier deadline | the text states no number for "as soon as feasible" |
| FM-6 | `s 117.03(2): "shall without delay be returned"` (s 117.03(2)) | the claim window (14 days after the seizure) is a function with a test on both sides of its end, and a regulative rule (DO ... WITHIN 14 ... LEST FULFILLED); the officer's duty has no WITHIN | WITHIN 0, or a deadline of some days | the text states no period for "without delay" |
| FM-7 | `s 117.03(2), s 117.05(1), s 117.06(1)(a): counting "within 14 days after the seizure" and "within 30 days after the date of execution"` (s 117.03(2), s 117.05(1), s 117.06(1)) | the day of the seizure or execution is day 0, the 14th and the 30th day after it are still within, a date before it is outside | the day of the seizure counts as day 1 | the text says "after the date of execution of the warrant or of the seizure" and "within thirty days after the date" |
| FM-8 | `s 118 "witness"` (s 118 "witness") | the child of tender years who gives unsworn evidence is a witness only when giving it in a judicial proceeding | any child who gives unsworn evidence anywhere | the "includes a child of tender years who gives evidence but does not give it under oath" limb does not repeat "in a judicial proceeding", but "the person presiding" implies a proceeding |
| FM-9 | `s 118: "means ... and includes" and "includes"` (s 118 "witness", s 118 "office", s 118 "official") | "witness means ... and includes" is read as closed (JUST FALSE outside); "office includes" is open (NOTHING outside); "official means a person who (a) holds an office" carries the open "office" through | witness read as open | the keel reads "means ... and includes" as closed (ccc-definitions.l4 header); "includes" alone does not close a list |
| FM-10 | `s 127(1): "other than an order for the payment of money"` (s 127(1)) | an order for the payment of money answers JUST FALSE (the "(other than X)" case, decided at encoding time per the ruling of 2026-11-05T10:25:24Z) | NOTHING (the text restricts the offence rather than saying no) | "disobeys a lawful order made by a court of justice or by a person or body ..., other than an order for the payment of money" |
| FM-11 | `s 126(1), s 127(1): "unless a punishment ... is expressly provided by law"` (s 126(1), s 127(1)) | JUST FALSE where a punishment is expressly provided elsewhere (the text closes the gate with "unless") | NOTHING | the residual offence applies only where nothing else punishes the conduct |
| FM-12 | `compositions of alternative limbs (every offence section with paragraphs (a), (b), (c))` (s 119(1), s 120, s 121(1)...) | the composite is JUST TRUE if any limb is JUST TRUE, and NOTHING otherwise: a limb's JUST FALSE (an exception such as consent) is not carried to the composite, because the text says no to that limb only | JUST FALSE for the composite when a limb says no and no limb says yes | each paragraph is an alternative; the exception sits in its own paragraph. A person who states a limb's exception is told so by the limb's own question where the seat asks it (s 117.01(4), s 121.1(2) and (3), s 131(3), s 134(2), s 141(2), s 145(6) and (8)) |
| FM-13 | `s 145(1): where "without lawful excuse" attaches` (s 145(1)) | only to the second limb (at large before the end of the term); escaping from lawful custody has no excuse element | both limbs | "escapes from lawful custody or who is, before the expiration of a term of imprisonment ..., at large in or outside Canada without lawful excuse" |
| FM-14 | `s 145(8): which paragraphs it reaches` (s 145(8), s 145(2), s 145(5)) | it reaches (2)(a), (3), (4), (5)(a) and (5)(b); the fact that the failure is of a kind (8) lists is asked, so a case outside the kinds answers JUST FALSE for the excuse, never TRUE | not (5)(b), because an order under s 515(12), 516.1(1) or 522(2.1) is not "a condition of an undertaking or release order" | "For the purposes of paragraph (2)(a) and subsections (3) to (5)" |
| FM-15 | `s 145(6): how it limits the lawful excuse` (s 145(6)) | a defective statement of the substance of the alleged offence is not a lawful excuse for (3) and (4): the lawful-excuse element is satisfied when the person has no excuse OR (6) answers JUST TRUE | a separate exception clause that answers JUST FALSE for the excuse | "it is not a lawful excuse that an appearance notice or undertaking states defectively the substance of the alleged offence" |
| FM-16 | `s 117.07(1) etc.: "by reason only that"` (s 117.07(1)) | asked as a fact: "the act is the only reason the person would be guilty of an offence" | left out (the exemption is read as covering the act) | the exemption is of guilt "by reason only that" the person did the listed act |
| FM-17 | `s 117.1: "do not apply if ..."` (s 117.1) | JUST FALSE when the "if" fails (ruling (a) of 2026-11-05: a failed "if" is the text's no, within the provision that holds the "if") | NOTHING | the text says the exemptions "do not apply if" the person is subject to a prohibition order and acts contrary to it; it does not say they apply otherwise |
| FM-18 | `s 113(3)(a) and (b): "Where an order is made under subsection (1)"` (s 113(3)(a), s 113(3)(b)) | both answer JUST FALSE when no order is made ("where", ruling (b) of 2026-11-05): (a) is a bar, (b) a permission closed by "only" and listed in the name-test sweep as a "may" power with a where-kind gate (test 3(i)) | both NOTHING (the line on grants), or (b) alone NOTHING | (a) and (b) share a lead-in; the guide's ruling (b) says JUST FALSE for a failed "where" and its line on grants points to NOTHING for (b) |
| FM-19 | `s 110.4(2)(b), s 117.0104(2)(b): "the Attorney General of the province"` (s 110.4(2)(b), s 117.0104(2)(b)) | the core Party `the Attorney General or Solicitor General of the province` stands for "the Attorney General of the province" (the core has no separate constructor; NEEDS-CORE.md) | a new core constructor | the text names the Attorney General of the province; section 2 "Attorney General" gives "the Attorney General or Solicitor General of the province" |
| FM-20 | `s 117.14(1), (2): orders of the Governor in Council` (s 117.14(1), s 117.14(2)) | encoded for what an amnesty order means to the person in possession (the order declared; its purposes), not as machinery | machinery (reason 2 of the three): an order-making power | the order is what gives the person the protection of s 117.14(3) and (4) |
| FM-21 | `s 111(10), s 117.011(9), s 117.05(9): Part XXVII` (s 111(10), s 117.011(9), s 117.05(9)) | which sections are "of Part XXVII" is an input; the excepted ranges (785 to 812, 816 to 819, 829 to 838) are tested by number; "with such modifications as the circumstances require" is not encoded (the text states none) | a closed list of the applicable sections | the text excepts three ranges and states no others |
| FM-22 | `s 111(4), s 117.011(4), s 117.05(2): "the same circumstances as those in which a summary conviction court may ... proceed with a trial in the absence of the defendant"` (s 111(4), s 117.011(4), s 117.05(2)) | asked as a MAYBE BOOLEAN input named `Part XXVII the circumstances are ...` (ccc29 answers it); a power, NOTHING when not shown | encode the circumstances here | the circumstances are in Part XXVII, outside these ranges |
| FM-23 | `s 117.11: "Where ... any question arises"` (s 117.11) | the offence is tested by section number (89, 90, 91, 93, 97, 101, 104, 105); outside the list NOTHING; inside the list with no question JUST FALSE ("where") | NOTHING when no question arises | ruling (b) of 2026-11-05: a failed "where" is JUST FALSE |
| FM-24 | `s 117.0102(2), (3): dates of expiry` (s 117.0102(2), s 117.0102(3)) | (2) answers a MAYBE BOOLEAN for "expires on the day in question" (JUST FALSE if revoked earlier, NOTHING on another day); (3) answers a MAYBE DATE (NOTHING when no date is fixed: subsection (2) governs) | (2) as a date | the text says "it expires on the day on which the order ... expires or is revoked" |
| FM-25 | `the "whether or not" clauses (s 118 "evidence or statement", s 118 "judicial proceeding", s 118 "witness", s 121(1)(a), s 122, s 131(2), s 131(1.1), s 136(1))` (s 131(2)) | the fact is asked and the answer does not change the result (tested both ways) | left out | "whether or not" says the fact is irrelevant; asking it and ignoring it shows that the encoding read the words |

### Name-test sweep of 2026-11-12

The sweep covers the **48** functions of this part whose name says "may" as a grant or a power (every `DECIDE` name that contains the word).
The three tests are those of the ruling copied at the top of this register.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 12 | 3 | 20 | 0 |

**Flipped to NOTHING (12; test 1).** A function named for a grant whose "if" gate ("if ... believes", "if ... satisfied", "if the judge considers", "with leave of the court") fails answers NOTHING, with one fork row above (`FA-`) and one line in the marginal readings below; the other reading, JUST FALSE, is named in the row.
None of these twelve carries a RECONCILED comment: each answers NOTHING as first written.
- `s 110.4(1) the provincial court judge may fix a date for the hearing of an application under subsection 111(1)`
- `s 111(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order prohibiting a person from possessing weapons`
- `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order`
- `s 117.0101(2) the provincial court judge may hold the hearing in private`
- `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` -- also carries the closed limb of s 117.0101(10) ("only if they are satisfied that there is no other way ..."), which answers JUST FALSE when (10) says no (test 2)
- `s 117.0101(7) the peace officer may search for and seize without a warrant`
- `s 117.0101(9) the provincial court judge may require the person to surrender the things` -- also carries the closed limb of s 117.0101(10) ("only if they are satisfied that there is no other way ..."), which answers JUST FALSE when (10) says no (test 2)
- `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information`
- `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents`
- `s 117.0104(1) the provincial court judge may fix a date for the hearing of an application under subsection 117.011(1)`
- `s 117.13(2) the party against whom a certificate of an analyst is produced may, with leave of the court, require the attendance of the analyst`
- `s 145(10) the accused may, with leave of the court, require the person who made the certificate to attend for cross-examination`

**Kept JUST FALSE, because the text closes the gate itself (3; test 2).**
- `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` -- closed by "only after taking the following factors into account"
- `s 117.0101(10) the judge may issue the warrant or include the requirement to surrender` -- closed by "only if they are satisfied that there is no other way to ensure that the terms and conditions of that order can reasonably be complied with"
- `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` -- closed by "unless its possession by the person in the circumstances in which it is found is authorized by any provision of this Part"; "or the person is under the direct and immediate supervision of another person who may lawfully possess it"

**Listed, not flipped: a "may" function whose gate is "where", "when" or "upon", or a condition of that kind (20; test 3(i)).**
The answer is the one the guide's ruling (b) of 2026-11-05 gives, JUST FALSE; the line on grants points to NOTHING; that is a question for the maintainer or a lawyer, and it is not settled by this sweep.
That a condition introduced by "on application by", "on being issued a receipt", "before or at any time during" or "after affording" goes with the group is ASSUMED, NOT RULED (the sweep file lists such equivalents).
Each function has its own row above (`FA-`, tag `power-where`) and appears here and in that register only.
- `s 110.4(3) the provincial court judge may adjourn the hearing` -- every failed limb answers JUST FALSE
- `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` -- the where-kind limb(s) "Where a provincial court judge makes an order under subsection (5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 111(9) the Attorney General may appeal to the superior court against the decision not to make an order` -- the where-kind limb(s) "Where a provincial court judge does not make an order under subsection (5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 112 a provincial court judge may revoke the order` -- the where-kind limb(s) "on application by the person against whom an order is made under subsection 110.1(3) or 111(5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` -- every failed limb answers JUST FALSE
- `s 113(3)(b) the authorization or licence may be issued to the person for the duration of the order` -- every failed limb answers JUST FALSE
- `s 127(2) proceedings for contravening or conspiring to contravene the order may be instituted and conducted at the instance of the Government of Canada` -- every failed limb answers JUST FALSE
- `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` -- the where-kind limb(s) "on being issued a receipt for it"; "before the expiry or revocation of the order made under subsection (3)" answer JUST FALSE; the other limbs answer NOTHING
- `s 117.0104(3) the provincial court judge may adjourn the hearing` -- every failed limb answers JUST FALSE
- `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` -- every failed limb answers JUST FALSE
- `s 117.011(7) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` -- the where-kind limb(s) "Where a provincial court judge makes an order under subsection (5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 117.011(8) the Attorney General may appeal to the superior court against the decision not to make an order` -- the where-kind limb(s) "Where a provincial court judge does not make an order under subsection (5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 117.012 a provincial court judge may revoke the order` -- the where-kind limb(s) "on application by the person against whom an order is made under subsection 117.0101(3) or 117.011(5)" answer JUST FALSE; the other limbs answer NOTHING
- `s 117.02(1) the peace officer may search without a warrant and seize` -- every failed limb answers JUST FALSE
- `s 117.03(3) the provincial court judge may declare the thing forfeited to Her Majesty` -- every failed limb answers JUST FALSE
- `s 117.04(1) the justice may issue a warrant authorizing a peace officer to search the building, receptacle or place and seize` -- every failed limb answers JUST FALSE
- `s 117.04(2) the peace officer may search for and seize without a warrant` -- every failed limb answers JUST FALSE
- `s 117.05(7) the person may appeal to the superior court against the order` -- the where-kind limb(s) "Where a justice makes an order under subsection (4) in respect of a person, or in respect of any thing that was seized from a person" answer JUST FALSE; the other limbs answer NOTHING
- `s 117.05(8) the Attorney General may appeal to the superior court against the failure to make the finding or the order` -- every failed limb answers JUST FALSE
- `s 117.06(2) the justice may order that the revocation be reversed and the authorization, licence or registration certificate restored` -- every failed limb answers JUST FALSE

Eight of these answer JUST FALSE on a where-kind limb that is worded "on application by", "on being issued a receipt", "before ...", "after affording" or "before or at any time during": `s 110.4(3)`, `s 117.0104(3)`, `s 112`, `s 117.012`, `s 113(3)(b)` (the permission to issue), `s 117.0101(11)`, `s 117.03(3)` and `s 127(2)`.
Every assertion on them whose answer changed (NOTHING to JUST FALSE) is restated in place with `-- RECONCILED 2026-11-12: was ...`, in the tests and in the seat cases; no input order or export signature changed, so no other assertion line differs.
Three of the eight rest on a literal "Where" (`s 113(3)(b)`, `s 117.03(3)`, `s 127(2)`); the other five rest on the equivalents that are ASSUMED, NOT RULED, to go with the group (`s 110.4(3)`, `s 117.0104(3)`, `s 112`, `s 117.012`, `s 117.0101(11)`), so those five are the ones to reverse if the equivalents are ruled out.
`s 112`, `s 117.012` and `s 117.0101(11)` also have an "if" limb ("if satisfied that the circumstances ... have ceased to exist"; "if the officer has reasonable grounds"), which still answers NOTHING; they are counted in the "listed" column for their where-kind limb.

**Listed: "entitled"-named functions (0; test 3(ii)).** None: no function of this part is named "entitled", "is permitted to" or "has power to" as a grant.

**Outside the sweep: named "it is lawful": 0.** Scoped ("s N makes it lawful ..."): 0. Unscoped and retitled to the scoped form: 0. No function of this part has a name of that kind, so none was retitled and no answer changed.
The nearest names, `s 145(6)` ("is not a lawful excuse") and `s 145(8)` ("is with lawful excuse because the Attorney General has made an election"), are a limit on an element of an offence and a defence; they are scoped by their own wording and were not touched.

**Not in any of the columns.** 13 "may" functions answer NOTHING outside their scope, a relative clause, a list the text does not close, or "in the same circumstances as ...", with no "if", "where", "when", "upon" or "only" to test (ruling (c) of 2026-11-05):
- `s 111(4) the provincial court judge may proceed ex parte to hear and determine the application`
- `s 113(3)(b) the chief firearms officer may attach further terms and conditions to the authorization or licence`
- `s 113(4) an order under subsection (1) may be made during the proceedings`
- `s 114 the competent authority may require the person to surrender the things and documents`
- `s 126(2) proceedings may be instituted at the instance of the Government of Canada`
- `s 117.0102(5) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge`
- `s 117.0103(2) the order may be for any period, definite or indefinite, that the judge considers necessary`
- `s 117.0103(4) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge`
- `s 117.011(4) the provincial court judge may proceed ex parte to hear and determine the application`
- `s 117.05(2) the justice may proceed ex parte to hear and determine the application`
- `s 117.09(7) the provincial minister may attach a condition to the designation`
- `s 117.14(1) the Governor in Council may declare an amnesty period`
- `s 149(1) the court may order that the term of imprisonment for an escape be served in a penitentiary`
Also named "may" and outside the three tests: 2 regulative rules (each has an asserted decision-function twin and no JUST FALSE or NOTHING answer): `s 117.03(2) the person may claim the thing within 14 days and the officer must then return it`; `s 117.05(1) the peace officer may apply within 30 days and the justice must then fix a date for the hearing`; and 1 definition that contains the word without granting anything: `s 118(e) before a tribunal by which a legal right or legal liability may be established`.
The words "permitted", "power", "entitled" and "authorized" also occur in 6 other names, as elements of an offence, a definition or a limit, never as a grant (s 118(b), s 118(d), s 127(1), s 131(3), s 134(1), s 146(c)).

## Jural relations (ccc5)

Hohfeld's correlatives: right (claim) / duty; privilege (liberty) / no-right; power / liability; immunity / disability. A provision that creates no relation (a definition, a rule of reading or of procedure) is listed once as `none`. The names of the L4 rules are the label of the provision followed by its title (see Coverage for every name).

| provision | holder | relation | bearer of the correlative | L4 rule |
| --- | --- | --- | --- | --- |
| s 110.4(1) | a provincial court judge | power (to fix a hearing date) | the person against whom a s 111(5) order is sought (liability) | `s 110.4(1) the provincial court judge may fix a date for the hearing of an application under subsection 111(1)` |
| s 110.4(1) | the person against whom a s 111(5) order is sought | right (to notice of the hearing) | a provincial court judge (duty to direct notice) | `s 110.4(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` |
| s 110.4(2) | none | none: a rule of deeming and of substitution of the applicant (who becomes applicant is computed) | none | (see Coverage) |
| s 110.4(3) | a provincial court judge, on application | power (to adjourn) | the applicant and the person (liability) | `s 110.4(3) the provincial court judge may adjourn the hearing` |
| s 110.4(3) | the person against whom the emergency order is made | right (hearing fixed before the end of the period) | a provincial court judge (duty) | `s 110.4(3) the date fixed for the hearing is before the end of the period of the order` |
| s 110.4(4) | the Attorney General who becomes the applicant | right (to notice not later than 15 days before the date fixed) | a provincial court judge (duty) | `s 110.4(4) the provincial court judge is bound to cause notice to be served on the Attorney General` |
| s 110.4(5) | the person against whom the emergency order was made | right (to have the hearing cancelled once the order is revoked) | a provincial court judge (duty) | `s 110.4(5) the provincial court judge is bound to cancel the hearing` |
| s 111(1) | a peace officer, firearms officer or chief firearms officer | power (to apply for a prohibition order) | the person against whom the order is sought (liability) | `s 111(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order prohibiting a person from possessing weapons` |
| s 111(2) | the person against whom the order is sought | right (to a hearing date and notice) | a provincial court judge (duty) | `s 111(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` |
| s 111(3) | the applicant and the person against whom the order is sought | right (to have all relevant evidence heard) | a provincial court judge (duty) | `s 111(3) the provincial court judge is bound to hear all relevant evidence presented by or on behalf of the applicant and the person` |
| s 111(4) | a provincial court judge | power (to proceed ex parte) | the person against whom the order is sought, when absent (liability) | `s 111(4) the provincial court judge may proceed ex parte to hear and determine the application` |
| s 111(5) | a provincial court judge | power (to prohibit possession for up to five years) and, for the applicant, a claim to the order once satisfied | the person against whom the order is made (liability); the judge (duty) | `s 111(5) the provincial court judge is bound to make an order prohibiting the person from possessing the things` |
| s 111(6) | the person and the Attorney General | right (to reasons on the record) | a provincial court judge (duty) | `s 111(6) the provincial court judge is bound to include a statement of reasons in the record` |
| s 111(7) | none | none: a rule of extension (ss 113 to 117 apply) | none | `s 111(7) sections 113 to 117 apply to the order, tested by section number` |
| s 111(8), s 111(9) | the person to whom the order relates, and the Attorney General | power (to appeal to the superior court) | the order and the other party (liability) | `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` |
| s 111(10) | none | none: a rule of procedure (Part XXVII, with its exceptions) | none | `s 111(10) the provision of Part XXVII applies to the appeal` |
| s 112 | a provincial court judge, on the person's application | power (to revoke the order); the person has a privilege to apply | the order and those it binds (liability) | `s 112 a provincial court judge may revoke the order` |
| s 113(1) | the competent authority | power (to authorize a licence for sustenance or employment); the person has a privilege to ask | the person, a chief firearms officer and the Registrar (liability) | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` |
| s 113(2) | the person | immunity (from an order lifting made without the factors considered) | the competent authority (disability) | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| s 113(3) | the person in whose favour the order is made | immunity (from denial solely on the prohibition order) and a privilege (to hold the licence for the stated purposes) | a chief firearms officer (disability, no-right) | (see Coverage) |
| s 113(4), s 113(5) | none | none: for greater certainty; a definition | none | `s 113(4) an order under subsection (1) may be made during the proceedings` |
| s 114 | the competent authority | power (to require surrender) | the person (liability) | `s 114 the competent authority may require the person to surrender the things and documents` |
| s 114 | the person | right (to a reasonable period) and privilege (s 117.01 does not apply in it) | the competent authority (duty); the Crown (no-right) | `s 114 the authority is bound to specify in the order a reasonable period for surrendering` |
| s 115 | Her Majesty; the Attorney General | claim (to forfeited things) and power (to direct their disposal) | the person whose things are forfeited (duty, liability) | (see Coverage) |
| s 116 | the state, by operation of law | power exercised by the Code itself (revocation or amendment on commencement) | the holder of the authorization, licence or registration certificate (liability) | (see Coverage) |
| s 117 | the owner who is not the prohibited person | right (to return, proceeds or value) | the competent authority (duty) | `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid` |
| s 117.01 | the Crown | claim (that a prohibited person not possess, and surrender when required) | the person prohibited (duty, SHANT); (4): the person holding a licence issued under a s 113(1) order has a privilege | (see Coverage) |
| s 117.0101(1), s 117.0101(2) | any person (applicant); a provincial court judge (private hearing) | power | the person against whom the order is sought (liability) | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` |
| s 117.0101(3), (4), (5) | the applicant and others protected; the person against whom the order is made | claim (to an order); right (to be served, to the least intrusive terms) | a provincial court judge (duty) | `s 117.0101(3) the provincial court judge is bound to make an emergency limitations on access order`; `s 117.0101(3) the period of the order is not more than 30 days` |
| s 117.0101(6), (7), (9), (10) | a provincial court judge; a peace officer | power (warrant, warrantless search, surrender), limited by (10) | the person subject to the order (liability) | `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` |
| s 117.0101(8) | a justice | claim (to an immediate report) | a peace officer (duty) | `s 117.0101(8) the peace officer is bound to make a report immediately to a justice having jurisdiction`; `s 117.0101(8) the report shows what the subsection requires` |
| s 117.0101(11), (12) | the person subject to the order | right (to return of the things, after expiry or revocation) | a peace officer, firearms officer or chief firearms officer (duty; (11): power) | `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` |
| s 117.0102 | the applicant and a provincial court judge | power (to deny access to information); the order expires as (2) and (3) say | the public, the person subject to the order (liability) | (see Coverage) |
| s 117.0103 | a provincial court judge, on application | power (to order identifying information deleted); duty to seal | the public (liability); the judge (duty) | (see Coverage) |
| s 117.0104 | as s 110.4, for orders under s 117.011(5) | as s 110.4(1) to (5) | as s 110.4(1) to (5) | (see Coverage) |
| s 117.011 | as s 111, for orders limiting access | as s 111(1) to (9) | as s 111(1) to (9) | (see Coverage) |
| s 117.012 | a provincial court judge, on the person's application | power (to revoke) | the order and those it binds (liability) | `s 117.012 a provincial court judge may revoke the order` |
| s 117.02 | a peace officer | power (search and seizure without warrant) | the person, vehicle or premises searched (liability); the person has a privilege against it in a dwelling-house | (see Coverage) |
| s 117.03 | a peace officer; the person | power (to seize); right (to return on a claim within 14 days with the licence); a provincial court judge: power (to declare forfeiture) | the person (liability); the peace officer (duty to return) | (see Coverage) |
| s 117.04 | a justice; a peace officer | power (warrant; warrantless seizure); claim (to a report) | the person searched (liability); the peace officer (duty to report) | (see Coverage) |
| s 117.05 | a peace officer; a justice; the person; the Attorney General | power (to apply within 30 days; to proceed ex parte; to forfeit and prohibit up to five years); right (to be heard, to appeal) | the person (liability); the justice (duty) | (see Coverage) |
| s 117.06 | the person from whom a thing was seized | right (to return if no application in 30 days or no finding) | the peace officer (duty); the justice: power (to restore authorizations) | (see Coverage) |
| s 117.07 | a public officer (as s 117.07(2) defines it) | immunity (from guilt by reason only of listed acts in the course of duties) | the Crown (disability to convict) | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| s 117.071, s 117.08, s 117.09 | a preclearance officer; an individual acting for a police force or department; a licensed business's employee; a carrier's employee; a museum's employee | immunity | the Crown (disability to convict) | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| s 117.09(6), (7) | the person who may be designated | immunity (from designation where not desirable) and a liability to conditions | a provincial minister (disability; power) | `s 117.09(6) the provincial minister is barred from designating the individual for the purpose of subsection (5)` |
| s 117.1 | the Crown | power to prosecute despite ss 117.07 to 117.09 (they do not apply) | the prohibited person who acts contrary to the order (liability) | `s 117.1 sections 117.07 to 117.09 do not apply to the person` |
| s 117.11 | the Crown | claim (that the accused prove the holding of the authorization, licence or registration certificate) | the accused (duty: the onus) | `s 117.11 the onus is on the accused to prove that the person is the holder of the authorization, licence or registration certificate` |
| s 117.12 | the party tendering the document | privilege (to rely on the document as evidence) | the opposing party (no-right) | (see Coverage) |
| s 117.13 | the party tendering an analyst's certificate; the party against whom it is produced | privilege (certificate as evidence); power (to require the analyst, with leave); claim (to notice before trial) | the opposing party; the court; the party tendering (duty to give notice) | (see Coverage) |
| s 117.14(1), (2) | the Governor in Council | power (to declare an amnesty period) | persons in possession of the things (liability) | `s 117.14(1) the Governor in Council may declare an amnesty period` |
| s 117.14(3), (4) | a person who acts in reliance on an amnesty order | immunity (from guilt under Part III); proceedings are a nullity | the Crown (disability) | `s 117.14(3) the person is not guilty of an offence under this Part by reason only of doing a thing provided for in an amnesty order` |
| s 117.15 | none (machinery: regulation-making power) | none | none | (see Coverage) |
| s 118 | none | none: definitions (evidence or statement, government, judicial proceeding, office, official, witness) | none | `s 118 evidence or statement`; `s 118 body` |
| s 119 | the Crown | claim (that judicial officers and legislators not take, and no one give, corrupt benefits); (2) the holder of a judicial office has an immunity from proceedings without the written consent of the Attorney General of Canada | the person (duty, SHANT); the Crown (disability under (2)) | (see Coverage) |
| s 120, s 121, s 121.1, s 122, s 123, s 124, s 125 | the Crown | claim (against bribery of officers, frauds on the government, unstamped tobacco dealing, breach of trust, municipal corruption, trading in offices) | the person (duty, SHANT) | `s 120 the person is guilty of an indictable offence under section 120` |
| s 126, s 127 | the Crown; the Government of Canada ((2): power to institute and conduct proceedings) | claim (obedience to Acts and court orders); power | the person (duty); the person (liability) | (see Coverage) |
| s 128, s 129, s 130, s 130.1 | the Crown; the court (130.1: the sentencing court is bound) | claim (against misconduct in executing process, resisting or obstructing officers, personation); duty of the court to treat personation as aggravating | the peace officer or coroner; the person; the accused (liability to the aggravating circumstance) | `s 128 the person is guilty of an offence under section 128` |
| s 131, s 132, s 134 | the Crown | claim (against perjury and unsworn false statements); (131(3), 134(2)) privileges for statements not specially permitted or made in a criminal investigation | the person (duty, SHANT) | `s 131 the person commits perjury` |
| s 133 | the accused | immunity (from conviction for perjury on one witness's uncorroborated evidence) | the court and the Crown (disability) | `s 133 the accused is barred from being convicted of perjury on the evidence of only one witness unless it is corroborated in a material particular` |
| s 136 | the Crown; the accused | claim (against contradictory evidence); immunity (no conviction without proof beyond reasonable doubt of intent to mislead; no proceedings without the Attorney General's consent) | the witness (duty); the court and the Crown (disability) | (see Coverage) |
| s 137, s 138, s 139, s 140, s 141, s 142 | the Crown | claim (against fabricating evidence, false affidavits, obstructing justice, public mischief, compounding, taking a reward for recovery); (141(2)) privilege to receive consideration under a diversion agreement | the person (duty, SHANT) | `s 137 the person fabricates anything to be used as evidence in a judicial proceeding`; `s 137 the class of the offence` |
| s 144, s 145, s 146, s 147, s 148 | the Crown | claim (against prison breach, escape, failing to attend or comply, permitting or assisting escape, rescue) | the person (duty); (145(6), (8)) the person has a privilege where a lawful excuse is given by the text | `s 144 the person is guilty of an offence under section 144` |
| s 145(9), (10), (11) | the Crown (certificate evidence); the accused (leave to cross-examine; notice) | privilege; power (with leave); claim (to notice before trial) | the accused; the court; the party producing (duty) | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| s 149 | a court that convicts a person for an escape | power (to order the term served in a penitentiary even if under two years) | the convicted person (liability) | (see Coverage) |

## Marginal readings for a lawyer (ccc5)

Readings (a) and (b) of the brief are taken as the status quo: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Every branch that rests on one is listed here, with the other reading.

**Reading (a), duties, bars and conditions closed by "if", "where", "only", "during which" or a period (32 functions answering JUST FALSE when the gate fails).** The other reading is NOTHING (an inference "if A then B" is not "if not A then not B").

- `s 110.4(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` -- s 110.4(1): "If a provincial court judge makes an order under subsection 110.1(3)"
- `s 110.4(4) the provincial court judge is bound to cause notice to be served on the Attorney General` -- s 110.4(4): "If the Attorney General becomes, under paragraph (2)(b), the applicant"
- `s 110.4(5) the provincial court judge is bound to cancel the hearing` -- s 110.4(5): "If a provincial court judge revokes an order made under subsection 110.1(3)"
- `s 111(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` -- s 111(2): "On receipt of an application made under subsection (1)"
- `s 111(5) the provincial court judge is bound to make an order prohibiting the person from possessing the things` -- s 111(5): "If, at the conclusion of a hearing of an application made under subsection (1), the provincial court judge is satisfied that the circumstances referred to in that subsection exist"
- `s 111(6) the provincial court judge is bound to include a statement of reasons in the record` -- s 111(6): "Where a provincial court judge does not make an order under subsection (1)"
- `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` -- s 113(2): "only after taking the following factors into account"
- `s 114 the authority is bound to specify in the order a reasonable period for surrendering` -- s 114: "where the competent authority does so"
- `s 114 section 117.01 does not apply to the person during the specified period` -- s 114: "during which section 117.01 does not apply to that person"
- `s 116(2) the authorization, licence or registration certificate remains revoked or amended` -- s 116(2): "only in respect of the period during which the order is in force"
- `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid` -- s 117: "on application for an order under this section, satisfied that a person"
- `s 130.1 the sentencing court is bound to treat as aggravating that the accused personated an officer to facilitate another offence` -- s 130.1: "If a person is convicted of an offence under section 130"
- `s 117.0101(3) the provincial court judge is bound to make an emergency limitations on access order` -- s 117.0101(3): "If, at the conclusion of a hearing of an application made under subsection (1), the provincial court judge is satisfied that the circumstances referred to in that subsection exist and that an order should be made without delay to ensure the immediate protection of any person"
- `s 117.0101(10) the judge may issue the warrant or include the requirement to surrender` -- s 117.0101(10): "only if they are satisfied that there is no other way to ensure that the terms and conditions of that order can reasonably be complied with"
- `s 117.0101(9) the judge is bound to specify in the order a reasonable period for surrendering the thing` -- s 117.0101(9): "if the judge does so"
- `s 117.0102(4) the documents are to be placed in a packet and sealed by the judge` -- s 117.0102(4): "If an order is made under subsection (1)"
- `s 117.0103(3) the originals of the documents are to be placed in a packet and sealed by the judge` -- s 117.0103(3): "If an order is made under subsection (1)"
- `s 117.0104(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` -- s 117.0104(1): "If a provincial court judge makes an order under subsection 117.0101(3)"
- `s 117.0104(4) the provincial court judge is bound to cause notice to be served on the Attorney General` -- s 117.0104(4): "If the Attorney General becomes, under paragraph (2)(b), the applicant"
- `s 117.0104(5) the provincial court judge is bound to cancel the hearing` -- s 117.0104(5): "If a provincial court judge revokes an order made under subsection 117.0101(3)"
- `s 117.011(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` -- s 117.011(2): "On receipt of an application made under subsection (1)"
- `s 117.011(5) the provincial court judge is bound to make an order imposing terms and conditions on the person's use and possession` -- s 117.011(5): "Where, at the conclusion of a hearing of an application made under subsection (1), the provincial court judge is satisfied that the circumstances referred to in that subsection exist"
- `s 117.03(2) the thing is to be returned without delay` -- s 117.03(2): "If a person from whom any thing is seized under subsection (1) claims the thing within 14 days after the seizure and produces"
- `s 117.03(3) the peace officer is bound to take the thing forthwith before a provincial court judge` -- s 117.03(3): "Where any thing seized pursuant to subsection (1) is not claimed and returned as and when provided by subsection (2)"
- `s 117.04(4) every authorization, licence and registration certificate held by the person is revoked as at the time of the seizure` -- s 117.04(4): "Where a peace officer who seizes any thing under subsection (1) or (2) is unable at the time of the seizure"
- `s 117.05(1) the justice is bound to fix a date for the hearing and direct that notice of it be given` -- s 117.05(1): "If any thing or document has been seized under subsection 117.04(1) or (2)"
- `s 117.05(4)(a) the justice is bound to order that any thing seized be forfeited to Her Majesty or otherwise disposed of` -- s 117.05(4): "If, following the hearing of an application made under subsection (1), the justice finds"
- `s 117.05(4)(b) the justice is bound to order that the person's possession be prohibited` -- s 117.05(4)(b): "where the justice is satisfied that the circumstances warrant such an action"
- `s 117.05(5) the justice is bound to include a statement of reasons in the record` -- s 117.05(5): "Where a justice does not make an order under subsection (4)"
- `s 117.06(1) the thing or document is to be returned to the person from whom it was seized` -- s 117.06(1): "shall be returned to the person from whom it was seized if"
- `s 117.1 sections 117.07 to 117.09 do not apply to the person` -- s 117.1: "do not apply if"
- `s 117.07(2) public officer` -- s 117.07(2): "In this section, public officer means"

**Closed "means" definitions (4 functions answering JUST FALSE for a case outside the definition).** A definition that says "means" is the text's own closed list, so a case outside it is JUST FALSE; the other reading is NOTHING where a term inside the definition is itself open.

- `s 113(5) competent authority` -- s 113(5): "means the competent authority that made or has jurisdiction to make the prohibition order"
- `s 118 evidence or statement` -- s 118 "evidence or statement": "means an assertion of fact, opinion, belief or knowledge"
- `s 123(3) municipal official` -- s 123(3): "means a member of a municipal council or a person who holds an office under a municipal government"
- `s 149(2) escape` -- s 149(2): "means breaking prison, escaping from lawful custody or, without lawful excuse, being at large before the expiration of a term of imprisonment to which a person has been sentenced"

**Flat negatives, "unless", "except", "only", "so long as" and exceptions (49 functions with an exception or a closed gate).** JUST FALSE where the exception holds. The other reading is NOTHING.

- `s 110.4(2)(a) the application for the order under subsection 110.1(3) is deemed an application made under subsection 111(1)` -- "except for the purpose of subsection 111(2)"
- `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` -- "Where a provincial court judge makes an order under subsection (5)"
- `s 111(9) the Attorney General may appeal to the superior court against the decision not to make an order` -- "Where a provincial court judge does not make an order under subsection (5)"
- `s 112 a provincial court judge may revoke the order` -- "on application by the person against whom an order is made under subsection 110.1(3) or 111(5)"
- `s 113(3)(a) an authorization, licence or registration certificate is barred from being denied solely on the basis of the prohibition order or the offence` -- "Where an order is made under subsection (1)"
- `s 113(3)(b) the authorization or licence may be issued to the person for the duration of the order` -- "only for sustenance or employment purposes"; "only in accordance with those terms and conditions"
- `s 115(1) the thing is forfeited to Her Majesty` -- "Unless a prohibition order against a person specifies otherwise"; "does not apply"
- `s 119(2) the proceedings against a holder of a judicial office are barred for want of the written consent of the Attorney General of Canada` -- "without the consent in writing of the Attorney General of Canada"
- `s 121(1)(b) the person having dealings with the government pays or confers a benefit on its employee or official without written consent` -- "unless the person has the consent in writing of the head of the branch of government with which the dealings take place"
- `s 121(1)(c) the official or employee of the government takes a benefit from a person dealing with it without written consent` -- "unless they have the consent in writing of the head of the branch of government that employs them or of which they are an official"
- `s 121.1(1) the person deals in unstamped tobacco` -- "unless it is stamped"; "Subsection (1) does not apply"; "does not contravene subsection (1)"
- `s 126(1) the person is guilty of an offence by intentionally contravening an Act of Parliament` -- "unless a punishment is expressly provided by law"
- `s 127(1) the person is guilty of an offence by disobeying a lawful order of a court or authorized body` -- "other than an order for the payment of money"; "unless a punishment or other mode of proceeding is expressly provided by law"
- `s 117.01(1) the person possesses a prohibited thing while prohibited from doing so by an order` -- "does not apply"
- `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` -- "only if they are satisfied that there is no other way to ensure that the terms and conditions of that order can reasonably be complied with"
- `s 117.0101(9) the provincial court judge may require the person to surrender the things` -- "only if they are satisfied that there is no other way to ensure that the terms and conditions of that order can reasonably be complied with"
- `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` -- "on being issued a receipt for it"; "before the expiry or revocation of the order made under subsection (3)"
- `s 117.0101(12) the things are to be returned to the person` -- "unless already returned under subsection (11)"
- `s 117.0104(2)(a) the application for the order under subsection 117.0101(3) is deemed an application made under subsection 117.011(1)` -- "except for the purpose of subsection 117.011(2)"
- `s 117.011(7) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` -- "Where a provincial court judge makes an order under subsection (5)"
- `s 117.011(8) the Attorney General may appeal to the superior court against the decision not to make an order` -- "Where a provincial court judge does not make an order under subsection (5)"
- `s 117.012 a provincial court judge may revoke the order` -- "on application by the person against whom an order is made under subsection 117.0101(3) or 117.011(5)"
- `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` -- "unless its possession by the person in the circumstances in which it is found is authorized by any provision of this Part"; "or the person is under the direct and immediate supervision of another person who may lawfully possess it"
- `s 117.05(7) the person may appeal to the superior court against the order` -- "Where a justice makes an order under subsection (4) in respect of a person, or in respect of any thing that was seized from a person"
- `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` -- "do not apply"
- `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` -- "do not apply"
- `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` -- "do not apply"
- `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` -- "do not apply"
- `s 117.09(2) the employee of a licensed business is not guilty of an offence by reason only of dealing with a partially manufactured barrelled weapon` -- "do not apply"
- `s 117.09(3) the employee of a carrier is not guilty of an offence by reason only of possessing or transferring the listed things in their duties` -- "do not apply"
- `s 117.09(4) the employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a functioning imitation antique firearm` -- "do not apply"
- `s 117.09(5) the designated employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a firearm` -- "do not apply"
- `s 117.12(2) the certified copy has the same probative force as the original would have had` -- "in the absence of evidence to the contrary"
- `s 117.13(3) the certificate of an analyst is barred from admission for want of reasonable notice before the trial` -- "unless the party intending to produce it has, before the trial, given to the party against whom it is intended to be produced reasonable notice of that intention together with a copy of the certificate"
- `s 131(1) the person commits perjury by a false statement under oath or solemn affirmation` -- "do not apply"
- `s 131(1.1) the person commits perjury by a false statement given by video link or under a mutual legal assistance order` -- "so long as the false statement was made in accordance with any formalities required by the law of the place outside Canada in which the person is virtually present or heard"; "do not apply"
- `s 133 the accused is barred from being convicted of perjury on the evidence of only one witness unless it is corroborated in a material particular` -- "unless the evidence of that witness is corroborated in a material particular by evidence that implicates the accused"
- `s 134(1) the person makes a false statement under oath or solemn affirmation without being permitted, authorized or required by law` -- "does not apply"
- `s 136(2) the evidence is evidence for the purposes of section 136` -- "does not include evidence that is not material"
- `s 136(1) the witness is guilty of giving contradictory evidence` -- "unless the court, judge or provincial court judge, as the case may be, is satisfied beyond a reasonable doubt that the accused, in giving evidence in either of the judicial proceedings, intended to mislead"
- `s 136(3) the proceedings are barred for want of the consent of the Attorney General` -- "without the consent of the Attorney General"
- `s 141(1) the person asks for or obtains valuable consideration for agreeing to compound or conceal an indictable offence` -- "No offence is committed"
- `s 145(2)(a) the person at large on a release order fails without lawful excuse to attend court` -- "it is a lawful excuse"
- `s 145(3) the person named in an appearance notice or served with a summons fails without lawful excuse to appear or attend` -- "it is a lawful excuse"
- `s 145(4)(a) the person at large on an undertaking fails without lawful excuse to comply with a condition` -- "it is a lawful excuse"
- `s 145(4)(b) the person at large on a confirmed undertaking fails without lawful excuse to appear or attend` -- "it is a lawful excuse"
- `s 145(5)(a) the person at large on a release order fails without lawful excuse to comply with a condition other than to attend court` -- "it is a lawful excuse"
- `s 145(5)(b) the person bound by an order under section 515(12), 516.1(1) or 522(2.1) fails without lawful excuse to comply` -- "it is a lawful excuse"
- `s 145(11) the certificate is barred from reception in evidence for want of reasonable notice before the trial` -- "unless the party intending to produce it has, before the trial, given to the accused reasonable notice of his intention together with a copy of the certificate"

**Reading (b), by tag.** The functions below answer as the tag says; each also has a row in the fork register (`FA-`).
The 20 "may" functions whose gate is "where", "when" or "upon" (tag `power-where`) are in the fork register only, and are listed in the name-test sweep subsection below.

- `bar-unless` (3): answer taken JUST FALSE when the "unless" is met; other reading NOTHING. `s 117.13(3)`, `s 133`, `s 145(11)`
- `bar-where` (2): answer taken JUST FALSE when the "where" fails; other reading NOTHING. `s 113(3)(a)`, `s 117.09(6)`
- `bar-without` (2): answer taken JUST FALSE when consent was given; other reading NOTHING. `s 119(2)`, `s 136(3)`
- `defence-if` (1): answer taken JUST FALSE when the "if" fails; other reading NOTHING. `s 145(8)`
- `immunity` (7): answer taken NOTHING when the gate fails; other reading JUST FALSE. `s 117.07`, `s 117.071`, `s 117.09(1)`, `s 117.09(2)`, `s 117.09(3)`, `s 117.09(4)`, `s 117.14(3)`
- `immunity-if` (2): answer taken NOTHING when the "if" fails; other reading JUST FALSE. `s 117.08`, `s 117.09(5)`
- `list-open` (3): answer taken NOTHING outside the list; other reading JUST FALSE. `s 113(4)`, `s 117.14(2)`, `s 139(3)`
- `power-if` (10): answer taken NOTHING; other reading JUST FALSE. `s 110.4(1)`, `s 111(1)`, `s 117.0101(1)`, `s 117.0101(2)`, `s 117.0101(6)`, `s 117.0101(7)`, `s 117.0101(9)`, `s 117.0102(1)`, `s 117.0103(1)`, `s 117.0104(1)`
- `power-scope` (12): answer taken NOTHING; other reading JUST FALSE. `s 111(4)`, `s 113(3)(b)`, `s 114`, `s 126(2)`, `s 117.0102(5)`, `s 117.0103(2)`, `s 117.0103(4)`, `s 117.011(4)`, `s 117.05(2)`, `s 117.09(7)`, `s 117.14(1)`, `s 149(1)`
- `power-unless` (1): answer taken JUST FALSE when the "unless" is met; other reading JUST FALSE is not a bar on the whole power. `s 117.03(1)`
- `power-with-leave` (2): answer taken NOTHING; other reading JUST FALSE. `s 117.13(2)`, `s 145(10)`
- `where-exception` (1): answer taken JUST FALSE when the "where" fails; other reading NOTHING. `s 141(2)`

**Hand-written functions with a JUST FALSE branch** (periods and dates, ranges of section numbers, lists): s 110.4(3), s 110.4(4), s 111(5) (length; start), s 111(10) / s 117.011(9) / s 117.05(9) (the excepted ranges, "except"), s 117.0101(3) (length; start), s 117.0102(2) ("Unless ... revoked earlier"), s 117.03(2) (the 14 days), s 117.05(1) (the 30 days), s 117.05(4)(b) (length), s 117.06(1)(a), s 117.11 ("Where ... any question arises"), s 118 (the five closed "means" definitions), s 123(3). Each has the quoted words beside the branch in the L4. The other reading is NOTHING for each.

**Composition of alternative limbs (FM-12).** The composite answer of an offence with paragraphs is JUST TRUE or NOTHING, never JUST FALSE: a limb's own JUST FALSE is not carried up. This loses information for a person who states an exception (consent, a licence under a s 113(1) order) and asks only the composite question; the exception's own question, where the seat has one, answers it.

### Reading a result: FALSE and NOTHING (ccc5)

In this part a **JUST TRUE** answers the question the name asks: an offence is made out, a duty falls on the judge or officer, a bar operates, an exemption holds, a thing is to be returned.
A **JUST FALSE** is the text's own "no" to the case, in its own words, and only there: an exception ("does not apply", "No offence is committed where", "unless the person has the consent in writing", "except for the purpose of subsection ..."); a closed gate ("only after", "only if", "only for sustenance or employment purposes"); a flat negative ("is not a lawful excuse"); a "means" definition the case falls outside ("official means a person who"); a duty or bar whose "If" or "Where" is not met (reading (a)); a period the text fixes in its own words ("within 14 days after the seizure", "not exceeding five years", "for a period not exceeding 30 days") when the case is outside it.
A **NOTHING** is "not covered", and never "no": the section limits its prohibition or grant in its own wording and the person's facts fall outside the limit (every offence limb whose elements are not all present); the section says "includes" and lists without closing ("office includes", "Without restricting the generality of subsection (2)"); the section is silent (no rule for how a period of years and days is compared); the answer lies outside the sources (the Excise Act, 2001, the Firearms Act, the Preclearance Act, the Visiting Forces Act, section 787(1), Part XXVII, section 2); or a "may" power whose "if" gate fails (ruling of 2026-11-12).
A caller must never turn NOTHING into FALSE: a person told NOTHING is told that the text does not decide the point on those facts, not that no offence was committed. Section 2 answers taken as inputs keep the same rule: a limb tests them with `EQUALS JUST TRUE`, and a negated element ("not being a peace officer") tests `EQUALS JUST FALSE`, so an undetermined section 2 answer stays NOTHING.
Every branch that answers JUST FALSE carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers NOTHING carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording. The quoted words of every JUST FALSE branch of a generated function were checked against the quoted source lines by the generator before the file was written.

## Seams (ccc5)

Inputs this part takes (each is a `GIVEN` of the function that needs it; the lead joins them at the merge):

| input | type | taken from | used by (labels) |
| --- | --- | --- | --- |
| `Part XXVII the circumstances are those in which a summary conviction court may proceed with a trial in the absence of the defendant` | MAYBE BOOLEAN | ccc29 (Part XXVII) | s 111(4), s 117.011(4), s 117.05(2) |
| `s 110.1 an emergency prohibition order has been made` | MAYBE BOOLEAN | ccc4 (s 110.1) | s 110.4(1) |
| `s 117.0101(3) an emergency limitations on access order has been made` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.0104(1) |
| `s 117.07(2) public officer: the person is one` | MAYBE BOOLEAN | another function of this part | s 117.07 |
| `s 118 evidence or statement: it is one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 136(2) |
| `s 118 judicial proceeding: the proceeding is one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 136(1), s 139(1)(a), s 139(1)(b) |
| `s 118 official: the person is one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 121(1)(a), s 122 |
| `s 118 witness: the person was one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 136(1) |
| `s 123(3) municipal official: the person concerned is one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 123(1), s 123(2) |
| `s 131 the person commits perjury: the answer` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 132 |
| `s 136(2) the earlier evidence is evidence for this section` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 136(1) |
| `s 136(2) the later evidence is evidence for this section` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 136(1) |
| `s 149(2) escape: the offence of which the person is convicted is one` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 149(1) |
| `s 2 dwelling-house: the place or premises is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.02(1) |
| `s 2 explosive substance: the thing possessed is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.01(1) |
| `s 2 firearm: the thing possessed is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.01(1) |
| `s 2 justice: the person is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.04(1), s 120(a) |
| `s 2 peace officer: the applicant is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 111(1), s 117.011(1) |
| `s 2 peace officer: the officer concerned is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 129(a), s 129(b) |
| `s 2 peace officer: the officer is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.0101(7), s 117.02(1), s 117.03(1), s 117.04(2) |
| `s 2 peace officer: the person is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.07(2), s 120(a), s 128(a), s 128(b), s 130(1)(b), s 147(b) |
| `s 2 prison: the place is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 144(a), s 144(b), s 146(b), s 147(c) |
| `s 2 public officer: the officer concerned is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 129(a), s 129(b) |
| `s 2 public officer: the person is one` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 120(a), s 130(1)(b) |
| `s 2.1 the term has the meaning it has in subsection 84(1): the thing possessed is a cross-bow, prohibited weapon, restricted weapon, prohibited device, firearm part, ammunition or prohibited ammunition` | MAYBE BOOLEAN | section 2 / 2.1 (the keel: `ccc-definitions.l4`) | s 117.01(1) |
| `s 515 the accused is bound by a release order` | BOOLEAN | ccc20 (s 515) | s 145(2)(a), s 145(5)(a) |
| `the answer of s 115(1.1)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 115(1) |
| `the answer of s 117.01(4)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.01(1) |
| `the answer of s 117.0101(10)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.0101(6), s 117.0101(9) |
| `the answer of s 117.03(2) the claim is made within 14 days after the seizure` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.03(2) |
| `the answer of s 117.05(1) the application is made within 30 days after the execution or the seizure` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.05(1) |
| `the answer of s 117.06(1)(a) no application was made within thirty days` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.06(1) |
| `the answer of s 117.1` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 117.07, s 117.071, s 117.08, s 117.09(1), s 117.09(2), s 117.09(3)... |
| `the answer of s 121.1(2)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 121.1(1) |
| `the answer of s 121.1(3)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 121.1(1) |
| `the answer of s 131(3)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 131(1), s 131(1.1) |
| `the answer of s 134(2)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 134(1) |
| `the answer of s 141(2)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 141(1) |
| `the answer of s 145(6)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 145(3), s 145(4)(a), s 145(4)(b) |
| `the answer of s 145(8)` | MAYBE BOOLEAN | this part (the answer of another function of ccc5) | s 145(2)(a), s 145(3), s 145(4)(a), s 145(4)(b), s 145(5)(a), s 145(5)(b) |
| `s 787(1) the general penalty for an offence punishable on summary conviction` | Punishment | ccc29 (s 787(1)) | every summary-conviction limb (`... the punishment on summary conviction`) |
| `Provision of the Code` (the core record) | record | the core | ss 111(7), 117.05(6), 117.11 (R1: a list of section numbers) |

Seams the plan lists and how this part meets them:

- [T] ss 110.4 to 113 asks ccc4 `s 110.1 an emergency prohibition order has been made` (MAYBE BOOLEAN): taken, as the first input of `s 110.4(1) ...`.
- [T] s 145 asks ccc20 `s 515 the accused is bound by a release order` (BOOLEAN): taken, as an input of `s 145(2)(a)` and `s 145(5)(a)`.
- [T] the summary limbs ask ccc29 `s 787(1) the general penalty for an offence punishable on summary conviction` (Punishment): taken (above).
- [T] ss 94 and 110.1 (ccc4) ask this part for ss 110.4, 117.07 and 117.1: answered by `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` (MAYBE BOOLEAN, exact name), `s 117.1 sections 117.07 to 117.09 do not apply to the person` and the `s 110.4(...)` functions.
- [H] ccc26, ccc14, ccc1, ccc20, ccc21 ask this part for the offence sections' class and punishment: answered, section by section, by `s N the class of the offence` (Class of offence) and `s N(x) the punishment on indictment` / `... on summary conviction` (Punishment), listed in the answer table above. For a section whose penalty is in the lead-in (ss 124, 125, 128, 129, 138, 144, 146 to 148, and the others) the label is the section.

Seams found that the plan lacks: (1) `Part XXVII the circumstances are those in which a summary conviction court may proceed with a trial in the absence of the defendant`, MAYBE BOOLEAN, used by ss 111(4), 117.011(4) and 117.05(2), to be answered by ccc29; (2) the facts "the provision is a provision of Part XXVII" (ss 111(10), 117.011(9), 117.05(9)); (3) ss 515.01, 508, 515(12), 516.1(1), 522(2.1) and 714.1 to 714.3 are named in ss 145 and 136 and taken as facts the person states; (4) `s 2.1 the term has the meaning it has in subsection 84(1)` is used for the cross-bow, prohibited weapon, restricted weapon, prohibited device, firearm part, ammunition and prohibited ammunition limb of s 117.01(1) (PLAN section 4 names it).

## What the text turns out to say

1. Section 131(3) and section 134(1) are mirror images: a person who is not specially permitted, authorized or required by law to make a statement under oath commits no perjury (s 131(3): "Subsections (1) and (1.1) do not apply"), but commits the summary-conviction offence of s 134(1) unless the statement is made in the course of a criminal investigation (s 134(2)). Asserted in `ccc5-cases-seat.l4` ("Dee swears an affidavit she knows is false").
2. Section 133 (no conviction on the evidence of one witness unless corroborated) is limited to "an offence under section 132", that is perjury. It does not reach s 136 (contradictory evidence), s 134 or s 137.
3. Section 136(1) carries its own proof requirement in the same sentence ("no person shall be convicted under this section unless the court ... is satisfied beyond a reasonable doubt that the accused ... intended to mislead"), and s 136(2) narrows "evidence" for that section to material evidence although s 118 says "whether material or not". The encoding takes the court's satisfaction as an input and never guesses it. Asserted.
4. Section 145(2)(c) (failing to surrender) has no "without lawful excuse" element, unlike (2)(a), (b) and (d). Section 145(8) (the Contraventions Act election as a lawful excuse) reaches paragraph (2)(a) and subsections (3) to (5) but not (2)(b), (c) or (d). Section 145(6) (a defective notice is no excuse) reaches subsections (3) and (4) only. Asserted at each limb.
5. Section 117.07(2) defines "public officer" for that section as a closed list ("In this section, public officer means" (a) to (j)), while section 2 says "public officer includes" (inputs/R.S.C.-1985-c.-C-46.txt lines 164 and 2629). The two functions are different (`s 117.07(2) public officer` answers JUST FALSE outside the list; `s 2 public officer` can answer NOTHING).
6. An order limiting access under s 117.011(5) states no duration ("imposing such terms and conditions ... as the provincial court judge considers appropriate"), unlike an order under s 111(5) (not exceeding five years), s 117.05(4)(b) (not exceeding five years) and an emergency order under s 117.0101(3) (not exceeding 30 days). The encoding states no period for s 117.011(5) and asks none.
7. Five sections in the range are indictable only, each with a maximum of fourteen years: ss 119(1), 120, 132, 136(1) and 137. Section 134(1) is summary only. Every other offence section is dual (an indictable limb and a summary limb) with a stated maximum on indictment of two, five or ten years; none states a penalty for its summary limb (see the answer table).
8. Sections 126(1) and 127(1) are residual offences: each applies "unless a punishment [or other mode of proceeding] is expressly provided by law", and s 127(1) excludes an order for the payment of money.
9. Section 129(c) (resisting or obstructing a person executing process against lands or goods, or making a lawful distress or seizure) has no peace-officer or public-officer element, unlike (a) and (b).
10. Sections 117.05(1) and 117.06(1) write the same period two ways: "within 30 days" (117.05(1)) and "thirty days" (117.06(1)(a) and (b)). The encoding treats them as one period (fork FM-7) and tests both edges.
11. Several duties have no number: "immediately" (ss 117.0101(8), 117.04(3)), "without delay" (s 117.03(2)), "forthwith" (s 117.03(3)), "as soon as feasible" (ss 110.4(4), 117.0101(12)), "a reasonable period" (ss 114, 117.0101(9)). The encoding states none.
12. Nine units of the range are repealed or blank in this text: ss 111(11), 117.13(4) and (5), 117.15(3) and (4), 121.1(5), 135, 143, 145(5.1) and 145(7) (counted: 9 rows).
13. While writing the cases, an expectation of mine was wrong and was revised, openly: for a person who states an exception to one paragraph (a licence under a s 113(1) order; the written consent of s 121(1)(b)), I first wrote JUST FALSE for the composite offence question; the composite is NOTHING by design (fork FM-12), because the text says no to that paragraph only. The expected values of those two cases were changed to NOTHING, with the exception's own question asserted beside the first. These are the only expected values changed after a run, and the reason is recorded here; no expected value was changed to match a failing test of the text. One other thing changed after a first run, and it was the generator, not an expectation: the generated "the other way it can fail" test for a MAYBE BOOLEAN input that is one alternative of an OR group asserted something false (a JUST FALSE alternative does not defeat a limb whose other alternative holds); the generator now makes that test only for an input that is alone in its group, which removed two malformed assertions from the first test file (166 satisfied became 164).

## What the stable binary does not accept, and what it does that surprises

Binary: `l4 1.6.110 (main, e51181d, 2026-11-11)`; `check.sh` also ran every module on `1.6.109 (main, 4c887e0, 2026-11-04)`.

- **Loud.** A `#TRACE` prints its outcome and cannot be asserted (it is a DEONTIC; `#ASSERT` over one is not possible). The four regulative rules (`s 110.4(4)`, `s 117.0104(4)`, `s 117.03(2)`, `s 117.05(1)`) are run with `#TRACE` in the tests files; each outcome was read, with the expected outcome decided from the text and written beside the trace; each has a decision-function twin that is asserted (`s 110.4(4) the notice was served not later than 15 days before the date fixed`, `s 117.03(2) the claim is made within 14 days after the seizure` and `... the thing is to be returned without delay`, `s 117.05(1) the application is made within 30 days ...` and the duty). `REFUSE`, `BECAUSE` (except `LEST BREACH BY ... BECAUSE`), `WAIT UNTIL` (spelled `WAITUNTIL`), `YMD` and `TYPICALLY` were not used.
- **Silent.** A `MAY` with a `HENCE` chain and no `LEST` enters the HENCE obligation when the permission lapses. Probe on both builds (1.6.109 and 1.6.110), `PARTY the accused MAY claim WITHIN 14 HENCE (PARTY a peace officer MUST return HENCE FULFILLED)`: after `WAITUNTIL 20` the trace result is the officer's standing obligation, and so it is when the act comes at day 15 (late); with `HENCE FULFILLED` alone the lapse is FULFILLED. The rules that needed "the person may claim, and the officer must then return" are therefore written `DO ... WITHIN 14 HENCE (...) LEST FULFILLED`, which gives FULFILLED on a lapse, on a late act and on no act, and the standing obligation after a timely claim, on both builds. `check.sh` cannot see this (a trace prints no assertion line); the traces of both builds were compared by hand and are identical.
- **Not an issue but checked.** `@export` on a function with no `GIVEN` (the class and punishment questions) is accepted; an enum from the core (`Province or territory`) and from a part (`s 118 forum`) is accepted as an input type; `BRANCH`, `DATE MINUS NUMBER`, `LESS THAN` on dates, a `MAYBE DATE` result and a `MAYBE Party` result are accepted; an unused `GIVEN` raises no diagnostic (used for the "whether or not" facts).

## Tests, and what check.sh prints

`L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` printed, exactly:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc5-cases-seat.l4                             0       783       0        0         0 |      0       783       0        0  same
ccc5-s110-4-to-117.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-01-to-117-012.l4                     0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-02-to-117-06.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc5-s117-07-to-117-15.l4                      0         0       0        0         0 |      0         0       0        0  same
ccc5-s118-to-130-1.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc5-s131-to-143.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc5-s144-to-149.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc5-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ccc5-tests-s110-4-to-117.l4                    0       165       0        0         0 |      0       165       0        0  same
ccc5-tests-s117-01-to-117-012.l4               0       209       0        0         0 |      0       209       0        0  same
ccc5-tests-s117-02-to-117-06.l4                0       137       0        0         0 |      0       137       0        0  same
ccc5-tests-s117-07-to-117-15.l4                0       141       0        0         0 |      0       141       0        0  same
ccc5-tests-s118-to-130-1.l4                    0       387       0        0         0 |      0       387       0        0  same
ccc5-tests-s131-to-143.l4                      0       203       0        0         0 |      0       203       0        0  same
ccc5-tests-s144-to-149.l4                      0       235       0        0         0 |      0       235       0        0  same
TOTAL (19 modules)                             0      2260       0        0           |      0      2260       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Every case file ends with assertions written equal to assertions satisfied; none fails on purpose, so `expected_failed` is empty and no file is registered as deliberately failing.
The baseline `check.sh` printed before this part wrote anything was the three keel files (`ccc-core.l4`, `ccc-definitions.l4`, `ccc-interpretation.l4`) with 0 errors and 0 assertions each; every `ccc5-` line is new.
`python3 -I srcrefs.py check --refs` and `--strict` over every `ccc5-*.l4`: see the report line printed by the last run in the final report of the part agent (0 problems).

## Seat questions (ccc5)

268 exported questions in `ccc5-seat.l4`, each beginning "Under section N,"; each has `@export`, and each input has `@desc` worded as the person would be asked. The second column is the layer-1 function each returns (or calls).

| question | returns | layer-1 function |
| --- | --- | --- |
| Under section 110.4(1), may the provincial court judge fix a date for the hearing of an application for an order against me under subsection 111(5) | MAYBE BOOLEAN | `s 110.4(1) the provincial court judge may fix a date for the hearing of an application under subsection 111(1)` |
| Under section 110.4(1), is the provincial court judge bound to direct that notice of the hearing be given to me | MAYBE BOOLEAN | `s 110.4(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` |
| Under section 110.4(2)(a), is the application for the order under subsection 110.1(3) deemed an application made under subsection 111(1) | MAYBE BOOLEAN | `s 110.4(2)(a) the application for the order under subsection 110.1(3) is deemed an application made under subsection 111(1)` |
| Under section 110.4(2)(b), who becomes the applicant in my case | MAYBE Party | `s 110.4(2)(b) the Attorney General who becomes the applicant` |
| Under section 110.4(3), is the date fixed for the hearing before the end of the period of the order I am under | MAYBE BOOLEAN | `s 110.4(3) the date fixed for the hearing is before the end of the period of the order` |
| Under section 110.4(3), may the provincial court judge adjourn the hearing on my application | MAYBE BOOLEAN | `s 110.4(3) the provincial court judge may adjourn the hearing` |
| Under section 110.4(4), is the provincial court judge bound to cause notice of the application and of the hearing date to be served on the Attorney General | MAYBE BOOLEAN | `s 110.4(4) the provincial court judge is bound to cause notice to be served on the Attorney General` |
| Under section 110.4(5), is the provincial court judge bound to cancel the hearing because my emergency order was revoked before the application was heard | MAYBE BOOLEAN | `s 110.4(5) the provincial court judge is bound to cancel the hearing` |
| Under section 111(1), may a peace officer, firearms officer or chief firearms officer apply to a provincial court judge for an order prohibiting me from possessing firearms and similar things | MAYBE BOOLEAN | `s 111(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order prohibiting a person from possessing weapons` |
| Under section 111(2), is the provincial court judge bound to fix a date for the hearing and direct that notice of it be given to me | MAYBE BOOLEAN | `s 111(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` |
| Under section 111(3), is the provincial court judge bound to hear all relevant evidence presented by or on behalf of the applicant and me | MAYBE BOOLEAN | `s 111(3) the provincial court judge is bound to hear all relevant evidence presented by or on behalf of the applicant and the person` |
| Under section 111(4), may the provincial court judge hear and determine the application in my absence | MAYBE BOOLEAN | `s 111(4) the provincial court judge may proceed ex parte to hear and determine the application` |
| Under section 111(5), is the provincial court judge bound to make an order prohibiting me from possessing firearms and similar things | MAYBE BOOLEAN | `s 111(5) the provincial court judge is bound to make an order prohibiting the person from possessing the things` |
| Under section 111(5), is the period of the order I face not more than five years | MAYBE BOOLEAN | `s 111(5) the period of the order is not more than five years` |
| Under section 111(5), does the order I face begin on the day on which it is made | MAYBE BOOLEAN | `s 111(5) the order begins on the day on which it is made` |
| Under section 111(6), is the provincial court judge bound to include a statement of reasons in the record where no order, or a narrower order, is made | MAYBE BOOLEAN | `s 111(6) the provincial court judge is bound to include a statement of reasons in the record` |
| Under section 111(7), do sections 113 to 117 apply to the order made against me | MAYBE BOOLEAN | `s 111(7) sections 113 to 117 apply to the order, tested by section number` |
| Under section 111(8), may I appeal to the superior court against the order the provincial court judge made against me | MAYBE BOOLEAN | `s 111(8) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` |
| Under section 111(9), may the Attorney General appeal to the superior court against the judge's decision not to make an order against me | MAYBE BOOLEAN | `s 111(9) the Attorney General may appeal to the superior court against the decision not to make an order` |
| Under section 111(10), does a provision of Part XXVII apply to my appeal to the superior court | MAYBE BOOLEAN | `s 111(10) the provision of Part XXVII applies to the appeal` |
| Under section 112, may a provincial court judge revoke the order made against me | MAYBE BOOLEAN | `s 112 a provincial court judge may revoke the order` |
| Under section 113(1), may the competent authority make an order authorizing a licence, authorization or registration certificate for me for sustenance or employment despite the prohibition order | MAYBE BOOLEAN | `s 113(1) the competent authority may make an order authorizing a licence, authorization or registration certificate for sustenance or employment` |
| Under section 113(2), may the competent authority make an order for me under section 113(1) after taking into account my criminal record, the offence and safety | MAYBE BOOLEAN | `s 113(2) the competent authority may make an order under subsection (1) only after taking the factors into account` |
| Under section 113(3)(a), is the chief firearms officer barred from denying me an authorization, licence or registration certificate solely on the basis of the prohibition order or my offence | MAYBE BOOLEAN | `s 113(3)(a) an authorization, licence or registration certificate is barred from being denied solely on the basis of the prohibition order or the offence` |
| Under section 113(3)(b), may an authorization or licence be issued to me for the duration of the order | MAYBE BOOLEAN | `s 113(3)(b) the authorization or licence may be issued to the person for the duration of the order` |
| Under section 113(3)(b), may the chief firearms officer attach further terms and conditions to my authorization or licence | MAYBE BOOLEAN | `s 113(3)(b) the chief firearms officer may attach further terms and conditions to the authorization or licence` |
| Under section 113(4), may an order lifting the prohibition for sustenance or employment be made during the proceedings I am in | MAYBE BOOLEAN | `s 113(4) an order under subsection (1) may be made during the proceedings` |
| Under section 113(5), is the authority the competent authority | MAYBE BOOLEAN | `s 113(5) competent authority` |
| Under section 114, may the authority that makes a prohibition order against me require me to surrender things and documents to a peace officer, firearms officer or chief firearms officer | MAYBE BOOLEAN | `s 114 the competent authority may require the person to surrender the things and documents` |
| Under section 114, is the authority bound to specify in the order a reasonable period for me to surrender things and documents | MAYBE BOOLEAN | `s 114 the authority is bound to specify in the order a reasonable period for surrendering` |
| Under section 114, does section 117.01 not apply to me during the period the order specifies for surrendering | MAYBE BOOLEAN | `s 114 section 117.01 does not apply to the person during the specified period` |
| Under section 115(1.1), does the forfeiture in section 115(1) not apply to the order made against me | MAYBE BOOLEAN | `s 115(1.1) subsection (1) does not apply to the order` |
| Under section 115(1), is a thing whose possession the prohibition order prohibits forfeited to Her Majesty | MAYBE BOOLEAN | `s 115(1) the thing is forfeited to Her Majesty` |
| Under section 115(2), is a thing forfeited to Her Majesty to be disposed of or otherwise dealt with as the Attorney General directs | MAYBE BOOLEAN | `s 115(2) the thing forfeited is to be disposed of or otherwise dealt with as the Attorney General directs` |
| Under section 116(1), is my authorization, licence or registration certificate revoked or amended on the commencement of the prohibition order | MAYBE BOOLEAN | `s 116(1) the authorization, licence or registration certificate is revoked or amended on the commencement of the prohibition order` |
| Under section 116(2), does my authorization, licence or registration certificate remain revoked or amended, because the order is under subsection 110.1(3) or section 515 and still in force | MAYBE BOOLEAN | `s 116(2) the authorization, licence or registration certificate remains revoked or amended` |
| Under section 117, is the competent authority bound to order the thing returned to me as its owner, or its proceeds or value paid to me | MAYBE BOOLEAN | `s 117 the competent authority is bound to order the thing returned to the owner, or its proceeds or value paid` |
| Under section 117, what must the competent authority order for me as the owner | `s 117 order for the owner` | `s 117 what the order for the owner is` |
| Under section 117.01(4), does section 117.01(1) not apply to me because I possessed a firearm in accordance with an authorization or licence issued as the result of an order under section 113(1) | MAYBE BOOLEAN | `s 117.01(4) subsection (1) does not apply to a person who possessed a firearm in accordance with an authorization or licence issued as a result of an order under subsection 113(1)` |
| Under section 117.01, is possessing a weapon while prohibited by an order, or wilfully failing to surrender an authorization, licence or registration certificate, an offence on what I did | MAYBE BOOLEAN | `s 117.01(3) the person who commits an offence under subsection (1) or (2) is guilty of an offence` |
| Under section 117.01(3), is an offence under section 117.01(1) or (2) indictable, punishable on summary conviction, or both | `Class of offence` | `s 117.01(3) the class of the offence` |
| Under section 117.01(3)(a), what is the greatest imprisonment I face on indictment for an offence under section 117.01 | Punishment | `s 117.01(3)(a) the punishment on indictment` |
| Under section 117.0101(1), may a person make an ex parte application to a provincial court judge for an emergency order limiting access to things in my possession | MAYBE BOOLEAN | `s 117.0101(1) any person may make an ex parte application to a provincial court judge for an emergency limitations on access order` |
| Under section 117.0101(2), may the provincial court judge hold the hearing of the application in private | MAYBE BOOLEAN | `s 117.0101(2) the provincial court judge may hold the hearing in private` |
| Under section 117.0101(3), is the provincial court judge bound to make an emergency order limiting my use and possession of firearms and similar things | MAYBE BOOLEAN | `s 117.0101(3) the provincial court judge is bound to make an emergency limitations on access order` |
| Under section 117.0101(3), is the period of the emergency order I face not more than 30 days | MAYBE BOOLEAN | `s 117.0101(3) the period of the order is not more than 30 days` |
| Under section 117.0101(4), is a copy of the emergency order to be served on me | MAYBE BOOLEAN | `s 117.0101(4) a copy of the order is to be served on the person to whom it is addressed` |
| Under section 117.0101(5), is the provincial court judge bound to impose the least intrusive terms and conditions possible in my emergency order | MAYBE BOOLEAN | `s 117.0101(5) the provincial court judge is bound to impose terms and conditions that are the least intrusive possible` |
| Under section 117.0101(10), may the judge issue a warrant, or include a requirement to surrender, in my emergency order | MAYBE BOOLEAN | `s 117.0101(10) the judge may issue the warrant or include the requirement to surrender` |
| Under section 117.0101(6), may the provincial court judge issue a warrant authorizing a peace officer to search for and seize things in my possession | MAYBE BOOLEAN | `s 117.0101(6) the provincial court judge may issue a warrant authorizing a peace officer to search and seize` |
| Under section 117.0101(7), may a peace officer search for and seize things in my possession without a warrant | MAYBE BOOLEAN | `s 117.0101(7) the peace officer may search for and seize without a warrant` |
| Under section 117.0101(8), is the peace officer who searched or seized bound to make a report immediately to a justice | MAYBE BOOLEAN | `s 117.0101(8) the peace officer is bound to make a report immediately to a justice having jurisdiction` |
| Under section 117.0101(8), does the peace officer's report show what the subsection requires | MAYBE BOOLEAN | `s 117.0101(8) the report shows what the subsection requires` |
| Under section 117.0101(9), may the provincial court judge require me to surrender things to a peace officer, firearms officer or chief firearms officer | MAYBE BOOLEAN | `s 117.0101(9) the provincial court judge may require the person to surrender the things` |
| Under section 117.0101(9), is the judge bound to specify a reasonable period for me to surrender the thing | MAYBE BOOLEAN | `s 117.0101(9) the judge is bound to specify in the order a reasonable period for surrendering the thing` |
| Under section 117.0101(11), may the officer return to me the thing seized or surrendered before the emergency order expires or is revoked | MAYBE BOOLEAN | `s 117.0101(11) the peace officer, firearms officer or chief firearms officer may return the thing before the expiry or revocation of the order` |
| Under section 117.0101(12), are the things seized or surrendered to be returned to me after the emergency order is revoked or its period ends | MAYBE BOOLEAN | `s 117.0101(12) the things are to be returned to the person` |
| Under section 117.0102(1), may the provincial court judge make an order prohibiting my access to, and the disclosure of, information about the emergency order and the search and seizure | MAYBE BOOLEAN | `s 117.0102(1) the provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| Under section 117.0102(2), does the order denying access to information expire on the day in question | MAYBE BOOLEAN | `s 117.0102(2) the order made under subsection (1) expires on the day in question` |
| Under section 117.0102(3), on what day does the order denying access to information cease to have effect | MAYBE DATE | `s 117.0102(3) the day on which the order made under subsection (1) ceases to have effect` |
| Under section 117.0102(4), are the documents about my emergency order to be placed in a packet and sealed by the judge | MAYBE BOOLEAN | `s 117.0102(4) the documents are to be placed in a packet and sealed by the judge` |
| Under section 117.0102(5), may an application to revoke or vary the order denying access to information be made to the judge who made it or to another provincial court judge | MAYBE BOOLEAN | `s 117.0102(5) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` |
| Under section 117.0103(1), may the provincial court judge order that information identifying the applicant be deleted from the copies of the documents I receive | MAYBE BOOLEAN | `s 117.0103(1) the provincial court judge may order that identifying information be deleted from copies of the documents` |
| Under section 117.0103(2), may the order deleting identifying information last for any period, definite or indefinite, the judge considers necessary | MAYBE BOOLEAN | `s 117.0103(2) the order may be for any period, definite or indefinite, that the judge considers necessary` |
| Under section 117.0103(3), are the originals of the documents to be placed in a packet and sealed by the judge | MAYBE BOOLEAN | `s 117.0103(3) the originals of the documents are to be placed in a packet and sealed by the judge` |
| Under section 117.0103(4), may an application to revoke or vary the order deleting identifying information be made to the judge who made it or to another provincial court judge | MAYBE BOOLEAN | `s 117.0103(4) an application to revoke or vary the order may be made to the judge who made it or to another provincial court judge` |
| Under section 117.0103(5), does an order made under section 117.0103 that is still in force apply at the hearing | MAYBE BOOLEAN | `s 117.0103(5) any order made under this section that is still in force applies in respect of the hearing` |
| Under section 117.0104(1), may the provincial court judge fix a date for the hearing of an application for an order against me under subsection 117.011(5) | MAYBE BOOLEAN | `s 117.0104(1) the provincial court judge may fix a date for the hearing of an application under subsection 117.011(1)` |
| Under section 117.0104(1), is the provincial court judge bound to direct that notice of the hearing be given to me | MAYBE BOOLEAN | `s 117.0104(1) the provincial court judge is bound to direct that notice of the hearing be given to the person` |
| Under section 117.0104(2)(a), is the application for the order under subsection 117.0101(3) deemed an application made under subsection 117.011(1) | MAYBE BOOLEAN | `s 117.0104(2)(a) the application for the order under subsection 117.0101(3) is deemed an application made under subsection 117.011(1)` |
| Under section 117.0104(2)(b), who becomes the applicant in my case | MAYBE Party | `s 117.0104(2)(b) the Attorney General who becomes the applicant` |
| Under section 117.0104(3), is the date fixed for the hearing before the end of the period of the order I am under | MAYBE BOOLEAN | `s 117.0104(3) the date fixed for the hearing is before the end of the period of the order` |
| Under section 117.0104(3), may the provincial court judge adjourn the hearing on my application | MAYBE BOOLEAN | `s 117.0104(3) the provincial court judge may adjourn the hearing` |
| Under section 117.0104(4), is the provincial court judge bound to cause notice of the application and of the hearing date to be served on the Attorney General | MAYBE BOOLEAN | `s 117.0104(4) the provincial court judge is bound to cause notice to be served on the Attorney General` |
| Under section 117.0104(5), is the provincial court judge bound to cancel the hearing because my emergency order was revoked before the application was heard | MAYBE BOOLEAN | `s 117.0104(5) the provincial court judge is bound to cancel the hearing` |
| Under section 117.011(1), may a peace officer, firearms officer or chief firearms officer apply to a provincial court judge for an order limiting my use and possession of firearms and similar things | MAYBE BOOLEAN | `s 117.011(1) a peace officer, firearms officer or chief firearms officer may apply to a provincial court judge for an order limiting access` |
| Under section 117.011(2), is the provincial court judge bound to fix a date for the hearing and direct that notice of it be given to me | MAYBE BOOLEAN | `s 117.011(2) the provincial court judge is bound to fix a date for the hearing and direct that notice be given to the person` |
| Under section 117.011(3), is the provincial court judge bound to hear all relevant evidence presented by or on behalf of the applicant and me | MAYBE BOOLEAN | `s 117.011(3) the provincial court judge is bound to hear all relevant evidence presented by or on behalf of the applicant and the person` |
| Under section 117.011(4), may the provincial court judge hear and determine the application in my absence | MAYBE BOOLEAN | `s 117.011(4) the provincial court judge may proceed ex parte to hear and determine the application` |
| Under section 117.011(5), is the provincial court judge bound to make an order imposing terms and conditions on my use and possession of firearms and similar things | MAYBE BOOLEAN | `s 117.011(5) the provincial court judge is bound to make an order imposing terms and conditions on the person's use and possession` |
| Under section 117.011(6), is the provincial court judge bound to impose the least intrusive terms and conditions possible | MAYBE BOOLEAN | `s 117.011(6) the provincial court judge is bound to impose terms and conditions that are the least intrusive possible` |
| Under section 117.011(7), may I appeal to the superior court against the order the provincial court judge made against me | MAYBE BOOLEAN | `s 117.011(7) the person to whom the order relates, or the Attorney General, may appeal to the superior court against the order` |
| Under section 117.011(8), may the Attorney General appeal to the superior court against the decision not to make an order against me | MAYBE BOOLEAN | `s 117.011(8) the Attorney General may appeal to the superior court against the decision not to make an order` |
| Under section 117.011(9), does a provision of Part XXVII apply to my appeal to the superior court | MAYBE BOOLEAN | `s 117.011(9) the provision of Part XXVII applies to the appeal` |
| Under section 117.012, may a provincial court judge revoke the order made against me | MAYBE BOOLEAN | `s 117.012 a provincial court judge may revoke the order` |
| Under section 117.02(1), may a peace officer search me, my vehicle or my premises other than a dwelling-house without a warrant, and seize things | MAYBE BOOLEAN | `s 117.02(1) the peace officer may search without a warrant and seize` |
| Under section 117.02(2), is a thing seized from me under section 117.02(1) to be dealt with in accordance with sections 490 and 491 | MAYBE BOOLEAN | `s 117.02(2) the thing seized is to be dealt with in accordance with sections 490 and 491` |
| Under section 117.03(1), may a peace officer seize my firearm, prohibited weapon, restricted weapon, prohibited device or prohibited ammunition because I did not produce an authorization or licence on demand | MAYBE BOOLEAN | `s 117.03(1) the peace officer may seize the firearm, weapon, device or ammunition` |
| Under section 117.03(2), is the thing seized from me to be returned without delay | MAYBE BOOLEAN | `s 117.03(2) the thing is to be returned without delay` |
| Under section 117.03(3), is the peace officer bound to take the thing seized from me forthwith before a provincial court judge, because it was not claimed and returned as subsection (2) provides | MAYBE BOOLEAN | `s 117.03(3) the peace officer is bound to take the thing forthwith before a provincial court judge` |
| Under section 117.03(3), may the provincial court judge declare the thing seized from me forfeited to Her Majesty | MAYBE BOOLEAN | `s 117.03(3) the provincial court judge may declare the thing forfeited to Her Majesty` |
| Under section 117.04(1), may a justice issue a warrant authorizing a peace officer to search a building, receptacle or place and seize my weapons and authorizations | MAYBE BOOLEAN | `s 117.04(1) the justice may issue a warrant authorizing a peace officer to search the building, receptacle or place and seize` |
| Under section 117.04(2), may a peace officer search for and seize my weapons and authorizations without a warrant | MAYBE BOOLEAN | `s 117.04(2) the peace officer may search for and seize without a warrant` |
| Under section 117.04(3), is the peace officer who searched or seized bound to make a report immediately to a justice | MAYBE BOOLEAN | `s 117.04(3) the peace officer is bound to make a report immediately to a justice having jurisdiction` |
| Under section 117.04(3), does the peace officer's report show what the subsection requires | MAYBE BOOLEAN | `s 117.04(3) the report shows what the subsection requires` |
| Under section 117.04(4), is every authorization, licence and registration certificate I hold revoked as at the time of the seizure | MAYBE BOOLEAN | `s 117.04(4) every authorization, licence and registration certificate held by the person is revoked as at the time of the seizure` |
| Under section 117.05(1), is the justice bound to fix a date for the hearing of the peace officer's application about the things seized from me and direct that notice of it be given | MAYBE BOOLEAN | `s 117.05(1) the justice is bound to fix a date for the hearing and direct that notice of it be given` |
| Under section 117.05(2), may the justice hear and determine the application in my absence | MAYBE BOOLEAN | `s 117.05(2) the justice may proceed ex parte to hear and determine the application` |
| Under section 117.05(3), is the justice bound to hear all relevant evidence, including evidence of the value of the thing | MAYBE BOOLEAN | `s 117.05(3) the justice is bound to hear all relevant evidence, including evidence respecting the value of the thing` |
| Under section 117.05(4)(a), is the justice bound to order that the things seized from me be forfeited to Her Majesty or otherwise disposed of | MAYBE BOOLEAN | `s 117.05(4)(a) the justice is bound to order that any thing seized be forfeited to Her Majesty or otherwise disposed of` |
| Under section 117.05(4)(b), is the justice bound to order that my possession of weapons and similar things be prohibited | MAYBE BOOLEAN | `s 117.05(4)(b) the justice is bound to order that the person's possession be prohibited` |
| Under section 117.05(4)(b), is the period of the order I face not more than five years | MAYBE BOOLEAN | `s 117.05(4)(b) the period of the order is not more than five years` |
| Under section 117.05(4)(b), does the order I face begin on the day on which it is made | MAYBE BOOLEAN | `s 117.05(4)(b) the order begins on the day on which it is made` |
| Under section 117.05(5), is the justice bound to include a statement of reasons in the record where no order, or a narrower order, is made | MAYBE BOOLEAN | `s 117.05(5) the justice is bound to include a statement of reasons in the record` |
| Under section 117.05(6), do sections 113 to 117 apply to the order made against me | MAYBE BOOLEAN | `s 117.05(6) sections 113 to 117 apply to the order, tested by section number` |
| Under section 117.05(7), may I appeal to the superior court against the order the justice made | MAYBE BOOLEAN | `s 117.05(7) the person may appeal to the superior court against the order` |
| Under section 117.05(8), may the Attorney General appeal to the superior court against the justice's failure to make the finding or the order | MAYBE BOOLEAN | `s 117.05(8) the Attorney General may appeal to the superior court against the failure to make the finding or the order` |
| Under section 117.05(9), does a provision of Part XXVII apply to my appeal to the superior court | MAYBE BOOLEAN | `s 117.05(9) the provision of Part XXVII applies to the appeal` |
| Under section 117.06(1), is the thing or document seized from me to be returned to me | MAYBE BOOLEAN | `s 117.06(1) the thing or document is to be returned to the person from whom it was seized` |
| Under section 117.06(2), may the justice order that the revocation of my authorization, licence or registration certificate be reversed and it be restored | MAYBE BOOLEAN | `s 117.06(2) the justice may order that the revocation be reversed and the authorization, licence or registration certificate restored` |
| Under section 117.07(2), am I a public officer for the purposes of section 117.07 | MAYBE BOOLEAN | `s 117.07(2) public officer` |
| Under section 117.07, am I, as a public officer, exempt from guilt of an offence under the Criminal Code or the Firearms Act by reason only of what I did in my duties | MAYBE BOOLEAN | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` |
| Under section 117.071, am I, as a preclearance officer, not guilty of an offence under the Criminal Code or the Firearms Act by reason only of what I did in my duties | MAYBE BOOLEAN | `s 117.071 the preclearance officer is not guilty of an offence by reason only of the listed acts done in their duties` |
| Under section 117.08, am I, acting for a police force, the Canadian Forces, a visiting force or a government department, not guilty of an offence by reason only of what I did | MAYBE BOOLEAN | `s 117.08 the individual is not guilty of an offence by reason only of the listed acts done on behalf of a police force, the Canadian Forces, a visiting force or a government department` |
| Under section 117.09(1), am I, as a licensed employee of a licensed business, not guilty of an offence by reason only of what I did in the specified activities | MAYBE BOOLEAN | `s 117.09(1) the licensed employee of a licensed business is not guilty of an offence by reason only of the listed acts in the specified activities` |
| Under section 117.09(2), am I, as an employee of a licensed business, not guilty of an offence by reason only of dealing with a partially manufactured barrelled weapon | MAYBE BOOLEAN | `s 117.09(2) the employee of a licensed business is not guilty of an offence by reason only of dealing with a partially manufactured barrelled weapon` |
| Under section 117.09(3), am I, as an employee of a carrier, not guilty of an offence by reason only of possessing or transferring firearms and similar things in my duties | MAYBE BOOLEAN | `s 117.09(3) the employee of a carrier is not guilty of an offence by reason only of possessing or transferring the listed things in their duties` |
| Under section 117.09(4), am I, as an employee of a licensed museum, not guilty of an offence by reason only of possessing or transferring a firearm that resembles an antique firearm | MAYBE BOOLEAN | `s 117.09(4) the employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a functioning imitation antique firearm` |
| Under section 117.09(5), am I, as a museum employee designated by name by a provincial minister, not guilty of an offence by reason only of possessing or transferring a firearm in my duties | MAYBE BOOLEAN | `s 117.09(5) the designated employee of a licensed museum is not guilty of an offence by reason only of possessing or transferring a firearm` |
| Under section 117.09(6), is the provincial minister barred from designating me for the purpose of section 117.09(5) | MAYBE BOOLEAN | `s 117.09(6) the provincial minister is barred from designating the individual for the purpose of subsection (5)` |
| Under section 117.09(7), may the provincial minister attach a condition to my designation | MAYBE BOOLEAN | `s 117.09(7) the provincial minister may attach a condition to the designation` |
| Under section 117.1, do the exemptions of sections 117.07 to 117.09 not apply to me because I am subject to a prohibition order and acted contrary to it | MAYBE BOOLEAN | `s 117.1 sections 117.07 to 117.09 do not apply to the person` |
| Under section 117.11, is the onus on me to prove that the person is the holder of an authorization, a licence or a registration certificate | MAYBE BOOLEAN | `s 117.11 the onus is on the accused to prove that the person is the holder of the authorization, licence or registration certificate` |
| Under section 117.12(1), is a document purporting to be an authorization, licence or registration certificate evidence of the statements in it | MAYBE BOOLEAN | `s 117.12(1) a document purporting to be an authorization, a licence or a registration certificate is evidence of the statements contained in it` |
| Under section 117.12(2), is a copy of an authorization, licence or registration certificate, certified as a true copy by the Registrar or a chief firearms officer, admissible in evidence | MAYBE BOOLEAN | `s 117.12(2) a certified copy is admissible in evidence` |
| Under section 117.12(2), does a certified copy have the same probative force as the original would have had | MAYBE BOOLEAN | `s 117.12(2) the certified copy has the same probative force as the original would have had` |
| Under section 117.13(1), is the analyst's certificate evidence of the results of the analysis without proof of the signature or official character of the person who signed it | MAYBE BOOLEAN | `s 117.13(1) a certificate of an analyst is evidence without proof of the signature or official character` |
| Under section 117.13(2), may I, with leave of the court, require the analyst who signed the certificate to attend for cross-examination | MAYBE BOOLEAN | `s 117.13(2) the party against whom a certificate of an analyst is produced may, with leave of the court, require the attendance of the analyst` |
| Under section 117.13(3), is the analyst's certificate barred from admission against me for want of reasonable notice before the trial | MAYBE BOOLEAN | `s 117.13(3) the certificate of an analyst is barred from admission for want of reasonable notice before the trial` |
| Under section 117.14(1), may the Governor in Council declare an amnesty period with respect to a weapon, prohibited device, prohibited ammunition, explosive substance or component or part designed exclusively for an automatic firearm | MAYBE BOOLEAN | `s 117.14(1) the Governor in Council may declare an amnesty period` |
| Under section 117.14(2), is the amnesty period declared for a purpose that section 117.14(2) names | MAYBE BOOLEAN | `s 117.14(2) the order declares the amnesty period for a purpose subsection (2) names` |
| Under section 117.14(3), am I not guilty of an offence under Part III by reason only of doing, during an amnesty period, a thing the amnesty order provides for | MAYBE BOOLEAN | `s 117.14(3) the person is not guilty of an offence under this Part by reason only of doing a thing provided for in an amnesty order` |
| Under section 117.14(4), are proceedings taken against me under Part III for something I did in reliance on section 117.14 a nullity | MAYBE BOOLEAN | `s 117.14(4) the proceedings are a nullity` |
| Under section 118, is what I said evidence or a statement | MAYBE BOOLEAN | `s 118 evidence or statement` |
| Under section 118, is the proceeding a judicial proceeding | MAYBE BOOLEAN | `s 118 judicial proceeding` |
| Under section 118, was I a witness | MAYBE BOOLEAN | `s 118 witness` |
| Under section 118, am I an official | MAYBE BOOLEAN | `s 118 official` |
| Under section 119(1), is accepting, obtaining, giving or offering a benefit corruptly, in connection with a judicial office or a legislature, an offence on what I did | MAYBE BOOLEAN | `s 119(1) the person is guilty of an indictable offence under subsection (1)` |
| Under section 119(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 119(1) the class of the offence` |
| Under section 119(1), what is the greatest imprisonment I face on indictment | Punishment | `s 119(1) the punishment on indictment` |
| Under section 119(2), are the proceedings against me barred for want of the written consent of the Attorney General of Canada | MAYBE BOOLEAN | `s 119(2) the proceedings against a holder of a judicial office are barred for want of the written consent of the Attorney General of Canada` |
| Under section 120, is corruptly taking or giving a benefit, in connection with the administration of justice, an offence on what I did | MAYBE BOOLEAN | `s 120 the person is guilty of an indictable offence under section 120` |
| Under section 120, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 120 the class of the offence` |
| Under section 120, what is the greatest imprisonment I face on indictment | Punishment | `s 120 the punishment on indictment` |
| Under section 121(1), is giving, taking or arranging a benefit in dealings with the government an offence on what I did | MAYBE BOOLEAN | `s 121(1) the person commits an offence under subsection (1)` |
| Under section 121(3), is an offence under section 121 indictable, punishable on summary conviction, or both | `Class of offence` | `s 121(3) the class of the offence` |
| Under section 121(3)(a), what is the greatest imprisonment I face on indictment for an offence under section 121 | Punishment | `s 121(3)(a) the punishment on indictment` |
| Under section 121(2), is subscribing to an election fund to obtain or retain a government contract an offence on what I did | MAYBE BOOLEAN | `s 121(2) the contractor subscribes to an election fund to obtain or retain a government contract` |
| Under section 121.1(2), does section 121.1(1) not apply in the circumstances the Excise Act, 2001 describes | MAYBE BOOLEAN | `s 121.1(2) subsection (1) does not apply in the circumstances the Excise Act, 2001 describes` |
| Under section 121.1(3), is a tobacco grower not contravening section 121.1(1) by reason only of possessing raw leaf tobacco described in the Excise Act, 2001 | MAYBE BOOLEAN | `s 121.1(3) the tobacco grower does not contravene subsection (1) by reason only of possessing raw leaf tobacco described in section 31 of the Excise Act, 2001` |
| Under section 121.1(1), is selling, transporting or possessing for sale unstamped tobacco an offence on what I did | MAYBE BOOLEAN | `s 121.1(4) the person who contravenes subsection (1) is guilty of an offence` |
| Under section 121.1(4), is an offence under section 121.1(1) indictable, punishable on summary conviction, or both | `Class of offence` | `s 121.1(4) the class of the offence` |
| Under section 121.1(4)(a), what is the greatest imprisonment I face on indictment for dealing in unstamped tobacco | Punishment | `s 121.1(4)(a) the punishment on indictment` |
| Under section 122, is an official's fraud or breach of trust in connection with the duties of their office an offence on what I did | MAYBE BOOLEAN | `s 122 the official commits fraud or a breach of trust in connection with the duties of their office` |
| Under section 122, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 122 the class of the offence` |
| Under section 122(a), what is the greatest imprisonment I face on indictment | Punishment | `s 122(a) the punishment on indictment` |
| Under section 123(1), is giving or taking a benefit for a municipal official's vote or official act an offence on what I did | MAYBE BOOLEAN | `s 123(1) the person gives, or the municipal official takes, a benefit for a vote or an official act` |
| Under section 123(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 123(1) the class of the offence` |
| Under section 123(1), what is the greatest imprisonment I face on indictment | Punishment | `s 123(1) the punishment on indictment` |
| Under section 123(2), is influencing or attempting to influence a municipal official by suppression of the truth, threats, deceit or unlawful means an offence on what I did | MAYBE BOOLEAN | `s 123(2) the person influences or attempts to influence a municipal official by suppression of the truth, threats, deceit or unlawful means` |
| Under section 123(2), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 123(2) the class of the offence` |
| Under section 123(2), what is the greatest imprisonment I face on indictment | Punishment | `s 123(2) the punishment on indictment` |
| Under section 123(3), is the person a municipal official | MAYBE BOOLEAN | `s 123(3) municipal official` |
| Under section 124, is selling or purchasing, or purporting to sell or purchase, an office an offence on what I did | MAYBE BOOLEAN | `s 124 the person is guilty of an offence under section 124` |
| Under section 124, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 124 the class of the offence` |
| Under section 124, what is the greatest imprisonment I face on indictment | Punishment | `s 124 the punishment on indictment` |
| Under section 125, is influencing or negotiating appointments, or dealing in offices, an offence on what I did | MAYBE BOOLEAN | `s 125 the person is guilty of an offence under section 125` |
| Under section 125, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 125 the class of the offence` |
| Under section 125, what is the greatest imprisonment I face on indictment | Punishment | `s 125 the punishment on indictment` |
| Under section 126(1), is intentionally contravening an Act of Parliament, for which no punishment is expressly provided, an offence on what I did | MAYBE BOOLEAN | `s 126(1) the person is guilty of an offence by intentionally contravening an Act of Parliament` |
| Under section 126(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 126(1) the class of the offence` |
| Under section 126(1)(a), what is the greatest imprisonment I face on indictment | Punishment | `s 126(1)(a) the punishment on indictment` |
| Under section 126(2), may the Government of Canada institute and conduct the proceedings against me | MAYBE BOOLEAN | `s 126(2) proceedings may be instituted at the instance of the Government of Canada` |
| Under section 127(1), is disobeying a lawful order of a court or of a person or body authorized by an Act, for which no punishment is expressly provided, an offence on what I did | MAYBE BOOLEAN | `s 127(1) the person is guilty of an offence by disobeying a lawful order of a court or authorized body` |
| Under section 127(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 127(1) the class of the offence` |
| Under section 127(1)(a), what is the greatest imprisonment I face on indictment | Punishment | `s 127(1)(a) the punishment on indictment` |
| Under section 127(2), may the Government of Canada institute and conduct proceedings against me for contravening the order | MAYBE BOOLEAN | `s 127(2) proceedings for contravening or conspiring to contravene the order may be instituted and conducted at the instance of the Government of Canada` |
| Under section 128, is misconduct, or a false return, by a peace officer or coroner executing process an offence on what I did | MAYBE BOOLEAN | `s 128 the person is guilty of an offence under section 128` |
| Under section 128, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 128 the class of the offence` |
| Under section 128, what is the greatest imprisonment I face on indictment | Punishment | `s 128 the punishment on indictment` |
| Under section 129, is resisting or obstructing an officer, or a person executing process, or failing to assist an officer, an offence on what I did | MAYBE BOOLEAN | `s 129 the person is guilty of an offence under section 129` |
| Under section 129, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 129 the class of the offence` |
| Under section 129(d), what is the greatest imprisonment I face on indictment | Punishment | `s 129(d) the punishment on indictment` |
| Under section 130(1), is falsely representing myself to be a peace officer or public officer, or using a badge or uniform that way, an offence on what I did | MAYBE BOOLEAN | `s 130(1) the person commits an offence under subsection (1)` |
| Under section 130(2), is an offence under section 130(1) indictable, punishable on summary conviction, or both | `Class of offence` | `s 130(2) the class of the offence` |
| Under section 130(2)(a), what is the greatest imprisonment I face on indictment for personating a peace officer | Punishment | `s 130(2)(a) the punishment on indictment` |
| Under section 130.1, must the court treat as an aggravating circumstance that I personated an officer to facilitate another offence | MAYBE BOOLEAN | `s 130.1 the sentencing court is bound to treat as aggravating that the accused personated an officer to facilitate another offence` |
| Under section 131(3), do subsections 131(1) and (1.1) not apply to a statement I made without being specially permitted, authorized or required by law to make it | MAYBE BOOLEAN | `s 131(3) subsections (1) and (1.1) do not apply to a statement made by a person not specially permitted, authorized or required by law to make it` |
| Under section 131(1), is making a false statement under oath or solemn affirmation, knowing it is false and with intent to mislead, perjury on what I did | MAYBE BOOLEAN | `s 131(1) the person commits perjury by a false statement under oath or solemn affirmation` |
| Under section 131(1.1), is making a false statement by video link or under a mutual legal assistance order, knowing it is false and with intent to mislead, perjury on what I did | MAYBE BOOLEAN | `s 131(1.1) the person commits perjury by a false statement given by video link or under a mutual legal assistance order` |
| Under section 131(2), does section 131(1) apply to my statement whether or not it was made in a judicial proceeding | MAYBE BOOLEAN | `s 131(2) subsection (1) applies whether or not the statement is made in a judicial proceeding` |
| Under section 132, is a person who commits perjury guilty of an indictable offence | MAYBE BOOLEAN | `s 132 the person who commits perjury is guilty of an indictable offence` |
| Under section 132, is perjury indictable, punishable on summary conviction, or both | `Class of offence` | `s 132 the class of the offence` |
| Under section 132, what is the greatest imprisonment I face on indictment for perjury | Punishment | `s 132 the punishment on indictment` |
| Under section 133, am I barred from being convicted of perjury on the evidence of only one witness | MAYBE BOOLEAN | `s 133 the accused is barred from being convicted of perjury on the evidence of only one witness unless it is corroborated in a material particular` |
| Under section 134(2), does section 134(1) not apply to a statement I made in the course of a criminal investigation | MAYBE BOOLEAN | `s 134(2) subsection (1) does not apply to a statement made in the course of a criminal investigation` |
| Under section 134(1), is making a false statement under oath or solemn affirmation, without being permitted, authorized or required by law to make it, an offence on what I did | MAYBE BOOLEAN | `s 134(1) the person makes a false statement under oath or solemn affirmation without being permitted, authorized or required by law` |
| Under section 134(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 134(1) the class of the offence` |
| Under section 136(2), is the evidence evidence for the purposes of section 136 | MAYBE BOOLEAN | `s 136(2) the evidence is evidence for the purposes of section 136` |
| Under section 136(1.1), is evidence I gave under section 714.1, 714.2 or 714.3, or by video link, deemed evidence given by a witness in a judicial proceeding | MAYBE BOOLEAN | `s 136(1.1) the evidence is deemed to be evidence given by a witness in a judicial proceeding` |
| Under section 136(1), can I be convicted of giving evidence contrary to my previous evidence as a witness in a judicial proceeding | MAYBE BOOLEAN | `s 136(1) the witness is guilty of giving contradictory evidence` |
| Under section 136(2.1), is the certificate evidence, without proof of the signature, that the evidence was given in a judicial proceeding | MAYBE BOOLEAN | `s 136(2.1) a certificate is evidence that the evidence was given in a judicial proceeding` |
| Under section 136(3), are the proceedings against me barred for want of the consent of the Attorney General | MAYBE BOOLEAN | `s 136(3) the proceedings are barred for want of the consent of the Attorney General` |
| Under section 136(1), is giving contradictory evidence indictable, punishable on summary conviction, or both | `Class of offence` | `s 136(1) the class of the offence` |
| Under section 136(1), what is the greatest imprisonment I face on indictment for giving contradictory evidence | Punishment | `s 136(1) the punishment on indictment` |
| Under section 137, is fabricating something to be used as evidence in a judicial proceeding an offence on what I did | MAYBE BOOLEAN | `s 137 the person fabricates anything to be used as evidence in a judicial proceeding` |
| Under section 137, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 137 the class of the offence` |
| Under section 137, what is the greatest imprisonment I face on indictment | Punishment | `s 137 the punishment on indictment` |
| Under section 138, is signing or using a false affidavit or statutory declaration an offence on what I did | MAYBE BOOLEAN | `s 138 the person is guilty of an offence under section 138` |
| Under section 138, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 138 the class of the offence` |
| Under section 138, what is the greatest imprisonment I face on indictment | Punishment | `s 138 the punishment on indictment` |
| Under section 139(1), is attempting to obstruct justice by indemnifying a surety, or as a surety taking a fee or indemnity, an offence on what I did | MAYBE BOOLEAN | `s 139(1) the person is guilty of an offence under subsection (1)` |
| Under section 139(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 139(1) the class of the offence` |
| Under section 139(1)(c), what is the greatest imprisonment I face on indictment | Punishment | `s 139(1)(c) the punishment on indictment` |
| Under section 139(2), is intentionally attempting to obstruct, pervert or defeat the course of justice in some other manner an offence on what I did | MAYBE BOOLEAN | `s 139(2) the person intentionally attempts to obstruct, pervert or defeat the course of justice otherwise than as subsection (1) describes` |
| Under section 139(2), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 139(2) the class of the offence` |
| Under section 139(2)(a), what is the greatest imprisonment I face on indictment | Punishment | `s 139(2)(a) the punishment on indictment` |
| Under section 139(3), am I deemed wilfully to have attempted to obstruct, pervert or defeat the course of justice | MAYBE BOOLEAN | `s 139(3) the person is deemed wilfully to attempt to obstruct, pervert or defeat the course of justice` |
| Under section 140(1), is misleading a peace officer into starting or continuing an investigation public mischief on what I did | MAYBE BOOLEAN | `s 140(1) the person commits public mischief` |
| Under section 140(2), is public mischief indictable, punishable on summary conviction, or both | `Class of offence` | `s 140(2) the class of the offence` |
| Under section 140(2)(a), what is the greatest imprisonment I face on indictment for public mischief | Punishment | `s 140(2)(a) the punishment on indictment` |
| Under section 141(2), is no offence committed under section 141(1) because of an agreement for compensation, restitution or personal services | MAYBE BOOLEAN | `s 141(2) the exception for diversion agreements applies` |
| Under section 141(1), is asking for or obtaining valuable consideration for agreeing to compound or conceal an indictable offence an offence on what I did | MAYBE BOOLEAN | `s 141(1) the person asks for or obtains valuable consideration for agreeing to compound or conceal an indictable offence` |
| Under section 141(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 141(1) the class of the offence` |
| Under section 141(1)(a), what is the greatest imprisonment I face on indictment | Punishment | `s 141(1)(a) the punishment on indictment` |
| Under section 142, is corruptly taking a reward for helping to recover goods obtained by an indictable offence an offence on what I did | MAYBE BOOLEAN | `s 142 the person corruptly accepts valuable consideration for helping to recover property obtained by an indictable offence` |
| Under section 142, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 142 the class of the offence` |
| Under section 142(a), what is the greatest imprisonment I face on indictment | Punishment | `s 142(a) the punishment on indictment` |
| Under section 144, is breaking a prison, or breaking out of a cell within one, to escape or set someone free an offence on what I did | MAYBE BOOLEAN | `s 144 the person is guilty of an offence under section 144` |
| Under section 144, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 144 the class of the offence` |
| Under section 144, what is the greatest imprisonment I face on indictment | Punishment | `s 144 the punishment on indictment` |
| Under section 145(8), is my failure with lawful excuse because the Attorney General made an election under section 50 of the Contraventions Act | MAYBE BOOLEAN | `s 145(8) the failure is with lawful excuse because the Attorney General has made an election under section 50 of the Contraventions Act` |
| Under section 145(6), is it not a lawful excuse that my appearance notice or undertaking states defectively the substance of the alleged offence | MAYBE BOOLEAN | `s 145(6) a defective statement of the alleged offence in an appearance notice or undertaking is not a lawful excuse` |
| Under section 145(1), is escaping from lawful custody an offence on what I did | MAYBE BOOLEAN | `s 145(1) the person escapes from lawful custody` |
| Under section 145(1), is being at large without lawful excuse before the end of a term of imprisonment an offence on what I did | MAYBE BOOLEAN | `s 145(1) the person is at large before the end of a term of imprisonment without lawful excuse` |
| Under section 145(1), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 145(1) the class of the offence` |
| Under section 145(1)(a), what is the greatest imprisonment I face on indictment for escaping or being at large | Punishment | `s 145(1)(a) the punishment on indictment` |
| Under section 145(2)(a), is failing without lawful excuse to attend court as a release order requires an offence on what I did | MAYBE BOOLEAN | `s 145(2)(a) the person at large on a release order fails without lawful excuse to attend court` |
| Under section 145(2)(b), is failing without lawful excuse to attend court again as required, after appearing, an offence on what I did | MAYBE BOOLEAN | `s 145(2)(b) the person who has appeared fails without lawful excuse to attend court again as required` |
| Under section 145(2)(c), is failing to surrender as an order of a court, justice or judge requires an offence on what I did | MAYBE BOOLEAN | `s 145(2)(c) the person fails to surrender in accordance with an order of the court, justice or judge` |
| Under section 145(2)(d), is failing without lawful excuse to comply with an order made under section 515.01 an offence on what I did | MAYBE BOOLEAN | `s 145(2)(d) the person fails without lawful excuse to comply with an order made under section 515.01` |
| Under section 145(2), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 145(2) the class of the offence` |
| Under section 145(2), what is the greatest imprisonment I face on indictment for failing to attend court or surrender | Punishment | `s 145(2) the punishment on indictment` |
| Under section 145(3), is failing without lawful excuse to appear or attend court as an appearance notice or summons requires an offence on what I did | MAYBE BOOLEAN | `s 145(3) the person named in an appearance notice or served with a summons fails without lawful excuse to appear or attend` |
| Under section 145(3), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 145(3) the class of the offence` |
| Under section 145(3)(a), what is the greatest imprisonment I face on indictment for failing to comply with an appearance notice or summons | Punishment | `s 145(3)(a) the punishment on indictment` |
| Under section 145(4)(a), is failing without lawful excuse to comply with a condition of an undertaking an offence on what I did | MAYBE BOOLEAN | `s 145(4)(a) the person at large on an undertaking fails without lawful excuse to comply with a condition` |
| Under section 145(4)(b), is failing without lawful excuse to appear or attend as a confirmed undertaking requires an offence on what I did | MAYBE BOOLEAN | `s 145(4)(b) the person at large on a confirmed undertaking fails without lawful excuse to appear or attend` |
| Under section 145(4), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 145(4) the class of the offence` |
| Under section 145(4), what is the greatest imprisonment I face on indictment for failing to comply with an undertaking | Punishment | `s 145(4) the punishment on indictment` |
| Under section 145(5)(a), is failing without lawful excuse to comply with a condition of a release order, other than to attend court, an offence on what I did | MAYBE BOOLEAN | `s 145(5)(a) the person at large on a release order fails without lawful excuse to comply with a condition other than to attend court` |
| Under section 145(5)(b), is failing without lawful excuse to comply with an order under section 515(12), 516.1(1) or 522(2.1) an offence on what I did | MAYBE BOOLEAN | `s 145(5)(b) the person bound by an order under section 515(12), 516.1(1) or 522(2.1) fails without lawful excuse to comply` |
| Under section 145(5), is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 145(5) the class of the offence` |
| Under section 145(5), what is the greatest imprisonment I face on indictment for failing to comply with a release order condition | Punishment | `s 145(5) the punishment on indictment` |
| Under section 145(9), is the certificate evidence of its statements without proof of the signature or official character of the person who signed it | MAYBE BOOLEAN | `s 145(9) the certificate is evidence of the statements it contains without proof of the signature or the official character` |
| Under section 145(10), may I, with leave of the court, require the person who made the certificate to attend for cross-examination | MAYBE BOOLEAN | `s 145(10) the accused may, with leave of the court, require the person who made the certificate to attend for cross-examination` |
| Under section 145(11), is the certificate barred from reception in evidence against me for want of reasonable notice before the trial | MAYBE BOOLEAN | `s 145(11) the certificate is barred from reception in evidence for want of reasonable notice before the trial` |
| Under section 146, is permitting an escape, conveying a thing into a prison to help one, or procuring a prisoner's improper discharge an offence on what I did | MAYBE BOOLEAN | `s 146 the person is guilty of an offence under section 146` |
| Under section 146, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 146 the class of the offence` |
| Under section 146, what is the greatest imprisonment I face on indictment | Punishment | `s 146 the punishment on indictment` |
| Under section 147, is rescuing a person from lawful custody, or helping or wilfully permitting an escape, an offence on what I did | MAYBE BOOLEAN | `s 147 the person is guilty of an offence under section 147` |
| Under section 147, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 147 the class of the offence` |
| Under section 147, what is the greatest imprisonment I face on indictment | Punishment | `s 147 the punishment on indictment` |
| Under section 148, is knowingly assisting a prisoner of war to escape an offence on what I did | MAYBE BOOLEAN | `s 148 the person is guilty of an offence under section 148` |
| Under section 148, is the offence indictable, punishable on summary conviction, or both | `Class of offence` | `s 148 the class of the offence` |
| Under section 148, what is the greatest imprisonment I face on indictment | Punishment | `s 148 the punishment on indictment` |
| Under section 149(1), may the court order that my term of imprisonment for an escape be served in a penitentiary | MAYBE BOOLEAN | `s 149(1) the court may order that the term of imprisonment for an escape be served in a penitentiary` |
| Under section 149(2), is what I did an escape | MAYBE BOOLEAN | `s 149(2) escape` |

### Direction and subject sweep (done before the files were closed)

Every question was read against the function it calls. A permission ("may") returns a function named for the permission; a duty ("is bound") a function named for the duty; a bar ("is barred") a function named for the bar; an exemption or exception ("does not apply", "not guilty") a function whose JUST TRUE means the exemption holds; an offence ("is ... an offence on what I did") a function whose JUST TRUE means the offence is made out; a definition ("is ... a public officer") a definition. No question negates the answer of its function. Questions whose name and body were compared word by word for direction or subject: all 268; 264 agree as first written and 4 were retitled by the second pass of 2026-11-12 (below). Names that differ in wording only: "must the court treat as an aggravating circumstance" (function: "is bound to treat"), "can I be convicted of giving evidence contrary to my previous evidence" (function: "the witness is guilty of giving contradictory evidence"), "may I, with leave of the court, require ... to attend" (function: "may, with leave of the court, require the attendance"); each asks the same question in the same direction.

### Second seat-question audit pass of 2026-11-12

**Read: 268 seat questions**, each against the BODY of the layer-1 function it calls (the gate, the `excl` limbs, the answer type and the words quoted in the function's comments), not against its own title, using the tightened test of 2026-11-12 (a different limb, route or scope; a premise, qualifier or consequence the function does not compute; a wrong polarity or modal; a different answer type).
**Retitled after the tightening: 4. Put back: 0** (the first reading of the pass made no retitle that the tightened test excludes, so there was nothing to restore).
The four questions were retitled; each is written out exactly below as it is exported in `ccc5-seat.l4`, and each earlier assertion on it is restated in place in `ccc5-cases-seat.l4` (and, for `s 117.05(1)`, the hand-written cases) with `-- RECONCILED 2026-11-12: was #ASSERT ...`, which carries the previous title.

| question as exported | what the function answers (test) |
| --- | --- |
| Under section 117.05(1), is the justice bound to fix a date for the hearing of the peace officer's application about the things seized from me and direct that notice of it be given | the whole duty, `s 117.05(1) the justice is bound to fix a date for the hearing and direct that notice of it be given`, not only the date (test 1) |
| Under section 117.14(1), may the Governor in Council declare an amnesty period with respect to a weapon, prohibited device, prohibited ammunition, explosive substance or component or part designed exclusively for an automatic firearm | whether the order is for one of those things; it computes no premise that I possess the thing, and the text does not say it (test 2) |
| Under section 127(1), is disobeying a lawful order of a court or of a person or body authorized by an Act, for which no punishment is expressly provided, an offence on what I did | both limbs of who made the order, the court or the authorized body (test 1) |
| Under section 131(3), do subsections 131(1) and (1.1) not apply to a statement I made without being specially permitted, authorized or required by law to make it | only those two subsections, which are the ones section 131(3) limits (test 1) |

**Read, left, with the reason (the cases a reader may expect on this list).**
- `s 113(2)` and `s 117.0101(10)`: each question restates the function's own name (a grant-shaped name over a necessary condition, closed by "only after" and "only if"); the test says not to retitle where the title restates the function's name. Flagged to the lead in case the function names themselves should change, which is outside this pass.
- `s 141(2)`: the question carries "because of an agreement for compensation, restitution or personal services"; the function's name, "the exception for diversion agreements applies", carries the same status.
- `s 121.1(1)` (asked as "Under section 121.1(1)"): the conduct is in subsection (1) and the offence in (4); the function name (`s 121.1(4) the person who contravenes subsection (1) is guilty of an offence`) cites (1), so no premise differs.
- `s 117.01`, asked as the whole section: the function is `s 117.01(3) ...`, which answers for a contravention of (1) or (2); the title names both conducts.
- `s 111(4)`, `s 117.011(4)`, `s 117.05(2)`, asked as "in my absence" against "ex parte": a synonym.
- The class and penalty questions of every offence ("is the offence indictable, punishable on summary conviction, or both"; "what is the greatest imprisonment I face on indictment"): the answer types are the function's own (a class; a term).

## Peeked

Nothing. No file outside `inputs/`, the two skills and the Commons guide copies was opened; nothing of any existing encoding, nothing under `<local tool>`, and no directory under the runs directory other than `dst-ccc5/`. (The session's context carried an index of someone's notes that mentions other encodings; it was not followed and none of the files it names was opened.)
