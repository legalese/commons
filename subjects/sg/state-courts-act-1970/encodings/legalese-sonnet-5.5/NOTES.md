# NOTES -- State Courts Act 1970 (Singapore), 2020 Revised Edition -- `legalese-sonnet-5.5`

Status: **draft**, target **main**.
No domain expert has read this encoding against the text; see `encoding.json` (`not_reviewed`).
The method is a single Sonnet 5.5 agent working alone from a brief.

The source is `SCA1970.txt`, a converter's plain-text rendering of the Singapore Statutes Online page https://sso.agc.gov.sg/Act/SCA1970, retrieved 2026-10-01 (sha256 `bb9fa01320f7a370fe8bbc6158a77a2eff632772888911fb61f8c0f6ae617051`).
It is an unofficial consolidation and not the official text (see `SOURCE-LICENSE.md`).
**Which version this encodes, and the two dates.**
The text is the version whose banner (`SCA1970.txt` line 15, repeated on every page, 71 times) reads "Informal Consolidation – version in force from 1/12/2023"; the title page (lines 4-7) says the 2020 Revised Edition "incorporates all amendments up to and including 1 December 2021 and comes into operation on 31 December 2021".
The metadata beside the file (`SCA1970.meta.json`, field `in_force`) says "Current version as at 01 Oct 2026" and `retrieved_date` is 2026-10-01.
**I encoded from the text as printed, so the version is the one in force from 1/12/2023.**
The two dates do not describe two texts: the banner dates when this version began and the metadata dates the day SSO showed it as the current one.
Its list of earlier versions (`historical_versions`) ends at 2022-04-01, which fits the banner.
I did not check the SSO page again, so whether a later version has appeared since 2026-10-01 is not known to this encoding.

Built with `l4` 1.6.109 (main, 4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`; `check.sh` compared it with the main build 1.6.108 (main, 2ae7c9b, 2026-11-02).
`JL4_LIBRARY_PATH` was left unset.

## Scope and edition

Encoded: the whole Act as printed in the file, ss 1 to 70 and the Schedule (the three oaths), in two layers.
Layer 1 is the law, one module per Part (Part 4 in three modules), with a nouns module first, each rule citing its lines of the text (`@ref ... (src:A-B)`, checked by `srcrefs.py`) and tested.
Layer 2 is the seat: `sca-seat.l4` (61 exported questions) and `sca-cases-seat.l4` (worked cases).

The monetary limits are the Act's own figures, $250,000 and $60,000 (s 2).
An order under s 30 or s 52(3) can change them; the layer-1 rules take the order's amount as an optional input and the seat passes "no order", so **if an order has been made, every seat answer that turns on a limit is an answer for the old figure** (fork F-LIMIT).

## Seat

**A person who wishes to start or defend a civil case in a State Court (a District Court or a Magistrate's Court), asking, on facts they can state, which court has jurisdiction, within what monetary limit, and what powers the court has.**

Why: Commons asks every Act from the position of the individual to whom the law is applied, and the Legalese website turns the seat layer into a question form.
The Act is mostly addressed to courts and officers, so the seat re-expresses what the Act decides about jurisdiction, limits, powers, costs, enforcement, appeals and transfers as the questions that person would ask ("Does a District Court have jurisdiction to hear and try my civil case?", "May I give up the part of my claim above the District Court limit ...?", "Can I appeal ...?").
There is no seat for an official.
Provisions that address only an official (the constitution of the courts, appointments, offices, the Rules Committee, the Chief Justice's and the Presiding Judge's administrative powers) are encoded in layer 1 for what they decide, and the person meets them only through the seat's questions where those matter to them (for example ss 57, 62, 63, 65 and 68).

The seat layer imports the layer-1 modules and calls their rules.
It does not restate a rule and no layer-1 module changes to suit it.
Its only logic is wiring: building a module's inputs from plain answers, reading "I am not sure" as `NOTHING`, and reading the Act's two figures as the limits.
The questions are grouped under `§§` headings in the order of the text.

Two seat inputs feed more than one record field, which a lawyer reading s 19(3)(c) against (d), or (a) against (b), will notice.
"Does a written law give this kind of case to another court or tribunal?" feeds both `jurisdiction over the action is vested exclusively in ...` (s 19(3)(c)) and `jurisdiction over the action is expressly excluded by written law` (s 19(3)(d)), because a person cannot be expected to say which of the two it is.
"Is my case a supervisory or review matter?" feeds both s 19(3)(a) (supervisory or revisionary jurisdiction) and s 19(3)(b) (judicial review of an act or decision).
Both are plain inputs and the module still tests each paragraph separately.

### Reading a result: FALSE and NOTHING

`JUST TRUE` and `JUST FALSE` are answers the Act itself gives.
`NOTHING` means the Act, as encoded, does not answer on the facts given; **never read `NOTHING` as no.**

In this row a "no" (`JUST FALSE`) is given only where the text says no in its own words: "does not include" (ss 19(3), 19(4), 52(1A)); a "means" definition (s 2); an "if", "where", "unless" or "until" that is not met ("a District Court has jurisdiction ... where" the defendant is served or submits, s 19(2); "Where" the amount exceeds the limit and a District Court would otherwise have jurisdiction, the claimant may give up the excess, s 22(1)); a ceiling ("not exceeding $100 for each offence", s 67(3); "not exceeding 15 days in any calendar year", s 61); or a flat negative ("must not", "shall not", "cannot": ss 35, 43(3), 48(1), 63(2), 65, 66).
A "no" is worded for its section: `s 23 this section gives a District Court jurisdiction ...` answering `JUST FALSE` means this section gives none on these facts, not that no jurisdiction exists.

"Not covered" (`NOTHING`) is given where the text lists without closing the list (s 3(1), s 26, s 31, s 52(1B)); says "includes" (s 2 "seal", s 49B(3)); leaves a term to someone else's judgment ("if it thinks fit", "it appears to the court"); is silent (what follows when a bare "must" is not done: ss 5, 6, 17, 49B(2), 59, 62(6)); points outside the sources (Rules of Court, the Criminal Procedure Code 2010, the Supreme Court of Judicature Act 1969, orders under s 30 or s 52(3)); or limits a grant in its own wording and the case falls outside the limit (for example s 19(2) is for "any action in personam", s 25 is for actions "for the recovery of immovable property").
Every branch that answers one or the other carries a comment `-- FALSE-kind (the text says no in its own words): "..."` or `-- NOTHING-kind (...)` in the module, 138 and 197 comments in all.
A caller must never turn `NOTHING` into `FALSE`.

Two shapes carry no kind comment on a `JUST FALSE`, and the grep `JUST FALSE` against `FALSE-kind` will show them.
First, a **classifier helper** (the functions named `... falls within a class ...` and `... exceeds ...`: in ss 19(3) and 19(4) they return `JUST TRUE` or `JUST FALSE`, and their s 52(1A) counterparts return a plain `BOOLEAN`) answers a plain yes/no fact about the case ("no listed class applies"), not the text's no about a grant; the grant is in the function that calls it, and that function carries the kind comment.
Second, where several adjacent `WHEN ... THEN JUST FALSE` arms of one `CONSIDER` are the same kind (`s 57(1)` has three such arms for Saturday, Sunday and a public holiday under one comment; `s 6A(1)` repeats its comment on each arm), one comment above the first covers the group.
A mechanical check of every line whose result is `JUST FALSE` or `NOTHING` against a kind comment on that line or in the four lines above found 335 result lines, 2 without one (the two classifier helpers above, now carrying a plain comment saying so).

## Jural relations

One row per provision or group of provisions that creates a relation, with the holder of the right, privilege, power or immunity, the bearer of the correlative duty, no-right, liability or disability, the section, and the L4 rule.
A provision that creates none (a definition, a counting rule, machinery) is listed as `none`.
Some rows group provisions that create the same relation (for example the District Court's jurisdiction grants in ss 19(2) to (6), 22, 23, 25, 26, 28 and 29(1)); every provision in a grouped range appears in some row, and the coverage table is the place that proves each provision is disposed of.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | section | L4 rule |
| --- | --- | --- | --- | --- |
| s 1, s 2 (definitions) | none | none | s 1; s 2 | none (definitions and a rule of reading: `s 2 the definitions in this section apply to this provision`) |
| s 3(1), (1A), (2), (4), (5) | none (constitutive: names the courts and says what jurisdiction each has) | none | s 3 | `s 3(1) ...`, `s 3(1A) ...`, `s 3(2) ...`, `s 3(4) ...`, `s 3(5) ...` |
| s 4 | the President: power to constitute State Courts | the State Courts (their existence); no person | s 4 | `s 4 the State Court is constituted ...` |
| s 5 | the State Courts: power to have and use a seal | the Chief Justice: the power to prescribe its nature; no person | s 5 | `s 5 ...` |
| s 6 | a person served with process: claim that it be signed by a judicial officer and bear the court's seal | the State Courts / judicial officers (duty to sign and seal); "Subject to Rules of Court" | s 6 | `s 6 the process ...`; regulative `s 6 duty: ...` |
| s 6A(1) | a person attending a State Court: no claim that it sits on Saturdays, Sundays and public holidays | the State Courts: duty to sit on other days; privilege not to sit on those days | s 6A(1) | `s 6A(1) ...` |
| s 6A(2) | a judicial officer: privilege to sit on those days if directed or if urgent | no-right of everyone else to object | s 6A(2) | `s 6A(2) ...` |
| s 6A(3) | the Chief Justice: power to appoint times and places | State Courts: liability, and duty to sit as appointed | s 6A(3) | `s 6A(3) ...` |
| s 7(1) | the public: privilege to have access | State Court: disability to exclude without s 7(2) | s 7(1) | `s 7(1) ...` |
| s 7(2), (2AB) | a State Court: power to hear in private (or, under (2AB), to hear otherwise than in private) | parties and the public: liability to a private hearing | s 7(2), (2AB) | `s 7(2) ...`, `s 7(2AB) ...` |
| s 7(2AA) | none stated (a duty on the court) | a State Court: duty to hear a national-interest application in private | s 7(2AA) | `s 7(2AA) ...` |
| s 7(2A), (3) | a State Court: power to order redaction / to forbid publication | witnesses' persons and the public: liability to the order; (3) bearer: any person | s 7(2A), (3) | `s 7(2A) ...`, `s 7(3) ...` |
| s 7(4) | the State (prosecution): claim that orders be obeyed | any person: duty not to contravene an order (offence, fine up to $5,000 or 12 months or both) | s 7(4) | `s 7(4) ...`; regulative `s 7(4) duty: ...` |
| s 7(5) | a State Court: power (discretion) to permit individuals to be present | a journalist, an interested individual, another individual: liability to be permitted or not | s 7(5) | `s 7(5) ...` |
| s 7(6), (7) | none (what the court may consider; definitions) | none | s 7(6), (7) | `s 7(6) ...`, `s 7(7) ...` |
| s 8(1) | a State Court: power to conduct hearings through electronic means | parties: liability to an electronic hearing | s 8(1) | `s 8(1) ...` |
| s 8(2) | none (a savings rule) | none | s 8(2) | `s 8(2) ...` |
| s 8(3) | a party to a civil proceeding: immunity from audio-only oral evidence unless all consent | State Court: disability to conduct audio-only (duty not to) | s 8(3) | `s 8(3) ...` (two functions); regulative `s 8(3) duty: ...` |
| s 8(4), (5) | a party: immunity from an unfair electronic hearing (5); the court: no audio-only finding for an insignificant disruption (4) | State Court: duty not to hold an unfair electronic hearing (5) | s 8(4), (5) | `s 8(4) ...`, `s 8(5) ...` |
| s 8(6) | none (a deeming) | none | s 8(6) | `s 8(6) ...` |
| s 8A(2), (3), (4) | the Presiding Judge: privilege to sit and, after the appointment ends, to give judgment | everyone else: no-right | s 8A | `s 8A(2) ...`, `s 8A(3) ...`, `s 8A(4) ...` |
| s 9(3), (3A), (4), (5); s 10(2), (3); s 12(2) | the Chief Justice and the President: power to appoint a qualified person (no claim by the candidate) | the candidate: liability to be appointed or not; disability to be appointed unless qualified | ss 9, 10, 12 | `s 9(3) ...`, `s 9(3A) ...`, `s 9(4) ...`, `s 9(5) ...`, `s 10(2) ...`, `s 10(3) ...`, `s 12(2) ...` |
| s 11(2), s 12(3), s 13 | Justices of the Peace, the registrar and deputy registrars: powers | the persons subject to those powers: liability | ss 11(2), 12(3), 13 | `s 11(2) ...`, `s 12(3) ...`, `s 13 ...` |
| s 15(1) | the State Courts: claim that bailiffs and process servers execute, return and arrest | bailiffs and process servers: duty | s 15(1) | `s 15(1) ...`; regulative `s 15(1)(a)`, `(b)`, `(c)` |
| s 15(2), s 15A | the registrar: power to engage and to authorise | those engaged or authorised: liability; (15A(2)) s 68(2) protection extends to them | ss 15(2), 15A | `s 15(2) ...`, `s 15A(1) ...`, `s 15A(2) ...` |
| s 16 | bailiffs: power to enter and, if necessary, break open | the occupier of the building: liability (no immunity against entry) | s 16 | `s 16 ...` (two functions) |
| s 17(1), (2), (2A), (3), (4), Schedule | the State Courts: claim that judicial officers and required officers take the oath | those officers: duty; the Presiding Judges: duty to record and transmit | s 17 | `s 17(1) ...`, `s 17(2) ...`, `s 17(2A) ...`, `s 17(3) ...`, `s 17(4) ...`; Schedule functions; regulative `s 17(1) duty: ...` |
| s 8A(1), s 9(1), s 10(1), s 11(1), s 12(1), s 14, s 18 | none stated (machinery: appointments) | none | those sections | none (inert, reason 2) |
| s 19(1) | the State Courts: status as a court of record | all persons: none | s 19(1) | `s 19(1) ...` |
| s 19(2), (3), (4), (6), s 22, s 23, s 25, s 26, s 28, s 29(1) | the claimant and the defendant: claim to be heard in a court that has jurisdiction; the District Court: power to hear and try | the other party: liability to be sued there; a person outside the grant: no duty to attend | those sections | `s 19(2) ...`, `s 19(3) ...`, `s 19(4) ...`, `s 19(6) ...`, `s 22(1) ...`, `s 23 ...`, `s 25 ...`, `s 26 ...`, `s 28 ...`, `s 29(1) ...`, and the hand-gathered `s 19 ...` |
| s 22(1)(c), (d); s 22(2) | the defendant: claim that the claimant who abandons the excess cannot recover it; the claimant: none beyond the limit; the judgment: a full discharge of all demands | the claimant: disability (cannot recover more than the limit or obtain relief for a subject matter above it) | s 22 | `s 22(1)(c) ...`, `s 22(1)(d) ...`, `s 22(2) ...` |
| s 29(2), s 36(2), s 41(1) and (2), s 54A to s 54F | a party: power to apply for transfer (ss 54A(1), 54B(1), 54C(1), 54D(1), 54E(1), 54F(1)); the court: power to order | the other party: liability to have the proceedings transferred | those sections | the `s 54A(1) ...` to `s 54F(4) ...` functions; `s 29(2) ...`; `s 36(2) ...`; `s 41(1) ...`, `s 41(2) ...` |
| s 31, s 32, s 33(1), s 34, s 52(1B) | the court, the District Judge, the registrar: power (relief, defences, injunction, declarations, medical examination, chambers powers, assessors) | the parties: liability | those sections | `s 31(1) ...`, `s 31(2) ...`, `s 32 ...`, `s 33(1) ...`, `s 34 ...`, `s 52(1B) ...` |
| s 33(2), (3), (4) | a party: privilege to object to an assessor (s 33(4)); the assessor: claim to remuneration (s 33(3)) | the parties (costs) or Parliament's moneys | s 33 | `s 33(2) ...`, `s 33(3) ...`, `s 33(4) ...` |
| s 35 | the defendant: claim that a cause of action is not divided to bring 2 or more actions | the claimant: duty not to divide (a flat negative with no named bearer; no SHANT rule is derived, N2) | s 35 | `s 35 ...` |
| s 36(1), s 39, s 54G | a party: power to ask for costs and a transfer; the General Division: power to order costs on a scale (s 39(4)) | the other party: liability for costs; the claimant: no entitlement to more costs (s 39(1)) | those sections | `s 36(1) ...`, `s 39(1) ...` to `s 39(6) ...`, `s 54G(1) ...`, `s 54G(2)(a) ...`, `s 54G(2)(b) ...` |
| s 42 | each party: claim that the judgment is final and conclusive | the other party: disability to relitigate | s 42 | `s 42 ...` |
| s 43, s 44, s 45 | the judgment creditor: power to enforce; the debtor: privilege to apply to suspend or stay (s 43(2)) | the judgment debtor: liability to enforcement (barred under s 43(3) where instalments are ordered); the party ordered to execute an instrument (s 45(1)) | those sections | `s 43(1) ...` to `s 45(2) ...` |
| s 48, s 49, s 54AA | the party against whom the decision is made: power to appeal (not stated here); the other party: claim that an appeal is barred by an agreement (ss 48(1), 54AA(1)) | the party seeking to appeal: disability unless fraud, illegality or breach of natural justice is proved | those sections | `s 48(1) ...` to `s 49(2) ...`, `s 54AA(1) ...`, `s 54AA(2) ...` |
| s 49A, s 49B | the parties: claim to an oral hearing where oral evidence is given unless all consent (s 49A(2)); the appellant: claim to an opportunity to show cause (s 49B(2)) | the District Court: duty not to hear asynchronously where that would be unfair (s 49A(4)); the District Judge: duty to give the opportunity and consider representations (s 49B(2)) | those sections | `s 49A(1) ...` to `s 49A(5) ...`, `s 49B(1) ...` to `s 49B(3) ...`; regulative `s 49B(2) duty: ...` |
| s 50, s 51 | the State Courts: criminal jurisdiction and power to order the medical examination of an accused | the accused: liability to be examined where the condition is relevant | ss 50, 51 | `s 50(1)(a) ...`, `s 50(1)(b) ...`, `s 50(2) ...`, `s 51(1)(a) ...`, `s 51(1)(b) ...`, `s 51(2) ...` |
| s 52(1), (1A), (1B), (2), s 54 | as for the District Court in civil matters; the Magistrate's Court limit bounds the grant | the defendant: liability to be sued in the Magistrate's Court | s 52 | `s 52(1) ...`, `s 52(1A) ...`, `s 52(1B) ...`, `s 52(2) ...`, the hand-gathered `s 52 ...`, `s 54 ...` |
| s 30, s 47, s 52(3), s 53 to s 56A (repealed) | none stated (machinery: a power to vary a limit by order; a direction that Rules of Court regulate appeals; repealed) | none | those sections | none (inert, reason 2, or repealed) |
| s 57 | a person with business at the Registry: claim that the Registry is open on ordinary days; the registrar: privilege to sit on a Saturday, Sunday or public holiday if directed or if the business is extremely urgent; the Presiding Judge: power to direct office hours | the State Courts: duty to open the Registry; the registrar: no duty to sit on those days | s 57 | `s 57(1) ...`, `s 57(2) ...`, `s 57(3) ...` |
| s 58, s 59, s 61 | the State Courts: power to try civil and criminal proceedings at one sitting (s 58); the Presiding Judge: power to direct the distribution of business (s 59); the Chief Justice: power to authorise vacations of up to 15 days in a calendar year (s 61) | the parties: none stated | those sections | `s 58 ...`, `s 59 ...`, `s 61 ...` |
| s 62 | the Presiding Judge of the State Courts: power to frame, publish, alter and amend the list and to exclude listed persons from the precincts; a listed person: claim to be heard before inclusion (s 62(3)); a listed person who is a party or witness: privilege to remain (s 62(2)); a person included: power to appeal to a Judge in chambers (s 62(4)) | the listed person: liability to be excluded; the State Courts: duty to hang up and publish the list (s 62(6)) | s 62 | `s 62(1) ...` to `s 62(7) ...` |
| s 63 | a State Court: power to impound a document and to direct that it be sent to an officer of the Government | the person who produced the document: liability to have it impounded; no one: may take it out of the court's custody or inspect it without an order signed by a judicial officer (s 63(2)) | s 63 | `s 63(1) ...`, `s 63(2) ...`, `s 63(3) ...` |
| s 64, s 65 | the Chief Justice: power to approve; a judicial officer: privilege with approval (s 64(2)); a party to a proceeding: claim that a judicial officer who is a party or interested does not try it without approval and consent (s 65) | the judicial officer: duty not to take another office of emolument, carry on business, accept fees or advantages, or sit in a proceeding in which the judicial officer is interested | those sections | `s 64(1)(a) ...`, `s 64(1)(b) ...`, `s 64(2)(a) ...`, `s 64(2)(b) ...`, `s 65 ...`; regulative `s 64(1)(b) duty: ...`, `s 65 duty: ...` |
| s 66 | a person selling property under a written law: claim that the court's officer does not purchase or bid | the officer of the State Courts: duty not to purchase or bid | s 66 | `s 66 ...`; regulative `s 66 duty: ...` |
| s 67 | a District Judge nominated by the Presiding Judge: power to inquire summarily, summon attendance, order repayment, damages, costs and fine up to $100; the Chief Justice: power to hear the appeal | the officer charged: liability to inquiry, order, fine and incapacity (s 67(4)) | s 67 | `s 67(1) ...` to `s 67(6) ...` |
| s 68 | a judicial officer, an officer executing process, a court-appointed mediator: immunity from suit on the conditions stated | the person who would sue: disability | s 68 | `s 68(1) ...`, `s 68(2) ...`, `s 68(3) ...`, `s 68(4) ...` |
| s 60, s 69 | none stated (machinery: offices and their staffing; the power to make Rules of Court) | none | those sections | none (inert, reason 2) |
| s 70 | the Court: power to convert a pending petition; the Presiding Judge with the Chief Justice's concurrence: power to direct conversion of a class | the parties to the pending action: liability to conversion and directions | s 70 | `s 70(1) ...` to `s 70(3)(b) ...` |
| the Schedule | the officer who takes the oath: none; the State Courts: claim to the oath in the Schedule's form | the officer: duty to take and subscribe (s 17(1)) | Schedule | `Schedule para 1 ...` to `Schedule para 3 ...`; `Schedule the oath that section 17(1) requires of the holder` |

## What is encoded and what is not

| module | sections |
| --- | --- |
| `sca-nouns.l4` | the types: courts and tribunals, office holders, kinds of day, the `Definition` record, the civil action and other fact records, the acts and bearers of the regulative rules |
| `sca-p1-preliminary.l4` | ss 1 and 2 (the ten definitions as a table, and the rules for the limits and the borrowed terms) |
| `sca-p2-constitution.l4` | ss 3 to 8 (the State Courts, seal, process, sittings, hearings in private, electronic hearings) |
| `sca-p3-appointments.l4` | ss 8A to 18 and the Schedule (appointments, qualifying years, duties of bailiffs, oaths) |
| `sca-p4-civil-district.l4` | ss 19 to 49B (civil jurisdiction of District Courts, powers, costs, enforcement, appeals) |
| `sca-p4-magistrates-criminal.l4` | ss 50 to 52, 54 and 54AA (criminal jurisdiction, Magistrates' Courts, agreement not to appeal) |
| `sca-p4-transfers.l4` | ss 54A to 54G (transfers of civil proceedings) |
| `sca-p5-administration.l4` | ss 57 to 68 (Registry, sittings, vacations, touts, impounding, judicial officers, misconduct, protection from suit) |
| `sca-p6-supplemental.l4` | s 70 (conversion of pending petitions) |
| `sca-seat.l4` | layer 2: 61 questions with `@export` and `@desc` |

Tests are `sca-tests-p1.l4`, `-p2`, `-p3`, `-p4a`, `-p4b`, `-p5` and `sca-cases-seat.l4`: {906} assertions and 11 `#TRACE` runs.

**Not encoded** (all of it listed in the coverage table with a reason):
- the Arrangement of Sections, the long title, the title page, headings and amendment marks (inert, reason 1: not operative);
- the Legislative History and Abbreviations at the end of the file, which say of themselves that they are "not part of the Act" (inert, reason 1);
- the machinery of the Act (inert, reason 2): the short title (s 1), appointments and their staffing (ss 8A(1), 9(1), 10(1), 11(1), 12(1), 14, 18), the offices attached to the State Courts (s 60), the powers to vary the limits by order (ss 30 and 52(3)), the direction that Rules of Court regulate appeals (s 47), and the power to make Rules of Court (s 69);
- provisions shown as repealed or deleted in this text (17 rows);
- everything the Act sends elsewhere: Rules of Court, the Criminal Procedure Code 2010, the Supreme Court of Judicature Act 1969, the Coroners Act 2010, the Broadcasting Act 1994, the Newspaper and Printing Presses Act 1974, the Limited Liability Partnerships Act 2005, the Distress Act 1934, the Civil Law Act 1909. These are inputs (a yes/no or a number the person states) or `NOTHING`.

## Coverage table

The table is built by script from the text (`coverage.py`, run as `python3 -I coverage.py <text> coverage-dispositions.txt --md`; `--check` fails if any unit is undisposed or any disposition matches no unit, and it printed `COVERAGE OK`).
Each row is one section, subsection, paragraph, sub-paragraph, defined term, Explanation, heading block, Schedule paragraph, or the front matter and the Legislative History, with its line range in `SCA1970.txt` and exactly one disposition: `encoded`, `inert` (with the reason number: 1 not operative, 2 machinery, 3 shown repealed or blank) or `repealed`.
Every non-blank line of the file (2,398 of them) falls in some row or is page furniture (139 repeated page headers and footers); none is unassigned.
Counts: 480 rows; encoded 344; inert 119 (reason 1: 79; reason 2: 40); repealed 17; no `fork`, `out-of-scope` or `deferred` rows.

| unit | lines | disposition | where / why |
| --- | --- | --- | --- |
| Title page and revised-edition notice | 1-16 | inert | 1: not operative (title page and revised-edition notice) |
| Arrangement of Sections (table of contents; converter output misaligns its headings) | 18-181 | inert | 1: not operative (table of contents; headings only) |
| Long title | 183-184 | inert | 1: not operative (long title) |
| Amendment mark [5/2014] after the long title | 186-186 | inert | 1: not operative (amendment history mark) |
| Date of commencement [1 January 1971] | 188-188 | inert | 1: not operative (date of enactment/commencement mark) |
| heading before s 1 | 190-192 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 1 | 193-195 | inert | 2: machinery (short title) |
| heading before s 2 | 197-197 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 2 | 199-199 | encoded | sca-p1-preliminary: `s 2 the definitions in this section apply to this provision` ("unless the context otherwise requires"); `s 2 the ten definitions` |
| s 2 term action | 201-202 | encoded | sca-p1-preliminary: `s 2 definition: action`, `s 2 "action" the proceeding is an action` |
| s 2 term commissioner for oaths | 204-206 | encoded | sca-p1-preliminary: `s 2 definition: commissioner for oaths`, `s 2 "commissioner for oaths" the person is a commissioner for oaths` |
| s 2 term Coroner | 208-209 | encoded | sca-p1-preliminary: `s 2 definition: Coroner`, `s 2 "Coroner" the person is a Coroner` (borrowed term, asked as a fact) |
| s 2 term District Court limit | 214-215 | encoded | sca-p1-preliminary: `s 2 definition: District Court limit`, `s 2 "District Court limit" the amount in dollars` (F-LIMIT) |
| s 2 term judicial officer | 217-217 | encoded | sca-p1-preliminary: `s 2 definition: judicial officer`, `s 2 "judicial officer" the holder is a judicial officer` |
| s 2 term Magistrate’s Court limit | 219-220 | encoded | sca-p1-preliminary: `s 2 definition: Magistrate's Court limit`, `s 2 "Magistrate's Court limit" the amount in dollars` (F-LIMIT) |
| s 2 term prescribed | 222-222 | encoded | sca-p1-preliminary: `s 2 definition: prescribed`, `s 2 "prescribed" the matter is prescribed` |
| s 2 term registrar | 224-225 | encoded | sca-p1-preliminary: `s 2 definition: registrar`, `s 2 "registrar" the holder is the registrar` |
| s 2 term Rules of Court | 227-228 | encoded | sca-p1-preliminary: `s 2 definition: Rules of Court`, `s 2 "Rules of Court" the instrument is within the Rules of Court` |
| s 2 term seal | 230-232 | encoded | sca-p1-preliminary: `s 2 definition: seal`, `s 2 "seal" the thing is within the word seal` |
| heading before s 3(1) | 234-238 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 3(1) | 240-241 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1)(a) | 243-243 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1)(b) | 245-245 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1)(c) | 247-247 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1)(d) | 249-249 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1)(e) | 251-253 | encoded | sca-p2-constitution: `s 3(1) the court is one of the State Courts` (paragraphs (a) to (e): one branch each) |
| s 3(1A) | 255-258 | encoded | sca-p2-constitution: `s 3(1A) the court has the jurisdiction conferred by this Act and any other written law` |
| s 3(2) | 260-261 | encoded | sca-p2-constitution: `s 3(2) the court has the jurisdiction conferred by the Small Claims Tribunals Act 1984 and any other written law` |
| s 3(3) | 263-263 | repealed | the text shows "[Deleted by Act 33 of 2018]" |
| s 3(4) | 268-271 | encoded | sca-p2-constitution: `s 3(4) the court has the jurisdiction conferred by the Coroners Act 2010 and any other written law` |
| s 3(5) | 273-277 | encoded | sca-p2-constitution: `s 3(5) the court has the jurisdiction conferred by the Employment Claims Act 2016 and any other written law` |
| heading before s 4 | 279-279 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 4 | 281-288 | encoded | sca-p2-constitution: `s 4 the State Court is constituted by the President under an appropriate name` |
| heading before s 5 | 290-290 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 5 | 292-296 | encoded | sca-p2-constitution: `s 5 the State Courts have and use a seal of the nature the Chief Justice has prescribed` (QB) |
| heading before s 6 | 298-298 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 6 | 300-305 | encoded | sca-p2-constitution: `s 6 the process of the State Courts is signed by a judicial officer and bears the seal of the court` (QB); regulative `s 6 duty: ...` |
| heading before s 6A(1) | 307-307 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 6A(1) | 309-313 | encoded | sca-p2-constitution: `s 6A(1) the State Court is to sit on the day` (F-VACATION) |
| s 6A(2) | 315-317 | encoded | sca-p2-constitution: `s 6A(2) the judicial officer may lawfully sit on the day` |
| s 6A(2)(a) | 322-324 | encoded | sca-p2-constitution: `s 6A(2) the judicial officer may lawfully sit on the day` |
| s 6A(2)(b) | 326-329 | encoded | sca-p2-constitution: `s 6A(2) the judicial officer may lawfully sit on the day` |
| s 6A(3) | 331-336 | encoded | sca-p2-constitution: `s 6A(3) the State Court sits at the time and place the Chief Justice has appointed` (QB) |
| heading before s 7(1) | 338-338 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 7(1) | 340-343 | encoded | sca-p2-constitution: `s 7(1) the place is deemed an open and public court to which the public may have access` |
| s 7(2) | 345-353 | encoded | sca-p2-constitution: `s 7(2) the State Court has power to hear the matter or part of it in private` |
| s 7(2AA) | 355-359 | encoded | sca-p2-constitution: `s 7(2AA) the application is to be heard in private` |
| s 7(2AB) | 361-363 | encoded | sca-p2-constitution: `s 7(2AB) the State Court has power to hear the subsection (2AA) application otherwise than in private` |
| s 7(2AB)(a) | 365-367 | encoded | sca-p2-constitution: `s 7(2AB) the State Court has power to hear the subsection (2AA) application otherwise than in private` |
| s 7(2AB)(b) | 369-373 | encoded | sca-p2-constitution: `s 7(2AB) the State Court has power to hear the subsection (2AA) application otherwise than in private` |
| s 7(2A) | 378-382 | encoded | sca-p2-constitution: `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` |
| s 7(2A)(a) | 384-386 | encoded | sca-p2-constitution: `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` |
| s 7(2A)(b) | 388-392 | encoded | sca-p2-constitution: `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` |
| s 7(2A)(c) | 394-402 | encoded | sca-p2-constitution: `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` |
| s 7(3) | 404-404 | encoded | sca-p2-constitution: `s 7(3) the State Court may at any time order that no person is to do the act` |
| s 7(3)(a) | 406-412 | encoded | sca-p2-constitution: `s 7(3) the State Court may at any time order that no person is to do the act` |
| s 7(3)(b) | 414-419 | encoded | sca-p2-constitution: `s 7(3) the State Court may at any time order that no person is to do the act` |
| s 7(3)(c) | 421-426 | encoded | sca-p2-constitution: `s 7(3) the State Court may at any time order that no person is to do the act` |
| s 7(4) | 428-437 | encoded | sca-p2-constitution: `s 7(4) the person is guilty of an offence`, `s 7(4) the punishment is within the greatest the offence allows`, regulative `s 7(4) duty: ...` |
| s 7(5) | 439-442 | encoded | sca-p2-constitution: `s 7(5) the individual may be present in the courtroom while the matter is heard in private` |
| s 7(5)(a) | 444-445 | encoded | sca-p2-constitution: `s 7(5) the individual may be present in the courtroom while the matter is heard in private` |
| s 7(5)(b) | 447-448 | encoded | sca-p2-constitution: `s 7(5) the individual may be present in the courtroom while the matter is heard in private` |
| s 7(5)(c) | 450-455 | encoded | sca-p2-constitution: `s 7(5) the individual may be present in the courtroom while the matter is heard in private` |
| s 7(6) | 457-462 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(6)(a) | 464-466 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(6)(b) | 468-470 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(6)(c) | 472-474 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(6)(d) | 476-479 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(6)(e) | 484-490 | encoded | sca-p2-constitution: `s 7(6) the matter is one the State Court may consider in deciding whether to hear the matter in private` |
| s 7(7) | 492-492 | encoded | sca-p2-constitution: the two definitions of s 7(7) (chapeau "In this section —") |
| s 7(7) term broadcasting service | 494-495 | encoded | sca-p2-constitution: `s 7(7) "broadcasting service" the service is a broadcasting service` (borrowed term) |
| s 7(7) term newspaper | 497-500 | encoded | sca-p2-constitution: `s 7(7) "newspaper" the publication is a newspaper` (borrowed term) |
| heading before s 8(1) | 502-503 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 8(1) | 505-512 | encoded | sca-p2-constitution: `s 8(1) the State Court may conduct the hearing through the means` (QE) |
| s 8(2) | 514-521 | encoded | sca-p2-constitution: `s 8(2) subsection (1) affects the operation of the provision` |
| s 8(3) | 523-525 | encoded | sca-p2-constitution: `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` (QA), twin `s 8(3) the bar on a live audio link only applies to the part of the hearing`, regulative `s 8(3) duty: ...` |
| s 8(3)(a) | 527-528 | encoded | sca-p2-constitution: `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` (QA), twin `s 8(3) the bar on a live audio link only applies to the part of the hearing`, regulative `s 8(3) duty: ...` |
| s 8(3)(b) | 530-532 | encoded | sca-p2-constitution: `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` (QA), twin `s 8(3) the bar on a live audio link only applies to the part of the hearing`, regulative `s 8(3) duty: ...` |
| s 8(3)(c) | 537-540 | encoded | sca-p2-constitution: `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` (QA), twin `s 8(3) the bar on a live audio link only applies to the part of the hearing`, regulative `s 8(3) duty: ...` |
| s 8(4) | 542-550 | encoded | sca-p2-constitution: `s 8(4) the court is considered to have conducted the part of the hearing through a live audio link only` |
| s 8(5) | 552-557 | encoded | sca-p2-constitution: `s 8(5) the State Court may conduct the hearing in the manner provided under subsection (1)` |
| s 8(6) | 559-565 | encoded | sca-p2-constitution: `s 8(6) the court is deemed to be sitting at a place appointed under section 6A(3)` |
| heading before s 8A(1) | 567-571 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 8A(1) | 573-579 | inert | 2: machinery (appointment of the Presiding Judge of the State Courts: an office and its staffing) |
| s 8A(2) | 581-586 | encoded | sca-p3-appointments: `s 8A(2) the holder may sit in any State Court and act as a judge of it with all the jurisdiction, power and privileges of such a judge` |
| s 8A(3) | 591-597 | encoded | sca-p3-appointments: `s 8A(3) the person may continue to sit in the General Division of the High Court, the Appellate Division of the High Court or the Court of Appeal` |
| s 8A(4) | 599-606 | encoded | sca-p3-appointments: `s 8A(4) the person continues to sit as a judge of the State Court to give judgment or otherwise in the case` |
| heading before s 9(1) | 608-608 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 9(1) | 610-614 | inert | 2: machinery (appointment of District Judges: an office and its staffing) |
| s 9(2) | 616-616 | repealed | the text shows "[Deleted by Act 5 of 2014]" |
| s 9(3) | 618-622 | encoded | sca-p3-appointments: `s 9(3) the person may be appointed to be or to act as a District Judge` (QA) |
| s 9(3A) | 624-625 | encoded | sca-p3-appointments: `s 9(3A) the person may be appointed to be or to act as a District Judge despite subsection (3)` |
| s 9(3A)(a) | 627-629 | encoded | sca-p3-appointments: `s 9(3A) the person may be appointed to be or to act as a District Judge despite subsection (3)` |
| s 9(3A)(b) | 631-635 | encoded | sca-p3-appointments: `s 9(3A) the person may be appointed to be or to act as a District Judge despite subsection (3)` |
| s 9(4) | 637-645 | encoded | sca-p3-appointments: `s 9(4) the person is to sit as a District Judge for the purpose of giving judgment or otherwise in the case` |
| s 9(5) | 647-648 | encoded | sca-p3-appointments: `s 9(5) the person is ex officio a Magistrate` |
| heading before s 10(1) | 650-650 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 10(1) | 652-655 | inert | 2: machinery (appointment of Magistrates: an office and its staffing) |
| s 10(2) | 657-661 | encoded | sca-p3-appointments: `s 10(2) the person may be appointed to be or to act as a Magistrate` (QA) |
| s 10(3) | 663-664 | encoded | sca-p3-appointments: `s 10(3) the person may be appointed to be or to act as a Magistrate despite subsection (2)` |
| s 10(3)(a) | 666-668 | encoded | sca-p3-appointments: `s 10(3) the person may be appointed to be or to act as a Magistrate despite subsection (2)` |
| s 10(3)(b) | 670-674 | encoded | sca-p3-appointments: `s 10(3) the person may be appointed to be or to act as a Magistrate despite subsection (2)` |
| heading before s 11(1) | 676-676 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 11(1) | 678-679 | inert | 2: machinery (appointment of Justices of the Peace: an office and its staffing) |
| s 11(2) | 681-683 | encoded | sca-p3-appointments: `s 11(2) Justices of the Peace have and may exercise the power or perform the duty of a Magistrate` |
| heading before s 12(1) | 685-686 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 12(1) | 688-692 | inert | 2: machinery (appointment of the registrar and deputy registrars: offices and their staffing) |
| s 12(2) | 697-701 | encoded | sca-p3-appointments: `s 12(2) the person may be appointed to be or to act as registrar` (QA) |
| s 12(3) | 703-704 | encoded | sca-p3-appointments: `s 12(3) the holder is ex officio a commissioner for oaths` |
| heading before s 13 | 706-706 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 13 | 708-709 | encoded | sca-p3-appointments: `s 13 the holder may exercise the powers and duties conferred and imposed on the registrar` |
| heading before s 14 | 711-711 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 14 | 713-719 | inert | 2: machinery (officers attached to the State Courts: offices and their staffing) |
| heading before s 15(1) | 721-721 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 15(1) | 723-723 | encoded | sca-p3-appointments: `s 15(1) the holder is to do the duty`, regulative `s 15(1)(a) duty: ...`, `s 15(1)(b) duty: ...`, `s 15(1)(c) duty: ...` |
| s 15(1)(a) | 725-727 | encoded | sca-p3-appointments: `s 15(1) the holder is to do the duty`, regulative `s 15(1)(a) duty: ...`, `s 15(1)(b) duty: ...`, `s 15(1)(c) duty: ...` |
| s 15(1)(b) | 729-731 | encoded | sca-p3-appointments: `s 15(1) the holder is to do the duty`, regulative `s 15(1)(a) duty: ...`, `s 15(1)(b) duty: ...`, `s 15(1)(c) duty: ...` |
| s 15(1)(c) | 733-738 | encoded | sca-p3-appointments: `s 15(1) the holder is to do the duty`, regulative `s 15(1)(a) duty: ...`, `s 15(1)(b) duty: ...`, `s 15(1)(c) duty: ...` |
| s 15(2) | 740-752 | encoded | sca-p3-appointments: `s 15(2) the registrar may engage the person` |
| heading before s 15A(1) | 754-754 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 15A(1) | 756-763 | encoded | sca-p3-appointments: `s 15A(1) the registrar may authorise the person to exercise the powers and perform the duties of a bailiff` |
| s 15A(2) | 765-768 | encoded | sca-p3-appointments: `s 15A(2) section 68(2) applies to the person as it applies to an officer of a State Court` |
| heading before s 16 | 770-770 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 16 | 772-779 | encoded | sca-p3-appointments: `s 16 the bailiff may effect an entry into a building`, `s 16 the bailiff may break open an outer or inner door or window of the building or any receptacle in it` |
| heading before s 17(1) | 781-781 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 17(1) | 783-788 | encoded | sca-p3-appointments: `s 17(1) the officer is to take and subscribe the oath before exercising the functions of the office`, `s 17(1) the oath was taken and subscribed before the functions of the office were exercised` (QB), regulative `s 17(1) duty: ...` |
| s 17(2) | 790-795 | encoded | sca-p3-appointments: `s 17(2) the oath may be taken and subscribed before the person` |
| s 17(2A) | 800-808 | encoded | sca-p3-appointments: `s 17(2A) the person may take and subscribe the oath by appearing through a live video link or live television link` |
| s 17(2A)(a) | 810-812 | encoded | sca-p3-appointments: `s 17(2A) the person may take and subscribe the oath by appearing through a live video link or live television link` |
| s 17(2A)(b) | 814-815 | encoded | sca-p3-appointments: `s 17(2A) the person may take and subscribe the oath by appearing through a live video link or live television link` |
| s 17(2A)(c) | 817-819 | encoded | sca-p3-appointments: `s 17(2A) the person may take and subscribe the oath by appearing through a live video link or live television link` |
| s 17(3) | 821-822 | encoded | sca-p3-appointments: `s 17(3) the Presiding Judge of the State Courts has entered the oath in the record and transmitted a certified copy` (QB) |
| s 17(3)(a) | 824-825 | encoded | sca-p3-appointments: `s 17(3) the Presiding Judge of the State Courts has entered the oath in the record and transmitted a certified copy` (QB) |
| s 17(3)(b) | 827-830 | encoded | sca-p3-appointments: `s 17(3) the Presiding Judge of the State Courts has entered the oath in the record and transmitted a certified copy` (QB) |
| s 17(4) | 832-833 | encoded | sca-p3-appointments: `s 17(4) the Presiding Judge of the Family Justice Courts has entered the oath in the record and transmitted the certified copies` (QB) |
| s 17(4)(a) | 835-836 | encoded | sca-p3-appointments: `s 17(4) the Presiding Judge of the Family Justice Courts has entered the oath in the record and transmitted the certified copies` (QB) |
| s 17(4)(b) | 838-839 | encoded | sca-p3-appointments: `s 17(4) the Presiding Judge of the Family Justice Courts has entered the oath in the record and transmitted the certified copies` (QB) |
| s 17(4)(c) | 841-844 | encoded | sca-p3-appointments: `s 17(4) the Presiding Judge of the Family Justice Courts has entered the oath in the record and transmitted the certified copies` (QB) |
| heading before s 18 | 849-849 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 18 | 851-852 | inert | 2: machinery (appointments and revocations to be gazetted: an office and its staffing) |
| heading before s 19(1) | 854-860 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 19(1) | 862-863 | encoded | sca-p4-civil-district: `s 19(1) the court is a court of record` |
| s 19(2) | 865-867 | encoded | sca-p4-civil-district: `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 19(2)(a) | 869-870 | encoded | sca-p4-civil-district: `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 19(2)(a)(i) | 872-873 | encoded | sca-p4-civil-district: `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 19(2)(a)(ii) | 875-878 | encoded | sca-p4-civil-district: `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 19(2)(b) | 880-883 | encoded | sca-p4-civil-district: `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 19(3) | 885-887 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(a) | 889-889 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(b) | 891-894 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(b)(i) | 896-896 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(b)(ii) | 901-901 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(b)(iii) | 903-903 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(b)(iv) | 905-905 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(c) | 907-912 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(ca) | 914-916 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(3)(d) | 918-920 | encoded | sca-p4-civil-district: `s 19(3) the action falls within a class that subsection (3) excludes from a District Court's jurisdiction`, `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` |
| s 19(4) | 922-924 | encoded | sca-p4-civil-district: `s 19(4) the amount claimed or the value of the subject matter of the remedy or relief exceeds the District Court limit`, `s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value` |
| s 19(4)(a) | 926-927 | encoded | sca-p4-civil-district: `s 19(4) the amount claimed or the value of the subject matter of the remedy or relief exceeds the District Court limit`, `s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value` |
| s 19(4)(b) | 929-933 | encoded | sca-p4-civil-district: `s 19(4) the amount claimed or the value of the subject matter of the remedy or relief exceeds the District Court limit`, `s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value` |
| s 19(5) | 935-935 | repealed | the text shows "(5) [Deleted by Act 27 of 2014]" |
| s 19(6) | 937-938 | encoded | sca-p4-civil-district: `s 19(6) a District Court has the jurisdiction vested in it by another written law` |
| s 20 | 940-940 | repealed | the text shows "20. [Repealed by Act 31 of 2010]" |
| s 21 | 942-942 | repealed | the text shows "21. [Repealed by Act 31 of 2010]" |
| heading before s 22(1) | 944-945 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 22(1) | 947-947 | encoded | sca-p4-civil-district: `s 22(1) the claimant may abandon the excess amount or the remedy or relief`, `s 22(1) this section gives a District Court jurisdiction under section 19(2) to hear and try the action`, `s 22(1)(c) the claimant may recover the amount in the action`, `s 22(1)(d) the claimant may obtain the remedy or relief in the action` |
| s 22(1)(a) | 949-952 | encoded | sca-p4-civil-district: `s 22(1) the claimant may abandon the excess amount or the remedy or relief`, `s 22(1) this section gives a District Court jurisdiction under section 19(2) to hear and try the action`, `s 22(1)(c) the claimant may recover the amount in the action`, `s 22(1)(d) the claimant may obtain the remedy or relief in the action` |
| s 22(1)(b) | 957-965 | encoded | sca-p4-civil-district: `s 22(1) the claimant may abandon the excess amount or the remedy or relief`, `s 22(1) this section gives a District Court jurisdiction under section 19(2) to hear and try the action`, `s 22(1)(c) the claimant may recover the amount in the action`, `s 22(1)(d) the claimant may obtain the remedy or relief in the action` |
| s 22(1)(c) | 967-967 | encoded | sca-p4-civil-district: `s 22(1) the claimant may abandon the excess amount or the remedy or relief`, `s 22(1) this section gives a District Court jurisdiction under section 19(2) to hear and try the action`, `s 22(1)(c) the claimant may recover the amount in the action`, `s 22(1)(d) the claimant may obtain the remedy or relief in the action` |
| s 22(1)(d) | 969-974 | encoded | sca-p4-civil-district: `s 22(1) the claimant may abandon the excess amount or the remedy or relief`, `s 22(1) this section gives a District Court jurisdiction under section 19(2) to hear and try the action`, `s 22(1)(c) the claimant may recover the amount in the action`, `s 22(1)(d) the claimant may obtain the remedy or relief in the action` |
| s 22(2) | 976-978 | encoded | sca-p4-civil-district: `s 22(2) the judgment of the court in the action is a full discharge of all demands in respect of the cause of action` |
| heading before s 23 | 980-980 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 23 | 982-984 | encoded | sca-p4-civil-district: `s 23 this section gives a District Court jurisdiction under section 19(2) to hear and try the action even though its amount or value exceeds the District Court limit` |
| s 23(a) | 986-987 | encoded | sca-p4-civil-district: `s 23 this section gives a District Court jurisdiction under section 19(2) to hear and try the action even though its amount or value exceeds the District Court limit` |
| s 23(b) | 989-993 | encoded | sca-p4-civil-district: `s 23 this section gives a District Court jurisdiction under section 19(2) to hear and try the action even though its amount or value exceeds the District Court limit` |
| s 24 | 995-995 | repealed | the text shows "24. [Repealed by Act 26 of 2005]" |
| heading before s 25 | 997-997 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 25 | 999-1002 | encoded | sca-p4-civil-district: `s 25 this section gives a District Court jurisdiction to hear and try the action for the recovery of immovable property` and two helpers |
| s 25(a) | 1007-1009 | encoded | sca-p4-civil-district: `s 25 this section gives a District Court jurisdiction to hear and try the action for the recovery of immovable property` and two helpers |
| s 25(b) | 1011-1014 | encoded | sca-p4-civil-district: `s 25 this section gives a District Court jurisdiction to hear and try the action for the recovery of immovable property` and two helpers |
| s 25(c) | 1016-1020 | encoded | sca-p4-civil-district: `s 25 this section gives a District Court jurisdiction to hear and try the action for the recovery of immovable property` and two helpers |
| heading before s 26 | 1022-1022 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 26 | 1024-1025 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 26(a) | 1027-1027 | repealed | the text shows "(a) [Deleted by Act 27 of 2014]" |
| s 26(b) | 1029-1032 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 26(c) | 1034-1037 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 26(d) | 1039-1044 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 26(e) | 1046-1046 | repealed | the text shows "(e) [Deleted by Act 27 of 2014]" |
| s 26(f) | 1048-1058 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 26(g) | 1060-1065 | encoded | sca-p4-civil-district: `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` (paragraphs (b), (c), (d), (f), (g) by kind; the LLP carve-out of (f) is QE) |
| s 27 | 1067-1067 | repealed | the text shows "27. [Repealed by Act 27 of 2014]" |
| heading before s 28 | 1069-1069 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 28 | 1071-1073 | encoded | sca-p4-civil-district: `s 28 this section gives a District Court jurisdiction under the Distress Act 1934` |
| heading before s 29(1) | 1075-1075 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 29(1) | 1077-1079 | encoded | sca-p4-civil-district: `s 29(1) this section gives a District Court jurisdiction to grant relief by way of interpleader` (fork F-29: paragraphs (a) and (b) are joined by "and") |
| s 29(1)(a) | 1081-1087 | encoded | sca-p4-civil-district: `s 29(1) this section gives a District Court jurisdiction to grant relief by way of interpleader` (fork F-29: paragraphs (a) and (b) are joined by "and") |
| s 29(1)(b) | 1089-1096 | encoded | sca-p4-civil-district: `s 29(1) this section gives a District Court jurisdiction to grant relief by way of interpleader` (fork F-29: paragraphs (a) and (b) are joined by "and") |
| s 29(2) | 1098-1110 | encoded | sca-p4-civil-district: `s 29(2) the General Division of the High Court may order that the proceedings be transferred to a District Court` |
| heading before s 30 | 1112-1112 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 30 | 1114-1116 | inert | 2: machinery (a power of the President to vary the District Court limit by order; the effect of an order is carried by the limit parameter of `s 2 "District Court limit" the amount in dollars`) |
| heading before s 31(1) | 1118-1119 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 31(1) | 1121-1122 | encoded | sca-p4-civil-district: `s 31(1) the District Court has the power in the proceedings before it`, `s 31 the power is conferred if the action is within the jurisdiction` |
| s 31(1)(a) | 1124-1125 | encoded | sca-p4-civil-district: `s 31(1) the District Court has the power in the proceedings before it`, `s 31 the power is conferred if the action is within the jurisdiction` |
| s 31(1)(b) | 1127-1133 | encoded | sca-p4-civil-district: `s 31(1) the District Court has the power in the proceedings before it`, `s 31 the power is conferred if the action is within the jurisdiction` |
| s 31(2) | 1135-1136 | encoded | sca-p4-civil-district: `s 31(2) the District Court has the power as regards the action` |
| s 31(2)(a) | 1138-1139 | encoded | sca-p4-civil-district: `s 31(2) the District Court has the power as regards the action` |
| s 31(2)(b) | 1141-1142 | encoded | sca-p4-civil-district: `s 31(2) the District Court has the power as regards the action` |
| s 31(2)(c) | 1144-1149 | encoded | sca-p4-civil-district: `s 31(2) the District Court has the power as regards the action` |
| heading before s 32 | 1154-1154 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 32 | 1156-1162 | encoded | sca-p4-civil-district: `s 32 the District Judge has power to make the order or exercise the authority or jurisdiction` |
| heading before s 33(1) | 1164-1164 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 33(1) | 1166-1171 | encoded | sca-p4-civil-district: `s 33(1) the District Judge may summon the persons to assist and act as assessors` |
| s 33(2) | 1173-1176 | encoded | sca-p4-civil-district: `s 33(2) the remuneration of the assessors is costs in the proceedings` |
| s 33(3) | 1178-1181 | encoded | sca-p4-civil-district: `s 33(3) the remuneration of the assessor is payable out of moneys provided by Parliament` |
| s 33(4) | 1183-1185 | encoded | sca-p4-civil-district: `s 33(4) a party may object to the person, personally or in respect of qualification` |
| heading before s 34 | 1187-1187 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 34 | 1189-1192 | encoded | sca-p4-civil-district: `s 34 the registrar may exercise the jurisdiction and powers conferred on a District Court relating to civil proceedings` |
| heading before s 35 | 1194-1194 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 35 | 1196-1197 | encoded | sca-p4-civil-district: `s 35 a cause of action may be divided` |
| heading before s 36(1) | 1202-1202 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 36(1) | 1204-1211 | encoded | sca-p4-civil-district: `s 36(1) the General Division of the High Court has power to issue a request or an order to examine witnesses abroad for the purpose of civil proceedings in a District Court` |
| s 36(2) | 1213-1217 | encoded | sca-p4-civil-district: `s 36(2) the General Division of the High Court may order the proceedings to be transferred to it` |
| s 37 | 1219-1219 | repealed | the text shows "37. [Repealed by Act 26 of 2005]" |
| s 38 | 1221-1221 | repealed | the text shows "38. [Repealed by Act 26 of 2005]" |
| heading before s 39(1) | 1223-1225 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 39(1) | 1227-1229 | encoded | sca-p4-civil-district: `s 39(1) the claimant is entitled to more costs than an action brought in a State Court with that limit would carry` |
| s 39(1)(a) | 1231-1234 | encoded | sca-p4-civil-district: `s 39(1) the claimant is entitled to more costs than an action brought in a State Court with that limit would carry` |
| s 39(1)(b) | 1236-1243 | encoded | sca-p4-civil-district: `s 39(1) the claimant is entitled to more costs than an action brought in a State Court with that limit would carry` |
| s 39(2) | 1245-1258 | encoded | sca-p4-civil-district: `s 39(2) the claimant is treated as recovering the full amount recoverable without regard to the deduction`, `s 39(2) the sum the claimant is treated as recovering in dollars` |
| s 39(3) | 1260-1267 | encoded | sca-p4-civil-district: `s 39(3) the Registrar of the Supreme Court has the same power of allowing items of costs as a District Judge or Magistrate would have had` |
| s 39(4) | 1269-1270 | encoded | sca-p4-civil-district: `s 39(4) the General Division of the High Court may make an order allowing the costs on the General Division scale or the State Courts scale as it directs` |
| s 39(4)(a) | 1272-1273 | encoded | sca-p4-civil-district: `s 39(4) the General Division of the High Court may make an order allowing the costs on the General Division scale or the State Courts scale as it directs` |
| s 39(4)(b) | 1275-1282 | encoded | sca-p4-civil-district: `s 39(4) the General Division of the High Court may make an order allowing the costs on the General Division scale or the State Courts scale as it directs` |
| s 39(5) | 1284-1285 | encoded | sca-p4-civil-district: `s 39(5) section 39 applies to the proceedings` |
| s 39(6) | 1287-1295 | encoded | sca-p4-civil-district: `s 39(6) section 39 affects the question as to costs` |
| s 40 | 1297-1297 | repealed | the text shows "40. [Repealed by Act 26 of 2005]" |
| heading before s 41(1) | 1299-1299 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 41(1) | 1301-1313 | encoded | sca-p4-civil-district: `s 41(1) the Chief Justice may by order direct a class of proceedings to be heard and determined by the General Division of the High Court` |
| s 41(2) | 1315-1320 | encoded | sca-p4-civil-district: `s 41(2) the order may make incidental provision for the transfer of the proceedings, including matters relating to procedure and costs` |
| heading before s 42 | 1322-1322 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 42 | 1324-1326 | encoded | sca-p4-civil-district: `s 42 the judgment or order is final and conclusive between the parties` |
| heading before s 43(1) | 1328-1328 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 43(1) | 1330-1334 | encoded | sca-p4-civil-district: `s 43(1) the District Court may order the money to be paid in one sum or by instalments` |
| s 43(1)(a) | 1336-1337 | encoded | sca-p4-civil-district: `s 43(1) the District Court may order the money to be paid in one sum or by instalments` |
| s 43(1)(b) | 1339-1339 | encoded | sca-p4-civil-district: `s 43(1) the District Court may order the money to be paid in one sum or by instalments` |
| s 43(2) | 1341-1347 | encoded | sca-p4-civil-district: `s 43(2) the District Court may suspend or stay the judgment or order` |
| s 43(2)(a) | 1349-1349 | encoded | sca-p4-civil-district: `s 43(2) the District Court may suspend or stay the judgment or order` |
| s 43(2)(b) | 1351-1352 | encoded | sca-p4-civil-district: `s 43(2) the District Court may suspend or stay the judgment or order` |
| s 43(3) | 1357-1361 | encoded | sca-p4-civil-district: `s 43(3) enforcement may issue`, `s 43(3) the bar on enforcement applies`, `s 43(3) the payment is to be made into court` |
| heading before s 44 | 1363-1363 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 44 | 1365-1366 | encoded | sca-p4-civil-district: `s 44 the judgment or order of a District Court may be enforced in the manner` |
| heading before s 45(1) | 1368-1368 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 45(1) | 1370-1375 | encoded | sca-p4-civil-district: `s 45(1) the interested party may prepare the instrument and tender it to a District Court for execution`, `s 45(1) the signature has the same effect as the execution, signing or indorsement by the party ordered to execute` |
| s 45(1)(a) | 1377-1378 | encoded | sca-p4-civil-district: `s 45(1) the interested party may prepare the instrument and tender it to a District Court for execution`, `s 45(1) the signature has the same effect as the execution, signing or indorsement by the party ordered to execute` |
| s 45(1)(b) | 1380-1385 | encoded | sca-p4-civil-district: `s 45(1) the interested party may prepare the instrument and tender it to a District Court for execution`, `s 45(1) the signature has the same effect as the execution, signing or indorsement by the party ordered to execute` |
| s 45(2) | 1387-1389 | encoded | sca-p4-civil-district: `s 45(2) section 45 abridges the powers of a District Court` |
| s 46 | 1391-1391 | repealed | the text shows "46. [Repealed by Act 15 of 1993]" |
| heading before s 47 | 1393-1393 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 47 | 1395-1401 | inert | 2: machinery (directs that Rules of Court regulate the procedure on appeals; a rule-making provision, and the Rules are not among the sources) |
| heading before s 48(1) | 1406-1406 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 48(1) | 1408-1411 | encoded | sca-p4-civil-district: `s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction`, `s 48(1) the bar on an appeal applies to the decision` |
| s 48(1)(a) | 1413-1413 | encoded | sca-p4-civil-district: `s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction`, `s 48(1) the bar on an appeal applies to the decision` |
| s 48(1)(b) | 1415-1416 | encoded | sca-p4-civil-district: `s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction`, `s 48(1) the bar on an appeal applies to the decision` |
| s 48(2) | 1418-1418 | encoded | sca-p4-civil-district: `s 48(2) an agreement mentioned in subsection (1) may be made at that time`, `s 48(2) the references in subsection (1) to a decision are references to that part of the decision` |
| s 48(2)(a) | 1420-1421 | encoded | sca-p4-civil-district: `s 48(2) an agreement mentioned in subsection (1) may be made at that time`, `s 48(2) the references in subsection (1) to a decision are references to that part of the decision` |
| s 48(2)(b) | 1423-1427 | encoded | sca-p4-civil-district: `s 48(2) an agreement mentioned in subsection (1) may be made at that time`, `s 48(2) the references in subsection (1) to a decision are references to that part of the decision` |
| heading before s 49(1) | 1429-1429 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 49(1) | 1431-1438 | encoded | sca-p4-civil-district: `s 49(1) the appeal operates as a stay of execution or enforcement or of proceedings under the judgment or order appealed from` |
| s 49(2) | 1440-1445 | encoded | sca-p4-civil-district: `s 49(2) an intermediate act or proceeding is invalidated` |
| heading before s 49A(1) | 1447-1447 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 49A(1) | 1449-1451 | encoded | sca-p4-civil-district: `s 49A(1) a District Court may decide the matter in its civil jurisdiction without hearing oral arguments` |
| s 49A(2) | 1453-1455 | encoded | sca-p4-civil-district: `s 49A(2) the part of the proceeding where oral evidence is given may be conducted without an oral hearing`, `s 49A(2) the bar on conducting the part of the proceeding without an oral hearing applies` |
| s 49A(3) | 1460-1464 | encoded | sca-p4-civil-district: `s 49A(3) a District Court may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` |
| s 49A(4) | 1466-1468 | encoded | sca-p4-civil-district: `s 49A(4) a District Court may hear the matter in an asynchronous manner` |
| s 49A(5) | 1470-1474 | encoded | sca-p4-civil-district: `s 49A(5) section 49A affects the power of a District Court to hear oral arguments before deciding the matter` |
| heading before s 49B(1) | 1476-1476 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 49B(1) | 1478-1481 | encoded | sca-p4-civil-district: `s 49B(1) the District Judge may on his or her own motion summarily dismiss the appeal` |
| s 49B(1)(a) | 1483-1486 | encoded | sca-p4-civil-district: `s 49B(1) the District Judge may on his or her own motion summarily dismiss the appeal` |
| s 49B(1)(b) | 1488-1489 | encoded | sca-p4-civil-district: `s 49B(1) the District Judge may on his or her own motion summarily dismiss the appeal` |
| s 49B(2) | 1491-1492 | encoded | sca-p4-civil-district: `s 49B(2) the District Judge has done what must be done before summarily dismissing the appeal`, regulative `s 49B(2) duty: a District Judge must give the appellant a reasonable opportunity to show cause` (QB) |
| s 49B(2)(a) | 1494-1495 | encoded | sca-p4-civil-district: `s 49B(2) the District Judge has done what must be done before summarily dismissing the appeal`, regulative `s 49B(2) duty: a District Judge must give the appellant a reasonable opportunity to show cause` (QB) |
| s 49B(2)(b) | 1497-1497 | encoded | sca-p4-civil-district: `s 49B(2) the District Judge has done what must be done before summarily dismissing the appeal`, regulative `s 49B(2) duty: a District Judge must give the appellant a reasonable opportunity to show cause` (QB) |
| s 49B(3) | 1499-1501 | encoded | sca-p4-civil-district: `s 49B(3) the thing is within the word appeal in this section` |
| heading before s 50(1) | 1506-1508 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 50(1) | 1510-1511 | encoded | sca-p4-magistrates-criminal: carried by the two paragraph functions `s 50(1)(a) ...` and `s 50(1)(b) ...` (the opening words add only "Subject to subsection (2)") |
| s 50(1)(a) | 1513-1514 | encoded | sca-p4-magistrates-criminal: `s 50(1)(a) a District Court exercising criminal jurisdiction has the jurisdiction or power` |
| s 50(1)(b) | 1516-1522 | encoded | sca-p4-magistrates-criminal: `s 50(1)(b) a District Court has the power to order the medical examination of the accused` |
| s 50(2) | 1524-1525 | encoded | sca-p4-magistrates-criminal: `s 50(2) the criminal jurisdiction of a District Court is exercisable over the offence` |
| s 50(2)(a) | 1527-1527 | encoded | sca-p4-magistrates-criminal: `s 50(2) the criminal jurisdiction of a District Court is exercisable over the offence` |
| s 50(2)(b) | 1529-1529 | encoded | sca-p4-magistrates-criminal: `s 50(2) the criminal jurisdiction of a District Court is exercisable over the offence` |
| s 50(2)(c) | 1531-1532 | encoded | sca-p4-magistrates-criminal: `s 50(2) the criminal jurisdiction of a District Court is exercisable over the offence` |
| s 50(2)(d) | 1534-1535 | encoded | sca-p4-magistrates-criminal: `s 50(2) the criminal jurisdiction of a District Court is exercisable over the offence` |
| heading before s 51(1) | 1537-1539 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 51(1) | 1541-1542 | encoded | sca-p4-magistrates-criminal: carried by the two paragraph functions `s 51(1)(a) ...` and `s 51(1)(b) ...` (the opening words add only "Subject to subsection (2)") |
| s 51(1)(a) | 1544-1545 | encoded | sca-p4-magistrates-criminal: `s 51(1)(a) a Magistrate's Court exercising criminal jurisdiction has the jurisdiction or power` |
| s 51(1)(b) | 1547-1553 | encoded | sca-p4-magistrates-criminal: `s 51(1)(b) a Magistrate's Court has the power to order the medical examination of the accused` |
| s 51(2) | 1558-1559 | encoded | sca-p4-magistrates-criminal: `s 51(2) the criminal jurisdiction of a Magistrate's Court is exercisable over the offence` |
| s 51(2)(a) | 1561-1561 | encoded | sca-p4-magistrates-criminal: `s 51(2) the criminal jurisdiction of a Magistrate's Court is exercisable over the offence` |
| s 51(2)(b) | 1563-1563 | encoded | sca-p4-magistrates-criminal: `s 51(2) the criminal jurisdiction of a Magistrate's Court is exercisable over the offence` |
| s 51(2)(c) | 1565-1566 | encoded | sca-p4-magistrates-criminal: `s 51(2) the criminal jurisdiction of a Magistrate's Court is exercisable over the offence` |
| s 51(2)(d) | 1568-1569 | encoded | sca-p4-magistrates-criminal: `s 51(2) the criminal jurisdiction of a Magistrate's Court is exercisable over the offence` |
| heading before s 52(1) | 1571-1571 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 52(1) | 1573-1575 | encoded | sca-p4-magistrates-criminal: `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 52(1)(a) | 1577-1578 | encoded | sca-p4-magistrates-criminal: `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 52(1)(a)(i) | 1580-1581 | encoded | sca-p4-magistrates-criminal: `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 52(1)(a)(ii) | 1583-1586 | encoded | sca-p4-magistrates-criminal: `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 52(1)(b) | 1588-1591 | encoded | sca-p4-magistrates-criminal: `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` |
| s 52(1A) | 1593-1594 | encoded | sca-p4-magistrates-criminal: `s 52(1A) the action falls within a class that subsection (1A) excludes from a Magistrate's Court's jurisdiction`, `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action`, `s 52(1A) the amount claimed or the value of the subject matter of the remedy or relief exceeds the Magistrate's Court limit` |
| s 52(1A)(a) | 1596-1596 | encoded | sca-p4-magistrates-criminal: `s 52(1A) the action falls within a class that subsection (1A) excludes from a Magistrate's Court's jurisdiction`, `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action`, `s 52(1A) the amount claimed or the value of the subject matter of the remedy or relief exceeds the Magistrate's Court limit` |
| s 52(1A)(aa) | 1598-1600 | encoded | sca-p4-magistrates-criminal: `s 52(1A) the action falls within a class that subsection (1A) excludes from a Magistrate's Court's jurisdiction`, `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action`, `s 52(1A) the amount claimed or the value of the subject matter of the remedy or relief exceeds the Magistrate's Court limit` |
| s 52(1A)(b) | 1602-1603 | encoded | sca-p4-magistrates-criminal: `s 52(1A) the action falls within a class that subsection (1A) excludes from a Magistrate's Court's jurisdiction`, `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action`, `s 52(1A) the amount claimed or the value of the subject matter of the remedy or relief exceeds the Magistrate's Court limit` |
| s 52(1A)(c) | 1605-1614 | encoded | sca-p4-magistrates-criminal: `s 52(1A) the action falls within a class that subsection (1A) excludes from a Magistrate's Court's jurisdiction`, `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action`, `s 52(1A) the amount claimed or the value of the subject matter of the remedy or relief exceeds the Magistrate's Court limit` |
| s 52(1B) | 1616-1617 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(a) | 1619-1619 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(a)(i) | 1621-1623 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(a)(ii) | 1625-1630 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(b) | 1632-1632 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(b)(i) | 1634-1634 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(b)(ii) | 1636-1636 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(b)(iii) | 1638-1641 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(c) | 1643-1647 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(d) | 1649-1649 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(d)(i) | 1651-1653 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(1B)(d)(ii) | 1655-1657 | encoded | sca-p4-magistrates-criminal: `s 52(1B) the Magistrate's Court has the power in the proceedings`, `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` |
| s 52(2) | 1659-1668 | encoded | sca-p4-magistrates-criminal: `s 52(2) a Magistrate's Court is subject to the limitation or provision in exercising its jurisdiction or powers`, `s 52 a Magistrate's Court has jurisdiction over the action` (fork F-S52(2)) |
| s 52(3) | 1670-1671 | inert | 2: machinery (a power of the President to vary the Magistrate's Court limit by order; the effect of an order is carried by the limit parameter of `s 2 "Magistrate's Court limit" the amount in dollars`) |
| s 53 | 1673-1673 | repealed | the text shows "53. [Repealed by Act 26 of 2005]" |
| heading before s 54 | 1675-1675 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54 | 1677-1680 | encoded | sca-p4-magistrates-criminal: `s 54 the judgment or order has the same effect and is enforced in the same manner as if given by a District Court` |
| heading before s 54AA(1) | 1682-1682 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54AA(1) | 1684-1687 | encoded | sca-p4-magistrates-criminal: `s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction`, `s 54AA(1) the bar on an appeal applies to the decision` |
| s 54AA(1)(a) | 1689-1689 | encoded | sca-p4-magistrates-criminal: `s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction`, `s 54AA(1) the bar on an appeal applies to the decision` |
| s 54AA(1)(b) | 1691-1692 | encoded | sca-p4-magistrates-criminal: `s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction`, `s 54AA(1) the bar on an appeal applies to the decision` |
| s 54AA(2) | 1694-1694 | encoded | sca-p4-magistrates-criminal: `s 54AA(2) an agreement mentioned in subsection (1) may be made at that time`, `s 54AA(2) the references in subsection (1) to a decision are references to that part of the decision` |
| s 54AA(2)(a) | 1696-1697 | encoded | sca-p4-magistrates-criminal: `s 54AA(2) an agreement mentioned in subsection (1) may be made at that time`, `s 54AA(2) the references in subsection (1) to a decision are references to that part of the decision` |
| s 54AA(2)(b) | 1699-1703 | encoded | sca-p4-magistrates-criminal: `s 54AA(2) an agreement mentioned in subsection (1) may be made at that time`, `s 54AA(2) the references in subsection (1) to a decision are references to that part of the decision` |
| heading before s 54A(1) | 1705-1708 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54A(1) | 1710-1719 | encoded | sca-p4-transfers: `s 54A(1) a District Court may order the proceedings to be transferred to the District Court` |
| s 54A(2) | 1721-1722 | encoded | sca-p4-transfers: `s 54A(2) the order may be made on such terms as the court sees fit` |
| heading before s 54B(1) | 1724-1725 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54B(1) | 1727-1735 | encoded | sca-p4-transfers: `s 54B(1) the General Division of the High Court may order the proceedings to be transferred to it` |
| s 54B(2) | 1737-1738 | encoded | sca-p4-transfers: `s 54B(2) the order may be made on such terms as the court sees fit`, `s 54B Explanation the intended enforcement overseas would ordinarily be sufficient reason for transferring the proceedings to the General Division of the High Court` |
| s 54B(2) Explanation | 1740-1745 | encoded | sca-p4-transfers: `s 54B(2) the order may be made on such terms as the court sees fit`, `s 54B Explanation the intended enforcement overseas would ordinarily be sufficient reason for transferring the proceedings to the General Division of the High Court` |
| heading before s 54C(1) | 1747-1748 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54C(1) | 1750-1755 | encoded | sca-p4-transfers: `s 54C(1) a party may apply to the General Division of the High Court for an order that the proceedings be transferred to a State Court` |
| s 54C(2) | 1757-1762 | encoded | sca-p4-transfers: `s 54C(2) the General Division of the High Court may order the proceedings to be transferred to a State Court` |
| s 54C(3) | 1767-1771 | encoded | sca-p4-transfers: `s 54C(3) an order under subsection (2) may be made in respect of the proceedings`, `s 54C Explanation the fact that the proceedings fall within the civil jurisdiction of the State Courts is by itself ordinarily sufficient reason for transferring the proceedings to the State Courts` |
| s 54C(3) Explanation | 1773-1779 | encoded | sca-p4-transfers: `s 54C(3) an order under subsection (2) may be made in respect of the proceedings`, `s 54C Explanation the fact that the proceedings fall within the civil jurisdiction of the State Courts is by itself ordinarily sufficient reason for transferring the proceedings to the State Courts` |
| heading before s 54D(1) | 1781-1782 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54D(1) | 1784-1787 | encoded | sca-p4-transfers: `s 54D(1) a party may apply to the District Court for an order that the proceedings be transferred to a Magistrate's Court` |
| s 54D(2) | 1789-1792 | encoded | sca-p4-transfers: `s 54D(2) the District Court may order the proceedings to be transferred to a Magistrate's Court` |
| s 54D(3) | 1794-1797 | encoded | sca-p4-transfers: `s 54D(3) an order under subsection (2) may be made in respect of the proceedings` |
| heading before s 54E(1) | 1799-1800 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54E(1) | 1802-1815 | encoded | sca-p4-transfers: `s 54E(1) a party may apply to the General Division of the High Court for a transfer of the proceedings or of the counterclaim` |
| s 54E(2) | 1817-1819 | encoded | sca-p4-transfers: `s 54E(2) the General Division of the High Court may make the order` |
| s 54E(2)(a) | 1821-1822 | encoded | sca-p4-transfers: `s 54E(2) the General Division of the High Court may make the order` |
| s 54E(2)(b) | 1824-1824 | encoded | sca-p4-transfers: `s 54E(2) the General Division of the High Court may make the order` |
| s 54E(2)(c) | 1826-1834 | encoded | sca-p4-transfers: `s 54E(2) the General Division of the High Court may make the order` |
| s 54E(3) | 1836-1844 | encoded | sca-p4-transfers: `s 54E(3) enforcement on the judgment on the claim is stayed` |
| s 54E(4) | 1846-1851 | encoded | sca-p4-transfers: `s 54E(4) the State Court has jurisdiction to try the proceedings despite any other provision of this Act` |
| heading before s 54F(1) | 1853-1854 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54F(1) | 1856-1866 | encoded | sca-p4-transfers: `s 54F(1) a party may apply to the District Court for a transfer of the proceedings or of the counterclaim` |
| s 54F(2) | 1868-1870 | encoded | sca-p4-transfers: `s 54F(2) the District Court may make the order` |
| s 54F(2)(a) | 1872-1873 | encoded | sca-p4-transfers: `s 54F(2) the District Court may make the order` |
| s 54F(2)(b) | 1875-1876 | encoded | sca-p4-transfers: `s 54F(2) the District Court may make the order` |
| s 54F(2)(c) | 1878-1884 | encoded | sca-p4-transfers: `s 54F(2) the District Court may make the order` |
| s 54F(3) | 1886-1891 | encoded | sca-p4-transfers: `s 54F(3) enforcement on the judgment on the claim is stayed` |
| s 54F(4) | 1893-1896 | encoded | sca-p4-transfers: `s 54F(4) the Magistrate's Court has jurisdiction to try the proceedings despite any other provision of this Act` |
| heading before s 54G(1) | 1898-1898 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 54G(1) | 1900-1900 | encoded | sca-p4-transfers: `s 54G(1) the costs of the whole proceedings are in the discretion of the court to which the proceedings are transferred`, `s 54G(1) the court to which the proceedings are transferred has power to make orders as to costs and the scales on which the costs of the several parts are to be paid` |
| s 54G(1)(a) | 1902-1903 | encoded | sca-p4-transfers: `s 54G(1) the costs of the whole proceedings are in the discretion of the court to which the proceedings are transferred`, `s 54G(1) the court to which the proceedings are transferred has power to make orders as to costs and the scales on which the costs of the several parts are to be paid` |
| s 54G(1)(b) | 1905-1906 | encoded | sca-p4-transfers: `s 54G(1) the costs of the whole proceedings are in the discretion of the court to which the proceedings are transferred`, `s 54G(1) the court to which the proceedings are transferred has power to make orders as to costs and the scales on which the costs of the several parts are to be paid` |
| s 54G(1)(c) | 1908-1921 | encoded | sca-p4-transfers: `s 54G(1) the costs of the whole proceedings are in the discretion of the court to which the proceedings are transferred`, `s 54G(1) the court to which the proceedings are transferred has power to make orders as to costs and the scales on which the costs of the several parts are to be paid` |
| s 54G(2) | 1923-1925 | encoded | sca-p4-transfers: carried by the two paragraph functions `s 54G(2)(a) ...` and `s 54G(2)(b) ...` |
| s 54G(2)(a) | 1927-1927 | encoded | sca-p4-transfers: `s 54G(2)(a) the costs of the part of the proceedings before the transfer are subject to section 39` |
| s 54G(2)(b) | 1929-1935 | encoded | sca-p4-transfers: `s 54G(2)(b) the State Court may exercise the powers of the General Division of the High Court under section 39(4)` |
| s 55 | 1937-1937 | repealed | the text shows "55. [Repealed by Act 27 of 2014]" |
| s 56 | 1939-1939 | repealed | the text shows "56. [Repealed by Act 14 of 2010]" |
| s 56A | 1941-1941 | repealed | the text shows "56A. [Repealed by Act 15 of 2010]" |
| heading before s 57(1) | 1943-1947 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 57(1) | 1949-1952 | encoded | sca-p5-administration: `s 57(1) the Registry of the State Courts is to be open on the day` (fork F-VACATION) |
| s 57(2) | 1954-1956 | encoded | sca-p5-administration: `s 57(2) the registrar may lawfully sit or carry out the business of the Registry on the day` |
| s 57(2)(a) | 1958-1960 | encoded | sca-p5-administration: `s 57(2) the registrar may lawfully sit or carry out the business of the Registry on the day` |
| s 57(2)(b) | 1962-1965 | encoded | sca-p5-administration: `s 57(2) the registrar may lawfully sit or carry out the business of the Registry on the day` |
| s 57(3) | 1970-1974 | encoded | sca-p5-administration: `s 57(3) the time is within the office hours of the Registry` |
| heading before s 58 | 1976-1976 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 58 | 1978-1979 | encoded | sca-p5-administration: `s 58 both civil and criminal proceedings may be tried at the sitting of the court` |
| heading before s 59 | 1981-1981 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 59 | 1983-1988 | encoded | sca-p5-administration: `s 59 the distribution of business in the State Courts has been made in accordance with the directions` (QB) |
| heading before s 60(1) | 1990-1990 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 60(1) | 1992-1996 | inert | 2: machinery (an office attached to each State Court or a number of State Courts: an office and its staffing) |
| s 60(2) | 1998-2003 | inert | 2: machinery (the Presiding Judge apportions the work among the officers in an office: an office and its staffing) |
| heading before s 61 | 2005-2005 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 61 | 2007-2009 | encoded | sca-p5-administration: `s 61 the Chief Justice may authorise the vacations` |
| heading before s 62(1) | 2011-2011 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 62(1) | 2013-2013 | encoded | sca-p5-administration: `s 62(1) the Presiding Judge of the State Courts may frame, publish, alter and amend the list of touts`, `s 62(1)(a) the person may be named in the list of touts` |
| s 62(1)(a) | 2015-2018 | encoded | sca-p5-administration: `s 62(1) the Presiding Judge of the State Courts may frame, publish, alter and amend the list of touts`, `s 62(1)(a) the person may be named in the list of touts` |
| s 62(1)(b) | 2023-2025 | encoded | sca-p5-administration: `s 62(1) the Presiding Judge of the State Courts may frame, publish, alter and amend the list of touts`, `s 62(1)(a) the person may be named in the list of touts` |
| s 62(2) | 2027-2033 | encoded | sca-p5-administration: `s 62(2) the Presiding Judge of the State Courts may exclude the person from the precincts of the State Courts`, `s 62(2) the person is allowed to remain in the precincts of the State Courts for such time as is necessary` |
| s 62(3) | 2035-2037 | encoded | sca-p5-administration: `s 62(3) the person's name may be included in the list of touts` (fork F-PASSIVE) |
| s 62(4) | 2039-2043 | encoded | sca-p5-administration: `s 62(4) an appeal lies to a Judge sitting in chambers in the General Division of the High Court` |
| s 62(5) | 2045-2047 | encoded | sca-p5-administration: `s 62(5) the decision of the Judge is final` |
| s 62(6) | 2049-2052 | encoded | sca-p5-administration: `s 62(6) a copy of the list is kept hung up and the list has been published in the Gazette` (QB) |
| s 62(7) | 2054-2059 | encoded | sca-p5-administration: `s 62(7) the person is deemed to be included in the list under this section`, `s 62(7) the person is deemed to be included in the list under section 73 of the Supreme Court of Judicature Act 1969 or section 39 of the Family Justice Act 2014` |
| heading before s 63(1) | 2061-2061 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 63(1) | 2063-2066 | encoded | sca-p5-administration: `s 63(1) a State Court may order the document to be impounded` |
| s 63(2) | 2068-2070 | encoded | sca-p5-administration: `s 63(2) the impounded document may be delivered out of the custody of the court or inspected` (fork F-PASSIVE) |
| s 63(3) | 2072-2074 | encoded | sca-p5-administration: `s 63(3) the court may direct the document to be sent to the Attorney-General, the Commissioner of Stamp Duties or any other officer of the Government` |
| heading before s 64(1) | 2079-2079 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 64(1) | 2081-2082 | encoded | sca-p5-administration: carried by `s 64(1)(a) ...` and `s 64(1)(b) ...` (the opening words add only "Except with the approval of the Chief Justice") |
| s 64(1)(a) | 2084-2084 | encoded | sca-p5-administration: `s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business` |
| s 64(1)(a)(i) | 2086-2086 | encoded | sca-p5-administration: `s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business` |
| s 64(1)(a)(ii) | 2088-2089 | encoded | sca-p5-administration: `s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business` |
| s 64(1)(b) | 2091-2095 | encoded | sca-p5-administration: `s 64(1)(b) the judicial officer may accept the fees of office, perquisites, emoluments or advantages`, regulative `s 64(1)(b) duty: ...` |
| s 64(2) | 2097-2098 | encoded | sca-p5-administration: carried by `s 64(2)(a) ...` and `s 64(2)(b) ...` (the opening words add only "Without limiting subsection (1) ... with the approval of the Chief Justice") |
| s 64(2)(a) | 2100-2105 | encoded | sca-p5-administration: `s 64(2)(a) the judicial officer may be appointed to the body or hold the office` |
| s 64(2)(b) | 2107-2110 | encoded | sca-p5-administration: `s 64(2)(b) the judicial officer may receive the allowance or other honorarium` |
| heading before s 65 | 2112-2112 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 65 | 2114-2117 | encoded | sca-p5-administration: `s 65 the judicial officer may investigate, try or commit for trial the proceedings`, regulative `s 65 duty: ...` |
| heading before s 66 | 2119-2119 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 66 | 2121-2125 | encoded | sca-p5-administration: `s 66 the officer may purchase or bid for the property`, regulative `s 66 duty: ...` |
| heading before s 67(1) | 2130-2130 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 67(1) | 2132-2134 | encoded | sca-p5-administration: `s 67(1) it is lawful for the District Judge to inquire into the matter in a summary manner` |
| s 67(1)(a) | 2136-2137 | encoded | sca-p5-administration: `s 67(1) it is lawful for the District Judge to inquire into the matter in a summary manner` |
| s 67(1)(b) | 2139-2146 | encoded | sca-p5-administration: `s 67(1) it is lawful for the District Judge to inquire into the matter in a summary manner` |
| s 67(2) | 2148-2150 | encoded | sca-p5-administration: `s 67(2) the District Judge may summon and enforce the attendance of all necessary parties` |
| s 67(3) | 2152-2157 | encoded | sca-p5-administration: `s 67(3) the District Judge may order repayment of the money extorted or payment of the money levied, damages and costs`, `s 67(3) the District Judge may impose the fine upon the officer` |
| s 67(4) | 2159-2167 | encoded | sca-p5-administration: `s 67(4) the officer is incapable of being an officer of the State Courts` |
| s 67(5) | 2169-2170 | encoded | sca-p5-administration: `s 67(5) an appeal lies to the Chief Justice` |
| s 67(6) | 2172-2172 | encoded | sca-p5-administration: `s 67(6) the decision of the Chief Justice is final` |
| heading before s 68(1) | 2177-2177 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 68(1) | 2179-2183 | encoded | sca-p5-administration: `s 68(1) the judicial officer is liable to be sued for the act` |
| s 68(2) | 2185-2187 | encoded | sca-p5-administration: `s 68(2) the officer is liable to be sued`, `s 68(2) the bar on suing the officer applies` |
| s 68(2)(a) | 2189-2191 | encoded | sca-p5-administration: `s 68(2) the officer is liable to be sued`, `s 68(2) the bar on suing the officer applies` |
| s 68(2)(b) | 2193-2200 | encoded | sca-p5-administration: `s 68(2) the officer is liable to be sued`, `s 68(2) the bar on suing the officer applies` |
| s 68(3) | 2202-2209 | encoded | sca-p5-administration: `s 68(3) the officer is deemed to have acted knowingly in excess of his or her authority` |
| s 68(4) | 2211-2214 | encoded | sca-p5-administration: `s 68(4) the person is liable to be sued for the act` |
| s 68(4)(a) | 2216-2216 | encoded | sca-p5-administration: `s 68(4) the person is liable to be sued for the act` |
| s 68(4)(b) | 2218-2221 | encoded | sca-p5-administration: `s 68(4) the person is liable to be sued for the act` |
| heading before s 69(1) | 2226-2226 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 69(1) | 2228-2233 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(2) | 2235-2244 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3) | 2246-2247 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(a) | 2249-2251 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(b) | 2253-2254 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(c) | 2256-2261 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(d) | 2263-2267 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(e) | 2272-2272 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(e)(i) | 2274-2276 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(e)(ii) | 2278-2281 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(f) | 2283-2283 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(f)(i) | 2285-2287 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(f)(ii) | 2289-2289 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(f)(iii) | 2291-2291 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(f)(iv) | 2293-2302 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(g) | 2304-2304 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(g)(i) | 2306-2310 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(g)(ii) | 2312-2318 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(g)(iii) | 2323-2330 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(h) | 2332-2333 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(h)(i) | 2335-2337 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(h)(ii) | 2339-2340 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(h)(iii) | 2342-2349 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(i) | 2351-2356 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3)(j) | 2358-2361 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(3A) | 2363-2367 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| s 69(4) | 2369-2370 | inert | 2: machinery (the power of the Rules Committee to make Rules of Court: a rule-making power; the Rules are not among the sources) |
| heading before s 70(1) | 2375-2380 | inert | 1: not operative (Part, sub-Part or section heading) |
| s 70(1) | 2382-2382 | encoded | sca-p6-supplemental: `s 70(1) the Court may order the pending action or application to be converted and continued by way of a writ of summons or an originating summons` (moved out of the savings reading of reason 2) |
| s 70(1)(a) | 2384-2387 | encoded | sca-p6-supplemental: `s 70(1) the Court may order the pending action or application to be converted and continued by way of a writ of summons or an originating summons` (moved out of the savings reading of reason 2) |
| s 70(1)(b) | 2389-2404 | encoded | sca-p6-supplemental: `s 70(1) the Court may order the pending action or application to be converted and continued by way of a writ of summons or an originating summons` (moved out of the savings reading of reason 2) |
| s 70(2) | 2406-2414 | encoded | sca-p6-supplemental: `s 70(2) the Presiding Judge of the State Courts may by order direct that a class or description of pending actions or applications be converted` |
| s 70(3) | 2416-2423 | encoded | sca-p6-supplemental: carried by `s 70(3)(a) ...` and `s 70(3)(b) ...` |
| s 70(3)(a) | 2425-2429 | encoded | sca-p6-supplemental: `s 70(3)(a) the converted action or application is continued in accordance with the relevant written law and the practice and procedure in force at the time of the conversion` |
| s 70(3)(b) | 2431-2437 | encoded | sca-p6-supplemental: `s 70(3)(b) the Court may give the parties directions as to the conduct and costs of the action or application` |
| Schedule heading (THE SCHEDULE, Forms of oaths and affirmations) | 2439-2441 | inert | 1: not operative (heading) |
| Schedule para 1 (oath of office and allegiance of a judicial officer) | 2443-2459 | encoded | sca-p3-appointments: `Schedule para 1 the oath of office and allegiance of a judicial officer`; `Schedule the oath that section 17(1) requires of the holder` |
| Schedule para 2 (oath of office of an interpreter) | 2461-2484 | encoded | sca-p3-appointments: `Schedule para 2 the oath of office of an interpreter`; `Schedule the oath that section 17(1) requires of the holder` |
| Schedule para 3 (oath of office of other officer of a court) | 2486-2507 | encoded | sca-p3-appointments: `Schedule para 3 the oath of office of other officer of a court`; `Schedule the oath that section 17(1) requires of the holder` |
| Legislative History (not part of the Act) and Abbreviations | 2510-3719 | inert | 1: not operative (the text says: "It is not part of the Act") |

rows: 480; by disposition: encoded=344, inert=119, repealed=17
inert by reason: 1=79, 2=40
non-blank lines: 2398; in a row: 2259; page furniture (footers): 139; unassigned: 0
COVERAGE OK

## Fork register

Every ambiguity, the readings seen, the one taken, and the text that licenses each.
The four rulings that bind this row are copied here word for word from the brief:

- **E1.** Do not look for, or propose, a language construct that gathers a legal effect "by name" from every section that gives it. Where several sections give the same legal effect, encode each section's answer on its own (option C). You may, by hand and in plain L4, write one function that gathers the routes to a legal effect where that helps a reader (option B as guidance for hand-gathering only); say in the fork register where you did. The Magna Carta pilot is not to be run.
- **N2.** A flat negative in the text ("shall not", "is not", "no person") counts as the text's no, so the answer is `JUST FALSE`, and where the text names who bears a prohibition, the prohibition (`SHANT`) is derived from that answer. Do not type the Hohfeld kind into the person-facing answer. Record the kinds in `NOTES.md` under `## Jural relations`.
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

| id | provision | function | readings seen | reading taken | text licensing each |
| --- | --- | --- | --- | --- | --- |
| F-LIMIT | s 2 "District Court limit", "Magistrate's Court limit" | `sca-p1-preliminary.l4:187` | (1) the limit is the Act's own figure ($250,000, $60,000) unless an order under s 30 or s 52(3) specifies another amount; (2) the limit is whatever the latest order says, so the figure in the Act is only a default | (1): the Act's figure, with the order's amount taken as an optional input (`MAYBE NUMBER`, `NOTHING` = no order); the seat uses the Act's figure and does not ask the person for an order's amount, so a substitution by order would change every answer that turns on a limit | "means $250,000 or any other amount specified by an order under section 30" (s 2); "The President may ... by order vary the Magistrate’s Court limit" (s 52(3)) |
| F-BORROWED | s 2 "Coroner", s 7(7) "broadcasting service", "newspaper" | `sca-p1-preliminary.l4:176` | (1) the meaning is wholly the other Act's, so the borrowed fact decides; (2) the term is undefined here and the answer is `NOTHING` | (1): the text says "has the meaning given by" another provision, so the fact is asked and its answer passed through (`JUST TRUE` / `JUST FALSE`) | "has the meaning given by section 2(1) of the Coroners Act 2010" (s 2); "has the meaning given by section 2(1) of the Broadcasting Act 1994" (s 7(7)) |
| F-S3-LIST | s 3(1) | `sca-p2-constitution.l4:20` | (1) the five paragraphs close the list of State Courts; (2) the list is open | (2): "the following subordinate courts called the State Courts" does not say "only", so a court outside the five is `NOTHING`, not `JUST FALSE` | s 3(1) |
| F-VACATION | s 6A(1), (2) | `sca-p2-constitution.l4:133` | (1) a day in a vacation authorised under s 61 is an ordinary day for s 6A(1), so the court is to sit; (2) subsection (1) is "Subject to subsection (2)", which treats sitting during a vacation like sitting on a Saturday, Sunday or public holiday, so the court is not to sit | neither: `NOTHING` for a vacation day under (1); (2) answers the lawful-sitting question on its own terms | s 6A(1) "except on Saturdays, Sundays and public holidays" (vacations not excepted); s 6A(2) "or during a vacation authorised under section 61" |
| F-QUALYEARS | ss 9(3), 9(3A), 10(2), 10(3), 12(2) | `sca-p3-appointments.l4:67` | (1) "a qualified person as defined in section 2 of the Legal Profession Act 1966" is asked as a count of complete years; (2) as a date from which the person has been qualified | (1): a plain number of complete years, so the boundary is tested at 6/7, 4/5, 2/3 and 0/1 | "for not less than 7 years" (s 9(3)); "for not less than 5 years" (s 9(3A)(a)); "for not less than 3 years" (s 10(2)); "for not less than one year" (s 10(3)(a)) |
| F-S15-ENGAGE | s 15(2) | `sca-p3-appointments.l4:255` | (1) the list ("auxiliary police officer ... solicitor or any other appropriate person") is a closed set of kinds; (2) the last item hands the judgment of "appropriate" to the registrar | (2): one yes/no input, whether the person is one of the listed kinds or otherwise appropriate (a judgment handed to someone else is a conditional input) | s 15(2) "or any other appropriate person" |
| F-S16-FORCE | s 16 | `sca-p3-appointments.l4:310` | (1) breaking open when it is not necessary is not allowed (JUST FALSE); (2) not decided (NOTHING); and force beyond what is reasonably necessary: (a) forbidden (JUST FALSE) or (b) outside the grant (NOTHING) | not necessary -> JUST FALSE (a failed "if necessary", the lawyer's reading (a)); excessive force -> NOTHING (the grant is limited by "such force as is reasonably necessary" and nothing in s 16 forbids more) | s 16 "if necessary, may break open ... using such force as is reasonably necessary to effect an entry" |
| F-S17-OATH | s 17(1) and the Schedule | `sca-p3-appointments.l4:403` | (1) the Schedule's oath 3 ("other officer of a court") is for every officer who is neither a judicial officer nor an interpreter; (2) it is for the officers s 14 lists | (1) for a bailiff, process server, commissioner for oaths and other officer of a State Court; the Presiding Judge, a Justice of the Peace and a Supreme Court Judge are not placed in any oath (NOTHING), because the Schedule does not say | Schedule paras 1 to 3; s 17(1) |
| F-S17-2A | s 17(2A)(a) to (c) (SCA1970.txt l.800-817) | `sca-p3-appointments.l4:452` | (1) the subsection opens "To avoid doubt" and confirms that a person "may take and subscribe the oath by appearing ... through a live video link or live television link created using a remote communication technology that allows" (a), (b) and (c); a link that fails any one, for example (c) "verify by inspection the oath to be subscribed", is outside the confirmation and the subsection is silent on it; (2) (a) to (c) are conditions of taking the oath by link, so a link failing (c) is not allowed | (1): `NOTHING` when any of (a), (b), (c) fails. The subsection has no "if" and no "only", and "to avoid doubt" confirms a power that subsection (1) is read as already giving rather than granting a new one; it is not a flat negative | l.800 "To avoid doubt, where an oath is required to be taken and subscribed under subsection (1), a person may take and subscribe the oath by appearing before ..."; l.817 "(c) verify by inspection the oath to be subscribed." |
| F-COMBINE | ss 19, 22, 23 and s 52 read together | `sca-p4-civil-district.l4:241`; `sca-p4-magistrates-criminal.l4:257` | (1) no combined function at all (ruling E1, option C: each section answers for itself); (2) one function that gathers the sections by hand (option B) | both: the per-section functions are the encoding of the text, and the two combined functions are hand-gathered and say so in their header comment; a reader of the seat needs one answer to "does this court have jurisdiction?", and the gathering is recorded here so it can be checked against the sections | s 19(2) to (4), ss 22 and 23, s 52(1), (1A) and (2) |
| F-S19-28A | s 19(3) | `sca-p4-civil-district.l4:84` | (1) the exclusions of s 19(3) apply whatever section 28A of the Supreme Court of Judicature Act 1969 or an order under it says; (2) "Subject to section 28A ... and any order under subsection (1) thereof" lets that section or order change the result, and neither is among the sources | (2): an input `section 28A ... affects the action`; when it is true, the answer is `NOTHING` (points outside the text) | s 19(3) "Subject to section 28A of the Supreme Court of Judicature Act 1969 and any order under subsection (1) thereof" |
| F-S25-B | s 25(b) (SCA1970.txt l.1011-1014) | `sca-p4-civil-district.l4:279` | (1) paragraphs (a), (b) and (c) are alternatives ("; or" ends (b)), and inside (b) the annual-rent test and the monthly-rent test are alternatives ("or"), so any one test met is enough; (2) the annual-rent and monthly-rent tests are cumulative | (1): either the annual-rent test or the monthly-rent test is enough. The monthly test is one-twelfth of the District Court limit, which is $20,833.33 at $250,000; "does not exceed" makes $20,833.33 pass, so a monthly rent of $20,833 passes and $20,834 fails (asserted at `sca-tests-p4a.l4`). If an order under s 30 has changed the limit, the figure moves with it | l.1011 "(b) the annual rent payable by the tenant does not exceed the District Court limit or the monthly rent payable by the tenant does not exceed one-twelfth of the District Court limit; or" |
| F-S25-C | s 25(c) (SCA1970.txt l.1016-1018) | `sca-p4-civil-district.l4:307` | (1) "if the annual value, annual rent or monthly rent cannot be ascertained" means that none of the three can be ascertained, so the last-transacted-price test (10 times the limit) applies only when no measure of value or rent exists; when one is known it is tested under (a) or (b) and failing it answers `JUST FALSE`; (2) it means that any one of the three cannot be ascertained, so the price test applies as soon as one figure is missing, and a missing figure plus a price within ten times the limit gives `JUST TRUE` | (1): all three. A failed "where" is `JUST FALSE` (ruling (b) of 2026-11-05) and a fallback that is not triggered is a failed "if". Asserted: annual value $300,000 known, price $100 known, nothing else known: `JUST FALSE` | l.1016 "(c) if the annual value, annual rent or monthly rent cannot be ascertained, the last transacted price of the property does not exceed 10 times the District Court limit." |
| F-S29-AND | s 29(1)(a) and (b) (SCA1970.txt l.1077-1094) | `sca-p4-civil-district.l4:394` | (1) paragraphs (a) and (b) are joined by "and", so both must hold (cumulative); (2) they are two different situations, each its own ground: (a) a bailiff executing a writ or order of the Court against a claimant who is not the person against whom it was issued; (b) a person under liability for a debt or movable property, within the District Court limit, who has been or expects to be sued by 2 or more parties making adverse claims | (2), assumed, not ruled (fix round, 2026-11-05): `JUST TRUE` when (a) holds, whatever the amount; `JUST TRUE` when (b) holds and the amount or value is at most the District Court limit; `JUST FALSE` when neither holds (a "where" that is not met, ruling (b) of 2026-11-05); the limit is tested only on (b), because only (b) carries it in its own words. Reading (1) was the earlier encoding: it left a District Court almost never able to grant interpleader relief and answered `JUST FALSE` for a stakeholder owed $100,000 by two rival claimants | l.1081 "(a) where a bailiff of a District Court is charged with the execution of any writ or order of the Court ...; and"; l.1089 "(b) where the person seeking relief is under liability for any debt, money, or other movable property of which the amount or value does not exceed the District Court limit ... expects to be sued by 2 or more parties making adverse claims thereto"; the "and" at the end of (a) supports (1), the different subject matter of the two paragraphs supports (2) |
| F-S52-2 | s 52(2), with s 19(3), s 22 and s 23 | `sca-p4-magistrates-criminal.l4:257` | (1) "the same limitations and provisions as are applicable to a District Court under this Act" brings s 19(3)'s exclusions to the Magistrate's Court and also brings ss 22 and 23 (abandoning the excess, agreeing in writing), read with the Magistrate's Court limit; (2) it brings s 19(3) only; (3) it brings nothing, because s 52(1A) is the Magistrate's Court's own list | s 19(3)'s exclusions apply (`JUST FALSE`); for an action over the Magistrate's Court limit where the claimant has abandoned the excess or the parties have agreed in writing, `NOTHING`, because ss 22 and 23 name "a District Court" and the text does not say they are among the "provisions" borrowed | s 52(2) "subject to the same limitations and provisions as are applicable to a District Court under this Act"; s 22(1) "a District Court has jurisdiction"; s 23 "a District Court has jurisdiction" |
| F-S39-LIMIT | s 39(1)(a) and (b) (SCA1970.txt l.1227-1240) | `sca-p4-civil-district.l4:633` | (1) paragraphs (a) (the District Court limit) and (b) (the Magistrate's Court limit) are two limbs, and a recovery that satisfies both (any sum at or below the Magistrate's Court limit) is capped by both, so the function would have to pick the lower; (2) the single function takes "the limit" as an input, and the caller chooses which limit to ask about | (2): one function with the limit as an input, because the two paragraphs have the same shape and differ only in the figure. At or below the limit given the answer is `JUST FALSE`, above it `NOTHING`; the function does not say which limit governs when a recovery satisfies both, so a recovery of $50,000 asked against $250,000 and against $60,000 answers `JUST FALSE` both times, and a recovery of $100,000 answers `JUST FALSE` against $250,000 and `NOTHING` against $60,000. The caller who wants the tighter cap asks against the Magistrate's Court limit. The seat passes the figures from the Act | l.1231 "(a) if he or she recovers a sum not exceeding the District Court limit, is not entitled to any more costs ... than those ... if the action had been brought in a District Court; and"; l.1236 "(b) if he or she recovers a sum not exceeding the Magistrate's Court limit ... Magistrate's Court"; the text does not say how (a) and (b) combine when both are met |
| F-S54-EXPLAIN | the Explanations to s 54B(2) and s 54C(3) | `sca-p4-transfers.l4:74`; `sca-p4-transfers.l4:133` | (1) "would ordinarily be sufficient" is a rule that overseas enforcement is sufficient reason; (2) it is a hedge that leaves the court free in a given case | (2): the function answers "ordinarily", as its name says, and not "always"; for the case outside the Explanation it is `NOTHING` | "would ordinarily be sufficient reason"; "would not, by itself, ordinarily constitute sufficient reason" |
| F-S57-VACATION | s 57(1) | `sca-p5-administration.l4:16` | (1) the Registry is open on a day in a vacation authorised under s 61, because only Saturdays, Sundays and public holidays are excepted; (2) a vacation under s 61 closes the Registry, because s 61 allows vacations | (1): s 57(1) excepts three kinds of day in its own words, and s 61 speaks of vacations "for District Courts and Magistrates’ Courts in the exercise of their civil jurisdiction", not of the Registry | s 57(1) "on every day of the year except on Saturdays, Sundays and public holidays"; s 61 |
| F-PASSIVE | s 35, s 62(3), s 63(2) | `sca-p4-civil-district.l4:577`; `sca-p5-administration.l4:160`; `sca-p5-administration.l4:244` | (1) a flat negative in the passive voice ("must not be divided", "must not be included", "must not be delivered") gets a regulative `SHANT` rule (ruling N2: SHANT is derived); (2) with no bearer named in the sentence, a `SHANT` rule would need an invented actor | (2): the decision function answers `JUST FALSE` in the text's own words and no `PARTY ... SHANT` rule is written; the brief says not to invent actors. Where the sentence names its bearer (ss 7(4), 8(3), 64(1)(b), 65, 66), a `SHANT` rule is written | s 35 "A cause of action must not be divided"; s 62(3) "A person’s name must not be included in the list until"; s 63(2) "must not be delivered out of the custody of the court or inspected except on an order" |
| F-S64-APPROVAL | s 64(2) | `sca-p5-administration.l4:320`; `sca-p5-administration.l4:336` | (1) "may, with the approval of the Chief Justice" makes the approval a condition, so without it a judicial officer may not (`JUST FALSE`); (2) it describes the occasion on which the power arises, and without it the subsection says nothing (`NOTHING`) | (1): a condition stated in the grant's own words is read as an "if" (marginal reading (a)); s 64(1) separately forbids the same things "Except with the approval of the Chief Justice" | s 64(2) "may, with the approval of the Chief Justice"; s 64(1) |
| F-S70-SAVINGS | s 70 | `sca-p6-supplemental.l4:36` | (1) s 70 is a savings provision for pending petitions and is inert (reason 2); (2) it is operative, because it gives a court a power over pending proceedings | (2): encoded, with nothing left inert on the strength of a reading the text does not state | s 70(1) "the Court may, if it thinks just and expedient, order that the action or application ... be converted" |

Rulings applied without a fork, because the brief rules them: a failed "where" is `JUST FALSE` (ruling (b) of 2026-11-05; the sites carry a comment naming it); "On", "upon" and "thereupon" count as "where" (ruling (c)); a deeming or a stay lifted by "unless" or "except" answers `JUST FALSE` (the brief's own carve-out from QA).
Hand-gathering is recorded under F-COMBINE.

## Judgment calls

The six sites the brief names.
QA is "unless" or "except" once met; QB is a bare "must" not done; QC is "listed in Schedule N"; QD is a duty whose "if" or "where" is unmet; QE is "(other than X)"; QF is a missing event in a ledger.
The defaults apply unless the text points the other way, and each site is one line.
**QC** never arises (the only Schedule holds three oaths).
**QD** never arises in this Act as a compliance question (see the QD line below).
**QF** is not applicable: this encoding writes no events to the state ledger.
**The nine QB functions are named to say what they ask.**
Each ends "as the section requires" (ss 5, 6, 6A(3), 17(1), 17(3), 17(4), 49B(2), 59, 62(6)), so the name says the function asks whether a requirement is met and not what a fact is: it answers `NOTHING` when the thing is not done, because the text says nothing of the consequence.

| question id | provision | function name | file:line | answer taken | other reading |
| --- | --- | --- | --- | --- | --- |
| QA | s 8(3)(b) | s 8(3) the State Court may conduct the part of the hearing through a live audio link only | `sca-p2-constitution.l4:448` | NOTHING when "unless all the parties consent" is met (a lifted bar grants nothing); a twin `s 8(3) the bar on a live audio link only applies to the part of the hearing` answers `JUST FALSE` there | JUST TRUE (the exception permits it) |
| QB | s 5 | s 5 the State Courts have and use a seal of the nature the Chief Justice has prescribed as the section requires | `sca-p2-constitution.l4:95` | NOTHING (a bare "are to have and use" not done) | JUST FALSE for the compliance question |
| QB | s 6 | s 6 the process of the State Courts is signed by a judicial officer and bears the seal of the court as the section requires | `sca-p2-constitution.l4:110` | NOTHING (bare "must be signed ... must bear the seal"; "Subject to Rules of Court" also points outside the text) | JUST FALSE for the compliance question |
| QB | s 6A(3) | s 6A(3) the State Court sits at the time and place the Chief Justice has appointed as the section requires | `sca-p2-constitution.l4:173` | NOTHING (bare "is to sit") | JUST FALSE for the compliance question |
| QE | s 8(1) | s 8(1) the State Court may conduct the hearing through the means | `sca-p2-constitution.l4:406` | NOTHING for a matter prescribed by the Rules of Court or the Criminal Procedure Rules ("other than" limits a grant) | JUST FALSE (as "except") |
| QA | s 9(3) | s 9(3) the person may be appointed to be or to act as a District Judge | `sca-p3-appointments.l4:67` | NOTHING at 7 years or more (a lifted bar grants nothing; the power is s 9(1)) | JUST TRUE (the exception permits it) |
| QA | s 10(2) | s 10(2) the person may be appointed to be or to act as a Magistrate | `sca-p3-appointments.l4:125` | NOTHING at 3 years or more | JUST TRUE |
| QA | s 12(2) | s 12(2) the person may be appointed to be or to act as registrar | `sca-p3-appointments.l4:172` | NOTHING when the person is a qualified person; JUST TRUE when the Chief Justice appoints an unqualified person in his or her discretion (the exception "except that the Chief Justice may" is itself a grant, so the default is not followed there) | JUST TRUE in both cases / NOTHING in both |
| QB | s 17(1) | s 17(1) the oath was taken and subscribed before the functions of the office were exercised as the section requires | `sca-p3-appointments.l4:339` | NOTHING (bare "are to take and subscribe"; the Act does not say here what follows) | JUST FALSE for the compliance question |
| QB | s 17(3) | s 17(3) the Presiding Judge of the State Courts has entered the oath in the record and transmitted a certified copy as the section requires | `sca-p3-appointments.l4:472` | NOTHING (bare "he or she is to") | JUST FALSE |
| QB | s 17(4) | s 17(4) the Presiding Judge of the Family Justice Courts has entered the oath in the record and transmitted the certified copies as the section requires | `sca-p3-appointments.l4:492` | NOTHING (bare "he or she is to") | JUST FALSE |
| QA | s 19(4) | s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value | `sca-p4-civil-district.l4:115` | NOTHING when the claimant has abandoned the excess or the parties have agreed ("Subject to sections 22 and 23": a lifted bar grants nothing; ss 22 and 23 are the grants); the combined `s 19 a District Court has jurisdiction over the action` gathers them and answers JUST TRUE | JUST TRUE (the exception permits it) |
| QA | s 43(3) | s 43(3) enforcement may issue | `sca-p4-civil-district.l4:822` | NOTHING once the District Court has given permission ("except with the permission"); a twin `s 43(3) the bar on enforcement applies` answers JUST FALSE then | JUST TRUE |
| QA | s 48(1) | s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction | `sca-p4-civil-district.l4:926` | NOTHING when the appellant proves fraud, illegality or a fundamental breach of natural justice ("unless"); a twin `s 48(1) the bar on an appeal applies to the decision` answers JUST FALSE then | JUST TRUE |
| QA | s 49(1) | s 49(1) the appeal operates as a stay of execution or enforcement or of proceedings under the judgment or order appealed from | `sca-p4-civil-district.l4:979` | NOTHING once the District Court or the General Division of the High Court has ordered a stay ("unless ... so orders": the stay then rests on the order) | JUST TRUE |
| QA | s 49(2) | s 49(2) an intermediate act or proceeding is invalidated | `sca-p4-civil-district.l4:991` | NOTHING to the extent the General Division of the High Court has directed invalidation ("except so far as ... may direct") | JUST TRUE |
| QA | s 49A(2) | s 49A(2) the part of the proceeding where oral evidence is given may be conducted without an oral hearing | `sca-p4-civil-district.l4:1017` | NOTHING when all the parties consent ("unless all the parties consent"); a twin `s 49A(2) the bar on conducting the part of the proceeding without an oral hearing applies` answers JUST FALSE then | JUST TRUE |
| QA | s 54AA(1) | s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction | `sca-p4-magistrates-criminal.l4:303` | NOTHING when the appellant proves fraud, illegality or a fundamental breach of natural justice ("unless"); the twin answers JUST FALSE then | JUST TRUE |
| QA | s 54C(3) | s 54C(3) an order under subsection (2) may be made in respect of the proceedings | `sca-p4-transfers.l4:118` | NOTHING when the proceedings could have been commenced in the State Court ("may only be made in respect of ... proceedings as could have been commenced": a lifted bar grants nothing; subsection (2) is the grant) | JUST TRUE |
| QA | s 54D(3) | s 54D(3) an order under subsection (2) may be made in respect of the proceedings | `sca-p4-transfers.l4:177` | NOTHING when the proceedings could have been commenced in the Magistrate's Court | JUST TRUE |
| QA | not this question: s 33(2), s 42, s 54E(3), s 54F(3) | s 33(2) the remuneration of the assessors is costs in the proceedings; s 42 the judgment or order is final and conclusive between the parties; s 54E(3) and s 54F(3) enforcement on the judgment on the claim is stayed | `sca-p4-civil-district.l4:522`; `sca-p4-civil-district.l4:765`; `sca-p4-transfers.l4:245`; `sca-p4-transfers.l4:327` | each is a deeming or a stay lifted by "unless" or "except", so the requirement does not apply and the answer is JUST FALSE (the brief's own carve-out from QA) | NOTHING (a lifted bar grants nothing) |
| QB | s 49B(2) | s 49B(2) the District Judge has done what must be done before summarily dismissing the appeal as the section requires | `sca-p4-civil-district.l4:1109` | NOTHING when a step is not done (a bare "must give ... must consider"; the subsection does not say what follows) | JUST FALSE for the compliance question |
| QC | none in this Act | no function | no line | never arises: the only Schedule holds three oaths and no sentence asks whether something is "listed in" it | the two readings in the brief do not apply |
| QD | none in this Act | no function | no line | never arises: no duty with an "if" or "where" trigger is asked as a compliance question here (the duties of ss 15, 17 and 49B(2) have no trigger to be unmet, or are bare "must" under QB) | the three readings in the brief do not apply |
| QE | s 26(f) | s 26 this section gives a District Court jurisdiction to hear and try the proceeding | `sca-p4-civil-district.l4:351` | NOTHING for a limited liability partnership registered under the Limited Liability Partnerships Act 2005 ("other than" limits a grant of jurisdiction) | JUST FALSE (as "except") |
| QE | s 49A(1) | s 49A(1) a District Court may decide the matter in its civil jurisdiction without hearing oral arguments | `sca-p4-civil-district.l4:1004` | NOTHING for a matter prescribed by the Rules of Court ("other than" limits a grant) | JUST FALSE (as "except") |
| QA | s 62(2) | s 62(2) the Presiding Judge of the State Courts may exclude the person from the precincts of the State Courts | `sca-p5-administration.l4:136` | NOTHING when the person is a party to or a witness in proceedings ("except that when the person is a party to or a witness ... he or she is allowed to remain for such time as is necessary"); a twin `s 62(2) the person is allowed to remain ...` answers JUST TRUE then | JUST FALSE |
| QA | s 62(3) | s 62(3) the person's name may be included in the list of touts | `sca-p5-administration.l4:160` | NOTHING once the person has been heard or had an opportunity ("until"); JUST FALSE before | JUST TRUE after |
| QA | s 63(2) | s 63(2) the impounded document may be delivered out of the custody of the court or inspected | `sca-p5-administration.l4:244` | NOTHING on an order signed by a judicial officer ("except on an order") | JUST TRUE |
| QA | s 64(1)(a) | s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business | `sca-p5-administration.l4:276` | NOTHING with the Chief Justice's approval ("Except with the approval") | JUST TRUE |
| QA | s 64(1)(b) | s 64(1)(b) the judicial officer may accept the fees of office, perquisites, emoluments or advantages | `sca-p5-administration.l4:292` | NOTHING with the Chief Justice's approval | JUST TRUE |
| QA | s 65 | s 65 the judicial officer may investigate, try or commit for trial the proceedings | `sca-p5-administration.l4:353` | NOTHING with both the Chief Justice's approval and the parties' consent ("except with the approval ... and with the consent") | JUST TRUE |
| QA | s 68(2) | s 68(2) the officer is liable to be sued | `sca-p5-administration.l4:527` | NOTHING when the officer knowingly acted in excess of authority ("unless"); the twin `s 68(2) the bar on suing the officer applies` answers JUST FALSE then | JUST TRUE |
| QA | not this question: s 57(1) | s 57(1) the Registry of the State Courts is to be open on the day | `sca-p5-administration.l4:16` | a duty lifted by an exception ("except on Saturdays, Sundays and public holidays"): JUST FALSE on those days (the brief's own carve-out from QA) | NOTHING |
| QB | s 59 | s 59 the distribution of business in the State Courts has been made in accordance with the directions as the section requires | `sca-p5-administration.l4:80` | NOTHING when it does not accord (a bare "is to be made") | JUST FALSE for the compliance question |
| QB | s 62(6) | s 62(6) a copy of the list is kept hung up and the list has been published in the Gazette as the section requires | `sca-p5-administration.l4:195` | NOTHING when either is not done (bare "is to be kept" and "must be published") | JUST FALSE for the compliance question |
| QE | s 64(1)(b) | s 64(1)(b) the judicial officer may accept the fees of office, perquisites, emoluments or advantages | `sca-p5-administration.l4:292` | NOTHING for the judicial officer's salary and allowances ("other than" limits a prohibition) | JUST FALSE (as "except") |

## Marginal readings for a lawyer

Two readings are for a lawyer, not for the encoder.
The encoding takes them as the status quo.

- **(a) A failed "if" counts as the text's no, and flat negatives count as the text saying no.** "If A then B" does not itself say "if not A then not B"; the encoding answers `JUST FALSE` for B when A fails, within the provision that holds the "if", and records the branch with a comment `marginal reading (a)`. The other reading: the answer is `NOTHING` when A fails (the text grants B on A and is silent otherwise).
- **(b) A prohibition or grant limited by its own wording does not say no outside the limit.** The encoding answers `NOTHING` outside the limit and marks the branch `NOTHING-kind (limited by its own wording)`. The other reading: the limit implies a no outside it (`JUST FALSE`).

Branches resting on (a), by function (a branch of a ruled kind, such as a failed "where", is not listed here):

| file:line | function | branches resting on (a) |
| --- | --- | --- |
| `sca-p2-constitution.l4:158` | `s 6A(2) the judicial officer may lawfully sit on the day` | 1 |
| `sca-p2-constitution.l4:200` | `s 7(2) the State Court has power to hear the matter or part of it in private` | 1 |
| `sca-p2-constitution.l4:231` | `s 7(2AB) the State Court has power to hear the subsection (2AA) application otherwise than in private` | 1 |
| `sca-p2-constitution.l4:254` | `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` | 1 |
| `sca-p3-appointments.l4:86` | `s 9(3A) the person may be appointed to be or to act as a District Judge despite subsection (3)` | 1 |
| `sca-p3-appointments.l4:144` | `s 10(3) the person may be appointed to be or to act as a Magistrate despite subsection (2)` | 1 |
| `sca-p3-appointments.l4:310` | `s 16 the bailiff may break open an outer or inner door or window of the building or any receptacle in it` | 1 |
| `sca-p4-civil-district.l4:415` | `s 29(2) the General Division of the High Court may order that the proceedings be transferred to a District Court` | 1 |
| `sca-p4-civil-district.l4:693` | `s 39(4) the General Division of the High Court may make an order allowing the costs on the General Division scale or the State Courts scale as it directs` | 1 |
| `sca-p4-civil-district.l4:807` | `s 43(2) the District Court may suspend or stay the judgment or order` | 1 |
| `sca-p4-civil-district.l4:882` | `s 45(1) the interested party may prepare the instrument and tender it to a District Court for execution` | 1 |
| `sca-p4-civil-district.l4:1092` | `s 49B(1) the District Judge may on his or her own motion summarily dismiss the appeal` | 1 |
| `sca-p5-administration.l4:39` | `s 57(2) the registrar may lawfully sit or carry out the business of the Registry on the day` | 1 |
| `sca-p5-administration.l4:320` | `s 64(2)(a) the judicial officer may be appointed to the body or hold the office` | 1 |
| `sca-p5-administration.l4:336` | `s 64(2)(b) the judicial officer may receive the allowance or other honorarium` | 1 |
| `sca-p5-administration.l4:405` | `s 67(1) it is lawful for the District Judge to inquire into the matter in a summary manner` | 1 |
| `sca-p5-administration.l4:468` | `s 67(4) the officer is incapable of being an officer of the State Courts` | 1 |

Flat negatives answered `JUST FALSE` (the other half of (a): the quoted words of the branch's `FALSE-kind` comment contain "must not", "shall not", "cannot", "does not", "is not", "may not" or a like phrase), by function:

| file:line | function | flat negatives answered JUST FALSE |
| --- | --- | --- |
| `sca-p2-constitution.l4:421` | `s 8(2) subsection (1) affects the operation of the provision` | 3 |
| `sca-p2-constitution.l4:448` | `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` | 3 |
| `sca-p2-constitution.l4:491` | `s 8(4) the court is considered to have conducted the part of the hearing through a live audio link only` | 1 |
| `sca-p2-constitution.l4:505` | `s 8(5) the State Court may conduct the hearing in the manner provided under subsection (1)` | 1 |
| `sca-p3-appointments.l4:67` | `s 9(3) the person may be appointed to be or to act as a District Judge` | 1 |
| `sca-p3-appointments.l4:125` | `s 10(2) the person may be appointed to be or to act as a Magistrate` | 1 |
| `sca-p3-appointments.l4:172` | `s 12(2) the person may be appointed to be or to act as registrar` | 1 |
| `sca-p4-civil-district.l4:84` | `s 19(3) a District Court's jurisdiction under subsection (2) includes the action` | 1 |
| `sca-p4-civil-district.l4:115` | `s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value` | 1 |
| `sca-p4-civil-district.l4:185` | `s 22(1)(c) the claimant may recover the amount in the action` | 1 |
| `sca-p4-civil-district.l4:198` | `s 22(1)(d) the claimant may obtain the remedy or relief in the action` | 1 |
| `sca-p4-civil-district.l4:351` | `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` | 1 |
| `sca-p4-civil-district.l4:368` | `s 28 this section gives a District Court jurisdiction under the Distress Act 1934` | 1 |
| `sca-p4-civil-district.l4:394` | `s 29(1) this section gives a District Court jurisdiction to grant relief by way of interpleader` | 1 |
| `sca-p4-civil-district.l4:415` | `s 29(2) the General Division of the High Court may order that the proceedings be transferred to a District Court` | 1 |
| `sca-p4-civil-district.l4:577` | `s 35 a cause of action may be divided` | 1 |
| `sca-p4-civil-district.l4:633` | `s 39(1) the claimant is entitled to more costs than an action brought in a State Court with that limit would carry` | 1 |
| `sca-p4-civil-district.l4:704` | `s 39(5) section 39 applies to the proceedings` | 1 |
| `sca-p4-civil-district.l4:719` | `s 39(6) section 39 affects the question as to costs` | 1 |
| `sca-p4-civil-district.l4:926` | `s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction` | 1 |
| `sca-p4-civil-district.l4:979` | `s 49(1) the appeal operates as a stay of execution or enforcement or of proceedings under the judgment or order appealed from` | 1 |
| `sca-p4-civil-district.l4:991` | `s 49(2) an intermediate act or proceeding is invalidated` | 1 |
| `sca-p4-civil-district.l4:1017` | `s 49A(2) the part of the proceeding where oral evidence is given may be conducted without an oral hearing` | 1 |
| `sca-p4-civil-district.l4:1057` | `s 49A(4) a District Court may hear the matter in an asynchronous manner` | 1 |
| `sca-p4-civil-district.l4:1070` | `s 49A(5) section 49A affects the power of a District Court to hear oral arguments before deciding the matter` | 1 |
| `sca-p4-magistrates-criminal.l4:176` | `s 52(1A) a Magistrate's Court's jurisdiction under subsection (1) includes the action` | 1 |
| `sca-p4-magistrates-criminal.l4:303` | `s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction` | 1 |
| `sca-p5-administration.l4:160` | `s 62(3) the person's name may be included in the list of touts` | 1 |
| `sca-p5-administration.l4:244` | `s 63(2) the impounded document may be delivered out of the custody of the court or inspected` | 1 |
| `sca-p5-administration.l4:276` | `s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business` | 1 |
| `sca-p5-administration.l4:292` | `s 64(1)(b) the judicial officer may accept the fees of office, perquisites, emoluments or advantages` | 1 |
| `sca-p5-administration.l4:353` | `s 65 the judicial officer may investigate, try or commit for trial the proceedings` | 1 |
| `sca-p5-administration.l4:374` | `s 66 the officer may purchase or bid for the property` | 1 |
| `sca-p5-administration.l4:504` | `s 68(1) the judicial officer is liable to be sued for the act` | 1 |
| `sca-p5-administration.l4:554` | `s 68(3) the officer is deemed to have acted knowingly in excess of his or her authority` | 1 |

Branches resting on (b), by function (the count is the number of `limited by its own wording` comments in the function):

| file:line | function | branches resting on (b) |
| --- | --- | --- |
| `sca-p2-constitution.l4:35` | `s 3(1A) the court has the jurisdiction conferred by this Act and any other written law` | 1 |
| `sca-p2-constitution.l4:47` | `s 3(2) the court has the jurisdiction conferred by the Small Claims Tribunals Act 1984 and any other written law` | 1 |
| `sca-p2-constitution.l4:58` | `s 3(4) the court has the jurisdiction conferred by the Coroners Act 2010 and any other written law` | 1 |
| `sca-p2-constitution.l4:70` | `s 3(5) the court has the jurisdiction conferred by the Employment Claims Act 2016 and any other written law` | 1 |
| `sca-p2-constitution.l4:133` | `s 6A(1) the State Court is to sit on the day` | 1 |
| `sca-p2-constitution.l4:158` | `s 6A(2) the judicial officer may lawfully sit on the day` | 1 |
| `sca-p2-constitution.l4:186` | `s 7(1) the place is deemed an open and public court to which the public may have access` | 1 |
| `sca-p2-constitution.l4:212` | `s 7(2AA) the application is to be heard in private` | 1 |
| `sca-p2-constitution.l4:254` | `s 7(2A) the State Court may order the material to be removed or sufficiently redacted` | 1 |
| `sca-p2-constitution.l4:292` | `s 7(4) the person is guilty of an offence` | 1 |
| `sca-p2-constitution.l4:330` | `s 7(5) the individual may be present in the courtroom while the matter is heard in private` | 1 |
| `sca-p2-constitution.l4:406` | `s 8(1) the State Court may conduct the hearing through the means` | 2 |
| `sca-p2-constitution.l4:448` | `s 8(3) the State Court may conduct the part of the hearing through a live audio link only` | 1 |
| `sca-p2-constitution.l4:491` | `s 8(4) the court is considered to have conducted the part of the hearing through a live audio link only` | 1 |
| `sca-p2-constitution.l4:505` | `s 8(5) the State Court may conduct the hearing in the manner provided under subsection (1)` | 1 |
| `sca-p2-constitution.l4:520` | `s 8(6) the court is deemed to be sitting at a place appointed under section 6A(3)` | 1 |
| `sca-p3-appointments.l4:19` | `s 8A(2) the holder may sit in any State Court and act as a judge of it with all the jurisdiction, power and privileges of such a judge` | 1 |
| `sca-p3-appointments.l4:34` | `s 8A(3) the person may continue to sit in the General Division of the High Court, the Appellate Division of the High Court or the Court of Appeal` | 1 |
| `sca-p3-appointments.l4:53` | `s 8A(4) the person continues to sit as a judge of the State Court to give judgment or otherwise in the case` | 1 |
| `sca-p3-appointments.l4:67` | `s 9(3) the person may be appointed to be or to act as a District Judge` | 1 |
| `sca-p3-appointments.l4:102` | `s 9(4) the person is to sit as a District Judge for the purpose of giving judgment or otherwise in the case` | 1 |
| `sca-p3-appointments.l4:113` | `s 9(5) the person is ex officio a Magistrate` | 1 |
| `sca-p3-appointments.l4:125` | `s 10(2) the person may be appointed to be or to act as a Magistrate` | 1 |
| `sca-p3-appointments.l4:157` | `s 11(2) Justices of the Peace have and may exercise the power or perform the duty of a Magistrate` | 1 |
| `sca-p3-appointments.l4:172` | `s 12(2) the person may be appointed to be or to act as registrar` | 1 |
| `sca-p3-appointments.l4:186` | `s 12(3) the holder is ex officio a commissioner for oaths` | 1 |
| `sca-p3-appointments.l4:199` | `s 13 the holder may exercise the powers and duties conferred and imposed on the registrar` | 1 |
| `sca-p3-appointments.l4:222` | `s 15(1) the holder is to do the duty` | 1 |
| `sca-p3-appointments.l4:255` | `s 15(2) the registrar may engage the person` | 1 |
| `sca-p3-appointments.l4:271` | `s 15A(1) the registrar may authorise the person to exercise the powers and perform the duties of a bailiff` | 1 |
| `sca-p3-appointments.l4:284` | `s 15A(2) section 68(2) applies to the person as it applies to an officer of a State Court` | 1 |
| `sca-p3-appointments.l4:300` | `s 16 the bailiff may effect an entry into a building` | 1 |
| `sca-p3-appointments.l4:310` | `s 16 the bailiff may break open an outer or inner door or window of the building or any receptacle in it` | 1 |
| `sca-p3-appointments.l4:328` | `s 17(1) the officer is to take and subscribe the oath before exercising the functions of the office` | 1 |
| `sca-p3-appointments.l4:452` | `s 17(2A) the person may take and subscribe the oath by appearing through a live video link or live television link` | 1 |
| `sca-p4-civil-district.l4:20` | `s 19(1) the court is a court of record` | 1 |
| `sca-p4-civil-district.l4:40` | `s 19(2) a District Court has the jurisdiction of the General Division of the High Court to hear and try the action` | 1 |
| `sca-p4-civil-district.l4:115` | `s 19(4) a District Court's jurisdiction under subsection (2) includes the action despite its amount or value` | 1 |
| `sca-p4-civil-district.l4:131` | `s 19(6) a District Court has the jurisdiction vested in it by another written law` | 1 |
| `sca-p4-civil-district.l4:185` | `s 22(1)(c) the claimant may recover the amount in the action` | 1 |
| `sca-p4-civil-district.l4:198` | `s 22(1)(d) the claimant may obtain the remedy or relief in the action` | 1 |
| `sca-p4-civil-district.l4:241` | `s 19 a District Court has jurisdiction over the action` | 1 |
| `sca-p4-civil-district.l4:279` | `s 25 this section gives a District Court jurisdiction to hear and try the action for the recovery of immovable property` | 1 |
| `sca-p4-civil-district.l4:351` | `s 26 this section gives a District Court jurisdiction to hear and try the proceeding` | 1 |
| `sca-p4-civil-district.l4:437` | `s 31(1) the District Court has the power in the proceedings before it` | 1 |
| `sca-p4-civil-district.l4:447` | `s 31 the power is conferred if the action is within the jurisdiction` | 1 |
| `sca-p4-civil-district.l4:490` | `s 32 the District Judge has power to make the order or exercise the authority or jurisdiction` | 1 |
| `sca-p4-civil-district.l4:508` | `s 33(1) the District Judge may summon the persons to assist and act as assessors` | 1 |
| `sca-p4-civil-district.l4:550` | `s 33(4) a party may object to the person, personally or in respect of qualification` | 1 |
| `sca-p4-civil-district.l4:566` | `s 34 the registrar may exercise the jurisdiction and powers conferred on a District Court relating to civil proceedings` | 1 |
| `sca-p4-civil-district.l4:577` | `s 35 a cause of action may be divided` | 1 |
| `sca-p4-civil-district.l4:608` | `s 36(2) the General Division of the High Court may order the proceedings to be transferred to it` | 1 |
| `sca-p4-civil-district.l4:633` | `s 39(1) the claimant is entitled to more costs than an action brought in a State Court with that limit would carry` | 2 |
| `sca-p4-civil-district.l4:653` | `s 39(2) the claimant is treated as recovering the full amount recoverable without regard to the deduction` | 1 |
| `sca-p4-civil-district.l4:704` | `s 39(5) section 39 applies to the proceedings` | 1 |
| `sca-p4-civil-district.l4:719` | `s 39(6) section 39 affects the question as to costs` | 1 |
| `sca-p4-civil-district.l4:749` | `s 41(2) the order may make incidental provision for the transfer of the proceedings, including matters relating to procedure and costs` | 1 |
| `sca-p4-civil-district.l4:765` | `s 42 the judgment or order is final and conclusive between the parties` | 1 |
| `sca-p4-civil-district.l4:785` | `s 43(1) the District Court may order the money to be paid in one sum or by instalments` | 1 |
| `sca-p4-civil-district.l4:807` | `s 43(2) the District Court may suspend or stay the judgment or order` | 1 |
| `sca-p4-civil-district.l4:822` | `s 43(3) enforcement may issue` | 2 |
| `sca-p4-civil-district.l4:856` | `s 44 the judgment or order of a District Court may be enforced in the manner` | 1 |
| `sca-p4-civil-district.l4:893` | `s 45(1) the signature has the same effect as the execution, signing or indorsement by the party ordered to execute` | 1 |
| `sca-p4-civil-district.l4:905` | `s 45(2) section 45 abridges the powers of a District Court` | 1 |
| `sca-p4-civil-district.l4:926` | `s 48(1) an appeal can be brought against the decision of a District Court exercising civil jurisdiction` | 2 |
| `sca-p4-civil-district.l4:966` | `s 48(2) the references in subsection (1) to a decision are references to that part of the decision` | 1 |
| `sca-p4-civil-district.l4:979` | `s 49(1) the appeal operates as a stay of execution or enforcement or of proceedings under the judgment or order appealed from` | 1 |
| `sca-p4-civil-district.l4:991` | `s 49(2) an intermediate act or proceeding is invalidated` | 1 |
| `sca-p4-civil-district.l4:1004` | `s 49A(1) a District Court may decide the matter in its civil jurisdiction without hearing oral arguments` | 1 |
| `sca-p4-civil-district.l4:1017` | `s 49A(2) the part of the proceeding where oral evidence is given may be conducted without an oral hearing` | 2 |
| `sca-p4-civil-district.l4:1044` | `s 49A(3) a District Court may direct that the matter be heard in an asynchronous manner by exchange of written correspondence` | 2 |
| `sca-p4-civil-district.l4:1057` | `s 49A(4) a District Court may hear the matter in an asynchronous manner` | 1 |
| `sca-p4-civil-district.l4:1070` | `s 49A(5) section 49A affects the power of a District Court to hear oral arguments before deciding the matter` | 1 |
| `sca-p4-civil-district.l4:1092` | `s 49B(1) the District Judge may on his or her own motion summarily dismiss the appeal` | 1 |
| `sca-p4-magistrates-criminal.l4:21` | `s 50(1)(a) a District Court exercising criminal jurisdiction has the jurisdiction or power` | 1 |
| `sca-p4-magistrates-criminal.l4:37` | `s 50(1)(b) a District Court has the power to order the medical examination of the accused` | 1 |
| `sca-p4-magistrates-criminal.l4:74` | `s 51(1)(a) a Magistrate's Court exercising criminal jurisdiction has the jurisdiction or power` | 1 |
| `sca-p4-magistrates-criminal.l4:90` | `s 51(1)(b) a Magistrate's Court has the power to order the medical examination of the accused` | 1 |
| `sca-p4-magistrates-criminal.l4:134` | `s 52(1) a Magistrate's Court has the jurisdiction of the General Division of the High Court to hear and try the action` | 1 |
| `sca-p4-magistrates-criminal.l4:234` | `s 52(1B) the power is conferred if the proceedings are within the jurisdiction` | 1 |
| `sca-p4-magistrates-criminal.l4:247` | `s 52(2) a Magistrate's Court is subject to the limitation or provision in exercising its jurisdiction or powers` | 1 |
| `sca-p4-magistrates-criminal.l4:257` | `s 52 a Magistrate's Court has jurisdiction over the action` | 1 |
| `sca-p4-magistrates-criminal.l4:285` | `s 54 the judgment or order has the same effect and is enforced in the same manner as if given by a District Court` | 1 |
| `sca-p4-magistrates-criminal.l4:303` | `s 54AA(1) an appeal can be brought against the decision of a Magistrate's Court exercising civil jurisdiction` | 2 |
| `sca-p4-magistrates-criminal.l4:343` | `s 54AA(2) the references in subsection (1) to a decision are references to that part of the decision` | 1 |
| `sca-p4-transfers.l4:31` | `s 54A(2) the order may be made on such terms as the court sees fit` | 1 |
| `sca-p4-transfers.l4:61` | `s 54B(2) the order may be made on such terms as the court sees fit` | 1 |
| `sca-p4-transfers.l4:90` | `s 54C(1) a party may apply to the General Division of the High Court for an order that the proceedings be transferred to a State Court` | 1 |
| `sca-p4-transfers.l4:104` | `s 54C(2) the General Division of the High Court may order the proceedings to be transferred to a State Court` | 1 |
| `sca-p4-transfers.l4:118` | `s 54C(3) an order under subsection (2) may be made in respect of the proceedings` | 1 |
| `sca-p4-transfers.l4:150` | `s 54D(1) a party may apply to the District Court for an order that the proceedings be transferred to a Magistrate's Court` | 1 |
| `sca-p4-transfers.l4:164` | `s 54D(2) the District Court may order the proceedings to be transferred to a Magistrate's Court` | 1 |
| `sca-p4-transfers.l4:177` | `s 54D(3) an order under subsection (2) may be made in respect of the proceedings` | 1 |
| `sca-p4-transfers.l4:200` | `s 54E(1) a party may apply to the General Division of the High Court for a transfer of the proceedings or of the counterclaim` | 1 |
| `sca-p4-transfers.l4:224` | `s 54E(2) the General Division of the High Court may make the order` | 1 |
| `sca-p4-transfers.l4:282` | `s 54F(1) a party may apply to the District Court for a transfer of the proceedings or of the counterclaim` | 1 |
| `sca-p4-transfers.l4:307` | `s 54F(2) the District Court may make the order` | 1 |
| `sca-p4-transfers.l4:394` | `s 54G(2)(a) the costs of the part of the proceedings before the transfer are subject to section 39` | 1 |
| `sca-p4-transfers.l4:413` | `s 54G(2)(b) the State Court may exercise the powers of the General Division of the High Court under section 39(4)` | 1 |
| `sca-p5-administration.l4:39` | `s 57(2) the registrar may lawfully sit or carry out the business of the Registry on the day` | 1 |
| `sca-p5-administration.l4:66` | `s 58 both civil and criminal proceedings may be tried at the sitting of the court` | 1 |
| `sca-p5-administration.l4:93` | `s 61 the Chief Justice may authorise the vacations` | 1 |
| `sca-p5-administration.l4:112` | `s 62(1) the Presiding Judge of the State Courts may frame, publish, alter and amend the list of touts` | 1 |
| `sca-p5-administration.l4:121` | `s 62(1)(a) the person may be named in the list of touts` | 1 |
| `sca-p5-administration.l4:136` | `s 62(2) the Presiding Judge of the State Courts may exclude the person from the precincts of the State Courts` | 2 |
| `sca-p5-administration.l4:148` | `s 62(2) the person is allowed to remain in the precincts of the State Courts for such time as is necessary` | 1 |
| `sca-p5-administration.l4:160` | `s 62(3) the person's name may be included in the list of touts` | 1 |
| `sca-p5-administration.l4:173` | `s 62(4) an appeal lies to a Judge sitting in chambers in the General Division of the High Court` | 1 |
| `sca-p5-administration.l4:183` | `s 62(5) the decision of the Judge is final` | 1 |
| `sca-p5-administration.l4:208` | `s 62(7) the person is deemed to be included in the list under this section` | 1 |
| `sca-p5-administration.l4:217` | `s 62(7) the person is deemed to be included in the list under section 73 of the Supreme Court of Judicature Act 1969 or section 39 of the Family Justice Act 2014` | 1 |
| `sca-p5-administration.l4:231` | `s 63(1) a State Court may order the document to be impounded` | 1 |
| `sca-p5-administration.l4:244` | `s 63(2) the impounded document may be delivered out of the custody of the court or inspected` | 2 |
| `sca-p5-administration.l4:259` | `s 63(3) the court may direct the document to be sent to the Attorney-General, the Commissioner of Stamp Duties or any other officer of the Government` | 1 |
| `sca-p5-administration.l4:276` | `s 64(1)(a) the judicial officer is capable of accepting or taking another office of emolument or carrying on a business` | 1 |
| `sca-p5-administration.l4:292` | `s 64(1)(b) the judicial officer may accept the fees of office, perquisites, emoluments or advantages` | 2 |
| `sca-p5-administration.l4:320` | `s 64(2)(a) the judicial officer may be appointed to the body or hold the office` | 1 |
| `sca-p5-administration.l4:336` | `s 64(2)(b) the judicial officer may receive the allowance or other honorarium` | 1 |
| `sca-p5-administration.l4:353` | `s 65 the judicial officer may investigate, try or commit for trial the proceedings` | 2 |
| `sca-p5-administration.l4:374` | `s 66 the officer may purchase or bid for the property` | 1 |
| `sca-p5-administration.l4:405` | `s 67(1) it is lawful for the District Judge to inquire into the matter in a summary manner` | 1 |
| `sca-p5-administration.l4:419` | `s 67(2) the District Judge may summon and enforce the attendance of all necessary parties` | 1 |
| `sca-p5-administration.l4:435` | `s 67(3) the District Judge may order repayment of the money extorted or payment of the money levied, damages and costs` | 2 |
| `sca-p5-administration.l4:448` | `s 67(3) the District Judge may impose the fine upon the officer` | 2 |
| `sca-p5-administration.l4:479` | `s 67(5) an appeal lies to the Chief Justice` | 1 |
| `sca-p5-administration.l4:489` | `s 67(6) the decision of the Chief Justice is final` | 1 |
| `sca-p5-administration.l4:504` | `s 68(1) the judicial officer is liable to be sued for the act` | 1 |
| `sca-p5-administration.l4:527` | `s 68(2) the officer is liable to be sued` | 2 |
| `sca-p5-administration.l4:554` | `s 68(3) the officer is deemed to have acted knowingly in excess of his or her authority` | 1 |
| `sca-p5-administration.l4:574` | `s 68(4) the person is liable to be sued for the act` | 1 |
| `sca-p6-supplemental.l4:36` | `s 70(1) the Court may order the pending action or application to be converted and continued by way of a writ of summons or an originating summons` | 1 |
| `sca-p6-supplemental.l4:56` | `s 70(2) the Presiding Judge of the State Courts may by order direct that a class or description of pending actions or applications be converted` | 1 |
| `sca-p6-supplemental.l4:97` | `s 70(3)(b) the Court may give the parties directions as to the conduct and costs of the action or application` | 1 |

Beyond the two, the following branches rest on a fork in the register and not on a ruling: F-S17-2A, F-S25-B, F-S25-C, F-S29-AND, F-S39-LIMIT, F-S52-2, F-S64-APPROVAL, F-S57-VACATION, F-S19-28A, F-PASSIVE.

## Dependencies

None copied.
The Interpretation Act modules staged in `inputs/DEPENDENCIES/` (`sgia-interpretation-time.l4`, `sgia-p1-definitions.l4`) are unused: no period in this Act is counted from an event (the only durations are ceilings, "not exceeding 15 days in any calendar year" in s 61 and "12 months" in s 7(4), and a count of complete years of qualification in ss 9 to 12, taken as an input, fork F-QUALYEARS), and a time "as may be prescribed by Rules of Court" (ss 54E(1), 54F(1)) is an input.
The Interpretation Act's s 2(1) meaning of "year" could stand behind F-QUALYEARS; it is not used because the years are stated by the person.
"Public holiday", "written law" and "Gazette" are borrowed terms asked as facts (a `Kind of day`, a yes/no, a yes/no); the Coroners Act 2010, the Broadcasting Act 1994 and the Newspaper and Printing Presses Act 1974 definitions are passed through as borrowed facts (fork F-BORROWED).

## Seams

Three things the Act hands to something outside the sources are **plain inputs, with no import**; every `IMPORT` in the deposit is `prelude` or one of the `sca-` modules.

- **The Supreme Court of Judicature Act 1969, section 28A** (and an order under its subsection (1)): s 19(3) is "Subject to" it. Layer 1 takes a yes/no field of the civil action record, "section 28A ... affects the action"; the seat asks it as a `My answer` (yes, no, I am not sure). The right of appeal itself, which s 47 leaves "Subject to" that Act, is not modelled (fork F-S19-28A).
- **The Rules of Court**: the time within which a counterclaim may be taken up in ss 54E(1) and 54F(1) is a yes/no input ("the application is made within the time prescribed by Rules of Court"); s 36(1) has the same shape for the manner of an application ("the application is made in the manner prescribed by Rules of Court"). Rules of Court are not among the sources.
- **Orders under s 30 and s 52(3)**: the District Court limit and the Magistrate's Court limit are numbers the rules take as inputs, with the Act's $250,000 and $60,000 as the figures when there is no order; the seat passes "no order" (fork F-LIMIT).

Any other row that encodes those instruments could replace these inputs; nothing here is waiting on it.

## What the text does not answer

Two kinds of line: provisions whose text does answer but which are machinery, so no function asks them (inert, reason 2; the coverage table has the line range), and things the text leaves out or sends elsewhere (answered `NOTHING` where a question reaches them).
Line numbers are those of `SCA1970.txt`.

| item | provision (line) | what the text says or leaves out | what the encoding does |
| --- | --- | --- | --- |
| The short title | s 1 (193) | "This Act is the State Courts Act 1970." | inert, reason 2: no question to ask |
| Who may be the Presiding Judge of the State Courts, and who appoints | s 8A(1) (573-577) | the President, on the Chief Justice's recommendation, may appoint "a Supreme Court Judge or a Judicial Commissioner" for "such period as the Chief Justice may recommend"; it says nothing about a District Judge being eligible | inert, reason 2 (an office and its staffing): no function answers "who may be Presiding Judge"; a lawyer who wants it asked can have it encoded, and a District Judge would then be outside the two named classes |
| Who appoints District Judges, Magistrates, Justices of the Peace, the registrar | ss 9(1) (610-614), 10(1) (652-655), 11(1) (678-679), 12(1) (688-692) | the President on the Chief Justice's recommendation (District Judges, "Subject to section 8A"; Magistrates, "any fit and proper person"); the President by warrant (Justices of the Peace, "fit and proper persons"); the Chief Justice (a registrar and deputy registrars) | inert, reason 2: the qualification rules that restrict these appointments are encoded (ss 9(3), 9(3A), 10(2), 10(3), 12(2)) |
| Which officers are attached to the courts | s 14 (713-719) | "such commissioners for oaths, interpreters, clerks, bailiffs, process servers and other officers as may appear to the Chief Justice to be necessary" | inert, reason 2: the number and kinds are left to the Chief Justice's view |
| Gazetting of appointments | s 18 (851-852) | "All appointments and revocations made under this Part must be published in the Gazette", with no consequence stated for failing to | inert, reason 2 |
| Who may vary the two limits, and the order | ss 30 (1114-1116), 52(3) (1670-1671) | the President, after consulting the Chief Justice, "by order" | inert, reason 2: a limit is a number input and an order under either section is the "no order" input; the amounts of an order, and when it takes effect, are not in the text |
| Who apportions the work among an office's officers | s 60(2) (1998-2003) | the Presiding Judge of the State Courts, subject to the Chief Justice's directions | inert, reason 2 (an office and its staffing) |
| Rule-making and the interest cap | s 69 (2228-2370; the cap is at 2263-2267) | the Rules Committee's power to make Rules of Court; (3)(d) allows rules "directing interest to be paid on debts, including judgment debts", where the rate "must not in any case exceed 8% per annum unless it has been otherwise agreed between parties". 8% is the only interest figure in the Act; I found no 9% | inert, reason 2 (a rule-making power): the 8% is a limit on rules and not a duty or right of a person; a lawyer may want it encoded as a rule of the cap |
| A limitation period | none | the Act states none; the word "limitations" occurs only in s 52(2) ("the same limitations and provisions") | silent |
| Court fees | none | no fee schedule; "fees" occurs only in s 64(1)(b) (officers not to accept "fees of office") and s 67 (an officer extorting a fee) | silent |
| The Small Claims Tribunals' limit | s 3(2) (260-261) | "The Small Claims Tribunals have the jurisdiction conferred by the Small Claims Tribunals Act 1984 and any other written law" | a pointer to another Act: s 3(1)'s list of courts is encoded, the Tribunals' limit is not in this Act |
| Time to appeal from a District Court | s 47 (1393-1401) | "Subject to" the Supreme Court of Judicature Act 1969, "Rules of Court are to regulate and prescribe the procedure on appeals"; no time is stated | inert, reason 2; the only appeal functions are the final-decision bars (ss 48, 54AA) and the stay (s 49) |
| A District Judge's salary | none | s 64(1)(b) mentions "the judicial officer's salary" only as what an officer may accept; no amount | silent |
| What follows when a bare "must" is not done | ss 5, 6, 17(1), 17(3), 17(4), 49B(2), 59, 62(6) | the text states the requirement and no consequence | the "... as the section requires" functions answer `NOTHING` (QB) |
| Rules of Court content | ss 6, 36(1), 54E(1), 54F(1) and elsewhere | service, prescribed times and prescribed matters are in the Rules | yes/no inputs; `NOTHING` when not met |
| Section 28A of the Supreme Court of Judicature Act, and the powers conferred by the Criminal Procedure Code 2010 | s 19(3) (885); ss 50(1) (1514) and 51(1) (1545); s 8(2) (516) | s 19(3) is "Subject to section 28A"; the criminal courts have "the jurisdiction and powers conferred on [them] by the Criminal Procedure Code 2010 and any other written law"; s 8(2) refers to section 281 of that Code | inputs or `NOTHING` (fork F-S19-28A); the Code's content is not among the sources |
| Whether ss 22 and 23 reach a Magistrate's Court | s 52(2) | the same "limitations and provisions" as for a District Court, with no word on ss 22 and 23 | `NOTHING` (fork F-S52-2) |
| Any remedy for dividing a cause of action | s 35 | forbids it without naming who bears the prohibition | `JUST FALSE` for the purpose, no `SHANT` (fork F-PASSIVE) |
| An officer's liability outside the s 68 conditions | s 68 | the immunities are conditional; outside the condition the text does not say the officer is liable | `NOTHING` |
| A court outside the five named in s 3(1) | s 3(1) | the list is not closed | `NOTHING` (fork F-S3-LIST) |

## Unstable dialect

I looked at time (no provision applies differently on different dates and no period runs from an event), versions (the file is one consolidation and the monetary limits that an order may vary are inputs, not dated versions) and workarounds on main (listed under "What the main binary does not accept") in the whole text and found no shape that earns a second, unstable encoding.

## What the text turns out to say

1. **The two monetary limits are the Act's own words, and a limit is exceeded only by more than the figure.** Section 2 defines the District Court limit as "$250,000 or any other amount specified by an order under section 30" and the Magistrate's Court limit as "$60,000 or any other amount specified by an order under section 52(3)". The encoding takes the order's amount as an optional input (fork F-LIMIT). A claim of exactly $250,000 is within the District Court limit and $250,001 is over it. Cases: `sca-tests-p1.l4:33`; `sca-tests-p4a.l4:51`; `sca-tests-p4a.l4:52`. Asserted.

2. **The amount claimed and the value of the relief are tested separately, and either can put a case over the limit.** Section 19(4)(a) asks about "the amount claimed" and (b) about the value of the subject matter of "any remedy or relief sought ... in addition or as an alternative". A claim for $1,000 with relief worth $400,000 is over the District Court limit. Cases: `sca-cases-seat.l4:20`. Asserted.

3. **Over the District Court limit a District Court has no jurisdiction under section 19(2), unless the claimant gives up the excess (section 22) or the parties sign an agreement (section 23).** Section 19(4) is "Subject to sections 22 and 23". Read by itself, section 19(4) answers `NOTHING` once either has happened (a lifted bar grants nothing, QA); the hand-gathered `s 19 a District Court has jurisdiction over the action` answers `JUST TRUE` for both (fork F-COMBINE). Cases: `sca-tests-p4a.l4:85`; `sca-tests-p4a.l4:86`; `sca-tests-p4a.l4:56`. Asserted.

4. **A claimant who gives up the excess cannot recover more than the limit, but the Act says nothing about recovering exactly the limit or less.** Section 22(1)(c) and (d) say what the claimant "cannot" do; recovering up to the limit is not mentioned (`NOTHING`). The judgment is "a full discharge of all demands in respect of the cause of action" (section 22(2)), but only where the District Court has jurisdiction "by virtue of this section". Cases: `sca-tests-p4a.l4:69`; `sca-tests-p4a.l4:70`; `sca-tests-p4a.l4:75`. Asserted.

5. **Sections 22 and 23 name only "a District Court"; the Magistrate's Court has no counterpart in its own section.** Section 52(2) subjects a Magistrate's Court to "the same limitations and provisions as are applicable to a District Court under this Act" without saying whether sections 22 and 23 are among them, so an over-limit Magistrate's Court case where the excess is given up or the parties agree is `NOTHING` (fork F-S52-2). Cases: `sca-tests-p4b.l4:89`; `sca-cases-seat.l4:76`. Asserted.

6. **A Magistrate's Court cannot hear an action with no claim for a sum of money (section 52(1A)(a)); section 19 has no such limit for a District Court.** Section 52(1A) lists four classes the Magistrate's Court's jurisdiction "does not include": no claim for a sum of money, passing off, an amount claimed over the limit, relief over the limit. Section 19(3) and (4) list the District Court's exclusions, and a claim for no sum of money is not among them. Cases: `sca-tests-p4b.l4:62`; `sca-cases-seat.l4:78`. Asserted.

7. **Passing off is outside both courts.** Section 19(3)(ca) excludes it from a District Court's jurisdiction and section 52(1A)(aa) from a Magistrate's Court's; both paragraphs carry the amendment mark "Act 23 of 2019 wef 01/04/2022". Cases: `sca-tests-p4a.l4:42`; `sca-cases-seat.l4:80`. Asserted.

8. **Section 19(3) is "Subject to section 28A of the Supreme Court of Judicature Act 1969 and any order under subsection (1) thereof", and neither is among the sources.** Where that section or an order affects a case in an excluded class, the encoding answers `NOTHING` and not `JUST FALSE` (fork F-S19-28A). Cases: `sca-tests-p4a.l4:89`; `sca-cases-seat.l4:66`. Asserted.

9. **The recovery-of-property test (section 25) takes one-twelfth of the limit for the monthly rent, and uses the last transacted price only when the annual value, annual rent and monthly rent all cannot be ascertained; either the annual-rent test or the monthly-rent test is enough.** (forks F-S25-B and F-S25-C) One-twelfth of $250,000 is $20,833.33, so a monthly rent of $20,833 is within and $20,834 is over; the price test is ten times the limit, $2,500,000. Cases: `sca-tests-p4a.l4:109`; `sca-tests-p4a.l4:110`; `sca-tests-p4a.l4:105`; `sca-cases-seat.l4:115`; `sca-cases-seat.l4:116`; `sca-cases-seat.l4:118`. Asserted.

10. **A limited liability partnership registered under the Limited Liability Partnerships Act 2005 is taken out of the dissolution and winding-up grant of section 26(f), and the Act does not say it cannot be heard elsewhere.** "(other than a limited liability partnership ...)" limits a grant, so the answer is `NOTHING` (QE), not `JUST FALSE`. Cases: `sca-tests-p4a.l4:119`; `sca-cases-seat.l4:125`. Asserted.

11. **Section 29(1) gives a District Court interpleader jurisdiction on either of two grounds, and only the second carries the District Court limit.** (a) is a bailiff executing a writ or order of the Court against a claimant who is not the person it was issued against; (b) is a person under liability for a debt or movable property, within the limit, who has been or expects to be sued by 2 or more adverse claimants. Each head is its own ground: (a) alone is `JUST TRUE` whatever the amount, (b) alone is `JUST TRUE` at or below the limit and `JUST FALSE` above it, and neither is `JUST FALSE` (fork F-S29-AND; assumed, not ruled). Cases: `sca-tests-p4a.l4:128`; `sca-tests-p4a.l4:130`; `sca-tests-p4a.l4:132`; `sca-tests-p4a.l4:133`; `sca-tests-p4a.l4:134`; `sca-cases-seat.l4:134`; `sca-cases-seat.l4:137`. Asserted.

12. **A video-link oath that fails any of the three things the technology must allow (visual contact and communication, confirming identity, verifying the oath by inspection) is not covered, and the Act does not say it is invalid.** Section 17(2A) opens "To avoid doubt" and confirms a power; it has no "if" and no "only" (fork F-S17-2A). Cases: `sca-tests-p3.l4:104`; `sca-tests-p3.l4:102`. Asserted.

13. **Section 35 forbids dividing a cause of action to bring two or more actions, and names no bearer.** The decision function answers `JUST FALSE` when the purpose is to bring two or more actions and `NOTHING` for any other purpose; no `SHANT` rule is written because that would invent an actor (fork F-PASSIVE). Cases: `sca-tests-p4a.l4:173`; `sca-cases-seat.l4:166`. Asserted.

14. **Section 39(1)(a) and (b) are asked one limit at a time, and the Act does not say how they combine.** A recovery of $50,000 is within both limits and answers `JUST FALSE` against $250,000 and against $60,000; a recovery of $100,000 answers `JUST FALSE` against $250,000 and `NOTHING` against $60,000. The caller who wants the tighter cap asks against the Magistrate's Court limit (fork F-S39-LIMIT). Cases: `sca-tests-p4a.l4:192`; `sca-tests-p4a.l4:193`; `sca-tests-p4a.l4:194`; `sca-tests-p4a.l4:195`. Asserted.

15. **A claimant who sues in the High Court for a sum that a State Court could have heard gets no more costs than the State Court scale would give, if the sum recovered is within the State Court limit (section 39(1)); proceedings by the Government are outside section 39 (section 39(5)).** Recovering more than the limit is not decided by this subsection. Cases: `sca-tests-p4a.l4:185`; `sca-tests-p4a.l4:187`; `sca-tests-p4a.l4:204`. Asserted.

16. **Where payment by instalments is ordered, no enforcement may issue without the District Court's permission (section 43(3)); with permission the bar is lifted and the grant to enforce is section 44.** The permission question answers `NOTHING` and a twin, `s 43(3) the bar on enforcement applies`, answers `JUST FALSE`. Cases: `sca-tests-p4a.l4:227`; `sca-tests-p4a.l4:228`; `sca-tests-p4a.l4:231`. Asserted.

17. **An agreement in writing that a decision is final bars an appeal unless the appellant proves fraud, illegality or a fundamental breach of natural justice (sections 48(1) and 54AA(1)); an appeal does not stay enforcement unless the court so orders (section 49(1)).** Without the agreement the section is silent on appeals (`NOTHING`); the right of appeal itself is in the Supreme Court of Judicature Act 1969, which is not among the sources. Cases: `sca-tests-p4a.l4:250`; `sca-tests-p4a.l4:251`; `sca-tests-p4b.l4:106`; `sca-tests-p4a.l4:263`. Asserted.

18. **A part of a proceeding where oral evidence is given cannot be conducted without an oral hearing unless all the parties consent (section 49A(2)), and a District Court must not hear a matter asynchronously if that would be unfair (section 49A(4)).** Cases: `sca-tests-p4a.l4:269`; `sca-tests-p4a.l4:277`. Asserted.

19. **A transfer between courts is bounded in both directions by what the lower court could have heard (sections 54C(3) and 54D(3)), and a counterclaim beyond the lower court's limit may be taken up only within the time Rules of Court prescribe (sections 54E(1) and 54F(1)).** The time is not among the sources, so a late application is `NOTHING`. Cases: `sca-tests-p4b.l4:138`; `sca-tests-p4b.l4:153`; `sca-tests-p4b.l4:171`. Asserted.

20. **A person named in the list of touts who is a party to or a witness in proceedings is allowed to remain in the precincts of the State Courts "for such time as is necessary" (section 62(2)).** The Presiding Judge's power to exclude is lifted for that person and a lifted power grants nothing (QA); a name may not be included before the person has been heard (section 62(3)). Cases: `sca-tests-p5.l4:46`; `sca-tests-p5.l4:48`; `sca-tests-p5.l4:51`. Asserted.

21. **The immunities in section 68 are conditional, and where the condition fails the section does not say that the officer is liable.** A judicial officer is not liable to be sued for an act in the discharge of judicial duty "provided that" the officer in good faith believed there was jurisdiction; an officer executing process is protected "unless the officer knowingly acted in excess of the authority"; a mediation immunity is "if the act" was in good faith and involved no fraud or wilful misconduct. Outside each condition the answer is `NOTHING`. Cases: `sca-tests-p5.l4:127`; `sca-tests-p5.l4:128`; `sca-tests-p5.l4:132`; `sca-tests-p5.l4:143`. Asserted.

22. **The Registry is to be open every day except Saturdays, Sundays and public holidays; a day in a vacation authorised under section 61 is not excepted** (fork F-S57-VACATION). By contrast section 6A(1) leaves a vacation day to section 6A(2) and answers `NOTHING` for it (fork F-VACATION). Cases: `sca-tests-p5.l4:14`; `sca-tests-p2.l4:44`. Asserted.

23. **The list of State Courts in section 3(1) is not closed.** Five courts are named; a court outside them is `NOTHING`, not `JUST FALSE` (fork F-S3-LIST). Cases: `sca-cases-seat.l4:16`. Asserted.

24. **The offence in section 7(4) carries a fine of up to $5,000 or imprisonment of up to 12 months or both; the ceiling is tested on both sides.** Cases: `sca-tests-p2.l4:86`; `sca-tests-p2.l4:88`; `sca-tests-p2.l4:89`. Asserted.

25. **Section 70 lets a Court convert a pending petition into a writ of summons or originating summons after the commencing law is amended, and the Presiding Judge, with the Chief Justice's concurrence, may direct conversion of a class.** The encoding treats it as operative and not as a saving provision (fork F-S70-SAVINGS). Cases: `sca-tests-p5.l4:151`; `sca-tests-p5.l4:156`. Asserted.

26. **When the seat's user is "not sure" whether a written law gives the case to another court, or whether section 28A applies, the seat answers `NOTHING` even if another stated fact (passing off, for example) would settle the case on its own.** The module rules, called directly, do answer on those facts. This is a limit of the seat layer, not a reading of the text. Cases: `sca-cases-seat.l4:70`. Asserted.

27. **Several sentences say what "is to" or "must" be done and not what follows when it is not (sections 5, 6, 17, 49B(2), 59 and 62(6)).** The compliance functions, named "... as the section requires", answer `NOTHING` when the thing is not done (QB), and the duties are written as regulative rules with no time limit and no consequence, because the text states none. Cases: `sca-tests-p5.l4:31`; `sca-tests-p5.l4:58`; `sca-tests-p4a.l4:286`. Asserted.

28. **The Arrangement of Sections in the source text is garbled by the converter: its headings are misaligned with their section numbers, so the body numbering governs.** Nothing is encoded from the Arrangement. Not asserted: a property of the source file.

29. **The Legislative History and Abbreviations at the end of the text say of themselves that they are "not part of the Act"**, so they are inert (reason 1). Not asserted.

## What the main binary does not accept

The binary governs where the skills describe a construct it rejects.
Measured on `l4` 1.6.109 (main) and read the same way by 1.6.108 (the `check.sh` main column is `same` for every module):

1. **A regulative value cannot be compared in `#ASSERT`.** `#ASSERT <rule> EQUALS FULFILLED` fails with `eval/unsupported-equality` ("Trying to check equality on types that do not support it"). The regulative rules (ss 6, 7(4), 8(3), 15(1)(a) to (c), 17(1), 49B(2), 64(1)(b), 65, 66) are run with `#TRACE` (11 traces, read by eye: a party's act produces `FULFILLED` for a `MUST` and `DEONTIC BREACHED` for a `SHANT`), and the same duties are asserted as decision functions over the facts.
2. **`NOT (a) OR b AT MOST c` is read as `NOT ((a) OR (b AT MOST c))`.** Probe: `f TRUE 5 5` returned `FALSE` for `NOT (a) OR v AT MOST l` and `TRUE` for `(NOT (a)) OR (v AT MOST l)`. This is the brief's rule "parenthesise every `NOT`", carried one step further: wrap the whole `NOT (...)` as well. The modules write `(NOT (a)) OR (b AT MOST c)`; four sites were first written the other way (s 52(1A) twice, s 54E(1), s 54F(1)) and the tests of the last two failed until they were rewritten.
3. **`JUST (` followed by a parenthesised application that runs over more than one line is a parse error** (`parse/unexpected-open-paren` at the opening bracket). Probe: `JUST (big x)` on one line evaluates (`JUST OF TRUE`); the same call split across two lines after `JUST (` fails. The seat wraps a plain `BOOLEAN` with a one-line function, `the module's yes or no`, instead, so no multi-line argument follows `JUST (`.
4. **A record type with a multi-word name needs backticks before `OF`** (`` `Civil action` OF ... ``); without them the parse error is `parse/unexpected-OF`.
5. Not tried because the brief lists them as unavailable on main: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section `GIVEN`, sets, `TYPICALLY`, `YMD`, `EVERY`, `@lang`, `@infix`. The encoding uses none of them.

## What check.sh printed

`L4=<l4-main-109> L4_MAIN=<l4-main-108> ./check.sh`, run in the encoding folder.
The baseline numbers it replaced: none (the folder held no module before).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sca-cases-seat.l4                              0       181       0        0         0 |      0       181       0        0  same
sca-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
sca-p1-preliminary.l4                          0         0       0        0         0 |      0         0       0        0  same
sca-p2-constitution.l4                         0         0       0        0         0 |      0         0       0        0  same
sca-p3-appointments.l4                         0         0       0        0         0 |      0         0       0        0  same
sca-p4-civil-district.l4                       0         0       0        0         0 |      0         0       0        0  same
sca-p4-magistrates-criminal.l4                 0         0       0        0         0 |      0         0       0        0  same
sca-p4-transfers.l4                            0         0       0        0         0 |      0         0       0        0  same
sca-p5-administration.l4                       0         0       0        0         0 |      0         0       0        0  same
sca-p6-supplemental.l4                         0         0       0        0         0 |      0         0       0        0  same
sca-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sca-tests-p1.l4                                0        38       0        0         0 |      0        38       0        0  same
sca-tests-p2.l4                                0       108       0        0         0 |      0       108       0        0  same
sca-tests-p3.l4                                0        83       0        0         0 |      0        83       0        0  same
sca-tests-p4a.l4                               0       220       0        0         0 |      0       220       0        0  same
sca-tests-p4b.l4                               0       152       0        0         0 |      0       152       0        0  same
sca-tests-p5.l4                                0       124       0        0         0 |      0       124       0        0  same
TOTAL (17 modules)                             0       906       0        0           |      0       906       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Assertions written equal assertions satisfied in every case file (38, 108, 83, 220, 152, 124 and 181 = 906); no assertion failed or was refused; `l4 check` printed no error and no warning for any of the 17 modules; `python3 -I srcrefs.py check --refs SCA1970.txt sca-*.l4` reported 0 problems.
No test is meant to fail, so `check.sh` has no `expected_failed`.

## What would need doing before relying on it

1. A Singapore litigator reads each module against the **official** text on Singapore Statutes Online. This encoding follows a converter's rendering of an unofficial consolidation, and the file's banner ("version in force from 1/12/2023") and its metadata ("Current version as at 01 Oct 2026") should be reconciled against the current version.
2. The lawyer rules on the two marginal readings (above) and on each fork in the register, in particular F-S52-2 (whether ss 22 and 23 reach a Magistrate's Court), F-S29-AND (whether the two heads of s 29(1) are separate grounds or cumulative), F-COMBINE (the two hand-gathered jurisdiction functions), F-PASSIVE (no `SHANT` rule where no bearer is named), F-S25-C (whether one unknown figure or all three trigger the price test) and F-S17-2A (a video-link oath that fails one of the three requirements).
3. The things the Act sends elsewhere are not encoded: Rules of Court (service, time limits, the prescribed manner of objections), orders under s 30 and s 52(3), the Criminal Procedure Code 2010, the Supreme Court of Judicature Act 1969 (including section 28A). A user's answer is only as good as the figures and facts they state.
4. If an order has varied either limit, the seat answers for the old figure; the fix is to give the seat a number for the order, which the layer-1 rules already take.
5. The seat answers `NOTHING` whenever the user says "I am not sure" about a legal conclusion that the rule reads, even where another stated fact would settle the case; a finer seat would run the rule under each reading and answer only where they agree.
6. Re-run `check.sh` on a later main build; it does not see a different `#TRACE` outcome, only assertion counts.

## Note on the source text

The Arrangement of Sections is garbled by the converter (its headings are misaligned with their section numbers), so the body numbering governs.
A separate part of the file, the Legislative History, is "not part of the Act" and is inert.

