# NOTES: Employment Act 1968 (Singapore), the keel (`ea-core`, `ea-definitions`)

## What this is, and how it was checked

This is the keel of a three-part encoding of the Employment Act 1968 (Singapore), 2020 Revised Edition, informal consolidation "version in force from 5/12/2025", together with the part agents' work that follows it.
The keel owns lines 1-784 of `EmA1968.txt`: the title page, the Arrangement of Sections, Part 1 (ss 1-7) and all of s 2(1), the definitions.
It also writes the shared vocabulary (`ea-core.l4`) that the parts ea1, ea2 and ea3 use, and `PLAN.md`, which says how.
The source text is a plain-text rendering made by a converter script from Singapore Statutes Online; it is not the official text, and nothing here is verified against the official text.
Every `-- src:` line copies a line of that file with `srcrefs.py quote`; every quoted phrase in a `-- FALSE-kind` or `-- NOTHING-kind` comment was checked mechanically against the converted text (a script, `lint.py` in the keel's scratch folder, that reads the file).

Checked on 2026-11-05 with `l4` 1.6.109 (main, 4c887e0) and the second main build 1.6.108 (main, 2ae7c9b):
- `check.sh` printed 0 errors, 155 assertions satisfied, 0 failed, 0 refused, on 3 modules, the same on the 1.6.108 column ("same").
- `l4 run` of each module shows no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` on either build.
- `python3 -I srcrefs.py check --refs` (and `--strict`) over the three `.l4` files reports 0 problems.
- No assertion is meant to fail. Expected values are written beside each group from the quoted words of the Act, before the function was run.

The seat is the one the parts serve: an employee working in Singapore (or about to start), asking whether the Act covers them, what they are owed, when, and what they can do if it is not given.
The keel has no seat layer of its own.
Its functions answer the first questions an employee asks of any later section: "Am I an employee?", "Am I a workman?", "Is this my employer?", "What counts as my salary?", "What is my rate of pay for a day?"

## Files

- `ea-core.l4`: declarations only, no rule, no assertion. Sixteen types (see `PLAN.md` section 3).
- `ea-definitions.l4`: the 39 definitions of s 2(1), plus the proviso to "workman" as its own function, plus ss 3(1), 5 and 6. 44 functions, and three small types of its own (the kinds of work in "domestic worker", the kinds of thing in "machinery", the salary-period record in "workman"), each prefixed `s 2(1)`.
- `ea-definitions-tests.l4`: 155 assertions.
- `PLAN.md`: for each part its line ranges, the core names it should expect, the seams, the naming rules.
- `PROGRESS.md`: the keel's own memory.
- `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`: supplied with the folder, unchanged.

## Coverage table (lines 1-784)

Every line of 1-784 is in a row. "Reason" numbers are the brief's three reasons for `inert`.

| lines | provision | disposition | encoded as | tests | note |
| --- | --- | --- | --- | --- | --- |
| 1-13 | Title page (Statutes of the Republic of Singapore; 2020 Revised Edition; publisher) | inert (reason 1, not operative) | - | - |  |
| 14-19 | Informal Consolidation page footer; page heading | inert (reason 1) | - | - | The page headers and footers recur at lines 348-349, 398-399, 443-444, 491-492, 540-541, 588-589, 636-637, 684-685, 729-730, 782-783; all inert for the same reason. |
| 20-337 | Arrangement of Sections (the table of contents, Parts 1 to 16 and the five Schedules) | inert (reason 1) | - | - | A table of contents creates no rule. |
| 339 | Long title: "An Act relating to employment." | inert (reason 1) | - | - |  |
| 341 | Date of enactment [15 August 1968] | inert (reason 1) | - | - |  |
| 343-344 | Part 1 heading (Preliminary) | inert (reason 1) | - | - |  |
| 345-346 | s 1 Short title | inert (reason 2, machinery: short title) | - | - |  |
| 348-351 | Page footer, running heading and the heading "Interpretation" | inert (reason 1) | - | - |  |
| 353 | s 2(1) preface: "In this Act, unless the context otherwise requires —" | fork | not a condition on any definition | - | F1 |
| 355-358 | s 2(1) "approved medical institution" | encoded | `s 2(1) "approved medical institution" the institution is one` | 3 assertions | F8 |
| 360-361 | s 2(1) "authorised officer" | encoded | `s 2(1) "authorised officer" the person is one` | 3 assertions | F8 |
| 363-382 | s 2(1) "basic rate of pay" | encoded | `s 2(1) "basic rate of pay" the amount` | 2 assertions | F4 |
| 384-385 | s 2(1) "civil contravention" | encoded | `s 2(1) "civil contravention" the contravention is one` | 3 assertions | F9 |
| 387-388 | s 2(1) "collective agreement" | encoded | `s 2(1) "collective agreement" the agreement is one` | 3 assertions | F9 |
| 390-391 | s 2(1) "confinement" | encoded | `s 2(1) "confinement" the event is a confinement` | 3 assertions |  |
| 393-406 | s 2(1) "constructional contractor" | encoded | `s 2(1) "constructional contractor" the person is one` | 3 assertions | F2 |
| 408-410 | s 2(1) "constructional work" | encoded | `s 2(1) "constructional work" the work is constructional work` | 3 assertions | F2 |
| 412-416 | s 2(1) "contract of service" | encoded | `s 2(1) "contract of service" the agreement is one` | 3 assertions | F2 |
| 418-421 | s 2(1) "contractor" | encoded | `s 2(1) "contractor" the person is one` | 3 assertions |  |
| 423 | s 2(1) "day" | encoded | `s 2(1) "day" the period is a day` | 3 assertions |  |
| 425-428 | s 2(1) "dependant" | encoded | `s 2(1) "dependant" the member of the family is one` | 7 assertions | F7 |
| 430-437 | s 2(1) "dismiss" | encoded | `s 2(1) "dismiss" the ending of the contract is a dismissal` | 4 assertions | F5 |
| 439-441 | s 2(1) "domestic worker" | encoded | `s 2(1) "domestic worker" the person is one` | 4 assertions | F12; the Kind of work type is declared here, not in the core |
| 446-463 | s 2(1) "employee" | encoded | `s 2(1) "employee" the person is one` | 8 assertions | F8; F2; limb (c) of the exclusion list is "[Deleted by Act 55 of 2018]" (line 458), inert (reason 3) |
| 465-481 | s 2(1) "employer" | encoded | `s 2(1) "employer" the person is one` | 5 assertions | F2 |
| 483-505 | s 2(1) "gross rate of pay" | encoded | `s 2(1) "gross rate of pay" the amount` | 2 assertions | F4 |
| 507-510 | s 2(1) "hours of work" | encoded | `s 2(1) "hours of work" the number of hours` | 2 assertions |  |
| 512-531 | s 2(1) "industrial undertaking" | encoded | `s 2(1) "industrial undertaking" the undertaking is one` | 4 assertions | F3 |
| 533-534 | s 2(1) "inspecting officer" | encoded | `s 2(1) "inspecting officer" the person is one` | 2 assertions | F8 |
| 536-547 | s 2(1) "machinery" | encoded | `s 2(1) "machinery" the thing is machinery` | 4 assertions | F2; the Kind of thing type is declared here, not in the core |
| 549-550 | s 2(1) "mediation request" | encoded | `s 2(1) "mediation request" the request is one` | 2 assertions | F9 |
| 552-559 | s 2(1) "medical officer" | encoded | `s 2(1) "medical officer" the person is one` | 5 assertions | F8 |
| 561-563 | s 2(1) "medical practitioner" | encoded | `s 2(1) "medical practitioner" the person is one` | 3 assertions | F2 |
| 565-567 | s 2(1) "no-pay leave" | encoded | `s 2(1) "no-pay leave" the leave is no-pay leave` | 3 assertions |  |
| 569-570 | s 2(1) "overtime" | encoded | `s 2(1) "overtime" the number of hours` | 3 assertions | F13 |
| 572-574 | s 2(1) "place of employment" | encoded | `s 2(1) "place of employment" the place is one` | 3 assertions |  |
| 576-580 | s 2(1) "principal" | encoded | `s 2(1) "principal" the person is one` | 3 assertions |  |
| 582-596 | s 2(1) "productivity incentive payment" | encoded | `s 2(1) "productivity incentive payment" the payment is one` | 5 assertions |  |
| 598-603 | s 2(1) "quarters" | encoded | `s 2(1) "quarters" the building is quarters` | 4 assertions | F2 |
| 605-626 | s 2(1) "salary" | encoded | `s 2(1) "salary" the amount` | 2 assertions | F4 |
| 628-648 | s 2(1) "seafarer" | encoded | `s 2(1) "seafarer" the person is one` | 6 assertions | F14 |
| 650-651 | s 2(1) "stillborn child" | encoded | `s 2(1) "stillborn child" the child is one` | 3 assertions | F9 |
| 653 | Amendment note [Act 19 of 2021 wef 29/05/2022] | inert (reason 1; an amendment note, not a rule) | - | - |  |
| 655-661 | s 2(1) "subcontractor" | encoded | `s 2(1) "subcontractor" the person is one` | 3 assertions | F2 |
| 663-667 | s 2(1) "subcontractor for labour" | encoded | `s 2(1) "subcontractor for labour" the person is one` | 3 assertions |  |
| 669-670 | s 2(1) "Tribunal" | encoded | `s 2(1) "Tribunal" the body is the Tribunal` | 2 assertions | F9 |
| 672 | s 2(1) "wages" | encoded | `s 2(1) "wages" the amount` | 2 assertions |  |
| 674 | s 2(1) "week" | encoded | `s 2(1) "week" the period is a week` | 3 assertions |  |
| 676-711 | s 2(1) "workman" | encoded | `s 2(1) "workman" proviso: the person is deemed to be a workman`; `s 2(1) "workman" the person is one` | 15 assertions | F6; the proviso (lines 697-705) is its own function |
| 713 | Amendment note [6/2014; 27/2015; 21/2016; 55/2018; 19/2021] | inert (reason 1) | - | - |  |
| 715 | s 2(2) [Deleted by Act 55 of 2018] | inert (reason 3, shown repealed) | - | - |  |
| 717 | Heading "Appointment of officers" | inert (reason 1) | - | - |  |
| 719-727 | s 3(1) Commissioner, Deputy and Assistant Commissioners | encoded | `s 3(1) the officer's performance of the Commissioner's duty or exercise of the Commissioner's power is deemed duly done` | 3 assertions | F10; the Minister's power to appoint is the first clause and is left to the Minister, see Jural relations |
| 732-734 | s 3(2) Appointment of authorised officers, inspecting officers and other officers | inert (reason 2, staffing) | - | - | F10: the appointment is a fact asked by `s 2(1) "authorised officer"` and `s 2(1) "inspecting officer"` |
| 736 | Amendment note [27/2015] | inert (reason 1) | - | - |  |
| 738-743 | s 3(3) Authorised persons | inert (reason 2, staffing) | - | - |  |
| 745 | Amendment note [21/2016] | inert (reason 1) | - | - |  |
| 747-758 | s 3(4) Authorisation of authorised persons | inert (reason 2, staffing) | - | - |  |
| 760 | Amendment note [21/2016] | inert (reason 1) | - | - |  |
| 762-765 | s 4 Rules and orders for the conduct of officers' duties | inert (reason 2, rule-making power) | - | - |  |
| 767-771 | s 5 Minister may restrict application | encoded | `s 5 this Act, or the Part or provision, applies at the premises` | 4 assertions | F11 |
| 773-778 | s 6 Existing law not affected | encoded | `s 6 this Act relieves the employer of the duty or liability`; `s 6 this Act limits the power given to the public officer` | 4 assertions | two functions, one for the employer's duty and one for the public officer's power |
| 780 | s 7 [Repealed by Act 32 of 2008] | inert (reason 3, shown repealed) | - | - |  |
| 782-784 | Page footer and running heading | inert (reason 1) | - | - |  |

## Fork register

### Rulings of 2026-11-04 (word for word from the brief)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

How E1 and N2 applied in the keel:
- E1. No effect is gathered across sections in the keel. Each definition is its own answer (option C). No hand-gathering function (option B) was written; the closest thing is that `s 2(1) "employee"` collects the limbs and exclusions of its own single definition, which is the definition itself and not a gathering across sections.
- N2. The flat negatives in the keel's range ("does not include" in "employee", "seafarer" and "productivity incentive payment"; "does not apply" in s 5; "Nothing in this Act operates" in s 6) are answered `JUST FALSE`. None of them names a bearer of a prohibition, so no `SHANT` is derived from any. The Hohfeld kinds are in `## Jural relations` below and are not typed into any answer.

### Forks decided by the keel (each lists the reading taken and the other reading)

- **F1. The preface of s 2(1), "unless the context otherwise requires".** Taken: each definition applies as written, and no function takes an input for the preface, because no fact a witness could state would say what the context requires. Other reading: a caller could argue that a particular section's context requires another meaning; a part that thinks so may decline to call the definition and say why in its own fork register.
- **F2. "means X and includes Y" (policy P-INC), applied uniformly.** Taken: `JUST TRUE` if the case falls within X or within Y, and `NOTHING` (NOTHING-kind includes) otherwise. Applies to "constructional contractor", "constructional work", "contract of service", "employer", "industrial undertaking", "medical practitioner", "quarters", "subcontractor", for "machinery", which says only "includes", to anything not in the list, and for "employee" and "dismiss", whose last branch is the same `NOTHING` (eleven branches carry `NOTHING-kind (includes)`). Other reading: because the definition begins "means", a case outside X and Y is `JUST FALSE`. The brief's rule gives FALSE for "means" and NOTHING for "includes"; a definition that has both words has no stated priority, so the keel chose one policy and applied it to all, rather than a different answer per definition.
- **F3. "industrial undertaking" read literally.** Taken: "means public and private undertakings and any branch thereof" makes any undertaking an industrial undertaking, and the four kinds after "includes particularly" are examples; the function answers `JUST TRUE` for any undertaking or branch of one. Other reading (the purposive one): only the four listed kinds are industrial; then a retail shop is not. Parts that rely on the term should read it with this in mind.
- **F4. The three pay terms.** `Pay for a period` (in the core) lists the items the Act mentions, one NUMBER each. "basic rate of pay", "gross rate of pay" and "salary" are three functions over it, each a sum minus the items its own limbs leave out. Taken: commissions are counted in all three, because no exclusion list mentions them; the six items that are not money paid for working (value of an amenity, value of a service excluded by order, value of a travelling concession, the employer's contributions to a pension or provident fund, a gratuity, a retrenchment benefit) never enter "basic" or "gross", and are listed in "salary" only to be taken out again by its limbs (a)-(f). Other reading: a commission that varies with output is a "productivity incentive payment" and so excluded from "basic" and "gross"; the caller then states it under that item.
- **F5. "dismiss" and the resignation that is forced.** Taken: the includes-limb says "if the employee can show ... that the employee did not resign voluntarily"; where the employee resigned and cannot show it, the includes-limb answers `JUST FALSE` (a failed "if", marginal reading (a)); where the contract ended in some other way that is neither at the employer's initiative nor a resignation, `NOTHING` (F2). Other reading: a resignation not shown forced is `NOTHING`, because "if" does not itself say "only if".
- **F6. The proviso to "workman".** Taken: the proviso is printed under limb (c) by the converter, but it speaks of "any person ... employed by any one employer partly as a workman and partly in some other capacity or capacities", so it is read as qualifying the whole definition, and it is its own function (`s 2(1) "workman" proviso: the person is deemed to be a workman`) over a list of salary periods. It deems `JUST TRUE` unless it is established that, in every salary period, the workman time was less than one-half of the total (`JUST FALSE` then means only "the proviso does not deem", never "not a workman"; the main function never reads it as a no). With no salary period recorded, the exception is not established, so the person is deemed a workman. Other readings: the proviso qualifies limb (c) only; or with no period recorded the answer is `NOTHING`. The First Schedule (limb (d)) is an input from ea3.
- **F7. "dependant".** Taken: "living with or dependent on the employee" qualifies "any adopted or illegitimate child" only, not "child"; "child" is not defined in s 2(1), so a stepchild and a child the employee fosters are `NOTHING` (NOTHING-kind undefined term); a relationship the list does not name is `JUST FALSE` ("means any of the following ... namely"). Other readings: the qualifier attaches to every child; or a stepchild is a "child" (`JUST TRUE`).
- **F8. Declarations and appointments made outside the sources.** The Gazette notifications of the Minister and the President, and the appointments under s 3(2), are not among the sources. Whether one was made is a plain BOOLEAN input in "approved medical institution", "authorised officer", "inspecting officer", "medical officer" (limb (b)), "employee" (the Government limb and limb (d) of the exclusions), "employer" (limb (a), the Government) and "workman" (limb (e)). An unmade declaration is `false` and the function then answers from its other limbs.
- **F9. Terms that point to another Act, or to a section in another part.** "collective agreement" (Industrial Relations Act 1960), "mediation request" (Employment Claims Act 2016), "stillborn child" (Registration of Births and Deaths Act 2021), "Tribunal" (State Courts Act 1970), and "civil contravention" (s 126A, in ea3's range) each take the other source's answer as a `MAYBE BOOLEAN` input and pass a `NOTHING` on; `JUST FALSE` appears only when the other source says no. The same shape is used for the Part 4 limit in "overtime" (F13) and for the First Schedule in "workman".
- **F10. Staffing is inert, and s 3(1) is encoded for what it does to an employee.** ss 3(2)-(4) and 4 are machinery (reason 2). s 3(1) is encoded: an act of a Deputy, Principal Assistant or Assistant Commissioner for Labour is deemed done by the Commissioner, unless a limitation prescribed under s 3(1) applies (then `NOTHING`, limited by its own wording). Other reading: a prescribed limitation that applies is a no (`JUST FALSE`); see Marginal readings.
- **F11. s 5.** Taken: where the Minister has declared, the declaration covers the Part or provision, and the premises are within the notification, the Act does not apply there (`JUST FALSE`, a flat negative); in every other case the answer is `NOTHING` (silent), never `JUST TRUE`, because s 5 only takes premises out and nowhere says the Act applies to the rest. The caller states the three facts.
- **F12. "domestic worker".** Taken: "employed in or in connection with the domestic services of any private premises" qualifies all four named kinds (house servant, stable servant, garden servant, motor car driver). Other reading: it qualifies only the last.
- **F13. "overtime" and "hours of work".** "overtime" is the hours worked in a day or week in excess of "the limits specified in Part 4"; the limit is Part 4's answer (ea1, ss 38 and 40) and is a `MAYBE NUMBER` input, so a `NOTHING` from Part 4 gives `NOTHING`. "hours of work" is the hours at the employer's disposal less the intervals allowed for rest and meals, with no clamp: if the caller states more interval hours than hours at disposal, the result is negative, and the Act does not say what then.
- **F14. "seafarer" limb (d).** The harbour craft or pleasure craft must be licensed under regulations made under s 41 of the Maritime and Port Authority of Singapore Act 1996 and used within a port declared under s 3 of that Act. Both borrowed facts are asked as one BOOLEAN.

### Reading a result: FALSE and NOTHING

In this row, a decision function is asked of one case, for example "is this person an employee?".
`JUST TRUE` and `JUST FALSE` are answers the Act gives in its own words.
`JUST FALSE` appears only where the Act itself says no: a definition that says "means" and the case is not within it; "but does not include"; "does not apply"; "Nothing in this Act operates"; "unless".
It is never the answer to "the Act does not say".
`NOTHING` means the Act does not answer on these facts: a list the Act does not close ("includes"), a term the Act does not define (a stepchild is neither named nor excluded by "dependant", because "child" is undefined), a case the Act is silent on, a fact that lies outside the sources (the other Acts, the Gazette), or a grant limited by its own wording (s 3(1), "subject to such limitations as may be prescribed").
Example: a person registered under neither Act is `NOTHING` as a "medical practitioner" (the definition "includes" a dentist and does not close the class), whereas a person on board a ship who is a pilot is `JUST FALSE` as a "seafarer" ("but does not include (a) a pilot").
A caller must never turn `NOTHING` into `FALSE`: it means "the Act does not say", and a person who needs a yes or no from it has to ask a lawyer.

## Marginal readings for a lawyer

The brief's two readings are taken as the status quo: (a) a failed "if" is the text's no, clause by clause, and flat negatives are noes; (b) a prohibition or grant limited by its own wording is not a no.
Every branch in the keel that rests on one of them:

| function | branch | rests on | reading taken | other reading |
| --- | --- | --- | --- | --- |
| `s 2(1) "employee" the person is one` | seafarer, domestic worker, or a class the Minister has declared: `JUST FALSE` | (a) flat negative, "but does not include any of the following" | a no | `NOTHING` |
| `s 2(1) "seafarer" the person is one` | pilot, port worker, person temporarily on the ship in port, harbour craft: `JUST FALSE` | (a) flat negative, "but does not include" | a no | `NOTHING` |
| `s 2(1) "productivity incentive payment" the payment is one` | forms part of regular remuneration: `JUST FALSE` | (a) flat negative, "but does not include any payment which forms part of the employee's regular remuneration" | a no | `NOTHING` |
| `s 2(1) "dismiss" the ending of the contract is a dismissal` | resigned and cannot show it was forced: `JUST FALSE` | (a) a failed "if" (F5) | a no | `NOTHING` |
| `s 2(1) "dependant" the member of the family is one` | adopted or illegitimate child neither living with nor dependent on the employee: `JUST FALSE` | (b) a grant limited by its own wording, "living with or dependent on the employee" (F7) | a no | `NOTHING`, because the limit is a limit on the grant and not a statement that others are excluded |
| `s 5 this Act, or the Part or provision, applies at the premises` | declared, covered, premises within: `JUST FALSE` | (a) flat negative, "does not apply" | a no | `NOTHING` |
| `s 6 this Act relieves the employer of the duty or liability`, `s 6 this Act limits the power given to the public officer` | duty or power under another written law: `JUST FALSE` | (a) flat negative, "Nothing in this Act operates" | a no | `NOTHING` |
| `s 6` (both functions) | duty or power not under another written law: `NOTHING` | (b) limited by its own wording, "imposed ... by any other written law" | not covered | `JUST TRUE` that the Act may relieve or limit |
| `s 3(1) the officer's performance ... is deemed duly done` | a prescribed limitation applies: `NOTHING` | (b) limited by its own wording, "subject to such limitations as may be prescribed" | not covered | `JUST FALSE` |
| the eleven P-INC branches of F2 | the case is outside both "means" and "includes": `NOTHING` | not the brief's reading (a) or (b): a policy between "means" (FALSE) and "includes" (NOTHING) | `NOTHING` | `JUST FALSE` |

## Jural relations

One row per provision of lines 1-784.
Definitions create no relation and are listed once each as `none`.
No `SHANT` is derived in the keel (see N2 above): the flat negatives in its range name no bearer of a prohibition.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| Title page, Arrangement of Sections, long title, date of enactment, Part 1 heading, page headers, amendment notes (lines 1-351 other than s 1, and 653, 713, 736, 745, 760, 782-784) | none | none | none | - |
| s 1 | none | none | none | - |
| s 2(1) preface | none | none | none | - |
| s 2(1) "approved medical institution" | none | none | none (a definition) | `s 2(1) "approved medical institution" the institution is one` |
| s 2(1) "authorised officer" | none | none | none (a definition) | `s 2(1) "authorised officer" the person is one` |
| s 2(1) "basic rate of pay" | none | none | none (a definition) | `s 2(1) "basic rate of pay" the amount` |
| s 2(1) "civil contravention" | none | none | none (a definition) | `s 2(1) "civil contravention" the contravention is one` |
| s 2(1) "collective agreement" | none | none | none (a definition) | `s 2(1) "collective agreement" the agreement is one` |
| s 2(1) "confinement" | none | none | none (a definition) | `s 2(1) "confinement" the event is a confinement` |
| s 2(1) "constructional contractor" | none | none | none (a definition) | `s 2(1) "constructional contractor" the person is one` |
| s 2(1) "constructional work" | none | none | none (a definition) | `s 2(1) "constructional work" the work is constructional work` |
| s 2(1) "contract of service" | none | none | none (a definition) | `s 2(1) "contract of service" the agreement is one` |
| s 2(1) "contractor" | none | none | none (a definition) | `s 2(1) "contractor" the person is one` |
| s 2(1) "day" | none | none | none (a definition) | `s 2(1) "day" the period is a day` |
| s 2(1) "dependant" | none | none | none (a definition) | `s 2(1) "dependant" the member of the family is one` |
| s 2(1) "dismiss" | none | none | none (a definition) | `s 2(1) "dismiss" the ending of the contract is a dismissal` |
| s 2(1) "domestic worker" | none | none | none (a definition) | `s 2(1) "domestic worker" the person is one` |
| s 2(1) "employee" | none | none | none (a definition) | `s 2(1) "employee" the person is one` |
| s 2(1) "employer" | none | none | none (a definition) | `s 2(1) "employer" the person is one` |
| s 2(1) "gross rate of pay" | none | none | none (a definition) | `s 2(1) "gross rate of pay" the amount` |
| s 2(1) "hours of work" | none | none | none (a definition) | `s 2(1) "hours of work" the number of hours` |
| s 2(1) "industrial undertaking" | none | none | none (a definition) | `s 2(1) "industrial undertaking" the undertaking is one` |
| s 2(1) "inspecting officer" | none | none | none (a definition) | `s 2(1) "inspecting officer" the person is one` |
| s 2(1) "machinery" | none | none | none (a definition) | `s 2(1) "machinery" the thing is machinery` |
| s 2(1) "mediation request" | none | none | none (a definition) | `s 2(1) "mediation request" the request is one` |
| s 2(1) "medical officer" | none | none | none (a definition) | `s 2(1) "medical officer" the person is one` |
| s 2(1) "medical practitioner" | none | none | none (a definition) | `s 2(1) "medical practitioner" the person is one` |
| s 2(1) "no-pay leave" | none | none | none (a definition) | `s 2(1) "no-pay leave" the leave is no-pay leave` |
| s 2(1) "overtime" | none | none | none (a definition) | `s 2(1) "overtime" the number of hours` |
| s 2(1) "place of employment" | none | none | none (a definition) | `s 2(1) "place of employment" the place is one` |
| s 2(1) "principal" | none | none | none (a definition) | `s 2(1) "principal" the person is one` |
| s 2(1) "productivity incentive payment" | none | none | none (a definition) | `s 2(1) "productivity incentive payment" the payment is one` |
| s 2(1) "quarters" | none | none | none (a definition) | `s 2(1) "quarters" the building is quarters` |
| s 2(1) "salary" | none | none | none (a definition) | `s 2(1) "salary" the amount` |
| s 2(1) "seafarer" | none | none | none (a definition) | `s 2(1) "seafarer" the person is one` |
| s 2(1) "stillborn child" | none | none | none (a definition) | `s 2(1) "stillborn child" the child is one` |
| s 2(1) "subcontractor" | none | none | none (a definition) | `s 2(1) "subcontractor" the person is one` |
| s 2(1) "subcontractor for labour" | none | none | none (a definition) | `s 2(1) "subcontractor for labour" the person is one` |
| s 2(1) "Tribunal" | none | none | none (a definition) | `s 2(1) "Tribunal" the body is the Tribunal` |
| s 2(1) "wages" | none | none | none (a definition) | `s 2(1) "wages" the amount` |
| s 2(1) "week" | none | none | none (a definition) | `s 2(1) "week" the period is a week` |
| s 2(1) "workman" | none | none | none (a definition) | `s 2(1) "workman" proviso: the person is deemed to be a workman`; `s 2(1) "workman" the person is one` |
| s 2(2) | none | none | none (repealed) | - |
| s 3(1) | The Deputy Commissioner, Principal Assistant Commissioner or Assistant Commissioner for Labour holds the Commissioner's power; the Minister holds the power to appoint | Anyone subject to the Commissioner's duties and powers is subject to the officer's exercise of them (liability); no duty of an individual is created | power / liability (Minister's appointment: power / liability of the officer appointed) | `s 3(1) the officer's performance of the Commissioner's duty or exercise of the Commissioner's power is deemed duly done` |
| s 3(2) | The Minister (power to appoint authorised officers, inspecting officers and others) | The officers appointed (liability) | power / liability | not encoded (inert, machinery); the appointment is an input of `s 2(1) "authorised officer"` and `s 2(1) "inspecting officer"` |
| s 3(3) | The Commissioner (power to appoint an authorised person in writing) | The person appointed (liability) | power / liability | not encoded (inert, machinery) |
| s 3(4) | Each authorised person (claim to a written authorisation specifying the functions, powers, conditions and limitations) | The Commissioner (duty: "must, in writing, issue") | claim / duty | not encoded (inert, machinery) |
| s 4 | The Minister (power to make rules and orders for the conduct of officers' duties) | The officers (liability) | power / liability | not encoded (inert, rule-making) |
| s 5 | The Minister (power to declare, by notification in the Gazette, that the Act or a Part or provision does not apply to specified premises or a class of premises) | Those at the specified premises are subject to the declaration (liability); its stated effect is that the Act does not apply there | power / liability | `s 5 this Act, or the Part or provision, applies at the premises` |
| s 6 | The employer's duties and liabilities under another written law, and a public officer's powers under another written law, are immune from being relieved or limited by this Act | This Act cannot relieve or limit them (disability) | immunity / disability | `s 6 this Act relieves the employer of the duty or liability`; `s 6 this Act limits the power given to the public officer` |
| s 7 | none | none | none (repealed) | - |

## Findings

### What the main binary does not accept

- A `GIVEN` written once under a `§` heading and shared by the rules after it. Measured 2026-11-05 on 1.6.108 and on 1.6.109: the rules report `check/unknown-identifier` for the name the section `GIVEN` introduced. Every rule in these files carries its own `GIVEN`. (`dialects.md` says the same; this was probed, not copied.)
- `length` and `isEmpty` are not names in the prelude of 1.6.109 (a probe with `#CHECK length` and `#CHECK isEmpty` gave `check/unknown-identifier`). `null`, `all` and `sum` are; the files use those.

### A slow case that gives no error (measured, loud only by waiting)

A function that adds up about a dozen `pay's `field`` terms with `PLUS`, through local names defined in a `WHERE` block after the expression that uses them, did not finish `l4 check` in 60 seconds on 1.6.109 (killed), with no error and no output.
Moving the local definitions above the expression made 1.6.109 finish that function in under a second, but 1.6.108 still did not finish the pay section in 25 seconds.
Writing the sum as `sum (LIST ...)` over inline field projections, one term per line, finishes in about a second on both builds, so `ea-definitions.l4` is written that way.
The reason was not investigated; the lesson for the parts is in `PLAN.md` section 6.

## Unstable dialect

I looked at time, versions and workarounds in lines 1-784 (the definitions and ss 1-7), found no shape that the unstable dialect would express better than the main one (there is no dated alternative, deadline or amendment in force from different days in that range, and the one workaround, repeating `GIVEN` on every rule, is small), and so the keel has no second encoding.
The Act's dated shapes are in the parts' ranges (`PLAN.md` section 6); whether any of them earns a second encoding is for the part that owns it to judge.
